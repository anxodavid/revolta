"""Compatibilidade coa v1: os planos sen `animacion` teñen que saír igual coa montaxe nova ca coa vella.

Monta os primeiros 10 s da v1 (planos 1-3, Ken Burns) con `montaxe.py` actual e coa versión anterior ao Gauntlet 4
(git show REV:herramientas/pipeline/montaxe.py) e compara os fotogramas descodificados.
Uso (venv principal, co candado): python proba_compat_v1.py [REV]   (REV por defecto: db3d3a7)
"""
import glob, importlib.util, json, os, subprocess, sys, tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(RAIZ / 'herramientas' / 'pipeline'))
import numpy as np


def cargar(nome, ruta):
    spec = importlib.util.spec_from_file_location(nome, ruta)
    m = importlib.util.module_from_spec(spec)
    sys.modules[nome] = m                     # o Pool da montaxe busca _chunk polo nome do módulo
    spec.loader.exec_module(m)
    return m


def main():
    """Compara os fotogramas en memoria (sen codificar: x264 non é determinista entre execucións) que dan a montaxe
    actual e a anterior ao Gauntlet 4 para os planos 1-3 da v1 (Ken Burns, sen `animacion`)."""
    rev = sys.argv[1] if len(sys.argv) > 1 else 'db3d3a7'
    td = Path(tempfile.mkdtemp(prefix='compat_', dir=os.environ.get('SCRATCH')))
    vello = td / 'montaxe_vello.py'
    vello.write_text(subprocess.run(['git', '-C', str(RAIZ), 'show', f'{rev}:herramientas/pipeline/montaxe.py'],
                                    capture_output=True, text=True, check=True).stdout)
    novo = cargar('montaxe_novo', RAIZ / 'herramientas' / 'pipeline' / 'montaxe.py')
    vel = cargar('montaxe_vello', vello)
    esc0 = json.loads((RAIZ / 'plan-de-negocio/gauntlet3/video/escenas-montadas.json').read_text())[:3]
    imgs = [sorted(glob.glob(str(RAIZ / f"plan-de-negocio/gauntlet3/video/imaxes/{e['n'] - 1:03d}-*.jpg")))[0] for e in esc0]
    dur = 10.0
    escenas = [{'b0': e['b0'], 'b1': min(e['b1'], dur), 'movemento': e['movemento'], 'xf': e['xf']} for e in esc0]
    esc = []
    for k, e in enumerate(escenas):                 # o mesmo cálculo de 'vis' ca render()
        xf_in = e.get('xf', 1.2); xf_out = escenas[k + 1].get('xf', 1.2) if k + 1 < len(escenas) else 1.2
        esc.append({**e, 'vis': (max(0.0, e['b0'] - xf_in / 2), min(dur, e['b1'] + xf_out / 2))})
    rot = [{'t0': 2.0, 't1': 6.0, 'texto': 'Proba', 'sub': 'Capítulo I'}]
    tempos = [0.5, 2.2, 4.338, 4.6, 7.0, 9.5]
    fr = {}
    for nome, m in (('novo', novo), ('vello', vel)):
        m._init(imgs, None, rot)
        fr[nome] = [m._frame(t, esc, dur) for t in tempos]
    dif = [int(np.abs(a.astype(np.int16) - b.astype(np.int16)).max()) for a, b in zip(fr['novo'], fr['vello'])]
    print(json.dumps({'tempos': tempos, 'dif_max_por_fotograma': dif, 'iguais': all(d == 0 for d in dif)}))


if __name__ == '__main__':
    main()
