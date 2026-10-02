"""Compara un clip I2V escalado a 1080p sen e con transferencia de detalle (movemento.Clip._detalle).

Uso (venv principal, co candado): python proba_detalle.py CLIP.mp4 IMAXE.jpg SAIDA.jpg [fotogramas...]
Saída: folla con recortes 1:1 de 480x270 (sen | con) de varios fotogramas e o tempo por fotograma.
"""
import json, os, sys, time
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(RAIZ / 'herramientas' / 'pipeline'))
import numpy as np
import movemento as M


def main():
    mp4, imaxe, saida = sys.argv[1], sys.argv[2], sys.argv[3]
    idx = [int(x) for x in sys.argv[4:]] or [0, 24, 48]
    from PIL import Image, ImageDraw
    os.environ['MOVEMENTO_DETALLE'] = '0'
    a = M.Clip(mp4, 2.0, zoom=1.0)
    os.environ['MOVEMENTO_DETALLE'] = '1'
    b = M.Clip(mp4, 2.0, zoom=1.0, imaxe=imaxe)
    cw, ch = 480, 270
    folla = Image.new('RGB', (cw * 4, ch * len(idx)), 'black')
    tempos = []
    for r, i in enumerate(idx):
        t = i / M.FPS
        fa = np.clip(a.frame(t), 0, 255).astype(np.uint8)
        t0 = time.time(); fb = np.clip(b.frame(t), 0, 255).astype(np.uint8); tempos.append(time.time() - t0)
        # dous recortes 1:1: centro e terzo superior esquerdo
        for k, (y, x) in enumerate([(M.OH // 2 - ch // 2, M.OW // 2 - cw // 2), (M.OH // 4 - ch // 2, M.OW // 4 - cw // 2)]):
            for j, f in enumerate((fa, fb)):
                im = Image.fromarray(f[y:y + ch, x:x + cw])
                d = ImageDraw.Draw(im); d.rectangle((0, 0, 150, 16), fill='black')
                d.text((3, 2), f"f{i} {'con' if j else 'sen'} detalle", fill='white')
                folla.paste(im, ((2 * k + j) * cw, r * ch))
    folla.save(saida, quality=90)
    print(json.dumps({'s_por_fotograma_con_detalle': round(float(np.mean(tempos)), 3)}))


if __name__ == '__main__':
    main()
