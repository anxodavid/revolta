# Estado da peza MOVEMENTO (Gauntlet 4, rolda 1)

Ficheiro do construtor (enxeñeiro de VFX, axente Claude). Actualízase en cada fito. **Se a sesión se corta, retomar
desde aquí** (non repetir medidas que xa estean en `probas/medidas-*.json`).

Última actualización: 03-10-2026, 11:35 UTC (rolda 1 pechada).

## Feito (rolda 1 pechada)

- Código: `herramientas/pipeline/movemento.py` (paralaxe 2,5D, 8 cámaras, 8 efectos, clips I2V con cámara lenta
  RIFE en MP4 e transferencia de detalle, porta de vídeo recalibrada), `movemento_i2v.py` (T5 fp8 por lotes, LTX 2B
  con caché por hash; colle o candado cooperativo el mesmo: **non envolvelo en `candado.sh`**, interbloquéase),
  integración en `montaxe.py` (planos con `animacion`; sen ela, fotogramas idénticos aos da v1) e `longo.py`.
- Medidas e tiras en `probas/`: 6 clips I2V (470-660 s por clip), paralaxe e efectos, porta.
- Demos: `demo-gancho.mp4` (I2V nos planos 14 e 22) e `demo-durmir.mp4`. Informe: `informe-r1.md`.
- Caché en `$SCRATCH/movemento/` (`i2v/`: 6 clips + cámara lenta; `prof/`, `masc/`). Embeddings das 14 accións de
  proba en `$SCRATCH/video/emb/`. O T5 fp8 está borrado (volver baixalo para accións novas).

## Falta

- Pasar a porta cos 4 malos sintéticos e remontar a demo cos 5 clips (3, 14, 17, 18, 22): `bash
  plan-de-negocio/gauntlet4/movemento/scripts/lote_r3.sh` (≈ 20 min de CPU co candado). Cancelouse o 03-10 ás 11:30
  UTC porque a produción da v2 tiña o candado.
- Rolda 2 (se o crítico o pide): máis clips para calibrar a porta, 1024x576 só en rostros e mans, Wan non probado.

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
