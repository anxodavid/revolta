#!/usr/bin/env bash
# Cadea para despois das imaxes da v2 (Gauntlet 4, peza 5), sen agardar polo orquestrador: aplica as escollas da
# revisión r1 a revision.json cando non corre longo.py, agarda ao T5 e lanza a rexeneración (candado de prioridade) e
# os clips I2V (movemento.sh, que agarda detrás). Relanzable: cada paso é idempotente.
set -u
R=/home/user/revolta
cd $R/herramientas/pipeline && source entorno.sh
S=$R/plan-de-negocio/gauntlet4/video/scripts
while pgrep -f "v2/imaxes.sh" >/dev/null || pgrep -f "longo.py" >/dev/null; do sleep 60; done
python3 $S/produccion.py revision $R/plan-de-negocio/gauntlet4/video/revision-imaxes-r1.json || exit 1
while pgrep -f "video/scripts/t5.sh" >/dev/null; do sleep 30; done
pgrep -f "video/scripts/rexenerar.sh" >/dev/null ||
  setsid nohup bash $S/rexenerar.sh >> $SCRATCH/v2/rexenerar.log 2>&1 < /dev/null &
sleep 90
pgrep -f "video/scripts/movemento.sh" >/dev/null ||
  setsid nohup bash $S/movemento.sh >> $SCRATCH/v2/movemento.log 2>&1 < /dev/null &
echo "tras-imaxes: rexenerar e movemento lanzados $(date -u)"
