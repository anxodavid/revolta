# Formato de los canales de "historia para dormir": qué hacen los mejores y qué copiar en galego

Fecha: 29-09-2026. Investigación para el business plan del canal de historia de Galicia para durmir (100 % galego, IA).

**Leyenda**
- **[MED]**: medido por mí sobre datos reales. Metadatos y subtítulos automáticos de YouTube descargados con `yt-dlp` el 29-09-2026; palabras/min = palabras de la transcripción ÷ duración.
- **[DATO]**: dato con fuente (URL).
- **[OBS]**: observación directa (miniaturas, storyboards, descripciones).
- **[EST]**: estimación o recomendación mía.

Referencias textuales guardadas (uso interno):
- `refs/sleep_reference_en.md`: transcripciones literales de History at Night, History Time y Sleepless Historian.
- `refs/galego_experto.md`: Pegerto Saavedra (CCG 2020) y Carlos Barros (Praza 2022).

---

## 0. Resumen ejecutivo

1. **El listón (lo "inalcanzable") es History Time, "After Rome - The War For Britain".** https://www.youtube.com/watch?v=sXBgNNtEJ6M
   - [MED] 27,9 M de vistas, 3 h 28 min, ~98 palabras/min, 133K "me gusta", canal de 1,34 M de suscriptores.
   - Guion de autor, narración humana grave y pausada, fuentes y arqueología.
   - Tema casi gemelo del nuestro: reinos britanos post-romanos en la fachada atlántica ≈ Gallaecia sueva y post-romana.
2. **La referencia operativa, la que hay que igualar, es History at Night, "The Great Maya Collapse".** https://www.youtube.com/watch?v=hbufma0ZlUw
   - Es el mismo modelo de producción que el nuestro: guion con IA dirigido y verificado por un humano, voz clonada con licencia de un locutor profesional, imágenes IA hechas "one by one" y bibliografía en la descripción.
   - [MED] Con **solo 6 vídeos** (jul-2025 a ene-2026) tiene 74,3K suscriptores y ~4,1 M de vistas: una media de ~690K por vídeo. Dos vídeos pasan de 1,1 M.
   - **Es la prueba de que "pocos y excelentes" funciona**, que es justo lo que cabe en 4-10 h/semana.
3. **Anti-referencia de tono: Sleepless Historian** (715K suscriptores, ~1 vídeo al día, IA).
   - Usa segunda persona sarcástica ("you probably wouldn't last a day"), miniaturas grotescas e imágenes que cambian cada ≤10 s.
   - Le funciona en inglés por volumen, pero es incompatible con el concepto y con una audiencia galega exigente.
4. **Ritmo de narración medido** [MED]:
   - Narración humana "para dormir" de verdad: **94-115 palabras/min** (Lights Out Library, ASMR Historian, History Time).
   - Canales IA de volumen: 120-160 palabras/min.
   - Castellano: 124-147 palabras/min. El vídeo medieval de Relatos para Dormir con 1,05 M de vistas va a 124.
   - **Objetivo para el galego [EST]: 110-125 palabras/min, con pausas largas entre párrafos y capítulos.** Un vídeo de 2 h equivale a ~13.000-15.000 palabras de guion; uno de 1 h, a ~6.500-7.500.
5. **Duración.** El núcleo del género está en **1 h 15 min a 2 h 30 min**; los líderes en castellano ya van a 3-4 h.
   - [EST] Para el piloto galego: **60-90 min**. Cuesta menos revisar el guion y el formato de History at Night (47-87 min) ya demuestra que funciona. Escalar a 2 h cuando el pipeline sea fiable.
6. **Plantilla de apertura casi universal** [OBS en 8 de 11 transcripciones]:
   - bienvenida → "esta noche..." → resumen del viaje sin sobresaltos → **CTA suave** ("like/subscribe only if you enjoy", "dinos desde dónde y a qué hora escuchas") → "acomódate / deja que el mundo se apague" → cuerpo.
   - **Cierre:** despedida con relajación guiada ("Let your jaw unclench...", "Buenas noches, dulces sueños").
7. **Anuncios.** Los mejores venden la ausencia de cortes:
   - History at Night pone "**NO AD BREAKS**" en la miniatura [OBS].
   - Sleepy History Channel pone "— No Adverts —" en todos sus títulos [OBS].
   - Lights Out Library: "no mid-roll ads inside" [DATO en la descripción].
   - Para el galego [EST]: pre-roll sí; mid-rolls como mucho 2-3 en los primeros 20-25 min, y ninguno después. Se debe decir en título o miniatura ("sen cortes publicitarios"). La economía está en `research/retornos.md` §3.
8. **Visuales** [MED, storyboards de YouTube, 1 fotograma cada 10 s]. Hay dos estilos válidos y uno a evitar:
   - (a) Oscuro, casi estático y con fundidos: Sleepy History Channel, luminancia media 34/255 y ~1 cambio de plano cada 4 min. **Es el más "dormible".**
   - (b) Pinturas IA de tonos apagados con Ken Burns lento: History at Night, luminancia 86/255 y ~1 imagen nueva cada 35 s.
   - (c) A evitar: cambios cada ≤10 s y colores saturados (Sleepless Historian, luminancia 101/255).
   - Mucha audiencia escucha con la pantalla apagada o en negro (lo dice la descripción de Sleepless Historian: "the black screen background sets the scene"), así que **el audio es el 90 % del producto** [EST].

---

## 1. Método

- **Muestra:**
  - 7 búsquedas de YouTube (40 resultados cada una), en inglés y castellano: "history for sleep", "boring history for sleep", "fall asleep to history", "historia para dormir", "documental para dormir historia", "historia aburrida para dormir", "medieval history sleep". Resultados agregados por canal.
  - Listados completos de vídeos de 11 canales.
  - Metadatos y subtítulos automáticos (`en-orig` / `es-orig`) de 18 vídeos top.
- **Palabras por minuto:** palabras de la transcripción ÷ duración total del vídeo; incluye silencios y música, así que es el ritmo "percibido".
- **Errores del ASR:** el reconocimiento automático de YouTube (ASR) rara vez añade o quita palabras enteras; el error estimado es ±5 % [EST].
- **Limitación:** la API `youtube-transcript-api` estaba bloqueada por IP (IpBlocked). `yt-dlp` funcionó con reintentos, aunque a veces pedía "Sign in to confirm you're not a bot".
- **Visuales:** análisis de los *storyboards* públicos de YouTube (formato sb1, 1 fotograma cada 10 s, primeros ~33 min).
  - Luminancia media: escala de grises, de 0 a 255.
  - "Cambio de plano": diferencia media entre fotogramas consecutivos mayor que 18/255.
- Los datos de mercado, RPM y políticas de YouTube están en `research/retornos.md` y `research/audiencia.md`; aquí no se repiten.

---

## 2. Tabla de benchmarks (medida el 29-09-2026)

| Canal (idioma, voz) | Vídeo de referencia | Suscriptores | Vistas | Duración | Palabras | **Palabras/min** | Capítulos (mediana) |
|---|---|---|---|---|---|---|---|
| **History Time** (en, humana) | After Rome – The War For Britain · https://www.youtube.com/watch?v=sXBgNNtEJ6M (2021) | 1,34 M | 27,9 M | 208 min | 20.445 | **98** | 8 (27 min) |
| History Time (en, humana) | The Sea Peoples & Late Bronze Age Collapse · https://www.youtube.com/watch?v=xl9RaHE9ZpI | 1,34 M | 24 M | 149 min | 14.780 | **99** | – |
| **History at Night** (en, IA con voz clonada con licencia) | The Great Maya Collapse · https://www.youtube.com/watch?v=hbufma0ZlUw (03-08-2025) | 74,3K | 1,16 M | 47 min | 7.392 | **157** | 13 (3,6 min) |
| Sleepless Historian (en, IA) | Why You Wouldn't Last a Day in Medieval Times · https://www.youtube.com/watch?v=9jnekLeHz3c (25-04-2025) | 715K | 4,29 M | 127 min | 15.442 | 122 sobre la duración total (143 sobre el tramo con subtítulos, que acaba en el min 108) | 42 (2,6 min) |
| Sleepy History Channel (en; voz sin verificar) | 100 Sleepy Facts About the Seven Wonders — No Adverts · https://www.youtube.com/watch?v=LheSNj9s__A (01-04-2026) | 52,6K | 324K | 135 min | 18.890 | **140** | 16 (11,5 min) |
| Boring History Secrets (en, IA) | How Did People Sleep in Medieval Castles… · https://www.youtube.com/watch?v=vMtRXe5eQmM | 104K | 1,48 M | 148 min | 22.255 | 151 | 0 |
| Bedtime & Historian (en) | The First Crusade (1096–1099) · https://www.youtube.com/watch?v=oI7gRvhi-S4 (02-07-2026) | 102K | 485K | 133 min | 21.497 | 161 | 10 (16 min) |
| Sleepy Time Historian (en, IA; su descripción enlaza a autotube.pro) | What Did Early Humans ACTUALLY Do All Day? · https://www.youtube.com/watch?v=AHTEnwz0bL4 | – | 2,67 M | 136 min | 19.280 | 142 | 9 (12,8 min) |
| **ASMR Historian** (en, humana, soft-spoken) | Fall Asleep to 9 Hours of Medieval History · https://www.youtube.com/watch?v=a4ITFL_coq4 | 389K | 560K | 553 min | 51.793 | **94** | 89 (5,8 min) |
| **Lights Out Library** (en, humana, "no AI") | 10 hours of Ancient Lost Cities · https://www.youtube.com/watch?v=QZGuJ0gkUxw | 11,6K | 52K | 576 min | 59.987 | **104** | 23 (17 min) |
| Lights Out Library (en, humana) | One Thousand and One Nights · https://www.youtube.com/watch?v=wWlWrhD_DJQ | 11,6K | 29K | 75 min | 8.677 | **115** | 8 |
| **Relatos para Dormir** (es) | ¿Cómo Era un Día Completo en la Edad Media? · https://www.youtube.com/watch?v=3uBP9QaWfPM (10-01-2026) | 14,4K | 1,05 M | 150 min | 18.527 | **124** | 0 |
| **El Historiador Nocturno** (es, líder en castellano) | Toda La Mitología Egipcia Explicada · https://www.youtube.com/watch?v=BDgAVSlC9yQ | 304K | 1,73 M | 133 min | 17.285 | 130 sobre la duración total (154 sobre el tramo con subtítulos) | 0 |
| Pasado Aburrido para Dormir (es/en) | Historia Completa de la COCAÍNA · https://www.youtube.com/watch?v=FaR6BF93Vls | 39,5K | 414K | 129 min | 18.304 | 142 | 0 |
| Documental Nocturno by Eric (es, "Soy Eric") | Duérmete con la historia de Leonardo da Vinci · https://www.youtube.com/watch?v=s_9kZ33gSXQ (18-01-2026) | 17,8K | 514K | 88 min | 12.949 | 147 | 24 (4 min) |

**Duración media por canal** [MED, pestaña "Vídeos" completa]:
- Sleepless Historian: 122 min (362 vídeos).
- El Historiador Nocturno: 166 min (343 vídeos); los recientes duran 3-3,9 h.
- Sleepy History (humano, @SleepyHistoryShow): 180 min (93 vídeos).
- Sleepy History Channel: 144 min (128).
- Pasado Aburrido: 117 min (120).
- Lights Out Library: 94 min (148).
- History at Night: 70 min (6).
- History Time: 38 min de media (164 vídeos), pero sus clásicos más vistos duran 2,5-3,5 h.

**Lectura [EST]:**
- La voz humana de calidad va lenta, a 94-115 palabras/min. Los canales IA de volumen van más rápido (140-160), porque el TTS por defecto habla a velocidad de lectura y rara vez lo ralentizan.
- History at Night va a 157 y aun así funciona, lo que indica que **el timbre y la entonación pesan más que la velocidad pura**.
- En castellano el vídeo con más vistas por suscriptor (Relatos para Dormir: 1,05 M de vistas con 14,4K suscriptores) es el más lento de la muestra en castellano (124).

---

## 3. Parámetros del formato, uno a uno

### 3.1 Duración
- **Rango dominante: 2-2,5 h** [MED] (tabla anterior).
- Los líderes suben con el tiempo:
  - El Historiador Nocturno pasó de ~2,2 h en 2025 a 3-3,9 h en 2026.
  - Existen compilaciones de 6-10 h: ASMR Historian 9 h, Lights Out 10 h, Sleepy History 8 h.
  - La guía de un proveedor (autotube.pro, con interés comercial) recomienda 2-3 h, 10-20 capítulos, intro de 5-10 min y cierre de 10-20 min. [DATO débil] https://autotube.pro/blog/how-to-launch-faceless-ai-sleep-channel-long-form
  - Fortune (30-12-2025): el operador de "Boring History" hace vídeos de hasta 6 h. [DATO] https://fortune.com/2025/12/30/ai-slop-faceless-youtube-accounts-adavia-davis-user-generated-content/
- **Contrapunto:** History at Night logra más de 1 M de vistas con 47 y 76 min.
- **Recomendación [EST]:**
  - Etapa 1: 60-90 min (unas 7.000-11.000 palabras que revisar a mano en galego).
  - Etapa 2: 2 h.
  - Después, compilaciones de 4-8 h ensambladas con episodios ya publicados. Cuestan casi nada; el riesgo de "reused content" se analiza en `retornos.md` §6.

### 3.2 Ritmo (palabras por minuto)
- **Medido:** 94-161 palabras/min (tabla anterior). Narración humana para dormir: 94-115. Narración IA: 122-161.
- **Referencia del sector:** "Sleep stories are typically narrated at 100–130 words per minute — notably slower than standard narration (160–180 wpm)". [DATO débil, blog comercial] https://www.otherworldtales.com/blog/calming-bedtime-stories-for-adults
- **Galego [EST]:**
  - La palabra media gallega tiene más sílabas que la inglesa, así que 120 palabras/min en galego es "más lento de oír" que 120 en inglés. Tomar como ancla el castellano: 124-147 medido.
  - **Objetivo: 110-125 palabras/min.** Pausa de 0,6-0,9 s entre frases, de 1,5-2,5 s entre párrafos y de 5-10 s (solo ambiente) entre capítulos.
  - Se mide en el kit A/B con cada voz de Nós (Brais, Celtia, Icía, Sabela, Iago, Paulo). La voz que suene natural a 115 palabras/min, sin "arrastrar" las vocales, gana.

### 3.3 Tono
- **Principios de la guionista de Calm (Phoebe Smith):**
  - "If there's any action, it has to start in the beginning. And then it has to slow down."
  - Se quitan elementos que asustan ("had to edit out that snake").
  - "You are not writing a gripping thriller".
  - Fuente [DATO]: https://slate.com/human-interest/2018/05/phoebe-smith-sleep-story-writer-for-the-calm-app-on-the-art-of-boring-people-to-sleep.html
- **Nothing Much Happens** (más de 100 M de descargas): la mente necesita "a place to land"; en la técnica original se cuenta la historia dos veces, la segunda más lenta. [DATO] https://www.iheartmedia.com/press/sleep-enthusiasts-rejoice-nothing-much-happens-bedtime-stories-help-you-sleep-joins
- **Lo que hacen los mejores de historia** [OBS en las transcripciones]:
  - Tercera persona narrativa y descriptiva, con escenas visuales ("Deep in the rainforests of Central America, there are silent cities…").
  - Ritmo de frase regular y ausencia de preguntas retóricas agresivas.
  - Los hechos violentos se cuentan con distancia.
- **Lo que hace la IA de volumen:** segunda persona burlona ("Congratulations, you've just woken up in the year 1325. The good news, you're alive. The bad news, so are the fleas."). Es el estilo "engagement" que el contexto del proyecto descarta explícitamente.
- **Para la Revolta Irmandiña [EST]:**
  - El conflicto (fortalezas derribadas, batallas de 1469) se cuenta en la primera mitad, con distancia y sin gore.
  - La segunda mitad va a paisaje, vida cotidiana, oficios, estaciones y la memoria de las ruinas.
  - Así la "curva de tensión" desciende, siguiendo la regla de Smith.

### 3.4 Estructura del guion
**Plantilla observada** [OBS]:
- **Apertura (60-120 s):**
  - Bienvenida con el nombre del canal: History at Night, Sleepy History Channel, Bedtime & Historian, Lights Out.
  - "Tonight…/Esta noche…" y un resumen poético del viaje.
  - **CTA suave:** "like and subscribe, but only if you genuinely enjoy what I do here" (Sleepless Historian, Boring History Secrets y Bedtime & Historian usan casi la misma frase: plantilla compartida). Pregunta por "where in the world and at what time you're joining me" (6 de 11 canales).
  - Transición de relajación ("settle in", "dim the lights", "pónganse cómodos, apaguen…").
- **Cuerpo en capítulos.** Mediana por canal: 2,6 min (Sleepless), 3,6 min (History at Night), 11-17 min (Sleepy History Channel, Lights Out, Bedtime & Historian), 27 min (History Time). Los capítulos aparecen con marcas de tiempo en la descripción.
  - History at Night: 13 capítulos en 47 min, con un arco completo: contexto → edad dorada → escritura y cosmos → declive → guerra → causas → éxodo → "los que quedaron" → desciframiento → epílogo.
- **Cierre (1-3 min):** agradecimiento y "calm and peaceful night" (History at Night), o relajación guiada por el cuerpo ("Tus pies se vuelven pesados…", Relatos para Dormir; "Let your jaw unclench…", Sleepy History Channel). Sleepy History Channel pone el CTA en el cierre ("if you are still awake, there is another video waiting for you").
- **Apertura "de cine documental" (History Time):** sin CTA. Abre con una escena concreta y un lugar (la muerte de Eric Bloodaxe en Stainmore) y enlaza con el gran tema. Es la apertura de más calidad de la muestra.

**Plantilla propuesta para el galego [EST]:**
1. Escena de lugar de 45-60 s: por ejemplo, las ruinas de Rocha Forte con la niebla de la mañana.
2. "Boas noites e benvidos a…".
3. Resumen de qué se contará.
4. CTA de una sola frase ("se che gusta, subscríbete; e se queres, dinos desde onde nos escoitas").
5. "Acomódate…".
6. Entre 8 y 14 capítulos de 5-8 min.
7. Epílogo contemplativo.
8. Cierre de relajación de 60-90 s y 20-40 min de ambiente solo (opcional; es watch time sin coste de guion).

### 3.5 Música y ambiente
- **Observado:**
  - Chimenea crepitante (descripción de Sleepless Historian).
  - "432 hz background music" (Sleepy History Channel).
  - Tormenta, chimenea y "quiet reading room" (podcast Boring History For Sleep, Apple Podcasts). [DATO] https://podcasts.apple.com/us/podcast/boring-history-for-sleep-gentle-storytelling-and/id1847901984
  - "Rain sounds" en títulos y etiquetas.
- **Mezcla (proxy):** YouTube marca "[Music]" en la transcripción cuando la música tapa o separa la voz. History Time tiene 196 marcas en 208 min (interludios musicales frecuentes); History at Night, 0 (música muy baja bajo la voz, sin interludios); Documental Nocturno, 43. [MED]
- **Recomendación [EST]:**
  - Cama sonora continua 20-26 dB por debajo de la voz: lluvia suave, lareira, o un pad de gaita o zanfona muy lento sin melodía marcada, solo en las transiciones.
  - Sin cambios bruscos de pista ni golpes musicales. Normalizar a ~-16 LUFS y con limitador, para que no haya picos que despierten.
  - Música con licencia o generada con derechos claros; hay que evitar reclamaciones de Content ID en vídeos de 2 h.
  - Un sello sonoro galego (ambiente de lluvia atlántica, curros, mar de fondo) puede ser un elemento de marca distintivo.

### 3.6 Visuales
**Medido (primeros ~33 min)** [MED]:

| Vídeo | Luminancia media (0-255) | Cambios de imagen | Estilo [OBS] |
|---|---|---|---|
| Sleepy History Channel, Seven Wonders | **34** | ~1 cada 250 s; el resto, movimiento lento o fundido | Paisajes nocturnos IA, naranjas y azules muy oscuros |
| History at Night, Maya | 86 | ~1 cada 35 s, con Ken Burns lento continuo | Pintura digital "matte painting", verdes y ocres apagados, coherente |
| Sleepless Historian, Medieval | 101 | ≥1 cada 10 s | Ilustración "manuscrito medieval" IA, colores saturados |
| History Time, After Rome | 112 | ≥1 cada 10 s | Fotos reales de paisajes y yacimientos, mapas animados, objetos de museo; patrocinio de Magellan TV integrado hacia el minuto 17-20 |

- La guía del proveedor recomienda "darker, muted" (azul marino, morado oscuro, marrones suaves) y cambios cada 30-120 s, y desaconseja flashes y zooms rápidos [DATO débil, autotube.pro]. Coincide con lo medido en los dos mejores ejemplos "dormibles".
- **Recomendación [EST]:**
  - Estilo History at Night pero más oscuro (luminancia 40-70), 1 imagen cada 40-90 s con Ken Burns lento (≤3 % de zoom por plano) y fundidos de 2-3 s.
  - Coherencia de estilo: una sola "biblia visual" de pintura al óleo atlántica, con niebla, piedra, verdes húmedos y luz de vela.
  - Mapas de Galicia con topónimos en galego normativo: aportan rigor y son reutilizables.
  - En la Etapa 1 bastan 60-120 imágenes por vídeo de 60-90 min.
  - Evitar personas "realistas" identificables. Etiqueta de contenido sintético según `retornos.md` §6.2.

### 3.7 Ausencia de sobresaltos (checklist técnico) [EST, a partir de lo anterior]
- Sin pantallas de suscripción animadas, sin tarjetas con sonido y sin *jump cuts* de audio.
- Tarjetas finales en silencio.
- Nada de gritos, cifras de muertos "a golpe", efectos de espadas o campanas fuertes. Si hay campanas, lejanas y por debajo de -30 dB.
- Volumen constante (LUFS) de principio a fin.
- Control de calidad automático del TTS: detectar *glitches* de voz. 404 Media documenta un glitch audible en el minuto 1:15 de un vídeo de 2,3 M de vistas. [DATO] https://www.404media.co/ai-generated-boring-history-videos-are-flooding-youtube-and-drowning-out-real-history/
- En galego, además, detectar vocales abiertas/cerradas mal pronunciadas, topónimos mal acentuados y castellanismos fonéticos (lo cubre `voz_guion.md`).

### 3.8 Gestión de anuncios (formato; la economía está en `retornos.md` §3)
- **Señal comercial:** los mejores canales para dormir usan "sin cortes" como argumento de venta.
  - History at Night: "NO AD BREAKS" en la miniatura del vídeo Maya [OBS, miniatura del 29-09-2026].
  - Sleepy History Channel: "— No Adverts —" en todos sus títulos [OBS].
  - Lights Out: "no 'mid-roll' ads inside" [DATO en la descripción].
  - ASMR Historian: "Patreon for Ad Free Viewing" [DATO en la descripción].
  - Sleepy History (@SleepyHistoryShow): "no ai, no ads" (`retornos.md`).
- **Alternativa del listón:** History Time integra un patrocinio (Magellan TV) al principio del documental [OBS en el storyboard].
- **Recomendación [EST]:** pre-roll activado; mid-rolls manuales solo en los primeros 20-25 min, o ninguno, con un test A/B por lotes. Decir "sen cortes publicitarios" en título o miniatura como argumento de marca. Membresía o Patreon con versión sin anuncios y descargable, como hace Lights Out.

### 3.9 Cadencia de publicación
- **Observado:**
  - Sleepless Historian: ~1 vídeo al día (`retornos.md`).
  - El Historiador Nocturno: 1 cada 1-2 días (`retornos.md`).
  - Sleepy History (humano): 2-3 por semana (`retornos.md`).
  - Lights Out: ~semanal por episodio de podcast [OBS].
  - History Time: ~1 al mes o menos (`retornos.md`).
  - **History at Night: 6 vídeos en 6 meses (17-07-2025 → 29-01-2026) y ninguno desde entonces**, con 74,3K suscriptores y ~4,1 M de vistas [MED].
- La guía del proveedor dice que con flujo integrado se pueden hacer 2-4 vídeos por semana [DATO débil].
- **Recomendación [EST]:** en la Etapa 1, **1 vídeo cada 2 semanas** (compatible con 4 h/semana si el pipeline genera y el humano solo revisa). En la Etapa 2, semanal, más una compilación al mes. La calidad por vídeo pesa más que la cadencia, como demuestra History at Night; además, la política de "inauthentic content" castiga la plantilla repetitiva (`retornos.md` §6).

### 3.10 Miniaturas [OBS en 6 miniaturas; montaje en `fmt/thumbs/grid_thumbs.jpg`, carpeta de trabajo]
- **History at Night:** paisaje brumoso oscuro, tipografía serif pequeña ("HISTORY FOR SLEEP" y "NO AD BREAKS"), sin caras. Sobria y "de biblioteca".
- **Sleepless Historian:** caricatura grotesca de campesinos comiendo ratas y texto grande "BORING HISTORY FOR SLEEP". Estética de clickbait.
- **History Time:** foto real y figuras en silueta, título documental ("LOST HISTORY OF THE OLD NORTH", "BRITAIN AFTER ROME", fechas "400-650 AD").
- **Sleepy History Channel:** pirámides al anochecer, "100 Sleepy Facts" y un sello de "432 Hz".
- **El Historiador Nocturno:** ilustración plana de dioses egipcios en naranja y azul con "MITOLOGÍA PARA DORMIR".
- **Relatos para Dormir:** anciano IA fotorrealista junto al fuego en la nieve, "HISTORIA PARA DORMIR".
- **Patrón:** etiqueta de género ("para dormir", "for sleep") siempre visible, paleta cálida sobre fondo oscuro y un solo motivo central.
- **Recomendación [EST]:**
  - Etiqueta fija "HISTORIA PARA DURMIR" en la misma esquina y tipografía (marca de serie).
  - Paisaje o monumento gallego nocturno reconocible: Rocha Forte, Pena Corneira, las torres de Altamira, Soutomaior.
  - Fecha ("1467-1469") al estilo History Time.
  - Sin caras gritando.
  - Valorar un sello "sen cortes".

### 3.11 Títulos [OBS en listados de canal]
- **Fórmulas dominantes:**
  - "[Tema] | History for Sleep" (History at Night).
  - "Boring History For Sleep | [pregunta o hecho sorprendente] and more" (Sleepless Historian).
  - "Toda [X] Explicada | Historia/Mitología (Aburrida) Para Dormir" (El Historiador Nocturno; 6 de sus 6 vídeos más vistos siguen esta fórmula).
  - "100 Sleepy Facts About [X] — Fall Asleep to History — No Adverts" (Sleepy History Channel).
  - "[Tema] // [Ancient/European] History Documentary" (History Time).
- **Palabras gancho observadas:** "ENTIRE", "Toda", "What it was like", "How did people…", "REAL", "Completa". En castellano funciona mucho "Toda la historia de X explicada".
- **Propuestas en galego [EST]** (a validar por el lingüista):
  - "A Revolta Irmandiña: toda a historia (1467-1469) | Historia de Galicia para durmir"
  - "Como era un día nunha aldea galega do século XV | Historia para durmir"
  - "O Reino suevo de Gallaecia, contado devagar | Historia para durmir · sen cortes"
- **SEO:** el público galego busca en castellano ("Galicia para dormir", 107K vistas en castellano según `retornos.md` §4.4). [EST] Poner título en galego, y en la descripción una línea bilingüe y etiquetas en castellano, sin traducir el audio.

---

## 4. La referencia elegida y por qué

| Papel | Canal y vídeo | Motivo |
|---|---|---|
| **Listón "inalcanzable"** (techo de calidad) | History Time, "After Rome – The War For Britain" · https://www.youtube.com/watch?v=sXBgNNtEJ6M | 27,9 M de vistas; guion de autor con arqueología y fuentes; voz humana grave a ~98 palabras/min; tema post-romano atlántico análogo a Gallaecia; apertura de escena sin CTA. En los tests ciegos, ningún guion ni voz IA debería "ganarle", pero hay que medir la distancia. |
| **Referencia operativa** (lo que hay que igualar) | History at Night, "The Great Maya Collapse" · https://www.youtube.com/watch?v=hbufma0ZlUw | Mismo proceso que el proyecto (IA + dirección humana + voz clonada con licencia + imágenes una a una + bibliografía); 1,16 M de vistas con 47 min; 6 vídeos, 74,3K suscriptores. Es el patrón para la Etapa 3 (licenciar la voz de un locutor galego). |
| **Anti-referencia de tono** | Sleepless Historian, "Why You Wouldn't Last a Day in Medieval Times" · https://www.youtube.com/watch?v=9jnekLeHz3c | Lo que no hacer: sarcasmo en segunda persona, cambios de imagen cada 10 s, miniaturas grotescas. |
| **Referencia en castellano** (mercado vecino) | Relatos para Dormir, "¿Cómo Era un Día Completo en la Edad Media?" · https://www.youtube.com/watch?v=3uBP9QaWfPM y El Historiador Nocturno (304K) | Relatos: 1,05 M de vistas con 14,4K suscriptores a 124 palabras/min, en "usted" plural y tono sereno. Es un formato de "vida cotidiana" trasladable a la aldea galega medieval. |
| **Listón lingüístico en galego** | Pegerto Saavedra, CCG 2020 (`refs/galego_experto.md`) | Galego académico normativo impecable. El guion debe igualarlo en corrección, con frase más oral. |

**Cómo usarlas en el gauntlet [EST]:**
- Comparación ciega de fragmentos de ~600 palabras: guion galego traducido al inglés frente a los bloques A y B de `sleep_reference_en.md`. Se juzgan especificidad, imágenes concretas, curva de tensión y ausencia de clichés IA.
- Comparación ciega de la prosa galega contra `galego_experto.md`: corrección y naturalidad, puntuadas por el promotor y su mujer.

---

## 5. Especificación de formato v0 para el piloto galego [EST, derivada de todo lo anterior]

| Parámetro | Valor Etapa 1 | Valor Etapa 2 |
|---|---|---|
| Duración | 60-90 min | 2 h (más compilaciones de 4-8 h) |
| Guion | 7.000-11.000 palabras; 8-12 capítulos de 5-8 min | 13.000-15.000 palabras; 12-16 capítulos |
| Ritmo | 110-125 palabras/min; pausas de 0,7 s entre frases, 2 s entre párrafos y 5-10 s entre capítulos | igual |
| Apertura | Escena de lugar (45-60 s) + bienvenida + CTA de 1 frase + "acomódate" | igual |
| Curva | Acción y conflicto solo en el primer 40 %; después, descripción, paisaje y vida cotidiana | igual |
| Cierre | Epílogo + 60-90 s de relajación + 20-40 min de ambiente (opcional) | igual |
| Voz | La ganadora del kit A/B de Nós | Valorar la licencia de un locutor galego (modelo History at Night) |
| Audio | Lluvia o lareira a -20/-26 dB bajo la voz; -16 LUFS; sin picos | Sello sonoro propio |
| Visual | 60-120 imágenes IA de estilo único y oscuro (luminancia 40-70); Ken Burns ≤3 %; fundidos de 2-3 s; mapas con topónimos en galego | Más mapas y fotos propias de yacimientos |
| Anuncios | Pre-roll; 0-2 mid-rolls en los primeros 20 min; "sen cortes" en el título | Test A/B y membresía sin anuncios |
| Cadencia | 1 vídeo cada 2 semanas | Semanal y 1 compilación al mes |
| Título | "[Tema] (fechas) \| Historia de Galicia para durmir" | igual |
| Miniatura | Monumento gallego nocturno + "HISTORIA PARA DURMIR" + fechas | igual |
| Descripción | Capítulos con marcas de tiempo; "Nota sobre o proceso" (IA + revisión humana + voz sintética); bibliografía en galego (Barros, López Carreira, Saavedra…) | igual |

---

## 6. Incertidumbres y lagunas
- **Voz de Sleepy History Channel (humana o IA) sin verificar.** No es el Sleepy History humano de @SleepyHistoryShow; son canales distintos con nombres parecidos.
- **Voz de Documental Nocturno by Eric sin verificar.** La descripción está en primera persona ("Soy Eric"), pero eso no prueba que la narración sea humana.
- **Sleepy History (@SleepyHistoryShow), "Sleepy History of London":** la transcripción automática solo cubre ~55 min de 180 (5.104 palabras). Su ritmo real no se ha medido; puede que el resto sea ambiente o un bucle.
- **Tramos sin subtítulos:** en Sleepless Historian y El Historiador Nocturno los subtítulos acaban antes del final (min 108 de 127 y min 112 de 133). Puede ser una cola de ambiente o subtítulos truncados.
- **"Boring History For Sleep" (@boringhistory25, 221K suscriptores según vidIQ):** hoy tiene 14 vídeos con cientos de vistas. Los datos no son coherentes (¿canal comprado o reciclado?). El vídeo de 2,3 M que cita 404 Media pertenece en realidad a Sleepless Historian (título "Boring History For Sleep | How Medieval PEASANTS Survived…").
- **No se ha verificado el porcentaje de oyentes que usan pantalla negra o apagada.** Es una inferencia a partir de descripciones y de que Premium permite la reproducción en segundo plano.
- **El objetivo de 110-125 palabras/min en galego es una hipótesis.** Se valida con el kit A/B y, más adelante, con la retención media en Studio.
- **No hay canales de historia para dormir en galego que medir** (`retornos.md` §4.4); todos los parámetros se extrapolan del inglés y del castellano.
