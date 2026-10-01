"""Follas de fotogramas para o tribunal final dun episodio longo.

    python probas/tribunal_follas.py DIR_SAIDA REF_16.jpg DIR_TRIBUNAL DIR_CEGO

- DIR_CEGO/imagen1.jpg e imagen2.jpg: a folla de 16 fotogramas do episodio (4x4 a 320x180, sen números, un fotograma no
  medio de 16 planos repartidos por todo o episodio) e a de referencia, nunha orde ao chou; a clave queda en
  DIR_CEGO/clave.txt, para lela só despois de escribir a comparación a cegas. DIR_CEGO vai no scratchpad: a folla de
  referencia é dunha canle real e non se sube ao repo.
- DIR_TRIBUNAL/folla16_320.jpg: a mesma folla do episodio (para o repo).
- DIR_TRIBUNAL/detalle_N.jpg: 40 fotogramas a 640x360 (un no medio de cada 4 planos aprox.), 8 por folla en 2x4, co
  tempo e o número de plano debaixo de cada un, para buscar defectos con minuto e segundo.
"""
import json
import random
import subprocess
import sys
from pathlib import Path

import imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont

FF = imageio_ffmpeg.get_ffmpeg_exe()


def fotograma(video, t, w, h):
    r = subprocess.run([FF, '-v', 'error', '-ss', f'{t:.2f}', '-i', str(video), '-frames:v', '1', '-vf', f'scale={w}:{h}',
                        '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True, check=True)
    return Image.frombytes('RGB', (w, h), r.stdout)


def hms(s):
    s = int(round(s)); return f'{s // 60}:{s % 60:02d}'


def main():
    saida, ref, trib, cego = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]), Path(sys.argv[4])
    trib.mkdir(parents=True, exist_ok=True); cego.mkdir(parents=True, exist_ok=True)
    qa = json.loads((saida / 'qa.json').read_text())
    pl = qa['escenas']; video = saida / 'video.mp4'
    medio = lambda p: p['b0'] + p['dur_s'] / 2

    # folla a cegas: 16 planos repartidos, fotograma no medio de cada un
    idx = [round(i * (len(pl) - 1) / 15) for i in range(16)]
    folla = Image.new('RGB', (1280, 720))
    for k, i in enumerate(idx):
        folla.paste(fotograma(video, medio(pl[i]), 320, 180), (k % 4 * 320, k // 4 * 180))
    folla.save(trib / 'folla16_320.jpg', quality=90)
    (trib / 'folla16_320.json').write_text(json.dumps(
        [{'pos': k + 1, 'plano': pl[i]['n'], 't': hms(medio(pl[i])), 'fase': pl[i]['fase']} for k, i in enumerate(idx)],
        ensure_ascii=False, indent=1))
    orde = [('episodio', trib / 'folla16_320.jpg'), ('referencia', ref)]
    random.shuffle(orde)
    for k, (_, f) in enumerate(orde, 1):
        Image.open(f).convert('RGB').resize((1280, 720)).save(cego / f'imagen{k}.jpg', quality=92)
    (cego / 'clave.txt').write_text(''.join(f'imagen{k}.jpg = {n}\n' for k, (n, _) in enumerate(orde, 1)))

    # follas de detalle: 40 fotogramas, 8 por folla
    sel = [round(i * (len(pl) - 1) / 39) for i in range(40)]
    try:
        fonte = ImageFont.truetype('DejaVuSans.ttf', 20)
    except OSError:
        fonte = ImageFont.load_default()
    for h in range(5):
        F = Image.new('RGB', (1280, 4 * 392), (20, 20, 20)); d = ImageDraw.Draw(F)
        for k, i in enumerate(sel[h * 8:(h + 1) * 8]):
            x, y = k % 2 * 640, k // 2 * 392
            F.paste(fotograma(video, medio(pl[i]), 640, 360), (x, y))
            d.text((x + 8, y + 364), f"{hms(medio(pl[i]))} · plano {pl[i]['n']} · {pl[i]['fase']}", fill=(235, 235, 235), font=fonte)
        F.save(trib / f'detalle_{h + 1}.jpg', quality=85)
    print('feito:', trib, cego)


if __name__ == '__main__':
    main()
