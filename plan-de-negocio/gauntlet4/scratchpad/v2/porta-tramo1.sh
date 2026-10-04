#!/usr/bin/env bash
# Porta de vídeo dos 11 clips do tramo 1 (a de movemento.sh fallou ás 01:50 por un erro xa arranxado en movemento.py)
R=/home/user/revolta
cd $R/herramientas/pipeline && source entorno.sh
$R/herramientas/gauntlet/candado.sh --prioridade "$PY" $R/plan-de-negocio/gauntlet4/video/scripts/porta_clips.py $SCRATCH/v2/i2v-p1-gancho.json
echo "porta tramo 1 rc $? $(date -u)"
