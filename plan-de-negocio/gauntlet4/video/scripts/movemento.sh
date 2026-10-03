#!/usr/bin/env bash
# Clips I2V da v2 (Gauntlet 4, peza 5) por tramos de prioridade, cada un seguido da súa porta de vídeo. Só entran os
# planos cunha imaxe aprobada (pola porta ou pola revisión do axente); relanzalo despois de cada rexeneración. A
# caché salta os clips feitos e porta_clips.py os xa medidos. NON envolver en candado.sh: movemento_i2v.py colle o
# candado por clip (deixa pasar por diante a quen teña o de prioridade, p. ex. rexenerar.sh).
set -u
R=/home/user/revolta
cd $R/herramientas/pipeline && source entorno.sh
V=$SCRATCH/video/venv/bin/python
S=$R/plan-de-negocio/gauntlet4/video/scripts
export MALLOC_ARENA_MAX=2
while pgrep -f "video/scripts/t5.sh" >/dev/null; do sleep 60; done     # os embeddings das accións
for tramo in "1 gancho,transicion" "1 calma,durmir" "2 gancho,transicion" "2 calma,durmir"; do
  set -- $tramo
  L=$SCRATCH/v2/i2v-p$1-${2%%,*}.json
  echo "== tramo prioridade $1 ($2) $(date -u)"
  while true; do
    # só imaxes que revisou o axente: a porta deixa pasar de máis (revisión r1: 16 de 29)
    python3 $S/produccion.py lista >/dev/null &&
      python3 $S/produccion.py i2v $L --prioridade $1 --fases $2 --so-revisadas || exit 1
    $V movemento_i2v.py xerar $L
    rc=$?
    [ $rc = 75 ] || break            # 75: cedeu a CPU a un traballo prioritario (saíu para liberar a memoria)
    echo "agardo a que remate o traballo prioritario $(date -u)"
    flock "$CPU_LOCK.prio" true
  done
  $R/herramientas/gauntlet/candado.sh "$PY" $S/porta_clips.py $L
done
echo "movemento fin $(date -u)"
