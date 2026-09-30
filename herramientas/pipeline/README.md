# Pipeline automático de "Serán" (historia de Galicia para durmir)

De una **ficha de tema** (YAML con título, extensión y dossier de fuentes verificadas) a un **MP4 1920x1080 en
galego** con voz sintética de Nós, imágenes generadas en CPU y revisadas por una puerta automática, lluvia de fondo,
subtítulos galegos y un informe de QA. **Un solo comando, sin revisión humana (D5)**: el pipeline arranca su propio
LLM local, escribe el guion, lo valida, lo narra, genera y revisa las imágenes, monta y mide. Todo el software y los
modelos son abiertos o de pesos abiertos y corren en CPU (4 núcleos, 15 GB).

    source entorno-llm.sh        # variables del LLM local (ver abajo); nada más
    PY=$SCRATCH/tts/venv/bin/python
    $PY pipeline.py temas/irmandinos-apertura.yaml --llm openai --traballo DIR_VACÍO --saida ../../plan-de-negocio/gauntlet2/video

Salida en `--saida`: `qa.json`, `qa.md` (veredicto PUBLICABLE / NON PUBLICABLE con sus puertas) y
`subtitulos.gl.srt`; **solo si el veredicto es PUBLICABLE**, también `ejemplo.mp4` y `contactsheet.jpg` (4x3
fotogramas de 960x540), copiados de forma atómica (temporal + renombrado). Si el texto no pasa las puertas, el
pipeline sale con código 4 sin generar vídeo; si falla una puerta tras el render, el MP4 queda en `--traballo` como
`rexeitado.mp4`. Los intermedios (respuestas del LLM con sus prompts y metadatos, guion, WAV, PNG de todos los
intentos, revisión de imágenes) quedan en `--traballo`; cada etapa se salta si ya está hecha.

## Historia honesta de la muestra

- **Ronda 1 (29-09-2026, archivada en `plan-de-negocio/gauntlet2/video/ronda1/`)**: las tres etapas LLM las respondió
  Claude Opus 5.5 en modo `manual` (el pipeline paraba con código 3 y se relanzaba). **No fue una ejecución
  desatendida** aunque el README y el qa.md de entonces lo decían. Su QA daba PUBLICABLE 9/9 sin mirar el contenido de
  las imágenes: el plano final tenía cuatro manos (un par sin cuerpo), una aldea con ventanas de vidrio y balcones y una
  multitud con picas y cruces.
- **Ronda 2 (archivada en `plan-de-negocio/gauntlet2/video/ronda2/`)**: `--llm openai` contra un LLM local (EuroLLM-9B) arrancado por el propio pipeline, en un
  directorio de trabajo vacío, y puerta automática de imágenes con regeneración. Ninguna respuesta del LLM ni ninguna
  imagen se tocó a mano. El mismo comando se relanzó 4 veces en el mismo directorio para corregir código (cortes de
  plano, reservas y lista del revisor, bloqueo de la montaje, esqueletos y hogueras que la lista no cubría). Las etapas
  ya hechas se leyeron de la caché de esa misma ejecución. Todo está detallado en la nota de `qa.md` y en
  `video/execucion/logs/`. **Veredicto automático: NON PUBLICABLE** (10/12 puertas): falla lengua (11 avisos de
  LanguageTool) y H1 (1 falso positivo del tokenizador). El modo `manual` queda solo para depurar prompts. Aun así
  se entregó ese MP4 como ejemplo, y su gancho decía "a irmandade venceu" (falso) e inventaba "fortaleiras".
- **Ronda 3 (esta versión, 30-09-2026)**: lengua, H1 y una nueva puerta de **veracidad** son **bloqueantes** por bloque
  y antes de la voz; el dossier incluye el **desenlace** (derrota de 1469, reconstrucción de las fortalezas); el
  pipeline **no publica** un MP4 que no pase todas las puertas. Ejecución desatendida con EuroLLM-9B local en un
  directorio vacío; se relanzó una vez el mismo comando en el mismo directorio porque la etapa de voz murió por
  memoria (LLM + NLI + LanguageTool seguían cargados; ahora se paran antes de la voz). Antes hubo **siete lanzamientos
  de desarrollo abortados** (unas 4 h de reloj no contabilizadas) en los que se vieron, y se corrigieron en el código,
  los fallos que dejaban pasar las puertas: un gancho con "os señores non foron castigados con morte", un párrafo con
  "os señores ... derrubaron as fortalezas dos irmandiños", frases de relleno ("a chuvia mollar a pedra"), repeticiones
  entre gancho y relato, el LLM copiando el dossier entero en el resumen y dos OOM. **Veredicto automático:
  PUBLICABLE 13/13.** Precio honesto: de 18 párrafos del relato el LLM no consiguió **ninguno** limpio en tres
  intentos; 13 son "reserva mixta" (frases del LLM que pasan una a una + el hecho literal) y 5 el hecho literal del
  dossier; el resumen se omitió y la invitación es texto fijo. El gancho sí es del LLM (pasó a la primera). El
  guion resultante es verdadero pero seco y con algún giro torpe que LanguageTool no marca (ver Limitaciones).

## Etapas

| # | Etapa | Qué hace | Software / modelo (licencia) |
|---|---|---|---|
| 1 | guion | **Por bloques** (por defecto): el LLM elige 2-3 hechos del dossier para el gancho y los reescribe; escribe el resumen; el código añade hechos al relato hasta la extensión objetivo (orden cronológico de la ficha, sin repetir los del gancho) y el LLM escribe **un párrafo por hecho**. Cada bloque pasa, antes de aceptarse, **lengua (LanguageTool + hunspell), H1 y veracidad** además de las reglas de estilo; hasta 3 intentos con los problemas concretos. Si no pasa: **reserva mixta** (solo las frases del LLM que pasan una a una, sin frases de ambiente, más el hecho literal que falte) o **texto literal del dossier**. Aviso, fórmula e **invitación a dormir** son texto fijo del canal. Tope de tokens por bloque (sin él copiaba el dossier) | LLM local, `prompts/bloque_*.md`, `veracidade.py` |
| 2 | corrixir | LanguageTool gl-ES por párrafo; si hay avisos, el LLM corrige ese párrafo; solo se acepta si baja el número de avisos y no empeora la validación | LanguageTool 6.8 (LGPL-2.1) con hunspell gl; `prompts/corrixir_parrafo.md` |
| 3 | voz | Narra frase a frase con **ritmo en embudo** (feedback del promotor): escala de duraciones 1,05 en las primeras 150 palabras que sube hasta 1,25 hacia la palabra 320; pausas de 0,55 s entre frases al principio que suben hasta 1,35 s, más 0,45-1,0 s entre párrafos y un ajuste por longitud de la frase siguiente (la cadencia ya no es fija) | Nos_StyleTTS2-Brais-GL (Proxecto Nós/USC), Cotovía para fonemas |
| 4 | escenas | El **código** corta los planos con las duraciones reales de la voz: ~5,5 s en el gancho, subiendo a ~12,5 s; una frase larga se reparte en varios planos. El LLM escribe un prompt de imagen por plano (`prompts/escenas.md`: personas haciendo cosas, planos medios, luz variada, lista de anacronismos prohibidos) | LLM local |
| 5 | imaxes | **Gauntlet 3:** SDXL base + UNet **SDXL-Lightning 4 pasos a 1344x768** (`IMG_MODEL=lightning`, por defecto; `turbo` = SDXL-Turbo 1024x576 del Gauntlet 2), estilo común de fotograma de cine de época con matiz y luz por fase (biblia visual `plan-de-negocio/gauntlet3/visual/biblia.md`). **Puerta de imágenes** (`revisor.py` v5): cada imagen se revisa y, si falla, se regenera con otra semilla y una corrección según el motivo (lousa y granito delante si salen tejados naranjas; menos gente si hay multitud); si el prompt repite arquetipo o imagen dos veces, o tras 5 intentos, va a la **reserva de la fase** (un plano sin personas). `graduar` **por fase** (sección siguiente) | SDXL base 1.0 + SDXL-Lightning (CreativeML OpenRAIL++-M); MediaPipe (Apache-2.0); Florence-2-large (MIT); CLIP ViT-L/14 (MIT) |
| 6 | son | `pipeline.py`: lluvia continua sintetizada por código. `longo.py` (D13/D14): **ambiente por escena** con un catálogo procedural de 9 tipos (choiva, lume, mar, vento, fonte, xente, noite, aldea, campas; sin grabaciones de terceros), variación por tramo, eventos limitados y cada vez más escasos al dormir y voz limpia donde la imagen no tiene sonido (`gauntlet3/son/guia-son.md`, `informe.md`). El murmullo de `xente` sale de un banco de frases narradas con la voz de Nós (`son_xente.py`, `son_datos/`). Voz a -17 LUFS | numpy/scipy, pyloudnorm |
| 7 | montaxe | Ken Burns, niebla ligera (6 %, antes 13 %: lavaba todo de verde), viñeta, **fundidos de 1,2 s** (antes 3 s: la doble exposición se veía mucho), x264 CRF 22 con tope de 1,1 Mb/s, AAC 128 kb/s, subtítulos `mov_text` `glg` | PIL, numpy, ffmpeg de `imageio-ffmpeg` |
| 8 | qa | Controles automáticos y hoja de contactos (sus 12 fotogramas se desplazan fuera de los fundidos) | faster-whisper + Whisper turbo galego de Nós, LanguageTool, ffmpeg `ebur128` |

## Imágenes en el Gauntlet 3 (modelo, estilo por fase, gradación y puerta v5)

El crítico visual de la ronda 3 vio luz plana y monótona, composiciones repetidas, "óleo genérico de IA",
iconografía no gallega (cipreses, ruedas de radios, fachadas mediterráneas, tejados naranjas) e imágenes blandas.
Cambios (detalle y medidas en `plan-de-negocio/gauntlet3/aprendizajes/visual.md`):

- **Modelo**: SDXL-Lightning 4 pasos (UNet destilada por ByteDance sobre SDXL base) a 1344x768: 47,6 s por imagen
  (mediana, 4 núcleos) frente a 25,5 s de Turbo a 1024x576, más nítido y más "de cine". Los codificadores de texto
  se cargan del repo de Turbo (mismo sha256 que los de SDXL base). `montaxe.py` recorta a 16:9 sin deformar.
- **Estilo**: `cinematic film still, period drama, photorealistic` más un matiz corto por fase (gancho `dramatic
  chiaroscuro`, calma `soft light`, durmir `dim and quiet`). Las palabras de luz y color de los prompts del agente
  **ya no se quitan**; si un prompt no trae luz, se añade una luz por defecto de su fase (rotando). Los prompts sin fase
  (LLM del pipeline corto) solo pierden `sepia, neon, vivid...`.
- **Gradación por fase** (`imaxes.graduar(paths, outdir, escenas)`): sustituye la igualación a la media del episodio,
  que aplanaba la luz. Por imagen: la luminancia media se lleva al rango de su fase solo si se sale (gancho 0,13-0,45;
  transición 0,25-0,58; calma 0,18-0,48; durmir 0,08-0,30), contraste y brillo de `curva.py`, nivel de negro por fase
  (negros profundos en el gancho, levantados al durmir), saturación por fase con tope de croma y un virado común muy
  ligero. Los parámetros se suavizan con los planos vecinos (±60 palabras de guion): no hay saltos entre fases.
  `graduacion.json` guarda lo aplicado a cada imagen.
- **Puerta v5**: CLIP para la iconografía y la repetición en todo el episodio (punto 4 de la sección siguiente).
- **Límites medidos** (experimento de iconografía, `plan-de-negocio/gauntlet3/visual/comparativa/`): SDXL-Lightning
  **no sabe dibujar el hórreo** (tres descripciones: sale una cabaña, una casa con tejado de hierba o una casa de dos
  plantas) **ni la rueda maciza** del carro del país (ocho carros, todos con radios); el cruceiro y la palloza sí salen.
  La biblia pide no ponerlos como sujeto. La puerta de CLIP caza los casos foráneos claros (aldea toscana, olivar,
  palmeras, eucaliptal, paisaje seco) con 0 falsos positivos en 72 imágenes, pero no los tejados naranjas pequeños y
  apagados (eso queda para Florence-2); el par de ruedas de radios está desactivado porque salía invertido.

## Voz en el Gauntlet 3 (embudo, referencias y Cotovía)

Pieza VOZ (`plan-de-negocio/gauntlet3/voz/informe.md`; medidas automáticas, **nadie ha escuchado la voz**):

- **Embudo por frase.** `longo.py` escribe en el JSON de cada frase los valores de `curva.py` en su posición del guion
  (`escala` y `curva.VOZ`: `estilo`, `f0_rango`, `f0_media`, `enerxia`, `beta`, `embedding_scale`) y `voz_st2.py` los
  aplica: `estilo` interpola el vector de estilo entre `REF_WAV` (viva) y `REF_WAV_CALMO` (calma); `f0_media`
  multiplica la F0 y `f0_rango` escala el log F0 alrededor de su media en la frase (solo tramos sonoros, sin bajar
  nada de 80 Hz: evita la voz cascada); `enerxia` multiplica la N del descodificador; `beta`/`embedding_scale` son los
  de StyleTTS2. Sin esos campos (vídeo corto, `pipeline.py`) la voz es la de antes. Cada frase lleva su semilla
  (SEED + texto): el mismo texto suena igual aunque se retome el render.
- **Medido en 5 puntos** (palabra 0, 280, 950, 1.800 y 3.600 de un guion de 3.600): arousal 0,643 → 0,432, F0 sd 4,76 →
  2,60 st, 7,56 → 5,19 síl/s (182 → 113 pal/min con pausas), bajando en cada paso; WER frase a frase ≤ 0,054.
- **Referencias** (`entorno.sh`): `REF_WAV` = vector medio de tres grabaciones de Brais (11535, 01372, 04078),
  `REF_WAV_CALMO` = 03720 (la más lenta y menos activada de 40). Admiten listas `a.wav:b.wav`.
- **Cotovía** por defecto: la compilada de Nós en modo `-p1` (ver "Instalación rápida"): da los fonemas del corpus con
  que se entrenó la voz (0,8 % de caracteres distintos frente al 7,8 % de la 0.5) sin "pra" ni "facelo lume".
- **Aviso para el QA**: el mismo pasaje da WER 0-0,054 frase a frase y 0,18-0,28 transcrito entero con las pausas
  del embudo y sin VAD, como hace `qa.asr`; en el A/B de Cotovía la causa fue que Whisper se salta frases enteras. El
  WER de la mezcla puede salir alto sin que sea de la voz (detalle en el informe de la pieza VOZ).

## La puerta de imágenes (`revisor.py`)

1. **Manos y cuerpos** (MediaPipe `hand_landmarker` + `pose_landmarker_full`): una mano cuya muñeca está a más de 0,14
   (distancia normalizada) de la muñeca de cualquier cuerpo detectado es "man sen corpo"; más de dos manos por cuerpo
   también falla.
2. **Lista de anacronismos y vetos** sobre la descripción detallada y los objetos que ve **Florence-2-large** (MIT):
   ventanas de vidrio, balcones, tejados rojos o de teja, vehículos, objetos modernos (farolas, relojes, cables...),
   interiores modernos (dormitorios, lámparas, cortinas), texto o letras (también "writing"), cruces portadas, armas de
   fuego, sangre, edificios ardiendo, esqueletos, calaveras o cadáveres y hogueras grandes en el exterior. Las
   vidrieras góticas ("stained glass") no cuentan como ventanas modernas. `VERSION` sube cuando cambia la lista, y
   `imaxes.py` vuelve a revisar las imágenes guardadas con una versión anterior. Versión 4 (ronda 3): **multitudes**
   (crowd, army, soldiers, knights, procession...), porque el crítico visual vio "multitudes clónicas y recargadas".
3. **Repetición** (`imaxes.repetida`, ronda 3): la imagen no puede parecerse de más a ninguna de las 4 anteriores del
   episodio (correlación de la imagen en grises desenfocada a 48x27 > 0,6, o Jaccard de las palabras de la descripción
   de Florence-2 > 0,5). En las 24 imágenes de la ronda 2 el p95 de la correlación era 0,50 y el máximo 0,67.
   Versión 5 (Gauntlet 3): en la lista, iconografía no gallega (cypress, olive trees, palm trees, eucalyptus,
   whitewashed, stucco, mediterranean, tuscan, spoked...); sin "procession" (una Santa Compaña de 3-4 figuras es
   legítima; los cuerpos los cuenta MediaPipe: más de 5 es multitud); "lamp" solo con adjetivos modernos (el candil
   es la luz de la fase calma) y el fuego grande no cuenta si es de la lareira (fireplace, hearth, pot...).
4. **CLIP ViT-L/14** (versión 5): (a) **iconografía**: pares "malo/bueno" (teja naranja/lousa, encalado/granito,
   ciprés/carballo, olivo/prado, palmera/carballo, rueda de radios/rueda maciza, paisaje seco/atlántico,
   eucalipto/carballeira) en tres recortes cuadrados (izquierda, centro, derecha: CLIP solo ve un cuadrado y los
   tejados suelen estar en los lados); falla si sim(malo) − sim(bueno) supera el margen calibrado y el concepto es
   pertinente; también los conceptos del campo `negativo` del plano; (b) **repetición contra todas las imágenes
   aceptadas del episodio** (coseno de los embeddings > `SIM_CLIP`); (c) **arquetipos** de composición con tope por
   episodio y separación mínima de 5 planos (los "caminantes de espaldas" que el crítico vio 3-4 veces: 3 %).
   Calibración: `probas/visual_calibrar_clip.py` (ver aprendizajes).

**Coherencia visual (ronda 3).** El crítico visual vio una "toma repetida" (era un plano de 18,9 s que caía en dos
fotogramas de la hoja) y una paleta que saltaba de pictórica a saturada y a sepia. Cambios: (a) ningún plano dura más
de 12,5 s (`PLANO_MAX`: los largos se parten en varios planos con imágenes distintas); (b) un único estilo al principio
del prompt ("muted oil painting, soft overcast light, grey-green and slate palette...") y el código quita las palabras
de color del LLM (golden, amber, blood-orange, sepia...); (c) `imaxes.graduar` iguala el color de todas las imágenes
del episodio (transferencia de media y desviación por canal en YCbCr hacia la media del episodio, saturación 0,85);
(d) el prompt de escenas pide como mucho tres o cuatro figuras, nada de multitudes ni ejércitos, y **solo lo que se
narra** (en la ronda 2 inventaba rendiciones, heridos, tronos y tesoros); (e) la hoja de contactos tiene fotogramas de
960x540 (3840x1620) para ver los artefactos finos.

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
| **Lengua (bloqueante)** | LanguageTool gl-ES con hunspell gallego; los nombres del dossier no cuentan como error ortográfico; lista cerrada y documentada de falsos positivos de estilo (`qa.FALSOS_POSITIVOS_LT`: "ceo" = firmamento, "Esta noite + verbo"), **nunca de hunspell** | 0 avisos |
| **H1-léxico (bloqueante)** (`ancoraxe.py`) | Nombres propios y cantidades que no están en el dossier ni en la ficha del tema | 0 sin anclar |
| **Veracidad (bloqueante)** (`veracidade.py`) | Por frase: NLI multilingüe (mDeBERTa-v3, MIT) + coincidencia léxica con los hechos del dossier + reglas deterministas de desenlace, nombres y tiempo largo. Gancho: todas las frases apoyadas | 0 frases sin apoyo |
| Estilo | Sin cifras, signos que la voz no lee, preguntas ni palabras vetadas; aviso y fórmula literales | todo cumplido |
| **Imágenes** | `revisor.py` sobre la imagen escogida de cada plano | todas aprobadas |
| Sonoridad | `ebur128` sobre el MP4 | -18 a -16 LUFS (A2 del plan) |
| Peso y formato | MB, resolución | ≤ 50 MB, 1920x1080 |

**Puertas bloqueantes (ronda 3).** Lengua, H1, veracidad y estilo se comprueban **en cada bloque del guion** y otra
vez sobre el guion completo **antes de la voz**. Un bloque que no pasa en tres intentos del LLM (cada reintento lleva
los problemas concretos: "la palabra «fortaleiras» no existe", "esta frase no se puede afirmar con el dossier") **no se
usa**: el gancho y los párrafos pasan a ser el **texto literal de los hechos del dossier**, la invitación un texto fijo
del canal y el resumen se omite. Si aun así el guion completo no pasa, el pipeline sale con código 4 **sin generar
vídeo**. Si falla cualquier puerta después del render (WER, sonoridad...), el MP4 se queda en el directorio de trabajo
como `rexeitado.mp4` y **no se copia a la salida** (y se borra de la salida un `ejemplo.mp4` viejo): el pipeline solo
publica un vídeo con todas las puertas en verde.

**La puerta de veracidad (`veracidade.py`)**, por frase del guion (premisa = un hecho o un par de hechos del dossier):
- apoyada = NLI de implicación ≥ 0,6 **y** coincidencia léxica ≥ 0,5 (0,6 en el gancho) con esa misma premisa, o coincidencia ≥ 0,8, o la
  frase está literalmente en un hecho;
- **desenlace** (vencer, gañar, triunfo, vitoria, derrota, perder, render...): la **misma forma** de la palabra tiene que
  estar en un hecho ("derrotou" no se ancla en "foi derrotada") y el NLI de ese hecho ≥ 0,7 con contradicción < 0,5.
  "A irmandade venceu" (ronda 2) no pasa nunca: el dossier dice "a irmandade foi derrotada";
- gancho: todas las frases apoyadas; relato: las frases con nombre propio, tiempo largo (séculos, nunca...) o desenlace
  apoyadas, y el párrafo tiene que contar su hecho. Las frases de ambiente sin nombres ni desenlace pasan.
- **Quién hizo qué**: para los verbos de acción (derrubar, reconstruír, vencer, regresar, castigar...), el actor que
  los precede en la frase tiene que ser de la misma clase (pueblo / señores) que en algún hecho con ese verbo. "Os
  señores ... derrubaron as fortalezas dos irmandiños" pasaba el NLI (0,92) y la coincidencia léxica (0,67): la
  escribió el LLM en una prueba de esta ronda y esta regla la para.
- Relato **sin frases de ambiente**: las frases sin personas, nombres, tiempo ni desenlace ("a chuvia caía mansa") ya
  no se aceptan en el relato; eran el relleno sin sentido de la ronda 2 ("o lume ardeu en silencio").
- Calibración en `probas/veracidade_calibracion.md` (script `probas/veracidade_calibracion.py`): rechaza las frases
  falsas o inventadas del gancho de la ronda 2 ("a irmandade venceu", "fortaleiras perderon", "paus e pedras", "un
  exército"), "As chaves da Rocha Forte caeron", "o lume ardeu durante séculos", "a irmandade derrotou os señores",
  "os señores reconstruíron as fortalezas" y "os señores non foron castigados con morte"; acepta los 21 hechos del
  dossier y sus paráfrasis cercanas. El NLI solo **no sirve** en gallego (da "implicación 0,92" a "a irmandade venceu"
  y "contradicción 0,87" a una frase de lluvia): por eso decide junto con la coincidencia léxica y las reglas.

Lo que **no** controla: una frase falsa construida solo con palabras del dossier puede pasar (la coincidencia léxica
no entiende quién hace qué fuera de los desenlaces); una causa inventada en una frase de ambiente ("aproveitando a
chuvia") tampoco se ve; la naturalidad del gallego más allá de LanguageTool; caras deformes o ropas anacrónicas que
Florence-2 no nombre.

## Instalación rápida (una orden)

El scratchpad, el venv y los modelos no sobreviven entre sesiones. Para reconstruirlo todo (Ubuntu 24.04 como root,
Python 3.11 del sistema, Java ≥ 17):

    bash herramientas/pipeline/instalar.sh             # todo: ≈ 6 min en limpio, ≈ 15,7 GB (medido el 30-09-2026)
    source herramientas/pipeline/entorno.sh            # SCRATCH, HF_HOME, PY, ST2_DIR, REF_WAV, WHISPER_DIR, REVISOR_DIR...
    bash herramientas/pipeline/instalar.sh verificar   # prueba mínima de cada etapa (probas/proba_entorno.py, ≈ 5 min)

- `SCRATCH` es configurable (`SCRATCH=/ruta bash .../instalar.sh`); si no se da, `entorno.sh` toma el scratchpad de
  Claude Code más reciente. Todas las demás rutas cuelgan de él.
- **Idempotente**: cada paso deja una marca en `$SCRATCH/.instalado/` y se salta si ya está (una segunda ejecución
  tarda 1 s); `FORZAR=1 bash .../instalar.sh PASO` rehace un paso. Las descargas van en paralelo, con un registro por
  paso en `$SCRATCH/logs/`. La conversión del Whisper y la compilación de Cotovía usan el candado `$CPU_LOCK`.
- Versiones exactas en `requisitos-entorno.txt` (torch 2.10.0+cpu, diffusers 0.35.2, transformers 4.57.6, mediapipe
  1.0.1, faster-whisper 1.2.1, ctranslate2 4.8.2, language_tool_python 3.4.0 con LanguageTool 6.8).
- Solo se bajan los ficheros que se cargan (SDXL-Turbo fp16 y no el repo de 55 GB; Whisper sin `optimizer.pt`; CLIP
  solo en safetensors) y los checkpoints de StyleTTS2 se guardan sin el estado del optimizador (de 3,2 a 1,1 GB).
- **No** instala el LLM local (ver "El LLM local"): en el Gauntlet 3 el guion lo escribe Claude.
- Problemas encontrados, stubs y detalles: `plan-de-negocio/gauntlet3/aprendizajes/entorno.md`.

| Pieza | Dónde (`$SCRATCH/...`) | Tamaño | Tiempo en limpio |
|---|---|---|---|
| venv único: torch CPU + ~80 paquetes | `tts/venv` | 2,4 GB | 2 min 19 s (*) |
| SDXL-Lightning 4 pasos (UNet 5,14 GB) + VAE de SDXL base (0,17) + codificadores de texto de Turbo (1,64); `sdxl_turbo` (opcional) añade la UNet y el VAE de Turbo (5,3) | `hf/` | 6,95 GB | 2 min (UNet de Lightning: 121 s) |
| Florence-2-large / CLIP ViT-L/14 / NLI mDeBERTa | `hf/` | 1,56 / 1,71 / 0,56 GB | 2 min 40 s / 56 s / 17 s (*) |
| Nos_StyleTTS2-Brais-GL (sin 1.ª etapa ni optimizador) | `bench/st2` | 1,1 GB | 1 min 43 s (*) + 31 s |
| Whisper galego de Nós en CTranslate2 int8 | `bench/wgl_ct2` | 788 MB | 1 min 42 s (*) + 22 s |
| LanguageTool 6.8 (con hunspell gl) | `languagetool/` | 400 MB | 11 s |
| Cotovía 0.5 (`.deb` extraído) y su envoltorio | `cotovia/`, `bench/pathbin` | 16 MB | 3 s |
| Cotovía compilada de Nós (**la de por defecto de la voz**, modo `-p1`) | `cotovia_nova/`, `bench/pathbin_nova` | 121 MB | 2 min 0 s |
| Stubs para importar StyleTTS2 (`monotonic_align`, `speechmos`) | `bench/stubs` | — | 8 s |
| MediaPipe (manos y pose) | `revisor/` | 17 MB | 2 s |
| Nos_Brais-GL: referencia de estilo (`REF_WAV`) y 40 grabaciones variadas con su texto (`refs.tsv`) | `tts/kit/t1`, `tts/refs` | 11 MB | 1 min 26 s (*) |

(*) en paralelo: el grupo de descargas duró lo que la más lenta, ~2 min 41 s. Las grabaciones de Nos_Brais-GL tienen
términos de uso que prohíben difundirlas: se quedan en el scratchpad y no se suben ni se publican.

**Prueba mínima** (`instalar.sh verificar`, 30-09-2026, 4 núcleos, cada prueba con el candado de CPU):

| Etapa | Resultado |
|---|---|
| Voz (`voz_st2.py`, 2 frases, el mismo env que pone `pipeline.py`) | carga del modelo + 1.ª frase 31,7 s; **RTF 0,39** después |
| Imagen SDXL-Turbo 1024x576, 4 pasos, bf16 | carga 14-15 s; **25-26 s por imagen** (Gauntlet 2: mediana 18,1 s) |
| Imagen SDXL-Lightning 1344x768, 4 pasos (por defecto desde el Gauntlet 3; `proba_entorno.py` usa `imaxes.cargar_pipe`) | carga 18 s (≈10 min con el disco frío tras reiniciar el contenedor); **47,6 s por imagen** de mediana con otros agentes en la máquina, 31-38 s sin competencia |
| `python revisor.py` | carga + 1.ª imagen 29,7 s; **18,9 s por imagen** después |
| ASR (faster-whisper + Whisper gl) sobre la voz | carga 4 s; **WER 0,0** |
| LanguageTool gl-ES / NLI | detecta "Os rapaces foi"; contradicción 0,998 en un par negado |
| Montaje (`son.mesturar` + `montaxe.render`, 2 planos de 4 s) | 22,7 s; MP4 1920x1080 con AAC y `mov_text` que decodifica entero sin errores |

**Dos hallazgos del entorno para las piezas de voz e imagen** (medidos, no aplicados; detalle en el fichero de
aprendizajes):
- **Cotovía** (aplicado por la pieza VOZ): la 0.5 del `.deb` no marca las vocales abiertas (*po^rta* por *pÓrta*) y
  acentúa los monosílabos átonos; en 122 frases del corpus difiere un 7,8 % en caracteres de los fonemas con los que se
  entrenó el modelo. La Cotovía que trae el repo del modelo (`instalar.sh cotovia_nova`) difiere un 0,9 % y, en modo
  `-p1` (sin "pra" ni segunda forma del artículo, que el corpus no tiene), un 0,8 %. **Ahora es la de por defecto**
  (`entorno.sh`; si no está compilada, la 0.5); WER igual (0,028 frente a 0,032 de la 0.5). Medida:
  `probas/comparar_cotovia.py` y `plan-de-negocio/gauntlet3/voz/informe.md`.
- **SDXL-Turbo**: el VAE se lleva ~11 s de cada imagen; con `pipe.vae.to(memory_format=torch.channels_last)` baja a
  ~6 s con la misma salida (imagen de ~28 s a ~20-22 s).

## Instalación (CPU)

`instalar.sh` hace todo lo de esta sección salvo el LLM local.

- Python 3.11 con `torch` (CPU), `diffusers==0.35.2`, `huggingface-hub<1.0`, `transformers<5` (4.57, que ya trae
  `Florence2ForConditionalGeneration`), `accelerate`, `faster-whisper`, `jiwer`, `language_tool_python` (Java ≥ 17),
  `pyloudnorm`, `imageio-ffmpeg`, `soundfile`, `scipy`, `pyyaml`, `mediapipe` (1.0.1; necesita `libegl1` y `libgles2`
  del sistema).
- Modelos de MediaPipe en `REVISOR_DIR`: `hand_landmarker.task` y `pose_landmarker_full.task`
  (https://storage.googleapis.com/mediapipe-models/). Florence-2: `florence-community/Florence-2-large` (1,55 GB).
- LLM: `llama-cpp-python[server]==0.3.19` en su propio venv, compilado desde PyPI (GitHub no es accesible desde el
  contenedor, así que no hay ruedas precompiladas), y el GGUF de EuroLLM (5,6 GB).
- StyleTTS2 de Nós, Cotovía y ASR: ver `herramientas/voz/README.md` y las variables de `CFG` en `pipeline.py`.

## Medidas de la muestra (30-09-2026, ronda 3)

Vídeo de 3 min 11 s, 29 planos (11 en el primer minuto, ninguno de más de 12,5 s), 28,3 MB, -17,2 LUFS, WER de la
mezcla 0,037, sincronía de subtítulos 99,7 %. Veracidad: 24 frases evaluadas, 0 con problemas. Puerta de imágenes: 63
imágenes generadas para 29 planos; 18 aprobadas a la primera, 11 tras regenerar (motivos más frecuentes: tejados
naranjas, multitudes, fuego), 0 sin aprobar. Tiempo acumulado de la ejecución buena (los dos lanzamientos): 91,3 min
de reloj y **5,17 h de CPU de núcleo**, de las que 2,29 h son del LLM local (64 llamadas, casi todas reintentos por
bloque). No se cuentan los siete lanzamientos de desarrollo abortados. Extrapolación lineal a 60 min: ≈28,6 h de reloj
y ≈97 h de CPU [S]: un episodio largo sigue sin caber en una noche de esta máquina.

Ronda 2 (archivada): 3 min 24 s, 30,4 MB, WER 0,026, 4,69 h de CPU, NON PUBLICABLE 10/12.

## Licencias a vigilar

- **SDXL-Lightning** (https://huggingface.co/ByteDance/SDXL-Lightning) sobre **SDXL base 1.0**: CreativeML OpenRAIL++-M
  (uso comercial permitido con las restricciones de uso de la licencia). Es el modelo por defecto desde el Gauntlet 3.
- **SDXL-Turbo**: Stability AI Community License (https://huggingface.co/stabilityai/sdxl-turbo/blob/main/LICENSE.md):
  gratis por debajo de 1 M USD de ingresos anuales, con registro para uso comercial. No es OSI.
- **EuroLLM-9B-Instruct-2512**: Apache-2.0 (https://huggingface.co/utter-project/EuroLLM-9B-Instruct-2512).
- **Florence-2-large**: MIT. **MediaPipe** y sus modelos: Apache-2.0.
- **mDeBERTa-v3-base-xnli-multilingual-nli-2mil7** (puerta de veracidad): MIT (https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7).
- Voz Nós StyleTTS2 y Whisper galego: fichas de https://huggingface.co/proxectonos (crédito a Nós/USC, D4).
- LanguageTool: LGPL-2.1. Lluvia: código propio.

## Limitaciones conocidas

- **Ronda 3: la verdad se consigue a costa del LLM.** Con las puertas bloqueantes, EuroLLM-9B no escribió ningún
  párrafo del relato que pasara entero; el texto es sobre todo el dossier literal más frases sueltas del LLM. Queda
  verdadero pero plano, sin la "chispa" que pide el promotor fuera del gancho. Un LLM mejor (o uno grande vía API,
  que rompería el "todo local") es la palanca principal [S].
- Errores de gallego que LanguageTool no ve y que siguen en la muestra: "lembrando co que viran" (por "lembrando o
  que"), "vivían ao limiar" (por "no limiar"), "Decididos os veciños ..., botaron abaixo" (construcción torpe),
  "Botáronse abaixo moitas fortalezas ... que ... botou abaixo moitas fortalezas" (redundante).
- Imágenes que pasaron la puerta con defectos visibles en la hoja de contactos: tejados naranjas en 1:43 y 2:46 y una
  pequeña multitud alrededor de un obispo en 1:43 (Florence-2 no los nombró). El LLM de escenas sigue añadiendo cosas
  no narradas (flechas, huidas, torres ardiendo); la puerta veta las más graves, no todas.

- El guion de un LLM local de 9B en CPU es claramente peor que el de un modelo grande (ver `video/ronda2/comparacion-llm.md`): más
  avisos de LanguageTool, frases planas y riesgo de datos inventados (ahora los para la puerta de veracidad, en parte). Es el punto débil del canal
  desatendido y la razón para reportar errores y pedir un modelo instruccional mejor a Nós [S].
- Las imágenes se generan a 1344x768 (Gauntlet 3; antes 1024x576) y se reescalan x1,43 a 1080p.
- La niebla se repite cada ~6,4 min.
- Whisper escribe a veces el galego con grafías portuguesas, lo que infla el WER.
- Puerta de imágenes (ronda 2): Florence-2 no nombra detalles pequeños, así que pasan tejados rojos lejanos en algún
  plano (p. ej., el primero). Cuando el LLM pide una escena que la lista veta por diseño (un escriba escribiendo, una
  torre en llamas), la imagen de reserva genérica encaja peor con lo que se narra. Los prompts de escenas llegaron con
  `**` de Markdown del LLM y el código no los limpia todavía.
