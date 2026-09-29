# Pipeline automático de "Serán" (historia de Galicia para durmir)

De una **ficha de tema** (YAML con título, extensión y dossier de fuentes verificadas) a un **MP4 1920x1080 en
galego** con voz sintética de Nós, imágenes generadas en CPU y revisadas por una puerta automática, lluvia de fondo,
subtítulos galegos y un informe de QA. **Un solo comando, sin revisión humana (D5)**: el pipeline arranca su propio
LLM local, escribe el guion, lo valida, lo narra, genera y revisa las imágenes, monta y mide. Todo el software y los
modelos son abiertos o de pesos abiertos y corren en CPU (4 núcleos, 15 GB).

    source entorno-llm.sh        # variables del LLM local (ver abajo); nada más
    PY=$SCRATCH/tts/venv/bin/python
    $PY pipeline.py temas/irmandinos-apertura.yaml --llm openai --traballo DIR_VACÍO --saida ../../plan-de-negocio/gauntlet2/video

Salida en `--saida`: `ejemplo.mp4` (escrito de forma atómica: primero `.ejemplo.tmp.mp4` y se renombra al acabar),
`subtitulos.gl.srt`, `contactsheet.jpg` (4x3 fotogramas), `qa.json` y `qa.md` (veredicto PUBLICABLE / NON PUBLICABLE
con sus puertas). Los intermedios (respuestas del LLM con sus prompts y metadatos, guion, WAV, PNG de todos los
intentos, revisión de imágenes) quedan en `--traballo`; cada etapa se salta si ya está hecha.

## Historia honesta de la muestra

- **Ronda 1 (29-09-2026, archivada en `plan-de-negocio/gauntlet2/video/ronda1/`)**: las tres etapas LLM las respondió
  Claude Opus 5.5 en modo `manual` (el pipeline paraba con código 3 y se relanzaba). **No fue una ejecución
  desatendida** aunque el README y el qa.md de entonces lo decían. Su QA daba PUBLICABLE 9/9 sin mirar el contenido de
  las imágenes: el plano final tenía cuatro manos (un par sin cuerpo), una aldea con ventanas de vidrio y balcones y una
  multitud con picas y cruces.
- **Ronda 2 (esta versión)**: `--llm openai` contra un LLM local (EuroLLM-9B) arrancado por el propio pipeline, en un
  directorio de trabajo vacío, y puerta automática de imágenes con regeneración. Ninguna respuesta del LLM ni ninguna
  imagen se tocó a mano. El mismo comando se relanzó 4 veces en el mismo directorio para corregir código (cortes de
  plano, reservas y lista del revisor, bloqueo de la montaje, esqueletos y hogueras que la lista no cubría). Las etapas
  ya hechas se leyeron de la caché de esa misma ejecución. Todo está detallado en la nota de `qa.md` y en
  `video/execucion/logs/`. **Veredicto automático: NON PUBLICABLE** (10/12 puertas): falla lengua (11 avisos de
  LanguageTool) y H1 (1 falso positivo del tokenizador). El modo `manual` queda solo para depurar prompts.

## Etapas

| # | Etapa | Qué hace | Software / modelo (licencia) |
|---|---|---|---|
| 1 | guion | **Por bloques** (por defecto): el LLM elige 2-3 hechos del dossier para el gancho y los reescribe; escribe el resumen y la invitación a dormir; elige los hechos del relato y escribe **un párrafo por hecho** (tono que baja de vivo a sereno). Cada bloque se valida (cifras, signos, preguntas, "imaxina", frases > 30 palabras, nombres y cantidades no anclados en el dossier) y se reintenta hasta 2 veces con los problemas. El aviso y la fórmula son texto fijo que pone el código. Alternativa `--guion enteiro`: un solo prompt (`prompts/guion.md`) con validación y 2 revisiones (`prompts/revisar.md`) | LLM local, `prompts/bloque_*.md` |
| 2 | corrixir | LanguageTool gl-ES por párrafo; si hay avisos, el LLM corrige ese párrafo; solo se acepta si baja el número de avisos y no empeora la validación | LanguageTool 6.8 (LGPL-2.1) con hunspell gl; `prompts/corrixir_parrafo.md` |
| 3 | voz | Narra frase a frase con **ritmo en embudo** (feedback del promotor): escala de duraciones 1,05 en las primeras 150 palabras que sube hasta 1,25 hacia la palabra 320; pausas de 0,55 s entre frases al principio que suben hasta 1,35 s, más 0,45-1,0 s entre párrafos y un ajuste por longitud de la frase siguiente (la cadencia ya no es fija) | Nos_StyleTTS2-Brais-GL (Proxecto Nós/USC), Cotovía para fonemas |
| 4 | escenas | El **código** corta los planos con las duraciones reales de la voz: ~5,5 s en el gancho, subiendo a ~12,5 s; una frase larga se reparte en varios planos. El LLM escribe un prompt de imagen por plano (`prompts/escenas.md`: personas haciendo cosas, planos medios, luz variada, lista de anacronismos prohibidos) | LLM local |
| 5 | imaxes | SDXL-Turbo 1024x576, 4 pasos. **Puerta de imágenes** (`revisor.py`): cada imagen se revisa y, si falla, se regenera con otra semilla (desde el 3.er intento, con una coletilla prudente: figuras de cuerpo entero); tras 5 intentos se queda la de menos problemas y la puerta `imaxes_revisadas` falla | SDXL-Turbo (Stability AI Community License); MediaPipe (Apache-2.0); Florence-2-large (MIT) |
| 6 | son | Lluvia sintetizada por código (sin grabaciones de terceros). Voz a -17 LUFS, lluvia 17 dB por debajo | numpy/scipy, pyloudnorm |
| 7 | montaxe | Ken Burns, niebla ligera (6 %, antes 13 %: lavaba todo de verde), viñeta, **fundidos de 1,2 s** (antes 3 s: la doble exposición se veía mucho), x264 CRF 22 con tope de 1,1 Mb/s, AAC 128 kb/s, subtítulos `mov_text` `glg` | PIL, numpy, ffmpeg de `imageio-ffmpeg` |
| 8 | qa | Controles automáticos y hoja de contactos (sus 12 fotogramas se desplazan fuera de los fundidos) | faster-whisper + Whisper turbo galego de Nós, LanguageTool, ffmpeg `ebur128` |

## La puerta de imágenes (`revisor.py`)

1. **Manos y cuerpos** (MediaPipe `hand_landmarker` + `pose_landmarker_full`): una mano cuya muñeca está a más de 0,14
   (distancia normalizada) de la muñeca de cualquier cuerpo detectado es "man sen corpo"; más de dos manos por cuerpo
   también falla.
2. **Lista de anacronismos y vetos** sobre la descripción detallada y los objetos que ve **Florence-2-large** (MIT):
   ventanas de vidrio, balcones, tejados rojos o de teja, vehículos, objetos modernos (farolas, relojes, cables...),
   interiores modernos (dormitorios, lámparas, cortinas), texto o letras (también "writing"), cruces portadas, armas de
   fuego, sangre, edificios ardiendo, esqueletos, calaveras o cadáveres y hogueras grandes en el exterior. Las
   vidrieras góticas ("stained glass") no cuentan como ventanas modernas. `VERSION` sube cuando cambia la lista, y
   `imaxes.py` vuelve a revisar las imágenes guardadas con una versión anterior.

**Calibración con las 15 imágenes de la ronda 1** (`probas/revisor_ronda1.jsonl`, versión 3): marca 9 de 15, entre ellas la del cierre con cuatro
manos ("man sen corpo"), la aldea de 1:15 (tejados), la multitud con cruces, el dormitorio moderno, el reloj de la torre
y los pueblos de tejado rojo. Deja pasar paisajes, el anciano junto al fuego y los caminantes. Coste: ≈20 s por imagen
en CPU (dos pasadas de Florence-2) además de ≈16 s de generación.

Límites: MediaPipe solo ve manos medianas o grandes (las de una multitud lejana no se revisan, pero tampoco se notan);
Florence-2 describe objetos y materiales pero no cuenta dedos ni detecta caras deformes; la lista de palabras es
conservadora (falsos positivos = una regeneración más). No sustituye a una mirada humana: reduce la frecuencia de los
defectos graves, no la anula [S].

## El LLM local

`llm.py` renderiza cada prompt de `prompts/`, calcula su hash y guarda en `<traballo>/llm_cache/` el prompt, la
respuesta y sus metadatos (modelo, sha256 del GGUF, tokens, segundos, CPU del servidor). Con `LLM_SERVER_CMD` el
propio pipeline arranca el servidor si no hay uno escuchando y lo para al acabar la etapa 4 (libera ~9 GB de RAM para
SDXL-Turbo y Florence-2).

Modelos probados en CPU el 29-09-2026 (llama-cpp-python 0.3.19, Q4_K_M, 4 hilos), con el mismo prompt de guion:

| Modelo (licencia) | Resultado | Evidencia |
|---|---|---|
| `proxectonos/Llama-3.1-Carballo-Instr3` (Llama 3.1), GGUF `sdocio/...-Q4_K_M` | No trae plantilla de chat; con el formato `User:/Assistant:` de sus datos de instrucciones **no hace la tarea**: escribe un texto genérico sobre el canal. 1,1 tokens/s de media | `probas/llm_carballo_instr3/` |
| `proxectonos/Carvalho-Salamandra-Instruct` (MIT, "versión preliminar"), GGUF `mradermacher/...Q4_K_M` | Copia el dossier, luego **degenera** (repeticiones, traducciones y noticias en portugués) hasta el tope de 2.200 tokens | `probas/llm_carvalho_salamandra/` |
| **`utter-project/EuroLLM-9B-Instruct-2512`** (Apache-2.0, el gallego está entre sus lenguas), GGUF `mradermacher/...Q4_K_M` | Sigue la estructura y escribe en gallego. Con un solo prompt escribe corto, repite ejemplos del prompt y **se inventa datos** (fechas, cifras, una frase gritada): `probas/llm_eurollm_enteiro/`. Por eso el modo por bloques: tareas pequeñas de reescritura de 1-3 hechos, temperatura 0,3, validación y reintento por bloque | `probas/llm_eurollm_enteiro/`, `probas/llm_eurollm_bloques_proba/` |

Variables (`entorno-llm.sh` de la muestra): `LLM_URL`, `LLM_MODEL`, `LLM_FORMATO=chat`, `LLM_TEMP=0.3`,
`LLM_MAX_TOKENS=1600`, `LLM_SERVER_CMD="python -m llama_cpp.server --model EuroLLM-9B-Instruct-2512.Q4_K_M.gguf
--n_ctx 8192 --n_threads 4 --use_mmap false"`, `LLM_MODEL_FILE`, `LLM_MODEL_SHA256`. `--use_mmap false` evita tener los
pesos dos veces en RAM (mmap + reempaquetado), que provocó un OOM al compartir la máquina con Florence-2.

## Controles automáticos (etapa 8) y puertas de publicación

| Control | Cómo | Puerta |
|---|---|---|
| LLM local desatendido | Todas las respuestas del LLM vienen del servidor local (backend `openai`), ninguna de `manual` | obligatorio |
| Inteligibilidad | WER de ASR sobre la mezcla final y sobre la voz sola (`proxectonos/whisper-large-v3-turbo-gl-v1.0` en CTranslate2 int8); WER por frase | WER mezcla ≤ 0,06 (A1 del plan) |
| Sincronía subtítulos-voz | Marcas de tiempo por palabra del ASR contra el SRT (±0,5 s) | ≥ 95 % |
| Sincronía A/V | Duración decodificada de vídeo y audio | ≤ 0,1 s |
| Duración | Duración del vídeo | 180-300 s en esta muestra |
| Lengua | LanguageTool gl-ES; los nombres del dossier no cuentan como error ortográfico | ≤ 2 avisos [S] |
| H1-léxico (`ancoraxe.py`) | Nombres propios y cantidades que no están en el dossier ni en la ficha del tema | 0 sin anclar |
| Estilo | Sin cifras, signos que la voz no lee, preguntas ni palabras vetadas; aviso y fórmula literales | todo cumplido |
| **Imágenes** | `revisor.py` sobre la imagen escogida de cada plano | todas aprobadas |
| Sonoridad | `ebur128` sobre el MP4 | -18 a -16 LUFS (A2 del plan) |
| Peso y formato | MB, resolución | ≤ 50 MB, 1920x1080 |

Lo que **no** controla: la verdad de lo que el texto dice sin nombres ni cifras (una causa inventada, un sujeto
cambiado: sería H2, un juez LLM, sin implementar), la naturalidad del gallego más allá de LanguageTool, caras
deformes o ropas anacrónicas que Florence-2 no nombre.

## Instalación (CPU)

- Python 3.11 con `torch` (CPU), `diffusers==0.35.2`, `huggingface-hub<1.0`, `transformers<5` (4.57, que ya trae
  `Florence2ForConditionalGeneration`), `accelerate`, `faster-whisper`, `jiwer`, `language_tool_python` (Java ≥ 17),
  `pyloudnorm`, `imageio-ffmpeg`, `soundfile`, `scipy`, `pyyaml`, `mediapipe` (1.0.1; necesita `libegl1` y `libgles2`
  del sistema).
- Modelos de MediaPipe en `REVISOR_DIR`: `hand_landmarker.task` y `pose_landmarker_full.task`
  (https://storage.googleapis.com/mediapipe-models/). Florence-2: `florence-community/Florence-2-large` (1,55 GB).
- LLM: `llama-cpp-python[server]==0.3.19` en su propio venv, compilado desde PyPI (GitHub no es accesible desde el
  contenedor, así que no hay ruedas precompiladas), y el GGUF de EuroLLM (5,6 GB).
- StyleTTS2 de Nós, Cotovía y ASR: ver `herramientas/voz/README.md` y las variables de `CFG` en `pipeline.py`.

## Medidas de la muestra (29-09-2026, ronda 2)

Vídeo de 3 min 24 s, 24 planos (9 en el primer minuto), 30,4 MB, -17,1 LUFS, WER de la mezcla 0,026, sincronía de
subtítulos 100 %. Puerta de imágenes: 43 imágenes generadas para 24 planos; 18 aprobadas a la primera, 6 tras
regenerar (una con el prompt genérico de reserva) y 0 sin aprobar. Tiempo acumulado: 91,7 min de reloj y **4,69 h de
CPU de núcleo**, de las que 1,69 h son del LLM local (28 llamadas, 2-4 tokens/s de salida y 5-12 tokens/s de lectura
de prompt). No se cuentan unos 30 min de trabajo interrumpido por los relanzamientos. Extrapolación lineal a 60 min:
≈27 h de reloj y ≈83 h de CPU [S]. Con estos números, un episodio de 60 min no cabe en una noche de esta máquina: o
se paraleliza (dos máquinas, o GPU), o se bajan los intentos de imagen y las llamadas al LLM.

Ver `plan-de-negocio/gauntlet2/video/qa.md` (tiempos por etapa con el CPU del servidor LLM incluido, llamadas al LLM
con tokens y segundos, puerta de imágenes con los intentos rechazados) y `comparacion-llm.md` (guion del LLM local
frente al de Claude de la ronda 1 con los mismos controles).

## Licencias a vigilar

- **SDXL-Turbo**: Stability AI Community License (https://huggingface.co/stabilityai/sdxl-turbo/blob/main/LICENSE.md):
  gratis por debajo de 1 M USD de ingresos anuales, con registro para uso comercial. No es OSI.
- **EuroLLM-9B-Instruct-2512**: Apache-2.0 (https://huggingface.co/utter-project/EuroLLM-9B-Instruct-2512).
- **Florence-2-large**: MIT. **MediaPipe** y sus modelos: Apache-2.0.
- Voz Nós StyleTTS2 y Whisper galego: fichas de https://huggingface.co/proxectonos (crédito a Nós/USC, D4).
- LanguageTool: LGPL-2.1. Lluvia: código propio.

## Limitaciones conocidas

- El guion de un LLM local de 9B en CPU es claramente peor que el de un modelo grande (ver la comparación): más
  avisos de LanguageTool, frases planas y riesgo de datos inventados que H1 no ve. Es el punto débil del canal
  desatendido y la razón para reportar errores y pedir un modelo instruccional mejor a Nós [S].
- Las imágenes se generan a 1024x576 y se reescalan: en pantalla grande se ven algo blandas.
- La niebla se repite cada ~6,4 min.
- Whisper escribe a veces el galego con grafías portuguesas, lo que infla el WER.
- Puerta de imágenes (ronda 2): Florence-2 no nombra detalles pequeños, así que pasan tejados rojos lejanos en algún
  plano (p. ej., el primero). Cuando el LLM pide una escena que la lista veta por diseño (un escriba escribiendo, una
  torre en llamas), la imagen de reserva genérica encaja peor con lo que se narra. Los prompts de escenas llegaron con
  `**` de Markdown del LLM y el código no los limpia todavía.
