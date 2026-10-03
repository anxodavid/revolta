#!/usr/bin/env bash
# Terceira rolda de imaxes (Gauntlet 4, peza 5), cun só candado de prioridade (o I2V en marcha sae para liberar a
# memoria e retoma despois): (1) embeddings de T5 das accións I2V novas das revisións r1 e r2 (baixa o T5 fp8, 4,9 GB,
# e bórrao), (2) rexeneración dos planos que pediu a r2 con tres intentos sempre (IMG_MIN_INTENTOS=3: a porta deixa
# pasar de máis e o axente precisa onde escoller). Dentro do candado, os procesos non o volven coller (CPU_LOCK baleira).
R=/home/user/revolta
cd $R/herramientas/pipeline && source entorno.sh
S=$R/plan-de-negocio/gauntlet4/video/scripts
V=$SCRATCH/video/venv/bin/python
python3 $S/produccion.py lista && python3 $S/produccion.py i2v $SCRATCH/v2/i2v-accions.json --accions || exit 1
export MALLOC_ARENA_MAX=2 HF_HUB_DISABLE_XET=1 IMG_MODEL=lightning IMG_MAX_INTENTOS=3 IMG_MIN_INTENTOS=3 IMG_RESERVAS=0 \
       IMG_CFG_REINTENTO=0 REVISOR_LUME_DURMIR=0.015 REVISOR_VLM=florence-community/Florence-2-base
echo "r3 inicio $(date -u)"
$R/herramientas/gauntlet/candado.sh --prioridade env CPU_LOCK= bash -c "
  $V movemento_i2v.py baixar && $V movemento_i2v.py texto $SCRATCH/v2/i2v-accions.json &&
    rm -rf $SCRATCH/video/hf/hub/models--comfyanonymous--flux_text_encoders && echo \"t5 feito \$(date -u)\"
  \"$PY\" longo.py temas/meigas-de-verdade-v2.yaml --guion ../../plan-de-negocio/gauntlet4/guion/guion-r2.txt \
    --traballo \"$SCRATCH/v2/w\" --saida \"$SCRATCH/v2/s\" \
    --excepcions ../../plan-de-negocio/gauntlet4/guion/excepcions-r2.yaml \
    --escenas ../../plan-de-negocio/gauntlet4/video/escenas-v2-produccion.json --so-imaxes
  echo \"rc \$? \$(date -u)\""
pkill -f languagetool-server.jar
echo "r3 fin $(date -u)"
