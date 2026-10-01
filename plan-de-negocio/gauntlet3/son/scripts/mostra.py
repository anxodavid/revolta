"""Mostras de escoita para o promotor (peza SON): as catro opcións seguidas e o catálogo, en AAC.

    source herramientas/pipeline/entorno.sh
    $PY plan-de-negocio/gauntlet3/son/scripts/mostra.py

mostra-opcions.m4a: o mesmo fragmento en A, B, C e D, separadas por 1 s de silencio (< 6 MB).
mostra-catalogo.m4a: cada tipo de ambiente só, 12 s (catalogo.py).
Escritura atómica (temporal + renomeado) e comprobación de que o ficheiro se descodifica enteiro.
"""
import json, os, subprocess
from pathlib import Path
import numpy as np, soundfile as sf
import imageio_ffmpeg

FF = imageio_ffmpeg.get_ffmpeg_exe()
HERE = Path(__file__).resolve().parent
DEST = HERE.parent
S = Path(os.environ['SCRATCH']) / 'son'


def aac(wav, m4a, kbps):
    tmp = m4a.with_name('.' + m4a.stem + '.tmp.m4a')
    subprocess.run([FF, '-y', '-v', 'error', '-i', str(wav), '-c:a', 'aac', '-b:a', f'{kbps}k', '-movflags', '+faststart',
                    str(tmp)], check=True)
    r = subprocess.run([FF, '-v', 'error', '-i', str(tmp), '-f', 'null', '-'], capture_output=True, text=True)
    if r.stderr.strip():
        raise SystemExit(f'{tmp} non se descodifica enteiro: {r.stderr[:300]}')
    os.replace(tmp, m4a)
    return round(m4a.stat().st_size / 1e6, 2)


def main():
    partes, idx, t = [], [], 0.0
    sil = np.zeros((48000, 2), np.float32)
    for k, op in enumerate('ABCD'):
        x, sr = sf.read(S / 'opcions' / f'{op}_mestura.wav', dtype='float32')
        idx.append({'opcion': op, 'inicio_s': round(t, 1), 'fin_s': round(t + len(x) / sr, 1)})
        partes.append(x); t += len(x) / sr
        if k < 3:
            partes.append(sil); t += 1.0
    wav = S / 'mostra-opcions.wav'
    sf.write(wav, np.concatenate(partes), 48000, subtype='PCM_16')
    mb = aac(wav, DEST / 'mostra-opcions.m4a', 80)
    if mb >= 6.0:
        mb = aac(wav, DEST / 'mostra-opcions.m4a', 64)
    mb_c = aac(S / 'catalogo.wav', DEST / 'mostra-catalogo.m4a', 96)
    print(json.dumps({'opcions': idx, 'mb': mb, 'catalogo_mb': mb_c}, ensure_ascii=False))


if __name__ == '__main__':
    main()
