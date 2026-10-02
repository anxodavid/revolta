"""Une cada ficheiro baixado por baixar_refs.sh coa súa fila de docs/referencias-graficas/referencias.csv.
Saída (stdout, JSON): [{concepto, ficheiro, fila, titulo, url_pagina, autor, licenza, resolucion, ...}]."""
import csv, json, re, sys
from pathlib import Path
REPO = Path(__file__).resolve().parents[4]
rows = list(csv.DictReader(open(REPO / 'docs/referencias-graficas/referencias.csv')))
por_url = {r['url_imagen_original']: (i, r) for i, r in enumerate(rows)}
out = []
for l in open(REPO / 'docs/referencias-graficas/descargar.sh'):
    m = re.match(r'^bajar "([^"]+)" "([^"]+)" "([^"]+)"', l)
    if not m:
        continue
    c, f, u = m.groups()
    orig = u
    if '/thumb/' in u:          # .../thumb/a/ab/Nome.jpg/1920px-Nome.jpg -> .../a/ab/Nome.jpg
        orig = u.replace('/thumb/', '/').rsplit('/', 1)[0]
    i, r = por_url.get(orig) or por_url.get(u) or (None, None)
    if r is None:
        print('sen fila:', c, f, u, file=sys.stderr); continue
    out.append({'concepto': c, 'ficheiro': f'{c}/{f}', 'fila_csv': i, 'titulo': r['titulo'], 'url_pagina': r['url_pagina'],
                'url_imaxe': r['url_imagen_original'], 'autor': r['autor'], 'licenza_csv': r['licencia'],
                'resolucion': r['resolucion'], 'tipo': r['tipo'], 'texto_atribucion': r['texto_atribucion']})
json.dump(out, sys.stdout, ensure_ascii=False, indent=1)
print(len(out), 'ficheiros', file=sys.stderr)
