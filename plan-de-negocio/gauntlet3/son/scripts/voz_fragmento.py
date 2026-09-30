"""Voz do fragmento de proba (peza SON) e banco do murmullo de xente, nunha soa carga do modelo.

    source herramientas/pipeline/entorno.sh
    PATH=$ST2_PATHBIN:$PATH PYTHONPATH=$ST2_STUBS flock "$CPU_LOCK" $PY plan-de-negocio/gauntlet3/son/scripts/voz_fragmento.py

Cada frase leva os parámetros da curva do embude (curva.py) na súa posición virtual do episodio (fragmento.py), coma
en longo.py: escala, f0_media, f0_rango, enerxia e estilo (este último só fai algo se REF_WAV_CALMO está definida).
Saída: $SCRATCH/son/voz/frag_XX.wav (24 kHz) e o banco de son_xente.py.
"""
import os, sys
from pathlib import Path
import soundfile as sf

REPO = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO / 'herramientas/pipeline')); sys.path.insert(0, str(Path(__file__).resolve().parent))
import curva, fragmento as FR, son_xente

OUT = Path(os.environ['SCRATCH']) / 'son' / 'voz'


def main():
    import voz_st2 as V
    OUT.mkdir(parents=True, exist_ok=True)
    for f in FR.frases_con_pal0():
        p = OUT / f"frag_{f['i']:02d}.wav"
        if p.exists():
            continue
        c = curva.en(f['pal0'], FR.TOT)
        V.cargar()
        w, _ = V.infer(f['texto'], escala=c['escala'], estilo=c['estilo'], f0_media=c['f0_media'],
                       f0_rango=c['f0_rango'], enerxia=c['enerxia'])
        sf.write(str(p) + '.tmp.wav', w, 24000); os.replace(str(p) + '.tmp.wav', p)
        print(f"frag {f['i']:02d} {f['tramo']:7s} escala {c['escala']:.3f} {len(w) / 24000:4.1f}s {f['texto'][:50]}",
              flush=True)
    son_xente.main(Path(os.environ['SCRATCH']) / 'son' / 'banco')


if __name__ == '__main__':
    main()
