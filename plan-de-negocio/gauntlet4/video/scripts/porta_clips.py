"""Porta de vídeo (movemento.porta_video) dos clips I2V da v2 que aínda non a pasaron.

Uso (venv principal, co candado de CPU): porta_clips.py LISTA.json [LISTA.json ...]
LISTA.json: os traballos de `produccion.py i2v` ({n, imaxe, accion, i2v}). Para cada clip que xa estea na caché
(movemento.i2v_ficheiro) e non teña resultado para ese mesmo clip, pasa a porta e garda o resultado en
video/porta-i2v.json (por plano: clip, ok, problemas, avisos, medidas e os parámetros i2v) e unha tira de 8
fotogramas en $SCRATCH/v2/tiras. Un plano cun clip novo (imaxe rexenerada ou outra semente) substitúe o resultado vello.
"""
import json, sys, time
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(RAIZ / 'herramientas' / 'pipeline'))
sys.path.insert(0, str(RAIZ / 'plan-de-negocio' / 'gauntlet4' / 'movemento' / 'scripts'))
import movemento as M                                          # noqa: E402
from produccion import PORTA, SCR, gardar, ler                  # noqa: E402  (mesmo cartafol: sys.path[0])


def main():
    res = ler(PORTA, {})
    tiras = SCR / 'v2' / 'tiras'; tiras.mkdir(parents=True, exist_ok=True)
    clip = None
    for L in sys.argv[1:]:
        for t in ler(L, []):
            if t['imaxe'] == '-':
                continue
            f = M.i2v_ficheiro(t['imaxe'], t['accion'], t.get('i2v'))
            n = str(t['n'])
            if not f.exists() or res.get(n, {}).get('clip') == f.name:
                continue
            if clip is None:
                import revisor
                clip = revisor.Clip()
            t0 = time.time()
            r = M.porta_video(f, clip=clip)
            r.update(clip=f.name, imaxe=Path(t['imaxe']).name, i2v=t.get('i2v') or {}, s_porta=round(time.time() - t0, 1))
            res[n] = r
            from porta_probas import tira
            tira(f, tiras / f'p{int(n):02d}-{f.stem}.jpg')
            print(f"plano {n}: {'ok' if r['ok'] else r['problemas']}", flush=True)
            gardar(PORTA, res)


if __name__ == '__main__':
    main()
