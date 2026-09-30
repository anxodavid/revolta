# Aprendizajes: pieza VISUAL (Gauntlet 3)

Agente director de arte e ingeniero de imagen (Claude), 30-09-2026. Todo lo que sigue lo hizo Claude (agente) con
scripts; las medidas son automáticas; **las valoraciones de imágenes ("se ve", "sale") son de Claude mirando las
imágenes**, no de una persona. La hoja de prueba no la juzga este agente: la juzga un crítico ciego.

## Referencia (storyboard de *Historia Desconocida*)

- yt-dlp 2026.08.19: con el cliente `android_vr` YouTube pedía "Sign in to confirm you're not a bot" (HTTP 429 en la
  página); `tv_simply` e `ios` igual. **`mweb` sí da los storyboards y además uno de 320x180** (`sb0`, antes solo
  teníamos 160x90 con `android_vr`); `web_embedded` da 160x90.
- El `.mhtml` que escribe yt-dlp llegó con **la mayoría de las hojas corruptas** (JPEG que PIL abre pero con basura
  de colores; dos que no abren). Bajando cada hoja con `curl` desde su `Content-Location` salieron todas bien: 25
  hojas de 3x3 → **220 miniaturas de 320x180** (una cada ~9,9 s). Están en el scratchpad
  (`$SCRATCH/visual/ref/`), no en el repo (imágenes de terceros).
- Lo que se ve a 320x180: fotorrealismo de drama de época; interiores dorados con velas y lámparas, contraluces en
  ventanas, sótanos con antorcha, cocina con fuego, exteriores fríos (niebla, nieve) y jardines soleados; cada plano
  con una acción concreta (fregar, cocinar, escribir, vestir); mucho plano medio y detalle de manos con objetos.

## Modelos: qué se reutiliza y qué se baja

- API de HF (30-09-2026, `HfApi.model_info(files_metadata=True)`): `text_encoder/model.fp16.safetensors` y
  `text_encoder_2/model.fp16.safetensors` tienen **el mismo sha256 en SDXL-Turbo y en SDXL base 1.0**
  (`660c6f5b…` y `ec310df2…`): se cargan del repo de Turbo y no se bajan 1,6 GB más. Los `vocab.json` y
  `merges.txt` también son iguales; los `config.json` solo difieren en la versión de transformers/diffusers.
- El **VAE fp16 es distinto** (`02ee4bd1…` en Turbo, `bcb60880…` en base): se baja el de base (167 MB, 4 s).
- ByteDance/SDXL-Lightning (licencia `openrail++`, la de SDXL base): `sdxl_lightning_4step_unet.safetensors`
  5,14 GB en **121 s** a través del proxy. Cada UNet completa pesa lo mismo (1, 2, 4 y 8 pasos); las LoRA
  (394 MB) necesitarían además la UNet de SDXL base (5,14 GB) y dan algo menos de calidad según la ficha.
- Disco: 15 GB libres al empezar; 9,2 GB tras bajar la UNet de 4 pasos (los otros agentes también escriben).
