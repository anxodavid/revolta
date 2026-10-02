#!/bin/bash
# Uso: con_candado.sh orde args...   Lanza unha proba da peza MOVEMENTO co candado cooperativo do Gauntlet 4
# (herramientas/gauntlet/candado.sh: cede a vez ao guion e á voz). Non usar con movemento_i2v.py, que o colle el.
export SCRATCH=${SCRATCH:-/tmp/claude-0/-home-user-revolta/c92eba35-e89d-5d11-bb3d-f517a84dab48/scratchpad}
source /home/user/revolta/herramientas/pipeline/entorno.sh
export MALLOC_ARENA_MAX=2
exec bash /home/user/revolta/herramientas/gauntlet/candado.sh "$@"
