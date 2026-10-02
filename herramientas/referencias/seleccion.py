"""Construye la selección final (seleccion.json) desde datos/*.jsonl. Heurística + listas manuales; ver README."""
import json, re, glob, collections, html
from curar import pick, lic_ok, score

EXCL = re.compile(r"lotería|LNAP|Dark Dancers|BANDA DE GAITAS|Haahla|Castro de Vigo|Lareira Mós|Targ niew|\.djvu|\.pdf|\.webm|Cantigas\.(PNG)|Machado|Jornal|mulheres|sertanejo", re.I)
MANUAL12 = ["Afonso II o Casto, de Oviedo (Tumbo A), r.jpg","Afonso III o Magno (Tumbo A), r.jpg","Bispo Teodomiro.jpg","Adeffonsus rex legionensium et gallecie.jpg",
 "Fernando II de Galicia e Leon no tombo A.jpg","Fernando III como rei de Castela e Toledo e de Galiza e Leon no Tombo A.jpg",
 "Caballeria Cantiga 106.jpg","Cantigas de Santa Maria. Codice de El Escorial. Cantiga 123 miniaturas.jpg","Miniatura representant l’exèrcit almohade.jpg"]
CAP12 = {"Pambre":2,"Monterrei":2,"Sobroso":1,"Ribadavia":1,"Oseira":1,"capitals":2,"corbels":4}
Met_KEEP = re.compile(r"1[3-7]\d\d|1[4-7]th|late 15th|16th|17th", re.I)

def norm(r, conc, tipo="foto", notas=""):
    a = r["author"].split("\n")[0].strip() or "Autor no indicado"
    lic = r["license"]
    return dict(concepto=conc, titulo=r["title"].replace("File:", ""), url_pagina=r["page"], url_imagen=r["url"].split("?")[0], autor=a, licencia=lic,
                resolucion=f"{r['w']}x{r['h']}", epoca=(r["date"] or "")[:30], tipo=tipo, sa=("SA" in lic), notas=notas, score=r.get("score", 0), fuente="Wikimedia Commons")

def main():
    out = {}
    for f in sorted(glob.glob("datos/[0-9]*.jsonl")):
        conc = f.split("/")[-1][:-6]
        if conc in ("12b-canecillos", "13-armas-ropa"): continue
        rows = [json.loads(l) for l in open(f) if not EXCL.search(l.split('"title": ')[1][:160] if '"title": ' in l else "")]
        rows = [r for r in rows if r["mime"] in ("image/jpeg", "image/png") and not EXCL.search(r["title"])]
        if conc == "12-iconografia":
            rows += [json.loads(l) for l in open("datos/12b-canecillos.jsonl")]
            rows = [r for r in rows if r["mime"] in ("image/jpeg","image/png")]
            sel = []; cnt = collections.Counter()
            for r in pick([r for r in rows if not r["origen"].startswith("find")], conc, n=200, per_author=3):
                key = next((k for k in CAP12 if k.lower() in r["origen"].lower()), None)
                if key is None or cnt[key] >= CAP12[key]: continue
                cnt[key] += 1; sel.append(norm(r, conc, notas=f"{key}"))
            for t in MANUAL12:
                for r in rows:
                    if r["title"] == "File:" + t and lic_ok(r["license"]):
                        r["score"] = 5; sel.append(norm(r, conc, tipo="miniatura/grabado", notas="Escaneo de manuscrito/obra antigua (dominio público por antigüedad de la obra; verificar)")); break
            out[conc] = sel
        else:
            out[conc] = [norm(r, conc) for r in pick(rows, conc, n=16)]
    # 13: Met CC0 + algo de Commons
    met = [json.loads(l) for l in open("datos/met.jsonl")]
    cnt = collections.Counter(); sel = []
    for m in met:
        if m["obj"] not in ("Rapier","Cup-hilted rapier","Sword","Early sword","Helmet","Helmet (Sallet)","Sallet","Cabasset","War hat","Shield (Adarga)","Sword with scabbard","Close-helmet","Transitional Rapier","Smallsword") or not Met_KEEP.search(m["date"]): continue
        if m["obj"] in cnt and cnt[m["obj"]] >= 3: continue
        cnt[m["obj"]] += 1
        sel.append(dict(concepto="13-armas-ropa", titulo=f"{m['title']} ({m['date']})", url_pagina=m["page"], url_imagen=m["img"], autor=(m["artist"] or m["culture"] or "The Met (autoría no indicada)"),
            licencia="CC0 (The Met Open Access)", resolucion="no verificada (original del Met, normalmente >2000 px)", epoca=m["date"], tipo="objeto de museo (foto)", sa=False,
            notas=f"{m['culture']}; {m['credit']}", score=6, fuente="The Met Open Access"))
    out["13-armas-ropa"] = sel[:18]
    json.dump(out, open("seleccion.json", "w"), ensure_ascii=False, indent=1)
    for k, v in out.items(): print(k, len(v))
main()
