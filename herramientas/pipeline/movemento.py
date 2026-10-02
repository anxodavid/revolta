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
        if an.get('modo') in (None, 'fixo', 'i2v') and not an.get('efectos'):
            continue
        profundidade(im, lado)
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
        xn = (xs * 2 + 0.5 - W / 2) / self.f; yn = (ys * 2 + 0.5 - H / 2) / self.f
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
        """Zoom mínimo (≥ 1) para que nin a esquina máis próxima nin a máis lonxana saian da fonte en ningún momento."""
        k = 1.0
        hw, hh = (self.W / SOBRE) / 2 / self.f, (self.H / SOBRE) / 2 / self.f     # semiancho visible (normalizado)
        lim_x, lim_y = (self.W / 2 - 2) / self.f, (self.H / 2 - 2) / self.f
        for u in np.linspace(0, 1, 9):
            tx, ty, tz, sx, sy = self.cam(u)
            for Z in (1.0, 1.4, 2.5, ZFAR):
                for cx, cy in ((hw, hh), (-hw, hh), (hw, -hh), (-hw, -hh)):
                    # punto de saída (cx/k, cy/k): onde está na fonte?
                    for kk in np.arange(k, 1.6, 0.01):
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
