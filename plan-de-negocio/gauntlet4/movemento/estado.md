# Estado da peza MOVEMENTO (Gauntlet 4, rolda 1)

Ficheiro do construtor (enxeñeiro de VFX, axente Claude). Actualízase en cada fito. **Se a sesión se corta, retomar
desde aquí** (non repetir medidas que xa estean en `probas/medidas-*.json`).

Última actualización: 02-10-2026, 23:35 UTC.

## Feito

- Contorno de vídeo aparte (`$SCRATCH/video/venv`, 1,8 GB): torch 2.14.1+cpu, diffusers 0.40.0, transformers
  5.18.0, accelerate 1.15.0, opencv-python-headless 5.0.0.93, imageio-ffmpeg 0.6.0 (lista enteira:
  `scripts/requisitos-video.txt`).
- Modelos baixados (en `$SCRATCH/video/hf`, `HF_HOME` propio para poder borralos sen tocar o contorno principal):
  - `Lightricks/LTX-Video`: `ltxv-2b-0.9.8-distilled.safetensors` (6,34 GB, transformer e VAE en bf16) e os
    `json`/`tokenizer` do repo. Licenza: **LTXV Open Weights License 0.X** (ver informe).
  - `comfyanonymous/flux_text_encoders`: `t5xxl_fp8_e4m3fn.safetensors` (4,89 GB, Apache-2.0): o T5-XXL que usa LTX.
- Embeddings de T5 para 14 accións (`scripts/accions.json`) en `$SCRATCH/video/emb/` (`scripts/t5_emb.py`: pesos
  en fp8, cálculo en fp32; 6 s de carga, ≈ 21 s por texto, pico 6,4 GB). O T5 só fai falta para accións novas.

- Primeira medida de I2V (LTX 2B, plano 22, 800x448, 49 fotogramas, 8 pasos): 470 s; camiña de verdade
  (`probas/ltx_p22_*`, `probas/medidas-ltx.json`).
- Código: `herramientas/pipeline/movemento.py` (paralaxe 2,5D, efectos, encaixe de clips I2V con cámara lenta
  RIFE e transferencia de detalle, porta de vídeo), `movemento_i2v.py` (T5 por lotes e LTX con caché por hash, no
  venv de vídeo; colle o candado el mesmo: non envolvelo en `flock`), integración en `montaxe.py` (planos con
  `animacion`; sen ela, Ken Burns coma na v1) e `longo.py` (pasa `animacion`).
- Imaxes da v1 graduadas coma na montaxe da v1 en `$SCRATCH/video/demo/graduadas/` (`scripts/demo_gancho.py
  preparar`): os clips I2V da demo condiciónanse nelas.

## En curso

- Clips I2V das probas que serven tamén para a demo (`scripts/lanzar_i2v.sh xerar i2v_probas1.json`: planos 3, 7,
  22, 1 e 14) e primeira proba da paralaxe e dos efectos (`lanzar_plx1.sh`). Os dous agardan o candado.

## Falta

Mirar as tiras (mans, rostro, lume), calibrar a porta de vídeo, resto de clips da demo (2, 5, 17, 18), montar a
demo (`demo_gancho.py montar`), informe e aprendizaxes. Opcional: Wan2.2-TI2V-5B (só se cabe en ≈ 13 GB para
`$SCRATCH/video`), proba a 1024x576 e con 6 pasos.

Tiras de Versalles (tarefa 10): YouTube só dá storyboards de 320x180 co cliente `mweb` (android_vr, ios e tv piden
iniciar sesión); non serven para ver movemento. Descartado.

## Como reconstruír o contorno de vídeo nunha sesión nova

    export SCRATCH=…/scratchpad; source herramientas/pipeline/entorno.sh
    /usr/bin/python3.11 -m venv $SCRATCH/video/venv
    $SCRATCH/video/venv/bin/pip install torch==2.14.1 torchvision==0.29.1 --index-url https://download.pytorch.org/whl/cpu
    $SCRATCH/video/venv/bin/pip install -c plan-de-negocio/gauntlet4/movemento/scripts/requisitos-video.txt \
        diffusers transformers accelerate huggingface-hub safetensors sentencepiece protobuf imageio imageio-ffmpeg \
        opencv-python-headless einops av ftfy psutil pillow numpy scipy
    # modelos (HF_HOME propio; HF_HUB_DISABLE_XET=1 como no contorno principal)
    HF_HOME=$SCRATCH/video/hf HF_HUB_DISABLE_XET=1 $SCRATCH/video/venv/bin/python -c "
    from huggingface_hub import hf_hub_download as d
    for f in ['model_index.json','scheduler/scheduler_config.json','transformer/config.json','vae/config.json',
              'text_encoder/config.json','tokenizer/added_tokens.json','tokenizer/special_tokens_map.json',
              'tokenizer/spiece.model','tokenizer/tokenizer_config.json','ltxv-2b-0.9.8-distilled.safetensors']:
        d('Lightricks/LTX-Video', f)
    d('comfyanonymous/flux_text_encoders', 't5xxl_fp8_e4m3fn.safetensors')"
    # embeddings das accións (co candado): copiar scripts/ a $SCRATCH/video/probas/ e
    flock $CPU_LOCK env HF_HOME=$SCRATCH/video/hf $SCRATCH/video/venv/bin/python t5_emb.py accions.json 256

Descarga medida o 02-10-2026: 11,2 GB en ≈ 100 s.
