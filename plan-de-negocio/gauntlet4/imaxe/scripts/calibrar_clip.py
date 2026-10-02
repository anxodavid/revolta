"""Calibración da porta v6 e da medida de correlación (Gauntlet 4, peza IMAXE) con CLIP ViT-L/14.

Dúas fases:
  calcular  (pesada: flock "$CPU_LOCK"): embeddings de CLIP-L das 173 imaxes da v1 (162 do episodio + 11 anteriores á
            rolda de arranxos, que saen de git 4f43fb5) en 9 recortes (3 cadrados grandes, como a v5, e unha grella
            3x2 de cadrados pequenos), e dos textos candidatos (pares malo/bo, claves, distractores e o texto_en de
            cada plano, frase a frase). Garda $SCRATCH/imaxe4/calib/clip.npz e textos.json.
  analizar  (lixeira): le o anterior e as etiquetas (calibracion/etiquetas-v1.json) e imprime, para cada porta, os
            valores das malas e das boas.

    flock "$CPU_LOCK" $PY calibrar_clip.py calcular
    $PY calibrar_clip.py analizar
"""
import json, os, re, subprocess, sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
sys.path.insert(0, str(REPO / 'herramientas/pipeline'))
S = Path(os.environ.get('SCRATCH', '/tmp')) / 'imaxe4'
CAL = S / 'calib'
V1 = REPO / 'plan-de-negocio/gauntlet3/video'
ETIQ = AQUI.parent / 'calibracion' / 'etiquetas-v1.json'

# ---- textos candidatos ------------------------------------------------------------------------------------------
PARES_NOVOS = [   # (etiqueta, malo, bo)
    ('bombilla', 'a bare electric light bulb hanging from the ceiling', 'a dark wooden ceiling with old beams'),
    ('radiador', 'a white cast iron radiator under a window', 'a rough granite wall under a small window'),
    ('lampada colgante', 'a hanging pendant lamp with a glass shade', 'a black iron pot hanging from a chain'),
    ('aplique', 'an electric wall sconce lamp', 'a candle burning in a niche of a stone wall'),
    ('farolas', 'lit electric street lamps on lamp posts', 'a dark meadow at night'),
    ('farol victoriano', 'a victorian cast iron lamp post', 'a wooden fence post'),
    ('maleta de rodas', 'a modern wheeled suitcase with a telescopic handle', 'an old leather suitcase carried by hand'),
    ('fregadoiro', 'a modern kitchen sink with a chrome faucet', 'a stone water basin in a peasant kitchen'),
    ('cocina economica', 'a cast iron kitchen range stove with an oven door', 'an open stone hearth at floor level with a wood fire'),
    ('casa inglesa', 'an English country cottage with gable chimneys and sash windows',
     'a low Galician granite farmhouse with small openings and a slate roof'),
    ('casa xeorxiana', 'a Georgian manor house with rows of sash windows', 'a Galician granite manor house with a stone coat of arms'),
    ('casa colonial', 'a two-story colonial house with a porch and lit windows', 'a dark stone farmhouse at night'),
    ('cotswolds', 'a Cotswolds village street with stone cottages', 'a Galician village lane with granite houses and slate roofs'),
    ('casa nordica', 'colourful wooden houses on stilts by the sea', 'granite fishermen houses by the sea'),
    ('ventas acesas', 'a house with brightly lit windows at night', 'a dark stone house at night'),
    ('roupa actual', 'a person in modern clothes', 'a peasant in coarse wool clothes of the seventeenth century'),
    ('chaqueta tweed', 'a man in a tweed jacket and a flat cap', 'a peasant man in a coarse wool cloak'),
    ('abrigo moderno', 'a woman in a modern tailored coat with a handbag', 'a peasant woman in a long wool skirt and a shawl'),
    ('gorro de la', 'a woman wearing a knitted beanie hat', 'a woman wearing a dark wool headscarf'),
    ('sombreiro moderno', 'a person wearing a bowler hat or a cowboy hat', 'a person wearing a wool cap'),
    ('cadros', 'framed pictures hanging on the wall', 'a bare stone wall'),
    ('xanela moderna', 'a large window with many glass panes', 'a small window with wooden shutters'),
    ('lume na mesa', 'a fire burning on top of a wooden table', 'a candle on a wooden table'),
    ('salon', 'a cozy modern living room', 'a smoke-blackened peasant kitchen'),
    ('pobo iluminado', 'a town with many lit windows in the background at night', 'dark hills at night'),
    ('catedral', 'a large baroque cathedral with two tall towers', 'a small romanesque granite church'),
]
DISTRACTORES = ['person', 'woman', 'man', 'old woman', 'old man', 'face', 'hands', 'cat', 'dog', 'cow', 'sheep', 'horse',
                'bird', 'house', 'village', 'church', 'castle', 'tree', 'forest', 'field', 'hills', 'mountain', 'sea', 'river',
                'boat', 'ship', 'fire', 'candle', 'lantern', 'table', 'chair', 'bench', 'door', 'window', 'wall', 'road',
                'bread', 'pot', 'bowl', 'jug', 'cup', 'basket', 'book', 'paper', 'flowers', 'herbs', 'moon', 'sky', 'clouds',
                'rain', 'snow', 'smoke', 'stone', 'cross', 'fountain', 'bridge', 'kitchen', 'room', 'shoes', 'clothes',
                'rope', 'coins', 'jewel', 'animal', 'food', 'drink', 'fish', 'night', 'sunset', 'statue', 'cloister']


def recortes(im, grella=True):
    """3 cadrados grandes (esquerda, centro, dereita, como a v5) e, con grella, 6 pequenos (3x2)."""
    w, h = im.size
    s = min(w, h)
    xs = [0, (w - s) // 2, w - s] if w >= h else [0]
    ys = [0] if w >= h else [0, (h - s) // 2, h - s]
    out = [im.crop((x, y, x + s, y + s)) for x in xs for y in ys]
    if grella:
        t = min(w // 3, h // 2) if w >= h else min(w // 2, h // 3)
        nx, ny = (3, 2) if w >= h else (2, 3)
        for j in range(ny):
            for i in range(nx):
                x = round(i * (w - t) / (nx - 1)); y = round(j * (h - t) / (ny - 1))
                out.append(im.crop((x, y, x + t, y + t)))
    return out


def imaxes():
    et = json.load(open(ETIQ))['imaxes']
    vellas = S / 'v1vellas'; vellas.mkdir(parents=True, exist_ok=True)
    out = []
    for d in et:
        if d['version'] == 'vella':
            p = vellas / Path(d['ficheiro']).name
            if not p.exists():
                b = subprocess.run(['git', '-C', str(REPO), 'show',
                                    f'4f43fb5:plan-de-negocio/gauntlet3/video/imaxes/{p.name}'], capture_output=True, check=True).stdout
                p.write_bytes(b)
        else:
            p = V1 / d['ficheiro']
        out.append((d, p))
    return out


def frases_en(t):
    return [x.strip() for x in re.split(r'(?<=[.!?])\s+', t) if len(x.strip()) > 3]


def calcular():
    import numpy as np, torch
    from PIL import Image
    import revisor
    torch.set_num_threads(int(os.environ.get('NTH', '4')))
    CAL.mkdir(parents=True, exist_ok=True)
    clip = revisor.Clip()
    ims = imaxes()
    E = []
    for k, (d, p) in enumerate(ims):
        rec = recortes(Image.open(p).convert('RGB'))
        with torch.no_grad():
            e = clip.m.get_image_features(**clip.proc(images=rec, return_tensors='pt'))
        E.append((e / e.norm(dim=-1, keepdim=True)).numpy())
        if k % 20 == 0:
            print('imaxe', k, flush=True)
    E = np.stack(E)                      # [N, 9, 768]
    esc = json.load(open(REPO / 'plan-de-negocio/gauntlet4/imaxe/v1-texto-en.json'))['planos']
    claves = sorted({x.get('clave') for x in json.load(open(V1 / 'escenas-montadas.json')) if x.get('clave')})
    textos = ['a photo']
    textos += [t for _, a, b in PARES_NOVOS for t in (a, b)]
    textos += [t for _, a, b in revisor.PARES for t in (a, b)]
    textos += [f'a photo with {c}' for c in claves] + [f'a photo of {c}' for c in claves + DISTRACTORES]
    textos += [t for et, ts, _, _ in revisor.ARQUETIPOS for t in ts]
    for x in esc:
        textos += frases_en(x['texto_en']) + [x['texto_en']]
    textos = list(dict.fromkeys(textos))
    T = clip.textos(textos)
    np.savez_compressed(CAL / 'clip.npz', E=E, T=T)
    (CAL / 'textos.json').write_text(json.dumps({'textos': textos, 'imaxes': [str(p) for _, p in ims]}, ensure_ascii=False))
    print('feito', E.shape, T.shape, flush=True)


def cargar():
    import numpy as np
    z = np.load(CAL / 'clip.npz')
    t = json.loads((CAL / 'textos.json').read_text())
    ix = {x: i for i, x in enumerate(t['textos'])}
    et = json.load(open(ETIQ))['imaxes']
    return z['E'], z['T'], ix, et


CATEGORIA = {   # par -> defecto das etiquetas que debería cazar
    'bombilla': 'luz_electrica', 'radiador': 'radiador', 'lampada colgante': 'luz_electrica', 'aplique': 'luz_electrica',
    'farolas': 'luz_electrica', 'farol victoriano': 'luz_electrica', 'ventas acesas': 'luz_electrica',
    'pobo iluminado': 'luz_electrica', 'maleta de rodas': 'maleta_rodas', 'fregadoiro': 'billa_fregadoiro',
    'cocina economica': 'cocina_economica', 'casa inglesa': 'casa_allea', 'casa xeorxiana': 'casa_allea',
    'casa colonial': 'casa_allea', 'cotswolds': 'casa_allea', 'casa nordica': 'casa_allea', 'roupa actual': 'roupa_actual',
    'chaqueta tweed': 'roupa_actual', 'abrigo moderno': 'roupa_actual', 'gorro de la': 'roupa_actual',
    'sombreiro moderno': 'roupa_actual', 'cadros': 'interior_moderno', 'xanela moderna': 'xanela_moderna',
    'lume na mesa': 'lume_mesa', 'salon': 'interior_moderno', 'catedral': 'catedral_inventada'}


def defectos(d):
    return set(d.get('defectos') or []) | set(d.get('defectos_claude') or [])


def limpa(d):
    """Imaxe sen ningún defecto anotado (nin do tribunal nin de Claude)."""
    return not defectos(d) and d['tribunal'] in ('funciona', 'aceptable', 'sen_mencion', 'despois_dos_arranxos')


def auc(pos, neg):
    import numpy as np
    pos, neg = np.asarray(pos, float), np.asarray(neg, float)
    if not len(pos) or not len(neg):
        return float('nan')
    return float(((pos[:, None] > neg[None, :]).mean() + 0.5 * (pos[:, None] == neg[None, :]).mean()))


def pares(E, T, ix, et, imprimir=True):
    """Para cada par novo: marxe (peor recorte) en 3 e en 9 recortes; umbral = máximo das imaxes limpas + 0,003."""
    import numpy as np
    out = {}
    for etq, a, b in PARES_NOVOS:
        sa, sb = E @ T[ix[a]], E @ T[ix[b]]
        cat = CATEGORIA[etq]
        for nome, sl in (('3', slice(0, 3)), ('9', slice(0, 9))):
            marxe = (sa[:, sl] - sb[:, sl]).max(1)
            pert = np.maximum(sa[:, sl].max(1), sb[:, sl].max(1))
            ok = [i for i, d in enumerate(et) if limpa(d) and not (cat == 'roupa_actual' and d['seculo_xx'])]
            malas = [i for i, d in enumerate(et) if cat in defectos(d)]
            umbral = float(marxe[ok].max()) + 0.003
            cazadas = [i for i in malas if marxe[i] > umbral]
            outras = [i for i, d in enumerate(et) if i not in ok and i not in malas and marxe[i] > umbral]
            out[(etq, nome)] = {'umbral': round(umbral, 3), 'malas': [(et[i]['n'], et[i]['version'][0], round(float(marxe[i]), 3)) for i in malas],
                                'cazadas': [(et[i]['n'], et[i]['version'][0]) for i in cazadas],
                                'outras_marcadas': [(et[i]['n'], et[i]['version'][0], et[i]['tribunal'][:4], sorted(defectos(et[i]))) for i in outras],
                                'auc': round(auc(marxe[malas], marxe[ok]), 3), 'pert_mediana': round(float(np.median(pert)), 3)}
            if imprimir:
                o = out[(etq, nome)]
                print(f"{etq:18s} [{nome}] umbral {o['umbral']:.3f} AUC {o['auc']:.2f} cazadas {len(cazadas)}/{len(malas)} {o['cazadas']} "
                      f"| malas {o['malas']} | outras {o['outras_marcadas'][:6]}")
    return out


def clave(E, T, ix, et, imprimir=True):
    """Tres maneiras de ver se está a clave do plano, contra a etiqueta de Claude (`clave_ve`)."""
    import numpy as np
    esc = json.load(open(V1 / 'escenas-montadas.json'))
    base = E @ T[ix['a photo']]
    claves = sorted({x.get('clave') for x in esc if x.get('clave')})
    res = {}
    datos = [(i, d) for i, d in enumerate(et) if d['version'] == 'actual' and d.get('clave')]
    for i, d in datos:
        c = d['clave']
        sw = E[i] @ T[ix[f'a photo with {c}']] - base[i]
        so = E[i] @ T[ix[f'a photo of {c}']]
        outros = [x for x in claves + DISTRACTORES if x != c and x not in c and c not in x]
        Do = np.stack([E[i] @ T[ix[f'a photo of {x}']] for x in outros])      # [n_outros, 9]
        z = (so - Do.mean(0)) / (Do.std(0) + 1e-6)
        rango = (Do < so[None, :]).mean(0)                                     # fracción de outros por debaixo
        res[i] = {'v5_3': float(sw[:3].max()), 'v5_9': float(sw.max()), 'z_3': float(z[:3].max()), 'z_9': float(z.max()),
                  'rango_9': float(rango.max()), 'rango_3': float(rango[:3].max())}
    for met in ('v5_3', 'v5_9', 'z_3', 'z_9', 'rango_3', 'rango_9'):
        ve = [res[i][met] for i, d in datos if d['clave_ve']]
        nove = [res[i][met] for i, d in datos if not d['clave_ve']]
        # umbral que colle a metade das ausentes e falsas alarmas a ese umbral
        nv = np.sort(nove)
        u = float(np.median(nv))
        fa = float(np.mean(np.asarray(ve) < u))
        if imprimir:
            print(f'clave {met:8s} AUC(ve>non) {auc(ve, nove):.3f}  ausentes {len(nove)}: mediana {u:.3f} -> falsas alarmas {fa:.0%} das {len(ve)} presentes')
    return res, datos


def correlacion(E, T, ix, et, imprimir=True):
    """CLIP-L entre cada imaxe e o texto_en do seu plano, fronte á etiqueta `ilustra` de Claude (0/1/2)."""
    import numpy as np
    esc = json.load(open(REPO / 'plan-de-negocio/gauntlet4/imaxe/v1-texto-en.json'))['planos']
    datos = [(i, d) for i, d in enumerate(et) if d['version'] == 'actual']
    emb = E[:, :3].mean(1); emb = emb / np.linalg.norm(emb, axis=1, keepdims=True)
    textos_unicos = list(dict.fromkeys(x['texto_en'] for x in esc))
    Tt = np.stack([T[ix[t]] for t in textos_unicos])
    fr = {t: [T[ix[f]] for f in frases_en(t) if f in ix] for t in textos_unicos}
    res = {}
    for i, d in datos:
        t = esc[d['n'] - 1]['texto_en']
        s_all = Tt @ emb[i]                       # imaxe fronte a todos os textos
        s = float(emb[i] @ T[ix[t]])
        sf = max(float(emb[i] @ v) for v in fr[t]) if fr[t] else s
        # frases de todos os textos, para normalizar a medida por frase
        res[i] = {'cos': s, 'cos_frase': sf, 'z': float((s - s_all.mean()) / (s_all.std() + 1e-6)),
                  'rango': float((s_all < s).mean())}
    for met in ('cos', 'cos_frase', 'z', 'rango'):
        v = {k: [res[i][met] for i, d in datos if d['ilustra'] == k] for k in (0, 1, 2)}
        if imprimir:
            print(f'correlación {met:9s} medias 0/1/2: {np.mean(v[0]):.3f} / {np.mean(v[1]):.3f} / {np.mean(v[2]):.3f}  '
                  f'AUC 2 fronte a 0: {auc(v[2], v[0]):.3f}  (1+2) fronte a 0: {auc(v[1] + v[2], v[0]):.3f}  n={[len(v[k]) for k in (0, 1, 2)]}')
    return res, datos


def analizar():
    E, T, ix, et = cargar()
    print('== pares novos (porta v6) ==')
    o = pares(E, T, ix, et)
    print('== clave ==')
    clave(E, T, ix, et)
    print('== correlación imaxe-texto ==')
    correlacion(E, T, ix, et)
    CAL.mkdir(parents=True, exist_ok=True)
    (CAL / 'pares.json').write_text(json.dumps({f'{a}|{b}': v for (a, b), v in o.items()}, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    {'calcular': calcular, 'analizar': analizar}[sys.argv[1]]()
