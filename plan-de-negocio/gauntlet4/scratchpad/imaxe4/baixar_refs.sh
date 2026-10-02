#!/usr/bin/env bash
# Equivalente a docs/referencias-graficas/descargar.sh (mesmos nomes), cun User-Agent co URL do repositorio como
# contacto e as miniaturas estándar de Commons no canto dos orixinais. Unha a unha, con pausa e reintentos.
set -u
cd "$SCRATCH/referencias"
UA="revolta-refs/0.2 (+https://github.com/anxodavid/revolta)"
while IFS=$'\t' read -r c f u; do
  mkdir -p "$c"; [[ -s "$c/$f" ]] && continue
  for i in 1 2 3 4; do
    code=$(curl -sSL --max-time 240 -A "$UA" -o "$c/$f.tmp" -w "%{http_code}" "$u")
    if [[ "$code" == 200 ]]; then mv "$c/$f.tmp" "$c/$f"; echo "ok $c/$f"; break; fi
    echo "HTTP $code en $c/$f (intento $i) $u"; rm -f "$c/$f.tmp"; sleep $((20*i))
  done
  sleep 2
done < "$SCRATCH/imaxe4/urls_refs.tsv"
echo "baixar_refs: rematou"
