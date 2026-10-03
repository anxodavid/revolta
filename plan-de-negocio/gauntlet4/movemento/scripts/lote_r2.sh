#!/bin/bash
# lote_r2.sh (rolda 1, despois do 2.º reinicio): compatibilidade coa v1, 3 clips I2V máis (rostro, camiñar, dúas
# persoas), porta e tiras de todos os clips e demo do gancho. Cada paso co seu candado; os clips I2V collen o
# candado eles mesmos (movemento_i2v.py, mesmo protocolo ca candado.sh), sen envoltorio para non interbloquearse.
export SCRATCH=${SCRATCH:-/tmp/claude-0/-home-user-revolta/c92eba35-e89d-5d11-bb3d-f517a84dab48/scratchpad}
source /home/user/revolta/herramientas/pipeline/entorno.sh
cd /home/user/revolta
R=plan-de-negocio/gauntlet4/movemento/scripts; O=plan-de-negocio/gauntlet4/movemento/probas
P=$SCRATCH/video/probas; L=$SCRATCH/video/logs
bash $R/con_candado.sh $PY $R/proba_compat_v1.py > $L/compat.log 2>&1
bash $R/lanzar_i2v.sh xerar $P/i2v_probas3.json > $L/i2v3.log 2>&1
bash $R/con_candado.sh $PY $R/porta_probas.py $SCRATCH/video/saida/porta.json $O \
  $(ls $SCRATCH/movemento/i2v/*.mp4 | grep -v '_x[0-9]') $SCRATCH/video/saida/ltx/ltx_p22_800x448_f49_s8.mp4 > $L/porta.log 2>&1
cp $SCRATCH/video/saida/porta.json $O/medidas-porta.json
cp $SCRATCH/movemento/i2v/*.json $SCRATCH/video/saida/ 2>/dev/null
bash $R/con_candado.sh $PY $R/demo_gancho.py montar > $L/demo.log 2>&1
echo LOTE2_FIN
