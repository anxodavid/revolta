"""Metadatos de The Met Open Access (CC0) para armas, armaduras y grabados hispanos. No descarga imágenes."""
import json, sys, time, urllib.request, urllib.parse
B = "https://collectionapi.metmuseum.org/public/collection/v1/"
def get(u):
    for i in range(5):
        try:
            with urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "revolta-refs/0.1"}), timeout=30) as r:
                time.sleep(0.4); return json.load(r)
        except Exception as e:
            print("#", e, file=sys.stderr); time.sleep(5 * (i + 1))
QUERIES = sys.argv[1:] or ["Spanish armor","Spanish sword rapier","Spanish helmet morion","Spanish crossbow","Spanish arquebus","Spain costume 16th century print","Spanish peasant costume print","Spanish halberd","Spanish shield rodela","Spanish dagger","Spanish breastplate"]
seen = {}
for q in QUERIES:
    d = get(B + "search?" + urllib.parse.urlencode({"q": q, "isPublicDomain": "true", "hasImages": "true"}))
    ids = (d or {}).get("objectIDs") or []
    print("#", q, len(ids), file=sys.stderr)
    for i in ids[:40]:
        if i in seen: continue
        o = get(B + f"objects/{i}")
        if not o or not o.get("isPublicDomain") or not o.get("primaryImage"): continue
        blob = " ".join(str(o.get(k, "")) for k in ("culture", "title", "country", "region", "objectName")).lower()
        if not any(w in blob for w in ("spain", "spanish", "españ", "toledo", "seville", "galicia", "catalan", "castil")): continue
        seen[i] = dict(id=i, title=o["title"], date=o["objectDate"], culture=o["culture"], obj=o["objectName"], dept=o["department"],
                       page=o["objectURL"], img=o["primaryImage"], credit=o["creditLine"], artist=o["artistDisplayName"], q=q)
        print(json.dumps(seen[i], ensure_ascii=False), flush=True)
