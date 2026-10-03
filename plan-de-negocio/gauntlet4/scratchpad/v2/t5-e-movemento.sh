#!/usr/bin/env bash
# Relanzamento tras o reinicio das 18:53: remata os embeddings do T5 (xa baixado) e lanza os clips I2V das imaxes
# revisadas; a rexeneración lánzaa o orquestrador cando estea aplicada a 2.ª pasada da revisión (43-77).
R=/home/user/revolta
bash $R/plan-de-negocio/gauntlet4/video/scripts/t5.sh
exec bash $R/plan-de-negocio/gauntlet4/video/scripts/movemento.sh
