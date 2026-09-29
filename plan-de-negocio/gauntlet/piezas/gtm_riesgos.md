# Pieza del business plan: MERCADO, MARCA, LANZAMIENTO, RIESGOS Y PLAN DE PRUEBAS

Versión 5 (constructor, ronda 5) · 29-09-2026 · Redactado en castellano. Todo lo que ve u oye el público (nombre, lemas, textos de descripción, avisos) va en galego normativo (RAG).

**Leyenda de evidencia**
- **[F]**: dato con fuente (URL al lado).
- **[R]**: tomado de los informes de investigación del proyecto (`research/*.md`), que citan la fuente original; se repite la URL cuando la cifra es decisiva.
- **[COMP]**: comprobación hecha para esta pieza el 29-09-2026 (descarga de datos abiertos, búsquedas).
- **[S]**: supuesto o decisión de diseño propia. No está verificado; lo sustituye el dato del piloto.

**Coherencia con las otras piezas.** Se usan el nombre recomendado **"Serán · Historia de Galicia para durmir"** y la especificación de producto de `drafts/formato.md`. Las etapas y los presupuestos son los de `drafts/retornos.md` (mes 1 = octubre de 2026). **Las puertas P1-P3 tienen exactamente los mismos umbrales de adquisición que `drafts/retornos.md` §1** (la v4 añade KPIs de hábito que deciden el *tipo* de GO y un control en M9 que hay que reflejar en `retornos.md`, §4.2 bis); esta pieza fija además la cadencia de publicación, el número de vídeos en cada puerta, las horas de control y el desbloqueo al que apunta cada umbral (§4.0 y §4.2). Los controles anti-*slop* y el expediente por episodio son los de `drafts/pipeline.md` §8. Aquí no se repite la economía: esta pieza responde a **a quién se vende, cómo se llega, qué puede salir mal y cómo se comprueba antes de gastar más**.

---

## 0. Resumen en 14 líneas

1. **El hueco existe y está vacío.** No hay ningún canal ni pódcast de historia (ni de relatos) para dormir para adultos en galego. Hay competencia en castellano que ya explota temas gallegos: el vídeo "Duérmete con las leyendas… de Galicia" suma 107.810 vistas [R `audiencia.md` §4.3].
2. **Está vacío, en parte, porque es pequeño.** Solo el **3,59 %** de los gallegos de 16 años o más ve audiovisual "sempre" o "máis" en galego [F IGE]. Mercado atendible: **~2.000-20.000 oyentes habituales** [R, estimación con supuestos].
3. **Posicionamiento:** no competir con los canales IA en volumen ni en castellano. Ser **"o serán galego"**: la única historia de Galicia contada despacio, en un galego cuidado, con fuentes y sin cortes. **El foso es la calidad lingüística e histórica, no la IA.**
4. **Cuatro públicos, por orden:** (A) galegofalantes adultos que ya escuchan audio para dormir; (B) quienes aprenden o recuperan el galego; (C) la diáspora nacida en Galicia; (D) mediadores (docentes, bibliotecas, entidades), que no son público final sino canal de difusión.
5. **Lanzamiento "lento y con aval"**: primero un panel privado de oyentes nativos y un historiador que revise; después un lanzamiento con 2-3 episodios y un calendario anclado en fechas gallegas. La fecha más potente del año es el **Día das Letras Galegas 2027 (17 de mayo), dedicado a Xosé Neira Vilas**, autor marcado por la emigración a Argentina y Cuba [F]. Es un puente natural con la diáspora.
6. **La transparencia sobre la IA se convierte en argumento** si se enmarca como *"a IA ao servizo do galego"*: voz sintética **con nombre y con permiso** (se dice de quién es la voz de base y que su dueño la autorizó), fuentes publicadas, página de erratas y revisión humana firmada. **No se oculta nada, pero tampoco se hace de la IA el reclamo.**
7. **Riesgo n.º 1, de plataforma:** la política de contenido inauténtico de YouTube, aclarada el 16-07-2026, deja sin monetizar el contenido "genérico o repetitivo" hecho con plantillas [F]. El formato "para dormir" tiene un riesgo estructural. La defensa es la variedad real y el expediente de proceso.
8. **Riesgo n.º 2, de reputación:** el ecosistema cultural gallego es hoy hostil a la voz sintética. Ejemplos: la denuncia de ADA, AGPTI y A Mesa contra el doblaje IA de RTVE (febrero de 2026) y la oleada de críticas a la CSAG por recrear con IA la voz de Begoña Caamaño el 17-05-2026 [F]. **Regla: ninguna voz de una persona real identificable sale al público sin su consentimiento escrito para este uso; jamás se imita a una persona concreta ni se recrea a nadie fallecido.** Toda voz sintética nace de la voz de alguien: las candidatas de Nós (Brais, Celtia, Sabela-Nós) son de un locutor, una locutora y una locutora de radio profesionales con nombre y apellidos, así que **el consentimiento del locutor es condición de la Puerta 0** (§3.3 bis) y se habla con ADA y AGPTI **antes** del lanzamiento, no después de la crítica.
9. **Riesgo n.º 3, legal:** el **art. 50 del AI Act se aplica desde el 2-08-2026 y el Digital Omnibus no lo aplazó** [F]. Para el texto, la revisión humana con responsabilidad editorial exime de etiquetar. Para imágenes realistas y audio que imite personas, siempre hay que etiquetar. Se cumple de sobra con el diseño propuesto.
10. **Riesgo n.º 4, de licencias y de voz:** los modelos de voz de Nós son Apache-2.0, pero sus *datasets* son "solo investigación" y **la licencia del modelo no cubre el derecho a la propia voz del locutor** (LO 1/1982, art. 7.6: usar la voz de una persona con fines comerciales sin su consentimiento es una intromisión ilegítima [F]). Por eso una voz de Nós **solo entra si hay doble permiso escrito** (USC/Gradiant como titulares de los datos + la persona que prestó la voz). Si no llega a tiempo, se publica con la mejor voz de proveedor comercial (Azure, Google) cuyos términos cubren el uso comercial. FLUX.1 [dev] no permite uso comercial del modelo. Material del CCG: no comercial (§3.3 bis y §3.4).
11. **Plan de pruebas:** 16 experimentos (E0-E15) y **una sola tabla de puertas, idéntica a la del modelo de retornos** (§4.2): P0 antes de publicar; **P1 en M6 con 12 vídeos (≥ 60 vistas a 30 días, ≥ 20 suscriptores)**; **P2 en M12 con 36 vídeos (≥ 100 vistas, ≥ 100 suscriptores)**; P3 en M18 (YPP o ≥ 50 €/mes); y una "puerta roja" de reputación. Cada umbral separa la rama base de la clónica y apunta a un desbloqueo real: fan funding (500 suscriptores + 3.000 h) y YPP (1.000 + 8.000 h).
12. **Hábito antes que alcance (nuevo en v4).** El contenido para dormir vive de que la misma persona vuelva cada noche, y en M6 las ramas base y estancada son **idénticas** en vistas y suscriptores: solo se separan por el hábito. Por eso el plan mide **cinco KPIs de hábito con umbral** (espectadores recurrentes ≥ 20 % en la P1 y ≥ 30 % en la P2; horas por espectador; vistas por espectador; tráfico de reproducción continua y de navegación ≥ 30 % en la P1 y ≥ 45 % en la P2) y los cruza con los de adquisición en una **matriz de decisión** que dice cuándo **acelerar**, cuándo **cambiar el formato** y cuándo **parar antes** (control de hábito en M9) (§4.2 bis). Para moverlos hay un **ritual propio, "o serán"** (día y hora fijos, estrea con el promotor en el chat, "Bos días: ata onde chegaches onte?"), un **bucle con el oyente** (temas propuestos y votados, comentarios en galego moderados con normas publicadas, "Carta do serán" por correo desde M2) y **presencia medida en el ecosistema galegofalante** (Bluesky, mastodon.gal, Telegram, Reddit, X mínimo, Podgalego y Obradoiro Dixital Galego) con ≤ 1 h/semana en la Etapa 1 (§2.8).
13. **Cómo recomienda YouTube (nuevo en v5).** Hoy la demanda de "Galicia para dormir" la captan vídeos en castellano (107.810 vistas el de leyendas de Galicia). Serán tiene que **aparecer a su lado**, en la columna de sugeridos, y no solo esperar a que alguien lo busque en galego. Para eso hay una **táctica de adyacencia** (§2.4 bis): temas, títulos y miniaturas en espejo de una lista de **vídeos semilla** que se vigila cada mes en la fuente "Vídeos sugeridos", pruebas con **Test & Compare** en cuanto el canal tenga funciones avanzadas y una prueba de **metadatos traducidos** cruzada con el CTR. Y tres **KPIs de embudo** con umbral en M4, P1, M9 y P2 (§4.0): **impresiones por vídeo a 28 días** (≥ 700 en la P1 y ≥ 1.200 en la P2), **CTR de impresiones** en navegación y sugeridos (objetivo del 4-6 %, alerta por debajo del 3 %) y **cuota de sugeridos desde canales ajenos** (≥ 10 % en la P1 y ≥ 20 % en la P2). **Regla nueva en la matriz: si fallan las impresiones o el CTR, se cambia primero el empaquetado (miniatura y título) y después el formato** (§4.2 bis).
14. **Calendario de 12 meses** (octubre de 2026 a septiembre de 2027): octubre para la voz, el guion y las licencias; lanzamiento con 3 episodios el domingo 22 de noviembre, después 2 al mes y 12 vídeos en la Puerta 1 (31 de marzo); semanal desde abril; Letras Galegas en mayo; Xacobeo 2027 en verano; Puerta 2 en septiembre.

---

## 1. Mercado, competencia y posicionamiento

### 1.1 El mercado en cinco cifras

| Indicador | Dato | Fuente |
|---|---|---|
| Población de Galicia (1-1-2025) | 2.714.741 | [R] https://www.elprogreso.es/articulo/galicia/galicia-gana-8908-habitantes-llega-271-millones-2024/202512021326291928680.html (cifras INE) |
| Saben hablar galego "moito" o "bastante" (5 años o más) | 83,4 % (51,28 + 32,11) | [F] https://www.ige.gal/estatico/html/gl/OperacionsEstruturais/Resumo_resultados_EEF_Galego.html |
| Hablan habitualmente en galego ("sempre" o "máis") | 46,2 % | [F] ídem |
| **Ven audiovisual "sempre" o "máis" en galego (16 años o más)** | **3,59 %** (0,73 + 2,86); el 68,06 % "sempre en castelán" | [F] ídem |
| Escuchan radio "sempre" o "máis" en galego | 15,13 % | [F] ídem |
| Oyentes de pódcast en España que lo usan antes de dormir | 30,6 % (Prodigioso Volcán 2025) - 37 % (NielsenIQ/Audible) | [F] https://www.prodigiosovolcan.com/pv/sismogramas/informe-voz-2025/podcast.html ; https://www.que.es/2025/10/24/podcasts-vida-cotidiana-espanoles |
| La historia en el ranking de géneros de iVoox | 2.º, con 14,08 % (muestra autoseleccionada) | [F] https://prensa.ivoox.com/2025/09/30/el-podcast-se-consolida-como-habito-diario-en-espana-8-de-cada-10-espanoles-escuchan-podcasts-y-lo-convierten-en-un-canal-de-confianza-para-las-marcas/ |

**Lectura.** El galego se entiende y se habla, pero **no se consume en pantalla**. El perfil más cercano al nuestro es el oyente de Radio Galega o el espectador de la TVG: galegofalante, de más de 45 años y a menudo del interior. En radio, el consumo mayoritario en galego es **4 veces mayor** que en audiovisual online (15,13 % frente a 3,59 %). **Por eso el producto se piensa como audio que se escucha a oscuras, no como vídeo que se mira.** Esto encaja con el formato y abre la puerta a Spotify e iVoox [S sobre F].

**Embudo de mercado** [R `audiencia.md` §8; todos los pasos son supuestos salvo las tasas citadas]:

| Paso | Personas |
|---|---|
| Internautas de 16 años o más en Galicia (supuesto: 86 % de adultos × 90 % internautas) | ~2,1 M |
| Escuchan pódcast o audio largo cada semana (47,3 %, Prodigioso Volcán) | ~990.000 |
| Lo usan antes de dormir (30,6-37 %) | ~300.000-370.000 |
| Lo aceptarían en galego (entre 3,6 % audiovisual y 15-18 % radio/TV, IGE) | ~11.000-67.000 |
| Les interesa la historia (15-30 %, supuesto a partir del 14 % de iVoox) | **~2.000-20.000** |

Fuera de Galicia hay un complemento difícil de medir: la diáspora galegofalante (§2.2 C), las personas que aprenden galego (§2.2 B) y un posible "desbordamiento" algorítmico hacia no galegofalantes. Este último es solo una hipótesis, sugerida por el caso atípico de "VaniMani en galego" (11,8K suscriptores y 4,83 M de vistas en 10 meses) [R `audiencia.md` §1.7]. Se mide en el experimento E7, no se da por supuesto.

### 1.2 Competencia

**Directa (historia o relatos para dormir, en galego, para adultos): ninguna.** Búsquedas en YouTube, Spotify y la web con "historia para durmir", "contos para durmir galego", "relaxación galego" y "ASMR en galego" [R `audiencia.md` §5]. Lo más parecido que existe:

| Tipo | Ejemplo | Tamaño | Qué nos enseña |
|---|---|---|---|
| ASMR en galego | "Na utopía non existe a vertixe ASMR" | 273 suscriptores; vídeo de 1 h para durmir con 585 vistas; inactivo desde hace 4-5 años [R, SCRAPE 29-09-2026] | Hubo demanda puntual de "sono en galego" y no se sostuvo. Hace falta constancia y un tema que dé motivo para volver (la historia lo da; el ASMR, no) [S]. |
| Contenido infantil para dormir en galego | Galego para peques (nanas) | 2,48K suscriptores; 341K vistas [R] | Los padres buscan "durmir en galego" para los niños. Hay que **distinguirse de lo infantil** en nombre, miniatura y configuración "no dirigido a niños" (§3.6). |

**Indirecta 1: historia para dormir en castellano, con temas gallegos.** Captan hoy la demanda que no exige galego.

| Canal | Datos | Fuente |
|---|---|---|
| RELATOS AL OIDO | 65,9K suscriptores; "DUÉRMETE CON las Leyendas… de GALICIA", 2 h, **107.810 vistas** en 11 meses; hace 2 días publicó "the hidden history of Lugo" | [R `audiencia.md` §4.3, §5] |
| Imperios y Misterios | 5,18K suscriptores (alta en enero de 2026); "O origen dos galegos", 1 h 50 min, 22.541 vistas | [R] |
| Misterios para Dormir Profundo / El Pergamino Mágico | Leyendas de Galicia para dormir: 9.059 y 5.100 vistas | [R] |
| Líderes del género en castellano | El Historiador Nocturno, 304K suscriptores; Detrás De La Historia, 65,2K suscriptores en ~13 meses | [R `retornos.md` §4.2; `audiencia.md` §6.1] |

**Indirecta 2: divulgación histórica en galego (no para dormir).** Son **aliados potenciales antes que competidores**.

| Canal / pódcast | Datos | Fuente |
|---|---|---|
| Historia a Debate (Carlos Barros) | 9,27K suscriptores; 695K vistas; desde 2010 | [R, SCRAPE] |
| Orgullo Galego | 11,5K suscriptores; sus conversas de historia sacan 300-3.200 vistas | [R] |
| Falemos do Reino de Galicia (Carlos Lixó) | 2,1K suscriptores | [R] |
| Burla Negra (archivo de documentales en galego) | 1,71K suscriptores; "O Reino Suevo da Galiza", 23.763 vistas | [R] |
| TVG, "Historias de Galicia" (resubida) | 670-3.900 vistas por capítulo en un canal de 134K suscriptores | [R] |
| Descifrando a Historia (pódcast, David Gesteira) | Finalista de Carballo Interplay; sin cifras públicas | [R] |

**Indirecta 3: apps de sueño (Calm, BetterSleep…).** Producen su propio contenido y **no tienen catálogo en galego** [R `ingresos_alt.md` §6]. Storytel España no ofrece galego [R].

**Indirecta 4: los medios públicos.** La CRTVG/CSAG tiene categoría de historia en su plataforma de pódcast (https://radiogalegapodcast.gal/categorias/historia) [R] y en 2023 financió proyectos digitales de historia de Galicia [R `ingresos_alt.md` §1.4]. **Puede ser competidor, cliente o las dos cosas** (§2.5).

### 1.3 Mapa de posicionamiento

Dos ejes: la **lengua** (castellano ↔ galego) y el **modo** (divulgación "despierta" ↔ contenido para dormir).

| | Divulgación "despierta" | Para dormir |
|---|---|---|
| **Castellano** | Crónicas de la Historia, CARKI (millones de vistas en temas gallegos) | RELATOS AL OIDO, El Historiador Nocturno, decenas de canales IA clónicos (saturado) |
| **Galego** | Historia a Debate, Orgullo Galego, TVG, Burla Negra (miles de suscriptores, pocos miles de vistas) | **Serán: vacío** |

Dentro de "para dormir", **el eje de calidad** separa la *fábrica IA* (plantilla, 1 vídeo al día, errores; Sleepless Historian ha pasado de millones a 8-31K vistas por vídeo [R `retornos.md` §4.1]) del *oficio* (History Time, History at Night: pocos vídeos, fuentes, voz cuidada [R `formato.md`]). **Serán se coloca en el cuadrante galego × para dormir × oficio.**

### 1.4 Propuesta de valor

**Promesa (para el público, en galego)** — alineada con `drafts/formato.md` §2:

> *"A historia de Galicia contada amodo, nun galego coidado, para que te deixes levar ata o sono. Sen sustos, sen présa e sen cortes."*

**Declaración de posicionamiento** (interna):
> Para galegofalantes adultos que se duermen escuchando audio y no encuentran nada en su lengua, **Serán** es el único canal de historia para dormir en galego. A diferencia de los canales IA en castellano y de la divulgación académica en galego, combina **rigor con fuentes publicadas, galego normativo revisado por nativos y una narración pensada para dormir** (lenta, sin sobresaltos, sin mid-rolls).

**Por segmento** [S; se validan en E2, E7 y E9]:

| Segmento | "Trabajo" que nos encarga | Qué le damos | Qué le haría irse |
|---|---|---|---|
| A. Galegofalante adulto con hábito de audio nocturno | "Axúdame a desconectar na miña lingua" | Voz calmada, temas de su tierra, 1-2 h sin cortes, cola de ambiente | Un error de lengua o una pronunciación "de castellano"; un anuncio que despierta |
| B. Quien aprende o recupera el galego | "Quero escoitar galego bo, amodo, sen esforzo" | Ritmo lento (110-125 palabras/min), galego normativo, subtítulos exactos (el guion es el subtítulo) | Un vocabulario demasiado culto sin contexto |
| C. Diáspora nacida en Galicia | "Quero volver á casa un anaco cada noite" | Paisaje, aldea, emigración, lendas | La sensación de "producto de fábrica" |
| D. Mediadores (docentes, bibliotecas, entidades) | "Necesito contido en galego de calidade que poida recomendar sen vergoña" | Fuentes, créditos, transparencia sobre la IA, capítulos sueltos | Cualquier sospecha de errores o de engaño sobre la IA |

---

## 2. Go-to-market

### 2.1 Principios

1. **Calidad antes que alcance.** Solo se promociona lo que ha pasado la Puerta 0 (§4.2). En una comunidad pequeña, la primera impresión es casi definitiva [S].
2. **Promoción en temporada, producción a ritmo constante.** Los episodios salen cada dos semanas en la Etapa 1 (lanzamiento con 3 y 12 vídeos en M6) y cada semana en la Etapa 2 (36 vídeos en M12); calendario exacto en el §4.0. La promoción se concentra en 5-6 fechas gallegas del año (§4.4).
3. **Canal propio + comunidad propia + mediadores, sin pagar publicidad** en la Etapa 1. La publicidad pagada se prueba solo si la retención es buena (E10), porque llevar tráfico a un vídeo que no retiene es tirar el dinero [S].
4. **Hábito antes que alcance.** Los mediadores traen una primera escucha; lo que hace viable el canal es que esa persona vuelva la noche siguiente. Cada acción de difusión saliente (§2.2-2.7) tiene su contrapartida de retención (§2.8), y las puertas miden las dos (§4.2 bis) [S].
5. **Audio en todas partes.** El mismo máster se publica en YouTube, Spotify for Creators (SPP en España desde el 20-10-2026 [F https://www.infobae.com/america/agencias/2026/09/25/spotify-anuncia-la-llegada-a-espana-de-partner-program-iniciativa-para-convertir-los-podcast-en-negocios-sostenibles/]), iVoox y Apple Podcasts. En galego, la radio es el hábito, así que el audio probablemente pese más que el vídeo [S sobre F IGE].

### 2.2 Segmentos y cómo llegar a cada uno

**A. Galegofalantes adultos (núcleo)**
- **Descubrimiento en YouTube:** título y miniatura con etiqueta fija "HISTORIA PARA DURMIR" y un monumento gallego de noche [R `formato.md` §3.10]. **SEO en galego** (§2.4).
- **Radio y prensa en galego:** la noticia "primeira canle de historia para durmir en galego" tiene gancho para Radio Galega, Nós Diario, Praza, Galicia Confidencial y la sección de cultura de La Voz de Galicia. Se ofrece **después** de tener 3-4 episodios buenos, con el panel del E2 como aval [S].
- **Grupos locales:** asociaciones vecinales y culturales y clubes de lectura de bibliotecas municipales. Con un mensaje de "para escoitar antes de durmir", no de "mira o noso canal de YouTube" [S].

**B. Quienes aprenden o recuperan el galego**
- Tamaño indicativo: las pruebas **CELGA** tramitaron más de 4.000 inscripciones en 2025, la primera vez que se podían hacer en línea [F débil, snippet de búsqueda; https://www.galiciaconfidencial.com/noticia/5837110-tes-interese-facer-as-probas-celga ; oficial: https://www.lingua.gal/o-galego/aprendelo/celga]. A eso se suman los alumnos de galego de las Escuelas Oficiales de Idiomas y de los centros de estudios gallegos en universidades extranjeras [S, sin cifra].
- **Palanca de producto:** subir el guion exacto como **subtítulo manual en galego** en todos los episodios. Coste casi nulo, porque el guion ya existe, y es un valor claro para quien aprende [S]. Además ayuda al SEO, porque YouTube indexa los subtítulos [S, práctica habitual].
- Canales: profesorado de galego para adultos, EOI y foros de aprendizaje. Con un mensaje explícito: "galego coidado, amodo".

**C. Diáspora**
- Realismo: hay 563.303 inscritos en el exterior, pero **solo el 23 % nació en Galicia**; la mayoría son descendientes hispanohablantes [F https://praza.gal/acontece/hai-xa-563-mil-galegos-no-estranxeiro-pero-so-o-23-naceu-en-galicia]. **Es un nicho emocional, no de volumen.**
- **Canal concreto y medible:** el **Rexistro da Galeguidade** tiene **202 entidades** (112 "comunidades galegas", 50 centros colaboradores y 32 centros de estudio y difusión de la cultura galega): 69 en el resto de España, 42 en Argentina, 15 en Brasil, 13 en Uruguay, 13 en Suiza, 11 en Alemania y 10 en Cuba. **201 de ellas publican un correo electrónico** [COMP, datos abiertos de la Xunta: https://abertos.xunta.gal/catalogo/administracion-publica/-/dataset/0571/entidades-rexistro-galeguidade].
- Acción: un correo personal (no masivo) por oleadas de 20-30 entidades, con un episodio recomendado y una propuesta de **"serán compartido"**: escucha colectiva en el local social, o simplemente difusión en su boletín [S]. Lo razonable es empezar por las entidades del resto de España y de Suiza y Alemania, más jóvenes y más galegofalantes que las americanas [S]. Protección de datos: son correos institucionales publicados; se contacta una vez y se respeta la baja (RGPD, interés legítimo) [S; ver §3.7].
- **Fecha ancla:** el Día das Letras Galegas de 2027 se dedica a **Xosé Neira Vilas** (Gres, Vila de Cruces, 1928-2015), cuya obra está marcada por la emigración, que vivió en Argentina y Cuba. Lo acordó la RAG el 8-07-2026 [F https://academia.gal/-/as-letras-galegas-2027-celebraran-a-xose-neira-vilas ; https://www.galiciaconfidencial.com/noticia/5945510-xose-neira-vilas-sera-autor-homenaxeado-nas-letras-galegas-2027]. Propuesta: un episodio sobre **"a aldea galega dos anos corenta e a emigración a Bos Aires e á Habana"** como contexto histórico de su obra. **Sin leer ni adaptar textos de Neira Vilas**, que siguen protegidos hasta el 31-12-2085 (§3.4) [S].

**D. Mediadores**
- **Centros educativos:** con cuidado. El producto "para dormir" no es para el aula ni para menores. Lo que sí sirve son los **capítulos sueltos de 10-15 min** ya previstos como derivado [R `drafts/formato.md` §9], como recurso de escucha para Xeografía e Historia o para la materia de lengua galega. Se ofrecen a través de los equipos de dinamización de la lingua galega de los centros y del profesorado [S]. Se pide permiso a la persona docente, no al centro, y no se hace ninguna campaña dirigida a menores.
- **Bibliotecas y servicios municipales de normalización lingüística:** son los que organizan Youtubeiras+ (10 concellos, las 3 universidades y la Deputación da Coruña) [F https://www.nosdiario.gal/articulo/cultura/youtubeiras-lanza-novo-galardon-honorifico-traxectoria-creacion-dixital-celebrar-decima-edicion-dos-seus-premios/20260917171230267018.html]. **Son el canal institucional más natural**: tienen presupuesto de difusión y necesitan contenido digital en galego [S].
- **Asociaciones culturales y de la lengua:** Real Academia Galega (Portal das Palabras), Consello da Cultura Galega y asociaciones de profesorado. **A Mesa pola Normalización Lingüística es un caso delicado**: es la más activa en difusión del galego, pero criticó con dureza el doblaje con IA [F, §3.5]. Se la contacta **después** de tener la voz con consentimiento documentado y el diálogo previo con ADA/AGPTI (§2.6 bis) y, a ser posible, un historial de calidad; nunca al principio [S].

### 2.3 Lanzamiento en tres fases

| Fase | Cuándo | Qué | Criterio para pasar a la siguiente |
|---|---|---|---|
| **0. Silenciosa** | Oct-nov 2026 (M1-M2) | Voz (E0), guion (E1), licencias (§3.4), 3 episodios terminados **antes de publicar el primero**. Panel privado (E2): 10-15 oyentes nativos, 1 filólogo y 1 historiador | Puerta 0 (§4.2) |
| **1. Suave** | 2.ª quincena de nov 2026 - ene 2027 (M2-M4) | Se publican los episodios 1-3 juntos y luego uno cada 2 semanas, **siempre el mismo día y a la misma hora, con estrea** (ritual del §2.8.2). Difusión solo en el entorno del panel, en 2-3 entidades de la diáspora y en 1-2 servicios de normalización lingüística. **Desde el día 1:** "Carta do serán" (los panelistas del E2 son sus primeros suscriptores, con su permiso), canal de Telegram, cuentas en Bluesky y mastodon.gal y alta en Podgalego y Obradoiro Dixital Galego (§2.8.4). **Sin prensa todavía** | Lectura temprana de E3 en M4 (vídeos 1-4): vistas a 30 días en el carril base o mejor (≥ 50), AVD ≥ 20 min, sin quejas lingüísticas graves y **espectadores recurrentes ≥ 15 %** (si es < 10 %, el cambio de formato del §4.2 bis se adelanta a M5-M6) |
| **2. Pública** | Feb-mar 2027 (M5-M6) y fechas ancla | Nota de prensa ("primeira canle…"), propuesta a Radio Galega, oleadas de correos a la diáspora y a mediadores, colaboraciones con divulgadores (§2.5) | Puerta 1 (fin de marzo de 2027) |

**Por qué no lanzar en Samaín (31-10-2026):** sería la fecha ideal (lendas, Santa Compaña), pero el pipeline no dará un episodio publicable hasta la semana 7-8 [R `drafts/pipeline.md` §0.10]. Lanzar a medias en una fecha tan visible quemaría la primera impresión. **Samaín 2027 será el primer gran episodio de temporada** [S].

**Decisión pendiente, Youtubeiras+ 2026** (inscripción hasta el 15-11-2026; exige al menos 3 publicaciones desde el 16-11-2025) [F https://youtubeiras.gal/bases-youtubeiras-2026/]. Hay dos opciones:
- **(a)** Presentarse con 3 piezas cortas si pasan la Puerta 0 antes del 10-11. Es arriesgado: un jurado que valora la "calidade lingüística" y los "dotes interpretativos" juzgaría un canal con días de vida.
- **(b) Recomendada:** presentarse a la edición de 2027 (patrón de inscripción de septiembre a noviembre [S]) con un año de catálogo, en las categorías "Revelación" (canal de menos de 2 años) y "Pódcast".

### 2.4 SEO y descubrimiento en galego

Hechos que condicionan el SEO:
- Solo el **15,75 %** escribe habitualmente en galego, e incluso entre quienes siempre lo hablan, el 61 % escribe en castellano [R `audiencia.md` §2.3, IGE]. **Gran parte del público galegofalante busca en castellano.**
- "Galicia para dormir" funciona hoy **en castellano** (107.810 vistas) [R].
- No hay datos de volumen de búsqueda en galego: Google Trends no se pudo consultar [R `audiencia.md` §11]. **Laguna: revisarlo a mano en M1.**

Reglas [S; se miden en E6]:
1. **Título en galego, siempre**, con la fórmula de `drafts/formato.md`: "[Tema] (fechas) | Historia de Galicia para durmir". Ejemplo: *"O Reino suevo de Gallaecia (411-585) | Historia de Galicia para durmir · sen cortes"*.
2. **Descripción en galego con una línea final bilingüe**, marcada como aviso de idioma y no como traducción del contenido: *"(Narración en galego · Narrated in Galician · Historia de Galicia para dormir, en gallego)"*. Así se captan las búsquedas en castellano sin prometer un audio que no existe.
3. **Idioma del vídeo y de los metadatos = galego** en Studio. Hay que verificar en M1 que "galego" se puede seleccionar como idioma del vídeo y de los subtítulos (la investigación indica que sí [R `retornos.md` §7.1]).
4. **Traducción de metadatos** (título y descripción en es/pt): **no por defecto**, porque choca con el "100 % galego" y se prueba como experimento (E6). Si YouTube muestra "O Reino suevo…" como "El Reino suevo…" a un espectador en castellano, que luego oye galego, puede subir la tasa de abandono.
5. **Subtítulos manuales exactos en galego** (el guion): accesibilidad, aprendizaje (segmento B) e indexación.
6. **Palabras clave gallegas** en descripción y capítulos: topónimos en forma oficial (Nomenclátor), nombres propios en su forma galega (Xelmírez, Pardo de Cela, Hermerico) y términos del género ("para durmir", "relaxación", "sono", "contos", "lendas").
7. **Listas por serie** ("Gallaecia sueva", "Os Irmandiños", "Vida nunha aldea"): más tiempo de sesión y más variedad aparente, que también cuenta ante la política de contenido inauténtico (§3.1).
8. **Web propia mínima** (seran.gal, previsto en `drafts/formato.md` §10) con una página por episodio: resumen en galego, fuentes y erratas. Es SEO en Google, que YouTube no da, y es la prueba de transparencia (§2.6) [S].
9. **Pruebas A/B de título y miniatura** con la función "Test & Compare" de YouTube Studio. Gana la variante con más tiempo de visionado, no la de más clics: "the title or combination of title and thumbnail with the highest watch time will be shown to all viewers" [F https://support.google.com/youtube/answer/13861714?hl=en]. **No exige estar en el YPP**: pide YouTube Studio en ordenador y tener activadas las **funciones avanzadas**, que se obtienen por historial del canal o verificando la identidad con un documento o un vídeo [F ídem; https://support.google.com/youtube/answer/9890437?hl=en]. **Limitación importante para el ritual:** no se pueden probar los vídeos que se publican como estrea ("You are not able to A/B test Shorts, Scheduled Lives, and Premiere videos") [F https://support.google.com/youtube/answer/13861714?hl=en]. Cómo se resuelve, en el §2.4 bis.

### 2.4 bis Adyacencia: aparecer junto a los vídeos de historia para dormir sobre Galicia (nuevo en v5)

**Por qué.** El SEO del §2.4 capta a quien busca. Pero en un canal nuevo de sueño la mayor parte de la audiencia nueva no llega buscando: llega porque YouTube le pone el vídeo **en la página de inicio o en la columna de sugeridos, junto a otro vídeo que ya está viendo**. "Vídeos sugeridos" es, según YouTube, el "traffic from suggestions that appear next to or after other videos, and from links in video descriptions" [F https://support.google.com/youtube/answer/9314355?hl=en]. Y los vídeos que hoy captan la demanda de "Galicia para dormir" están en castellano [R `audiencia.md` §4.3]. **La táctica es colocarse al lado de esos vídeos, no competir con ellos de frente.** Es además la vía de YouTube que menos depende del tiempo del promotor: la siembra saliente (§2.2) cuesta horas cada mes; un sugerido bien ganado trae vistas sin más trabajo [S].

**Cómo se mide que funciona.** Studio dice qué vídeos concretos traen tráfico sugerido: "You can see specific videos on the 'Traffic source: Suggested videos' card of the Reach tab" [F https://support.google.com/youtube/answer/9314355?hl=en]. Con eso se separa el sugerido que viene **del propio catálogo** (ya contado en H4, hábito) del que viene **de canales ajenos** (R3, nuevo KPI de adquisición, §4.0). Las impresiones solo cuentan lo que se ve dentro de YouTube (búsqueda, inicio, feeds y "A continuación"); no cuentan las webs externas, las pantallas finales ni las miniaturas vistas menos de 1 segundo [F https://support.google.com/youtube/answer/9314486?hl=en].

**1. Lista de vídeos semilla** (se vigila cada mes en la tarjeta "Fuente de tráfico: vídeos sugeridos"; datos de audiencia, SCRAPE del 29-09-2026) [R `audiencia.md` §4.3 y §5; `formato.md` §3]:

| # | Vídeo semilla | Canal · idioma | Vistas | Episodio espejo de Serán (título provisional, galego) | Cuándo |
|---|---|---|---|---|---|
| S1 | "DUÉRMETE CON las Leyendas… de GALICIA" (2 h) | RELATOS AL OIDO · es | 107.810 | *Lendas de Galicia para durmir: a Santa Compaña, as mouras e os mouros* | M3 (Nadal, "de inverno") |
| S2 | "Fall asleep to the hidden history of Lugo" | RELATOS AL OIDO · es | 7.176 (2 días) | *Lugo romana: a muralla, Lucus Augusti e o sono da cidade* | M4-M5 |
| S3 | "O origen dos galegos (Celtas, romanos…)" (1 h 50 min) | Imperios y Misterios · es | 22.541 | *De onde vimos: castros, celtas e romanos na Gallaecia* | M5-M6 |
| S4 | "Leyendas oscuras de Galicia y Asturias (para dormir)" | Misterios para Dormir Profundo · es | 9.059 | S1 cubre el tema; se vigila, no se replica | — |
| S5 | "Legends of Galicia – Santa Compaña tales to calm the mind" | El Pergamino Mágico · es | 5.100 | Ídem S1 | — |
| S6 | "El Reino Suevo de Gallaecia" (27 min, no es de sueño) | Crónicas de la Historia · es | 165.297 | *O Reino suevo de Gallaecia (411-585)* (ya previsto como episodio de lanzamiento) | M2 |
| S7 | "O Reino Suevo da Galiza, parte I" | Burla Negra · **gl** | 23.763 | Ídem S6 | M2 |
| S8 | "¿Cómo Era un Día Completo en la Edad Media?" | Relatos para Dormir · es | 1,05 M | *Un día nunha aldea galega da Idade Media* (formato "vida cotidiana") | M6-M7 |
| S9 | Vídeos del Camino y Xacobeo para dormir en castellano (a identificar) | — | — | Serie *Historias do Camiño* | M10 (Año Santo) |

**Encaje con el catálogo de `drafts/formato.md` §8:** tres de los cuatro primeros temas por prioridad (Reino suevo, aldea medieval y castro) ya son espejo de un semilla (S6-S7, S8 y S3), así que la táctica no desvía el plan editorial: lo ordena. Las lendas (S1) y Lugo (S2) son los dos espejos que se añaden por demanda medida.

Reglas de la lista [S]: se revisa el día 1 de cada mes buscando en una ventana privada "Galicia para dormir", "leyendas de Galicia dormir", "historia de Galicia", "Camino de Santiago historia dormir" y "Lugo historia", **con la interfaz en castellano y en galego**, y se añaden los 3 primeros resultados nuevos de sueño con más de 5.000 vistas; se retira un vídeo cuando lleva 3 meses sin traer tráfico ni subir de vistas. Las URL exactas se guardan en la hoja del cuadro de mando en M1 (los informes de investigación solo guardan título, canal y vistas).

**2. Espejo de temas, títulos y miniaturas** [S; se mide con R1-R3 y en E15]:
- **Temas:** en la Etapa 1, **1 de cada 3 episodios** es espejo de un vídeo semilla (tabla anterior); el resto sigue el plan editorial y las votaciones del §2.8.3. En la Etapa 2, 1 de cada 4.
- **Títulos: las palabras que se escriben igual en galego y en castellano van delante.** "Galicia", "historia", "Lugo", "Santa Compaña", "celtas", "romanos", "suevos", "Compostela" e "Idade Media/Edad Media" (casi igual) son señales que YouTube asocia a las mismas búsquedas y a los mismos vídeos en los dos idiomas. Ejemplo: *"Galicia e a Santa Compaña: lendas para durmir (2 h)"* en lugar de *"As lendas da noite galega"*. El título sigue siendo 100 % galego normativo: no se castellaniza ninguna palabra para posicionar.
- **Miniaturas: misma gramática visual que el género, identidad propia.** Noche, un monumento o paisaje gallego reconocible, luz cálida, 2-4 palabras grandes; es lo que el espectador de S1-S8 ya asocia con "vídeo para dormir" [R `formato.md` §3.10]. Serán añade su franja fija "HISTORIA PARA DURMIR" y su paleta. **Nunca** se copian miniaturas ajenas, ni se imita el nombre o el logotipo de otro canal, ni se usan títulos engañosos: YouTube lo trata como spam o metadatos engañosos [S, política de spam y prácticas engañosas; verificar el texto en M1] y además rompería el tono calmado del canal.
- **Duración parecida** a la del semilla (1,5-2 h), porque el espectador de un vídeo de 2 h busca otro de 2 h [S].
- **Descripción:** la línea bilingüe del §2.4 (regla 2) nombra el tema en castellano ("Leyendas de Galicia para dormir, narradas en gallego"), que es la palabra que usan los vídeos semilla.

**3. Test & Compare, en cuanto esté disponible** [F sobre requisitos; S sobre el calendario]:
- **M1:** activar las funciones avanzadas del canal verificando la identidad (sin coste) [F https://support.google.com/youtube/answer/9890437?hl=en].
- **Conflicto con la estrea:** los vídeos publicados como estrea no se pueden probar [F https://support.google.com/youtube/answer/13861714?hl=en]. Solución en dos pasos: (a) en M2, con el episodio 1, se comprueba si el vídeo admite la prueba una vez acabada la estrea [S, no documentado]; (b) si no la admite, los **episodios espejo** (1 de cada 3) se publican sin estrea, a la misma hora del ritual y con aviso en la Carta y el Telegram, y en ellos se hace la prueba. Eso encaja con el ABAB de estrea del E13 en M7-M10.
- **Qué se prueba:** 3 variantes de miniatura (y, desde la Etapa 2, de título) con el mismo tono. **Se acepta el resultado de YouTube** porque gana el tiempo de visionado, que es exactamente lo que interesa en un canal para dormir; la única excepción es una variante que rompa la guía de tono (sobresalto, clickbait), que no se sube a la prueba.
- **Lo que aprende el canal:** después de 6 pruebas se fija la plantilla de miniatura por serie [S].

**4. Idioma de los metadatos, cruzado con el CTR** (amplía el E6) [F sobre la función; S sobre el diseño]:
- YouTube permite añadir títulos y descripciones traducidos: "We'll show the title and description of the video in the right language, to the right viewers" y "Translated video titles and descriptions can show up in YouTube search results for viewers who speak those other languages" [F https://support.google.com/youtube/answer/4792576?hl=en].
- **Riesgo:** que un espectador en castellano haga clic en "Leyendas de Galicia para dormir", oiga galego y se vaya (retención baja, mala señal para la recomendación) y que parezca que se esconde la lengua del canal.
- **Diseño:** la traducción **siempre dice el idioma del audio**: *"Leyendas de Galicia para dormir (narrado en gallego) | 2 h sin cortes"*. Variante A: solo metadatos en galego. Variante B: galego + traducción al castellano. Se alterna en 4 + 4 episodios comparables (dentro de una misma serie) en M7-M9.
- **Métricas:** CTR de impresiones en navegación y sugeridos (R2), cuota de sugeridos ajenos (R3), retención al minuto 1 por fuente y % de espectadores desde España fuera de Galicia (E7).
- **Regla:** se adopta B si sube el CTR en sugeridos **≥ 1 punto** o R3 **≥ 5 puntos** sin bajar la retención al minuto 1 **más de 5 puntos**. Si la retención cae más, se vuelve a A: la audiencia que llega engañada por el idioma no sirve para el hábito. **El audio y el título principal nunca dejan de estar en galego.**

**5. Colaboración con los canales semilla pequeños** [S]: Imperios y Misterios (5,18K suscriptores) y los canales de S4-S5 son pequeños y tratan temas gallegos. Se les propone una mención mutua en la descripción o una lista compartida "Galicia para durmir / para dormir" con sus vídeos y los de Serán. Los enlaces en la descripción cuentan como sugeridos [F https://support.google.com/youtube/answer/9314355?hl=en]. **Nunca** se dejan comentarios promocionales en vídeos ajenos: eso es spam y en una comunidad pequeña se nota.

**Tiempo:** revisión de semillas y ajuste del empaquetado ≈ 20 min al mes en la Etapa 1, dentro del bloque de comunidad del §2.8.5 [S].

### 2.5 Colaboraciones con historiadores y divulgadores

**Objetivo doble:** aval de rigor (reduce el riesgo reputacional) y difusión cruzada con audiencias que ya existen.

| Formato | Con quién (ejemplos) | Qué gana el colaborador | Coste [S] | Cuándo |
|---|---|---|---|---|
| **Revisión científica de un episodio** (lectura del guion y de la hoja de fuentes, 1-2 h) | Profesorado universitario o de secundaria de historia; divulgadores como Carlos Lixó o David Gesteira | Crédito visible ("Revisión histórica: …"), enlace y remuneración | **50-150 € por revisión** [S, sin tarifa de referencia; se negocia] | Desde el episodio 1 si el presupuesto lo permite; como mínimo, 1 de cada 4 episodios |
| **Episodio "da man de…"**: el divulgador propone el tema y la bibliografía | Historia a Debate, Orgullo Galego, Descifrando a Historia | Contenido nuevo para su audiencia y difusión | 0 € (intercambio) | Desde M5 (fase pública) |
| **Conversa de extras**: 20-30 min **con voz humana** del historiador, fuera del formato para dormir, en la lista "Detrás do serán" | Los mismos | Visibilidad | 0 € + tiempo de edición | Desde M6 |
| **Presencia en su pódcast o directo** | Orgullo Galego (sus conversas de historia sacan 300-3.200 vistas [R]), Descifrando a Historia | Tema de conversación: "IA e galego" | 0 € | Fase pública |

**La conversa con voz humana tiene un valor adicional:** pone caras y voces reales detrás del canal y desactiva el reproche de "canal sin personas".

**Reglas de colaboración** [S]:
- El colaborador ve el guion final y el expediente de fuentes antes de dar su nombre.
- **Nunca se sintetiza su voz ni su imagen.**
- Crédito exacto en descripción y web.
- Derecho de retirar su nombre si detecta un error no corregido.

### 2.6 Transparencia sobre la IA: de riesgo a ventaja

**El problema.** Una parte del ecosistema cultural gallego asocia la IA con la precarización del doblaje y con la pérdida de calidad del galego ("máis como freo ca como impulso para a lingua galega", ADA, AGPTI y A Mesa sobre RTVE) [F https://www.nosdiario.gal/articulo/social/mesa-agpti-ada-denuncian-incumprimentos-rtve-coa-programacion-galego/20260220110723248001.html]. Y reacciona muy mal cuando la IA suplanta a una persona real (la recreación de Begoña Caamaño por la CSAG el Día das Letras Galegas de 2026) [F https://www.nosdiario.gal/articulo/social/que-non-deixala-falar-criticas-ia-empregada-pola-crtvg-recrear-begona-caamano/20260518160723256730.html].

**La oportunidad.** La propia Xunta financia el **Proxecto Nós** para que "o galego estea na IA" [F https://www.lingua.gal/recursos/todos/_/promovelo/contido_607/nos-intelixencia-artificial-servizo-lingua-galega]. Un canal que **usa una voz sintética galega con el permiso de la persona que la prestó, la acredita con su nombre y demuestra que en galego se puede hacer contenido de calidad con IA** encaja en el relato institucional de "a IA ao servizo da lingua", no en el de "a IA contra os profesionais" [S]. Además, la AESIA (la agencia española de supervisión de la IA) tiene su sede en A Coruña [F https://www.economistjurist.es/zbloque-1/ley-organica-de-ia-espana-aterriza-el-ai-act-con-aesia-sanciones-y-sandboxes/]: la conversación sobre IA responsable tiene acento gallego.

**Seis compromisos públicos** (una página "Como facemos Serán" en la web y enlazada en cada descripción) [S]:
1. **Qué hace la IA y qué hacen las personas**, sin eufemismos.
2. **Fuentes de cada episodio** publicadas.
3. **Página de erratas** con fecha y corrección.
4. **Créditos de la voz completos:** modelo y licencia (Proxecto Nós/Gradiant o el proveedor que corresponda) **y la persona cuya voz sirvió de base**, con su nombre si lo autoriza o, si prefiere el anonimato o el proveedor no lo publica, "locutor/a profesional".
5. **Ninguna voz de una persona real sin su consentimiento escrito para este uso.** Nunca se imita a una persona concreta (viva o muerta) ni se recrea a nadie fallecido; nunca se sintetiza la cara de nadie. Si la persona retira el permiso, su voz sale del canal (§3.3 bis).
6. **Remuneración y crédito al locutor desde el primer día** si se usa una voz de Nós (oferta en §3.3 bis), y, si el proyecto crece (Etapa 3), **licenciar y remunerar la voz de un locutor galego** con contrato justo [R `voz_guion.md` §1.6].

**Texto modelo para la descripción** (galego; revisar con el lingüista del pipeline). El aviso dice **de quién es la voz de base**, no solo que es sintética. Hay dos variantes, según la voz que pase la Puerta 0:

> **Nota sobre o proceso.** Este episodio fíxose con ferramentas de intelixencia artificial. O guion redactouse en galego cunha IA a partir das fontes que se citan máis abaixo, e revisárono persoas galegofalantes, que comprobaron os datos e a lingua. **A voz é sintética.** [Variante Nós:] Xerouse co modelo [Brais] do Proxecto Nós (Universidade de Santiago de Compostela e Gradiant), con licenza Apache 2.0, adestrado coa voz do locutor [nome e apelidos], que autorizou por escrito o seu uso nesta canle e recibe unha parte dos ingresos. [Variante provedor:] É a voz [Sabela] de Microsoft Azure, creada por Microsoft a partir da voz dunha locutora profesional que non se identifica publicamente; non imita a ningunha persoa concreta. As imaxes son ilustracións xeradas con IA e non representan persoas nin documentos reais. Se atopas un erro, dínolo nos comentarios: corrixímolo e anotámolo na páxina de erratas.

**Aviso hablado** (primeros 30 s, dentro de la bienvenida; además sirve como "aviso de audio" del Código de Práctica de la UE, §3.3):

> Variante Nós: *"A voz que vas escoitar é sintética: está feita a partir da voz de [nome], que nos deu permiso para usala. O texto revisárono persoas galegofalantes."*
>
> Variante provedor: *"A voz que vas escoitar é sintética, e o texto revisárono persoas galegofalantes."*

Si el locutor prefiere no ser nombrado, se sustituye el nombre por "dun locutor profesional galego" y se mantiene la mención de que dio su permiso [S].

**Lema interno de comunicación** (no como reclamo en miniaturas): *"Feito con IA, coidado á man."* La IA **no** aparece en títulos ni miniaturas: no es el motivo por el que alguien escucha, y ponerla ahí atrae a quien viene a criticar [S].

**Cómo se mide si la transparencia ayuda o perjudica:** E8 (análisis del sentimiento de los comentarios y del panel sobre la IA) y el umbral de la Puerta roja (§4.3).

### 2.6 bis Diálogo previo con el sector de la voz (ADA, AGPTI) y con el locutor

**Por qué antes y no después.** El sector de la voz gallego ya ha dicho públicamente lo que piensa de la IA (ADA, AGPTI y A Mesa sobre RTVE, febrero de 2026) [F, §2.6], y la cláusula PASAVE prohíbe usar grabaciones de doblaje para entrenar IA [R `voz_guion.md` §1.6]. Si el canal sale con la voz de un profesional gallego y ADA se entera por la prensa, el titular será "outra IA que usa a voz dun actor galego". Si se entera por nosotros, con el consentimiento del locutor en la mano y una oferta de crédito y remuneración, la conversación es otra [S].

**Secuencia (M1-M2, antes de la Puerta 0):**

| Paso | Cuándo | Con quién | Qué se pide o se ofrece |
|---|---|---|---|
| 1 | Semana 1 de octubre (en paralelo al E0, sin esperar a su resultado) | Proxecto Nós, `proxecto.nos@usc.gal` [F https://huggingface.co/datasets/proxectonos/Nos_Brais-GL], con copia a Gradiant (desarrollador de los StyleTTS2) | (a) Confirmación escrita de que el uso del modelo en un canal monetizado de YouTube y pódcast es compatible con las condiciones de los datos; (b) **alcance del consentimiento que firmaron los locutores** (¿incluye usos comerciales de terceros?); (c) que **trasladen nuestra petición a cada locutor** o nos den un contacto profesional. Para Sabela-Nós, Icía, Iago y Paulo, la vía es el CRPIH (USC) y el GTM-atlanTTic (UVigo), autores del corpus [F https://zenodo.org/records/8027725] |
| 2 | Semanas 2-4 | La persona detrás de cada voz que siga en carrera tras el E0 | Consentimiento escrito (plantilla abajo). Solo por la vía que indique la USC o por su canal profesional público; **nunca** por canales personales |
| 3 | Segunda quincena de octubre, **antes de publicar nada** | ADA (Actores e Actrices da Dobraxe Asociados) y AGPTI (profesionales de la traducción e interpretación) [F, citadas en nosdiario.gal, §2.6]; contacto por sus canales públicos [S, localizar en M1] | Una carta breve y una llamada: qué es Serán, qué voz se usa y con qué permiso, qué cobra el locutor, la página "Como facemos Serán". **Ofertas:** (a) crédito nominal al locutor y mención de la asociación si el locutor es socio y lo quiere; (b) remuneración al locutor (abajo); (c) compromiso público de que la voz de la Etapa 3 se contrata a un profesional gallego con cláusulas compatibles con PASAVE (uso limitado a Serán, sin cesión a terceros ni entrenamiento de otros modelos); (d) invitar a AGPTI a proponer un revisor lingüístico remunerado cuando haya ingresos (el filólogo del E2 puede ser ya un profesional de AGPTI, con los 0-150 € previstos). **Se pregunta, no se pide permiso:** su opinión se registra en el expediente |
| 4 | Antes de la Puerta 0 (~15-11) | Promotor | Decisión con la regla del §4.2: voz con doble permiso o voz de proveedor |

**Oferta al locutor** [S, a validar con él y con ADA; no está en el modelo de `drafts/retornos.md` y hay que añadirla]:
- **Crédito** en cada descripción y en el aviso hablado, con su nombre o anónimo, a su elección.
- **10 % de los ingresos netos del canal** mientras se use su voz (hoy 0 €; en la rama base, nada antes de M25), liquidado cada seis meses con el informe de ingresos.
- **Pago simbólico de 100 € a la firma**, que sale del margen de la Etapa 1 (35 € de gasto en el modelo frente a un techo de 50 €/mes); si la P1 da GO, **se revisa al alza** tomando como referencia las tarifas de la UVA (1.000-7.500 € por una licencia de voz sintética) [R `voz_guion.md` §1.6].
- **Veto por episodio:** puede pedir que su voz no lea un tema concreto.
- **Retirada:** el consentimiento es revocable por ley en cualquier momento (LO 1/1982, art. 2.2) [F https://www.boe.es/buscar/act.php?id=BOE-A-1982-11196]; el canal se compromete a **sustituir su voz en todo el catálogo en ≤ 30 días**, re-sintetizando los guiones con la voz de reserva (el pipeline es independiente de la voz: coste ~0 € y ~1 h por episodio [S]).

**Plantilla del consentimiento** (una página, en galego, firmada): identidad; modelo y voz; usos autorizados (YouTube, Spotify, iVoox, Apple Podcasts, fragmentos promocionales de ≤ 90 s, web propia); idioma (galego; cualquier uso en es/pt requiere nueva firma); **exclusiones** (publicidad de terceros leída con su voz, política, contenido para menores, cesión a terceros, entrenamiento de otros modelos); duración (hasta el 31-12-2028, renovable); crédito sí/no; remuneración; retirada con sustitución en 30 días.

**Qué hacemos con lo que respondan:**
- **Locutor dice sí:** la voz puede ganar la Puerta 0.
- **Locutor dice no o no responde antes del 6-11-2026:** esa voz **queda excluida** y se publica con la voz de reserva (§4.1, E0). Se puede volver a intentar en la revisión semestral de voz.
- **ADA o AGPTI expresan oposición en privado:** se registra, se responde por escrito y **se mantiene la decisión solo si el locutor ha dado su permiso**. Si el propio locutor, tras hablar con su asociación, prefiere retirarse, se retira sin discusión.
- **Oposición pública antes del lanzamiento:** se activa la Puerta roja (§4.2) antes de publicar.

### 2.7 Mensaje por canal (resumen operativo)

| Canal | Mensaje | Frecuencia [S] |
|---|---|---|
| YouTube (título y miniatura) | Tema + "Historia de Galicia para durmir" + "sen cortes" | Cada episodio |
| Descripción y web | Resumen, capítulos, fuentes, "Nota sobre o proceso" | Cada episodio |
| Spotify, iVoox, Apple | El mismo máster; la descripción incluye la nota sobre la IA (Spotify exige declarar la narración IA, según una fuente secundaria [R `ingresos_alt.md` §3.1]) | Cada episodio |
| Correos a entidades | "Un serán en galego para a vosa xente", con un episodio concreto | Oleadas en M4, M6, M8 y M11 |
| Prensa y radio | "Primeira canle de historia para durmir en galego" + el aval del panel o de un historiador | 1 vez en M5-M6, y en las fechas ancla |
| Postales verticales (60-90 s, Shorts/Reels) | Una imagen, una frase y un paisaje sonoro, que llevan al episodio largo | 1-2 por episodio [R `drafts/formato.md` §9] |
| Comunidad propia (Carta do serán, Telegram, Bluesky, mastodon.gal, Reddit, red de pódcast) | "Esta noite hai serán" + lo que no entró en el guion + la pregunta de temas | Ver la tabla de presencia del §2.8.4 |

### 2.8 Comunidad y hábito: "o serán" como ritual (nuevo en v4)

#### 2.8.1 Por qué hace falta: el GTM saliente mide adquisición, y aquí manda el hábito

Hasta la v3, el lanzamiento era casi solo difusión institucional saliente (correos a entidades, prensa, mediadores). Eso consigue **una primera escucha**. El contenido para dormir, en cambio, se consume por **repetición**: la misma persona vuelve la noche siguiente, deja correr la lista y a veces repite el mismo episodio [S, coherente con `research/ingresos_alt.md` §3, que describe el formato como "escucha repetida nocturna"]. Tres hechos del propio plan lo convierten en algo decisivo:

1. **En M6 la rama base y la estancada son indistinguibles** en las métricas de adquisición (vistas a 30 días 86-91 en las dos; 24 frente a 23 suscriptores) y solo se separan después (115 frente a 91 vistas y 107 frente a 87 suscriptores en M12) [S, salida de `model/puertas_gtm.py`]. En el modelo, lo que las separa es el factor de crecimiento del catálogo y de la recomendación. En YouTube, ese factor tiene nombre: **espectadores que vuelven y tráfico que llega sin que nadie lo empuje** (inicio, suscripciones, listas, sugeridos del propio canal) [S, interpretación]. Medir el hábito es la única forma de ver en M6 lo que las vistas solo muestran en M12.
2. **En la base, casi la mitad de las vistas de M12 vienen del catálogo**, no del vídeo nuevo (883 vistas en el mes, de las que ~460 son de los 4 vídeos nuevos) [S, modelo]. El catálogo solo trabaja si el oyente encadena episodios.
3. **La audiencia galegofalante digital es pequeña y densa.** Las cuentas "centro" del galego en Bluesky tienen entre 1.500 y 2.800 seguidores y la instancia gallega de Mastodon, 1.414 cuentas (§2.8.4) [COMP]. En un ecosistema así, **el boca a boca de 200 personas fieles vale más que 2.000 vistas de paso**, y la reputación se juega en la conversación, no en la nota de prensa [S].

Por eso esta sección añade tres cosas: un **ritual** que da motivo para volver (§2.8.2), un **bucle con el oyente** desde el lanzamiento (§2.8.3) y una **presencia medida** en el espacio digital galegofalante (§2.8.4). Los KPIs de hábito y las decisiones que disparan están en E3 (§4.1) y en la matriz del §4.2 bis.

#### 2.8.2 Ritual e identidad: "o serán"

El nombre ya trae el ritual. El *Dicionario da RAG* define *serán* como la parte del día "desde que comeza a pórse o sol ata que se fai noite", la "reunión de mulleres para fiar que se facía destas horas" y la "reunión nocturna de carácter festivo" [F https://academia.gal/dicionario/-/termo/ser%C3%A1n]. Es decir: **gente que se junta al caer la noche para escuchar y contar**. El canal no inventa una identidad; recupera una.

| Elemento del ritual | Qué es (lo que ve u oye el público, en galego) | Por qué | Coste |
|---|---|---|---|
| **Día y hora fijos** | Siempre el **domingo a las 21:30** (hora de Galicia): quincenal en la Etapa 1 y semanal en la Etapa 2; lanzamiento el domingo 22-11-2026. Los especiales de fecha ancla (Día Mundial do Sono, Letras, Samaín) salen el domingo previo que fije el calendario (§4.4). Lema de las publicaciones: *"Esta noite hai serán."* | El domingo por la noche es cuando más cuesta dormir antes de la semana [S]. La hora fija convierte el episodio en una cita. Se revisa en M4 con el informe "Cando están os teus espectadores en YouTube" de Studio [F https://support.google.com/youtube/answer/9314416?hl=en] | 0 € |
| **Estrea con el lume aceso** | Cada episodio se publica como estreno de YouTube. **El promotor está en el chat, con su nombre, los primeros 15 minutos**: saluda, dice de dónde vienen las fuentes y se despide con un "boas noites". Después el chat se apaga solo | Da presencia humana real, que pide la política de contenido inauténtico (§3.1) y que la comunidad galega exige (§2.6). Es el único momento "en directo" y está pensado para terminar antes de que el oyente se duerma | 15 min cada estreno |
| **Fórmulas fijas en el audio** | Entrada *"Boas noites. Isto é Serán…"* y cierre *"Boas noites"*, como en `drafts/formato.md` §4.1. En los episodios elegidos por la audiencia, **una sola frase de dedicatoria** en la entrada suave: *"O serán desta noite propúxoo Uxía, desde Zúric."* (solo con permiso escrito de la persona) | Reconocimiento sin romper la regla de "sono seguro" (ni llamadas a la acción ni cambios de tono en el audio). La dedicatoria a alguien de la diáspora es la forma más barata de decir "isto é teu" [S] | 0 € |
| **El ritual de la mañana** | Comentario fijado en cada episodio: *"Bos días. Ata onde chegaches onte á noite? Dinos en que capítulo adormeciches."* | Da a la audiencia de sueño un motivo para comentar **al día siguiente** y no durante la escucha. Además, da un dato de producto gratis: en qué capítulo se duerme la gente, que se cruza con la curva de retención [S] | 0 € |
| **Nombre de la comunidad** | *"a xente do serán"* (en la Carta, en las redes y en la web; nunca en el audio) [S, revisar con el lingüista] | Pertenencia sin estridencia: el tono es de invitación, no de "fandom" | 0 € |
| **Seráns de temporada** | *Serán de Samaín* (31-10), *Serán das Letras* (17-05), *Serán do Camiño* (verano Xacobeo) y *serán compartido* en los locales de la diáspora (§2.2 C) | Anclan el año a fechas gallegas y dan motivo de vuelta para quien lo dejó [S] | Ya en el calendario |

**Lo que no se hace:** nada de rachas, retos, "non esquezas activar a campá" hablado ni cualquier mecánica de "engagement" que despierte al oyente. El ritual es de **calma y constancia**, no de estímulo [S, coherente con `contexto.md`].

#### 2.8.3 El bucle con el oyente, desde el día 1

**(a) Temas propuestos por la audiencia: "Propón un serán".**
- **Entrada:** comentarios, un formulario en seran.gal, las respuestas a la Carta y la etiqueta **#PropónUnSerán** en Bluesky y mastodon.gal.
- **Filtro:** cada propuesta pasa por los criterios del catálogo de `drafts/formato.md` §8 (fuentes suficientes, riesgo, encaje "para dormir") y por la lista de temas excluidos (§8.3). A quien propone algo excluido se le responde por qué, con amabilidad [S].
- **Votación trimestral:** los 3-4 temas viables se votan con una **encuesta en la pestaña de publicaciones de YouTube** (admite encuestas y cuestionarios y no exige un mínimo de suscriptores en su página de ayuda; no está disponible para canales "para nenos", que no es nuestro caso) [F https://support.google.com/youtube/answer/9409631?hl=en] y, a la vez, en la Carta.
- **Salida:** el especial de marzo de 2027 (M6) ya es "o serán que pediches". Desde la Etapa 2, **1 de cada 4 episodios** es un tema votado, con crédito a quien lo propuso (con su permiso) y la dedicatoria del §2.8.2.
- **Cierre del bucle:** cuando se publica, la Carta y las redes dicen *"Pedístelo, e aquí está"*. Si un tema no sale, se explica por qué.

**(b) Comentarios en galego, moderados y con normas publicadas.**
Texto de las normas, fijado en la pestaña del canal y en la web (galego; revisar con el lingüista):

> **Normas do serán.** Aquí vense a escoitar e a descansar. Podes comentar na lingua que queiras; nós respondemos sempre en galego. **Aquí ninguén corrixe o galego de ninguén**: se atopas un erro noso, dínolo e corrixímolo. Non se admiten insultos nin spam, e as ligazóns quedan retidas ata que as revisemos. Os debates sobre normativa e política quedan fóra: isto é un serán, non un parlamento.

- **Por qué "ninguén corrixe o galego de ninguén":** el segmento B (quienes aprenden o recuperan la lengua) y los neofalantes huyen de los espacios donde se les corrige en público. El canal corrige **sus** errores (E5) y protege los de los demás [S, criterio sociolingüístico].
- **Configuración de Studio:** retención de comentarios en nivel "básico" (o "estricto" si hay ataques), lista de palabras bloqueadas (insultos, spam, consignas partidistas) y retención de los comentarios con enlaces; YouTube guarda los retenidos hasta 60 días para revisarlos [F https://support.google.com/youtube/answer/9483359?hl=en]. Personas de confianza del panel del E2 como "usuarios aprobados".
- **Respuesta humana, siempre:** el promotor responde en ≤ 48 h, en galego y firmando con su nombre. **Nunca se automatizan las respuestas** (aunque el pipeline redacte las publicaciones, §2.8.5): una respuesta generada, en una comunidad que ya desconfía de la IA, sería el peor titular posible [S].
- **Métrica sociolingüística:** % de comentarios escritos en galego (objetivo ≥ 60 %) y nº de comentarios de personas que dicen estar aprendiendo. Si el galego baja del 40 %, se revisa si la difusión está trayendo público que no es el nuestro (E6, E7) [S].

**(c) Lista de correo: "Carta do serán", desde M2 (antes: opcional desde M6).**
- **Qué lleva** (mensual en la Etapa 1, quincenal en la Etapa 2; ≤ 400 palabras, en galego): el serán del mes y el de la próxima quincena; **"O que non coubo"** (un dato o una escena que se quedó fuera del guion, con su fuente); **"A palabra do serán"** (una palabra del episodio con su sentido y su uso, pensada para quien aprende); erratas; y la pregunta de temas.
- **Por qué desde M2:** es el único canal que **no depende de ninguna plataforma** (riesgo del §3.6), llega a la diáspora sin algoritmo y es la base de las futuras membresías: el fan funding se desbloquea con 500 suscriptores de YouTube, pero quien paga es quien ya abre la Carta [S, coherente con el 0,5-2 % de conversión de la audiencia recurrente de `research/ingresos_alt.md` §4].
- **Herramienta:** Buttondown gratis hasta 100 suscriptores [F https://buttondown.com/pricing]; al superarlos, MailerLite gratis hasta 250 suscriptores y 2.500 envíos al mes [F https://www.mailerlite.com/pricing]. Por encima de 250 (rama alta, Etapa 2) se paga un plan básico dentro del presupuesto de 50-200 € [S, precio sin verificar].
- **Captación sin romper el sueño:** enlace en la descripción, en el comentario fijado y en la web; código QR en los correos a entidades. **Nunca se pide en el audio.**
- **RGPD:** doble confirmación, aviso de privacidad, baja en un clic y solo mayores de 14 años (edad mínima para consentir en España, art. 7 LOPDGDD [S, conocido; verificar redacción]). Los panelistas del E2 se apuntan solo si lo piden.

#### 2.8.4 Presencia en el espacio digital galegofalante

**Qué hay** (medido el 29-09-2026):

| Espacio | Dato | Fuente |
|---|---|---|
| **Bluesky** | Cuentas "centro" del galego: *Bluesky en galego* (@engalego.gal) 1.479 seguidores; *Orgullo Galego* 1.784; *Nós Diario* (puente no oficial) 2.769. **Agregadores de Obradoiro Dixital Galego:** *YouTube en Galego* (@galegotube) 140 seguidores y 8.458 publicaciones (reenvía el contenido de canales en galego) y *Podgalego* (@podgalego) 203 seguidores y 5.854 publicaciones | [COMP, API pública de Bluesky, `app.bsky.actor.getProfile`] |
| **Mastodon** | **mastodon.gal**: "servidor en galego de Mastodon para a comunidade galega", 1.414 cuentas, 231.430 publicaciones, idioma gl, alta con aprobación | [COMP, https://mastodon.gal/api/v1/instance] |
| **Red de pódcast en galego** | **Podgalego** (Agora.gal): 108 pódcast activos y 164 inactivos (272); **16 en la categoría "Historia"**; se añade un pódcast con un formulario de contacto. Canal de Telegram de avisos de episodios: **120 suscriptores** | [COMP, https://podgalego.agora.gal ; https://t.me/podgalego_episodios] |
| **Asociación de creadores** | **Obradoiro Dixital Galego**: asociación que indexa canales, pódcast y directos en galego, **si publican al menos una vez al mes** y cumplen sus normas; tiene Discord, cuenta en mastodon.gal y un formulario de alta de proyectos | [COMP, https://obradoirodixitalgalego.gal/] |
| **Reddit** | r/galicia y r/Galiza: **tamaño sin verificar** (Reddit bloqueó la consulta) | [S, laguna; mirar a mano en M1] |
| **X** | Sin datos del uso en galego | [S] |

**Lectura.** El ecosistema es pequeño: la mayor cuenta "centro" del galego en Bluesky no llega a 3.000 seguidores. **No es una fuente de volumen, es el núcleo de mediadores, activistas y creadores** que decide si un proyecto en galego "é dos nosos" o "outra IA". Su valor es de reputación y de boca a boca, y se mide así [S].

**Plan de presencia** (metas [S]; se revisan en la lectura de M4):

| Espacio | Acción | Frecuencia | Métrica | Meta M6 / M12 | Regla de abandono |
|---|---|---|---|---|---|
| **Bluesky** (@seran.gal, con el dominio propio como usuario) | (1) Alta en los agregadores de Obradoiro (YouTube en Galego y Podgalego), para que reenvíen cada episodio. (2) Por episodio: una imagen de "noite atlántica", dos líneas y **"O que non coubo"**. (3) Participación humana en conversaciones de historia y lengua, sin enlazar | 2 publicaciones por episodio + 2 respuestas por semana | Seguidores; republicaciones de cuentas centro; clics (enlace corto por red) | 60 / 200 seguidores; ≥ 1 republicación de una cuenta centro por episodio | Si tras 3 meses da < 1 % de las vistas **y** < 5 interacciones por publicación, pasa a espejo automático |
| **mastodon.gal** | Cuenta en la instancia gallega (pedir alta en M1; requiere aprobación). Mismas publicaciones que en Bluesky, con #historia #galego #PropónUnSerán y descripción de imagen (accesibilidad, norma de la casa en el fediverso) | Igual que Bluesky | Seguidores; impulsos | 40 / 120 | Igual |
| **Telegram** | Canal propio *"Serán · avisos"*: un solo mensaje por episodio, a la hora de la estrea: *"Esta noite hai serán: [tema], [duración]. Boas noites."* Además, cada episodio entra en el canal de avisos de Podgalego (120 suscriptores) | 1 por episodio | Suscriptores; clics | 30 / 100 | No se abandona (coste casi cero); es el canal preferido para la diáspora mayor [S] |
| **Reddit** (r/galicia, r/Galiza) | **Nada de autopromoción por episodio.** El promotor participa con su cuenta personal en hilos de historia y, en la fase pública, hace **una sola publicación por serie** explicando qué es Serán, cómo se hace (IA incluida) y pidiendo temas. Se respetan las normas de cada comunidad | 1 publicación en M5 + 1 en las Letras (M8) + 1 por serie nueva | Votos, comentarios, tráfico desde reddit.com; sentimiento sobre la IA (entra en E8) | 2 / 5 publicaciones; sentimiento negativo ≤ 30 % | Si una publicación recibe rechazo neto por la IA, no se repite en esa comunidad y se registra en E8 |
| **X** | Solo espejo automático de las publicaciones de Bluesky; handle reservado | Automático | Clics | Sin meta | Se reconsidera solo si en M6 aporta > 10 % de los clics de redes |
| **Red de pódcast en galego** | (1) Alta en **Podgalego** y en **Obradoiro Dixital Galego** en M3 (cuando ya se cumple la regla de ≥ 1 publicación al mes). (2) Entrar en el Discord de Obradoiro y presentarse como proyecto, con la nota sobre la IA por delante. (3) **Intercambio de menciones** con los pódcast de la categoría "Historia" de Podgalego: ellos nombran Serán con su voz humana; nosotros los recomendamos en la Carta y en la descripción (nunca con la voz sintética leyendo a otros). (4) Invitaciones a conversas (§2.5) | Alta única; 1 intercambio al mes desde M5 | Nº de intercambios; tráfico por enlace propio; menciones | 2 / 8 intercambios | — |
| **Carta do serán** (§2.8.3 c) | Mensual (Etapa 1), quincenal (Etapa 2) | Según etapa | Suscriptores; tasa de apertura; clics al episodio; respuestas con temas | 40 / 150 suscriptores; apertura ≥ 45 % | Si la apertura es < 25 % durante 3 envíos, se acorta y se pasa a trimestral |

**Métrica agregada de comunidad:** vistas atribuibles a los espacios propios (enlaces cortos + fuente "Externo" desglosada por sitio en Studio: bsky.app, t.me, reddit.com, el proveedor de correo) **≥ 5 % de las vistas en M6 y ≥ 8 % en M12** [S]. La cifra es modesta a propósito: el objetivo de estos espacios es el hábito y la reputación, no el volumen.

#### 2.8.5 Presupuesto de tiempo y automatización

| Tarea | Quién | Tiempo Etapa 1 | Tiempo Etapa 2 |
|---|---|---|---|
| Redactar las publicaciones de cada episodio (Bluesky/Mastodon/Telegram) y el borrador de la Carta | Agente "productor" del pipeline (`drafts/pipeline.md`) a partir del guion y la hoja de fuentes; pasan por el mismo control lingüístico que el guion | 0 h del promotor | 0 h |
| Aprobar y programar | Promotor | 10 min por episodio | 10 min por episodio |
| Estrea en el chat | Promotor | 15 min cada 2 semanas | 15 min por semana |
| Responder comentarios y menciones (siempre a mano) | Promotor | 20 min por semana | 45 min por semana |
| Carta (revisar y enviar) | Promotor | 30 min al mes | 30 min cada 2 semanas |
| Intercambios, Reddit, Discord | Promotor | **10 min** al mes desde M5 (antes 30; v5) | 1 h al mes |
| **Adyacencia (v5):** revisar la lista de semillas y la tarjeta de sugeridos, anotar R1-R3, preparar Test & Compare (§2.4 bis) | Promotor; el agente "productor" propone 3 miniaturas y el título espejo | **20 min al mes** | 30 min al mes |
| **Total** | | **≈ 1 h/semana** | **≈ 2 h/semana** |

**Encaje con el presupuesto de horas.** Etapa 1: 12 episodios × ≤ 6,5 h = 78 h, más ~24 h de comunidad (≈ 1 h/semana durante 24 semanas desde M2) ≈ **102 h**, que es exactamente el total de la Etapa 1 (17 h/mes × 6, `drafts/retornos.md` A15-17). **Queda sin margen**, y la construcción del pipeline en M1 ya presiona ese total. **La adyacencia (v5) no añade horas:** sus 20 min al mes salen de Reddit y los intercambios, que bajan de 30 a 10 min, porque un sugerido ganado sigue trayendo vistas sin más trabajo y una publicación en Reddit no [S]. Por eso hay un **mínimo innegociable de ≈ 35 min/semana** (estrea, respuesta a comentarios, publicaciones automáticas aprobadas y Telegram) y todo lo demás es recortable: si las horas por episodio superan 6,5 h, se quitan primero Reddit y los intercambios, después la participación en Bluesky/Mastodon, después la revisión mensual de semillas (se hace cada 2 meses), y nunca la respuesta a comentarios ni la estrea [S]. Si ni el mínimo cabe, es una señal de que el pipeline no cumple su promesa de tiempo, y eso se evalúa en la P1 (KPI "horas del promotor por episodio"). Etapa 2: 4 episodios × ~2 h + ~9 h de comunidad ≈ 17 h/mes, dentro de las ~35 h/mes de `drafts/retornos.md` §0.

**Transparencia también aquí:** la biografía de cada cuenta dice *"Historia de Galicia para durmir. Feito con IA, revisado por persoas."* Las publicaciones redactadas con ayuda del pipeline van firmadas por quien las revisa.

---

## 3. Riesgos y cumplimiento

### 3.1 Política de contenido inauténtico de YouTube

**Qué dice** [F]:
- Desde el 15-07-2025, el antiguo "contenido repetitivo" se llama **"inauthentic content"**. Incluye "AI-generated content made with generic or unoriginal templates giving the impression of mass production" y "similar or repetitive content with low educational value". Sí se permiten series con un "distinct storyline, focus, or concept" [F https://support.google.com/youtube/answer/1311392?hl=en].
- **El 16-07-2026 se aclaró** en tres categorías no monetizables: (1) contenido genérico, repetitivo o de plantilla con variación mínima; (2) contenido perturbador o manipulador; (3) **personas IA que hablan de finanzas, derecho o salud**. Un canal con "demasiado" de cualquiera de ellas no puede monetizar, **sea o no IA** [F https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/].
- Aplicación real: en enero de 2026 se terminaron 16 canales de *slop*, con 35 M de suscriptores [F https://www.techtimes.com/articles/320629/20260715/youtube-wiped-35m-subscribers-over-ai-slop-now-its-judging-your-taste.htm].

**Por qué nos afecta:** el formato "para dormir" es plantillado por naturaleza (misma voz, ritmo, imágenes lentas y duración) [R `retornos.md` §6.1]. **Probabilidad media, impacto alto**: sin YPP no hay anuncios, Premium ni membresías.

**Categoría 3 (salud):** el canal habla de sueño. **No se hacen afirmaciones terapéuticas** ("cura o insomnio", "tratamento"), no hay una persona IA con cara y el sueño no se trata como tema de salud. La Sociedad Española de Neurología ya alerta contra productos "sin validez médica" para el insomnio [F https://www.vademecum.es/noticia-251216-la+sociedad+espa+ntilde+ola+de+neurolog+iacute+a+advierte+sobre+el+creciente+aumento+de+productos+y+servicios+sin+validez+m+eacute+dica+dirigidos+a+personas+con+insomnio+_644195]. **Lema permitido:** "para relaxarte e deixarte levar ata o sono". **Prohibido:** cualquier mensaje de salud.

**Mitigaciones** (alineadas con los 12 controles de `drafts/pipeline.md` §8):
1. **Tema, fuentes y estructura únicos** en cada episodio, con hoja de fuentes pública.
2. **Series con arco propio** y cadencia moderada: 2 episodios al mes en la Etapa 1 y 3-4 en la Etapa 2. **Nunca a diario.**
3. **Nada de bucles, directos 24/7 con material repetido ni recopilaciones** hasta tener un catálogo amplio. Cuando lleguen, con un montaje nuevo (introducción y transiciones propias) y como máximo 1 al mes [S].
4. **Presencia humana visible:** créditos de revisión, conversas con voz humana (§2.5) y respuestas a comentarios con nombre.
5. **Expediente por episodio** (fuentes, versiones, informes de control de calidad y firmas), por si hay que apelar [R `drafts/pipeline.md`].
6. **Indicador de alerta:** si llega un aviso de "limited or no ads" o se rechaza la solicitud al YPP, se congela la producción, se revisa la variedad del catálogo y se apela con el expediente.

### 3.2 Etiqueta de contenido alterado o sintético de YouTube

- Es obligatoria para contenido **realista** que se pueda confundir con personas, lugares o hechos reales. **Declarar no reduce el alcance ni la monetización**; no declarar puede llevar a la retirada del contenido o a la suspensión del YPP [F https://support.google.com/youtube/answer/14328491?hl=en ; https://blog.youtube/news-and-events/disclosing-ai-generated-content/].
- **Decisión** [S]:
  - estilo visual pictórico (óleo oscuro), no fotorrealista;
  - **activar la etiqueta siempre** en cualquier caso: la voz es sintética y el coste es cero;
  - coherente con la política de transparencia (§2.6).

### 3.3 AI Act, artículo 50

**Estado:** las obligaciones de transparencia del art. 50 **se aplican desde el 2-08-2026 y no se aplazaron**. El Digital Omnibus (acuerdo del 7-05-2026, adoptado por el Consejo el 29-06-2026) retrasó los sistemas de alto riesgo, no el art. 50 [F https://www.goodwinlaw.com/en/insights/publications/2026/08/alerts-technology-dpc-eu-ai-act-transparency-obligations-now-in-force ; https://www.joneswalker.com/en/insights/blogs/ai-law-blog/yes-august-2-still-matters-the-eu-approved-a-high-risk-ai-delay-but-most-trans.html?id=102nbon]. Lo que sí se aplazó, hasta el 2-12-2026, es el marcado legible por máquina (art. 50.2) para los **proveedores** de sistemas generativos ya en el mercado [F ídem, usercentrics]. Es obligación del proveedor (Nós, Google, ElevenLabs…), no nuestra.

**Nuestro papel:** somos **responsables del despliegue** (*deployer*), porque usamos la IA en una actividad profesional y monetizada [S, interpretación].

| Obligación del art. 50.4 | ¿Nos aplica? | Cómo cumplimos |
|---|---|---|
| **Texto generado por IA publicado "para informar al público sobre asuntos de interés público"** | Probablemente sí: la divulgación histórica puede entrar [S] | **Excepción:** no hay que etiquetar si el contenido "has undergone a process of human review or editorial control" y una persona "holds editorial responsibility" [F https://artificialintelligenceact.eu/article/50/]. **El promotor firma como responsable editorial**; el expediente prueba la revisión. Aun así, se declara (§2.6) |
| **Deepfakes**: el art. 3(60) los define como contenido de imagen, audio o vídeo generado o manipulado por IA "that resembles existing persons, objects, places, entities or events and would falsely appear to a person to be authentic or truthful" [F https://artificialintelligenceact.eu/article/3/] | Imágenes realistas de lugares o hechos reales: posible. **Voz: sí, si se usa una voz de Nós.** Brais es la voz de Gaspar González Somoza y Celtia la de Consuelo Díaz Isorna, locutores profesionales identificados en las fichas de los datos [F https://huggingface.co/datasets/proxectonos/Nos_Brais-GL ; https://huggingface.co/datasets/proxectonos/Nos_Celtia-GL]; Sabela-Nós es una locutora de radio profesional [F https://zenodo.org/records/8027725]. Un audio que suena como una persona existente **se parece a ella**; que "parezca auténtico" es discutible con un aviso, pero **se trata como deepfake por prudencia** [S, interpretación]. Con las voces de Azure o Google, la persona de base no es identificable para el público y el riesgo es menor [S] | Estilo pictórico en las imágenes; si alguna es realista, se etiqueta. **Voz: el aviso dice que es sintética y de quién es la voz de base** (§2.6), no solo "voz sintética". La excepción para obras "evidently artistic, creative… or fictional" **no aplica** a la divulgación histórica, así que el aviso es completo, no reducido [F https://artificialintelligenceact.eu/article/50/] |
| **Momento y forma:** "at the latest at the time of the first interaction or exposure", de forma clara y accesible (art. 50.5) [F ídem] | Sí | **Aviso hablado en los primeros 30 s** + etiqueta de YouTube + nota en la descripción |

- **Código de Práctica** sobre marcado y etiquetado (versión final publicada el 10-06-2026; voluntario): contempla el icono de la UE y, para el contenido **solo de audio, avisos hablados** [F https://digital-strategy.ec.europa.eu/en/news/commission-publishes-code-practice-marking-and-labelling-ai-generated-content ; https://www.scl.org/european-commission-publishes-code-of-practice-on-marking-and-labelling-ai-generated-content/]. **Se adopta como referencia de buenas prácticas**, sin firmarlo (está pensado para organizaciones) [S].
- **Sanciones:** los incumplimientos del art. 50 pueden llegar a 15 M€ o al 3 % de la facturación; el art. 99.4 fija "whichever is higher" con carácter general, pero **para pymes y *start-ups* se aplica la menor de las dos cifras (art. 99.6)** [F https://artificialintelligenceact.eu/article/99/]. En la práctica, el riesgo para un canal pequeño que etiqueta es bajo [S].
- **España:** el Proyecto de Ley Orgánica para el buen uso y la gobernanza de la IA (Consejo de Ministros, 26-05-2026; BOCG, 12-06-2026) está **en tramitación, todavía no vigente**. Designa a la AESIA y regula el etiquetado de los *deepfakes* [F https://www.lamoncloa.gob.es/consejodeministros/resumenes/paginas/2026/260526-rueda-prensa-ministros.aspx ; https://www.congreso.es/public_oficiales/L15/CONG/BOCG/A/BOCG-15-A-97-1.PDF]. **Acción:** revisarla cada trimestre; el diseño actual ya va por encima del mínimo.

### 3.3 bis La voz de base: derecho a la propia voz y consentimiento del locutor

**El problema, sin rodeos.** Toda voz sintética "natural" sale de horas de grabación de una persona real. Las candidatas del kit A/B que mejor pueden sonar (Nós StyleTTS2 Brais y Celtia, Sabela-Nós VITS) son voces de profesionales **con nombre y apellidos publicados** y reconocibles en un mercado pequeño como el gallego. La licencia Apache-2.0 del modelo cubre los derechos sobre el software y los pesos, **no el derecho de la persona sobre su voz**.

| Capa | Qué dice | Qué implica para Serán |
|---|---|---|
| **Derecho a la propia voz** (LO 1/1982) | Art. 7.6: es intromisión ilegítima "la utilización del nombre, de la voz o de la imagen de una persona para fines publicitarios, comerciales o de naturaleza análoga". Art. 2.2: el consentimiento debe ser expreso y "será revocable en cualquier momento", indemnizando los daños y las "expectativas justificadas" [F https://www.boe.es/buscar/act.php?id=BOE-A-1982-11196] | Un canal monetizado es un fin comercial. Si una voz sintética reconocible "es" la voz del locutor —cuestión que la jurisprudencia no ha cerrado para voces generadas [S]—, sin su consentimiento expreso para **este** uso hay riesgo de demanda. **Se trata como si la ley aplicara** |
| **Condiciones de los datos** (USC) | Brais y Celtia: "solely for research purposes and for developing artificial intelligence tools focused on linguistic objectives"; prohibido usarlos de forma que vulnere "the rights, privacy, or dignity" de las personas representadas. En Celtia, la propiedad de los datos está cedida a la USC durante 15 años y se borrarán desde el 30-11-2037 [F https://huggingface.co/datasets/proxectonos/Nos_Brais-GL ; https://huggingface.co/datasets/proxectonos/Nos_Celtia-GL] | Lo que firmaron los locutores con la USC probablemente cubre la investigación y las herramientas lingüísticas, **no** un canal comercial de terceros [S]. Solo la USC puede aclararlo (paso 1 del §2.6 bis) |
| **Licencia del modelo** (Apache-2.0) | Permite uso comercial con atribución [R `voz_guion.md` §1.1]. La ficha del modelo no dice nada sobre el consentimiento del locutor [F https://huggingface.co/proxectonos/Nos_StyleTTS2-Brais-GL] | Necesaria, **no suficiente** |
| **AI Act, art. 50.4 y 3(60)** | Deepfake = audio que se parece a personas existentes (§3.3) | Aviso con la identidad de la voz de base |
| **Voces de proveedor** (Azure, Google) | Microsoft permite usar las voces neuronales precompiladas en los casos de uso que elija el cliente, conforme a su política de uso aceptable y su código de conducta, "No registration or pre-approval is required", y exige revelar la naturaleza sintética de la voz [F https://learn.microsoft.com/en-us/legal/cognitive-services/speech-service/text-to-speech/transparency-note]. La relación con la locutora la gestiona el proveedor [S] | **Cadena de consentimiento documentada**: se archiva la versión de los términos en el expediente. Es la **voz de reserva por defecto** |

**Regla del proyecto (sustituye a "nunca recrear la voz de una persona real", que era incoherente con usar las voces de Nós):**
1. **Ninguna voz de una persona identificable sale al público sin doble permiso escrito**: el del titular de los datos (USC/Gradiant, o el proveedor) y el de la persona que prestó la voz.
2. **Voces de proveedor comercial** (Azure Sabela/Roi, Google gl-ES): el permiso es la licencia del servicio; se archiva.
3. **Voces de Nós** (Brais, Celtia, Sabela-Nós, Icía, Iago, Paulo): solo con el consentimiento personal firmado (§2.6 bis). **Sin él, la voz queda excluida del E0 a efectos de publicación**, aunque gane la escucha ciega interna.
4. **ElevenLabs:** solo voces por defecto del propio servicio con uso comercial en el plan contratado; **nunca** voces de la biblioteca comunitaria ni clonación sin contrato [S, verificar términos en M1].
5. **Nunca** se imita a una persona concreta, viva o muerta, ni se clona una voz a partir de grabaciones públicas.

### 3.4 Derechos de autor: fuentes, textos, imágenes, música y licencias de voz

| Material | Situación | Regla del proyecto |
|---|---|---|
| **Hechos históricos** | No tienen derechos de autor; los tiene la **expresión** | El guion se escribe en galego y es original. Nunca se copian frases ni estructuras de obras protegidas [S, principio general del TRLPI: https://www.boe.es/buscar/act.php?id=BOE-A-1996-8930] |
| **Galipedia** | CC BY-SA 4.0 [R `voz_guion.md` §2.3] | Se usa como esqueleto factual. Si se reutilizan frases, hay que atribuir y compartir igual. **Por defecto se parafrasean los hechos** y se contrastan con fuentes académicas |
| **Consello da Cultura Galega / culturagalega.org** | Prohibida la reutilización comercial sin autorización; CC 3.0 no comercial y sin obra derivada [R `voz_guion.md` §2.3] | **Solo para verificar datos.** Nada de su texto entra en el guion ni en el RAG. Si se quiere más, se pide autorización por escrito |
| **Clásicos de dominio público** (Murguía †1923, López Ferreiro †1910, Vicetto †1878) | Dominio público: vida del autor + 80 años para autores fallecidos antes de 1987 [R] | Se pueden usar para ambiente y relato. **Su historiografía romántica está superada**: nunca como fuente de verdad sin contraste |
| **Autores modernos**, p. ej. **Neira Vilas (†2015)** | Protegidos: vida + 70 años (autores fallecidos después del 7-12-1987), es decir, hasta el 31-12-2085 inclusive [F TRLPI art. 26: https://www.boe.es/buscar/act.php?id=BOE-A-1996-8930] | Para la fecha de las Letras: **contexto histórico propio**, sin leer ni adaptar sus textos ni usar sus personajes. Si se quiere cita, solo la breve del art. 32 TRLPI, con atribución, y mejor evitarla |
| **Imágenes generadas con IA** | En España solo protege obras de una persona natural (TRLPI art. 5) → nuestras imágenes probablemente **no son protegibles**: otros podrían reutilizarlas [S, interpretación] | Hay que aceptarlo. La marca se protege con nombre, estilo y sello sonoro, no con las imágenes |
| **Licencia del generador de imágenes** | **FLUX.1 [dev]: licencia no comercial para el modelo**; la cláusula sobre las salidas cambió en la v1.1 y la situación es ambigua [F https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md ; https://artificialguy.com/blog/flux-licensing-commercial-use/] | **No usar FLUX.1 [dev] en un canal monetizado.** Alternativas: FLUX.1 [schnell] (Apache-2.0 [S, verificar ficha]), una API de pago con licencia comercial (p. ej. Imagen, como prevé `drafts/pipeline.md`) o una licencia comercial de BFL |
| **Imágenes históricas reales** (grabados, mapas antiguos, fotos de yacimientos) | Wikimedia Commons: muchas en dominio público o CC; hay que revisar una a una [S] | Atribución en la descripción. Los mapas de base de OpenStreetMap exigen atribución (ODbL) [S, conocido] |
| **Música y ambiente** | Riesgo de reclamaciones de Content ID en vídeos de 2 h | Paisaje sonoro grabado por el promotor, como prevé `drafts/formato.md` §6, o bibliotecas con licencia comercial documentada. Umbral: 0 reclamaciones en los 6 primeros episodios |
| **Voz: Proxecto Nós** | Los **modelos** tienen licencia Apache-2.0 (permite uso comercial con atribución). Los **datasets** de Brais y Celtia dicen "solely for research purposes" y prohíben la "public exposure" de las grabaciones [R `voz_guion.md` §1.1] | La vía Apache cubre el modelo, **no la voz de la persona** (LO 1/1982, §3.3 bis). **Doble permiso escrito antes del primer episodio:** USC/Gradiant (uso comercial compatible con las condiciones de los datos) **y** el locutor (consentimiento personal, §2.6 bis). Crédito al modelo y a la persona en cada episodio. Si falta cualquiera de los dos antes del 6-11-2026, se publica con la voz de reserva de proveedor |
| **Voz: Azure, Google o ElevenLabs** | Uso comercial según las condiciones de cada servicio (ElevenLabs: desde el plan Starter) [R `voz_guion.md` §1.4] | Guardar una copia de las condiciones vigentes en la fecha de uso, dentro del expediente |
| **Voz: locutor licenciado (Etapa 3)** | Referencia de mercado: 1.000-7.500 € (UVA, 2024) [R] | Contrato con medios, plataformas y duración definidos; remuneración y *revenue share*; **cláusula de retirada** [R] |
| **Spotify** | Prohíbe los pódcast IA que suplantan a otra persona [F https://variety.com/2026/digital/news/spotify-bans-ai-generated-podcasts-impersonate-verified-badges-1236752944/] | Se cumple: no se suplanta a nadie (la voz se presenta como sintética y con el nombre y el permiso de su dueño) |
| **Marca "Serán"** | El handle y el dominio están libres; falta la búsqueda en OEPM y EUIPO [R `drafts/formato.md` §10] | Búsqueda en M1. Si no hay conflicto, valorar el registro de la marca nacional en la clase 41 cuando se pase la Puerta 1 [S] |

### 3.5 Reputación en la comunidad galega

| Riesgo | Señal | Probabilidad / impacto [S] | Mitigación |
|---|---|---|---|
| **Errores de lengua** (castellanismos, vocales abiertas o cerradas mal dichas, topónimos) | Comentarios que señalan errores; crítica en redes de filólogos | Media / **alto**: es justo lo que el público galego castiga | Cinturón lingüístico del pipeline; "mosaico de risco" de audio [R `drafts/pipeline.md` §3.3]; panel E2; corrección pública en menos de 72 h |
| **Errores históricos** | Corrección de un historiador en público | Media / alto | Hoja de fuentes; revisión científica (§2.5); página de erratas |
| **Rechazo a la IA** por parte del sector de la voz y del activismo lingüístico | Artículo crítico en prensa en galego; campaña en redes | Media / medio-alto. Hay precedentes: RTVE (febrero de 2026) y la CSAG/Caamaño (mayo de 2026) [F, §2.6] | Transparencia total (§2.6); créditos al modelo y al locutor; **nunca suplantar a nadie**; **contacto con ADA y AGPTI antes del lanzamiento, con oferta de crédito y remuneración** (§2.6 bis); compromiso público con la voz licenciada en la Etapa 3; tono no defensivo: responder con datos y corregir |
| **Voz de un profesional gallego usada sin su consentimiento comercial** (Brais, Celtia o Sabela-Nós) | El locutor, un compañero o ADA reconocen la voz; artículo "a IA usa a voz dun actor galego sen permiso"; requerimiento legal por el art. 7.6 de la LO 1/1982 | **Baja si se aplica la regla / muy alto si ocurre**: combina el precedente de la CSAG/Caamaño con un posible conflicto legal, y afecta al corazón del producto (la voz) [S] | **Consentimiento del locutor verificado = condición de la Puerta 0** (§4.2); doble permiso archivado en el expediente; aviso que nombra la voz de base; oferta de crédito, 10 % de ingresos y pago a la firma; diálogo previo con ADA y AGPTI (§2.6 bis); voz de reserva de proveedor lista desde el E0; si hay retirada, sustitución del catálogo en ≤ 30 días |
| **Guerra normativa** (norma RAG frente al reintegracionismo) | Debate en los comentarios sobre la ortografía | Alta / bajo | Norma RAG/ILG declarada en la web ("seguimos a norma oficial"), sin entrar en polémica; las "Normas do serán" dejan el debate normativo fuera de los comentarios y prohíben corregir el galego de otros usuarios (§2.8.3 b). La prioridad es el oyente dormido, no el debate |
| **Politización de temas identitarios** (Reino de Galicia, Irmandiños, 25 de xullo) | Captura partidista del canal; comentarios polarizados | Media / medio | Tono descriptivo y sereno; temas excluidos (Guerra Civil, represión, política reciente) según `drafts/formato.md` §8; moderación de comentarios con reglas publicadas |
| **Imagen de "fábrica de slop"** | Comparación con canales IA de castellano | Baja-media / alto | Cadencia moderada, variedad, presencia humana (§3.1) |
| **Confusión con contenido infantil** | Nombre o estética "de nana"; que YouTube lo trate como "made for kids" | Baja / medio | Configurar "non dirixido a nenos"; miniaturas adultas; descartado el nombre "Arrolo" [R `drafts/formato.md` §10] |

### 3.6 Otros riesgos

| Riesgo | Probabilidad / impacto [S] | Mitigación / indicador |
|---|---|---|
| **Demanda insuficiente** (3,59 % de consumo audiovisual en galego) | Alta / alto | El plan de pruebas lo mide pronto y barato (Puerta 1, M6, 12 vídeos: coste máximo de ~210 € y ~100 h [R `drafts/retornos.md` §0]). Salida: pasar a audio-primero (Spotify, iVoox, Radio Galega) o a la Etapa 3 de localización |
| **Dependencia de una plataforma** | Media / alto | Feeds de pódcast propios (RSS) desde el principio; web propia; **"Carta do serán" desde M2** y canal de Telegram (§2.8.3-2.8.4): la relación con el oyente no depende de una sola plataforma. Indicador: suscriptores de la Carta ≥ 40 en M6 y ≥ 150 en M12 |
| **Cambio de condiciones del YPP** (8.000 h desde el 1-02-2027 para nuevos solicitantes [F https://blog.youtube/news-and-events/youtube-partner-program-updates-2027-new-opportunities-earn/]) | Cierta / medio | Ya incluido en el modelo de `drafts/retornos.md` |
| **Anuncios que despiertan al oyente** (quejas públicas en el género [F https://www.sbs.com.au/news/article/sleep-videos-are-hugely-popular-but-youtube-adverts-are-disrupting-peoples-dreaming/edc0h3p1r]) | Alta cuando se monetice / medio | "Sen cortes" como marca; 20-30 min de cola de ambiente como colchón [R `drafts/formato.md`] |
| **Tiempo y desgaste del promotor** (4 h/semana) | Media / alto | Cadencia de 2 episodios al mes; el pipeline absorbe la producción; la promoción se limita a las fechas ancla |
| **Protección de datos** (correos a entidades, Carta, propuestas de temas) | Baja / bajo | Solo correos institucionales publicados, un contacto por entidad, baja inmediata. Carta: doble confirmación, aviso de privacidad, baja en un clic, solo mayores de 14 años. Nombre de quien propone un tema o recibe una dedicatoria: **solo con permiso escrito** (§2.8.2) [S] |
| **Comunidad que se agria** (debate normativo, política, ataques a quien aprende) | Media / medio | "Normas do serán" publicadas y moderación de Studio (§2.8.3 b); respuesta humana en ≤ 48 h; % de comentarios retenidos como indicador (alerta si > 15 % en un mes) [S] |
| **Carga de comunidad que se come el tiempo del promotor** | Media / medio | Tope de ≈ 1 h/semana en la Etapa 1 con mínimo innegociable de 35 min y orden de recorte (§2.8.5) |

### 3.7 Lista de cumplimiento previa al primer episodio (resumen)

- [ ] **Voz con cadena de consentimiento documentada:** si es de Nós, confirmación escrita de la USC/Gradiant **y** consentimiento firmado del locutor (§2.6 bis); si es de proveedor, copia de los términos de uso vigentes.
- [ ] Aviso escrito y hablado que dice **de quién es la voz de base** (o "locutor/a profesional", si es anónima o de proveedor).
- [ ] Carta a ADA y AGPTI enviada y su respuesta (o su silencio) registrada en el expediente.
- [ ] Voz de reserva generada y probada en 15 min del episodio 1 (para sustituir en ≤ 30 días si alguien retira su permiso).
- [ ] Generador de imágenes con licencia comercial clara (sin FLUX.1 [dev]).
- [ ] Paisaje sonoro propio o con licencia documentada.
- [ ] Búsqueda de "Serán" en OEPM y EUIPO.
- [ ] Página "Como facemos Serán", con la nota del proceso y las erratas.
- [ ] Aviso hablado en los primeros 30 s.
- [ ] Etiqueta de contenido alterado o sintético activada.
- [ ] Canal configurado como "non dirixido a nenos".
- [ ] Expediente del episodio completo, con firma editorial del promotor.
- [ ] Ninguna afirmación de salud en título, descripción ni narración.
- [ ] "Normas do serán" publicadas; retención de comentarios, palabras bloqueadas y retención de enlaces configuradas en Studio (§2.8.3 b).
- [ ] Carta do serán con doble confirmación, aviso de privacidad y baja en un clic; formulario "Propón un serán" con consentimiento para citar el nombre.

---

## 4. Plan de pruebas por etapas

### 4.0 Reglas comunes (cadencia, relojes y de dónde sale cada número)

**Una sola cadencia para todo el plan** (igual que la del modelo `drafts/retornos.md`, A4):

| Tramo | Cadencia fija | Vídeos publicados al cierre |
|---|---|---|
| M1 (oct-2026) | 0: construcción, E0 y E1 | 0 |
| M2 (nov-2026) | **Lanzamiento con 3 episodios** (los 3 que exige la Puerta 0), el **domingo 22-11** (día fijo del ritual, §2.8.2) | 3 |
| M3-M5 (dic-2026 a feb-2027) | **Quincenal: 2 al mes** | 5 · 7 · 9 |
| M6 (mar-2027) | 2 quincenales + 1 especial del Día Mundial do Sono | **12 → Puerta 1** |
| M7-M12 (abr-sep 2027, Etapa 2) | **Semanal: 4 al mes** (26 semanas con 2 de descanso) | 16 · 20 · 24 · 28 · 32 · **36 → Puerta 2** |
| M13-M18 | Semanal: 4 al mes | **60 → Puerta 3** |
| Mantenimiento (si no se pasa la P3) | 1 al mes | 78 en M36 |

**Por qué el lanzamiento con 3 episodios y el especial de marzo.** El pipeline no da un episodio publicable hasta la semana 7-8 [R `drafts/pipeline.md` §0.10], así que el reloj de publicación empieza en M2 y no en M1 como en el modelo. Los dos vídeos "extra" (el tercero del lanzamiento y el especial de marzo) compensan ese mes perdido y hacen que **la Puerta 1 se evalúe con 12 vídeos, como en `drafts/retornos.md`**. Coste en horas: 12 episodios × ≤ 6,5 h [R `drafts/pipeline.md`] = 78 h, dentro de las ~102 h de la Etapa 1.

**Comprobación de que el cambio de calendario no mueve las puertas.** Se ha repetido el modelo mensual de `drafts/retornos.md` con este calendario exacto (script `gauntlet/model/puertas_gtm.py`, que reutiliza `modelo2.py` y solo cambia los vídeos publicados por mes). Los valores en los cortes cambian en ±1 unidad (base en M6: 24 suscriptores frente a 25; en M12: 107 frente a 108; horas en 12 meses en M12: 2.681 frente a 2.696). **Las fechas de desbloqueo no cambian** (tabla 4.2). En lo que sigue se usan los valores del calendario real; todos son [S], salida del modelo.

**Qué es cada métrica en las puertas** (para que se lea igual en Studio que en el modelo):
- **"Vistas a 30 días"** = media de las vistas que acumula cada vídeo en sus primeros 30 días, calculada sobre los vídeos que ya han cumplido 30 días en la fecha de la puerta (en la P1, los vídeos 4-9; en la P2, los publicados en M10-M11). Equivale a `vnew` del modelo.
- **"Suscriptores"** = total del canal en la fecha de la puerta.
- **"Horas 12 m"** = horas de visionado públicas de los últimos 365 días que muestra Studio (las *qualified* del YPP).
- **"AVD"** = duración media vista del conjunto de vídeos largos del periodo.

**KPIs de hábito (nuevos en v4) y de embudo de recomendación (R1-R3, nuevos en v5).** Todos se leen en Studio con las definiciones oficiales y se calculan como **media de las dos últimas ventanas de 28 días** antes de la fecha de lectura, para amortiguar el ruido de números pequeños (en M6 la base tiene ~200 espectadores únicos al mes [S]):

| Código | KPI | Definición (Studio) | M4 (lectura temprana) | **P1 · M6** | M9 (control) | **P2 · M12** | Señal alta (P1 / P2) |
|---|---|---|---|---|---|---|---|
| **H1** | **% espectadores recurrentes** | Recurrentes / (nuevos + recurrentes). "Returning viewers: the number of viewers who already watched your channel, and returned to watch in the selected time period" [F https://support.google.com/youtube/answer/9314416?hl=en] | ≥ 15 % | **≥ 20 %** | ≥ 25 % | **≥ 30 %** | ≥ 35 % / ≥ 40 % |
| **H1b** | Espectadores habituales | "Regular viewers": han visto el canal al menos una vez al mes durante más de 6 meses del último año [F ídem]. Solo es medible desde ~M8 (el canal nace en M2) | — | — | control | **control**: ≥ 25 personas [S] | ≥ 100 |
| **H2** | Horas por espectador único | Tiempo de visualización / espectadores únicos (28 días) | ≥ 0,6 h | **≥ 0,75 h** | ≥ 0,9 h | **≥ 1,0 h** | ≥ 1,5 h / ≥ 2,0 h |
| **H3** | Vistas por espectador | Vistas / espectadores únicos (28 días); capta a quien repite el mismo episodio | ≥ 1,2 | **≥ 1,3** | ≥ 1,4 | **≥ 1,5** | ≥ 1,8 / ≥ 2,0 |
| **H4** | Reproducción continua | % de vistas desde "Listas de reproducción" ("any playlist that included one of your videos") + "Vídeos sugeridos" cuyo vídeo de origen es del propio canal [F https://support.google.com/youtube/answer/9314355?hl=en] | ≥ 10 % | **≥ 15 %** | ≥ 18 % | **≥ 20 %** | — |
| **H5** | Navegación | % de vistas desde "Funciones de navegación": "Home, subscriptions, Watch Later, Trending/Explore, and other browsing features" [F ídem] | ≥ 10 % | **≥ 15 %** | ≥ 20 % | **≥ 25 %** | — |
| **H4+H5** | **Tráfico de hábito** | Suma de H4 y H5 (más "Notificaciones") | ≥ 20 % | **≥ 30 %** | ≥ 35 % | **≥ 45 %** | ≥ 45 % / ≥ 60 % |
| control | Dependencia de siembra | % de vistas desde "Fuentes externas" + "Directo o desconocido" | — | control | — | **alerta si > 50 %** | — |
| **R1** | **Embudo (v5): impresiones por vídeo a 28 días** | Impresiones de miniatura registradas por YouTube ("How many times your thumbnails were shown to viewers on YouTube through registered thumbnail impressions"; búsqueda, inicio, feeds y "A continuación"; no cuentan webs externas ni pantallas finales) [F https://support.google.com/youtube/answer/9314486?hl=en]. Media de los vídeos que han cumplido 28 días en la fecha de lectura | ≥ 450 | **≥ 700** | ≥ 1.000 | **≥ 1.200** | ≥ 2.000 / ≥ 5.000 |
| **R2** | **Embudo (v5): CTR de impresiones en navegación y sugeridos** | "How often viewers watched a video after seeing a thumbnail" [F ídem], filtrado por fuente de tráfico ("Funciones de navegación" + "Vídeos sugeridos"). Media de 28 días de los vídeos largos | Objetivo **4-6 %**; **alerta < 3 %**; **se recalibra aquí** (objetivo = mediana propia de los vídeos 1-4, dentro de 3-7 %) | **≥ 4 %** (alerta < 3 %) | ≥ 4 % | **≥ 4 %** (alerta < 3 %) | ≥ 6 % con AVD ≥ 30 min |
| **R3** | **Embudo (v5): cuota de sugeridos desde canales ajenos** | % de vistas desde "Vídeos sugeridos" cuyo vídeo de origen **no** es del propio canal (tarjeta "Fuente de tráfico: vídeos sugeridos" [F https://support.google.com/youtube/answer/9314355?hl=en]). Disjunto de H4, que cuenta el sugerido propio | ≥ 5 % (control) | **≥ 10 %** | ≥ 15 % | **≥ 20 %** | ≥ 25 % / ≥ 35 % |
| R3b | Semillas activas | N.º de vídeos de la lista de semillas (§2.4 bis) que aparecen entre las 10 primeras fuentes de sugeridos ajenos en 28 días | — | **≥ 1** (control) | ≥ 2 | **≥ 3** (control) | — |
| control | Guardarraíl de empaquetado | CTR de R2 **> 8 %** con AVD **< 20 min** en el mismo vídeo = la miniatura promete otra cosa | alerta | alerta | alerta | alerta | — |

**De dónde salen los umbrales** [S, derivados del modelo, sin *benchmark* público localizado]:
- **H1.** En la base, en M6 hay 24 suscriptores y ~285 vistas al mes; con ~1,4 vistas por espectador son ~200 espectadores únicos. Si vuelven los suscriptores y un número parecido de no suscritos (~48 personas), los recurrentes son ~24 %: el umbral del 20 % deja margen de ruido. En M12: 108 suscriptores, ~880 vistas y ~590 únicos → ~30 %. En el clónico (5 suscriptores, ~70 únicos) saldría un ~10-14 %, por debajo del umbral.
- **H4+H5.** En la base, el catálogo (vídeos de más de 30 días) aporta ~36 % de las vistas en M6 y ~48 % en M12 [S, `model/puertas_gtm.py`]. Esas vistas no las trae la siembra saliente, sino la navegación, las listas y los sugeridos: los umbrales (30 % y 45 %) quedan algo por debajo de esa proporción.
- **H2 y H3.** Con AVD de 30 min (carril base) y 1,5 vistas por espectador salen 0,75 h; es el suelo coherente con la AVD que ya exige la P1.
- **Advertencia:** con tan pocos espectadores, Studio puede ocultar algún dato ("no hay datos suficientes"). En ese caso se usan como sustitutos las respuestas al comentario fijado "ata onde chegaches", los seguidores en Spotify, Apple e iVoox y los suscriptores de la Carta, y se anota en el informe de la puerta [S]. **Todos estos umbrales se recalibran en la lectura de M4**, igual que los de adquisición.

**De dónde salen los umbrales de embudo R1-R3 (v5)** [F para el rango general de CTR; S para el resto, sin *benchmark* público de canales de sueño en galego]:
- **Rango de referencia del CTR.** Según YouTube, "Half of all channels and videos on YouTube have an impressions CTR that can range between 2% and 10%", y el CTR baja cuando un vídeo recibe muchas impresiones en inicio, porque llega a gente menos cercana [F https://support.google.com/youtube/answer/7628154?hl=en]. El 4-6 % es la mitad baja-media de ese rango: una miniatura de sueño es calmada a propósito y no debe competir en estridencia. **Por debajo del 3 %** el empaquetado está fallando; **por encima del 8 % con AVD < 20 min**, promete algo que el vídeo no da (guardarraíl).
- **R1 (impresiones) se deriva de las vistas de las puertas.** Vistas a 30 días × cuota de vistas que llegan desde superficies con impresión (navegación, sugeridos y búsqueda) ÷ CTR. En la P1: 60 vistas (umbral) × 50 % (el otro 50 % es siembra externa, notificaciones y directo en el arranque [S]) ÷ 4 % ≈ **750 → umbral 700**. En la rama base (86-91 vistas) salen ~980 y en la clónica (26), ~290, con el CTR del 4,5 %. En M4: 40 vistas (frontera entre el carril clónico y el base en la lectura de M4) × 45 % ÷ 4 % = **450**. En M9: 103 × 60 % ÷ 4,5 % ≈ 1.370 → **1.000** con margen. En la P2: 100 × 60 % ÷ 5 % = **1.200** (base: 115 × 65 % ÷ 4,5 % ≈ 1.660). Coherencia: los umbrales de impresiones separan las ramas como los de vistas, pero **se leen antes** (una semana después de publicar ya hay señal) y **dicen dónde está el fallo**: si no hay impresiones, YouTube no enseña el vídeo; si hay impresiones y no clics, el problema es la miniatura o el título.
- **R3 (sugeridos ajenos).** En la P1 el canal vive de la siembra; el 10 % es la señal mínima de que YouTube ya lo coloca junto a vídeos de otros. En la P2 se pide el 20 %: con H4+H5 ≥ 45 % y R3 ≥ 20 % quedan ~35 puntos para búsqueda y siembra externa, lo que baja la dependencia de siembra por debajo del 50 % que se vigila como alerta. **Suma de control:** H4 + H5 + R3 ≤ 100 % en todos los cortes (P1: 30 + 10; P2: 45 + 20).
- **Recalibración en M4:** igual que los de adquisición y hábito. El CTR objetivo pasa a ser la mediana propia de los vídeos 1-4 (acotada entre el 3 % y el 7 %), y R1 se recalcula con la cuota de superficies con impresión que se haya observado de verdad.
- **Advertencia:** con pocas impresiones Studio puede no mostrar el CTR filtrado por fuente [S, verificar en M2]. En ese caso se usa el CTR total del vídeo y se anota.

**Los dos desbloqueos reales a los que se anclan las puertas** (lo único que convierte audiencia en dinero de plataforma):

| Desbloqueo | Requisito | Fuente |
|---|---|---|
| **Fan funding** (membresías, Super Thanks) | **500 suscriptores + 3.000 h en 12 meses** + 3 subidas en 90 días | [F] https://support.google.com/youtube/answer/72902 |
| **YPP completo** (anuncios + Premium) | **1.000 suscriptores + 8.000 h *qualified* en 365 días** para solicitudes desde el 1-02-2027 | [F] 8.000 h: https://blog.youtube/news-and-events/youtube-partner-program-updates-2027-new-opportunities-earn/ · [F] 1.000 suscriptores: https://support.google.com/youtube/answer/72851 · [S] que los 1.000 suscriptores se mantengan en 2027 |

Ninguna puerta usa umbrales "redondos" que no desbloqueen nada. Cada umbral responde a una pregunta: **¿esta trayectoria llega a 500 + 3.000 h (y, después, a 1.000 + 8.000 h) dentro del horizonte de 36 meses?**

### 4.1 Experimentos

Métricas de YouTube Studio salvo que se indique otra cosa. Los umbrales de E3, E4 y E10 son **los mismos números de la tabla de puertas (§4.2)**, derivados de las ramas del modelo; el resto son [S] de diseño.

| # | Experimento | Hipótesis | Diseño | KPI y umbral de éxito | Cuándo | Coste |
|---|---|---|---|---|---|---|
| **E0** | Voz A/B ciega | Existe una voz en galego "dormible" y correcta | Kit ciego: el mismo texto trampa con 5-7 motores, normalizados en volumen, a 105, 115 y 125 palabras/min [R `voz_guion.md` §1.9] | La ganadora saca **≥ 4/5 en "durmiríame con isto"** y ninguna nota **≤ 2 en corrección galega**; aguanta 15 min continuos sin artefactos. **Dos clasificaciones:** (A) voces con consentimiento comercial documentado (Azure Sabela/Roi, Google gl-ES, voces por defecto de ElevenLabs) y (B) voces de Nós pendientes de consentimiento. **La mejor de A es siempre la voz de reserva.** Una voz de B solo se publica si tiene el doble permiso (§3.3 bis) **y** supera a la mejor de A en ≥ 0,5 puntos de "durmiríame"; si no los supera, se elige A directamente y no se corre el riesgo [S] | M1 | ~0 € (100 € si se firma con un locutor) |
| **E1** | Guion ciego | Un LLM frontier con el cinturón lingüístico alcanza el listón | 3 modelos escriben el mismo capítulo; se compara con la referencia [R `drafts/formato.md` §11] | Empata o gana en ≥ 2 de 4 criterios; **≤ 1 error normativo por 1.000 palabras** tras el control de calidad automático, contado por un nativo | M1 | < 20 € |
| **E2** | Panel privado previo al lanzamiento | La comunidad nativa acepta el producto | 10-15 oyentes nativos (edades y zonas variadas), 1 filólogo y 1 historiador escuchan el episodio 1 completo en casa, de noche. Cuestionario breve | **≥ 70 % "volvería a escoitalo"**; filólogo: **0 errores graves** (uno que se oiga y que avergüence); historiador: 0 errores de hecho sin corregir; ≤ 20 % molestos por la IA una vez leída la nota | M2 | 0-150 € (revisión) |
| **E3** | Retención, **hábito** y rama de audiencia | El formato retiene, **la gente vuelve** y la audiencia sigue la rama base o mejor | Episodios 1-12 (y, desde v4, seguimiento hasta la P2). **Lectura temprana en M4** con los vídeos 1-4 (primera recalibración de `drafts/retornos.md` §11), lectura en la Puerta 1, **control de hábito en M9** y lectura en la Puerta 2 | **Adquisición:** AVD ≥ 20 min; retención a 10 min ≥ 50 % [S]; **vistas a 30 días ≥ 60** de media (clónico 26 · base 86-91 · alta 294-318). Lectura en M4: < 40 = trayectoria de clónico; 50-150 = base; > 180 = alta. **Hábito (tabla del §4.0):** H1 recurrentes ≥ 15 % (M4) · **≥ 20 % (P1)** · ≥ 25 % (M9) · **≥ 30 % (P2)**; H2 horas por espectador ≥ 0,75 h (P1) y ≥ 1,0 h (P2); H3 vistas por espectador ≥ 1,3 y ≥ 1,5; **tráfico de hábito H4+H5 ≥ 30 % (P1) y ≥ 45 % (P2)**. **Embudo (v5, tabla del §4.0):** R1 impresiones por vídeo a 28 días ≥ 450 (M4) · **≥ 700 (P1)** · ≥ 1.000 (M9) · **≥ 1.200 (P2)**; R2 CTR en navegación y sugeridos 4-6 % (alerta < 3 %); R3 sugeridos ajenos **≥ 10 % (P1)** y **≥ 20 % (P2)**. **Qué decide:** la matriz del §4.2 bis (acelerar, GO, **cambiar el empaquetado**, cambiar el formato o parar) | M2-M12 | 0 € |
| **E4** | Conversión a suscriptor sin CTA hablada | Quitar la llamada a suscribirse no hunde la suscripción | En 3 episodios, una frase suave de despedida; en el resto, nada. **Cruce con el hábito:** si H1 cumple pero la conversión no, el problema es que quien vuelve no se suscribe → se adopta la frase suave aunque no gane por 0,5 puntos, y se refuerza la invitación a la Carta en el comentario fijado | **≥ 1,6 suscriptores por cada 100 vistas** en el conjunto. Es el punto medio entre el clónico (1,3 %) y la base (2,0 %) del modelo, y el mínimo con el que la base aún llega al fan funding en M28 (con 1,3 % llegaría en M31 y nunca al YPP en 36 m) [S, `puertas_gtm.py`]. Si la variante con frase suave supera a la silenciosa en ≥ 0,5 puntos, se adopta | M3-M6 | 0 € |
| **E5** | Calidad percibida pública | Los errores son raros y se corrigen | Registro de todos los comentarios que señalan errores: verificados o no, y tiempo de corrección | **≤ 1 error verificado por hora de audio** en la media móvil de 4 episodios; corrección en menos de 72 h en el 100 % | Continuo | 0 € |
| **E6** | SEO y metadatos | La línea bilingüe capta búsquedas sin coste de abandono | Lote A (descripción solo en galego) frente a lote B (con línea bilingüe), alternando episodios. En M7-M9, prueba de metadatos traducidos al castellano en 2 episodios | % de tráfico de búsqueda; términos de búsqueda; retención a 1 min por fuente. Éxito: el lote B sube la búsqueda ≥ 30 % sin bajar la retención a 1 min más de 5 puntos. **v5: la prueba de metadatos traducidos de M7-M9 pasa a 4 + 4 episodios, con la traducción que declara el idioma del audio ("narrado en gallego"), y se cruza con R2 y R3:** se adopta si el CTR en sugeridos sube ≥ 1 punto o R3 ≥ 5 puntos sin perder más de 5 puntos de retención al minuto 1 (§2.4 bis, punto 4) | M3-M9 | 0 € |
| **E7** | Geografía y "desbordamiento" | Hay audiencia fuera del público galegofalante (hipótesis VaniMani) | Informe de geografía, idioma de subtítulos y fuentes de tráfico | Solo medición: si **> 25 % de las horas** vienen de fuera de España, se abre la pregunta de pistas es/pt en la Etapa 2 | M3-M12 | 0 € |
| **E8** | Transparencia sobre la IA | Declarar la IA no provoca rechazo neto | Clasificación mensual de los comentarios que mencionan IA: positivo, neutro o negativo. Encuesta en la pestaña Comunidad cuando esté disponible | **Negativos ≤ 30 % de los que mencionan IA** y ninguna crítica pública de una entidad relevante sin respuesta en 48 h | M2-M12 | 0 € |
| **E9** | Mediadores | Las entidades y los divulgadores traen audiencia | Un enlace distinto (lista de reproducción propia o enlace acortado) por entidad o colaborador | **≥ 3 de cada 20 entidades contactadas responden**; ≥ 1 colaboración con un divulgador en M6; tráfico externo ≥ 10 % de las vistas en los meses de oleada | M4-M12 | 0 € |
| **E10** | Audio primero | En galego, el oyente de audio pesa tanto como el de YouTube | El mismo máster en Spotify, iVoox y Apple | Horas en plataformas de audio **≥ 25 % de las de YouTube** en M6 (supuesto A10 de la rama base; clónico 10 %, alta 40 %). Si superan el 100 %, se replantea el canal principal. Control de hábito en audio: seguidores en Spotify, Apple e iVoox | M2-M12 | 0 € |
| **E11** | Duración | 2 h retiene lo mismo o más horas por vista que 75 min | Etapa 2: alternar 75 min y 2 h en 4 + 4 episodios | Horas por vista; AVD; comentarios. Con AVD de 15 min la base nunca llega a las 8.000 h del YPP en 36 m [S, `puertas_gtm.py`]: por eso gana el formato que mantenga la AVD ≥ 30 min | M7-M10 | 0 € |
| **E12** | Patrocinio o canje | Hay una marca gallega dispuesta a asociarse | Oferta a 5-10 candidatos (balnearios, editoriales, textil del hogar) [R `ingresos_alt.md` §5] con mención solo al inicio y en tono calmado | **≥ 5 propuestas enviadas antes de M12** (condición de la Puerta 2, igual que en `drafts/retornos.md`). Cerrar un canje es un objetivo, **no** una condición: en el modelo el patrocinio solo empieza a pagar con ≥ 2.000 vistas/mes, que la base alcanza en M25 (con E2 continuada), no en M12 | M9-M12 | 0 € |
| **E13** | Ritual del serán | Un día y una hora fijos, la estrea con el promotor en el chat y el comentario fijado de la mañana aumentan la vuelta del oyente | M2-M6: ritual completo en todos los episodios (con 12 vídeos no cabe un A/B). M7-M10: **ABAB** de estrea frente a publicación directa (4 + 4 episodios), el resto del ritual fijo. Día y hora revisados en M4 con el informe de horas de Studio | Vistas de los primeros 7 días desde "Notificaciones" y "Funciones de navegación"; H1 de los espectadores de cada episodio; participantes en el chat; respuestas a "ata onde chegaches". **Se mantiene la estrea** si sube las vistas de la primera semana ≥ 10 % o H1 ≥ 3 puntos; si no, se deja (ahorra 15 min por episodio) | M2-M10 | 0 € |
| **E14** | Bucle con el oyente y presencia galegofalante | La comunidad propia trae oyentes que vuelven, no solo visitas | Metas del §2.8.3-2.8.4, con un enlace corto por espacio y la fuente "Externo" desglosada por sitio | **M6 / M12:** propuestas de temas ≥ 3 / ≥ 10 al mes; votos en la encuesta trimestral ≥ 30 / ≥ 100; Carta ≥ 40 / ≥ 150 suscriptores con apertura ≥ 45 %; comentarios en galego ≥ 60 %; respuesta en ≤ 48 h en ≥ 90 % de los comentarios; tráfico de los espacios propios ≥ 5 % / ≥ 8 % de las vistas. Cada red tiene su regla de abandono (§2.8.4) | M2-M12 | 0 € (Carta gratis hasta 250 suscriptores) |
| **E15** | **Empaquetado y adyacencia (v5)** | Con temas espejo de los vídeos semilla y títulos y miniaturas en su misma gramática, YouTube coloca a Serán junto a ellos, y el empaquetado se puede mejorar sin tocar el formato | (a) **Espejo:** 1 de cada 3 episodios en la Etapa 1 (1 de cada 4 en la Etapa 2) es espejo de un semilla (§2.4 bis); se comparan R1 y R3 de los episodios espejo frente a los demás. (b) **Test & Compare:** 3 miniaturas por episodio espejo desde que haya funciones avanzadas (M1-M2); en los vídeos con estrea, solo si YouTube lo permite al acabar (se comprueba con el episodio 1). (c) **Idioma de los metadatos:** el E6 ampliado. (d) **Semillas:** revisión mensual de la tarjeta de sugeridos | **Espejo:** R1 de los episodios espejo ≥ 1,5 veces el de los demás **o** R3 ≥ 5 puntos más; si no lo consigue en 4 espejos, se baja a 1 de cada 6 y se da más peso a las votaciones. **CTR (R2):** 4-6 %, alerta < 3 %. **R3:** ≥ 10 % (P1), ≥ 20 % (P2). **Semillas activas (R3b):** ≥ 1 (P1), ≥ 3 (P2). **Test & Compare:** plantilla de miniatura fijada tras 6 pruebas | M1-M12 | 0 € |

**Publicidad pagada (opcional, no es un experimento base):** solo si la Puerta 1 da GO, un test de 30-50 € con anuncios de YouTube, segmentado por Galicia e idioma galego y dirigido al mejor episodio. Mide el coste por suscriptor y la retención del tráfico pagado. Si el coste es **> 1 € por suscriptor**, no se repite [S].

### 4.2 Puertas go/no-go: tabla única del plan

Esta tabla **es la misma** que la de `drafts/retornos.md` §1 (umbrales de P1, P2 y P3 idénticos), ampliada con la Puerta 0, la Puerta roja, las horas de visionado, el número de vídeos y el desbloqueo al que apunta cada umbral. Si una de las dos piezas cambia un umbral, se cambia en las dos.

**Valores de cada rama en la fecha de la puerta** [S, salida de `model/puertas_gtm.py` con el calendario del §4.0; E2 continuada para proyectar los desbloqueos]: Las filas de embudo (v5) **no salen del modelo**, que no tiene impresiones ni fuentes de tráfico: son las vistas de cada rama pasadas por la fórmula del §4.0 (cuota de superficies con impresión del 50 % en la P1 y del 65 % en la P2, CTR del 4,5 %) [S]. La cuota de sugeridos ajenos no tiene valor por rama: es una hipótesis que se mide.

| Puerta · fecha · vídeos | Métrica | Umbral GO | Clónico (baja) | Estancada | **Base** | Alta |
|---|---|---|---|---|---|---|
| **P1 · 31-03-2027 (M6) · 12 vídeos** | Vistas a 30 días | **≥ 60** | 26 ✗ | 86-91 | **86-91** | 294-318 |
| | Suscriptores | **≥ 20** | 5 ✗ | 23 | **24** | 99 |
| | Horas 12 m (control, no condición) | — | 120 | 583 | **612** | 2.632 |
| | AVD | **≥ 20 min** | 20 | 30 | **30** | 40 |
| | Embudo (diagnóstico, v5): impresiones por vídeo a 28 días · sugeridos ajenos | ≥ 700 · ≥ 10 % | ~290 · — | ~980 · — | **~980** · — | ~3.400 · — |
| | Resultado | | **PARA** | pasa (en M6 no se distingue de la base) | **pasa** | pasa |
| **P2 · 30-09-2027 (M12) · 36 vídeos** | Vistas a 30 días | **≥ 100** | — | 91 ✗ | **115** | 459 |
| | Suscriptores | **≥ 100** | — | 87 ✗ | **107** | 475 |
| | Horas 12 m (control) | — | — | 2.182 | **2.681** | 12.662 |
| | Embudo (diagnóstico, v5): impresiones por vídeo a 28 días · sugeridos ajenos | ≥ 1.200 · ≥ 20 % | — | ~1.310 · — | **~1.660** · — | ~6.630 · — |
| | Resultado | + ≥ 1 solicitud de ayuda o premio presentada y ≥ 5 propuestas de patrocinio enviadas | | **PARA** | **pasa** | pasa |
| **P3 · 31-03-2028 (M18) · 60 vídeos** | En el YPP (1.000 suscr. + 8.000 h) **o** ≥ 50 €/mes recurrentes (media de 3 meses) **o** ayuda o encargo concedido | | — | — | 252 suscr. · 5.687 h · 0 € → **mantenimiento** | 1.177 suscr. · 28.756 h, YPP en M17 → **pasa** |

**A qué desbloqueo real apunta cada puerta** (fechas proyectadas si se continúa en la Etapa 2):

| Rama | Fan funding (500 + 3.000 h) | YPP (1.000 + 8.000 h) | Qué separa la puerta |
|---|---|---|---|
| Clónico | **Nunca** (119 suscriptores en M36) | Nunca | **La P1 la corta:** con esta trayectoria ningún desbloqueo llega en 36 meses |
| Estancada | M34 | Nunca | **La P2 la corta:** el fan funding llega demasiado tarde para pagar 22 meses más de Etapa 2 (~2.400 € de caja) |
| **Base** | **M25** (M28 si baja a mantenimiento) | **M35** (nunca en 36 m si baja a mantenimiento) | Pasa P1 y P2 porque llega al fan funding dentro del horizonte; **no pasa la P3** porque el YPP llega demasiado tarde → mantenimiento, que conserva el catálogo y las ayudas |
| Alta | **M13** | **M17** | Pasa las tres; la P3 abre la opción de la Etapa 3 |

**Lectura de los umbrales.**
- **P1 (≥ 60 vistas, ≥ 20 suscriptores):** separa el clónico de la base con margen amplio en vistas (26 frente a 86) y estrecho en suscriptores (5 frente a 24). Los 20 suscriptores no son un número redondo: son los que da el tráfico de la base con una conversión del **1,6 %** (el umbral de E4), el mínimo con el que la base aún alcanza el fan funding en M28.
- **P2 (≥ 100 vistas, ≥ 100 suscriptores):** separa la base de la estancada, que en M6 eran idénticas. Márgenes estrechos (107 frente a 87 suscriptores; 115 frente a 91 vistas): por eso se exigen **las dos** condiciones de audiencia y, además, dos condiciones de esfuerzo comercial que no dependen del azar.
- **Horas de visionado:** en las P1 y P2 se miden como control, **no** como condición. En la base, el cuello de botella son los suscriptores, no las horas: con E2 continuada, las 3.000 h llegan en M13 y las 8.000 h en M23, pero los 500 suscriptores en M25 y los 1.000 en M35. Exigir 8.000 h en M12 (versión 1 de esta pieza) habría cortado también la base, que tiene 2.681 h.
- **Señal de rama alta** (lectura complementaria, no una puerta): si en la P1 hay **≥ 200 vistas a 30 días y ≥ 70 suscriptores**, o en la P2 **≥ 400 suscriptores y ≥ 8.000 h en 12 meses**, la trayectoria es la alta (fan funding en M13, YPP en M17). Entonces se adelantan la preparación de membresías, el dossier para patrocinio y la solicitud a la CRTVG.
- **Los márgenes de P1 y P2 son estrechos a propósito.** Se recalibran con los datos de los vídeos 1-4 (lectura de E3 en M4): si las vistas a 30 días de los primeros vídeos son de ~40 en lugar de ~75, se recalculan todas las ramas con ese punto de partida y se mantiene la regla: **se sigue solo si la trayectoria llega al fan funding antes de M30**.

**Tabla completa de puertas** (qué se hace en cada caso):

| Puerta | Cuándo · vídeos | GO si se cumple **todo** | NO-GO → qué se hace |
|---|---|---|---|
| **0. Publicable** | ~15-11-2026 (M2) · 3 episodios terminados, 0 publicados | E0 y E1 superados; **E2 superado**; **consentimiento del locutor verificado** (voz de Nós: USC/Gradiant + consentimiento firmado de la persona antes del 6-11; voz de proveedor: términos archivados); carta a ADA/AGPTI enviada; lista de cumplimiento completa (§3.7) | Si falla **solo** el consentimiento: **no es un NO-GO**, se publica con la voz de reserva (mejor de la clasificación A del E0), siempre que también cumpla el umbral del E0. Si ninguna voz con permiso cumple el E0: máximo 2 iteraciones de voz o guion (≤ 4 semanas). Si sigue sin pasar: **parar**, con un coste hundido de < 100 € [S]. Se revisa cada 6 meses si hay una voz mejor. En el modelo es parte del 15 % de riesgo lingüístico o comunitario, que para en la P1 |
| **1. Señal de mercado** | 31-03-2027 (M6) · 12 vídeos | **Vistas a 30 días ≥ 60**; **≥ 20 suscriptores**; **AVD ≥ 20 min**; E5 cumplido (sin quejas graves de lengua); A/B ciego del promotor y su mujer sin veredicto en contra. **El hábito (H1 ≥ 20 %, H4+H5 ≥ 30 %) decide el tipo de GO:** acelerar, GO normal o GO condicionado con cambio de formato y control en M9 (§4.2 bis). **El embudo (R1 ≥ 700 impresiones, R2 ≥ 4 %, R3 ≥ 10 %) no decide el GO: dice qué se cambia primero** (empaquetado antes que formato, §4.2 bis) | **Parar**, como en el modelo (camino P1: −210 € y ~100 h). El catálogo queda publicado y se sigue midiendo la cola larga a coste 0. **No hay prórroga de 3 meses** (la versión 1 la tenía): cada mes extra en la rama clónica cuesta sin acercar ningún desbloqueo, y el valor esperado del plan depende de parar aquí |
| **2. Proyecto lateral viable** | 30-09-2027 (M12) · 36 vídeos | **Vistas a 30 días ≥ 100**; **≥ 100 suscriptores**; **≥ 1 solicitud de ayuda o premio presentada** (CRTVG ~junio de 2027 o Youtubeiras+ 2027); **≥ 5 propuestas de patrocinio enviadas** (E12). **El hábito (H1 ≥ 30 %, H4+H5 ≥ 45 %) decide el tipo de GO** (§4.2 bis); **el embudo (R1 ≥ 1.200, R2 ≥ 4 %, R3 ≥ 20 %) decide qué se cambia primero** | **Parar** la producción (camino P2: −870 € acumulados). Se conserva el catálogo y la opción de ayudas ya solicitadas. **No se abre la Etapa 3** |
| **3. Etapa 3** | 31-03-2028 (M18) · 60 vídeos | En el YPP **o** ≥ 50 €/mes recurrentes (media de 3 meses) **o** ayuda o encargo concedido | **Mantenimiento** (1 vídeo al mes, ~20 €/mes, ~8 h/mes): conserva el catálogo y la elegibilidad para CRTVG, B2B y Youtubeiras+ ([R `drafts/retornos.md` §6]) |
| **Puerta roja** (en cualquier momento) | Se activa por un solo hecho | — | **Cualquiera de estos hechos congela la publicación durante 2 semanas y obliga a revisar:** (1) crítica pública de una entidad relevante (RAG, CCG, A Mesa, asociaciones de dobladores o un medio en galego) por un error o por la IA; (2) un error de hecho grave publicado y señalado por un historiador; (2 bis) **oposición pública del locutor, de ADA o de AGPTI al uso de la voz**, o retirada del consentimiento (en este caso, además, sustitución de la voz en ≤ 30 días); (3) aviso de monetización limitada o de "inauthentic content"; (4) E8 con > 50 % de negativos en un mes. Respuesta: corregir, publicar la errata, responder con transparencia y, si hace falta, retirar el episodio. Si la causa es de fondo (la voz o el guion no aguantan), se trata como un NO-GO de la puerta siguiente |

### 4.2 bis Hábito en las puertas: matriz de decisión (nuevo en v4)

**Qué cambia y qué no.** Los umbrales de **adquisición** de P1 y P2 (vistas a 30 días, suscriptores, AVD) **no cambian** y siguen siendo idénticos a los de `drafts/retornos.md` §1: deciden si hay GO o NO-GO. Los KPIs de **hábito** (tabla del §4.0) deciden **qué tipo de GO** y añaden **una parada anticipada** en M9, que solo ahorra dinero en trayectorias que la P2 cortaría igualmente. La única modificación del árbol de `retornos.md` es ese control de M9, y hay que reflejarla allí (§5).

**Criterio de "hábito cumple" en cada lectura:** H1 **y** (H4+H5) en su umbral; H2 y H3 son de apoyo: si una de las dos principales falla por ≤ 3 puntos y H2 y H3 cumplen, cuenta como cumplido [S].

**Regla previa, en todas las lecturas (v5): empaquetado antes que formato.** Antes de aplicar cualquiera de las matrices de abajo se mira el embudo (R1-R3, tabla del §4.0). Cambiar la miniatura y el título cuesta minutos y se puede deshacer; cambiar el formato cuesta episodios. Por eso:

| Diagnóstico del embudo | Qué significa | Qué se cambia primero | Cómo y cuánto |
|---|---|---|---|
| **R1 por debajo del umbral y R2 < 3 %** | YouTube enseña poco el vídeo y, cuando lo enseña, no se pincha | **Empaquetado** (miniatura y título) | Test & Compare en los siguientes 4 episodios (o, si no está disponible, variante nueva en 4 episodios comparables) y **cambio retroactivo de miniatura en los 3 vídeos del catálogo con más impresiones**. Se vuelve a leer a los 28 días |
| **R1 bien y R2 < 3 %** | Hay escaparate, pero la miniatura o el título no convencen | **Empaquetado** | Ídem |
| **R1 por debajo del umbral y R2 ≥ 4 %** | Lo que se enseña funciona, pero se enseña poco: el problema es de **tema y de adyacencia**, no de miniatura | **Temas y títulos espejo** (§2.4 bis): subir a 1 de cada 2 episodios espejo durante 4 episodios y revisar la lista de semillas | Se vuelve a leer a los 28 días |
| **R1 y R2 bien, R3 bajo** | Se gana en inicio y búsqueda, no junto a otros vídeos | Adyacencia (espejo de semillas) y metadatos traducidos (E6) | Sin tocar el formato |
| **R2 > 8 % con AVD < 20 min** (guardarraíl) | La miniatura promete otra cosa | Empaquetado **más fiel** al contenido, aunque baje el CTR | Inmediato |
| **Embudo en umbral y hábito o AVD bajos** | La gente llega y no se queda o no vuelve: **ahora sí es el formato** | Menú de cambio de formato (abajo) | Según las matrices |

**Consecuencia en las matrices:** donde abajo dice "CAMBIAR EL FORMATO", **si el embudo también está por debajo del umbral, se cambia antes el empaquetado** (4 episodios) y el formato solo se toca si, con el embudo ya en su umbral, el hábito sigue bajo. Si el calendario no deja hueco para las dos cosas antes de una puerta (por ejemplo, en la P1 con 12 vídeos), se hacen en paralelo: empaquetado nuevo **y** el cambio de formato de menor coste (serializar), para no llegar a la puerta sin dato. El empaquetado nunca rompe la guía de tono: nada de sobresaltos ni de clickbait para subir el CTR. Un CTR bajo con una miniatura fiel y calmada se acepta si el hábito cumple [S].

**Matriz en M4 (lectura temprana, vídeos 1-4)**

| | Hábito alto (H1 ≥ 35 %, H2 ≥ 1,5 h) | Hábito cumple (H1 ≥ 15 %, H4+H5 ≥ 20 %) | Hábito bajo (H1 < 10 % o H4+H5 < 15 %) |
|---|---|---|---|
| **Vistas a 30 días ≥ carril base (~75)** | **ACELERAR:** pasar a semanal en M5-M6 (hasta 16 vídeos en la P1, con los mismos umbrales), **solo si** las horas del promotor por episodio son ≤ 4 h; si no, acelerar la Carta a quincenal y adelantar el primer tema votado | Seguir el plan | **CAMBIAR EL FORMATO ya** (menú de abajo) en los episodios 8-12, para llegar a la P1 con un dato de hábito corregido |
| **Vistas a 30 días entre 40 y 75** | Seguir el plan; la difusión saliente es la que falla (reforzar la fase pública del §2.3) | Seguir el plan | Cambiar el formato en los episodios 8-12 |
| **Vistas < 40 (carril clónico)** | Seguir hasta la P1 (no hay parada en M4) | Seguir hasta la P1 | Seguir hasta la P1 y preparar el informe de cierre |

**Matriz en la Puerta 1 (M6, 12 vídeos)**

| | Hábito alto (H1 ≥ 35 %, H4+H5 ≥ 45 %, H2 ≥ 1,5 h) | Hábito cumple (H1 ≥ 20 %, H4+H5 ≥ 30 %) | Hábito bajo |
|---|---|---|---|
| **Adquisición cumple** (≥ 60 vistas, ≥ 20 suscr., AVD ≥ 20 min) | **GO + ACELERAR:** Etapa 2 con el techo de presupuesto (revisión científica en cada episodio en vez de 1 de cada 4, dentro de 50-200 €/mes), Carta quincenal desde M7 y **preparación de membresías y del dossier de patrocinio adelantada a M9**. La cadencia no pasa de semanal (límite de contenido inauténtico, §3.1) | **GO** normal a la Etapa 2 | **GO CONDICIONADO + CAMBIO DE FORMATO:** los 8 primeros episodios de la Etapa 2 (M7-M8) prueban el menú de cambios. **Control de hábito en M9** (abajo) |
| **Adquisición no cumple** | **PARAR**, como en el modelo. Se documenta que el hábito era alto; la Carta, el Telegram y el catálogo siguen a coste 0 € y se vuelve a leer la cola larga en M12 **sin reabrir producción** (no hay prórroga, igual que en la v2) | **PARAR** | **PARAR** |

**Control de hábito en M9 (solo si la P1 dio GO condicionado):** si **H1 < 25 % y H4+H5 < 35 %**, **y además** las vistas a 30 días están por debajo del carril base de M9 (103), se **para en M9** en lugar de en M12. Es la firma de la rama estancada: en M6 no se distinguía de la base y en el modelo no llega al fan funding hasta M34. Ahorro frente a esperar a la P2: **~330 € de caja (3 × 110 €) y ~105 h (3 × 35 h)** [S, cifras de caja y horas de la Etapa 2 de `drafts/retornos.md`]. Si solo falla el hábito o solo fallan las vistas, se sigue hasta la P2. **El embudo no da prórroga en M9:** como la regla de empaquetado se aplica cada mes, en M9 ya se habrán probado al menos dos rondas de miniatura y título; si aun así se cumplen las tres condiciones, se para.

**Matriz en la Puerta 2 (M12, 36 vídeos)**

| | Hábito alto (H1 ≥ 40 %, H4+H5 ≥ 60 %, H2 ≥ 2,0 h) | Hábito cumple (H1 ≥ 30 %, H4+H5 ≥ 45 %) | Hábito bajo |
|---|---|---|---|
| **Adquisición y esfuerzo comercial cumplen** (≥ 100 vistas, ≥ 100 suscr., ≥ 1 solicitud, ≥ 5 propuestas) | **GO + ACELERAR hacia la Etapa 3:** se activa la "señal de rama alta" del §4.2 (membresías, dossier, CRTVG) y se estudia la voz licenciada | **GO** hasta la P3 | **GO CONDICIONADO:** segunda ronda del menú de cambios en M13-M14 y control en M15 con los umbrales de la P2; si no se cumplen, **mantenimiento** anticipado (1 vídeo al mes) |
| **Adquisición no cumple** | **PARAR** la producción, como en el modelo; la Carta y el Telegram se mantienen si cuestan < 1 h/mes | **PARAR** | **PARAR** |

**Menú de cambio de formato** (ordenado de menor a mayor coste; cada cambio se prueba en 4 episodios y se mide con H1 y H4+H5) [S]:
0. **Empaquetado (v5, va siempre primero si R1 o R2 fallan):** miniatura y título nuevos con Test & Compare, cambio retroactivo en los 3 vídeos del catálogo con más impresiones y más episodios espejo (§2.4 bis). Se mide con R1, R2 y R3.
1. **Serializar:** series con arco y orden ("Os Irmandiños, 1 de 4"), una línea de recuerdo del episodio anterior en la entrada suave, y lista de reproducción de la serie en orden y con reproducción continua.
2. **Listas "Serán longo":** listas de 4-6 horas que encadenan episodios de una serie; y, como máximo 1 al mes, una recopilación de 3 h con montaje nuevo (§3.1).
3. **Duración:** adelantar el E11 (75 min frente a 2 h).
4. **Voz y ritmo:** volver al kit del E0 con la velocidad inmediatamente inferior (105 palabras/min).
5. **Día y hora:** mover la estrea según el informe de horas de Studio.

**Tabla de decisiones de un vistazo**

| Qué dice el hábito | Decisión | Cuándo |
|---|---|---|
| Alto con adquisición en el carril base o mejor | **Acelerar** (cadencia en la Etapa 1 si las horas lo permiten; presupuesto, Carta y monetización en la Etapa 2) | M4, P1, P2 |
| Embudo por debajo del umbral (R1 o R2), con cualquier hábito | **Cambiar el empaquetado primero** (miniatura, título, temas espejo) y volver a medir en 28 días | Mensual, M4, P1, M9, P2 |
| Bajo con adquisición correcta **y embudo en su umbral** | **Cambiar el formato** (menú) y volver a medir | M4, P1, P2 |
| Bajo con adquisición por debajo del carril base en M9 | **Parar antes** | M9 |
| Cualquiera con adquisición por debajo del umbral de la puerta | **Parar** (regla de `retornos.md`, sin cambios) | P1, P2 |

### 4.3 Cuadro de mando mensual: carriles por rama

Cada mes se compara el dato real con los **carriles** del modelo. La pregunta no es "¿llegamos a X?", sino "¿a qué rama nos parecemos?".

**Carriles de audiencia** [S, `model/puertas_gtm.py`, calendario del §4.0]:

| Mes · vídeos | Métrica | Clónico | Base | Alta |
|---|---|---|---|---|
| **M4 (ene-27) · 7** | Vistas a 30 días (vídeos 1-4) | ~25 | ~75-80 | ~225-250 |
| | Suscriptores | 3 | 12 | 48 |
| | Horas 12 m | 65 | 309 | 1.277 |
| | Impresiones por vídeo a 28 días (v5, [S] derivado) | ~250 | ~750 | ~2.300 |
| **M6 (mar-27) · 12 · P1** | Vistas a 30 días | 26 | 86-91 | 294-318 |
| | Suscriptores | 5 | 24 | 99 |
| | Horas 12 m | 120 | 612 | 2.632 |
| | Impresiones por vídeo a 28 días (v5) | ~290 | ~980 | ~3.400 |
| **M9 (jun-27) · 24** | Vistas a 30 días | 27 | 103 | 388 |
| | Suscriptores | (parado) | 59 | 252 |
| | Horas 12 m | | 1.478 | 6.729 |
| | Impresiones por vídeo a 28 días (v5) | | ~1.370 | ~5.200 |
| **M12 (sep-27) · 36 · P2** | Vistas a 30 días | | 115 | 459 |
| | Suscriptores | | 107 | 475 |
| | Horas 12 m | | 2.681 | 12.662 (≥ 8.000 ✓) |
| | Impresiones por vídeo a 28 días (v5) | | ~1.660 | ~6.630 |
| **Desbloqueos** | Fan funding (500 + 3.000 h) | nunca | M25 | M13 |
| | YPP (1.000 + 8.000 h) | nunca | M35 | M17 |

**KPIs mensuales** (los umbrales coinciden con los de las puertas y los experimentos):

| KPI | Definición | Fuente | Referencia |
|---|---|---|---|
| Vistas por vídeo a 30 días | Media de los vídeos que cumplen 30 días en el mes | Studio | Carril base de la tabla anterior; **≥ 60 en la P1 y ≥ 100 en la P2** |
| Suscriptores (total) | Total del canal | Studio | Carril base; **≥ 20 en la P1, ≥ 100 en la P2**. Hitos de desbloqueo: 500 (fan funding) y 1.000 (YPP) |
| Suscriptores por 100 vistas | Conversión | Studio | **≥ 1,6** (E4); base del modelo: 2,0 |
| AVD | Duración media de visionado | Studio | **≥ 20 min**; carril base 30 min, alto 40 min [R `retornos.md` §1] |
| Retención a 10 min | % de audiencia en el minuto 10 | Studio | ≥ 50 % [S] |
| **H1 · % espectadores recurrentes** | Recurrentes / (nuevos + recurrentes), 28 días | Studio | **≥ 20 % (P1) · ≥ 25 % (M9) · ≥ 30 % (P2)**; alerta si cae 2 meses seguidos |
| H1b · Espectadores habituales | "Regular viewers" | Studio | Desde M8; ≥ 25 en la P2 (control) |
| **H2 · Horas por espectador** | Tiempo de visualización / espectadores únicos | Studio | ≥ 0,75 h (P1) · ≥ 1,0 h (P2) |
| H3 · Vistas por espectador | Vistas / espectadores únicos | Studio | ≥ 1,3 (P1) · ≥ 1,5 (P2) |
| **H4+H5 · Tráfico de hábito** | Listas + sugeridos del propio canal + navegación (+ notificaciones) | Studio, fuentes de tráfico | **≥ 30 % (P1) · ≥ 45 % (P2)** |
| Dependencia de siembra | Externo + directo o desconocido | Studio | Alerta si > 50 % en la P2 |
| **R1 · Impresiones por vídeo a 28 días (v5)** | Impresiones de miniatura registradas (búsqueda, inicio, feeds, "A continuación") | Studio, pestaña Alcance | **≥ 450 (M4) · ≥ 700 (P1) · ≥ 1.000 (M9) · ≥ 1.200 (P2)**; carril base en la tabla anterior |
| **R2 · CTR de impresiones en navegación y sugeridos (v5)** | Clics / impresiones, filtrado por fuente | Studio, modo avanzado | **Objetivo 4-6 %; alerta < 3 %**; recalibrado en M4 con la mediana de los vídeos 1-4; guardarraíl: > 8 % con AVD < 20 min |
| **R3 · Cuota de sugeridos desde canales ajenos (v5)** | Vistas desde "Vídeos sugeridos" con vídeo de origen de otro canal / vistas totales | Studio, tarjeta "Fuente de tráfico: vídeos sugeridos" | **≥ 5 % (M4, control) · ≥ 10 % (P1) · ≥ 15 % (M9) · ≥ 20 % (P2)** |
| R3b · Semillas activas (v5) | Vídeos de la lista de semillas entre las 10 primeras fuentes de sugeridos ajenos | Studio + lista del §2.4 bis | ≥ 1 (P1) · ≥ 3 (P2) (control) |
| Test & Compare (v5) | Pruebas hechas y variante ganadora | Studio | ≥ 1 prueba al mes desde que haya funciones avanzadas; plantilla fijada tras 6 |
| Comunidad propia | Suscriptores de la Carta y apertura; propuestas de temas; % de comentarios en galego; tráfico de los espacios propios | Proveedor de correo, registro propio, Studio | E14: 40 / 150 suscriptores; apertura ≥ 45 %; ≥ 3 / ≥ 10 propuestas al mes; galego ≥ 60 %; tráfico propio ≥ 5 % / ≥ 8 % |
| Horas de comunidad del promotor | Registro de tiempo | Propio | ≈ 1 h/semana (Etapa 1), ≈ 2 h/semana (Etapa 2); mínimo innegociable 35 min |
| Horas en 365 días | Horas *qualified* | Studio | Carril base: 612 (M6) → 2.681 (M12) → 3.000 en M13 (umbral de horas del fan funding) → 8.000 en M23 con E2 continuada o M32 en mantenimiento. El umbral de 8.000 h en M12 solo lo cumple la rama alta |
| Horas en audio | Spotify, iVoox y Apple | Paneles de cada plataforma | ≥ 25 % de las de YouTube (E10) |
| Errores verificados por hora de audio | E5 | Registro propio | ≤ 1 |
| % de comentarios negativos sobre la IA | E8 | Registro propio | ≤ 30 % |
| % de tráfico externo y de búsqueda | Fuentes de tráfico | Studio | Externo ≥ 10 % en meses de oleada |
| % de horas fuera de España | E7 | Studio | Medición (umbral de decisión: 25 %) |
| Horas del promotor por episodio | Registro de tiempo | Propio | ≤ 6,5 h [R `drafts/pipeline.md`] |
| Caja mensual | Gasto | Propio | ≤ 50 € (Etapa 1); modelo 35 €. Etapa 2: modelo 110 € |

**Regla de lectura:** dos meses seguidos por debajo del carril base en vistas a 30 días **y** en suscriptores adelantan la revisión: se aplica la puerta siguiente con los datos de ese momento, sin esperar a la fecha. **Regla de embudo (v5):** un mes con R1 o R2 por debajo del umbral de la siguiente lectura activa el cambio de empaquetado (§4.2 bis, regla previa) sin esperar a la puerta; es barato y reversible, así que no se esperan dos meses. **Regla de hábito:** dos meses seguidos con H1 y H4+H5 por debajo del umbral de la siguiente lectura activan el menú de cambio de formato (§4.2 bis) sin esperar a la puerta.

### 4.4 Calendario de 12 meses (octubre de 2026 - septiembre de 2027)

| Mes | Producción (vídeos publicados en el mes · acumulado) | Pruebas y puertas | Go-to-market y fechas ancla | Cumplimiento y financiación |
|---|---|---|---|---|
| **M1 · oct-2026** | 0 · 0. Construcción del pipeline; guías de estilo; guiones de los episodios 1-3 | **E0** (voz), **E1** (guion) | Registrar @seran y seran.gal; alta en Spotify for Creators (**SPP en España desde el 20-10**); revisión manual de búsquedas en galego (laguna de SEO). **Comunidad:** cuentas en Bluesky (@seran.gal) y mastodon.gal (alta con aprobación), canal de Telegram, handle en X; Carta en Buttondown; "Normas do serán" y formulario "Propón un serán" en la web; mirar a mano el tamaño y las normas de r/galicia y r/Galiza. **Embudo (v5):** activar las funciones avanzadas del canal (verificación de identidad) para tener Test & Compare; guardar las URL de la lista de semillas S1-S9 y primera búsqueda de semillas con la interfaz en castellano y en galego (§2.4 bis) | **Semana 1:** correo a Proxecto Nós/Gradiant (y CRPIH/UVigo) pidiendo el doble permiso y el contacto con cada locutor. **Semanas 2-4:** consentimiento de los locutores cuya voz siga en carrera; **carta y llamada a ADA y AGPTI** (§2.6 bis). Decidir el generador de imágenes; búsqueda en OEPM y EUIPO; ¿"O teu Xacobeo" (plazo del 1 al 31-10)? Solo si ya hay alta de autónomo: **no recomendado** en la Etapa 1 [R `ingresos_alt.md` §1.5] |
| **M2 · nov-2026** | **3 · 3.** Episodios 1-3 terminados y **publicados juntos el domingo 22-11** | **6-11: fecha límite del consentimiento del locutor** (si no hay, voz de reserva) → **E2** (panel) → **Puerta 0** (~15-11) | Fase suave: panel, 2-3 entidades y 1-2 servicios de normalización. **Ritual desde el episodio 1:** estrea el domingo a las 21:30 con el promotor en el chat; comentario fijado "ata onde chegaches"; Carta n.º 1 (panelistas que lo pidan); aviso en Telegram. **Episodio espejo de S6-S7 (Reino suevo) en el lanzamiento**; comprobar con el episodio 1 si Test & Compare admite un vídeo tras la estrea | Youtubeiras+ 2026 (15-11): **no presentarse** (opción b, §2.3), salvo que la Puerta 0 se pase antes del 10-11 |
| **M3 · dic-2026** | 2 · 5 (episodios 4-5) | E3, E4, E5, E8 en marcha; E6 lote A/B | Nadal: episodio "de inverno" **espejo de S1: "Galicia e a Santa Compaña: lendas para durmir"** [S]. **Alta en Podgalego y Obradoiro Dixital Galego** (ya hay ≥ 1 publicación al mes); presentación en su Discord; primeros reenvíos de los agregadores de Bluesky | Web: "Como facemos Serán" y erratas |
| **M4 · ene-2027** | 2 · 7 (episodios 6-7) | **Lectura temprana de E3** (vistas a 30 días de los vídeos 1-4 frente a los carriles) y recalibración de umbrales | 1.ª oleada de correos a la diáspora (20-30 entidades del resto de España y de Europa); contacto con 3 divulgadores. **Lectura temprana de hábito (H1-H5) y de embudo (R1-R3): recalibración del CTR objetivo con la mediana de los vídeos 1-4; regla de empaquetado antes que formato y matriz de M4**; revisión del día y la hora de la estrea; **primera votación trimestral** (tema del especial de marzo: "o serán que pediches") | — |
| **M5 · feb-2027** | 2 · 9 (episodios 8-9) | E9 | **Fase pública:** nota de prensa y propuesta a Radio Galega. 24-02: nacimiento de Rosalía de Castro (gancho opcional). **Episodio espejo de S2 (Lugo romana)**. **Primera publicación en Reddit** (qué es Serán y cómo se hace); **primer intercambio** con un pódcast de historia de Podgalego | Nueva regla del YPP de 8.000 h desde el 1-02 (ya en el modelo) |
| **M6 · mar-2027** | **3 · 12** (episodios 10-12; el 12 es el especial del Día Mundial do Sono) | **Puerta 1** (31-03) | Día Mundial del Sueño (**19-03-2027**, viernes anterior al equinoccio [S, calculado; confirmar en worldsleepday.org]): episodio especial **elegido por votación y con dedicatoria** y nota a la prensa. **Matriz de hábito de la P1, con la regla previa de embudo (R1 ≥ 700, R2 ≥ 4 %, R3 ≥ 10 %)** | ~Abril: ayudas de innovación ICC del Ministerio [R `ingresos_alt.md` §1.7]; solo si hay alta en RETA |
| **M7 · abr-2027** | Si hay GO: **Etapa 2**, 4 · 16, formato de 2 h | E11 (duración); E6 metadatos traducidos (2 episodios) | 2.ª oleada de correos a la diáspora (América). Carta quincenal; primer tema votado de la Etapa 2 (1 de cada 4 episodios); si la P1 dio GO condicionado, empieza el menú de cambio de formato (con el empaquetado primero si el embudo falla); E13 ABAB de estrea; **E6 ampliado: metadatos traducidos "narrado en gallego" en 4 + 4 episodios (M7-M9), cruzados con R2 y R3**; episodio espejo de S8 ("Un día nunha aldea galega da Idade Media") | — |
| **M8 · may-2027** | 4 · 20 | — | **Letras Galegas (17-05), Neira Vilas:** episodio "a aldea dos anos corenta e a emigración" una semana antes; oleada a Argentina y Cuba; oferta de capítulos a docentes. **Serán das Letras:** Carta especial, segunda publicación en Reddit y *serán compartido* en los locales de la diáspora | Revisión de derechos del episodio (§3.4) |
| **M9 · jun-2027** | 4 · 24 | **E12** (propuestas de patrocinio); control de carril (base: 59 suscriptores, 1.478 h); **control de hábito de M9** (solo si hubo GO condicionado: parar si H1 < 25 %, H4+H5 < 35 % y vistas < 103); **control de embudo** (R1 ≥ 1.000, R3 ≥ 15 %, ≥ 2 semillas activas) y cierre del E6 ampliado | Colaboración "da man de…" con un divulgador | **Convocatoria de contenidos digitales de la CRTVG (~junio)**: dossier con catálogo y datos [R `ingresos_alt.md` §1.4]. Cuenta como la solicitud que exige la P2 |
| **M10 · jul-2027** | 4 · 28. Serie **"Historias do Camiño"** (2027 es Año Santo Xacobeo: el 25-07 cae en domingo [S, calculado]) | — | Xacobeo 2027: difusión en el ámbito del Camino; **serie espejo de los vídeos del Camino para dormir en castellano (S9), con títulos que empiezan por "Camiño de Santiago"/"Compostela"**. **El 25-07 se trata como Santiago y Camino, no como Día da Patria política**. Segunda votación trimestral | — |
| **M11 · ago-2027** | 4 · 32. Posible primer recopilatorio (con montaje nuevo; no cuenta como vídeo nuevo en las puertas) | — | Verano: visitas de la diáspora; 3.ª oleada de correos. Primera lectura de espectadores habituales (H1b) | Revisión del proyecto de ley español de IA |
| **M12 · sep-2027** | 4 · **36** | **Puerta 2** (30-09) | Preparar Samaín 2027 (*Serán de Samaín*, gran fecha de otoño). **Matriz de hábito de la P2, con la regla previa de embudo (R1 ≥ 1.200, R3 ≥ 20 %, ≥ 3 semillas activas)**; balance de E14, E15 y de las reglas de abandono por red | **Youtubeiras+ 2027**: inscripción (Revelación y Pódcast) [S, patrón de septiembre a noviembre] |

---

## 5. Supuestos críticos y lagunas (para el revisor)

1. **Volumen de búsqueda en galego:** no hay datos (Google Trends no se pudo consultar). Todo el §2.4 son reglas razonadas, no medidas; lo resuelve E6.
2. **Cifra CELGA (más de 4.000 inscripciones en 2025):** sale de un fragmento de búsqueda. Hay que confirmarla en el Portal da Lingua.
3. **Encaje del art. 50.4 (texto) con la divulgación histórica:** es una interpretación. Como se declara todo igualmente, el riesgo de equivocarse es mínimo.
4. **Voces de Nós: doble permiso pendiente.** Falta (a) la respuesta escrita de la USC/Gradiant y (b) el consentimiento personal de Gaspar González Somoza (Brais), Consuelo Díaz Isorna (Celtia) o la locutora de Sabela-Nós (nombre no publicado). No sabemos si aceptarán ni qué pedirán: la probabilidad es un supuesto sin base. **No bloquea el lanzamiento**, porque la voz de reserva de proveedor está preparada desde el E0; lo que se juega es la calidad de la voz, no la fecha. La oferta (100 € + 10 % de los ingresos netos) **hay que añadirla al modelo de `drafts/retornos.md`**. Tampoco está cerrado si una voz sintética reconocible es "la voz" de la persona a efectos del art. 7.6 de la LO 1/1982; el plan asume que sí.
4 bis. **Respuesta de ADA/AGPTI:** desconocida. Pueden ignorar la carta o criticarla en público; en ambos casos, el precedente de haber avisado antes, con permiso y oferta de remuneración, es la mejor defensa disponible [S].
5. **Acceso a "Test & Compare":** verificado en v5 que **no exige el YPP** (basta Studio en ordenador y funciones avanzadas, que se obtienen verificando la identidad) [F https://support.google.com/youtube/answer/13861714?hl=en ; https://support.google.com/youtube/answer/9890437?hl=en]. **Queda abierto** si un vídeo publicado como estrea admite la prueba una vez acabada (la ayuda solo dice que las estreas no se pueden probar); se comprueba con el episodio 1 y, si no, los episodios espejo se publican sin estrea (§2.4 bis).
6. **Tarifas de la revisión científica (50-150 €)** y de los patrocinios: supuestos sin referencia gallega.
7. **Día Mundial del Sueño de 2027:** las fuentes dan el 13 o el 19 de marzo. El 13-03-2027 es sábado, así que por la regla del "viernes anterior al equinoccio" es el **19**. Confirmar en la web oficial.
8. **Márgenes estrechos de las puertas:** en la P1, 24 frente a 20 suscriptores; en la P2, 107 frente a 100 (y la estancada en 87). Salen de un modelo sin ruido. Se recalibran en M4 con los vídeos 1-4 (§4.2); lo que no cambia es la regla: se sigue solo si la trayectoria llega al fan funding (500 + 3.000 h) antes de M30.
9. **Youtubeiras+ 2026 y el valor esperado:** `drafts/retornos.md` §6 asigna un 8-30 % de probabilidad de premio en 2026, que exige 3 piezas publicadas antes del 15-11-2026. Con la opción (b) recomendada aquí (§2.3), esa esperanza (~88 € en el camino P1) pasa a 2027. Efecto pequeño en el valor esperado, pero hay que alinearlo en `retornos.md`.
10. **Entidades de la diáspora:** 202 en el Rexistro da Galeguidade [COMP]. No se ha medido cuántas siguen activas ni su uso de redes. La tasa de respuesta (≥ 3 de cada 20) es un supuesto.
11. **Umbrales de hábito (H1-H5) sin *benchmark* público.** Se derivan del modelo (suscriptores, vistas y peso del catálogo en la rama base; §4.0) y no de datos de canales de sueño reales. El modelo **no tiene una variable de hábito**: que la rama que va a crecer muestre más recurrentes ya en M6 es una **hipótesis**, no una salida del modelo. Por eso el hábito solo decide el tipo de GO y la parada de M9 exige que fallen a la vez el hábito **y** las vistas. Se recalibran en M4.
12. **Control de M9: hay que añadirlo a `drafts/retornos.md`.** Cambia el árbol solo en la rama estancada con GO condicionado (ahorro de ~330 € y ~105 h); el valor esperado mejora un poco, pero hay que recalcularlo allí.
13. **Tamaño de r/galicia y r/Galiza y uso del galego en X:** sin verificar (Reddit bloqueó la consulta). Las metas de Reddit son de participación, no de tráfico, por esta razón.
14. **Metas de comunidad** (seguidores, Carta, propuestas, % de comentarios en galego, 45 % de apertura): supuestos de diseño sin referencia gallega.
15. **Horas:** la Etapa 1 queda sin margen con la comunidad (78 h + 24 h = 102 h); el orden de recorte del §2.8.5 es la salvaguarda. Precio del plan de correo por encima de 250 suscriptores y edad mínima de consentimiento (14 años, LOPDGDD) por verificar.
16. **Umbrales de embudo (R1-R3) sin *benchmark* de canales de sueño ni de canales en galego.** El único dato oficial es que la mitad de los canales y vídeos tiene un CTR de impresiones de entre el 2 % y el 10 % [F https://support.google.com/youtube/answer/7628154?hl=en]. Las impresiones por vídeo se derivan de las vistas de las puertas con dos supuestos (cuota de vistas desde superficies con impresión del 45-65 % y CTR del 4-5 %), y la cuota de sugeridos ajenos es una hipótesis sin valor por rama, porque el modelo de `drafts/retornos.md` no tiene fuentes de tráfico. Por eso el embudo **no decide el GO**: solo ordena qué se cambia primero. Se recalibra en M4. Tampoco está verificado que Studio muestre el CTR filtrado por fuente con tan pocas impresiones.
17. **Vídeos semilla:** los informes guardan título, canal y vistas, no la URL; se completa en M1. La hipótesis de que los temas y títulos espejo hacen que YouTube coloque a Serán junto a vídeos en castellano (con audio en galego) es exactamente lo que mide el E15; puede que el sistema no cruce idiomas de audio y R3 se quede bajo aunque R1 y R2 cumplan. En ese caso la adyacencia se limita a los semillas en galego (S7 y la divulgación del §1.2) y pesa más la siembra.
18. **Espejo sin copia:** el texto exacto de la política de spam y metadatos engañosos de YouTube no se ha citado en esta pieza; se verifica en M1. La regla interna (no copiar miniaturas, nombres ni logotipos; el título dice siempre la verdad sobre el contenido y el idioma) va más allá de lo que cabe esperar que exija la política [S].

---

## 6. Fuentes nuevas de esta pieza (no incluidas en `research/`)

- Letras Galegas 2027, Neira Vilas: https://academia.gal/-/as-letras-galegas-2027-celebraran-a-xose-neira-vilas ; https://www.galiciaconfidencial.com/noticia/5945510-xose-neira-vilas-sera-autor-homenaxeado-nas-letras-galegas-2027 ; https://editorialgalaxia.gal/xose-neira-vilas-sera-a-figura-homenaxeada-no-dia-das-letras-galegas-2027/
- Críticas a la recreación con IA de Begoña Caamaño (CSAG, 17-05-2026): https://www.nosdiario.gal/articulo/social/que-non-deixala-falar-criticas-ia-empregada-pola-crtvg-recrear-begona-caamano/20260518160723256730.html
- Art. 50 en vigor y no aplazado: https://www.goodwinlaw.com/en/insights/publications/2026/08/alerts-technology-dpc-eu-ai-act-transparency-obligations-now-in-force ; https://www.joneswalker.com/en/insights/blogs/ai-law-blog/yes-august-2-still-matters-the-eu-approved-a-high-risk-ai-delay-but-most-trans.html?id=102nbon ; https://usercentrics.com/knowledge-hub/eu-ai-act-high-risk-delay-article-50-transparency-consent/ ; texto: https://artificialintelligenceact.eu/article/50/ ; sanciones: https://artificialintelligenceact.eu/article/99/
- Código de Práctica de marcado y etiquetado (10-06-2026): https://digital-strategy.ec.europa.eu/en/news/commission-publishes-code-practice-marking-and-labelling-ai-generated-content ; https://www.scl.org/european-commission-publishes-code-of-practice-on-marking-and-labelling-ai-generated-content/
- Proyecto de ley español de IA: https://www.lamoncloa.gob.es/consejodeministros/resumenes/paginas/2026/260526-rueda-prensa-ministros.aspx ; https://www.congreso.es/public_oficiales/L15/CONG/BOCG/A/BOCG-15-A-97-1.PDF ; https://www.economistjurist.es/zbloque-1/ley-organica-de-ia-espana-aterriza-el-ai-act-con-aesia-sanciones-y-sandboxes/
- Aclaración de YouTube del 16-07-2026: https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/
- Licencia de FLUX.1 [dev]: https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md ; https://artificialguy.com/blog/flux-licensing-commercial-use/
- Rexistro da Galeguidade (datos abiertos, descargado el 29-09-2026): https://abertos.xunta.gal/catalogo/administracion-publica/-/dataset/0571/entidades-rexistro-galeguidade
- CELGA 2025: https://www.galiciaconfidencial.com/noticia/5837110-tes-interese-facer-as-probas-celga ; https://www.lingua.gal/o-galego/aprendelo/celga
- Test & Compare de títulos: https://www.socialmediatoday.com/news/youtube-adds-title-testing-youtube-studio/753015/ ; https://routenote.com/blog/youtube-expands-a-b-title-testing/
- Día Mundial del Sueño: https://en.wikipedia.org/wiki/World_Sleep_Day ; https://days.to/world-sleep-day/2027
- TRLPI (texto consolidado): https://www.boe.es/buscar/act.php?id=BOE-A-1996-8930
- LO 1/1982, de protección civil del derecho al honor, a la intimidad personal y familiar y a la propia imagen (arts. 2.2 y 7.6): https://www.boe.es/buscar/act.php?id=BOE-A-1982-11196
- AI Act, art. 3(60) (deepfake): https://artificialintelligenceact.eu/article/3/ ; art. 99.4 y 99.6 (sanciones y pymes): https://artificialintelligenceact.eu/article/99/
- Identidad y condiciones de las voces de Nós: https://huggingface.co/datasets/proxectonos/Nos_Brais-GL (Gaspar González Somoza) ; https://huggingface.co/datasets/proxectonos/Nos_Celtia-GL (Consuelo Díaz Isorna; cesión a la USC por 15 años) ; https://zenodo.org/records/8027725 (Sabela, locutora de radio profesional; CRPIH y UVigo) ; ficha del modelo sin mención al consentimiento: https://huggingface.co/proxectonos/Nos_StyleTTS2-Brais-GL
- Microsoft, nota de transparencia de Text to speech (uso de voces precompiladas y obligación de revelar su carácter sintético): https://learn.microsoft.com/en-us/legal/cognitive-services/speech-service/text-to-speech/transparency-note
- Requisitos de fan funding (500 suscriptores + 3.000 h): https://support.google.com/youtube/answer/72902 ; YPP (1.000 suscriptores + 4.000 h vigente): https://support.google.com/youtube/answer/72851 ; 8.000 h desde el 1-02-2027: https://blog.youtube/news-and-events/youtube-partner-program-updates-2027-new-opportunities-earn/
- **Comunidad y hábito (v4, consultado el 29-09-2026):** definiciones de espectadores nuevos, ocasionales, habituales, recurrentes y únicos, e informe de horas de la audiencia: https://support.google.com/youtube/answer/9314416?hl=en ; fuentes de tráfico (navegación, sugeridos, listas, externas, notificaciones): https://support.google.com/youtube/answer/9314355?hl=en ; publicaciones y encuestas de la comunidad: https://support.google.com/youtube/answer/9409631?hl=en ; moderación de comentarios: https://support.google.com/youtube/answer/9483359?hl=en ; *serán* en el Dicionario da RAG: https://academia.gal/dicionario/-/termo/ser%C3%A1n ; mastodon.gal (API de la instancia): https://mastodon.gal/api/v1/instance ; Podgalego: https://podgalego.agora.gal y https://t.me/podgalego_episodios ; Obradoiro Dixital Galego: https://obradoirodixitalgalego.gal/ ; perfiles de Bluesky (API pública `app.bsky.actor.getProfile`: engalego.gal, orgullogalego.bsky.social, galegotube.bsky.social, podgalego.bsky.social, nosdiario.gal.web.brid.gy) ; Buttondown: https://buttondown.com/pricing ; MailerLite: https://www.mailerlite.com/pricing
- **Embudo de recomendación (v5, consultado el 29-09-2026):** impresiones y CTR (qué cuenta como impresión y dónde): https://support.google.com/youtube/answer/9314486?hl=en ; rango de CTR (la mitad de canales y vídeos entre el 2 % y el 10 %): https://support.google.com/youtube/answer/7628154?hl=en ; tarjeta "Fuente de tráfico: vídeos sugeridos" con los vídeos concretos de origen: https://support.google.com/youtube/answer/9314355?hl=en ; Test & Compare (requisitos, exclusión de estreas, gana el tiempo de visionado): https://support.google.com/youtube/answer/13861714?hl=en ; funciones avanzadas (historial del canal o verificación con documento o vídeo): https://support.google.com/youtube/answer/9890437?hl=en ; títulos y descripciones traducidos: https://support.google.com/youtube/answer/4792576?hl=en
- Carriles y fechas de desbloqueo por rama: `gauntlet/model/puertas_gtm.py` (reutiliza `model/modelo2.py` con el calendario del §4.0). Todas sus salidas son [S].

---

## 7. Registro de cambios v1 → v2 (respuesta al crítico)

| Carencia señalada | Cómo se resuelve |
|---|---|
| Umbrales de la P1 (≥ 300 vistas, ≥ 150 suscriptores) y de la P2 (≥ 350 suscriptores, ≥ 8.000 h) incompatibles con `drafts/retornos.md` (≥ 60/20 y ≥ 100/100) y atribuidos a él por error | Tabla única en el §4.2 con **los umbrales de `retornos.md`**, los valores de cada rama (clónico, estancada, base, alta) en cada puerta y el resultado. Eliminada la atribución errónea |
| 350 suscriptores no desbloquean nada | Cada puerta se ancla a un desbloqueo real: fan funding (500 + 3.000 h) y YPP (1.000 + 8.000 h), con la fecha proyectada por rama. La P1 corta las trayectorias que nunca llegan al fan funding; la P2, las que llegan demasiado tarde (M34); la P3, las que no entran en el YPP a tiempo |
| "Camino a 8.000 h en M12" cuando la base tiene 2.681 h | Las horas pasan a ser **control por carril**: base 612 h (M6) → 2.681 h (M12) → 3.000 h (M13) → 8.000 h (M23 con E2, M32 en mantenimiento). Solo la rama alta llega a 8.000 h en M12, y se usa como "señal de rama alta", no como condición |
| Cadencia incoherente: ~9 vídeos en M6 frente a 12 | Cadencia fija (§4.0): lanzamiento con 3 en M2, 2 al mes en M3-M5, 3 en M6 (con el especial del Día Mundial do Sono) → **12 vídeos en la P1**; semanal desde M7 → **36 en la P2**; 60 en la P3. Se comprobó con el modelo que las puertas no cambian (±1) |
| E3, E4 y el cuadro de mando con números distintos | E3: ≥ 60 vistas a 30 días y lectura temprana en M4 por carriles. E4: ≥ 1,6 suscriptores por 100 vistas (punto medio clónico/base, mínimo para el fan funding en M28). E10: ≥ 25 % (supuesto A10). E12: ≥ 5 propuestas enviadas (condición de la P2), no un patrocinio cerrado. Cuadro de mando con carriles por rama (§4.3) |
| Prórroga de 3 meses tras un NO-GO en la P1 (no estaba en el modelo) | Eliminada: NO-GO en la P1 = parar, como en el árbol de `retornos.md` |

---

## 8. Registro de cambios v2 → v3 (respuesta al crítico de la ronda 2)

| Carencia señalada | Cómo se resuelve |
|---|---|
| Las voces de Nós son de personas reales identificables; contradicción con "nunca recrear la voz de una persona real" (§2.6, compromiso 5) | Identificadas con fuente: Brais = Gaspar González Somoza, Celtia = Consuelo Díaz Isorna, Sabela-Nós = locutora de radio profesional sin nombre publicado. La regla pasa a ser "ninguna voz de una persona real sin su consentimiento escrito para este uso; nunca imitar a nadie concreto ni recrear a fallecidos" (§0.8, §2.6, §3.3 bis) |
| Solo había un correo a la USC sobre la licencia del dataset | **Doble permiso**: USC/Gradiant + consentimiento personal del locutor, con secuencia, plantilla de consentimiento, oferta (crédito, 10 % de ingresos netos, 100 € a la firma, veto por episodio, retirada con sustitución en ≤ 30 días) y fecha límite del 6-11-2026 (§2.6 bis) |
| Falta el derecho a la propia voz y el encaje con el art. 3(60) y el 50.4 | §3.3 bis (LO 1/1982, arts. 7.6 y 2.2, con cita literal) y fila de deepfakes del §3.3 reescrita: la voz de Nós **se trata como deepfake**; el aviso dice de quién es la voz de base; la excepción artística no aplica a la divulgación |
| Contactar con ADA/AGPTI antes del lanzamiento | §2.6 bis, paso 3 (segunda quincena de octubre), con ofertas concretas; en la lista del §3.7 y en el calendario de M1 |
| "Consentimiento del locutor verificado" como condición de la Puerta 0 y como riesgo de la tabla §3.5 | Añadido a la Puerta 0 (§4.2) con salida a la voz de reserva si falla; nueva fila en el §3.5; nuevo detonante de la Puerta roja; E0 con dos clasificaciones (A: consentimiento documentado por el proveedor, siempre voz de reserva; B: Nós, solo con doble permiso y ≥ 0,5 puntos de ventaja) |
| Art. 99.4 citado para la regla de pymes | Corregido: la regla de "la menor de las dos cifras" es del **art. 99.6**; el 99.4 fija 15 M€ o el 3 %, "whichever is higher" |
| Afirmación del §3.3 de que la voz no imita a ninguna persona real | Eliminada y sustituida por el análisis del §3.3 bis |

---

## 9. Registro de cambios v3 → v4 (respuesta al crítico de la ronda 3: panel de *growth marketer* y sociolingüista)

| Carencia señalada | Cómo se resuelve |
|---|---|
| El GTM era casi solo difusión institucional saliente y medía adquisición, no hábito | Nuevo principio "hábito antes que alcance" (§2.1) y nueva **§2.8 Comunidad y hábito**, con el diagnóstico de por qué el hábito decide en este formato: en M6 la base y la estancada son idénticas en adquisición (§2.8.1) |
| KPIs de hábito con umbrales numéricos integrados en E3 y en P1/P2, y qué decisión dispara cada uno | **Cinco KPIs** con definición oficial de Studio y umbral en M4, P1, M9 y P2 (§4.0): H1 recurrentes (≥ 20 % en la P1, ≥ 30 % en la P2), H1b habituales, H2 horas por espectador, H3 vistas por espectador, H4+H5 tráfico de reproducción continua y navegación (≥ 30 % y ≥ 45 %), más dependencia de siembra. Integrados en E3, en las filas de la P1 y la P2 y en el cuadro de mando. **Matriz de decisión** (§4.2 bis): acelerar (cadencia en la Etapa 1 si las horas lo permiten; presupuesto, Carta y monetización en la Etapa 2), cambiar el formato (menú de 5 cambios ordenados por coste) o parar antes (control de M9, con ahorro de ~330 € y ~105 h). Los umbrales de adquisición no cambian: siguen siendo los de `retornos.md` |
| Plan de presencia en el espacio digital galegofalante, con acciones, frecuencia y métrica | §2.8.4: tamaño medido del ecosistema (Bluesky, mastodon.gal con 1.414 cuentas, Podgalego con 108 pódcast activos y 16 de historia, Obradoiro Dixital Galego, Telegram de Podgalego con 120 suscriptores) y tabla con acción, frecuencia, métrica, meta en M6/M12 y regla de abandono para Bluesky, mastodon.gal, Telegram, Reddit, X y la red de pódcast. Nuevo experimento **E14** |
| Bucle propio con el oyente: temas propuestos, comentarios en galego moderados, lista de correo desde M2, ritual o identidad de "serán" | §2.8.2: ritual (domingo 21:30, estrea con el promotor en el chat, fórmulas fijas, dedicatoria, comentario "ata onde chegaches", "a xente do serán", seráns de temporada), con la definición de *serán* de la RAG. §2.8.3: "Propón un serán" con votación trimestral y 1 de cada 4 episodios elegido por la audiencia; "Normas do serán" en galego ("ninguén corrixe o galego de ninguén"), moderación de Studio y respuestas siempre humanas; **"Carta do serán" desde M2** (antes opcional desde M6), con herramienta gratuita y RGPD. Nuevo experimento **E13** (ritual) |
| (Coherencia) | Presupuesto de tiempo de la comunidad (≈ 1 h/semana en la Etapa 1, con mínimo innegociable y orden de recorte) (§2.8.5); nuevos riesgos en el §3.6 (comunidad que se agria, carga de tiempo); calendario de 12 meses con las acciones de comunidad; nuevas lagunas en el §5 (umbrales de hábito sin *benchmark*, control de M9 pendiente de pasar a `retornos.md`) |

---

## 10. Registro de cambios v4 → v5 (respuesta al crítico de la ronda 4: panel con sociolingüista galega)

| Carencia señalada | Cómo se resuelve |
|---|---|
| No hay KPI de impresiones, de CTR de impresiones ni de tráfico sugerido desde otros canales | Tres KPIs de embudo con definición oficial de Studio, en la **tabla de KPIs del §4.0** y en el **cuadro de mando del §4.3**, con umbral en M4, P1, M9 y P2: **R1 impresiones por vídeo a 28 días** (≥ 450 · ≥ 700 · ≥ 1.000 · ≥ 1.200, derivados de las vistas de las puertas); **R2 CTR de impresiones en navegación y sugeridos** (objetivo 4-6 %, alerta < 3 %, recalibrado en M4 con la mediana de los vídeos 1-4, dentro del rango oficial del 2-10 %); **R3 cuota de sugeridos desde canales ajenos** (≥ 5 % de control · ≥ 10 % · ≥ 15 % · ≥ 20 %), disjunta de H4; y R3b semillas activas. Guardarraíl contra el clickbait (CTR > 8 % con AVD < 20 min). Carriles de impresiones por rama (§4.2 y §4.3), marcados como derivados y no como salida del modelo. Integrados en E3 |
| No hay táctica para aparecer junto a los vídeos de historia para dormir en castellano sobre Galicia | Nueva **§2.4 bis Adyacencia**: (1) **lista de 9 vídeos semilla** con vistas (RELATOS AL OIDO Galicia y Lugo, Imperios y Misterios, Misterios para Dormir Profundo, El Pergamino Mágico, Crónicas de la Historia, Burla Negra, Relatos para Dormir, Camino) y su episodio espejo, vigilados cada mes en la tarjeta de sugeridos; (2) **temas, títulos y miniaturas en espejo** (1 de cada 3 episodios en la Etapa 1; palabras comunes a galego y castellano delante; misma gramática visual sin copiar), que coinciden con los primeros temas del catálogo de `formato.md`; (3) **Test & Compare** verificado: no exige YPP, sí funciones avanzadas (se activan en M1) y **no admite estreas**, con la solución para el ritual; (4) **prueba de metadatos traducidos** que declaran el idioma del audio ("narrado en gallego"), cruzada con R2, R3 y la retención al minuto 1, con regla de adopción; (5) colaboración con los semillas pequeños, sin spam. Nuevo experimento **E15**; E6 ampliado; 20 min al mes financiados recortando Reddit (§2.8.5); calendario actualizado (M1, M2, M3, M4, M5, M6, M7, M9, M10 y M12) |
| La matriz del §4.2 bis no dice qué hacer si fallan el CTR o las impresiones | **Regla previa en todas las lecturas: empaquetado antes que formato**, con una tabla de diagnóstico (impresiones bajas + CTR bajo → empaquetado; impresiones bajas + CTR bien → temas espejo; sugeridos ajenos bajos → adyacencia y metadatos; embudo en umbral y hábito bajo → formato). Paso 0 del menú de cambios; fila nueva en la tabla de decisiones; regla mensual en el §4.3; sin prórroga en M9 por embudo. **Los umbrales de GO/NO-GO de adquisición no cambian** y siguen idénticos a `drafts/retornos.md`: el embudo ordena qué se cambia, no decide si se sigue |

