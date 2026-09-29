# Pieza del business plan: PRODUCTO — formato "historia para durmir" en galego

Versión 4 (constructor, ronda 4) · 29-09-2026 · Redactado en castellano; todo lo que se dirige al público va en galego normativo (RAG).

**Cambios respecto a la v3:**
1. **Empaquetado ejecutable.** La §7.3 pasa de 4 viñetas a una **plantilla de miniatura con medidas**: lienzo, rejilla, posición y tamaño de cada texto en píxeles, contraste mínimo, zonas prohibidas (sello de duración, barra de progreso, iconos) y una prueba de legibilidad a tamaño de móvil. La plantilla se ha **maquetado y medido de verdad** sobre un fondo de prueba (§7.3.4).
2. **Miniatura del Episodio 1** con motivo, prompt completo, texto y **3 variantes para el test A/B** (nueva §11.9), con protocolo previo sin tráfico y test en YouTube "Probar y comparar". Entra en el checklist de salida (ahora §11.10).
3. **Ritmo coherente.** El brief de la voz (§3A.1) pedía 120-135 palabras/min de habla, pero la tabla de §3A.3 implicaba ~143. Se corrige el brief a **130-145 en los actos I-II y 125-140 en el III**, que es lo que se deduce de 115 percibidas con ~20 % de silencio, y la tabla muestra ahora el ritmo de habla implícito de cada bloque.
4. **"Hermerico" no es una trampa castellana.** En castellano también es llana y sin tilde (es.wikipedia, RAH). El riesgo real es otro: circula una forma popular esdrújula, *Hermérico* (§3A.4).
5. **Lista cerrada de las 30 palabras puntuables de M2**, con la pronunciación esperada de cada una, la hoja de puntuación y la regla de acuerdo entre jueces. El umbral ≥27/30 ya es reproducible (§3A.1.2).
6. **§11.6 sin mezcla de normas.** Se quitan las formas "terceira feira, cuarta feira", que no son ni portuguesas (*terça-feira*, *quarta-feira*) ni galegas del DRAG. El texto dice ahora que al otro lado del Miño los días se cuentan por números, sin nombrar las formas portuguesas.

**Cambios de la v3 respecto a la v2:** (1) nueva **§3A, especificación ejecutable de la voz y del render**: brief del narrador con referencias de escucha con marca de tiempo y descalificaciones (§3A.1); receta de render frase a frase para StyleTTS2, VITS y Matcha de Nós, con el parámetro real de velocidad de cada motor verificado en su código y un audio de referencia "tranquilo" (§3A.2); fórmula y valores de pausas y velocidad por acto, con el Acto III un ~10 % más lento (§3A.3); léxico de pronunciación con sustitución automática en el front-end Cotovía (§3A.4); (2) se corrige la v2, que decía que el ritmo se ajustaba con "la velocidad del motor": los modelos de Nós no aceptan SSML y StyleTTS2 no expone la velocidad; (3) la fecha del SPP en España se cita ya de la fuente primaria que la da (Infobae/Europa Press), no de TechCrunch (§9.1).

**Cambios de la v2 respecto a la v1:** (1) nueva **§11, hoja de producción del Episodio 1** (*O Reino suevo de Gallaecia*): 10 capítulos con minutado, presupuesto de palabras, activación y fuentes; 74 planos con prompts; ~600 palabras de prosa del Acto II y ~300 del Acto III; título, descripción completa y comentario fijado; (2) la promesa del canal ya no dice "sen cortes" (§2); (3) el catálogo lleva las puntuaciones D/Dem/Fx/R calculadas y está **reordenado por esa puntuación** (§8); (4) §9 separa lo que el Spotify Partner Program paga al audio y al vídeo, verificado en la página oficial de Spotify.

**Leyenda de evidencia**
- **[F]** dato con fuente (URL al lado o en §13).
- **[MED]** medido sobre datos reales en la investigación previa (`research/formato.md`, yt-dlp y storyboards de YouTube, 29-09-2026).
- **[COMP]** comprobación hecha para esta pieza el 29-09-2026 (curl a YouTube, RDAP de dominios, iTunes Search API, Dicionario da RAG, Galipedia en bruto).
- **[S]** supuesto o decisión de diseño propia. Se valida en las pruebas o en la Etapa 1.

---

## 0. Resumen: las decisiones de producto en 15 líneas

1. **Listón elegido:** *History at Night*, "The Great Maya Collapse" (https://www.youtube.com/watch?v=hbufma0ZlUw). Mismo modelo de producción que el nuestro (IA dirigida por humano), 1,16 M de vistas con 47 min [MED]. El techo (no el listón) es *History Time*, "After Rome" (§1).
2. **Promesa del canal:** "A historia de Galicia contada amodo, nun galego coidado, para que te deixes levar ata o sono. Sen sustos e sen présa." El "sen cortes" **no** forma parte de la promesa del canal: es una etiqueta por vídeo que solo llevan los vídeos sin mid-rolls (regla 13) (§2).
3. **Duración:** 75 min en la Etapa 1 (rango 60-90) y 2 h en la Etapa 2, más 20-30 min de cola de ambiente sin voz (§3).
4. **Ritmo:** 110-125 palabras/min "percibidas" (con pausas incluidas), unas 8.400-8.600 palabras por episodio de 75 min [S sobre MED] (§3). Se consigue con silencios insertados frase a frase (~20 % del tiempo) y un estiramiento de duraciones ≤10 % (≤15 % en el Acto III), nunca con SSML, que Nós no admite (§3A.3). Eso implica un habla de 130-145 palabras/min sin contar los silencios (125-140 en el Acto III).
5. **Estructura en tres actos con tensión decreciente:** el conflicto solo en el primer 35-40 %, luego vida cotidiana y paisaje, y un desenlace que "se apaga" con frases más largas, sin fechas y con la imagen cada vez más oscura (§4).
6. **"Sono seguro":** 14 reglas medibles. Sin llamada a suscribirse en la voz, sin picos de volumen, sin mid-rolls después del minuto 20 y la cola de ambiente como colchón ante el anuncio final (§5).
7. **Paisaje sonoro galego** grabado por el propio promotor en lo posible (chuvia en lousa, ría en calma, lareira suavizada, río, carballeira), para evitar reclamaciones de Content ID (§6).
8. **Identidad visual "noite atlántica":** pintura al óleo IA oscura (luminancia 40-70/255), una imagen cada 40-90 s y el último tercio casi en negro, con una plantilla de prompt fija (§7).
9. **Miniatura con plantilla medida (§7.3):** texto en la columna izquierda (etiqueta, título de ≤2 líneas con 104 px de altura de mayúscula sobre 1280×720, fechas en color candea), motivo con una sola luz cálida a la derecha, esquina inferior derecha vacía para el sello de duración y contraste ≥7:1 en el título. La del Ep. 1 tiene 3 variantes de motivo para el test A/B (§11.9).
10. **Catálogo:** 30 temas puntuados con P = 2·D + Dem + Fx − R y ordenados por la prioridad de lanzamiento L = P + Dem. Los 4 primeros: Reino suevo, Camiño do s. XII, aldea del s. XV y castro. Hay además una lista de temas excluidos (§8).
11. **Derivados:** videopódcast en Spotify (la única vía al ingreso Premium del SPP, que llega a España el 20-10-2026 según Infobae/Europa Press, §9.1), feed de audio (Apple, iVoox; en Spotify el audio solo cobra publicidad), "postais" verticales de 60-90 s y capítulos sueltos. En la Etapa 2-3, compilaciones y pistas de audio es/pt (§9).
12. **Nombre recomendado: "Serán · Historia de Galicia para durmir"** (@seran libre en YouTube, seran.gal libre). Alternativas: "Á Luz do Candil" y "Historia para Durmir" (§10).
13. **Episodio 1 listo para producir:** hoja de producción de *O Reino suevo de Gallaecia (411-585)* con escaleta, fuentes por capítulo, 74 planos, prosa de muestra, metadatos y miniatura con 3 variantes para el test A/B (§11).
14. **Voz:** se juzga con un brief y unas descalificaciones fijos (§3A.1) y se renderiza con una receta por motor (§3A.2). La pronunciación se corrige con un léxico que se aplica automáticamente dentro de Cotovía (§3A.4) y se examina con una lista cerrada de 30 palabras trampa (§3A.1.2).
15. Todo lo marcado [S] se convierte en hipótesis medibles con puertas de decisión (§12).

---

## 1. La referencia: qué vídeo real es el listón y por qué

### 1.1 Candidatas evaluadas

| Papel | Vídeo | Datos [MED] | Encaje con nuestro producto |
|---|---|---|---|
| **LISTÓN (elegido)** | History at Night, "The Great Maya Collapse" · https://www.youtube.com/watch?v=hbufma0ZlUw | 1,16 M de vistas; 47 min; 157 palabras/min; 13 capítulos (mediana 3,6 min); canal de 74,3K suscriptores con solo 6 vídeos (~690K de media por vídeo); "NO AD BREAKS" en la miniatura; luminancia media 86/255 y 1 imagen cada ~35 s | **Mismo modelo de producción:** guion con IA dirigido y verificado por un humano, voz clonada con licencia, imágenes IA hechas una a una y bibliografía en la descripción. Demuestra que "pocos vídeos y excelentes" funciona, que es lo que cabe en 4-10 h/semana. |
| Techo de calidad (no listón) | History Time, "After Rome – The War For Britain" · https://www.youtube.com/watch?v=sXBgNNtEJ6M | 27,9 M de vistas; 3 h 28 min; ~98 palabras/min; voz humana; apertura de escena sin CTA | Tema gemelo (reinos post-romanos de la fachada atlántica ≈ Gallaecia sueva, nuestro Episodio 1), pero con guion de autor, voz humana y 15 años de oficio. Sirve para medir la distancia, no como objetivo. |
| Referencia de mercado vecino | Relatos para Dormir, "¿Cómo era un día completo en la Edad Media?" · https://www.youtube.com/watch?v=3uBP9QaWfPM | 1,05 M de vistas con 14,4K suscriptores; 150 min; 124 palabras/min | Prueba que el formato "vida cotidiana medieval" funciona en una lengua románica. Inspira nuestro tema "aldea do século XV". |
| Anti-referencia | Sleepless Historian, "Why You Wouldn't Last a Day in Medieval Times" · https://www.youtube.com/watch?v=9jnekLeHz3c | 4,29 M de vistas; un cambio de imagen cada ≤10 s; segunda persona burlona; miniaturas grotescas | Justo lo que NO somos. Además, su rendimiento por vídeo se ha desplomado (de 2-4 M en 2025 a unas 8-31K en sep-2026, `research/retornos.md` §0.5). |

### 1.2 Por qué History at Night y no History Time
- **Es alcanzable con nuestros medios.** Igualar History Time exige un historiador-guionista y una voz humana de primera. History at Night demuestra que la combinación IA + criterio humano + voz de calidad llega al millón de vistas [MED].
- **Es comparable 1:1.** Ya existe una traducción al galego de su apertura (`refs/sleep_reference_gl.md`, bloque A). La §11.7 fija el protocolo de comparación ciega de nuestra prosa (§11.5-11.6) contra ese bloque, a igualdad de lengua.
- **Marca el estándar visual y de anuncios** que queremos: paleta apagada, Ken Burns lento, "NO AD BREAKS" como argumento.

### 1.3 En qué SUPERAMOS deliberadamente al listón (las diferencias son de diseño)
| Aspecto | History at Night | Nosotros | Motivo |
|---|---|---|---|
| Ritmo | 157 palabras/min [MED] | 110-125 | La narración humana para dormir va a 94-115 [MED]; el galego tiene palabras más largas que el inglés [S]. |
| Llamada a suscribirse | Hablada al inicio ("take a moment to like and subscribe"; en la versión galega del bloque A, "tómate un momento para darlle a «Gústame»…") | **Ninguna en la voz**; solo en texto (descripción y comentario fijado, §11.8) | Coherencia con el "sono seguro" y diferenciación frente a la plantilla compartida de los canales IA [MED: la misma frase en 3 canales]. |
| Luminancia | 86/255 | 40-70, y <20 en el desenlace | El más "dormible" medido es Sleepy History Channel, con 34 [MED]. |
| Curva | Arco documental completo, el conflicto hasta la mitad | Conflicto concentrado en el primer 35-40 % | Regla de la guionista de Calm: "If there's any action, it has to start in the beginning" [F] (Slate, §13). |
| Transparencia | Bibliografía en la descripción | Bibliografía **y** una "Nota sobre o proceso" que explica qué hizo la IA y qué revisó una persona (§11.8) | La comunidad galega castiga el error; declarar el proceso y ofrecer corrección pública convierte la crítica en colaboración [S]. |

### 1.4 Advertencia sobre el listón
History at Night no publica desde el 29-01-2026 (6 vídeos en total) [MED]. No sabemos si es por economía, por agotamiento o por política de YouTube. **Tomamos su producto, no su modelo de cadencia.** Riesgo que debe revisar la pieza de riesgos.

---

## 2. Promesa del producto

**Promesa del canal, en galego (cabecera, descripción del canal y tráiler)** — [S], pendiente de revisión lingüística:
> *A historia de Galicia contada amodo, nun galego coidado, para que te deixes levar ata o sono. Sen sustos e sen présa. Cada noite, un serán.*

**Qué NO dice la promesa del canal, y por qué:** no dice "sen cortes publicitarios". En la Etapa 2 se probarán 0-2 mid-rolls en los primeros 20 minutos (regla 12), así que prometerlo a nivel de canal sería falso. "Sen cortes" es **una etiqueta por vídeo** (título, miniatura, primera línea de la descripción) que solo llevan los vídeos que de verdad no tienen mid-rolls (regla 13). Todos los episodios de la Etapa 1 la llevan, porque el canal aún no estará en el YPP y no hay anuncios de ningún tipo.

**En castellano (posicionamiento interno):**
- **Para quién:** adulto galegofalante o que entiende el galego, de 35 a 70 años, que ya escucha radio o pódcast para dormirse. Es el perfil más cercano al oyente de Radio Galega/TVG, donde el uso mayoritario del galego es 4-5 veces mayor que en el audiovisual online (`research/audiencia.md` §2.4 [F, IGE]).
- **Qué tarea resuelve:** dormirse sin pantalla estimulante y "aprender algo sin esforzarse"; oír el galego bien hablado de noche.
- **Diferencial:** (1) la única propuesta de este tipo en galego (no se encontró ningún competidor directo, `audiencia.md` §5 [COMP previo]); (2) rigor verificable (bibliografía por episodio y corrección pública de errores); (3) galego normativo cuidado y pronunciación nativa; (4) "sono seguro" como estándar explícito.
- **Qué NO promete:** efectos terapéuticos. La Sociedad Española de Neurología alerta sobre los productos para el insomnio "sin validez médica" [F] (`audiencia.md` §6.2). Nunca se dice "cura o insomnio"; se dice "para acompañar o sono".

---

## 3. Duración, ritmo y volumen de guion

| Parámetro | Etapa 1 (piloto) | Etapa 2 | Base |
|---|---|---|---|
| Duración narrada | **75 min** (rango 60-90) | **2 h** | El núcleo del género está en 1 h 15 min - 2 h 30 min; History at Night triunfa con 47-76 min [MED]. En la Etapa 1 manda el coste de revisar el galego [S]. |
| Cola de ambiente sin voz | 20-30 min | 30-45 min | Colchón para que el anuncio final llegue con el oyente ya dormido (§5), más watch time sin coste de guion [S]. |
| Ritmo "percibido" (silencios incluidos) | **110-125 palabras/min** (objetivo 115) | igual | Voz humana para dormir: 94-115 [MED]; blog del sector: 100-130 [F débil, otherworldtales]. |
| Palabras por episodio | ~8.400-8.600 (75 × 112-115); el Ep. 1 presupuesta 8.435 (§11.2) | ~13.800 (120 × 115) | Cálculo [S]. |
| Caracteres (para el coste de TTS) | ~53.000 | ~85.000 | ~6,2 caracteres por palabra en galego (`voz_guion.md` §1.8 [S]). |
| Capítulos | 8-10, de 5-12 min | 12-16, de 7-9 min | Mediana observada: 3,6-17 min [MED]. |
| Pausas | Insertadas por el renderizador, calculadas por acto con la fórmula de §3A.3. **Suelo:** 0,7 s entre frases, 2 s entre párrafos y 6-8 s de solo ambiente entre capítulos. **Valores del Ep. 1 con r_nat = 150:** 1,4-1,45 s / 3,9-4,1 s / 7 s en los actos I-II, y 1,9 s / 5,4 s / 8 s en el III | igual | `formato.md` §3.2 y §3A.3 [S]. |
| Cadencia | 1 episodio cada 2 semanas | 1 por semana más 1 compilación al mes | `formato.md` §3.9 y la política de "inauthentic content" (`retornos.md` §6) [S]. |

**Cómo se mide el ritmo en la QA [S]:** palabras del guion final ÷ duración del audio narrado (sin la cola), por acto, con una tolerancia de ±5 % sobre el objetivo. Si falla, se corrigen primero las pausas insertadas y después el parámetro de duración del motor (`DUR_SCALE` parcheado en StyleTTS2, `length_scale` en VITS, `speaking_rate` en Matcha), dentro de sus topes. Si ni así cuadra, se recorta el guion. Los modelos de Nós no tienen SSML ni un control de velocidad "de fábrica" en StyleTTS2: la receta completa está en §3A.2-3A.3. El Acto III va a ~105 (−9 %): +5 % de estiramiento y +35 % de pausa.

## 3A. La voz y el render de audio: especificación ejecutable

En este formato el audio es casi todo el producto (§6.1), y la voz es la parte más difícil. Esta sección convierte las reglas de ritmo (§3), estructura (§4) y "sono seguro" (§5) en tres cosas ejecutables:
1. un **brief del narrador** para juzgar el kit A/B;
2. una **receta de render** para cada motor candidato de Nós;
3. un **léxico de pronunciación** que sustituye automáticamente las formas problemáticas.

**Corrección respecto a la v2.** En la v2 se decía que el ritmo se ajustaba con "la velocidad del motor TTS". Para los modelos elegidos eso era falso. Los modelos de Nós **no aceptan SSML**: no hay `<break>` ni `<prosody rate>`. Además, el CLI de StyleTTS2 **no expone la velocidad**. Lo que sí existe, verificado en el código publicado el 29-09-2026, es lo siguiente:

| Motor (Nós) | Palanca de velocidad real | Palanca de estilo | Pausas | Base |
|---|---|---|---|---|
| **StyleTTS2** (Brais, Celtia) | Ninguna en el CLI. Hay que parchear una línea de `inference.py`: `pred_dur = torch.round(duration.squeeze()).clamp(min=1)` pasa a `torch.round(duration.squeeze() * DUR_SCALE).clamp(min=1)` | Un **audio de referencia** (`normal_reference` en `Configs/inference_config.yml`) mezclado con el estilo generado mediante `alpha` (timbre) y `beta` (prosodia). Cuanto más bajo el valor, más pesa la referencia | El script divide por `. : ? !` y **concatena sin silencio** (`np.concatenate(wavs)`) | [COMP] https://huggingface.co/proxectonos/Nos_StyleTTS2-Brais-GL (README, `inference.py`, `Configs/inference_config.yml`) |
| **VITS** (Sabela-Nós, Brais, Celtia, Icía, Iago, Paulo), vía Coqui TTS | `length_scale` (1 por defecto; >1 = más lento). Coqui multiplica con él las duraciones predichas (`w = torch.exp(logw) * x_mask * self.length_scale`) | No hay audio de referencia. Solo `inference_noise_scale` (0,667 por defecto) e `inference_noise_scale_dp` (1,0 por defecto; variabilidad de las duraciones) | Ninguna: `synthesizer.tts(texto)` devuelve una sola onda | [COMP] https://github.com/coqui-ai/TTS/blob/dev/TTS/tts/models/vits.py ; uso en Nós: https://huggingface.co/proxectonos/Nos_TTS-brais-vits-phonemes |
| **Matcha** (Icía, Celtia, Brais) | `--speaking_rate`, que el CLI pasa como `length_scale` (>1 = más lento) | `--temperature` (0,667 por defecto) | Ninguna | [COMP] https://github.com/shivammehta25/Matcha-TTS/blob/main/matcha/cli.py ; https://huggingface.co/proxectonos/Nos_TTS-icia-extended-matcha-phonemes |

**Consecuencia de diseño.** Todos los motores se envuelven en un **renderizador propio, frase a frase**, que:
- inserta silencios exactos (el único control de pausa que existe);
- aplica la velocidad con el parámetro de duración de cada motor;
- pasa el texto por un **G2P con léxico de excepciones** antes de sintetizar.

El guion no lleva marcas de SSML. Lleva una estructura simple: `##` marca un capítulo, una línea en blanco marca un párrafo y cada frase termina en `.`.

---

### 3A.1 Brief del narrador (con esto se juzga el kit A/B)

**Persona (en una línea):** *unha persoa adulta que conta ao pé da lareira, non unha que le en voz alta.* Es el "contador de serán", no el locutor de telediario, ni el maestro que dicta, ni el susurrador de ASMR.

| Dimensión | Objetivo | Cómo se mide |
|---|---|---|
| Registro | Narrativo y cálido, con energía baja y constante. Intimidad sin susurro. Cero "sonrisa de anuncio" | Escucha ciega (rúbrica de §3A.1.3) |
| Tono (F0), voz masculina | Mediana de 95-120 Hz; rango P10-P90 de un párrafo **≤ 6 semitonos** y **≥ 2** (por debajo de 2 suena robótico) [S] | `librosa.pyin` sobre la muestra M1 |
| Tono (F0), voz femenina | Mediana de 165-205 Hz; mismo rango en semitonos [S] | Ídem |
| Timbre | Grave-medio, cercano ("micrófono próximo") y sin brillo sibilante. Encaja con la regla 4 (de-esser, atenuación por encima de 8-10 kHz) | Escucha, más la energía por encima de 8 kHz comparada con la media del kit |
| Final de frase declarativa | Descendente. Nada de subidas sistemáticas en cada coma o final de frase | Escucha, más la pendiente de F0 en los últimos 500 ms de cada frase |
| Ritmo del habla (sin silencios) | **130-145 palabras/min en los actos I-II y 125-140 en el III.** Es una consecuencia, no un objetivo aparte: con 115 percibidas y ~20 % de silencio, el habla sale a 115 ÷ 0,8 ≈ 144; con el tope de silencio más bajo (~12 %), a ~130. El valor exacto es r_nat ÷ V (§3A.3; con r_nat = 150 y V = 1,05, **~143**). Una voz que necesite >145 para cuadrar el tiempo se considera rápida y va al recorte de guion o a otra voz | Palabras ÷ duración del audio sin silencios insertados |
| Galego | Pronunciación nativa estándar: vocales medias abiertas y cerradas distintas, `x` = [ʃ], nasal velar en *unha* [ˈuŋa], sin entonación castellana | Frases trampa M2 (§3A.1.2) y léxico (§3A.4) |

#### 3A.1.1 Referencias de escucha, con marca de tiempo

Antes de puntuar, el jurado escucha estos fragmentos para calibrar el oído. Los ritmos son [MED] sobre los subtítulos automáticos de YouTube (`en`), descargados con yt-dlp el 29-09-2026.

| Ref. | Fragmento | Qué se toma | Qué NO se toma |
|---|---|---|---|
| **R1: cadencia de la entrada** | History Time, "After Rome", **0:00-2:50** (https://www.youtube.com/watch?v=sXBgNNtEJ6M&t=0s): "Stainmore, Northern England, a land of open skies, desolate hills… ruins of the old world" hasta "…much longer for an empire of comparable power to arise." | Escena de lugar antes de cualquier dato; **98 palabras/min** [MED]; frases cortas separadas por silencios largos, con un interludio de ~16 s entre 1:07 y 1:23 [MED, hueco entre subtítulos] | La música de interludio a volumen alto |
| **R2: tono del desenlace (Acto III)** | History Time, "After Rome", **3:25:13-3:26:05** (https://www.youtube.com/watch?v=sXBgNNtEJ6M&t=12313s): "Place names today in Cumbria still bear testimony…" hasta "…the British rulers who once held sway." | Es literalmente nuestro capítulo 9 ("o que quedou": topónimos y lengua que sobreviven). **87 palabras/min** [MED]. Se apaga sin cerrar con una fecha | La CTA que viene justo después (3:26:13 en adelante) |
| **R3: timbre del listón (voz clonada con licencia)** | History at Night, "The Great Maya Collapse", **1:42-2:50** (https://www.youtube.com/watch?v=hbufma0ZlUw&t=102s): "And now, settle in. Let the noise of the modern world fade away…" | El timbre grave y próximo, la declinación suave y la ausencia de artefactos en una voz IA | **La velocidad: 163 palabras/min** [MED], demasiado rápida para nuestro formato (§1.3). Este vídeo tiene **0 pausas ≥8 s en 47 min** frente a **114 en History Time** (207 min) [MED, proxy: huecos ≥8 s entre subtítulos, que incluyen interludios musicales] |
| **R4: galego nativo humano** | *Pendiente:* el promotor elige 60 s de un locutor o locutora galegos nativos en registro narrativo tranquilo (un audiolibro, un programa nocturno de la Radio Galega) y anota la URL y el minuto | La referencia de "así suena el galego de verdad" para el criterio de lengua | – |

#### 3A.1.2 Material del kit (el mismo texto para todas las voces)
- **M1: cuerpo (≈2 min).** Las primeras ~250 palabras de §11.5, renderizadas con los ajustes del Acto II.
- **M2: frases trampa (≈1 min).** Diez frases que concentran las palabras trampa y los nombres del Ep. 1. Es un borrador [S] que revisa el lingüista antes de usarlo:
  1. *A pedra do muro está fría, e a xente pasa ao pé dela sen mirar.*
  2. *O home novo chegou de noite; a nova casa quedaba lonxe da fonte.*
  3. *Chove sobre a terra, e a néboa non levanta en todo o día.*
  4. *Os monxes vellos gardaban unha candea enriba dunha mesa de carballo.*
  5. *O río leva a auga cara ao mar, e todo queda en silencio.*
  6. *Hidacio escribiu en Chaves; Martiño viviu en Dumio, preto de Braga.*
  7. *Hermerico, Requiario e Leovixildo foron reis, e o Órbigo é un río.*
  8. *Ninguén lembra ben por que; faise, sen máis, coma quen saúda.*
  9. *Nos portos novos descansaban os corpos cansos dos mariñeiros.*
  10. *A voz de nós volve cada noite coa chuvia.*

  **Lista cerrada de las 30 palabras puntuables de M2 (v1) [S, pendiente de la marca `verificado` del lingüista].** Las 10 frases contienen más palabras con alguna dificultad (unas 35), pero **solo estas 30 puntúan**. El resto (Hidacio, Chaves, Martiño, Dumio, Braga, Requiario, *queda*, *lembra*, *preto*, *mesa*…) se escucha pero no cuenta en (e): o no discriminan entre un galego nativo y uno castellanizado (*Chaves*, *Martiño*, la *r* inicial de *Requiario* suenan igual en castellano), o su pronunciación está marcada ⚠ en el léxico y el resultado no sería reproducible.

  | # | Frase | Palabra | Esperado (IPA) | Fonemas Nós | Qué se escucha (error típico) |
  |---|---|---|---|---|---|
  | 1 | 1 | pedra | [ˈpɛðɾa] | `pÉDra` | *e* abierta (error: cerrada) |
  | 2 | 1 | xente | [ˈʃɛnte] | `SÉnte` | *x* = [ʃ] **y** *e* abierta; si falla una de las dos, 0 |
  | 3 | 1 | pé | [ˈpɛ] | `pÉ` | *e* abierta |
  | 4 | 2 | home | [ˈɔme] | `Óme` | *o* abierta |
  | 5 | 2 | novo | [ˈnoβo] | `nóBo` | *o* cerrada (metafonía: contrasta con 7) |
  | 6 | 2 | noite | [ˈnojte] | `nójte` | *o* cerrada (error: abrirla) |
  | 7 | 2 | nova | [ˈnɔβa] | `nÓBa` | *o* abierta |
  | 8 | 2 | lonxe | [ˈlonʃe] | `lónSe` | *o* cerrada **y** *x* = [ʃ] |
  | 9 | 2 | fonte | [ˈfonte] | `fónte` | *o* cerrada |
  | 10 | 3 | chove | [ˈtʃɔβe] | `CÓBe` | *o* abierta |
  | 11 | 3 | terra | [ˈtɛra] | `tÉRa` | *e* abierta |
  | 12 | 3 | néboa | [ˈnɛβoa] | `nÉBoa` | *e* abierta; tres sílabas, sin diptongar *-boa* en [bwa] |
  | 13 | 4 | monxes | [ˈmonʃes] | `mónSes` | *o* cerrada **y** *x* = [ʃ] |
  | 14 | 4 | vellos | [ˈbeʎos] | `béZos` | *e* cerrada; *ll* = [ʎ] (error: yeísmo, [ʝ]) |
  | 15 | 4 | unha | [ˈuŋa] | `úNa` | nasal velar (error: [n] alveolar) |
  | 16 | 4 | dunha | [ˈduŋa] | `dúNa` | nasal velar |
  | 17 | 5 | leva | [ˈlɛβa] | `lÉBa` | *e* abierta |
  | 18 | 7 | Hermerico | [eɾmeˈɾiko] | `ermeríko` | llana y *h* muda (error: la forma popular esdrújula *Hermérico*, §3A.4) |
  | 19 | 7 | Leovixildo | [leoβiˈʃildo] | `leoBiSíldo` | *x* = [ʃ] (error: [x] del castellano *Leovigildo*) |
  | 20 | 7 | Órbigo ⚠ | [ˈɔɾβiɣo] | `ÓrBiGo` | *o* abierta. **Si el lingüista no puede fijar la abertura, se sustituye por la reserva R1** |
  | 21 | 7 | é | [ˈɛ] | `É` | verbo con *e* abierta, frente a la conjunción *e* cerrada de la misma frase |
  | 22 | 7 | un | [ˈuŋ] | `úN` | nasal velar final |
  | 23 | 8 | ninguén | [niŋˈɡeŋ] | `niNGéN` | las dos nasales velares |
  | 24 | 8 | quen | [ˈkeŋ] | `kéN` | nasal velar final |
  | 25 | 9 | portos | [ˈpɔɾtos] | `pÓrtos` | *o* abierta (metafonía del plural) |
  | 26 | 9 | novos | [ˈnɔβos] | `nÓBos` | *o* abierta (contrasta con 5) |
  | 27 | 9 | corpos | [ˈkɔɾpos] | `kÓrpos` | *o* abierta |
  | 28 | 10 | voz | [ˈbɔθ] | `bÓT` | *o* abierta |
  | 29 | 10 | nós | [ˈnɔs] | `nÓs` | *o* abierta |
  | 30 | 10 | volve | [ˈbɔlβe] | `bÓlBe` | *o* abierta |
  | R1 | 5 | todo | [ˈtoðo] | `tóDo` | *o* cerrada. Reserva, solo si se retira la n.º 20 |

  La frase 6 no tiene palabras puntuables: sirve para oír los nombres del Ep. 1 y alimentar la lista de pendientes del léxico.

  **Cómo se puntúa (reproducible):**
  1. Antes del test, el lingüista revisa las 30 filas y la reserva y las marca `verificado`. A partir de ahí la lista queda **congelada** para todo el kit: si cambia algo, se cambia antes de escuchar la primera muestra, nunca durante.
  2. Cada juez tiene una hoja impresa con las 30 palabras y su "qué se escucha". Escucha M2 de cada voz **dos veces** como máximo y marca cada palabra ✓ o ✗.
  3. Una palabra cuenta como correcta **solo si los dos jueces la marcan ✓**. Si discrepan, se escucha la frase una tercera vez juntos y se decide; si sigue la duda, cuenta como ✗.
  4. En las filas con dos rasgos (2, 8, 13, 14, 23), hay que acertar todos para tener el punto.
  5. La nota (e) es el número de ✓ (0-30). El umbral de la ganadora es **≥27/30**, con el léxico ya aplicado (§3A.4).
  6. Control automático complementario: la cadena de fonemas que el renderizador envió al motor para esas 30 palabras debe coincidir con la columna "Fonemas Nós". Si coincide y el juez oye ✗, el fallo es del **motor** (no se arregla con el léxico); si no coincide, es del **léxico** o de Cotovía.

- **M3: desenlace (≈1 min).** Los últimos ~120 palabras de §11.6, renderizadas con los ajustes del Acto III.

Todas las muestras se normalizan a **-16 LUFS** (para que no gane la más fuerte), van sin cama de ambiente, llevan nombres aleatorios y se escuchan con auriculares a volumen de noche.

#### 3A.1.3 Rúbrica y descalificaciones
- **Puntuación de 1 a 5:** (a) naturalidad galega; (b) calma ("durmiríame con isto"); (c) ausencia de artefactos; (d) timbre agradable a los 2 minutos; (e) solo en M2: acierto de pronunciación, contado sobre la **lista cerrada de 30 palabras** de §3A.1.2 con la regla de acuerdo entre jueces descrita allí.
- **Descalificación automática** si cualquiera de los dos jueces marca **dos veces** una de estas faltas en M1 o M3, sea cual sea la media:
  1. **Vocales arrastradas:** átonas estiradas, "voz de goma". Es el síntoma de un `DUR_SCALE` o un `length_scale` demasiado alto.
  2. **Tono de lectura escolar:** sílaba a sílaba, subida en cada coma, énfasis de dictado.
  3. **Pronunciación castellana:** `e`/`o` sin distinción de abertura en palabras trampa, `x` como jota, *unha* con [n] alveolar, *Leovixildo* dicho con la [x] del castellano *Leovigildo*, *ll* con yeísmo, entonación de telediario de Madrid.
  4. **Tono de locutor comercial:** energía alta, sonrisa, "venta".
  5. **Artefactos:** timbre metálico, clics entre frases, respiraciones cortadas, cambios de timbre de una frase a otra (deriva de estilo).
  6. **Susurro o ASMR:** otro género; fatiga y suena impostado.
- **Ganadora:** la de mayor media en (a)+(b) sin descalificación y con ≥27/30 en (e) **después** de aplicar el léxico (§3A.4). Si ninguna llega, se prueba la siguiente vía (Azure como control, ElevenLabs), con este mismo brief.

**Candidatas del kit (≤8 muestras, para no fatigar al jurado) [S]:**
- StyleTTS2 Brais ×2: (i) ajustes recomendados de la ficha; (ii) con la referencia REF-CALMA y `beta` 0,6.
- StyleTTS2 Celtia ×2: ídem.
- VITS Sabela-Nós.
- Matcha Icía-extended.
- VITS Brais.
- Azure Sabela como **control**: es la voz que el promotor ya probó en Clipchamp.

---

### 3A.2 Receta de render (la misma estructura para los tres motores)

**Paso 0: calibración (una vez por voz, ~30 min).** Se renderiza M1 con `DUR_SCALE`/`length_scale` = 1,00 y **sin** silencios insertados. Se mide la duración y se calcula **r_nat** = palabras ÷ minutos. Es el ritmo natural de esa voz; se desconoce hasta medirlo [S]. Todo lo demás se deriva de r_nat con la fórmula de §3A.3.

**Pipeline por frase (pseudocódigo del `render_nos.py` propio):**

```
para cada capítulo c, párrafo p, frase f del guion:
    fon = g2p_con_lexico(f)                      # §3A.4: Cotovía + sustitución automática
    seed = hash(id_frase) ; torch.manual_seed(seed) # reproducible: se puede re-renderizar 1 frase
    wav = motor.sintetiza(fon, velocidad = V[acto], estilo = E[acto], s_prev)   # ver tabla
    wav = recorta_silencios(wav, top_db=40) ; fundido de 15 ms de entrada y salida   # evita clics (regla 5)
    añade wav + silencio(P_frase[acto])          # o P_parrafo si es la última frase del párrafo
    al terminar el capítulo: silencio(P_cap[acto]) y sello de zanfona debajo (§6.2)
guarda por frase: wav, seed, s_pred (StyleTTS2) → la QA vuelve a renderizar solo las frases marcadas
```

**Parámetros por motor [S, punto de partida del kit; se afinan con el jurado]:**

| Motor | Velocidad | Estilo y estabilidad | Notas de implementación |
|---|---|---|---|
| StyleTTS2 Brais/Celtia | `DUR_SCALE` (parche de 1 línea) | `alpha` 0,6 (ficha); `beta` **0,6** con REF-CALMA frente a 1,0 de la ficha (más peso de la referencia tranquila en la prosodia); `t` **0,6** (continuidad de estilo entre frases, recomendado en la ficha); `diffusion_steps` 10; `embedding_scale` 1,0 | (1) En `inference_config.yml` corregir las rutas: el config apunta a `Models/galician/brais_final/…`, pero en el repositorio el fichero está en `Models/galician/brais/epoch_2nd_00057.pth` [COMP, listado de ficheros de HF]. (2) **Forzar `normal_reference` para todas las frases**: el guion no debería tener `?` ni `!`, pero si los tiene no se usan las referencias interrogativa y exclamativa del script. (3) Mantener `s_prev` a lo largo de todo el capítulo y guardarlo por frase. |
| VITS (Coqui) | `synthesizer.tts_model.length_scale = V` después de cargar | `inference_noise_scale` 0,5-0,667; `inference_noise_scale_dp` **0,6-0,8** (ritmo más regular; se prueba en el kit) | El texto entra ya en fonemas (Cotovía + `accent_convert`, como en el `synthesize.py` de Nós). No hay referencia de estilo: la calma sale solo de la velocidad, el ruido y las pausas. |
| Matcha | `speaking_rate = V` | `temperature` 0,5-0,667 | Igual que VITS. |

**REF-CALMA (la referencia de estilo, solo para StyleTTS2).**
- **Qué es:** el script oficial toma el estilo de `Data/Nos_<voz>-GL/audios/…-00001.wav`, una frase cualquiera del corpus [COMP, `inference_config.yml`]. La sustituimos por la frase más tranquila de la misma voz.
- **Selección:**
  1. Tomar 300 clips del corpus con ≥12 palabras y sin `?` ni `!`.
  2. Calcular la velocidad (fonemas por segundo) y la desviación de F0 en semitonos.
  3. Preseleccionar los 10 con menor velocidad y menor desviación.
  4. El promotor elige 1 a oído.
- **Licencia:** los datasets de Brais y Celtia son "solo investigación" (`voz_guion.md` §1.1). El clip solo se usa como condicionamiento interno y nunca se publica, pero **entra en la consulta escrita a Nós**.
- **Alternativa sin dataset:** usar como referencia 15 s generados por el propio modelo con `DUR_SCALE` 1,10 y `beta` 1,0, escogidos a oído (autoarranque) [S].

---

### 3A.3 Ritmo: fórmula y valores por acto

**Fórmula.** La velocidad percibida objetivo (§3) es la suma de habla y silencio:

- habla (min) = W × V ÷ r_nat, donde W son las palabras del bloque y V es `DUR_SCALE` o `length_scale`;
- silencio necesario S (s) = 60 × (T − habla), donde T son los minutos del bloque (§11.2);
- con n_f frases, n_p párrafos y n_c capítulos, y la proporción fija P_párrafo = 2,8 × P_frase:
  **P_frase = (S − n_c·P_cap) ÷ [(n_f − n_p) + 2,8·(n_p − n_c)]**.

**Topes anti "voz de goma" [S, a validar en el kit].**
- V ≤ **1,10** en los actos I-II y ≤ **1,15** en el Acto III.
- P_frase ≤ 1,6 s (≤ 2,2 s en el Acto III) y P_párrafo ≤ 4,5 s (≤ 6 s en el III).
- Si con los topes no se alcanza T, **se recorta el guion**: el presupuesto de palabras baja. **Nunca** se estira más la voz.
- Es preferible **más silencio que más estiramiento**, porque así lo hace el techo del género: History Time tiene 114 pausas de ≥8 s en 207 min [MED, proxy].

**Valores del Episodio 1 con r_nat = 150 palabras/min** (supuesto de partida; se recalculan en el paso 0). Palabras y minutos de §11.2; frases de 20, 19 y 22 palabras de media en I, II y III; 5, 5 y 4 frases por párrafo:

| Bloque | Percibido objetivo | V | Habla implícita (r_nat ÷ V) | P_frase | P_párrafo | P_cap (solo ambiente + sello) | Silencio total (1 − percibido ÷ habla) |
|---|---|---|---|---|---|---|---|
| Entrada (cap. 1) | ~107 palabras/min | 1,05 | 143 | 1,2 s | 3,3 s | 7 s | ~25 % |
| **Acto I** (caps. 2-5) | 115 | **1,05** | **143** | **1,45 s** | **4,1 s** | 7 s | ~20 % |
| **Acto II** (caps. 6-8) | 115 | **1,05** | **143** | **1,4 s** | **3,9 s** | 7 s | ~20 % |
| **Acto III** (cap. 9) | **105 (−9 %, "un 10 % más lento")** | **1,10** (+5 % de estiramiento) | **136** | **1,9 s** (+35 %) | **5,4 s** | 8 s | ~23 % |
| Despedida (cap. 10) | ~100 | 1,10 | 136 | 2,0 s | – | – | ~27 %, con pausas de respiración de 4-6 s |

Comprobación de coherencia: el habla implícita de todos los bloques (136-143) cae dentro de la banda del brief (§3A.1: 130-145 en I-II, 125-140 en el III). Ejemplo del Acto I con la fórmula: 2.925 palabras × 1,05 ÷ 150 = 20,5 min de habla en 25,5 min, es decir, 301 s de silencio; de ellos, 28 s en 4 cortes de capítulo y el resto repartido entre ~146 frases y ~29 párrafos, lo que da P_frase ≈ 1,46 s.

**Sensibilidad (calculada con la misma fórmula) [S].**
- Si r_nat = **140**, bastan ~1,0 s y 2,8 s en los actos I-II (1,45 s y 4,1 s en el III). Las pausas de 0,7 s / 2 s / 6-8 s de la v2 quedan como **suelo** del Acto I. Habla implícita: 133 (I-II) y 127 (III), dentro de la banda del brief.
- Si r_nat = **160**, harían falta ~1,85 s y 5,2 s, por encima del tope. En ese caso se recorta el guion un ~8 % (8.435 → ~7.750 palabras) o se elige otra voz. Es coherente con el brief: su habla implícita (160 ÷ 1,05 ≈ 152) ya se sale de la banda de 130-145.

**QA del ritmo:**
- Por acto, el ritmo percibido medido (palabras ÷ minutos de audio narrado) debe quedar a **±5 %** del objetivo.
- El Acto III debe ir entre un 8 % y un 12 % más lento que el II.
- Si falla, se ajustan primero P_frase y P_párrafo y después V, dentro de los topes. **No se reescribe el texto para cuadrar tiempos**, salvo el recorte previsto arriba.

---

### 3A.4 Léxico de pronunciación: sustitución automática, no "contrastar"

**Dónde entra.** El front-end de todos los modelos de fonemas de Nós es **Cotovía**. StyleTTS2 lo llama frase a frase (`cotovia -n -S -A0`) y lee la salida por líneas `palabra<TAB>transcripción` (`Utils/ASR/AuxiliaryASR/phonemize.py`, función `run_cotovia_with_phrase`) [COMP]. Cotovía no trae un diccionario de excepciones de usuario: sus ficheros `data/lang/gl/*.txt` son morfológicos [COMP]. Por eso el léxico se aplica **en esa función**, palabra a palabra:

```python
LEX = carga_tsv("lexico_gl.tsv")      # palabra en minúsculas -> fonemas (alfabeto Nós)
# dentro del bucle de run_cotovia_with_phrase, antes de "if col2:":
if col1.lower() in LEX:
    tokens.append(LEX[col1.lower()]); continue
```

Para VITS y Matcha se usa **la misma función** (con el léxico) en lugar de la llamada `-t3` de sus fichas.
- **Prueba de equivalencia:** con 20 frases, la cadena de fonemas debe coincidir con la del script oficial de cada modelo.
- **Si no coincide:** se aplica el léxico sobre la salida `-t3`, alineando palabra a palabra.
- **Modelos de grafemas** (`…-graphemes`): el léxico se aplica como **reescritura ortográfica**, en la columna `grafia_tts`.

**Alfabeto (los 69 tokens de `phoneme_token_maps.json`) [COMP].**
- **Vocales:** `a e E i o O u`. La tónica se marca con tilde sobre el símbolo: `á é É í ó Ó ú`, donde `É`/`Ó` son las **abiertas** tónicas y `é`/`ó` las **cerradas**.
- **Consonantes:**
  - `T` = [θ], `S` = [ʃ], `C` = [tʃ], `J` = [ɲ], `N` = [ŋ], `Z` = [ʎ];
  - `r` = vibrante simple, `R` = múltiple;
  - `B D G` = aproximantes, `x` = [x];
  - `j w` = semivocales.
- **Validación al cargar el TSV:**
  - Cada entrada solo usa esos símbolos.
  - Ninguna contiene `rr ll nh ch ao tS`, porque `clean_output` los reconvierte.
  - Tiene exactamente una vocal tónica.
  - Si falla, **error y no se renderiza**.

**Flujo automático.**
1. `g2p_check.py lexico_gl.tsv` pasa cada palabra por Cotovía dentro de una frase soporte ("Dixo ___ de novo.") y la compara con el léxico.
2. **Solo las entradas que difieren quedan activas**, y el informe lista las diferencias.
3. Antes de cada render, un script extrae del guion los nombres propios y las palabras trampa que **no** están en el léxico y los manda al lingüista.
4. La regla 6 de §5 pasa a ser: "0 palabras del guion en la lista de pendientes y léxico validado".

**`lexico_gl.tsv` v0 para el Episodio 1 [S].** Son propuestas del constructor. **Ninguna entrada se activa sin la marca `verificado` del lingüista**, contrastada con el *Dicionario de pronuncia da lingua galega* (ILG) y el DRAG. Las marcadas con ⚠ son dudosas incluso para el constructor.

| palabra | tipo | IPA | fonemas Nós | grafia_tts (modelos de grafemas) | nota |
|---|---|---|---|---|---|
| Hidacio | nombre | [iˈðaθjo] | `iDáTjo` | Hidacio | *h* muda |
| Dumio | nombre | [ˈdumjo] | `dúmjo` | Dumio | |
| Panonia | nombre | [paˈnɔnja] ⚠ | `panÓnja` | Panonia | ¿abierta, como *Babilonia*? |
| Martiño | nombre | [maɾˈtiɲo] | `martíJo` | Martiño | |
| Hermerico | nombre | [eɾmeˈɾiko] | `ermeríko` | Hermerico | Llana y sin tilde también en castellano (es.wikipedia y RAH escriben *Hermerico*) [F, §13]. **El riesgo no es el castellano normativo**, sino la forma popular esdrújula *Hermérico*, que circula en Galicia (p. ej. el nombre de la Asociación Hermérico) [F, §13], y que un G2P sin la palabra en su diccionario desplace el acento. Entra en M2 (n.º 18) |
| Requiario | nombre | [reˈkjaɾjo] | `Rekjárjo` | Requiario | *r* inicial múltiple |
| Requila | nombre | [reˈkila] | `Rekíla` | Requila | |
| Leovixildo | nombre | [leoβiˈʃildo] | `leoBiSíldo` | Leovixildo | `x` = [ʃ] |
| Órbigo | nombre | [ˈɔɾβiɣo] | `ÓrBiGo` | Órbigo | abierta tónica |
| Braga | nombre | [ˈbɾaɣa] | `bráGa` | Braga | |
| Bracara | nombre | [ˈbɾakaɾa] | `brákara` | Brácara | Latín; preferible "Braga" en voz |
| Gallaecia | nombre | ⚠ [gaˈlɛθja] o [gaʎaˈeθja] | *decide el lingüista* | *ídem* | Una sola forma, fija para toda la serie "Gallaecia" |
| Chaves | nombre | [ˈtʃaβes] | `CáBes` | Chaves | Sustituye a *Aquae Flaviae* en voz |
| Aecio | nombre | [aˈeθjo] ⚠ | `aéTjo` | Aecio | |
| Polemio | nombre | [poˈlɛmjo] ⚠ | `polÉmjo` | Polemio | |
| Astorga | nombre | [asˈtɔɾɣa] ⚠ | `astÓrGa` | Astorga | Sustituye a *Asturica* en voz |
| Limia | nombre | [ˈlimja] | `límja` | Limia | |
| Suevos | nombre | [ˈsweβos] ⚠ | `swéBos` | Suevos | Abertura por confirmar |
| Arteixo | nombre | [aɾˈtejʃo] | `artéjSo` | Arteixo | |
| Miño | nombre | [ˈmiɲo] | `míJo` | Miño | |
| Exipto | nombre | [eˈʃipto] | `eSípto` | Exipto | |
| Europa | nombre | [ewˈɾɔpa] | `ewrÓpa` | Europa | |
| Xoán | nombre | [ʃoˈaŋ] | `SoáN` | Xoán | nasal velar final |
| pedra | trampa | [ˈpɛðɾa] | `pÉDra` | pedra | abierta |
| terra | trampa | [ˈtɛra] | `tÉRa` | terra | abierta |
| xente | trampa | [ˈʃɛnte] | `SÉnte` | xente | abierta |
| pé | trampa | [ˈpɛ] | `pÉ` | pé | |
| é / e | trampa | [ˈɛ] / [e] | `É` / `e` | é / e | verbo frente a conjunción |
| home | trampa | [ˈɔme] | `Óme` | home | abierta |
| novo / nova / novos | trampa | [ˈnovo] / [ˈnɔβa] / [ˈnɔβos] | `nóBo` / `nÓBa` / `nÓBos` | – | metafonía |
| corpo / corpos | trampa | [ˈkoɾpo] / [ˈkɔɾpos] | `kórpo` / `kÓrpos` | – | metafonía |
| porto / portos | trampa | [ˈpoɾto] / [ˈpɔɾtos] | `pórto` / `pÓrtos` | – | metafonía |
| vello / vellos / vella | trampa | [ˈbeʎo] / [ˈbeʎos] / [ˈbɛʎa] | `béZo` / `béZos` / `bÉZa` | – | |
| noite, lonxe, fonte, monxe, monxes, sono, todo | trampa | cerradas | `nójte`, `lónSe`, `fónte`, `mónSe`, `mónSes`, `sóno`, `tóDo` | – | típico error: abrirlas |
| chove | trampa | [ˈtʃɔβe] | `CÓBe` | chove | título del cap. 1 |
| néboa | trampa | [ˈnɛβoa] | `nÉBoa` | néboa | |
| leva | trampa | [ˈlɛβa] | `lÉBa` | leva | §11.6 |
| volve | trampa | [ˈbɔlβe] | `bÓlBe` | volve | §11.6 |
| cobre | trampa | [ˈkɔβɾe] ⚠ | `kÓBre` | cobre | §11.6 |
| queda | trampa | ⚠ | *lingüista* | queda | §11.6, última frase |
| lembra | trampa | [ˈlɛmbɾa] ⚠ | `lÉmbra` | lembra | §11.6 |
| voz / nós | trampa | [ˈbɔθ] / [ˈnɔs] | `bÓT` / `nÓs` | – | |
| unha, dunha, algunha, ningunha, ninguén, un, quen | trampa | [ŋ] | `úNa`, `dúNa`, `alGúNa`, `niNGúNa`, `niNGéN`, `úN`, `kéN` | – | nasal velar (también la *-n* final): el error castellano más audible |

**Reglas de guion que reducen el léxico (se aplican antes, en la revisión lingüística):**
- Los nombres latinos se dicen en su forma gallega: *Aquae Flaviae* → "Chaves", *Asturica* → "Astorga", *Lucus Augusti* → "Lugo".
- Los títulos latinos no se leen: *De correctione rusticorum* → "unha carta"; *Parochiale suevorum* → "a lista das parroquias".
- Sin cifras escritas: todo número va en letra, para que la normalización de Cotovía no decida.
- Sin abreviaturas.


---

## 4. Estructura de un episodio para dormir

### 4.1 Minutado del episodio tipo de 75 min [S]

| Bloque | Tiempo | % | Contenido | Densidad máxima de datos |
|---|---|---|---|---|
| **0. Umbral** | 0:00-0:15 | – | Solo ambiente (chuvia) y fundido desde negro. Sello sonoro de 4 s. | 0 |
| **1. Entrada suave** | 0:15-2:30 | 3 % | Escena de lugar en presente (45-60 s) → "Boas noites. Isto é Serán…" → qué se contará esta noche (3 frases) → permiso para dormirse ("non tes que lembrar nada") → "acomódate". **Sin CTA de suscripción.** | 1 fecha, 2 nombres propios |
| **2. Acto I: contexto y movimiento** | 2:30-28:00 | ~35 % | El "qué pasó": llegada, fundación, conflicto **y el final ya anticipado** (cómo acaba la historia se cuenta aquí, no al final). Los hechos violentos, con distancia ("o cronista fala de…"), en pasado y sin detalles corporales. | ≤3 nombres propios nuevos por minuto; fechas redondeadas ("a mediados do século V") |
| **3. Acto II: vida y paisaje** | 28:00-62:00 | ~45 % | Cómo se vivía: casas, oficios, estaciones, comida, caminos y ríos. Descripción sensorial lenta. Repeticiones suaves de imágenes ya presentadas (la misma fonte, el mismo rego). | ≤1 nombre propio nuevo por minuto; sin cifras |
| **4. Acto III: desenlace que se apaga** | 62:00-73:30 | ~15 % | Qué quedó: ruinas, topónimos, costumbres. Frases más largas y más lentas (+10 % de pausa); presente contemplativo; ninguna fecha; la imagen baja a luminancia <20. | 0 fechas; ≤0,3 nombres por minuto |
| **5. Despedida** | 73:30-75:00 | 2 % | Relajación guiada de 60-90 s (respiración, peso del cuerpo, sonido de la lluvia) y "Boas noites". Nada de "ata a próxima semana". | 0 |
| **6. Cola de ambiente** | 75:00-100:00 | – | Solo el ambiente del episodio, con fundido final de 60 s. Pantalla casi negra. | – |

**Curva de tensión objetivo:** tensión máxima entre el 10 % y el 30 % del episodio; desde el 40 %, siempre descendente. El auditor QA puntúa cada capítulo de 1 a 5 en "activación" (sustos, suspense, preguntas abiertas) y comprueba que la serie no sube después del capítulo 4 [S]. El Episodio 1 lleva la serie 1-2-3-3-2-1-1-1-1-0 (§11.2).

### 4.2 Reglas de escritura del guion (galego) [S, derivadas de `formato.md` §3.3 y `voz_guion.md` §2]
- **Persona:** tercera persona narrativa. Se habla al oyente de **ti** (singular, íntimo) solo en la entrada y la despedida. Nunca la segunda persona "de reto" ("non aguantarías nin un día").
- **Frases** de 15-30 palabras, con cadencia regular. Nada de preguntas retóricas en cadena ni de *cliffhangers* ("pero o que ían descubrir cambiaríao todo…").
- **Nada de números largos:** "arredor de mil homes", no "1.247 homes". Los años, solo en el Acto I.
- **Lo reconstruido se marca como tal:** "podemos imaxinar", "quizais". Lo documentado se cuenta sin muletillas. Nunca se inventan diálogos ni rasgos de carácter de personas reales.
- **Topónimos en su forma oficial gallega** (Nomenclátor de Galicia) y pronunciación verificada en el *Dicionario de pronuncia da lingua galega* (https://ilg.usc.gal/gl/proxectos/dicionario-de-pronuncia-da-lingua-galega [F]).
- **Norma RAG** fijada en el prompt, con lista negra de castelanismos y sin lusismos ni hiperenxebrismos (`voz_guion.md` §2.1-2.2). Preferencia por los tiempos simples (pluscuamperfecto sintético "chegara", condicional simple "gustaría") frente a los compuestos calcados del castellano.
- **Sin militancia:** tono descriptivo en temas identitarios (Reino suevo, Reino de Galicia, irmandiños). Se exponen los debates historiográficos como tales ("uns historiadores pensan…, outros…").
- **Cada afirmación histórica, con su fuente** en un anexo interno que no se lee en voz alta (ver la columna de fuentes de §11.2). La bibliografía resumida va en la descripción.

### 4.3 Muestra de entrada suave (≈150 palabras, tema vikingos) [S; es un borrador que debe pasar la revisión lingüística y el kit A/B]

> Na ribeira do Ulla, cando a marea baixa, as Torres de Oeste quedan soas entre a lama e os xuncos. Son dúas torres, un anaco de muro e o rumor da auga que vai e vén. Hai mil anos, por aquí subían os barcos cara a Compostela, e por aquí mesmo tentaron pasar outros barcos, máis longos, que viñan do norte.
>
> Boas noites. Isto é Serán, historia de Galicia para durmir.
>
> Esta noite imos remontar o río amodo, sen présa ningunha. Falaremos dos homes do norte que chegaron ás rías, dos bispos que levantaron torres para detelos, e das vilas que, co paso dos séculos, esqueceron o medo e volveron mirar para o mar.
>
> Non tes que lembrar nada. Se o sono chega antes do final, déixao vir: a historia seguirá aquí mañá.
>
> Acomódate. Apaga a luz. Escoita a chuvia.

Nótese: el conflicto (los vikingos) se anuncia en la entrada y se resuelve en el Acto I; el episodio termina en las villas en paz. La entrada no pide nada al oyente. Las muestras del Acto II y III del Episodio 1 están en §11.5 y §11.6.

---

## 5. Reglas de "sono seguro" (estándar de producto, verificable en QA)

Cada regla tiene un umbral que el auditor automático o humano comprueba antes de publicar. Los umbrales numéricos son [S] salvo que se indique fuente.

| # | Regla | Umbral / comprobación |
|---|---|---|
| 1 | Volumen constante | Integrado **-16 LUFS** (±1), por debajo de los -14 a los que YouTube normaliza, así que YouTube no lo toca [F: YouTube baja el contenido que supera ~-14 LUFS y no sube el más bajo, productionadvice.co.uk]. |
| 2 | Sin picos | True peak ≤ **-1,5 dBTP**; rango de sonoridad (LRA) ≤ 5 LU; ningún evento de más de 3 dB sobre la media móvil de 3 s. |
| 3 | Ambiente por debajo de la voz | Cama sonora 20-26 dB por debajo de la voz [S, `formato.md` §3.5]. Chasquidos de lareira limitados (ver §6). |
| 4 | Voz sin brillo agresivo | De-esser; atenuación suave por encima de 8-10 kHz (`voz_guion.md` §1.7). |
| 5 | Sin *glitches* de TTS | Detector automático (saltos de energía o de tono, repeticiones, palabras cortadas, deriva de F0 mediana >2 semitonos entre capítulos) más escucha humana del primer y el último capítulo completos y un muestreo del 20 % del resto. Las frases marcadas se vuelven a renderizar una a una con su semilla (§3A.2). Fundidos de 15 ms en cada frase contra los clics. 404 Media documentó un glitch audible en un vídeo de 2,3 M de vistas [F]. |
| 6 | Pronunciación galega | **Automática:** léxico `lexico_gl.tsv` validado por el lingüista y aplicado dentro de Cotovía (§3A.4). Umbral: 0 nombres propios o palabras trampa del guion fuera del léxico; `g2p_check` sin diferencias no resueltas; ≥27/30 en las frases trampa M2 de la voz elegida (§3A.1.2). |
| 7 | Sin llamada a suscribirse en la voz | Cero menciones de "subscríbete", "gústame", "campá" o "comenta" en el audio. La CTA vive en la descripción, el comentario fijado y la pantalla final **muda**. |
| 8 | Sin sobresaltos narrativos | Nada de gritos, cifras de muertos "a golpe", efectos de espadas ni campanas cercanas. Campanas lejanas, a -30 dB o menos. Puntuación de "activación" decreciente (§4.1). |
| 9 | Sin sobresaltos visuales | Ninguna transición brusca; fundidos de 2-3 s o más; sin *flashes*; sin caras "gritando"; zoom por plano ≤3 %. |
| 10 | Tarjetas y pantallas finales mudas | Sin animación sonora de "suscríbete". Pantalla final solo al terminar la cola de ambiente. |
| 11 | **Anuncios: pre-roll y post-roll** | En vídeos nuevos, YouTube solo deja activar o desactivar "antes y después" en conjunto; ya no se pueden elegir por separado [F, Marketing Brew 2023]. Por eso **la cola de ambiente de 20-45 min es parte del diseño**: el anuncio final llega cuando el oyente ya lleva mucho rato dormido. |
| 12 | **Anuncios: mid-rolls** | Etapa 1: **ninguno** (el canal aún no estará en el YPP; `retornos.md` §1). Etapa 2: **0-2 mid-rolls manuales, solo en los primeros 20 min**, en los cortes entre capítulos, con 3 s de silencio. Test A/B por lotes: RPM frente a retención frente a comentarios de "espertoume" [S, `retornos.md` §3.3]. En Spotify, el único corte permitido es el de 00:00 (§9). |
| 13 | Honestidad del "sen cortes" | "Sen cortes" en el título, la miniatura o la descripción **solo** en los vídeos sin mid-rolls; **nunca** en la promesa del canal (§2). Hay precedente: History at Night ("NO AD BREAKS") y Sleepy History Channel ("No Adverts") [MED]. |
| 14 | Temporizador | Una línea fija en la descripción: "Podes usar o temporizador de apagado de YouTube". YouTube lo extendió a todos los usuarios en octubre de 2024 [F, Yahoo Tech]. |

**Excepción consciente [S]:** el pre-roll (inicio) no despierta, porque el oyente aún no se ha dormido. Es la fuente de ingresos menos dañina y se mantiene activa cuando haya YPP.

---

## 6. Paisaje sonoro galego

### 6.1 Principio
Mucha audiencia escucha con la pantalla apagada (`formato.md` §0.8 [S]), así que **el audio es el producto**. El ambiente no es decoración: es un **sello de marca** que ningún canal en castellano o inglés tiene (la lluvia atlántica y las lenguas de la costa).

### 6.2 Biblioteca de ambientes (v1) [S]

| Código | Ambiente | Uso por tema | Nota técnica |
|---|---|---|---|
| AMB-LOUSA | **Chuvia miúda nun tellado de lousa** | Ambiente por defecto (aldea, mosteiro) | El más neutro y "dormible". Evitar el goteo irregular fuerte. |
| AMB-CARBALLEIRA | **Chuvia na fiestra / na carballeira** | Temas de camino, bosque, castros | Espectro suave. |
| AMB-RÍA | **Ría en calma** (resaca lenta, sin rompientes) | Temas marítimos: vikingos, emigración, balea, faros | **No** usar el mar de la Costa da Morte con golpes de ola: son picos. |
| AMB-LAREIRA | **Lareira** | Temas de invierno y serán, Rosalía, escenas de escritura | Los chasquidos del fuego son transitorios que despiertan: limitarlos a 6 dB por encima de la cama y filtrarlos [S]. |
| AMB-REGO | **Río, rego e muíño** | Oficios, muíños, Ribeira Sacra, mosteiros | Rumor continuo; la rueda, muy lejana. |
| AMB-VERÁN | **Noite de verán** (grilos, vento suave nos piñeiros) | Castros, mámoas, islas | Grillos a volumen muy bajo (son agudos). |

- **Música:** mínima. Un *drone* de zanfona o un pad de arpa muy lento, solo en los cambios de capítulo (6-8 s) y en el umbral. **Se evita la gaita** por su registro agudo y penetrante [S].
- **Sello sonoro (4 s):** lluvia y una sola nota grave de zanfona que se apaga. Siempre el mismo, siempre bajo.

### 6.3 Origen y derechos
- **Prioridad 1: grabaciones propias** del promotor en Galicia (lluvia de verdad, ría, río). Coste: un grabador portátil de gama de entrada, ~100-150 € [S, precio no verificado], o el móvil con micrófono externo para empezar. Da autenticidad ("chuvia gravada en Lalín", por ejemplo) y **evita el riesgo de Content ID**: hay precedente de un vídeo de ruido blanco que recibió cinco reclamaciones falsas de otros canales "para dormir" [F, Tubefilter 2018].
- **Prioridad 2:** Freesound (https://freesound.org [F]), **solo archivos CC0 o CC BY** (nunca CC BY-NC en un canal monetizado), registrando licencia y autor en una hoja por episodio [S].
- **Prioridad 3:** Biblioteca de audio de YouTube para la música de transición.
- **Música generada por IA:** solo con una herramienta cuyos términos den derechos comerciales claros, y nunca imitando piezas tradicionales con autor identificable [S].
- **No registrar** nuestros ambientes en Content ID: generaría conflictos con terceros [S].

---

## 7. Identidad visual: "noite atlántica"

### 7.1 Biblia visual (v1) [S, derivada de las mediciones de `formato.md` §3.6]
- **Estilo:** pintura al óleo o *matte painting* atlántica: néboa, pedra con liques, verdes húmidos, luz de candea, ceos de chuvia. **No fotorrealista** (evita confundir con imagen real y la etiqueta obligatoria de contenido sintético realista, `retornos.md` §6.2 [F]). Sin personas identificables ni caras en primer plano; figuras pequeñas, de espaldas o en silueta.
- **Paleta (tokens de marca):**

| Token | Hex | Uso |
|---|---|---|
| noite | `#0E1A22` | fondo, 60 % del cuadro |
| lousa | `#2B3A42` | piedra, sombras |
| musgo | `#3F5A4A` | vegetación |
| néboa | `#C9D1D3` | texto, brumas |
| candea | `#D9A05B` | único acento cálido (ventanas, fuego, título) |

- **Luminancia:** 40-70/255 de media en los actos I y II; <20 en el Acto III y en la cola, sin llegar al negro absoluto (que parece un error) [S]. Referencias: Sleepy History Channel 34, History at Night 86 [MED].
- **Movimiento:** una imagen nueva cada **40-90 s**; Ken Burns ≤3 % por plano; fundidos de 2-3 s. Sin texto en pantalla salvo el título del capítulo (serif, pequeño, 4 s, en fundido).
- **Mapas:** mapa base de Galicia propio, oscuro, con topónimos en galego normativo, reutilizable en todos los episodios. Refuerza el rigor.
- **Volumen de imágenes:** 60-120 por episodio de 75 min (el Ep. 1 lleva 74, §11.4).
- **Tipografía:** una serif clásica con buen soporte de acentos (p. ej. EB Garamond o Cormorant, de Google Fonts, licencia OFL [S]).

### 7.2 Plantilla de prompt "noite atlántica" (fija para todos los episodios) [S]
Los prompts de imagen se escriben en inglés (los modelos de imagen responden mejor) y se componen siempre igual: `[ESTILO] + [MOTIVO del plano] + [LUZ] + [NEGATIVO]`.

- **ESTILO (fijo):** `dark atlantic oil painting, matte painting, visible soft brushstrokes, muted palette of deep blue-black #0E1A22, slate grey #2B3A42 and moss green #3F5A4A, low contrast, soft mist, gentle rain, calm, quiet, 16:9 wide composition, no text`
- **LUZ (según acto):** Acto I `overcast dusk light, mean brightness low`; Acto II `night, a single warm candlelight accent #D9A05B, very low key`; Acto III y cola `almost dark, faint silhouette only, brightness under 10 percent`.
- **NEGATIVO (fijo):** `photorealistic, photograph, close-up faces, identifiable people, blood, gore, corpses, raised weapons, battle chaos, fire explosion, bright sky, saturated colors, text, letters, watermark, logo, modern objects, horned helmets, fantasy armor`.
- **Figuras humanas:** solo `small distant figure seen from behind` o `silhouette`.
- **Arquitectura real conocida** (catedrales, Pórtico, Torre de Hércules): no se genera con IA "de memoria"; se usa foto propia o de dominio público repintada con filtro de estilo, para no publicar un monumento inventado [S].

### 7.3 Miniatura (plantilla fija)
- Un solo motivo gallego reconocible de noche: Torres de Oeste, Castro de Baroña, Pórtico da Gloria, un hórreo bajo la lluvia, Santa Tegra.
- Etiqueta fija **"HISTORIA PARA DURMIR"** siempre en la misma esquina y tipografía, y el rango de fechas estilo History Time ("411-585").
- Sello "sen cortes" solo cuando sea cierto (regla 13).
- Nada de caras, sangre ni texto de clickbait.

### 7.4 Títulos (fórmula)
`[Tema en galego] ([fechas]) | Historia de Galicia para durmir` y, solo si no hay mid-rolls, `· sen cortes` [S; `formato.md` §3.11]. La descripción lleva una línea en castellano para la búsqueda ("Historia de Galicia para dormir, narrada en gallego") y etiquetas en castellano, sin traducir el audio. El público galego busca en castellano (`audiencia.md` §2.3: el 61 % de quienes siempre hablan galego escribe en castellano [F, IGE]). Plantilla completa aplicada al Ep. 1 en §11.8.

---

## 8. Catálogo de 30 temas, ordenados por prioridad

### 8.1 Criterios y fórmula [S]
Cuatro puntuaciones de 1 a 5, con anclas para que dos personas puntúen igual:

| Criterio | 5 | 3 | 1 |
|---|---|---|---|
| **D, "durmibilidade"**: cuánto admite una curva descendente, con más descripción que acción | Sin conflicto: vida cotidiana, paisaje, oficio | Conflicto que cabe en el Acto I y luego se apaga | Bélico o trágico de principio a fin |
| **Dem, demanda del tema GALLEGO** (no del formato genérico, que ya está probado por el género entero) | Tema gallego medido con ≥100K vistas en castellano o ≥10K en galego | Señales indirectas (tema relacionado, nicho identificable, turismo) | Sin señales |
| **Fx, fuentes y visuales** | Fuentes primarias editadas + bibliografía galega + visuales reutilizables | Bibliografía general, visuales genéricos | Especulativo, casi sin fuentes |
| **R, riesgo** (polémica, dolor, sustos, especulación, error fácil) | Dolor reciente o polarización fuerte | Riesgo manejable con la curva o con cautelas | Nulo |

(Dem = 4: tema gallego medido con 10-100K en castellano o 3-10K en galego. Dem = 2: sin medición pero con marca turística o escolar.)

- **Puntuación de producto:** **P = 2·D + Dem + Fx − R** (rango −1 a 19). Mide el encaje a largo plazo.
- **Prioridad de lanzamiento:** **L = P + Dem**. En la Etapa 1 el canal es desconocido y el cuello de botella es el **descubrimiento**, así que la demanda cuenta doble.
- **Orden:** por L; empates, por Dem más alta; después, por R más bajo. ▲ = demanda medida con cifras.

### 8.2 Catálogo puntuado

| # | Tema · título de trabajo (galego) | D | Dem | Fx | R | **P** | **L** | Por qué funciona para dormir | Demanda / evidencia | Riesgo y cómo tratarlo |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 ▲ | *O Reino suevo de Gallaecia (411-585)* | 4 | 5 | 4 | 2 | 15 | **20** | Época remota con fuentes escasas: invita a describir villas y parroquias. Es el gemelo atlántico de "After Rome" (el techo). | 165K vistas en castellano (Crónicas de la Historia); 23,7K en galego (Burla Negra, 1 h) [F en `audiencia.md` §4.3] | Debate "primer reino de Europa": presentarlo como debate. Hoja de producción completa en §11. https://gl.wikipedia.org/wiki/Reino_Suevo |
| 2 | *Un peregrino do século XII no Camiño de Santiago* | 5 | 3 | 5 | 1 | 17 | **20** | Caminar es el ritmo perfecto para dormir: etapa a etapa, siguiendo la guía del Codex Calixtinus. | Temática global; posible financiación "O teu Xacobeo" (`ingresos_alt.md` §1.5 [F]) | Mínimo. https://gl.wikipedia.org/wiki/Codex_Calixtinus |
| 3 | *Un día nunha aldea galega do século XV* | 5 | 3 | 4 | 1 | 16 | **19** | Sin conflicto; cotidiano, sensorial y repetitivo (la mañana, el trabajo, la lareira, la noche). | Formato probado: 1,05 M en castellano con "día completo en la Edad Media" [MED], pero sin medición del tema gallego (por eso Dem = 3) | Mínimo. Contrastar con la historia social (Saavedra). |
| 4 | *A vida nun castro (séculos IX a.C.-I d.C.)* | 5 | 3 | 4 | 2 | 15 | **18** | Arqueología, paisaje y oficios; pocos hechos políticos, así que la curva es plana por naturaleza. | "Origen de los gallegos", 22,5K en castellano (tema relacionado) [F `audiencia.md`] | El celtismo romántico: separar mito y arqueología con calma. https://gl.wikipedia.org/wiki/Cultura_castrexa |
| 5 | *O Mestre Mateo e o Pórtico da Gloria* | 5 | 2 | 5 | 1 | 16 | **18** | Descripción minuciosa de figuras de piedra: "lectura lenta" de una imagen. | Patrimonio y turismo [S] | Visual: exige imágenes fieles del monumento real (§7.2), no IA "de memoria". https://gl.wikipedia.org/wiki/Pórtico_da_Gloria |
| 6 | *A Torre de Hércules: dous mil anos de luz* | 4 | 3 | 4 | 1 | 14 | **17** | Faro, mar y continuidad: una sola imagen que se repite a lo largo de los siglos. | Patrimonio de la Humanidad; muy buscado [S] | Mismo cuidado visual que el n.º 5. https://gl.wikipedia.org/wiki/Torre_de_Hércules |
| 7 | *Rosalía de Castro e o Rexurdimento* | 4 | 3 | 5 | 2 | 14 | **17** | Poesía en galego de dominio público (†1885): puede leerse en voz baja; el registro nocturno por excelencia. | Día das Letras y ámbito escolar [S] | Tono melancólico: bien, pero sin dramatismo. https://gl.wikipedia.org/wiki/Rexurdimento |
| 8 | *Os mosteiros da Ribeira Sacra: Samos, Oseira, Santo Estevo* | 5 | 2 | 4 | 1 | 15 | **17** | Silencio monástico, horas canónicas, viñas en socalcos: el tema más "arrolador" del catálogo. | Turismo y marca Ribeira Sacra [S] | Mínimo. https://gl.wikipedia.org/wiki/Ribeira_Sacra |
| 9 | *O ano labrego: do magosto ás mallas* | 5 | 2 | 4 | 1 | 15 | **17** | El ciclo de las estaciones se repite por diseño; incluye seráns, fiadeiros y magostos (coherencia de marca). | [S] | Mínimo. https://gl.wikipedia.org/wiki/Serán ; https://gl.wikipedia.org/wiki/Magosto |
| 10 | *Hórreos, cruceiros e petos de ánimas* | 5 | 2 | 4 | 1 | 15 | **17** | Contemplación de objetos en el paisaje; muy visual. | [S] | Castelao (†1950) no es dominio público hasta 2031 [S, derecho español]: citar sin reproducir extensamente. https://gl.wikipedia.org/wiki/Hórreo |
| 11 ▲ | *Lendas de Galicia: mouras, lagoas asolagadas e tesouros encantados* | 3 | 5 | 3 | 3 | 11 | **16** | Mito y paisaje. **Versión "amable":** sin Santa Compaña ni terror. | 107,8K en castellano ("Duérmete con las leyendas de Galicia", 2 h) [F `audiencia.md` §4.3] | Riesgo de miedo: filtrar las lendas de ánimas y muerte o tratarlas con distancia. |
| 12 | *A Compostela de Xelmírez (século XII)* | 4 | 3 | 4 | 2 | 13 | **16** | La construcción de la catedral, piedra a piedra: una narración de obra lenta. | Compostela, tema muy buscado [S] | Bajo (las intrigas del obispo van en el Acto I). https://gl.wikipedia.org/wiki/Diego_Xelmírez |
| 13 | *Lucus Augusti e as vías romanas de Gallaecia* | 4 | 2 | 5 | 1 | 14 | **16** | Ingeniería, calzadas y murallas: descripción lenta de piedra y caminos. Precuela natural del n.º 1. | [S] | Mínimo. https://gl.wikipedia.org/wiki/Lucus_Augusti |
| 14 | *Baroña e os castros do mar* | 5 | 2 | 3 | 1 | 14 | **16** | Complemento del n.º 4, más marino y visual. | [S] | Mínimo. https://gl.wikipedia.org/wiki/Castro_de_Baroña |
| 15 ▲ | *A Revolta Irmandiña (1467-1469)* | 2 | 4 | 5 | 3 | 10 | **14** | Gran relato identitario. Conflicto en el Acto I; ruinas de fortalezas y memoria en el II-III. | 6,9K y 6K vistas en galego, las más altas de su tipo [F `audiencia.md`]; fuentes de Carlos Barros | Conflicto: aplicar la curva con rigor. https://gl.wikipedia.org/wiki/Revolta_irmandiña |
| 16 | *Canteiros, afiadores e arrieiros: os oficios do camiño* | 4 | 2 | 3 | 1 | 12 | **14** | Oficio y camino; jergas propias (verbas dos canteiros) con sabor único. | [S] | Mínimo. https://gl.wikipedia.org/wiki/Canteiro |
| 17 | *As illas: Cíes, Ons e Sálvora, a vida que se foi* | 4 | 2 | 3 | 1 | 12 | **14** | Aldeas insulares abandonadas, faros, aves: melancolía serena. | [S] | Mínimo. https://gl.wikipedia.org/wiki/Illas_Cíes |
| 18 | *Os muíños e a auga: muiñeiros e maquías* | 5 | 1 | 3 | 1 | 13 | **14** | El sonido del río encaja con el ambiente; ritmo del trabajo circular. | [S] | Mínimo. https://gl.wikipedia.org/wiki/Muíño |
| 19 | *A travesía: dun porto galego a Bos Aires* | 3 | 3 | 4 | 3 | 10 | **13** | Un viaje lento en barco, días iguales en el mar: episodio emocional para la diáspora. | Nicho de la diáspora (`audiencia.md` §7) | Pena y separación: tratarlas con serenidad y cerrar en la memoria. https://gl.wikipedia.org/wiki/Emigración_galega |
| 20 | *Os faros da Costa da Morte e os seus fareiros* | 4 | 2 | 3 | 2 | 11 | **13** | Vida solitaria, noches de guardia, mar. **Sin naufragios en detalle.** | [S] | Los naufragios, en una frase y con distancia. |
| 21 | *Unha recua de viño do Ribeiro camiño de Betanzos* | 5 | 1 | 2 | 1 | 12 | **13** | Viaje de arrieros a paso de mula. | [S] | Mínimo; fuentes dispersas. |
| 22 | *O Reino de Galicia: reis coroados en Compostela* | 2 | 4 | 4 | 4 | 8 | **12** | Gran relato; coronación de Afonso VII en 1111. | Tema estrella de la divulgación en galego; "Galicia vs. Castilla", 19,9K en castellano (`audiencia.md` §9) | Polarización identitaria: tono descriptivo. https://gl.wikipedia.org/wiki/Afonso_VII_de_León_e_Castela |
| 23 | *Mámoas e petróglifos: a Galicia de hai cinco mil anos* | 4 | 2 | 3 | 3 | 10 | **12** | Misterio tranquilo, piedra y horizontes. | [S] | La especulación: marcar siempre la incertidumbre. https://gl.wikipedia.org/wiki/Mámoa |
| 24 | *Os viquingos nas rías e as Torres de Oeste* | 2 | 3 | 4 | 3 | 8 | **11** | Ataques en el Acto I; torres, puertos y paz después (ver muestra §4.3). | 146K en portugués ("Durma com história", vikingos, no gallego) [F `audiencia.md` §6.1] | Violencia: curva estricta. https://gl.wikipedia.org/wiki/Torres_de_Oeste |
| 25 | *Santo André de Teixido: vai de morto quen non foi de vivo* | 3 | 2 | 3 | 2 | 9 | **11** | Romería, acantilados, creencias. | [S] | La muerte como tema: desde la tradición, no desde el miedo. |
| 26 | *A caza da balea e as salgas das rías* | 3 | 2 | 3 | 2 | 9 | **11** | Economía marítima, puertos, estaciones de pesca. | [S] | La sangre de la caza: con distancia. https://gl.wikipedia.org/wiki/Salga |
| 27 | *Prisciliano, o bispo de Gallaecia* | 3 | 3 | 2 | 4 | 7 | **10** | Misterio de la tumba, Gallaecia tardorromana. | [S] | Sensibilidad religiosa y especulación. https://gl.wikipedia.org/wiki/Prisciliano |
| 28 | *Sargadelos: a fábrica no bosque (1791)* | 3 | 1 | 3 | 2 | 8 | **9** | Industria ilustrada en un valle; cerámica y hornos. | [S] | El motín de 1798, en el Acto I. https://gl.wikipedia.org/wiki/Sargadelos |
| 29 | *1809: Galicia fronte a Napoleón* | 1 | 3 | 4 | 4 | 5 | **8** | Menos dormible; valor de demanda en castellano. | [S] | Bélico: solo en la Etapa 2 y con curva estricta. https://gl.wikipedia.org/wiki/Batalla_de_Elviña |
| 30 | *O mariscal Pardo de Cela (1483)* | 1 | 3 | 3 | 4 | 4 | **7** | Relato trágico y final del mundo nobiliario gallego. | Identitario [S] | Ejecución: tratamiento muy distanciado. https://gl.wikipedia.org/wiki/Pedro_Pardo_de_Cela |

**Lectura de la tabla.** La puntuación premia lo que el formato necesita: los temas sin conflicto (Camiño, aldea, castro, mosteiros) tienen la P más alta, y los temas identitarios con conflicto (irmandiños, Reino de Galicia, Pardo de Cela) quedan abajo aunque tengan demanda. El Reino suevo es n.º 1 porque es el único que combina demanda medida en las dos lenguas (Dem = 5) con una curva manejable. **Todas las puntuaciones son [S]**: las pone el promotor con las anclas de §8.1 y se recalibran con la retención real de la Etapa 1.

**Plan de publicación de la Etapa 1 (primeros 6 episodios, en 12 semanas) [S]:**
1. **Reino suevo** (L = 20; hoja de producción en §11).
2. **Aldea do século XV** (L = 19). Se adelanta al Camiño para alternar "evento" y "cotidiano" y probar pronto el formato de más D.
3. **Camiño do século XII** (L = 20). Además, abre la vía de financiación Xacobeo.
4. **Castro** (L = 18).
5. **Lendas amables** (n.º 11, L = 16) — **experimento deliberado:** el tema con más demanda medida en castellano; mide si la búsqueda en castellano trae oyentes que se quedan con el galego.
6. **Irmandiños** (n.º 15, L = 14) — **experimento deliberado:** un tema con conflicto y la demanda galega más alta; mide si la curva descendente aguanta en un tema "caliente". Reutiliza la muestra de guion de `drafts/guion.md`.

El Pórtico (n.º 5) y la Torre (n.º 6) pasan a la Etapa 2 aunque puntúan alto: exigen imágenes fieles de monumentos reales (§7.2), que es lo más caro de la cadena visual. *Nota de coherencia para el ensamblaje:* `drafts/guion.md` usa los irmandiños como muestra de registro; el primer episodio **publicado** es el Reino suevo.

**Series (defensa frente a "inauthentic content"):** agrupar en arcos con identidad propia: "Gallaecia" (Reino suevo, Lucus Augusti, Prisciliano, castro, Baroña), "O mundo labrego" (aldea, ano labrego, oficios, hórreos, muíños, recua), "O mar" (Torre, faros, illas, balea, viquingos, travesía) y "O Reino" (Reino de Galicia, irmandiños, Pardo de Cela, Xelmírez, Pórtico). Cada serie tiene su ambiente y su mapa. Es la "distinct storyline, focus or concept" que la política de YouTube permite [F, `retornos.md` §6.1].

### 8.3 Temas excluidos (por ahora) [S]
- **Guerra Civil, represión y franquismo:** dolor reciente, memoria familiar viva y polarización; no son compatibles con dormirse.
- **Política contemporánea, Prestige, incendios:** conflicto actual.
- **Santa Compaña y el terror folclórico** como episodio propio: solo en un posible especial de Samaín, fuera de la línea principal.
- **Genealogías reales sin fuentes y "misterios" especulativos** (tesoros templarios, etc.): alto riesgo de error, y la comunidad galega los castiga.

---

## 9. Formatos derivados

### 9.1 Qué paga el Spotify Partner Program (SPP), según la página oficial [F, consultada el 29-09-2026]
El SPP llega a España "a partir del próximo 20 de octubre" (2026), según la nota de Europa Press publicada por Infobae el 25-09-2026 tras el Spotify NEXT! de Madrid [F, https://www.infobae.com/america/agencias/2026/09/25/spotify-anuncia-la-llegada-a-espana-de-partner-program-iniciativa-para-convertir-los-podcast-en-negocios-sostenibles/ , comprobado el 29-09-2026]. La nota de TechCrunch del 17-09-2026 solo confirma la expansión a 35 países, sin fecha para España. Requisitos: alojar el programa en Spotify for Creators, al menos 3 episodios, 2.000 horas de consumo y 1.000 de audiencia en los últimos 30 días (https://support.spotify.com/us/creators/article/spotify-partner-program/). Hay **dos fuentes de ingreso, y no son iguales para audio y vídeo**:
1. **Reparto de publicidad (50 %)** de los anuncios que Spotify inserta en el programa, "both on and off Spotify". Vale para audio y vídeo, pero exige **insertar al menos un corte publicitario por episodio**: "You need to insert at least one ad break into an episode in order to earn any ad revenue".
2. **Ingreso Premium por vídeo:** Spotify paga según el consumo de **episodios de vídeo** por usuarios Premium, a los que sirve el programa sin anuncios dinámicos. Los oyentes que escuchan "any non-video episodes" solo generan ingresos por anuncios. También exige al menos un corte de anuncio insertado en el episodio de vídeo.

**Consecuencias para el producto [S]:**
- **El videopódcast es la vía principal del SPP**, porque es el único formato que cobra el consumo Premium, y ese consumo llega sin anuncios (compatible con el "sono seguro").
- **El feed de solo audio, dentro del SPP, solo cobra publicidad.** Y como los anuncios del SPP se sirven también fuera de Spotify, un corte mal puesto despertaría al oyente en Apple o iVoox.
- **Regla:** un único corte, en **00:00** (equivale al pre-roll, §5), nunca a mitad del episodio. Si en la Etapa 1 la escucha en audio fuera de Spotify pesa más que la de Spotify, se valora no activar el SPP en el feed de audio.

### 9.2 Tabla de derivados

| Formato | Qué es | Para qué | Etapa | Base |
|---|---|---|---|---|
| **Videopódcast en Spotify** | El vídeo completo (sin la cola larga; con 10 min de lluvia) subido como episodio de vídeo a Spotify for Creators, con un solo corte de anuncio en 00:00 | **Única vía al ingreso Premium del SPP** (§9.1). El formato "para dormir" acumula horas con pocos oyentes (`ingresos_alt.md` §3.1) | 1-2 | [F Spotify Support; `ingresos_alt.md` §3.1] |
| **Pódcast de audio (RSS)** | El mismo máster de audio, con 10 min de cola, en Apple Podcasts e iVoox (y en Spotify como audio si el feed se aloja allí) | Otra superficie de escucha nocturna; iVoox concentra oyentes de historia en España. En Spotify el audio solo cobra publicidad (§9.1); en iVoox, suscripción o pago único | 1 | Historia, 2.º género en iVoox (14,1 %) [F `audiencia.md` §6.2]. Cómo se reparte técnicamente el feed de audio de un programa con vídeo en Spotify for Creators: [S, verificar al abrir la cuenta] |
| **"Postais" verticales (Shorts)** | 60-90 s: un solo plano oscuro, un párrafo de la entrada o del Acto III, lluvia de fondo; texto "episodio completo na canle" | Descubrimiento. Nunca un corte rápido: tienen el mismo tono calmado que el producto. Los Shorts admiten hasta 3 min desde el 15-10-2024 | 1 | [F YouTube Help, 3-min Shorts] |
| **Capítulo suelto** | 8-15 min, un capítulo autosuficiente del Acto II (p. ej. "Martiño chega de Panonia", §11.2) | Consumo diurno o "sesta", y SEO de temas concretos | 2 | [S] |
| **Compilaciones de 4-8 h** | Serie completa encadenada ("Toda Gallaecia para durmir") | Watch time de noche entera. **Solo** con transiciones nuevas y presentación propia, para no caer en "reused content" | 2 | [S, `retornos.md` §6] |
| **Pistas de audio es/pt** | El mismo vídeo con pistas de audio multilingües | Ampliar el mercado sin abrir canales. YouTube abrió las pistas multilingües a todos los creadores (sep-2025); en el piloto, más del 25 % del watch time vino de idiomas no principales | 3 | [F TechCrunch 10-09-2025] |
| **Versión sin anuncios / descargable** | Membresía o pago único (packs de iVoox "Pack Irmandiños 6 h") | Monetización de oyentes fieles sin despertar a nadie | 2 | [F `ingresos_alt.md` §3.2] |

**Regla común [S]:** ningún derivado rompe el "sono seguro". Las postais no llevan música fuerte ni texto parpadeante; ni el pódcast ni el videopódcast llevan cortes publicitarios después de 00:00.

---

## 10. Nombre del canal: 5 propuestas y comprobación básica de disponibilidad

**Método de comprobación [COMP, 29-09-2026]:**
- Handle de YouTube: `curl https://www.youtube.com/@handle` (404 = no existe; control positivo: @bretema devuelve 200).
- Canales parecidos: búsqueda de YouTube filtrada por canal.
- Dominio: RDAP (`rdap.org`, que redirige a `rdap.nic.gal`; 404 = no registrado; control positivo: academia.gal y crtvg.gal devuelven 200).
- Pódcast homónimos: iTunes Search API (country=ES).
- Significado: Dicionario da RAG.

**Pendiente (no hecho):** búsqueda de marcas en la OEPM y la EUIPO, handles de Instagram y TikTok y búsqueda en Spotify.

| # | Nombre | Significado (RAG) | YouTube @handle | Dominio .gal | Conflictos encontrados | Valoración |
|---|---|---|---|---|---|---|
| **1 (recomendado)** | **Serán** · Historia de Galicia para durmir | "Parte do día que vai desde que comeza a pórse o sol ata que se fai noite"; "reunión… que se facía destas horas" [F, https://academia.gal/dicionario/-/termo/serán]. Galipedia: en los seráns "contábanse contos" [F, https://gl.wikipedia.org/wiki/Serán] | **@seran libre**; @serangalicia libre | **seran.gal libre**; serangalicia.gal libre; seran.es libre | Un canal "SERÁN" de una marca de moda pakistaní (@seranbydynasty, 531 suscriptores) y canales de personas apellidadas Seran. Ningún pódcast "Serán" en Apple España. | **Cultural y exacto:** la hora (el anochecer) y el acto de contar historias alrededor del fuego. Corto, sin acentos problemáticos en el handle. **Contra:** en castellano "serán" es un verbo, lo que diluye la búsqueda. Se compensa con el subtítulo fijo "Historia de Galicia para durmir". |
| 2 | Á Luz do Candil | Candil: lámpara de aceite tradicional | @aluzdocandil libre | aluzdocandil.gal libre (y .com libre) | "Crónicas del Candil" y "Amores de Candil" (castellano, pequeños) | Muy evocador y visual (encaja con el acento "candea"). **Contra:** largo, con una "Á" que complica el handle y la escritura en el móvil. |
| 3 | Historia para Durmir | Descriptivo | @historiaparadurmir libre | historiaparadurmir.gal libre (y .com libre) | Muchos "Historias para dormir" en castellano (p. ej. @HistoriasParaDormir0125, 59,3K) | El **mejor SEO en galego**, pero genérico, difícil de proteger como marca y confundible con canales IA en castellano. **Mejor como subtítulo fijo** que como nombre. |
| 4 | Arrolo | "Canto ou son para apazugar ou adormentar o neno"; sinónimo de *nana* [F, https://academia.gal/dicionario/-/termo/arrolo] | @arrolo libre | arrolo.gal libre | Solo nombres de persona (Arrolo) | Bonito y galego puro, pero **suena a contenido infantil**. Riesgo de que YouTube lo trate como "made for kids" o de confundir al público. Descartado como nombre principal; utilizable como nombre de sección ("o arrolo final"). |
| 5 | A Lareira da Historia | Lareira: hogar, fuego de la casa | @lareiradahistoria libre | lareiradahistoria.gal libre | **Espacio saturado:** pódcast en galego "A Lareira" (Raquel Besteiro), "Contos na lareira", "Ecos da Lareira", "À'Lareira" (pt) [COMP, iTunes y YouTube] | Riesgo de confusión con pódcast galegos ya existentes. **Descartado.** |

**Descartado en la comprobación:** "Brétema" (@bretema ya existe en YouTube [COMP]; además es un nombre muy usado por negocios gallegos [S]).

**Recomendación:** nombre **"Serán"**, subtítulo fijo **"Historia de Galicia para durmir"**, handle **@seran** (o @serangalicia si se quiere coherencia con el dominio) y dominio **seran.gal**. Como está libre, **conviene registrar hoy el handle y el dominio** (coste del dominio .gal: supuesto de ~20-30 €/año, sin verificar) y hacer la búsqueda en la OEPM antes de invertir en identidad visual.

---

## 11. Episodio 1: hoja de producción de *O Reino suevo de Gallaecia (411-585)*

Esta sección convierte la plantilla (§3-§7) en un encargo ejecutable. Es la entrada directa del pipeline (investigador → lingüista → director → prompts visuales → montador → QA).

### 11.1 Ficha del episodio

| Campo | Valor |
|---|---|
| Serie | "Gallaecia" (1/5) |
| Duración | 75:00 narrados + 25:00 de cola (total 1:40:00) |
| Palabras presupuestadas | **8.435** (media 112 palabras/min; Acto III a ~105) |
| Caracteres TTS estimados | ~52.300 (8.435 × 6,2) [S] |
| Imágenes | 74, de ellas 3 mapas propios (1 imagen cada ~62 s durante la narración) |
| Ambientes | AMB-LOUSA (base), AMB-CARBALLEIRA, AMB-LAREIRA, AMB-REGO (§6.2) |
| Voz y render | La ganadora del kit (§3A.1). Parámetros por acto de §3A.3 recalculados con su r_nat. Léxico v0 de §3A.4 (23 nombres y ~30 palabras trampa), validado antes de renderizar |
| Anuncios | Ninguno (Etapa 1, sin YPP) → lleva "sen cortes" en título y miniatura (regla 13) |
| Hilo narrativo | Del ruido de las invasiones al silencio de las parroquias. El fin del reino (585) se cuenta en el Acto I, como anticipación serena, para que el episodio termine en lo que perdura y no en una conquista. |

### 11.2 Escaleta: 10 capítulos con minutado, palabras, activación, fuentes y ambiente

Activación (1-5) = sustos, suspense o preguntas abiertas; debe ser no creciente desde el capítulo 4 (§4.1). Las fuentes de cada capítulo van al anexo interno de verificación, y las principales, a la descripción.

| Cap. | Título (galego) | Inicio-fin | Min | Palabras | Act. | Contenido | Fuentes primarias | Fuentes secundarias | Ambiente |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **Entrada: chove sobre Braga** | 0:00-2:30 (umbral 0:00-0:15) | 2,5 | 240 | 1 | Escena: la lluvia sobre las murallas de Braga de noche. "Boas noites. Isto é Serán…". Qué se cuenta esta noche; permiso para dormirse. | — | Galipedia, *Bracara Augusta* | AMB-LOUSA + sello sonoro |
| 2 | **O fin dun mundo: Gallaecia arredor do ano 400** | 2:30-9:30 | 7 | 800 | 2 | La provincia romana: Bracara, Lucus, Asturica; calzadas, villas, castros aún habitados; un imperio que ya no llega. | Hidacio, *Crónica* (prefacio); Orosio, *Historiae adversus paganos* (libro VII) | Díaz (2011), cap. 1; Torres Rodríguez (1977) | AMB-CARBALLEIRA |
| 3 | **Os que chegaron do Rin (409-411)** | 9:30-17:00 | 7,5 | 860 | **3** | Suevos, vándalos y alanos cruzan los Pirineos (409). Los años duros, contados con distancia: "o cronista fala de fame e de peste" (sin detalle). El reparto de las provincias "por sortes" (411): a los suevos, el extremo occidental de Gallaecia. | Hidacio, entradas de 409-411 | Díaz (2011); Galipedia *Reino Suevo* | AMB-CARBALLEIRA + viento suave |
| 4 | **Reis en Braga, e como remata a historia (411-585)** | 17:00-23:00 | 6 | 690 | **3** | Hermerico, Requila, Requiario (católico hacia 448-449); la derrota del Órbigo (456), en una sola frase; el siglo VI; y el final anticipado: en 585 Leovixildo incorpora el reino al visigodo. "Pero entre o principio e o fin houbo século e medio de vida." | Hidacio; Isidoro de Sevilla, *Historia Suevorum*; Xoán de Biclaro, *Chronicon* (585) | Galipedia *Reino Suevo* (Órbigo 456; catolicismo 448-449; fin 585); Díaz (2011) | AMB-LOUSA |
| 5 | **O bispo que contaba os anos** | 23:00-28:00 | 5 | 575 | 2 | Hidacio: nacido en la Limia, obispo de Aquae Flaviae (Chaves) desde 427, viaje a la Galia para hablar con el general Aecio, un breve cautiverio; su crónica termina en 468. Después, un siglo casi sin textos: "o silencio das fontes". | Hidacio (autobiográfico en la *Crónica*) | Galipedia *Hidacio*; RAH, *Historia Hispánica*; ed. galega de Candelas Colodrón (2004) | AMB-LAREIRA (chasquidos filtrados) |
| 6 | **Un século en silencio: a vida nas vilas e nos castros** | 28:00-39:00 | 11 | 1.265 | 1 | Lo que dice la arqueología cuando callan las crónicas: villas reaprovechadas, castros reocupados, centeno y castañas, ganado, caminos romanos que siguen en uso. Reconstrucción marcada como tal ("podemos imaxinar"). | (Silencio de las fuentes escritas: se dice así) | Díaz (2011), capítulos de sociedad y economía; Sánchez Pardo (2014) | AMB-LOUSA + AMB-REGO |
| 7 | **Martiño chega de Panonia** | 39:00-50:00 | 11 | 1.265 | 1 | Dumio, el monje de Panonia, la carta *De correctione rusticorum*: pan en las fuentes, candelas en piedras, árboles y encrucijadas, las calendas de enero, los días con nombres de dioses. **Prosa de muestra en §11.5.** | Martiño de Dumio, *De correctione rusticorum* (texto latino); Gregorio de Tours, *Historia Francorum* | Tradución galega de Pedret Casado (revista *Nós*, 1932); Galipedia *Martiño de Dumio*; EGU | AMB-LOUSA + AMB-REGO |
| 8 | **O mapa das parroquias** | 50:00-62:00 | 12 | 1.380 | 1 | Los concilios de Braga (sin años en voz: "no primeiro concilio"); el *Parochiale suevorum*: trece diócesis, iglesia por iglesia. Se leen solo unos pocos nombres que aún se reconocen (≤1 nombre nuevo/min). | *Parochiale suevorum* (copia en el *Liber Fidei*, doc. 551); actas de los concilios I y II de Braga | Sánchez Pardo (2014); Fernández Calo (2015, en galego); Galipedia *Parochiale suevorum* | AMB-LAREIRA + lluvia fuera |
| 9 | **O que quedou** | 62:00-73:30 | 11,5 | 1.210 | 1 | Monedas, piedras labradas, un sarcófago; los nombres de las parroquias; la parroquia de Suevos (Arteixo); las fuentes donde aún se deja algo; las "ferias" de la semana al otro lado del Miño. Sin fechas. **Prosa de muestra en §11.6.** | *Parochiale suevorum* | Galipedia *Suevos, Arteixo*; culturagalega.gal (sarcófago de Martiño, exposición Galicia 100); Galipedia *Martiño de Dumio* (nombres de los días) | AMB-LOUSA, alejándose |
| 10 | **Despedida** | 73:30-75:00 | 1,5 | 150 | 0 | Respiración, peso del cuerpo, la lluvia. "Boas noites." | — | — | AMB-LOUSA |
| — | *Só chuvia* (cola) | 75:00-1:40:00 | 25 | 0 | 0 | Pantalla casi negra; fundido final de 60 s. | — | — | AMB-LOUSA |

**Totales:** 8.435 palabras en 75 min; Acto I (caps. 2-5) = 2.925 palabras (35 %); Acto II (caps. 6-8) = 3.910 (46 %); Acto III (cap. 9) = 1.210 (14 %). Serie de activación: 1-2-3-3-2-1-1-1-1-0 (pico entre el 12 % y el 31 % del episodio, como pide §4.1).

**Datos que el auditor debe fijar antes de grabar** [pendiente de verificación en la fuente primaria o en Díaz 2011]: (a) conversión de Requiario, 448 o 449 (Galipedia da 449 en el texto y 448 en la cronología: se dice "arredor da metade do século V"); (b) la fecha exacta del cautiverio de Hidacio (460) y del viaje a Aecio (431), que no se leen en voz alta con año; (c) que la parroquia de Suevos (Arteixo) tenga relación etimológica con los suevos, que el guion **no afirma**: solo dice que se llama así.

### 11.3 Bibliografía del episodio (con URL)
**Fuentes primarias**
- Hidacio, *Crónica* (379-468). Edición galega: *O cronicón de Hidacio*, trad. César Candelas Colodrón, Toxosoutos (col. Trivium, 13), 2004, ISBN 978-84-96259-13-3 [F, ficha: https://www.buscalibre.us/libro-cronicon-de-hidacio-o-trivium-n-13-segiundo-premio-historia-medieval-de-galicia/9788496259133/p/3323533]. Versión castellana antigua de dominio público (Macías, 1906): https://archive.org/details/cronicndeidacio00idatgoog
- Martiño de Dumio, *De correctione rusticorum* (c. 572-574), texto latino: https://www.thelatinlibrary.com/martinbraga/rusticus.shtml ; corpus galego CODOLGA: https://corpus.cirp.gal/codolga/fontes/2018_de_correctione_rusticorum . Traducción galega de Paulino Pedret Casado en *Nós* (1932) [F: https://academia.gal/membro/-/membro/paulino-pedret-casado].
- *Parochiale suevorum* (s. VI; 134 parroquias en trece diócesis): https://gl.wikipedia.org/wiki/Parochiale_suevorum
- Isidoro de Sevilla, *Historia Suevorum*; Xoán de Biclaro, *Chronicon*; Gregorio de Tours, *Historia Francorum*; Orosio, *Historiae* (citados en https://gl.wikipedia.org/wiki/Reino_Suevo).

**Bibliografía secundaria**
- Pablo C. Díaz, *El reino suevo (411-585)*, Madrid, Akal, 2011, 302 pp.: https://www.akal.com/libro/el-reino-suevo-411-585_34123/
- Casimiro Torres Rodríguez, *El reino de los suevos (Galicia sueva)*, A Coruña, Fundación Pedro Barrié de la Maza, 1977: https://www.iberlibro.com/9788485319114/Reino-Suevos-Galicia-Sueva-Torres-8485319117/plp
- José Carlos Sánchez Pardo, "Organización eclesiástica y social en la Galicia tardoantigua. Una perspectiva geográfico-arqueológica del Parroquial Suevo", *Hispania Sacra* 66 (134), 2014, pp. 439-480, doi:10.3989/hs.2014.058.
- Martín Fernández Calo, "Plinio, o Parroquial Suevo, e a evolución estrutural do poder local galaico na Antigüidade", *Gallaecia*, 2015 (en galego; citado en Galipedia, *Parochiale suevorum*).
- Galipedia: *Reino Suevo* https://gl.wikipedia.org/wiki/Reino_Suevo ; *Hidacio* https://gl.wikipedia.org/wiki/Hidacio ; *Martiño de Dumio* https://gl.wikipedia.org/wiki/Marti%C3%B1o_de_Dumio ; *Suevos, Arteixo* https://gl.wikipedia.org/wiki/Suevos,_Arteixo
- Enciclopedia Galega Universal, *De correctione rusticorum*: https://egu.xunta.gal/gl/termo/109948/de-correctione-rusticorum
- RAH, *Historia Hispánica*, biografía de Hidacio: https://historia-hispanica.rah.es/biografias/22911-hidacio
- culturagalega.gal, "Nas orixes do reino" (sarcófago de Martiño de Dumio): https://culturagalega.gal/noticia.php?id=26577

**Nota:** la bibliografía secundaria de referencia está sobre todo en castellano; el galego aporta la edición de Hidacio, la traducción de Martiño, Fernández Calo y la Galipedia. Para la Etapa 2, buscar un asesor de la USC (p. ej. del ámbito de Sánchez Pardo) para revisar los guiones de la serie "Gallaecia" [S].

### 11.4 Plano visual: 74 imágenes con prompts "noite atlántica"
Cada prompt = ESTILO + MOTIVO + LUZ + NEGATIVO (§7.2). Aquí se escribe solo el **MOTIVO**; la LUZ la fija el acto. ★ = prompt clave, escrito completo abajo. M = mapa propio (no IA).

| Cap. | N.º | Planos (motivo) |
|---|---|---|
| 1 | 3 | 01★ murallas de Braga bajo la lluvia, de noche · 02 una ventana con luz de candea en una casa de piedra · 03 rego que corre bajo la lluvia |
| 2 | 8 | 04★ calzada romana entre carballos con niebla · 05 M: Gallaecia romana (Bracara, Lucus, Asturica) · 06 villa romana con pórtico y huerta · 07 castro habitado en una ladera · 08 muralla de Lugo al atardecer, de lejos · 09 miliario cubierto de liquen · 10 barca en un río ancho · 11 campos al anochecer con humo de hogares |
| 3 | 8 | 12★ columna de carros y gente a pie, diminutos, cruzando un paso de montaña en la niebla · 13 campamento de noche con hogueras pequeñas, a gran distancia · 14 villa romana abandonada con tejado hundido · 15 campos sin segar bajo la lluvia · 16 río crecido · 17 M: reparto de 411 (suevos al noroeste) · 18 familia en silueta junto a un carro, de espaldas · 19 camino vacío hacia el oeste |
| 4 | 7 | 20★ Braga de noche vista desde una colina, pocas luces · 21 sala con columnas y un trono vacío en penumbra · 22 pila bautismal de piedra con una vela · 23 río ancho al atardecer, llanura vacía (Órbigo, sin batalla) · 24 moneda sueva (tremís) sobre paño oscuro · 25 estandarte caído en la hierba, sin cuerpos · 26 horizonte de colinas con nubes bajas |
| 5 | 5 | 27★ monje escribiendo a la luz de una vela, visto de espaldas · 28 puente romano de Chaves con niebla · 29 camino hacia el norte bajo la lluvia · 30 cielo nocturno con un cometa tenue · 31 pergamino a medio escribir, pluma quieta |
| 6 | 10 | 32★ aldea de casas de piedra y colmo al anochecer · 33 castiñeiros en otoño con lluvia · 34 cercado con ovejas quietas bajo la niebla · 35 muíño de río pequeño · 36 horno de pan apagado, brasas · 37 campo de centeno al anochecer · 38 camino romano cubierto de hierba · 39 telar con hilo, sin tejedora · 40 fuente de piedra con musgo · 41 humo que sube de un tejado bajo la lluvia |
| 7 | 10 | 42★ monasterio pequeño de piedra con huerta, Dumio, de noche · 43★ fuente de piedra con un pedazo de pan en el borde · 44★ velas encendidas sobre una gran roca en una encrucijada · 45 roble viejo con una vela a sus pies · 46 mesa de madera adornada con laurel · 47 manos hilando junto al fuego (sin cara) · 48 rego junto a un huerto de noche · 49 monje caminando de espaldas por un sendero · 50 carta sellada sobre una mesa · 51★ vela que se apaga entre dos piedras en un otero |
| 8 | 11 | 52★ sala de concilio en penumbra con bancos de piedra vacíos · 53 M: las trece diócesis del *Parochiale* · 54 iglesia prerrománica pequeña entre prados · 55 campanario de espadaña bajo la lluvia · 56 manuscrito abierto con una lista de nombres (sin texto legible) · 57 valle con varias iglesias lejanas y humo · 58 camino entre dos parroquias · 59 cruz de piedra en un cruce · 60 puerta de iglesia con luz dentro · 61 niebla sobre un valle · 62 lámpara de aceite sobre un atril |
| 9 | 9 | 63★ sarcófago de piedra en una cripta con una sola vela · 64 moneda sobre piedra, casi en negro · 65 iglesia rural de San Martiño bajo la lluvia (Suevos) · 66★ fuente con una flor y una vela pequeña · 67 señal de camino con un nombre de parroquia (sin texto legible) · 68 colinas del sur y del norte bajo la lluvia · 69 río hacia el mar, casi oscuro · 70 niebla que baja al fondo del valle · 71★ brasas cubiertas en un hogar, casi negro |
| 10 | 1 | 72 ventana con lluvia, sin luz |
| Cola | 2 | 73 tejado de lousa bajo la lluvia, luminancia <10 · 74 fundido a casi negro |

**Prompts clave completos (MOTIVO + LUZ; ESTILO y NEGATIVO se añaden automáticamente):**

| ID | Prompt |
|---|---|
| E1-01 | `the Roman city walls of Bracara Augusta at night in steady rain, wet granite, a few distant warm windows, puddles reflecting faint light` + LUZ Acto I |
| E1-04 | `a straight Roman road paved with worn stones crossing an oak forest in thick mist, moss on the stones, no people` + LUZ Acto I |
| E1-12 | `a long line of tiny carts and people on foot crossing a mountain pass in the mist, seen from very far away, calm, no weapons visible` + LUZ Acto I |
| E1-20 | `a late antique town seen from a hill at night, low stone houses, a basilica roof, very few lights, rain clouds` + LUZ Acto I |
| E1-27 | `an old bishop seen from behind writing on parchment at a wooden desk, a single candle, stone wall, rain on a small window` + LUZ Acto I |
| E1-32 | `a small hamlet of granite houses with thatched roofs at dusk, smoke rising, chestnut trees, wet path` + LUZ Acto II |
| E1-42 | `a small early medieval stone monastery with a walled vegetable garden, a stream beside it, night, one lit window` + LUZ Acto II |
| E1-43 | `a small granite fountain by a path, a piece of bread resting on its edge, water flowing, moss, night` + LUZ Acto II |
| E1-44 | `several small candles burning on top of a large boulder at a crossroads of two dirt paths, oak trees, night mist` + LUZ Acto II |
| E1-51 | `a single small candle between two stones on a hilltop, about to go out, rain, distant valley in darkness` + LUZ Acto II |
| E1-52 | `an empty early medieval council hall, stone benches, columns, a lamp on a lectern, dim` + LUZ Acto II |
| E1-63 | `a plain stone sarcophagus in a small crypt, one candle, deep shadows` + LUZ Acto III |
| E1-66 | `a stone fountain with a single wildflower and a tiny candle at its edge, rain, almost dark` + LUZ Acto III |
| E1-71 | `embers covered with ash in a stone hearth, faint orange glow, the rest of the room in darkness` + LUZ Acto III |

**Comprobaciones visuales de QA:** luminancia media por capítulo (caps. 2-8: 40-70; cap. 9 y cola: <20); ningún plano con caras, armas en alto o sangre; el tremís (plano 24), el sarcófago (63) y los lugares reales (08 muralla de Lugo, 28 puente de Chaves, 65 iglesia de Suevos) se hacen desde foto real o de dominio público repintada con el estilo (§7.2), para no inventar un objeto o un monumento conocido; mapas revisados contra el *Parochiale* y la Galipedia.

### 11.5 Prosa de muestra: Acto II, capítulo 7 "Martiño chega de Panonia" (600 palabras) [S: borrador para revisión lingüística y kit A/B]

> A pouca distancia das murallas de Braga, alí onde o camiño deixa atrás as últimas casas e empeza a subir entre leiras, hai un mosteiro novo. Non é grande. Ten uns muros de pedra sen labrar, un tellado de tella, quizais aproveitada dalgunha vila romana que xa ninguén habita, e unha horta pechada cun valado baixo. Ao pé da horta corre un rego pequeno, tan pequeno que só se oe de noite, cando todo o demais cala. Ese lugar chámase Dumio.
>
> O home que o levantou chegara de moi lonxe. Nacera en Panonia, unha terra de grandes chairas e ríos lentos, no corazón de Europa, e antes de chegar a Gallaecia percorrera camiños que a xente de aquí nin sequera sabía imaxinar. Sabía grego. Traducira ao latín as palabras dos vellos monxes do deserto de Exipto, frases curtas e sinxelas sobre a paciencia e o silencio. Chamábase Martiño.
>
> Podemos imaxinar os seus primeiros anos aquí. Tivo que aprender os nomes dos regos e dos outeiros. Tivo que aprender cando se sementa o centeo e cando se sega, en que semanas a néboa non levanta en todo o día e en que noites o vento chega do mar cheirando a sal. Camiñou moito. Ía de aldea en aldea, ás veces só, ás veces cun ou dous monxes, e paraba onde había lume.
>
> E o que viu nesas aldeas deixouno escrito, anos máis tarde, nunha carta longa a outro bispo, que lle pedira consello.
>
> Viu fontes. Fontes pequenas, de pedra, á beira dun camiño, onde a auga saía fría todo o ano. E viu que a xente, ao pasar, botaba nelas un anaco de pan. Non por descoido, senón amodo, con coidado, como quen deixa unha ofrenda a alguén que vive alí dentro e que merece respecto. Os vellos dicían que nas fontes vivían ninfas, e nos ríos, lamias.
>
> Viu candeas acesas enriba das pedras grandes, ao pé das árbores vellas e nas encrucilladas, alí onde un camiño se parte en dous. Pequenas luces que ninguén vixiaba e que se ían apagando soas, unha por unha, coa humidade da noite.
>
> Viu que o primeiro día de xaneiro se celebraba como se dese día dependese o ano enteiro: quen comía ben e estaba contento ao comezo do ano, dicían, así estaría ata o inverno seguinte. E por iso ese día ninguén quería que lle faltase nada na mesa.
>
> Viu que as mulleres, cando tecían, nomeaban unha antiga deusa, e que había días do ano en que se enfeitaban as mesas e se poñían ramas de loureiro. Viu que a xente lles daba aos días da semana os nomes dos vellos deuses: o día de Marte, o día de Mercurio, o día de Venus.
>
> A Martiño todo aquilo parecíalle un erro, e así o escribiu. Pero lendo hoxe a súa carta, o que máis chama a atención non é a reprensión. É a paciencia. Martiño non ameaza. Explica, pon exemplos, volve explicar. Escribe como quen lle fala a xente cansa, diante dun lume, ao remate dunha xornada longa, sen présa.
>
> E, sen querelo, deixounos unha das poucas fiestras que temos a aquela Galicia de hai tantos séculos. Unha Galicia de fontes con pan, de candeas nas encrucilladas, de mulleres que falan baixiño mentres o fío lles pasa entre os dedos.
>
> Pola noite, en Dumio, os monxes rezan e despois calan. Fóra chove. É unha chuvia miúda, desas que non se ven e que só se oen no tellado. O rego segue correndo ao pé da horta. Alá enriba, nalgún outeiro, unha candea que alguén deixou ao solpor aínda arde un pouco, entre dúas pedras, antes de apagarse.

**Anexo de verificación de este fragmento:** Panonia, llegada a Gallaecia y fundación de Dumio junto a Braga (Galipedia, *Martiño de Dumio*); traducción del griego de las sentencias de los padres del desierto de Egipto (*Sententiae Patrum Aegyptiorum*, obra atribuida a Martiño; a confirmar en Díaz 2011); carta al obispo Polemio de Astorga, que le pidió que escribiera sobre el origen de los ídolos (Wikipedia en inglés, *De correctione rusticorum*); "ad petras et ad arbores et ad fontes et per trivia cereolos incendere" y "panem in fontem mittere" (texto latino, The Latin Library); ninfas en las fuentes, lamias en los ríos, las mujeres que nombran a Minerva al tejer, mesas adornadas, laurel, calendas de enero y los días con nombres de dioses (mismo texto). **Reconstruido y marcado como tal:** los primeros años ("Podemos imaxinar"), el tejado "quizais" reaprovechado, la escena nocturna final.

**Chequeo contra las reglas del Acto II:** nombres propios nuevos en ~5,2 min: Dumio, Panonia, Europa, Exipto, Martiño (5 → ≤1/min); Braga y Gallaecia ya se presentaron en el Acto I, y los dioses de la semana cuentan como una sola enumeración. Sin cifras, sin preguntas retóricas, frases de 8-35 palabras con repeticiones deliberadas ("Viu…") que funcionan como letanía para dormir.

### 11.6 Prosa de muestra: Acto III, capítulo 9 "O que quedou" (~300 palabras) [S]

> Do reino dos suevos quedan poucas pedras. Non hai un castelo que visitar nin unha coroa gardada nun museo. Quedan unhas moedas pequenas, algunhas pedras labradas, o sartego onde descansou un bispo. E queda algo que non se ve, pero que está en todas partes.
>
> Cando alguén di o nome da súa parroquia, cando di que é de tal lugar e non doutro, está a falar, sen sabelo, unha lingua moi vella. Algúns deses nomes xa aparecían naquela lista que redactaron os bispos, igrexa por igrexa. Mudaron un pouco, como muda a voz dunha persoa co paso dos anos. Pero seguen aí. Preto do mar, no norte, hai unha parroquia que aínda se chama Suevos, e a súa igrexa, coma tantas outras do país, leva o nome de San Martiño.
>
> E seguen as fontes. Aínda hoxe hai fontes onde alguén deixa unha moeda, ou unha flor, ou unha candea pequena. Ninguén lembra ben por que. Faise, sen máis, como quen saúda.
>
> E alén do Miño, os días da semana aínda se contan dun xeito que ao vello monxe lle gustaría: segunda feira, terceira feira, cuarta feira. Sen deuses. Só días, un despois doutro, coma as contas dun colar que pasan devagar entre os dedos.
>
> Agora a chuvia volve ser a mesma chuvia. Cae sobre os outeiros do sur e sobre os do norte, sobre as leiras e sobre os tellados, sobre as pedras que xa estaban alí antes dos suevos e que seguirán alí despois de nós. Cae amodo, sen présa ningunha, como caeu aquela noite en Dumio, cando unha candea se apagou soa entre dúas pedras.
>
> O río leva a auga cara ao mar. A néboa baixa ata o fondo do val. Nunha casa, lonxe, alguén cobre as brasas do lume.
>
> E todo queda en silencio.

**Anexo de verificación:** monedas suevas (tremises) y sarcófago de Martiño (culturagalega.gal); la lista de los obispos = *Parochiale suevorum* (Galipedia); parroquia de Suevos (Arteixo, cerca de la costa norte) con iglesia de San Martiño (Galipedia, *Suevos, Arteixo*). El guion **no afirma** que el nombre venga de los suevos ni que ese San Martiño sea el de Dumio ("coma tantas outras do país"). Nombres de los días en portugués atribuidos por la tradición a Martiño (Galipedia, *Martiño de Dumio*); "segunda feira…" también son formas recogidas en galego [S, a confirmar en el DRAG por el lingüista]. La última imagen retoma la candea del capítulo 7 (repetición suave, §4.1).

**Chequeo contra las reglas del Acto III:** 0 fechas; nombres: Suevos, San Martiño, Miño (Dumio ya presentado) → 3 en ~2,9 min. En el capítulo completo (11,5 min) eso da ~0,26/min, dentro del ≤0,3 si el resto del capítulo no añade nombres nuevos. Presente contemplativo; frases que se alargan hacia el final y se cortan en seco solo en la última línea.

### 11.7 Protocolo de comparación ciega contra el listón [S]
- **Qué se compara:** (A) nuestras 600 palabras del §11.5 frente a las 351 palabras de narración del bloque A de `refs/sleep_reference_gl.md` a partir de "Durante séculos, as grandes cidades…" (la parte posterior a la CTA), completados con el tramo inicial del bloque (quitando la CTA) hasta igualar extensión; (B) nuestras ~300 del §11.6 frente a las últimas ~300 del mismo bloque.
- **Cómo:** textos sin título ni nombre del canal, en orden aleatorio, leídos por el promotor y su mujer y, en paralelo, por un juez LLM con rúbrica fija.
- **Criterios (1-5):** especificidad (datos concretos y verificables), imágenes concretas, curva (¿baja la activación?), ausencia de clichés, y un quinto solo para la lengua: corrección y naturalidad en galego, con `refs/galego_experto.md` como listón de norma.
- **Criterio de éxito:** empatar o ganar en al menos 3 de 5 criterios, y ninguna nota ≤2 en lengua. Si pierde, el lingüista reescribe y se repite antes de grabar.

### 11.8 Metadatos: título, descripción y comentario fijado (plantilla aplicada al Ep. 1)

**Título (83 caracteres; máximo de YouTube: 100):**
> O Reino suevo de Gallaecia (411-585) | Historia de Galicia para durmir · sen cortes

**Descripción** (los capítulos cumplen los requisitos de YouTube: el primero en 00:00, al menos tres, en orden y de al menos 10 s cada uno [F, https://support.google.com/youtube/answer/9884579]):

```
Esta noite imos á Gallaecia dos séculos V e VI, cando un pobo chegado do Rin fixo de Braga a capital dun reino. Contámolo amodo, cunha chuvia miúda de fondo, para que te deixes levar ata o sono.

Este vídeo non ten cortes publicitarios. Cando remata a narración quedan 25 minutos só de chuvia. Podes usar o temporizador de apagado de YouTube (na roda de axustes do reprodutor).

CAPÍTULOS
00:00 Entrada: chove sobre Braga
02:30 O fin dun mundo: Gallaecia arredor do ano 400
09:30 Os que chegaron do Rin (409-411)
17:00 Reis en Braga, e como remata a historia
23:00 O bispo que contaba os anos
28:00 Un século en silencio: a vida nas vilas e nos castros
39:00 Martiño chega de Panonia
50:00 O mapa das parroquias
1:02:00 O que quedou
1:13:30 Boas noites
1:15:00 Só chuvia

NOTA SOBRE O PROCESO
Este episodio fíxose con ferramentas de intelixencia artificial, baixo dirección e revisión humana:
· Guion: redactado coa axuda dun modelo de linguaxe a partir das fontes de abaixo. Unha persoa galegofalante revisou a lingua e contrastou cada dato coa súa fonte.
· Voz: sintética ([modelo e voz elixidos no kit A/B], [licenza]). Non imita ningunha persoa real.
· Imaxes: xeradas con IA. Son evocacións pictóricas, non reconstrucións arqueolóxicas nin retratos de persoas reais. Os mapas son de elaboración propia.
· Son: chuvia gravada en [lugar]; [créditos CC BY de Freesound, se os houber].
Se atopas un erro de lingua ou de historia, dínolo nos comentarios: corrixímolo e deixámolo anotado aquí.

FONTES
Hidacio, Crónica (ed. galega: O cronicón de Hidacio, trad. César Candelas Colodrón, Toxosoutos, 2004).
Martiño de Dumio, De correctione rusticorum (trad. galega de Paulino Pedret Casado, Nós, 1932).
Parochiale suevorum (séc. VI).
Pablo C. Díaz, El reino suevo (411-585), Akal, 2011.
Casimiro Torres Rodríguez, El reino de los suevos, Fundación Barrié, 1977.
J. C. Sánchez Pardo, "Organización eclesiástica y social en la Galicia tardoantigua", Hispania Sacra, 2014.
M. Fernández Calo, "Plinio, o Parroquial Suevo…", Gallaecia, 2015.
Galipedia: Reino Suevo, Hidacio, Martiño de Dumio, Parochiale suevorum.

Serán · Historia de Galicia para durmir. Un episodio novo cada dúas semanas.

Historia de Galicia para dormir, narrada en gallego: el reino suevo de Gallaecia (411-585). Sin anuncios intermedios.

#HistoriaDeGalicia #HistoriaParaDurmir #Galego
```

**Etiquetas** (castellano y galego): reino suevo, suevos Galicia, Gallaecia, historia de Galicia, historia para dormir, historia para durmir, Braga, Hidacio, Martín de Dumio, Martiño de Dumio, relatos para dormir en gallego.

**Comentario fijado** (el único sitio donde se pide algo, y solo por escrito):
```
Se aínda non adormeciches: boas noites outra vez.
Grazas por escoitar. Se esta historia che axudou a descansar, subscribirse e deixar un comentario axuda moito a que haxa máis noites coma esta, e non fai ningún ruído.
Cóntasnos desde onde nos escoitas? E se atopaches un erro de lingua ou de historia, dío aquí: corrixímolo.
Próximo episodio: Un día nunha aldea galega do século XV.
```

**Pantalla final:** muda, 20 s, al final de la cola (1:39:40-1:40:00), con el vídeo siguiente de la serie y el botón de suscripción (regla 10).

### 11.9 Checklist de salida del Episodio 1 (puerta antes de publicar)
- [ ] Palabras finales 8.000-8.900 y ritmo medido 105-130 (§3).
- [ ] Activación 1-2-3-3-2-1-1-1-1-0 confirmada por el auditor; ningún capítulo posterior al 4 sube.
- [ ] Los tres datos pendientes de §11.2 fijados en la fuente.
- [ ] Revisión lingüística completa del guion (norma RAG, lista negra). Nombres latinos sustituidos por su forma gallega en la voz (§3A.4).
- [ ] `lexico_gl.tsv` con todas las entradas del Ep. 1 marcadas `verificado`; `g2p_check` sin diferencias pendientes; lista de pendientes del guion vacía.
- [ ] Render: paso 0 hecho (r_nat medido), tabla de §3A.3 recalculada, ritmo por acto a ±5 % y Acto III entre un 8 % y un 12 % más lento que el II; semillas y `s_prev` archivados por frase.
- [ ] Comparación ciega del §11.7 superada.
- [ ] Audio: -16 LUFS ±1, true peak ≤ -1,5 dBTP, LRA ≤ 5 LU; escucha completa de los capítulos 1 y 9 y del 20 % del resto.
- [ ] Imagen: 74 planos, luminancias por acto, planos 08, 24, 28, 63 y 65 hechos desde foto real.
- [ ] Metadatos: capítulos válidos, "Nota sobre o proceso" con el modelo de voz real, bibliografía, línea en castellano.
- [ ] Hoja de licencias de sonido e imagen archivada.

---

## 12. Supuestos de producto que se convierten en pruebas (entrada para las puertas de decisión)

| Hipótesis [S] | Cómo se prueba | Criterio de éxito propuesto |
|---|---|---|
| 115 palabras/min en galego suenan naturales y "dormibles" | Kit A/B ciego (§3A.1) con el promotor y su mujer. La voz finalista se renderiza a 105, 115 y 125 percibidas variando solo las pausas, con V fija | La voz y la velocidad ganadoras obtienen ≥4/5 en "durmiríame con isto", ninguna descalificación y ≥27/30 en las frases trampa |
| El estiramiento ≤10 % no produce "voz de goma" | Misma muestra con V = 1,00 / 1,05 / 1,10 / 1,15 y las pausas recalculadas para igualar el ritmo percibido | El jurado no marca "vocales arrastradas" hasta el tope fijado; si lo marca antes, el tope baja |
| REF-CALMA mejora la calma de StyleTTS2 | Brais y Celtia con la configuración de la ficha frente a REF-CALMA y `beta` 0,6 (§3A.2) | +1 punto de media en (b) calma sin perder en (a) naturalidad |
| El guion IA en galego alcanza el listón | Protocolo de §11.7 con las muestras de §11.5-11.6 | Empata o gana en al menos 3 de 5 criterios y ninguna nota ≤2 en lengua |
| La curva descendente retiene mejor que el arco documental | Retención en Studio: % de audiencia a los 10 y a los 30 min; comparar el Ep. 6 (irmandiños, tema con conflicto) con los Ep. 1-4 | Retención a 10 min ≥ 50 % y duración media de visionado ≥ 25 min en 75 min [S, sin benchmark galego] |
| La puntuación L del catálogo predice el rendimiento | Correlación entre L y vistas/retención de los 6 episodios de la Etapa 1 | Si los Ep. 5-6 (experimentos) superan a los Ep. 1-4, se recalibran las anclas de Dem y D |
| Quitar la CTA hablada no hunde la suscripción | Comparar la tasa de suscripción por 1.000 vistas con la de canales pequeños; alternativa: una frase suave de despedida en 3 episodios | Tasa ≥ 1 % de las vistas (`retornos.md` §0.2 usa 1-2 %) |
| El ambiente propio evita reclamaciones | Registro de reclamaciones de Content ID por episodio | 0 reclamaciones en los 6 primeros episodios |
| El videopódcast de Spotify suma horas al SPP | Horas de consumo en Spotify en los 30 días posteriores a cada publicación | Trayectoria hacia 2.000 h/30 días al final de la Etapa 1 (`ingresos_alt.md` §3.1) |
| "Serán" se entiende como marca | Mini encuesta a 10 conocidos galegofalantes: "¿qué esperas de un canal llamado Serán?" | ≥7 de 10 lo asocian a noche, historias o tradición |

---

## 13. Fuentes citadas en esta pieza

**Investigación previa del proyecto (con sus propias URLs):** `research/formato.md`, `research/audiencia.md`, `research/retornos.md`, `research/voz_guion.md`, `research/ingresos_alt.md`, `refs/sleep_reference_gl.md`, `refs/galego_experto.md`.

**Verificadas o añadidas el 29-09-2026:**
- History at Night, "The Great Maya Collapse": https://www.youtube.com/watch?v=hbufma0ZlUw
- History Time, "After Rome": https://www.youtube.com/watch?v=sXBgNNtEJ6M
- Relatos para Dormir: https://www.youtube.com/watch?v=3uBP9QaWfPM
- Sleepless Historian: https://www.youtube.com/watch?v=9jnekLeHz3c
- Phoebe Smith (Calm), Slate: https://slate.com/human-interest/2018/05/phoebe-smith-sleep-story-writer-for-the-calm-app-on-the-art-of-boring-people-to-sleep.html
- Normalización de YouTube (-14 LUFS, solo baja): https://productionadvice.co.uk/stats-for-nerds/
- Control de anuncios antes y después (2023): https://www.marketingbrew.com/stories/2023/09/08/youtube-scraps-some-creator-ad-controls-builds-out-livestream-ad-capabilities ; ayuda oficial de formatos: https://support.google.com/youtube/answer/2467968?hl=en
- Capítulos de YouTube (requisitos): https://support.google.com/youtube/answer/9884579?hl=en
- Temporizador de apagado de YouTube: https://tech.yahoo.com/streaming/articles/youtube-sleep-timer-best-feature-191515174.html
- Reclamaciones de Content ID por ruido blanco: https://www.tubefilter.com/2018/01/05/white-noise-youtube-content-id/
- Freesound: https://freesound.org
- Shorts de hasta 3 minutos: https://support.google.com/youtube/answer/15424877?hl=en ; https://variety.com/2024/digital/news/youtube-shorts-maximum-video-length-three-minutes-1236166349/
- Pistas de audio multilingües para todos los creadores: https://techcrunch.com/2025/09/10/youtubes-multi-language-audio-feature-for-dubbing-videos-rolls-out-to-all-creators/
- **Spotify Partner Program, página oficial (requisitos; reparto de anuncios; ingreso Premium solo para vídeo; corte obligatorio):** https://support.spotify.com/us/creators/article/spotify-partner-program/ ; expansión a 35 países: https://techcrunch.com/2026/09/17/spotify-expands-its-partner-program-for-podcasts-to-35-new-countries/
- 404 Media (glitch de TTS, ola de "boring history"): https://www.404media.co/ai-generated-boring-history-videos-are-flooding-youtube-and-drowning-out-real-history/
- Dicionario da RAG, "serán": https://academia.gal/dicionario/-/termo/serán ; "arrolo": https://academia.gal/dicionario/-/termo/arrolo
- Galipedia, "Serán": https://gl.wikipedia.org/wiki/Serán (y las páginas de cada tema del catálogo, enlazadas en §8.2)
- Dicionario de pronuncia da lingua galega: https://ilg.usc.gal/gl/proxectos/dicionario-de-pronuncia-da-lingua-galega
- Pódcast "A Lareira" (conflicto de nombre): https://podgalego.agora.gal/a-lareira/
- Episodio 1 (Reino suevo): todas las fuentes de §11.3.
- **Voz y render (§3A), código revisado el 29-09-2026 [COMP]:**
  - Nós StyleTTS2 (README; `inference.py`, con la línea de `pred_dur`, la división en frases y la concatenación sin silencio; `Configs/inference_config.yml`, con las referencias de estilo y la ruta del checkpoint; `phonemize.py`; `phoneme_token_maps.json`): https://huggingface.co/proxectonos/Nos_StyleTTS2-Brais-GL y https://huggingface.co/proxectonos/Nos_StyleTTS2-Celtia-GL
  - Nós VITS: https://huggingface.co/proxectonos/Nos_TTS-brais-vits-phonemes
  - Nós Matcha: https://huggingface.co/proxectonos/Nos_TTS-icia-extended-matcha-phonemes
  - `length_scale` y escalas de ruido en Coqui VITS: https://github.com/coqui-ai/TTS/blob/dev/TTS/tts/models/vits.py
  - `speaking_rate` → `length_scale` en Matcha: https://github.com/shivammehta25/Matcha-TTS/blob/main/matcha/cli.py
  - Cotovía: https://github.com/proxectonos/cotovia
- **Referencias de escucha (§3A.1.1)**, medidas sobre los subtítulos automáticos en inglés descargados con yt-dlp el 29-09-2026: History Time 0:00-2:50 (98 palabras/min) y 3:25:13-3:26:05 (87 palabras/min); History at Night 1:42-2:50 (163 palabras/min); huecos ≥8 s entre subtítulos: 114 en History Time frente a 0 en History at Night.
- **SPP en España, fecha del 20 de octubre:** https://www.infobae.com/america/agencias/2026/09/25/spotify-anuncia-la-llegada-a-espana-de-partner-program-iniciativa-para-convertir-los-podcast-en-negocios-sostenibles/
- Comprobaciones técnicas [COMP]: `https://www.youtube.com/@<handle>`, `https://rdap.org/domain/<dominio>`, `https://itunes.apple.com/search?media=podcast&country=ES&term=<nombre>`, `https://gl.wikipedia.org/w/index.php?title=<página>&action=raw`.
