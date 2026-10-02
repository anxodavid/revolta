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
MAN_DETALLE = 0.12   # sen corpos na imaxe, unha man máis ancha ca isto (fracción do ancho) é un primeiro plano
CORPOS_MAX = 5
VERSION = 8   # súbese cando cambia a lista ou as portas; imaxes.py volve revisar as imaxes gardadas cunha versión anterior

# (etiqueta, expresión regular sobre a descrición en inglés e os obxectos de <OD>)
LISTA = [
    # as vidreiras das igrexas góticas si son de época: "stained glass" non conta
    ('xanelas de vidro', r'(?<!stained )\bglass (window|pane)s?\b|\bwindow ?panes?\b|\bglazed\b'),
    ('balcóns', r'\bbalcon(y|ies)\b'),
    ('tellados laranxas', r'\b(red|orange|terracotta|clay)[- ]?(tiled? )?roofs?\b|\broof tiles\b|\btiled roofs?\b'),
    ('vehículos modernos', r'\b(car|cars|truck|bus|bicycle|motorcycle|train|airplane|traffic light)\b'),
    ('obxectos modernos', r'\b(street ?lamps?|lamp ?posts?|streetlights?|street lights?|lanterns? hanging|hanging lanterns?|'
                          r'city lights?|town lights?|tea ?lights?|glass jar|jar candle|sliced bread|slices? of bread|'
                          r'kettle|teapot|coffee pot|feather boa|power lines?|telephone|umbrella|glasses|sunglasses|'
                          r'asphalt|electric|light bulbs?|plastic|laptop|cell phone|clock|tv|television|'
                          # tribunal final do Gauntlet 3 (01-10-2026): o que se escapou e Florence si nomeara. Engadido sen
                          # subir VERSION a propósito: só o ven os planos que se rexeneran, non as 151 imaxes xa aprobadas
                          r'radiators?|sinks?|faucets?|water taps?|rolling suitcases?|suitcases? on wheels|wheeled suitcases?|'
                          r'trolley|briefcases?|handbags?|teddy bears?|beanies?|bowler hats?|cowboy hats?|light poles?|'
                          r'wall lamps?|wall lights?|sconces?|porch lights?|ceiling lights?)\b'),
    # versión 5: "lamp" só con adxectivos modernos (o candil, "oil lamp", é a luz da fase calma)
    ('interior moderno', r'\b(bedroom|nightstand|bedside|(table|floor|desk|bedside|electric) lamps?|lampshades?|curtains?|sofa|couch|'
                         r'picture frames?|pillows|cushions?|upholstered|armchairs?|window seat|mantel(piece)?|potted plants?|'
                         r'flower ?pots?|vase of flowers|large window|view from the window)\b'),
    ('texto na imaxe', r'\b(text|letters?|words?|writing|written|sign that reads|watermark|logo|caption|signature|'
                       r'open book|book open|pages of|document|newspaper)\b'),
    ('cruces portadas', r'\b(carrying|holding|with) (large |wooden )?(crosses|a cross|crucifix(es)?)\b'),
    ('armas', r'\b(guns?|rifles?|muskets?|pistols?|cannons?|swords? drawn)\b'),
    ('violencia', r'\b(blood|bloody|corpses?|dead bod(y|ies)|burning (building|house|castle|village|keep|tower|fortress)s?|flames engulf)'),
    ('morte', r'\b(skeletons?|skulls?|bones|corpses?|dead)\b'),
    # ronda 3: multitudes clónicas e exércitos (o crítico visual: "multitudes clónicas y recargadas")
    # versión 5: sen "procession" (unha Santa Compaña de 3-4 figuras é lexítima); os corpos cóntaos MediaPipe (CORPOS_MAX)
    ('multitude', r'\b(crowds?|large group|big group|army|armies|soldiers|knights|many people|multitude|throng)\b'),
    # versión 5: unha fogueira pequena e afastada (San Xoán) xa non falla; si as grandes e o que arde
    ('lume grande no exterior', r'\b(large|big|huge|raging|massive) (fire|bonfire|blaze)s?\b|\bon fire\b|\bengulfed\b|'
                                r'\bcampfire\b|\bburning brightly\b',
     r'\b(fireplace|hearth|stove|oven|kitchen)\b'),     # 3.º: excepción (o lume da lareira é interior; o caldeiro xa non)
    # versión 6 (veredicto visual-r1): clichés de meiga e animais en grupo
    ('clichés de meiga', r'\b(potion|witch(es|craft)?|broom(stick)?s?|pointed hat|spell ?books?|casting a spell|crystal ball|'
                         r'cauldron with (a )?(glowing|bubbling|red|green)|(glowing|bubbling) (liquid|potion))\b'),
    ('animais en grupo', r'\b(three|four|five|six|several|many|a herd of|a group of) (cows|oxen|cattle|bulls|sheep|goats|horses|'
                         r'cats|dogs)\b'),
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
    # versión 6 (veredicto visual-r1 §4.2): luz eléctrica e interiores e casas alleas que Florence non nomeou
    ('luz eléctrica (CLIP)', 'a street at night lit by rows of electric street lamps',
     'a dark lane at night lit only by a hand-held lantern'),
    ('luces de cidade (CLIP)', 'city lights glowing in a valley at night', 'dark hills at night with no lights'),
    ('salón moderno (CLIP)', 'a cozy living room with cushions and a fireplace with a mantelpiece',
     'a smoke-blackened peasant kitchen with an open stone hearth at floor level'),
    ('patio mediterráneo (CLIP)', 'an arcaded courtyard with potted plants and hanging lanterns',
     'a granite village fountain with a stone trough'),
    ('casas británicas (CLIP)', 'English stone cottages with gable chimneys and sash windows',
     'low granite houses with small openings and slate roofs'),
    ('caldeiro de meiga (CLIP)', "a witch's cauldron with a glowing potion",
     'an iron cooking pot over embers in a peasant hearth'),
]
# Umbrais por par, calibrados o 30-09-2026 con probas/visual_calibrar_clip.py (72 imaxes etiquetadas por Claude:
# 33 fotogramas das rondas 1-3 do Gauntlet 2, 32 da comparativa de modelos e 7 escenas alleas feitas adrede):
# marxe = sim(malo) - sim(bo) no peor recorte; pertinencia = máx(sim(malo), sim(bo)). Con estes valores, 0 falsos
# positivos no conxunto; collen os casos claros (Toscana, Andalucía, oliveiras, palmeiras, eucaliptos, paisaxe seca)
# pero NON os tellados laranxas e os ciprés apagados polo lavado verde da ronda 3 (neses, CLIP puntúa máis "lousa"):
# eses quedan para Florence-2. Poucas imaxes malas por par (1-8): son provisionais.
PAR_MARXE = {'tellados laranxas (CLIP)': 0.045, 'muros encalados (CLIP)': 0.060, 'ciprés (CLIP)': 0.060,
             'oliveiras (CLIP)': 0.040, 'palmeiras (CLIP)': 0.020,
             'rodas de raios (CLIP)': 9.0,    # DESACTIVADO: o par estaba invertido; as rodas quedan para Florence ("spoked")
             'paisaxe seca (CLIP)': 0.072, 'eucaliptos (CLIP)': 0.070,
             # versión 6, calibrados con probas/visual_calibrar_r2.py sobre a folla r1 (1-6 malas por par: provisionais).
             # Patio e caldeiro saen INVERTIDOS nas imaxes da r1 (o patio puntúa máis "fonte con pía"; o caldeiro, "pota
             # sobre brasas"): desactivados; deses encárgase Florence ("potted plants", "potion"...).
             'luz eléctrica (CLIP)': 0.015, 'luces de cidade (CLIP)': 0.012, 'salón moderno (CLIP)': 0.015,
             'patio mediterráneo (CLIP)': 9.0, 'casas británicas (CLIP)': 0.010, 'caldeiro de meiga (CLIP)': 9.0}
PAR_PERTINENCIA = 0.15       # (0,20 deixaba fóra a maioría das malas: as similitudes de CLIP-L andan en 0,08-0,30)
# Conceptos do campo `negativo`: sim("a photo with X") − sim("a photo") no mesmo recorte. Na calibración, as boas
# chegan a 0,037 e as malas claras a 0,047-0,12 (o valor absoluto non separaba: boas ata 0,19, malas desde 0,09).
NEGATIVO_MARXE = 0.040
# Versión 6: campo `clave` (o que TEN que verse): sim("a photo with X") − sim("a photo") no mellor recorte, por riba
# de CLAVE_MARXE. Calibrado coas imaxes da folla r1 (ver aprendizajes/visual.md).
CLAVE_MARXE = 0.020   # r1: colle 7 dos 12 elementos que faltaban, cunha falsa alarma (unha vela, -0,011)
# Versión 6: na fase de durmir, nada de lume vivo: fracción de píxeles con luminancia > 0,85 (as brasas quedan
# por debaixo; as chamas amarelas, por riba). Na r1: o caldeiro con chamas do plano 16 daba 0,97 %.
ALTAS_LUCES_DURMIR = 0.0012   # r1: fogueira 0,36 %, caldeiro 2,2 %, vela 0,15-1,4 %; lúa e néboa 0,03-0,10 %
# Versión 7 (orquestador, tras a folla r2): a fracción de altas luces daba falsos positivos ao durmir (flores amarelas
# xunto a unha xanela 0,27-0,98 %, a lúa 0,29 %) e 15 rexeneracións inútiles. Agora só contan as altas luces COR DE
# CHAMA (laranxa: R >= 0,80, 0,25 <= G <= 0,85, B <= 0,45, R-G >= 0,12). Medido: flores e lúa 0,00 %; lareira con
# chamas 1,1 %; queimada 6,0 %; fogueira de r1 0,33 %; vela nun bodegón 0,40 %; brasas (máis escuras) por debaixo.
# REVISOR_LUME_DURMIR: na produción do 01-10-2026 o 0,25 % rexeitaba velas e brasas (0,3-0,9 %) en todos os intentos
# dos planos de lareira da zona de durmir; 1,5 % segue parando os lumes grandes (6-10 %)
LUME_DURMIR = float(os.environ.get('REVISOR_LUME_DURMIR', '0.0025'))
# Repetición: coseno dos embeddings medios. Na calibración, prompts distintos ata 0,879 (p99 0,866); o mesmo prompt
# noutro modelo ou estilo, mediana 0,864 (p10 0,80). 0,90: só as imaxes case iguais en contido e composición.
SIM_CLIP = 0.90
# Arquetipos de composición: (etiqueta, texto, fracción máxima do episodio, sim mínima co texto). Tope =
# máx(1, ceil(fracción x planos)). Umbrais da calibración (as similitudes texto-imaxe de CLIP son baixas, 0,15-0,26):
# camiñantes de costas 6/6 con 0 falsos (a máis alta sen eles, 0,217); lareira 0,205 colle tamén as lareiras sen
# persoa (mesmo arquetipo visual); o do retrato non ten datos [S].
ARQUETIPOS = [   # (etiqueta, textos, fracción máxima, sim mínima); a sim é a máxima entre os textos
    ('camiñantes de costas', ['people in long cloaks seen from behind walking away along a path',
                              'a lone person seen from behind walking away along a path or street'], 0.03, 0.202),
    ('castelo no outeiro', ['a distant castle on a hill in a wide landscape'], 0.03, 0.225),
    ('grupo de pé', ['a group of several people standing together in a row'], 0.04, 0.195),
    ('rúa da aldea', ['a street of a stone village with a few people'], 0.05, 0.240),
    # versión 6: texto máis estreito, e só conta se o prompt nomea lume (unha vela non é unha lareira: visual-r1 §4.5)
    ('persoa á lareira', ['a person sitting beside an open hearth fire'], 0.06, 0.240),
    ('bosque con néboa', ['a misty forest with no people'], 0.06, 0.210),
    ('mans en primeiro plano', ['a close-up of hands doing a task'], 0.06, 0.180),
    ('retrato', ['a close-up portrait of a face'], 0.08, 0.220),
]
ARQ_CONDICION = {'persoa á lareira': r'\b(fire|hearth|fireplace|embers?|flames?|firelight)\b'}
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
        base = E @ self.textos(['a photo'])[0]
        for x in _lista_negativo(negativo):
            s = float((E @ self.textos([f'a photo with {x}'])[0] - base).max())
            det[f'negativo: {x}'] = round(s, 3)
            if s > NEGATIVO_MARXE:
                problemas.append(f'negativo do plano: {x} (CLIP)')
        return problemas, det

    def clave(self, E, clave=None):
        """O que o plano TEN que mostrar (campo `clave`, 1-3 conceptos): falla se ningún recorte o amosa."""
        problemas, det = [], {}
        base = E @ self.textos(['a photo'])[0]
        for x in _lista_negativo(clave):
            s = float((E @ self.textos([f'a photo with {x}'])[0] - base).max())
            det[f'clave: {x}'] = round(s, 3)
            if s < CLAVE_MARXE:
                problemas.append(f'falta: {x} (CLIP)')
        return problemas, det

    def arquetipo(self, emb, prompt=None):
        """Arquetipo de composición: o que máis supera o seu umbral (ou None se ningún o pasa). Os arquetipos con
        condición (ARQ_CONDICION) só contan se o prompt a cumpre."""
        mellor = None
        for et, textos, _, umbral in ARQUETIPOS:
            if et in ARQ_CONDICION and prompt is not None and not re.search(ARQ_CONDICION[et], prompt, re.I):
                continue
            sim = float((self.textos(textos) @ emb).max())
            if sim >= umbral and (mellor is None or sim - umbral > mellor[0]):
                mellor = (sim - umbral, et, sim)
        if mellor is None:
            return None
        return {'etiqueta': mellor[1], 'sim': round(mellor[2], 3)}


def _lista_negativo(negativo):
    if not negativo:
        return []
    if isinstance(negativo, str):
        negativo = re.split(r'[,;]', negativo)
    return [x.strip() for x in negativo if x and x.strip()][:6]


def lume_quente(png):
    """Fracción de píxeles cor de chama (laranxa brillante): o lume vivo, non a lúa nin unha xanela."""
    import numpy as np
    from PIL import Image
    a = np.asarray(Image.open(png).convert('RGB').resize((672, 384)), np.float32) / 255
    R, G, B = a[..., 0], a[..., 1], a[..., 2]
    return float(((R >= 0.80) & (G >= 0.25) & (G <= 0.85) & (B <= 0.45) & ((R - G) >= 0.12)).mean())


def altas_luces(png, umbral=0.85):
    """Fracción de píxeles con luminancia (sRGB, 0-1) por riba de `umbral`: chamas vivas, ceos brillantes."""
    import numpy as np
    from PIL import Image
    x = np.asarray(Image.open(png).convert('RGB').resize((448, 256)), np.float32) / 255
    return float(((x @ np.array([0.2126, 0.7152, 0.0722], np.float32)) > umbral).mean())


def repeticion(emb, aceptadas, arquetipos, arq, n_total=None):
    """Porta de repetición contra todas as imaxes aceptadas do episodio e tope de arquetipos.
    aceptadas: embeddings de CLIP das imaxes escollidas dos planos anteriores; arquetipos: os seus arquetipos."""
    import numpy as np
    pr = []
    if aceptadas:
        sims = np.stack(aceptadas) @ emb
        j = int(sims.argmax())
        if sims[j] > SIM_CLIP:
            pr.append(f'repetida (CLIP {sims[j]:.2f} co plano {j + 1})')
    if arq:
        et = arq['etiqueta']
        prev = [k for k, a in enumerate(arquetipos) if a and a['etiqueta'] == et]
        frac = {e: f for e, _, f, _ in ARQUETIPOS}[et]
        tope = max(1, math.ceil(frac * (n_total or len(arquetipos) + 1)))
        if len(prev) >= tope:
            pr.append(f'arquetipo repetido: {et} ({len(prev)} xa, tope {tope})')
        elif prev and len(arquetipos) - prev[-1] < ARQ_ESPAZO:
            pr.append(f'arquetipo seguido: {et} (xa no plano {prev[-1] + 1})')
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
                         'dist_corpo': round(d, 3), 'tamaño': round(max(q.x for q in lm) - min(q.x for q in lm), 3)})
        problemas = []
        # Gauntlet 3: nun primeiro plano de mans non hai corpo que detectar; unha man grande sen ningún corpo na imaxe
        # é un detalle (a biblia pídeos), non unha man solta. Sen corpos, só falla unha man pequena ou máis de dúas.
        if p.pose_landmarks:
            orfas = [m for m in mans if m['dist_corpo'] > MAN_DIST]
        else:
            orfas = [m for m in mans if m['tamaño'] < MAN_DETALLE]
            if len(mans) > 2:
                problemas.append(f'{len(mans)} mans sen corpo')
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

    def revisar(self, png, negativo=None, clave=None, fase=None, prompt=None, **_):
        """{'ok', 'problemas', 'mans', 'corpos', 'descricion', 'obxectos', 'iconografia', 'arquetipo', 'clip_emb',
        'altas_luces'}. A repetición non se mira aquí (depende do episodio): ver `repeticion`."""
        pr, det = self.mans(png)
        luces = altas_luces(png)
        det['altas_luces'] = round(luces, 4)
        quente = lume_quente(png)
        det['lume_quente'] = round(quente, 4)
        if fase == 'durmir' and quente > LUME_DURMIR:
            pr.append(f'lume vivo ao durmir ({quente:.1%} de altas luces cor de chama)')
        if self.vlm is not None:
            p2, d2 = self.anacronismos(png)
            # Versión 8 (orquestador): o veto de lume grande veu do Gauntlet 2 (edificios ardendo). Neste episodio o lume
            # é o tema (a queimada, as fogueiras de San Xoán): se o prompt pide lume, non se veta; o de durmir segue.
            if prompt and re.search(r'\b(fire|flames?|bonfires?|blaze|queimada|burning)\b', prompt, re.I):
                p2 = [x for x in p2 if x != 'lume grande no exterior']
            pr += p2; det.update(d2)
        if self.clip is not None:
            E, emb = self.clip.analizar(png)
            p3, d3 = self.clip.iconografia(E, negativo)
            p4, d4 = self.clip.clave(E, clave)
            pr += [x for x in p3 + p4 if x not in pr]
            det.update({'iconografia': {**d3, **d4}, 'arquetipo': self.clip.arquetipo(emb, prompt), 'clip_emb': emb})
        return {'ok': not pr, 'problemas': pr, **det}

    def repeticion(self, emb, aceptadas, arquetipos, arq, n_total=None):
        return repeticion(emb, aceptadas, arquetipos, arq, n_total)


if __name__ == '__main__':   # python revisor.py IMAXE.png [...]  -> JSON por imaxe
    import json, sys
    r = Revisor()
    for f in sys.argv[1:]:
        res = r.revisar(f); res.pop('clip_emb', None)
        print(json.dumps({'imaxe': Path(f).name, **res}, ensure_ascii=False), flush=True)
