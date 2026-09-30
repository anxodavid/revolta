# Aprendizajes: entorno local del pipeline (Gauntlet 3, pieza 0)

Agente de entorno (Claude), 30-09-2026. Contenedor nuevo, sin nada instalado. Todo lo que sigue lo hizo Claude (agente)
con órdenes de shell y scripts; las pruebas son automáticas. Nadie escuchó los audios; la única salida que se miró
fue la imagen de prueba (la miró Claude, ver abajo).

## Resultado

- `herramientas/pipeline/instalar.sh` reconstruye todo el entorno en `$SCRATCH` con **una orden**. Es idempotente
  (una marca por paso en `$SCRATCH/.instalado/`; `FORZAR=1` rehace un paso) y baja los modelos **en paralelo**.
  En limpio: **3 min 41 s** de reloj, más 31 s del paso que aligera los checkpoints de StyleTTS2 (añadido después) y
  2 min 0 s de la compilación opcional de Cotovía (`cotovia_nova`). Una segunda ejecución con todo hecho: 1,1 s.
- `herramientas/pipeline/entorno.sh` exporta `SCRATCH` (configurable; si no está definida, toma el scratchpad de
  Claude Code más reciente), `HF_HOME` y todas las rutas que leen `pipeline.py`, `longo.py`, `revisor.py` y `qa.py`
  (`PY_TTS`, `ST2_DIR`, `ST2_PATHBIN`, `ST2_STUBS`, `REF_WAV`, `WHISPER_DIR`, `REVISOR_DIR`, `LTP_PATH`...), además de
  `REFS_DIR`, `COTOVIA_NOVA_PATHBIN`, `CLIP_MODEL` y `CPU_LOCK`.
- `herramientas/pipeline/requisitos-entorno.txt`: `pip freeze` de la instalación probada; `instalar.sh` lo usa como
  restricciones para que la próxima sesión instale exactamente las mismas versiones.
- `herramientas/pipeline/probas/proba_entorno.py` (`instalar.sh verificar`): una prueba mínima por etapa, con tiempos.
- `herramientas/pipeline/probas/comparar_cotovia.py`: mide si la Cotovía instalada da los fonemas del entrenamiento.

## Tiempos de la instalación (30-09-2026, en limpio)

| Paso | Reloj | Qué |
|---|---|---|
| sistema | 9 s | apt: `libegl1`, `libgles2`, `libportaudio2` (`libgl1` y Java 21 ya estaban en la imagen) |
| cotovia | ~3 s | 2 `.deb` de SourceForge (4,7 MB) extraídos con `dpkg-deb -x` |
| venv_base | 10 s | venv con `/usr/bin/python3.11` + `huggingface-hub` |
| paquetes (paralelo) | 139 s | torch 2.10.0+cpu, torchaudio y ~80 paquetes (sin caché de pip) |
| st2 (paralelo) | 103 s | 419 ficheros, 3,2 GB; después se aligeran (31 s) a 1,1 GB |
| brais (paralelo) | 86 s | 40 WAV + 2 CSV |
| sdxl / florence / clip / nli (paralelo) | 159 / 160 / 56 / 17 s | 6,95 / 1,56 / 1,71 / 0,56 GB |
| whisper_hf (paralelo) | 102 s | 3,2 GB (temporal: se borra tras convertir) |
| stubs | 8 s | incluye importar el código de StyleTTS2 y fonemizar una frase |
| whisper | 22 s | conversión a CTranslate2 int8 (con el candado de CPU) |
| languagetool | 11 s | descarga automática de LanguageTool 6.8 (259 MB a ~120 MB/s) y prueba gl-ES |
| cotovia_nova (opcional) | 2 min 0 s | compila la Cotovía de Nós: cmake (baja string_theory de GitHub y PCRE de SourceForge) + make del ejecutable; 2 min 52 s de CPU. Las dependencias de compilación ya estaban instaladas: en un contenedor nuevo, apt añade unos segundos |
| **Total** | **≈ 6 min 15 s** | 3 min 41 s + 31 s + 2 min 0 s; el grupo paralelo dura lo que el más lento (~2 min 41 s) |

Velocidad a través del proxy: ~27 MB/s por fichero desde el puente de Hugging Face (`us.aws.cdn.hf.co/xet-bridge-us`),
con varios ficheros a la vez sin problema; ~120-150 MB/s desde el servidor de LanguageTool. Ningún corte ni reintento.
Una segunda ejecución con todo hecho tarda 1,1 s (solo comprueba marcas).

## Tamaños y disco

| Pieza | Tamaño |
|---|---|
| venv (`tts/venv`) | 2,4 GB |
| caché HF (`hf/`): SDXL-Turbo fp16 6,95 + CLIP 1,71 + Florence-2 1,56 + NLI 0,56 | 11 GB |
| StyleTTS2 Brais (`bench/st2`), aligerado | 1,1 GB (3,1 GB tal como se baja) |
| Whisper gl CT2 int8 (`bench/wgl_ct2`) | 788 MB |
| LanguageTool 6.8 (`languagetool/`) | 400 MB |
| Cotovía compilada (`cotovia_nova/`, opcional) | 121 MB |
| Cotovía 0.5, MediaPipe, grabaciones de Brais | 16 + 17 + 11 MB |
| **Total del entorno** | **≈ 15,7 GB** |

Disco del contenedor: 30 GB libres al empezar; **15 GB libres** al terminar (con el entorno completo y lo que ya
tenían en el scratchpad los demás agentes). Lo que se evitó bajar o se borró, porque no se carga nunca:

- SDXL-Turbo: el repo pesa 55,5 GB (fp32, ONNX, checkpoints de un fichero); solo se bajan los ficheros fp16 (6,95 GB).
- Whisper galego: `optimizer.pt` (6,5 GB) y el estado de entrenamiento; el original fp32 (3,2 GB) se borra al convertir.
- CLIP: el repo trae el mismo modelo en 4 formatos (6,8 GB); solo `model.safetensors` (1,71 GB).
- NLI: sin `pytorch_model.bin` ni ONNX (duplicados del safetensors).
- StyleTTS2: sin `epoch_1st_00095.pth` (1,7 GB, primera etapa de entrenamiento) y sin el estado del optimizador de
  los tres checkpoints (2,1 GB de 3,2 GB): el código de inferencia solo lee `net` o `model`.
- pip sin caché (`PIP_NO_CACHE_DIR=1`).

## Problemas encontrados y cómo se resolvieron

1. **mediapipe 1.0.1 depende de `opencv-contrib-python`** (no de la versión *headless*). Instalar además
   `opencv-python-headless` deja dos paquetes escribiendo el mismo `cv2`. Solución: no se instala el *headless*;
   `cv2` viene de mediapipe y necesita `libgl1` (ya estaba en la imagen; el script lo comprueba). mediapipe 1.x
   trae también `sounddevice`, que busca PortAudio: se instala `libportaudio2` por prevención.
2. **Cotovía 0.5 sin instalar en el sistema.** Los `.deb` de 2012 dependen de `libgcc1` y `libasound2`, que en Ubuntu
   24.04 existen solo como paquetes virtuales (`libgcc-s1`, `libasound2t64`). Para no tocar el sistema ni depender
   de eso, se extraen con `dpkg-deb -x` en `$SCRATCH/cotovia` y `bench/pathbin/cotovia` es un envoltorio que añade
   `-D <datos>`. Cotovía 0.5 acepta UTF-8 en la entrada (se comprobó: misma transcripción que con ISO-8859-1) y
   escribe ISO-8859-1, que `phonemize.py` de Nós ya descodifica.
3. **Stubs de StyleTTS2** (`bench/stubs`, PYTHONPATH del subproceso de voz). El código de Nós importa al cargarse dos
   paquetes que solo usa para entrenar o evaluar:
   - `monotonic_align` (`utils.py`: `maximum_path`, `mask_from_lens`, `core.maximum_path_c`): alineamiento monótono
     del entrenamiento. El de StyleTTS2 se instala desde GitHub y compila Cython; el `monotonic-align` de PyPI es
     otro paquete con otra API.
   - `speechmos` (`inference.py`: `from speechmos import dnsmos`): puntuación DNSMOS del `main` de Nós; arrastra
     onnxruntime y modelos.
   Los stubs son módulos vacíos que lanzan `NotImplementedError` si algo los llamara. El resto de dependencias del
   código (`librosa`, `torchaudio`, `nltk`, `munch`, `einops`, `einops-exts`, `matplotlib`) se instalan de verdad.
4. **`torch.load` con `weights_only=True`** (por defecto desde torch 2.6): los tres checkpoints de Nós cargan sin
   cambios (solo tensores y números). Se fijó torch 2.10.0, la versión del `requirements.txt` de Nos_StyleTTS2.
5. **Nos_Brais-GL es un dataset "gated"** con términos de uso (prohibido difundir las grabaciones), pero sus ficheros
   se descargan sin token. Las 40 grabaciones se quedan en `$SCRATCH/tts/refs` como referencia de estilo; **no se
   suben al repo ni se publican**. `refs.tsv` las describe (split, categoría, segundos, texto): 21 de test (no usadas
   para entrenar, 16 kHz) y 19 de train elegidas de forma determinista (5 exclamaciones, 5 preguntas, 4 con puntos
   suspensivos, 5 largas). `REF_WAV` es `brais-norm-07156.wav` ("As medidas afectan en Galicia...", la del kit A/B,
   como en el Gauntlet 2).
6. **LanguageTool**: `language_tool_python` 3.4.0 baja LanguageTool 6.8 solo, a través del proxy, en `LTP_PATH`. No
   hizo falta bajarlo a mano. Trae el hunspell gallego (marca "fortaleiras" como `HUNSPELL_RULE`).
7. **Hugging Face**: `HF_HUB_DISABLE_XET=1` en `entorno.sh` para bajar por HTTP normal a través del puente de HF
   (comprobado con curl antes de empezar); el protocolo xet no se probó.
8. **Error de idempotencia (corregido)**: la primera versión del paso `whisper` borraba la marca de `whisper_hf`, y
   una segunda ejecución volvía a bajar 3,2 GB (141 s). Ahora `whisper_hf` se salta si el modelo convertido existe.
9. **No editar `instalar.sh` mientras se ejecuta**: bash lee el script a trozos según avanza. Se editó una vez con
   la instalación en marcha y terminó bien, pero es una fuente de fallos raros.
10. **El candado de CPU también para compilar.** La configuración de cmake de Cotovía compila dependencias (84 s); se
    lanzó una vez sin candado, se solapó con la prueba de imagen y le inflaba los tiempos. El paso `cotovia_nova`
    usa el candado en cmake y en make, y compila solo el ejecutable `cotovia` (el `make` completo compila una docena
    de variantes que no se usan).
11. **GitHub sí se pudo clonar en esta sesión.** El cmake de Cotovía hizo `git clone https://github.com/zrax/string_theory.git`
    (repo público) a través del proxy de git y funcionó, aunque `CLAUDE.md` y los aprendizajes del 29-09 dicen que
    clonar repos ajenos de GitHub no funciona. Puede depender de la sesión: si falla, el paso `cotovia_nova` (opcional)
    es el único afectado.

## Verificación mínima (`probas/proba_entorno.py`, `instalar.sh verificar`)

| Etapa | Resultado |
|---|---|
| Voz: `voz_st2.py`, 2 frases, JSON como el de `pipeline.py`, env de `pipeline.py` | 9,7 s de audio; carga del modelo + 1.ª frase 31,7 s; **RTF 0,39** en la 2.ª frase (1,7 s de cálculo para 4,4 s de audio) |
| Imagen: SDXL-Turbo 1024x576, 4 pasos, bf16 | carga 14-15 s; **25-26 s por imagen** (la 1.ª con calentamiento, 26-30 s) |
| `python revisor.py` (2 imágenes) | carga + 1.ª imagen 29,7 s; **18,9 s por imagen** después |
| ASR: faster-whisper + Whisper gl CT2 int8 sobre la voz de la prueba 1 | carga 4 s; transcripción 6 s; **WER 0,0** |
| LanguageTool gl-ES (`qa.lingua`) | "Os rapaces foi á praia." → `GENERAL_VERB_AGREEMENT_ERRORS` (3,5 s con el arranque de Java) |
| NLI (`veracidade.Verificador.nli`) | "irmandiños derrubaron" / "non derrubaron ningunha": contradicción 0,998. "foi derrotada" / "perdeu a guerra": neutral 0,979 (el NLI no ve la implicación: ya se sabía que en galego mide mal) |
| Montaje: `son.mesturar` + `montaxe.render`, 2 planos de 4 s | 22,7 s; MP4 1920x1080 h264 + AAC + subtítulos `mov_text`, 8,0 s, 1,25 MB; decodifica entero sin errores; mezcla -17,1 LUFS |

**La imagen de prueba** (prompt con el estilo de `imaxes.py` + "a granite hórreo beside a stone house with a slate
roof, oak trees, Galicia"): Claude la miró. Salen tejados de teja naranja, contraventanas verdes y fachadas claras de
pueblo mediterráneo, y **ningún hórreo**; el revisor la rechaza con razón ("tellados laranxas"), con las dos semillas
probadas. Con una sola escena no es una medida, pero apunta a lo que dijo el crítico de la ronda 3: SDXL-Turbo no
conoce "hórreo" ni obedece "slate roof". Para el agente visual: describir el objeto ("a raised granite granary on
stone pillars") en vez de nombrarlo, y poner la lousa y el granito al principio del prompt [S].

## Rendimiento de las imágenes (para el agente visual y el de vídeo)

Las imágenes son la etapa más cara del vídeo largo. Con torch 2.10.0+cpu (CPU con AVX512 y AMX-BF16, 4 hilos) una
imagen tarda **25-26 s** (Gauntlet 2: mediana 18,1 s en 63 imágenes, con otro contenedor y otra versión de torch).
Desglose medido con un script ad hoc (pipeline con `output_type='latent'` y el VAE aparte, 1024x576, con el
candado; no se guardó):

| Variante | Tiempo |
|---|---|
| Texto + 4 pasos de la UNet (latente) | 16,5 s (`channels_last` en la UNet no cambia nada: 16,6 s) |
| VAE bf16 (como hoy) | 11,3 s |
| **VAE bf16 con `channels_last`** | **5,9 s** (misma salida: diferencia media 0,003 frente a fp32) |
| VAE fp32 con `channels_last` | 19,8 s (peor) |
| VAE pequeño TAESDXL (`madebyollin/taesdxl`, MIT) | 1,7 s, pero se aparta más (diferencia media 0,065 frente al VAE completo) |

**Recomendación** (no aplicada: `imaxes.py` es del agente de pipeline/visual): tras cargar el pipeline,
`pipe.vae.to(memory_format=torch.channels_last)` baja cada imagen de ~28 s a ~20-22 s (−20 a −27 % en dos medidas)
sin cambiar el resultado.

## Hallazgo para la voz: Cotovía 0.5 no da los fonemas con los que se entrenó el modelo

El `.deb` de Cotovía 0.5 (SourceForge, 2012) es el que usaba el pipeline. Nos_StyleTTS2-Brais-GL se entrenó con la
Cotovía de Nós (`github.com/proxectonos/cotovia`, cuyo código viene dentro del repo del modelo, `Utils/cotovia`), que
**marca las vocales abiertas** (É, Ó: *pÓrta*, *tÉrra*, *Óme*) y **deja átonos los monosílabos** (*a*, *de*, *que*,
*en*). La 0.5 no distingue abiertas de cerradas (*po^rta*, *te^rra*) y acentúa los monosílabos (*á*, *ké*, *éN*).

Medido con `probas/comparar_cotovia.py` contra la columna `phonetic_transcription` del corpus Nos_Brais-GL (122 frases:
las 21 de test y 101 de train), tras quitar ¿ ¡ y normalizar dígrafos como hace `clean_output`:

| Cotovía | Frases idénticas | Caracteres distintos | Vocales abiertas tónicas (corpus: 135) |
|---|---|---|---|
| 0.5 (`.deb`, la de por defecto) | 8 / 122 | 7,8 % | 10 |
| Compilada de Nós (`cotovia_nova`) | 84 / 122 | 0,9 % | 142 |

Es decir, con la 0.5 el modelo recibe en inferencia una entrada distinta de la del entrenamiento en casi 1 de cada 12
caracteres, sobre todo en la calidad de las vocales medias y en el acento de las palabras átonas: justo lo que hace
sonar "natural" o "de fuera" a un locutor gallego [S]. `voz_st2.py` funciona igual con la compilada (mismas 2 frases:
WER 0,0; fonemas *nÓjtes*, *imbÉrno*, *BÉZas*, *istÓrjas*). Diferencias que quedan con la compilada: alguna palabra
suelta (*DúN* por *DuN*, *kompléksa* por *kompléSa*) y la puntuación. Una rareza vista: "para escoitar" sale como
*pra eskojtár*.

**Recomendación al agente de voz**: hacer A/B de escucha y medidas con `ST2_PATHBIN=$COTOVIA_NOVA_PATHBIN` frente a la
de por defecto. No se ha cambiado el valor por defecto porque la voz de la ronda 3 (WER 0,037) se midió con la 0.5
y el cambio altera la pronunciación de todo el vídeo: lo decide la pieza de voz.

## Qué no instala el script

- El LLM local (llama-cpp-python compilado + GGUF de EuroLLM, 5,6 GB): en el Gauntlet 3 el guion lo escribe Claude
  (decisión del promotor) y no hay disco de sobra. `entorno-llm.sh` sigue documentando cómo era.
- Las voces VITS de Nós (`coqui-tts`) del kit A/B: no las usa el pipeline.
