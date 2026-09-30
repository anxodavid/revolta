import re, html as H, sys
def decodificar(b):
    m = re.search(rb'charset=["\']?([\w-]+)', b[:5000])
    enc = m.group(1).decode().lower() if m else 'utf-8'
    try:
        return b.decode(enc)
    except Exception:
        try:
            return b.decode('utf-8')
        except Exception:
            return b.decode('latin-1')
def texto(h):
    h = re.sub(r'(?is)<(script|style|noscript|svg)[^>]*>.*?</\1>', ' ', h)
    h = re.sub(r'(?i)<br\s*/?>|</p>|</h\d>|</li>|</div>|</tr>', '\n', h)
    t = H.unescape(re.sub(r'(?s)<[^>]+>', ' ', h))
    t = re.sub(r'[ \t\xa0]+', ' ', t)
    t = re.sub(r'\s*\n\s*', '\n', t)
    return t.strip()
if __name__ == '__main__':
    src, dst = sys.argv[1], sys.argv[2]
    open(dst, 'w').write(texto(decodificar(open(src, 'rb').read())))
