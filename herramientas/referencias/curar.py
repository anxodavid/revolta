"""Puntúa y selecciona candidatos a partir de datos/*.jsonl (metadatos de Commons y Met) -> candidatos.json.
La puntuación es HEURÍSTICA (título/descripción, resolución, categoría de calidad); no sustituye a la revisión visual."""
import json, re, glob, collections, sys
import commons

POS = {
 "01-horreo": ["hórreo","horreo","hórreos","horreos"],
 "02-carro-bois": ["carro","carreta","cart","bois","bueyes","xugo","yugo","yoke","ox"],
 "03-palloza-casa": ["palloza","pallozas","lousa","pizarra","casa","granito","aldea","aldeia"],
 "04-pazo": ["pazo","palomar","capela","capilla","fachada","patio","torre"],
 "05-cruceiro-peto": ["cruceiro","peto","ánimas","animas","shrine","cross"],
 "06-cocina": ["lareira","cociña","cocina","escano","pote","gramalleira","lacena","cunca","kitchen","hearth","fogar"],
 "07-queimada": ["queimada"],
 "08-traje": ["traxe","traje","costume","refaixo","dengue","mantelo","montera","zoca","clog","coroza","dress","gaita","vestimenta"],
 "09-herramientas": ["arado","grade","fouce","sacho","mallo","roca","fuso","tear","loom","plough","plow","spinning","ferramenta","hoz","azada"],
 "10-muino-fonte": ["muíño","muino","molino","mill","batán","batan","fonte","fuente","lavadoiro","lavadero","wash house"],
 "11-barcos-costa": ["dorna","gamela","traiñeira","trainera","boat","barco","bote","embarcación","ría","costa"],
 "12-iconografia": ["canecillo","corbel","capitel","capital","castelo","castle","castillo","torre","miniatur","grabado","engraving","pambre","sobroso","monterrei","tumbo","cantigas"],
 "13-armas-ropa": ["armor","armour","armadura","sword","espada","helmet","morion","arquebus","costume","escribano","halberd","crossbow","print"],
 "14-samos-antiguo": ["samos","claustro","cloister","anderson","aldea","1910","1920","igrexa","iglesia"],
}
NEG = ["map","mapa","logo","escudo","flag","bandera","diagram","screenshot","pdf","wappen","coat of arms","locator"]
OKLIC = re.compile(r"^(cc0|public domain|pd[- ]|pdm|cc[- ]by\b|cc[- ]by[- ]sa\b|cc by|cc[- ]zero|attribution)", re.I)
BADLIC = re.compile(r"\b(nc|nd|gfdl only|fair use|all rights)\b", re.I)

def lic_ok(l):
    return bool(OKLIC.match(l)) and not BADLIC.search(l) and not re.search(r"by-(nc|nd)", l, re.I)

def score(r, conc):
    s = 0; t = (r["title"] + " " + r["desc"]).lower()
    if max(r["w"], r["h"]) >= 1024: s += 2
    if max(r["w"], r["h"]) >= 2000: s += 1
    if r["mime"] != "image/jpeg" and r["mime"] != "image/png": s -= 10
    hit = sum(1 for k in POS[conc] if k in t); s += min(hit, 3) * 2
    if "Quality images" in r["origen"] or "quality image" in t: s += 2
    if any(n in t for n in NEG): s -= 6
    if r["restrictions"]: s -= 4
    if "unidentified" in r["author"].lower() or not r["author"]: s -= 1
    return s

def pick(rows, conc, n=16, per_author=4):
    rows = [r for r in rows if lic_ok(r["license"]) and max(r["w"], r["h"]) >= 1024]
    rows.sort(key=lambda r: -score(r, conc))
    out, authors, stems = [], collections.Counter(), set()
    for r in rows:
        a = r["author"][:40]
        stem = re.sub(r"[\d_\-\. ]+\w{3,4}$", "", r["title"])[:35]
        if authors[a] >= per_author or stem in stems: continue
        authors[a] += 1; stems.add(stem); r["score"] = score(r, conc); out.append(r)
        if len(out) >= n: break
    return out

if __name__ == "__main__":
    res = {}
    for f in sorted(glob.glob("datos/[0-9]*.jsonl")):
        conc = f.split("/")[-1][:-6]
        rows = [json.loads(l) for l in open(f)]
        res[conc] = dict(total=len(rows), libres=sum(lic_ok(r["license"]) for r in rows), sel=pick(rows, conc))
        print(conc, res[conc]["total"], res[conc]["libres"], len(res[conc]["sel"]))
    json.dump(res, open("candidatos.json", "w"), ensure_ascii=False, indent=1)
