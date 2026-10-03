#!/bin/bash
# Imaxes da v2 (Gauntlet 4): portas de texto (caché), voz (caché), planos pola lista e imaxes coa porta v6; para
# despois das imaxes (--so-imaxes). Reintenta se morre (OOM, reinicio de proceso): o feito queda na caché.
cd /home/user/revolta/herramientas/pipeline && source entorno.sh
export MALLOC_ARENA_MAX=2 IMG_MODEL=lightning IMG_MAX_INTENTOS=3 IMG_RESERVAS=0 IMG_CFG_REINTENTO=0 \
       REVISOR_LUME_DURMIR=0.015 REVISOR_VLM=florence-community/Florence-2-base
for i in $(seq 1 8); do
  echo "inicio intento $i $(date -u)"
  /home/user/revolta/herramientas/gauntlet/candado.sh "$PY" longo.py temas/meigas-de-verdade-v2.yaml \
    --guion ../../plan-de-negocio/gauntlet4/guion/guion-r2.txt --traballo "$SCRATCH/v2/w" --saida "$SCRATCH/v2/s" \
    --excepcions ../../plan-de-negocio/gauntlet4/guion/excepcions-r2.yaml \
    --escenas ../../plan-de-negocio/gauntlet4/planos/escenas-v2.json --so-imaxes
  rc=$?; echo "rc $rc $(date -u)"
  pkill -f languagetool-server.jar
  if [ "$rc" = 0 ] || [ "$rc" = 3 ] || [ "$rc" = 4 ]; then break; fi
  sleep 20
done
echo "saida $rc $(date -u)"
