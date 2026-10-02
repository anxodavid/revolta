"""Proba dun plano animado (paralaxe + efectos, ou clip I2V) sen son: MP4, tira de 8 fotogramas e tempos.

Uso (venv principal, co candado de CPU):
    python proba_plano.py IMAXE 'ANIMACION_JSON' DUR SAIDA_SEN_EXTENSION [--media]
--media: MP4 a 960x540 (para mirar e subir pouco); os tempos mídense igual sobre o fotograma de 1920x1080.
"""
import json, os, subprocess, sys, time
from pathlib import Path

AQUI = Path(__file__).resolve()
sys.path.insert(0, str(AQUI.parents[4] / 'herramientas' / 'pipeline'))
import numpy as np
import movemento as M


def tira(frames_idx, frames, f, ancho=480):
    from PIL import Image, ImageDraw
    h, w = frames[0].shape[:2]
    alto = round(ancho * h / w)
    folla = Image.new('RGB', (ancho * 4, alto * 2), 'black')
    for k, (i, fr) in enumerate(zip(frames_idx, frames)):
        im = Image.fromarray(fr).resize((ancho, alto), Image.LANCZOS)
        d = ImageDraw.Draw(im); d.rectangle((0, 0, 70, 18), fill='black'); d.text((4, 3), f'f{i}', fill='white')
        folla.paste(im, ((k % 4) * ancho, (k // 4) * alto))
    folla.save(f, quality=88)


def main():
    imaxe, an, dur, saida = sys.argv[1], json.loads(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
    media = '--media' in sys.argv
    import imageio_ffmpeg
    t0 = time.time()
    M.profundidade(imaxe)
    for ef in an.get('efectos', []):
        if ef in M.TEXTOS_MASCARA:
            M.clipseg(imaxe, M.TEXTOS_MASCARA[ef])
    t_prep = time.time() - t0
    t0 = time.time()
    pl = M.Plano({'animacion': an, 'n': 0}, imaxe, dur)
    t_ini = time.time() - t0
    nf = int(round(dur * M.FPS))
    W, H = (960, 540) if media else (M.OW, M.OH)
    cmd = [imageio_ffmpeg.get_ffmpeg_exe(), '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24',
           '-s', f'{W}x{H}', '-r', str(M.FPS), '-i', '-', '-c:v', 'libx264', '-preset', 'medium', '-crf', '18',
           '-pix_fmt', 'yuv420p', saida + '.tmp.mp4']
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    idx = set(np.linspace(0, nf - 1, 8).round().astype(int).tolist())
    guardados = []
    import cv2
    t_fr = []
    for i in range(nf):
        t = time.time()
        F = pl.frame(i / max(1, nf - 1), i / M.FPS)
        F = np.clip(F, 0, 255).astype(np.uint8)
        t_fr.append(time.time() - t)
        if i in idx:
            guardados.append((i, F.copy()))
        if media:
            F = cv2.resize(F, (W, H), interpolation=cv2.INTER_AREA)
        p.stdin.write(F.tobytes())
    p.stdin.close(); p.wait()
    os.replace(saida + '.tmp.mp4', saida + '.mp4')
    tira([i for i, _ in guardados], [f for _, f in guardados], saida + '_tira.jpg')
    res = {'imaxe': imaxe, 'animacion': an, 'dur': dur, 'fotogramas': nf, 's_preparar': round(t_prep, 2),
           's_iniciar': round(t_ini, 2), 's_por_fotograma': round(float(np.mean(t_fr)), 3),
           's_por_fotograma_p95': round(float(np.percentile(t_fr, 95)), 3),
           'zoom_k': round(getattr(getattr(pl, 'plx', None), 'k', 0) or 0, 3),
           'efectos_activos': [type(e).__name__ for e in pl.efs + pl.efp]}
    print(json.dumps(res, ensure_ascii=False), flush=True)
    with open(saida + '.json', 'w') as f:
        json.dump(res, f, ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
