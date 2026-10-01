# Notas para Claude en este repo

## Qué es este repo

Proyecto **"Serán · Historia de Galicia para durmir"**: canal de YouTube desatendido, hecho con IA, de historia y cultura
de Galicia para quedarse dormido, **100 % en galego**. Es un hobby con opción de negocio del promotor.

**Al empezar una sesión, lee en este orden:**
1. [`docs/HANDOFF.md`](docs/HANDOFF.md): qué se hizo, estado actual, decisiones vigentes y próximos pasos.
2. [`docs/APRENDIZAJES.md`](docs/APRENDIZAJES.md): lo aprendido (producto, tecnología, método y entorno).
3. [`plan-de-negocio/decisiones.md`](plan-de-negocio/decisiones.md) y las secciones "PRIORITARIO" de
   [`plan-de-negocio/gauntlet2/contexto.md`](plan-de-negocio/gauntlet2/contexto.md): decisiones del promotor.
4. El plan vigente: [`plan-de-negocio/plan-v2-desatendido.md`](plan-de-negocio/plan-v2-desatendido.md). El
   `plan-de-negocio.md` (v1) está sustituido; se conserva como histórico.

## Estructura

| Ruta | Contenido |
|---|---|
| `docs/` | Handoff y aprendizajes |
| `plan-de-negocio/` | Planes v1 y v2, decisiones, guion muestra v1, tribunal del Gauntlet 1 |
| `plan-de-negocio/gauntlet/` | Gauntlet 1: investigación y piezas finales |
| `plan-de-negocio/gauntlet2/` | Gauntlet 2: contexto, referencia, piezas, veredictos de cada ronda, medidas y vídeo de ejemplo |
| `plan-de-negocio/gauntlet3/` | Gauntlet 3: episodio largo "As meigas de verdade" (31 min): tema, dossier, guion, voz, son, visual, `video/` (QA, avance, imágenes elegidas) y tribunal final |
| `herramientas/voz/` | Voces de Nós (VITS y StyleTTS2), kit A/B y control ASR |
| `herramientas/pipeline/` | Pipeline automático tema → MP4 (guion, corrección, voz, escenas, imágenes, sonido, montaje, QA). Su README explica instalación, etapas y licencias |

## Convenciones

- **Idioma:** documentos de trabajo y planes en **castellano**; todo lo que ve u oye el público en **galego normativo (RAG)**.
- **Evidencia:** cada cifra con fuente (URL) o marcada como supuesto [S]. No inventar datos.
- **Nunca afirmar en público una revisión humana que no existe.** Aviso hablado vigente: "A voz que vas escoitar é
  sintética, e este texto preparouno un proceso automático."
- **Distinguir siempre** qué es automático y qué hizo Claude o una persona a mano (en QA, README y mensajes al promotor).
- Cuando el promotor cambie una decisión, revisar los textos públicos heredados (avisos, guiones, correos) que dependan de ella.
- El trabajo va en la rama que indique la sesión y el promotor decide cuándo pasa a `main`.

## Entorno (Claude Code en la nube)

- El scratchpad y los entornos (venvs, modelos de ~1-6 GB) **no sobreviven** entre sesiones: hay que reconstruirlos con
  las instrucciones de `herramientas/pipeline/README.md` y `herramientas/voz/README.md`.
- Solo CPU (4 núcleos). **Límite real de memoria: 13,36 GiB para todos los procesos** (no los 15,7 de `free`). Un
  workflow corre 2 agentes a la vez. Un episodio de 31 min ≈ 16,5 h de CPU de núcleo (imágenes ≈ 100 s por intento en
  una CPU sin bf16; ≈ 30 s si `/proc/cpuinfo` tiene `amx_bf16`).
- Hugging Face y PyPI son accesibles. Clonar repos públicos de GitHub falló el 29-09-2026 pero funcionó el 30-09-2026
  (`git ls-remote`/`git clone` por el proxy de git): depende de la sesión. ffmpeg completo vía `imageio-ffmpeg`.
- **Entorno en una orden:** `bash herramientas/pipeline/instalar.sh` (≈6 min, ≈15,7 GB en el scratchpad) y
  `source herramientas/pipeline/entorno.sh`; `instalar.sh verificar` prueba cada etapa.
- `coqui-tts[codec]` necesita `transformers>=4.56,<5`. Cotovía 0.5 (`.deb` de SourceForge) para las voces de fonemas.
- El guion del pipeline debe usar un **LLM potente por API** (decisión del promotor); no hay clave de API en el entorno.
- Para compartir un fichero recién subido, usar la URL `raw/<commit>/...` de GitHub (la de la rama va con caché).
  Adjuntar al chat admite como máximo 30 MB.

## Trabajos largos (render de horas): lo aprendido el 01-10-2026

- **El contenedor se reinicia si la sesión queda ociosa sin ninguna tarea en segundo plano**, aunque haya procesos
  `setsid nohup` trabajando: mientras dure el trabajo, mantener **siempre un Monitor armado** (re-armarlo al caducar)
  y una revisión programada cada hora (`send_later`), que sí sobrevive al reinicio. El scratchpad sobrevive a los
  reinicios, no a una sesión nueva.
- Todo lo que use CPU o memoria de verdad va con `flock "$CPU_LOCK"`, también las pruebas: `nice 19` no basta.
- Lanzar con `herramientas/pipeline/lanzar-longo.sh` (reintentos y caché por etapas); mirar la hoja de rechazos de la
  puerta de imágenes en los primeros planos antes de dejarlo horas (la puerta puede rechazar de más).
- En los vigilantes, `awk` es `mawk`: usar `awk -W interactive` o no avisa. El ffmpeg estático da *segfault* al leer
  `.ts`.
- Páginas (Artifacts): solo sirven `.mp4/.webm` como vídeo y texto en `.txt/.json` (≤ 15 MB por fichero, ≤ 64 MB por
  publicación, 256 MB por versión). Un episodio se publica como HLS fMP4 con `paxina_episodio.py` (ver el README del
  pipeline). Para cambiar una página publicada, volver a publicar el mismo fichero: la URL no cambia.
- Másteres de vídeo de cientos de MB: no subirlos a git sin que el promotor decida dónde archivarlos (quedan para
  siempre en el historial y en cada clon).
- Generar imágenes fuera: desde aquí responden por HTTPS Replicate, fal, Hugging Face, OpenAI y Google; Modal no
  (gRPC). Una clave nueva del entorno solo llega a una sesión nueva.

## Gauntlet Loop: guardar resultados parciales en git

En los Gauntlet Loop (y en cualquier workflow multiagente largo) hay que **ir guardando en git los resultados parciales**, sin esperar al final:

- Commit y push de cada pieza cuando termina una ronda (borrador + veredicto del crítico), de la integración y de cada ronda del tribunal.
- Guardar también los veredictos de los críticos (ganó/perdió, mayor carencia), no solo los borradores.
- Motivo: el 29-09-2026 un reinicio del contenedor y el límite de uso de la sesión cortaron el Gauntlet del plan de negocio a medias. Lo que solo estaba en el scratchpad o en el journal del workflow estuvo a punto de perderse y el tribunal final quedó sin terminar.
- Los borradores de trabajo van en el repo (p. ej. `plan-de-negocio/gauntlet/`), no solo en el scratchpad.
- Las decisiones nuevas del promotor se pasan a un workflow en marcha escribiéndolas en su fichero de contexto.
- Si un workflow se corta, no confiar en `resumeFromRunId` tras editar el script (el 30-09-2026 repitió la ronda 1):
  lanzar un workflow nuevo que haga solo lo que falta, leyendo el estado del repo.

## No subir ficheros a medio escribir

- Antes de hacer commit de un vídeo o audio, comprobar que se decodifica entero (`ffmpeg -v error -i fichero -f null -`) y que ningún proceso lo está escribiendo (`ps`).
- Los renders deben escribir en un fichero temporal y renombrarlo al final (escritura atómica), para que un commit intermedio nunca capture un MP4 incompleto.
- Motivo: el 29-09-2026 se subió `gauntlet2/video/ejemplo.mp4` a mitad de render y quedó corrupto en GitHub (commits fb72a95 y fba68aa).
- No subir ficheros de más de 50 MB (p. ej. WAV de pruebas de escala: están en `.gitignore`).
