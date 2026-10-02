"""¿Paga a pena xerar a 1024x576 e refinar a escollida a 1344x768 con img2img? (Gauntlet 4, peza IMAXE; D18: calidade)

Para cada imaxe: reescalado LANCZOS a 1344x768 (o que fai hoxe a montaxe, que ademais a leva a 1920x1080) fronte a
img2img a 1344x768 coa mesma semente e o mesmo prompt, forza 0,35 (1 paso de Lightning) e 0,5 (2 pasos). Tamén mide
unha xeración directa a 1344x768 (texto só) para ter o tempo.

    herramientas/gauntlet/candado.sh $PY refinar_proba.py xerar PROBA:CLAVE [PROBA:CLAVE ...]   # p. ex. biblia:084-v2-lightning1024
    $PY refinar_proba.py folla
"""
import json, os, sys, time
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
sys.path.insert(0, str(REPO / 'herramientas/pipeline'))
S = Path(os.environ.get('SCRATCH', '/tmp')) / 'imaxe4'
OUT = S / 'refinar'


def xerar(items):
    import torch
    from PIL import Image
    import imaxes
    torch.set_num_threads(int(os.environ.get('NTH', '4')))
    OUT.mkdir(parents=True, exist_ok=True)
    rexf = OUT / 'refinar.json'
    rex = json.loads(rexf.read_text()) if rexf.exists() else {}
    m = imaxes.modelo('lightning')            # 1344x768, 4 pasos
    pipe = imaxes.cargar_pipe('lightning')
    for it in items:
        proba, k = it.split(':', 1)
        v = json.loads((S / proba / f'{proba}.json').read_text())[k]
        orixe = Image.open(S / proba / f'{k}.png').convert('RGB')
        up = orixe.resize((m['W'], m['H']), Image.LANCZOS)
        up.save(OUT / f'{k}-lanczos.png')
        for forza in (0.35, 0.5):
            f = OUT / f'{k}-refinada{int(forza * 100):03d}.png'
            if f.exists():
                continue
            t = time.time()
            im = imaxes.xerar_unha(pipe, v['prompt'], v.get('semente', 1), m,
                                   ref={'modo': 'img2img', 'forza': forza, 'imaxe': up, 'ficheiro': k})
            s = round(time.time() - t, 1)
            im.save(f)
            rex[f.stem] = {'orixe': k, 'forza': forza, 's': s}
            print(f.stem, s, 's', flush=True)
            rexf.write_text(json.dumps(rex, ensure_ascii=False, indent=1))
        f = OUT / f'{k}-directa1344.png'
        if not f.exists():
            t = time.time()
            im = imaxes.xerar_unha(pipe, v['prompt'], v.get('semente', 1), m)
            s = round(time.time() - t, 1)
            im.save(f)
            rex[f.stem] = {'orixe': k, 'directa': True, 's': s}
            print(f.stem, s, 's', flush=True)
            rexf.write_text(json.dumps(rex, ensure_ascii=False, indent=1))
        imaxes._liberar()


def folla():
    from PIL import Image, ImageDraw, ImageFont
    rex = json.loads((OUT / 'refinar.json').read_text())
    orixes = sorted({v['orixe'] for v in rex.values()})
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 16)
    cols = ['lanczos', 'refinada035', 'refinada050', 'directa1344']
    cw, ch = 448, 336                         # recorte 1:1 do centro (o detalle que se ve en pantalla grande)
    sheet = Image.new('RGB', (len(cols) * (cw + 6), len(orixes) * (ch + 26) + 30), (20, 20, 20))
    d = ImageDraw.Draw(sheet)
    d.text((6, 6), 'Recorte 1:1 do centro a 1344x768: reescalado, refinado (forza 0,35 e 0,5) e xeración directa', fill=(255, 255, 255), font=font)
    for r, o in enumerate(orixes):
        y = 30 + r * (ch + 26)
        for c, col in enumerate(cols):
            p = OUT / f'{o}-{col}.png'
            if not p.exists():
                continue
            im = Image.open(p).convert('RGB')
            W, H = im.size
            im = im.crop(((W - cw) // 2, (H - ch) // 2, (W + cw) // 2, (H + ch) // 2))
            sheet.paste(im, (c * (cw + 6), y))
            s = rex.get(f'{o}-{col}', {}).get('s')
            d.text((c * (cw + 6) + 4, y + ch + 4), f'{o[:14]} {col}' + (f' {s:.0f} s' if s else ''), fill=(255, 255, 160), font=font)
    dest = AQUI.parent / 'refinar-1344.jpg'
    sheet.save(dest, quality=85, optimize=True)
    print(dest, sheet.size)


if __name__ == '__main__':
    xerar(sys.argv[2:]) if sys.argv[1] == 'xerar' else folla()
