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

## Comparativa de modelos (30-09-2026, `herramientas/pipeline/probas/visual_comparar_modelos.py`)

Mismos 8 prompts (escenas gallegas de las 4 fases: lareira de noche, cruceiro con luna y tormenta, aldea con hórreo,
carro de bois, costa al atardecer, manos hilando junto a un candil, carballeira con luna, brasas) y mismas semillas,
en dos estilos: `filme` = "cinematic film still, period drama, photorealistic" y `pintura` = "realistic oil painting,
dramatic chiaroscuro". CPU de 4 núcleos, bf16, VAE en `channels_last`, cada modelo con el candado de CPU.
Rejillas en `plan-de-negocio/gauntlet3/visual/comparativa/`.

| Modelo | Resolución | Carga | s/imagen (mediana; mín-máx) | Licencia |
|---|---|---|---|---|
| (a) SDXL-Turbo, 4 pasos (Gauntlet 2) | 1024x576 | 13,7 s | **25,5** (22,2-28,3), 16 imágenes | Stability AI Community License |
| (b) SDXL base + UNet Lightning 4 pasos | 1344x768 | 18,0 s | **47,6** (44,0-75,5), 16 imágenes (23 con las de calibración: 47,1) | OpenRAIL++-M |

Lo que vio Claude en las imágenes (juicio de Claude, no de una persona):
- **El prompt pesa más que el modelo en la luz**: con los prompts nuevos (fuente de luz explícita, fase) Turbo ya da
  lumbre, luna, contraluz y atardecer; el gris plano de la ronda 3 venía del estilo fijo "soft overcast light".
- **Lightning 1344x768 es claramente más nítido y más "de cine"**: planos más abiertos y compuestos, manos más
  creíbles, texturas (musgo, piedra, lana) reales; Turbo a 1024x576 es más blando y más "ilustración".
- Estilo: `pintura` en Lightning sale saturado y brillante, el "óleo genérico de IA" que el crítico rechazó; `filme`
  es lo más parecido a la referencia. **Se elige `filme`.**
- **Ninguno de los dos entiende "granary raised on stone pillars" ni "solid wooden disc wheels"**: sale una aldea
  inglesa (Cotswolds) sin hórreo y carros con **ruedas de radios** (en los dos modelos y los dos estilos). Hace falta
  otra forma de pedirlos (experimento de iconografía, abajo) y la puerta de CLIP.
- Lightning mete **detalles modernos** que Turbo no: ventanas de cristal con cuarterones, una estufa de hierro en
  vez de lareira, una farola junto al cruceiro. Florence-2 (ventanas, farolas) y la lista de la puerta deben pararlos.
- "a traditional village in Galicia, Spain, stone houses" dio una aldea de piedra con tejado gris verosímil
  (1 imagen): **la palabra "Galicia, Spain" no confunde a SDXL** como supuse; se corrige la biblia (se desaconsejaba).

## Gradación por fase (`imaxes.graduar`, sustituye la igualación a la media del episodio)

- La igualación de la ronda 3 (transferencia de media y desviación en YCbCr hacia la media del episodio, saturación
  0,85) es justo lo que aplanaba la luz: llevaba el plano de lumbre y el de mediodía al mismo gris. Ahora cada imagen
  conserva su luz y solo se corrigen los extremos: si la luminancia media se sale del rango de su fase, una gamma la
  lleva al borde (no a la media); contraste alrededor de su propia media y brillo de `curva.py`; nivel de negro por
  fase; saturación por fase con tope de croma; virado común muy ligero.
- Prueba con 6 fotogramas de la ronda 3 (antes/después mirado por Claude): el plano de durmir (luminancia 0,415) baja
  a 0,31 con gamma 1,37, contraste 0,92 y saturación 0,80; el del gancho sube el contraste a 1,07. **Primer intento
  con negros levantados (toe 0,012) en todas las fases: lavaba el "negro profundo" del gancho**; ahora el nivel de
  negro es por fase (0 en el gancho, 0,02 al durmir).
- **Suavizado**: con una media móvil de ±3 planos, en una hoja de 16 planos (4 por fase) se mezclaban fases enteras;
  ahora la ventana va en palabras del guion (±60, ~30 s de narración): solo mezcla cerca de los cambios de fase.

## Rótulos y grano (`montaxe.py`)

- Fotograma de prueba (`probas/visual_rotulo_proba.py`) con el título sobre una carballeira nocturna y sobre una costa
  al atardecer: sobre lo oscuro se lee bien; sobre espuma y cielo claros el título perdía contraste. Se añade una
  **banda oscura muy difusa** detrás del bloque de texto (opacidad 0,30, desenfoque 45 px): se lee en los dos casos sin
  que se vea una caja (juicio de Claude mirando los fotogramas).
- **Grano de película** opcional (`MONTAXE_GRAO`, 0 por defecto): ruido gaussiano a media resolución (grano de ~2 px),
  6 texturas alternadas cada 2 fotogramas, más fuerte en tonos medios. Al 3 % se ve "sucio" en el cielo; al 1,5 % es
  sutil. **No se activa por defecto** hasta medir su coste en bitrate (x264 CRF 22 con tope de 1,4 Mb/s: el grano es
  lo primero que el codificador se come y lo que más bits gasta) [S].
