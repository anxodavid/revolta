"""Clips malos sintéticos para calibrar a porta de vídeo (non hai clips I2V malos de verdade nas probas):
quieto (o primeiro fotograma repetido), caótico (fotogramas en orde ao chou), parpadeo (luz que salta) e deriva
(a segunda metade doutro clip). Uso: python porta_negativos.py CLIP_A.mp4 CLIP_B.mp4 DIR_SAIDA
"""
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(RAIZ / 'herramientas' / 'pipeline'))
import numpy as np
import movemento as M
import movemento_i2v as I


def main():
    a, b, out = M.ler_video(sys.argv[1]), M.ler_video(sys.argv[2]), Path(sys.argv[3])
    out.mkdir(parents=True, exist_ok=True)
    n = min(len(a), len(b))
    rng = np.random.default_rng(1)
    fl = a[:n].astype(np.float32) * np.where(np.arange(n) % 6 < 3, 1.0, 0.86)[:, None, None, None]
    casos = {'neg_quieto': np.repeat(a[:1], n, 0),
             'neg_caotico': a[rng.permutation(n)],
             'neg_parpadeo': np.clip(fl, 0, 255).astype(np.uint8),
             'neg_deriva': np.concatenate([a[:n // 2], b[n // 2:n]])}
    for nome, fr in casos.items():
        I.gardar_mp4(fr, out / f'{nome}.mp4')
        print(out / f'{nome}.mp4')


if __name__ == '__main__':
    main()
