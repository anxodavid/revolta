# Pieza del business plan: OPERACIONES — pipeline de producción agéntico, costes y tiempos

Versión 5 (constructor, ronda 5) · 29-09-2026 · Redactado en castellano. Todo lo que se dirige al público (guion, voz, metadatos) va en galego normativo (RAG).

**Cambios de la v5**
- **Nuevo §4.1.1: dónde corre el cómputo de voz y cómo habla con el orquestador local.** La v4 ponía TTS, ASR y GEC "en Colab T4" sin explicar cómo los llamaba un `Makefile`. Ahora hay:
  - una **decisión explícita** entre (a) Colab como *worker*, (b) CPU local y (c) Runpod por horas, con pros y contras;
  - **(a) queda descartada**: la FAQ de Colab prohíbe, en la versión gratuita, los *workers* y el uso fuera de la interfaz del cuaderno [F];
  - **(b) es la opción por defecto** y (c) el plan B, con el mismo código.
- **Medida propia en CPU** [P] (4 vCPU, sin GPU) con el modelo real de Nós (Brais) sobre las 1.263 palabras del guion muestra:
  - **TTS con RTF 0,28**, arranque en frío de 27,6 s y 3,65 GB de RAM;
  - **Whisper-gl int8 con RTF 0,75 por frase**;
  - un hallazgo que cambia el QA: **pasado sobre el audio entero, Whisper alucina** (WER 48-53 %), mientras que **frase a frase la mediana es 0 %**. Por eso el ASR va por párrafo y la hipótesis se normaliza con Cotovía (§3.2);
  - también atrapó 2-3 fallos reales del TTS (un tartamudeo).
- **Protocolo de la cola `jobs/`** (§4.1.1 c):
  - formato del trabajo y `job_id` por hash de su contenido (idempotente);
  - `rename` atómico con latido;
  - reanudación tras un corte;
  - espera por *polling* con plazo;
  - las vueltas automáticas se resuelven dentro de la misma sesión.
- **Tiempo humano por sesión de cómputo** llevado al §6 (0,1-0,2 h por episodio en (b); 0,25-0,4 h en (c)).
- **Prueba B0** (§4.1.1 e): 10 min de audio en la CPU del promotor y en T4 **antes de G0**, con reglas de decisión.
- **Coste de (c) por episodio con las vueltas incluidas**: ~0,6-0,8 USD, con el volumen de red.
- **MVP**: nuevo bloque 11 (*worker* + cola + B0, 4 h). Pasa de 28,5 a **32,5 h en (b) / 35,5 h en (c)**, y el primer episodio se mueve a la **semana 10-12** (§9, §9.1).
- Caja de la Etapa 1 recalculada sin Colab Pro: **~18-24 €/mes**.

**Cambios de la v4**
- **El LLM ya no copia la cita: la extrae una herramienta** (§3.6.1-§3.6.2). En la v3 el investigador "copiaba" 15-40 palabras del `.txt`, y un LLM no reproduce literalmente un fragmento largo: corrige erratas de OCR, moderniza la ortografía preestándar, normaliza comillas y guiones, se salta o reordena palabras. Con 150-250 afirmaciones por episodio eso habría producido bloqueos falsos de H2 no presupuestados. Ahora:
  - el investigador solo propone un **ancla aproximada**;
  - `extrae_cita.py` la localiza en `fontes/<id>.txt` (distancia de edición con rapidfuzz, prefiltro de palabras raras y, en fuentes largas, FTS5 `NEAR` para elegir páginas candidatas), devuelve los desplazamientos `[ini, fin)` y **escribe la columna `cita` con el texto exacto de la fuente**, cortado en límites de palabra;
  - R3 comprueba el hash de la fuente, los desplazamientos y que `texto[ini:fin] == cita`;
  - si el ancla del LLM se aleja del texto real (distancia > 0,08, o cambia una cifra o una palabra de matiz), la afirmación **va al estrato A con el diff a la vista**; si se aleja mucho (> 0,20), se bloquea como `CITA_INVENTADA`.
- **Prototipo probado** [P] (`drafts/extrae_cita_prototipo.py` + `drafts/proba_extrae_cita.py`): **0 bloqueos falsos en 480 copias ruidosas** (fuente limpia, con OCR sucio al 2 % y al 5 %, y en ortografía preestándar simulada); ancla en el sitio correcto en 120 de 120; y **145 de 145 falsificaciones** bloqueadas o enviadas al estrato A con la diferencia señalada (§3.6.2).
- **G2 mide la tasa de bloqueos falsos con afirmaciones del LLM real** (≤ 2 %, sobre ≥ 100 afirmaciones), y cada episodio registra sus rebloqueos en `metricas_verificacion.csv` (§3.6.5). El tiempo humano de escalado y las filas extra del estrato A ya están en el §6.
- **Erratas corregidas** en la lectura del código de Nós: la firma de `LFinference` trae `beta=0.9` (el 0,7 es el del config y de `main`), y `main` **ya fija** `cudnn.deterministic = True` y `cudnn.benchmark = False` (§3.5.1, §3.5.4).
- MVP: el bloque 2-3 sube 2 h (26,5 → 28,5 h, dentro del margen de 20-30 h de la v4; la v5 lo lleva a 32,5-35,5 h).

**Cambios de la v3**
- **Nuevo §3.6: control determinista de la veracidad histórica**, al mismo nivel que el de pronunciación. Tiene cuatro piezas:
  - cada afirmación lleva una **cita literal de 15-40 palabras con localizador**, y `qa.py` la busca en `fontes/` con SQLite FTS5; si no la encuentra, la marca como `CITA_INVENTADA` y bloquea H2 (**sustituido en la v4**: la cita ya no la copia el LLM, la extrae `extrae_cita.py`);
  - un **juez de otra familia** (Gemini, frente al redactor Claude) decide si la cita respalda la frase;
  - una **muestra humana estratificada por riesgo** con umbral de revisión completa;
  - una **prueba adversarial en G2** y **canarios en cada ejecución**.
- Hay **prototipo probado** [P]: 5 de 5 citas falsas atrapadas, 5 de 5 citas reales aceptadas, más un error de localizador y una cifra sin respaldo detectados.
- **Estilo por frontera de párrafo** (`s_prev` guardado; §3.5.4): regenerar un párrafo ya no cambia los siguientes.
- **Versión de Cotovía fijada** (§3.5.9). Se ha comprobado [P] que el `/usr/bin/cotovia` 0.5 de 2013 **da otra salida** que el compilado desde el repositorio de Nós, y que `phonemize.py` llama a `cotovia` por el `PATH`.
- **MVP explícito de 20-30 h** (§9.1). Los controles de similitud, CLIP, ECAPA, NFA, detector de caras, *hash* perceptual, CarvalhoChat_GEC y Wikidata pasan a una fase posterior con fecha.
- **Precios con fuente oficial**: Colab, Runpod y Gemini (en la v5, Colab ya no se usa como *worker*, §4.1.1). **Imagen 4 Fast se apagó en la API de Gemini el 17-08-2026** [F] https://ai.google.dev/gemini-api/docs/deprecations, así que se sustituye por Nano Banana 2 Lite.

**Leyenda de evidencia**
- **[F]**: dato con fuente (URL al lado). Precios consultados el 29-09-2026 salvo que se indique.
- **[R]**: tomado de los informes de investigación previos (`research/*.md`), que a su vez citan la fuente.
- **[S]**: supuesto o decisión de diseño propia; hay que medirlo en el piloto.
- **[P]**: prueba propia ejecutada el 29-09-2026. Incluye Cotovía compilado desde `Utils/cotovia` del repositorio de Nós, el prototipo de `g2p_override.py` (`drafts/g2p_override_prototipo.py`), el de `verifica_citas.py` (`drafts/verifica_citas_prototipo.py`) y el de `extrae_cita.py` con su batería (`drafts/extrae_cita_prototipo.py`, `drafts/proba_extrae_cita.py`). Son reproducibles y los resultados literales están en los §3.5 y §3.6.
- Tipo de cambio de trabajo: **1 USD = 0,87 €** [S]. Los precios de API se dan en USD, como los publica el proveedor.

Coherencia con otras piezas: se usan los parámetros de producto de `drafts/formato.md` (Etapa 1: 75 min narrados + 20-30 min de ambiente; Etapa 2: 2 h; 110-125 palabras/min; ~8.600 y ~13.800 palabras) y los presupuestos de caja de `drafts/retornos.md` (modelo de 35 €/mes en la Etapa 1 y 110 €/mes en la Etapa 2).

---

## 0. Resumen en 10 líneas

1. **El coste de la IA es casi irrelevante; el coste real son las horas humanas de galego.** Un episodio de 2 h cuesta entre **~4 y ~16 USD en IA** según el stack (§5), frente a **6,8-7,8 h de revisión humana** (§6).
2. **Diez agentes, tres puertas humanas obligatorias**: aprobación de la escaleta, lectura íntegra del guion y escucha dirigida del audio. Ninguna pieza sale a YouTube sin firma humana registrada (§2, §3).
3. **Etapa 1 = Claude Code + Python, sin frameworks**. Los "agentes" son subagentes de Claude Code (`.claude/agents/*.md`) que llaman a scripts Python deterministas. Voz con Proxecto Nós (0 €) **en la CPU del propio ordenador** (RTF 0,28 medido [P]; Runpod por horas como plan B con el mismo código, §4.1.1), imágenes con Nano Banana 2 Lite en *batch*, juez factual con Gemini, montaje con FFmpeg y subida manual. **Caja: ~18-24 €/mes** (§4.1, §5.3).
4. **Etapa 2 = el mismo grafo, pero desatendido**: LangGraph (o el Agent SDK de Claude) con la API y *batch*, GPU alquilada por horas y revisor lingüístico externo por muestreo. **Caja: ~95-130 €/mes** con 4 episodios de 2 h (§4.2).
5. **Etapa 3** añade una voz de locutor galego licenciada y pistas es/pt. Es la única etapa en la que la IA deja de ser la partida pequeña (licencia de 2.000-6.000 €) (§4.3).
6. **El auditor QA es un bucle con umbrales numéricos**, no una opinión. Los principales: castelanismos = 0; **anclas de cita sin correspondencia en la fuente = 0** (la cita la extrae una herramienta, no el LLM); error de retrotranscripción del audio (WER) ≤ 6 % por bloque; −16 LUFS ±1; luminancia 40-70. Tiene un máximo de 3 vueltas por etapa; después, escala al humano (§3).
   **La veracidad se comprueba igual que la pronunciación: con máquina y no con fe** (§3.6). El LLM investigador **no copia** la cita: propone un ancla y una herramienta extrae el fragmento exacto de la fuente con sus desplazamientos. Si el ancla no se parece a nada de la fuente, bloquea; si se parece pero cambia algo (una cifra, un *posiblemente*), va a revisión humana con el cambio resaltado. Un LLM **de otra familia** juzga si la cita real respalda la frase. El humano revisa **el 100 % de fechas, cifras, causas y atribuciones** y una muestra aleatoria del resto; si la muestra falla, revisa todo. La puerta G2 exige que **ninguna cita falsa plantada pase sin bloqueo o sin ir al estrato A**, y **≤ 2 % de bloqueos falsos** con afirmaciones del LLM real.
7. **La pronunciación se corrige de verdad, no con buenas intenciones.** StyleTTS2-GL fonemiza siempre con Cotovía y no acepta léxico ni velocidad. Por eso el plan incluye un **wrapper `g2p_override.py`** que sustituye la transcripción de Cotovía palabra a palabra con el léxico del canal (con reglas por contexto para homógrafos como *o corte / a corte*), y un **parche de ~10 líneas en `LFinference`** que escala las duraciones predichas y añade pausas por puntuación. El "mosaico de risco" (2-4 min con solo las palabras de riesgo) se corta con **los tiempos que da el propio TTS**, sin depender del ASR, y cada palabra marcada en él entra en ese léxico (§3.3, §3.5).
8. **Cadencia sostenible**: Etapa 1, **2 episodios/mes** (~5,8-6,9 h humanas por episodio, que caben en 4 h/semana). Etapa 2, **3-4 episodios/mes de 2 h** (6-10 h/semana). No se recomienda la cadencia diaria (§7).
9. **Anti-"slop"**: 12 controles que se corresponden con el texto literal de la política de YouTube de *inauthentic content* (actualizada el 16-jul-2026), y un expediente de evidencias por episodio que sirve a la vez para una apelación y para la excepción del artículo 50 del AI Act (§8).
10. **Puesta en marcha con un MVP de ~32,5 h** de construcción [S] (35,5 h si hace falta Runpod; §9.1), incluida la integración del cómputo de voz y la prueba B0, más ~6-8 h de escucha y juicio de G0 y G1. Incluye lo innegociable: galego, veracidad con citas y pronunciación. Lo demás (similitud, CLIP, ECAPA, NFA…) va a una fase posterior de 12-20 h, entre los episodios 2 y 6. Primer episodio publicable entre la **semana 10 y la 12** (§9). La **puerta G0** exige que la corrección de pronunciación se oiga de verdad en una prueba ciega de 50 palabras de riesgo (§3.5.8).

---

## 1. Principios de diseño

1. **Galego primero, siempre.** Cada etapa que produce texto o voz tiene una comprobación automática específica del galego y una humana. El guion se escribe **directamente en galego**, no se traduce del castellano, para evitar el calco [R `voz_guion.md` §2.1].
2. **Determinista donde se pueda y LLM donde haga falta.** Ortografía, loudness, luminancia, ritmo y WER los miden scripts. Los LLM redactan, critican y proponen, pero no se autoaprueban.
3. **Agente redactor ≠ agente revisor.** El lingüista usa otro modelo u otra configuración (otro *system prompt*, sin ver el razonamiento del redactor), para no heredar sus sesgos [R `voz_guion.md` §2.1]. El juez de respaldo factual va más allá: es **de otra familia** (Gemini frente a Claude), porque dos modelos de la misma familia tienden a dar por buena la misma paráfrasis errónea [S] (§3.6.3).
4. **Todo es un fichero en git.** Cada episodio es una carpeta con su expediente: fuentes, escaleta, versiones del guion, informes QA y firmas humanas. Esto da trazabilidad para el control de calidad, las apelaciones a YouTube y el cumplimiento del AI Act.
5. **Barato por defecto, caro solo donde el A/B lo justifique.** El stack de la Etapa 1 cuesta casi 0 € en voz y montaje. Solo se paga más cuando una prueba ciega (voz o guion) demuestra que se oye la diferencia.
6. **Nada se publica solo.** Ni siquiera técnicamente: YouTube restringe a *privado* los vídeos subidos por API desde proyectos no verificados creados después del 28-07-2020 [F] https://developers.google.com/youtube/v3/docs/videos/insert. En la Etapa 1 la subida es manual. Es una puerta humana más, no un inconveniente.

---

## 2. El pipeline: agentes, entradas, salidas y quién decide

### 2.1 Vista general

```
[0 Humano: tema + ángulo]
        │
 1 INVESTIGADOR (RAG fuentes galegas) ──► dossier + fontes/ (instantáneas) + afirmacions.csv (ANCLA propuesta + localizador)
        │
 1b extrae_cita.py (determinista) ──► cita EXACTA de la fuente + [ini, fin) + distancia al ancla
        │
 2 ESCALETA (guionista, modo plan) ──► [PUERTA H1: humano aprueba escaleta]
        │
 3 GUIONISTA (capítulo a capítulo, en galego; solo cita ids de afirmacions.csv) ──► borrador v1
        │
 4 LINGÜISTA GALEGO (LLM distinto + Hunspell + LanguageTool + lista negra; GEC tras el MVP)
        │
 5 VERIFICADOR HISTÓRICO
     5a verifica_citas.py (hash + [ini, fin) + texto exacto; FTS5 en el localizador; cifras de la frase ⊂ cita) ── determinista
     5b XUÍZ de otra familia (Gemini): ¿la cita respalda la frase? si / parcial / non
        │            ▲
        └─ AUDITOR QA (texto, con 5 canarios por ejecución) ── falla → vuelve a 1/3/4/5 (máx. 3 vueltas)
        │
   [PUERTA H2: revisión estratificada de afirmacións + lectura humana íntegra + firma do guion]
        │
 6 DIRECTOR / PROMPTS VISUALES (biblia visual "noite atlántica") ──► lista de planos
 7 GENERADOR DE IMÁGENES ──► imágenes + hoja de contacto
 8 TTS (voz ganadora del A/B) + posproducción de audio
        │
   AUDITOR QA (audio + imagen) ── falla → vuelve a 7/8 (por bloque)
        │
   [PUERTA H3: escucha dirigida (mosaico de risco) + hoja de contacto]
        │
 9 MONTAJE (FFmpeg) ──► máster vídeo + máster audio (podcast)
        │
   AUDITOR QA (máster) ── falla → vuelve a 9
        │
10 PUBLICACIÓN (metadatos, capítulos, bibliografía, declaración IA) ──► [PUERTA H4: subida y publicación manual]
```

### 2.2 Ficha de cada agente

| # | Agente | Entrada | Salida (fichero) | Qué hace la IA | Qué hace el humano |
|---|---|---|---|---|---|
| 0 | — | Idea | `brief.md` (tema, ángulo, periodo, 3 escenas ancla, temas a evitar) | Propone 3 ángulos a partir del catálogo de `formato.md` §8 | **Elige** el tema y el ángulo (15-20 min) |
| 1 | **Investigador** | `brief.md` + corpus | `dossier.md`; `fontes/*.txt` (**instantánea del texto**, con `revid` de Galipedia o hash del PDF); `fontes.yaml` (id, URL, revisión, licencia, fiabilidad); `afirmacions.csv` (id, tipo de riesgo, afirmación, id de fuente, localizador, **ancla propuesta** de 15-40 palabras; las columnas `ini`, `fin`, `cita`, `dist` y `estado_ancla` las escribe `extrae_cita.py`, §3.6.1) | Busca en Galipedia/Wikidata (API, con *user-agent* propio y ritmo lento: Wikimedia corta las ráfagas [P]), en textos de dominio público de Galiciana y en artículos académicos en abierto. Resume y extrae afirmaciones **con un ancla** que apunta al pasaje. **No escribe la cita**: la extrae la herramienta. Si el ancla no se encuentra, recibe los 3 pasajes más parecidos y elige uno o retira la afirmación | Añade o veta fuentes (15 min). La revisión de afirmaciones se hace en H2 (§3.6.4) |
| 2 | **Guionista (escaleta)** | dossier | `escaleta.md` (8-16 capítulos, curva de tensión decreciente, escena de apertura) | Diseña la estructura según `formato.md` §4 | **PUERTA H1**: aprueba o corrige (15-20 min) |
| 3 | **Guionista (redacción)** | escaleta + dossier + guía de estilo + párrafos modelo validados por nativos (*few-shot*) | `guion_v1.md`, con una marca `⟦a:037⟧` por afirmación (invisible para la voz) y `⟦amb⟧` en las frases de pura ambientación | Redacta en galego capítulo a capítulo (1.000-1.200 palabras), con un resumen del capítulo anterior como memoria. **Solo puede usar hechos que ya tengan id** en `afirmacions.csv`; si necesita uno nuevo, se lo pide al investigador, que debe traerlo con su cita | — |
| 4 | **Lingüista galego** | guion | `guion_v2.md` + `informe_lingua.md` (cada cambio justificado) | (a) Deterministas: Hunspell-gl, LanguageTool-gl y lista negra de castelanismos. (b) CarvalhoChat_GEC (LoRA de Nós) frase a frase, tras el MVP (§9.1). (c) Un LLM **distinto** del redactor reescribe solo lo marcado y justifica cada cambio. **No puede tocar cifras, fechas ni nombres** sin volver a pasar por el paso 5 | Revisa los cambios dudosos que el agente marque como "consultar" (dentro de H2) |
| 5 | **Verificador histórico** | guion v2 + `afirmacions.csv` + `fontes/` | `verificacion.json` (por afirmación: estado determinista + veredicto del juez) + `revision_afirmacions.html` (hoja de revisión humana) | **5a** `verifica_citas.py`, determinista (§3.6.2). **5b** Juez LLM **de otra familia** que el redactor (§3.6.3). Señala anacronismos y celtismo romántico no marcado como leyenda | **Revisión estratificada** (§3.6.4) y decisión sobre los casos "parcial/non" (dentro de H2) |
| QA-T | **Auditor QA (texto)** | guion v2 + informes | `qa_texto.json` (pasa/falla por regla) | Aplica los umbrales del §3.1; si falla, devuelve el trabajo al agente responsable con el motivo | — |
| H2 | — | guion final | `firma_guion.yaml` (quién, cuándo, hash del fichero) | — | **Lectura íntegra** en voz baja por el promotor y su mujer (repartida por capítulos) y corrección final. **Nunca se omite** |
| 6 | **Director / prompts visuales** | guion firmado + biblia visual | `planos.csv` (tiempo, descripción, prompt, semilla, tipo: pintura/mapa/negro) | 1 plano cada 40-90 s, oscureciéndose hacia el final; mapas con toponimia RAG | — |
| 7 | **Generador de imágenes** | `planos.csv` | `img/*.png` + `contact_sheet.jpg` | Genera y hace auto-rechazos (texto espurio, caras realistas, luminancia fuera de rango) | Revisa la hoja de contacto y pide repetir (dentro de H3, 15-20 min) |
| 8 | **TTS + posproducción de audio** | guion firmado + `normalizado.txt` (números y siglas ya escritos con letra) + `lexico.tsv` | `voz/*.wav` por párrafo, `narracion.wav`, `tempos_palabra.json`, `g2p_log.jsonl` | Fonemización Cotovía + léxico con `g2p_override.py`; síntesis por frase con el `inference.py` **parcheado** (factor de duración y semilla por párrafo); pausas insertadas por puntuación; EQ suave; retrotranscripción con ASR galego (§3.5). Sin el parche, StyleTTS2-GL no admite ni léxico ni velocidad | **PUERTA H3**: escucha del "mosaico de risco" + los 10 primeros minutos + 3 catas aleatorias |
| QA-A | **Auditor QA (audio/imagen)** | wav + img | `qa_audio.json`, `qa_img.json` | Umbrales del §3.2-3.4; regenera los bloques que fallan (otra semilla o ajuste) | — |
| 9 | **Montaje** | narración + ambiente + imágenes + planos | `master.mp4`, `master_audio.m4a`, `capitulos.txt` | FFmpeg: Ken Burns ≤3 %, fundidos de 2-3 s, cama de ambiente −20/−26 dB, cola de ambiente, −16 LUFS | — |
| 10 | **Publicación** | todo lo anterior | `metadatos_yt.json`, descripción, miniatura | Título según la fórmula, descripción en galego con capítulos, bibliografía y nota de proceso, etiquetas es/gl, declaración de contenido sintético si procede | **PUERTA H4**: revisa los metadatos, sube por Studio, marca la declaración y publica |

### 2.3 Qué es humano y qué es IA (resumen)

| Siempre humano | Siempre IA (con control determinista) | Mixto |
|---|---|---|
| Elección de tema y ángulo | Propuesta de afirmaciones con ancla (LLM); extracción de la cita exacta y su comprobación en la fuente (`extrae_cita.py` + FTS5, deterministas) | Guion: redacta la IA; lee, corrige y firma el humano |
| Aprobación de la escaleta | Corrección ortográfica y gramatical automática | Imágenes: genera la IA; aprueba la hoja de contacto el humano |
| Lectura íntegra del guion en galego | Síntesis de voz, pausas, loudness | Audio: la IA sintetiza y audita; el humano escucha el mosaico de riesgo |
| Decisión final sobre afirmaciones dudosas | Prompts visuales, generación y montaje | Metadatos: propone la IA y edita el humano |
| Publicación y respuesta a comentarios | Retrotranscripción y cálculo de métricas QA | Erratas: detecta la comunidad o el QA; decide el humano |
| Firma y responsabilidad editorial (AI Act, art. 50) | | |

---

## 3. El auditor QA: reglas, umbrales y bucle de retorno

El auditor es un script (`qa.py`) que devuelve JSON por regla, más un LLM juez solo para las rúbricas cualitativas. **Regla de bucle** [S]: cada etapa tiene como máximo 3 vueltas automáticas. A la cuarta, se detiene y escala al humano con el informe. Esto evita bucles infinitos y gasto descontrolado.

### 3.1 Texto (antes de la puerta H2)

| Regla | Herramienta | Umbral para pasar [S] | Si falla, vuelve a |
|---|---|---|---|
| Castelanismos de la lista negra | regex + lista mantenida por el promotor (arranca con la de `voz_guion.md` §2.1) | **0** | Lingüista |
| Palabras desconocidas | Hunspell-gl [F] https://gitlab.com/trasno/hunspell-gl, con lista blanca de nombres propios | 0 sin resolver (cada una: corregida o añadida a la lista blanca con justificación) | Lingüista |
| Errores gramaticales | LanguageTool gl-ES (sin mantenedor desde 2019 [R]) + CarvalhoChat_GEC [F] https://huggingface.co/proxectonos/CarvalhoChat_GEC | Cada propuesta aceptada o rechazada con motivo | Lingüista |
| Frases factuales sin marca | regex en el guion: frases con cifras, romanos, años, conectores causales o verbos de atribución que no llevan `⟦a:…⟧` (§3.6.2, regla R1) | **0** (o marcadas `⟦amb⟧` y sin datos concretos, o reformuladas como "segundo a tradición…" con su fuente) | Guionista |
| **Ancla sin correspondencia / cita alterada** | `extrae_cita.py` (distancia de edición al texto real) + `verifica_citas.py` (hash, `[ini, fin)`, texto exacto, FTS5 en el localizador) (§3.6.2) | **0 `CITA_INVENTADA`** · 0 `FONTE_ERRADA` · 0 `LOCALIZADOR_ERRADO` · 0 `CITA_MANIPULADA`. **Bloquea H2**. `AXUSTADA`, `CIFRA_ALTERADA` y `MATIZ_ALTERADO` no bloquean: van al estrato A con el diff | Investigador (1 reintento automático con los 3 pasajes candidatos; después, humano) |
| Cifras sin respaldo | cada número o año de la frase del guion tiene que estar en la cita | **0** | Guionista / Investigador |
| Respaldo semántico | juez LLM **de otra familia** (Gemini) sobre la frase del guion y la cita con su contexto (§3.6.3) | Las respuestas "non" vuelven al guionista; las "parcial" van al estrato A de la revisión humana | Guionista |
| Autocomprobación del verificador | **5 canarios** (anclas mutadas) inyectados en cada ejecución (§3.6.5) | **5 de 5 con el estado esperado** (ninguno `ANCORADA`); si no, `qa.py` aborta | — (se arregla el verificador) |
| Fechas y nombres | Wikidata (SPARQL), tras el MVP | 0 discrepancias sin explicar | Verificador |
| Ritmo del texto | recuento de palabras | 8.000-9.200 (75 min) / 13.000-14.600 (2 h) | Guionista |
| "Sono seguro" | lista de patrones: preguntas retóricas en cadena, *cliffhangers*, segunda persona burlona, cifras de muertos, gore | 0 patrones prohibidos; conflicto solo en el primer 40 % (LLM juez + posición) | Guionista |
| Similitud con episodios anteriores (**tras el MVP**: solo tiene sentido con ≥ 3 episodios) | *embeddings* locales (modelo multilingüe abierto) + n-gramas de 8 palabras | Coseno < 0,85 con cualquier guion previo; < 2 % de 8-gramas compartidos fuera de la fórmula de bienvenida | Guionista (anti-slop §8) |
| Rúbrica de calidad | LLM juez (modelo distinto al redactor) con los ejemplos de `refs/` | ≥ 4/5 en especificidad, imágenes concretas y ausencia de clichés IA | Guionista |

### 3.2 Audio (antes de la puerta H3)

| Regla | Herramienta | Umbral [S] | Si falla |
|---|---|---|---|
| Fidelidad (sin palabras comidas, repetidas ni alucinadas) | Retrotranscripción con `proxectonos/whisper-large-v3-turbo-gl-v1.0` [F] https://huggingface.co/proxectonos/whisper-large-v3-turbo-gl-v1.0 (alternativa: `stt_gl_conformer_ctc_large_v1.0`) y WER por párrafo contra el guion. **Siempre por párrafo y con `condition_on_previous_text=False`, nunca sobre el audio entero**: pasado de una vez, Whisper alucinó un tramo y dio un WER del 48-53 % sobre un audio correcto [P, §4.1.1 a]. **La hipótesis se normaliza con Cotovía** (números con letra) antes de comparar, porque el ASR escribe *1467* | WER ≤ 6 % por párrafo (en la medida propia, frase a frase: mediana 0 %, y 6 de las 15 frases por encima del 6 % eran solo números; umbral a calibrar en G0) | Se regenera el párrafo con **otra semilla** (el `inference.py` original fija `torch.manual_seed(0)`, así que la semilla por párrafo es parte del parche del §3.5) o con otro `alpha`/`beta`/`t`/`diffusion_steps`, que son los únicos parámetros que expone el script; tras 3 intentos, se marca para escucha humana |
| Pronunciación controlada | `g2p_log.jsonl` (cada sustitución del léxico) + comprobación de que ningún token de entrada es `X` (desconocido) | 100 % de las entradas del léxico presentes en el guion aplicadas; 0 tokens `X` | Corregir `lexico.tsv` (el wrapper aborta si un fonema no existe en el inventario) |
| Ritmo | palabras ÷ duración narrada (pausas incluidas), por párrafo y global | 110-125 palabras/min | Se ajustan **el factor de duración `speed` y el presupuesto de pausas** del §3.5.4. StyleTTS2-GL **no tiene `length_scale`** (eso es de VITS/Matcha): el control existe solo con el parche. Estirar con `atempo` en posproducción es el plan B, y el A/B de G0 decide. **Nunca se toca el texto** (`formato.md` §3) |
| Silencios anómalos o *glitches* | `ffmpeg silencedetect` + detección de picos | Sin silencios > 4 s dentro de un párrafo; sin clics | Regenerar el párrafo |
| Loudness | `ffmpeg -af ebur128` / `loudnorm` | −16 LUFS integrados ±1; *true peak* ≤ −1,5 dBTP | Renormalizar |
| Continuidad de estilo en la frontera | distancia entre el estilo de salida del párrafo regenerado y el `s_prev` guardado para el siguiente (§3.5.4) | Coseno ≥ umbral calibrado en G0 | Otra semilla (máx. 3) |
| Continuidad de timbre (**tras el MVP**) | *embedding* de hablante (p. ej. ECAPA de SpeechBrain) entre párrafos | Distancia < umbral calibrado en el piloto | Regenerar el párrafo |

### 3.3 El "mosaico de risco" (la escucha humana más eficiente)

1. **Lista de palabras de riesgo** (automática): topónimos y antropónimos; palabras con vocal media tónica que la ortografía no distingue (e/o abierta o cerrada) y que están en la lista de homógrafos del léxico; palabras para las que Cotovía devuelve **más de una variante** (el script original se queda con la primera, §3.5.1); palabras **sin transcripción** (Cotovía devuelve la grafía tal cual); latinismos; y palabras que el ASR transcribió distinto al guion.
2. **Corte de cada palabra con 1 s de contexto.** Los tiempos salen, por orden de preferencia: (a) **del propio TTS**, porque el parche del §3.5 devuelve la duración predicha de cada fonema y se sabe dónde cae cada espacio entre palabras y cada pausa insertada. Son los tiempos exactos con los que se generó el audio y no dependen del ASR; (b) si (a) no está disponible (otra voz; se construye tras el MVP y solo en ese caso), **alineación forzada CTC** del texto con el conformer galego de Nós mediante NeMo Forced Aligner (el modelo está etiquetado `forced-alignment` y NFA trabaja con audios de más de 1 h) [F] https://huggingface.co/proxectonos/stt_gl_conformer_ctc_large_v1.0 · https://github.com/NVIDIA/NeMo/tree/main/tools/nemo_forced_aligner; (c) como último recurso, las marcas por palabra de Whisper. El Whisper galego trae las `alignment_heads` del modelo base [P: `generation_config.json`], pero tras el ajuste fino no está garantizado que sigan alineando bien, así que **no es la fuente principal**. En G0 se comprueba que (a) o (b) cae a ±80 ms de 20 palabras marcadas a mano [S].
3. El humano escucha el mosaico con la lista delante y marca las que suenan mal. Cada marca se resuelve consultando el *Dicionario de pronuncia da lingua galega* (ILG/RAG), que incluye topónimos [R] https://ilg.usc.es/pronuncia/ (consulta manual, sin scraping), y se convierte en **una línea de `lexico.tsv`** con los fonemas en el alfabeto interno del modelo (§3.5.1, §3.5.3). Esa línea se aplica en la siguiente síntesis a través de `g2p_override.py`. **No hay respelling**: la ortografía no marca la apertura de é/ó, así que reescribir la palabra no puede corregirla.
4. **Cierre del bucle**: tras añadir entradas, se regeneran solo los párrafos afectados y el mosaico de esas palabras se vuelve a escuchar (ABX: antes y después). La palabra no se da por corregida hasta que el humano confirma que se oye la diferencia.
5. Efecto esperado [S]: el léxico crece con cada episodio y el mosaico se acorta. Es el activo que hace que la voz "suene a Galicia" episodio tras episodio.

### 3.4 Imagen y máster

| Regla | Herramienta | Umbral [S] |
|---|---|---|
| Luminancia media por plano | `ffmpeg signalstats` / Pillow | 40-70/255 (último tercio < 20) (`formato.md` §7) |
| Texto espurio en imágenes (letras inventadas) | OCR Tesseract (tiene modelo `glg`) | 0 caracteres detectados, salvo en los mapas |
| Caras fotorrealistas | MVP: *prompt* negativo + hoja de contacto humana. Tras el MVP: detector de caras (OpenCV/MediaPipe) + clasificador de estilo | 0 caras realistas en primer plano (evita la obligación de etiqueta y el *uncanny*) |
| Coherencia de estilo (**tras el MVP**; mientras tanto, la hoja de contacto) | similitud CLIP con 5 imágenes de referencia de la biblia visual | ≥ umbral calibrado |
| Reutilización de imágenes de otros episodios (**tras el MVP**: hacen falta episodios previos) | *hash* perceptual | ≤ 10 % (anti-slop) |
| Máster | `ffprobe` | Duración esperada ±2 %, sin *frames* negros no previstos, capítulos coherentes con el guion |

### 3.5 Control de pronunciación y ritmo con la voz por defecto (StyleTTS2-GL de Nós): diseño implementable

La calidad de la narración en galego es innegociable, así que esta es la pieza técnica que más importa del pipeline. Se ha diseñado **sobre el código real** del modelo, no sobre parámetros supuestos.

#### 3.5.1 Qué hace hoy el código de Nós (y por qué no basta)

Leído el 29-09-2026 en https://huggingface.co/proxectonos/Nos_StyleTTS2-Brais-GL (`inference.py`, `Utils/ASR/AuxiliaryASR/phonemize.py`, `text_utils_gal.py`, `phoneme_token_maps.json`; Celtia comparte la misma estructura) [F]:

| Hecho del código | Consecuencia |
|---|---|
| `LFinference` fonemiza **siempre** con `clean_output(run_cotovia_with_phrase(text))`, que llama a `cotovia -n -S -A0` | No hay punto de entrada para fonemas ni léxico de usuario |
| Cotovía devuelve **una línea por palabra**: columna 1 = palabra (ya normalizada: minúsculas, números escritos con letra, *ao* → *ó*), columna 2 = una o varias variantes de transcripción. El script **se queda con la primera** | Ni se ve ni se puede elegir la variante; los homógrafos quedan a merced del etiquetador de Cotovía |
| `clean_output` pasa la tilde de Cotovía (`^`) a vocal acentuada, quita los guiones silábicos y convierte dígrafos (`rr`→`R`, `ll`→`Z`, `nh`→`N`, `ch`→`C`, `tS`→`W`) | El alfabeto interno es de **un carácter por fonema** |
| El inventario **sí distingue** e/o abiertas y cerradas, átonas (`E`/`e`, `O`/`o`) y tónicas (`É`/`é`, `Ó`/`ó`) | Un léxico en ese alfabeto **puede** fijar la apertura, cosa que el respelling ortográfico no puede |
| `TextCleanerGal` recorre la cadena **carácter a carácter** y cambia cualquier símbolo desconocido por `X` **sin avisar** | Un léxico mal escrito fallaría en silencio: hace falta validación |
| `LFinference` solo expone `alpha`, `beta`, `t`, `diffusion_steps` y `embedding_scale`. **Ojo, hay dos juegos de valores por defecto**: la firma de la función trae `alpha=0.3, beta=0.9, t=0.7, diffusion_steps=5, embedding_scale=1` (línea 67), mientras que `main` los lee de `inference_config.yml` (`alpha 0.3`, `beta 0.7`, `t 0`, 5, 1; con `config.get('beta', 0.7)` como respaldo, líneas 206-215). `sintetiza.py` llama a `LFinference` directamente, sin pasar por `main`, así que **pasa siempre los cinco valores explícitos** para no heredar los de la firma sin querer. **No hay `length_scale` ni velocidad**; la duración sale de `pred_dur = round(sigmoid(duration).sum())` | El ritmo de 110-125 palabras/min no se puede fijar sin tocar el código |
| `main` fija `torch.manual_seed(0)`, `torch.backends.cudnn.benchmark = False` y `torch.backends.cudnn.deterministic = True` (líneas 130-132), trocea el texto por `. : ? !` y **concatena las frases sin silencio** entre ellas | Hay una semilla global, pero no una por párrafo para "regenerar", ni pausas controladas. Los ajustes de cuDNN están en `main`: si `sintetiza.py` no pasa por `main`, tiene que copiarlos |

Todo lo anterior se resuelve con **un wrapper y un parche pequeño** sobre una copia del script (licencia Apache-2.0, que permite modificarlo). El parche se guarda como `patches/styletts2_gl.patch`, para poder reaplicarlo si Nós actualiza el repositorio.

#### 3.5.2 Lo que Cotovía acierta y lo que falla: prueba propia [P]

Se compiló Cotovía desde `Utils/cotovia` del mismo repositorio (CMake; la compilación tarda unos minutos y pide `flex`, `libfl-dev`, `libexpat1-dev` y `libasound2-dev`), se ejecutó con `-D` apuntando al `data/` de ese mismo repositorio y se pasaron frases de riesgo. **Con otro binario los resultados cambian** (§3.5.9). Salida tras `clean_output` (1.ª variante):

| Frase | Cotovía | Valoración |
|---|---|---|
| *eu **porto** a pedra* / *ao **porto** de Betanzos* | `pÓrto` / `pórto` | ✔ Desambigua verbo y nombre por categoría gramatical |
| ***o corte** da espada* | `kÓrte` | ✔ abierta |
| ***a corte** de Castela* | `kÓrte` | ✘ Debería ser cerrada, la misma que en *o porto* [S: confirmar en el *Dicionario de pronuncia*]. **Homógrafo que falla** |
| *Brigantium* | `BriGantíwm` | ✘ Acento en *-ti-* en lugar de *-gan-* |
| *Betanzos* | `BetáNTos` (2.ª variante: `BetánTos`) | ? La 1.ª variante lleva nasal velar ante /θ/. Lo deciden los jueces |
| *século XII* | "décimo segundo" | ✘ Normalización: en galego se lee "século doce" [S: confirmar con la norma]. Se corrige **antes** de Cotovía (§3.5.5) |
| *1120* | "mil cento vinte" | ✔ |
| *Xelmírez*, *Mondoñedo*, *Oseira*, *Castelao* | `SelmíreT`, `mondoJéDo`, `oséjra`, `kasteláo` | ✔ (a confirmar de oído) |

Lectura: Cotovía es buena base (acierta muchos casos gracias al etiquetado gramatical), pero **falla en homógrafos que dependen del significado, en latinismos y en algunas normalizaciones**. Son justo las palabras que más aparecen en historia de Galicia. De ahí el léxico.

#### 3.5.3 `g2p_override.py`: el léxico conectado de verdad con la voz

**Formato de `lexico.tsv`** (en git; una línea por regla):

```
# palabra (forma de la col. 1 de Cotovía)  fonemas (alfabeto interno)  contexto: regex sobre la palabra anterior  fuente
corte	kórte	^(a|da|na|á|pola|coa)$	Dicionario de pronuncia (consulta 2026-10-xx)
brigantium	BriGántjum		acento latino en -gan-
betanzos	#2		usar la 2.ª variante de Cotovía (decisión G0)
```

**Algoritmo** (sustituye a una sola línea de `LFinference`: `ps = fonemizar(text, LEXICO, INV, REXISTRO)`):

1. Llama a Cotovía con **los mismos parámetros** (`-n -S -A0`) y recorre sus líneas: palabra (col. 1) y variantes (col. 2).
2. Si la palabra está en el léxico: primero se prueban las reglas **con contexto** (regex sobre la palabra anterior, que cubre artículos y contracciones: *o corte / a corte*) y después la regla por defecto. `#n` elige la variante *n* de Cotovía.
3. Si no está: primera variante, **igual que el original**. Si Cotovía no da transcripción, se emite la grafía como hace el original, pero se registra como `sen_transcricion` y la palabra entra automáticamente en el mosaico.
4. **Validación dura**: cada carácter de los fonemas del léxico tiene que existir en `phoneme_token_maps.json` y no puede ser `X`. Si no, **aborta** con el nombre de la palabra. Así se evita el fallo silencioso de `TextCleanerGal`.
5. Cada sustitución se escribe en `g2p_log.jsonl` (palabra, transcripción de Cotovía, transcripción aplicada, párrafo). El QA de audio (§3.2) comprueba que todas las entradas del léxico que aparecen en el guion se han aplicado.
6. **Anotación en línea para los casos que el contexto no resuelve**: en `normalizado.txt` (el texto que va al TTS, no a los subtítulos), el lingüista puede escribir `{{sede|sÉDe}}`. El wrapper quita la marca antes de llamar a Cotovía, guarda el índice de la palabra y, a la salida, **comprueba que la col. 1 en ese índice es la misma palabra** antes de sustituir. Si no coincide, aborta. Como los números ya llegan escritos con letra (§3.5.5), la correspondencia palabra a palabra es 1:1.

**Resultado del prototipo** [P] (script de ~90 líneas en `drafts/g2p_override_prototipo.py`, que reutiliza `clean_output` de Nós):
- **Regresión**: con el léxico vacío, la salida es **idéntica carácter a carácter** a la del código original en las 6 frases de prueba. El wrapper no cambia nada que no deba cambiar.
- Con el léxico de arriba: *a corte* pasa de `kÓrte` a `kórte` y ***o corte* se queda en `kÓrte`** (la regla de contexto funciona). *Brigantium* pasa de `BriGantíwm` a `BriGántjum`.
- Un léxico con un símbolo inexistente (`Q`) o con `X` **se rechaza** con error explícito.
- Coste: una llamada a Cotovía tarda ~40 ms por frase [P]. Es despreciable frente a la síntesis.

Núcleo del código (resumido):

```python
def fonemizar(frase, lexico, inv, rexistro):
    toks, prev = [], ""
    for col1, variantes in cotovia_lineas(frase):          # cotovia -n -S -A0, línea a línea
        if es_puntuacion(col1): toks.extend(col1); continue
        fon = next((f for ctx, f in lexico.get(col1.lower(), [])
                    if ctx is None or ctx.search(prev)), None)  # reglas con contexto primero
        if fon is not None:
            if fon.startswith("#"): fon = clean_output(variantes[int(fon[1:]) - 1])
            validar(fon, inv)                                # aborta si hay símbolo ajeno o "X"
            rexistro.append({"palabra": col1, "cotovia": variantes[:1], "lexico": fon})
        else:
            fon = clean_output(variantes[0]) if variantes else col1   # = comportamiento original
        toks.append(fon); prev = col1.lower()
    return unir_con_puntuacion(toks)                         # mismo espaciado que run_cotovia_with_phrase
```

**¿Por qué no editar los diccionarios de Cotovía?** Se ha comprobado [P] que `nomes.txt` y `principal.txt` (`data/lang/gl/`) son **diccionarios morfológicos**: `porto,SCMS,V` o `corte,SCAS,V` guardan la categoría, el género y el número, **no la pronunciación**. Añadir una entrada solo cambia el análisis gramatical, que influye en la tilde y la apertura de forma indirecta y poco predecible. `variantes.txt` contiene reglas regex que generan las variantes alternativas. Conclusión: los diccionarios solo se tocan para dar categoría a palabras desconocidas (p. ej. un antropónimo suevo), y **la corrección fonética va siempre por el wrapper**. Así la copia de Cotovía queda intacta y se puede actualizar.

#### 3.5.4 Ritmo: factor de duración + pausas (el parche de `LFinference`)

```python
def LFinference(text, s_prev, ref_s, ..., speed=1.0, seed=None):
    if seed is not None: torch.manual_seed(seed)                 # semilla por párrafo; s_prev llega de estado/p{k}.pt
    ps = fonemizar(text, LEXICO, INV, REXISTRO)                   # §3.5.3
    ...
    duration = torch.sigmoid(duration).sum(axis=-1) / speed       # speed < 1 → más lento
    pred_dur = torch.round(duration.squeeze()).clamp(min=1)
    ...
    return wav, s_pred, pred_dur.cpu().numpy(), ps                 # duraciones → tiempos por palabra (§3.5.6)
```

Es la misma técnica que usa Kokoro, un TTS derivado de StyleTTS2: `duration = torch.sigmoid(duration).sum(axis=-1) / speed` [F] https://github.com/hexgrad/kokoro/blob/main/kokoro/model.py.

**Estilo guardado en cada frontera de párrafo (para que regenerar uno no cambie los siguientes).** Hay dos cosas en el código de Nós que encadenan una frase con la siguiente [F, `inference.py`]:

- **El estilo.** `s_pred = t * s_prev + (1 - t) * s_pred` es una combinación convexa con el estilo de la frase anterior. El `inference_config.yml` trae `t: 0`, lo que la desactiva; la firma de `LFinference` trae `t = 0.7` por defecto (y `beta = 0.9`, frente al 0,7 del config: §3.5.1). Por eso `sintetiza.py` pasa los valores de forma explícita.
- **El generador aleatorio global.** El muestreador de difusión parte de `torch.randn(...)` y `main` fija la semilla una sola vez. Así, regenerar la frase *k* consume otro número de muestras aleatorias y **desplaza el ruido de todas las posteriores**.

Diseño (`sintetiza.py`):

1. La unidad de regeneración es el **párrafo**. Antes de sintetizar el párrafo *k* se guarda `estado/p{k}.pt` con cinco campos:
   - `s_in` (el `s_prev` que recibe, un tensor de 1×256, ~1 KB);
   - `seed_k`, derivada de forma determinista de `(episodio, k, intento)`;
   - `speed`;
   - la escala de pausas `k_p`;
   - el `ref_s` usado.

   Tras la síntesis se guarda `s_out`.
2. Síntesis del párrafo *k*: `torch.manual_seed(seed_k)` y `s_prev = s_in`. Cada párrafo arranca de su propio estado, no del que dejó el anterior en memoria.
3. **Regenerar el párrafo *k*** (por WER, *glitch* o mosaico) carga `s_in` de *k*, usa otra semilla y **no vuelve a sintetizar k+1…n**. Sus `s_in` guardados siguen siendo el `s_out` antiguo de *k*, así que su audio queda idéntico.
4. **Control de costura**: se compara el `s_out` nuevo de *k* con el `s_in` guardado de *k+1*. Si la similitud del coseno baja del umbral de G0, se prueba otra semilla (máximo 3). Si sigue sin pasar, se regenera también *k+1*, y así en cadena hasta un máximo de 2 párrafos.
5. Para dormir se fuerza `normal_reference` en todas las frases. El script original cambia a una referencia "interrogativa" o "exclamativa" si ve `?` o `!`, y eso mete saltos de estilo [S].
6. **Prueba en G0**: se sintetizan 10 párrafos, se regenera el 5.º con otra semilla y se comprueba que los párrafos 6-10 salen **idénticos bit a bit**. El `main` de Nós **ya fija** `cudnn.deterministic = True` y `cudnn.benchmark = False`; `sintetiza.py` copia esas dos líneas porque no pasa por `main`. Si aun así no sale idéntico (quedan operaciones CUDA no deterministas fuera de cuDNN), se prueba `torch.use_deterministic_algorithms(True)` con `CUBLAS_WORKSPACE_CONFIG=:4096:8` [F] https://docs.pytorch.org/docs/stable/notes/randomness.html y, si una capa no lo admite, basta con una correlación > 0,9999 entre versiones. El A/B de ritmo incluye además `t = 0` frente a `t = 0,7`: con 0,7 la prosodia es más estable en tiradas largas, y es justo el caso en el que guardar `s_in` resulta imprescindible [S].

**Pausas insertadas** en el bucle de `main`, que hoy concatena las frases sin silencio. Valores iniciales [S, a calibrar en G0]: fin de frase `.` `?` `!` → 700 ms; `:` y `;` → 450 ms (se añade `;` al troceado); fin de párrafo → 1.600 ms; fin de capítulo → 4.000 ms. Las comas no se tocan: el modelo tiene token de coma y hace su propia micro-pausa.

**Presupuesto de ritmo por párrafo** (`ritmo.py`, determinista):
- Objetivo: `T_obj = 60 · palabras / W`, con W = 118 palabras/min (centro de 110-125).
- `speed` es **fijo para todo el canal** (se decide en G0), para que el timbre y el tempo no cambien entre párrafos. Solo se ajusta la escala de pausas `k` para que `T_voz + k · T_pausas = T_obj`, con `k` entre 0,7 y 1,6.
- Si `k` se sale del rango, el párrafo se marca en el informe. **No se toca el texto.**
- Ejemplo [S]: si la voz habla a 150 palabras/min de habla pura, un párrafo de 150 palabras dura 60 s; con `speed` = 0,9 pasa a 66,7 s. El objetivo son 76,3 s, así que hacen falta 9,6 s de pausas. Con 8 frases (5,6 s) y fin de párrafo (1,6 s) hay 7,2 s de base, luego k = 1,33 ✔.
- Criterio de diseño: escalar las duraciones estira también las consonantes, mientras que un narrador humano lento alarga sobre todo vocales y silencios. Por eso **la mayor parte del ralentizado va en pausas** y `speed` no baja de 0,85 [S].

**A/B de ritmo (dentro de G0)**: el mismo pasaje de 3 min en 4 versiones, todas con el mismo presupuesto de pausas:
- (A) `speed` 1,0;
- (B) `speed` 0,92;
- (C) `speed` 0,85;
- (D) `speed` 1,0 y después `ffmpeg -af atempo=0.9`, que es estirar en posproducción.

Los jueces puntúan a ciegas la naturalidad y "¿me dormiría con esto?" (1-5). Como medidas objetivas se usan DNSMOS (el propio `inference.py` ya lo trae con `--evaluate` vía `speechmos`) y el WER del ASR. Regla [S]: se elige la versión más lenta cuya nota no baje más de 0,3 frente a (A) y cuyo WER no suba más de 1 punto. Si gana (D), el estirado pasa a posproducción y el parche se queda solo con pausas y semilla.

#### 3.5.5 Normalización previa del texto (antes de Cotovía)

`normaliza.py` + lingüista generan `normalizado.txt`, el texto exacto que se dirá. Números romanos y fechas se escriben con letra (*século doce*, *mil catrocentos sesenta e sete*), también abreviaturas y siglas, y se quitan los símbolos. La **lectura humana de H2 se hace sobre ese fichero**: se revisa lo que se va a oír, no lo que se va a leer en pantalla. El guion "de pantalla" (subtítulos, descripción) conserva cifras y romanos.

#### 3.5.6 Tiempos por palabra salidos del propio TTS

El parche devuelve `pred_dur` (duración de cada token) y la cadena fonémica. Las palabras se separan por el token espacio, y hay que descontar el token en blanco que el script inserta al principio. La conversión de unidades de duración a muestras se **calibra** una vez como `r = len(wav) / sum(pred_dur)` (debe ser constante para cada modelo; se comprueba en G0). Sumando el desfase de cada frase y las pausas insertadas sale `tempos_palabra.json` para todo el episodio, **exacto por construcción**. Sirve para cortar el mosaico (§3.3) y para los subtítulos. El ASR queda para lo suyo: detectar palabras comidas o cambiadas (WER). Si la voz ganadora no es StyleTTS2, se usa la alineación forzada CTC (§3.3, punto 2b).

#### 3.5.7 Si gana otra voz del A/B: la "controlabilidad" también puntúa

| Voz candidata | ¿Admite léxico de fonemas? | ¿Control de ritmo? |
|---|---|---|
| StyleTTS2 Brais/Celtia (Nós) | **Sí, con el wrapper del §3.5.3** | Sí, con el parche del §3.5.4 |
| VITS `*-phonemes` de Nós (Sabela, Icía, Celtia, Brais, Iago, Paulo) [F] https://huggingface.co/api/models?author=proxectonos | Probable, con el mismo enfoque si su frontend es Cotovía [S: verificar en su código] | Sí (`length_scale` de VITS) |
| Matcha y VITS `*-graphemes` de Nós (Brais, Celtia) | **No**: entran letras y solo cabe respelling, que no marca é/ó | Sí |
| Azure (Sabela/Roi) | SSML `<phoneme>` o léxico personalizado [S: verificar soporte en gl-ES] | Sí (`prosody rate`) |
| ElevenLabs | Diccionarios de pronunciación con alias; fonemas solo en algunos modelos [S: verificar en galego] | Limitado |

**Regla para el A/B de voz**: se añade el criterio "**¿se puede corregir?**". Una voz que suena algo mejor en la muestra pero **no permite fijar é/ó ni el acento** de un topónimo pierde frente a una que sí lo permite, porque el canal va a acumular cientos de nombres propios.

#### 3.5.8 Prueba G0 de 50 palabras de riesgo: ¿la corrección se oye de verdad?

La voz no se da por buena por escuchar un párrafo bonito. Antes de cerrar G0 (§9) se pasa esta prueba (~1 h de máquina y ~1,5 h de escucha de los jueces [S]):

- **Lote** (en frases portadoras neutras, siempre las mismas):
  - **20 nombres propios** de la serie: *Brigantium, Lucus Augusti, Iria Flavia, Gallaecia, Mondoñedo, Betanzos, Celanova, Oseira, Sobrado, Ribadavia, Viveiro, Monforte de Lemos, Compostela, Xelmírez, Prisciliano, Hermerico, Requiario, Pardo de Cela, Breogán, Castelao*.
  - **20 palabras = 10 pares é/ó** en frase portadora: *o corte / a corte*, *eu porto / o porto*, *óso / oso*, *sede* (de beber / institución) [S: confirmar el par] y otros 6 pares que elige el lingüista en el *Dicionario de pronuncia*.
  - **10 casos de normalización y fonética**: *século XII, 1467, 1486, unha, algunha, en + vogal, ao, coa, pola, Rosalía*.
- **Protocolo**:
  1. Síntesis con el léxico vacío (línea base). Los dos jueces marcan cada ítem como OK o KO, con el *Dicionario de pronuncia* delante.
  2. Cada KO se convierte en una entrada de `lexico.tsv` (o en una regla de normalización).
  3. **Comprobación automática**: para cada entrada, `g2p_log.jsonl` muestra la sustitución y la secuencia de *token IDs* cambia respecto a la línea base, sin ningún `X`. Esto demuestra que la corrección **llega al modelo**.
  4. Nueva síntesis y **ABX ciego**: cada juez oye línea base y corregida en orden aleatorio y dice cuál es correcta, o si suenan igual.
- **Criterios para pasar** [S]:
  - ≥ 90 % de los ítems corregidos se juzgan correctos por **los dos** jueces.
  - **≥ 8 de los 10 pares é/ó** se oyen distintos tras la corrección. Si el modelo no hace audible el contraste `É`/`é` aunque le lleguen los fonemas correctos, es un **límite del modelo** (sus datos de entrenamiento), no del léxico: esa voz no pasa en este punto, y se prueba la siguiente del A/B o se deja la solución para el *fine-tune* de la Etapa 3.
  - 0 regresiones entre los ítems que ya estaban bien.
  - Tiempos por palabra (§3.5.6) a ±80 ms de 20 palabras marcadas a mano.

#### 3.5.9 Versión de Cotovía fijada (la corrección depende de ella)

**Hallazgo** [P, 29-09-2026]: `phonemize.py` de Nós llama a `'cotovia -n -S -A0'` **por el `PATH`** (línea 23), sin ruta y sin `-D`. En una máquina que tenga instalado el paquete de la distribución (`cotovia 0.5`, binario del 10-12-2013, que es el que trae este entorno en `/usr/bin/cotovia`), el wrapper usaría ese binario **sin avisar**, y ese binario da otra salida:

| Entrada | Cotovía compilado desde `Utils/cotovia` de Nós, con `-D` de ese repositorio | `/usr/bin/cotovia` 0.5 (2013) |
|---|---|---|
| *eu **porto** a pedra* | `pO^rto` (abierta ✔) | `po^rto` (cerrada ✘: no distingue el verbo del nombre) |
| *pedra* | `pE^Dra` | `pe^Dra` (✘) |
| *no século XII* | `sE^kulo De^Timo seGu^ndo` ("décimo segundo") | `se^kulo Do^Te` ("doce") |

Con el binario antiguo, los resultados del §3.5.2 no se reproducen: se pierden las vocales abiertas y cambia la normalización. Por eso el pipeline **fija la versión**:

1. `vendor/cotovia/` guarda el binario compilado y su `data/`, del *commit* de Nós anotado en `versions.lock`, junto con el `sha256` del binario y del directorio de datos.
2. El wrapper llama siempre a **la ruta absoluta con `-D vendor/cotovia/data`** y nunca a `cotovia` a secas. Esa llamada es la única línea que el parche cambia en `phonemize.py`.
3. **Canario al arrancar**: *eu porto a pedra* tiene que dar `pO^rto` y *ao porto de Betanzos* tiene que dar `po^rto`. Si no, aborta con el mensaje "Cotovía incorrecto".
4. Cada `g2p_log.jsonl` registra el hash de Cotovía que se usó, y el expediente del episodio lo conserva.
5. La normalización de números y romanos (§3.5.5) se hace **antes** de Cotovía y no depende de su versión: lo que se dice es *século doce*, decidido por el lingüista (la versión de Nós diría "décimo segundo").

### 3.6 Control determinista de la veracidad histórica: diseño implementable

Para la pronunciación, el léxico se aplica y se comprueba por máquina. La veracidad necesita el mismo trato. Si solo se pide que cada frase lleve una marca de fuente, un LLM puede **inventarse la fuente** (o la página) y pasar el control. El principio es el mismo que en el §3.5: **lo que se puede comprobar con un script no se deja al juicio de un LLM**, y lo que juzga un LLM lo juzga uno de otra familia y lo muestrea un humano con un criterio fijado de antemano.

#### 3.6.1 Formato de `afirmacions.csv` (un contrato, no una sugerencia)

**Principio de diseño: el LLM apunta, la herramienta copia.** Un LLM no es un copista fiable de 15-40 palabras de un texto largo. Al "copiar", corrige las erratas de OCR, actualiza la ortografía preestándar (Murguía, López Ferreiro, Vicetto, prensa del XIX), normaliza comillas y guiones, y se salta o reordena alguna palabra. Si se le exigiera una cita literal, un investigador honesto fallaría a menudo, y con 150-250 afirmaciones por episodio eso serían decenas de bloqueos falsos. Por eso la columna `cita` **nunca la escribe el LLM**:

| Columna | Contenido | Quién la rellena |
|---|---|---|
| `id` | `a037` (la marca `⟦a:037⟧` del guion) | Investigador (LLM) |
| `tipo` | `data`, `cifra`, `causa`, `atribucion`, `lenda`, `outra` | Investigador; `qa.py` puede **subir** el riesgo, nunca bajarlo (§3.6.4) |
| `afirmacion` | El hecho en galego, en una frase | Investigador |
| `fonte` | id de `fontes.yaml` | Investigador |
| `loc` | Localizador: página (`p. 214`) en PDF; título de sección en Galipedia, con `revid` fijado en `fontes.yaml` | Investigador |
| `ancla` | **15-40 palabras que el LLM cree que están en la fuente**, en el idioma de la fuente. Puede venir con erratas corregidas o con ortografía moderna: es una dirección, no una prueba | Investigador |
| `sha_fonte` | `sha256` de `fontes/<id>.txt` en el momento de la extracción | `extrae_cita.py` |
| `ini`, `fin` | Desplazamientos de carácter `[ini, fin)` del fragmento en `fontes/<id>.txt`, cortados en límite de palabra | `extrae_cita.py` |
| `cita` | **`texto[ini:fin]`, literal de la fuente**, con sus erratas de OCR y su ortografía original | `extrae_cita.py` |
| `dist` | Distancia de edición normalizada entre el ancla y la cita (0 = idénticas), calculada tras quitar tildes, mayúsculas y puntuación | `extrae_cita.py` |
| `estado_ancla` | `ANCORADA` / `AXUSTADA` / `CIFRA_ALTERADA` / `MATIZ_ALTERADO` / `CITA_INVENTADA` / `SEN_ANCORA` (§3.6.2) + la lista de palabras que el ancla quita o añade frente a la fuente | `extrae_cita.py` |

Con este reparto, la afirmación de la v3 ("un investigador honesto siempre encuentra coincidencia") pasa a ser cierta **por construcción**: la cita siempre es un trozo real del `.txt`, porque la ha cortado un programa. Lo que el LLM hace mal al copiar ya no bloquea; queda medido en `dist` y, si importa, se ve en la revisión. Que el OCR sea fiel al papel lo sigue cubriendo la revisión humana del estrato A (§3.6.4), que tiene el PDF a un clic.

#### 3.6.2 `extrae_cita.py` + `verifica_citas.py`: extraer, luego comprobar

**Ingestión** (una vez por fuente): cada fichero de `fontes/` se guarda como texto UTF-8 NFC, se une el guion de fin de línea y se calcula su `sha256`, que va a `fontes.yaml`. Se trocea en **unidades de localizador**, que son la página (el `\f` de `pdftotext`) o la sección (`== … ==` de Galipedia). Cada unidad guarda su intervalo de caracteres `[ini_loc, fin_loc)` y es una fila `(doc, loc, ini_loc, fin_loc, texto)` de una tabla virtual FTS5 con `tokenize='unicode61 remove_diacritics 2'` [F] https://www.sqlite.org/fts5.html.

**`extrae_cita.py`** (determinista, ~80 líneas; prototipo [P] en `drafts/extrae_cita_prototipo.py`):

1. **Dónde buscar.** Primero, en la unidad declarada (`loc`) y en las vecinas (±1 página, para las citas que cruzan de página). Si no aparece, en todo el documento declarado. En fuentes largas (un PDF de 400 páginas), las páginas candidatas se eligen con una consulta FTS5 `NEAR` sobre las 3-4 palabras más raras del ancla, y la búsqueda fina solo recorre esas páginas.
2. **Búsqueda fina.** Se tokeniza la fuente conservando la posición de cada palabra. Se comparan ventanas de n−4 a n+4 palabras (n = longitud del ancla), después de quitar tildes, mayúsculas y puntuación, con la distancia de Levenshtein normalizada de `rapidfuzz` [F] https://rapidfuzz.github.io/RapidFuzz/Usage/distance/Levenshtein.html. Un prefiltro exige que la ventana contenga al menos 2 de las palabras "raras" (≥ 6 letras) del ancla. Gana la ventana de menor distancia.
3. **Salida.** `ini` = inicio de la primera palabra de la ventana y `fin` = final de la última, en el texto **original** (no en el normalizado). Así la cita queda cortada en límite de palabra y es literal. `cita = texto[ini:fin]`.
4. **Diferencias.** Un diff de secuencia palabra a palabra (no de conjuntos) entre el ancla y la cita da lo que el LLM **quitó** y lo que **añadió**.
5. **Estado** (umbrales [S], calibrados en la simulación de abajo y a recalibrar en G2):

| Estado | Condición | Efecto |
|---|---|---|
| `ANCORADA` | `dist` ≤ 0,08 y sin cambios de cifras ni de palabras de matiz | Pasa. Estrato según su tipo |
| `AXUSTADA` | 0,08 < `dist` ≤ 0,20 | Pasa (la cita guardada es la real), pero va al **estrato A** con el diff resaltado: puede ser paráfrasis, no solo ruido de copia |
| `CIFRA_ALTERADA` | `dist` ≤ 0,20 y el diff incluye un número | **Estrato A** con la cifra real resaltada. Además, R5 compara las cifras del guion con la cita **real**, así que si el guion lleva la cifra alterada, bloquea |
| `MATIZ_ALTERADO` | `dist` ≤ 0,20 y el diff incluye una palabra de matiz: *non, nunca, nin, posiblemente, probablemente, quizais, talvez, segundo, arredor, case, algúns, uns, máis, menos, lenda, tradición, contan, dise* (y sus equivalentes castellanos y portugueses) | **Estrato A**. El juez del §3.6.3 recibe la cita real, con el matiz, así que ve lo que el guion ha perdido |
| `CITA_INVENTADA` | `dist` > 0,20 | **Bloquea H2** |
| `SEN_ANCORA` | Ninguna ventana pasa el prefiltro | **Bloquea H2** |

6. **Reintento automático antes de molestar a nadie.** Ante `CITA_INVENTADA` o `SEN_ANCORA`, el investigador recibe los **3 pasajes más parecidos** con su distancia, y hace una de dos cosas: elige uno (la herramienta vuelve a extraer y el resultado entra con estado `AXUSTADA` como mínimo, es decir, al estrato A) o retira la afirmación. Cuenta como una de las 3 vueltas del §3. Solo llega al humano lo que sigue bloqueado tras las 3.

**`verifica_citas.py`: reglas** (todas deterministas; cualquier fallo **bloquea H2** y devuelve el trabajo a quien se indica en el §3.1):

| Regla | Qué comprueba | Estado si falla |
|---|---|---|
| R1 Marca | Toda frase del guion con cifra, año, romano, conector causal (*porque, por iso, provocou, levou a, a causa de, de aí que…*) o verbo de atribución (*dixo, escribiu, segundo, contan, chamoulle…*) lleva `⟦a:…⟧`. Las `⟦amb⟧` no pueden contener nada de eso | `SEN_MARCA` |
| R2 Longitud | La cita extraída tiene entre 15 y 40 palabras. Si es más corta, es ambigua; si es más larga, se está copiando texto | `LONXITUDE_CITA` |
| R3 Integridad | `sha256(fontes/<id>.txt)` coincide con `sha_fonte` y con `fontes.yaml`, y `texto[ini:fin] == cita` **byte a byte**. Detecta que alguien (un LLM en una vuelta posterior, o una edición a mano) haya retocado la columna `cita` o la instantánea de la fuente | `CITA_MANIPULADA` / `FONTE_CAMBIADA` |
| R3b Anclaje | `estado_ancla` no es `CITA_INVENTADA` ni `SEN_ANCORA` | `CITA_INVENTADA` |
| R4 Procedencia | `[ini, fin)` cae dentro de la unidad declarada en `loc` (o cruza a la siguiente). Si cae en otra unidad, se informa de cuál | `LOCALIZADOR_ERRADO` (y `FONTE_ERRADA` si el mejor pasaje está en otro documento) |
| R4b Contraprueba FTS5 | La cita extraída, como frase FTS5 de tokens consecutivos, aparece en esa unidad. Es redundante con R3 a propósito: si el tokenizador o el índice cambian, discrepan y se nota | `INDICE_INCOHERENTE` (aborta) |
| R5 Cifras | Cada número o año de **la frase del guion** (no de la columna `afirmacion` ni del ancla) aparece en la cita **real**. Se compara el guion "de pantalla", que conserva las cifras (§3.5.5) | `NUMERO_SEN_RESPALDO` |

**Prueba del prototipo v3** [P, `drafts/verifica_citas_prototipo.py`] sobre 3 artículos de Galipedia (*Gran Guerra Irmandiña*, *Castelo da Rocha Forte*, *Pardo de Cela*; ~9.600 palabras): las 5 citas reales pasaron, se detectaron un localizador erróneo y una cifra del guion (*1468*) sin respaldo, y las 5 citas falsas se bloquearon. Esa prueba usaba citas copiadas a mano, así que **no medía el ruido de un LLM copista**. La nueva batería sí lo hace.

**Prueba de `extrae_cita.py`** [P, `drafts/proba_extrae_cita.py`, mismo corpus, semilla fija]:

*(a) Casos de la v3*: las 7 citas reales dan `ANCORADA` (dist = 0). Las 5 falsas: inventada → `SEN_ANCORA`; año cambiado → `CIFRA_ALTERADA` (quita `1467`, añade `1468`); *posiblemente* eliminado → `MATIZ_ALTERADO` (dist = 0,084); empalme → `CITA_INVENTADA` (0,258); traducción al castellano → `CITA_INVENTADA` (0,361).

*(b) Bloqueos falsos*: 480 fragmentos reales de 18-35 palabras "copiados" con 0-3 alteraciones al azar de las que hace un LLM sin cambiar el sentido (comillas «», guiones, tildes quitadas, *omes* → *homes*, *tódalas* → *todas as*, una palabra saltada, dos palabras intercambiadas). La búsqueda se hizo en cuatro versiones de la fuente: limpia; con erratas de OCR al 2 % y al 5 % de los caracteres susceptibles (*m→rn, e→c, l→1, h→li, u→n*…), con el ancla limpia (el LLM "corrigió" el OCR); y con ortografía preestándar simulada (*d'a, d'o, n-a, gente, Hirmandade, hestoria*):

| Fuente | n | `ANCORADA` | `AXUSTADA` (→ A) | `MATIZ_ALTERADO` (→ A) | **Bloqueos falsos** |
|---|---|---|---|---|---|
| Limpia | 120 | 111 | 8 | 1 | **0** |
| OCR 2 % | 120 | 105 | 14 | 1 | **0** |
| OCR 5 % | 120 | 114 | 4 | 2 | **0** |
| Preestándar | 120 | 110 | 9 | 1 | **0** |

El ancla cae en el pasaje correcto en **120 de 120** casos con la fuente limpia. Coste: el ~8-13 % de las afirmaciones pasa al estrato A por ruido de copia (se presupuesta en el §6). Con 3 alteraciones simultáneas, la distancia del ruido legítimo queda en mediana 0,039, p95 0,129, p99 0,180 y máximo 0,198 (n = 225).

*(c) Falsificaciones en serie* (145): cita real de otro documento atribuida a este → 30 de 30 bloqueadas (`SEN_ANCORA` o `CITA_INVENTADA`); empalme de dos mitades de pasajes distintos → 30 de 30 `CITA_INVENTADA`; palabras barajadas → 30 de 30; año +1 → 28 de 28 `CIFRA_ALTERADA`; matiz eliminado → 27 de 27 `MATIZ_ALTERADO`. **Ninguna falsificación queda como `ANCORADA`.**

*(d) Margen del umbral*: con 75 empalmes adicionales, la distancia mínima fue 0,147 y el p5 0,226. Con el umbral en 0,20 se bloquea el 99 % y el resto cae en `AXUSTADA`, es decir, en el estrato A con el diff a la vista: **no pasa sin ojos humanos**. Bajar el umbral a 0,15 subiría los bloqueos falsos al 2,7 %; subirlo a 0,25 dejaría bloquear solo el 89 % de los empalmes. **El margen entre ruido y fraude es estrecho (0,198 frente a 0,147)**, y por eso el estado intermedio `AXUSTADA` va siempre a revisión humana y el umbral se recalibra en G2 con anclas del LLM real.

Rendimiento: 480 extracciones en 21 s sobre documentos de ~1.600-4.100 palabras, con búsqueda por fuerza bruta (~44 ms por afirmación, ~11 s para 250) [P]. En PDF largos, el paso 1 (FTS5 `NEAR` + página declarada ±1) acota la búsqueda. Coste: 0.

Límite honesto de la simulación: las alteraciones las genera un script, no un LLM. Un LLM puede parafrasear más (sustituir sinónimos, resumir), y eso subiría `dist`. Por eso G2 mide la tasa de bloqueos falsos con **el investigador real** (§3.6.5), y cada episodio la registra.

**Lo que este control NO garantiza** (por eso existen el §3.6.3 y el §3.6.4):
- que la cita respalde lo que dice la frase del guion (se puede citar bien y parafrasear mal);
- que la fuente tenga razón.

Ejemplo real encontrado al montar el prototipo [P]: el mismo artículo de Galipedia sobre Pardo de Cela dice en la entradilla "executado en Mondoñedo **o 3 de outubro de 1483**" y en *O enfrontamento coa coroa* que fue detenido "o 7 de decembro" y que "dez días despois lle cortan a cabeza". **Las dos citas pasarían R3-R5.** Por eso, para cada afirmación de tipo `data`, la hoja de revisión muestra automáticamente **las demás fechas que aparecen junto al mismo nombre propio en todo el corpus** (consulta FTS5 `NEAR`). Una contradicción entre fuentes, o dentro de una misma fuente, se ve en la pantalla de revisión y no depende de que alguien la recuerde.

#### 3.6.3 Juez de respaldo de otra familia

- **Modelo**: el redactor es Claude (Opus) y el lingüista LLM también es Claude (Sonnet). El juez es **Gemini 3.8 Flash** (Google), de otra familia y otros datos de entrenamiento, a **0,75/3,75 USD por 1M de tokens (entrada/salida) hasta el 31-12-2026 y 1,50/7,50 desde el 1-1-2027; *batch* al −50 %; con capa gratuita** [F] https://ai.google.dev/gemini-api/docs/pricing. En la capa gratuita, Google usa el contenido para mejorar sus productos [F, misma URL]. Como el guion es inédito, **se usa la capa de pago**, que cuesta céntimos. Alternativa equivalente: un modelo de OpenAI. Nunca otro Claude.
- **Entrada** (y solo esta): la **frase del guion** tal como quedó tras el lingüista, más la cita **real** (la extraída, no el ancla del LLM) y **±150 palabras de contexto** de la fuente, recortadas alrededor de `[ini, fin)`. No ve la columna `afirmacion`, ni el dossier, ni el razonamiento del redactor. Así juzga lo que se va a decir, no lo que se quería decir.
- **Salida** (JSON): `{"veredicto": "si|parcial|non", "elemento_sen_apoio": "...", "matiz_perdido": true/false}`. La rúbrica pide marcar `parcial` cuando el guion **quita un matiz** (*posiblemente*, *segundo a tradición*), **generaliza** (de "algúns" a "os"), **convierte una leyenda en hecho** o **atribuye a otra persona**.
- **Reglas**: `non` → vuelve al guionista (reformular o quitar). `parcial` → estrato A de la revisión humana. `si` → estrato según su tipo.
- **Coste** [S sobre F]: unas 250 afirmaciones × ~1.500 tokens de entrada y ~150 de salida ≈ 375k/38k tokens → **~0,2 USD por episodio de 2 h en *batch*** (~0,4 USD en 2027).

#### 3.6.4 Revisión humana estratificada por riesgo, con umbral

Se hace dentro de H2, sobre `revision_afirmacions.html`. Cada fila muestra la frase del guion, la cita resaltada dentro de su contexto, el enlace a la fuente (PDF en la página), el veredicto del juez y, en las fechas, las otras fechas del corpus.

| Estrato | Qué entra | Cuánto se revisa |
|---|---|---|
| **A: alto riesgo** | Toda afirmación de tipo `data`, `cifra`, `causa` o `atribucion`. El tipo lo da el investigador, pero `qa.py` **lo sube** si la frase tiene cifras o años, conectores causales o verbos de atribución (las mismas regex de R1). Entran también las `parcial` del juez; las `AXUSTADA`, `CIFRA_ALTERADA` y `MATIZ_ALTERADO` de `extrae_cita.py` (la fila muestra el ancla del LLM y la cita real con las diferencias resaltadas); las que se desbloquearon eligiendo un pasaje candidato; y las fuentes con fiabilidad "media" en `fontes.yaml` | **100 %** |
| **B: resto** | Descripción, contexto, leyenda ya marcada como tal | **Muestra aleatoria de max(20, 15 %)**, con la semilla registrada en `firma_guion.yaml` |

**Qué cuenta como error**: que el humano juzgue que la cita **no respalda** la frase, o que la respalda solo en parte y el guion no lo matiza. También cuenta que haya contradicción con otra fuente del corpus y no se haya resuelto.

**Umbrales** [S, a revisar tras 5 episodios]:
- **Estrato B**: **1 error en la muestra obliga a revisar el 100 % de B.** Potencia de detección con n = 20 (probabilidad de ver al menos un error): 88 % si la tasa real de error es del 10 %, 64 % si es del 5 % y 96 % si es del 15 % (1 − (1 − p)^20).
- **Estrato A**: los errores se corrigen uno a uno. Si pasan del **5 % de A**, o si el humano discrepa del juez en más del 10 % de las filas de A, se entiende que el verificador está fallando de forma sistemática. Entonces **se revisa también el 100 % de B** y, antes del siguiente episodio, se corrigen los *prompts* del investigador y del juez.
- Los errores y discrepancias por episodio se acumulan en `metricas_verificacion.csv`. Si el estrato B da 0 errores en 5 episodios seguidos, se puede bajar la muestra al 10 % (con un mínimo de 20). Si aparece un error publicado (fe de erratas), se vuelve al 100 % de B en los 2 episodios siguientes.

**Volumen y tiempo** [S, a medir]: ~1 afirmación cada 55 palabras da ~150 afirmaciones en 75 min (A ≈ 60, B ≈ 90 → 20 revisadas) y ~250 en 2 h (A ≈ 100, B ≈ 150 → 23 revisadas). **El ruido de copia del LLM mueve filas de B a A**: en la simulación, el 5-13 % de las anclas acaba en `AXUSTADA` o `MATIZ_ALTERADO` (§3.6.2). Con un 10-15 % en la práctica [S], y como ~60 % de ellas serían de B, pasan a A ~9-14 filas más en 75 min y ~15-22 en 2 h. Con la cita ya resaltada al lado, cada fila lleva ~25-35 s (las `AXUSTADA`, algo más, porque hay que mirar el diff). Salen **~0,7-0,8 h por episodio en la Etapa 1** y **~1,0-1,2 h en la Etapa 2**.

**Escalados al humano por bloqueo** [S]: con una tasa de bloqueos falsos ≤ 2 % tras el reintento automático (la condición de G2), llegan como mucho ~3 filas en 75 min y ~5 en 2 h, a ~2 min cada una (abrir la fuente, localizar el pasaje, elegirlo o retirar la afirmación): **≤ 0,1 h y ≤ 0,17 h**. Están en el §6. Si en un episodio pasan de 5, se para y se revisa el *prompt* del investigador antes de seguir.

#### 3.6.5 Prueba adversarial y de bloqueos falsos (puerta G2), canarios en cada ejecución y métricas por episodio

**Prueba de G2** (una vez, con el episodio de prueba de 20 min):
1. **Anclas falsas plantadas.** Se añaden a `afirmacions.csv` 5 anclas falsas, una de cada tipo: inventada verosímil, real con la cifra alterada, real sin un matiz, empalme de dos fragmentos y traducción presentada como literal. **Criterio: ninguna queda `ANCORADA`.** La inventada, el empalme y la traducción tienen que quedar **bloqueadas** (`CITA_INVENTADA` o `SEN_ANCORA`). La cifra alterada tiene que salir como `CIFRA_ALTERADA`, y la frase del guion que usa la cifra falsa, bloqueada por R5. El matiz tiene que salir como `MATIZ_ALTERADO` y acabar en el estrato A con la palabra perdida resaltada. Con un solo fallo no se pasa: se arregla y se repite.
2. **Respaldo falso con cita real.** Se insertan 5 frases con cita real que no las respalda: causa cambiada, generalización, matiz eliminado en la paráfrasis, leyenda contada como hecho y atribución a otra persona. **Criterio: el juez marca ≥ 4 de 5 como `non` o `parcial`**, y las 5 acaban en el estrato A, así que el humano las ve todas.
3. **Bloqueos falsos con el LLM real** (lo que la v3 no medía). El investigador de producción, con su *prompt* y su modelo reales, propone anclas para **todas las afirmaciones del dossier** del episodio de 20 min, no solo las que usa el guion: **≥ 100 afirmaciones** (si el dossier da menos, se completa con un segundo tema corto). Se cuentan los bloqueos (`CITA_INVENTADA` / `SEN_ANCORA`) que quedan **después** del reintento automático, y el promotor comprueba cada uno en la fuente. Es **bloqueo falso** si el hecho está en ese pasaje de la fuente y el LLM solo lo citó mal.
   - **Criterio: tasa de bloqueos falsos ≤ 2 %** (≤ 2 de 100). Si es mayor, primero se ajusta el *prompt* del investigador (p. ej., "copia de la fuente sin corregir nada, aunque veas erratas"), luego el umbral de `dist` (dentro de 0,18-0,25: por debajo de 0,18, suben los bloqueos falsos; por encima de 0,25, dejan de bloquearse empalmes, §3.6.2), y se repite.
   - Se registran también la **tasa de `AXUSTADA` + `MATIZ_ALTERADO`** (objetivo ≤ 15 %, porque cada una es una fila más del estrato A) y los **bloqueos antes del reintento** (miden el trabajo de máquina, no el humano).
   - Control complementario: 10 afirmaciones reales y bien respaldadas pasan el juez sin bloqueo (≤ 1 marcada `parcial`).

**Canarios en producción**: en cada ejecución, `qa.py` genera **5 anclas mutadas de forma determinista** a partir de citas reales del propio episodio, y comprueba el estado que cada una debe recibir **antes** de verificar el guion real:

| Canario | Estado esperado |
|---|---|
| Año ±1 | `CIFRA_ALTERADA`, con el `[ini, fin)` de la cita original |
| Una palabra de matiz borrada (si la cita no tiene ninguna, se inserta *posiblemente*) | `MATIZ_ALTERADO`, con el mismo `[ini, fin)` que la cita original (prueba a la vez que el anclaje tolera el cambio y que lo señala) |
| Empalme de dos citas del episodio | `CITA_INVENTADA` |
| Palabras barajadas | `CITA_INVENTADA` |
| Cita real de **otro** documento atribuida a este | `SEN_ANCORA` o `FONTE_ERRADA` |

Además, R3 se prueba en cada ejecución alterando **una letra** de la columna `cita` de una copia de una fila: tiene que salir `CITA_MANIPULADA`. Si algún canario no da lo esperado, **el verificador está ciego** (índice corrupto, fuente vacía, tokenizador cambiado, umbral mal cargado) y `qa.py` aborta sin emitir veredicto. Los canarios no tocan el guion y quedan en `qa_texto.json` como evidencia.

**`metricas_verificacion.csv`** (una fila por episodio; son las cifras que dicen si el sistema aguanta la producción):

| Columna | Qué mide | Alarma [S] |
|---|---|---|
| `n_afirmacions`, `n_A`, `n_B` | Volumen y reparto por estrato | A > 55 % del total |
| `bloqueos_1a_volta` | Anclas bloqueadas antes del reintento automático | — (trabajo de máquina) |
| `rebloqueos` | Anclas que siguen bloqueadas tras las 3 vueltas y llegan al humano | > 5 por episodio |
| `bloqueos_falsos` | De esos, cuántos eran hechos reales de la fuente mal anclados (lo decide el humano al resolverlos) | > 2 % de las afirmaciones |
| `axustadas`, `matiz_alterado`, `cifra_alterada` | Ruido y deriva del LLM copista | `axustadas` + `matiz_alterado` > 15 % |
| `dist_p50`, `dist_p95` | Distribución de `dist` de las anclas aceptadas | `dist_p95` > 0,15 (el LLM se acerca al umbral: se revisa el *prompt*) |
| `erros_A`, `erros_B`, `discrepancias_xuiz` | Resultados de la revisión humana (§3.6.4) | Umbrales del §3.6.4 |
| `min_revision`, `min_escalados` | Tiempo humano real de la hoja de revisión y de los escalados | Por encima de lo presupuestado en el §6 durante 2 episodios seguidos |

---

## 4. Stack concreto por etapa

### 4.1 Etapa 1: coste mínimo con Claude Code + Python (meses 1-6)

**Orquestación**
- **Claude Code** con el plan **Pro (20 USD/mes; 17 USD/mes en anual), que incluye Claude Code** [F] https://claude.com/pricing.
- Cada agente es un **subagente de Claude Code** (`.claude/agents/investigador.md`, `guionista.md`, `linguista.md`, `verificador.md`, `director_visual.md`, `auditor.md`) con su *system prompt* y sus herramientas permitidas.
- Un comando propio (`/episodio <slug>`) encadena las etapas y se para en cada puerta humana. Sin LangGraph todavía: el "grafo" es un `Makefile` o un `pipeline.py` con estados en ficheros (`estado.json`). Cualquier etapa se puede relanzar.
- Supuesto crítico [S]: **2 episodios/mes caben en los límites de uso del plan Pro**. Si no caben, hay dos salidas: pasar las etapas de redacción a la API (≈3-4 USD por episodio de 75 min, §5.1) o subir temporalmente a Max (desde 100 USD/mes [F] https://claude.com/pricing, fuera del presupuesto de la Etapa 1).

**Por etapa**

| Etapa | Herramienta Etapa 1 | Coste |
|---|---|---|
| Corpus / RAG | **RAG "de carpeta"**: por episodio, 30-80 documentos (artículos de Galipedia vía la API de MediaWiki, entidades de Wikidata vía SPARQL, PDFs de Galiciana/Minerva/RUC pasados a texto con `pdftotext` o Tesseract `glg`) en `fontes/`, registrados en `fontes.yaml` con su licencia [R `voz_guion.md` §2.3]. Con 50-150k tokens por dossier, **el modelo lee el dossier entero**: no hace falta base vectorial. Índice SQLite FTS5 para buscar citas | 0 € |
| Regla de licencias | CC BY-SA (Galipedia): se parafrasean hechos y se atribuye. CCG / Álbum de Galicia: **solo verificación**, nunca texto al guion. Dominio público (Murguía, López Ferreiro, Vicetto): relato y ambiente, marcando la historiografía superada [R] | — |
| Guion y revisión LLM | Claude (redactor: Opus; lingüista: Sonnet con otro *prompt*; **juez de respaldo: Gemini, de otra familia**, §3.6.3) dentro de la suscripción. **Antes de fijarlo, prueba ciega de redactor** (Claude, GPT, Gemini y, si se puede servir, ALIA-40b) [R `voz_guion.md` §2.1] | Incluido en Pro [S] |
| Corrección determinista | `hunspell-gl` (pyhunspell), LanguageTool autoalojado (Java), CarvalhoChat_GEC (LoRA sobre una base *gated*: hay que pedir acceso; aplazado, y cuando entre, en una sesión de Runpod, §4.1.1 d) | 0 € |
| Voz | **La ganadora del kit A/B** (decidido aparte). Por defecto, **Nós StyleTTS2 (Brais o Celtia)** **en la CPU local** mediante `voz_worker.py` y la cola `jobs/` (§4.1.1; Runpod como plan B si falla B0), con **Cotovía compilado desde el *commit* fijado de Nós** (binario y `data/` en `vendor/`, verificados por hash y canario al arrancar el orquestador; nunca el `cotovia` del sistema, §3.5.9) + `g2p_override.py` + `inference.py` parcheado (§3.5). Alternativa: VITS/Matcha en CPU [R]. Alternativa: Azure Sabela/Roi dentro de la capa gratuita de 500k caracteres/mes (~53k por episodio, así que 2 episodios caben de sobra) [R] | 0 € en CPU (b). Plan B (c): ~0,6-0,8 USD por episodio (GPU + volumen) [S sobre F] https://www.runpod.io/pricing. Colab (Pro 9,99 USD/mes [F] https://colab.research.google.com/signup) no se usa como *worker* (§4.1.1 b) |
| Retrotranscripción QA | `whisper-large-v3-turbo-gl` de Nós convertido a CTranslate2 int8 (`faster-whisper`), en CPU local, **por párrafo**. RTF 0,75 medido [P] (§4.1.1 a) | 0 € |
| Verificación factual | `extrae_cita.py` (`rapidfuzz`, licencia MIT, `pip install rapidfuzz`) + `verifica_citas.py` (SQLite FTS5, en la biblioteca estándar de Python) + juez **Gemini 3.8 Flash** por API de pago (§3.6.3) | ~0,1 USD por episodio de 75 min [S sobre F] |
| Imágenes | Opción A: **Nano Banana 2 Lite (`gemini-3.1-flash-lite-image`) en *batch*, 0,0168 USD por imagen 1K (0,0336 sin *batch*)** [F] https://ai.google.dev/gemini-api/docs/pricing. Opción B: FLUX en una sesión de Runpod (§4.1.1 d), solo si A no convence; en CPU no es viable [S]. **Imagen 4 Fast queda descartado**: `imagen-4.0-fast-generate-001` se apagó el 17-08-2026 y Google recomienda sustituirlo por `gemini-3.1-flash-image` [F] https://ai.google.dev/gemini-api/docs/deprecations | ~1,8 USD por episodio (A) |
| Mapas | Hechos una vez con QGIS y datos abiertos (OpenStreetMap, ODbL [S: verificar la atribución exigida]), con toponimia oficial en galego. Plantilla reutilizable | 0 € |
| Ambiente | Grabaciones propias (chuvia, ría, lareira), según `formato.md` §6, o la Biblioteca de audio de YouTube | 0 € |
| Montaje | **FFmpeg** (`zoompan` o recorte animado sobre imágenes preescaladas a 4K; `xfade`; `amix`; `loudnorm`), llamado desde Python. MoviePy solo si simplifica, porque es más lento en vídeos de 1-2 h [S] | 0 € |
| Publicación | **Subida manual por YouTube Studio**, con la declaración de contenido alterado/sintético si procede (§8). Metadatos generados en `metadatos_yt.json` para copiar y pegar | 0 € |
| Versionado | git (repositorio privado) | 0 € |

### 4.1.1 Dónde corren la voz y el ASR en la Etapa 1, y cómo se conectan con el orquestador

**El problema.** El orquestador es local: Claude Code, `pipeline.py`/`Makefile` y `estado.json`. La síntesis (StyleTTS2-GL), la retrotranscripción (Whisper-gl) y, más adelante, CarvalhoChat_GEC necesitan cómputo pesado. Además, los bucles del QA exigen tener ese cómputo **disponible varias veces por episodio**:
- el primer pase;
- la regeneración por WER, con otra semilla, hasta 3 veces;
- el control de costura;
- el ABX del mosaico después de cada entrada nueva del léxico.

Si cada vuelta obliga a reabrir una sesión, ese coste humano se come el presupuesto de 4 h/semana. Por eso esta decisión se toma con medidas y no con supuestos.

#### a) Medida propia en CPU [P, 29-09-2026]

**Entorno de la prueba**:
- servidor Xeon de **4 vCPU** (1 hilo por núcleo), 15 GB de RAM y **sin GPU**;
- `torch 2.14.0+cpu`, `faster-whisper 1.2.1` y `ctranslate2 4.8.2`;
- modelo `proxectonos/Nos_StyleTTS2-Brais-GL` (`epoch_2nd_00057.pth` + PL-BERT + ASR auxiliar);
- Cotovía compilado desde el repositorio de Nós con `-D` (hash `9614a4b6…`);
- texto: las **1.263 palabras / 72 frases** del guion muestra de la Revolta Irmandiña (`drafts/guion.md`);
- **`LFinference` original**, sin el parche de ritmo del §3.5.4, con `alpha 0,3`, `beta 0,7`, `t 0`, `diffusion_steps 5` y `embedding_scale 1`.

Scripts y resultados literales en `drafts/bench_cpu/` (`bench_tts.py`, `bench_asr.py`, `per_sent.py`, `*.json`).

| Medida | Resultado |
|---|---|
| Descarga de los pesos de voz (3,0 GB) / de Whisper-gl (3,2 GB, `model.safetensors`) | 103 s / 105 s (en este servidor, ~30 MB/s) |
| Conversión de Whisper-gl a CTranslate2 int8 (una sola vez) | 34 s → 788 MB |
| **Arranque en frío de la voz** (importar + cargar los 3 modelos a RAM) | **27,6 s** (22-30 s en 4 ejecuciones) |
| Canario de Cotovía (*eu porto* → `pO^rto`; *ao porto* → `po^rto`) | 0,11 s ✔ |
| **TTS, 4 hilos: 395,8 s de audio en 110,6 s de cálculo** | **RTF 0,28** (frase más lenta: 6,3 s) |
| TTS, 2 hilos (314 palabras) | RTF 0,38 |
| Velocidad natural de Brais sin pausas ni parche | **191,5 palabras/min** (por eso hacen falta el `speed` y las pausas del §3.5.4 para llegar a 110-125) |
| RAM máxima: TTS / ASR | 3,65 GB / 1,67 GB |
| **ASR int8, 4 hilos, audio entero de 6,6 min de una vez** | RTF 0,58, pero **WER 48-53 %**: Whisper **alucinó** un tramo de ~1 min (texto sin sentido que se repite) aunque el audio de ese tramo estaba bien |
| **ASR int8, frase a frase** (`beam 1`, `condition_on_previous_text=False`) | **RTF 0,75**; **WER mediana 0 %**; 15 de 72 frases por encima del 6 % |

**Qué hay detrás de esas 15 frases por encima del 6 %** (lectura manual de `per_sent.json`):
- **6** son solo números: el ASR escribe *1467* y el guion normalizado dice *mil catrocentos sesenta e sete*;
- **2-3** parecen **fallos reales del TTS** (a confirmar de oído) que el control debe atrapar: un tartamudeo inicial (*"A bababonda con te deixares levar"*) y *Uns* oído como *Algúns* en una frase de dos palabras;
- el resto son diferencias de una palabra en frases muy cortas, donde una palabra ya supera el 6 %.

**Cuatro consecuencias para el diseño**, que ya pasan al §3.2:
1. El ASR del QA se hace **por párrafo y nunca sobre el audio entero**, con `condition_on_previous_text=False`.
2. **La hipótesis del ASR se normaliza con el mismo Cotovía** (su columna 1 escribe los números con letra, §3.5.2) antes de calcular el WER.
3. El WER se mide **por párrafo** (100-200 palabras), no por frase, para que una palabra no dispare el umbral.
4. El umbral del 6 % se calibra en G0 con esta tasa de falsas alarmas como punto de partida.

**Proyección por episodio con la voz en CPU** [S sobre P]. Supuestos:
- el parche alarga el habla pura entre ×1,0 y ×1,18 (`speed` 1,0-0,85);
- las pausas insertadas no cuestan cálculo;
- se regenera un +15 % de párrafos;
- el ASR recorta los silencios con VAD.

| | Etapa 1 (8.600 palabras) | Etapa 2 (13.800 palabras) |
|---|---|---|
| Habla pura que hay que sintetizar | 45-53 min | 72-85 min |
| TTS (RTF 0,28 + 15 % de regeneraciones) | **15-17 min** | **23-28 min** |
| ASR por párrafo (RTF 0,75) | **34-40 min** | **54-64 min** |
| **Total, máquina desatendida** | **≈ 50-60 min** | **≈ 1,3-1,6 h** |
| Una vuelta de regeneración (1 párrafo de ~150 palabras: TTS + ASR) | < 1 min | < 1 min |
| ABX del mosaico (resintetizar ~10 párrafos afectados) | ~8-10 min | ~8-10 min |

**Aviso importante**: todo lo anterior se ha medido en un servidor, **no en el ordenador del promotor**. Un portátil puede ir entre 0,7 y 2 veces más lento [S], y eso es justo lo que mide la prueba B0 del apartado (e).

#### b) Tres opciones, con pros y contras

| | (a) Cuaderno de Colab como *worker* (cola en Drive) | **(b) Inferencia local en CPU** | (c) Runpod por horas desde la Etapa 1 |
|---|---|---|---|
| Cómo funciona | Un cuaderno lee `jobs/*.json` en Drive, escribe `out/*.wav` + tiempos + log, y `pipeline.py` espera por *polling* | `pipeline.py` lanza `voz_worker.py` como proceso local; el modelo se carga una vez y atiende la cola hasta vaciarla | `gpu_run.sh` crea un *pod*, sube la cola, ejecuta el mismo `voz_worker.py`, baja los resultados y **para el pod** |
| Coste | 0 € (gratis) o 9,99 USD/mes (Pro) [F] https://colab.research.google.com/signup | **0 €** | ~0,15-0,40 USD por episodio en GPU + 1,05 USD/mes de volumen (detalle abajo) |
| ¿Está permitido? | **En la versión gratuita, no para este uso.** Para usuarios sin saldo de unidades de cómputo, la FAQ de Colab prohíbe *"running distributed computing workers"* y *"bypassing the notebook UI to interact primarily via a web UI"* [F] https://research.google.com/colaboratory/faq.html | Sí | Sí: `runpodctl pod create / stop / delete` desde la línea de comandos [F] https://docs.runpod.io/runpodctl/reference/runpodctl-create-pod |
| ¿Aguanta desatendido? | No. *"Runtimes will time out if you are idle"*; como mucho 12 h; la GPU no está garantizada (*"heavily restricted"*); la ejecución en segundo plano es solo de Pro+ (49,99 USD/mes) [F, FAQ y signup] | Sí, mientras el equipo esté encendido | Sí; el pod se para solo al vaciar la cola (con `timeout` de seguridad) |
| Coste de cada reconexión | Montar Drive (clic de OAuth), `pip install`, copiar ~3,8 GB de modelos desde Drive, cargar (~30 s), verificar el hash de Cotovía y el canario: **10-20 min de reloj y 5-10 min de atención humana** [S] | Ninguno: arranque en frío de 27,6 s [P] sin intervención | Crear el pod + bajar la imagen + cargar desde el volumen: 3-8 min de reloj [S], ~1 min humano (un comando) |
| Bucles de regeneración (WER ×3, costura, ABX del mosaico) | Cada vuelta después de una desconexión = reconexión completa | **Inmediatos**: < 1 min por párrafo | Cada vuelta necesita una sesión nueva, o hay que agruparlas (ver protocolo) |
| Determinismo (prueba de G0 "regenerar el 5.º deja idénticos el 6-10") | CUDA: hay que forzar cuDNN y cuBLAS (§3.5.4) | **Más fácil**: en CPU no hay cuDNN | CUDA, como (a) |
| Lo que no puede hacer | — | FLUX (las imágenes van por API: opción A del §4.1) y CarvalhoChat_GEC (un LLM; ya aplazado en el §9.1) | — |
| Horas de montaje | 2-3 h, y frágiles: la sincronización de Drive no garantiza el `rename` atómico en el que se basa la cola [S] | **2,5 h** (bloque 11 del MVP) | 2,5 h + **3 h** (imagen Docker o *template*, volumen de red, `gpu_run.sh`, parada automática, claves) |

**Decisión.**
- **(b), CPU local, es la opción por defecto de la Etapa 1**, porque con RTF 0,28 en TTS y 0,75 en ASR un episodio de 75 min se sintetiza y se audita en ~1 h desatendida. Está **condicionada a la prueba B0** en el equipo del promotor.
- **(c) es el plan B**, y usa **el mismo `voz_worker.py` y la misma cola**: cambiar de (b) a (c) es cambiar de dónde está la carpeta `jobs/`, no reescribir nada.
- **(a) queda descartada como *worker***. Colab solo se usa de forma **interactiva y puntual**: la medida de T4 en B0, probar FLUX o probar CarvalhoChat_GEC cuando se conceda el acceso. Es decir, el uso que Colab gratis sí permite.

**Coste de (c) por episodio, con las vueltas de regeneración incluidas** [S sobre F]:
- **Precios** [F] https://www.runpod.io/pricing:
  - RTX 4090 a 0,34 USD/h en Community;
  - RTX A5000 a 0,16 USD/h;
  - volumen de red a 0,07 USD/GB/mes.
- **Supuestos** [S]:
  - RTF en GPU de 0,05-0,1, tanto en TTS como en ASR;
  - arranque de 3-8 min por sesión.
- **Tres sesiones por episodio de 75 min**:
  - **S1, primer pase + ASR + regeneraciones automáticas por WER y costura**: ~15-25 min;
  - **S2, correcciones tras H3**: párrafos marcados en las catas, ~8-12 min;
  - **S3, ABX del mosaico tras añadir entradas al léxico**: ~8-12 min.
  - Total: **~0,6-0,9 h facturadas → 0,20-0,31 USD en 4090, o 0,10-0,15 USD en A5000**.
- Si S2 y S3 se juntan en una sola sesión (el mosaico se escucha antes de lanzarla), se ahorra un arranque.
- **Volumen de 15 GB** (modelos de voz 3,0 GB + Whisper int8 0,8 GB + entorno + margen): **1,05 USD/mes**, es decir, ~0,5 USD por episodio con 2 episodios al mes.
- **Total de (c): ~0,6-0,8 USD por episodio**, más el riesgo de un pod olvidado encendido. Para cubrirlo: `trap` + `timeout 3h` en `gpu_run.sh`, parada al vaciar la cola y alerta si `runpodctl pod list` muestra un pod vivo > 4 h [S].

#### c) Protocolo de trabajo: la cola `jobs/` (el mismo en (b) y en (c))

**Principio.** Cotovía, `g2p_override.py`, la normalización y el control de ritmo corren **siempre en local**: son CPU y tardan milisegundos. El *worker* recibe **fonemas ya resueltos** (el parche del §3.5.4 acepta `ps` precalculado en lugar de llamar a `fonemizar`) y solo hace la red neuronal. Así el *worker* no depende de Cotovía, y el canario y el hash de Cotovía se comprueban **una vez, en el orquestador**. En (c), eso quita del arranque la parte más delicada.

**Formato del trabajo** (`jobs/pending/<job_id>.json`):

```jsonc
{
  "job_id": "tts-9f3c21ab04d7e8c2",        // sha256[:16] del JSON canónico de TODOS los campos de abajo
  "tipo": "tts_parrafo",                    // tts_parrafo | asr_parrafo | abx_palabras
  "episodio": "e01-irmandinos", "parrafo": 37, "intento": 2,
  "depende_de": ["tts-1a2b…"],              // s_out del párrafo 36 (solo en el primer pase)
  "frases": [{"fonemas": "pO^rto …", "pausa_ms": 700}, …],   // salida de g2p_override + ritmo.py
  "params": {"alpha": 0.3, "beta": 0.7, "t": 0, "diffusion_steps": 5, "embedding_scale": 1, "speed": 0.92},
  "seed": 3120937, "s_in": "estado/p037.pt", "s_in_sha": "…", "ref_s_sha": "…",
  "modelo": {"repo_commit": "…", "ckpt_sha256": "…", "patch_sha": "…"},
  "salida": {"wav": "out/tts-9f3c….wav", "tempos": "out/tts-9f3c….tempos.json", "s_out": "estado/p037.out.pt"}
}
```

**Ciclo de vida y garantías**:
1. **Reclamar**: el *worker* mueve `pending/X.json` → `running/X.json` con `os.rename`, que es atómico en un mismo sistema de ficheros local o en el volumen del pod. Por eso la cola vive en disco local y **nunca en Drive**. Mientras trabaja, toca `running/X.json` cada 30 s como latido.
2. **Escribir**: primero `X.wav.tmp`, `X.tempos.json.tmp` y `X.log.json.tmp`, y después se renombran. `X.log.json` guarda: tiempos, RTF, dispositivo, versión de torch, hashes de entrada y salida, y la semilla. **El último paso es escribir `done/X.json`**, que es la señal de terminado.
3. **Idempotencia**: el `job_id` es un hash del contenido. Volver a encolar el mismo trabajo no hace nada si existe `done/X.json` y el sha del wav coincide con el anotado. Si se cambia una coma del texto, un fonema del léxico, la semilla o el `speed`, el `job_id` es otro, y el anterior queda como historial en el expediente.
4. **Reanudación tras un corte** (portátil suspendido, pod caído):
   - al arrancar, el *worker* devuelve a `pending/` todo `running/` cuyo latido tenga más de 5 min, y borra los `*.tmp`;
   - el primer pase es una **cadena**: el párrafo *k* depende del `s_out` de *k−1* (§3.5.4). Como cada `s_out` se guarda al terminar su párrafo, el pase se reanuda en el primer párrafo sin `done/` y no repite nada.
5. **Espera del orquestador**: `pipeline.py` espera por *polling* (cada 10 s) a que existan todos los `done/` de la tanda, con un plazo máximo (2× el tiempo previsto por el RTF de B0). Si se vence el plazo, se para y deja un informe en `estado.json` para el humano; **no reintenta indefinidamente**.
6. **Tandas en (c)**: los bucles automáticos (WER ×3 y costura) se resuelven **dentro de la misma sesión**. El `worker` llama a `qa_audio.py` al terminar cada párrafo y encola él mismo el siguiente intento. Solo sale del pod lo que necesita a un humano (mosaico y catas). Así S1 cubre todas las vueltas automáticas.

**Tiempo humano por sesión de cómputo** (llevado al §6):

| Opción | Por sesión | Sesiones por episodio | Por episodio |
|---|---|---|---|
| (b) CPU local | ~2-4 min: `make voz EP=…`, y a la mañana siguiente leer `qa_audio.json` | 2-3 (primer pase; correcciones de H3; ABX) | **0,1-0,2 h** |
| (c) Runpod | ~5 min: `gpu_run.sh`, comprobar que el pod se paró y revisar el log | 2-3 | **0,25-0,4 h** |
| (a) Colab (descartada) | 10-20 min: reconexión y vigilancia de la pestaña | 3 o más (una por desconexión) | 0,5-1 h |

#### d) Qué se mueve a GPU y qué no, en la Etapa 1

| Trabajo | Dónde |
|---|---|
| Cotovía, `g2p_override.py`, `ritmo.py`, `normaliza.py`, canario | CPU local, siempre |
| TTS StyleTTS2-GL + ASR Whisper-gl (primer pase y bucles) | **(b) CPU local**; si B0 falla, (c) |
| Imágenes | API (opción A, Nano Banana 2 Lite *batch*). FLUX, solo en una sesión de (c) si A no convence |
| CarvalhoChat_GEC (aplazado, §9.1) | Una sesión de (c) cuando se conceda el acceso, en la misma tanda que S1 |
| Montaje FFmpeg | CPU local, ya previsto |

#### e) Prueba B0: 10 minutos de audio en CPU y en T4, antes de G0 (semana 1)

- **Objetivo**: saber con números del **equipo real** si (b) basta antes de construir el resto de la capa de voz.
- **Material**: ~1.900 palabras del guion muestra (≈10 min de habla pura a 191 palabras/min [P]).
- **Coste**: 0 € en CPU y en Colab T4 (uso interactivo, permitido). Si se quiere el dato de 4090, ~0,1 USD en Runpod.
- **Tiempo**: **1,5 h humanas** (preparar el entorno y lanzar) + ~1 h de máquina desatendida. Van en el bloque 11 del MVP.

| Se mide | CPU del promotor | Colab T4 | (opcional) Runpod 4090 |
|---|---|---|---|
| Arranque en frío, por partes: instalación, descarga o copia de modelos, carga, hash + canario de Cotovía | ✔ | ✔ (con copia desde Drive) | ✔ (desde el volumen) |
| RTF de TTS (`diffusion_steps 5`), con 2 y 4 hilos en CPU | ✔ | ✔ | ✔ |
| RTF de ASR int8 **por párrafo** (y audio entero, solo para confirmar la alucinación del apartado a) | ✔ | ✔ (`float16`) | ✔ |
| RAM/VRAM máximas | ✔ | ✔ | ✔ |
| Determinismo: regenerar el párrafo 5 deja idénticos los párrafos 6-10 | ✔ | ✔ | — |
| WER por párrafo con la hipótesis normalizada por Cotovía | ✔ | = CPU | — |

**Reglas de decisión** [S]:
- **(b) se queda** si, en el equipo del promotor, **RTF_TTS ≤ 0,6** y **RTF_ASR ≤ 1,5**. Eso da un episodio de 75 min en ≤ 2,5 h desatendidas. Además, tiene que haber **≥ 8 GB de RAM libres**, porque TTS y ASR se ejecutan uno detrás de otro (3,65 + 1,67 GB de pico [P]).
- Si no se cumple, **(c)** con A5000 o 4090, y se suman las 3 h de su montaje.
- Si el portátil no puede quedarse encendido por la noche, también (c), aunque cumpla los RTF.
- El dato de T4 se guarda solo como referencia de GPU para la Etapa 2.

### 4.2 Etapa 2: proyecto lateral, pipeline desatendido (meses 7-18)

Cambios respecto a la Etapa 1 (solo si se pasa la Puerta 1 de `drafts/retornos.md`):

| Pieza | Cambio | Por qué |
|---|---|---|
| Orquestación | **LangGraph** (grafo con *checkpoints* y nodos `interrupt` en las 4 puertas humanas) o el **Claude Agent SDK**, ejecutado con **API key** en un pequeño servidor o en el propio ordenador por la noche | Lanzar un episodio a las 23:00 y encontrarlo en la puerta H2 por la mañana |
| LLM | API de Anthropic: **Opus 5.5 a 4/20 USD por 1M de tokens (entrada/salida), Sonnet 5.5 a 2/10 y Haiku 4.5 a 1/5; *batch* al −50 %** [F] https://claude.com/pricing. *Prompt caching* de la guía de estilo y el dossier. Claude Code (Pro) se mantiene para el desarrollo | Coste por episodio medible y predecible (§5.1) |
| RAG | Corpus acumulado de la serie con índice vectorial local (embeddings multilingües abiertos + SQLite/Chroma). El dossier por episodio sigue siendo la unidad de verificación | La serie crece y los episodios se citan entre sí |
| Voz | Si gana Nós: **la CPU local sigue sirviendo** (≈1,3-1,6 h de máquina por episodio de 2 h con el RTF medido, §4.1.1 a), lanzada por la noche. Si el equipo no da abasto o se necesita libre, GPU por horas con el mismo `voz_worker.py`: **RTX 4090 en Runpod a 0,34 USD/h (Community Cloud) o 0,74 USD/h (Secure Cloud)**; alternativa más barata: RTX A5000 a 0,16 USD/h (Community) [F oficial] https://www.runpod.io/pricing. Si gana ElevenLabs: API v3 a 0,08 USD por 1.000 caracteres (v4 a 0,08; promoción a 0,022 hasta el 12-10-2026) [F] https://elevenlabs.io/pricing/api. Si gana Gemini-TTS: **Gemini 3.8 Flash TTS a 9 USD por 1M de tokens de audio hasta el 31-12-2026 y 18 USD desde el 1-1-2027** [F] https://ai.google.dev/gemini-api/docs/pricing | Paga lo que gane el A/B |
| Imágenes | Nano Banana 2 (Gemini 3.1 Flash Image) con imágenes de referencia de estilo para más coherencia: 0,067 USD por imagen 1K y **0,034 en batch** [F] https://ai.google.dev/gemini-api/docs/pricing | La consistencia visual de la serie es un control anti-slop |
| Música | Opcional: Epidemic Sound Creator, **9,99 USD/mes en anual o 17,99 mensual**, un canal monetizado por plataforma [F] https://wyzowl.com/epidemic-sound-review/ (secundaria; oficial: https://www.epidemicsound.com/our-plans/creator-plan/) | Solo si hacen falta transiciones musicales; lo preferente sigue siendo el ambiente propio |
| Revisión humana | **Revisor/a lingüístico/a externo/a por muestreo**: el 10-20 % de un episodio de cada dos, a 0,015-0,03 €/palabra [R `voz_guion.md` §3] (≈40-80 € por muestra). Su tarea principal es **mejorar la guía de estilo y la lista negra**, no corregir episodios | Sube el listón de todo lo que venga después |
| Publicación | Subida por la API (`videos.insert`, 1 unidad del cupo de subidas, 100 al día [F] https://developers.google.com/youtube/v3/docs/videos/insert), con `status.containsSyntheticMedia` [F, misma URL], **solo tras superar la auditoría de verificación del proyecto API**. Hasta entonces, manual. La publicación final siempre la pulsa un humano | Ahorra 10-15 min por episodio |
| Derivado audio | El máster de audio se publica como pódcast (RSS → Spotify, iVoox, Apple). Spotify Partner Program en España desde el 20-10-2026 [R `retornos.md` §7] | Coste marginal ~0 |

### 4.3 Etapa 3: apuesta seria (solo si se pasan las puertas 1-3)

| Pieza | Opción | Coste |
|---|---|---|
| Voz licenciada de locutor/a galego/a | (a) ElevenLabs Professional Voice Cloning (desde Creator, 22 USD/mes) sobre v3/v4 con galego; (b) *fine-tune* de StyleTTS2-GL de Nós con 1-4 h grabadas en estudio | Licencia 2.000-6.000 € + *revenue share* 5-15 % [R, S]; *fine-tune* (b): ~20-60 h de GPU A40/4090 ≈ 10-30 USD [S] |
| Pistas es/pt (multi-audio de YouTube) | Adaptación por LLM **desde el guion galego firmado** + revisión nativa es (promotor) / pt (revisor pagado) + TTS en es/pt. Hasta 6 pistas por vídeo [F] https://blog.novadub.ai/blog/en/youtube-multi-audio-complete-guide-2026/ (secundaria); ayuda oficial https://support.google.com/youtube/answer/13338784?hl=en. **Verificar que el galego se admite como idioma original en Studio** [R, pendiente] | ~3-8 USD de IA por pista + revisión |
| Revisor galego recurrente | Muestreo sistemático de cada episodio, o lectura completa de los episodios "insignia" | Lectura completa de 14k palabras = 210-420 € [R]; solo para episodios clave |
| Orquestación | La misma de la Etapa 2; se añaden ramas de localización al grafo | — |

---

## 5. Costes por episodio y por hora de vídeo

### 5.1 Consumo de LLM por episodio de 2 h (API, precios de lista) [S sobre precios F]

Supuestos: 13.800 palabras ≈ 28-39k tokens de salida por versión completa (~2-2,8 tokens por palabra en galego [S]; el informe previo usa 1,6 [R], así que aquí se es conservador).

| Agente | Modelo | Entrada (tokens) | Salida (tokens) | USD |
|---|---|---|---|---|
| Investigador | Sonnet 5.5 | 250k | 15k | 0,65 |
| Escaleta | Opus 5.5 | 40k | 6k | 0,28 |
| Guionista (14 capítulos) | Opus 5.5 | 252k | 39k | 1,79 |
| Lingüista (LLM) | Sonnet 5.5 | 168k | 30k | 0,64 |
| Verificador (anacronismos, leyendas; el juez de respaldo va aparte en §5.2) | Sonnet 5.5 | 200k | 15k | 0,55 |
| Director visual | Sonnet 5.5 | 60k | 25k | 0,37 |
| Auditor (LLM juez) | Opus 5.5 | 120k | 8k | 0,64 |
| Retrabajo (+30 % de guionista y lingüista) | — | — | — | 0,73 |
| Metadatos | Haiku 4.5 | 30k | 4k | 0,05 |
| **Total precio de lista** | | | | **≈ 5,7 USD** |
| **Con *prompt caching* + *batch* en las etapas no interactivas** | | | | **≈ 3 USD** [S] |

Precios: https://claude.com/pricing [F]. Coincide en orden de magnitud con los 3,4 USD del informe previo [R `voz_guion.md` §2.1]. Episodio de 75 min: ×0,62 ≈ **3,5 USD de lista (≈2 USD optimizado)**, o **0 € marginal dentro de la suscripción Pro** [S].

### 5.2 Coste variable por episodio (sin cuotas fijas)

**Etapa 1: 75 min narrados, ~53k caracteres, ~75 planos + 40 % de repeticiones ≈ 105 imágenes** [S]

| Partida | Stack mínimo | Stack típico | Stack "premium" |
|---|---|---|---|
| LLM | 0 (Pro) | 0 (Pro) | 3,5 USD (API de lista) |
| Voz + QA ASR | 0 (Nós en CPU local, RTF medido [P]) | 0 en CPU, o **0,6-0,8 USD** si B0 obliga a Runpod (§4.1.1 b) [S sobre F] | 4,2 USD (ElevenLabs v3: 53k × 0,08/1k) [F] |
| Imágenes | ~0,2 USD (FLUX en Runpod, ~0,5 h de 4090) [S sobre F] | 1,8 USD (Nano Banana 2 Lite batch) [F] | 3,5 USD (Nano Banana 2 Lite sin batch) [F] |
| Juez factual (Gemini) | 0 (capa gratuita, solo para pruebas) | 0,1 USD | 0,1 USD |
| Montaje, ambiente, mapas | 0 | 0 | 0 |
| **Total por episodio** | **≈ 0,2 USD** | **≈ 1,9 USD en CPU (2,5-2,7 con Runpod)** | **≈ 11 USD** |
| **Por hora narrada** (1,25 h) | ≈ 0,2 USD/h | **≈ 1,5 USD/h** (2,0-2,2) | ≈ 9 USD/h |
| Por hora de vídeo publicada (con 25 min de cola de ambiente ≈ 1,67 h) | ≈ 0,1 USD/h | ≈ 1,1 USD/h (1,5-1,6) | ≈ 6,6 USD/h |

**Etapa 2: 2 h narradas, ~85k caracteres, ~120 planos + 40 % ≈ 170 imágenes** [S]

| Partida | Stack Nós | Stack Gemini-TTS | Stack ElevenLabs |
|---|---|---|---|
| LLM (API optimizada) | 3,0 USD | 3,0 USD | 3,0 USD |
| Voz | 0 en CPU local, o 0,5 USD (≈1,5 h de 4090 a 0,34 USD/h, TTS + ASR) [S sobre F] | 1,6 USD en 2026 / 3,2 USD en 2027 (7.200 s × 25 tokens/s = 180k tokens × 9 o 18 USD/M) [F] | 6,8 USD (85k × 0,08/1k, v3) [F] |
| QA ASR (si no va con el TTS) | incluido | 0,3 USD (GPU) | 0,3 USD |
| Imágenes (Nano Banana 2 batch, 0,034) | 5,8 USD | 5,8 USD | 5,8 USD |
| Juez factual (Gemini 3.8 Flash batch) | 0,2 USD | 0,2 USD | 0,2 USD |
| **Total por episodio** | **≈ 9,5 USD** | **≈ 11-12,5 USD** | **≈ 16,1 USD** |
| **Por hora narrada** | **≈ 4,8 USD/h** | ≈ 5,5-6,3 USD/h | ≈ 8,1 USD/h |

Lectura: **incluso el stack más caro se queda por debajo de 10 USD por hora narrada.** Una hora humana de revisión a 15 €/h (el valor que usa `retornos.md`) ya cuesta más que toda la IA de un episodio.

### 5.3 Caja mensual por etapa

| Partida (€/mes) | Etapa 1 (2 ep. × 75 min) | Etapa 2 (4 ep. × 2 h) | Fuente |
|---|---|---|---|
| Claude Pro (incluye Claude Code) | 14,8-17,4 (17-20 USD) | 14,8-17,4 | [F] https://claude.com/pricing |
| GPU por horas en Runpod (solo si B0 descarta la CPU): volumen de 15 GB + sesiones | 0-1,4 (1,05 USD de volumen + 2 × ~0,15-0,3 USD) | 0-3 (volumen + 4 × ~0,5 USD) | [F] https://www.runpod.io/pricing, §4.1.1 |
| Variable de IA (§5.2, típico) | ~3,3 (2 × 1,9 USD) | ~33-56 (4 × 9,5-16,1 USD) | §5.2 |
| Música con licencia | 0 | 0-15,6 (Epidemic) | [F secundaria] |
| Revisor lingüístico por muestreo | 0 | 40-80 (1-2 muestras/mes; con 1 cada 2 episodios, 2 al mes) | [R] |
| **Total** | **≈ 18-24 €/mes** | **≈ 88-170 €/mes (central ~110)** | |
| Límite del promotor | < 50 € ✔ | 50-200 € ✔ | `contexto.md` |

Coincide con el modelo financiero de `drafts/retornos.md` (35 €/mes y 110 €/mes). Allí la Etapa 1 lleva algo más de margen para imprevistos.

---

## 6. Horas humanas por episodio

### 6.1 Etapa 1 (75 min, ~8.600 palabras) [S, a medir en el piloto]

| Tarea | Quién | Horas |
|---|---|---|
| Elegir tema y ángulo, redactar el brief | Promotor | 0,3 |
| Vetar o añadir fuentes | Promotor | 0,2 |
| **Revisión estratificada de afirmaciones** (100 % del estrato A, incluidas las anclas `AXUSTADA`/`MATIZ_ALTERADO` que el ruido de copia pasa a A, + muestra de B, con la cita al lado; §3.6.4) | Promotor | **0,7-0,8** |
| **Bloqueos de anclaje escalados** (≤ 2 % tras el reintento automático: ≤ 3 filas × ~2 min; §3.6.4) | Promotor | **0-0,1** |
| Puerta H1: escaleta | Promotor | 0,3 |
| **Puerta H2: lectura íntegra y corrección del guion** (~3.500-4.000 palabras/h con incidencias ya marcadas; repartido por capítulos entre el promotor y su mujer) | Promotor + mujer | **2,2-2,5** |
| Resolver incidencias "contradita" o "consultar" | Promotor | 0,3 |
| Puerta H3: mosaico de risco + 10 primeros minutos + 3 catas + hoja de contacto | Promotor (mujer en el mosaico) | 0,8 |
| Supervisar el pipeline (relanzar etapas, ajustar *prompts*) | Promotor | 0,5-1 |
| **Sesiones de cómputo de voz**: lanzar `make voz`, leer `qa_audio.json` y relanzar tras un corte; 2-3 sesiones por episodio (§4.1.1 c). En (b) CPU: 0,1-0,2; en (c) Runpod: 0,25-0,4 | Promotor | **0,1-0,2** |
| Puerta H4: metadatos, subida, declaración y publicación | Promotor | 0,4 |
| **Total por episodio** | | **≈ 5,8-6,9 h** (6,0-7,1 con Runpod) |

- Con 2 episodios al mes, son **~11,6-13,8 h al mes, ≈ 2,7-3,2 h/semana**. Queda ~1 h/semana para comentarios, analítica y mejoras. **Cabe en 4 h/semana** ✔. Si salta el umbral del estrato B (§3.6.4), la revisión completa de B añade ~0,6 h a ese episodio.
- Aviso: los **3 primeros episodios** costarán el doble o más (guía de estilo, lista negra y léxico vacíos) [S].
- Esfuerzo de construcción inicial (no recurrente) [S]: **MVP de 32,5-35,5 h** (§9.1), más ~6-8 h humanas de escucha y juicio en G0/G1, más **12-20 h tras el MVP** para los controles aplazados, repartidas entre los episodios 2 y 6. En total, **~50-64 h** repartidas en unos 6 meses (la v2 estimaba 31-50 h, pero sin la integración del cómputo ni la extracción de citas), **ordenado para que el primer episodio no espere a los controles que aún no sirven**. Los prototipos de `g2p_override.py` y `verifica_citas.py` ya existen [P].

### 6.2 Etapa 2 (2 h, ~13.800 palabras)

| Tarea | Horas |
|---|---|
| Brief + escaleta + vetar fuentes | 0,5 |
| Revisión estratificada de afirmaciones, con las filas que el ruido de copia pasa a A (§3.6.4) | 1,0-1,2 |
| Bloqueos de anclaje escalados (≤ 5 filas × ~2 min) | 0-0,17 |
| Lectura íntegra del guion (promotor + mujer) | 3,5-4 |
| Incidencias y verificación | 0,4 |
| Escucha dirigida + hoja de contacto (el léxico ya maduro acorta el mosaico) | 0,7 |
| Supervisión (pipeline desatendido) | 0,3 |
| Sesiones de cómputo de voz (CPU nocturna o Runpod; §4.1.1 c) | 0,1-0,25 |
| Publicación + pódcast | 0,3 |
| **Total** | **≈ 6,8-7,8 h/episodio** |

- A 6-10 h/semana: **3 episodios/mes** caben con holgura (~20,5-23,5 h al mes de producción + gestión). **4 al mes** solo en el extremo alto (~27-31 h + gestión ≈ 8-9 h/semana) [S].
- El ahorro de la Etapa 2 **no viene de revisar menos**. La lectura íntegra es innegociable por la exigencia de calidad del galego. Viene de supervisar menos y de un guion que llega más limpio a la lectura, gracias a la guía de estilo afinada por el revisor externo.

### 6.3 Tiempo de máquina por episodio de 2 h (para planificar la noche) [S; TTS y ASR sobre medida propia P]

| Etapa | Tiempo de reloj estimado |
|---|---|
| Investigación + escaleta | 20-40 min |
| Guion + lingüista + verificador (con vueltas) | 1-2 h (batch: hasta 24 h de plazo, normalmente mucho menos) |
| TTS StyleTTS2 en CPU local (RTF 0,28 medido en 4 vCPU [P], + 15 % de regeneraciones; un portátil puede ir 0,7-2 veces más lento [S], lo mide B0) | 23-28 min (hasta ~1 h) |
| ASR Whisper-gl int8 por párrafo (RTF 0,75 [P]) + QA de audio | 55-65 min (hasta ~2 h) |
| Imágenes (170 por API) | 20-40 min |
| Render FFmpeg de 2 h a 1080p con Ken Burns (CPU de portátil) | 1-3 h |
| **Total** | **≈ 4,5-9 h: se lanza por la noche**. TTS/ASR y el render compiten por la misma CPU y van en serie; si no caben en una noche, la voz va una noche y el render la siguiente, o la voz pasa a Runpod (§4.1.1) |

---

## 7. Cadencia sostenible

| Etapa | Cadencia recomendada | Vídeo narrado al mes | Horas humanas al mes | Por qué no más |
|---|---|---|---|---|
| 1 | **2 episodios/mes** de 75 min | 2,5 h | ~11,6-13,8 | Límite de 4 h/semana; la lectura íntegra manda |
| 2 | **3 episodios/mes** de 2 h (4 si sobra tiempo) | 6-8 h | ~20-30 | 6-10 h/semana; más cadencia sube el riesgo de *inauthentic content* (`retornos.md` §6 [R]) |
| 3 | 4 episodios/mes + pistas es/pt | 8 h × idiomas | ~30-40 (con revisores pagados) | Cuello de botella: revisión nativa por idioma |

**Sobre la "compilación mensual" de `formato.md`**: aquí se recomienda **no publicarla en el canal principal durante la Etapa 1-2**. El informe de retornos aconseja "nada de relleno repetido, bucles ni recopilaciones de vídeos propios" [R `retornos.md` §6.1], y una compilación de material ya publicado es justo el patrón *reused* que un revisor humano de YouTube podría señalar. Si se hace, que sea con presentación y transiciones nuevas narradas, como indica la propia pieza de formato. Mejor todavía: llevar las compilaciones solo al pódcast. **Pendiente de resolver en el gauntlet entre piezas.**

---

## 8. Controles anti-"slop" (para no perder la monetización por contenido inauténtico)

**Qué dice la norma** [R, citas literales de `retornos.md` §6]:
- No monetizable: "AI-generated content made with generic or unoriginal templates giving the impression of mass production"; "Similar or repetitive content with low educational value" [F] https://support.google.com/youtube/answer/1311392?hl=en.
- Aclaración del 16-jul-2026: "material that can be easily made with AI, CGI, or templates, with little variation from video to video"; "Any YouTube channel that has too much of any of these three types of content will not be able to monetize" [F] https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/.
- Criterio subjetivo: contenido que "mimics existing formats to a degree that the videos feel interchangeable" [F] https://www.techtimes.com/articles/320629/20260715/youtube-wiped-35m-subscribers-over-ai-slop-now-its-judging-your-taste.htm.
- Permitido: la misma intro y outro con sustancia distinta, y series con "distinct storyline, focus, or concept" [F] support.google.com (misma URL).

**Controles** (cada uno con evidencia en el expediente del episodio):

| # | Control | Riesgo de la política que ataca | Cómo se verifica |
|---|---|---|---|
| 1 | **Investigación propia por episodio**: dossier + `afirmacions.csv` + **bibliografía en la descripción** | "low educational value" | QA: 0 anclas sin correspondencia en la fuente, citas extraídas de la fuente con desplazamientos, revisión estratificada firmada (§3.6); ≥ 8 fuentes distintas por episodio [S] |
| 2 | **Ángulo único declarado** en el brief ("que aporta este episodio que non estea nos anteriores") | "little variation from video to video" | Brief firmado; el LLM juez compara con los briefs previos |
| 3 | **Guard de similitud** entre guiones (coseno < 0,85; < 2 % de 8-gramas compartidos) | "generic templates", "interchangeable" | `qa_texto.json` |
| 4 | **Aperturas distintas**: escena de lugar propia de cada episodio; la fórmula de bienvenida fija ocupa como mucho 1 frase | plantilla repetitiva | QA de n-gramas en los primeros 90 s |
| 5 | **Series con arco** (p. ej. "Gallaecia sueva", "Irmandiños", "O mar") en lugar de temas sueltos intercambiables | "distinct storyline, focus, or concept" (permitido) | Plan editorial trimestral |
| 6 | **Voz editorial humana**: lectura íntegra, correcciones propias y erratas publicadas en la descripción o el comentario fijado | "mass production" | `firma_guion.yaml` + historial de git |
| 7 | **Imágenes hechas para cada plano**, con ≤ 10 % reutilizadas y mapas propios | "easily made with AI… little variation" | *Hash* perceptual en QA |
| 8 | **Cadencia moderada** (2-4 al mes) | "impression of mass production" | Calendario |
| 9 | **Sin bucles, sin directos 24/7 repetidos y sin recopilaciones de material propio sin narración nueva** | *reused content* | Regla editorial |
| 10 | **Transparencia**: nota de proceso en la descripción (galego) y **declaración "contenido alterado o sintético"** cuando haya imágenes realistas de hechos o personas. Con estilo pictórico no fotorrealista no es obligatoria, pero la nota de proceso se pone siempre [R `retornos.md` §6.2] | Retirada o suspensión del YPP por no declarar | Casilla de Studio / `status.containsSyntheticMedia` en la API [F] |
| 11 | **Crédito y licencia de la voz** (p. ej. "Voz sintética: Proxecto Nós (USC), modelo X, Apache-2.0") y confirmación escrita de Nós para el uso comercial [R `voz_guion.md` §1.1] | Reputación ante la comunidad galega | Correo archivado en el expediente |
| 12 | **Expediente de evidencias** por episodio (dossier, versiones, informes QA, firmas) | Apelación ante YouTube; **excepción del art. 50 del AI Act** (revisión humana + responsabilidad editorial) [R `retornos.md` §6.3] | Carpeta del episodio en git |

**Nota de proceso modelo para la descripción** [S, pendiente de revisión lingüística]:
> *Sobre este episodio: o guión elaborouse con axuda de intelixencia artificial a partir das fontes citadas máis abaixo, e foi lido, corrixido e verificado por persoas. A narración é unha voz sintética ([modelo], Proxecto Nós – USC, licenza Apache-2.0). As imaxes son ilustracións xeradas con IA. Se atopas algún erro, indícanolo nos comentarios: publicaremos as correccións aquí.*

---

## 9. Plan de puesta en marcha (Etapa 1, a 4 h/semana) [S]

| Semanas | Entregable | Puerta técnica |
|---|---|---|
| 1-3 | **Semana 1: prueba B0** (§4.1.1 e): 10 min de audio con la voz de Nós en la CPU del promotor y en Colab T4 (uso interactivo): RTF de TTS y de ASR, arranque en frío con Cotovía, RAM y determinismo. **Decide dónde corre la voz**: (b) CPU local o (c) Runpod. Después: `voz_worker.py` + cola `jobs/` integrados con `pipeline.py` (bloque 11 del MVP). Kit A/B de voz escuchado a ciegas (se prepara aparte). Repositorio con la estructura de carpetas y subagentes vacíos. Correo a Proxecto Nós sobre el uso comercial. **Capa de pronunciación y ritmo** (§3.5): Cotovía fijado (§3.5.9) + `g2p_override.py` + parche (velocidad, semilla, pausas, `s_prev` por párrafo); **prueba de 50 palabras de riesgo** y **A/B de ritmo** (4 variantes, más `t` 0 frente a 0,7) sobre las 1-2 voces finalistas | **B0**: RTF_TTS ≤ 0,6, RTF_ASR ≤ 1,5 y ≥ 8 GB de RAM libres en la CPU del promotor → (b); si no, (c). **G0**: se elige voz **solo si** se cumplen tres cosas: (1) pasa la prueba de 50 palabras (≥ 90 % de corregidas bien, ≥ 8/10 pares é/ó audibles, 0 regresiones); (2) hay un `speed` y un presupuesto de pausas que den 110-125 palabras/min sin perder naturalidad; (3) regenerar el párrafo 5 deja idénticos los párrafos 6-10 (§3.5.4, §3.5.8) |
| 3-4 | Prueba ciega de redactor: el mismo capítulo con 3-4 modelos, puntuado por el promotor y su mujer. Guía de estilo v0 + lista negra v0 + 3 párrafos modelo validados | **G1**: redactor elegido; ≥ 4/5 en corrección galega |
| 4-7 | Investigador (con anclas) + `extrae_cita.py` + guionista + lingüista + `verifica_citas.py` + juez Gemini + hoja de revisión estratificada + `qa.py` (texto) sobre un **episodio corto de prueba de 20 min** | **G2**, con cinco condiciones: (1) el guion de 20 min pasa el QA y la lectura humana en menos de 1 h; (2) **prueba adversarial** (§3.6.5): **ninguna de las 5 anclas falsas queda `ANCORADA`** (3 bloqueadas, cifra y matiz señalados y en el estrato A); (3) el juez marca ≥ 4 de 5 respaldos falsos, con ≤ 1 falso positivo en 10 reales; (4) **≤ 2 % de bloqueos falsos** en ≥ 100 anclas del investigador real y ≤ 15 % de `AXUSTADA` + `MATIZ_ALTERADO`, con la primera fila de `metricas_verificacion.csv` escrita; (5) los canarios activos en `qa.py` |
| 7-9 | TTS por párrafos (a través de la cola) + ASR por párrafo + mosaico + montaje FFmpeg + biblia visual | **G3**: máster de 20 min sin fallos de "sono seguro"; la mujer del promotor lo aguanta 20 min sin quejas de lengua |
| 10-12 | Primer episodio de 75 min, publicado | Entra en las puertas de negocio de `drafts/retornos.md` |

Calendario ajustado a las horas [S]: el MVP (32,5 h con la voz en CPU, 35,5 h si hace falta Runpod; §9.1) y la evaluación de G0/G1 (~6-8 h) suman **38,5-43,5 h**. A 4 h/semana son **10-11 semanas**, con el primer episodio publicable entre la **semana 10 y la 12**. B0 y la prueba de 50 palabras van al principio a propósito: si la máquina no da abasto o la voz no se deja corregir, se sabe antes de invertir en el resto.

Si G0 o G1 fallan (ninguna voz o ningún redactor llega al listón del galego), **el proyecto se para aquí**, con un coste de ~40 € y ~18-22 h (bloques 1, 6 y 11 del MVP + evaluación de G0/G1). Esa es la puerta más barata de todo el plan.

### 9.1 MVP explícito (32,5-35,5 h de construcción) y lo que se aplaza

Criterio de recorte: el MVP incluye **todo lo que protege lo innegociable** (galego, veracidad y pronunciación) y lo mínimo para producir un máster. Se aplaza lo que **todavía no puede funcionar** (la similitud necesita episodios previos) o lo que **una mirada humana cubre mientras tanto** (hoja de contacto, escucha).

| # | Bloque del MVP | Horas [S] | Nota |
|---|---|---|---|
| 1 | Repositorio, estructura por episodio, `estado.json`, 6 subagentes y comando `/episodio` | 3 | Sin LangGraph |
| 2 | Investigador: ingestión (Galipedia con `revid` y *user-agent*; `pdftotext`/Tesseract `glg`; `sha256` e intervalos de cada unidad de localizador), `fontes.yaml`, `afirmacions.csv` con anclas | 3,5 | |
| 3 | **`extrae_cita.py`** (búsqueda en la página declarada ±1, FTS5 `NEAR` para fuentes largas, `rapidfuzz`, diff, estados, 3 pasajes candidatos para el reintento) + `verifica_citas.py` (R1-R5, integridad por hash y `[ini, fin)`, fechas `NEAR`) + canarios + `metricas_verificacion.csv` | 3,5 | Prototipos de los dos hechos y probados [P]; +2 h respecto a la v3 entre los bloques 2 y 3 |
| 4 | Juez Gemini + `revision_afirmacions.html` (estratos, semilla, umbral) | 2,5 | |
| 5 | Lingüista: Hunspell-gl + LanguageTool (Docker) + lista negra + LLM revisor | 2,5 | |
| 6 | Voz: Cotovía fijado + `g2p_override.py` + parche (`speed`, semilla, pausas, `s_prev` por párrafo, `pred_dur`) + `ritmo.py` | 5 | Prototipo del wrapper hecho [P] |
| 7 | ASR con WER por párrafo + `silencedetect` + `loudnorm` | 2 | |
| 8 | Mosaico de risco con los tiempos del TTS (`tempos_palabra.json`) | 1,5 | |
| 9 | Imágenes: `planos.csv` → API *batch* → hoja de contacto + luminancia + OCR | 2 | |
| 10 | Montaje FFmpeg + capítulos + `metadatos_yt.json` | 3 | |
| 11 | **Integración del cómputo de voz** (§4.1.1): prueba B0 (1,5 h: entorno, 10 min de audio en CPU y T4, informe) + `voz_worker.py` que carga el modelo una vez y atiende `jobs/` (formato, `job_id` por hash, `rename` atómico, latido, reanudación, `done/`) + espera con plazo en `pipeline.py` + bucle WER/costura dentro del *worker* (2,5 h) | 4 | Nuevo en la v5. Los *scripts* de medida ya existen [P] (`drafts/bench_cpu/`) |
| 11c | *Solo si B0 descarta la CPU*: imagen o *template* de Runpod, volumen de red con los modelos, `gpu_run.sh` (crear → subir cola → ejecutar → bajar → parar, con `trap` y `timeout`), alerta de pod vivo | +3 | Plan B (c) |
| | **Total** | **32,5 en (b) / 35,5 en (c)** | Sube 4-7 h respecto a la v4: el bloque 6 no incluía la conexión entre el orquestador y el cómputo |

**Aplazado, con fecha** (12-20 h en total, entre los episodios 2 y 6 y **siempre antes de pedir la entrada en el YPP**):

| Control aplazado | Por qué puede esperar | Qué lo cubre mientras tanto | Cuándo entra |
|---|---|---|---|
| Similitud entre guiones (*embeddings* + 8-gramas) | Con 0-2 episodios no hay con qué comparar | El brief declara el ángulo; el humano lo compara con los anteriores | Antes del episodio 4 |
| *Hash* perceptual de imágenes | Igual: no hay imágenes previas | Imágenes nuevas por plano (regla editorial) | Antes del episodio 4 |
| CLIP (coherencia de estilo) | La biblia visual se está afinando todavía | Hoja de contacto (H3) | Episodio 5-6 |
| ECAPA (timbre entre párrafos) | Con `ref_s` fijo, `s_prev` guardado y semilla por párrafo, el riesgo es bajo | Control de costura de estilo (§3.2) + catas humanas | Episodio 5-6, o antes si las catas detectan saltos |
| NeMo Forced Aligner | Solo hace falta si la voz no es StyleTTS2 | Tiempos del propio TTS (§3.5.6) | Solo si cambia la voz |
| Detector de caras | Estilo pictórico + *prompt* negativo | Hoja de contacto | Episodio 5-6 |
| CarvalhoChat_GEC | La base es *gated*: hay que pedir acceso | Hunspell + LanguageTool + LLM revisor + lectura íntegra | Cuando se conceda el acceso |
| Wikidata SPARQL | Las fechas ya pasan al 100 % por el estrato A | Revisión humana + fechas `NEAR` del corpus | Episodio 4-6 |

---

## 10. Riesgos operativos y mitigación

| Riesgo | Prob. [S] | Impacto | Mitigación |
|---|---|---|---|
| Límites de uso de Claude Pro insuficientes para el pipeline | Media | Retraso | Mover la redacción a la API (+3-4 USD por episodio) |
| StyleTTS2-GL inestable en tiradas largas (es reciente: publicado jun/jul-2026) | Media | Voz inservible | Síntesis por frase y párrafo + WER por bloque + regeneración con semilla por párrafo; *fallback* a VITS o Azure |
| El modelo no hace audible el contraste é/ó aunque reciba los fonemas correctos (límite de sus datos de entrenamiento) | Media [S] | Errores de apertura que el léxico no arregla | Se detecta en la prueba G0 de 50 palabras (§3.5.8), antes de producir nada; siguiente voz del A/B o *fine-tune* en la Etapa 3 |
| Nós actualiza `inference.py` o `phonemize.py` y rompe el parche | Media | Pipeline de voz parado | Copia fijada por *commit* (`sha` del repositorio) en el propio repo; el parche vive en `patches/`; la prueba de regresión del wrapper (léxico vacío = salida idéntica al original) se ejecuta al actualizar |
| El léxico introduce errores (fonema mal elegido) | Media | Error sistemático en todos los episodios | Cada entrada lleva fuente (*Dicionario de pronuncia*) y pasa por ABX en el mosaico antes de consolidarse; validación contra el inventario |
| Licencia comercial de Nós no confirmada | Media | Bloqueo de la monetización con esa voz | Pedir confirmación escrita antes de la Puerta 1; plan B de voz del A/B |
| El LLM "castellaniza" el galego en textos largos | Alta | Rechazo de la comunidad | Lista negra, GEC, LLM revisor distinto, lectura íntegra humana, *few-shot* nativo |
| Errores históricos detectados por comentaristas | Media | Reputación | Citas extraídas de la fuente por herramienta (nunca copiadas por el LLM) y comprobadas por hash, desplazamientos y FTS5, juez de otra familia, 100 % del estrato de riesgo revisado por humano, fuentes en la descripción y erratas públicas (que devuelven el estrato B al 100 % durante 2 episodios) (§3.6) |
| Cita real pero fuente equivocada o contradictoria (p. ej. las dos fechas de la ejecución de Pardo de Cela en el mismo artículo [P]) | Media | Error "con fuente" | Fechas `NEAR` del corpus en la hoja de revisión; ≥ 2 fuentes independientes para toda fecha o cifra que abra un capítulo [S]; el investigador prioriza fuentes académicas sobre Galipedia |
| El verificador queda ciego sin que nadie lo note (índice vacío, tokenizador cambiado) | Baja | Citas falsas que pasan | 5 canarios por ejecución + prueba de `CITA_MANIPULADA`: si alguno no da el estado esperado, `qa.py` aborta (§3.6.5) |
| El LLM investigador ancla mal muchas afirmaciones reales (paráfrasis en vez de copia) y H2 se atasca en bloqueos | Media [S] | Horas humanas no presupuestadas | Extracción por herramienta; reintento automático con 3 pasajes candidatos; métrica en G2 (≤ 2 %) y alarma por episodio en `metricas_verificacion.csv` (> 5 rebloqueos: se para y se corrige el *prompt*) (§3.6.2, §3.6.5) |
| El umbral de `dist` deja pasar como `AXUSTADA` un empalme o una paráfrasis interesada | Media [P: el margen simulado es estrecho, 0,198 frente a 0,147] | Una cita con matiz cambiado llega al guion | `AXUSTADA` nunca pasa sola: estrato A al 100 %, con el diff; el juez y el humano ven siempre la cita **real**, no el ancla (§3.6.2, §3.6.4) |
| Se usa otro binario de Cotovía (`PATH`) y cambian las vocales abiertas | Media [P: ocurre en este entorno] | Regresión de pronunciación silenciosa | Ruta absoluta + `-D` + hash en `versions.lock` + canario *eu porto* al arrancar (§3.5.9) |
| Imágenes con anacronismos o texto basura | Alta | Estética "slop" | OCR, hoja de contacto, biblia visual, estilo pictórico no realista |
| La CPU del promotor es mucho más lenta que la del servidor medido, o el portátil no puede quedarse encendido por la noche | Media [S] | La voz no cabe en una noche | Se sabe en B0 (semana 1), antes de construir; plan B (c) con el mismo `voz_worker.py` (+3 h de montaje, ~0,6-0,8 USD por episodio) (§4.1.1) |
| Whisper alucina en audios largos y el WER da falsos fallos masivos | **Cierta si se pasa el audio entero** [P: WER 48-53 % sobre un audio correcto] | Regeneraciones inútiles y horas de escucha | ASR siempre por párrafo, `condition_on_previous_text=False`, hipótesis normalizada por Cotovía; canario de audio conocido en cada ejecución del QA [S] |
| Un pod de Runpod se queda encendido (solo en c) | Baja | 0,34 USD/h hasta que alguien lo vea | `trap` + `timeout 3h` en `gpu_run.sh`, parada al vaciar la cola, alerta si hay un pod vivo > 4 h |
| Corte a mitad del primer pase de voz (suspensión, caída del pod) | Media | Retraso | Cola idempotente con `s_out` guardado por párrafo: se reanuda en el primer párrafo sin `done/` (§4.1.1 c) |
| Render lento en el portátil | Media | Retraso | Preescalar imágenes, bajar a 24 fps, Ken Burns precalculado por plano, render nocturno |
| Subida por API bloqueada en privado | Cierta sin auditoría | Ninguno en la Etapa 1 | Subida manual |
| Cambio de precios o retirada de modelos (Gemini TTS y Gemini 3.8 Flash se duplican el 1-1-2027; Imagen 4 Fast se apagó el 17-08-2026) | Cierta | Bajo | El coste de IA es < 10 USD/h; cada proveedor va detrás de un adaptador y se cambia sin rehacer el grafo; `versions.lock` fija también los ids de modelo |

---

## 11. Supuestos que el piloto debe medir

1. Horas humanas reales por episodio (objetivo ≤ 6 h en el episodio 4 de la Etapa 1).
2. Palabras/hora de la lectura humana con incidencias preseñaladas (supuesto: 3.500-4.000).
3. RTF de StyleTTS2-GL y de Whisper-gl **en la CPU del promotor** (B0; referencia medida [P] en 4 vCPU de servidor: 0,28 y 0,75) y en T4; arranque en frío real; porcentaje de párrafos regenerados por WER; y tasa de falsas alarmas del WER por párrafo con la hipótesis normalizada por Cotovía (referencia [P]: 6 de 15 alarmas por frase eran solo números).
4. Umbral de WER útil con el Whisper galego de Nós (¿el 6 % separa bien los errores reales del ruido del ASR?).
5. Consumo real de tokens por episodio y si cabe en el plan Pro.
6. Tasa de rechazo de imágenes (supuesto: 40 %).
7. Tiempo de render de 2 h en el equipo del promotor.
8. Tamaño y crecimiento del léxico de pronunciación (señal de que la voz mejora) y porcentaje de palabras del mosaico que necesitan entrada nueva por episodio (objetivo: que baje).
9. Si el contraste é/ó llega al audio cuando se fuerzan los fonemas (prueba G0, §3.5.8).
10. Velocidad natural de la voz ganadora (palabras/min de habla pura), `speed` óptimo y escala de pausas `k` real por párrafo (§3.5.4).
11. Factor de conversión duración→muestras del TTS y error de los tiempos por palabra frente a marcas manuales (§3.5.6).
12. Afirmaciones por episodio y proporción del estrato A (supuesto: ~1 cada 55 palabras; A ≈ 40 %), y segundos por fila de la hoja de revisión (supuesto: 25-35 s) (§3.6.4).
13. **Tasa de bloqueos falsos del anclaje con el LLM real** (objetivo ≤ 2 %), proporción de anclas `AXUSTADA` + `MATIZ_ALTERADO` (supuesto: 10-15 %; en simulación, 5-13 %) y `dist_p95` por episodio; si el umbral de 0,20 sigue separando ruido de fraude con anclas reales (§3.6.2, §3.6.5).
14. Acuerdo entre el juez Gemini y el humano en el estrato A, y tasa de error del estrato B por episodio (`metricas_verificacion.csv`): son las cifras que dicen si se puede bajar la muestra o hay que subirla.
15. Si el MVP cabe de verdad en 32,5-35,5 h (se registra el tiempo por bloque del §9.1).

---

### Fuentes verificadas en esta versión (29-09-2026)

- Claude, planes y precios de la API (Pro 20 USD/mes con Claude Code; Opus 5.5 4/20, Sonnet 5.5 2/10, Haiku 4.5 1/5 USD por 1M de tokens; batch −50 %): https://claude.com/pricing
- Gemini API: Nano Banana 2 / Lite / Pro, Gemini 3.8 Flash TTS (9 USD → 18 USD por 1M de tokens de audio el 1-1-2027): https://ai.google.dev/gemini-api/docs/pricing
- Gemini API, retirada de modelos (Imagen 4 / 4 Fast / 4 Ultra apagados el 17-08-2026; sustituto `gemini-3.1-flash-image`): https://ai.google.dev/gemini-api/docs/deprecations
- Gemini 3.8 Flash como juez (0,75/3,75 USD por 1M hasta el 31-12-2026; 1,50/7,50 desde el 1-1-2027; *batch* −50 %; la capa gratuita usa el contenido): https://ai.google.dev/gemini-api/docs/pricing
- ElevenLabs API (v3 0,08 USD por 1k caracteres; v4 promoción 0,022 hasta el 12-10): https://elevenlabs.io/pricing/api
- YouTube `videos.insert` (restricción a privado sin verificar; cupo de subidas; `status.containsSyntheticMedia`): https://developers.google.com/youtube/v3/docs/videos/insert
- Multi-audio de YouTube (hasta 6 pistas; secundaria): https://blog.novadub.ai/blog/en/youtube-multi-audio-complete-guide-2026/ ; oficial: https://support.google.com/youtube/answer/13338784?hl=en
- Colab, límites de la versión gratuita (*"Runtimes will time out if you are idle"*, máx. 12 h, GPU *"heavily restricted"*, y prohibido para usuarios sin saldo de unidades de cómputo *"running distributed computing workers"* y *"bypassing the notebook UI"*; segundo plano solo en Pro+): https://research.google.com/colaboratory/faq.html
- Runpod, `runpodctl pod create / stop / delete` (creación y parada por línea de comandos, `--network-volume-id`, `--cloud-type COMMUNITY`): https://docs.runpod.io/runpodctl/reference/runpodctl-create-pod ; almacenamiento (volumen de red a 0,07 USD/GB/mes) y *serverless* (24 GB a 0,69 USD/h, no elegido): https://www.runpod.io/pricing
- Prueba propia [P]: `drafts/bench_cpu/` (StyleTTS2-Brais de Nós y `whisper-large-v3-turbo-gl` convertido a CTranslate2 int8, en 4 vCPU Xeon sin GPU, sobre las 1.263 palabras del guion muestra): RTF de TTS 0,28 (4 hilos) y 0,38 (2 hilos); arranque en frío de 27,6 s; RAM de 3,65 y 1,67 GB; ASR por frase con RTF 0,75 y WER mediana 0 %; ASR del audio entero con WER 48-53 % por alucinación (§4.1.1 a)
- Colab Pro 9,99 USD/mes y Pro+ 49,99 (oficial): https://colab.research.google.com/signup ; unidades de cómputo (100 CU; T4 ≈ 1,76 CU/h), solo en secundaria: https://www.thundercompute.com/blog/colab-alternatives-for-cheap-deep-learning-in-2025
- Runpod (oficial): RTX 4090 a 0,34 USD/h (Community) o 0,74 (Secure); RTX A5000 a 0,16 (Community): https://www.runpod.io/pricing
- Epidemic Sound Creator (secundaria): https://wyzowl.com/epidemic-sound-review/
- **Código de la voz por defecto** (leído el 29-09-2026): https://huggingface.co/proxectonos/Nos_StyleTTS2-Brais-GL (`inference.py`, `Utils/ASR/AuxiliaryASR/phonemize.py`, `text_utils_gal.py`, `phoneme_token_maps.json`, `Configs/inference_config.yml`, `Utils/cotovia/docs/USAGE.md`, `Utils/cotovia/data/lang/gl/{nomes,principal,variantes}.txt`); Celtia: https://huggingface.co/proxectonos/Nos_StyleTTS2-Celtia-GL
- Técnica de velocidad por escalado de duraciones en un derivado de StyleTTS2 (Kokoro): https://github.com/hexgrad/kokoro/blob/main/kokoro/model.py
- NeMo Forced Aligner (alineación forzada CTC, audios de más de 1 h): https://github.com/NVIDIA/NeMo/tree/main/tools/nemo_forced_aligner ; conformer CTC galego de Nós (etiqueta `forced-alignment`): https://huggingface.co/proxectonos/stt_gl_conformer_ctc_large_v1.0
- Catálogo de voces TTS de Nós (`*-phonemes` y `*-graphemes`): https://huggingface.co/api/models?author=proxectonos&pipeline_tag=text-to-speech
- Prueba propia [P]: Cotovía compilado desde el repositorio anterior y prototipo de `g2p_override.py` (regresión idéntica con el léxico vacío; corrección de *a corte* y *Brigantium*; rechazo de símbolos fuera del inventario)
- Prueba propia [P]: comparación entre Cotovía de Nós (con `-D`) y el paquete `cotovia 0.5` de 2013 (`/usr/bin/cotovia`), en el §3.5.9. En el `phonemize.py` de Nós, la llamada a `cotovia` va sin ruta
- Prueba propia [P]: `drafts/verifica_citas_prototipo.py` sobre tres artículos de Galipedia (*Gran Guerra Irmandiña*, *Castelo da Rocha Forte*; *Pardo de Cela*, revid 7405255) en el §3.6.2. Nota: la API de Wikimedia devolvió "too many requests" ante peticiones seguidas, así que la ingestión debe ir con *user-agent* y pausas (https://www.mediawiki.org/wiki/Wikimedia_APIs/Rate_limits)
- Prueba propia [P]: `drafts/extrae_cita_prototipo.py` + `drafts/proba_extrae_cita.py` (rapidfuzz 3.14.6, semilla 20260929) sobre el mismo corpus: 0 bloqueos falsos en 480 anclas ruidosas (fuente limpia, OCR 2 %/5 %, preestándar simulado), 145/145 falsificaciones no aceptadas como `ANCORADA`, distribución de `dist` y barrido de umbral (§3.6.2)
- `rapidfuzz`, distancia de Levenshtein normalizada: https://rapidfuzz.github.io/RapidFuzz/Usage/distance/Levenshtein.html ; SQLite FTS5 (consultas de frase y `NEAR`, `remove_diacritics`): https://www.sqlite.org/fts5.html
- Determinismo en PyTorch (`use_deterministic_algorithms`, `CUBLAS_WORKSPACE_CONFIG`, cuDNN): https://docs.pytorch.org/docs/stable/notes/randomness.html
- Valores por defecto de `LFinference` (firma: `alpha=0.3, beta=0.9, t=0.7`; config y `main`: `beta 0.7`, `t 0`) y ajustes de cuDNN en `main` (líneas 130-132): `inference.py` y `Configs/inference_config.yml` del repositorio de Nós, releídos el 29-09-2026
- Modelos ASR/GEC de Proxecto Nós (API de Hugging Face, consultada hoy): https://huggingface.co/api/models?author=proxectonos → `whisper-large-v3-turbo-gl-v1.0`, `stt_gl_conformer_ctc_large_v1.0`, `CarvalhoChat_GEC`
- Política de YouTube y AI Act: citas y URLs de `research/retornos.md` §6 (support.google.com/youtube/answer/1311392, techcrunch 20-07-2026, artificialintelligenceact.eu/article/50)
- Voz, corrección y fuentes: `research/voz_guion.md` (Nós, Azure, ElevenLabs, Hunspell-gl, LanguageTool, Dicionario de pronuncia, licencias del CCG y Galipedia)
