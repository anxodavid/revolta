#!/bin/bash
# lote_r1.sh: as probas pendentes da rolda 1 en serie, cada unha co seu candado (sobrevive ao fin do turno, non a un
# reinicio do contedor). Os clips I2V collen o candado eles mesmos (movemento_i2v.py), sen envoltorio.
export SCRATCH=${SCRATCH:-/tmp/claude-0/-home-user-revolta/c92eba35-e89d-5d11-bb3d-f517a84dab48/scratchpad}
source /home/user/revolta/herramientas/pipeline/entorno.sh
R=/home/user/revolta/plan-de-negocio/gauntlet4/movemento/scripts
P=$SCRATCH/video/probas; L=$SCRATCH/video/logs; O=/home/user/revolta/plan-de-negocio/gauntlet4/movemento/probas
bash $R/con_candado.sh bash $P/plx2_corpo.sh > $L/plx2.log 2>&1
bash $R/lanzar_i2v.sh xerar $P/i2v_probas1.json > $L/i2v1.log 2>&1
bash $R/lanzar_i2v.sh xerar $P/i2v_probas2.json > $L/i2v2.log 2>&1
bash $R/con_candado.sh $PY $R/porta_probas.py $SCRATCH/video/saida/porta.json $O \
  $(ls $SCRATCH/movemento/i2v/*.mp4 | grep -v '_x[0-9]') > $L/porta.log 2>&1
C22=$(grep -l '021-de4f25ff' $SCRATCH/movemento/i2v/*.json | head -1)
[ -n "$C22" ] && bash $R/con_candado.sh $PY $R/proba_detalle.py ${C22%.json}.mp4 \
  $SCRATCH/video/demo/graduadas/021-de4f25ff-0.png $O/i2v_p22_detalle.jpg 0 48 96 > $L/detalle.log 2>&1
echo LOTE_FIN
