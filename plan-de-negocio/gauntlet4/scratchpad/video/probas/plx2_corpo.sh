G=$SCRATCH/video/demo/graduadas
O=$SCRATCH/video/saida/plx2
mkdir -p $O
R=/home/user/revolta/plan-de-negocio/gauntlet4/movemento/scripts
$PY $R/proba_plano.py $G/004-6c78d74f-0.png '{"modo":"paralaxe","camara":"xira_esq","efectos":["ceo","po"]}' 6 $O/p05_xira_ceo_po --media
$PY $R/proba_plano.py $G/009-7d019425-1.png '{"modo":"paralaxe","camara":"xira_der","efectos":["candea"]}' 6 $O/p10_xira_candea --media
$PY $R/proba_bordos.py $G/016-02ec0d98-0.png '{"modo":"paralaxe","camara":"xira_esq"}' 6 $O/p17_bordos.jpg
$PY $R/proba_bordos.py $G/001-69418ea4-0.png '{"modo":"paralaxe","camara":"pan_der"}' 6 $O/p02_bordos.jpg
$PY $R/proba_bordos.py $G/007-751c8b43-1.png '{"modo":"paralaxe","camara":"avanza","efectos":["lume"]}' 6 $O/p08_bordos.jpg
$PY $R/proba_compat_v1.py
echo PLX2_FIN
