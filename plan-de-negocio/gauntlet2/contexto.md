# Gauntlet 2: canal desatendido (contexto para todos los agentes)

## Qué se construye
Un **canal de YouTube desatendido**: vídeos de historia de Galicia **para dormir**, **100 % en galego**, hechos por un
**proceso automático sin revisión humana**, con el mejor software **open source** disponible. Se publica en **anónimo**,
como **hobby**. Referencia de estilo y de listón: el canal *Historia Desconocida*, vídeo
"Versalles en 1682: Lujo por fuera, suciedad por dentro: la realidad que ocultaban" (https://youtu.be/_lnOveSTjWA,
canal https://www.youtube.com/@HistoriaDesconocida-m4j): imágenes o animaciones evocativas generadas con IA, narración
sintética continua y larga duración. Nuestro vídeo toma ese estilo visual, pero con tono sereno para dormir (sin el
estilo "fábrica de engagement" visceral).

## Decisiones del promotor (ver ../decisiones.md)
- D5: sin revisión humana pagada; proceso automático "que dé el pego". D6: hobby en anónimo.
- D1: validación formal de la voz (850-1.500 €) solo si el canal muestra tracción. D2: usar la voz más cercana al listón.
- D3: ~6 h/semana mientras se monta el pipeline; ~1 h/semana después. D4: pedir permiso a Nós/USC y darles crédito.

## Tesis del promotor que hay que analizar en serio (no dar por buena)
Este enfoque **no tiene por qué ser "contra o galego"**, sino al contrario: promoción de la historia de Galicia que podría
acabar buscando apoyo. Puede **fomentar mejores modelos open source en galego** y la preparación de **buen contexto para
IAs en galego** (corpus, RAG, evaluaciones, errores reportados a Nós). Se podría acabar defendiendo su uso **pro lingua e
cultura**. Hay que analizar qué problemas acarrea con la comunidad Nós, la USC/CiTIUS, la CRTVG/TVG, la RAG, el Consello
da Cultura Galega, la Secretaría Xeral da Lingua, el sector del doblaje y la locución galega, AGPTI, la comunidad
tecnológica y la comunidad de hablantes, y cómo convertirlo en apoyo.

## Material existente (reutilizar, no rehacer)
- Plan v1 (con garantía humana, suspendido por el tribunal): ../plan-de-negocio.md; veredictos en ../tribunal.md.
- Investigación y piezas del Gauntlet 1: ../gauntlet/investigacion/*.md y ../gauntlet/piezas/*.md.
- Guion muestra en galego: ../guion-mostra-revolta-irmandina.md.
- Voz: StyleTTS2 Brais de Nós funciona en CPU. Script: /home/user/revolta/herramientas/voz/st2_sleep.py. Instalación
  operativa en /tmp/claude-0/-home-user-revolta/2e7d1051-da1e-54e9-bb2d-6cd0b746c55a/scratchpad/bench/st2 (modelos en st2/Models/galician/brais). Se ejecuta así (ver herramientas/voz/README.md):
  cd /tmp/claude-0/-home-user-revolta/2e7d1051-da1e-54e9-bb2d-6cd0b746c55a/scratchpad/bench && PATH=$PWD/pathbin:$PATH PYTHONPATH=$PWD/stubs TXT=... OUT=... SCALE=1.2 /tmp/claude-0/-home-user-revolta/2e7d1051-da1e-54e9-bb2d-6cd0b746c55a/scratchpad/tts/venv/bin/python st2_sleep.py
  (st2_sleep.py de bench usa como referencia de estilo /tmp/claude-0/-home-user-revolta/2e7d1051-da1e-54e9-bb2d-6cd0b746c55a/scratchpad/tts/kit/t1/brais_1_human.wav). Factor de tiempo real ~0,3-0,4 en CPU.
  Voces VITS de Nós y su script: herramientas/voz/synth.py (venv: /tmp/claude-0/-home-user-revolta/2e7d1051-da1e-54e9-bb2d-6cd0b746c55a/scratchpad/tts/venv). Control ASR: herramientas/voz/asr.py (faster-whisper).
- Kit A/B de voces para los jueces humanos: https://claude.ai/artifact/MTsjYNFmH5WaWYqAEJ7HGH

## Entorno de cómputo
Solo CPU: 4 núcleos, 15 GB de RAM, ~13 GB de disco libre. Hugging Face y PyPI accesibles. El ffmpeg del sistema no
tiene codificadores: usa `pip install imageio-ffmpeg` (binario completo). Para imágenes, elige un modelo open source
que corra en CPU en tiempo razonable (p. ej. SD-Turbo, SDXL-Turbo, LCM o similar) y comprueba su licencia.

## Reglas de trabajo
- Todo lo que produzcas va en el repo, en /home/user/revolta/plan-de-negocio/gauntlet2/ (piezas, vídeo, código del
  pipeline en /home/user/revolta/herramientas/pipeline/). Los binarios pesados (modelos) no van al repo; el vídeo final
  y sus fotogramas sí, si pesan < 50 MB.
- Plan en CASTELLANO; todo lo que ve u oye el público en GALEGO normativo.
- Cada cifra con URL o marcada como supuesto [S]. Fecha: 29-09-2026.

## Feedback del promotor tras ver el vídeo de ejemplo (29-09-2026) — PRIORITARIO
El promotor, como juez humano, vio `video/ejemplo.mp4`: **vale como primera aproximación**, está cerca de algo publicable
"sin dar vergüenza ajena". Pide dos cambios:
1. **El ritmo es algo lento.** Subirlo, sobre todo al principio.
2. **Más "picante" para enganchar**, como la referencia de Versalles: ganchos del tipo *"non vas crer o que facían as persoas
   daquela"*, contraste "lujo por fuera, suciedad por dentro", curiosidad y detalle cotidiano sorprendente.

Cómo aplicarlo sin romper el formato para dormir (fórmula de "embudo"):
- **Título, miniatura y primeros 60-120 s:** ganchos claros y ritmo más vivo, al estilo de la referencia.
- **Después:** el ritmo y la intensidad bajan poco a poco hasta el tono sereno de dormir; los ganchos se vuelven suaves
  (curiosidades tranquilas, sin sobresaltos ni gritos).
- Los ganchos deben ser **verdaderos** (nada inventado para impactar) y en galego natural, no calcos del castellano.
- Reflejarlo en el pipeline (prompts de guion, ritmo de la voz y de los cortes), en el vídeo de ejemplo y en el plan.

## Directriz del promotor sobre temas y tono (29-09-2026) — PRIORITARIO
- **Ganchos solo al principio** (título, miniatura, primeros 60-120 s); después, bajada al tono de dormir.
- **Temas ampliados a toda Galicia**, no solo historia medieval: mitos, lendas (Santa Compaña, meigas, mouras…), el mar,
  castros, Camino, vida cotidiana de antes y **el porqué de la idiosincrasia galega** (retranca, morriña, minifundio,
  emigración, etc.). El catálogo del plan y del pipeline debe reflejarlo.
- **Prioridad: enganchar y ser atractivo audiovisualmente**, por encima de la exhaustividad. Nada de "chapa histórica
  aleccionadora y ultrarrigurosa que nadie quiera consumir". Pero **sin perder rigor**: nada falso ni inventado; lo
  legendario se presenta como leyenda; si algo es dudoso se dice o se omite.
- **Contexto de mercado:** el promotor duda de que el nicho exista ("¿a quién le importan los irmandiños y cuántos se
  duermen con vídeos de YouTube?"). El plan debe responderlo con cifras (3,59 % de consumo audiovisual en galego; 2.000-20.000
  oyentes atendibles; ninguna competencia directa; demanda de "Galicia para dormir" en castellano) y con la ampliación de temas.
- **Pistas de audio multilingües** (gl original + es/pt en el mismo vídeo): **aún no decidido por el promotor**; el plan
  puede evaluarlas como opción con números, sin darlas por aprobadas.

## PREGUNTA OBLIGATORIA: ¿apuntamos a un nicho inexistente? (29-09-2026)
El promotor sospecha que el nicho (gente que consume en galego contenido de historia/cultura de Galicia para dormir) puede
**no existir** o ser demasiado pequeño para sostener un canal. Todo plan, pieza e integración debe:
1. **Dar un veredicto explícito:** existe / existe pero es marginal / no hay evidencia suficiente; con la evidencia a favor
   y en contra (cifras con fuente) y sin maquillarlo.
2. **Separar tres nichos** y estimar cada uno: (a) historia de Galicia para dormir en galego; (b) toda Galicia (mitos, lendas,
   mar, idiosincrasia) para dormir en galego; (c) lo mismo con pistas de audio es/pt (opción no aprobada).
3. **Proponer una prueba barata y falsable** con el pipeline automático: qué se publica, cuánto tiempo, qué métricas
   (vistas, retención, % de audiencia en galego, suscriptores, comentarios) y **qué umbral concreto declara el nicho
   inexistente y manda parar**.
4. Los críticos y el tribunal deben suspender cualquier pieza que esquive esta pregunta o la conteste sin cifras.

## Decisión del promotor: explorar pistas de audio multilingües (29-09-2026)
- **Aprobado explorarlo** (sustituye al "aún no decidido" anterior): vídeo con **pista original en galego** y pistas
  adicionales en **portugués** (el más natural por cercanía lingüística y cultural: pt-PT y/o pt-BR), **castellano** e **inglés**.
- El plan debe estimar el nicho (c) con estas cuatro lenguas: audiencias, competencia de canales de historia/"para dormir"
  en cada idioma, coste y calidad del TTS open source en pt/es/en, traducción automática gl→pt/es/en con control de
  calidad automático, y cómo funcionan y cuentan en YouTube las pistas multi-audio (métricas consolidadas, descubrimiento).
- Riesgo a tratar: que el galego acabe siendo una pista marginal. La identidad del canal sigue siendo galega
  (título/miniatura/pista por defecto a decidir con datos) y eso encaja con la tesis pro lingua.
- Si es barato y viable, el pipeline puede añadir al vídeo de ejemplo al menos una pista extra (portugués) como prueba.

## Decisión del promotor tras la ronda 2 del vídeo (30-09-2026) — PRIORITARIO
- **Hallazgo:** con un LLM open source pequeño en CPU (EuroLLM-9B), el guion desatendido **inventa historia**
  ("a irmandade venceu") **y palabras** ("fortaleiras"). Voz, imágenes, sonido y montaje sí dan el pego.
- **Decisión:** el **guion lo escribe un LLM potente por API** (coste de céntimos por episodio); voz (Nós StyleTTS2),
  imágenes, montaje y controles siguen siendo open source y locales. Se mantienen los controles automáticos
  (veracidad contra el dossier, LanguageTool, ASR) como red de seguridad.
- **El vídeo se cierra en la ronda 3**: después se integra el plan v2 y pasa al tribunal. El plan v2 debe recoger este
  hallazgo (por qué el LLM local no basta hoy en galego, coste por episodio con API, y qué aportaría a Nós/la comunidad
  un modelo open source mejor en galego).
