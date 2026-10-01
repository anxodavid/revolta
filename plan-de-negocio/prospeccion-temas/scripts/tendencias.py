#!/usr/bin/env python3
"""Google Trends (pytrends): volumen relativo de búsqueda en YouTube (España, 5 años) e índice por mes.

Ancla común "Santa Compaña" en cada lote para poder comparar lotes. Índice de un mes = media de ese mes / media anual.
Uso: python tendencias.py > ../datos/tendencias.txt
"""
import time, statistics, collections
from pytrends.request import TrendReq

ANCLA = "Santa Compaña"
TERMS = ["Camino de Santiago", "vikingos", "suevos", "Torre de Hércules", "indianos", "entroido", "monasterio de Samos",
         "irmandiños", "Prisciliano", "Rande", "Costa da Morte", "San Andrés de Teixido", "Ribarteme", "hórreo",
         "magosto", "castros", "Antela", "afiladores", "ballenas Galicia", "Ribeira Sacra"]
pt = TrendReq(hl="es-ES", tz=0, requests_args={"verify": "/root/.ccr/ca-bundle.crt"})
res = {}
for i in range(0, len(TERMS), 4):
    lote = [ANCLA] + TERMS[i:i + 4]
    for intento in range(4):
        try:
            pt.build_payload(lote, timeframe="today 5-y", geo="ES", gprop="youtube")
            df = pt.interest_over_time()
            break
        except Exception as e:
            print("# reintento", lote, e, flush=True); time.sleep(30)
    else:
        continue
    anc = df[ANCLA].mean() or 1e-9
    for t in lote[1:]:
        s = df[t]
        meses = collections.defaultdict(list)
        for d, x in s.items():
            meses[d.month].append(x)
        media = s.mean() or 1e-9
        idx = {m: statistics.mean(v) / media for m, v in meses.items()}
        pico = max(idx, key=idx.get)
        ceros = (s == 0).mean()
        res[t] = (s.mean() / anc * 2.9, pico, idx[pico], idx.get(10, 0), idx.get(11, 0), ceros)
    time.sleep(10)
print("termino\tvol_rel(Santa Compaña=2,9 como en gauntlet3)\tmes_pico\tindice_pico\tindice_oct\tindice_nov\tsemanas_a_cero")
for t, (v, p, ip, io, inov, c) in sorted(res.items(), key=lambda kv: -kv[1][0]):
    print(f"{t}\t{v:.2f}\t{p}\t{ip:.2f}\t{io:.2f}\t{inov:.2f}\t{c:.0%}")
