#!/bin/bash
# Lanza longo.py desacoplado (non depende do terminal do axente) e reinténtao se morre (OOM, reinicio de proceso):
# o feito queda na caché de cada etapa. Uso: lanzar.sh ETIQUETA
cd /home/user/revolta/herramientas/pipeline && source entorno.sh
# MALLOC_ARENA_MAX=2: menos arenas de glibc = menos memoria fragmentada cos fíos de torch (OOM do 01-10-2026)
export MALLOC_ARENA_MAX=${MALLOC_ARENA_MAX:-2}
export IMG_MAX_INTENTOS=${IMG_MAX_INTENTOS:-4} IMG_CFG_REINTENTO=${IMG_CFG_REINTENTO:-0} IMG_MODEL=${IMG_MODEL:-lightning1024} REVISOR_VLM=${REVISOR_VLM:-florence-community/Florence-2-base}
L=$SCRATCH/longo/$1.log
for i in $(seq 1 12); do
  { echo "inicio intento $i $(date -u)"; time flock "$CPU_LOCK" "$PY" longo.py temas/meigas-de-verdade.yaml --guion "$SCRATCH/longo/guion-producion.txt" \
      --traballo "$SCRATCH/longo/w" --saida ../../plan-de-negocio/gauntlet3/video \
      --escenas ../../plan-de-negocio/gauntlet3/video/escenas.json; rc=$?; echo "rc $rc $(date -u)"; } >> "$L" 2>&1
  pkill -f languagetool-server.jar
  if [ "$rc" = 0 ] || [ "$rc" = 3 ] || [ "$rc" = 4 ]; then break; fi
  sleep 20
done
echo "saida $rc $(date -u)" >> "$L"
