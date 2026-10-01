import re, sys, time, subprocess, html as H
sys.path.insert(0, '.')
from limpar import texto, decodificar
import requests
UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36'
for w in sys.argv[1:]:
    url = 'https://academia.gal/dicionario/-/termo/busca/' + requests.utils.quote(w)
    r = requests.get(url, headers={'User-Agent': UA}, timeout=60, verify='/root/.ccr/ca-bundle.crt')
    t = texto(decodificar(r.content))
    open(f'rag/{w}.txt', 'w').write(t)
    # liñas de definición: a forma visible (sen JSON)
    ls = [l for l in t.split('\n') if re.match(r'^' + re.escape(w.split()[0]) + r'\b', l, re.I) and ('substantivo' in l or 'adxectivo' in l or 'verbo' in l or 'VÉXASE' in l) and '"htmlContent"' not in l and 'referencesContent' not in l]
    print('=====', w, r.status_code, url)
    for l in ls[:3]:
        print(l[:1500])
    if not ls:
        print('(sen entrada) ', ' | '.join(x for x in t.split('\n') if 'Non se atop' in x or 'suxest' in x.lower())[:300])
    time.sleep(1.5)
