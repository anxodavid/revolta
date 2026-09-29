"""Porta automática de imaxes: revisa cada imaxe xerada e, se falla, a etapa IMAXES rexenera con outra semente.

Dous revisores abertos, en CPU:

1. Anatomía das mans (MediaPipe Tasks, Apache-2.0: hand_landmarker + pose_landmarker_full).
   - "man sen corpo": unha man detectada cuxo pulso non está preto (distancia normalizada > MAN_DIST) do
     pulso de ningún corpo detectado. É o defecto do plano final da ronda 1 (catro mans, un par sen brazo).
   - "máis de dúas mans por corpo": mans > 2 x corpos (cando hai corpos).
2. Lista de anacronismos e contidos vetados sobre a descrición e os obxectos que ve un modelo visión-linguaxe
   aberto (Florence-2-large, MIT): <MORE_DETAILED_CAPTION> + <OD>. Se a descrición ou os obxectos
   conteñen algo da lista (xanelas de vidro, balcóns, tellados laranxas, coches, texto, cruces
   portadas, armas de fogo, sangue...) a imaxe falla.

Limitacións (medidas na proba con 15 imaxes da ronda 1, ver README): MediaPipe só ve mans medianas ou
grandes (as mans pequenas dunha multitude non se revisan, pero tampouco se notan); Florence describe
ben obxectos e materiais pero non conta dedos; a lista de palabras é conservadora e dá falsos positivos
(que só custan unha rexeneración, uns 16 s).
"""
import os, re
from pathlib import Path

MODELOS = Path(os.environ.get('REVISOR_DIR', '/tmp/claude-0/-home-user-revolta/2e7d1051-da1e-54e9-bb2d-6cd0b746c55a/scratchpad/revisor'))
FLORENCE = os.environ.get('REVISOR_VLM', 'florence-community/Florence-2-large')
MAN_DIST = 0.14

# (etiqueta, expresión regular sobre a descrición en inglés e os obxectos de <OD>)
LISTA = [
    # as vidreiras das igrexas góticas si son de época: "stained glass" non conta
    ('xanelas de vidro', r'(?<!stained )\bglass (window|pane)s?\b|\bwindow ?panes?\b|\bglazed\b'),
    ('balcóns', r'\bbalcon(y|ies)\b'),
    ('tellados laranxas', r'\b(red|orange|terracotta|clay)[- ]?(tiled? )?roofs?\b|\broof tiles\b|\btiled roofs?\b'),
    ('vehículos modernos', r'\b(car|cars|truck|bus|bicycle|motorcycle|train|airplane|traffic light)\b'),
    ('obxectos modernos', r'\b(street ?lamps?|lamp ?posts?|power lines?|telephone|umbrella|glasses|sunglasses|'
                          r'asphalt|electric|light bulbs?|plastic|laptop|cell phone|clock|tv|television)\b'),
    ('interior moderno', r'\b(bedroom|nightstand|bedside|lamps?|lampshades?|curtains?|sofa|couch|picture frames?|pillows)\b'),
    ('texto na imaxe', r'\b(text|letters?|words?|writing|written|sign that reads|watermark|logo|caption|signature)\b'),
    ('cruces portadas', r'\b(carrying|holding|with) (large |wooden )?(crosses|a cross|crucifix(es)?)\b'),
    ('armas', r'\b(guns?|rifles?|muskets?|pistols?|cannons?|swords? drawn)\b'),
    ('violencia', r'\b(blood|bloody|corpses?|dead bod(y|ies)|burning (building|house|castle|village)s?|flames engulf)'),
]


class Revisor:
    def __init__(self, vlm=True, nth=None):
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
        return problemas, {'mans': mans, 'corpos': len(p.pose_landmarks)}

    def anacronismos(self, png):
        from PIL import Image
        im = Image.open(png).convert('RGB')
        cap = self._florence(im, '<MORE_DETAILED_CAPTION>')
        od = self._florence(im, '<OD>', 80)
        obx = sorted(set(od.get('labels', [])))
        texto = (cap + ' | ' + ', '.join(obx)).lower()
        problemas = [et for et, rx in LISTA if re.search(rx, texto)]
        return problemas, {'descricion': cap, 'obxectos': obx}

    def revisar(self, png):
        pr, det = self.mans(png)
        if self.vlm is not None:
            p2, d2 = self.anacronismos(png)
            pr += p2; det.update(d2)
        return {'ok': not pr, 'problemas': pr, **det}


if __name__ == '__main__':   # python revisor.py IMAXE.png [...]  -> JSON por imaxe
    import json, sys
    r = Revisor()
    for f in sys.argv[1:]:
        print(json.dumps({'imaxe': Path(f).name, **r.revisar(f)}, ensure_ascii=False), flush=True)
