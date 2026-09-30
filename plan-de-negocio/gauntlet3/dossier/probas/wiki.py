import re, sys, time, html as H, urllib.parse, requests
UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36'
def baixar(url, dest_html):
    for i in range(6):
        r = requests.get(url, headers={'User-Agent': UA}, timeout=60, verify='/root/.ccr/ca-bundle.crt')
        if r.status_code == 429:
            time.sleep(15 * (i + 1)); continue
        r.raise_for_status()
        open(dest_html, 'w').write(r.text)
        return r.text
    raise SystemExit(f'429 {url}')
def texto(h):
    m = re.search(r'<div id="mw-content-text".*', h, re.S)
    h = m.group(0) if m else h
    h = re.sub(r'(?is)<(script|style|noscript)[^>]*>.*?</\1>', ' ', h)
    h = re.sub(r'(?is)<sup[^>]*class="reference"[^>]*>.*?</sup>', ' ', h)   # [1] fóra do texto
    h = re.sub(r'(?is)<span class="mw-editsection">.*?</span>\s*</span>', ' ', h)
    h = re.sub(r'(?i)<br\s*/?>|</p>|</h\d>|</li>|</div>|</tr>|</dd>', '\n', h)
    t = H.unescape(re.sub(r'(?s)<[^>]+>', ' ', h))
    t = re.sub(r'[ \t\xa0]+', ' ', t)
    t = re.sub(r'\s*\n\s*', '\n', t)
    t = re.sub(r' ([,.;:])', r'\1', t)
    return t.strip()
if __name__ == '__main__':
    # uso: wiki.py ETIQUETA URL [ETIQUETA URL ...]
    a = sys.argv[1:]
    for k in range(0, len(a), 2):
        et, url = a[k], a[k + 1]
        h = baixar(url, f'html/{et}.html')
        t = texto(h)
        open(f'fontes/{et}.txt', 'w').write(t)
        print(et, len(t.split()), url)
        time.sleep(4)
