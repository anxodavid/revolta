#!/usr/bin/env python3
"""Resumen por tema de las búsquedas: vídeos únicos pertinentes, >10K, mediana, máximo, formato para dormir, galego."""
import json, os, re, sys, statistics, unicodedata
sys.path.insert(0, os.path.dirname(__file__))
from buscar import REL, VIS, CACHE, slug


def norm(s):
    s = unicodedata.normalize("NFD", s or "")
    return "".join(c for c in s if unicodedata.category(c) != "Mn").lower()


# Título pertinente al tema (sin tildes, minúsculas)
TOPIC = {
    "meigas": r"meiga|bruxa|bruja|witch|soli[nñ]a|inquisici|habelas|haberlas",
    "queimada": r"queimada|conxuro|conjuro",
    "santa_compana": r"compa[nñ]|companha|holy company|holy compa",
    "san_xoan": r"san xoan|san juan|sao joao|saint john|st\.? john",
    "muineira": r"mui[nñ]eira|gaita|bagpipe",
    "mouras": r"moura|mouro|castro|tesour|tesoro|treasure|encantad",
    "romasanta": r"romasanta|lobishome|lobisome|hombre lobo|home lobo|werewolf|allariz|lobis",
    "rande": r"rande|galeon|galleon|vigo",
    "maria_pita": r"maria pita|pita",
    "camino": r"camino|camino|cami[nñ]o|caminho|santiago|compostela|pilgrim|peregrin",
    "samain": r"samain|samhain|samaim|calacu",
    "teixido": r"teixido",
    "costa_morte": r"costa da morte|costa de la muerte|coast of death|naufrag|shipwreck",
    "celtas": r"celt",
    "magosto": r"magosto",
    "xeral": r"galicia|galiza|galeg|gallego|gallega|galician",
    "comparable": r"witch|bruj|bruxa|leyend|lenda|legend|zugarramurdi",
}
SLEEP = r"dormir|durmir|sleep|duerm|asmr|bedtime|relax|para descansar|to fall asleep"
MUSIC = (r"official|oficial|videoclip|video clip|\baudio\b|lyric|letra|disco completo|album|concierto|concerto|en directo|"
         r"\blive\b|remix|feat\.|cover|canci[oó]n|cancion|song|\bmusic|musica|m[uú]sica|orquesta|banda de gaitas|"
         r"tutorial|karaoke|partitura|sheet music|como tocar|how to play|1h\b|1 hora|hour")
# palabras frecuentes en títulos galegos y raras en castellano/portugués
GL = r"\b(unha|galiza|galega|galegas|galego|galegos|lendas|lenda|durmir|xente|noite|conxuro|historia da|historia de galicia en galego|cando|moito|nosa|nosas|dos mouros|das meigas|coñece|coñecer|lume|mariñ|aldea galega|contos|conto|traxedia|as bruxas|os mouros|tamén|agora|porque non|ollo)\b"


def cargar(key):
    path = os.path.join(CACHE, key + ".jsonl")
    with open(path) as f:
        return [json.loads(l) for l in f if l.strip()]


def main():
    vids = {}  # id -> dict
    por_tema = {}
    for tema, lang, q in REL:
        for d in cargar("rel_" + slug(q)):
            vids[d["id"]] = d
            por_tema.setdefault(tema, {}).setdefault(d["id"], set()).add(("rel", lang, q))
    for tema, q in VIS:
        for d in cargar("vis_" + slug(q)):
            vids[d["id"]] = d
            por_tema.setdefault(tema, {}).setdefault(d["id"], set()).add(("vis", "-", q))

    detalle = "--detalle" in sys.argv
    filas = []
    for tema, ids in por_tema.items():
        pat = TOPIC[tema]
        pert = []
        for i in ids:
            d = vids[i]
            t = norm(d.get("title")) + " " + norm(d.get("description") or "")[:0]
            if re.search(pat, norm(d.get("title"))):
                pert.append(d)
        narr = [d for d in pert if not re.search(MUSIC, norm(d.get("title")))]
        mus = [d for d in pert if re.search(MUSIC, norm(d.get("title")))]
        vs = [d.get("view_count") or 0 for d in narr]
        sleep = [d for d in narr if re.search(SLEEP, norm(d.get("title")))]
        gl = [d for d in narr if re.search(GL, norm(d.get("title")))]
        fila = dict(tema=tema, n_total=len(ids), n_pert=len(pert), n_mus=len(mus), n_narr=len(narr),
                    n10k=sum(v > 10000 for v in vs), n100k=sum(v > 100000 for v in vs),
                    mediana=int(statistics.median(vs)) if vs else 0, maximo=max(vs) if vs else 0,
                    suma=sum(vs),
                    sleep_max=max([d.get("view_count") or 0 for d in sleep], default=0), n_sleep=len(sleep),
                    n_gl=len(gl), gl_max=max([d.get("view_count") or 0 for d in gl], default=0))
        filas.append(fila)
        if detalle and (len(sys.argv) < 3 or tema in sys.argv[2:]):
            print(f"\n######## {tema}: {len(narr)} narrativos, {len(mus)} música/otros (pertinentes {len(pert)} de {len(ids)})")
            for d in sorted(narr, key=lambda d: -(d.get('view_count') or 0)):
                flags = ("S" if re.search(SLEEP, norm(d.get('title'))) else "-") + ("G" if re.search(GL, norm(d.get('title'))) else "-")
                print(f"{(d.get('view_count') or 0):>9} {flags} {d.get('upload_date','?')[:6]} {int(d.get('duration') or 0):>6}s | {(d.get('channel') or '')[:28]:28} | {d.get('title')[:95]} | {d['id']}")
            print("  -- música/otros:")
            for d in sorted(mus, key=lambda d: -(d.get('view_count') or 0))[:8]:
                print(f"{(d.get('view_count') or 0):>9}    {d.get('upload_date','?')[:6]} {int(d.get('duration') or 0):>6}s | {(d.get('channel') or '')[:28]:28} | {d.get('title')[:95]} | {d['id']}")
    if not detalle:
        print(f"{'tema':14} {'total':>5} {'pert':>4} {'mús':>4} {'narr':>4} {'>10K':>4} {'>100K':>5} {'mediana':>8} {'máximo':>9} {'suma':>9} {'nSleep':>6} {'maxSleep':>8} {'nGL':>4} {'maxGL':>7}")
        for f in sorted(filas, key=lambda f: -f['suma']):
            print(f"{f['tema']:14} {f['n_total']:5} {f['n_pert']:4} {f['n_mus']:4} {f['n_narr']:4} {f['n10k']:4} {f['n100k']:5} {f['mediana']:8} {f['maximo']:9} {f['suma']:9} {f['n_sleep']:6} {f['sleep_max']:8} {f['n_gl']:4} {f['gl_max']:7}")


main()
