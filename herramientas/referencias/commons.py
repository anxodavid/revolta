#!/usr/bin/env python3
"""Cliente mínimo y educado de la API de Wikimedia Commons (solo metadatos; no descarga imágenes).

Uso:
  commons.py cat  "Category:Hórreos in Galicia" [--sub]    # ficheros de una categoría (y subcategorías nivel 1)
  commons.py find "hórreo Galicia"                          # búsqueda de ficheros
  commons.py subcats "Category:Hórreos in Galicia"          # solo lista subcategorías
Salida: JSON por línea con título, licencia, autor, tamaño, fecha, URLs. Respeta 429/Retry-After.
"""
import json, sys, time, re, urllib.parse, urllib.request, urllib.error, html

API = "https://commons.wikimedia.org/w/api.php"
UA = "revolta-refs/0.1 (afeijoo@ecomt.net; investigacion de referencias graficas)"
OK = re.compile(r"^(cc0|cc[- ]zero|public domain|pd|pdm|cc[- ]by(?![- ]nc)(?![- ]nd)|cc[- ]by[- ]sa|attribution|no restrictions)", re.I)

def call(params, tries=8):
    params = dict(params, format="json", formatversion="2")
    url = API + "?" + urllib.parse.urlencode(params)
    for i in range(tries):
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=40) as r:
                time.sleep(1.5)
                return json.load(r)
        except urllib.error.HTTPError as e:
            wait = int(e.headers.get("retry-after", "30")) + 3 if e.code == 429 else 10 * (i + 1)
            print(f"# HTTP {e.code}, espero {wait}s", file=sys.stderr)
            time.sleep(wait)
        except Exception as e:
            print(f"# {e}", file=sys.stderr); time.sleep(10)
    raise SystemExit("API no disponible")

def clean(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s or "")).strip()

def info_from_pages(pages):
    out = []
    for p in pages:
        ii = (p.get("imageinfo") or [None])[0]
        if not ii: continue
        m = ii.get("extmetadata", {})
        g = lambda k: clean(m.get(k, {}).get("value", ""))
        out.append(dict(title=p["title"], page=ii["descriptionurl"], url=ii["url"], w=ii["width"], h=ii["height"],
                        mime=ii.get("mime"), license=g("LicenseShortName"), licurl=g("LicenseUrl"),
                        author=g("Artist"), date=g("DateTimeOriginal") or g("DateTime"), credit=g("Credit"),
                        restrictions=g("Restrictions"), desc=g("ImageDescription")[:200], usage=g("UsageTerms")))
    return out

IIPROP = dict(prop="imageinfo", iiprop="url|size|mime|extmetadata")

def gen(generator_params):
    cont = {}
    while True:
        d = call({**generator_params, **IIPROP, "action": "query", **cont})
        yield from info_from_pages(d.get("query", {}).get("pages", []))
        if "continue" not in d: return
        cont = d["continue"]

def cat_files(cat, limit=200):
    n = 0
    for r in gen(dict(generator="categorymembers", gcmtitle=cat, gcmtype="file", gcmlimit=50)):
        yield r; n += 1
        if n >= limit: return

def subcats(cat):
    d = call(dict(action="query", list="categorymembers", cmtitle=cat, cmtype="subcat", cmlimit=200))
    return [m["title"] for m in d["query"]["categorymembers"]]

def find(q, limit=100):
    n = 0
    for r in gen(dict(generator="search", gsrsearch=q, gsrnamespace=6, gsrlimit=50)):
        yield r; n += 1
        if n >= limit: return

if __name__ == "__main__":
    cmd, arg = sys.argv[1], sys.argv[2]
    if cmd == "subcats":
        print("\n".join(subcats(arg)))
    else:
        it = cat_files(arg) if cmd == "cat" else find(arg)
        for r in it: print(json.dumps(r, ensure_ascii=False))
