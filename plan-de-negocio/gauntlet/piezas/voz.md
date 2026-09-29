# Pieza del business plan: VOZ. Estrategia de narración en galego y protocolo de validación A/B

Versión 5 (constructor, ronda 5) · 29-09-2026 · Redactado en castellano. Todo lo que se dirige al público (textos de prueba, ejemplos) va en galego normativo (RAG).

**Qué cambia en la versión 5: el oído que firma cada episodio también se mide.** La v4 daba por hecho que quien escucha el episodio detecta el 100 % de los defectos. Ese escuchador son el promotor y su mujer, nativos pero sin formación de corrector de locución, así que la calidad publicada quedaba sin un juez calibrado. Cambios:
1. **Prueba de defectos sembrados** antes del primer episodio (§5B.3.1). Se inyectan 36 defectos conocidos por episodio de prueba (16 graves y 20 leves: é/è y ó/ò, metafonía, acento de topónimos, pausas desviadas ±150-300 ms, clics y artefactos de vocoder) en dos episodios de prueba, y se mide la tasa de acierto de cada revisor a 1,25× y a 1×. **Umbral para firmar un episodio en solitario: ≥ 90 % en graves (≥ 15/16) y ≥ 70 % en leves (≥ 14/20)** a la velocidad a la que va a trabajar. Quien no llega, no firma solo.
2. **Revisor lingüístico profesional de referencia**, un corrector o asesor lingüístico galego de locución o doblaje, pagado (§5B.3.2). Escucha completos los **6 primeros episodios** y hace **cada muestreo de la Etapa 2**. Sus hallazgos sirven de verdad de referencia para calibrar a los revisores de la casa (captura-recaptura). **La tarifa no se ha podido verificar con una fuente gallega** (§5B.3.2): se presupuesta con un ancla española y un supuesto, y se fija con 3 presupuestos por escrito en la semana 1.
3. **AOQ y plan de muestreo rehechos con la probabilidad de detección** (§5B.3.4, `sim/muestreo_deteccion.py`). Al rehacerlo apareció además un **error de cálculo en la v4**: el AOQL de 0,48 bloques aplicaba dos veces el factor (N − n)/N. Con detección perfecta es 0,72, y con revisores reales el plan de n = 20 deja salir 0,66-0,97 bloques defectuosos por episodio con *p* = 2-3 %. El plan nuevo (**20 bloques del profesional + 20 de la casa**, c = 0) baja a **0,37-0,53** en ese rango.
4. **Prueba de defectos sembrados cada trimestre** y seguimiento continuo de la sensibilidad con el profesional, para vigilar la fatiga (V16).
5. **Tarifa de los narradores corregida** (§3 y §7.2). Los 0,05-0,07 €/palabra eran una tarifa genérica de audiolibro en España (Cronoshare). El dato gallego "desde 0,29 €/palabra" procedía de un fragmento de buscador y **se retira**: la página, abierta ahora, no publica precios. Se añade la tarifa publicada de una agencia con catálogo de locutores galegos (audiolibro: 450 € por 2.000 palabras, con descuentos del 20-40 %). **El presupuesto por narrador sube de 200-350 € a 300-500 €**, y el de la excepción única se rehace (Q1).
6. **Licencia de Nós: el silencio ya no cuenta como permiso** (§4 y §8.1). Sin confirmación escrita de la USC, no se publica con voz de Nós.
7. **La identificación humano/IA se hace en seco** (§7.2 y §7.7), como se escucha un audiolibro profesional. La cama sonora pasa a un bloque secundario, solo informativo.
8. Detalle: ~170-190 frases por narrador, no ~190 (§5B.2).

**Qué cambió de la versión 3 a la 4 (se mantiene, con las cifras de §5B.3 revisadas en la v5): además de medir la calidad, se explica cómo fabricarla y mantenerla.** La v3 solo tenía una puerta de medición. La v4 añade **§5B, un método de producción de calidad audiolibro** en cuatro piezas:
1. **Síntesis con contexto y "mejor de N"** (§5B.1): 3-5 variantes por frase encadenadas con el estilo de la anterior, elegidas con una puntuación automática (UTMOSv2/DNSMOS, confianza de ASR, prosodia y continuidad) calibrada contra un nativo, más un pase de dirección humana solo en las frases dudosas (15-35 min por episodio).
2. **Modelo de pausas y entonación aprendido de H1/H2** (§5B.2): pausas según el tipo de frontera y de frase, con su distribución humana real, y caída tonal de final de párrafo. Se valida **dentro del mismo test ciego** con la comparación "pausas fijas (F) / modelo (M)" en R1, R2 y R3, con una regla de decisión prerregistrada.
3. **Escucha de corrección en cada episodio** (§5B.3): completa en la Etapa 1 y **muestreo de aceptación c = 0 con inspección rectificadora** en la Etapa 2. *(En la v5 se añaden la calibración de los revisores y el revisor profesional, y se corrige el AOQL.)*
4. **Vía intermedia financiable antes del plan B** (§5B.4): *fine-tune* de StyleTTS2-GL con 30-60 min de H1 o H2 en estilo "durmir", con la **opción de cesión firmada en el mismo contrato que las referencias**. Cuesta ~700-1.250 € hasta saber si funciona (cifra de la v5), frente a 1.000-2.500 € del plan B, y la licencia de publicación solo se paga si pasa la Puerta V. Da una salida realista al escenario central (60-80 % de suspenso).

También cambian: el árbol de decisión (§8.1), los contratos (§4 y §7.2), los costes (§3), los riesgos (V14-V16), el plan de ejecución (§10) y las preguntas al promotor (Q3).

**Qué cambió de la versión 2 a la 3 (se mantiene; el protocolo ciego se había diseñado mal y se corrigió).**
1. **Control positivo humano.** Ya no graba un solo narrador sino **2 narradores profesionales nativos, un hombre y una mujer**, de modo que la voz candidata tenga siempre un humano de su mismo género. Si el presupuesto lo permite, se añade un **3.º narrador del género de la finalista** antes de R3. En cada pantalla MUSHRA, un narrador hace de referencia marcada y **el otro se esconde como una condición más**. Ese segundo humano tiene que **pasar la misma puerta que la IA** (Δ ≤ 10 e identificación ≤ 60 %) para que la prueba se dé por válida. Si no la pasa, el umbral se **recalibra con una fórmula escrita de antemano, antes de abrir la clave de los motores**, y si el fallo es grave la prueba se repite. Un "suspenso" ya no puede deberse al test (§7.6).
2. **La Δ ya no mide el parecido a una lectura concreta.** La referencia marcada rota entre narradores (por pantalla en R1 y por oyente en R3), y el listón queda **validado empíricamente**: otro profesional tiene que alcanzarlo. Se retira el argumento de la franja "excelente" de MUSHRA (§7.6).
3. **La prueba de identificación se rediseña para que no se resuelva distinguiendo dos timbres.** Cada oyente oye 10 fragmentos de 5 voces distintas (2 humanas, la candidata, la 2.ª clasificada y un ancla sintética), **cada voz dos veces**, para que contar repeticiones no dé pistas. La prueba se hace **antes** del MUSHRA, así nadie ha oído todavía a la referencia marcada (§7.7).
4. **El análisis se hace por oyente y no por ensayo.** La métrica es la **exactitud equilibrada (BA)** por oyente, con IC por *bootstrap* de oyentes y un modelo logístico mixto como confirmación. Se añade un **control negativo** (ancla sintética que tiene que ser detectada) para comprobar que la prueba es sensible. **N = 20 oyentes como mínimo y 24 como objetivo**, fijados en el prerregistro, con la potencia **simulada** con correlación dentro de cada oyente (`sim/potencia_ident_v2.py`, `sim/extremo.py`). Se reconoce que la v2 sobreestimaba la potencia: la "P ≈ 0,026" pasa a ser de hasta ~0,22 si los oyentes responden por timbre (§7.7).
5. **Apertura de la clave en dos fases**: primero, solo los códigos humanos y las anclas (controles y umbral efectivo, que se sella); después, los motores.
6. **Coste**: la excepción única pasa de 200-450 € a 400-700 € (2 narradores), más 200-350 € opcionales por el 3.º; techo de 1.100 € (*cifras rehechas en la v5: 600-1.000 € por dos narradores y techo de 1.500 €, §3*). El panel pasa de 10-12 a **20-24 personas** (§3, §10, Q1).

**Qué cambió de la versión 1 a la 2 (se mantiene).** (1) La referencia humana oculta pasa a ser un **narrador profesional galego** que graba ~20 min del guion piloto en condiciones de estudio (coste y fuentes en §7.2). (2) La Puerta V exige quedar **a ≤ 10 puntos de esa referencia** en las escalas A, B y C, con los mismos márgenes en el panel. (3) Se añade una **prueba ciega de identificación humano/IA** con fragmentos de 5 min y un tamaño de muestra calculado de antemano (§7.7). (4) La prueba de sueño y parte del panel se hacen en **dispositivos reales** (altavoz del móvil, auriculares de botón a volumen bajo). (5) Hay **objetivos técnicos de audio**: frecuencia de muestreo nativa, suelo de ruido y artefactos de vocoder (§5.3). (6) Queda escrito que **si ninguna voz llega a ese listón, no se publica o se adelanta el locutor con licencia** (§8.1). Además se corrigen los datos de las voces de Nós, ahora contrastados con las fichas de los *datasets* (§2.1).

**Leyenda de evidencia**
- **[F]** dato con fuente (URL al lado). Consultado el 29-09-2026.
- **[F-sec]** dato de fuente secundaria (blog, prensa, fragmento de un buscador). Hay que confirmarlo antes de depender de él.
- **[MED]** medido en la investigación previa (`research/formato.md`, yt-dlp sobre vídeos reales).
- **[CALC]** cálculo propio reproducible (se indica cómo).
- **[S]** supuesto o decisión de diseño propia. Se valida con el protocolo de esta pieza o en la Etapa 1.
- **[?]** desconocido. Solo lo resuelve una prueba.

Documentos relacionados: `research/voz_guion.md` (inventario técnico de voces), `drafts/formato.md` (ritmo, duración, audio), `drafts/guion.md` (guion piloto "A Revolta Irmandiña"), `drafts/retornos.md` (etapas, presupuestos y Puertas 1-3).

---

## 0. Resumen: la estrategia de voz en 14 líneas

1. **La voz es la puerta de entrada del proyecto, no un detalle de producción.** El listón no es "suena bien": es **"no se distingue de un narrador nativo profesional"**. Si ninguna voz sintética lo alcanza en el protocolo ciego, **no se publica con esa voz** (Puerta V, §7.6 y §8.1). Así se aplica la condición "calidad de narración imprescindible".
2. **Hay 7 vías reales de voz en galego** (§2). Ninguna tiene evidencia pública de calidad en narración larga para dormir, así que **el oído nativo decide y no la ficha técnica.**
3. **Candidatos favoritos para la Etapa 1:** Nós StyleTTS2 **Brais** y **Celtia** (gratis, modelo Apache-2.0, G2P gallego nativo). Están entrenados con ~18 h y ~25 h de un locutor y una locutora profesionales grabados en estudio, con el corpus a **16 kHz** [F] (fichas de los *datasets*, §2.1). **Aspirantes de pago:** ElevenLabs v4/v3 (lista el galego) [F] y Gemini-TTS gl-ES (Preview) [F]. **Línea base:** Azure Sabela/Roi, la voz que el promotor ya probó en Clipchamp [F].
4. **Referencias humanas profesionales con control positivo** (§7.2): **dos narradores galegos profesionales (un hombre y una mujer)** graban el texto trampa y ~30 min del guion piloto a 48 kHz/24 bits, en cabina. Presupuesto de **300-500 € por narrador**, contratado directamente como narración de audiolibro para uso interno: **600-1.000 € por los dos**, más un 3.º narrador opcional del género de la finalista (+300-500 €); **techo de 1.500 €**. La horquilla va de la tarifa genérica española de audiolibro (185-250 € por ~3.700 palabras) a la tarifa publicada de una agencia con locutores galegos (500-830 €) [F-sec + CALC + S; §3]. **No hay tarifa gallega publicada verificada**: la cifra se cierra con 3 presupuestos en la semana 1. Cada uno sirve de referencia para el otro: si un humano no pasa la puerta, el test está mal calibrado y no se castiga a la voz. Además son los primeros candidatos de casting para la Etapa 3.
5. **Coste por hora narrada** (§3): de 0 € (Nós) a ~0,84 USD (Azure, gratis dentro de 500k caracteres/mes), ~1,2 USD (Gemini Flash) y ~4,5 USD (ElevenLabs por API), contando un 30 % de regeneraciones. Con un locutor licenciado, ~20-60 €/h amortizados. **La voz no es el coste que decide: lo son las horas de escucha y corrección.**
6. **Licencias** (§4): todas las opciones oficiales permiten el uso comercial. Hay dos cabos sueltos. Los *datasets* de Nós son "solely for research purposes", así que hay que **pedir confirmación escrita a la USC. Sin esa confirmación no se publica con una voz de Nós: el silencio no cuenta como permiso** (§8.1). Y `edge-tts` queda **excluido** porque va contra los términos de Microsoft [F-sec].
7. **Ritmo y señal "de durmir"** (§5): 110-125 palabras/min percibidas, pausas insertadas por programa, −16 LUFS / −1,5 dBTP, **master a 48 kHz/24 bits**, suelo de ruido de la voz ≤ −65 dBFS en las pausas, cero clics en las uniones y un detector de artefactos de vocoder.
8. **Riesgos principales** (§6): acento castellanizado o aportuguesado, prosodia de "telediario", *glitches* en tiradas de 1-3 h, **ancho de banda limitado de Nós (corpus a 16 kHz)** y rechazo del sector cultural gallego a un canal "100 % IA".
9. **Protocolo ciego en 5 rondas** (§7): R0, criba automática con ASR; R1, MUSHRA con **referencia rotatoria y segundo humano oculto** (promotor y mujer, con auriculares); R2, preferencia por pares y **prueba de sueño en dispositivos reales**; R3, **panel de 20-24 nativos con filólogo**: primero la **identificación humano/IA en seco, sin cama sonora** (10 fragmentos de ~3 min, 5 voces × 2, con controles positivo y negativo, más un bloque corto con cama, solo informativo) y después un MUSHRA ligero; R4, repetición sobre el episodio publicado antes de monetizar.
10. **Umbral para aprobar una voz** (§7.6): corrección A ≥ 80; **distancia a la referencia oculta ≤ 10 puntos en A, B y C**, un listón que **el humano de control también tiene que cumplir** (si no lo cumple, se aplica la recalibración prerregistrada); 0 errores graves; ≤ 1 molestia cada 10 min; y en la identificación, **exactitud equilibrada ≤ 0,60 con el límite superior del IC 90 % ≤ 0,70, calculada por oyente sobre ≥ 20 oyentes**, con el control positivo ≤ 0,60 y el negativo ≥ 0,75.
11. **Control automático de pronunciación** (§9): doble ASR (Whisper y w2v-BERT-gl de Nós) contra el guion, párrafo a párrafo, calibrado con las grabaciones de los dos narradores. **Detecta omisiones, repeticiones y palabras mal leídas. No detecta el acento**: eso sigue siendo trabajo del oído humano.
12. **Árbol de decisión** (§8): en la Etapa 1, la mejor voz que cumpla el listón (primero Nós, después las de pago). **Si no lo cumple ninguna, hay tres salidas y ninguna es "publicar igual":** (a) no publicar y repetir la prueba cuando salgan modelos nuevos; (c) **vía intermedia**: *fine-tune* de StyleTTS2-GL con 30-60 min de H1 o H2, con la opción ya firmada (~700-1.250 € hasta saber si funciona; licencia de publicación prefijada y pagada solo si aprueba; §5B.4); (b) **plan B**, locutor con licencia y clonación completa (1.000-2.500 €). (c) y (b) obligan a reabrir el presupuesto de la Etapa 1 con el promotor. En la Etapa 3, licencia completa y extensión es/pt.
13. **Método de producción** (§5B): la calidad no sale de una toma. Cada frase se genera 3-5 veces con el contexto de la anterior y se elige la mejor (máquina + director humano en las dudosas); pausas y entonación siguen un modelo aprendido de los narradores humanos y se validan en el test ciego; y cada episodio pasa una **escucha de corrección nativa** (completa en la Etapa 1 y por muestreo estadístico en la Etapa 2), con las horas y el coste integrados en las etapas. **Desde la v5, esa escucha la firma solo un revisor calibrado.** Cada revisor de la casa pasa una prueba de defectos sembrados (≥ 90 % de acierto en graves y ≥ 70 % en leves), que se repite cada trimestre. Un **corrector o asesor lingüístico galego profesional y pagado** escucha los 6 primeros episodios y cada muestreo de la Etapa 2, y sus hallazgos son la verdad de referencia con la que se mide a la casa. El plan de muestreo se ha rehecho con esas sensibilidades: se esperan **~0,5 bloques de 2 min con algún defecto por episodio de 2 h** (0,48-0,53) con *p* ≤ 3 %, y ~0,17 con un defecto grave. No es cero, y el documento lo dice (§5B.3).
14. **Expectativa honesta [S]:** es **probable que ninguna voz sintética en galego "de fábrica" pase hoy la identificación ciega con fragmentos largos frente a narradores profesionales** (lo estimo en un 60-80 %, aun con el método de §5B). El plan de negocio debe tratar ese suspenso como escenario central. **Su salida realista dentro de un presupuesto pequeño es la vía intermedia (c)**, con un 30-50 % estimado de aprobar [S]. Si también falla, quedan (a) o (b). Por eso el test tiene que ser válido: **un suspenso solo activa (c) o (b) si los controles positivo y negativo han pasado** (§7.6, §8.1).

---

## 1. Qué tiene que hacer bien una "voz de durmir" en galego

El formato elegido (`drafts/formato.md`) exige cosas que las fichas de los motores TTS no miden. Se traducen en siete requisitos, que son los que puntúa el protocolo:

| # | Requisito | Por qué importa en este canal | Cómo se mide |
|---|---|---|---|
| R1 | **Corrección galega**: fonética normativa, vocales abiertas y cerradas, topónimos, sin gheada ni seseo involuntarios, sin "sotaque" castellano o portugués | La comunidad lingüística castiga los errores de lengua (contexto del proyecto; `research/audiencia.md`). Un fallo en "Xelmírez" o "Mondoñedo" se oye en los comentarios | Escala A de MUSHRA (§7.5), texto trampa (§7.3), ASR (§9) |
| R2 | **Naturalidad y prosodia** en frases largas y subordinadas | El guion usa frases largas y cadenciosas (`drafts/guion.md`). La prosodia de "lectura de noticias" rompe el arrullo | Escala B de MUSHRA y prueba de identificación (§7.7) |
| R3 | **Calma y "arrullo"**: timbre cálido, sin sibilancias, sin énfasis bruscos | Es la promesa del producto: "sen sustos" (`drafts/formato.md` §0) | Escala C de MUSHRA y prueba de sueño real (§7.5) |
| R4 | **Estabilidad en tiradas largas**: sin *glitches*, sin deriva de timbre ni de acento en 60-120 min | 404 Media documenta un *glitch* audible en un vídeo IA de 2,3 M de vistas [F] https://www.404media.co/ai-generated-boring-history-videos-are-flooding-youtube-and-drowning-out-real-history/ | Escucha larga (R2) y detector automático (§9.5) |
| R5 | **Controlabilidad del ritmo**: 110-125 palabras/min percibidas sin "arrastrar" las vocales | Narración humana para dormir: 94-115 palabras/min; canales IA: 120-160 [MED] `research/formato.md` §3.2 | Medición automática con alineamiento (§9.4) |
| R6 | **Calidad de señal**: ancho de banda, suelo de ruido y ausencia de artefactos de vocoder en el dispositivo real del oyente | El oyente duerme con el móvil en la mesilla o con auriculares de botón a volumen bajo. Un zumbido metálico o un clic se oyen más en el silencio de la noche | Objetivos de §5.3, detector de §9.5 y escucha en dispositivos reales (§7.5) |
| R7 | **Sostenibilidad**: licencia comercial clara, coste dentro de la etapa y proveedor estable | Presupuesto de < 50 €/mes en la Etapa 1 (contexto del proyecto) | §3 y §4 |

R1-R3 son de oído humano. R4-R6 se miden en parte por máquina. R7 es documental.

---

## 2. Comparativa de opciones de voz

### 2.1 Tabla general

| Opción | Galego | Voces (datos del corpus de entrenamiento) | Calidad esperada | Control de ritmo y estilo | Madurez / riesgo técnico |
|---|---|---|---|---|---|
| **A. Nós StyleTTS2 Brais / Celtia** | Nativo (G2P Cotovía + PL-ModernBERT-gl) [F] https://huggingface.co/proxectonos/Nos_StyleTTS2-Brais-GL | **Brais:** "professional male voice talent", elegido entre 3 candidatos con un test perceptivo de 37 oyentes; grabado en estudio; ~18 h, 16.121 frases; **WAV a 16 kHz y 16 bits** [F] https://huggingface.co/datasets/proxectonos/Nos_Brais-GL . **Celtia:** "professional female voice talent", elegida entre 4 con más de 50 oyentes; ~25 h, 20.000 frases; 16 kHz [F] https://huggingface.co/datasets/proxectonos/Nos_Celtia-GL . *La ficha del modelo no dice que sean actores de doblaje ni da horas: esos datos vienen de la ficha del dataset.* | Pronunciación: alta [S]. Prosodia en tirada larga: [?]. DNSMOS OVRL **predicho** (speechmos, no es MOS humano): 3,43 / 3,44 / 3,40 en textos cortos, medios y largos (> 60 s), frente a 3,31 del corpus original y 3,24-3,28 del VITS de Brais [F] ficha del modelo. **Ancho de banda útil ≤ 8 kHz**, por estar entrenado con audio a 16 kHz aunque el preprocesado trabaje a 24 kHz [F ficha + S sobre su efecto] | Medio. Valores recomendados para Brais: `alpha 0.6`, `beta 1.0`, `t 0.6`, `diffusion_steps 10`, `embedding_scale 1.0` [F] ficha. La velocidad se toca escalando las duraciones en el código [S] | Publicados en junio y julio de 2026, sin comunidad todavía. Hace falta GPU (sirve Colab T4) [S] |
| **B. Nós VITS / Matcha** (Sabela-Nós, Icía, Iago, Paulo, Brais, Celtia) | Nativo [F] https://huggingface.co/api/models?author=proxectonos | **Sabela-Nós:** 9.999 frases de una "professional radio broadcaster" [F] https://huggingface.co/proxectonos/Nos_TTS-sabela-vits-phonemes . **Icía:** 2.950 frases, "amateur voice talent" (*fine-tune* sobre Celtia). **Iago y Paulo:** 1.316 frases cada uno, amateurs [F] fichas de `Nos_TTS-icia/iago/paulo-vits-phonemes` | Media. Prosodia más plana que StyleTTS2 [S] | `length_scale` y `noise_scale` (VITS); `speaking_rate` y `temperature` (Matcha) [S] | Maduros. Corren en CPU. Hay versión ONNX de Celtia en Colab (Pronunza) [F] https://github.com/gas/pronunza-tts-galego-onnx-colab |
| **C. Azure Sabela / Roi** (y Clipchamp, que usa las mismas voces) | Oficial [F] https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts | `gl-ES-SabelaNeural` (F) y `gl-ES-RoiNeural` (M). **Sin estilos, sin HD y sin Custom/Personal Voice para gl-ES** [F] ídem. Salida a 24 kHz o 48 kHz (formato `Riff48Khz16BitMonoPcm`) [F-sec] ídem y https://learn.microsoft.com/en-us/dotnet/api/microsoft.cognitiveservices.speech.speechsynthesisoutputformat | Media: correcta pero "de lectura de noticias" [S] | SSML `prosody rate/pitch` y `break` [S; verificar en gl-ES] | Muy estable. Es la **línea base** del A/B |
| **D. Google** | Standard-B: GA. Gemini-TTS gl-ES: **Preview** [F] https://docs.cloud.google.com/text-to-speech/docs/gemini-tts | Standard-B (una sola voz). Gemini-TTS: voces multilingües dirigidas por prompt. Salida PCM de 16 bits a **24 kHz**; como mucho 4.000 bytes de texto por petición [F] ídem | Standard-B: baja (se usa como **ancla** sintética). Gemini: [?] | Gemini: alto (instrucciones en lenguaje natural: "fala baixo, amodo…") | En Preview puede cambiar o empeorar sin aviso [S] |
| **E. ElevenLabs v4 / v3** | Galego (glg) listado en **v4, v3 y v3 Conversational**; no en Multilingual v2 ni en Flash v2.5 [F] https://elevenlabs.io/docs/overview/models | Biblioteca de voces, *Voice Design* y clonación. MP3 a 44,1 kHz en los planes bajos; PCM a 44,1 kHz por API desde el plan Pro [F] https://elevenlabs.io/pricing | Expresividad muy alta. Galego: [?], sin reseñas públicas | Alto: etiquetas de audio, velocidad y estabilidad [F-sec] https://elevenlabs.io/blog/eleven-v3 | Límite de 10.000 caracteres por petición en v4 y de 5.000 en v3 [F] docs de modelos. Riesgo de *hallucination* (saltarse o repetir frases) en textos largos [S] |
| **F. OpenAI gpt-4o-mini-tts** | "Sigue a Whisper", que incluye el galego, "despite voices being optimized for English" [F] https://developers.openai.com/api/docs/guides/text-to-speech | Voces genéricas en inglés | Probable acento extranjero [S] | Medio (instrucciones) | Candidato de relleno. Solo entra en R0 |
| **G. Locutor galego con licencia** (clonación ElevenLabs PVC o *fine-tune* de StyleTTS2-GL) | Nativo | La del locutor, grabada a 48 kHz | La mejor posible [S], pero **también tiene que pasar la Puerta V**: un clon no es el locutor | Alto | Coste, contrato y sensibilidad sectorial (§6). **Etapa 3, o antes como plan B (§8.1)** |
| *Excluida:* `edge-tts` (voces de Edge "Read aloud" sin API) | Sabela/Roi | | | | Servicio no oficial; va contra los términos de Microsoft y puede bloquearse en cualquier momento [F-sec] https://github.com/rany2/edge-tts , https://learn.microsoft.com/en-us/answers/questions/2392491/unofficial-edge-tts-api |

### 2.2 Valoración de cada opción para este canal [S salvo cita]

- **A. Nós StyleTTS2.** Es el candidato con más sentido estratégico: galego "de verdad" (G2P hecho en Galicia), gratis, abierto y con un relato legítimo ("voz do Proxecto Nós, USC"). Tiene tres incógnitas: la prosodia en fragmentos largos, la estabilidad en 60-120 min y el **techo de ancho de banda**. Con el corpus a 16 kHz no hay contenido real por encima de ~8 kHz. Con auriculares y frente a una referencia a 48 kHz eso puede sonar "apagado" y delatarlo en la identificación. La cadena final corta igualmente por encima de 9-10 kHz (§5.1), así que la diferencia se reduce, y es la prueba ciega la que dice si se nota. Debilidad operativa: se ejecuta a mano (clonar el repositorio de HF, instalar Cotovía, PyTorch), algo que Claude Code puede empaquetar en un script de Colab.
- **B. Nós VITS/Matcha.** Sirven de reserva gratuita y de comparación interna. Sabela-Nós (locutora de radio profesional) es la más prometedora de este grupo. Icía, Iago y Paulo son amateurs con pocas frases y solo entran en R0.
- **C. Azure Sabela/Roi.** Es el suelo conocido y la única opción que da 48 kHz nativos. El promotor y su mujer ya la oyeron, lo que introduce un **sesgo de reconocimiento** (§7.2). Con el listón nuevo es muy improbable que la apruebe [S]: "correcto pero plano" no pasa de ≤ 10 puntos de un narrador profesional en B.
- **D. Gemini-TTS.** Lo interesante es el control del estilo por prompt a un precio muy bajo. Riesgos: Preview, posible deriva del acento en tiradas largas y el límite de 4.000 bytes, que obliga a trocear y hace más probables las discontinuidades entre trozos.
- **E. ElevenLabs v4/v3.** Es la apuesta de "máxima expresividad" y la más probable de pasar la identificación **si** el acento es correcto. El riesgo es precisamente el acento: vocales abiertas y cerradas neutralizadas "a la castellana" y grafías leídas "a la portuguesa".
- **F. OpenAI.** Solo pasa por la criba automática. Si en R0 suena con acento inglés, se descarta sin molestar a los jueces.
- **G. Locutor licenciado.** Es el techo de calidad y el modelo de *History at Night* (voz clonada con licencia; 1,16 M de vistas con 47 min) [MED] `research/formato.md`. Con el listón de la ronda 2 deja de ser solo una opción de la Etapa 3 y pasa a ser el **plan B natural** si ninguna voz abierta o comercial llega al listón.

---

## 3. Coste por hora narrada

**Supuesto de volumen [S]:** 1 hora de vídeo a ~115 palabras/min percibidas ≈ 6.900 palabras ≈ **43.000 caracteres** (6,2 caracteres por palabra con espacio; `research/voz_guion.md` §1.8). Se añade un **30 % de regeneraciones** (párrafos que fallan en la QA) ≈ **56.000 caracteres por hora publicada**.

| Opción | Precio de tarifa | Coste por hora publicada (con el 30 % de regeneración) | Coste en la Etapa 1 (2 vídeos de 75 min/mes ≈ 2,5 h) | Coste en la Etapa 2 (≈ 9 h/mes: 4 × 2 h + compilación) |
|---|---|---|---|---|
| Nós StyleTTS2 | 0 € el modelo + GPU. Colab gratis, o T4/A4000 alquilada a ~0,2-0,5 USD/h [S] `research/voz_guion.md` §3 | **< 0,10 USD** si el factor de tiempo real ronda 0,1-0,2 en GPU [S; medir] | 0 € (Colab gratis) | 0-10 € (Colab Pro o GPU por horas) |
| Nós VITS/Matcha | 0 € (CPU) | **0** | 0 € | 0 € |
| Azure Sabela/Roi | 15 USD/1M caracteres; capa gratuita de 500k caracteres/mes [F] https://prices.azure.com/api/retail/prices , https://azure.microsoft.com/en-us/pricing/details/speech/ | **~0,84 USD** (0 dentro de la capa gratuita, que da para unas 9 h/mes) | 0 € | 0-1 € |
| Google Standard-B | 4 USD/1M caracteres; 4M gratis al mes [F] https://cloud.google.com/text-to-speech/pricing | ~0,22 USD (0 en la capa gratuita) | 0 € | 0 € |
| Gemini-TTS Flash / Pro | 10 / 20 USD por 1M tokens de audio; 25 tokens por segundo [F] ídem | **~1,2 USD / ~2,3 USD** (3.600 s × 25 = 90k tokens × 1,3) [CALC] | ~3 USD | ~11-21 USD |
| ElevenLabs API v4 / v3 | 0,08 USD/1k caracteres (v4 con promoción a 0,022 hasta el 12-10-2026); v4 Turbo 0,04 [F] https://elevenlabs.io/pricing/api | **~4,5 USD** (v4/v3); ~2,2 USD (v4 Turbo) [CALC] | ~11 USD (o el plan Creator, 22 USD/mes con 121k créditos: justo para 2,5 h sin margen) [F] https://elevenlabs.io/pricing | ~40 USD por API (el plan Pro de 99 USD no compensa a este volumen) [S] |
| OpenAI gpt-4o-mini-tts | ~0,015 USD/min [F-sec] https://costgoat.com/pricing/openai-tts | ~1,2 USD | (solo pruebas) | — |
| Locutor licenciado (clon) | Referencia de la UVA: 1.000-1.500 € por demos de voz sintética; 5.000-7.500 € con varias jornadas de grabación [F-sec] https://escueladedoblajedemadrid.es/blog/alerta-maxima-ante-la-cesion-de-voz-para-aprendizaje-neuronal-de-la-ia-segun-uva/ | **20-60 €/h** si 2.000-6.000 € se amortizan en ~100 h de catálogo, más el motor (0-4,5 USD/h) y un posible royalty del 5-15 % de los ingresos [S] | Solo si se activa el plan B (§8.1) | Etapa 3 |

**Coste único de validación (rehecho en la v5 con tarifas contrastadas).** Volumen por narrador [CALC]: ~30 min de guion × ~115 palabras/min = 3.450 palabras, + ~250 del texto trampa = **~3.700 palabras**.

| Referencia de tarifa | Qué es y qué vale como prueba | €/palabra | Por narrador (3.700 palabras) |
|---|---|---|---|
| Cronoshare: audiolibro, 750-1.000 € por 15.000 palabras [F-sec] https://www.cronoshare.com/cuanto-cuesta/locucion | Tarifa **genérica de España** en un portal de profesionales autónomos. **No es del mercado gallego** | 0,05-0,067 | 185-250 € |
| Escena Digital (locutortv.es), tarifas generales: "Audiolibros - 2000 palabras: 450 €", con descuentos de "20 a 40 %"; "Casting (por locutor): 200 €"; precios sin IVA [F-sec, página abierta el 29-09-2026] https://www.locutortv.es/presupuestos_y_tarifas.htm | **Agencia con catálogo de locutores galegos** (https://www.locutortv.es/locutores_gallegos-locutor.htm), pero con una tarifa general que no es específica del galego. Es el precio de lista con el margen de la agencia | 0,135-0,225 | 500-830 € (+ IVA) |
| Voicebros: narración de audiolibro, 100-300 USD por hora terminada [F-sec] https://voicebros.com/en/voice-over-rates | Mercado internacional por hora terminada (~0,55 h aquí). Solo es un orden de magnitud | — | ~50-150 € |
| *Retirada en la v5:* "locución en galego desde 0,29 €/palabra" | Salía de un fragmento de buscador. Al abrir las páginas (Trágora, Anyvoz, LocutorTV), **ninguna publica precios del galego**: todas piden presupuesto | — | — |

**Presupuesto de planificación [S]: 0,08-0,135 €/palabra, es decir, 300-500 € por narrador**, contratando al narrador directamente y no a la agencia (por eso queda por debajo del precio de lista), con el uso interno y sin publicación como argumento de negociación. Salen **600-1.000 € por H1 + H2**, **+300-500 € por el H3 opcional** y un **techo de 1.500 €** para las grabaciones. **Regla:** en la semana 1 se piden 3 presupuestos por escrito. Si los dos más baratos que cumplen el perfil (§7.2) superan el techo, se pasa a la variante mínima; no se recorta el control positivo.

**Revisor lingüístico profesional (nuevo en la v5; §5B.3.2):** escucha de los 6 primeros episodios más la prueba sembrada, **~250-500 €** una sola vez [S; tarifa sin fuente gallega verificada].

**Total de la excepción única: ~850-1.500 € (H1 + H2 + revisor)**, y hasta ~2.050 € con H3 y el sorteo del panel. **No cabe en el sobre de la Etapa 1 (< 50 €/mes, < 300 € en 6 meses).** **Es una excepción presupuestaria que el promotor tiene que aprobar de forma explícita** (Q1, §11). Justificación: con un solo humano, un suspenso de la IA no se distingue de un fallo del test, y ese suspenso activaría 1.000-2.500 € de plan B. Y sin un revisor calibrado, la corrección galega de lo publicado, que es la condición no negociable del proyecto, no tiene un juez medido. **Variante mínima si Q1 se aprueba solo en parte [S]:** 2 narradores con ~20 min cada uno (~2.550 palabras → 205-345 € por narrador, **~400-700 € los dos**) y 8 fragmentos de 2,5 min en la identificación. La potencia baja un poco, pero el control positivo se mantiene. **El revisor profesional de los 6 primeros episodios no entra en lo que se puede recortar.**

**Coste del método de producción de §5B (nuevo en la v4) [CALC sobre S]:**

| Concepto | Etapa 1 | Etapa 2 |
|---|---|---|
| N = 4 variantes por frase con Nós (GPU + ASR + UTMOSv2) | 0 € en Colab, o ~0,5-1,5 USD/mes en GPU alquilada | ~1-3 USD/mes |
| N = 4 con un motor de pago | ×4 en la tarifa de la tabla (ElevenLabs: ~18 USD por hora publicada). **Se usa N = 2 y se sube a 4 solo en las frases que fallen** | ídem |
| Escucha de corrección (§5B.3) | La casa: 1,0-1,6 h por episodio, según la velocidad para la que esté validado cada revisor. **Revisor profesional:** ~250-500 € una vez (episodios 1-6 + prueba sembrada) y, después, una cata de 20 bloques uno de cada 4 episodios (~8-14 €/mes) [S] | Revisor profesional para 20 bloques por episodio: **48-84 €/mes con 3 episodios** (64-112 € con 4) [S]. La casa escucha otros 20 bloques y los rechazos |
| Prueba de defectos sembrados (§5B.3.1) | 0 € (script y horas de la casa: ~2 h por revisor, una vez) | ~0,6 h por revisor cada trimestre |
| Vía intermedia (§5B.4), **solo si se activa** | ~700-1.250 € una vez hasta saber si funciona; si aprueba, licencia de 300-600 € + 10-15 % de ingresos | — |

**Lectura.** Salvo la licencia de locutor, ninguna voz supera los 45 USD al mes ni siquiera en la Etapa 2. **El precio no debe decidir la voz.** Lo que la decide es la calidad percibida frente a un humano y la estabilidad. El coste real está en el tiempo humano de escucha y corrección, que el control automático de §9 reduce y que el método de §5B ordena y presupuesta.

---

## 4. Licencias y uso comercial

| Opción | ¿Uso comercial en YouTube? | Condiciones y cabos sueltos | Acción |
|---|---|---|---|
| Nós (todos los modelos) | Sí, por la licencia Apache-2.0 del **modelo** [F] fichas de HF | Los **datasets** Brais y Celtia llevan la etiqueta CC-BY-4.0, pero sus términos dicen "solely for research purposes and for developing artificial intelligence tools focused on linguistic objectives" y prohíben la "public exposure" de las grabaciones. En Celtia, la propiedad de la voz está cedida a la USC durante 15 años y los datos se borran desde el 30-11-2037 [F] fichas de `Nos_Brais-GL` y `Nos_Celtia-GL`. El audio sintético no es la grabación, pero la voz es reconocible como la de una persona real [S] | **Correo a Proxecto Nós (proxecto.nos@usc.gal) en la semana 0** pidiendo confirmación del uso en un canal monetizado. **Solo se publica con la confirmación escrita en la mano** (correo o documento de la USC que cite el uso en YouTube con monetización). El silencio no es consentimiento: los términos dicen "solely for research purposes", y la cautela que aplica este documento a todas las demás licencias no admite leerlos a favor. Si no hay respuesta en 30 días: segundo correo con copia a los responsables que figuren en las fichas y consulta por la vía de transferencia de la USC por si hace falta un acuerdo formal [S: no se ha verificado que la USC tenga un procedimiento para esto]. Mientras tanto se aplica §8.1 (voz de pago aprobada o esperar). Crédito en la descripción: "Voz sintética: Proxecto Nós (USC), modelo Nos_StyleTTS2-Brais-GL, Apache-2.0" |
| Azure Sabela/Roi | Sí, dentro de las condiciones del servicio [S; son las condiciones estándar de Azure] | Microsoft recomienda transparencia con la voz sintética [S] | Nota de proceso en la descripción |
| Clipchamp (TTS integrado) | Sí: "licensed for personal and commercial use" [F] https://learn.microsoft.com/en-us/answers/questions/5779941/permissions-to-use-clipchamp-ai-text-to-voice-for | No permite redistribuir la pista de voz por separado [F] ídem | Útil solo para prototipos (demasiado manual) |
| `edge-tts` | **No** (servicio no oficial) [F-sec] https://github.com/rany2/edge-tts | Puede cortarse en cualquier momento | **Excluido** |
| Google Cloud / Gemini-TTS | Sí (condiciones de Google Cloud) [S] | Preview: sin garantías de continuidad [S] | Guardar la versión del modelo que se usa |
| ElevenLabs | Sí, desde el plan Starter [F] https://elevenlabs.io/pricing | Las voces de la *Voice Library* traen licencia comercial gratuita, pero su dueño puede retirarlas con un preaviso que él mismo elige, desde retirada inmediata hasta 2 años [F] https://elevenlabs.io/docs/eleven-creative/voices/payouts | Si se usa una voz de la biblioteca, elegir solo voces con preaviso largo y guardar un plan B |
| OpenAI | Sí; sus políticas exigen avisar al usuario de que la voz es generada por IA [F] https://developers.openai.com/api/docs/guides/text-to-speech | | Solo pruebas |
| **Grabaciones de referencia de los 2-3 narradores** (§7.2) | **No se publican** | Contrato en **tres tramos separados**, cada uno con su consentimiento expreso (coherente con la cláusula PASAVE que defiende el sector: nada de entrenamiento sin un consentimiento específico, `research/voz_guion.md` §1.6). **T0 (se ejecuta siempre):** referencia de uso interno de evaluación, sin publicar y **sin entrenamiento ni clonación**; se borra a los 24 meses. **T1 (opción, se ejecuta solo si el promotor la activa en 6 meses):** grabación extra de 30-60 min y cesión para el *fine-tune* **solo para evaluación interna**. **T2 (opción, solo si el modelo pasa la Puerta V-2):** licencia de publicación de 12-24 meses, un canal, con fijo + porcentaje, revisión de muestras y borrado final (§5B.4) | El narrador puede firmar T0 y rechazar T1/T2. Precio de T1 y T2 fijado al firmar |
| Locutor licenciado | Por contrato | Buenas prácticas: medios y plataformas definidos, duración limitada, exclusividad opcional y tarifa por uso [F-sec] https://www.milenio.com/negocios/que-debe-contener-un-contrato-para-licenciar-una-voz-a-ia | §8.3 |

**YouTube.** El canal declarará siempre el proceso en la descripción ("narración sintética; guion revisado por…"), según la política de etiquetado y de "inauthentic content" recogida en `drafts/retornos.md` y `research/retornos.md` §6. Con una **voz clonada de una persona real**, además se activa la etiqueta "Altered or synthetic content" en Studio. El propio YouTube pone como ejemplo de declaración "synthetically generating a person's voice to narrate a video" [F] `research/retornos.md` §6.2. **"Indistinguible" es un listón de calidad, no un intento de engañar:** el canal dice siempre que la voz es sintética.

---

## 5. Control de ritmo, tono y señal para dormir

### 5.1 Objetivos de ritmo y tratamiento (comunes a todas las voces)

| Parámetro | Objetivo | Fuente |
|---|---|---|
| Ritmo percibido (pausas incluidas) | 110-125 palabras/min | [S sobre MED] `drafts/formato.md` §0, `research/formato.md` §3.2 |
| Ritmo "hablado" (sin pausas) | ~140-155 palabras/min: velocidad natural de lectura pausada. Las pausas bajan la media [S] | Se calibra en R1 **con las grabaciones profesionales (H1 y H2)** como patrón |
| Pausa entre frases / párrafos / capítulos | 0,6-0,9 s / 1,5-2,5 s / 5-10 s (solo ambiente) | `research/formato.md` §3.2 |
| Sonoridad integrada | −16 LUFS, limitador a −1,5 dBTP y sin picos | `research/formato.md` §3.6 |
| Cama sonora | 20-26 dB por debajo de la voz | ídem |
| Ecualización | Paso alto a 70-80 Hz; realce leve de 150-250 Hz para dar calidez; de-esser (4-8 kHz); caída suave por encima de 9-10 kHz [S] | Práctica de audio [S] |

**Principio de diseño [S]:** las pausas **las pone la posproducción y no el motor TTS**. El motor sintetiza párrafo a párrafo (o frase a frase) y el ensamblador inserta silencios medidos. Con esto se consigue que (a) todas las voces sean comparables, (b) el ritmo sea exacto y (c) un fallo solo obligue a regenerar un párrafo. La referencia humana conserva sus pausas naturales, porque es el patrón que se quiere alcanzar. Solo recibe la misma cadena de EQ y sonoridad. **Desde la v4, los valores de la tabla son las medias por acto; la duración de cada pausa concreta la da el modelo aprendido de H1/H2 (§5B.2)**, si gana a las pausas fijas en la comparación ciega.

### 5.2 Palancas por motor

| Motor | Velocidad | Estilo / calma | Pronunciación dudosa (topónimos) |
|---|---|---|---|
| Nós StyleTTS2 | Escalar las duraciones predichas (×1,05-1,15) en el script de inferencia [S] | Partir de los valores recomendados (`alpha 0.6`, `beta 1.0`, `t 0.6`, `diffusion_steps 10`) [F] ficha; `t` alto para la continuidad entre fragmentos; probar un audio de referencia de estilo "íntimo" [?] | Léxico de Cotovía o reescritura fonética solo en la entrada del TTS [S] |
| Nós VITS | `length_scale` 1,1-1,2 | `noise_scale` más bajo = más estable y más plano [S] | Modelos de fonemas: se edita la transcripción [S] |
| Azure | `<prosody rate="-10%" pitch="-2st">` | Sin estilos [F] | `<phoneme>` o `<sub alias>` [S; verificar en gl-ES] |
| Gemini-TTS | Instrucción: "Le en galego, moi amodo, con voz baixa e cálida…" | Prompt de estilo | Reescritura de la entrada [S] |
| ElevenLabs v4/v3 | Velocidad ~0,8-0,9; estabilidad alta [F-sec] | Etiquetas de audio (`[calm]`, `[softly]`) [F-sec] | Diccionarios de pronunciación [?, verificar si aplican a v4 en galego] o reescritura |

**Reescritura fonética [S]:** para palabras problemáticas se mantiene un fichero `lexico_tts.tsv` (forma escrita, forma que se envía al TTS, fuente). La forma que se envía puede llevar tildes diacríticas que la norma no escribe o una ortografía forzada; el subtítulo usa siempre el texto normativo. La pronunciación correcta se comprueba en el **Dicionario de pronuncia da lingua galega** (ILG/RAG), que incluye topónimos [F] https://ilg.usc.es/pronuncia/ . Las grabaciones profesionales (§7.2) sirven también de **patrón auditivo** para los topónimos del piloto.

### 5.3 Objetivos técnicos de la señal (nuevo) [S salvo cita]

Son requisitos de publicación, y el QA automático los comprueba en cada episodio (§9.5).

| Aspecto | Objetivo | Cómo se consigue o se mide |
|---|---|---|
| **Frecuencia de muestreo nativa por motor** | Se sintetiza a la frecuencia nativa del motor: Nós StyleTTS2 a 24 kHz (preprocesado a 24 kHz; corpus a 16 kHz) [F]; Azure a 48 kHz (`Riff48Khz16BitMonoPcm`) [F-sec]; Gemini a 24 kHz [F]; ElevenLabs a 44,1 kHz [F]. **No se sintetiza a una frecuencia menor para luego subirla.** | Registrar en `decision_voz.md` el formato de salida de cada motor. Medir el **ancho de banda efectivo** (frecuencia por debajo de la cual está el 99 % de la energía) de 60 s de cada voz |
| **Remuestreo** | Un solo remuestreo, al final, a **48 kHz** con un remuestreador de calidad (`soxr` en ffmpeg: `aresample=48000:resampler=soxr`). Se trabaja internamente en coma flotante de 32 bits | Script de ensamblado |
| **Master de entrega** | WAV mono o estéreo duplicado, **48 kHz / 24 bits**, −16 LUFS integrados, −1,5 dBTP, rango de sonoridad (LRA) de la voz ≤ 6 LU | `ffmpeg loudnorm` en dos pasadas + `pyloudnorm` para verificar |
| **Ancho de banda y extensión** | No se "inventan" agudos por defecto. Si Nós (≤ 8 kHz útiles) queda por debajo del listón **y** los comentarios del panel señalan "soa apagado/de teléfono", se prueba como configuración adicional una extensión de ancho de banda por IA (p. ej. AudioSR o AP-BWE [S; sin probar]), que pasa por el mismo protocolo ciego | Configuración extra en R1 |
| **Suelo de ruido de la voz** | En las pausas de la pista de voz (antes de la cama sonora): **≤ −65 dBFS RMS**. Las pausas se rellenan con *room tone* del propio motor o de la grabación, a −70/−65 dBFS, y **nunca con silencio digital puro** (el salto de "silencio absoluto" a "voz con ruido" se percibe como un corte) | Medición automática en todos los silencios > 0,5 s |
| **Uniones entre párrafos** | Corte en paso por cero y fundido cruzado de 10-30 ms con el *room tone*; **0 clics** audibles | Detector de discontinuidades (salto de muestra > umbral) |
| **Artefactos de vocoder** | Sin zumbido metálico, "fase" o ruido tonal en las eses y en las respiraciones; sin ruido musical por reducción de ruido | (1) Detector: ráfagas de planitud espectral o energía anómala por encima de 6 kHz de < 200 ms (§9.5); (2) escucha dirigida de los puntos marcados; (3) si aparecen: regenerar con otra semilla, bajar `diffusion_steps` o la variabilidad (`noise_scale`), suavizar con un de-esser dinámico. **Nunca** una reducción de ruido agresiva, que empeora los artefactos |
| **Respiraciones** | Se conservan si suenan naturales, bajadas 6-10 dB. Se eliminan si son sintéticas o "raspan" | Escucha y detector |
| **Compatibilidad con dispositivos** | Inteligible y sin sibilancias en el **altavoz del móvil** (que corta por debajo de ~200-300 Hz [S]) y en **auriculares de botón a volumen bajo** (35-45 dB SPL aproximados [S]) | Escucha en dispositivos reales en R2 y R3 (§7.5) |

## 5B. Método de producción: llevar la voz sintética a calidad de audiolibro en cada episodio (nuevo en la v4)

La Puerta V (§7) **mide** si una voz llega al listón, pero no **fabrica** esa calidad ni la mantiene episodio a episodio. Un audiolibro humano tampoco sale de una toma única: el locutor repite frases y un director de grabación escoge, corrige y escucha el máster entero. Esta sección traslada ese oficio a la voz sintética en cuatro piezas:

| Pieza | Qué hace | Equivalente en un estudio | Dónde se valida |
|---|---|---|---|
| **5B.1 Síntesis con contexto y "mejor de N"** | Genera 3-5 variantes de cada frase, encadenadas con el contexto anterior. Una puntuación automática elige y un humano dirige solo las frases dudosas | El locutor repite la toma y el director elige | R1-R3 (el kit ya se renderiza así) y R4 |
| **5B.2 Modelo de pausas y entonación** | Pausas y caída tonal de final de párrafo aprendidas de H1/H2, en vez de valores fijos | La respiración y la cadencia del narrador | Comparación ciega "pausas fijas / modelo de pausas" (R1, R2 y R3) |
| **5B.3 Escucha de corrección** | Revisores de la casa **calibrados con defectos sembrados**; un **corrector profesional de referencia** en los 6 primeros episodios y en cada muestreo; escucha completa en la Etapa 1 y muestreo de aceptación en la Etapa 2, diseñado con la sensibilidad medida | La escucha de control de calidad (QC) del máster por un corrector de audio o un asesor lingüístico | Prueba sembrada (inicial y trimestral), captura-recaptura con el profesional y tasa de defectos residuales por episodio |
| **5B.4 Vía intermedia: *fine-tune* con licencia** | StyleTTS2-GL ajustado con 30-60 min de H1 o H2 en estilo "durmir", con la cesión firmada en el mismo contrato que las referencias | Contratar al narrador, pero pagando solo lo que se usa | La misma Puerta V (§7.6) |

**Regla de coherencia con el protocolo.** Todas las voces sintéticas del kit (R1-R3) se renderizan con 5B.1 (solo la parte automática) y 5B.2. Así se compara **lo mejor que puede dar cada motor con el método de producción real**, y no una toma única. El pase humano de dirección de 5B.1 **no se aplica al kit**: lo haría el promotor, que es juez y rompería el ciego (§7.2, sesgo del constructor). Esto es conservador, porque el producto real sale algo mejor que el kit, y **R4 lo comprueba sobre el episodio publicado, que sí lleva el pase humano**.

### 5B.1 Síntesis con contexto y selección entre variantes

**Unidad:** la frase. Es la unidad en la que ya trabaja el renderizador (`drafts/formato.md` §3A.2) y la que el ASR comprueba (§9.3). Un episodio de 75 min tiene unas 8.500 palabras; con ~20 palabras por frase son **~420 frases** [CALC sobre `drafts/formato.md` §3A.3].

**a) Contexto al motor.** El motor recibe el contexto del párrafo anterior, para que cada frase continúe la anterior en lugar de "empezar de cero":

| Motor | Mecanismo de contexto | Fuente |
|---|---|---|
| Nós StyleTTS2 | Estilo encadenado: el vector de estilo de la frase se mezcla con el de la frase anterior ya elegida (`s_pred = t·s_prev + (1−t)·s_pred`). Es la función `LFinference` de la demo oficial de StyleTTS2 para textos largos, y el parámetro `t` es el que recomienda la ficha de Nós. **Se encadena con la variante elegida y no con la última generada** | [F] https://github.com/yl4579/StyleTTS2/blob/main/Demo/Inference_LibriTTS.ipynb ; ficha de Nós (§2.1). El PL-ModernBERT-gl solo ve la frase, así que el contexto textual no llega al modelo [S] |
| ElevenLabs | `previous_text`, `next_text` y `previous_request_ids` ("improve the speech's continuity when concatenating together multiple generations") y `seed` para reproducir | [F] https://elevenlabs.io/docs/api-reference/text-to-speech/convert (no dice si `previous_request_ids` funciona en v3/v4: verificar [?]) |
| Gemini-TTS | Se envía el párrafo anterior en el prompt como contexto, con la instrucción de leer solo la frase objetivo | [S; comprobar que no lo lee en voz alta] |
| Azure / VITS / Matcha | No tienen mecanismo de contexto. Se sintetiza por párrafo (Azure) o por frase, y la continuidad depende solo de las pausas y de la selección | [S] |

**b) N variantes.** Por defecto **N = 4** (rango 3-5) por frase, con semillas distintas (StyleTTS2: ruido de la difusión; VITS/Matcha: `noise_scale`; ElevenLabs: `seed`). Se hace de forma **secuencial**: la frase *k* se genera con el estilo de la variante ya elegida para *k−1*. Si se vuelve a generar una frase después, se regeneran también las siguientes de su párrafo, para que la cadena no se rompa; el corte de párrafo, con su pausa larga, absorbe el salto [S].

**c) Puntuación automática (fórmula fija y versionada en `seleccion_v1.yaml`) [S salvo cita].** Se aplica en dos pasos:
1. **Filtros eliminatorios** (una variante que falla no puede ganar): marcas `OMISION`, `INSERCION`, `WER_ALTO` o `LISTA_CRITICA` del ASR (§9.3); cualquier anomalía de señal de §9.5 (clic, ráfaga > 6 kHz, recorte); duración fuera de ±20 % de la esperada para esa frase (palabras × ritmo hablado del narrador).
2. **Puntuación entre las supervivientes**, normalizada dentro de la misma frase (la escala absoluta no importa, solo el orden):
   - **Calidad predicha:** UTMOSv2 (predictor de MOS, licencia MIT, 1.º en 7 de 16 métricas de la VoiceMOS Challenge 2024) [F] https://github.com/sarulab-speech/UTMOSv2 y DNSMOS (el que ya usa la ficha de Nós, vía `speechmos`) [F] ficha de Nós. **Ninguno está validado en galego ni en voz "de durmir"** [S]: por eso solo ordenan variantes de una misma frase y su peso se calibra (abajo).
   - **Confianza del ASR:** probabilidad media por palabra de Whisper y acuerdo de los dos ASR (§9.2). Una palabra con confianza baja suele estar mal articulada.
   - **Prosodia frente al modelo de 5B.2:** distancia de la caída de F0 final y del rango de F0 (2-6 semitonos por párrafo; `drafts/formato.md` §3A.1) a la distribución de H1/H2.
   - **Continuidad:** similitud del *embedding* de locutor (ECAPA) con el centroide del capítulo, y salto de F0 medio y de centroide espectral respecto a la frase anterior (controla la deriva, V5).
   - Puntuación = suma ponderada de las cuatro con pesos iniciales 0,3 / 0,2 / 0,3 / 0,2 [S].
3. **Calibración de los pesos (una vez por voz, ~1 h humana).** Se toman 60 frases × 4 variantes. Un nativo **que no sea juez de R1-R3** (p. ej. uno de los narradores H1/H2, como servicio adicional, o una persona del panel que después se excluye de R3) elige la mejor de cada frase a ciegas. El selector automático tiene que acertar la primera elegida en **≥ 50 % de las frases** (el azar es 25 %) y **no elegir nunca una que el humano marque como "inaceptable"**. Si no llega, se ajustan los pesos con esas 60 frases (regresión logística de preferencia) y se comprueba en otras 40. Solo entonces se sella `seleccion_v1.yaml` y se genera el kit.

**d) Pase de dirección humana (solo en producción, no en el kit).** El informe `qa_voz.html` presenta como **dudosas** las frases en las que (i) la diferencia de puntuación entre la 1.ª y la 2.ª variante es pequeña (percentil 10 inferior del episodio), (ii) sobrevive una marca `DISCREPANCIA`, (iii) la frase contiene una palabra de `lista_critica.txt` o (iv) es la última del párrafo y su caída tonal está fuera del rango humano. El director (el promotor o su mujer) oye las 2-3 mejores variantes seguidas y elige, o manda la frase a regenerar con el léxico corregido. **Estimación [S]:** el 10-20 % de las frases, 40-85 por episodio de 75 min, a ~20-25 s cada una: **15-35 min por episodio**.

**Coste de cómputo de N = 4 [CALC sobre S]:** con Nós, sintetizar 4 × 75 min ≈ 5 h de audio. Con un factor de tiempo real de 0,1-0,2 en una RTX 4090 [S; medir], son 0,5-1 h de GPU, es decir, **0,2-0,7 USD por episodio** a 0,34-0,74 USD/h [F] https://www.runpod.io/pricing (o 0 € en Colab). Los ASR y UTMOSv2 sobre 5 h de audio añaden otra ~0,5 h de GPU. Con **motores de pago, N = 4 multiplica el coste por 4** (ElevenLabs v4/v3: ~18 USD por hora publicada en lugar de ~4,5): en ese caso se usa N = 2 y solo se sube a 4 en las frases que no superen los filtros [CALC con §3].

### 5B.2 Modelo de pausas y entonación aprendido de H1/H2

**Problema.** Las pausas de `drafts/formato.md` §3A.3 son valores fijos por acto (p. ej. 1,45 s entre frases y 4,1 s entre párrafos en el Acto I). Un narrador humano no hace eso: alarga la pausa tras una frase larga o antes de un cambio de escena y la acorta dentro de una enumeración. Una pausa idéntica 400 veces es **un patrón que el oído detecta** y que puede delatar a la máquina en la identificación ciega (§7.7). Lo mismo pasa con la entonación: si cada párrafo acaba con la misma caída, o sin ella, suena a lectura mecánica.

**Datos.** Las grabaciones de H1 y H2 (~30 min cada una, S1-S10, más el texto trampa; §7.2): ~3.700 palabras y **~170-190 frases y ~40 finales de párrafo por narrador** [CALC: 3.450 palabras de S1-S10 ÷ ~18-20 palabras por frase = 172-192]. Se alinean palabra a palabra con el guion (alineamiento CTC con w2v-BERT-gl o whisperX; §9.2 y §9.4).

**Modelo de pausas [S].**
- **Qué se mide** en cada frontera: la duración del silencio y sus rasgos. Tipo de frontera: coma, punto y coma o dos puntos, punto dentro del párrafo, fin de párrafo, fin de capítulo, entrada o salida de una cita («…»). Tipo de frase: declarativa, enumeración, cita directa, apelación al oyente ("Pecha os ollos"). Longitud de la frase anterior y de la siguiente, posición en el párrafo, acto y narrador.
- **Modelo:** regresión sobre el logaritmo de la duración, `log(pausa) ~ tipo_frontera + tipo_frase + long_prev + long_sig + posición + (1 | narrador)`, con su dispersión residual por tipo de frontera. Es un modelo pequeño (una decena de parámetros) que cabe en las ~200-230 fronteras con pausa medible de cada narrador [S: finales de frase y de párrafo más los puntos y coma y dos puntos con silencio]; no hace falta nada más complejo.
- **Uso:** para cada frontera del guion, pausa = exp(predicción + ε), con ε aleatorio de la dispersión residual × 0,7 (un poco menos variable que el humano, para no provocar sobresaltos), recortada entre los percentiles 5 y 95 humanos de ese tipo. Después, **se reescala por acto para que la media coincida con la fórmula de `drafts/formato.md` §3A.3**. Así se mantiene el ritmo percibido objetivo (110-125 palabras/min, Acto III más lento): el modelo **cambia la forma de la distribución, no su media**.
- **Pausas dentro de la frase** (comas): las hace el motor. Se mide su distribución en la voz sintética frente a H1/H2. Si el motor las hace mucho más cortas, se prueba como configuración extra partir las frases largas por punto y coma o dos puntos, pero solo si pasa la comparación ciega, porque partir una frase añade una caída tonal que puede sonar peor [S].
- **Sin fuga de información hacia la prueba ciega:** el modelo que renderiza un segmento S*k* se ajusta con los otros nueve segmentos (**ajuste cruzado dejando un segmento fuera**) y solo aprende parámetros por *tipo* de frontera, nunca la pausa concreta de una frase. Así la IA no puede "copiar" las pausas exactas de la lectura humana con la que se la compara en R1-R3.

**Modelo de entonación de final de párrafo [S].**
- **Qué se mide** en H1/H2, en semitonos respecto a la mediana de F0 del narrador (`librosa.pyin` o Praat vía `parselmouth`): (1) la **caída final**, pendiente de F0 en los últimos 500 ms de la última frase de cada párrafo; (2) el **tono final** relativo a la mediana; (3) la **declinación del párrafo**, mediana de F0 de la primera frase menos la de la última; (4) la bajada de energía en la última frase (dB). Las frases que no cierran párrafo se miden aparte: su caída es más suave (tono de continuación).
- **Uso, en este orden de preferencia:**
  1. **Selección:** en la última frase de cada párrafo, la puntuación de 5B.1 premia la variante cuya caída cae entre los percentiles 10 y 90 humanos (normalizado en semitonos, así que vale para voces de ambos géneros).
  2. **Referencia de estilo de cierre (solo StyleTTS2):** además de REF-CALMA (`drafts/formato.md` §3A.2) se elige una **REF-PECHE**, una frase del corpus de la misma voz con caída final amplia y lenta. Se usa como referencia (mezclada con `beta`) solo en las frases que cierran párrafo.
  3. **Corrección de señal, último recurso:** si ninguna de las N variantes entra en rango, se ajusta la F0 del último segundo con PSOLA (Praat/`parselmouth`), **como máximo 2 semitonos**. El resultado pasa otra vez por el detector de artefactos de §9.5; si lo marca, se descarta y se regenera.
- **Control de deriva a lo largo del episodio:** la mediana de F0 y la declinación por párrafo se registran en el informe; si se desvían más de 1,5 semitonos de la media del capítulo, se marca la frase como dudosa (V5).

**Validación en la misma prueba ciega (prerregistrada en `preregistro_voz.md`).** El modelo se ajusta en la semana 2, en cuanto llegan H1/H2, **antes** de generar el kit (§10).
- **R1, pantalla 2** (P1, 3 min; §7.5): para el mejor motor de Nós y para el mejor de pago, el kit incluye **dos versiones idénticas salvo en las pausas y la caída final**: **"F" = pausas fijas** de `drafts/formato.md` §3A.3 y selección sin criterio de entonación; **"M" = modelo de pausas y entonación**. Mismo texto, mismas variantes elegidas en todo lo demás, misma duración total (± 3 %) y códigos distintos.
- **R2:** 6 pares A/B adicionales "F contra M" de la finalista, con la pregunta "¿Cal soa máis a unha persoa contando?" y el orden alternado.
- **R3, MUSHRA ligero:** se añade la versión que perdió en R1-R2 como un estímulo más (7 en total). Con 20-24 oyentes da una comparación con potencia razonable (Wilcoxon por pares sobre oyentes) [S].
- **Regla de decisión (fijada antes):** se adopta **M** salvo que pierda de forma clara: media de los jueces en B o en C ≥ 5 puntos peor que F en R1, **o** F gana ≥ 5/6 pares en los dos jueces en R2. La versión elegida es la que pasa a la identificación de R3. Si en el MUSHRA de R3 la otra versión resulta mejor en B o C con p < 0,05, se cambia **para R4 y para la producción**, sin repetir R3. Si hay empate, se queda M (es la que se parece por construcción a la cadencia humana) [S].

### 5B.3 Escucha de corrección en cada episodio, con revisores calibrados (rehecha en la v5)

**Qué es un defecto.** Cualquier cosa que un oyente nativo notaría: palabra mal pronunciada, vocal abierta o cerrada errónea, *glitch*, omisión o repetición, pausa extraña, cambio de timbre, clic o artefacto. Hay dos clases:
- **Grave:** cambia el significado o suena claramente a castellano o a portugués (la misma definición que el "erro grave" de §7.3), una omisión, o un clic o artefacto fuerte que despertaría a alguien.
- **Leve:** todo lo demás, incluidas las pausas raras y los artefactos débiles.

Se mide por **bloques de 2 minutos**: un bloque es "defectuoso" si tiene al menos un defecto que **se escapó a la QA automática** (§9). Cada hallazgo se registra en `defectos.csv` (episodio, minuto, clase, tipo, causa y **quién lo encontró**). Ese registro alimenta `lexico_tts.tsv`, los pesos de 5B.1 y la medición de sensibilidad (5B.3.5).

**El problema que corrige la v5.** Una escucha solo garantiza algo si se conoce la **sensibilidad** de quien escucha (*d*: la probabilidad de detectar un defecto que oye). Con una escucha completa, lo que se publica no es "cero defectos" sino **N·p·(1 − d)**: con *d* = 0,7 y un 5 % de bloques defectuosos en un episodio de 75 min, salen publicados ~0,6 bloques defectuosos por episodio, y con un 10 %, ~1,1 [CALC `sim/muestreo_deteccion.py`]. El promotor y su mujer son nativos exigentes, pero no correctores de locución, y nadie ha medido su *d*. La v5 lo mide antes de empezar, lo contrasta con un profesional y lo vigila después.

#### 5B.3.1 Prueba de defectos sembrados (antes del episodio 1 y cada trimestre) [S salvo cálculo]

**Cuándo:** después de la Puerta V (ya hay voz elegida) y antes de producir el episodio 1. Es un requisito para empezar la Etapa 1, igual que la Puerta V.

**Material.** `siembra_defectos.py` (Claude Code) genera **dos episodios de prueba, E_A y E_B, de ~45 min cada uno**, con la voz y la cadena reales, a partir de capítulos del guion piloto que ningún revisor haya oído. En cada uno inyecta **36 defectos conocidos: 16 graves y 20 leves**:

| Clase | Tipo | N.º por episodio | Cómo se genera |
|---|---|---|---|
| Grave | Vocal abierta o cerrada cambiada en palabras de uso alto o en pares con tilde diacrítica (*é/e*, *fóra/fora*, *bóla/bola*, *pé*, *home*, *festa*) | 4 | Entrada fonética forzada al G2P o reescritura de la entrada del TTS; la pronunciación correcta se fija con el Dicionario de pronuncia (https://ilg.usc.es/pronuncia/) y la revisa el profesional (5B.3.2) |
| Grave | Metafonía perdida (*ovos*, *porcos*, *novos* con la *o* cerrada del singular) | 3 | Ídem |
| Grave | Acento de topónimo o de nombre desplazado (*Mondoñedo*, *Xelmírez*, *Ribadavia*, *Hermerico*) | 4 | Reescritura con la tilde en otra sílaba |
| Grave | Consonante castellanizada (*x* leída como jota: *Xinzo*, *Xoán*) | 2 | Reescritura forzada |
| Grave | Palabra omitida que cambia el sentido (p. ej. *non*) | 2 | Se borra del audio con un corte limpio |
| Grave | Clic fuerte (pico > −20 dBFS en una unión) | 1 | Discontinuidad de muestra inyectada |
| Leve | Pausa alargada **+150-300 ms** en un sitio donde no tocaba | 6 | El ensamblador cambia la duración del silencio |
| Leve | Pausa acortada **−150-300 ms** | 6 | Ídem |
| Leve | Clic débil (−45 a −35 dBFS) | 3 | Ídem que el clic fuerte, atenuado |
| Leve | Artefacto de vocoder breve (100-200 ms de zumbido metálico o "fase") | 3 | Se injertan fragmentos de variantes que el detector de §9.5 descartó |
| Leve | Acento de frase raro (+3 semitonos en una palabra átona) | 2 | PSOLA (`parselmouth`) |

- **Colocación:** posiciones al azar, estratificadas por tercios del episodio y separadas ≥ 45 s. La clave (minuto, tipo y clase) se guarda cifrada con hash sellado. **Nadie la oye antes**: la genera el script y el promotor no escucha E_A ni E_B mientras los monta. A los revisores se les dice que "pode haber entre 0 e 60 defectos".
- **Densidad:** ~0,8 defectos/min, muy por encima de la real. Eso mantiene alerta al revisor y **sobreestima *d***. Por eso se complementa con la medida sobre defectos reales (5B.3.5), y en la repetición trimestral la densidad baja a ~0,4/min.

**Procedimiento.** Diseño cruzado para separar el efecto de la velocidad del efecto del episodio: el revisor 1 escucha E_A a 1,25× y E_B a 1×, y el revisor 2 al revés. Son días distintos, con el mismo equipo y el mismo reproductor de `qa_voz.html` que en producción y con las mismas reglas (pausa cada 30 min; 10 min en el altavoz del móvil). El **revisor profesional** (5B.3.2) escucha uno de los dos a 1×.
- **Acierto:** una marca a ±5 s de un defecto sembrado, con el tipo bien descrito ("vogal", "pausa", "clic", "acento"…). Las marcas sin defecto sembrado detrás se contrastan con el profesional. Si él confirma un defecto natural, pasa a la verdad de referencia; si no, cuenta como **falsa alarma** (se registra; > 10 por episodio indica un revisor que marca "por si acaso" y su *d* está inflada).
- **Resultado:** sensibilidad por revisor, velocidad y clase, con IC del 90 % (Clopper-Pearson).

**Umbral de validez (prerregistrado en `preregistro_voz.md`):**

| Resultado a una velocidad | Consecuencia |
|---|---|
| **Graves ≥ 90 % (≥ 15/16) y leves ≥ 70 % (≥ 14/20)** | Validado **a esa velocidad**: puede firmar solo la escucha de un episodio |
| Solo validado a 1× | Trabaja a 1× (75 min → 1,25-1,6 h por episodio; +0,25-0,3 h frente a 1,25×) |
| A 1 acierto del umbral en una clase (14/16 o 13/20) | Repite con un tercer episodio sembrado (E_C) a esa velocidad y se juzga el acumulado (graves ≥ 29/32, leves ≥ 28/40) |
| No validado a ninguna velocidad | **No firma solo.** Opciones: (i) escucha en pareja (los dos revisores de la casa, cada uno el episodio entero por su cuenta; se juntan las marcas: con 0,7 y 0,7 independientes, *d* ≈ 0,91, y en la práctica algo menos porque los defectos difíciles lo son para los dos); (ii) el profesional hace la escucha completa (coste de 5B.3.2 en cada episodio → la Etapa 1 baja a 1 episodio al mes); (iii) formación: 2 sesiones con el profesional sobre sus hallazgos y se repite la prueba |
| El profesional no llega al umbral a 1× | Se cambia de profesional. Su papel es ser la referencia |

**Qué discrimina la prueba (honestidad estadística) [CALC].** Con 16 graves y el umbral en 15, un revisor cuya sensibilidad real es 0,95 pasa el 81 % de las veces; uno de 0,90, el 51 %; uno de 0,80, el 14 %; y uno de 0,70, el 3 %. En leves, con 20 y el umbral en 14: 0,80 pasa el 91 %, 0,70 el 61 % y 0,60 el 25 %. **La prueba es exigente en graves** (en la práctica pide ~0,93-0,95 real, y a un revisor real de 0,90 lo manda la mitad de las veces a repetir) **y permisiva en leves** (un revisor de 0,60 pasa uno de cada cuatro intentos). Es deliberado: el error grave es el que la comunidad no perdona (V1). La laxitud en leves se compensa con la vigilancia sobre defectos reales (5B.3.5) y con el profesional en el muestreo.

**Tiempo:** ~2 h de preparación (Claude Code; una vez) y ~2 h por revisor de la casa (2 × 45 min más la puesta en común). El profesional, ~1 h.

**Repetición trimestral (vigila la fatiga, V16).** Cada 3 meses se hace un episodio sembrado nuevo de ~30 min con 12 defectos (5 graves y 7 leves; densidad ~0,4/min), a la velocidad de trabajo de cada revisor, sin avisar de qué día se incluye en la cola normal si se puede [S]. **Alarma:** una caída de ≥ 15 puntos frente a su prueba inicial, o fallar un grave. La alarma obliga a (1) bajar a 1× o pasar a escucha en pareja, (2) repetir con un E_C completo (16 + 20) y (3) recalcular el plan de 5B.3.4 con el nuevo *d*. Son 12 defectos, así que la trimestral es una alarma y no una medición precisa. La medición continua la da 5B.3.5.

#### 5B.3.2 Revisor lingüístico profesional de referencia (pagado)

**Perfil:** corrector o asesor lingüístico de galego con experiencia en **locución, doblaje o audiolibro** (en la dobraxe galega es la figura que revisa la pronunciación en sala), nativo, **que no sea uno de los narradores H1-H3** (su oído ya está "contaminado" por su propia lectura) y que no participe en el panel R3.
- **Dónde buscarlo:** el buscador de profesionales de la AGPTI [F: el directorio existe; la web no publica tarifas] https://www.agpti.org/ ; estudios de dobraxe galegos; y correctores de audiolibros en galego ya publicados. Hay que contar con la postura del sector sobre la IA (V6): se le ofrece crédito nominal ("Revisión lingüística da locución: …") y el encargo se presenta como lo que es, **un control humano de calidad sobre una voz sintética**.
- **Qué hace:**
  1. Revisa la lista de defectos sembrados (0,5 h) y hace la prueba sembrada a 1× (~1 h).
  2. **Escucha completa a 1× de los episodios 1-6**, en paralelo con la escucha de la casa y **sin ver las marcas de la casa**. Sus hallazgos más los de la casa, confirmados por él, forman la **verdad de referencia** de cada episodio.
  3. En la **Etapa 2, cada muestreo**: sus 20 bloques de cada episodio (5B.3.4).
  4. En la Etapa 1, después del episodio 6: **una cata de 20 bloques uno de cada 4 episodios**, para seguir midiendo a la casa (5B.3.5).
  5. Una sesión de 1 h de puesta en común con la casa después de los episodios 3 y 6, para que el oído de la casa aprenda de sus hallazgos.
- **Tarifa: [?], no verificada con una fuente gallega.** Se intentó y no se encontró una tarifa pública de corrección de locución o de asesoría lingüística de dobraxe en galego: la AGPTI no publica tarifas y las agencias de locución consultadas solo dan presupuesto a petición. En esta versión no se pudo consultar el convenio de dobraxe de Galicia, que podría fijar tarifas de referencia (**tarea pendiente para la semana 1**). **Ancla más cercana [F-sec]:** corrección de textos en castellano, "tarifa media de 0,015 EUR por palabra + IVA" y "10 000 palabras: 7-10 h" https://correccionencastellano.com/tarifas-correccion-textos/ , que implica **~15-21 €/h** [CALC: 150 € ÷ 7-10 h]. **Supuesto de planificación [S]: 20-35 €/h**, por encima del ancla por la especialidad (oído fonético y galego) y por ser encargos pequeños. **Prueba de estrés:** a 50 €/h, el paquete de la Etapa 1 pasa a ~625-715 € (12,5-14,3 h) y el muestreo de la Etapa 2 a ~120 €/mes con 3 episodios (160 € con 4), lo que obliga a bajar la Etapa 2 a 3 episodios al mes o a pasar a 15 bloques del profesional + 25 de la casa (hay que rehacer la tabla de 5B.3.4).
- **Cómo se cierra la tarifa:** 3 presupuestos por escrito en la semana 1 (a la vez que el casting), por hora escuchada o por episodio, con el entregable definido: `defectos.csv` con minuto, clase y propuesta de corrección.
- **Coste Etapa 1 [CALC sobre S]:** episodio de 75 min a 1× con paradas ≈ 1,5-1,8 h × 20-35 €/h = 30-63 € por episodio → **180-380 € por los episodios 1-6**, + prueba sembrada y revisión de la lista (~1,5 h: 30-53 €), + 2 puestas en común de 1 h (40-70 €) → **~250-500 € en total** [CALC: 12,5-14,3 h × 20-35 €/h], dentro de la excepción única (Q1). Las catas posteriores (uno de cada 4 episodios, ~0,8 h) salen a **~8-14 €/mes** y caben en el margen de la Etapa 1 [S].

#### 5B.3.3 Etapa 1: escucha completa de cada episodio

- **Quién firma:** un revisor de la casa **validado** (5B.3.1) a la velocidad a la que escucha, que no sea el que dirigió las frases dudosas (en la práctica se alternan). En los **episodios 1-6** escucha además el profesional, por separado. Si ningún revisor de la casa está validado: escucha en pareja o el profesional (5B.3.1).
- **Cómo:** el episodio completo a la velocidad validada (1,25× con el tono preservado, WSOLA; o 1×) y los tramos marcados siempre a 1×. **1,5× solo para una segunda escucha**, que no cuenta para la firma. 10 min en el altavoz del móvil. Cada defecto se marca con el minuto en `qa_voz.html`, se corrige (otra variante, léxico o regenerar) y **se vuelve a escuchar a 1× el punto corregido y los 30 s de alrededor**, porque una regeneración puede meter un defecto nuevo.
- **Tiempo de la casa [CALC sobre S]:** 1,0-1,3 h por episodio a 1,25× y 1,25-1,6 h a 1×, **2-3,2 h al mes** con 2 episodios. Sustituye a las "3 catas aleatorias" de la v3 (§9.6) y a los "10 primeros minutos" de la puerta humana H3 de `drafts/pipeline.md` (no confundir con el narrador H3), que suman ~0,3-0,5 h. **Neto: +0,7-1,3 h por episodio.**
- **Qué se publica en la práctica:** con un revisor validado (*d* de leves ≥ 0,7 medido), un episodio de 75 min con un 5 % de bloques defectuosos a la entrada deja **≤ 0,6 bloques defectuosos leves** y, en graves (*d* ≥ 0,9, *p* ≈ 1 % [S]), **≤ 0,04** [CALC: 38·p·(1 − d)]. En los episodios 1-6, con la casa y el profesional juntos (*d* combinada ~0,9-0,97), queda en ~0,1-0,2.
- **Condición para dejar la doble escucha tras el episodio 6:** en los episodios 4-6, la estimación de defectos que se le escaparon a la casa (N̂ de captura-recaptura menos lo que encontró la casa; 5B.3.5) es **≤ 1 bloque por episodio y 0 graves**. Si no se cumple, el profesional sigue en los episodios 7-8 y se repite la comprobación.

#### 5B.3.4 Etapa 2: muestreo de aceptación con sensibilidad medida [CALC] `sim/muestreo_deteccion.py`

**Corrección del cálculo de la v4.** El AOQL de 0,48 bloques con n = 20 multiplicaba **dos veces** por (N − n)/N. Con detección perfecta, lo que sale publicado de media con un plan c = 0 es P(aceptar)·p·(N − n), que alcanza un máximo de **0,72** bloques por episodio de 2 h (con *p* ≈ 5 %), no 0,48. Y con revisores reales la cifra empeora, porque (a) un bloque defectuoso de la muestra que el revisor no oye hace aceptar el episodio y (b) la escucha completa tras un rechazo tampoco lo encuentra todo. **El AOQ ya no tiene techo**: si *p* crece, la escucha completa deja pasar N·p·(1 − d). Por eso el plan solo vale dentro de un rango de *p*, que vigilan las reglas de cambio.

**Modelo:** episodio de 2 h = 60 bloques; cada bloque defectuoso con probabilidad *p*; *d*_pro y *d*_casa son la sensibilidad en la muestra; *d*_f es la de la escucha completa de la casa tras un rechazo.

| Plan (bloques de 2 min por episodio) | Sensibilidades | *p* = 1 % | *p* = 2 % | *p* = 3 % | *p* = 5 % |
|---|---|---|---|---|---|
| v4: 20 del profesional, detección perfecta | 1 / — / 1 | 0,33 | 0,53 | 0,65 | 0,72 |
| v4 con revisores reales: 20 | 0,9 / — / 0,7 | 0,37 | 0,66 | 0,89 | 1,22 |
| ídem, peor caso | 0,8 / — / 0,7 | 0,39 | 0,71 | 0,97 | 1,34 |
| **v5: 20 del profesional + 20 de la casa** | **0,9 / 0,7 / 0,7** | **0,23** | **0,37** | **0,48** | 0,61 |
| ídem, peor caso | 0,8 / 0,7 / 0,7 | 0,25 | 0,41 | 0,53 | 0,68 |
| ídem, casa buena | 0,9 / 0,8 / 0,8 | 0,20 | 0,31 | 0,38 | 0,44 |
| alternativa: 30 del profesional | 0,9 / — / 0,7 | 0,28 | 0,47 | 0,60 | 0,79 |

*(Celdas = bloques defectuosos que salen publicados por episodio de 2 h, de media. Probabilidad de aceptar sin escucha completa con el plan v5 y 0,9/0,7: 0,73 / 0,52 / 0,38 / 0,20.)*

**Plan de la Etapa 2 (v5):**
- **Condición para pasar al muestreo:** en los 4 últimos episodios, la tasa de bloques defectuosos a la entrada de la escucha, estimada con la verdad de referencia (5B.3.5) y no con lo que encontró la casa, es ***p̂* ≤ 3 %**, sin ningún grave escapado, y los dos revisores de la casa siguen validados en la última prueba trimestral.
- **Muestra:** **40 bloques** al azar estratificados por tercios (el primer tercio con 14, porque ahí decide el oyente si se queda; 3 en el altavoz del móvil), más todos los puntos marcados por la QA automática. **20 los escucha el profesional a 1× y los otros 20 un revisor de la casa** a su velocidad validada, sin solaparse. **Criterio c = 0:** si ninguno de los dos encuentra nada, se acepta. **Con un solo defecto, la casa escucha el episodio entero** y lo corrige (inspección rectificadora), y el profesional vuelve a oír los puntos corregidos.
- **Qué garantiza:** con *p* ≤ 3 %, **≤ 0,48-0,53 bloques defectuosos publicados por episodio de 2 h** (1 cada ~2 episodios), con *d*_pro de 0,8-0,9 y *d*_casa de 0,7. Para los graves, con *d* ≥ 0,9 y *p*_grave ≤ 1 % [S], **~0,17 por episodio** (1 cada ~6 episodios de 2 h; 0,26 si *p*_grave llega al 2 %). Queda muy por debajo del umbral de publicación de ≤ 1 molestia cada 10 min (§7.6), pero **no es cero**. Es la cifra honesta de un proceso con oídos humanos, y R4 y los comentarios la contrastan.
- **Reglas de cambio (inspiradas en ISO 2859-1, sin aplicarla al pie de la letra) [S]:** se vuelve a la escucha completa si se rechazan 2 de los últimos 5 episodios, **si *p̂* pasa del 3 %**, si un revisor de la casa pierde la validación trimestral o si se escapa un grave que después encuentra el público o el profesional. Se vuelve al muestreo tras 4 episodios limpios. Los episodios "insignia" (estreno de temporada, compilaciones y el que se usa en una convocatoria) se escuchan siempre enteros, **y en ellos también el profesional**.
- **Tiempo esperado por episodio de 2 h (casa) [CALC]:** 20 bloques (~0,5 h) + escucha completa cuando se rechaza (1,6-2,0 h × P(rechazo)) = **~1,0 h si *p* = 1 %; ~1,4 h si *p* = 2 %; ~1,6 h si *p* = 3 %** (rechazo en el 27 %, 48 % y 62 % de los episodios), frente a 2,0-2,6 h de la escucha completa.
- **Coste del profesional:** 20 bloques a 1× ≈ 0,8 h con marcas × 20-35 €/h = **16-28 € por episodio → 48-84 €/mes con 3 episodios, 64-112 €/mes con 4** [S]. Con los ~95-130 €/mes de `drafts/pipeline.md` §4.2 quedan 143-242 €/mes: **cabe en el techo de 200 €/mes con 3 episodios, o con 4 si la tarifa real queda en la mitad baja**. Si no cabe, se baja a 3 episodios, que es preferible a recortar la muestra del profesional.

#### 5B.3.5 Vigilancia continua de la sensibilidad con defectos reales (captura-recaptura)

Cuando dos revisores escuchan lo mismo por separado (la casa y el profesional en los episodios 1-6, en las catas de la Etapa 1 y, en la Etapa 2, cuando el profesional repite a ciegas 5 de los 20 bloques de la casa en uno de cada 4 episodios), se cuentan *n*₁ (hallazgos de la casa), *n*₂ (del profesional) y *m* (de los dos). Entonces:
- **sensibilidad de la casa ≈ m / n₂**, y la del profesional ≈ m / n₁;
- **total de defectos ≈ (n₁ + 1)(n₂ + 1)/(m + 1) − 1** (estimador de Chapman), del que sale *p̂* para las reglas de 5B.3.4.

**Limitación [S]:** el estimador supone que los dos revisores detectan de forma independiente y que todos los defectos son igual de fáciles de encontrar. No es así: lo difícil lo es para los dos, así que **subestima el total**. Por eso no sustituye a la prueba sembrada: la complementa con defectos reales y con la densidad real. Se lleva en `sensibilidad.csv`, **se acumula por trimestre** (un solo episodio da muy pocos datos), y si la sensibilidad de la casa sobre defectos reales queda **≥ 15 puntos por debajo** de la de la prueba sembrada, manda la cifra real: se recalculan 5B.3.3 y 5B.3.4 con ella.

**Integración en las horas de las etapas [CALC sobre `drafts/pipeline.md` §6]:**

| | Etapa 1 (2 × 75 min/mes) | Etapa 2 (3-4 × 2 h/mes) |
|---|---|---|
| Pase de dirección (5B.1 d) | 0,25-0,6 h/episodio → 0,5-1,2 h/mes | 0,4-0,9 h/episodio → 1,2-3,6 h/mes |
| Escucha de corrección (5B.3) | 1,0-1,6 h/episodio (neto +0,7-1,3) → +1,4-2,6 h/mes | 20 bloques + rechazos: ~1,0-1,7 h/episodio de la casa → 3-6,8 h/mes |
| Prueba sembrada | ~2 h por revisor una vez (antes del episodio 1) + ~0,6 h por trimestre (≈ 0,2 h/mes) | ≈ 0,2 h/mes |
| **Total añadido al presupuesto de horas de `pipeline.md`** | **+2,1-4,0 h/mes** → de ~11-13 h a **~13-17 h/mes (3,0-3,9 h/semana)**: cabe en 4 h/semana, pero sin holgura. **Si un revisor solo está validado a 1×, la escucha pasa a la mujer del promotor o se publica 1 episodio ese mes** | **+4,4-10,6 h/mes de la casa** → ~24-39 h/mes (5,6-9 h/semana): cabe en 6-10 h/semana con 3 episodios; con 4, solo en el extremo alto |
| Coste añadido | Paquete del profesional de ~250-500 € (una vez, Q1) + catas de ~8-14 €/mes | 48-112 €/mes de profesional + ~1-3 USD/mes de GPU por N = 4 |

### 5B.4 Vía intermedia financiable antes del plan B: *fine-tune* de StyleTTS2-GL con licencia de H1 o H2

**Por qué hace falta.** El escenario central (60-80 %, §0 punto 13) es que ninguna voz sintética pase la Puerta V. Hasta la v3 las únicas salidas eran "esperar" o el plan B de 1.000-2.500 € (licencia y clonación), que rompe el presupuesto de la Etapa 1. Falta un paso intermedio que aproveche lo ya pagado: **H1 y H2 son narradores galegos profesionales ya contratados, ya grabados en estilo "durmir" y ya medidos contra el listón.** Ajustar el modelo de Nós a uno de ellos ataca la causa más probable del suspenso: la prosodia y el timbre de un corpus leído en estilo neutro, a 16 kHz.

**Qué se hace [S salvo cita].**
1. **Grabación "corpus durmir":** el narrador elegido (H1 si la mejor base es Brais y H2 si es Celtia, para ajustar de hombre a hombre y de mujer a mujer) graba **30-60 min adicionales** con el mismo *brief* y el mismo formato (48 kHz / 24 bits). **Son textos distintos de S1-S10 y del texto trampa:** otros capítulos del guion y un bloque fonéticamente rico. **S1-S10 y el texto trampa nunca entran en el entrenamiento**: son el conjunto de prueba, y si entrasen el clon "se sabría" las frases de la prueba ciega.
2. ***Fine-tune*** del StyleTTS2 de Nós con ese material. El repositorio de Nós publica el código y la configuración de entrenamiento, el G2P Cotovía y el PL-ModernBERT-gl [F] https://huggingface.co/proxectonos/Nos_StyleTTS2-Brais-GL . La referencia pública es el *fine-tune* oficial de StyleTTS2, que usa **1 hora de audio (~1.000 frases)** y tarda **~4 h en 4 A100** [F] https://github.com/yl4579/StyleTTS2 . Se remuestrea a 24 kHz (la frecuencia de trabajo del modelo): de paso, **puede recuperar parte del ancho de banda** que el corpus de Nós a 16 kHz no tiene [?, V11].
3. **Evaluación con la misma Puerta V (R1 → R3)**, con dos cambios obligatorios. (a) El narrador de origen **no aparece como humano** en ninguna prueba del clon: en la identificación se usan los otros dos humanos, así que **H3 pasa a ser obligatorio** en esta vía; en el MUSHRA, la referencia marcada y el control positivo son los otros narradores. (b) Se prueba con 5B.1 y 5B.2 igual que el resto.

**Coste y financiación [CALC sobre F y S].**

| Concepto | Cuándo se paga | Coste |
|---|---|---|
| **Opción de entrenamiento** firmada en el contrato de referencia de H1 y H2 (§7.2): precio de la grabación extra y de la cesión, fijado ya, pero **solo se ejecuta si el promotor la activa en los 6 meses siguientes** | Al firmar (prima de la opción) | 0-50 € por narrador [S] |
| **T1: grabación del corpus durmir + cesión para entrenar** (uso interno de evaluación; sin publicar) | Solo si se activa la vía; un solo narrador | **30 min por defecto** (~3.450 palabras) × 0,08-0,135 €/palabra (tarifa de planificación de §3) ≈ 275-465 € [CALC], + un 20-40 % de prima por la cesión para IA [S] → **~330-650 €**. Otros 30 min con el mismo precio, **solo si** el primer *fine-tune* queda "cerca" (Δ ≤ 15 en B y C en R1) |
| GPU para el *fine-tune* | Al activar | 16 GPU-h de A100 por ejecución × 1,19-1,59 USD/h ≈ 19-25 USD; con 3-4 ejecuciones de ajuste, **~60-100 USD** [CALC con https://www.runpod.io/pricing y la referencia de 4 h × 4 A100] |
| H3 (obligatorio en esta vía) | Si no se contrató antes | 300-500 € (§3, §7.2) |
| Horas del promotor con Claude Code | Al activar | 10-20 h (preparar datos, entrenar, evaluar) [S] |
| **Subtotal hasta saber si funciona** | | **~700-1.250 €** (v5, con las tarifas revisadas; 500-1.100 € en la v4), frente a 1.000-2.500 € del plan B |
| **T2: licencia de publicación** (solo si el clon **pasa** la Puerta V-2) | Al publicar | Prefijada en el mismo contrato: 12-24 meses, un canal de YouTube en galego, revisión de muestras por el narrador, crédito ("voz de X, con licenza") y borrado del modelo al terminar. **300-600 € fijos + 10-15 % de los ingresos netos del canal** durante la licencia [S]. El fijo se puede pagar en 6 cuotas mensuales de 50-100 € |

**Honestidad sobre las cifras.** La referencia de mercado de la UVA para "demos de voz sintética" es de 1.000-1.500 € [F-sec, §3]. **Lo que se propone está por debajo**, y se justifica porque (i) el narrador ya está contratado y grabado, (ii) la cesión es limitada (un canal, un idioma, 12-24 meses) y (iii) cobra un porcentaje si el canal funciona. **Es posible que muchos narradores lo rechacen**, sobre todo con la postura del sector (V6). Por eso **la opción se negocia en el casting de la semana 1** y la aceptación de la opción es un criterio para elegir H1 y H2 cuando la calidad empata (§7.2). Si ninguno la acepta, esta vía desaparece y quedan "esperar" o el plan B.

**Por qué se espera que ayude y por qué puede fallar [S].** Ayuda porque ataca tres causas probables del suspenso a la vez: la prosodia del estilo "durmir" (el corpus de Nós es lectura neutra de frases sueltas), el timbre (un narrador elegido por su voz para este género) y el ancho de banda. Puede fallar porque 30-60 min es el mínimo de la literatura, porque el ajuste se hace desde un modelo de un solo locutor y no desde uno multilocutor como en la receta oficial, y porque la estabilidad en tiradas de 1-2 h queda por probar. **Estimación: 30-50 % de probabilidad de pasar la Puerta V** [S; sin datos, se revisa tras la primera ejecución]. En paralelo, y con el mismo material, se puede probar un ElevenLabs PVC: su mínimo recomendado es 30 min ("ideally as close to three hours as possible") y **exige que el propio narrador verifique su voz** [F] https://elevenlabs.io/docs/product-guides/voices/voice-cloning/professional-voice-cloning . Eso obliga a que la cuenta o la verificación sean del narrador y hay que preverlo en el contrato.

---

## 6. Riesgos de la voz y mitigaciones

| # | Riesgo | Probabilidad [S] | Impacto | Mitigación |
|---|---|---|---|---|
| V1 | **Acento castellanizado** (vocales é/è y ó/ò neutralizadas, metafonía perdida en *ovo/ovos*) o **aportuguesado** (grafías leídas "a la portuguesa") | Alta en motores globales (E, F); baja en Nós | Alto: comentarios de "isto non é galego" | Texto trampa (§7.3), escala A, prioridad a Nós y filólogo en el panel (R3) |
| V2 | **Topónimos y nombres mal acentuados** (Mondoñedo, Xelmírez, Hermerico) | Media en todos | Medio-alto | `lexico_tts.tsv`, lista crítica en el ASR (§9) y escucha dirigida |
| V3 | **Prosodia de telediario**: correcta pero no adormece | Alta en Azure y en VITS | Alto (retención) | Escala C, distancia a la referencia humana y prueba de sueño real |
| V4 | ***Glitches*, omisiones o repeticiones** en tiradas largas | Media (ElevenLabs y Gemini con textos largos; StyleTTS2 sin probar) [S] | Alto: despierta al oyente y delata "IA barata" | Síntesis por párrafos, doble ASR y detector de anomalías (§9) |
| V5 | **Deriva** de timbre o estilo entre párrafos | Media en modelos con difusión y en los de prompt | Medio | `t` de StyleTTS2, semilla fija, referencia de estilo fija y control de la variación de tono por párrafo [S] |
| V6 | **Rechazo social**: dobladores (ADA), AGPTI y A Mesa denuncian el doblaje con IA al galego ("máis como freo ca como impulso para a lingua") [F] https://www.nosdiario.gal/articulo/social/mesa-agpti-ada-denuncian-incumprimentos-rtve-coa-programacion-galego/20260220110723248001.html | Media | Medio-alto (prensa, comentarios, convocatorias) | Transparencia total, crédito a Nós, nunca clonar sin consentimiento, grabación de referencia contratada **sin** cesión para IA salvo opción firmada aparte y remunerada (T1/T2, §4), y en la vía intermedia, en el plan B o en la Etapa 3, voz licenciada, remunerada y acreditada ("voz dun narrador galego, con licenza") |
| V7 | **Licencia Nós no confirmada** o denegada | Media (los términos del *dataset* dicen "solely for research purposes") | Alto si se publicase sin permiso; medio con la regla de la v5 (retrasa o cambia la voz, pero no hay que retirarla con el canal en marcha) | Correo en la semana 0; **solo se publica con la confirmación escrita** (el silencio no cuenta); mientras tanto, voz de pago aprobada o esperar (§4, §8.1); voz de reserva ya validada que no sea de Nós |
| V8 | **Cambio o retirada del proveedor** (Preview de Gemini, voces de la Voice Library, precios) | Media | Medio | Guardar la versión del modelo, preferir modelos abiertos y reservar una segunda voz aprobada |
| V9 | **Sesgo de los jueces** (el promotor construye el kit; ambos ya conocen a Sabela) | Alta | Medio (decisión errónea) | Kit con aleatorización automática, claves selladas en dos fases, prerregistro sellado, señuelos y panel ampliado de 20-24 personas (§7.1, §7.2) |
| V10 | **Cambiar de voz con el canal crecido** confunde a la audiencia | Baja si se sigue §8 | Medio | Bloquear la voz ≥ 10 vídeos; cambiarla solo en la Etapa 3, con anuncio |
| V11 | **Ancho de banda limitado de Nós** (corpus a 16 kHz) delata a la voz frente a una referencia a 48 kHz | Media | Medio (puede tumbar la identificación) | Cadena final común con caída > 9-10 kHz; configuración con extensión de ancho de banda (§5.3); juzgar en dispositivos reales |
| V13 | **Falso suspenso por fallo del test**: el listón mide el parecido a una lectura concreta, o los oyentes resuelven la identificación distinguiendo timbres y no por naturalidad, y se paga el plan B sin necesidad | Media en el diseño v2; baja en el v3 [S] | Alto (1.000-2.500 € mal gastados) | Control positivo humano oculto que tiene que pasar la puerta; control negativo; referencia rotatoria; 5 voces × 2 fragmentos; análisis por oyente; recalibración y apertura de la clave en dos fases (§7.6-7.7) |
| V12 | **Ninguna voz pasa el listón** y el proyecto se retrasa | **Alta (60-80 %)** [S] | Alto (calendario y presupuesto) | Método de producción de §5B (sube la probabilidad de aprobar sin coste de licencia); árbol de decisión explícito (§8.1): vía intermedia de *fine-tune* con opción ya firmada (§5B.4), plan B o esperar; reevaluación trimestral de modelos nuevos |
| V14 | **El selector automático elige mal** (UTMOS y DNSMOS no están validados en galego ni en voz "de durmir") o premia siempre lo mismo y aplana la voz | Media | Medio | Filtros eliminatorios antes de puntuar; pesos calibrados contra un nativo (≥ 50 % de acierto, 0 elecciones "inaceptables"); pase de dirección en las dudosas; los defectos escapados de §5B.3 reajustan los pesos cada 4 episodios |
| V15 | **El *fine-tune* no mejora o "se sabe" la prueba** (sobreajuste, fuga de S1-S10 al entrenamiento) | Media | Alto (se gastan ~700-1.250 € o se aprueba un clon que no generaliza) | S1-S10 y el texto trampa excluidos del entrenamiento; el narrador de origen no aparece como humano en las pruebas del clon; H3 obligatorio; R4 sobre un episodio con texto nuevo |
| V16 | **Fatiga del escuchador**: la escucha completa se vuelve rutina y deja pasar defectos, o se come las horas de la Etapa 1 | Media-alta | Medio | Turnos alternos (promotor/mujer), pausa cada 30 min; **prueba de defectos sembrados trimestral** con alarma si cae ≥ 15 puntos (§5B.3.1); captura-recaptura continua con el profesional (§5B.3.5); paso al muestreo en la Etapa 2 con reglas de vuelta al 100 % |
| V17 | **Revisor no calibrado** (nuevo en la v5): los revisores de la casa son nativos, pero no correctores de locución, y su sensibilidad real es desconocida. Una escucha "completa" con *d* = 0,7 deja salir el 30 % de los defectos | Alta sin medir | Alto: errores de galego publicados (la condición no negociable) | Prueba sembrada antes del episodio 1 con umbral de ≥ 90 % en graves y ≥ 70 % en leves por velocidad; revisor profesional en los episodios 1-6 y en cada muestreo; plan de muestreo calculado con la *d* medida; escucha en pareja o por el profesional si nadie de la casa valida (§5B.3) |
| V18 | **Tarifas sin fuente gallega** (narradores y revisor profesional) (nuevo en la v5) | Media | Medio: la excepción única puede pasar de ~1.500 € | 3 presupuestos por escrito en la semana 1; techos explícitos; variante mínima para los narradores; prueba de estrés del revisor a 50 €/h (§5B.3.2) |

---

## 7. Protocolo de validación a ciegas

### 7.1 Principios

1. **Ciego de verdad:** los jueces no saben qué motor suena. Los ficheros tienen códigos aleatorios y la clave queda sellada.
2. **Mismo texto, mismo tratamiento:** todas las muestras pasan por la misma cadena (EQ, −16 LUFS, 48 kHz), con una duración igual ± 10 %.
3. **Referencia humana oculta y control positivo humano:** hay 2 (o 3) narradores galegos profesionales que leen el mismo texto. En cada pantalla, uno aparece marcado como "referencia" y también escondido entre las muestras (la **referencia oculta**, que solo sirve para el post-cribado y como cero de la escala). **El otro narrador se esconde como una condición más: es el control positivo.** La voz candidata se mide como distancia a la referencia oculta, **igual que el humano de control**, y el listón solo vale si ese humano lo alcanza. Qué narrador hace de referencia **rota** entre pantallas y entre oyentes, de modo que ningún listón depende de una sola lectura.
4. **Anclas y control negativo:** muestras malas a propósito que fijan el fondo de la escala. En la identificación hay además una voz claramente sintética que la prueba **tiene que** detectar: si no la detecta, la prueba no es sensible y su "aprobado" no vale.
5. **Rondas eliminatorias:** la máquina filtra primero (R0) para gastar el tiempo humano solo en lo que merece la pena.
6. **Umbrales, fórmula de recalibración, tamaños de muestra (N de oyentes) y script de análisis fijados de antemano** (§7.6 y §7.7). Se escriben en `preregistro_voz.md` y se sellan (commit en git con fecha + hash SHA-256 enviado por correo a un tercero) antes de abrir ningún audio. No hay análisis intermedios: se recluta hasta el N fijado y solo entonces se analiza.
6b. **Apertura de la clave en dos fases:** en la fase 1 se revelan **solo** los códigos de los humanos y de las anclas. El script comprueba los controles y fija el **umbral efectivo**, que queda sellado en `umbral_efectivo.json` (hash). En la fase 2 se revela qué motor es cada código y se aplica ese umbral sin tocarlo.
7. **Condiciones de escucha reales:** además de los auriculares cerrados del laboratorio, se escucha en el altavoz del móvil y con auriculares de botón a volumen bajo, porque así se consume el producto.

Base metodológica: MUSHRA (ITU-R BS.1534-3, "Multiple Stimuli with Hidden Reference and Anchor"), escala de 0 a 100, referencia oculta y anclas; la regla de post-cribado excluye a los oyentes que puntúan la referencia oculta por debajo de 90 en más del 15 % de los ítems [F] https://en.wikipedia.org/wiki/MUSHRA . MUSHRA necesita menos oyentes que un MOS porque todos oyen todas las muestras a la vez [F] ídem. Herramienta libre para montarlo en el navegador: **webMUSHRA** [F] https://openresearchsoftware.metajnl.com/articles/10.5334/jors.187 . **Adaptación [S]:** MUSHRA está pensado para códecs de audio (una sola dimensión, "calidad"). Aquí se puntúan **tres escalas por separado** y se añaden una prueba de preferencia, una de sueño real y una de **identificación humano/IA**, porque "me duermo con esto" no es lo mismo que "suena bien", y "suena bien" tampoco es lo mismo que "no se distingue de un humano".

### 7.2 Montaje del kit (`kit_voz.py`, construido con Claude Code) y referencias profesionales

**Entradas:** `texto_trampa.txt` (§7.3), `fragmento_largo.txt` (los **primeros ~30 min** del guion piloto de `drafts/guion.md`, "A Revolta Irmandiña", divididos en **10 segmentos de ~3 min, S1-S10**, cortados en finales de párrafo; P1 = S1-S2) y `config_motores.yaml` (motores y ajustes de "voz calma").

**Referencias humanas profesionales (obligatorias; son a la vez patrón y control positivo):**

| Aspecto | Especificación |
|---|---|
| Quiénes | **H1 y H2: dos narradores o locutores profesionales galegos nativos, un hombre y una mujer**, con experiencia en audiolibro o documental, que **no sean jueces** y que el panel no conozca (nada de voces famosas de la TVG). Así, sea cual sea el género de la finalista, hay al menos un humano de su mismo género. **H3 (opcional, recomendado):** un 3.º narrador **del mismo género que la finalista de R2**, contratado solo para R3. Con él, la parte humana del panel tampoco se resuelve por el género. Los candidatos se buscan en directorios de locutores galegos (hay agencias y estudios en A Coruña, Lugo y Pontevedra [F-sec] resultados de búsqueda: https://tragoratraducciones.com/locutores-gallegos/ , https://www.locutortv.es/locutores_gallegos-locutor.htm , https://anyvoz.com/locutores-gallegos/ ), en estudios de doblaje galegos o entre narradores de audiolibros en galego ya publicados. Se eligen por una demo de 1 min del texto trampa (casting gratuito o simbólico). **Criterio de desempate: que acepten las opciones T1/T2** (§5B.4) |
| Qué graba cada uno | Texto trampa (~90 s) + **los mismos ~30 min del guion piloto (S1-S10)**. Todos los narradores graban **todos** los segmentos, de modo que cualquier segmento puede sonar con cualquier voz y el texto no se confunde con la voz |
| Dirección | Todos reciben el mismo *brief* que las voces sintéticas: "narración para durmir", 110-125 palabras/min percibidas, voz baja y cálida, sin interpretación teatral. Pronunciación de los topónimos según el Dicionario de pronuncia. **No se les pone la grabación del otro narrador**, para que las lecturas sean independientes |
| Formato | **WAV a 48 kHz / 24 bits**, mono, cabina tratada; suelo de ruido de la sala **≤ −60 dBFS** (idealmente ≤ −65); sin reducción de ruido ni compresión en la toma; entrega en bruto y editada (sin clics de boca, con respiraciones) |
| Contrato | **T0 (siempre):** uso **solo interno para evaluación**; no se publica, no se usa para entrenar ni clonar, y se borra a los 24 meses. **En el mismo contrato, dos opciones con precio cerrado (§4 y §5B.4):** **T1**, grabación extra de 30-60 min en estilo "durmir" con textos distintos de S1-S10 y cesión para *fine-tune* solo de evaluación, ejercitable en 6 meses; **T2**, licencia de publicación de 12-24 meses (fijo + 10-15 % de ingresos) solo si el modelo pasa la Puerta V-2. El narrador puede firmar T0 y rechazar las opciones. **Además**, un servicio opcional de ~1 h: elegir a ciegas la mejor de 4 variantes en 60 frases para calibrar el selector de §5B.1 (~25-40 € [S]). Se cita a los narradores en `decision_voz.md` |
| Coste | Tabla de tarifas contrastadas en §3 (v5). Resumen: tarifa genérica española de audiolibro, 0,05-0,067 €/palabra (Cronoshare) [F-sec]; precio de lista de una agencia con catálogo de locutores galegos, 450 € por 2.000 palabras con un 20-40 % de descuento, es decir 0,135-0,225 €/palabra (Escena Digital) [F-sec]; ninguna tarifa específica del galego publicada (el "desde 0,29 €/palabra" de la v4 se retira: no se pudo verificar). Para ~3.700 palabras por narrador [CALC: 30 min × ~115 palabras/min = 3.450, + 250 del texto trampa]: 185-250 € (genérica) a 500-830 € + IVA (agencia). **Presupuesto: 300-500 € por narrador** contratado directamente; **600-1.000 € por H1 + H2**; **+300-500 € por H3**; **techo de 1.500 €** [S]. Casting: gratuito o simbólico con autónomos; la agencia cobra "Casting (por locutor): 200 €" [F-sec], así que se evita el casting por agencia. Las opciones T1/T2 se pagan aparte y solo si se ejercen (§5B.4) |
| Valor añadido | Los narradores son los **primeros contactos de casting** para el plan B y la Etapa 3. Son también el **patrón auditivo** de pronunciación y ritmo, y el **rango humano** para calibrar la cadena y el ASR: con dos lecturas se ve cuánto varían dos profesionales entre sí (§9.3) |

**Roles en cada prueba (resumen):**

| Prueba | Referencia marcada | Referencia oculta (misma grabación que la marcada) | Humano de control oculto (control positivo) | Control negativo |
|---|---|---|---|---|
| R1, pantalla 1 (texto trampa) | H1 para un juez y H2 para el otro | La misma que la marcada | El otro narrador | Anclas paso bajo y Google Standard-B |
| R1, pantalla 2 (P1, 3 min) | Se invierte respecto a la pantalla 1 | ídem | ídem | ídem |
| R3, MUSHRA ligero | Rota por oyente (mitad H1 y mitad H2, o un tercio cada uno con H3) | ídem | Otro narrador distinto (del género de la candidata cuando sea posible) | Ancla baja |
| R3, identificación | **No hay referencia** (estímulo único) | — | 2 humanos por oyente, cada uno × 2 fragmentos | Ancla sintética (Azure Sabela sin ajustes o Google Standard-B) × 2 |
**Resto del kit:**
- **Síntesis con el método de producción (§5B):** todas las voces sintéticas se generan con contexto, N = 4 variantes por frase y el selector automático calibrado (`seleccion_v1.yaml`, sellado antes de generar el kit), **sin pase humano** (lo haría un juez), y con el modelo de pausas y entonación (salvo las versiones "F" de la comparación de §5B.2). Cada motor con **2 configuraciones** (p. ej. velocidad normal y lenta). Así hay más muestras que motores, lo que dificulta reconocer a Sabela o adivinar cuál es cuál (**señuelos**).
- **Tratamiento:** la misma cadena de §5.1 y §5.3 para todas, **grabaciones humanas incluidas** (EQ, caída > 9-10 kHz, `loudnorm` a −16 LUFS, 48 kHz / 24 bits) y los metadatos borrados. Las voces sintéticas llevan las pausas insertadas y los humanos conservan las suyas. **Todos los estímulos se igualan en *room tone***: los silencios de todas las pistas se rellenan con el mismo ruido de sala a −68 dBFS. Así el "silencio demasiado limpio" de la IA o el ruido de cabina del humano no delatan a nadie. **Todas las pruebas que deciden (MUSHRA e identificación) se hacen en seco, sin cama sonora (v5).** El listón declarado es el de un audiolibro profesional, que se escucha en seco, y la cama puede enmascarar justo los defectos que delatan a una máquina (artefactos en las eses, uniones, respiraciones). La cama del producto (20-26 dB por debajo; §5.1) solo aparece en un **bloque secundario de identificación** (§7.7), que es informativo, y en la prueba de sueño de R2, que se hace con la mezcla final del producto (voz + cama), porque mide el uso real.
- **Aleatorización y claves en dos fases:** nombres del tipo `M07.wav`, en un orden distinto para cada juez. Hay **dos claves cifradas**. `clave_controles.json` dice qué códigos son humanos (y cuál), cuáles son la referencia oculta y cuáles las anclas. `clave_motores.json` dice qué motor y qué configuración hay detrás de cada código sintético. La contraseña la guarda **la mujer del promotor**. La 1.ª clave se abre cuando se han entregado todas las hojas; la 2.ª, solo cuando el umbral efectivo ya está sellado (§7.1, punto 6b).
- **Anclas:** (1) ancla baja: la referencia marcada con un filtro paso bajo a 3,5 kHz (ancla estándar de MUSHRA [F] https://en.wikipedia.org/wiki/MUSHRA ); (2) ancla media: la referencia con un paso bajo a 7 kHz (BS.1534-3 incluye un ancla media de este tipo [F-sec] ídem); (3) ancla sintética: Google `gl-ES-Standard-B` sin ajustes, como "voz sintética antigua".
- **Sesgo del constructor:** el promotor genera el kit pero **no escucha las salidas** mientras lo monta. Sus puntuaciones y las de su mujer se analizan también por separado: si solo él puntúa alto a Sabela, se sospecha sesgo de reconocimiento.

### 7.3 Texto trampa (~90 s de lectura; galego normativo; revisar por nativos antes de usar)

Pensado para concentrar las dificultades: topónimos, nombres históricos, metafonía y vocales abiertas o cerradas, infinitivo conxugado, formas de *vós*, contracciones, números en letra y una subordinada larga. **Nota [S]:** el promotor, su mujer y los narradores profesionales deben revisarlo antes de la prueba; si algo "non soa", se cambia.

> Naquela noite de inverno, cando a chuvia batía mansamente nas lousas de Mondoñedo, o vello cóengo abriu o libro das memorias. Contaba que no ano mil catrocentos sesenta e sete os irmandiños baixaran das terras de Betanzos e de Xinzo de Limia, e que as torres dos señores caeran unha tras outra, coma follas no outono. Anos despois, o mariscal Pardo de Cela sería degolado diante da catedral, e o seu nome quedaría para sempre na memoria do pobo.
>
> Pero esta noite non imos falar de guerras. Imos camiñar amodo, pé ante pé, polas rúas de Ribadavia e de Compostela, onde o arcebispo Xelmírez soñara, séculos antes, cunha cidade digna dos reis. Imos lembrar a Prisciliano, e aos suevos de Hermerico, que chegaron a esta terra cando Roma xa se apagaba.
>
> Quixera contarche como era a vida fóra das murallas: a festa do San Xoán, o home que volvía do mar coa rede ao lombo, a nai que cocía o pan e apañaba os ovos polo serán, mentres dicía aos fillos: «Vós, deitádevos xa, que mañá hai que madrugar».
>
> Pecha os ollos. Non tes que lembralo todo. Deixa que a voz te leve amodiño, coma a marea que entra na ría de Baiona ao solpor. O camiño é longo, pero temos toda a noite para percorrérmolo xuntos.

**Puntos de control** (el juez tiene la lista a mano en la hoja; un fallo marcado es un "erro"):

| Tipo | Palabras a vigilar |
|---|---|
| Topónimos | Mondoñedo, Betanzos, Xinzo de Limia, Ribadavia, Compostela, Baiona |
| Nombres | Pardo de Cela, Xelmírez, Prisciliano, Hermerico, irmandiños, San Xoán |
| Vocales abiertas y cerradas, y metafonía | *ovos* (ó abierta, frente a *ovo* con o cerrada), *pé*, *festa*, *home*, *fóra* [S: los jueces fijan la pronunciación esperada con el Dicionario de pronuncia, https://ilg.usc.es/pronuncia/ , y con las lecturas de los narradores profesionales; si H1 y H2 difieren en una palabra, se consulta el Dicionario y esa palabra no puntúa como erro] |
| Morfología y sintaxis gallegas | *percorrérmolo* (infinitivo conxugado + clítico), *deitádevos*, *contarche*, *coa*, *polo*, *cunha* |
| Números en letra | "mil catrocentos sesenta e sete" |
| Prosodia | La frase "Contaba que… coma follas no outono" (subordinada larga con enumeración) |

**Clasificación de errores:**
- **Erro grave:** cambia el significado o suena claramente castellano o portugués (p. ej. "Xinzo" leído con /x/ castellana, "Xelmírez" con el acento en otra sílaba, una palabra omitida). **Un solo erro grave elimina la configuración.**
- **Erro leve:** una vocal abierta o cerrada dudosa, un acento de frase raro. Se tolera un máximo de 1 en el texto trampa para aprobar (§7.6).

### 7.4 Ronda 0 (R0): criba automática, sin jueces

Todas las configuraciones (unas 16-20: 8-9 motores o voces × 2 ajustes) pasan el control ASR de §9 sobre el texto trampa y el fragmento largo, además de los controles de señal de §5.3.

- **Se elimina** la configuración con omisiones o repeticiones de más de 3 palabras, con un WER superior al doble del **peor de los dos narradores profesionales**, con algún nombre de la lista crítica que no reconozca ninguno de los dos ASR (§9.3), o con más de 1 anomalía acústica cada 10 min (§9.5).
- **Resultado:** quedan como mucho **8 configuraciones** para R1. Si pasan más, se quedan las 8 de menor WER, con al menos una de Nós y la línea base de Azure dentro.

### 7.5 Rondas humanas

**R1: MUSHRA (promotor y mujer; ~70 min cada uno; por separado, con auriculares cerrados y a volumen fijo)**

- **Pantalla 1 (webMUSHRA), texto trampa completo:** la referencia marcada (H1 para un juez y H2 para el otro), 8 muestras sintéticas, la **referencia oculta** (la misma grabación que la marcada), el **humano de control oculto** (el otro narrador) y 3 anclas. Son 13 estímulos en orden aleatorio. Se puntúan tres escalas de 0 a 100, en pasadas separadas:
  - **A. Corrección galega** ("¿é galego ben pronunciado?"), marcando además los erros en la lista de control.
  - **B. Naturalidade** ("¿soa como unha persoa lendo con xeito?").
  - **C. Durmiríame con isto** ("¿relaxa?, ¿cansa?, ¿molesta algo?").
- **Pantalla 2, 3 minutos de P1 (S1):** las 4 mejores en C, la referencia oculta y el humano de control, **con los papeles de H1 y H2 invertidos** respecto a la pantalla 1. Se vuelven a puntuar B y C. Así cada juez juzga contra las dos lecturas humanas y ningún resultado depende de una sola. **Comparación de pausas (§5B.2):** del mejor motor de Nós y del mejor de pago entran **las dos versiones, "M" (modelo de pausas y entonación) y "F" (pausas fijas)**, con códigos distintos. Son hasta 8 estímulos por pantalla; si hacen falta más, se quitan motores y no versiones.
- **Post-cribado [F adaptado]:** si un juez puntúa la referencia oculta por debajo de 90 en más del 15 % de las pantallas, esa ronda se repite otro día (no se descarta al juez: solo hay dos).
- **Distancias:** para cada voz *v*, escala y juez, **Δ(v) = nota de la referencia oculta − nota de *v***, en la misma pantalla (esto corrige la severidad propia de cada juez). Se calcula igual para el humano de control: **Δ(control)**. Δ(control) indica cuánto "castiga" el test a un profesional por no ser la lectura marcada, y es la base de la recalibración de §7.6.
- **Aviso honesto:** con dos jueces, R1 es una **criba**, no una prueba estadística. Su control positivo solo detecta un test groseramente descalibrado (Δ(control) > 15). La validación con potencia estadística llega en R3.

**R2: finalistas (las 2 mejores de R1 que cumplan los mínimos de §7.6)**

- **Preferencia por pares (A/B forzada):** 6 pares de fragmentos de 60 s (partes distintas de S3-S10), con el orden A/B alternado y con auriculares. "¿Cal preferirías escoitar para durmir?". Se gana con ≥ 5/6 por juez; si no, empate.
- **Pares "F contra M" de la finalista (§5B.2):** otros 6 pares de 60 s, misma mecánica, con la pregunta "¿Cal soa máis a unha persoa contando?". Con esto y con R1 se aplica la regla de decisión de §5B.2 **antes de R3**, que ya usa la versión ganadora.
- **Prueba de sueño real, en dispositivos reales (cruzada):** cada juez escucha en la cama 30 min de la finalista X una noche y de la Y otra noche, en orden contrario al del otro juez. **Cada juez usa el dispositivo con el que dormiría de verdad, y entre los dos cubren las dos condiciones:** (a) el **altavoz del móvil** en la mesilla, a volumen bajo; (b) **auriculares de botón** o una banda de dormir a volumen bajo. Si los dos usan el mismo, se hace una tercera noche con el otro. A la mañana siguiente apunta: ¿se durmió antes del final? (sí/no, y cuándo, aproximadamente); ¿algo le **molestó o despertó**? (anotar el minuto si puede); ¿**notó algo que le recordase que era una máquina**?; una nota de 0 a 10. Además, el detector automático (§9.5) cuenta las anomalías en esos mismos 30 min.
- **Al acabar R2** se conoce el género de la finalista. Si se aprobó el H3 (Q1), se contrata ahora un 3.º narrador **de ese género**, que graba el mismo material (§7.2).

**R3: panel ampliado (ANTES del primer vídeo público; forma parte de la Puerta V)**

- **Tamaño fijado en el prerregistro: N = 20 oyentes válidos como mínimo y 24 como objetivo** (justificación en §7.7). Se recluta hasta llegar a 20 oyentes válidos tras el post-cribado. **No se mira ningún resultado antes de llegar a N** y no se añaden oyentes después de analizar.
- **Perfil:** familia, amigos y contactos de la diáspora (asociaciones culturales, grupos de antiguos alumnos) de edades y zonas distintas (costa e interior; urbano y rural). **Al menos una persona filóloga o docente de galego (idealmente dos)** y, si se puede, alguien "escéptico" con la IA. **Nadie debe haber oído antes a los narradores ni saber quiénes son.** Como incentivo opcional, un sorteo de 50 € entre los participantes [S].
- **Formato:** en línea (webMUSHRA alojado) o presencial, en **este orden obligatorio**:
  1. **Sesión 1, identificación humano/IA en seco (~35 min) + bloque secundario con cama (~6 min): §7.7.** Va primero para que el oyente no haya oído todavía ninguna voz etiquetada como "humana". Si se hiciera después del MUSHRA, reconocería el timbre de la referencia marcada y sabría que es humano.
  2. **Sesión 2, MUSHRA ligero (~15-20 min; puede ser otro día):** texto trampa con la referencia marcada (**rota por oyente**: mitad H1 y mitad H2, o un tercio cada uno si hay H3), la referencia oculta, el **humano de control oculto** (otro narrador; del género de la candidata siempre que lo haya), la voz candidata, la 2.ª clasificada, la **candidata con la otra versión de pausas** (la que perdió en R1-R2; §5B.2) y el ancla baja. Escalas A, B y C.
- **Dispositivos:** cada panelista declara con qué escucha. Se asignan cuotas: **al menos 1/3 del panel con el altavoz del móvil** y al menos 1/3 con auriculares de botón a volumen bajo (el resto, con auriculares normales). Los resultados se desglosan por dispositivo.
- **Análisis MUSHRA (unidad = oyente):** para cada escala, Δ media del panel de la candidata **y del humano de control** frente a la referencia oculta, con un **IC del 90 % por *bootstrap* de oyentes** (10.000 repeticiones). Se añade una **prueba de Wilcoxon por pares** entre la candidata y la 2.ª clasificada, **entre la candidata y el humano de control** y **entre las versiones M y F de la candidata** (decide las pausas de R4 y de la producción; §5B.2) [S]. Post-cribado: se excluye a quien puntúe la referencia oculta por debajo de 90 o por debajo del ancla baja, y se recluta a más hasta llegar a N.
- **Pregunta abierta obligatoria (al final, para no sugestionar):** "¿Notaches algo que non sexa galego correcto? Indica a palabra". Esas palabras alimentan `lexico_tts.tsv`.

**R4: confirmación sobre el producto real (antes de pedir la monetización o, a más tardar, en la Puerta 1 del mes 6)**

- Se repite la identificación de R3 con **N ≥ 20**, de los que **al menos 8 son nuevos**. Los fragmentos sintéticos salen **del episodio ya publicado**, tomados de la **pista de voz en seco** antes de la mezcla (la cadena real, sin la cama), con el mismo bloque secundario con cama que R3; los humanos, de las grabaciones del kit, porque no hay versión humana del episodio. Como la prueba es de estímulo único, no hace falta que los textos coincidan, y el segmento entra como efecto aleatorio en el modelo. Los mismos controles positivo y negativo. Sirve para comprobar que la cadena de producción real (troceo, uniones, 1-3 h de duración, **pase de dirección y escucha de corrección de §5B**) mantiene la calidad del kit. Como el episodio tiene texto nuevo, R4 también comprueba que el selector y el modelo de pausas **generalizan** fuera de S1-S10.

### 7.6 Umbrales para aprobar una voz y validez del test (fijados antes de escuchar) [S]

**Paso 0: validez del test (se comprueba en la fase 1 de la apertura, sin saber aún qué motor es cada código).** Se calcula con los mismos datos que se usarán para la candidata.

| Control | Qué se exige | Si falla |
|---|---|---|
| **Control positivo en MUSHRA** (el humano de control, en cada escala A, B y C) | **Δ(control) ≤ 10** de media, con el límite superior del IC 90 % ≤ 15 (en R1: media de los dos jueces ≤ 10) | Recalibración prerregistrada (abajo) |
| **Control positivo en la identificación** (cada narrador, tratado como si fuera la candidata frente a los demás humanos; §7.7) | **BA(humano) ≤ 0,60** | Recalibración prerregistrada (abajo) |
| **Control negativo en la identificación** (ancla sintética) | **BA(ancla) ≥ 0,75**: la prueba es capaz de detectar una voz claramente sintética | La prueba **no es sensible**: un "aprobado" de la candidata **no vale** (se repite con más oyentes o con otros fragmentos). Un suspenso sí vale |
| **Post-cribado** (referencia oculta ≥ 90) | Como en BS.1534 | Se excluye al oyente y se recluta otro |

**Recalibración prerregistrada (fórmula cerrada, escrita en `preregistro_voz.md`).** Idea: el listón es "no se distingue de un narrador profesional nativo", así que **nunca se exige a la máquina más de lo que consigue otro profesional**, pero tampoco se deja que un test roto baje mucho el listón.

- **MUSHRA**, por escala *s*: umbral efectivo **U_s = máx(10, Δ(control)_s)**, siempre que Δ(control)_s ≤ 15. **Si Δ(control)_s > 15, el test es inválido en esa escala.** Eso quiere decir que mide el parecido a una lectura y no la calidad. **No se decide nada:** se revisan el casting, el *brief* y la cadena, y se repite con otro humano de control o con la rotación corregida. **Un test inválido nunca activa el plan B.**
- **Identificación:** umbral efectivo **U_BA = máx(0,60, BA del peor humano)**, siempre que ese BA sea ≤ 0,65. Por encima de 0,65, el test es inválido (se revisa, por ejemplo, si un narrador suena "procesado" por la cadena común o si su toma tiene ruidos que lo delatan como grabación) y se repite.
- El script escribe `umbral_efectivo.json` y **se sella (hash) antes de la fase 2**. Después no se toca.

**Umbrales de aprobación** (Δ siempre frente a la referencia oculta de la misma pantalla; U_s y U_BA son 10 y 0,60 si el paso 0 pasa sin recalibración):

| Nivel | Condición (todas obligatorias) | Consecuencia |
|---|---|---|
| **Mínimo para R2** | Ambos jueces: A ≥ 70; Δ ≤ 20 en B y C; 0 erros graves; como mucho 2 erros leves | Pasa a finalista |
| **Puerta V-1: aprobada por los jueces** (R1 + R2) | Paso 0 de R1 superado (Δ(control) ≤ 15). Media de los dos jueces: **A ≥ 80** y **Δ ≤ U_s en A, B y C**; **ningún juez con Δ > U_s + 5** en ninguna escala; 0 erros graves y ≤ 1 leve. En la prueba de sueño, **≤ 1 molestia cada 10 min**, nota ≥ 7/10 en ambos jueces y **en los dos dispositivos**, y ningún comentario del tipo "notei que era unha máquina" que se repita en las dos noches. Control ASR y de señal superados sobre un episodio completo (§5.3 y §9) | Pasa al panel |
| **Puerta V-2: aprobada por el panel** (R3; **necesaria para publicar**) | Paso 0 de R3 superado (o recalibrado sin invalidar). MUSHRA: **Δ media ≤ U_s en A, B y C**, con el **límite superior del IC 90 % ≤ U_s + 5**; menos del 20 % del panel señala algún "non é galego"; el filólogo no detecta erros sistemáticos. Identificación (§7.7): **BA media ≤ U_BA**, con el **límite superior del IC 90 % ≤ U_BA + 0,10**, la prueba de signos sobre oyentes sin rechazo (α = 0,05) y el control negativo ≥ 0,75 | **Voz del canal. Se puede publicar** |
| **Confirmada para monetizar** (R4) | Los mismos umbrales de V-2, incluido el paso 0, sobre el episodio publicado | Se mantiene. Si falla: corregir el léxico o la cadena y repetir R4 una vez; si vuelve a fallar, cambiar a la 2.ª o activar el plan B (§8.1) |

**Por qué estos números [S].** La v2 justificaba Δ ≤ 10 con la franja "excelente" de MUSHRA. **Ese argumento se retira.** Como la referencia oculta es la misma grabación que la marcada, puntúa ~100 por construcción, así que Δ ≤ 10 solo medía cuánto se parece una voz a *esa* lectura. En la v3 el número 10 es solo un **punto de partida** y su validez se comprueba en cada prueba: **un segundo profesional, que lee de otra manera, tiene que quedar dentro**. Si queda, el listón es alcanzable por un humano y es justo exigírselo a la máquina. Si no, se ajusta hasta donde llegó ese humano (con un tope de 15) o se declara el test inválido. El margen de 5 (por juez y en el IC) admite el ruido de un panel de 20-24 personas sin dejar pasar una voz claramente peor. **Los umbrales y la fórmula se escriben en `preregistro_voz.md` antes de abrir ninguna clave y no se tocan después.** Solo se pueden recalibrar para la *siguiente* evaluación, con los datos de R4 y los comentarios reales.

Criterio de desempate entre dos voces aprobadas: (1) menor Δ en C; (2) menor BA en la identificación; (3) A; (4) coste y licencia (se prefiere Nós); (5) estabilidad en §9.

### 7.7 Prueba ciega de identificación humano/IA (rediseñada en la v3)

**Pregunta:** ¿un oyente nativo atento, sin nada con qué comparar, distingue la voz candidata de narradores humanos profesionales?

**Qué fallaba en la v2.** Cada oyente oía 4 fragmentos de **solo dos timbres** (un humano y la candidata), así que la tarea se reducía a "separar dos voces y adivinar cuál es la máquina". Los 4 ensayos de cada persona estaban muy correlacionados, y el cálculo binomial por ensayos (N = 40) **sobreestimaba la potencia**. En el caso extremo, en el que cada oyente responde por timbre, los 40 ensayos equivalen a 10: la regla "≤ 24/40" pasa a ser "≤ 6 de 10 oyentes", y **P(aprobar | p = 0,75) sube de 0,026 a ~0,22**; con p = 0,70, de 0,12 a ~0,35 [CALC] `sim/extremo.py`. Además, sin un humano de control no se podía saber si un suspenso era culpa de la voz o del test.

**Diseño v3 (fijado en `preregistro_voz.md`) [S salvo cálculo]:**
- **Estímulos:** 10 segmentos de ~3 min (S1-S10) del guion piloto. Para cada oyente se forma un bloque de **10 fragmentos = 5 voces × 2 fragmentos**:
  - **2 humanos** distintos (de H1-H3; al menos uno del género de la candidata);
  - **la candidata** (la finalista de R2);
  - **la 2.ª clasificada** (otra voz sintética; también sirve de distractor);
  - **el ancla sintética** (Azure Sabela o Google Standard-B sin ajustes): el **control negativo**.
- **Por qué así:** cada voz suena exactamente dos veces, de modo que **contar repeticiones no da pistas**. Hay 5 timbres, y en las voces sintéticas hay de los dos géneros siempre que sea posible, así que "separar dos voces" ya no resuelve la tarea. Además, el oyente **no sabe cuántas voces humanas hay**: se le dice que "pode haber entre 0 e 10 fragmentos lidos por persoas".
- **Asignación:** qué segmento suena con qué voz y en qué orden sale de un **diseño equilibrado (cuadrados latinos)**: cada segmento aparece con cada tipo de voz en proporciones iguales en el panel. Ningún oyente oye el mismo texto dos veces. Los pares de humanos rotan entre oyentes (H1+H2, H1+H3, H2+H3 si hay H3).
- **Tarea:** estímulo único. Tras cada fragmento, "¿Persoa ou IA?" y la **confianza** (1-4). Se permite pausar, pero no volver atrás.
- **Presentación (v5): en seco.** La misma cadena y el mismo *room tone* para todos, **sin cama sonora** (§7.2). Es la condición más exigente y la que corresponde al listón de "audiolibro profesional". Todo lo que sigue (métrica, umbrales, potencia) se refiere a este bloque.
- **Bloque secundario con cama (informativo, ~6 min, al final de la sesión 1):** 4 fragmentos de 90 s con la mezcla del producto (la candidata × 2 y un humano × 2, distintos de los del bloque principal). **No decide nada.** Se calcula su BA agregada de panel; si supera en ≥ 0,10 a la BA en seco de la candidata, la mezcla **delata** algo que el seco no delata (un *ducking* mal ajustado, un bombeo de la cama en las pausas) y se corrige la mezcla antes de publicar. Si queda por debajo, confirma que la cama no "salva" una voz que en seco suspende: **una voz no puede aprobar gracias a la cama**.

**Métrica y análisis (unidad = oyente):**
- Para cada oyente *i*: **BA_i = ½ · [ proporción de fragmentos de la candidata que llama "IA" + proporción de fragmentos humanos que llama "Persoa" ]**, con 2 fragmentos de la candidata y 4 humanos. **BA = 0,50 significa que no distingue** y BA = 1 que distingue perfectamente. La exactitud equilibrada no se ve afectada por la tendencia de cada oyente a decir "IA" más o menos a menudo. Equivale a los "% de aciertos" de la v2 con clases equilibradas: el listón del 60 % se mantiene.
- **Análisis principal:** media de BA_i entre oyentes, con el **límite superior del IC 90 % unilateral por *bootstrap* de oyentes** (10.000 remuestras de oyentes enteros, que conservan la correlación de sus ensayos).
- **Complemento a nivel de oyente:** **prueba de signos** (binomial sobre **oyentes**, no sobre ensayos) de cuántos oyentes tienen BA_i > 0,5 frente a < 0,5, sin contar los empates. Si rechaza H0 con α = 0,05 unilateral, la voz suspende.
- **Confirmación con un modelo logístico mixto:** `resp_IA ~ voz + (1 | oyente) + (1 | segmento)` (con `(1 | oyente:voz)` si converge), en R (`lme4::glmer`) o en Python (`statsmodels` BinomialBayesMixedGLM). Del modelo se obtienen las probabilidades marginales y el BA con IC. Si el modelo y el *bootstrap* no coinciden en la decisión, **se aplica la más conservadora**.
- **Controles con los mismos datos:** BA(ancla) (control negativo, ≥ 0,75) y **BA de cada humano**, tratado como si fuera la candidata frente al otro humano de su bloque (control positivo, ≤ 0,60). Así, el humano de control pasa **exactamente la misma puerta** que la máquina (§7.6, paso 0).

**Tamaño de muestra y potencia (simulación con correlación dentro de cada oyente) [CALC].** Scripts: `sim/regla_final.py`, `sim/potencia_ident_v2.py` y `sim/extremo.py`, 20.000 réplicas por celda. Se simulan tres modelos de dependencia. (a) Logístico mixto con sesgo y capacidad propios de cada oyente, más un efecto oyente × voz (el timbre) de DT 1,2. (b) Igual, pero con un efecto de timbre fuerte (DT 3). (c) **Extremo**: cada oyente da la misma respuesta a los dos fragmentos de cada voz. La regla simulada es la completa de §7.6: media ≤ 0,60, IC sup ≤ 0,70 y prueba de signos sin rechazo.

| Oyentes (N) | P(aprobar) si nadie distingue (BA = 0,50) | BA = 0,60 | BA = 0,65 | P(aprobar) con BA = 0,70 (p. ej. 80 % "IA" a la candidata y 40 % a los humanos) | P(aprobar) con BA = 0,75 |
|---|---|---|---|---|---|
| 16 | 0,80-0,94 | 0,33-0,44 | 0,13-0,14 | 0,017-0,030 | ≤ 0,003 |
| **20 (mínimo)** | **0,88-0,97** | 0,39-0,46 | 0,13-0,15 | **0,009-0,031** | **≤ 0,002** |
| **24 (objetivo)** | **0,93-0,97** | 0,43-0,45 | 0,10-0,16 | **0,005-0,025** | **≤ 0,001** |

*(Rango = mínimo y máximo de los tres modelos de dependencia; el peor caso es siempre el extremo.)*

- **Lectura:** con N = 20 una voz que el panel detecta claramente (BA ≥ 0,70) se cuela en ≤ 3 % de los casos **incluso si todos responden por timbre**, y una voz realmente indistinguible aprueba en el 88-97 % de los casos. Con N = 16 la potencia contra una voz buena baja al 80 % en el peor caso, así que **20 es el mínimo y no se aceptan paneles menores**. Una voz en la frontera (BA ≈ 0,60) aprueba ~40-45 % de las veces: es lo esperado para un umbral y **la prueba no sirve para afinar por debajo de ±0,05**.
- **Supuestos de la simulación [S]:** tasa base de respuestas "IA" del 40 % y DT del sesgo del oyente de 0,8 en logit. No se ha hecho un análisis de sensibilidad exhaustivo; en el modelo (b), con 30 oyentes, P(aprobar | BA = 0,50) sube a 0,98. Antes de sellar el prerregistro se vuelve a correr la simulación con la tasa base observada en R1. El IC de la simulación usa la aproximación t sobre las BA_i; en el análisis real se usa el *bootstrap*.
- **Filólogo(s):** reciben el mismo bloque de 10 y, si aceptan, un **2.º bloque** con otros humanos y otra voz sintética. Con 4-6 fragmentos de la candidata, un individuo **no tiene potencia estadística**: si responde por timbre, acertarlo todo tiene una probabilidad de 1/2 elevado al número de voces (1/8-1/16) aunque no distinga nada. Por eso su resultado **no es una puerta estadística sino una alarma cualitativa**: si identifica bien todas las voces **y** da una explicación articulatoria concreta ("as vogais abertas soan…"), se documenta, va al `lexico_tts.tsv` o a los ajustes y se revisa antes de publicar.
- **Dispositivos:** BA desglosada por dispositivo (con 6-8 oyentes por grupo es orientativa). Si un grupo supera 0,70, se investiga la causa (p. ej. sibilancias en el altavoz del móvil) antes de publicar.
- **Confianza:** si los aciertos van con confianza alta (3-4) y los fallos con confianza baja, hay señal aunque la BA no llegue al umbral. Se anota como riesgo y se revisa en R4.

**Coste:** 0 € (o 50 € de sorteo opcional) + los audios ya producidos. Tiempo del promotor: ~3-4 h de reclutamiento y organización (§10). Tiempo por panelista: ~55-60 min en dos sesiones (incluido el bloque secundario con cama).

---

## 8. Árbol de decisión por etapa

### 8.1 Etapa 1 (meses 1-6; < 50 €/mes + excepción única de ~850-1.500 € por las referencias y el revisor profesional, techo de ~2.050 €; ~4 h/semana)

```
Semana 0: correo a Proxecto Nós (USC) sobre el uso comercial
          + contratar H1 y H2 (hombre y mujer; §7.2)
          + preregistro sellado (umbrales, fórmula, N = 20-24, script)
          + kit_voz.py → R0 → R1 → R2 → (H3 opcional) → R3   (~5-6 semanas)
│
├─ PASO 0 (fase 1 de la clave): ¿pasan los controles?
│    ├─ Humano de control con Δ ≤ 15 y BA ≤ 0,65, y ancla con BA ≥ 0,75
│    │    → umbral efectivo sellado (10 / 0,60, o recalibrado) → seguir
│    └─ NO → TEST INVÁLIDO: ni aprueba ni suspende. Se corrige (casting,
│            brief, cadena, más oyentes) y se repite R1 o R3.
│            NUNCA activa el plan B ni el "esperar". (Excepción: si solo
│            falla el ancla, la prueba es poco sensible; un suspenso de la
│            candidata vale, pero un aprobado no.)
│
├─ ¿Supera la Puerta V (V-1 y V-2) alguna voz de Nós
│   (StyleTTS2 Brais/Celtia o VITS Sabela-Nós)?
│    └─ SÍ → VOZ DEL CANAL = Nós (0 €). Reserva = la 2.ª que apruebe.
│            └─ ¿Hay CONFIRMACIÓN ESCRITA de la USC para el uso en un canal
│               monetizado? → publicar, con crédito visible.
│               Sin respuesta en 30 días → 2.º correo + vía de transferencia
│               de la USC (§4). El silencio NO es permiso: mientras no haya
│               respuesta, la voz del canal es la mejor de pago que haya
│               aprobado la Puerta V (si la hay, con el cambio anunciado a Nós
│               solo si llega el permiso antes del vídeo 1); si no hay
│               ninguna de pago aprobada → ESPERAR sin publicar (preparar
│               guiones y pipeline). Negativa o condiciones inasumibles →
│               la reserva que no sea de Nós, o (c)/(b).
│
├─ NO → ¿La supera alguna de pago (ElevenLabs v4/v3, Gemini-TTS, Azure)?
│    └─ SÍ → VOZ DEL CANAL = la de menor Δ en C, si cuesta < 25 €/mes con
│            2,5 h al mes (§3). Si hay empate, la más barata.
│
└─ NINGUNA supera la Puerta V → NO SE PUBLICA CON VOZ SINTÉTICA.
       No hay otra salida del tipo "publicar con la menos mala".
       Orden de salidas (el promotor decide antes de R1, Q2):
       (c) VÍA INTERMEDIA (§5B.4), si algún narrador firmó la opción T1
           y la mejor voz de Nós quedó "cerca" (Δ ≤ 20 en B y C y A ≥ 75
           en R1; si quedó lejos, el fine-tune tiene pocas opciones):
           1. Ejercer T1 con el narrador del género de la mejor base
              (base Brais → el narrador; base Celtia → la narradora):
              30-60 min extra en estilo
              "durmir", con textos ajenos a S1-S10 y al texto trampa.
           2. Fine-tune de StyleTTS2-GL (Colab/Runpod, ~60-100 USD).
              Si en paralelo se quiere probar un PVC de ElevenLabs con el
              mismo audio, la verificación la hace el narrador.
           3. Contratar H3 si no se hizo (obligatorio en esta vía).
           4. R0 → R1 → R2 → R3 con §5B.1-5B.2; el narrador de origen NO
              aparece como humano en las pruebas del clon.
           Coste hasta saber si funciona: ~700-1.250 € (a 6-8 semanas).
           ├─ Pasa la Puerta V-2 → ejercer T2 (300-600 € en cuotas +
           │   10-15 % de ingresos) → VOZ DEL CANAL, con crédito
           │   "voz de X, con licenza". R4 como siempre.
           └─ No pasa → (a) o (b). Lo gastado deja un corpus de 30-60
               min, un narrador ya implicado y un modelo base para el (b).
       (a) ESPERAR: no publicar. Reevaluación trimestral (R0 + R1 exprés,
           reutilizando las mismas grabaciones H1/H2) con los modelos nuevos (Nós
           publica varias voces al año; ElevenLabs y Gemini evolucionan).
           Mientras tanto, la Etapa 1 avanza en guiones y pipeline, sin canal.
       (b) ADELANTAR EL LOCUTOR CON LICENCIA COMPLETA (plan B):
           1. Contrato de "demo" con H1, H2 o H3 (u otro del
              casting): 1-3 h grabadas a 48 kHz y cesión
              limitada para clonación (1-2 años, solo YouTube, revisión de
              muestras por el locutor, borrado del modelo al final).
           2. Clon: ElevenLabs PVC (plan Creator, 22 USD/mes [F]) y, en
              paralelo, fine-tune de StyleTTS2-GL (0 € + GPU).
           3. El clon pasa la MISMA Puerta V (R1 → R3). La grabación original
              del locutor hace de referencia y OTRO narrador hace de
              control positivo. Si no pasa: camino (a).
           Coste: 1.000-2.500 € iniciales [F-sec UVA + S] + 22 USD/mes.
       (c) y (b) rompen el presupuesto de la Etapa 1 → exigen una
       decisión explícita del promotor (es adelantar parte de la Etapa 3).
       Cuentas honestas [CALC sobre S; tarifas v5]: con P(aprobar c) =
       40 %, prueba de (c) ≈ 950 €, T2 ≈ 450 € y un (b) de ~1.550 €
       (reutilizando el corpus), el coste esperado de "(c) y, si falla,
       (b)" es ≈ 950 + 0,4·450 + 0,6·1.550 ≈ 2.060 €, MÁS que ir directo
       a (b) (≈ 1.750 €). La ventaja de (c) no es el coste esperado: es
       que compromete ~950 € en vez de ~1.750 €, que en el 30-50 % de los
       casos cierra el problema con ~1.400 € en total (con el fijo de T2
       en cuotas) y que, si falla, el promotor puede parar en (a) habiendo
       arriesgado algo más de la mitad. Con las tarifas revisadas la
       ventaja de (c) se estrecha; si los presupuestos reales de T1 salen
       en el extremo alto (> 650 €), (b) directo pasa a ser preferible.
```

**Reglas de la Etapa 1:**
- La voz queda **bloqueada durante los primeros 10 vídeos** (coherencia de marca, V10).
- R4 se hace **antes de pedir la monetización** o en la Puerta 1 (mes 6), lo que llegue antes.
- El control ASR y de señal (§5.3 y §9) corre en **cada episodio**. Si más del 5 % de los párrafos necesitan regeneración o revisión manual, se revisan los ajustes del motor [S].
- **Cada episodio se produce con el método de §5B**: N = 4 variantes con contexto, pase de dirección en las dudosas (15-35 min) y **escucha completa de corrección por un revisor validado con la prueba de defectos sembrados** (1,0-1,6 h según la velocidad validada; §5B.3.1 y 5B.3.3), más el **revisor profesional en los episodios 1-6**. **Ningún episodio se publica sin la firma de esa escucha** en `defectos.csv`. **Antes del episodio 1:** prueba sembrada superada por al menos un revisor de la casa y por el profesional, o bien un modo de escucha alternativo decidido (pareja o profesional). Prueba trimestral desde el mes 4.

### 8.2 Etapa 2 (meses 7-18; 50-200 €/mes; 6-10 h/semana)

- **Reevaluación semestral** (R0 + R1 exprés, ~2 h, con las mismas grabaciones H1/H2, rotación y control positivo incluidos): se meten los modelos nuevos (Nós, ElevenLabs, Gemini GA…) contra la voz del canal. **Solo se cambia** si la nueva reduce Δ en C en ≥ 5 puntos, no empeora A y supera también una identificación de R3. El cambio se anuncia y se aplica desde un vídeo concreto.
- **Señales de alarma que activan una revisión fuera de calendario:**
  - más del 2 % de los comentarios critican la voz o la pronunciación [S];
  - la retención media cae por debajo del umbral de `drafts/retornos.md` y la curva de audiencia muestra caídas en los primeros 2-3 min (el momento en que el oyente decide si la voz le vale) [S].
- **Control de calidad por muestreo (§5B.3.4, v5):** se pasa de la escucha completa al muestreo de aceptación cuando, en los 4 últimos episodios, la tasa de bloques defectuosos estimada contra la verdad de referencia es *p̂* ≤ 3 %, sin ningún grave escapado, y los revisores de la casa mantienen la validación trimestral. El plan: **40 bloques de 2 min (20 del revisor profesional a 1× y 20 de la casa), c = 0, escucha completa si aparece un solo defecto**, con ≤ 0,48-0,53 bloques defectuosos publicados por episodio de 2 h con *p* ≤ 3 %. Se vuelve al 100 % si se rechazan 2 de los últimos 5, si *p̂* > 3 % o si un revisor pierde la validación. Revisor profesional: 48-84 €/mes con 3 episodios (64-112 € con 4) [S]. Prueba sembrada trimestral y captura-recaptura continua (§5B.3.5). Los pesos del selector (§5B.1) y el modelo de pausas (§5B.2) se reajustan cada 4 episodios con los defectos registrados.
- **Preparación de la Etapa 3 sin gastar:** mantener la relación con los narradores H1-H3 y con 1-2 locutores más del casting. Las opciones T1/T2 que no se ejercieron caducan a los 6 meses; si el canal funciona, se renegocian como parte de la Etapa 3.

### 8.3 Etapa 3 (desde el mes 19; 1.000-5.000 € iniciales): ¿cuándo pagar licencia o clonación?

Con la Puerta V de la versión 2, la voz publicada ya queda "a ≤ 10 puntos del humano". La licencia de la Etapa 3 deja de ser un parche de calidad y pasa a ser una **decisión de marca y de escala**.

**Se paga la licencia completa de un locutor solo si se cumplen las tres condiciones [S]:**
1. **Negocio:** Puertas 1 y 2 superadas (`drafts/retornos.md`).
2. **Motivo medible**, por al menos uno de estos caminos:
   - R4 repetido en la Etapa 2 con Δ > 10 en C o una identificación > 60 % (la voz se ha quedado atrás, por ejemplo porque el oído del público se afina);
   - más del 2 % de los comentarios o reseñas critican "a voz de robot";
   - una convocatoria o patrocinio relevante (Youtubeiras+, Xunta, marcas galegas) exige o puntúa la voz humana (`research/ingresos_alt.md`);
   - la expansión es/pt de la Etapa 3 necesita una voz de marca común en tres idiomas;
   - ya se activó el plan B en la Etapa 1 y hay que pasar de la "demo" a un contrato completo.
3. **El prototipo gana:** el clon licenciado supera la Puerta V-2 y gana a la voz actual por **≥ 5 puntos en C y en B** en un R3 con 20 o más oyentes, con p < 0,05 en la prueba de Wilcoxon y con los controles positivo y negativo superados.

**Secuencia y costes:**

| Paso | Qué | Coste [S salvo cita] |
|---|---|---|
| 1 | Casting con 3 locutores (si no se hizo ya): demo de 2 min leyendo el texto trampa | 0-300 € |
| 2 | Contrato de **demo**: 1-3 h grabadas (ElevenLabs recomienda al menos 1 h e "ideally as close to three hours as possible" para el PVC [F] https://elevenlabs.io/docs/product-guides/voices/voice-cloning/professional-voice-cloning) → clonación PVC en ElevenLabs (plan Creator o superior [F] https://elevenlabs.io/pricing; verificación por el propio locutor) **y** *fine-tune* de StyleTTS2-GL en paralelo, para comparar. **Si ya se hizo la vía intermedia (§5B.4), este paso parte de su corpus y de su modelo** | 1.000-1.500 € (referencia UVA [F-sec]) + 22-99 USD/mes |
| 3 | R1-R3 con el prototipo frente a la grabación original y frente a la voz actual | 0 € |
| 4 | Si gana: contrato completo (2-4 h de estudio; cesión de 2-3 años; solo YouTube y pódcast; es/pt por separado; revenue share del 5-15 %; derecho del locutor a revisar muestras; cláusula de fin y borrado del modelo) | 2.000-6.000 € + royalties (referencia UVA de 5.000-7.500 € con varias jornadas [F-sec]) |
| 5 | Relanzamiento: vídeo de presentación del locutor (con su cara y su voz real) y etiqueta "Altered or synthetic content" | 0 € |

**Alternativa más barata que hay que comprobar en la Etapa 2 [S]:** si en la *Voice Library* de ElevenLabs aparece una voz de un **nativo galego** que supere la Puerta V, trae licencia comercial y su dueño cobra por uso [F] https://elevenlabs.io/docs/eleven-creative/voices/payouts . El riesgo es que la retire (preaviso de 0 a 2 años, a elección del dueño [F] ídem), así que solo sirve con preaviso largo.

**Qué no se hace nunca:** clonar sin consentimiento, usar la grabación de referencia para entrenar sin un contrato nuevo, usar las voces de Brais o Celtia fuera de los modelos publicados, o "imitar" a un locutor conocido (V6).

---

## 9. Control automático de pronunciación con ASR

### 9.1 Qué puede y qué no puede hacer un ASR

- **Sí detecta [S]:** palabras omitidas, repetidas o inventadas (*hallucinations* del TTS), palabras tan mal pronunciadas que se transcriben como otra cosa, topónimos irreconocibles, cortes y silencios anómalos.
- **No detecta [S]:** el **acento**. Las vocales abiertas y cerradas no se distinguen en la ortografía (*ovo* y *ovos* se escriben igual con cualquier pronunciación), y el modelo de lenguaje del ASR tiende a "corregir" hacia la palabra esperada. Una lectura castellanizada puede dar WER = 0. **El ASR es un detector de errores gruesos, no un juez de calidad galega.** R1-R4 no se sustituyen.

### 9.2 Herramientas (todas gratuitas)

| ASR | Por qué | Rendimiento en galego |
|---|---|---|
| **Whisper large-v3** (o *fine-tunes* para galego: `mozilla-ai/whisper-large-v3-gl` [F] https://huggingface.co/mozilla-ai/whisper-large-v3-gl ) con `faster-whisper` o `whisperX` para las marcas de tiempo por palabra [F] https://github.com/m-bain/whisperx | Robusto, con puntuación y marcas de tiempo | WER de Whisper según el corpus: 0,97 % (FalAI), 6,88 % (Common Voice), 8,08 % (OpenSLR), 19,8 % (FLEURS) [F] https://huggingface.co/proxectonos/w2v-bert-2.0-gl ; en FLEURS, large-v3 sin ajustar ~10 % y ajustado ~8,6 % [F-sec] https://arxiv.org/abs/2503.23542 |
| **Nós w2v-BERT 2.0 gl** (CTC, Apache-2.0) [F] https://huggingface.co/proxectonos/w2v-bert-2.0-gl | Modelo **acústico, sin modelo de lenguaje fuerte**: "corrige" menos, así que delata mejor la mala pronunciación [S]. Entrenado con galego de Galicia | WER de 11,6 % en el conjunto combinado; 6,3 % en Common Voice [F] ídem |
| (opcional) Nós wav2vec2-XLSR-53-gl con LM | Tercera opinión | WER 6,86 % (OpenSLR77) [F] https://huggingface.co/proxectonos/Nos_ASR-wav2vec2-large-xlsr-53-gl-with-lm |

**Sesgo a vigilar [S]:** los ASR de Nós pueden haberse entrenado con corpus que incluyen a los mismos locutores que los TTS de Nós. Eso los haría "demasiado buenos" reconociendo a Brais o a Celtia. Se compensa con Whisper como segundo ASR y con la calibración de §9.3. Los ASR trabajan a 16 kHz, así que el control ASR **no ve** los problemas de ancho de banda: para eso está §9.5.

### 9.3 Procedimiento por párrafo [S]

1. **Normalizar** el guion y las transcripciones: minúsculas, sin puntuación, números en letra (el guion ya viene así, `drafts/guion.md`) y la misma forma para las contracciones.
2. **Calibrar con las grabaciones profesionales:** pasar los dos ASR por los ~30 min de **cada** narrador (§7.2) para obtener el WER y el CER "de base" de cada ASR con este texto y este estilo. Las dos lecturas dan un **rango humano** (no un único número). Ese es el patrón "humano correcto": una voz sintética no debería superar con holgura al peor de los dos.
3. **Transcribir cada párrafo** sintetizado con los dos ASR (`language="gl"`) y alinearlo con el guion (distancia de edición por palabras).
4. **Marcas (flags):**
   - `OMISION` o `INSERCION`: 3 o más palabras seguidas que faltan o sobran en **ambos** ASR → **regenerar**.
   - `WER_ALTO`: WER del párrafo > 2 × la base del peor narrador **y** > 10 % en ambos ASR → **regenerar**.
   - `LISTA_CRITICA`: un topónimo o nombre de `lista_critica.txt` (generada del guion: mayúsculas y palabras de `lexico_tts.tsv`) que **ninguno** de los ASR reconoce (CER de esa palabra > 30 %) → regenerar; si falla dos veces, **escucha humana** de ese punto.
   - `DISCREPANCIA`: los ASR no coinciden entre sí en una palabra que sí está en el guion → **escucha humana** (solo esa palabra, con enlace al segundo exacto).
5. **Bucle:** máximo 3 regeneraciones por párrafo (cambiando la semilla o el ajuste). Después, a la cola de revisión humana. El informe `qa_voz.html` lista las marcas con reproductor por segmento, para que la revisión humana dure minutos y no horas.

```python
# Esquema mínimo (faster-whisper + jiwer); w2v-BERT-gl se añade igual con transformers
from faster_whisper import WhisperModel
import jiwer
asr = WhisperModel("large-v3", compute_type="int8")
def wer_parrafo(wav, texto_guion, norm):
    segs, _ = asr.transcribe(wav, language="gl", beam_size=5)
    hyp = " ".join(s.text for s in segs)
    return jiwer.wer(norm(texto_guion), norm(hyp)), hyp
```

### 9.4 Métricas de ritmo con el alineamiento [S]

A partir de las marcas de tiempo por palabra (whisperX o alineamiento CTC con w2v-BERT):
- **Palabras/min habladas** por párrafo. Marca si se desvía más de ±15 % de la mediana del episodio (detecta prisas o frenazos). Se compara con el rango de los dos narradores sobre el mismo texto.
- **Pausas reales** entre frases y párrafos frente al objetivo de §5.1. Marca los silencios mayores de 4 s que no estén en una transición de capítulo.
- **Palabras/min percibidas** del episodio completo (objetivo: 110-125).

### 9.5 Detector de anomalías de señal (sin ASR) [S]

- Sonoridad a corto plazo (`pyloudnorm`): saltos de más de 3 LU entre segmentos contiguos.
- Picos o recortes (*clipping*) por encima de −1 dBTP.
- **Suelo de ruido** en las pausas > 0,5 s: marca si es > −65 dBFS RMS o si hay tramos de silencio digital exacto (§5.3).
- **Clics en las uniones:** salto de amplitud entre muestras contiguas por encima de un umbral calibrado con las grabaciones de los narradores.
- **Artefactos de vocoder:** ráfagas de planitud espectral o de energía anómala por encima de 6 kHz de menos de 200 ms, y componentes tonales estrechos persistentes (zumbido metálico).
- **Deriva de la voz:** cambios bruscos de F0 medio o del centroide espectral entre párrafos (V5).
- **Ancho de banda efectivo** por episodio (para detectar cambios de motor o de formato de salida).
- **Resultado:** "anomalías por 10 min". Se usa en R0, en R2 (prueba de sueño) y en la QA de cada episodio. El umbral de publicación es ≤ 1 cada 10 min, y cada anomalía marcada se escucha.

### 9.6 Qué se sigue revisando a mano en cada episodio [S]

- La lista de `DISCREPANCIA`, `LISTA_CRITICA` y anomalías del informe (unos 5-15 min), dentro del **pase de dirección** de §5B.1 d.
- **Sustituido en la v4:** las "3 catas de 2 min" de la v3 no bastaban para garantizar calidad de audiolibro (con 3 bloques de 38, un episodio con 4 bloques defectuosos pasaba sin detectar el ~70 % de las veces [CALC, hipergeométrica]). Ahora hay **escucha completa en la Etapa 1 y muestreo de aceptación diseñado en la Etapa 2** (§5B.3), y desde la v5 **la hacen revisores con la sensibilidad medida** (prueba de defectos sembrados y revisor profesional de referencia; §5B.3.1-5B.3.5).
- El ASR **reduce** lo que tiene que encontrar el oído, pero **no sustituye** la escucha: el acento, las vocales abiertas y cerradas y las pausas raras solo los detecta un nativo.

---

## 10. Plan de ejecución (primeras 6-7 semanas de la Etapa 1)

| Semana | Tarea | Horas del promotor [S] | Coste |
|---|---|---|---|
| 1 | Correo a Proxecto Nós. Casting por correo de 4-6 narradores (al menos 2 hombres y 2 mujeres) (demo de 1 min del texto trampa). Claude Code construye `kit_voz.py` (Colab para StyleTTS2; API de Azure, Gemini y ElevenLabs con cuentas gratuitas o de prueba). Revisión del texto trampa con su mujer. Redacción y sellado de `preregistro_voz.md` (con los scripts de análisis y de simulación de `sim/`) | 4 h | ~5 USD de pruebas de pago (ElevenLabs Starter, 6 USD) |
| 1 | En el casting se negocian también las **opciones T1/T2** (§5B.4) y se firman con T0 | (incluido) | Prima de opción 0-50 € por narrador [S] |
| 1 | **Revisor lingüístico profesional (§5B.3.2):** 3 presupuestos por escrito (directorio de la AGPTI, estudios de dobraxe, correctores de audiolibros), con el entregable definido. Búsqueda del convenio de dobraxe de Galicia y de tarifas publicadas de asesoría lingüística (pendiente de la v5) | 0,5 h | 0 € |
| 2 | Grabación de H1 y H2 (remota; cada narrador entrega su WAV sin haber oído al otro). R0 automática, calibrada con las dos grabaciones | 1 h | **600-1.000 €** (300-500 € por narrador; 3 presupuestos en la semana 1), una sola vez |
| 2 | **Método de producción (§5B), con Claude Code:** alineamiento de H1/H2 y ajuste del **modelo de pausas y entonación** (cruzado, dejando un segmento fuera); renderizador con contexto y N = 4; **calibración del selector** con 60 frases elegidas a ciegas por un nativo que no es juez (uno de los narradores, ~1 h); sellado de `seleccion_v1.yaml` y del modelo de pausas antes de generar el kit | 2 h (+ construcción con Claude Code, dentro del MVP de `pipeline.md`) | 0-40 € (gratis si calibra un panelista que después se excluye de R3; 25-40 € si lo hace un narrador) + 0-2 USD de GPU |
| 2-3 | R1: ~70 min por juez (2 pantallas con los papeles de H1/H2 invertidos). Fase 1 de la clave y paso 0 | 1,5 h (+1,2 h de ella) | 0 € |
| 3 | R2: pares (20 min + 10 min de pares "F contra M") y 2-3 noches de sueño real por juez, en dispositivos reales. Decisión F/M según la regla de §5B.2 | 1,2 h (+1,2 h de ella) | 0 € |
| 3-4 | (Opcional) grabación de H3, del género de la finalista | 0,5 h | +300-500 € |
| 4-5 | R3: reclutar a **20-24 panelistas** (con filólogo, cuotas de dispositivo y diáspora), bloques equilibrados generados por `kit_voz.py`, enviar los enlaces de las 2 sesiones y recoger los resultados | 4 h | 0 € (webMUSHRA en un servicio gratuito o local) + sorteo opcional de 50 € |
| 5-6 | Apertura de la clave **en dos fases** (controles → umbral sellado → motores), análisis automático (script: Δ, *bootstrap* de oyentes, prueba de signos, modelo mixto), decisión según §7.6 y §8.1; `lexico_tts.tsv` inicial; ajustes finales de ritmo | 2 h | 0 € |
| 6-7 | **Prueba de defectos sembrados (§5B.3.1)** con la voz elegida: `siembra_defectos.py` genera E_A y E_B (36 defectos cada uno, clave sellada); el profesional valida la lista y hace su prueba; cada revisor de la casa, E_A y E_B a 1,25× y a 1× en diseño cruzado. Decisión sobre quién firma y a qué velocidad. **Sin este paso no hay episodio 1** | 2 h de preparación + 2 h de escucha (+2 h de ella) | Dentro del paquete del profesional (~250-500 € para la prueba y los episodios 1-6) |
| 7-14 | **Solo si ninguna voz aprueba y se elige (c):** ejercer T1, grabación extra, *fine-tune*, H3 y R0-R3 del clon (§5B.4) | 10-20 h (con Claude Code) + ~3 h de ella | ~700-1.250 € (decisión Q3) |
| **Total (sin la vía intermedia)** | | **~20 h del promotor + ~4,7-5,7 h de su mujer + ~55-60 min por panelista (2 sesiones)** | **~855-1.505 €** una sola vez (H1 + H2 600-1.000 € + profesional 250-500 € + ~5 USD de pruebas); con H3 y el sorteo, hasta **~2.050 €** (techo; sin contar las primas de opción de 0-50 € por narrador ni la calibración de 25-40 € si la paga un narrador) |

**Entregables:** `preregistro_voz.md` (umbrales y diseño, fechado antes de escuchar), `ranking_voces.csv` (A, B, C y Δ por juez y panelista), `identificacion.csv` (oyente, segmento, voz, respuesta, confianza y dispositivo), `umbral_efectivo.json` (sellado entre las dos fases), `decision_voz.md` (voz elegida, reserva, ajustes, formato de salida, licencia, narradores usados y resultado de los controles), `lexico_tts.tsv`, `lista_critica.txt`, `seleccion_v1.yaml` (pesos del selector, sellado), `modelo_pausas.json` (parámetros por tipo de frontera y de final de párrafo), `defectos.csv` (registro de la escucha de corrección, con quién encontró cada defecto), `siembra_clave.json` (sellada) y `sensibilidad.csv` (acierto de cada revisor en la prueba sembrada y en la captura-recaptura) y el pipeline de QA (§5.3, §5B y §9) integrado en el "auditor QA" del pipeline agéntico.

---

## 11. Supuestos clave y preguntas abiertas

| # | Supuesto o pregunta | Cómo se resuelve |
|---|---|---|
| S1 | Nós StyleTTS2 aguanta 60-120 min sin deriva ni *glitches* | R2 y detector de §9.5 |
| S2 | ElevenLabs v4 y Gemini-TTS no tienen acento claramente extranjero en galego | R1 con el texto trampa |
| S3 | El objetivo de 110-125 palabras/min adormece en galego sin sonar "arrastrado" | R1 con 2 velocidades por motor, patrón del narrador y retención en Studio |
| S4 | Los umbrales de §7.6 (A ≥ 80; Δ ≤ 10; BA ≤ 0,60), validados en cada prueba por el control positivo, separan bien lo publicable de lo que no lo es | Recalibración **solo para la siguiente evaluación**, con R4 y los comentarios reales |
| S5 | La USC confirma **por escrito** el uso comercial de las voces de Nós (el silencio no cuenta) | Correo en la semana 0; si no hay respuesta, 2.º correo y vía de transferencia; mientras tanto, §8.1 |
| S6 | Cada narrador de referencia cuesta 300-500 € (600-1.000 € por H1 + H2; techo de 1.500 € con H3). **No hay tarifa gallega publicada**: la horquilla va de la tarifa genérica española (185-250 €) al precio de lista de una agencia con locutores galegos (500-830 €) [F-sec, §3] | Casting de la semana 1 (3 presupuestos por escrito) |
| S7 | Coste de licencia de locutor: 1.000-2.500 € en el plan B; 2.000-6.000 € + 5-15 % en la Etapa 3 | Casting (§7.2, §8.3) |
| S8 | Las métricas de ASR y de señal detectan la mayoría de los fallos gruesos | Comparar las marcas automáticas con las molestias anotadas en R2 (tasa de acierto) |
| S9 | **Probabilidad de que ninguna voz sintética pase la Puerta V hoy: 60-80 %** | Lo resuelve R3. Si se confirma, el plan de negocio pasa al escenario "plan B" (§8.1) o "esperar" |
| S11 | Se pueden reclutar 20-24 nativos sin relación con los narradores en ~1-2 semanas (familia, amigos, diáspora) [S] | Si a las 2 semanas hay < 20 válidos, se amplía el plazo; **no se analiza con menos** |
| S12 | Los supuestos de la simulación de potencia (tasa base de "IA" del 40 %, heterogeneidad de oyentes) son razonables | Se vuelve a correr `sim/regla_final.py` con los datos de R1 antes de sellar el prerregistro |
| S10 | El techo de ~8 kHz de Nós no se nota en los dispositivos reales tras la cadena común | Desglose por dispositivo en R3 (§7.7) |
| S13 | El método de §5B (mejor de N, modelo de pausas) mejora la voz de forma audible frente a una toma única | Comparación F/M en R1-R3; la mejora del "mejor de N" se ve en R4 frente al kit. Sin datos previos [S] |
| S14 | La tasa de bloques defectuosos **a la entrada de la escucha**, estimada contra la verdad de referencia (profesional + casa, captura-recaptura), baja a *p̂* ≤ 3 % en ~6 episodios, lo que permite el muestreo en la Etapa 2 | `defectos.csv` y `sensibilidad.csv` de la Etapa 1. Si no baja, la Etapa 2 mantiene la escucha completa y hay que recortar la cadencia a 3 episodios/mes |
| S15 | Algún narrador galego acepta las opciones T1/T2 al precio de §5B.4, por debajo de la referencia UVA | Casting de la semana 1. Si nadie las acepta, desaparece la vía (c) |
| S16 | Un *fine-tune* con 30-60 min desde un modelo de un solo locutor funciona en StyleTTS2-GL (probabilidad de aprobar la Puerta V: 30-50 %) | Primera ejecución de (c); no hay precedente publicado en galego [?] |
| S17 | Al menos uno de los dos revisores de la casa llega al umbral de la prueba sembrada (≥ 90 % en graves y ≥ 70 % en leves) a 1× o a 1,25×, y lo mantiene en las pruebas trimestrales [S] | Prueba sembrada de las semanas 6-7. Si nadie valida: escucha en pareja (≈ doble de horas) o el profesional en cada episodio (Etapa 1 a 1 episodio/mes) |
| S18 | El revisor profesional cuesta 20-35 €/h [S; ancla española implícita de 15-21 €/h, sin fuente gallega] | 3 presupuestos en la semana 1; prueba de estrés a 50 €/h en §5B.3.2 |
| P1 | ¿Voz masculina o femenina? No se decide a priori: lo decide la escala C. En el género "sleep" en inglés predominan las voces masculinas graves (History Time, History at Night) [MED] `research/formato.md`, pero no hay datos del galego. **Resuelto en la v3:** se graban un hombre y una mujer (H1, H2), así que siempre hay un control del mismo género que la candidata; el H3 opcional refuerza el de la finalista | R2 → H3 |
| P2 | ¿Se puede ajustar Nós StyleTTS2 con una referencia de estilo "susurrada" o "íntima"? | Experimento técnico en la semana 1 [?] |
| **Q1 (para el promotor)** | ¿Se aprueba la **excepción única de ~850-1.500 €**, aunque rompa el "< 50 €/mes"? Incluye dos narradores (H1 y H2, 600-1.000 €) y el **revisor lingüístico profesional** de la prueba sembrada y los episodios 1-6 (~250-500 €). ¿Y los +300-500 € opcionales de H3 (techo total de ~2.050 € con el sorteo)? Si no se aprueba entera: variante mínima de los narradores (≈ 400-700 €, §3) **manteniendo el profesional**. **Sin un segundo humano no hay control positivo, y un suspenso no sería fiable como base para gastar los 1.000-2.500 € del plan B. Sin el profesional, la corrección galega de lo publicado no tiene un juez calibrado** | Decisión del promotor antes de la semana 1 |
| **Q2 (para el promotor)** | Si ninguna voz pasa la Puerta V, ¿en qué orden prefiere (c) la vía intermedia (~700-1.250 € hasta saber si funciona), (a) esperar sin publicar o (b) adelantar el locutor con licencia completa (1.000-2.500 €)? Recomendación: (c) → (a) o (b). Conviene decidirlo **antes** de ver los resultados, para no rebajar el listón a posteriori | Decisión del promotor antes de R1 |
| **Q3 (para el promotor)** | ¿Se autoriza firmar las **opciones T1/T2** en el contrato de H1/H2 (prima de 0-50 € por narrador ahora; T1 de ~330-650 € y T2 de 300-600 € + 10-15 % solo si se ejercen)? ¿Y **quiénes se presentan a la prueba de defectos sembrados** para firmar la escucha de cada episodio (él, su mujer o los dos), sabiendo que, si nadie valida, la alternativa es escuchar en pareja o pagar al profesional cada episodio y bajar a 1 episodio al mes? | Decisión del promotor antes del casting (semana 1) |

---

## 12. Fuentes principales (consultadas el 29-09-2026)

- Proxecto Nós, modelos TTS: https://huggingface.co/proxectonos/Nos_StyleTTS2-Brais-GL · https://huggingface.co/proxectonos/Nos_StyleTTS2-Celtia-GL · https://huggingface.co/proxectonos/Nos_TTS-sabela-vits-phonemes · https://huggingface.co/proxectonos/Nos_TTS-icia-vits-phonemes · https://huggingface.co/proxectonos/Nos_TTS-iago-vits-phonemes · https://huggingface.co/proxectonos/Nos_TTS-paulo-vits-phonemes · https://huggingface.co/api/models?author=proxectonos · https://github.com/gas/pronunza-tts-galego-onnx-colab
- Proxecto Nós, *datasets* (locutores, horas, 16 kHz, términos): https://huggingface.co/datasets/proxectonos/Nos_Brais-GL · https://huggingface.co/datasets/proxectonos/Nos_Celtia-GL
- Proxecto Nós, ASR: https://huggingface.co/proxectonos/w2v-bert-2.0-gl · https://huggingface.co/proxectonos/Nos_ASR-wav2vec2-large-xlsr-53-gl-with-lm
- Microsoft Azure: https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts · https://learn.microsoft.com/en-us/dotnet/api/microsoft.cognitiveservices.speech.speechsynthesisoutputformat · https://prices.azure.com/api/retail/prices · https://azure.microsoft.com/en-us/pricing/details/speech/ · Clipchamp: https://learn.microsoft.com/en-us/answers/questions/5779941/permissions-to-use-clipchamp-ai-text-to-voice-for · edge-tts: https://github.com/rany2/edge-tts
- Google: https://docs.cloud.google.com/text-to-speech/docs/gemini-tts · https://cloud.google.com/text-to-speech/pricing
- ElevenLabs: https://elevenlabs.io/docs/overview/models · https://elevenlabs.io/pricing/api · https://elevenlabs.io/pricing · https://elevenlabs.io/docs/eleven-creative/voices/payouts
- OpenAI TTS: https://developers.openai.com/api/docs/guides/text-to-speech
- MUSHRA / webMUSHRA: https://en.wikipedia.org/wiki/MUSHRA · https://openresearchsoftware.metajnl.com/articles/10.5334/jors.187
- Cálculos propios de potencia (reproducibles, sin fuente externa): `sim/regla_final.py`, `sim/potencia_ident_v2.py`, `sim/extremo.py`, `sim/v2_real.py` (carpeta `scratchpad/gauntlet/sim/`). Métodos estadísticos (exactitud equilibrada, *bootstrap* por oyente, prueba de signos, modelo logístico mixto con `lme4::glmer`): práctica estándar [S], sin fuente citada en esta pieza.
- Método de producción (§5B): StyleTTS2, *fine-tune* oficial (1 h de audio, ~4 h en 4 A100) y demo de síntesis larga con estilo encadenado (`LFinference`, `s_prev`, `t`): https://github.com/yl4579/StyleTTS2 · https://github.com/yl4579/StyleTTS2/blob/main/Demo/Inference_LibriTTS.ipynb · UTMOSv2: https://github.com/sarulab-speech/UTMOSv2 · ElevenLabs, parámetros de continuidad (`previous_text`, `next_text`, `previous_request_ids`, `seed`): https://elevenlabs.io/docs/api-reference/text-to-speech/convert · ElevenLabs PVC (duración recomendada y verificación): https://elevenlabs.io/docs/product-guides/voices/voice-cloning/professional-voice-cloning · Precios de GPU: https://www.runpod.io/pricing · Referencia de horas de corrección ("10 000 palabras: 7-10 h"; "tarifa media de 0,015 EUR por palabra"): https://correccionencastellano.com/tarifas-correccion-textos/ · Muestreo de aceptación: cálculo propio `sim/muestreo_aceptacion.py` (v4; su AOQL tenía el error de §5B.3.4) y **`sim/muestreo_deteccion.py` (v5: AOQ con sensibilidad imperfecta del revisor, plan mixto profesional + casa, característica operativa de la prueba sembrada con Clopper-Pearson)**; las reglas de cambio se inspiran en ISO 2859-1 [S, norma no consultada]; captura-recaptura (estimador de Chapman): práctica estándar [S], sin fuente citada
- Whisper en galego: https://huggingface.co/mozilla-ai/whisper-large-v3-gl · https://arxiv.org/abs/2503.23542 · https://github.com/m-bain/whisperx
- Pronunciación de referencia: https://ilg.usc.es/pronuncia/
- Tarifas de locución y narración: https://www.cronoshare.com/cuanto-cuesta/locucion (genérica de España) · https://voicebros.com/en/voice-over-rates · **Escena Digital, tarifas generales (audiolibro 450 € por 2.000 palabras, descuentos del 20-40 %, casting 200 €), abierta el 29-09-2026: https://www.locutortv.es/presupuestos_y_tarifas.htm** · su catálogo de locutores galegos: https://www.locutortv.es/locutores_gallegos-locutor.htm · directorios que **no publican precios** (abiertos el 29-09-2026): https://tragoratraducciones.com/locutores-gallegos/ · https://anyvoz.com/locutores-gallegos/
- Revisor lingüístico: directorio de profesionales de la AGPTI (sin tarifas publicadas): https://www.agpti.org/ · ancla de horas y precio de corrección (castellano): https://correccionencastellano.com/tarifas-correccion-textos/ · **Tarifa gallega de corrección de locución o asesoría lingüística de dobraxe: no encontrada [?]** (pendiente para la semana 1)
- Sector y reputación: https://www.nosdiario.gal/articulo/social/mesa-agpti-ada-denuncian-incumprimentos-rtve-coa-programacion-galego/20260220110723248001.html · https://escueladedoblajedemadrid.es/blog/alerta-maxima-ante-la-cesion-de-voz-para-aprendizaje-neuronal-de-la-ia-segun-uva/ · https://www.milenio.com/negocios/que-debe-contener-un-contrato-para-licenciar-una-voz-a-ia
- *Glitches* en canales IA: https://www.404media.co/ai-generated-boring-history-videos-are-flooding-youtube-and-drowning-out-real-history/
