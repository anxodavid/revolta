#!/bin/bash
# Uso: lanzar_i2v.sh fase planos.json  (movemento_i2v.py colle o candado de CPU el mesmo, clip a clip)
export SCRATCH=/tmp/claude-0/-home-user-revolta/c92eba35-e89d-5d11-bb3d-f517a84dab48/scratchpad
source /home/user/revolta/herramientas/pipeline/entorno.sh
export HF_HUB_OFFLINE=1 MALLOC_ARENA_MAX=2
exec "$SCRATCH/video/venv/bin/python" /home/user/revolta/herramientas/pipeline/movemento_i2v.py "$1" "$2"
