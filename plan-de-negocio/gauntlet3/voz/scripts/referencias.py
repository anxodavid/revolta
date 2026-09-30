#!/usr/bin/env python
"""Mide as 40 grabacións humanas de Brais (REFS_DIR, refs.tsv): velocidade, F0, enerxía, calidade e arousal.

    source herramientas/pipeline/entorno.sh
    PYTHONPATH=$SCRATCH/voz/pylib flock "$CPU_LOCK" $PY plan-de-negocio/gauntlet3/voz/scripts/referencias.py SAIDA.json

As grabacións son do corpus Nos_Brais-GL (prohibido difundilas): só se miden; non se suben nin se publican.
"""
import csv, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import acustica as A
import modelos

refs = os.environ['REFS_DIR']
filas = list(csv.DictReader(open(os.path.join(refs, 'refs.tsv'), encoding='utf-8'), delimiter='\t'))
em = modelos.Emocion()
out = []
for f in filas:
    p = os.path.join(refs, f['ficheiro'])
    r = A.medir(p, f['texto'])
    r.update(em.medir(p))
    r.update(ficheiro=f['ficheiro'], split=f['split'], categoria=f['categoria'], texto=f['texto'])
    out.append(r)
    print(f"{f['ficheiro']} {f['categoria']:12s} sil/s {r.get('sil_s')} F0 {r.get('f0_mediana_hz')} sd {r.get('f0_sd_st')} "
          f"rango {r.get('f0_rango_st')} din {r.get('dinamica_db')} ar {r['arousal']}", flush=True)
json.dump(out, open(sys.argv[1], 'w'), ensure_ascii=False, indent=1)
