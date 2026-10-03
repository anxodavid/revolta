"""Pasa a porta de vídeo (movemento.porta_video) polos clips I2V das probas e garda as medidas.

Uso (venv principal, co candado de CPU): python porta_probas.py SAIDA.json DIR_TIRAS CLIP.mp4 [CLIP.mp4 ...]
Garda tamén unha tira de 8 fotogramas de cada clip en DIR_TIRAS.
Para calibrar: os limiares (movemento.PORTA) compáranse co xuízo a ollo de cada clip (informe-r1.md, §porta).
"""
import json, sys, time
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(RAIZ / 'herramientas' / 'pipeline'))
import movemento as M
import revisor


def nome_clip(f):
    """Nome lexible do clip (plano da v1 e fotogramas) a partir do JSON que deixa movemento_i2v.py ao seu carón."""
    j = Path(f).with_suffix('.json')
    if j.exists():
        d = json.loads(j.read_text())
        n = int(Path(d['imaxe']).name[:3]) + 1
        return f"i2v_p{n:02d}_{d['W']}x{d['H']}_f{d['F']}_s{d['pasos']}"
    return Path(f).stem


def tira(f, saida, n=8, ancho=480):
    from PIL import Image, ImageDraw
    import numpy as np
    fr = M.ler_video(f)
    idx = np.linspace(0, len(fr) - 1, n).round().astype(int)
    h, w = fr.shape[1:3]
    alto = round(ancho * h / w)
    folla = Image.new('RGB', (ancho * 4, alto * 2), 'black')
    for k, i in enumerate(idx):
        im = Image.fromarray(fr[i]).resize((ancho, alto), Image.LANCZOS)
        d = ImageDraw.Draw(im); d.rectangle((0, 0, 70, 18), fill='black'); d.text((4, 3), f'f{i}', fill='white')
        folla.paste(im, ((k % 4) * ancho, (k // 4) * alto))
    folla.save(saida, quality=85)


def main():
    """Uso: porta_probas.py SAIDA.json DIR_TIRAS CLIP.mp4 [...]"""
    saida, tiras = Path(sys.argv[1]), Path(sys.argv[2])
    tiras.mkdir(parents=True, exist_ok=True)
    res = json.loads(saida.read_text()) if saida.exists() else {}
    clip = revisor.Clip()
    for f in sys.argv[3:]:
        nome = nome_clip(f)
        t = time.time()
        r = M.porta_video(f, clip=clip)
        r['s_porta'] = round(time.time() - t, 1)
        j = Path(f).with_suffix('.json')
        if j.exists():
            r['xeracion'] = {k: v for k, v in json.loads(j.read_text()).items() if k not in ('accion',)}
        res[nome] = r
        tira(f, tiras / f'{nome}_tira.jpg')
        print(nome, json.dumps(r, ensure_ascii=False), flush=True)
        saida.write_text(json.dumps(res, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
