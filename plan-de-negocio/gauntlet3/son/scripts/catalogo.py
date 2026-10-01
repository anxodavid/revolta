"""Mostra do catálogo (peza SON): cada tipo de ambiente só, 12 s, sen voz, para xulgar cada son por separado.

    source herramientas/pipeline/entorno.sh
    OMP_NUM_THREADS=1 nice -n 10 $PY plan-de-negocio/gauntlet3/son/scripts/catalogo.py

Cada tipo a -24 LUFS (máis forte do que irá baixo a voz, para oílo ben), calma 0,3 e os eventos máis frecuentes
ca no vídeo, para que se oian nos 12 s (leño, curuxa, chocallo, gorgolexo). 1 s de silencio entre tipos.
Saída: $SCRATCH/son/catalogo.wav e catalogo.json (minuto de cada tipo).
"""
import json, os, sys
from pathlib import Path
import numpy as np, soundfile as sf, pyloudnorm as pyln

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / 'herramientas/pipeline'))
import son

DUR, PAUSA = 12.0, 1.0
EXTRA = {'lume': {'lenos': 8.0}, 'noite': {'curuxa': 8.0}, 'aldea': {'chocallo': 8.0}, 'fonte': {'caudal': 1.0}}


def main():
    m = pyln.Meter(son.SR)
    partes, idx, t = [], [], 0.0
    f = int(1.5 * son.SR)
    for k, tipo in enumerate(son.AMBIENTES):
        fn, _ = son.AMBIENTES[tipo]
        x = fn(DUR, seed=100 + k, calma=0.3, **EXTRA.get(tipo, {}))
        x *= 10 ** ((-24 - m.integrated_loudness(x)) / 20)
        e = np.ones(len(x), np.float32); e[:f] = np.linspace(0, 1, f); e[-f:] = np.linspace(1, 0, f)
        partes += [x * e[:, None], np.zeros((int(PAUSA * son.SR), 2), np.float32)]
        idx.append({'tipo': tipo, 'inicio': f'{int(t // 60)}:{t % 60:04.1f}', 'inicio_s': round(t, 1)})
        t += DUR + PAUSA
    y = np.concatenate(partes)
    S = Path(os.environ['SCRATCH']) / 'son'
    sf.write(S / 'catalogo.wav', np.clip(y, -1, 1), son.SR, subtype='PCM_16')
    (S / 'catalogo.json').write_text(json.dumps(idx, ensure_ascii=False, indent=1))
    print(json.dumps(idx, ensure_ascii=False))


if __name__ == '__main__':
    main()
