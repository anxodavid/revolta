"""Follas de contactos das referencias por concepto (para mirar; NON van ao repo porque levan imaxes BY-SA).
Uso: python follas_refs.py CATALOGO.json DIR_REFERENCIAS DIR_SAIDA [prefixo_concepto]"""
import json, subprocess, sys
from collections import defaultdict
from pathlib import Path
cat, refs, saida = json.load(open(sys.argv[1])), Path(sys.argv[2]), Path(sys.argv[3])
filtro = sys.argv[4] if len(sys.argv) > 4 else ''
saida.mkdir(parents=True, exist_ok=True)
por = defaultdict(list)
for k, x in enumerate(cat):
    por[x['concepto']].append(x)
folla = Path(__file__).with_name('folla.py')
for c, xs in por.items():
    if not c.startswith(filtro):
        continue
    args = []
    for x in xs:
        f = refs / x['ficheiro']
        lic = x['licenza_csv'].replace('CC0 (The Met Open Access)', 'CC0 Met')
        args.append(f"{f}::{x['ficheiro'].split('/')[1][:2]} {lic} · {x['titulo'][:40]}")
    subprocess.run([sys.executable, str(folla), str(saida / f'{c}.jpg'), '380', '4'] + [a for a in args if Path(a.split('::')[0]).exists()],
                   check=True, stdout=subprocess.DEVNULL)
    print(c, sum(Path(a.split('::')[0]).exists() for a in args), 'de', len(args))
