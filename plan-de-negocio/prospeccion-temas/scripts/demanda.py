#!/usr/bin/env python3
"""Demanda en YouTube de los temas candidatos (prospección, 01-10-2026).

Búsqueda plana con yt-dlp (sin descargar vídeos), 20 resultados por consulta, por relevancia. Mismo método que
`gauntlet3/tema/scripts/buscar.py`. Guarda el JSON de cada consulta en $SCRATCH/prospeccion/cache y no repite.
Después filtra por título (regex de inclusión del tema, exclusión de música/películas) y resume por tema.
Las reglas de filtro las escribió Claude a mano; no hay revisión vídeo a vídeo (ver límites en el README).

Uso: python demanda.py [buscar|resumir]
"""
import hashlib, json, os, re, subprocess, sys, time, unicodedata, statistics

SCRATCH = os.environ.get("SCRATCH", "/tmp/claude-0/-home-user-revolta/a115a1ff-b3a6-5e24-9550-c1877fcd3063/scratchpad")
YTDLP = f"{SCRATCH}/yt/bin/yt-dlp"
CACHE = f"{SCRATCH}/prospeccion/cache"
OUT = os.path.join(os.path.dirname(__file__), "..", "datos")

# tema: (regex de inclusión sobre el título sin tildes, [consultas])
TEMAS = {
    "camino": (r"camino de santiago|cami[nñ]o de santiago|caminho de santiago|compostela|calixtin|botafumeiro|portico de la gloria",
               ["Camino de Santiago historia", "Camino de Santiago para dormir", "Códice Calixtino robo",
                "historia do Camiño de Santiago", "Camino de Santiago sleep story"]),
    "santa_compana": (r"santa compa|santa companha|holy company",
                      ["Santa Compaña", "Santa Compaña para dormir", "Santa Compaña lenda", "Santa Compaña legend"]),
    "teixido": (r"teixido", ["San Andrés de Teixido leyenda", "Santo André de Teixido", "San Andrés de Teixido historia"]),
    "asolagadas": (r"asolagad|sumergid|anegad|antela|valverde|limia|doni[nñ]os|cospeito|bajo el agua|baixo a auga|lagoa|laguna",
                   ["ciudades sumergidas Galicia leyenda", "lagoa de Antela", "cidades asolagadas Galicia",
                    "laguna de Antela pueblo bajo el agua"]),
    "prisciliano": (r"priscili", ["Prisciliano", "Prisciliano tumba de Santiago", "Prisciliano herexe", "Priscillian of Avila"]),
    "viquingos": (r"viking|vikingo|vikinga|viquingo|normand|catoira|torres de oeste|torres do oeste",
                  ["vikingos en Galicia", "Romaría Vikinga Catoira historia", "vikings in Galicia", "viquingos Galicia"]),
    "torre_hercules": (r"torre de h[eé]rcules|tower of hercules|breog",
                       ["Torre de Hércules historia", "Torre de Hércules leyenda", "Tower of Hercules"]),
    "irmandinos": (r"irmandi|hermandin", ["irmandiños", "revuelta irmandiña", "revolta irmandiña historia"]),
    "rande": (r"rande|vigo bay|bahia de vigo|ria de vigo|galeones de vigo",
              ["galeones de Rande", "batalla de Rande", "tesouro de Rande", "Vigo Bay treasure galleons"]),
    "costa_morte": (r"costa da morte|costa de la muerte|serpent|naufragi|naufraxi|raqueir|finisterre|fisterra",
                    ["Costa da Morte naufragios", "Costa da Morte lendas", "HMS Serpent Camariñas", "raqueiros Costa da Morte"]),
    "indianos": (r"indiano|emigra|emigrant|habana|cuba|america",
                 ["indianos gallegos", "emigración gallega a América historia", "casas de indianos Galicia",
                  "emigración galega Cuba"]),
    "baleeiros": (r"balle|bale|whal", ["balleneros gallegos", "caza de ballenas Galicia Caneliñas", "baleeiros Galicia",
                                       "whaling Galicia Spain"]),
    "linguas_secretas": (r"barallete|arxina|xerga|jerga|afiador|afilador|cantei|canter|lingua secreta|lengua secreta",
                         ["barallete afiadores", "afiladores de Ourense historia", "verbo dos arxinas canteiros",
                          "lengua secreta afiladores gallegos"]),
    "serans": (r"ser[aá]n|fiadeir|fiandeir|filand|invierno en la aldea|inverno na aldea|vida rural|aldea",
               ["seráns fiadeiros", "fiadeiros Galicia", "vida en la aldea gallega antigua", "historias de aldea gallega para dormir"]),
    "mosteiros": (r"mosteiro|monasterio|monastery|samos|oseira|sobrado|ribeira sacra|monxes|monjes",
                  ["monasterio de Samos", "monasterio de Oseira", "Ribeira Sacra historia monasterios",
                   "mosteiros de Galicia"]),
    "ouro_castros": (r"castro|castrex|torques|oro|ouro|gallaecia|celta|montefurado",
                     ["castros de Galicia", "oro de los castros torques", "Gallaecia romana oro", "cultura castrexa"]),
    "suevos": (r"suev|suab|gallaecia", ["reino suevo", "reino suevo de Galicia", "suevos Gallaecia", "Suebian kingdom"]),
    "ribarteme": (r"ribarteme|ataud|cadaleit|coffin|romeria|romaria",
                  ["Santa Marta de Ribarteme", "procesión de los ataúdes Galicia", "romerías raras de Galicia"]),
    "horreos": (r"h[oó]rreo|cruceiro|crucero|carnota|lira|hio",
                ["hórreos de Galicia historia", "hórreo de Carnota", "cruceiros de Galicia", "horreo Galicia"]),
    "entroido": (r"entroido|peliqueir|cigarr|pantalla|laza|verin|xinzo|carnaval",
                 ["Entroido de Laza peliqueiros", "cigarróns Verín", "Entroido galego historia", "carnaval gallego tradicional"]),
    "magosto": (r"magosto|casta[nñ]|souto", ["magosto", "castañas Galicia historia", "soutos de castiñeiros"]),
}
EXCL = re.compile(r"official|oficial|videoclip|lyric|letra|\baudio\b|full album|album|en directo|ao vivo|\blive\b|remix|"
                  r"cover|cancion|song|musica|music|trailer|tr[aá]iler|teaser|pelicula|movie|#shorts|tutorial|receta|recipe|"
                  r"vlog|precio|alquiler|venta|inmobiliar|futbol|partido|gol\b")
# Ruido visto al revisar los listados (Claude, a mano, 01-10-2026): homónimos, música, guías prácticas, otros países
EXCL_TEMA = {
    "camino": r"truths|things nobody|translators|everything you need|everything about|what to see",
    "santa_compana": r"top 5|golpes bajos|mago de oz|disco completo",
    "asolagadas": r"^(?!.*(antela|limia|doni[nñ]os|cospeito|galic|galeg|galleg|galiz)).*$",
    "ouro_castros": r"ryan castro|fidel|raul castro|coltan|westcol",
    "baleeiros": r"killer|orca|blue whale|fin whale|bdri|terranova|newfoundland",
    "serans": r"o fiadeiro|explorando|jota|muineira|fox n|pandereteir|afoutos",
    "magosto": r"los castanas|aduanas|\brap\b|es viral",
    "ribarteme": r"vikinga|viking",
    "linguas_secretas": r"rueda de afilar|flauta|cuchillo",
    "indianos": r"asturi|europeos migraron",
    "rande": r"teatro infantil|swimming|nadando",
    "costa_morte": r"ana kiro|luar na lubre|linea 900|turismo|4k|belleza",
    "horreos": r"asturiano|diy|palitos|autocaravana",
    "torre_hercules": r"what to see",
}
SLEEP = re.compile(r"dormir|durmir|sleep|asmr|lluvia|chuva|rain\b|relaj|relax")


def norm(s):
    s = unicodedata.normalize("NFD", s or "")
    return "".join(c for c in s if unicodedata.category(c) != "Mn").lower()


def cache_path(q):
    return os.path.join(CACHE, hashlib.md5(q.encode()).hexdigest() + ".jsonl")


def buscar():
    os.makedirs(CACHE, exist_ok=True)
    for tema, (_, qs) in TEMAS.items():
        for q in qs:
            p = cache_path(q)
            if os.path.exists(p) and os.path.getsize(p) > 0:
                continue
            r = subprocess.run([YTDLP, "--flat-playlist", "-j", "--extractor-args",
                                "youtube:player_client=android_vr", "--extractor-args", "youtubetab:approximate_date",
                                f"ytsearch20:{q}"], capture_output=True, text=True, timeout=120)
            open(p, "w").write(r.stdout)
            print(tema, q, len(r.stdout.splitlines()), r.stderr[-200:] if not r.stdout else "", flush=True)
            time.sleep(1.5)


def resumir():
    filas, crudo = [], []
    for tema, (inc, qs) in TEMAS.items():
        vistos = {}
        for q in qs:
            p = cache_path(q)
            if not os.path.exists(p):
                continue
            for l in open(p):
                try:
                    v = json.loads(l)
                except Exception:
                    continue
                t = norm(v.get("title"))
                ok = bool(re.search(inc, t)) and not EXCL.search(t) and not (
                    tema in EXCL_TEMA and re.search(EXCL_TEMA[tema], t))
                crudo.append((tema, q, ok, v.get("view_count") or 0, (v.get("duration") or 0) // 60,
                               v.get("upload_date") or "", v.get("channel") or "", v.get("title") or "",
                               f"https://youtu.be/{v.get('id')}"))
                if ok:
                    vistos[v["id"]] = v
        vs = sorted(vistos.values(), key=lambda v: -(v.get("view_count") or 0))
        views = [v.get("view_count") or 0 for v in vs]
        dormir = [v for v in vs if SLEEP.search(norm(v.get("title")) + " " + norm(v.get("channel")))]
        rec = [v for v in vs if (v.get("upload_date") or "0") >= "20250101" and (v.get("view_count") or 0) > 10000]
        top = vs[0] if vs else {}
        filas.append(dict(tema=tema, n=len(vs), m10k=sum(x > 10_000 for x in views), m100k=sum(x > 100_000 for x in views),
                          mediana=int(statistics.median(views)) if views else 0, maximo=views[0] if views else 0,
                          max_url=f"https://youtu.be/{top.get('id')}" if top else "", max_titulo=top.get("title", ""),
                          max_canal=top.get("channel", ""), dormir=len(dormir),
                          dormir_max=max([d.get("view_count") or 0 for d in dormir], default=0),
                          dormir_url=f"https://youtu.be/{max(dormir, key=lambda d: d.get('view_count') or 0)['id']}" if dormir else "",
                          recientes_10k=len(rec)))
    os.makedirs(OUT, exist_ok=True)
    json.dump(filas, open(os.path.join(OUT, "demanda-resumen.json"), "w"), ensure_ascii=False, indent=1)
    with open(os.path.join(OUT, "busquedas-yt.tsv"), "w") as f:
        f.write("tema\tconsulta\tcuenta\tvistas\tmin\tfecha_aprox\tcanal\ttitulo\turl\n")
        for r in crudo:
            f.write("\t".join(str(x).replace("\t", " ") for x in r) + "\n")
    for r in sorted(filas, key=lambda r: (-r["m10k"], -r["maximo"])):
        print(f"{r['tema']:17} n={r['n']:3} >10K={r['m10k']:2} >100K={r['m100k']:2} med={r['mediana']:>8} "
              f"max={r['maximo']:>9} dormir={r['dormir']}/{r['dormir_max']} rec10k={r['recientes_10k']} | {r['max_titulo'][:60]}")


if __name__ == "__main__":
    {"buscar": buscar, "resumir": resumir}[sys.argv[1] if len(sys.argv) > 1 else "resumir"]()
