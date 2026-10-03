#!/bin/bash
# Voz da v2 (Gauntlet 4): portas de texto + voz + planos.json; sae co código 3 porque aínda non hai lista de planos.
cd /home/user/revolta/herramientas/pipeline && source entorno.sh
export MALLOC_ARENA_MAX=2
echo "inicio $(date -u)"
/home/user/revolta/herramientas/gauntlet/candado.sh --prioridade "$PY" longo.py temas/meigas-de-verdade-v2.yaml \
  --guion ../../plan-de-negocio/gauntlet4/guion/guion-r2.txt --traballo "$SCRATCH/v2/w" --saida "$SCRATCH/v2/s" \
  --excepcions ../../plan-de-negocio/gauntlet4/guion/excepcions-r2.yaml
echo "rc $? $(date -u)"
pkill -f languagetool-server.jar
