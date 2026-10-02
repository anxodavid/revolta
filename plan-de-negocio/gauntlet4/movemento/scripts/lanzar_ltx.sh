#!/bin/bash
# Uso: lanzar_ltx.sh traballos.json saida_dir  (co candado de CPU)
export SCRATCH=/tmp/claude-0/-home-user-revolta/c92eba35-e89d-5d11-bb3d-f517a84dab48/scratchpad
source /home/user/revolta/herramientas/pipeline/entorno.sh
cd "$SCRATCH/video/probas"
exec flock "$CPU_LOCK" env HF_HOME="$SCRATCH/video/hf" HF_HUB_OFFLINE=1 "$SCRATCH/video/venv/bin/python" ltx_proba.py "$1" "$2"
