"""Porta automática de imaxes: revisa cada imaxe xerada e, se falla, a etapa IMAXES rexenera con outra semente.

Tres revisores abertos, en CPU:

1. Anatomía das mans e contas de corpos (MediaPipe Tasks, Apache-2.0: hand_landmarker + pose_landmarker_full).
   - "man sen corpo": unha man detectada cuxo pulso non está preto (distancia normalizada > MAN_DIST) do
     pulso de ningún corpo detectado. É o defecto do plano final da ronda 1 (catro mans, un par sen brazo).
   - "máis de dúas mans por corpo": mans > 2 x corpos (cando hai corpos).
   - "multitude (N corpos)": máis de CORPOS_MAX corpos (versión 5: as caras das multitudes saen deformes).
2. Lista de anacronismos e contidos vetados sobre a descrición e os obxectos que ve un modelo visión-linguaxe
   aberto (Florence-2-large, MIT): <MORE_DETAILED_CAPTION> + <OD>. Se a descrición ou os obxectos
   conteñen algo da lista (xanelas de vidro, balcóns, tellados laranxas, coches, texto, cruces
   portadas, armas de fogo, sangue, multitudes...) a imaxe falla. Versión 5: tamén ciprés, oliveiras, palmeiras,
   eucaliptos, muros encalados, estuco, rodas de raios e paisaxes "mediterráneas".
3. CLIP ViT-L/14 (openai/clip-vit-large-patch14, MIT), versión 5 (Gauntlet 3):
   - porta de ICONOGRAFÍA GALEGA: para cada par (concepto mediterráneo ou alleo, equivalente galego) —tella
     laranxa/lousa, encalado/granito, ciprés/carballo, oliveira/prado, palmeira/carballo, roda de raios/roda
     maciza, paisaxe seca/atlántica—, a imaxe falla se se parece ao concepto malo máis que ao bo por riba dunha
     marxe calibrada e o concepto é pertinente na imaxe. Mírase en tres recortes cadrados (esquerda, centro,
     dereita), porque CLIP só ve un cadrado e os tellados adoitan estar nos lados. Tamén os conceptos do campo
     `negativo` do plano.
   - porta de REPETICIÓN contra TODAS as imaxes aceptadas do episodio (non só as catro anteriores): similitude
     coseno dos embeddings de CLIP > SIM_CLIP.
   - ARQUETIPOS de composición con tope por episodio e separación mínima (o crítico visual viu "figuras con capa
     afastándose por un camiño" 3-4 veces en 12 fotogramas).

Limitacións (medidas nas probas, ver README e gauntlet3/aprendizajes/visual.md): MediaPipe só ve mans medianas ou
grandes; Florence describe ben obxectos e materiais pero non conta dedos; a lista de palabras é conservadora e dá falsos positivos (unha rexeneración máis).
"""
import math, os, re
from pathlib import Path

MODELOS = Path(os.environ.get('REVISOR_DIR', '/tmp/claude-0/-home-user-revolta/2e7d1051-da1e-54e9-bb2d-6cd0b746c55a/scratchpad/revisor'))
FLORENCE = os.environ.get('REVISOR_VLM', 'florence-community/Florence-2-large')
CLIP_MODEL = os.environ.get('CLIP_MODEL', 'openai/clip-vit-large-patch14')
MAN_DIST = 0.14
CORPOS_MAX = 5
VERSION = 5   # súbese cando cambia a lista ou as portas; imaxes.py volve revisar as imaxes gardadas cunha versión anterior

# (etiqueta, expresión regular sobre a descrición en inglés e os obxectos de <OD>)
LISTA = [
    # as vidreiras das igrexas góticas si son de época: "stained glass" non conta
    ('xanelas de vidro', r'(?<!stained )\bglass (window|pane)s?\b|\bwindow ?panes?\b|\bglazed\b'),
    ('balcóns', r'\bbalcon(y|ies)\b'),
    ('tellados laranxas', r'\b(red|orange|terracotta|clay)[- ]?(tiled? )?roofs?\b|\broof tiles\b|\btiled roofs?\b'),
    ('vehículos modernos', r'\b(car|cars|truck|bus|bicycle|motorcycle|train|airplane|traffic light)\b'),
    ('obxectos modernos', r'\b(street ?lamps?|lamp ?posts?|power lines?|telephone|umbrella|glasses|sunglasses|'
                          r'asphalt|electric|light bulbs?|plastic|laptop|cell phone|clock|tv|television)\b'),
    # versión 5: "lamp" só con adxectivos modernos (o candil, "oil lamp", é a luz da fase calma)
    ('interior moderno', r'\b(bedroom|nightstand|bedside|(table|floor|desk|bedside|electric) lamps?|lampshades?|curtains?|sofa|couch|picture frames?|pillows)\b'),
    ('texto na imaxe', r'\b(text|letters?|words?|writing|written|sign that reads|watermark|logo|caption|signature)\b'),
    ('cruces portadas', r'\b(carrying|holding|with) (large |wooden )?(crosses|a cross|crucifix(es)?)\b'),
    ('armas', r'\b(guns?|rifles?|muskets?|pistols?|cannons?|swords? drawn)\b'),
    ('violencia', r'\b(blood|bloody|corpses?|dead bod(y|ies)|burning (building|house|castle|village|keep|tower|fortress)s?|flames engulf)'),
    ('morte', r'\b(skeletons?|skulls?|bones|corpses?|dead)\b'),
    # ronda 3: multitudes clónicas e exércitos (o crítico visual: "multitudes clónicas y recargadas")
    # versión 5: sen "procession" (unha Santa Compaña de 3-4 figuras é lexítima); os corpos cóntaos MediaPipe (CORPOS_MAX)
    ('multitude', r'\b(crowds?|large group|big group|army|armies|soldiers|knights|many people|multitude|throng)\b'),
    # versión 5: unha fogueira pequena e afastada (San Xoán) xa non falla; si as grandes e o que arde
    ('lume grande no exterior', r'\b(large|big|huge|raging|massive) (fire|bonfire|blaze)s?\b|\bon fire\b|\bengulfed\b',
     r'\b(fireplace|hearth|stove|oven|pot|cauldron|kitchen)\b'),     # 3.º: excepción (o lume da lareira é interior)
    # versión 5 (Gauntlet 3): iconografía non galega que o crítico viu (ciprés toscanos, rodas de raios, fachadas
    # mediterráneas). "olive" só con árbores (Florence di "olive green"), "palm" só con árbores (a palma da man).
    ('iconografía mediterránea', r'\b(cypress(es)?|olive (trees?|groves?|orchards?)|palm trees?|eucalyptus|'
                                 r'whitewashed|white-washed|stucco|mediterranean|tuscan|tuscany|adobe|cactus|cacti|agave|'
                                 r'spoked|spokes|vineyard rows)\b'),
]

# ------------------------------------------------------------------ CLIP: iconografía, repetición e arquetipos
# (etiqueta, concepto malo, equivalente galego). Os textos van en inglés (CLIP adestrouse en inglés).
PARES = [
    ('tellados laranxas (CLIP)', 'houses with red-orange terracotta clay tile roofs', 'houses with dark grey slate roofs'),
    ('muros encalados (CLIP)', 'white-washed white plastered houses of a Mediterranean village',
     'grey granite stone houses of a rainy Atlantic village'),
    ('ciprés (CLIP)', 'tall narrow dark green cypress trees', 'broad round oak and chestnut trees'),
    ('oliveiras (CLIP)', 'an olive grove with silvery olive trees on dry soil', 'green meadows with oak trees'),
    ('palmeiras (CLIP)', 'palm trees', 'oak trees'),
    ('rodas de raios (CLIP)', 'a cart with spoked wooden wheels', 'an ox cart with solid wooden disc wheels'),
    ('paisaxe seca (CLIP)', 'a dry sunburnt Mediterranean landscape with yellow grass',
     'a green rainy Atlantic landscape with moss'),
    ('eucaliptos (CLIP)', 'a eucalyptus plantation with tall straight pale peeling trunks',
     'an old oak forest with thick gnarled mossy trunks'),
]
# Umbrais por par (calibrados en probas/visual_calibrar_clip.py: imaxes boas e malas da ronda 3 do Gauntlet 2 e das
# probas do Gauntlet 3): marxe = sim(malo) - sim(bo) no peor recorte; pertinencia = máx(sim(malo), sim(bo)).
PAR_MARXE = {'tellados laranxas (CLIP)': 0.020, 'muros encalados (CLIP)': 0.030, 'ciprés (CLIP)': 0.025,
             'oliveiras (CLIP)': 0.030, 'palmeiras (CLIP)': 0.030, 'rodas de raios (CLIP)': 0.020,
             'paisaxe seca (CLIP)': 0.030, 'eucaliptos (CLIP)': 0.030}
PAR_PERTINENCIA = 0.20
NEGATIVO_SIM = 0.26          # conceptos do campo `negativo`: sim("a photo with X") por riba disto = presente
SIM_CLIP = 0.92              # repetición: similitude coseno co embedding dalgunha imaxe aceptada do episodio
# Arquetipos de composición: (etiqueta, texto, fracción máxima do episodio). Tope = máx(1, ceil(fracción x planos)).
ARQUETIPOS = [
    ('camiñantes de costas', 'people in long cloaks seen from behind walking away along a path', 0.03),
    ('castelo no outeiro', 'a distant castle on a hill in a wide landscape', 0.03),
    ('grupo de pé', 'a group of several people standing together in a row', 0.04),
    ('rúa da aldea', 'a street of a stone village with a few people', 0.05),
    ('persoa á lareira', 'a person sitting by a fire in a dark room', 0.06),
    ('bosque con néboa', 'a misty forest with no people', 0.06),
    ('mans en primeiro plano', 'a close-up of hands doing a task', 0.06),
    ('retrato', 'a close-up portrait of a face', 0.08),
]
ARQ_SIM = 0.24               # sim mínima co texto do arquetipo para contalo
ARQ_ESPAZO = 5               # dous planos do mesmo arquetipo, polo menos a 5 planos de distancia


class Clip:
    """CLIP ViT-L/14 en CPU (fp32). Embeddings normalizados de tres recortes cadrados e da súa media."""

    def __init__(self, nth=None):
        import torch
        from transformers import CLIPModel, CLIPProcessor
        if nth:
            torch.set_num_threads(nth)
        self.torch = torch
        self.m = CLIPModel.from_pretrained(CLIP_MODEL, torch_dtype=torch.float32).eval()
        self.proc = CLIPProcessor.from_pretrained(CLIP_MODEL)
        self._txt = {}

    def textos(self, lista):
        import numpy as np
        faltan = [t for t in dict.fromkeys(lista) if t not in self._txt]
        if faltan:
            with self.torch.no_grad():
                e = self.m.get_text_features(**self.proc(text=faltan, return_tensors='pt', padding=True))
            e = (e / e.norm(dim=-1, keepdim=True)).numpy()
            self._txt.update(zip(faltan, e))
        return np.stack([self._txt[t] for t in lista])

    def analizar(self, png):
        """(E: embeddings dos 3 recortes [3, 768], emb: media normalizada [768])."""
        import numpy as np
        from PIL import Image
        im = Image.open(png).convert('RGB')
        w, h = im.size
        s = min(w, h)
        xs = [0, (w - s) // 2, w - s] if w >= h else [0]
        ys = [0] if w >= h else [0, (h - s) // 2, h - s]
        rec = [im.crop((x, y, x + s, y + s)) for x in xs for y in ys]
        with self.torch.no_grad():
            e = self.m.get_image_features(**self.proc(images=rec, return_tensors='pt'))
        E = (e / e.norm(dim=-1, keepdim=True)).numpy()
        m = E.mean(0)
        return E, m / (np.linalg.norm(m) + 1e-9)

    def imaxe(self, png):
        return self.analizar(png)[1]

    def iconografia(self, E, negativo=None):
        """Problemas de iconografía (pares malo/bo e conceptos do campo `negativo`) e o detalle das medidas."""
        problemas, det = [], {}
        T = self.textos([t for _, a, b in PARES for t in (a, b)])
        for k, (et, _, _) in enumerate(PARES):
            sb, sg = E @ T[2 * k], E @ T[2 * k + 1]
            marxe, pert = float((sb - sg).max()), float(max(sb.max(), sg.max()))
            det[et] = [round(marxe, 3), round(pert, 3)]
            if marxe > PAR_MARXE[et] and pert > PAR_PERTINENCIA:
                problemas.append(et)
        for x in _lista_negativo(negativo):
            s = float((E @ self.textos([f'a photo with {x}'])[0]).max())
            det[f'negativo: {x}'] = round(s, 3)
            if s > NEGATIVO_SIM:
                problemas.append(f'negativo do plano: {x} (CLIP)')
        return problemas, det

    def arquetipo(self, emb):
        """Arquetipo de composición máis parecido (ou None se ningún pasa de ARQ_SIM)."""
        T = self.textos([t for _, t, _ in ARQUETIPOS])
        s = T @ emb
        k = int(s.argmax())
        if s[k] < ARQ_SIM:
            return None
        return {'etiqueta': ARQUETIPOS[k][0], 'sim': round(float(s[k]), 3)}


def _lista_negativo(negativo):
    if not negativo:
        return []
    if isinstance(negativo, str):
        negativo = re.split(r'[,;]', negativo)
    return [x.strip() for x in negativo if x and x.strip()][:6]


def repeticion(emb, aceptadas, arquetipos, arq, n_total=None):
    """Porta de repetición contra todas as imaxes aceptadas do episodio e tope de arquetipos.
    aceptadas: embeddings de CLIP das imaxes escollidas dos planos anteriores; arquetipos: os seus arquetipos."""
    import numpy as np
    pr = []
    if aceptadas:
        sims = np.stack(aceptadas) @ emb
        j = int(sims.argmax())
        if sims[j] > SIM_CLIP:
            pr.append(f'repetida (CLIP {sims[j]:.2f} co plano {j})')
    if arq:
        et = arq['etiqueta']
        prev = [k for k, a in enumerate(arquetipos) if a and a['etiqueta'] == et]
        frac = {e: f for e, _, f in ARQUETIPOS}[et]
        tope = max(1, math.ceil(frac * (n_total or len(arquetipos) + 1)))
        if len(prev) >= tope:
            pr.append(f'arquetipo repetido: {et} ({len(prev)} xa, tope {tope})')
        elif prev and len(arquetipos) - prev[-1] < ARQ_ESPAZO:
            pr.append(f'arquetipo seguido: {et} (xa no plano {prev[-1]})')
    return pr


class Revisor:
    def __init__(self, vlm=True, nth=None, clip=True):
        import mediapipe as mp
        from mediapipe.tasks.python import vision, BaseOptions
        self.mp = mp
        self.hands = vision.HandLandmarker.create_from_options(vision.HandLandmarkerOptions(
            base_options=BaseOptions(model_asset_path=str(MODELOS / 'hand_landmarker.task')), num_hands=8,
            min_hand_detection_confidence=0.35, min_hand_presence_confidence=0.35))
        self.pose = vision.PoseLandmarker.create_from_options(vision.PoseLandmarkerOptions(
            base_options=BaseOptions(model_asset_path=str(MODELOS / 'pose_landmarker_full.task')), num_poses=8,
            min_pose_detection_confidence=0.3))
        self.vlm = None
        if vlm:
            import torch
            from transformers import AutoProcessor, Florence2ForConditionalGeneration
            if nth:
                torch.set_num_threads(nth)
            self.torch = torch
            self.vlm = Florence2ForConditionalGeneration.from_pretrained(FLORENCE, torch_dtype=torch.float32).eval()
            self.proc = AutoProcessor.from_pretrained(FLORENCE)
        self.clip = Clip(nth) if clip else None

    def _florence(self, im, task, max_new=120):
        inp = self.proc(text=task, images=im, return_tensors='pt')
        with self.torch.no_grad():
            ids = self.vlm.generate(**inp, max_new_tokens=max_new, num_beams=1, do_sample=False)
        txt = self.proc.batch_decode(ids, skip_special_tokens=False)[0]
        return self.proc.post_process_generation(txt, task=task, image_size=im.size)[task]

    def mans(self, png):
        im = self.mp.Image.create_from_file(str(png))
        asp = im.width / im.height
        h = self.hands.detect(im); p = self.pose.detect(im)
        pulsos = [(l[i].x * asp, l[i].y) for l in p.pose_landmarks for i in (15, 16)]
        mans = []
        for lm, hd in zip(h.hand_landmarks, h.handedness):
            w = (lm[0].x * asp, lm[0].y)
            d = min((((w[0] - q[0]) ** 2 + (w[1] - q[1]) ** 2) ** 0.5 for q in pulsos), default=9.0)
            mans.append({'pulso': [round(lm[0].x, 3), round(lm[0].y, 3)], 'confianza': round(hd[0].score, 2),
                         'dist_corpo': round(d, 3)})
        problemas = []
        orfas = [m for m in mans if m['dist_corpo'] > MAN_DIST]
        if orfas:
            problemas.append(f'man sen corpo ({len(orfas)})')
        if p.pose_landmarks and len(mans) > 2 * len(p.pose_landmarks):
            problemas.append(f'{len(mans)} mans para {len(p.pose_landmarks)} corpos')
        if len(p.pose_landmarks) > CORPOS_MAX:
            problemas.append(f'multitude ({len(p.pose_landmarks)} corpos)')
        return problemas, {'mans': mans, 'corpos': len(p.pose_landmarks)}

    def anacronismos(self, png):
        from PIL import Image
        im = Image.open(png).convert('RGB')
        cap = self._florence(im, '<MORE_DETAILED_CAPTION>')
        od = self._florence(im, '<OD>', 80)
        obx = sorted(set(od.get('labels', [])))
        texto = (cap + ' | ' + ', '.join(obx)).lower()
        problemas = [et for et, rx, *exc in LISTA if re.search(rx, texto) and not (exc and re.search(exc[0], texto))]
        return problemas, {'descricion': cap, 'obxectos': obx}

    def revisar(self, png, negativo=None, **_):
        """{'ok', 'problemas', 'mans', 'corpos', 'descricion', 'obxectos', 'iconografia', 'arquetipo', 'clip_emb'}.
        A repetición non se mira aquí (depende do episodio): ver `repeticion`."""
        pr, det = self.mans(png)
        if self.vlm is not None:
            p2, d2 = self.anacronismos(png)
            pr += p2; det.update(d2)
        if self.clip is not None:
            E, emb = self.clip.analizar(png)
            p3, d3 = self.clip.iconografia(E, negativo)
            pr += [x for x in p3 if x not in pr]
            det.update({'iconografia': d3, 'arquetipo': self.clip.arquetipo(emb), 'clip_emb': emb})
        return {'ok': not pr, 'problemas': pr, **det}

    def repeticion(self, emb, aceptadas, arquetipos, arq, n_total=None):
        return repeticion(emb, aceptadas, arquetipos, arq, n_total)


if __name__ == '__main__':   # python revisor.py IMAXE.png [...]  -> JSON por imaxe
    import json, sys
    r = Revisor()
    for f in sys.argv[1:]:
        res = r.revisar(f); res.pop('clip_emb', None)
        print(json.dumps({'imaxe': Path(f).name, **res}, ensure_ascii=False), flush=True)
