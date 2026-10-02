# Peza IMAXE (Gauntlet 4, rolda 1): estado

Director de arte: axente Claude. Actualízase en cada fito. Última actualización: 02-10-2026, 23:10 UTC.

## Feito

- Lecturas (contexto, biblia v1, aprendizaxes visuais, `imaxes.py`, `revisor.py` coa lista ampliada da rolda de
  arranxos, tribunal final §2, 162 imaxes da v1 e as 11 anteriores aos arranxos, recuperadas de git `4f43fb5`).
- Modelos na caché principal (`$SCRATCH/hf`): Florence-2-base (MIT), ControlNet depth SDXL small fp16 (OpenRAIL++),
  Depth-Anything-V2-Small (Apache-2.0). **Borrado Florence-2-large** (1,5 GB) por orde do orquestrador.
- `v1-texto-en.json`: versión en inglés (de Claude) dos 162 anacos de narración, para medir a correlación con CLIP-L.

## En curso

- Baixada das 226 referencias a `$SCRATCH/referencias/` (`scripts/baixar_refs.sh`; Commons dá 429 aos orixinais e ás
  veces ás miniaturas: o script usa miniaturas de tamaño estándar e reintenta).

## Falta

1. Follas de contactos por concepto, escolla e `referencias-escollidas.md` + `referencias.json` (licenza comprobada).
2. Porta v6 (`revisor.py`, VERSION 9) e a súa calibración coas 173 imaxes (162 + 11 anteriores aos arranxos).
3. Medida de correlación CLIP-L (imaxe fronte a `texto_en`).
4. Sementes: texto só / img2img / ControlNet depth en 5-6 conceptos; campo `referencia` en `imaxes.py`.
5. `biblia-v2.md` e proba de 8-10 prompts.
6. `informe-r1.md` e `../aprendizaxes/imaxe.md`.

Probas que non se farán nesta rolda por falta de disco (orde do orquestrador): SDXL fotorrealista afinado e
IP-Adapter.

## Como retomar

```bash
export SCRATCH=/tmp/claude-0/-home-user-revolta/c92eba35-e89d-5d11-bb3d-f517a84dab48/scratchpad   # ou o da sesión nova
cd /home/user/revolta && source herramientas/pipeline/entorno.sh
# referencias (≈ 10-15 min, só rede; reintenta os 429)
$PY plan-de-negocio/gauntlet4/imaxe/scripts/urls_refs.py > $SCRATCH/imaxe4/urls_refs.tsv
mkdir -p $SCRATCH/referencias && bash plan-de-negocio/gauntlet4/imaxe/scripts/baixar_refs.sh
# modelos desta peza (≈ 0,9 GB)
$PY plan-de-negocio/gauntlet4/imaxe/scripts/baixar_modelos.py
```
