#!/bin/bash
# Porta de texto completa do guion v2 r1 (Gauntlet 4): longo.py --so-texto sobre a copia conxelada do guion,
# co candado da CPU en modo prioritario (herramientas/gauntlet/candado.sh: camiño crítico).
export SCRATCH=/tmp/claude-0/-home-user-revolta/c92eba35-e89d-5d11-bb3d-f517a84dab48/scratchpad
source /home/user/revolta/herramientas/pipeline/entorno.sh
cd /home/user/revolta/herramientas/pipeline
echo "agardando o candado (prioridade): $(date -u +%H:%M:%S)"
/home/user/revolta/herramientas/gauntlet/candado.sh --prioridade bash -c 'echo "candado collido: $(date -u +%H:%M:%S)"; md5sum $SCRATCH/guion/guion-r1-conxelado.txt; /usr/bin/time -v "$PY" longo.py temas/meigas-de-verdade-v2.yaml --guion $SCRATCH/guion/guion-r1-conxelado.txt --traballo $SCRATCH/guion/w-r1 --saida $SCRATCH/guion/s-r1 --so-texto --excepcions ../../plan-de-negocio/gauntlet4/guion/excepcions-r1.yaml; echo "remate: $(date -u +%H:%M:%S) codigo $?"'
