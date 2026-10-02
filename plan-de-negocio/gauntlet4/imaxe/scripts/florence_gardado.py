"""Descricións de Florence-2-base que gardou a produción da v1 para cada imaxe etiquetada (as 162 de
gauntlet3/video/imaxes/revision.json e as 11 anteriores aos arranxos, do revision.json de git 4f43fb5).
Saída: $SCRATCH/imaxe4/calib_florence_gardado.json (entrada de avaliar_porta.py). Uso: python3 florence_gardado.py"""
import json, os, subprocess
from pathlib import Path
AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
S = Path(os.environ.get('SCRATCH', '/tmp')) / 'imaxe4'
et = json.load(open(AQUI.parent / 'calibracion' / 'etiquetas-v1.json'))['imaxes']
rv = json.load(open(REPO / 'plan-de-negocio/gauntlet3/video/imaxes/revision.json'))
rvv = json.loads(subprocess.run(['git', '-C', str(REPO), 'show', '4f43fb5:plan-de-negocio/gauntlet3/video/imaxes/revision.json'],
                                capture_output=True, check=True).stdout)
out = []
for d in et:
    base = d['ficheiro'].split('/')[-1].replace('.jpg', '')
    src = rvv if d['version'] == 'vella' else rv
    v = next(v for v in src.values() if v['ficheiro'].replace('.png', '') == base)
    it = v['intentos'][v['escollida']]
    d = dict(d, texto_florence=(it.get('descricion', '') + ' | ' + ', '.join(it.get('obxectos', []))).lower(),
             prompt=it.get('prompt', ''))
    out.append(d)
S.mkdir(parents=True, exist_ok=True)
(S / 'calib_florence_gardado.json').write_text(json.dumps(out, ensure_ascii=False))
print(len(out), 'imaxes')
