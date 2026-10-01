import os, glob
import pandas as pd
C = "/tmp/claude-0/-home-user-revolta/a8c9798c-edc6-5719-beda-018861fa4d7d/scratchpad/tema/trends_cache"
MES = ["ene","feb","mar","abr","may","jun","jul","ago","sep","oct","nov","dic"]
for f in sorted(glob.glob(C + "/*all*.csv") + glob.glob(C + "/*2008-01-01*.csv")):
    df = pd.read_csv(f, index_col=0, parse_dates=True)
    if "isPartial" in df.columns:
        df = df[df["isPartial"].astype(str) != "True"].drop(columns=["isPartial"])
    rec = df[df.index >= "2019-01-01"]  # índice estacional con los últimos años (más datos, menos ceros)
    print("\n##", os.path.basename(f)[:-4], f"({len(df)} meses; índice con {len(rec)} meses desde 2019)")
    for k in df.columns:
        s = rec[k]; m = s.mean()
        if m == 0:
            print(f"   {k:22} sin datos"); continue
        pm = s.groupby(s.index.month).mean() / m
        top = pm.sort_values(ascending=False).index[:3]
        print(f"   {k:22} media={m:6.1f}  oct={pm.get(10):.2f}  nov={pm.get(11):.2f}  meses pico: {', '.join(MES[i-1] for i in top)}  ceros={(s==0).mean()*100:.0f}%  oct2025={s.get(pd.Timestamp('2025-10-01'), float('nan'))}")
