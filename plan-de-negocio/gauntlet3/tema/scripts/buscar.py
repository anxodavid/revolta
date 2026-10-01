#!/usr/bin/env python3
"""Búsquedas en YouTube con yt-dlp (sin descargar vídeos) para la pieza TEMA del Gauntlet 3.

Guarda el JSON plano de cada consulta en cache/ y no repite las que ya están.
Uso: python buscar.py
"""
import json, os, subprocess, sys, time, urllib.parse, hashlib

SCRATCH = "/tmp/claude-0/-home-user-revolta/a8c9798c-edc6-5719-beda-018861fa4d7d/scratchpad"
YTDLP = f"{SCRATCH}/yt/bin/yt-dlp"
CACHE = f"{SCRATCH}/tema/cache"
os.makedirs(CACHE, exist_ok=True)

N = 20  # resultados por consulta (orden por relevancia)
NV = 20  # resultados por consulta (orden por vistas)

# (tema, idioma, consulta)
REL = [
    # meigas / bruxería (lenda e historia real)
    ("meigas", "es", "meigas de Galicia"),
    ("meigas", "gl", "meigas galegas"),
    ("meigas", "gl", "bruxas galegas"),
    ("meigas", "es", "brujas gallegas"),
    ("meigas", "es", "brujas de Galicia para dormir"),
    ("meigas", "es", "Inquisición en Galicia brujas"),
    ("meigas", "gl", "María Soliña"),
    ("meigas", "en", "Galician witches"),
    ("meigas", "gl", "habelas hainas"),
    ("meigas", "pt", "bruxas da Galiza"),
    # queimada
    ("queimada", "gl", "queimada conxuro"),
    ("queimada", "es", "conjuro de la queimada"),
    ("queimada", "es", "queimada gallega historia"),
    ("queimada", "en", "queimada Galician ritual"),
    # Santa Compaña
    ("santa_compana", "es", "Santa Compaña"),
    ("santa_compana", "es", "Santa Compaña para dormir"),
    ("santa_compana", "gl", "Santa Compaña lenda"),
    ("santa_compana", "pt", "Santa Companha"),
    ("santa_compana", "en", "Santa Compaña legend"),
    # San Xoán
    ("san_xoan", "gl", "noite de San Xoán"),
    ("san_xoan", "es", "noche de San Juan Galicia"),
    # muiñeira / gaita
    ("muineira", "gl", "muiñeira"),
    ("muineira", "es", "historia de la gaita gallega"),
    ("muineira", "gl", "historia da gaita galega"),
    # mouras e tesouros dos castros
    ("mouras", "gl", "mouras encantadas"),
    ("mouras", "es", "leyendas de mouras Galicia"),
    ("mouras", "es", "castros de Galicia leyendas tesoros"),
    ("mouras", "gl", "tesouros dos mouros castros"),
    # lobishome / Romasanta
    ("romasanta", "es", "Romasanta"),
    ("romasanta", "es", "hombre lobo de Allariz"),
    ("romasanta", "gl", "lobishome"),
    ("romasanta", "en", "Romasanta werewolf"),
    # galeóns de Rande
    ("rande", "es", "galeones de Rande"),
    ("rande", "es", "batalla de Rande"),
    ("rande", "gl", "tesouro de Rande"),
    ("rande", "en", "Vigo Bay treasure galleons"),
    # María Pita
    ("maria_pita", "es", "María Pita"),
    ("maria_pita", "es", "María Pita historia Drake Coruña"),
    # Camiño de Santiago
    ("camino", "es", "Camino de Santiago historia"),
    ("camino", "es", "Camino de Santiago para dormir"),
    ("camino", "en", "Camino de Santiago sleep story"),
    ("camino", "pt", "Caminho de Santiago história"),
    ("camino", "gl", "historia do Camiño de Santiago"),
    # Samaín
    ("samain", "gl", "Samaín"),
    ("samain", "es", "Samaín Galicia"),
    ("samain", "es", "Samhain Galicia celta"),
    # candidatos extra
    ("teixido", "es", "San Andrés de Teixido leyenda"),
    ("teixido", "gl", "Santo André de Teixido"),
    ("costa_morte", "es", "Costa da Morte naufragios leyendas"),
    ("costa_morte", "gl", "Costa da Morte lendas"),
    ("celtas", "es", "celtas de Galicia"),
    ("magosto", "gl", "magosto"),
    # contexto: lendas de Galicia en xeral e formato para durmir
    ("xeral", "es", "leyendas gallegas para dormir"),
    ("xeral", "es", "leyendas de Galicia"),
    ("xeral", "gl", "lendas galegas"),
    ("xeral", "gl", "lendas para durmir"),
    ("xeral", "gl", "contos galegos para durmir"),
    ("xeral", "en", "Galician folklore"),
    ("xeral", "gl", "mitoloxía galega"),
    ("xeral", "pt", "lendas da Galiza"),
    # comparables: bruxas e lendas en formato para durmir noutros sitios
    ("comparable", "es", "historia de las brujas para dormir"),
    ("comparable", "es", "brujas de Zugarramurdi"),
    ("comparable", "en", "witch trials boring history for sleep"),
    ("comparable", "pt", "bruxas história para dormir"),
    ("comparable", "es", "leyendas de España para dormir"),
]

# Orden por vistas (filtro sp=CAM%3D de YouTube): techo de demanda por tema
VIS = [
    ("meigas", "meigas Galicia"),
    ("meigas", "brujas gallegas"),
    ("meigas", "María Soliña"),
    ("meigas", "Inquisición Galicia brujas"),
    ("queimada", "conjuro queimada"),
    ("santa_compana", "Santa Compaña"),
    ("san_xoan", "San Xoán Galicia"),
    ("muineira", "muiñeira"),
    ("mouras", "mouras encantadas Galicia"),
    ("romasanta", "Romasanta"),
    ("rande", "Rande galeones"),
    ("maria_pita", "María Pita"),
    ("camino", "Camino de Santiago para dormir"),
    ("samain", "Samaín Galicia"),
    ("teixido", "Teixido"),
    ("costa_morte", "Costa da Morte leyendas"),
    ("xeral", "leyendas de Galicia"),
    ("xeral", "lendas galegas"),
]

EA = ["--extractor-args", "youtube:player_client=android_vr",
      "--extractor-args", "youtubetab:approximate_date"]


def run(target, key, n=None):
    path = os.path.join(CACHE, key + ".jsonl")
    if os.path.exists(path) and os.path.getsize(path) > 0:
        return path, None
    cmd = [YTDLP, "--flat-playlist", "-j", *EA]
    if n:
        cmd += ["--playlist-end", str(n)]
    cmd.append(target)
    for intento in range(3):
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
        if p.returncode == 0 and p.stdout.strip():
            tmp = path + ".tmp"
            with open(tmp, "w") as f:
                f.write(p.stdout)
            os.replace(tmp, path)
            return path, " ".join(cmd)
        print("  fallo", intento, p.stderr[-300:], file=sys.stderr)
        time.sleep(5 * (intento + 1))
    return None, " ".join(cmd)


def slug(s):
    return hashlib.md5(s.encode()).hexdigest()[:10]


if __name__ == "__main__":
    for tema, lang, q in REL:
        path, cmd = run(f"ytsearch{N}:{q}", "rel_" + slug(q))
        print("rel", tema, lang, q, "->", "ok" if path else "FALLO", flush=True)
        if cmd:
            time.sleep(1.0)
    for tema, q in VIS:
        url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote_plus(q) + "&sp=CAM%253D"
        path, cmd = run(url, "vis_" + slug(q), n=NV)
        print("vis", tema, q, "->", "ok" if path else "FALLO", flush=True)
        if cmd:
            time.sleep(1.0)
