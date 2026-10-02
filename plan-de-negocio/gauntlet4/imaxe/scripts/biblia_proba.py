"""Proba da biblia v2 (Gauntlet 4, peza IMAXE): 10 planos da v1 co prompt da v1 e co prompt reescrito segundo
biblia-v2.md, mesmo modelo e mesma semente (só cambia o prompt). Os prompts v2 son de Claude (este axente).

    flock "$CPU_LOCK" $PY biblia_proba.py xerar [n1,n2,...]
    $PY biblia_proba.py folla

Saída: $SCRATCH/imaxe4/biblia/<n>-<v1|v2>.png e biblia.json (tempos); a folla vai a ../biblia-v1-v2.jpg.
"""
import json, os, sys, time
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
sys.path.insert(0, str(REPO / 'herramientas/pipeline'))
OUT = Path(os.environ.get('SCRATCH', '/tmp')) / 'imaxe4' / 'biblia'
V1 = REPO / 'plan-de-negocio/gauntlet3/video/escenas-montadas.json'

V2 = {   # n: prompt v2 (a frase visual en galego, como comentario)
    8: 'close-up of an old midwife\'s hands holding out a pair of worn leather women\'s shoes towards a young man\'s bare '
       'feet on a straw-strewn floor, his hands gripping his knees, lit from the side by the hearth fire, deep black shadows',
       # a parteira calza ao home os zapatos da muller
    16: 'close-up of a stern judge in a black robe and white ruff collar looking down coldly, his hand pressing a brass '
        'seal into red wax on a folded parchment, two tall candles beside him, deep black shadows',
        # un xuíz duro sela a sentenza
    19: 'close-up of an old village woman\'s weathered hands offering a steaming clay bowl of herb infusion to the hands '
        'of a young pregnant woman, dried herbs hanging behind, warm glow of the hearth fire from the side',
        # a menciñeira dálle unha infusión á preñada
    20: 'seen from behind a mossy granite wall at night, the dark head of a man in the foreground peering at three women '
        'in dark wool shawls gathered at a stone fountain with a long trough, one holding a horn lantern, pale moonlight',
        # os veciños espreitan as mulleres na fonte
    26: 'medium shot of a young woman in a dark wool skirt leading two golden-brown cows to drink at a stone trough fed '
        'by a spring, her lips moving as she whispers to them, green hillside, morning sunlight through mist',
        # María do Barro díslle palabras ao gando que bebe
    33: 'medium shot of a village woman sitting on a granite doorstep winding wool yarn into a ball, looking up at a '
        'second woman in a dark shawl who stands before her, rough granite wall with a small shuttered opening, '
        'bright overcast daylight',
        # a veciña debanda á porta cando chega Ana González
    37: 'medium shot of a court bailiff in a black cloak reading aloud from a sealed paper to a middle-aged village woman '
        'who grips her apron with both hands, rough granite wall and a wooden door behind her, bright overcast daylight',
        # a xustiza chega á porta de Marta de Quián
    48: 'medium shot of three friends in 1960s clothes laughing around a small table in the wooden cabin of an old boat, '
        'one lifting a ladle of burning blue spirits over a clay bowl, their faces lit by the blue flames',
        # Mariano e os amigos fan a queimada no barco nos anos sesenta
    84: 'medium shot of an old midwife and her grown daughter side by side at a rough oak table, the mother guiding the '
        'daughter\'s hands as she grinds herbs in a stone mortar, bunches of dried herbs hanging, soft light from a small '
        'window on the left, bare granite walls',
        # a nai ensínalle o oficio á filla
    92: 'wide shot of a smoke-blackened room with an open stone hearth at floor level, a family eating from one clay pot '
        'on a low wooden bench, an old man telling a story with raised hands, a visitor in a wool cloak in the doorway, '
        'firelight',
        # a cociña onde se recibían as visitas, se comía e se falaba
}
EPOCA = {48: 'xx'}


def xerar(ns):
    import torch
    import imaxes
    torch.set_num_threads(int(os.environ.get('NTH', '4')))
    OUT.mkdir(parents=True, exist_ok=True)
    rexf = OUT / 'biblia.json'
    rex = json.loads(rexf.read_text()) if rexf.exists() else {}
    esc = json.load(open(V1))
    m = imaxes.modelo()
    pipe = None
    for n in ns:
        e1 = esc[n - 1]
        for ver, p in (('v1', e1['prompt']), ('v2', V2[n])):
            k = f'{n:03d}-{ver}-{m["nome"]}'
            f = OUT / f'{k}.png'
            if f.exists() and k in rex:
                continue
            if pipe is None:
                t = time.time(); pipe = imaxes.cargar_pipe(); print('carga', round(time.time() - t, 1), flush=True)
            e = {'prompt': p, 'fase': e1['fase'], 'tipo': e1.get('tipo')}
            pr = imaxes.compor_prompt(e, n, 0, (), m)
            seed = 3000 + n
            t = time.time()
            im = imaxes.xerar_unha(pipe, pr, seed, m)
            s = round(time.time() - t, 1)
            tmp = f.with_suffix('.tmp.png'); im.save(tmp); os.replace(tmp, f)
            rex[k] = {'n': n, 'version': ver, 'modelo': m['nome'], 'W': m['W'], 'H': m['H'], 'semente': seed, 'prompt': pr,
                      'clave': e1.get('clave'), 'texto': e1['texto'], 'epoca': EPOCA.get(n), 's_xeracion': s}
            rexf.write_text(json.dumps(rex, ensure_ascii=False, indent=1))
            print(f'{k}: {s} s', flush=True)
            imaxes._liberar()


def folla():
    import textwrap
    from PIL import Image, ImageDraw, ImageFont
    rex = json.loads((OUT / 'biblia.json').read_text())
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 16)
    ns = sorted({v['n'] for v in rex.values()})
    w, h, ht = 560, 315, 58
    sheet = Image.new('RGB', (2 * (w + 6) + 360, len(ns) * (h + 8) + 34), (20, 20, 20))
    d = ImageDraw.Draw(sheet)
    d.text((6, 6), 'Biblia v1 (esquerda) fronte a v2 (dereita): mesmo modelo e semente, só cambia o prompt', fill=(255, 255, 255), font=font)
    for r, n in enumerate(ns):
        y = 34 + r * (h + 8)
        for c, ver in enumerate(('v1', 'v2')):
            ks = [k for k, v in rex.items() if v['n'] == n and v['version'] == ver]
            if ks:
                im = Image.open(OUT / f'{ks[0]}.png').convert('RGB'); im.thumbnail((w, h))
                sheet.paste(im, (c * (w + 6), y))
                d.text((c * (w + 6) + 4, y + 4), f'{n} {ver}', fill=(255, 255, 160), font=font)
        txt = next(v['texto'] for v in rex.values() if v['n'] == n)
        for j, line in enumerate(textwrap.wrap(txt, 38)[:15]):
            d.text((2 * (w + 6) + 6, y + j * 20), line, fill=(220, 220, 220), font=font)
    dest = AQUI.parent / 'biblia-v1-v2.jpg'
    sheet.save(dest, quality=82, optimize=True)
    print(dest, sheet.size)


if __name__ == '__main__':
    if sys.argv[1] == 'xerar':
        xerar([int(x) for x in sys.argv[2].split(',')] if len(sys.argv) > 2 else sorted(V2))
    else:
        folla()
