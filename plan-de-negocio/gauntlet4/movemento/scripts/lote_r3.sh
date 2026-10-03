#!/bin/bash
# lote_r3.sh (rolda 1): porta de vídeo recalibrada sobre os 6 clips reais e 4 malos sintéticos, e demo do gancho
# outra vez (cos clips que agora pasan a porta). Cada paso co candado cooperativo.
export SCRATCH=${SCRATCH:-/tmp/claude-0/-home-user-revolta/c92eba35-e89d-5d11-bb3d-f517a84dab48/scratchpad}
source /home/user/revolta/herramientas/pipeline/entorno.sh
cd /home/user/revolta
R=plan-de-negocio/gauntlet4/movemento/scripts; O=plan-de-negocio/gauntlet4/movemento/probas
L=$SCRATCH/video/logs; N=$SCRATCH/video/saida/neg; C=$SCRATCH/movemento/i2v
A=$(grep -l '021-de4f25ff' $C/*.json | head -1); B=$(grep -l '013-ff9a4e6a' $C/*.json | head -1)
rm -f $SCRATCH/video/saida/porta.json
bash $R/con_candado.sh $PY $R/porta_negativos.py ${A%.json}.mp4 ${B%.json}.mp4 $N > $L/neg.log 2>&1
bash $R/con_candado.sh $PY $R/porta_probas.py $SCRATCH/video/saida/porta.json $O \
  $(ls $C/*.mp4 | grep -v '_x[0-9]') $SCRATCH/video/saida/ltx/ltx_p22_800x448_f49_s8.mp4 > $L/porta.log 2>&1
bash $R/con_candado.sh $PY $R/porta_probas.py $SCRATCH/video/saida/porta.json $N $N/neg_*.mp4 >> $L/porta.log 2>&1
cp $SCRATCH/video/saida/porta.json $O/medidas-porta.json
bash $R/con_candado.sh $PY $R/demo_gancho.py montar > $L/demo.log 2>&1
echo LOTE3_FIN
