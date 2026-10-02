#!/bin/bash
# Probas de paralaxe + efectos sobre imaxes do gancho da v1 (co candado de CPU, todas seguidas)
export SCRATCH=/tmp/claude-0/-home-user-revolta/c92eba35-e89d-5d11-bb3d-f517a84dab48/scratchpad
source /home/user/revolta/herramientas/pipeline/entorno.sh
I=/home/user/revolta/plan-de-negocio/gauntlet3/video/imaxes
O=$SCRATCH/video/saida/plx
PR=/home/user/revolta/plan-de-negocio/gauntlet4/movemento/scripts/proba_plano.py
exec flock "$CPU_LOCK" bash /tmp/claude-0/-home-user-revolta/c92eba35-e89d-5d11-bb3d-f517a84dab48/scratchpad/video/probas/plx1_corpo.sh
