import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from trends import consulta
LOTES2 = [["Santa Compaña", "meigas", "queimada", "Samaín"],
          ["brujas", "Santa Compaña", "meigas"],
          ["Santa Compaña", "leyendas de Galicia", "Camino de Santiago"]]
for geo in ["ES", "ES-GA"]:
    for gprop in ["", "youtube"]:
        for kw in LOTES2:
            tf = "all" if gprop == "" else "2008-01-01 2026-09-29"
            df = consulta(kw, geo, gprop, timeframe=tf)
            print(geo, gprop or "web", tf, kw, "ok" if df is not None else "FALLO", flush=True)
