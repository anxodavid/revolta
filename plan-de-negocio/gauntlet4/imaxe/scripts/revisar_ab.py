"""Pasa a porta v6 (revisor.py: MediaPipe, Florence-2-base e CLIP-L) polas imaxes das probas A/B de sementes e da
biblia v2, coa `clave`, o prompt e a fase de cada unha. Saída: $SCRATCH/imaxe4/<proba>/revision_v6.json e un resumo.

    herramientas/gauntlet/candado.sh $PY revisar_ab.py ab biblia      # ≈ 25 s por imaxe
"""
import json, os, sys, time
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
sys.path.insert(0, str(REPO / 'herramientas/pipeline'))
S = Path(os.environ.get('SCRATCH', '/tmp')) / 'imaxe4'


def main(probas):
    import torch
    import revisor
    torch.set_num_threads(int(os.environ.get('NTH', '4')))
    rev = None
    for proba in probas:
        d = S / proba
        rex = json.loads((d / f'{proba}.json').read_text())
        outf = d / 'revision_v6.json'
        out = json.loads(outf.read_text()) if outf.exists() else {}
        for k, v in rex.items():
            if k.endswith('-erro') or k in out:
                continue
            f = d / f'{k}.png'
            if not f.exists():
                continue
            if rev is None:
                rev = revisor.Revisor()
            fase = v.get('fase')
            if fase is None and proba == 'ab':
                fase = {'aldea': 'transicion', 'horreo': 'calma', 'carro': 'transicion', 'palloza': 'transicion',
                        'lareira': 'gancho', 'queimada': 'gancho', 'horreos': 'transicion', 'pote': 'calma'}.get(v['concepto'])
            t = time.time()
            r = rev.revisar(f, clave=v.get('clave'), fase=fase, prompt=v.get('prompt'), epoca=v.get('epoca'))
            r.pop('clip_emb', None)
            r['s_revision'] = round(time.time() - t, 1)
            out[k] = r
            outf.write_text(json.dumps(out, ensure_ascii=False, indent=1))
            print(k, r['problemas'] or 'ok', r.get('iconografia', {}).get(f"clave: {v.get('clave')}"), flush=True)


if __name__ == '__main__':
    main(sys.argv[1:] or ['ab', 'biblia'])
