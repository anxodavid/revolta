"""Lista (concepto, ficheiro, url) a partir de descargar.sh; os orixinais de Commons pásanse a miniaturas de tamaño
estándar (Wikimedia dá 429 aos orixinais: "use thumbnail images in sizes listed on https://w.wiki/GHai")."""
import csv, re, sys, urllib.parse
STD = [3840, 1920, 1280, 960, 500, 330, 250]
rows = list(csv.DictReader(open('/home/user/revolta/docs/referencias-graficas/referencias.csv')))
anchos = {}
for r in rows:
    m = re.match(r'(\d+)x(\d+)', r['resolucion'])
    if m:
        anchos[r['url_imagen_original']] = int(m.group(1))
for l in open('/home/user/revolta/docs/referencias-graficas/descargar.sh'):
    m = re.match(r'^bajar "([^"]+)" "([^"]+)" "([^"]+)"', l)
    if not m:
        continue
    c, f, u = m.groups()
    if 'upload.wikimedia.org' in u and '/thumb/' not in u:
        w = anchos.get(u)
        p = u.split('/wikipedia/commons/')[1]          # a/ab/Nome.jpg
        nome = p.split('/', 2)[2]
        lim = min(w or 1280, 1920)
        cand = [s for s in STD if s <= lim]
        tw = cand[0] if cand else 960
        if w and w <= tw:          # non se pode pedir unha miniatura igual ou maior ca o orixinal
            cand = [s for s in STD if s < w]; tw = cand[0] if cand else 250
        u = f'https://upload.wikimedia.org/wikipedia/commons/thumb/{p}/{tw}px-{nome}'
    print(c, f, u, sep='\t')
