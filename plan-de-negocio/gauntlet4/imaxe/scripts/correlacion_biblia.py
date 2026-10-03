"""Medida automática de correlación (herramientas/pipeline/correlacion.py) nas 20 imaxes da proba da biblia v2:
z de cada imaxe co texto_en do seu plano fronte ao banco dos 140 textos da v1. Saída: calibracion/correlacion-biblia.json

    herramientas/gauntlet/candado.sh $PY correlacion_biblia.py
"""
import json, os, sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
sys.path.insert(0, str(REPO / 'herramientas/pipeline'))
S = Path(os.environ.get('SCRATCH', '/tmp')) / 'imaxe4' / 'biblia'


def main():
    import correlacion, revisor
    planos = {x['n']: x for x in json.load(open(AQUI.parent / 'v1-texto-en.json'))['planos']}
    banco = [x['texto_en'] for x in planos.values()]
    rex = json.loads((S / 'biblia.json').read_text())
    clip = revisor.Clip()
    out = {}
    for ver in ('v1', 'v2'):
        ks = sorted(k for k, v in rex.items() if v['version'] == ver)
        pl = [planos[rex[k]['n']] for k in ks]
        out[ver] = correlacion.medir(pl, [S / f'{k}.png' for k in ks], banco, clip)
        print(ver, json.dumps(correlacion.resumo(out[ver]), ensure_ascii=False))
    (AQUI.parent / 'calibracion' / 'correlacion-biblia.json').write_text(json.dumps(
        {'descricion': __doc__.strip(), 'resumo': {v: correlacion.resumo(out[v]) for v in out}, 'planos': out},
        ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
