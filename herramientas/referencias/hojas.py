"""Descarga miniaturas pequeñas (320 px) SOLO para revisión visual y monta hojas de contacto en un directorio temporal."""
import json, sys, os, re, time, urllib.request, urllib.parse
from PIL import Image, ImageDraw
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
sel = json.load(open("seleccion.json"))
def thumb(u):
    if "upload.wikimedia.org" in u:
        m = re.match(r"(https://upload.wikimedia.org/wikipedia/commons)/(\w/\w\w)/(.+)$", u)
        if not m: return None
        ext = u.rsplit(".", 1)[-1].lower()
        name = m.group(3)
        suf = "" if ext in ("jpg","jpeg","png") else ".jpg"
        return f"{m.group(1)}/thumb/{m.group(2)}/{name}/330px-{name}{suf}"
    return u.replace("/original/", "/web-large/")
def fetch(u, path):
    if os.path.exists(path): return True
    for i in range(6):
        try:
            req = urllib.request.Request(u, headers={"User-Agent": "revolta-refs/0.1 (afeijoo@ecomt.net)"})
            with urllib.request.urlopen(req, timeout=40) as r, open(path, "wb") as f: f.write(r.read())
            time.sleep(0.6); return True
        except urllib.error.HTTPError as e:
            if e.code == 429: time.sleep(int(e.headers.get("retry-after", "20")) + 2)
            elif e.code == 404: return False
            else: time.sleep(5)
        except Exception: time.sleep(5)
    return False
for conc, rows in sel.items():
    if len(sys.argv) > 2 and conc not in sys.argv[2:]: continue
    tiles = []
    for i, r in enumerate(rows):
        p = f"{OUT}/{conc}-{i:02d}.jpg"; u = thumb(r["url_imagen"])
        ok = u and fetch(u, p)
        try: im = Image.open(p).convert("RGB") if ok else Image.new("RGB", (320, 240), "grey")
        except Exception: im = Image.new("RGB", (320, 240), "grey")
        im.thumbnail((300, 225)); c = Image.new("RGB", (300, 245), "white"); c.paste(im, (0, 0))
        ImageDraw.Draw(c).text((2, 228), f"#{i} {r['titulo'][:48]}", fill="black"); tiles.append(c)
    cols = 4; rws = (len(tiles) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * 300, rws * 245), "white")
    for i, t in enumerate(tiles): sheet.paste(t, ((i % cols) * 300, (i // cols) * 245))
    sheet.save(f"{OUT}/hoja-{conc}.jpg", quality=70); print("hoja", conc, flush=True)
