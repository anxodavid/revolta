"""Pasa a porta de vídeo (movemento.porta_video) polos clips I2V das probas e garda as medidas.

Uso (venv principal, co candado de CPU): python porta_probas.py SAIDA.json CLIP.mp4 [CLIP.mp4 ...]
Para calibrar: os limiares (movemento.PORTA) compáranse co xuízo a ollo de cada clip (informe-r1.md, §porta).
"""
import json, sys, time
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(RAIZ / 'herramientas' / 'pipeline'))
import movemento as M
import revisor


def main():
    saida = Path(sys.argv[1])
    res = json.loads(saida.read_text()) if saida.exists() else {}
    clip = revisor.Clip()
    for f in sys.argv[2:]:
        t = time.time()
        r = M.porta_video(f, clip=clip)
        r['s_porta'] = round(time.time() - t, 1)
        res[Path(f).stem] = r
        print(Path(f).stem, json.dumps(r, ensure_ascii=False), flush=True)
        saida.write_text(json.dumps(res, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
