#!/usr/bin/env bash
# Execución completa da v2 (Gauntlet 4, peza 5): portas de texto, voz e imaxes (da caché, coas escollas da revisión),
# movemento (clips I2V da caché; sen clip, paralaxe), son, montaxe e QA. Mesmas IMG_* que imaxes.sh e rexenerar.sh.
R=/home/user/revolta
cd $R/herramientas/pipeline && source entorno.sh
python3 $R/plan-de-negocio/gauntlet4/video/scripts/produccion.py lista || exit 1
export MALLOC_ARENA_MAX=2 IMG_MODEL=lightning IMG_MAX_INTENTOS=3 IMG_RESERVAS=0 IMG_CFG_REINTENTO=0 \
       REVISOR_LUME_DURMIR=0.015 REVISOR_VLM=florence-community/Florence-2-base
for i in 1 2 3; do
  echo "completo intento $i $(date -u)"
  $R/herramientas/gauntlet/candado.sh "$PY" longo.py temas/meigas-de-verdade-v2.yaml \
    --guion ../../plan-de-negocio/gauntlet4/guion/guion-r2.txt --traballo "$SCRATCH/v2/w" --saida "$SCRATCH/v2/s" \
    --excepcions ../../plan-de-negocio/gauntlet4/guion/excepcions-r2.yaml \
    --escenas ../../plan-de-negocio/gauntlet4/video/escenas-v2-produccion.json
  rc=$?; echo "rc $rc $(date -u)"
  pkill -f languagetool-server.jar
  if [ "$rc" = 0 ] || [ "$rc" = 3 ] || [ "$rc" = 4 ]; then break; fi
  sleep 20
done
echo "saida completo $rc $(date -u)"
