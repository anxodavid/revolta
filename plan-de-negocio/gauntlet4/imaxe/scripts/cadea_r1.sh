#!/usr/bin/env bash
# Cadea das probas pesadas da peza IMAXE (rolda 1): cada paso colle o candado por separado (candado.sh), así que as
# outras pezas poden entrar entre un e outro. Uso: setsid nohup bash cadea_r1.sh > $SCRATCH/imaxe4/logs/cadea.log 2>&1 &
cd /home/user/revolta && source herramientas/pipeline/entorno.sh >/dev/null
export MALLOC_ARENA_MAX=2 IMG_MODEL=lightning1024 CPU_LOCK
I=plan-de-negocio/gauntlet4/imaxe/scripts
C=herramientas/gauntlet/candado.sh
paso() { echo "== $(date -u +%H:%M:%S) $*"; "$C" "$PY" "$@" 2>&1 | grep -v -i -E "warn|deprecat|slow image|use_fast"; echo "== rc ${PIPESTATUS[0]} $(date -u +%H:%M:%S)"; }
paso $I/sementes_ab.py xerar palloza,queimada,horreo,horreos
paso $I/biblia_proba.py xerar 8,16,19,20,26
paso $I/biblia_proba.py xerar 33,37,48,84,92
paso $I/revisar_ab.py ab biblia
paso $I/florence_ovd.py
echo CADEA_FIN
