"""Etapa MOVEMENTO (Gauntlet 4): que ningún plano quede fixo.

Cada plano da lista (contexto do Gauntlet 4, §6.1) pode levar un campo `animacion`:

    {"modo": "paralaxe" | "i2v" | "fixo", "camara": "avanza" | "recua" | "xira_esq" | "xira_der" | "sobe" |
     "baixa" | "pan_esq" | "pan_der", "efectos": ["lume", "candea", "choiva", "bretema", "fume", "auga", "ceo",
     "po"], "accion": "texto en inglés para o modelo I2V", "forza": 1.0}

- `paralaxe`: cámara 2,5D sobre a imaxe fixa. A profundidade sae de Depth-Anything-V2-Small (Apache-2.0; as
  versións Base e Large son CC BY-NC e non se usan). Cada fotograma proxecta a imaxe coa profundidade (z-buffer a
  media resolución), enche os ocos que destapa a cámara co fondo máis próximo e mostrea outra vez a imaxe a
  resolución completa (cv2.remap); onde aparece fondo que estaba tapado mostrea unha copia da imaxe co primeiro
  termo "borrado" (inpaint de OpenCV na beira de cada salto de profundidade).
- `i2v`: clip xerado a partir da imaxe (LTX-Video 2B 0.9.8 destilado; ver `plan-de-negocio/gauntlet4/movemento/`).
  Corre noutro venv (`$SCRATCH/video/venv`) e noutro proceso; aquí só se le o clip da caché e se encaixa no plano
  (cámara lenta interpolada se o plano é máis longo ca o clip, escala a 1080p).
- `efectos`: microanimacións sutís sobre a imaxe (antes da cámara, para que se movan co relevo) ou sobre o
  fotograma (choiva, po). Máscaras por cor, profundidade e CLIPSeg (CIDAS/clipseg-rd64-refined, Apache-2.0).

Cachés (en `MOVEMENTO_CACHE`, por defecto `$SCRATCH/movemento`): profundidade e máscaras por sha256 da imaxe;
clips I2V por sha256 de imaxe + acción + parámetros. Cada proceso de montaxe só carga o que precisa o seu treito.

Este módulo corre no venv principal (numpy, OpenCV, PIL; torch e transformers só para preparar profundidade e
máscaras). Ningunha función de render carga modelos: se falta a profundidade na caché, `preparar()` faina antes.
"""
import hashlib, json, math, os, subprocess, sys, time
from pathlib import Path

import numpy as np

OW, OH, FPS = 1920, 1080, 24
SOBRE = 1.10                 # a imaxe fonte prepárase a 1,1 veces a saída: marxe para a cámara
FOV = 50.0                   # campo de visión horizontal suposto (graos) para pasar de profundidade a píxeles
ZFAR = 5.0                   # profundidade do fondo respecto do primeiro termo (= 1): canto relevo hai
DEPTH_REPO = 'depth-anything/Depth-Anything-V2-Small-hf'     # Apache-2.0
CLIPSEG_REPO = 'CIDAS/clipseg-rd64-refined'                  # Apache-2.0
CAMARAS = ('avanza', 'recua', 'xira_esq', 'xira_der', 'sobe', 'baixa', 'pan_esq', 'pan_der')
EFECTOS = ('lume', 'candea', 'choiva', 'bretema', 'fume', 'auga', 'ceo', 'po')


def _scratch():
    return os.environ.get('SCRATCH') or '/tmp/revolta-scratch'


def cache_dir(sub=''):
    d = Path(os.environ.get('MOVEMENTO_CACHE', f'{_scratch()}/movemento')) / sub
    d.mkdir(parents=True, exist_ok=True)
    return d


def sha_ficheiro(p, n=16):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()[:n]


def a_16_9(im):
    """Recorte central a 16:9 sen deformar (como montaxe._a_16_9)."""
    w, h = im.size
    r = OW / OH
    if abs(w / h - r) < 0.005:
        return im
    if w / h > r:
        nw = round(h * r); x = (w - nw) // 2
        return im.crop((x, 0, x + nw, h))
    nh = round(w / r); y = (h - nh) // 2
    return im.crop((0, y, w, y + nh))


def fonte(imaxe, escala=SOBRE):
    """Imaxe fonte en float32 (0-255) a escala x saída, recortada a 16:9, Lanczos + máscara de desenfoque
    suave (o mesmo tratamento que a montaxe da v1)."""
    from PIL import Image, ImageFilter
    im = a_16_9(Image.open(imaxe).convert('RGB'))
    W, H = round(OW * escala), round(OH * escala)
    im = im.resize((W, H), Image.LANCZOS).filter(ImageFilter.UnsharpMask(radius=2, percent=40, threshold=2))
    return np.asarray(im, np.float32)


# ------------------------------------------------------------------ preparación (modelos): profundidade e máscaras
_MOD = {}


def _hf_cache(repo):
    """Busca o repo na caché de HF do contorno principal ou na do contorno de vídeo."""
    for base in (os.environ.get('HF_HOME'), f'{_scratch()}/hf', f'{_scratch()}/video/hf'):
        if base and (Path(base) / 'hub' / ('models--' + repo.replace('/', '--'))).exists():
            return str(Path(base) / 'hub')
    return None


def _depth_model():
    if 'depth' not in _MOD:
        import torch
        from transformers import AutoImageProcessor, AutoModelForDepthEstimation
        cd = _hf_cache(DEPTH_REPO)
        _MOD['depth'] = (AutoImageProcessor.from_pretrained(DEPTH_REPO, cache_dir=cd),
                         AutoModelForDepthEstimation.from_pretrained(DEPTH_REPO, cache_dir=cd).eval())
        torch.set_num_threads(int(os.environ.get('NTH', '4')))
    return _MOD['depth']


def profundidade(imaxe, lado=756):
    """Disparidade relativa (1 = o máis preto, 0 = o máis lonxe) do tamaño da imaxe recortada a 16:9, con caché.
    `lado`: lado curto da entrada do modelo (adestrado a 518; a máis resolución saen bordos máis finos)."""
    from PIL import Image
    f = cache_dir('prof') / f'{sha_ficheiro(imaxe)}_{lado}.npy'
    if f.exists():
        return np.load(f).astype(np.float32)
    import torch
    proc, mod = _depth_model()
    im = a_16_9(Image.open(imaxe).convert('RGB'))
    w, h = im.size
    lw = int(round(lado * w / h / 14)) * 14
    x = proc(images=im.resize((lw, lado), Image.BICUBIC), return_tensors='pt', do_resize=False)
    with torch.no_grad():
        d = mod(**x).predicted_depth[0].float().numpy()
    import cv2
    d = cv2.resize(d, (w, h), interpolation=cv2.INTER_CUBIC)
    lo, hi = np.percentile(d, 1), np.percentile(d, 99.5)
    d = np.clip((d - lo) / max(hi - lo, 1e-6), 0, 1).astype(np.float32)
    tmp = f.with_suffix('.tmp.npy'); np.save(tmp, d.astype(np.float16)); os.replace(tmp, f)
    return d


def _clipseg():
    if 'clipseg' not in _MOD:
        from transformers import CLIPSegForImageSegmentation, CLIPSegProcessor
        cd = _hf_cache(CLIPSEG_REPO)
        _MOD['clipseg'] = (CLIPSegProcessor.from_pretrained(CLIPSEG_REPO, cache_dir=cd),
                           CLIPSegForImageSegmentation.from_pretrained(CLIPSEG_REPO, cache_dir=cd).eval())
    return _MOD['clipseg']


# textos de CLIPSeg por efecto (a probabilidade final é o máximo dos textos)
TEXTOS_MASCARA = {
    'lume': ['fire', 'flames'],
    'candea': ['candle flame', 'small flame'],
    'auga': ['water', 'river', 'water surface'],
    'ceo': ['sky', 'clouds'],
    'fume': ['smoke', 'mist'],
}


def clipseg(imaxe, textos):
    """Probabilidade (0-1) de cada texto, ao tamaño da imaxe recortada a 16:9, con caché."""
    from PIL import Image
    import cv2
    f = cache_dir('masc') / f'{sha_ficheiro(imaxe)}.npz'
    feito = dict(np.load(f)) if f.exists() else {}
    falta = [t for t in textos if t not in feito]
    if falta:
        import torch
        proc, mod = _clipseg()
        im = a_16_9(Image.open(imaxe).convert('RGB'))
        x = proc(text=falta, images=[im] * len(falta), padding='max_length', return_tensors='pt')
        with torch.no_grad():
            lg = mod(**x).logits
        lg = lg.reshape(len(falta), *lg.shape[-2:]).float().sigmoid().numpy()
        for t, p in zip(falta, lg):
            feito[t] = cv2.resize(p, im.size, interpolation=cv2.INTER_LINEAR).astype(np.float16)
        tmp = f.with_suffix('.tmp.npz'); np.savez_compressed(tmp, **feito); os.replace(tmp, f)
    return {t: feito[t].astype(np.float32) for t in textos}


def preparar(planos, imaxes, lado=756):
    """Calcula (con caché) a profundidade e as máscaras de CLIPSeg que precisan os planos animados. Vai antes da
    montaxe, nun só proceso (≈ 0,5 GB de modelos). Devolve segundos por imaxe."""
    t0 = time.time(); n = 0
    for e, im in zip(planos, imaxes):
        an = e.get('animacion') or {}
        if not an:
            continue
        profundidade(im, lado)          # tamén nos I2V: se falta o clip, o plano vai en paralaxe
        txt = [t for ef in an.get('efectos', []) for t in TEXTOS_MASCARA.get(ef, [])]
        if txt:
            clipseg(im, txt)
        n += 1
    for k in list(_MOD):
        del _MOD[k]
    return (time.time() - t0) / max(n, 1)


# ------------------------------------------------------------------ ruído e sinais
def ruido(h, w, escala, rng, oitavas=3):
    """Ruído de valor suave (0-1), h x w, coa escala dada en píxeles (oitavas de grellas reescaladas)."""
    import cv2
    acc = np.zeros((h, w), np.float32); amp, tot = 1.0, 0.0
    for _ in range(oitavas):
        gh, gw = max(2, int(h / escala) + 3), max(2, int(w / escala) + 3)
        acc += amp * cv2.resize(rng.random((gh, gw)).astype(np.float32), (w, h), interpolation=cv2.INTER_CUBIC)
        tot += amp; amp *= 0.5; escala = max(2.0, escala / 2)
    return acc / tot


def parpadeo(t, semente=0, rapido=1.0):
    """Sinal de parpadeo de chama en [-1, 1] aprox.: suma de senos de 0,4 a 11 Hz con fases ao chou (1/f)."""
    rng = np.random.default_rng(semente)
    fr = np.array([0.43, 0.9, 1.7, 2.9, 4.6, 7.1, 10.9]) * rapido
    am = 1 / np.sqrt(fr); am /= am.sum()
    ph = rng.random(len(fr)) * 2 * np.pi
    return float(np.sum(am * np.sin(2 * np.pi * fr * t + ph))) * 1.6


# ------------------------------------------------------------------ cámara 2,5D
def _z(disp):
    """Disparidade relativa (1 = preto) -> profundidade con primeiro termo en 1 e fondo en ZFAR."""
    return 1.0 / (1.0 / ZFAR + (1 - 1.0 / ZFAR) * disp)


def camara(nome, dur, forza=1.0, zp=2.0):
    """Percorrido da cámara: función u (0-1) -> (tx, ty, tz, sx, sy) en unidades normalizadas (tx, ty: fracción
    da distancia focal, coa profundidade do primeiro termo = 1). Amplitude segundo a duración, con tope: a
    velocidade é a dun travelling lento (≈ 4-6 % do ancho en 10 s para o primeiro termo)."""
    a = forza * min(0.055, max(0.022, 0.0042 * dur))          # tralación lateral total (primeiro termo)
    z = forza * min(0.13, max(0.05, 0.0105 * dur))           # avance total
    def f(u):
        tx = ty = tz = sx = sy = 0.0
        if nome == 'avanza':
            tz = z * u
        elif nome == 'recua':
            tz = z * (1 - u)
        elif nome in ('pan_esq', 'pan_der'):
            s = 1 if nome == 'pan_esq' else -1
            tx = s * a * (0.5 - u)
        elif nome in ('sobe', 'baixa'):
            s = 1 if nome == 'baixa' else -1
            ty = s * a * 0.7 * (0.5 - u)
        elif nome in ('xira_esq', 'xira_der'):
            s = 1 if nome == 'xira_esq' else -1
            tx = s * a * 1.3 * (0.5 - u)
            sx = tx / zp                                       # o punto de xiro (profundidade zp) queda quieto
            tz = 0.25 * z * u
        return tx, ty, tz, sx, sy
    return f


class Paralaxe:
    """Cámara 2,5D sobre unha imaxe con mapa de disparidade.

    Xeometría: punto da fonte con coordenadas normalizadas (x, y) (píxeles/focal, centro = 0) e profundidade Z;
    a cámara trasládase (tx, ty, tz) e despraza a imaxe (sx, sy):  x' = (x·Z − tx)/(Z − tz) + sx.
    Por fotograma: (1) proxección dos puntos da fonte a media resolución, de lonxe a preto (o máis preto queda
    enriba); (2) os ocos énchense coa profundidade máis lonxana da veciñanza (o fondo); (3) inversa analítica
    x = ((x' − sx)(Z − tz) + tx)/Z para cada píxel de saída e cv2.remap da fonte; (4) nos ocos mostréase a fonte co
    primeiro termo "borrado" (inpaint na beira de cada salto de profundidade)."""

    def __init__(self, src, disp, nome_camara, dur, forza=1.0, semente=0):
        import cv2
        self.src = src                                    # float32 HxWx3 (0-255), fonte a SOBRE x saída
        H, W = src.shape[:2]
        self.H, self.W = H, W
        self.f = (W / 2) / math.tan(math.radians(FOV / 2))
        d = cv2.resize(disp, (W, H), interpolation=cv2.INTER_LINEAR)
        self.Z = _z(d).astype(np.float32)
        cen = d[int(H * 0.3):int(H * 0.7), int(W * 0.3):int(W * 0.7)]
        zp = float(_z(np.percentile(cen, 60)))
        self.cam = camara(nome_camara, dur, forza, zp)
        # escala da saída: a saída ve a fonte reducida a 1/SOBRE; zoom extra se a cámara destapa os bordos
        self.k = self._zoom_necesario()
        # grella media para a proxección (z-buffer)
        self.hs, self.ws = H // 2, W // 2
        Zs = cv2.resize(self.Z, (self.ws, self.hs), interpolation=cv2.INTER_NEAREST)
        ys, xs = np.mgrid[0:self.hs, 0:self.ws].astype(np.float32)
        xn = (xs * 2 + 1.0 - W / 2) / self.f; yn = (ys * 2 + 1.0 - H / 2) / self.f
        orde = np.argsort(-Zs.ravel(), kind='stable')        # de lonxe a preto
        self.p_x, self.p_y, self.p_z = xn.ravel()[orde], yn.ravel()[orde], Zs.ravel()[orde]
        # grella de saída a media resolución (coordenadas normalizadas da cámara)
        self.oh, self.ow = OH // 2, OW // 2
        oy, ox = np.mgrid[0:self.oh, 0:self.ow].astype(np.float32)
        esc = self.f * self.k * (OW / W) * SOBRE           # píxeles de saída por unidade normalizada
        self.esc_o = esc
        self.o_x = (ox * 2 + 1.0 - OW / 2) / esc; self.o_y = (oy * 2 + 1.0 - OH / 2) / esc
        self.fondo = None                                 # fonte co primeiro termo borrado (preguiceira)
        self.d = d

    def _zoom_necesario(self):
        """Zoom mínimo (≥ 1) para que ningún punto do bordo da saída mostree fóra da fonte en ningún momento. Para
        cada bordo úsanse as profundidades que hai de verdade nunha banda da fonte xunto a ese bordo."""
        H, W = self.H, self.W
        b = max(4, int(0.12 * min(H, W)))
        bandas = {'esq': self.Z[:, :b], 'der': self.Z[:, -b:], 'arr': self.Z[:b], 'aba': self.Z[-b:]}
        zs = {k: np.unique(np.percentile(v, [0, 25, 50, 75, 100]).round(3)) for k, v in bandas.items()}
        hw, hh = (W / SOBRE) / 2 / self.f, (H / SOBRE) / 2 / self.f        # semiancho visible (normalizado)
        lim_x, lim_y = (W / 2 - 2) / self.f, (H / 2 - 2) / self.f
        t = np.linspace(-1, 1, 9)
        bordos = ([('esq', -hw, hh * v) for v in t] + [('der', hw, hh * v) for v in t] +
                  [('arr', hw * v, -hh) for v in t] + [('aba', hw * v, hh) for v in t])
        k = 1.0
        for u in np.linspace(0, 1, 9):
            tx, ty, tz, sx, sy = self.cam(u)
            for nome, cx, cy in bordos:
                for Z in zs[nome]:
                    for kk in np.arange(k, 1.6, 0.005):
                        x = ((cx / kk - sx) * (Z - tz) + tx) / Z
                        y = ((cy / kk - sy) * (Z - tz) + ty) / Z
                        if abs(x) <= lim_x and abs(y) <= lim_y:
                            k = kk; break
        return float(k)

    def _fondo(self):
        """Fonte co primeiro termo borrado nunha banda á beira de cada salto de profundidade (inpaint de Telea a
        media resolución), para mostrear o fondo que a cámara destapa."""
        import cv2
        if self.fondo is not None:
            return self.fondo
        H, W = self.H, self.W
        r = int(0.06 * W)
        d = self.d
        dmin = cv2.erode(d, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * r + 1, 2 * r + 1)))
        banda = ((d - dmin) > 0.10).astype(np.uint8)
        if banda.mean() < 1e-4:
            self.fondo = self.src; return self.fondo
        s2 = cv2.resize(np.clip(self.src, 0, 255).astype(np.uint8), (W // 2, H // 2), interpolation=cv2.INTER_AREA)
        b2 = cv2.resize(banda, (W // 2, H // 2), interpolation=cv2.INTER_NEAREST)
        b2 = cv2.dilate(b2, np.ones((3, 3), np.uint8))
        f2 = cv2.inpaint(s2, b2, 5, cv2.INPAINT_TELEA)
        f = cv2.resize(f2, (W, H), interpolation=cv2.INTER_CUBIC).astype(np.float32)
        m = cv2.GaussianBlur(cv2.resize(b2, (W, H), interpolation=cv2.INTER_NEAREST).astype(np.float32), (0, 0), 3)[..., None]
        self.fondo = self.src * (1 - m) + f * m
        return self.fondo

    def mapas(self, u):
        """(map_x, map_y, oco) en píxeles da fonte para o progreso u; oco = 1 onde a cámara destapa fondo."""
        import cv2
        tx, ty, tz, sx, sy = self.cam(u)
        Z = self.p_z
        xp = (self.p_x * Z - tx) / (Z - tz) + sx
        yp = (self.p_y * Z - ty) / (Z - tz) + sy
        # a píxeles da grella media de saída
        gx = xp * self.esc_o / 2 + self.ow / 2 - 0.5
        gy = yp * self.esc_o / 2 + self.oh / 2 - 0.5
        zt = np.zeros(self.oh * self.ow, np.float32)
        for dx, dy in ((0, 0), (1, 0), (0, 1), (1, 1)):     # 2x2: sen gretas ao achegarse
            ix = np.floor(gx).astype(np.int32) + dx; iy = np.floor(gy).astype(np.int32) + dy
            ok = (ix >= 0) & (ix < self.ow) & (iy >= 0) & (iy < self.oh)
            zt[(iy[ok] * self.ow + ix[ok])] = Z[ok]          # en orde de lonxe a preto: gaña o máis próximo
        zt = zt.reshape(self.oh, self.ow)
        oco = zt == 0
        if oco.any():
            k3 = np.ones((3, 3), np.uint8)
            for _ in range(40):
                zd = cv2.dilate(zt, k3)                       # máximo = o máis lonxano da veciñanza
                zt = np.where(oco, zd, zt)
                oco = zt == 0
                if not oco.any():
                    break
            zt[zt == 0] = ZFAR
        buraco = (zt == 0)  # (baleiro: xa enchido)
        del buraco
        # inversa analítica na grella media e escala a resolución completa
        mx = ((self.o_x - sx) * (zt - tz) + tx) / zt * self.f + self.W / 2 - 0.5
        my = ((self.o_y - sy) * (zt - tz) + ty) / zt * self.f + self.H / 2 - 0.5
        mx = cv2.resize(mx, (OW, OH), interpolation=cv2.INTER_LINEAR)
        my = cv2.resize(my, (OW, OH), interpolation=cv2.INTER_LINEAR)
        return mx, my, zt

    def frame(self, u, src=None):
        """Fotograma de saída (float32 OHxOWx3) para o progreso u; `src` permite pasar a fonte xa animada."""
        import cv2
        src = self.src if src is None else src
        mx, my, zt = self.mapas(u)
        out = cv2.remap(src, mx, my, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT101)
        # ocos destapados: onde a profundidade proxectada é moito máis lonxana ca a da fonte nese punto
        zsrc = cv2.remap(self.Z, mx, my, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT101)
        zt_full = cv2.resize(zt, (OW, OH), interpolation=cv2.INTER_LINEAR)
        oco = np.clip((zt_full / zsrc - 1.15) / 0.25, 0, 1)
        if oco.max() > 0.02:
            oco = cv2.GaussianBlur(oco.astype(np.float32), (0, 0), 2)[..., None]
            fb = cv2.remap(self._fondo() if src is self.src else self._fondo() + (src - self.src),
                           mx, my, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT101)
            out = out * (1 - oco) + fb * oco
        self.zt = zt_full
        return out


# ------------------------------------------------------------------ microanimacións
def _cl(x, a, b):
    """Rampla 0-1 entre a e b."""
    return np.clip((x - a) / (b - a), 0, 1)


def _lum(S):
    return S[..., 0] * 0.2126 + S[..., 1] * 0.7152 + S[..., 2] * 0.0722


def _caixa(m, lim, marxe=(0.3, 0.3, 0.8, 0.15), minimo=24):
    """Caixa (y0, y1, x0, x1) arredor de m > lim, ampliada (esquerda, dereita, arriba, abaixo) en fracción do seu tamaño."""
    ys, xs = np.nonzero(m > lim)
    if len(ys) == 0:
        return None
    y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
    h, w = max(y1 - y0, minimo), max(x1 - x0, minimo)
    H, W = m.shape
    return (max(0, int(y0 - marxe[2] * h)), min(H, int(y1 + marxe[3] * h)),
            max(0, int(x0 - marxe[0] * w)), min(W, int(x1 + marxe[1] * w)))


class Efecto:
    """`fonte(S, t)` cambia a imaxe fonte antes da cámara (o efecto vai co relevo); `pantalla(F, t)` o fotograma."""
    activo = True

    def fonte(self, S, t):
        return S

    def pantalla(self, F, t):
        return F


class _Chama:
    """Unha chama (compoñente conexa da máscara de lume): caixa, ruído que corre cara arriba e zona de desprazamento."""

    def __init__(self, F, caixa, alto, dur, rng, candea, forza):
        import cv2
        y0, y1, x0, x1 = caixa
        self.cx = caixa
        hr, wr = y1 - y0, x1 - x0
        self.v = (1.6 if not candea else 2.4) * alto                 # px/s que soben as linguas de lume
        lon = int(self.v * (dur + 2)) + hr + 8
        lam = max(4.0, (0.16 if not candea else 0.22) * alto)
        self.tx = (ruido(lon, wr, lam, rng) - 0.5).astype(np.float32)
        self.ty = (ruido(lon, wr, lam * 1.3, rng) - 0.5).astype(np.float32)
        self.A = (0.075 if not candea else 0.05) * alto * forza       # amplitude do desprazamento (px)
        Fr = F[y0:y1, x0:x1]
        dil = cv2.dilate(Fr, np.ones((max(3, alto // 6) | 1, max(3, alto // 10) | 1), np.uint8))
        arriba = np.zeros_like(dil)
        n = max(2, alto // 3)
        for k in range(1, n):                                           # estela cara arriba
            arriba[:-k] = np.maximum(arriba[:-k], dil[k:] * (1 - k / n))
        self.Fd = cv2.GaussianBlur(np.maximum(dil, arriba), (0, 0), max(1.0, alto / 25)).astype(np.float32)
        self.Fr = cv2.GaussianBlur(Fr, (0, 0), 1.0).astype(np.float32)[..., None]
        self.gy, self.gx = np.mgrid[0:hr, 0:wr].astype(np.float32)
        self.sem = int(rng.integers(0, 1 << 30))


class Lume(Efecto):
    """Chamas (lareira, fogueira, queimada) ou candea: as linguas de lume suben (desprazamento con ruído que
    corre cara arriba só sobre os píxeles de cada chama), cada chama tremela en intensidade co seu propio sinal e a
    luz do contorno tremela co sinal medio (o que máis vende o efecto). Máscara: píxeles brillantes e quentes
    (R > G > B) e, se hai, CLIPSeg "fire"/"candle flame"; cada compoñente conexa é unha chama."""

    def __init__(self, src, prob=None, dur=10.0, semente=0, candea=False, forza=1.0):
        import cv2
        S = src / 255.0
        R, G, B = S[..., 0], S[..., 1], S[..., 2]
        L = _lum(S)
        F = _cl(R - B, 0.16, 0.42) * _cl(L, 0.42, 0.68) * (R >= G * 0.98)
        if prob is not None:
            F *= _cl(prob, 0.12, 0.35)
        F = cv2.morphologyEx(F.astype(np.float32), cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
        self.candea = candea
        H, W = F.shape
        rng = np.random.default_rng(semente + 21)
        n, lab, st, _ = cv2.connectedComponentsWithStats((F > 0.2).astype(np.uint8), 8)
        minimo = (25 if candea else 120)
        self.chamas = []
        for c in np.argsort(-st[1:, cv2.CC_STAT_AREA])[:12] + 1:        # as 12 maiores
            x, y, w, h, area = st[c]
            if area < minimo:
                continue
            alto = max(10, int(h))
            caixa = (max(0, int(y - (1.4 if candea else 0.9) * alto)), min(H, int(y + h + 0.12 * alto)),
                     max(0, int(x - 0.35 * w)), min(W, int(x + w + 0.35 * w)))
            Fc = F * (lab == c)
            self.chamas.append(_Chama(Fc, caixa, alto, dur, rng, candea, forza))
        if not self.chamas:
            self.activo = False; return
        # mapa de luz do contorno: a chama desenfocada a gran escala, normalizada
        p = 4
        Fp = cv2.resize(F, (W // p, H // p), interpolation=cv2.INTER_AREA)
        sig = (0.10 if candea else 0.16) * W / p
        I = cv2.GaussianBlur(Fp, (0, 0), sig)
        I = I / max(I.max(), 1e-6)
        self.I = cv2.resize(I, (W, H), interpolation=cv2.INTER_LINEAR).astype(np.float32)[..., None]
        self.amp_luz = (0.07 if not candea else 0.045) * forza
        self.amp_chama = (0.16 if not candea else 0.12) * forza
        self.sem = semente
        self.ton = np.array([1.0, 0.86, 0.62], np.float32)          # a luz do lume é quente

    def fonte(self, S, t):
        import cv2
        S = S.copy() if S is self._orixe else S
        for ch in self.chamas:
            y0, y1, x0, x1 = ch.cx
            hr = y1 - y0
            L = ch.tx.shape[0]
            o = L - hr - int(ch.v * t) % max(1, (L - hr))               # o ruído corre cara arriba
            dx = ch.tx[o:o + hr] * ch.A * ch.Fd
            dy = (ch.ty[o:o + hr] * ch.A * 1.4 + ch.A * 0.25) * ch.Fd
            if self.candea:                                             # a candea abanea un pouco
                dx = dx + (0.35 * ch.A * math.sin(2 * math.pi * 0.55 * t + ch.sem % 7) +
                           0.2 * ch.A * math.sin(2 * math.pi * 1.37 * t)) * ch.Fd
            roi = S[y0:y1, x0:x1]
            w = cv2.remap(roi, ch.gx + dx, ch.gy + dy, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT101)
            pc = parpadeo(t, ch.sem, 1.4 if self.candea else 1.0)
            S[y0:y1, x0:x1] = w * (1 + self.amp_chama * pc * ch.Fr)
        # luz do contorno: parpadeo propio, algo máis lento (a luz suma as linguas de lume)
        pl = 0.65 * parpadeo(t, self.sem + 1, 1.0) + 0.35 * parpadeo(t - 0.05, self.sem + 2, 0.5)
        S *= 1 + self.amp_luz * pl * self.I * self.ton
        return S

    _orixe = None


class Choiva(Efecto):
    """Choiva en pantalla: tres capas de raias finas (lonxe, medio, preto) que caen a distinta velocidade, máis
    marcadas sobre fondos escuros. Texturas feitas unha vez (cv2.line con antialias) e desprazadas en cada
    fotograma: custo ≈ 3 sumas por fotograma."""
    CAPAS = [  # (velocidade px/s, lonxitude px, grosor, opacidade, gotas, desenfoque)
        (650, 16, 1, 0.13, 1100, 0.0),
        (1150, 30, 1, 0.16, 520, 0.5),
        (1850, 58, 2, 0.11, 110, 1.3),
    ]

    def __init__(self, dur=10.0, semente=0, forza=1.0, angulo=7.0):
        import cv2
        rng = np.random.default_rng(semente + 77)
        self.tex = []
        a = math.radians(angulo)
        for (v, lon, gr, op, n, bl) in self.CAPAS:
            T = np.zeros((2 * OH, OW), np.uint8)
            for _ in range(int(n * forza)):
                x, y = int(rng.integers(0, OW)), int(rng.integers(0, 2 * OH))
                l = lon * (0.6 + 0.8 * rng.random())
                x2, y2 = int(x - l * math.sin(a)), int(y - l * math.cos(a))
                b = int(140 + 115 * rng.random())
                cv2.line(T, (x, y), (x2, y2), b, gr, cv2.LINE_AA)
                if y2 < 0:   # continuidade ao dar a volta
                    cv2.line(T, (x, y + 2 * OH), (x2, y2 + 2 * OH), b, gr, cv2.LINE_AA)
            Tf = T.astype(np.float32) / 255
            if bl > 0:
                Tf = cv2.GaussianBlur(Tf, (0, 0), bl)
            self.tex.append((v, op * forza, Tf.astype(np.float16)))
        self.cor = np.array([228, 232, 238], np.float32)

    def pantalla(self, F, t):
        a = np.zeros((OH, OW), np.float32)
        for v, op, T in self.tex:
            o = 2 * OH - int(v * t) % (2 * OH)
            if o + OH <= 2 * OH:
                capa = T[o:o + OH]
            else:
                capa = np.concatenate([T[o:], T[:o + OH - 2 * OH]])
            a += capa.astype(np.float32) * op
        a = np.minimum(a, 0.6)[..., None]
        return F + a * (self.cor - F)


class Bretema(Efecto):
    """Brétema que se despraza amodo, máis densa ao lonxe (profundidade) e algo máis abaixo; cor tirada das
    luces lonxanas da propia imaxe (non un gris xenérico). Na fonte: vai co relevo da cámara."""

    def __init__(self, src, disp, dur=10.0, semente=0, forza=1.0, fume=False):
        import cv2
        H, W = src.shape[:2]
        rng = np.random.default_rng(semente + 5)
        self.p = 4
        h, w = H // self.p, W // self.p
        d = cv2.resize(disp, (w, h), interpolation=cv2.INTER_AREA)
        lonxe = _cl(1 - d, 0.35, 0.95) ** 1.3
        vert = np.linspace(0.75, 1.0, h, dtype=np.float32)[:, None]
        self.base = (0.25 + 0.75 * lonxe) * vert
        self.v1, self.v2 = 9.0 / self.p, 4.0 / self.p                  # px/s (a resolución da fonte: 9 e 4)
        L = int(w + self.v1 * (dur + 2) + 4)
        self.n1 = ruido(h, L, w / 3.0, rng)
        self.n2 = ruido(h, L, w / 6.0, rng)
        S = src / 255.0
        Lm = _lum(S)
        sel = (cv2.resize(lonxe, (W, H)) > 0.5) & (Lm > np.percentile(Lm, 70))
        c = S[sel].mean(0) * 255 if sel.sum() > 100 else S.reshape(-1, 3).mean(0) * 255
        self.cor = (0.55 * c + 0.45 * np.array([205, 210, 214])).astype(np.float32)
        self.op = 0.20 * forza
        self.hw = (h, w); self.HW = (H, W)

    def fonte(self, S, t):
        import cv2
        h, w = self.hw
        o1, o2 = int(self.v1 * t), int(self.v2 * t)
        n = 0.6 * self.n1[:, o1:o1 + w] + 0.4 * self.n2[:, o2:o2 + w]
        m = self.op * self.base * _cl(n, 0.25, 0.85)
        m = cv2.resize(m, (self.HW[1], self.HW[0]), interpolation=cv2.INTER_LINEAR)[..., None]
        return S * (1 - m) + self.cor * m


class Fluxo(Efecto):
    """Desprazamento suave que corre nunha dirección dentro dunha máscara: auga (ondas horizontais e reflexos que
    escintilan), ceo (nubes que se desprazan) e fume (sobe amodo)."""

    def __init__(self, src, m, tipo, dur=10.0, semente=0, forza=1.0):
        import cv2
        self.tipo = tipo
        H, W = m.shape
        m = cv2.GaussianBlur(m.astype(np.float32), (0, 0), 3)
        if m.max() < 0.3 or (m > 0.3).mean() < 0.004:
            self.activo = False; return
        cx = _caixa(m, 0.2, (0.05, 0.05, 0.05, 0.05))
        self.cx = cx
        y0, y1, x0, x1 = cx
        hr, wr = y1 - y0, x1 - x0
        self.m = m[y0:y1, x0:x1][..., None]
        rng = np.random.default_rng(semente + 11)
        self.gy, self.gx = np.mgrid[0:hr, 0:wr].astype(np.float32)
        if tipo == 'auga':
            self.v = 18.0; lam = max(6.0, W / 90); self.A = 2.2 * forza
            L = int(hr + self.v * (dur + 2) + 4)
            self.nx = ruido(L, wr, lam, rng) - 0.5
            self.ny = ruido(L, wr, lam * 2.5, rng) - 0.5
            S = src[y0:y1, x0:x1] / 255.0
            Lr = _lum(S)
            self.brillo = _cl(Lr - cv2.GaussianBlur(Lr, (0, 0), 6), 0.01, 0.08)[..., None]
            self.ns = ruido(L, wr, lam * 0.7, rng)
        elif tipo == 'ceo':
            self.v = 0.012 * W * forza                                  # nubes: ≈ 1,2 % do ancho por segundo
            self.A = 0
            lam = W / 8
            L = int(wr + 4)
            self.nx = (ruido(hr, wr, lam, rng) - 0.5) * 6
        else:   # fume
            self.v = 0.05 * hr + 6; lam = max(8.0, hr / 6); self.A = max(2.0, 0.03 * hr) * forza
            L = int(hr + self.v * (dur + 2) + 4)
            self.nx = ruido(L, wr, lam, rng) - 0.5
            self.ny = ruido(L, wr, lam * 1.4, rng) - 0.5

    def fonte(self, S, t):
        import cv2
        y0, y1, x0, x1 = self.cx
        hr = y1 - y0
        roi = S[y0:y1, x0:x1]
        if self.tipo == 'ceo':
            mx = self.gx - self.v * t + self.nx
            w = cv2.remap(roi, mx, self.gy, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT101)
        else:
            L = self.nx.shape[0]
            o = int(self.v * t) % max(1, L - hr)
            if self.tipo == 'fume':
                o = L - hr - o                                          # sobe
            dx = self.nx[o:o + hr] * self.A
            dy = self.ny[o:o + hr] * self.A * (0.35 if self.tipo == 'auga' else 1.0)
            w = cv2.remap(roi, self.gx + dx, self.gy + dy, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT101)
            if self.tipo == 'auga':
                s = self.ns[o:o + hr][..., None]
                w = w * (1 + 0.22 * (s - 0.5) * self.brillo)
        S = S.copy()
        S[y0:y1, x0:x1] = roi * (1 - self.m) + w * self.m
        return S


class Po(Efecto):
    """Po no aire: partículas moi pequenas que flotan amodo, visibles só onde hai luz."""

    def __init__(self, src, dur=10.0, semente=0, forza=1.0, n=90):
        import cv2
        rng = np.random.default_rng(semente + 3)
        self.n = int(n * forza)
        self.x0 = rng.random(self.n) * OW; self.y0 = rng.random(self.n) * OH
        self.vx = rng.normal(0, 6, self.n); self.vy = rng.normal(-1.5, 4, self.n)
        self.f = rng.random(self.n) * 0.4 + 0.15; self.ph = rng.random(self.n) * 6.28
        self.r = rng.random(self.n) * 1.2 + 0.9
        self.b = rng.random(self.n) * 0.6 + 0.4

    def pantalla(self, F, t):
        import cv2
        capa = np.zeros((OH, OW), np.float32)
        x = (self.x0 + self.vx * t + 6 * np.sin(self.f * t + self.ph)) % OW
        y = (self.y0 + self.vy * t + 5 * np.cos(0.7 * self.f * t + self.ph)) % OH
        for xi, yi, ri, bi in zip(x, y, self.r, self.b):
            cv2.circle(capa, (int(xi * 4), int(yi * 4)), int(ri * 4), float(bi), -1, cv2.LINE_AA, shift=2)
        capa = cv2.GaussianBlur(capa, (0, 0), 0.8)
        luz = _cl(F.mean(-1) / 255, 0.25, 0.75)
        a = (capa * luz * 0.55)[..., None]
        return F + a * (250 - F)


def efectos_do_plano(nomes, src, disp, imaxe, dur, semente=0, forza=1.0):
    """Instancia os efectos pedidos (os que non atopan onde actuar quedan inactivos e non custan nada)."""
    out = []
    for nome in nomes or []:
        if nome in ('lume', 'candea'):
            pr = clipseg(imaxe, TEXTOS_MASCARA[nome])
            pr = np.maximum.reduce(list(pr.values()))
            import cv2
            pr = cv2.resize(pr, (src.shape[1], src.shape[0]))
            e = Lume(src, pr, dur, semente, candea=(nome == 'candea'), forza=forza)
            e._orixe = src
        elif nome == 'choiva':
            e = Choiva(dur, semente, forza)
        elif nome in ('bretema',):
            e = Bretema(src, disp, dur, semente, forza)
        elif nome in ('auga', 'ceo', 'fume'):
            import cv2
            pr = clipseg(imaxe, TEXTOS_MASCARA[nome])
            pr = np.maximum.reduce(list(pr.values()))
            pr = cv2.resize(pr, (src.shape[1], src.shape[0]))
            dd = cv2.resize(disp, (src.shape[1], src.shape[0]))
            if nome == 'ceo':
                m = _cl(pr, 0.35, 0.6) * _cl(0.45 - dd, 0.0, 0.25)
            elif nome == 'auga':
                m = _cl(pr, 0.3, 0.55)
            else:
                Ls = _lum(src / 255.0)
                m = _cl(pr, 0.25, 0.5) * _cl(Ls - cv2.GaussianBlur(Ls, (0, 0), 25), -0.02, 0.06)
            e = Fluxo(src, m, nome, dur, semente, forza)
        elif nome == 'po':
            e = Po(src, dur, semente, forza)
        else:
            continue
        if e.activo:
            out.append((nome, e))
    return out


# ------------------------------------------------------------------ clips I2V: caché, cámara lenta e escala
I2V_PARAMS = {'modelo': 'ltxv-2b-0.9.8-distilled', 'W': 800, 'H': 448, 'F': 97, 'pasos': 8, 'semente': 42,
              'ruido_cond': 0.15}


def i2v_clave(imaxe, accion, params=None):
    p = dict(I2V_PARAMS, **(params or {}))
    txt = json.dumps({'imaxe': sha_ficheiro(imaxe), 'accion': accion, **p}, sort_keys=True)
    return hashlib.sha256(txt.encode()).hexdigest()[:16]


def i2v_ficheiro(imaxe, accion, params=None):
    """Ruta do clip na caché (exista ou non)."""
    return cache_dir('i2v') / f'{i2v_clave(imaxe, accion, params)}.mp4'


def ler_video(f):
    """Fotogramas (N, h, w, 3) uint8 dun vídeo, co ffmpeg de imageio."""
    import imageio_ffmpeg
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    info = subprocess.run([ff, '-i', str(f)], capture_output=True, text=True).stderr
    import re
    m = re.search(r'Stream.*Video.*?(\d{2,5})x(\d{2,5})', info)
    w, h = int(m.group(1)), int(m.group(2))
    p = subprocess.run([ff, '-v', 'error', '-i', str(f), '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'],
                       capture_output=True, check=True)
    return np.frombuffer(p.stdout, np.uint8).reshape(-1, h, w, 3)


_RIFE = {}


def _rife():
    """RIFE v4 (ECCV2022-RIFE, MIT, © Megvii) desde o repo TensorForger/RIFE-safetensors: só o punto medio."""
    if 'm' not in _RIFE:
        import importlib.util
        import torch
        from huggingface_hub import hf_hub_download
        from safetensors.torch import load_file
        cd = _hf_cache('TensorForger/RIFE-safetensors')
        py = hf_hub_download('TensorForger/RIFE-safetensors', 'interpolation_model.py', cache_dir=cd)
        pesos = hf_hub_download('TensorForger/RIFE-safetensors', 'flownet.safetensors', cache_dir=cd)
        spec = importlib.util.spec_from_file_location('rife_ifnet', py)
        mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
        mod.device, mod.dtype = torch.device('cpu'), torch.float32       # o módulo trae a grella en fp16
        m = mod.IFNet(); m.load_state_dict(load_file(pesos)); m.eval()
        _RIFE['m'] = m
    return _RIFE['m']


def interpolar(frames, veces=2):
    """Insire fotogramas intermedios con RIFE (punto medio, recursivo): N -> (N-1)*veces+1. veces = 2 ou 4."""
    import torch
    m = _rife()
    n, h, w, _ = frames.shape
    ph, pw = (32 - h % 32) % 32, (32 - w % 32) % 32
    x = torch.from_numpy(frames).permute(0, 3, 1, 2).float() / 255
    if ph or pw:
        x = torch.nn.functional.pad(x, (0, pw, 0, ph), mode='replicate')
    with torch.no_grad():
        for _ in range(int(math.log2(veces))):
            medios = []
            for i in range(0, x.shape[0] - 1, 4):
                a = x[i:i + 4]; b = x[i + 1:i + 5]
                k = min(len(a), len(b))
                medios.append(m(torch.cat([a[:k], b[:k]], 1)).clamp(0, 1))
            md = torch.cat(medios)
            out = torch.empty((x.shape[0] * 2 - 1, *x.shape[1:]))
            out[0::2] = x; out[1::2] = md
            x = out
    x = x[:, :, :h, :w]
    return (x.permute(0, 2, 3, 1).numpy() * 255 + 0.5).astype(np.uint8)


def clip_lento(mp4, veces=2):
    """Clip interpolado (caché xunto ao clip): para a cámara lenta dos planos máis longos ca o clip."""
    f = Path(mp4).with_name(Path(mp4).stem + f'_x{veces}.npy')
    if f.exists():
        return np.load(f, mmap_mode='r')
    fr = interpolar(ler_video(mp4), veces)
    tmp = f.with_suffix('.tmp.npy'); np.save(tmp, fr); os.replace(tmp, f)
    return np.load(f, mmap_mode='r')


class Clip:
    """Encaixa un clip I2V nun plano de duración `dur`: se o plano é máis longo ca o clip, cámara lenta (fotogramas
    de RIFE) ata `lento_min` (0,5 = a metade de velocidade); se aínda sobra plano, o derradeiro fotograma segue coa
    cámara 2D lenta. Escala a 1080p con Lanczos e unha máscara de desenfoque suave; zoom lento opcional."""

    def __init__(self, mp4, dur, camara_nome='avanza', lento_min=0.5, zoom=1.05, imaxe=None):
        base = ler_video(mp4)
        # detalle: a imaxe fonte a 1080p (a mesma coa que se condicionou o clip) para devolverlle ao clip o
        # detalle fino que perde a 448p (transferencia guiada polo fluxo óptico, ver _detalle)
        self.still = None
        if imaxe is not None and os.environ.get('MOVEMENTO_DETALLE', '1') == '1':
            self.still = fonte(imaxe, 1.0)
            self.f0 = base[0]
        self.fps = FPS
        dur_clip = (len(base) - 1) / FPS
        v = dur_clip / max(dur, 1e-3)
        if v >= 0.98:
            self.fr, self.vel = base, 1.0
        else:
            veces = 2 if v >= 0.45 else 4
            self.fr = clip_lento(mp4, veces) if os.environ.get('MOVEMENTO_RIFE', '1') == '1' else base
            fact = (len(self.fr) - 1) / (len(base) - 1)
            self.vel = max(v, lento_min) * fact                     # fotogramas do clip lento por fotograma de saída
        self.dur = dur
        self.camara = camara_nome
        self.zoom = zoom

    def frame(self, t):
        import cv2
        i = min(len(self.fr) - 1, t * FPS * self.vel)
        a = int(i); b = min(a + 1, len(self.fr) - 1); w = i - a
        im = self.fr[a].astype(np.float32) if w < 0.02 else (self.fr[a] * (1 - w) + self.fr[b] * w).astype(np.float32)
        h0, w0 = im.shape[:2]
        # recorte 16:9 do clip e zoom lento (a cámara 2D: o clip xa trae o seu propio movemento)
        u = min(1.0, max(0.0, t / max(self.dur, 1e-3)))
        z = 1 + (self.zoom - 1) * (u if self.camara != 'recua' else 1 - u)
        cw, ch = w0 / z, min(h0, w0 / z * OH / OW)
        x0, y0 = (w0 - cw) / 2, (h0 - ch) / 2
        M = np.array([[OW / cw, 0, -x0 * OW / cw], [0, OH / ch, -y0 * OH / ch]], np.float32)
        out = cv2.warpAffine(im, M, (OW, OH), flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REFLECT101)
        if self.still is not None:
            return self._detalle(im, out, M)
        bl = cv2.GaussianBlur(out, (0, 0), 1.6)
        return np.clip(out * 1.45 - bl * 0.45, 0, 255)

    def _detalle(self, im, out, M):
        """Transferencia de detalle: o fluxo óptico (DIS) do fotograma actual ao primeiro, escalado a 1080p,
        deforma a imaxe fonte a 1080p ata a xeometría do fotograma; o seu detalle fino (paso alto) súmase ao clip
        escalado só onde a imaxe deformada e o clip coinciden (confianza). Onde o clip trae contido novo (unha
        perna que avanza, algo que se destapa) a confianza baixa e queda o clip escalado."""
        import cv2
        h0, w0 = im.shape[:2]
        if not hasattr(self, '_dis'):
            self._dis = cv2.DISOpticalFlow_create(cv2.DISOPTICAL_FLOW_PRESET_MEDIUM)
            self._g0 = cv2.cvtColor(self.f0, cv2.COLOR_RGB2GRAY)
            # a fonte na xeometría do fotograma 0 do clip (mesmo recorte), a 1080p
            Hs, Ws = self.still.shape[:2]
            self._Ms = np.array([[w0 / Ws, 0, 0], [0, h0 / Hs, 0]], np.float32)
        g = cv2.cvtColor(np.clip(im, 0, 255).astype(np.uint8), cv2.COLOR_RGB2GRAY)
        fl = self._dis.calc(g, self._g0, None)                       # fotograma actual -> fotograma 0 (px do clip)
        sx, sy = M[0, 0], M[1, 1]
        flo = cv2.warpAffine(fl, M, (OW, OH), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
        # punto de saída -> punto do clip actual -> punto do fotograma 0 -> punto da fonte a 1080p
        if not hasattr(self, '_xy'):
            self._xy = np.mgrid[0:OH, 0:OW].astype(np.float32)
        ys, xs = self._xy
        cx = (xs - M[0, 2]) / sx + flo[..., 0]
        cy = (ys - M[1, 2]) / sy + flo[..., 1]
        mx = cx / self._Ms[0, 0]; my = cy / self._Ms[1, 1]
        W_ = cv2.remap(self.still, mx, my, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT101)
        # confianza: a fonte deformada e o clip teñen que coincidir a baixa frecuencia
        a = cv2.GaussianBlur(W_, (0, 0), 3.0); b = cv2.GaussianBlur(out, (0, 0), 3.0)
        err = np.abs(a - b).mean(-1)
        c = np.exp(-(err / 12.0) ** 2)
        c = cv2.GaussianBlur(c, (0, 0), 4.0)[..., None]
        det = W_ - cv2.GaussianBlur(W_, (0, 0), 1.8)
        bl = cv2.GaussianBlur(out, (0, 0), 1.6)
        base = out * 1.25 - bl * 0.25
        return np.clip(base + c * det, 0, 255)


# ------------------------------------------------------------------ plano animado (o que usa a montaxe)
class Plano:
    """Un plano animado: paralaxe + efectos, ou clip I2V (+ efectos de pantalla). `frame(u, t)` devolve float32
    OHxOWx3 (0-255) para o progreso u (0-1) e o tempo t (s) desde que o plano empeza a verse."""

    def __init__(self, e, imaxe, dur, semente=0):
        an = dict(e.get('animacion') or {})
        self.modo = an.get('modo', 'paralaxe')
        cam = an.get('camara') or 'avanza'
        forza = float(an.get('forza', 1.0))
        self.efs, self.efp = [], []
        self.clip = None
        if self.modo == 'i2v':
            f = an.get('clip') or i2v_ficheiro(imaxe, an.get('accion', ''), an.get('i2v'))
            if Path(f).exists():
                self.clip = Clip(f, dur, cam, imaxe=imaxe)
            else:                                    # sen clip na caché: paralaxe (e avísase)
                print(f'movemento: falta o clip I2V do plano {e.get("n")} ({f}); vai en paralaxe', flush=True)
                self.modo = 'paralaxe'
        if self.modo != 'i2v':
            self.src = fonte(imaxe)
            disp = profundidade(imaxe)
            efs = efectos_do_plano(an.get('efectos'), self.src, disp, imaxe, dur, semente, forza)
            self.efs = [x for n, x in efs if n not in ('choiva', 'po')]
            self.efp = [x for n, x in efs if n in ('choiva', 'po')]
            self.plx = Paralaxe(self.src, disp, cam if self.modo == 'paralaxe' else 'avanza', dur,
                                forza if self.modo == 'paralaxe' else 0.0, semente)
        else:
            efs = efectos_do_plano([x for x in an.get('efectos', []) if x in ('choiva', 'po')], None, None,
                                   imaxe, dur, semente, forza)
            self.efp = [x for n, x in efs]

    def frame(self, u, t):
        if self.clip is not None:
            F = self.clip.frame(t)
        else:
            S = self.src
            for ef in self.efs:
                S = ef.fonte(S, t)
            F = self.plx.frame(u, S)
        for ef in self.efp:
            F = ef.pantalla(F, t)
        return F


# ------------------------------------------------------------------ porta de vídeo (clips I2V)
# Limiares calibrados coas probas da rolda 1 (plan-de-negocio/gauntlet4/movemento/informe-r1.md, §porta)
PORTA = {
    'clip_min': 0.80,          # coseno CLIP entre o primeiro fotograma e calquera outro (cambio de escena / fusión)
    'parpadeo_max': 3.0,       # desviación (0-255) da luminancia media fóra da súa tendencia (media móbil de 9)
    'fluxo_min': 0.12,         # px/fotograma de media (a 800 px de ancho): por debaixo, o clip está quieto
    'fluxo_max': 4.5,          # px/fotograma de media: por riba, movemento caótico ou cámara tola
    'incoherencia_max': 0.85,  # desorde local do fluxo (0 = ríxido, 1 = ruído)
    'salto_max': 0.45,         # salto dos puntos do corpo entre mostras seguidas, en tamaños de torso
    'proporcion_cv_max': 0.30, # variación (CV) da lonxitude dos brazos e pernas respecto do torso
}


def _mediapipe():
    if 'mp' not in _MOD:
        import mediapipe as mp
        from mediapipe.tasks.python import BaseOptions, vision
        d = Path(os.environ.get('REVISOR_DIR', f'{_scratch()}/revisor'))
        hands = vision.HandLandmarker.create_from_options(vision.HandLandmarkerOptions(
            base_options=BaseOptions(model_asset_path=str(d / 'hand_landmarker.task')), num_hands=8,
            min_hand_detection_confidence=0.35, min_hand_presence_confidence=0.35))
        pose = vision.PoseLandmarker.create_from_options(vision.PoseLandmarkerOptions(
            base_options=BaseOptions(model_asset_path=str(d / 'pose_landmarker_full.task')), num_poses=4,
            min_pose_detection_confidence=0.3))
        _MOD['mp'] = (mp, hands, pose)
    return _MOD['mp']


def _corpos(fr):
    """Corpos de MediaPipe nun fotograma: lista de arrays (33, 3) x, y (en unidades do alto), visibilidade."""
    mp, hands, pose = _mediapipe()
    h, w = fr.shape[:2]
    im = mp.Image(image_format=mp.ImageFormat.SRGB, data=np.ascontiguousarray(fr))
    p = pose.detect(im); hd = hands.detect(im)
    cs = [np.array([[l.x * w / h, l.y, l.visibility] for l in lm], np.float32) for lm in p.pose_landmarks]
    mans = [np.array([lm[0].x * w / h, lm[0].y], np.float32) for lm in hd.hand_landmarks]
    return cs, mans


def porta_video(mp4, mostras=16, clip=None):
    """Porta automática dun clip I2V. Mide: (1) deriva de CLIP entre o primeiro fotograma e o resto; (2) parpadeo
    de luminancia; (3) fluxo óptico (Farneback): nin quieto nin caótico, e a súa desorde local; (4) MediaPipe
    (corpo e mans) en `mostras` fotogramas: saltos dos puntos do corpo, proporcións que cambian (corpos que se
    deforman), mans sen corpo. Devolve {'ok', 'problemas', 'avisos', medidas...}."""
    import cv2
    fr = ler_video(mp4)
    N, h, w = fr.shape[:3]
    res = {'fotogramas': int(N), 'res': f'{w}x{h}'}
    # (2) parpadeo
    L = fr.reshape(N, -1).mean(1)
    k = 9
    tend = np.convolve(np.pad(L, (k // 2, k // 2), mode='edge'), np.ones(k) / k, mode='valid')
    res['parpadeo'] = round(float(np.abs(L - tend).max()), 2)
    # (3) fluxo óptico a media resolución
    g = [cv2.cvtColor(cv2.resize(x, (w // 2, h // 2), interpolation=cv2.INTER_AREA), cv2.COLOR_RGB2GRAY) for x in fr]
    mags, inco = [], []
    for i in range(0, N - 1, 2):
        fl = cv2.calcOpticalFlowFarneback(g[i], g[i + 1], None, 0.5, 3, 15, 3, 5, 1.2, 0)
        mg = np.linalg.norm(fl, axis=-1) * 2                       # a px de resolución do clip
        mags.append(float(mg.mean()))
        loc = cv2.blur(fl, (15, 15))
        dev = np.linalg.norm(fl - loc, axis=-1) * 2
        inco.append(float(dev.mean() / (mg.mean() + 0.05)))
    esc = 800.0 / w                                                 # normalizado a 800 px de ancho
    res['fluxo_medio'] = round(float(np.mean(mags)) * esc, 3)
    res['fluxo_p95'] = round(float(np.percentile(mags, 95)) * esc, 3)
    res['incoherencia'] = round(float(np.median(inco)), 3)
    # (1) CLIP
    idx = np.linspace(0, N - 1, min(mostras, N)).round().astype(int)
    try:
        if clip is None:
            sys.path.insert(0, str(Path(__file__).resolve().parent))
            import revisor
            clip = revisor.Clip()
        import tempfile
        from PIL import Image
        embs = []
        with tempfile.TemporaryDirectory() as td:
            for i in idx[::2].tolist() + [int(idx[-1])]:
                f = f'{td}/{i}.png'; Image.fromarray(fr[i]).save(f)
                embs.append(clip.imaxe(f))
        cs = [float(embs[0] @ e) for e in embs[1:]]
        res['clip_min'] = round(min(cs), 3); res['clip_fin'] = round(cs[-1], 3)
    except Exception as ex:                                         # sen CLIP: a porta segue co resto
        res['clip_erro'] = str(ex)[:120]
    # (4) MediaPipe
    saltos, props, ncorp, orfas = [], [], [], 0
    prev = None
    for i in idx:
        cs, mans = _corpos(fr[i])
        ncorp.append(len(cs))
        for c in cs:
            vis = c[:, 2] > 0.5
            torso = np.linalg.norm((c[11, :2] + c[12, :2]) / 2 - (c[23, :2] + c[24, :2]) / 2)
            if torso < 0.04 or not vis[[11, 12, 23, 24]].all():
                continue
            membros = [(11, 13), (13, 15), (12, 14), (14, 16), (23, 25), (25, 27), (24, 26), (26, 28)]
            props.append([np.linalg.norm(c[a, :2] - c[b, :2]) / torso if vis[a] and vis[b] else np.nan
                          for a, b in membros])
            if prev is not None:
                cen = (c[11, :2] + c[24, :2]) / 2
                pc = min(prev, key=lambda q: np.linalg.norm((q[11, :2] + q[24, :2]) / 2 - cen))
                v2 = vis & (pc[:, 2] > 0.5)
                if v2.sum() >= 6:
                    saltos.append(float(np.median(np.linalg.norm(c[v2, :2] - pc[v2, :2], axis=1)) / torso))
        pulsos = [c[j, :2] for c in cs for j in (15, 16)]
        for m in mans:
            d = min((np.linalg.norm(m - q) for q in pulsos), default=9.0)
            orfas += d > 0.14 and len(cs) > 0
        prev = cs if cs else prev
    res['corpos'] = ncorp
    # salto entre mostras: normalízase a mostras cada ~3 fotogramas
    paso = max(1, (N - 1) / max(1, len(idx) - 1))
    res['salto_max'] = round(max(saltos) * 3 / paso, 3) if saltos else None
    if props:
        P = np.array(props, np.float32)
        cv = np.nanstd(P, 0) / (np.nanmean(P, 0) + 1e-6)
        cv = cv[np.sum(~np.isnan(P), 0) >= 4]
        res['proporcion_cv'] = round(float(np.nanmax(cv)), 3) if len(cv) else None
    res['mans_sen_corpo'] = int(orfas)
    pr, av = [], []
    if res.get('clip_min') is not None and res['clip_min'] < PORTA['clip_min']:
        pr.append(f"deriva da escena (CLIP {res['clip_min']})")
    if res['parpadeo'] > PORTA['parpadeo_max']:
        pr.append(f"parpadeo de luz ({res['parpadeo']})")
    if res['fluxo_medio'] < PORTA['fluxo_min']:
        pr.append(f"case quieto (fluxo {res['fluxo_medio']} px/f)")
    if res['fluxo_medio'] > PORTA['fluxo_max']:
        pr.append(f"movemento excesivo (fluxo {res['fluxo_medio']} px/f)")
    if res['incoherencia'] > PORTA['incoherencia_max']:
        av.append(f"movemento desordenado ({res['incoherencia']})")
    if res.get('salto_max') and res['salto_max'] > PORTA['salto_max']:
        pr.append(f"salto do corpo ({res['salto_max']} torsos)")
    if res.get('proporcion_cv') and res['proporcion_cv'] > PORTA['proporcion_cv_max']:
        pr.append(f"corpo que se deforma (CV {res['proporcion_cv']})")
    if orfas > 1:
        av.append(f'mans sen corpo en {orfas} mostras')
    if len(set(ncorp)) > 2:
        av.append(f'corpos que aparecen e desaparecen {sorted(set(ncorp))}')
    res.update({'ok': not pr, 'problemas': pr, 'avisos': av})
    return res
