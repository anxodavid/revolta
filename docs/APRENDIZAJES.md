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
