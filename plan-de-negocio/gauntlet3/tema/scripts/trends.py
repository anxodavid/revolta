#!/usr/bin/env python3
"""Google Trends (pytrends): estacionalidad (índice de octubre) y volumen relativo con un término ancla.

Guarda cada consulta en trends_cache/<clave>.csv y no la repite.
"""
import os, sys, time, json
import pandas as pd
from pytrends.request import TrendReq

SCRATCH = "/tmp/claude-0/-home-user-revolta/a8c9798c-edc6-5719-beda-018861fa4d7d/scratchpad"
C = f"{SCRATCH}/tema/trends_cache"
os.makedirs(C, exist_ok=True)

ANCLA = "Santa Compaña"
LOTES = [
    ["Santa Compaña", "meigas", "queimada", "Samaín", "Romasanta"],
    ["Santa Compaña", "muiñeira", "María Pita", "María Soliña", "San Andrés de Teixido"],
    ["Santa Compaña", "batalla de Rande", "mouras", "magosto", "Camino de Santiago"],
    ["Santa Compaña", "brujas gallegas", "leyendas gallegas", "conjuro queimada", "San Xoán"],
]
DESTINOS = [("ES", ""), ("ES", "youtube"), ("ES-GA", ""), ("ES-GA", "youtube")]


def pt():
    return TrendReq(hl="es-ES", tz=-60, timeout=(10, 30),
                    requests_args={"verify": "/root/.ccr/ca-bundle.crt"})


def consulta(kw, geo, gprop, timeframe="today 5-y"):
    clave = f"{geo}_{gprop or 'web'}_{timeframe.replace(' ', '')}_" + "_".join(k.replace(' ', '') for k in kw)
    path = os.path.join(C, clave + ".csv")
    if os.path.exists(path):
        return pd.read_csv(path, index_col=0, parse_dates=True)
    for intento in range(4):
        try:
            p = pt()
            p.build_payload(kw, timeframe=timeframe, geo=geo, gprop=gprop)
            df = p.interest_over_time()
            df.to_csv(path)
            time.sleep(8)
            return df
        except Exception as e:
            print("  error", kw, geo, gprop, repr(e)[:200], file=sys.stderr)
            time.sleep(30 * (intento + 1))
    return None


if __name__ == "__main__":
    for geo, gprop in DESTINOS:
        for kw in LOTES:
            df = consulta(kw, geo, gprop)
            print(geo, gprop or "web", kw, "ok" if df is not None else "FALLO", flush=True)
