"""seleccion.json -> referencias.csv, descargar.sh (en docs/referencias-graficas/). Puntuaciones = estimación automática por metadatos."""
import json, csv, re, os, unicodedata, collections, urllib.parse
OUT = "../../docs/referencias-graficas"; os.makedirs(OUT, exist_ok=True)
sel = json.load(open("seleccion.json"))
PERS = re.compile(r"festa|desfile|feira|día das letras|peliqueiro|banda|xuntanza|meigas|mural|hotel|castelao|moendo", re.I)
def slug(t):
    t = unicodedata.normalize("NFKD", t.rsplit(".", 1)[0]).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")[:50]
def ext(u): return u.rsplit(".", 1)[-1].lower().split("?")[0]
cols = "concepto titulo url_pagina url_imagen_original autor licencia resolucion año_época tipo idoneidad_img2img idoneidad_controlnet notas texto_atribucion".split()
rows = []; sh = []
for conc, lst in sel.items():
    for i, r in enumerate(lst, 1):
        big = 0; w, h = (r["resolucion"].split("x") + ["0"])[:2] if "x" in r["resolucion"] and r["resolucion"][0].isdigit() else ("0", "0")
        big = max(int(w), int(h))
        base = max(1, min(5, round(r["score"] / 2)))
        i2i = base; cn = base
        notas = ["Puntuación = estimación automática por metadatos (título, resolución, categoría de calidad); SIN revisión visual"]
        if r["sa"]: notas.append("CC BY-SA: la obra derivada podría tener que compartirse igual (SA)")
        if PERS.search(r["titulo"]) or conc in ("08-traje",): notas.append("Posible gente reconocible: revisar; usar solo como referencia de forma/ropa")
        if r["licencia"].lower().startswith("public domain"): notas.append("Dominio público declarado en Commons: verificar en la página")
        if "Doré" in r["autor"]: notas.append("Grabado de Doré (PD por antigüedad); la licencia CC BY 2.0 es de la copia de Flickr")
        if r["fuente"].startswith("The Met"): notas.append("Resolución no verificada"); i2i = min(i2i, 4)
        if r["tipo"].startswith("miniatura"): notas.append(r["notas"]); i2i = min(i2i, 3)
        elif r["notas"] and r["fuente"] == "Wikimedia Commons": notas.append("Subtema: " + r["notas"])
        elif r["fuente"].startswith("The Met"): notas.append(r["notas"])
        attr = f"«{r['titulo']}», {r['autor']}, {r['licencia']}, vía {r['fuente']}: {r['url_pagina']}"
        rows.append([conc, r["titulo"], r["url_pagina"], r["url_imagen"], r["autor"], r["licencia"], r["resolucion"], r["epoca"], r["tipo"], i2i, cn, " | ".join(notas), attr])
        fn = f"{i:02d}-{slug(r['titulo'])}.{ext(r['url_imagen'])}"
        u = r["url_imagen"]
        if "upload.wikimedia.org/wikipedia/commons/" in u and big > 2500 and ext(u) in ("jpg", "jpeg", "png"):
            m = re.match(r"(.*/commons)/(\w/\w\w)/(.+)$", u); u = f"{m.group(1)}/thumb/{m.group(2)}/{m.group(3)}/1920px-{m.group(3)}"
        sh.append(f'bajar "{conc}" "{fn}" "{u}"')
with open(f"{OUT}/referencias.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(cols); w.writerows(rows)
open(f"{OUT}/descargar.sh", "w").write('''#!/usr/bin/env bash
# Baja las imágenes elegidas a ./referencias/<concepto>/ (una a una, con pausa; respeta 429).
# Las originales de más de 2500 px se bajan reescaladas a 1920 px de ancho (suficiente para img2img/ControlNet).
# Uso: bash descargar.sh [prefijo_concepto]   p. ej.: bash descargar.sh 01
UA="revolta-refs/0.1 (afeijoo@ecomt.net)"
FILTRO="${1:-}"
bajar() {
  local c="$1" f="$2" u="$3"
  [[ -n "$FILTRO" && "$c" != "$FILTRO"* ]] && return
  mkdir -p "referencias/$c"; [[ -s "referencias/$c/$f" ]] && return
  for i in 1 2 3 4 5; do
    code=$(curl -sSL -A "$UA" -o "referencias/$c/$f.tmp" -w "%{http_code}" "$u")
    if [[ "$code" == 200 ]]; then mv "referencias/$c/$f.tmp" "referencias/$c/$f"; break; fi
    echo "HTTP $code en $f (intento $i)" >&2; rm -f "referencias/$c/$f.tmp"; sleep $((10*i))
  done
  sleep 2
}
''' + "\n".join(sh) + "\n")
os.chmod(f"{OUT}/descargar.sh", 0o755)
print(len(rows), "filas")
