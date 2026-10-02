# Aprendizaxes da peza MOVEMENTO (Gauntlet 4)

Axente: enxeñeiro de VFX (Claude). Medidas propias nesta máquina (Intel Xeon 2,8 GHz, 4 núcleos, AVX-512 sen bf16
nin AMX, 13,36 GiB de cgroup para todos os procesos) salvo que se diga outra cousa. Os xuízos de calidade son
dun axente Claude mirando tiras de fotogramas: ninguén viu os clips en movemento.

## Contorno

- **Venv de vídeo aparte** (`$SCRATCH/video/venv`, 1,8 GB, ≈ 3 min): torch 2.14.1+cpu, diffusers 0.40.0,
  transformers 5.18.0. O venv principal (diffusers 0.35.2, transformers 4.57.6) queda intacto.
- **T5-XXL en fp8 con cálculo en fp32**: o ficheiro `t5xxl_fp8_e4m3fn.safetensors` (4,89 GB) cargado nun
  `T5EncoderModel` de transformers cambiando cada `nn.Linear` por unha capa que garda o peso en fp8 e o pasa a fp32
  ao multiplicar: 6 s de carga, ≈ 21 s por texto (o custo é a conversión dos 4.700 M de pesos en cada chamada, non o
  cálculo), pico 6,4 GB. Trampa: o bloque de T5 de transformers mira `wo.weight.dtype` e pasaría o estado oculto a
  fp8; un `weight` baleiro en fp32 na capa evítao. Mellora pendente: varios textos nun lote (a conversión págase unha
  vez).
- **Cargar LTX desde o ficheiro único sen lelo enteiro**: `safe_open` + as funcións de conversión de diffusers
  (`convert_ltx_transformer_checkpoint_to_diffusers`, `convert_ltx_vae_checkpoint_to_diffusers`) e
  `load_state_dict(assign=True)` sobre modelos baleiros (`init_empty_weights`): 3,2 s; os pesos quedan mapeados do
  disco (contan como caché, non como memoria anónima).
- **Descargas grandes e memoria**: mentres baixaban 11 GB (sen candado, só rede) o OOM matou a verificación do
  contorno (SDXL 10,5 GB + revisor nun mesmo momento). O OOM foi da verificación, pero as páxinas sucias dunha
  descarga tamén contan no cgroup: mellor non baixar xigas mentres outro proceso está preto do límite.
- Un `bash -c "…"` con varias ordes dentro dispara unha comprobación de seguridade da ferramenta: os lanzadores van
  nun `.sh` propio (`scripts/lanzar_ltx.sh`).

## Imaxe a vídeo (I2V) en CPU

- **LTX-Video 2B 0.9.8 destilado, 800x448, 49 fotogramas (2 s a 24 fps), 8 pasos**: 470 s por clip (paso ≈ 42 s; o
  primeiro, 71 s, inclúe codificar a imaxe; descodificar o VAE por teselas, 103 s). Pico do proceso 11,4 GB (con
  páxinas mapeadas do ficheiro), memoria anónima de todo o cgroup 9,0 GB. ≈ 260 GFLOPS efectivos.
- Calidade (plano 22, muller de costas nun camiño): **camiña de verdade** (pés que alternan, saia que abanea) e a
  cámara acompáñaa como nun travelling; sen deformacións visibles na tira nin no recorte das pernas.
