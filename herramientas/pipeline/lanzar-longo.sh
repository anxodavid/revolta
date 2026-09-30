#!/bin/bash
# Lanza longo.py desacoplado (non depende do terminal do axente) e reinténtao se morre (OOM, reinicio de proceso):
# o feito queda na caché de cada etapa. Uso: lanzar.sh ETIQUETA
cd /home/user/revolta/herramientas/pipeline && source entorno.sh
export IMG_MAX_INTENTOS=${IMG_MAX_INTENTOS:-4} IMG_CFG_REINTENTO=${IMG_CFG_REINTENTO:-0}
L=$SCRATCH/longo/$1.log
for i in 1 2 3 4 5 6; do
  { echo "inicio intento $i $(date -u)"; time flock "$CPU_LOCK" "$PY" longo.py temas/meigas-de-verdade.yaml --guion "$SCRATCH/longo/guion-producion.txt" \
      --traballo "$SCRATCH/longo/w" --saida ../../plan-de-negocio/gauntlet3/video \
      --escenas ../../plan-de-negocio/gauntlet3/video/escenas.json; rc=$?; echo "rc $rc $(date -u)"; } >> "$L" 2>&1
  pkill -f languagetool-server.jar
  if [ "$rc" = 0 ] || [ "$rc" = 3 ] || [ "$rc" = 4 ]; then break; fi
  sleep 20
done
echo "saida $rc $(date -u)" >> "$L"
