"""Comprobación rápida (sen modelos pesados) dunha lista de planos escrita por un axente segundo a biblia visual.

    $PY probas/visual_validar_escenas.py ESCENAS.json [--planos TRABALLO/planos.json]

Mira, antes de gastar horas de CPU en imaxes: prompts que pasan de 77 tokens de CLIP co estilo e a luz que engade
imaxes.py (CLIP trunca o resto), palabras vetadas pola biblia (plan-de-negocio/gauntlet3/visual/biblia.md),
arquetipos repetidos por palabras, tipos de plano seguidos, e se cada fase ten luz dabondo. Só avisa: non cambia nada.
Con --planos engade a fase de cada plano (a de longo.py) se a lista non a trae.
"""
import argparse, collections, json, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import imaxes

VETADAS = [   # (motivo, expresión regular): biblia, sección 4 (lista negativa) e 6 (palabras que dan "aspecto IA")
    ('Galicia confunde a SDXL (Galitzia)', r'\bgalicia\w*|\bgalician\b'),
    ('aspecto IA xenérico', r'\b(masterpiece|8k|4k|hdr|trending|artstation|hyper-?detailed|ultra-?realistic|epic|'
                            r'vibrant|neon|fantasy|magical glow|octane|unreal engine)\b'),
    ('iconografía non galega', r'\b(cypress\w*|olive trees?|olive groves?|palm trees?|eucalyptus|whitewash\w*|stucco|'
                               r'terracotta roofs?|orange roofs?|red roofs?|spoked|tuscan|mediterranean|kilt|tartan|'
                               r'druid\w*|pointed hat|broomstick|cauldron bubbling)\b'),
    ('multitude (a porta rexeita)', r'\b(crowds?|army|armies|soldiers|knights|throng|multitude|many people|villagers gathered)\b'),
    ('texto (a porta rexeita)', r'\b(writing|written|letters?|inscription|sign|book pages|open book|map)\b'),
    ('negación (CLIP non a entende)', r'\b(no|without|not)\b'),
]
ARQ_PALABRAS = [   # arquetipos repetidos que o crítico viu, por palabras
    ('camiñantes de costas', r'(seen from behind|from behind|walking away)'),
    ('castelo no outeiro', r'castle on (a|the) hill|distant castle|fortress on a hill'),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('escenas'); ap.add_argument('--planos', default=None)
    a = ap.parse_args()
    from transformers import CLIPTokenizer
    tok = CLIPTokenizer.from_pretrained(imaxes.BASE, subfolder='tokenizer')
    d = json.loads(Path(a.escenas).read_text())
    d = d.get('escenas', d) if isinstance(d, dict) else d
    fases = {}
    if a.planos:
        fases = {p['n']: p['fase'] for p in json.loads(Path(a.planos).read_text())}
    avisos = collections.Counter()
    tipos_prev = None
    arq_pos = collections.defaultdict(list)
    luz_fase = collections.defaultdict(collections.Counter)
    for i, x in enumerate(d):
        e = dict(x, fase=x.get('fase') or fases.get(x.get('n')))
        pr = imaxes.compor_prompt(e, i)
        n = len(tok(pr).input_ids)
        msgs = []
        if n > 77:
            msgs.append(f'{n} tokens: CLIP perde "{tok.decode(tok(pr).input_ids[76:-1])}"')
        for motivo, rx in VETADAS:
            m = re.search(rx, x['prompt'], re.I)
            if m:
                msgs.append(f'{motivo}: "{m.group(0)}"')
        for et, rx in ARQ_PALABRAS:
            if re.search(rx, x['prompt'], re.I):
                arq_pos[et].append(x.get('n', i + 1))
        if x.get('tipo') and x.get('tipo') == tipos_prev and x.get('tipo') != 'paisaxe':
            msgs.append(f"tipo repetido co plano anterior: {x['tipo']}")
        if x.get('tipo') and x['tipo'] not in imaxes.TIPO_FRASE:
            msgs.append(f"tipo descoñecido: {x['tipo']} (válidos: {', '.join(imaxes.TIPO_FRASE)})")
        tipos_prev = x.get('tipo')
        luz = re.findall(imaxes.LUZ_RX, x['prompt'] + ' ' + str(x.get('luz') or ''), re.I)
        luz_fase[e['fase']][luz[0].lower() if luz else '(por defecto)'] += 1
        for m_ in msgs:
            avisos[m_.split(':')[0]] += 1
            print(f"plano {x.get('n', i + 1)}: {m_}")
    tot = len(d)
    for et, pos in arq_pos.items():
        tope = max(1, round(0.03 * tot))
        if len(pos) > tope:
            print(f'arquetipo {et}: {len(pos)} planos (tope {tope}): {pos}')
    print('\nLuces por fase (primeira palabra de luz de cada prompt):')
    for f_, c in luz_fase.items():
        print(f'  {f_}: {dict(c.most_common(8))}')
    print('\nResumo de avisos:', dict(avisos) or 'ningún')


if __name__ == '__main__':
    main()
