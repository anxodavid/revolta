# Aprendizajes de la sesión del 29-30 de septiembre de 2026

## Producto y mercado

- **El nicho en galego es diminuto.** Solo el 3,59 % de los mayores de 16 consume audiovisual sobre todo en galego
  (IGE, EEF 2023). En radio es el 15 %: el galego se escucha más de lo que se ve. Mercado atendible estimado: 2.000-20.000
  oyentes. No hay competencia directa, pero eso puede ser un hueco o un desierto.
- **El tema funciona, pero en castellano:** "Galicia para dormir" (sobre todo lendas) tiene vídeos de 5-108 K vistas. Por
  eso conviene **toda Galicia** y no solo historia, y explorar **pistas de audio** pt/es/en en el mismo vídeo.
- **El estilo "fábrica de engagement" y el contenido para dormir chocan.** Solución acordada: ganchos solo al principio
  (título, miniatura, primeros 60-120 s) y bajada gradual al tono de dormir.
- **La calidad humana cuesta dinero real:** corrector y historiador ≈ 305 € por episodio. Por eso el promotor eligió el
  canal desatendido. Con él, la calidad depende de controles automáticos y de un buen LLM.
- **Transparencia:** el aviso hablado debe ser veraz. En un guion heredado del plan v1 quedó "revisouno un corrector
  profesional", falso tras la decisión D5; el promotor lo detectó. Revisar todo texto público cuando cambie una decisión.

## Tecnología

- **Voz en galego:** los modelos abiertos del **Proxecto Nós** (Hugging Face `proxectonos`) funcionan en CPU. El mejor
  hoy es **Nos_StyleTTS2-Brais-GL** (WER 0,26 frente a 0,38-0,50 de las VITS en el control ASR del kit). Los modelos
  son Apache-2.0, pero los corpus de voz tienen condiciones de uso restringidas: pedir permiso a Nós/USC antes de
  publicar.
- **Guion:** un LLM local pequeño (EuroLLM-9B en CPU) **inventa historia y palabras** en galego ("a irmandade venceu",
  "fortaleiras"). Con filtros bloqueantes de veracidad no consigue escribir párrafos limpios y el guion queda como el
  dossier recitado. **Hace falta un LLM potente** (por API).
- **Controles automáticos útiles:** ASR con el Whisper galego de Nós (WER), LanguageTool gl + hunspell, veracidad por NLI
  contra un dossier de fuentes, ffmpeg `ebur128` para sonoridad, sincronía de subtítulos. **No detectan** giros torpes
  ni si una imagen "parece Galicia".
- **Imágenes:** SDXL-Turbo en CPU da un resultado evocativo, pero cuela iconografía mediterránea. La revisión con
  Florence-2 solo ve lo que su descripción nombra. Hace falta una lista positiva de iconografía galega.
- **Coste de cómputo:** 3 min de vídeo ≈ 5 h de CPU de núcleo en este entorno; 60 min ≈ 28,6 h de reloj. Para producir
  en serie hace falta GPU o episodios más cortos.
- **Cotovía** normaliza mal algunas cifras ("mil catrocentas sesenta e sete"): escribir los números en letra en el guion.

## Proceso y método (Gauntlet Loop)

- **Gauntlet Loop** (técnica de Matt Shumer): el agente parte el objetivo en piezas; cada pieza tiene un constructor y un
  crítico independiente con contexto limpio, que compara a ciegas con una referencia real y exigente; si pierde, el
  crítico señala la mayor carencia y la pieza vuelve al constructor; el bucle termina cuando gana o cuando el humano para.
- **Los críticos son muy útiles para cazar errores reales** (fechas, citas falsas, incoherencias entre secciones,
  palabras inventadas, imágenes no gallegas). Casi ninguna pieza "gana" del todo: el tope de rondas es la parada real.
- **El juez humano es insustituible** para la voz y para decir si algo engancha. El feedback del promotor tras ver el
  vídeo cambió el rumbo (ritmo, ganchos, temas).
- **Decir siempre qué hizo un humano o Claude a mano y qué fue automático.** El primer vídeo que vio el promotor tenía el
  guion escrito por Claude: no era desatendido. No se aclaró a tiempo.
- Las decisiones del promotor se comunican a un workflow en marcha **escribiéndolas en el fichero de contexto** que los
  agentes leen al empezar cada ronda. No hace falta pararlo.

## Entorno y herramientas (Claude Code en la nube)

- **Los contenedores se reinician** sin aviso y la sesión tiene **límite de uso**: se perdió trabajo varias veces. De ahí la
  regla de `CLAUDE.md`: commit y push de cada ronda, con sus veredictos.
- **No subir binarios a medio escribir:** un MP4 subido durante un render quedó corrupto en GitHub. Validar con ffmpeg y
  escribir renders de forma atómica.
- **Reanudar un workflow tras editar el script no es fiable:** al relanzarlo con `resumeFromRunId` volvió a ejecutar la
  ronda 1 (no reutilizó la caché). Para seguir, es más seguro lanzar un workflow nuevo que haga solo lo que falta,
  leyendo el estado del repo.
- Con 4 CPU, un workflow solo corre **2 agentes a la vez**: los Gauntlet llevan horas.
- **GitHub sirve con caché** las URL `raw/<rama>/...`: para compartir un fichero recién subido, usar `raw/<commit>/...`.
- **Adjuntar ficheros al chat** tiene un límite de 30 MB.
- La página de Gemini compartida no carga sin JS; se pudo leer llamando a su RPC `batchexecute` (`rpcids=ujx1Bf`).
- Chromium de Playwright necesitó importar el certificado del proxy en `~/.pki/nssdb` (con `certutil`).
- Versiones que funcionan: `coqui-tts[codec]` con `transformers>=4.56,<5`; `torch` CPU; ffmpeg completo vía
  `imageio-ffmpeg` (el del sistema no tiene codificadores). Hugging Face y PyPI son accesibles; GitHub (clonar repos
  ajenos) no.

# Sesión del 30-09-2026 (tarde): Gauntlet 3, vídeo largo "Cousas de Galiza para durmir"

Se va completando según avanzan las piezas. Detalle por pieza en `plan-de-negocio/gauntlet3/aprendizajes/`.

## Entorno

- **Reconstrucción en una orden:** `herramientas/pipeline/instalar.sh` (idempotente, descargas en paralelo) monta voz,
  imágenes, puerta de revisión, QA y LanguageTool en ≈6 min y ≈15,7 GB. Versiones fijadas en `requisitos-entorno.txt`.
  Bajar solo los ficheros que se cargan ahorra mucho: el repo de SDXL-Turbo pesa 55,5 GB y se usan 6,95.
- **Cotovía 0.5 (el `.deb` de 2012) no da los fonemas con los que se entrenó la voz de Nós:** no marca las vocales
  abiertas (*pÓrta*, *tÉrra*) y acentúa los monosílabos átonos. Difiere en el 7,8 % de los caracteres frente al
  corpus; la Cotovía del repo de Nós, compilada, en el 0,9 %. Las muestras anteriores se hicieron con la 0.5.
- **VAE de SDXL con `channels_last`:** de 11,3 a 5,9 s por imagen en CPU, con la misma salida.
- SDXL-Turbo no conoce "hórreo" ni obedece "slate roof": sale un pueblo mediterráneo con tejas naranjas. Hay que
  describir el objeto ("raised granite granary on stone pillars") y poner granito y lousa al principio del prompt.
- `Nos_Brais-GL` es un dataset con términos de uso que prohíben difundir las grabaciones: las referencias de estilo se
  quedan en el scratchpad, nunca en el repo.
- Clonar repos públicos de GitHub funcionó en esta sesión (falló en la anterior).

## Tema (elección con datos)

- **Elegido: "As meigas de verdade"** (brujería real en Galicia según los procesos de la Inquisición de Santiago y de
  la Real Audiencia, y las lendas contadas como lendas), con arranque en frío en el conxuro de la queimada (escrito en
  Vigo en 1967). Es el tema con más ganchos verdaderos y documentados; "brujas" es un término enorme en YouTube España
  (≈ 34 veces "Santa Compaña") que sube × 2,0 en octubre; en galego no hay nada para dormir. Segundo: Camiño de
  Santiago (el mejor dato "para dormir" de un tema gallego, 182.379 vistas). Detalle en `gauntlet3/tema/investigacion.md`.
- **La Santa Compaña** tiene más demanda y más pico en octubre (× 2,3-3,2), pero su público es de terror: sus versiones
  para dormir se quedan en 5-6 K vistas.
- **Medir YouTube sin clave:** `yt-dlp --flat-playlist -j` con el cliente `android_vr` (1,5 s por consulta, sin
  bloqueos); para metadatos completos, `mweb` con `--ignore-no-formats-error` y 3 s entre peticiones. Google Trends
  con `pytrends` a través del proxy (sin `retries`/`backoff_factor`), mejor con `gprop="youtube"`.
- **Limpiar los resultados es lo que más cuesta:** música (Mägo de Oz, Luar na Lubre) y homónimos inflan las cifras
  del folclore gallego (la "Santa Compaña" parecía tener 20 M de vistas).
- **Fuente de oro para meigas:** el PDF de la exposición "Meigas, feitizos das menciñeiras" del Arquivo do Reino de
  Galicia (2020), con transcripciones de procesos reales. Las fuentes discrepan en fechas (la única hoguera: 1627 o
  1579): se dice sin el año.

## Dossier (hechos verificados)

- **Una sola fuente de verdad con citas literales comprobadas por código:** `gauntlet3/dossier/feitos.yaml` guarda
  cada hecho en galego con su cita literal de la fuente; `xerar.py comprobar` busca cada cita en el texto descargado
  (350 citas, más una prueba negativa) y `xerar.py ficha` genera la ficha del pipeline (180 de 244 hechos).
- **LanguageTool sobre los hechos antes del guion**: evita que el guionista copie redacciones que la puerta de lengua
  rechaza (reflexivos, "decomisado" → "comisado", "ungüento").
- **El diccionario de la RAG como fuente de detalles tranquilos y verdaderos** (lareira, escano, orballo, lousa...),
  con URL por palabra: material para la parte de dormir.
- **La veracidad automática no para falsedades hechas con palabras del dossier** ("María Soliña morreu queimada",
  "Feijoo naceu en Samos" pasan): la lista **"Non dicir"** tiene que ir en el encargo del guion y en el crítico.
  Dejar fuera de la ficha los años y nombres en conflicto sí funciona: H1 impide decirlos.
- Galiciana sirve un desafío anti-bot en JavaScript (no saltarlo); la API de Galipedia da 429, la página normal con
  4 s entre peticiones funciona.

## Sonido

- El promotor oyó la lluvia de la muestra como **ruido blanco**: medida, era ruido gaussiano filtrado (curtosis 3,07,
  energía entre 2 y 8 kHz). La nueva lluvia con gotas, goteos y ráfagas (curtosis 9, 11-20 dB menos por encima de
  4 kHz) le gustó más, sobre todo con lareira, pero pidió **ambiente por escena, sin fondo constante y con tramos de
  voz limpia** (D13), variado para no cansar y con **murmullo de gentío** cuando la escena lo tenga (D14).

## Método: cortes por límite de uso

- **Con 5 agentes a la vez se agotó el límite de uso de la sesión en ~5 h** (corte a las 16:30 UTC). Gracias a los
  commits frecuentes solo se perdió el contexto de los agentes; lo que no habían subido seguía en disco y se subió al
  volver. El contenedor se reinició, pero el scratchpad (entorno y modelos) sobrevivió esta vez.
- **Retomar un agente cortado con `SendMessage` a su id** lo reanuda con su contexto intacto: mejor que lanzar uno
  nuevo que vuelva a leerlo todo. Solo se relanza desde cero el que apenas había empezado.
- Conviene guardar en el repo, y no solo en el scratchpad, las utilidades que crean los agentes (p. ej. el comprobador
  rápido del guion).

## Voz en embudo (gancho → dormir)

- **Resultado medido (sin escucha humana):** arousal 0,64 → 0,43, variación de la F0 4,8 → 2,6 semitonos y
  182 → 113 palabras/min (con pausas), bajando en cada punto de la curva, con WER frase a frase ≤ 0,054. Referencia
  "viva" = media de 3 grabaciones de Brais; "calma" = 1. Muestra: `gauntlet3/voz/mostra-embude.m4a`.
- **El ritmo es la palanca grande** del tono (escala 1,3 → −0,09 de arousal); la referencia de estilo pesa poco con los
  parámetros de siempre y solo se nota bajando `beta` (0,4-0,6). Hace falta juntar varias palancas pequeñas en el
  mismo sentido (ritmo, rango de F0, referencia calma, algo de altura).
- **Ampliar el rango de la F0 mete voz cascada** (tramos < 75 Hz): `voz_st2.py` no baja ningún tramo de 80 Hz.
- Algunas referencias con `beta` bajo hacen tartamudear al modelo ("di di diante"): probar el WER de cada referencia
  en su punto de la curva.
- **Cotovía compilada de Nós en modo `-p1`**: en modo síntesis dice "Cousas de Galiza **pra** durmir" y contrae el
  artículo ("facelo lume"), cosas que el corpus de entrenamiento no tiene; `-p1` las quita.
- **El WER de Whisper sobre un audio largo con pausas engaña:** el mismo pasaje da 0,18-0,28 entero y ≤ 0,054 frase a
  frase (se salta frases enteras). El QA del vídeo largo transcribe cada frase en su tramo (`qa.asr_por_frases`).
- **Sonido, resultado (pieza SON):** de 4 opciones (A lluvia continua, B lluvia y lareira por escena, C catálogo
  completo por escena, D sin ambiente) se recomienda **C**, que es la preferencia del promotor (D14): DNSMOS OVRL 3,02
  (D 3,37; A 2,65), la voz no se degrada (SIG 3,57-3,62 en todas), WER frase a frase 0,026, **0 sustos en la zona de
  dormir** y monotonía del 11 % (A: 93 %). El murmullo de gentío con 6-12 voces de nuestra propia voz TTS es
  ininteligible para Whisper. **La lista de planos decide el ritmo del sonido:** alternar sonido en cada plano da un
  parpadeo (62 cambios cada 10 min); la QA avisa por encima de 30 cambios cada 10 min en el gancho y de 10 al dormir.

## Guion (ronda 1)

- **Duración:** con la curva de voz medida (182 → 119 palabras/min con pausas), 3.500 palabras dan ≈ 26 min; para
  30 min harían falta ≈ 4.100. El comprobador rápido (0,43 s/palabra) sobrestimaba: recalibrar a ≈ 0,33 s/palabra.
- **Escribir para que la veracidad automática vea el apoyo:** en el gancho toda frase necesita coincidencia léxica alta
  con un hecho; las frases del narrador ("contarémolo...") fallan siempre; una mayúscula a media frase ("san Xoán",
  "Idade Media") o un "nunca" enfático vuelven exigida una frase de ambiente.
- **Galiza frente a Galicia:** H1 acepta las dos, pero la coincidencia léxica las ve como raíces distintas.
- **Si una frase fusionada dispara un aviso de LanguageTool, lo más limpio es volver a la redacción del hecho del
  dossier**, que ya pasó LT.
- **Medir la longitud de frase por fase:** en el primer borrador las frases de dormir eran más cortas que las de la
  transición, lo contrario del embudo.
- **Coste de la veracidad automática:** NLI contra los 180 hechos por frase = 26 min de CPU en un guion largo;
  limitándolo a los hechos que pueden apoyar la frase (coincidencia ≥ 0,5), 144 s con las mismas decisiones.

## Imagen (ronda 1 de la pieza visual)

- **La luz plana de la muestra anterior la causaba el prompt, no el modelo:** el estilo fijo "soft overcast light" y la
  igualación de color a la media del episodio. Con una fuente de luz explícita por plano y la gradación por fase
  (conserva la luz de cada imagen y solo corrige los extremos) sale luz variada incluso con SDXL-Turbo.
- **SDXL base + UNet SDXL-Lightning de 4 pasos a 1344x768** (OpenRAIL++): más nítido y "de cine" que Turbo a 1024x576
  (33-48 s por imagen frente a 25,5). La versión de 8 pasos no compensa (82 s, casi igual). Los codificadores de texto
  de Turbo y de SDXL base son idénticos (mismo sha256): no hace falta bajarlos dos veces.
- **SDXL no sabe dibujar el hórreo ni el carro de bois de roda maciza**, ni siquiera describiéndolos: salen una aldea
  inglesa y ruedas de radios. La biblia pide no ponerlos como sujeto.
- **Lightning mete detalles modernos que Turbo no** (farolas, luces de ciudad, sofás, ventanales de cristal): la
  puerta de Florence y CLIP no los caza todos.
- **Puerta CLIP por pares** (teja naranja frente a lousa, ciprés frente a carballo, olivo, palmera, eucalipto),
  calibrada con 72 imágenes: 0 falsos positivos, pero no ve tejas pequeñas y apagadas. La repetición se mide ahora
  contra todo el episodio (coseno 0,90), con un tope por arquetipo.
- **Referencia:** el cliente `mweb` de yt-dlp da storyboards de 320x180; las hojas del `.mhtml` llegan corruptas y
  hay que bajarlas una a una con curl.

## Entorno: memoria compartida (30-09-2026, noche)

- **Todos los procesos que lanzan las herramientas comparten un cgroup de memoria: límite real 13,36 GiB** (no los 15,7 GB de `free`; se ve con `dmesg | grep "memory: usage"`). Una puerta de texto
  (NLI + LanguageTool, ~2 GB) lanzada **sin el candado de CPU** mientras se generaban imágenes (11,8 GB) hizo que el
  OOM killer matase las dos. Lección: todo lo que carga modelos va con `flock "$CPU_LOCK"`, aunque sea "rápido"; el
  candado protege también la memoria. Tras un OOM, matar los servidores Java de LanguageTool huérfanos.
- **Las tareas en segundo plano de la herramienta Bash se cortan a los 30 min** (esperando el candado también
  cuentan). Para trabajos largos, lanzar un script desacoplado (`setsid nohup ... &`) que escriba un log, y vigilarlo
  con Monitor.
- **`pkill -f PATRÓN` puede matar la propia shell** si el patrón aparece en la orden que se está ejecutando: usar PID.
- La ronda 2 del guion ganó (ajustado) con 16 sustituciones exactas del crítico; la carencia que queda (tramo de
  6:27-11:36 con muchas atribuciones y cantidades) va a la plantilla del siguiente episodio.
- **`multiprocessing.Pool` se cuelga para siempre si el OOM mata a su trabajador** (el 30-09-2026 a las 23:09: 30 min
  perdidos sin ninguna línea en el log). Con `concurrent.futures.ProcessPoolExecutor` sale `BrokenProcessPool` y el
  lanzador (`herramientas/pipeline/lanzar-longo.sh`) reintenta; lo hecho queda en la caché de cada etapa.
- **Memoria de la etapa de imágenes: ~12 GB** (SDXL-Lightning, Florence-2 fp32, CLIP-L y MediaPipe en un proceso). El
  servidor Java de LanguageTool (0,55 GB) y el NLI que quedaban vivos del paso de texto, más un intento guiado con CFG
  (lote doble en la UNet), bastaron para pasar el límite. Solución: cerrar LanguageTool a la fuerza antes de las imágenes
  y sin intentos guiados en producción (`IMG_CFG_REINTENTO=0`).
- **Un reinicio del contenedor mata también los procesos desacoplados** (`setsid nohup`): el scratchpad sobrevivió,
  pero hay que relanzar. Tras el reinicio, la primera carga de los modelos desde el disco en frío tarda 10-20 min.
- **La CPU puede cambiar entre reinicios del contenedor.** Hasta el 30-09 a las 22:37 había AMX-BF16 (SDXL-Lightning
  1344x768 a ~30 s por imagen en bf16); después, una CPU sin bf16 nativo, donde el bf16 se emula y cada imagen tardaba
  370 s. Arreglo (`imaxes.bf16_rapido`): pesos de la UNet en bf16 y cálculo en fp32 capa a capa
  (`enable_layerwise_casting` sin excepciones, más las normas en fp32 y un *hook* que pasa a fp32 las entradas de la
  UNet), VAE en fp32 por teselas de 256 px: ~150 s a 1344x768 y ~90 s a 1024x576. Para que quepa la puerta en el mismo
  proceso (pico 13,3 GB), Florence-2-base en vez de -large. Comprobar `grep -o 'amx_bf16\|avx512_bf16' /proc/cpuinfo`
  antes de estimar tiempos.
- **`nice -n 19` no protege a la etapa de imágenes.** Una prueba de 6 min de ffmpeg (x264 a 720p) con `nice 19`
  mientras se generaba la primera imagen la llevó de ~90 s a 473 s (01-10-2026, 00:45): con 4 núcleos y una UNet que
  vive del ancho de banda de memoria, cualquier proceso pesado al lado cuesta mucho más que su parte de CPU. Todo lo
  que use CPU de verdad va con `flock "$CPU_LOCK"`, también las pruebas.
- **Generar imágenes fuera (01-10-2026):** desde este entorno responden por HTTPS Replicate, fal, Together, el router de
  Hugging Face, OpenAI, Google y BFL; **Modal no sirve** porque su cliente usa gRPC y el proxy del entorno no lo admite
  (`/root/.ccr/README.md`). Precios vistos ese día: SDXL-Lightning 4 pasos en Replicate ≈ 0,0018 $ por imagen y ~2 s
  (https://replicate.com/bytedance/sdxl-lightning-4step); FLUX.1 [schnell] en fal 0,003 $ por megapíxel
  (https://fal.ai/pricing); Hugging Face cobra lo mismo que el proveedor, sin margen, y la cuenta PRO trae 2 $ al mes
  (https://huggingface.co/docs/inference-providers/pricing). Una clave nueva del entorno solo llega a una sesión nueva.
- **Segundo OOM (01-10-2026, 01:09):** el trabajador de imágenes (12,2 GiB) más el proceso padre de `longo.py`
  (1,3-1,8 GiB que le quedaban de LanguageTool, el NLI y el audio de la voz) pasaron del límite de 13,36 GiB en el
  plano 4. Arreglo: caché de las puertas de texto (con el mismo guion, tema y código no se vuelven a cargar
  LanguageTool ni el NLI), `del` del audio por frases, `gc` + `malloc_trim(0)` en el padre y tras cada intento de
  imagen, `MALLOC_ARENA_MAX=2` y 12 reintentos en `lanzar-longo.sh`.
- **`mawk` (el `awk` de este sistema) lee la entrada por bloques:** en un vigilante `tail -F | grep | awk` no sale
  nada hasta que se llena el búfer, y el Monitor no avisó de la caída. Usar `awk -W interactive` (o no usar awk).
- **La puerta de imágenes rechazaba de más y empeoraba el vídeo (01-10-2026, planos 0-7 de la producción):** ~3,5
  intentos por plano (≈15 h para 162) y, al agotarlos, una imagen de reserva genérica. Mirando la hoja de los
  rechazos: "falta: clay bowl / lantern" con el objeto en la imagen (CLIP no ve objetos pequeños), "witch" en
  cualquier anciana junto al fuego (justo lo que pide el plano) y "arquetipo seguido" cuando la propia lista de planos
  pide dos lareiras seguidas. El plano de la queimada del gancho acabó en un retrato genérico. Ahora esos tres solo
  avisan (`imaxes.separar_avisos`; el arquetipo desde el 2.º intento) y se reeligió entre los intentos ya hechos sin
  regenerar. Los anacronismos (farolas, casas británicas, bañera, interiores modernos) sí acertaban y siguen
  bloqueando. Lección: antes de una producción larga, mirar la hoja de rechazos de los primeros planos.
- **Tercer reinicio del contenedor (01-10-2026, ~03:52 UTC):** mató la producción en el plano 41 y nadie lo vio hasta
  la revisión programada de las 05:50 (2 h perdidas). Las tareas en segundo plano y los Monitor mueren con el
  contenedor; lo único que sobrevive es una revisión programada (`send_later`). Para trabajos de horas: revisión cada
  ~1 h que mire `uptime` y relance si no hay proceso.
- **Causa probable de esos reinicios: la sesión ociosa.** Los dos del 01-10 (03:52 y ~06:00) llegaron 3-7 min después
  de terminar el turno **sin ninguna tarea en segundo plano** (ni Monitor ni Bash en background); con un Monitor o una
  espera en background armados, el render aguantó horas. El contenedor parece liberarse cuando la sesión queda
  inactiva, aunque haya procesos `setsid nohup` trabajando (el scratchpad sí sobrevive). Regla: mientras corra un
  trabajo largo, mantener siempre un Monitor armado (re-armarlo al caducar, cada 30 min) además de la revisión horaria.
- **Las imágenes de reserva ya no ayudan (01-10-2026, planos 90-93):** cuatro interiores con lareira agotaron los 6
  intentos; los 2 de reserva (prompt genérico sin personas) caían por "repetida" (CLIP 0,92 con otras reservas) o por
  vehículos y luz eléctrica. Cada plano difícil costaba 10 min para quedarse igualmente con el mejor intento. Ahora
  `IMG_RESERVAS=0` en producción (4 intentos como mucho). Queda pendiente para el siguiente episodio: "fireplace
  mantel" como negativo salta en casi cualquier lareira (4 de 4 en el plano 92) y "interior moderno" en muchos
  interiores; hay que calibrarlos con una hoja de rechazos antes de producir.
