#!/bin/bash
# Porta de texto completa do guion v2 r1 (Gauntlet 4). Colle o candado da CPU e corre longo.py --so-texto.
export SCRATCH=/tmp/claude-0/-home-user-revolta/c92eba35-e89d-5d11-bb3d-f517a84dab48/scratchpad
source /home/user/revolta/herramientas/pipeline/entorno.sh
cd /home/user/revolta/herramientas/pipeline
echo "agardando o candado: $(date -u +%H:%M:%S)"
flock "$CPU_LOCK" bash -c 'echo "candado collido: $(date -u +%H:%M:%S)"; md5sum /tmp/claude-0/-home-user-revolta/c92eba35-e89d-5d11-bb3d-f517a84dab48/scratchpad/guion/guion-r1-conxelado.txt; /usr/bin/time -v "$PY" longo.py temas/meigas-de-verdade-v2.yaml --guion /tmp/claude-0/-home-user-revolta/c92eba35-e89d-5d11-bb3d-f517a84dab48/scratchpad/guion/guion-r1-conxelado.txt --traballo /tmp/claude-0/-home-user-revolta/c92eba35-e89d-5d11-bb3d-f517a84dab48/scratchpad/guion/w-r1 --saida /tmp/claude-0/-home-user-revolta/c92eba35-e89d-5d11-bb3d-f517a84dab48/scratchpad/guion/s-r1 --so-texto --excepcions ../../plan-de-negocio/gauntlet4/guion/excepcions-r1.yaml; echo "remate: $(date -u +%H:%M:%S) codigo $?"'
