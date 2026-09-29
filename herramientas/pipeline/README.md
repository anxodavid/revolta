# Pipeline automático de "Serán" (historia de Galicia para durmir)

De una **ficha de tema** (YAML con título, extensión y dossier de fuentes verificadas) a un **MP4 1920x1080 en
galego** con voz sintética de Nós, imágenes generadas en CPU, lluvia de fondo, subtítulos galegos y un informe de
QA automático. Sin revisión humana entre la entrada y el MP4 (decisión D5): la única acción humana es lanzar el
comando. Todo el software y los modelos son abiertos o de pesos abiertos; todo corre en CPU (4 núcleos, 15 GB).

    PY=$SCRATCH/tts/venv/bin/python
    $PY pipeline.py temas/irmandinos-apertura.yaml --saida ../../plan-de-negocio/gauntlet2/video
    # opcional: --queimar-subtitulos (subtítulos grabados en la imagen; por defecto van en pista aparte)
    # opcional: --llm openai  (LLM local con API compatible: LLM_URL, LLM_MODEL)

Salida en `--saida`: `ejemplo.mp4`, `subtitulos.gl.srt`, `contactsheet.jpg` (4x3 fotogramas), `qa.json` y `qa.md`
(veredicto automático PUBLICABLE / NON PUBLICABLE con sus puertas). Los intermedios (guion, frases, WAV, PNG)
quedan en `--traballo` (por defecto `$SCRATCH/pipeline_work/<id>`) y cada etapa se salta si ya está hecha.

## Etapas

| # | Etapa | Qué hace | Software / modelo (licencia) |
|---|---|---|---|
| 1 | guion | Escribe el texto narrado solo con datos del dossier | LLM, `prompts/guion.md` (ver abajo) |
| 2 | corrixir | LanguageTool gl-ES revisa el guion; si hay avisos, el LLM corrige (una vuelta) | LanguageTool 6.8 (LGPL-2.1) con hunspell gl; `prompts/corrixir.md` |
| 3 | escenas | El LLM agrupa las frases en escenas de 12-20 s y escribe un prompt de imagen por escena | LLM, `prompts/escenas.md` |
| 4 | voz | Narra frase a frase; pausas de 0,7 s entre frases y 1,6 s entre párrafos; 4 s de lluvia antes de la voz y 6 s al final | Nos_StyleTTS2-Brais-GL (Proxecto Nós/USC), escala de duraciones 1,2; Cotovía para fonemas |
| 5 | imaxes | Una imagen 1024x576 por escena, 4 pasos, bfloat16, semilla fija por escena | SDXL-Turbo (Stability AI Community License) con `diffusers` 0.35 |
| 6 | son | Lluvia sintetizada por código (ruido filtrado + gotas de Poisson + rumor grave): no usa grabaciones de terceros, no hay licencia que anotar. Voz a -21 LUFS, lluvia 17 dB por debajo | numpy/scipy, pyloudnorm |
| 7 | montaxe | Ken Burns lento (zoom 1,00-1,12 o paneo), niebla animada semitransparente, viñeta, fundidos encadenados de 3 s, fundido de entrada y salida; x264 CRF 22 con tope de 1,1 Mb/s; AAC 128 kb/s; subtítulos `mov_text` en pista `glg` | PIL, numpy, ffmpeg de `imageio-ffmpeg` (el ffmpeg del sistema no tiene codificadores) |
| 8 | qa | Controles automáticos y hoja de contactos (abajo) | faster-whisper + Whisper turbo galego de Nós, LanguageTool, ffmpeg `ebur128` |

## Controles automáticos (etapa 8) y puertas de publicación

| Control | Cómo | Puerta |
|---|---|---|
| Inteligibilidad | WER de ASR sobre la **mezcla final** (voz + lluvia) y sobre la voz sola, con `proxectonos/whisper-large-v3-turbo-gl-v1.0` convertido a CTranslate2 int8; WER por frase (frases > 0,5 = posible error de pronunciación) | WER mezcla ≤ 0,25 [S] |
| Sincronía subtítulos-voz | Marcas de tiempo por palabra del ASR alineadas con el texto (jiwer); % de palabras que caen dentro del intervalo de su frase en el SRT (±0,5 s) y desfase al inicio de frase | ≥ 95 % |
| Sincronía A/V | Duración decodificada de la pista de vídeo y de audio | desfase ≤ 0,1 s |
| Duración | Duración del vídeo | 180-300 s en esta muestra (3-5 min) |
| Lengua | LanguageTool gl-ES (incluye hunspell); los nombres del dossier no cuentan como error ortográfico | ≤ 2 avisos tras la corrección [S] |
| Estilo del canal | Sin cifras ni signos que la voz no lea, sin preguntas, sin "imaxina"/CTA, aviso y fórmula literales, frases de 8-25 palabras, nombres propios nuevos por cada 110 palabras | sin cifras/signos/vetadas; aviso y fórmula presentes |
| Sonoridad | `ebur128` sobre el MP4 (integrado, LRA, pico real) | -24 a -18 LUFS |
| Imágenes | Luminancia, contraste y similitud con la anterior (para detectar negras, lavadas o repetidas) | informativo |
| Peso y formato | MB, resolución, fps, pista de subtítulos | ≤ 50 MB, 1920x1080 |

## El LLM

El guion y el guion visual los escribe un LLM a partir de los prompts versionados en `prompts/`. `llm.py` renderiza el
prompt, calcula su hash y busca la respuesta en `llm_cache/` (así el proceso es reproducible y auditable). Backends:

- `openai`: cualquier servidor compatible con la API de OpenAI (llama.cpp `llama-server`, vLLM, Ollama). Candidatos
  abiertos en galego: `proxectonos/Llama-3.1-Carballo-Instr3` (8B, Nós) o `proxectonos/Carvalho-Salamandra-Instruct`
  (https://huggingface.co/proxectonos). **No se han probado todavía en este pipeline** [S]: su calidad de guion y su
  velocidad en CPU están por medir (un 8B en Q4 con llama.cpp en 4 núcleos rinde del orden de unos pocos tokens/s [S],
  unos 10-20 min para las tres llamadas de esta muestra).
- `manual`: si falta la respuesta, el pipeline escribe el prompt renderizado en `llm_pending/` y sale con código 3;
  un LLM externo escribe la respuesta en `llm_cache/` y se relanza el mismo comando.

**En la muestra del 29-09-2026 el LLM fue Claude Opus 5.5 (`claude-opus-5-5`) en modo `manual`**, siguiendo
literalmente los tres prompts renderizados (están en `llm_pending/`, y las respuestas y su nota en `llm_cache/*.meta.json`).
No es un modelo abierto: para el canal real hay que sustituirlo por uno de los anteriores y repetir el QA.

## Instalación (CPU)

- Python 3.11 con `torch` (CPU), `diffusers==0.35.2`, `huggingface-hub<1.0` (diffusers 0.40 exige hub ≥ 1.23, que
  rompe `transformers` 4.57), `transformers<5`, `accelerate`, `faster-whisper`, `jiwer`, `language_tool_python`
  (descarga LanguageTool 6.8, 259 MB; necesita Java ≥ 17), `pyloudnorm`, `imageio-ffmpeg`, `soundfile`, `scipy`, `pyyaml`.
- StyleTTS2 de Nós: copia de https://huggingface.co/proxectonos/Nos_StyleTTS2-Brais-GL en `ST2_DIR`, Cotovía 0.5 en
  `ST2_PATHBIN` y los *stubs* de `monotonic_align`/`speechmos` en `ST2_STUBS` (ver `herramientas/voz/README.md`);
  `REF_WAV`: grabación de referencia de estilo del corpus Nos_Brais-GL (CC-BY-4.0).
- ASR: `ct2-transformers-converter --model proxectonos/whisper-large-v3-turbo-gl-v1.0 --output_dir wgl_ct2
  --copy_files tokenizer.json preprocessor_config.json` y `WHISPER_DIR=wgl_ct2`.
- SDXL-Turbo: se descarga solo (variante fp16, 6,5 GB) la primera vez.

Rutas por defecto: las de la sesión del 29-09-2026 bajo `$SCRATCH`; se cambian con las variables de entorno de
`CFG` en `pipeline.py`.

## Licencias a vigilar

- **SDXL-Turbo**: Stability AI Community License (https://huggingface.co/stabilityai/sdxl-turbo/blob/main/LICENSE.md):
  uso gratuito, también comercial, por debajo de 1 M USD de ingresos anuales, con registro en Stability AI para uso
  comercial. No es una licencia OSI. Alternativa más abierta: SD 1.5 + LCM (CreativeML OpenRAIL-M) con peor imagen [S].
- Voz Nós StyleTTS2 y Whisper galego: ver las fichas de https://huggingface.co/proxectonos (crédito a Nós/USC, D4).
- LanguageTool: LGPL-2.1. Lluvia: generada por código propio.

## Limitaciones conocidas (primera versión)

- Las imágenes se generan a 1024x576 y se reescalan a 2400x1350 (Lanczos + máscara de enfoque) para el movimiento:
  en pantalla grande se ve algo blanda. Un reescalador (Real-ESRGAN) mejoraría la nitidez a costa de CPU.
- La niebla se desplaza en bucle cada ~384 s; en vídeos largos habrá un salto de textura cada 6,4 min.
- LanguageTool en galego detecta poco (ortografía y algunas concordancias) y da falsos positivos; no sustituye a un
  corrector humano. Whisper escribe a veces el galego con grafías portuguesas, lo que infla el WER.
- No hay control automático de rigor histórico más allá de la regla "solo datos del dossier" del prompt.
