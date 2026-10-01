# Tribunal final del Gauntlet 3: encargo

Encargo para un único agente (Claude) que juzga el episodio largo terminado. Lo escribió Claude (orquestador) el
01-10-2026. No hay ninguna persona revisando: el veredicto es de un agente y así debe decirlo.

## Papel

Un solo tribunal con tres miradas: director de fotografía y editor de documentales de época; guionista de canales
de historia para dormir que conoce lo que retiene audiencia; responsable de cumplimiento para publicar en YouTube.
Exigente y concreto: cada defecto con minuto:segundo, plano y fichero.

## Material (rutas desde la raíz del repo; `$SCRATCH` = `source herramientas/pipeline/entorno.sh`)

- Hoja a ciegas: `$SCRATCH/tribunal/cego/imagen1.jpg` e `imagen2.jpg` (16 fotogramas a 320x180 cada una). Una es el
  episodio y la otra la referencia (un canal real de historia para dormir; no se sube al repo). **No leas
  `$SCRATCH/tribunal/cego/clave.txt` hasta haber escrito la sección 1.**
- Detalle: `plan-de-negocio/gauntlet3/tribunal/detalle_1.jpg` … `detalle_5.jpg` (40 fotogramas con minuto, plano y
  fase debajo) y, solo después de destapar, `folla16_320.json` (qué plano es cada uno de los 16).
- QA automático: `plan-de-negocio/gauntlet3/video/qa.md` (y `qa.json` si hace falta un dato).
- Lo locutado: `plan-de-negocio/gauntlet3/video/guion.txt`; rótulos `rotulos.json`; descripción `descricion.txt`;
  prompts por plano `escenas.json`. El vídeo es `plan-de-negocio/gauntlet3/video/video.mp4` (no puedes verlo entero:
  trabaja con las hojas; si necesitas un fotograma concreto, extráelo con ffmpeg bajo `flock "$CPU_LOCK"`).
- Lo que pidió el promotor: `plan-de-negocio/gauntlet3/contexto.md` §1, §7 (D13-D16) y §8.
- Rondas anteriores: `veredictos/visual-r1.md` (PIERDE: casi nadie hacía cosas, figuras solas, fuego repetido,
  farolas y luces eléctricas), `veredictos/guion-r2.md` (GANA ajustado), `voz/informe.md`, `son/informe.md`.

## Veredicto: `plan-de-negocio/gauntlet3/veredictos/tribunal-final.md`

1. **Imagen a ciegas** (antes de destapar): los mismos 6 criterios y escala 1-5 de `visual-r1.md` (luz y rango,
   variedad y repeticiones, coherencia de estilo, personas haciendo cosas, artefactos, anacronismos), elección a
   ciegas con porcentaje y por qué. Después, destape.
2. **Imagen tras destapar:** ¿se corrigió la mayor carencia de la ronda 1? Defectos visibles en `detalle_*.jpg` con
   minuto:segundo y plano, en tres grupos: bloquea publicar / molesta / menor.
3. **Gancho (0:00 a ~2:00):** con el texto del gancho y sus fotogramas, ¿engancha? Nota 1-5 y por qué, frente a lo
   que hacen los canales grandes del género (cifras con fuente o marcadas [S]).
4. **Embudo hacia dormir:** con las medidas por fase de `qa.md` (ritmo, duración de plano, luz) y el guion, ¿baja de
   forma gradual y sin saltos? ¿Hay tramos monótonos (D14) o que despierten?
5. **Sonido (D13, D14):** diseño y medidas. No puedes oírlo: dilo y juzga solo lo que se puede comprobar.
6. **Cumplimiento para publicar:** aviso hablado, autoría y créditos, conxuro (solo el primer verso y con autor),
   etiqueta de contenido alterado o sintético de YouTube, licencias (voz Apache-2.0, SDXL-Lightning OpenRAIL++),
   descripción y capítulos.
7. **Veredicto:** por pieza (imagen; guion y gancho; voz y embudo; sonido) GANA/PIERDE frente a la referencia y a la
   ronda anterior; global: ¿se puede publicar tal cual, con arreglos o no? Hasta 5 arreglos antes de publicar (con
   minuto y fichero) y hasta 5 mejoras para el siguiente episodio.

## Reglas

- Castellano. Cada cifra con fuente o marcada [S]. Distinguir lo automático, lo que hizo Claude y lo que haría una
  persona. No afirmar nada que no se pueda ver o leer en el material.
- Guardar en git cada sección terminada (commit y push a `ccr-691a2e7c-82f2t8`, solo rutas explícitas), con el pie:
  `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` y
  `Claude-Session: https://claude.ai/code/session_01BD94yPJF6iT3xx11HfzUbG`.
- Escribir solo en `plan-de-negocio/gauntlet3/tribunal/` y en `veredictos/tribunal-final.md`. Nada de modelos ni de
  trabajos pesados de CPU; ffmpeg puntual siempre con `flock "$CPU_LOCK"`.
- Al terminar, responder con 10 líneas como máximo: veredicto global, nota del gancho, los arreglos antes de publicar.
