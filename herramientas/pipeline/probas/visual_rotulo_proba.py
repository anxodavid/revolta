"""Fotograma de proba cun rótulo de montaxe.py (título do episodio ou capítulo) sobre unha imaxe do episodio.

    $PY probas/visual_rotulo_proba.py IMAXE.png SAIDA.png ["Texto do rótulo"] ["Liña pequena"] [--grao]

Serve para comprobar a ollo que o rótulo se le sobre imaxes claras e escuras (a sombra suave do rótulo e a viñeta)
e, con --grao, como queda o gran de película de montaxe.py. Un só fotograma: non precisa o candado de CPU.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
from PIL import Image
import montaxe


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    img, out = args[0], args[1]
    texto = args[2] if len(args) > 2 else 'As meigas de verdade'
    sub = args[3] if len(args) > 3 else 'Cousas de Galiza para durmir'
    if '--grao' in sys.argv:
        montaxe.GRAO = max(montaxe.GRAO, 0.03)
    rot = {'t0': 0.0, 't1': 10.0, 'texto': texto, 'sub': sub, 'y': 0.46, 'tam': 60, 'fundido': 0.8}
    montaxe._init([img], None, [rot])
    esc = [{'b0': 0.0, 'b1': 10.0, 'vis': (0.0, 10.0), 'movemento': 'zoom_in', 'xf': 1.0}]
    fr = montaxe._frame(5.0, esc, 10.0)
    Image.fromarray(fr).save(out)
    print(out, fr.shape, 'lum media', round(float(np.asarray(fr, np.float32).mean()), 1))


if __name__ == '__main__':
    main()
