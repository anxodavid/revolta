"""Recortes 1:1 da paralaxe nos saltos de profundidade (onde se ven os defectos: estiramentos, pantasmas, ocos).

Uso (venv principal, co candado): python proba_bordos.py IMAXE 'ANIMACION_JSON' DUR SAIDA.jpg
Fai os fotogramas u = 0, 0,5 e 1 a 1920x1080 e recorta 3 zonas de 400x300 arredor dos saltos de profundidade
máis fortes (e o mapa de profundidade, para ver que viu o modelo).
"""
import json, sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(RAIZ / 'herramientas' / 'pipeline'))
import numpy as np
import movemento as M


def main():
    imaxe, an, dur, saida = sys.argv[1], json.loads(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
    import cv2
    from PIL import Image, ImageDraw
    pl = M.Plano({'animacion': an, 'n': 0}, imaxe, dur)
    us = [0.0, 0.5, 1.0]
    fr = [np.clip(pl.frame(u, u * dur), 0, 255).astype(np.uint8) for u in us]
    d = cv2.resize(M.profundidade(imaxe), (M.OW, M.OH))
    g = cv2.GaussianBlur(np.hypot(cv2.Sobel(d, cv2.CV_32F, 1, 0, ksize=5), cv2.Sobel(d, cv2.CV_32F, 0, 1, ksize=5)), (0, 0), 25)
    zonas = []
    for _ in range(3):                                   # tres máximos separados
        y, x = np.unravel_index(np.argmax(g), g.shape)
        zonas.append((int(np.clip(y - 150, 0, M.OH - 300)), int(np.clip(x - 200, 0, M.OW - 400))))
        g[max(0, y - 300):y + 300, max(0, x - 400):x + 400] = 0
    cw, ch = 400, 300
    folla = Image.new('RGB', (cw * (len(us) + 1), ch * len(zonas)), 'black')
    dm = (np.clip(d, 0, 1) * 255).astype(np.uint8)
    for r, (y, x) in enumerate(zonas):
        for k, f in enumerate(fr):
            im = Image.fromarray(f[y:y + ch, x:x + cw])
            ImageDraw.Draw(im).text((4, 4), f'u={us[k]}', fill='white')
            folla.paste(im, (k * cw, r * ch))
        folla.paste(Image.fromarray(dm[y:y + ch, x:x + cw]).convert('RGB'), (len(us) * cw, r * ch))
    folla.save(saida, quality=90)
    print(json.dumps({'zonas': zonas, 'k': getattr(getattr(pl, 'plx', None), 'k', None)}))


if __name__ == '__main__':
    main()
