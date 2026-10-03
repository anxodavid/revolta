#!/usr/bin/env bash
# Embeddings de T5 das accións I2V da v2 (Gauntlet 4, peza 5): agarda a que rematen as imaxes, baixa o T5 fp8
# (4,9 GB), calcula nun lote os embeddings que falten (movemento_i2v.py colle o candado el mesmo: non envolver este
# script en candado.sh) e, se foi ben, borra o T5. Relanzable: os embeddings feitos quedan en $SCRATCH/video/emb.
set -u
R=/home/user/revolta
cd $R/herramientas/pipeline && source entorno.sh
V=$SCRATCH/video/venv/bin/python
P=$R/plan-de-negocio/gauntlet4/video/scripts/produccion.py
export MALLOC_ARENA_MAX=2 HF_HUB_DISABLE_XET=1
while pgrep -f "v2/imaxes.sh" >/dev/null || pgrep -f "longo.py.*--so-imaxes" >/dev/null; do sleep 60; done
echo "t5 inicio $(date -u)"
python3 $P lista && python3 $P i2v $SCRATCH/v2/i2v-accions.json --accions || exit 1
$V movemento_i2v.py baixar && $V movemento_i2v.py texto $SCRATCH/v2/i2v-accions.json
rc=$?
[ $rc = 0 ] && rm -rf $SCRATCH/video/hf/hub/models--comfyanonymous--flux_text_encoders
echo "t5 rc $rc $(date -u)"
