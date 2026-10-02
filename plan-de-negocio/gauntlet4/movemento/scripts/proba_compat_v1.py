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
    rev = sys.argv[1] if len(sys.argv) > 1 else 'db3d3a7'
    import imageio_ffmpeg
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    td = Path(tempfile.mkdtemp(prefix='compat_', dir=os.environ.get('SCRATCH')))
    vello = td / 'montaxe_vello.py'
    vello.write_text(subprocess.run(['git', '-C', str(RAIZ), 'show', f'{rev}:herramientas/pipeline/montaxe.py'],
                                    capture_output=True, text=True, check=True).stdout)
    novo = cargar('montaxe_novo', RAIZ / 'herramientas' / 'pipeline' / 'montaxe.py')
    vel = cargar('montaxe_vello', vello)
    esc = json.loads((RAIZ / 'plan-de-negocio/gauntlet3/video/escenas-montadas.json').read_text())[:3]
    imgs = [sorted(glob.glob(str(RAIZ / f"plan-de-negocio/gauntlet3/video/imaxes/{e['n'] - 1:03d}-*.jpg")))[0] for e in esc]
    dur = 10.0
    wav = td / 'a.wav'
    subprocess.run([ff, '-y', '-v', 'error', '-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=stereo', '-t', str(dur), str(wav)], check=True)
    srt = td / 's.srt'; srt.write_text('1\n00:00:01,000 --> 00:00:02,000\nproba\n')
    pl = [{'b0': e['b0'], 'b1': min(e['b1'], dur), 'movemento': e['movemento'], 'xf': e['xf']} for e in esc]
    fr = {}
    for nome, m in (('novo', novo), ('vello', vel)):
        out = td / f'{nome}.mp4'
        m.render(pl, imgs, dur, str(wav), str(srt), str(out), td / f'w_{nome}', procs=2)
        p = subprocess.run([ff, '-v', 'error', '-i', str(out), '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'],
                           capture_output=True, check=True)
        fr[nome] = np.frombuffer(p.stdout, np.uint8)
    dif = np.abs(fr['novo'].astype(np.int16) - fr['vello'].astype(np.int16))
    print(json.dumps({'bytes': int(fr['novo'].size), 'iguais': bool(dif.max() == 0), 'dif_max': int(dif.max()),
                      'dif_media': float(dif.mean())}))


if __name__ == '__main__':
    main()
