#!/bin/bash
# Proba do corte por sentido (peza PLANOS): longo.py --so-planos sobre $SCRATCH/v2/w, co candado prioritario.
export SCRATCH=/tmp/claude-0/-home-user-revolta/c92eba35-e89d-5d11-bb3d-f517a84dab48/scratchpad
cd /home/user/revolta/herramientas/pipeline && source entorno.sh
export MALLOC_ARENA_MAX=2
echo "inicio $(date -u)"
/home/user/revolta/herramientas/gauntlet/candado.sh --prioridade "$PY" longo.py temas/meigas-de-verdade-v2.yaml \
  --guion ../../plan-de-negocio/gauntlet4/guion/guion-r2.txt --traballo "$SCRATCH/v2/w" --saida "$SCRATCH/v2/s" \
  --excepcions ../../plan-de-negocio/gauntlet4/guion/excepcions-r2.yaml \
  --escenas ../../plan-de-negocio/gauntlet4/planos/escenas-v2.json --so-planos
echo "rc $? $(date -u)"
pkill -f languagetool-server.jar
