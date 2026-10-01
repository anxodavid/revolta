#!/usr/bin/env python3
"""Volumen relativo (reescalado con el ancla) e índice estacional de octubre por término, desde trends_cache."""
import os, sys, glob
import pandas as pd
sys.path.insert(0, os.path.dirname(__file__))
from trends import LOTES, DESTINOS, ANCLA, C

MESES = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]


def cargar(kw, geo, gprop):
    clave = f"{geo}_{gprop or 'web'}_today5-y_" + "_".join(k.replace(' ', '') for k in kw)
    p = os.path.join(C, clave + ".csv")
    if not os.path.exists(p):
        return None
    df = pd.read_csv(p, index_col=0, parse_dates=True)
    if "isPartial" in df.columns:
        df = df[df["isPartial"].astype(str) != "True"].drop(columns=["isPartial"])
    return df


for geo, gprop in DESTINOS:
    print(f"\n=== {geo} / {gprop or 'web'} (5 años, semanal; {ANCLA} = ancla) ===")
    ref = None
    filas = []
    for kw in LOTES:
        df = cargar(kw, geo, gprop)
        if df is None:
            print("  falta", kw)
            continue
        a = df[ANCLA].mean()
        if ref is None:
            ref = a
        f = ref / a if a else float("nan")
        for k in kw:
            if k == ANCLA and filas and any(r[0] == ANCLA for r in filas):
                continue
            s = df[k]
            media = s.mean()
            por_mes = s.groupby(s.index.month).mean()
            oct_idx = por_mes.get(10, float("nan")) / media if media else float("nan")
            nov_idx = por_mes.get(11, float("nan")) / media if media else float("nan")
            pico = MESES[int(por_mes.idxmax()) - 1] if media else "-"
            ult12 = s[s.index >= s.index.max() - pd.Timedelta(days=365)].mean()
            filas.append((k, media * f, oct_idx, nov_idx, pico, ult12 * f, (s == 0).mean()))
    print(f"{'término':24} {'vol.rel(5a)':>11} {'vol.rel(12m)':>12} {'oct/media':>9} {'nov/media':>9} {'mes pico':>8} {'%sem=0':>7}")
    for k, v, o, n, p, u, z in sorted(filas, key=lambda r: -r[1]):
        print(f"{k:24} {v:11.1f} {u:12.1f} {o:9.2f} {n:9.2f} {p:>8} {z*100:6.0f}%")
