"""Comproba na API de Wikimedia Commons (extmetadata da páxina de cada ficheiro) a licenza, o autor e o crédito das
referencias; e na API de The Met Open Access (isPublicDomain) as do Met. Peticións en lotes de 40, con pausa.
Uso: python licenzas_commons.py CATALOGO.json > licenzas.json"""
import json, re, sys, time, urllib.parse, urllib.request
UA = 'revolta-refs/0.2 (+https://github.com/anxodavid/revolta)'
cat = json.load(open(sys.argv[1]))
def get(url):
    for i in range(5):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            return json.load(urllib.request.urlopen(req, timeout=60))
        except Exception as ex:
            print('reintento', i, ex, file=sys.stderr); time.sleep(10 * (i + 1))
    raise SystemExit('fallou ' + url)
def limpar(h):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', h or '')).strip()
out = {}
commons = [x for x in cat if 'commons.wikimedia.org' in x['url_pagina']]
for k in range(0, len(commons), 40):
    lote = commons[k:k + 40]
    tit = [urllib.parse.unquote(x['url_pagina'].split('/wiki/')[1]).replace('_', ' ') for x in lote]
    q = urllib.parse.urlencode({'action': 'query', 'format': 'json', 'prop': 'imageinfo', 'iiprop': 'extmetadata|size',
                                'titles': '|'.join(tit), 'formatversion': '2'})
    r = get('https://commons.wikimedia.org/w/api.php?' + q)
    norm = {n['from']: n['to'] for n in r['query'].get('normalized', [])}
    pags = {p['title']: p for p in r['query']['pages']}
    for x, t in zip(lote, tit):
        p = pags.get(norm.get(t, t)) or pags.get(t)
        if not p or 'imageinfo' not in p:
            out[x['ficheiro']] = {'erro': 'sen páxina'}; continue
        m = p['imageinfo'][0]['extmetadata']
        g = lambda c: limpar(m.get(c, {}).get('value'))
        out[x['ficheiro']] = {'licenza': g('LicenseShortName'), 'licenza_url': g('LicenseUrl'), 'autor': g('Artist'),
                              'credito': g('Credit'), 'atribucion_requirida': g('AttributionRequired'),
                              'copyrighted': g('Copyrighted'), 'restricions': g('Restrictions'),
                              'data': g('DateTimeOriginal'), 'descricion': g('ImageDescription')[:300],
                              'ancho': p['imageinfo'][0].get('width'), 'alto': p['imageinfo'][0].get('height')}
    time.sleep(3)
for x in cat:
    if 'metmuseum.org' in x['url_pagina']:
        oid = x['url_pagina'].rstrip('/').split('/')[-1]
        r = get(f'https://collectionapi.metmuseum.org/public/collection/v1/objects/{oid}')
        out[x['ficheiro']] = {'licenza': 'CC0 (Met Open Access)' if r.get('isPublicDomain') else 'NON é dominio público',
                              'isPublicDomain': r.get('isPublicDomain'), 'autor': r.get('artistDisplayName') or r.get('culture'),
                              'titulo': r.get('title'), 'data': r.get('objectDate'), 'credito': r.get('creditLine'),
                              'imaxe': r.get('primaryImage')}
        time.sleep(1)
json.dump(out, sys.stdout, ensure_ascii=False, indent=1)
print(len(out), 'comprobadas', file=sys.stderr)
