I=/home/user/revolta/plan-de-negocio/gauntlet3/video/imaxes
O=$SCRATCH/video/saida/plx
PR=/home/user/revolta/plan-de-negocio/gauntlet4/movemento/scripts/proba_plano.py
$PY $PR $I/010-b2223ce8-0.jpg '{"modo":"paralaxe","camara":"avanza","efectos":["bretema"]}' 6 $O/p11_avanza_bretema --media
$PY $PR $I/000-c13ff7ad-0.jpg '{"modo":"paralaxe","camara":"avanza","efectos":["lume"]}' 5 $O/p01_avanza_lume --media
$PY $PR $I/009-7d019425-1.jpg '{"modo":"paralaxe","camara":"xira_der","efectos":["candea"]}' 6 $O/p10_xira_candea --media
$PY $PR $I/008-83441bad-0.jpg '{"modo":"paralaxe","camara":"pan_esq","efectos":["choiva"]}' 6 $O/p09_pan_choiva --media
$PY $PR $I/020-194670e7-0.jpg '{"modo":"paralaxe","camara":"avanza","efectos":["auga"]}' 5 $O/p21_avanza_auga --media
$PY $PR $I/004-6c78d74f-0.jpg '{"modo":"paralaxe","camara":"xira_esq","efectos":["ceo","po"]}' 6 $O/p05_xira_ceo_po --media
echo PLX1_FIN
