#!/usr/bin/env python3
"""Clasificación limpia por tema: vídeos NARRATIVOS sobre el tema (documental, pódcast, lenda narrada, explicación,
reportaje, historia para dormir). Excluye música, películas/tráilers, homónimos, guías prácticas de viaje y ruido.

Salida: tabla por tema + listas de control (--lista tema).
Reglas de exclusión escritas por Claude a mano tras revisar los listados (30-09-2026).
"""
import json, os, re, sys, statistics, unicodedata
sys.path.insert(0, os.path.dirname(__file__))
from buscar import REL, VIS, CACHE, slug


def norm(s):
    s = unicodedata.normalize("NFD", s or "")
    return "".join(c for c in s if unicodedata.category(c) != "Mn").lower()


# El título (sin tildes) debe casar con esto para contar como "sobre el tema"
INCL = {
    "meigas": r"meiga|soli[nñ]a|(bruxa|bruja|witch|inquisici).*(galic|galeg|galleg|galiza|maside|cangas)|(galic|galeg|galleg|galiza).*(bruxa|bruja|witch|inquisici)",
    "queimada": r"queimada|conxuro",
    "santa_compana": r"santa compa|santa companha|holy company|procession of the souls",
    "san_xoan": r"san xoan|san juan|saint john|st\. john",
    "muineira": r"mui[nñ]eira|gaita",
    "mouras": r"moura|mouros|tesouro dos|castros? .*(lend|leyend|tesor)",
    "romasanta": r"romasanta|lobishome|hombre lobo de allariz|werewolf of (allariz|galicia)|home lobo",
    "rande": r"rande|vigo bay|ria de vigo|bahia de vigo|galleon",
    "maria_pita": r"maria pita|contra ?armada",
    "camino": r"camino de santiago|cami[nñ]o de santiago|caminho de santiago|santiago de compostela|santiago apostol",
    "samain": r"samain|calacus|samhain.*(galic|galiz)|(galic|galiz).*samhain|samanos",
    "teixido": r"andres de teixido|andre de teixido",
    "costa_morte": r"costa da morte|serpent",
    "celtas": r"celt|castro",
    "magosto": r"magosto",
}
# Exclusiones comunes: música, películas, cortos de ficción, homónimos, recetas sin relato, guías prácticas
EXCL_COMUN = (r"official|oficial|videoclip|lyric|letra|\baudio\b|disco completo|full album|album|en directo|ao vivo|\blive\b|"
              r"remix|feat\.|\bft\.? |cover|cancion|song|musica|music|orquesta|banda |tutorial|partitura|coro |"
              r"trailer|tr[aá]iler|spot|teaser|pelicula|movie|film|lektor|dublado|end credits|clip \d|"
              r"#shorts|shorts|draw my life en espanol")
EXCL = {
    "meigas": r"lunabia|luar na lubre|carlos nu[nñ]ez|mago de oz|astarot|habelas hainas -|habelas hainas \"|ana kiro|tanxugueiras|"
              r"escola maria soli|acorde secreto|wyrdamur|ledicia|maria do ceo|teatro|claymore|pampurrias|jurema|salem|romenia|"
              r"zugarramurdi|witch vlog|terra de meigas \(|unhas meigas|garage|hockey|paixon de maria soli|a paixon|"
              r"rastrexo|basque|mi vida en el rural|gaita gallega|opinan sobre literatura|bella ciao|laranxi|corridinho|solsticio|ledicia costas|soportujar|queimadas in",
    "queimada": r"mago de oz|masterchef|pota o cazuela|record|capricho|actio|eventos y bodas",
    "santa_compana": r"mago de oz|golpes bajos|los suaves|santa companha -|santa companha @|santa companha  -|la brecha|luz azul|"
                     r"nano mz|432hz|ambient|top 5 leyendas|a costa da rock|lance de honor|en directo|how to win|castilla",
    "san_xoan": r"hey kid|sergio dalma|nando agueros|gallina pintadita|galicia 112|061|camposa|na lua|ana kiro|susana de lorenzo|"
                r"lenda artabra|anxo araujo|crimen|queimada|boricua|europa press|el pais|turismo|concello|must|clases de espa",
    "muineira": r"chantada|muineira de lugo|santo amaro|treixadura|noitarega|folk dances|dance|gadis|flashmob|coreograf|bailar|ronda|silvela|"
                r"brandenburgo|cantigas e agarimos|tanxugueiras|ceo do sil|xabier diaz|lagares|rodrigo cuevas|escocesa|"
                r"em do|jota|ronquilhos|raina da gaita|pequeno principe|luques|willian paiva|orixe da gaita - rafael|zulianidad",
    "mouras": r"ana moura|fidel castro|d pedro|puglia|tesouro direto|tesouro precioso|josue de castro|navio negreiro|"
              r"almirante|rande|sintra|castelo dos mouros|castro de oleiros|sao lourenco|cabeco de vide|prestige|fado|"
              r"almadense|alcacer|feira medieval|promocional|feminis|pin y pon|val das mouras|mogadouro|buraco dos mouros|"
              r"airinos|capela da fame",
    "romasanta": r"soledad|cruel dolor|sin ti|bajo mi voz|mix |lobishome -|lobishome, 240m|pe[nñ]as del prado|bulldozers|fuzzbombs|"
                 r"gravesen|festin|dioivo|berta franklin|mal de altitud|fobias|valdelana|la radio|colectivo lobishome|"
                 r"transformation|wolf tf|camino do lobishome|lobishome\.\.\.|avance lobishome|caza de la bestia|werewolf hunt|"
                 r"la casa da besta|casa da besta|romasanta \(2004\)|romasanta - trailer|el rugir|por las noches|sobreviviendo|"
                 r"lenguaje de dolor|alverez|luar na lubre|cantar de romasanta",
    "rande": r"nadando|swimming|natacion|travesia|a  nado|nado|puente de rande|ponte de rande|driving|recorrido|organizaci|"
             r"teatro infantil|castillo de rande|cove|pontes|interpretacion de rande podra|codax|presentacion libro|"
             r"batalla de rande 20|17 billion|loli paz|redondela\"|josefa calvar|kodama|humildad|sabunya|i\.a\.|firearms",
    "maria_pita": r"eli soares|pita amor|maria felix|moises andrade|deus nao|lunnis|ecceperdomo|cantora|pitache|swan lake|"
                  r"sou teu pai|reacciona|hunter files|historia sin fronteras",
    "camino": r"presupuesto|material necesario|equipaje|packing|empacan|reservations|hostel|albergue|sleeping bag|saco de dormir|"
              r"where to sleep|donde dormir|dormir bien|sleeping outdoors|tips|consejos|what to bring|que llevar|antes de hacer|"
              r"new rules|nobody talks|15 dias|etapa|money|assista antes|nao faca|scared|sarria|translators|app|"
              r"central portuguese way|camino ingles|camino guide|my story|not an ordinary|raul ferreira|piti|nick living|"
              r"robscamino|explain it|guia de viagem|pies y pedales|walking in spain|vida de mochila|in 14 minutes|"
              r"arqui\.cultura|curiosidades sobre o caminho|mountain shop|days we spend|caminotellers|buen camino|tubuencamino|"
              r"berta pim|itziar|travel light|carme fontanet|backcountry|abcfit|qntlc|meditation music|spanish for the camino|"
              r"language teacher|7 rutas|paco nadal|passo a passo|everything you need|everything about|guide from routes|what is the camino|estadao",
    "samain": r"brinca vai|uxia lambona|loreena|lisa thiel|selena sorvino|let the day begin|samain night|ratomik|"
              r"samhain - samhain|no time to lose|vibrations of doom|monstrinos|muineira do samain|nueche|ganchillo|"
              r"estrella galicia|cerveza|party|maquillaxe|promo samhain|hago periodismo|wicca|anima despertar|terapias|"
              r"back to school|our life in|apbvigo|catabois|garray|scottish|rte kids|highlands|aventura de nera",
    "teixido": r"michael teixido|non para a misa|ares teixido|oscar teixido|jose teixido|cucuza|ernesto castro|4k|fpv|drone|footage|"
               r"rochinha|cezarmario|vlog it|matthew 25",
    "costa_morte": r"4k|concerto|trailer|spot|camari[nñ]as en costa|faros en|60 segundos|60secspain|driving|bucear|drone|carballo\. senda|"
                   r"pinceladas|recovecos|5,200 km|capitulo 4|anime style|dolphin|castro de borneiro|amar o mar|top turismo|"
                   r"conoce a costa|hidden places|incredible places|increible|descubrindo|la odisea|luna misteriosa|muxia, la furza",
    "celtas": r"^$",
    "magosto": r"rap do magosto|cancion|salta castana|2016|2017|2022|2025|2011|2012|en 2|na escola|de d\.o\.|bierzo|cacabelos|riotorto|laredo",
}
# Formato "para dormir"
SLEEP = r"dormir|durmir|sleep|duerm|asmr|bedtime|calm the mind|calmar la mente|antes de dormir|to fall asleep|lluvia|rainy|chuva|\brain\b"
# Galego (título): marcas galegas y ausencia de marcas portuguesas
GL = r"\b(unha|galiza|galega|galegas|galego|galegos|lendas|durmir|xente|noite|conxuro|mitoloxia|conece|coñece|tamen|orixe|cando|moito|nosa|historia da|historia do|contos|lume|traxedia|as meigas|os mouros|a gaita galega|queimada galega|meigas galegas|naqueles|peregrinacion dos mortos|o samain|do samain|a moura)\b"
PT = r"ção|ções|ão\b|õe|você|história|mistério|galícia|lenda que não|bruxas da romênia|portugu|lendas de portugal|caminho"


def cargar(key):
    with open(os.path.join(CACHE, key + ".jsonl")) as f:
        return [json.loads(l) for l in f if l.strip()]


def datos():
    vids, por_tema = {}, {}
    for tema, lang, q in REL:
        for d in cargar("rel_" + slug(q)):
            vids[d["id"]] = d
            por_tema.setdefault(tema, set()).add(d["id"])
    for tema, q in VIS:
        for d in cargar("vis_" + slug(q)):
            vids[d["id"]] = d
            por_tema.setdefault(tema, set()).add(d["id"])
    return vids, por_tema


NO_GL = r"el camino verde|nemeton|frightful kitchen|videos bos|gypaetus|judicael|^queimada gallega$|comenta y habla|belinda|jose luis viajero|en espanol"


def es_gl(d):
    t = d.get("title") or ""
    c = norm(d.get("channel")) + " " + norm(t)
    return bool(re.search(GL, norm(t))) and not re.search(PT, t.lower()) and not re.search(NO_GL, c)


def limpios(tema, vids, ids):
    out = []
    for i in ids:
        d = vids[i]
        t = norm(d.get("title")) + " | " + norm(d.get("channel"))
        tt = norm(d.get("title"))
        if not re.search(INCL[tema], tt):
            continue
        if re.search(EXCL_COMUN, t) or re.search(EXCL[tema], t):
            continue
        out.append(d)
    return out


def main():
    vids, por_tema = datos()
    if "--lista" in sys.argv:
        for tema in sys.argv[2:]:
            L = limpios(tema, vids, por_tema[tema])
            print(f"\n######## {tema}: {len(L)} limpios")
            for d in sorted(L, key=lambda d: -(d.get('view_count') or 0)):
                fl = ("S" if re.search(SLEEP, norm(d.get('title')) + ' ' + norm(d.get('channel'))) else "-") + ("G" if es_gl(d) else "-")
                print(f"{(d.get('view_count') or 0):>9} {fl} {(d.get('upload_date') or '?')[:6]} {int(d.get('duration') or 0):>6}s | {(d.get('channel') or '')[:26]:26} | {(d.get('title') or '')[:90]} | {d['id']}")
        return
    filas = []
    for tema in INCL:
        L = limpios(tema, vids, por_tema[tema])
        vs = sorted([d.get("view_count") or 0 for d in L], reverse=True)
        big = [d for d in L if (d.get("view_count") or 0) > 10000]
        anos = sorted(int((d.get("upload_date") or "0000")[:4]) for d in big)
        sl = [d for d in L if re.search(SLEEP, norm(d.get("title")) + " " + norm(d.get("channel")))]
        gl = [d for d in L if es_gl(d)]
        rec = [d for d in L if (d.get("upload_date") or "0") >= "20250901"]
        def top(L2):
            L2 = sorted(L2, key=lambda d: -(d.get("view_count") or 0))
            return (L2[0].get("view_count") or 0, L2[0]["id"], (L2[0].get("channel") or ""), (L2[0].get("title") or ""), (L2[0].get("upload_date") or "")[:6]) if L2 else None
        recbig = sorted(big, key=lambda d: d.get("upload_date") or "", reverse=True)
        filas.append(dict(top=top(L), top_sleep=top(sl), top_gl=top(gl),
            rec_big=((recbig[0].get("view_count") or 0, recbig[0]["id"], recbig[0].get("channel"), recbig[0].get("title"), (recbig[0].get("upload_date") or "")[:6]) if recbig else None),
            tema=tema, n=len(L), n10k=len(big), n100k=sum(v > 100000 for v in vs),
            med=int(statistics.median(vs)) if vs else 0, max=vs[0] if vs else 0,
            anio_med=int(statistics.median(anos)) if anos else None,
            n_sleep=len(sl), max_sleep=max([d.get("view_count") or 0 for d in sl], default=0),
            n_gl=len(gl), max_gl=max([d.get("view_count") or 0 for d in gl], default=0),
            n_rec=len(rec), max_rec=max([d.get("view_count") or 0 for d in rec], default=0)))
    print(f"{'tema':14} {'n':>4} {'>10K':>5} {'>100K':>6} {'mediana':>8} {'máximo':>9} {'año med >10K':>12} {'nDormir':>7} {'maxDormir':>9} {'nGL':>4} {'maxGL':>7} {'n12m':>5} {'max12m':>8}")
    for f in sorted(filas, key=lambda f: -f['n10k']):
        print(f"{f['tema']:14} {f['n']:4} {f['n10k']:5} {f['n100k']:6} {f['med']:8} {f['max']:9} {str(f['anio_med']):>12} {f['n_sleep']:7} {f['max_sleep']:9} {f['n_gl']:4} {f['max_gl']:7} {f['n_rec']:5} {f['max_rec']:8}")
    json.dump(filas, open(os.path.join(os.path.dirname(__file__), "tabla.json"), "w"), ensure_ascii=False, indent=1)


main()
