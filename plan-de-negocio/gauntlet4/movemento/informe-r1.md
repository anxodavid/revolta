# MOVEMENTO, rolda 1: que movemento é posible en CPU e a que custo

Construtor: enxeñeiro de VFX (axente Claude), 02-10-2026. **Borrador en curso**: as táboas énchense segundo saen as
medidas (`probas/medidas-*.json`). Todo o que se di da calidade sae de mirar tiras de fotogramas (JPEG): ningún
axente viu os clips en movemento.

## 1. Resumo

(por escribir ao final)

## 2. Máquina e método

- CPU Intel Xeon 2,8 GHz, 4 núcleos, AVX-512 **sen bf16 nin AMX** (`/proc/cpuinfo`), 13,36 GiB de memoria para
  todos os procesos (cgroup v1: `memory.limit_in_bytes` = 14.345.035.776). Cada medida co candado común de CPU.
- Memoria: pico do proceso (`VmHWM`, inclúe as páxinas do ficheiro de pesos mapeadas) e pico da memoria anónima de
  todo o cgroup (`total_rss` de `memory.stat`, mostraxe cada 0,5 s).

## 3. Imaxe a vídeo (I2V)

(táboa de medidas e calidade por clip)

## 4. Paralaxe 2,5D

(que fai, custo por fotograma)

## 5. Microanimacións

(efectos, máscaras, custo)

## 6. Cámara lenta e escala

## 7. Porta de vídeo

## 8. Orzamento para un episodio de 12 min (D18)

## 9. Licenzas

| Peza | Licenza | URL |
|---|---|---|
| LTX-Video 2B 0.9.8 destilado (Lightricks) | **LTXV Open Weights License 0.X** (15-04-2025, vale para todas as versións desde a 0.9.6): uso libre, tamén comercial, para entidades con menos de 10 M$ de ingresos anuais; as de máis teñen que mercar licenza. Restricións de uso do anexo A, entre elas (e) non difundir contido xerado sen avisar de forma expresa e intelixible de que o xerou unha máquina | https://huggingface.co/Lightricks/LTX-Video/blob/main/LTX-Video-Open-Weights-License-0.X.txt |
| T5-XXL v1.1 (codificador de texto de LTX), ficheiro fp8 de comfyanonymous | Apache-2.0 | https://huggingface.co/comfyanonymous/flux_text_encoders |
| Depth-Anything-V2-Small | Apache-2.0 (as versións Base e Large son CC BY-NC 4.0: non se usan) | https://huggingface.co/depth-anything/Depth-Anything-V2-Small-hf |
| CLIPSeg rd64 refined (máscaras por texto) | Apache-2.0 | https://huggingface.co/CIDAS/clipseg-rd64-refined |
| RIFE v4 (ECCV2022-RIFE, © Megvii), en safetensors | MIT | https://huggingface.co/TensorForger/RIFE-safetensors |
| MediaPipe (pose e mans) / CLIP ViT-L/14 (porta) | Apache-2.0 / MIT | xa no contorno principal |
| Wan2.2-TI2V-5B / FastWan2.2-TI2V-5B (non probados en CPU, ver §3) | Apache-2.0 | https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers, https://huggingface.co/FastVideo/FastWan2.2-TI2V-5B-FullAttn-Diffusers |

Consecuencia da cláusula (e) de LTXV para a canle: o aviso falado actual di que a voz é sintética e que o texto o
preparou un proceso automático, pero non fala das imaxes; ademais da etiqueta de contido sintético de YouTube, a
descrición debería dicir que imaxes e vídeo están xerados por IA (proposta para o orquestrador).

## 10. Alternativa con GPU alugada (prezos do 02-10-2026)

| Servizo e modelo | Prezo | Fonte |
|---|---|---|
| Replicate, `wan-video/wan-2.2-i2v-fast` (Wan 2.2 A14B I2V optimizado por PrunaAI; 81 fotogramas a 16 fps ≈ 5 s) | 0,05 $ por vídeo a 480p; 0,11 $ a 720p (0,065 / 0,145 $ con interpolación a 30 fps) | https://replicate.com/wan-video/wan-2.2-i2v-fast |
| fal.ai, Wan 2.2 A14B I2V | 0,04 $/s a 480p, 0,06 $/s a 580p, 0,08 $/s a 720p (segundos contados a 16 fps) | https://fal.ai/models/fal-ai/wan/v2.2-a14b/image-to-video |
| fal.ai, LTX-Video 13B 0.9.8 destilado I2V | 0,02 $/s (contado a 24 fps) | https://fal.ai/models/fal-ai/ltxv-13b-098-distilled/image-to-video |
| fal.ai, LTX-2 fast I2V | 0,04 $/s a 1080p (clips de 6 a 20 s) | https://fal.ai/models/fal-ai/ltx-2/image-to-video/fast |
| Hugging Face Inference Providers | o mesmo prezo ca o provedor, sen marxe (`docs/APRENDIZAJES.md`) | https://huggingface.co/docs/inference-providers/pricing |

(custo dun episodio: ver §8)
