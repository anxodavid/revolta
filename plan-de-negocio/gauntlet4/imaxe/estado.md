# Peza IMAXE (Gauntlet 4, rolda 1): estado

Director de arte: axente Claude. Actualízase en cada fito. Última actualización: 03-10-2026, 09:10 UTC.

## Feito

- **Referencias** (A1): as 226 baixadas a `$SCRATCH/referencias/` e miradas por Claude en follas por concepto;
  licenzas comprobadas nas APIs de Commons e do Met (coinciden co CSV). Escolla en `referencias-escollidas.md` e
  `referencias.json` (29 sementes permitidas, 21 BY-SA tal cal, 1 "non").
- **Porta v6** (A2): `herramientas/pipeline/revisor.py` VERSION 9 (Florence-2-base por defecto, lista nova, campo
  `epoca`, CLIP con 9 recortes, 6 pares novos, `clave` por z). Calibración e avaliación nas 173 imaxes etiquetadas
  da v1: `calibracion/porta-v6.json`, `calibracion/etiquetas-v1.json` (scripts `etiquetas_v1.py`, `calibrar_clip.py`,
  `avaliar_porta.py`).
- **Correlación** (A3): `herramientas/pipeline/correlacion.py` (CLIP-L fronte a `texto_en`); `v1-texto-en.json`
  (tradución de Claude) e liña de base da v1 en `calibracion/correlacion-v1.json`.
- `imaxes.py`: campo `referencia` (img2img e ControlNet de profundidade; `encadre: encaixar` e `recorte`).
- Borradores: `biblia-v2.md`, `../aprendizaxes/imaxe.md`.
- Modelos novos na caché principal: Florence-2-base, ControlNet depth SDXL small (fp16), Depth-Anything-V2-Small.
  **Borrado Florence-2-large** (orde do orquestrador).

## Rolda 1 pechada (03-10-2026, orde do orquestrador)

Feito ademais do anterior: folla A/B das sementes (`ab-sementes.jpg`, 7 escenas x 4 técnicas), proba da biblia v2
(`biblia-v1-v2.jpg`), porta v6 sobre as 48 imaxes novas, perfil de tempos, Florence OVD (non serve) e correlación
v1/v2 da biblia (`calibracion/`). Informe: `informe-r1.md` (§6, configuración recomendada para D18).

Sen facer (por cota e por orde de non lanzar máis experimentos): refinado a 1344 (`scripts/refinar_proba.py`, listo),
TAESD-XL, SDXL afinado e IP-Adapter (disco). Para a rolda 2, o que diga o crítico visual.

## Como retomar

```bash
export SCRATCH=/tmp/claude-0/-home-user-revolta/c92eba35-e89d-5d11-bb3d-f517a84dab48/scratchpad   # ou o da sesión nova
cd /home/user/revolta && source herramientas/pipeline/entorno.sh && mkdir -p $SCRATCH/imaxe4/logs
I=plan-de-negocio/gauntlet4/imaxe/scripts
# 1) referencias (≈ 15 min, só rede; reintenta os 429)
$PY $I/urls_refs.py > $SCRATCH/imaxe4/urls_refs.tsv && mkdir -p $SCRATCH/referencias && bash $I/baixar_refs.sh
# 2) modelos desta peza (≈ 0,9 GB): Florence-2-base, ControlNet depth small, Depth-Anything-V2-Small
$PY $I/baixar_modelos.py
# 3) catálogo, licenzas e escolla (só rede e CPU lixeira)
python3 $I/catalogo_refs.py > $SCRATCH/imaxe4/catalogo_refs.json
python3 $I/licenzas_commons.py $SCRATCH/imaxe4/catalogo_refs.json > $SCRATCH/imaxe4/licenzas.json
python3 $I/escoller_refs.py $SCRATCH/imaxe4/catalogo_refs.json $SCRATCH/imaxe4/licenzas.json > plan-de-negocio/gauntlet4/imaxe/referencias.json
# 4) calibración da porta (CLIP-L ≈ 25 min con candado) e avaliación (lixeira)
herramientas/gauntlet/candado.sh $PY $I/calibrar_clip.py calcular && $PY $I/calibrar_clip.py analizar
git show c4fcc72:herramientas/pipeline/revisor.py > $SCRATCH/imaxe4/revisor_v8_arranxos.py
$PY $I/avaliar_porta.py $SCRATCH/imaxe4/revisor_v8_arranxos.py
# 5) A/B de sementes e biblia (SDXL, ≈ 20 min por tanda, con candado)
export IMG_MODEL=lightning1024
bash $I/cadea_r1.sh   # sementes (as 7 escenas), biblia, porta nas imaxes novas e Florence OVD, cada paso co candado
$PY $I/sementes_ab.py folla
$PY $I/biblia_proba.py folla
herramientas/gauntlet/candado.sh $PY $I/correlacion_biblia.py; herramientas/gauntlet/candado.sh $PY $I/perfil_tempos.py
```

Antes de `avaliar_porta.py`: `python3 $I/florence_gardado.py` (as descricións de Florence-2-base que gardou a
produción en `gauntlet3/video/imaxes/revision.json` e no `revision.json` de git `4f43fb5`).
