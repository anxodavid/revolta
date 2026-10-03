#!/bin/bash
# Demo de 60 s da zona de durmir (paralaxe e efectos, sen son), co candado cooperativo
export SCRATCH=${SCRATCH:-/tmp/claude-0/-home-user-revolta/c92eba35-e89d-5d11-bb3d-f517a84dab48/scratchpad}
source /home/user/revolta/herramientas/pipeline/entorno.sh
cd /home/user/revolta
exec bash /home/user/revolta/herramientas/gauntlet/candado.sh "$PY" plan-de-negocio/gauntlet4/movemento/scripts/demo_gancho.py durmir
