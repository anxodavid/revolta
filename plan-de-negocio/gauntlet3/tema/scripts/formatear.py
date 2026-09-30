#!/usr/bin/env python3
"""Vuelca la caché de búsquedas al formato de busquedas-yt.txt (el del Gauntlet 2 + fecha aproximada)."""
import json, os, sys, urllib.parse
sys.path.insert(0, os.path.dirname(__file__))
from buscar import REL, VIS, CACHE, slug, N, NV

OUT = sys.argv[1] if len(sys.argv) > 1 else "/dev/stdout"


def cargar(key):
    path = os.path.join(CACHE, key + ".jsonl")
    res = []
    with open(path) as f:
        for l in f:
            l = l.strip()
            if l:
                res.append(json.loads(l))
    return res


def fecha(d):
    u = d.get("upload_date")
    return f"{u[:4]}-{u[4:6]}" if u else "?"


def linea(d):
    t = (d.get("title") or "").replace("|", "/").replace("\n", " ")
    c = (d.get("channel") or "").replace("|", "/")
    v = d.get("view_count")
    dur = d.get("duration")
    return f"{v if v is not None else '?'} | {c} | {t} | {int(dur) if dur else ''} | {fecha(d)} | {d.get('url')}"


with open(OUT, "w") as f:
    f.write("# Búsquedas en YouTube con yt-dlp 2026.08.19 (sin descargar vídeos), 30-09-2026, pieza TEMA del Gauntlet 3.\n")
    f.write(f"# Comando (orden por relevancia): yt-dlp --flat-playlist -j --extractor-args \"youtube:player_client=android_vr\" "
            f"--extractor-args \"youtubetab:approximate_date\" \"ytsearch{N}:<consulta>\"\n")
    f.write(f"# Comando (orden por vistas, filtro sp=CAM%3D): yt-dlp --flat-playlist -j --playlist-end {NV} [mismos extractor-args] "
            f"\"https://www.youtube.com/results?search_query=<consulta>&sp=CAM%253D\"\n")
    f.write("# Columnas: vistas | canal | título | duración (s) | fecha aprox. (AAAA-MM) | URL\n")
    f.write("# La fecha sale del texto relativo de YouTube (\"hace 2 años\"): es aproximada (error de hasta 1 unidad: mes o año).\n")
    f.write("# Los títulos pueden salir traducidos al inglés por YouTube (el cliente pide inglés): el vídeo es el mismo.\n")
    f.write("# Etiqueta de cada bloque: [tema / idioma de la consulta]. Scripts: scratchpad tema/buscar.py y tema/formatear.py\n")
    for tema, lang, q in REL:
        f.write(f"== {q}   [{tema} / {lang}]\n")
        for d in cargar("rel_" + slug(q)):
            f.write(linea(d) + "\n")
    for tema, q in VIS:
        f.write(f"== [orden por vistas] {q}   [{tema}]\n")
        for d in cargar("vis_" + slug(q)):
            f.write(linea(d) + "\n")
