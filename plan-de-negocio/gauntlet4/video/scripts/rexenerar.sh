#!/usr/bin/env bash
# Rexeneración das imaxes que pediu a revisión (Gauntlet 4, peza 5): a lista de produción leva os prompts novos (clave
# nova na caché: tres intentos novos). Co candado de prioridade, para pasar por diante dos clips I2V (movemento_i2v.py
# sae para liberar a memoria). Mesmas variables que imaxes.sh: IMG_MAX_INTENTOS=3 non engade intentos aos planos vellos.
R=/home/user/revolta
cd $R/herramientas/pipeline && source entorno.sh
python3 $R/plan-de-negocio/gauntlet4/video/scripts/produccion.py lista || exit 1
export MALLOC_ARENA_MAX=2 IMG_MODEL=lightning IMG_MAX_INTENTOS=3 IMG_RESERVAS=0 IMG_CFG_REINTENTO=0 \
       REVISOR_LUME_DURMIR=0.015 REVISOR_VLM=florence-community/Florence-2-base
for i in 1 2 3; do
  echo "rexenerar intento $i $(date -u)"
  $R/herramientas/gauntlet/candado.sh --prioridade "$PY" longo.py temas/meigas-de-verdade-v2.yaml \
    --guion ../../plan-de-negocio/gauntlet4/guion/guion-r2.txt --traballo "$SCRATCH/v2/w" --saida "$SCRATCH/v2/s" \
    --excepcions ../../plan-de-negocio/gauntlet4/guion/excepcions-r2.yaml \
    --escenas ../../plan-de-negocio/gauntlet4/video/escenas-v2-produccion.json --so-imaxes
  rc=$?; echo "rc $rc $(date -u)"
  pkill -f languagetool-server.jar
  if [ "$rc" = 0 ] || [ "$rc" = 3 ] || [ "$rc" = 4 ]; then break; fi
  sleep 20
done
echo "saida rexenerar $rc $(date -u)"
