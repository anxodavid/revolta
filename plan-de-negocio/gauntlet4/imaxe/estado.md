# Peza IMAXE (Gauntlet 4, rolda 1): estado

Director de arte: axente Claude. Actualízase en cada fito. Última actualización: 02-10-2026, 23:55 UTC.

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

## En curso (á espera do candado de CPU)

- `scripts/sementes_ab.py xerar aldea,carro,lareira` (log `$SCRATCH/imaxe4/logs/ab1.log`) e
  `palloza,queimada,horreo` (`ab2.log`).
- `scripts/florence_ovd.py`: ¿ve Florence-2-base a bombilla, o radiador e a maleta de rodas? (`florence_ovd.log`).

## Falta

1. Folla A/B das sementes (`ab-sementes.jpg`) e xuízo; proba da biblia v2 (`scripts/biblia_proba.py`, 20 imaxes) e
   a folla `biblia-v1-v2.jpg`; tempo a 1344x768.
2. Revisar coa porta v6 as imaxes A/B e da biblia (clave e anacronismos).
3. `informe-r1.md` e pechar `../aprendizaxes/imaxe.md`.

Non se farán nesta rolda (falta de disco, orde do orquestrador): SDXL fotorrealista afinado e IP-Adapter.

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
flock "$CPU_LOCK" $PY $I/calibrar_clip.py calcular && $PY $I/calibrar_clip.py analizar
git show c4fcc72:herramientas/pipeline/revisor.py > $SCRATCH/imaxe4/revisor_v8_arranxos.py
$PY $I/avaliar_porta.py $SCRATCH/imaxe4/revisor_v8_arranxos.py
# 5) A/B de sementes e biblia (SDXL, ≈ 20 min por tanda, con candado)
export IMG_MODEL=lightning1024
flock "$CPU_LOCK" $PY $I/sementes_ab.py xerar aldea,carro,lareira
flock "$CPU_LOCK" $PY $I/sementes_ab.py xerar palloza,queimada,horreo
$PY $I/sementes_ab.py folla
flock "$CPU_LOCK" $PY $I/biblia_proba.py xerar && $PY $I/biblia_proba.py folla
```

Antes de `avaliar_porta.py`: `python3 $I/florence_gardado.py` (as descricións de Florence-2-base que gardou a
produción en `gauntlet3/video/imaxes/revision.json` e no `revision.json` de git `4f43fb5`).
