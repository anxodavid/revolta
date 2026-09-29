# Pieza del plan v2: el canal desatendido (retornos, costes, pipeline y riesgos de plataforma)

- **Versión:** v3 (ronda 3 del constructor), 29-09-2026. Cambios frente a v2: sección §A nueva (¿existe el nicho?,
  veredicto, tres nichos, multi-audio gl + pt + es + en medido, prueba falsable con umbral de parada), §1.3 y §8.2
  rehechos con el catálogo ampliado, P1 sin zona gris, controles H4 y M1-M6. Versión anterior: v2 (ronda 2), 29-09-2026. Cambios frente a v1: tiempos de máquina medidos (§4.1), horas
  del MVP unificadas (57-85 h), §3.3 nueva con el dossier cronometrado, C0 medido (70 % → 80 % tras corregir un fallo
  de H1) y umbrales del código alineados con los del plan (WER ≤ 6 %, −18 a −16 LUFS). Cadencia ajustada para cumplir D3.
- **Qué cubre:** si el nicho existe (§A, pregunta obligatoria), retornos esperables con comparables reales, costes, horas (D3), cadencia, arquitectura del pipeline
  automático, controles automáticos que sustituyen a la revisión humana (qué detectan y qué no), política de YouTube,
  AI Act art. 50, riesgos de lengua e historia sin filtro humano, puertas go/no-go y KPIs para pagar la validación de voz (D1).
- **Qué no cubre (otras piezas del Gauntlet 2):** el vídeo piloto y su especificación visual fina, y el análisis a fondo
  de la relación con la comunidad (Nós, USC/CiTIUS, CRTVG, RAG, CCG, SXL, sector de la voz). Aquí solo aparece lo que
  afecta a costes, puertas y riesgos de plataforma, con remisiones.
- **Convenciones:** [F] dato con fuente (URL al lado); [R] reutilizado del Gauntlet 1, con el fichero de origen (allí
  están las URLs); [P] medida propia en este entorno; [S] supuesto o estimación propia, sin verificar. Tipo de cambio de
  trabajo: 1 USD = 0,87 € [S, el mismo que usa `../../gauntlet/piezas/pipeline.md`].
- **Nombre de trabajo del canal:** *Serán* (del Gauntlet 1). Anónimo (D6).

---

## 0. Resumen

0. **¿Existe el nicho? Veredicto: no hay evidencia suficiente; lo más probable es que sea marginal** (§A). A favor:
   0 competidores en galego, 108 K vistas de "Galicia para dormir" (lendas) en castellano. En contra: solo el 3,59 %
   ve audiovisual sobre todo en galego y el mercado atendible es de 2.000-20.000 personas. Se estiman tres nichos por
   separado: (a) historia en galego, 15-100 vistas por vídeo; (b) toda Galicia en galego (lendas, mar, idiosincrasia),
   25-200, **la opción del plan**; (c) (b) con pistas pt/en/es, 40-400 en total, con el riesgo de que el galego quede
   en minoría. **Prueba falsable:** 8 episodios (4 de historia y 4 de Galicia ampliada) y decisión a las ≈ 10 semanas (el episodio 8 sale en la semana 6; se esperan sus 30 días).
   Si la mediana a 30 días es < 40 vistas, o menos del 15 % viene de Galicia sin ningún comentario en galego, se para.
   Con 40-149, modo mínimo; con ≥ 150, plan. Las pistas pt + en se prueban después en 4 de esos 8 vídeos, con 4 de
   control. El castellano va al final y con condiciones, porque es la pista que desplaza al galego en Galicia (§A.4).
1. **En dinero, el canal casi seguro pierde un poco; el caso es cultural y técnico, no económico.** Escenario central a
   12 meses: 0 € de ingresos y 20-100 € de gasto; ≈ 85-140 h del promotor el primer año natural (57-85 h de montaje + 25-55 h
   de régimen en las ≈ 40 semanas restantes, §3). Solo en el escenario optimista (≈ 8-12 % [S]) llega al YPP, y aun así a 10-60 €/mes (§1).
2. **El listón de referencia es un pico, no la media:** *Historia Desconocida* hace ≈ 1,0 M de vistas con 21 vídeos, pero
   el 67 % viene de 3 vídeos de una semana de abril; sus vídeos de ago-sep 2026 hacen 1.300-6.400 vistas en castellano
   [F, `../referencia.md`]. En galego, el techo es 1-2 órdenes de magnitud menor (§1.2).
3. **Coste casi cero de verdad:** voz, ASR, imágenes y montaje en CPU propia con open source (0 €); el guion con un LLM
   frontier por API ≈ 1-2 USD por episodio, o 0 € con un LLM abierto de Nós si se acepta peor galego (§2).
4. **Horas:** construir el MVP pide **≈ 57-85 h → 10-14 semanas a 6 h/semana** (§3.1, incluye el stock de 8 dossieres).
   Después, el régimen estable **no cabe en 1 h/semana a 1 episodio por semana** una vez que se acaba el stock: el
   dossier de un episodio de 60 min pide 25-75 min de persona (§3.3). Se cumple D3 bajando a **1 episodio cada 2
   semanas** tras los 8 primeros: 40-87 min/semana, ≈ 60 de centro (§3.2).
5. **Cadencia:** 3 episodios la primera semana y 1/semana hasta agotar el stock (8 episodios); después, 1 cada 2
   semanas (≈ 30 episodios el primer año). 60 min narrados + 30 de cola. La máquina no es el límite: **5,0-7,0 h de
   reloj por episodio medidas y extrapoladas** (4,4-5,8 h sin LLM, §4.1), una noche. El límite son las horas de
   persona (D3) y el riesgo de parecer producción masiva (§4).
6. **Pipeline:** diseño de 9 etapas en una cola local (§5.1); el código actual tiene 8 etapas con otro reparto más
   `dossier.py` aparte, y 10 puertas automáticas. El diseño tiene **14 controles** que bloquean la publicación; hoy
   hay 6, varios en versión parcial. Ninguno sustituye del todo a un filólogo ni a un historiador (§5-6).
7. **C0 (errores canario) medido: 70 %** (14/20) con los controles del código, **por debajo del 80 % de P0**.
   Un fallo de H1 (anclaba "dous" dentro de "douscentas") explicaba 2 fallos; corregido, **80 % (16/20)**, justo en el
   umbral y sobre el mismo conjunto con que se encontró el fallo. Las invenciones sin nombre ni cifra siguen en 2/5:
   solo las sube H2 (juez LLM). P0 exige además ≥ 80 % en un conjunto nuevo y ≥ 4/5 en "sin fuente": **hoy no se
   pasa** (§6.1). Los umbrales del código ya son los del plan (WER ≤ 6 %, −18 a −16 LUFS); el vídeo de ejemplo, a
   −20 LUFS, no pasaría A2 y hay que volver a mezclarlo.
8. **Lo que los controles NO ven:** errores históricos fluidos y plausibles que no se contradicen con las fuentes
   cargadas, castellanismos sutiles que no están en las listas, **errores de prosodia que el ASR entiende igual**
   (vocales abiertas/cerradas, acento), anacronismos visuales y tono (§6.3). Se mide su tasa con **errores canario**
   inyectados y se publica en la página de erratas.
9. **YouTube:** el formato es literalmente "presentación de imágenes + voz IA + plantilla", el patrón que la aclaración
   del 13-07-2026 nombra ("image slideshows and templated storylines") [F]. **Probabilidad de que el YPP se deniegue o
   se retire: 40-60 % [S].** Como hobby, eso no mata el proyecto; mata solo los ingresos (§7.1).
10. **Etiquetado:** imágenes fotorrealistas de época ⇒ la etiqueta "contenido alterado o sintético" es **obligatoria**,
   no opcional [F]. Se activa siempre (§7.2).
11. **AI Act art. 50:** sin revisión humana **no hay excepción** para el texto de interés público: hay que declarar que
    el texto es generado por IA, además de la voz y las imágenes. Aviso hablado en los primeros 30 s (§7.3).
12. **El riesgo más serio para la tesis "pro lingua" no es YouTube: es publicar galego sintético sin revisar en la web
    abierta**, que acaba en los corpus con que se entrenan los próximos modelos en galego. Mitigación obligatoria: todo
    texto publicado va marcado como sintético y nunca se ofrece como corpus limpio (§8.3).
13. **D1 (validación de voz, 850-1.500 €) solo se paga si se cumplen a la vez tracción (2 de 3 KPIs), permiso de
    Nós/USC y ninguna alarma de plataforma abierta.** Probabilidad de llegar a pagarla en 12 meses: ≈ 8-12 % [S] (§9).

---

## A. ¿Existe el nicho? (pregunta obligatoria del promotor, 29-09-2026)

Datos nuevos de esta sección: 10 búsquedas en YouTube con yt-dlp y una prueba de traducción y voces en pt/es/en, todo
en `../medidas/nicho/` (README con la tabla de tiempos, `busquedas-yt.txt` con las URLs de cada vídeo citado).

### A.1 Veredicto

**Veredicto: NO HAY EVIDENCIA SUFICIENTE de que exista un público en galego para historia y cultura de Galicia para
dormir. La hipótesis más probable [S] es que, si existe, es MARGINAL: decenas a pocos cientos de oyentes por vídeo.**
Lo que sí está demostrado es que **el tema** existe: "Galicia para dormir", sobre todo las lendas, funciona **en
castellano**. El plan no necesita que el nicho exista para tener sentido como hobby (D6), pero sí para justificar
horas: por eso la prueba de §A.4 lo decide en ≈ 10 semanas desde la primera publicación, con un umbral de parada sin
zona gris.

| A favor de que exista | Cifra | Fuente |
|---|---|---|
| El tema engancha en castellano | Relatos al Oído: **107.875** vistas (lendas de Galicia, 2 h), 17.264 (mosteiro), 13.904 (Compostela), 7.829 (Lugo); Misterios para Dormir Profundo: 9.135; El Pergamino Mágico (Santa Compaña): 5.106 | [P `../medidas/nicho/busquedas-yt.txt`] |
| Hueco total en galego | **0** canales o vídeos de historia o lendas para dormir en galego en 10 búsquedas (y 0 en el censo del Gauntlet 1) | [P] [R `audiencia.md` §5] |
| Hay público galego de historia y cultura en YouTube | Burla Negra 614-12.072 vistas por documental; Orgullo Galego 300-3.200; lendas en galego sin formato para dormir 522-1.577 (politicalinguistica), 1.396 (SAGA) | [R `retornos.md` §4.4] [P] |
| Acepta galego más gente de la que lo prefiere | 28 % mezcla ("máis castelán") además del 3,59 % | [R `audiencia.md` §2.4] |
| El hábito de dormirse con audio es masivo | 48 % de los oyentes de pódcast los usa para dormirse (Acast 2023) | [R `audiencia.md` §6.2] |
| **En contra** | | |
| Consumo audiovisual en galego mínimo | **3,59 %** de los mayores de 16 que ven contenidos audiovisuales los ve siempre o sobre todo en galego (IGE, EEF 2023; 68,1 % siempre en castellano) ≈ **60.000-84.000 personas** (sobre ≈ 2,34 M mayores de 16, según cuántos vean audiovisual [S]) | [R `audiencia.md` §2.4] |
| Mercado atendible pequeño | **2.000-20.000** oyentes habituales posibles | [R `audiencia.md` §8] |
| "0 competidores" también es una señal mala | Nadie lo ha intentado o nadie lo ha sostenido; la búsqueda no distingue entre hueco y desierto | [S] |
| El galegofalante habitual encaja mal con YouTube | Mayor, rural, del interior; el hábito de YouTube cae después de los 65 | [R `audiencia.md` §2.3 y §3] |
| Lo que hay en galego hace poco | Lendas en galego: 59-1.577 vistas **acumuladas en años**; la serie de TVG, 0,7-4 K por capítulo | [P] [R] |
| La demanda en castellano no se traslada | El 96,4 % de los mayores de 16 **no** consume audiovisual sobre todo en galego (3,59 % sí): el que busca "Galicia para dormir" ya lo tiene en castellano, con mejor voz | [R] [S] |
| La cola larga del tema es muy corta | "Galicia sleep" en inglés: 16-292 vistas (Relax and Let Go, Spain Dreams ASMR, The Dreaming Atlas) | [P] |

Embudo [S sobre R]: ≈ 2,34 M mayores de 16 en Galicia → 3,59 % en galego ≈ 60.000-84.000 → interesados en historia/cultura,
en YouTube y con hábito de audio para dormir: 2.000-20.000 → alcanzables el primer año sin comunidad previa ni prensa:
1-5 % → **20-1.000 personas distintas**.

### A.2 Tres nichos, estimados por separado [S]

| Nicho | Audiencia atendible | Competencia directa | Vistas por vídeo a 30 días (mediana) | Suscriptores a 12 meses | P(pasa la parada de §A.4: mediana ≥ 40) | P(mediana ≥ 150) | Veredicto |
|---|---|---|---|---|---|---|---|
| **(a) Historia de Galicia para dormir, en galego** (castros, suevos, Camiño, mosteiros, irmandiños) | 1.000-10.000 (la parte "historia" del 2-20 K) | 0 en galego. Indirecta: divulgación en galego sin formato para dormir (Historia a Debate, Burla Negra) | **15-100** | 10-150 | **35-50 %** | 5-10 % | Sin evidencia suficiente; probable marginal |
| **(b) Toda Galicia para dormir, en galego** (lendas, mar, castros, Camiño, vida cotiá, idiosincrasia) | 2.000-30.000 (las lendas atraen a quien no busca historia) | 0 en galego. Indirecta: Relatos al Oído y 2-3 canales más en castellano | **25-200** | 15-300 | **55-70 %** | 15-25 % | Sin evidencia suficiente; probable marginal, algo mayor que (a). **Es la opción del plan** |
| **(c) = (b) + pistas pt/en/es en el mismo vídeo** | Teórica: cientos de millones; real: la fracción que acepta una voz open source peor que la de los competidores (§A.3) | pt: género fuerte, **0 vídeos de Galicia**; es: Galicia ya cubierta (8-108 K); en: saturado | **40-400 en total**, de las que el galego se queda con el **25-70 %** del tiempo de visionado | 20-500 | P(las pistas suben ≥ 30 % las vistas, §A.4 fase 2): **40-55 %** | 20-30 % | El tema existe en es (demostrado) y hay hueco en pt; que nuestras voces lo capten: sin evidencia |

Por qué (b) puntúa más que (a): el único vídeo de "Galicia para dormir" con más de 100 K vistas es de **lendas**, no de
historia [P]; las lendas en galego son lo único con vistas en galego fuera de los canales con comunidad [P]; y los temas
de mar y Camiño ya los usan los canales de castellano en inglés (Relatos al Oído) [P]. Por qué no puntúa mucho más: el
público en galego sigue siendo el mismo embudo de 2-20 K; lo que cambia es la proporción que se interesa.

### A.3 Nicho (c) en detalle: pistas multi-audio gl + pt + es + en

**A.3.1 Cómo funciona en YouTube**
- Desde el 10-09-2025, todos los creadores con acceso a *funciones avanzadas* pueden subir pistas de audio en otros
  idiomas al mismo vídeo [F https://techcrunch.com/2025/09/10/youtubes-multi-language-audio-feature-for-dubbing-videos-rolls-out-to-all-creators/].
  Las pistas las pone el creador, deben durar "aproximadamente lo mismo" que el vídeo, y si el contenido de la pista
  difiere del original, puede retirarse [F https://support.google.com/youtube/answer/13338784?hl=en].
- **Vistas y horas se suman en un solo vídeo**: todas las pistas cuentan para el mismo contador, para las 8.000 h del
  YPP y para la señal del algoritmo [F https://ppc.land/youtube-makes-multi-language-audio-available-to-millions-of-creators/].
  De media, los creadores con pistas extra sacan **más del 25 %** del tiempo de visionado de la lengua no principal
  [F support.google.com, arriba]; es una media de canales grandes (Jamie Oliver: vistas ×3 [F TechCrunch]), no una
  previsión para nosotros.
- **Pista por defecto:** la de la lengua preferida del espectador, **deducida de su historial** [F support.google.com].
  Consecuencia directa: un galego que ve YouTube sobre todo en castellano (la gran mayoría del 96,4 % que no lo ve sobre todo en galego) oirá **por defecto la pista en castellano**.
  Ese es el mecanismo principal por el que el galego puede quedar marginal (§A.3.5).
- **Descubrimiento:** con título y descripción traducidos, el vídeo aparece en búsquedas en esos idiomas [F
  support.google.com]. Se ve en las búsquedas: Relatos al Oído sale con títulos en inglés [P].
- **Lo que no sabemos y se comprueba en Studio antes de construir nada [S]:** (1) si el galego está en la lista de
  idiomas de pista y de idioma del vídeo (si no está, el diseño multi-audio no sirve y (c) se descarta); (2) si la API
  permite subir pistas (no conocemos método: se supone subida a mano, 3-5 min por pista); (3) si Analytics desglosa el
  tiempo de visionado por pista (si no, se usa el país como sustituto: Portugal/Brasil ⇒ pt, países anglófonos ⇒ en).
- La etiqueta de contenido sintético (§7.2) y el aviso del AI Act (§7.3) valen para cada pista: el aviso hablado se
  traduce y se sintetiza como el resto.

**A.3.2 Competencia por idioma** [P `../medidas/nicho/busquedas-yt.txt`]

| Idioma | Género "historia para dormir" | Galicia en ese idioma | Lectura |
|---|---|---|---|
| pt (sobre todo pt-BR) | Fuerte y con IA: Histórias Chatas Para Dormir 439.701; Descanse com Histórias 214-240 K; Historias para relaxar e dormir 32-228 K; História para Acalmar 90.586 | **0 vídeos para dormir**. Señal de interés: "Galicia é de Portugal? A História que te Esconderam" (documental, pt) 129.332 | **El mejor hueco**: lengua hermana, tema sin cubrir, y no compite con el galego dentro de Galicia |
| es | Saturado (Detrás de la Historia 269-296 K por vídeo; Relatos para Dormir 1,05 M) | **Ya cubierto**: Relatos al Oído 7,8-108 K; Misterios 9,1 K; Pergamino 5,1 K | Donde está la demanda, pero con voces comerciales mejores que las nuestras, y es la pista que desplaza al galego |
| en | Saturado (Sleepless Historian 265 K-1 M por vídeo) | Cola larga de 16-2.488 vistas (Historify, Spain Dreams ASMR) | Descubrimiento internacional y diáspora; poca esperanza de volumen |

**A.3.3 Coste en CPU y calidad del TTS open source en pt/es/en** [P `../medidas/nicho/README.md`; CPU compartida con
otro proceso al 300 %, así que los tiempos son pesimistas]

| Paso | Herramienta (licencia) | Medido | Para 60 min narrados (≈ 7.000 palabras) | Nota |
|---|---|---|---|---|
| Traducción gl→es | Nós `Nos_MT-CT2-gl-es` (MIT) [F https://huggingface.co/proxectonos/Nos_MT-CT2-gl-es] | 126 palabras en 1,7 s; 9/11 frases bien; 2 errores: "acomódate" → "acuérdate" y "Rocha Forte" → "Roca Forte" | ≈ 2 min | Rápido; los 2 errores son justo los que tiene que cazar §A.3.4 |
| Traducción gl→en | Nós `Nos_MT-CT2-gl-en` (MIT) | No medido (1,7 GB; sin disco) | ≈ 2 min [S, misma arquitectura] | |
| Traducción gl→pt | Nós no tiene gl→pt; opciones: el LLM frontier que ya redacta, o Apertium gl-pt (reglas) | No medido | 10-30 min de API; ≈ 0,3-1 USD [S] | Recomendado: LLM, con Nós como juez de ida y vuelta |
| Voz pt-PT / es | Piper `tugão` / `davefx` (datos CC0, **afinadas desde la voz *lessac***, cuya licencia hay que revisar antes de monetizar [S]) | **RTF 0,13-0,14** | 8-10 min por idioma (15-20 con las pausas de dormir) | Voz de asistente, claramente por debajo de Brais ST2 [S, sin escucha ciega] |
| Voz pt-BR / en / es | Kokoro-82M (Apache-2.0) [F https://huggingface.co/hexgrad/Kokoro-82M] | **RTF 1,19-1,45** (int8, CPU cargada) | 70-90 min por idioma cargada; 35-60 [S] sin carga | La mejor licencia; pt solo en variante brasileña |
| Control ASR de ida y vuelta | Whisper multilingüe (small/medium), int8 | No medido | ≈ 12 min por idioma [S: RTF 0,2 como en gl] | |
| Mezcla y codificación de la pista | ffmpeg | — | ≈ 2 min | Misma lluvia y cola que la pista gl |

- **Por idioma extra: ≈ 30-45 min de CPU con Piper, 90-130 con Kokoro.** Las dos pistas de la fase 2 (pt-BR + en con
  Kokoro) suman ≈ 3-4,5 h: no caben en la misma noche que el episodio (5-7 h, §4.1), pero a 1 episodio cada 2 semanas
  la máquina está libre 13 de cada 14 noches: se hacen en una segunda noche.
- **Dinero:** +0,3-1 USD por episodio si el LLM traduce al pt y al en [S]; electricidad despreciable.
- **Horas de persona (D3):** subir 2 pistas a mano en Studio, 6-10 min por episodio ⇒ +3-5 min/semana a 1 episodio
  cada 2 semanas. Construir la etapa: **6-10 h** [S], después del MVP y solo si la fase 1 de §A.4 no manda parar: 1-2 semanas a ~6 h/semana (el ritmo de D3 mientras se monta el pipeline) justo después de la decisión de la semana 10. La comprobación en Studio de que el galego existe como idioma de pista se hace antes, en 5 min.
- **Calidad frente a la competencia:** los canales de pt/es/en que hacen cientos de miles de vistas usan voces
  comerciales o humanas [R `formato.md`]; con Piper o Kokoro vamos a peor voz en un mercado más exigente. Por eso (c)
  no se da por buena: se mide.

**A.3.4 Control de calidad automático de la traducción (M1-M6, solo si hay pistas)**

| # | Control | Umbral de bloqueo [S] | Qué detecta | Ejemplo de la prueba |
|---|---|---|---|---|
| M1 | Ida y vuelta: la pista se retraduce al galego (Nós es→gl, en→gl; LLM para pt→gl) y se compara frase a frase con el original (chrF + similitud de *embeddings*) | Frase por debajo del umbral → retraducir ×2 → si sigue, la frase se quita de esa pista; > 5 % de frases quitadas → la pista no sale | Cambios de sentido | "acuérdate" vuelve como "acórdate" ≠ "acomódate" [S: lo cazaría si el umbral es por frase] |
| M2 | Nombres bloqueados: todo nombre propio del dossier aparece igual, salvo exónimos permitidos (Galiza/Galicia, A Coruña/La Coruña...) | 0 cambios | Topónimos y personas traducidos o "corregidos" | "Rocha Forte" → "Roca Forte" [P: lo caza] |
| M3 | Cifras y fechas iguales | 0 diferencias | Años y cantidades alterados | |
| M4 | Encaje en el tiempo: cada frase traducida va en el hueco de la frase gl; si no cabe, se acelera hasta ×1,15 | Ninguna frase fuera de su hueco + 15 %; pista ±1 % de la duración del vídeo | Pistas que se desincronizan con las imágenes o que YouTube rechaza por longitud | |
| M5 | ASR de la pista contra su texto | WER ≤ 8 % | Palabras comidas o mal pronunciadas por el TTS | |
| M6 | Marcadores de lenda conservados ("conta a lenda" → "conta a lenda"/"cuenta la leyenda"/"legend has it") y glosario de préstamos (retranca, morriña, meiga, Santa Compaña se mantienen en galego) | 0 lendas sin marcador; 0 préstamos traducidos | Que la traducción convierta una leyenda en hecho o borre el galego del texto | |

**Qué no ven:** traducciones fluidas pero en registro equivocado, mezcla de pt-PT y pt-BR, calcos que la retraducción
"deshace", y el tono. Igual que en galego (§6.3), el residuo existe y se declara.

**A.3.5 Riesgo de que el galego quede marginal**
- **Mecanismo:** la pista por defecto sale del historial del espectador [F]. Con un público galegofalante de 2-20 K y
  públicos pt/es/en de cientos de millones, si las pistas funcionan, **lo normal es que el galego pase a ser minoría del
  tiempo de visionado** [S]. Y la pista es no solo capta a los de fuera: dentro de Galicia sustituye al galego.
- **Mitigaciones:** (1) título y miniatura originales en galego; traducciones de metadatos solo a pt y en en la fase 2;
  (2) cada pista extra abre con una frase fija: "este vídeo foi feito orixinalmente en galego, a lingua de Galicia"
  (traducida), que convierte la pista en escaparate del galego (tesis pro lingua); (3) **orden: pt y en primero; es
  al final y condicionado** (§A.4, fase 3), porque es la que desplaza al galego entre los galegos; (4) umbral numérico:
  si el galego baja del 25 % del tiempo de visionado, se reduce a la pista pt sola.

### A.4 Prueba falsable con el pipeline (sustituye a la P1 de la v2)

**Fase 1: ¿hay público en galego? (de M0 a ≈ semana 10)**
- **Qué se publica:** los 8 episodios del stock (§4.2), **4 de historia (nicho a) y 4 de Galicia ampliada (nicho b)**,
  alternados, con la misma duración y la misma receta de embudo (ganchos en el primer minuto, luego tono de dormir).
  Solo galego. 3 en la primera semana y 1 por semana después. No añade horas: el stock ya está en el MVP (§3.1).
- **Métricas (Studio, a los 30 días de cada vídeo):** M = mediana de vistas de los 8; Ma y Mb = medianas de cada bloque;
  **G = % de vistas desde ciudades galegas** (Studio > Audiencia > Geografía > ciudades; si Studio no da ciudades, %
  de España como techo [S: verificar el informe]); % de espectadores recurrentes; comentarios en galego de personas
  reales; retención a 2 min; suscriptores netos.
- **Decisión el día 30 del episodio 8 (≈ semana 10). Toda cifra lleva a una sola acción:**

| Resultado | Acción |
|---|---|
| **PARADA:** M < 40, **o** G < 15 % con 0 comentarios en galego | **Nicho declarado inexistente para este formato.** Se para la producción, se publican el código y los informes de error para Nós, y el canal queda quieto. Coste hundido: ≈ 60-95 h y < 30 € |
| **MÍNIMO:** 40 ≤ M < 150 (y no se cumple la parada) | 1 episodio al mes; el 75 % del catálogo del bloque ganador. En M6 se aplica la misma regla a los 4 últimos episodios: **M < 60 → PARADA; M ≥ 60 → sigue a 1 al mes** |
| **PLAN:** M ≥ 150 (y no se cumple la parada) | Régimen de §4.2 (1 cada 2 semanas) y puerta P2 (§9) |
| Reparto del catálogo (se aplica en MÍNIMO y en PLAN) | Mb/Ma ≥ 1,5 → 75 % Galicia ampliada; Mb/Ma ≤ 0,67 → 75 % historia; en otro caso, 50/50 |

- **Por qué 40:** 40 vistas × ≈ 30 episodios × 1,5 (vistas después del día 30) ≈ 1.800 vistas al año × 15-25 min ≈
  450-750 h de escucha al año ≈ **1,2-2,1 h por noche: menos de dos personas durmiéndose con el canal cada noche.** Es
  también el 2 % del extremo bajo del mercado atendible (2.000). Por debajo, la tesis "pro lingua" no tiene a quién
  servir y las horas del promotor no se justifican ni como hobby cultural.
- **Probabilidades [S]:** PARADA 35-50 %; MÍNIMO 40-50 %; PLAN 10-20 %.
- **Ruido declarado:** 8 vídeos y una ráfaga inicial; la mediana resiste un vídeo disparado, pero el reparto Ma/Mb con
  4 contra 4 es orientativo. Se acepta: la prueba decide si seguir, no el catálogo definitivo.

**Fase 2: ¿suman las pistas pt y en? (≈ semanas 12-17; solo si la fase 1 no da PARADA)**
- **Requisitos:** galego disponible como idioma de pista en Studio (§A.3.1); M1-M6 construidos (6-10 h, semanas 10-12).
- **Qué se hace:** se añaden pistas **pt-BR y en** (Kokoro) con título y descripción traducidos a **4 de los 8**
  episodios ya publicados (2 de cada bloque, elegidos a cara o cruz antes de mirar los datos). Los otros 4 son el
  control. YouTube permite añadir pistas a vídeos publicados. Portugués de Brasil por mercado (los competidores de §A.3.2 son
  brasileños) y por licencia (Kokoro, Apache-2.0); pt-PT (Piper `tugão`, más cercano al galego) si se aclara la licencia
  de la voz base *lessac* y el promotor prefiere la variante europea.
- **Métricas:** R = vistas de los 4 con pistas en los 30 días siguientes / vistas de los 4 de control en los mismos
  30 días; **L = % del tiempo de visionado en la pista gl** de los 4 con pistas (Studio por pista; si no, por país).
- **Decisión:**

| Resultado | Acción |
|---|---|
| R < 1,3 | Multi-audio descartado: las pistas no pagan su CPU ni sus minutos. Canal solo en galego |
| R ≥ 1,3 y L ≥ 40 % | pt + en en todos los episodios nuevos; se abre la fase 3 (es) |
| R ≥ 1,3 y 25 % ≤ L < 40 % | pt + en en todos los episodios nuevos; es, nunca |
| R ≥ 1,3 y L < 25 % | **Galego marginal:** solo la pista pt en los episodios nuevos (la lengua hermana, que no compite en Galicia); se quita el en; es, nunca |

**Fase 3: castellano (solo si R ≥ 1,3 y L ≥ 40 %)**. Mismo diseño con una pista es en 4 episodios: si L baja por debajo
del 30 % en esos 4 → se retira la pista es de esos vídeos y no se vuelve a usar; en otro caso, es en todos.

### A.5 Qué cambia en el resto de la pieza
- §1.3: escenarios rehechos con el catálogo ampliado y la opción multi-audio.
- §8.2: catálogo ampliado (lendas, mar, castros, Camiño, vida cotiá, idiosincrasia), con la regla "lo legendario como
  leyenda" convertida en control (H4, §6.1).
- §9: la P1 es ahora la fase 1 de §A.4.
- §6.1: controles H4 y M1-M6 añadidos; §2.1: fila de pistas extra; §11: supuestos nuevos.

---

## 1. Retornos esperables

### 1.1 Comparables reales (observados el 29-09-2026)

**Empezando por la referencia (castellano, IA, historia, 23-41 min):**

| Canal | Idioma | Subs | Vídeos | Vistas por vídeo | Lectura | Fuente |
|---|---|---|---|---|---|---|
| **Historia Desconocida** (referencia) | es (títulos traducidos a en) | 5.050 | 21 (abr-sep 2026) | Mediana ≈ 21.000; 3 picos de 167-331 K en la semana del 20-22 abril; **ago-sep: 1.300-6.400** | El éxito es de ráfaga inicial y del algoritmo anglófono (títulos traducidos). Lo reciente es "miles". | [F, `../referencia.md`, yt-dlp] |
| Sleepless Historian | en, IA, sleep | 715 K | 362 | 8-31 K (típico ~20 K), desde 2-4 M en 2025 | La ola de 2025 ya pasó; declive por vídeo | [R `retornos.md` §4.1] |
| History Before Sleep | en, IA, sleep | 57,7 K | 602 | 1,2-48 K (típico 5-10 K) | Volumen masivo ≠ crecimiento | [R] |
| Boring History Bites | en, IA, sleep | 8,9 K | 38 | **128-1.500** | Llegó tarde a la ola | [R] |
| El Historiador Nocturno | es, sleep | 304 K | 343 | 10-73 K | Líder en castellano | [R] |
| Decenas de "Historia Aburrida para Dormir" | es, IA | **1-1.890** | — | — | La cola larga real del formato | [R] |
| Burla Negra ("Historias da Galiza") | **gl**, documental humano | 1,7 K | — | **614-12.072** en 4 años | El mejor comparable de mercado en galego | [R `retornos.md` §4.4] |
| Orgullo Galego (conversas de historia) | **gl** | 11,5 K | — | **300-3.200** | Marca con comunidad previa | [R `audiencia.md`] |
| Relatos al Oído, "Duérmete con las leyendas... de Galicia" | es, sleep, 2 h | — | — | **107.810** en 11 meses | Hay demanda de "Galicia para dormir", **en castellano** | [R `retornos.md` §4.4] |
| Canal de historia o lendas para dormir **en galego** | gl | — | — | — | **No existe ninguno** (10 búsquedas el 29-09-2026). Veredicto sobre el nicho en §A.1: **sin evidencia suficiente; probable marginal** | [R] [P `../medidas/nicho/`] |
| Histórias Chatas Para Dormir / Descanse com Histórias | pt (BR), IA, sleep | — | — | 214-440 K (vídeos más vistos en la búsqueda) | El género existe en portugués; **ningún vídeo sobre Galicia** (nicho c, §A.3.2) | [P `../medidas/nicho/busquedas-yt.txt`] |

Casos de ingresos: Adavia Davis (red de 5 canales IA en inglés, 40-60 K$/mes, verificado por Fortune) y el informe
Kapwing (278 canales *slop*, ~117 M$/año) [R `retornos.md` §5] son **en inglés, con RPM de primer nivel y de la ola de
2025**. No son comparables para un canal en galego; sirven para entender por qué YouTube tuvo que **aclarar** cómo aplica
una política que ya existía desde julio de 2025 (§7.1).

### 1.2 Traducción al mercado galego [S sobre F]

- Hablantes: ~46 % de la población habla habitualmente galego, pero **solo el 3,6 % de los mayores de 16 años ve
  audiovisual siempre o sobre todo en galego** (IGE, EEF 2023) [R `audiencia.md` §2].
- Mercado atendible de oyentes habituales estimado en el Gauntlet 1: **2.000-20.000 personas** [R `audiencia.md`].
- Regla gruesa: *Historia Desconocida* opera en un mercado (castellano + inglés traducido) de cientos de millones. Si su
  "vídeo normal" reciente hace 1.300-6.400 vistas, un canal equivalente en galego, sin comunidad previa, debería esperar
  **decenas a pocos cientos de vistas por vídeo**, salvo empuje externo (prensa, TVG, un divulgador que lo comparta) [S].
- Señal que puede romper la regla: canales en galego que el algoritmo sirve a no galegofalantes (VaniMani en galego,
  4,8 M de vistas en 10 meses) [R `audiencia.md` §1]. En audio para dormir, entender cada palabra importa menos. Es una
  **hipótesis a medir** en Analytics (geografía e idioma), no un supuesto del plan.

### 1.3 Escenarios a 12 meses desde la primera publicación (≈ 30 episodios, catálogo ampliado) [S]

Supuestos: catálogo del nicho (b) de §A.2, **mitad historia y mitad Galicia ampliada** (lendas, mar, castros, Camiño,
vida cotiá, idiosincrasia; §8.2), con las lendas siempre presentadas como lenda; 8 episodios semanales y luego 1 cada 2
semanas (§4.2), de ~90 min (60 narrados + 30 de cola); AVD (duración media de visionado) de 15-25 min; conversión a
suscriptor del 1-1,5 % de las vistas; RPM de 1,5-4 € solo dentro del YPP [R `retornos.md` §2.4]; umbral del YPP para
nuevos solicitantes desde el 1-02-2027: **1.000 suscriptores + 8.000 h en 365 días** [F
https://blog.youtube/news-and-events/youtube-partner-program-updates-2027-new-opportunities-earn/]; fan funding con
500 subs + 3.000 h [F https://www.youtube.com/creators/earn/youtube-partner-program/]. Vistas a 12 meses ≈ mediana ×
30 episodios × 1,5 (lo que sigue sumando cada vídeo después del día 30).

| Escenario | Prob. [S] | Qué pasa en la prueba de §A.4 | Vistas por vídeo a 30 días (mediana) | Vistas en 12 meses | Horas vistas | Subs a M12 | YPP | Ingresos 12 meses |
|---|---|---|---|---|---|---|---|---|
| **Pesimista:** el nicho galego no aparece (ni con lendas); o YouTube lo trata como *slop* y no lo recomienda | 50-60 % | PARADA (M < 40) o MÍNIMO bajo | 15-100 | 0,2-4,5 K (con PARADA en la semana 10, el canal se queda en 8 episodios) | 50-1.900 h | 2-70 | No | **0 €** |
| **Base:** hueco en galego + las lendas atraen a quien no busca historia + algún eco en redes galegas | 30-38 % | MÍNIMO o PLAN | 100-600 | 4,5-27 K | 1.100-11.000 h | 45-400 | No (faltan subs) | **0 €** |
| **Optimista:** "a primeira canle para durmir en galego" sale en prensa/TVG, o un vídeo de lendas se dispara | 8-12 % | PLAN | 600-4.000 | 27-180 K | 7-75 K h | 270-2.700 | Posible en M8-M12 **si la revisión de YouTube no lo rechaza** (§7.1) | 0-60 €/mes desde la entrada en YPP; **≈ 0-300 € en el año** |
| *Suplemento multi-audio (nicho c), solo si la fase 2 de §A.4 da R ≥ 1,3* | 40-55 % condicionado a no PARAR | — | ×1,3-2 sobre la fila que toque; el galego conserva el 25-70 % del tiempo de visionado | ×1,3-2 | ×1,3-2 | ×1,3-2 (subs en pt/en) | Adelanta el YPP en el optimista; no cambia el pesimista | Casi igual: el RPM de pt-BR es bajo [S] |

Frente a la v2, el catálogo ampliado mueve ≈ 10 puntos de probabilidad del pesimista al base y al optimista (el único
vídeo de "Galicia para dormir" con > 100 K vistas es de lendas, §A.2). Las vistas totales siguen ≈ 40 % por debajo de
la v1 porque se publican ≈ 30 episodios en vez de 50: es el precio de cumplir D3 (§3.2).

**Valor esperado de ingresos en 12 meses: ≈ 0-25 € [S].** Gasto de caja en 12 meses: ≈ 20-100 € (§2), +10-25 € si
entran las pistas pt/en. **Resultado esperado en caja: ≈ −20 a −120 €**, más ≈ 85-140 h del promotor el primer año
natural (§3), +6-10 h si se construye la etapa multi-audio. En dinero es un hobby con coste, como decidió el promotor
(D6); no hay que venderlo como otra cosa.

**Qué no entra en el modelo y podría cambiarlo:**
- Ayudas y premios en galego (Carballo Interplay: 600 € a la mejor canle; líneas de la SXL a contenidos digitales)
  [R `retornos.md` §7]. **Casi todas exigen un solicitante identificado**, y el canal es anónimo (D6): hay que
  elegir entre anonimato y ayudas. Y un jurado cultural difícilmente premiará un canal sin revisión humana [S].
- Un **canal espejo** en castellano (canal aparte, no pista): donde está la demanda (Relatos al Oído, 108 K). Queda
  fuera: las pistas del mismo vídeo (aprobadas para explorar, §A.3-§A.4) cubren esa demanda sin partir las vistas y
  manteniendo el galego como pista original.
- Spotify Partner Program (España desde el 20-10-2026; 2.000 h en 30 días) [R `retornos.md` §7]: fuera de alcance
  salvo en el optimista.

### 1.4 Retorno no monetario (lo que justifica el hobby) [S]

| Retorno | Cómo se mide | Relevancia para la tesis "pro lingua" |
|---|---|---|
| Pipeline abierto de vídeo en galego con open source (código en `herramientas/pipeline/`) | Repositorio publicable con licencia libre | Alta: reutilizable por concellos, docentes, divulgadores |
| **Informes de errores para Nós** (pronunciaciones que falla StyleTTS2/Cotovía, errores que marca el ASR, léxico) | Nº de entradas de léxico/errores reportados por trimestre | Alta: es la contribución más limpia y valorada (datos de fallo reales) |
| Conjunto de evaluación: pares "texto generado → error detectado → corrección" (de controles y de comentarios) | Nº de pares con licencia abierta | Alta, **si se publica marcado como sintético** (§8.3) |
| Contexto curado para IAs en galego: fichas de episodio con fuentes, glosario de topónimos, cronología | Nº de fichas con fuente | Media-alta |
| Horas de escucha en galego | Horas vistas | Media: pequeño en absoluto |

---

## 2. Costes: casi cero

### 2.1 Cómputo propio frente a APIs, por etapa

| Etapa | Opción propia (open source) | Coste | Opción API | Coste por episodio de 60 min narrados | Elección |
|---|---|---|---|---|---|
| Guion (≈ 7.000 palabras) | LLM de Nós en CPU: `Llama-3.1-Carballo-Instr3` (8B) o `Carvalho-Salamandra-Instruct` (7B), cuantizado con llama.cpp [F https://huggingface.co/proxectonos/Llama-3.1-Carballo-Instr3] | 0 €; ≈ 2-4 h de CPU por pase [S] | LLM frontier (p. ej. Claude) | ≈ 1-2 USD (proporcional a los ≈ 3 USD optimizados del episodio de 2 h) [R `pipeline.md` §5.1] | **API frontier para redactar** (el Gauntlet 1 concluyó que los modelos de 7-8B van por detrás en redacción larga [R `voz_guion.md`]); **modelos de Nós como segundo corrector y juez** (ver §5). Probar Carballo como redactor en el piloto: si su galego gana, cambia a 0 € |
| Voz | StyleTTS2 Brais de Nós (Apache-2.0) en CPU | 0 €; 0,76-1,15 s de reloj por s narrado en el pipeline, con pausas y carga (§4.1) [P] | ElevenLabs/Azure | 3-4 USD [R] | **Propia** (D2: la voz más cercana al listón) |
| Control ASR | whisper-large-v3-turbo-gl de Nós, int8, por párrafo | 0 €; RTF 0,20 sobre 16 min (WER 1,5 %) [P, `../medidas/escala/`] | — | — | Propia |
| Imágenes (≈ 200-240 por episodio) | SDXL-Turbo o SD-Turbo en CPU + reescalado | 0 € | Nano Banana 2 Lite batch | ≈ 7-8 USD (0,034 USD × 220) [R `pipeline.md` §5.2] | **Propia**. Licencia: ver §2.3 |
| Montaje (Ken Burns lento, fundidos, cola) | ffmpeg (`imageio-ffmpeg`) | 0 € | — | — | Propia |
| Juez factual de otra familia | LLM abierto local o capa gratuita de otra API | 0-0,2 USD | — | — | Local si cabe en el tiempo de CPU |
| Pistas pt/en/es (solo desde la fase 2 de §A.4) | Nós MT gl→es/en (MIT) + Kokoro (Apache-2.0) o Piper; control M1-M6 | 0 €; 30-130 min de CPU por idioma [P/S, §A.3.3], en una segunda noche | LLM frontier para gl→pt (Nós no tiene ese par) | ≈ 0,3-1 USD | **Propia salvo gl→pt** |

### 2.2 Caja mensual (2-5 episodios/mes) [S sobre F/R]

| Partida | €/mes | Nota |
|---|---|---|
| LLM de redacción y extracción del dossier por API | 2-9 € | 2-5 × 1-2 USD (el dossier añade ≈ 0,1 USD); 0 € si se usa un LLM abierto o si la suscripción que ya tiene el promotor cubre el uso [S: comprobar los términos de uso automatizado] |
| Electricidad de la CPU propia | 0,2-1 € | 2-5 episodios × 5-7 h (§4.1) ≈ 10-35 h/mes a 60-100 W ≈ 0,6-3,5 kWh × 0,15-0,25 €/kWh [S] |
| Servidor alquilado (solo si el PC del promotor no puede quedarse encendido de noche) | 0 € (por defecto) / 10-30 € | VPS de 4-8 vCPU y 16 GB [S: precio sin verificar hoy] |
| Música/ambiente | 0 € | Ambiente generado o grabado propio; nada con Content ID |
| Validación de voz (D1) | 0 € | Solo tras la puerta P3 (§9): 850-1.500 € una vez |
| **Total** | **≈ 3-10 €/mes (≈ 1 € con LLM abierto)** | Frente a los ~305 €/episodio de la garantía humana del plan v1 (D5) |

### 2.3 Licencias del stack (condición de publicación)

| Componente | Licencia | ¿Uso en canal monetizado? |
|---|---|---|
| StyleTTS2 Brais (modelo) | Apache-2.0 [R `voz_guion.md` §1.1] | El modelo sí. **La voz de la persona no está cubierta por Apache**: los datos de Brais son "solely for research purposes", y hay derecho a la propia voz (LO 1/1982, art. 7.6) [R `gtm_riesgos.md` §3.3 bis]. Por eso D4 (pedir permiso a Nós/USC) es condición para **monetizar**, no un gesto (§9) |
| Whisper-gl de Nós | Apache-2.0 [R] | Sí (uso interno) |
| SDXL-Turbo / SD-Turbo | La ficha de Hugging Face dice licencia `sai-nc-community` y remite a stability.ai para uso comercial [F https://huggingface.co/stabilityai/sdxl-turbo]; la página de licencias de Stability incluye SDXL Turbo en la **Community License**, gratuita para quien facture < 1 M$ al año [F https://stability.ai/license] | Sí, dentro de la Community License [S: verificar si exige registro y conservar copia de los términos en el expediente] |
| FLUX.1 [schnell] | Apache-2.0 [S, verificar ficha] | Sí, pero 12B parámetros: en 4 núcleos de CPU, minutos por imagen [S] → inviable para 200 imágenes por episodio |
| FLUX.1 [dev] | No comercial [R `gtm_riesgos.md` §3.4] | **No** |
| LLM de Nós (Carballo, Llama 3.1) | Licencia Llama 3.1 [R] | Sí, con atribución |

---

## 3. Horas (D3)

### 3.1 Construcción del MVP a ~6 h/semana [S, con las partes medidas marcadas]

Parte del trabajo ya existe y está medido (§4.1): el código de `herramientas/pipeline/` (8 etapas propias, que el
diseño de §5.1 reparte en 9) produce un vídeo de 3,4-4 min de extremo a extremo, y `dossier.py` saca un dossier con
citas comprobadas (§3.3). Lo que falta es escalarlo a 60 min, H2 y los controles pendientes (§5.1).

| Bloque | Horas | Qué deja hecho |
|---|---|---|
| Orquestador y cola local (`pipeline.py`, `jobs/`, reanudación) | 5-7 | Un comando por episodio, reanudable tras un corte |
| Guion: escaleta + redacción por capítulos + reglas de densidad para dormir y embudo de ganchos al inicio | 8-10 | `guion.md` + `afirmacions.csv` |
| Cinturón lingüístico automático (Hunspell-gl, LanguageTool-gl, lista de castellanismos, LLM corrector de otra familia) | 5-7 | `qa_texto.json` |
| Verificación de afirmaciones: H2 (juez LLM de otra familia sobre `afirmacions.csv`) y conjunto nuevo de canarios | 6-8 | `qa_historia.json`; C0 ≥ 80 % en un conjunto nuevo (§6.1) |
| Voz + QA de audio (falta: ASR por párrafo y regeneración ×3) | 3-4 | `voz.wav` + `qa_audio.json` |
| Imágenes: plan de planos, lista de anacronismos, filtros I1-I3 | 6-8 | `planos/*.png` + `qa_imaxe.json` |
| Montaje por tramos (sin cargar las ≈ 270 imágenes en RAM) + miniatura + metadatos + subtítulos | 4-6 | `episodio.mp4`, `miniatura.png`, `metadatos.json` |
| Canarios C0 dentro del pipeline y panel de calidad | 3-4 | Tasa de detección por episodio |
| Piloto completo de 60 min + ajustes | 5-8 | 1 episodio publicable; criterio P0-a (§9): 60 min sin intervención en ≤ 8 h |
| `dossier.py`: falta PDF, fuentes no Wikipedia y calibrar el prompt (la parte medida ya existe, §3.3) | 3-5 | Dossier de 80-140 hechos por episodio |
| Escalar el código de 3,5 a 60 min (guion por capítulos, ASR por párrafo) | 5-8 | Sin cambios manuales entre etapas |
| Stock de 8 dossieres antes de publicar (8 × 25-75 min, §3.3) | 4-10 | Los 8 episodios semanales del arranque |
| **Total** | **≈ 57-85 h** | **≈ 10-14 semanas a 6 h/semana**. Es la única cifra del plan (§0 y §9 remiten aquí) |

### 3.2 Régimen estable (D3: ~1 h/semana)

Tareas fijas (no dependen de cuántos episodios salgan):

| Tarea semanal | Min | Nota |
|---|---|---|
| Lanzar la tanda (o nada, si va por cron) | 0-5 | |
| Mirar el semáforo de controles (no es revisión del contenido: solo verde/rojo) | 5 | Si está rojo, el episodio no sale |
| Comentarios: erratas señaladas → fichero de erratas → comentario fijado | 10-20 | **Con tope**: si hay más, se atienden en la semana sin episodio. Es la única "revisión humana", y es posterior a publicar |
| Mantenimiento (actualizaciones, fallos) | 10-15 | Promedio; habrá semanas de 0 y semanas de 2 h |
| **Subtotal fijo** | **25-45** | |

Tareas por episodio:

| Tarea | Min | Nota |
|---|---|---|
| **Subir o pasar a público** | 5-10 | La API de YouTube deja **privados** los vídeos subidos desde proyectos no auditados [F https://developers.google.com/youtube/v3/docs/videos/insert]: subida por API en privado y un clic en Studio |
| **Dossier** (elegir fuentes y leer el informe de `dossier.py`) | 25-75 | Medido en volumen en §3.3 |
| **Subtotal por episodio** | **30-85** | |

| Cadencia | Min/semana | ¿Cumple D3? |
|---|---|---|
| 1/semana con dossier del stock (primeros 8 episodios) | 30-55 | Sí |
| 1/semana con dossier nuevo | 55-130 (centro ≈ 90) | **No** |
| **1 cada 2 semanas con dossier nuevo** (régimen tras el stock) | **40-87 (centro ≈ 60)** | **Sí en el centro**; en el extremo alto se pasa ≈ 45 % |
| 1 cada 2 semanas reutilizando el dossier en una serie de 2 episodios [S: ahorra ≈ 1/3 del dossier] | 36-75 | Sí |

**Regla para cumplir D3:** el promotor apunta los minutos reales (una línea por semana en `jobs/horas.csv`). Si la
media de 4 semanas pasa de 70 min, se aplica la palanca siguiente, en este orden: (1) series de 2 episodios sobre un
mismo dossier ampliado (el control P1 vigila que no se repitan frases); (2) 1 episodio cada 3 semanas; (3) pausa. Nunca
se amplían horas. A 1 episodio cada 2 semanas el canal publica ≈ 30 episodios el primer año (§1.3).

**Riesgo de horas:** si un error llamativo se hace viral en redes galegas, la gestión se come varias semanas de
presupuesto de golpe [S]. Regla: ante un incidente, pausar la publicación en vez de ampliar horas (§10, alarma A3).

### 3.3 El dossier semimanual, medido (29-09-2026)

**Por qué es la parte cara.** Es la única etapa que pide a una persona en cada episodio: elegir fuentes admisibles
(§5.2) no se puede dejar a un LLM sin revisión, porque todo lo que viene después (H1, H2) solo comprueba coherencia
con el dossier.

**Prueba real.** Se hizo un dossier nuevo para un tema de la lista cerrada (§8.2), el mosteiro de Samos, con el código
nuevo `herramientas/pipeline/dossier.py` y el prompt `prompts/dossier.md`. Todo está en
`herramientas/pipeline/dossier/samos/` (fuentes descargadas, hechos, informe, `cronometro.md`).

| Paso | Quién | Medido | Min |
|---|---|---|---|
| 1 Buscar fuentes (API de búsqueda de Galipedia) y elegir 4 (3 gl + 1 es) | persona | 10 resultados; el artículo principal tiene 865 palabras | [S] 10-20 |
| 2 Descargar y limpiar (`dossier.py fontes`) | máquina | 13,6 y 16,0 s; 2.852 palabras de fuente [P] | 0,3 |
| 3 Extraer hechos con cita literal (LLM) | máquina | 45 hechos [P]; tiempo por API [S] | 1-3 |
| 4 Comprobar citas por código (`dossier.py comprobar`) | máquina | 0,02 s; 45/45 citas encontradas; **2 fuera por conflicto entre fuentes** (exclaustración en 1835 según Galipedia y en 1836 según la Wikipedia en castellano); 3 marcados como leyenda; prueba negativa con 3 citas falsas: 0/3 aceptadas [P] | 0 |
| 5 Leer el informe (rechazados, conflictos, leyendas; no los 43 hechos) | persona | ≈ 120 palabras [P] | [S] 2-5 |
| **Por dossier de 4 fuentes** | | **43 hechos usables, 611 palabras** | **≈ 15-30, de ellos 12-25 de persona** |

Qué es medida y qué no: los pasos de máquina y el volumen que la persona tiene que leer están medidos [P]; los
minutos de persona (pasos 1 y 5) son un supuesto [S] a partir de ese volumen, porque la prueba la hizo un agente, no
el promotor. **Condición de P0 (§9): el promotor cronometra los 3 primeros dossieres del stock** y la tabla de §3.2
se rehace con su medida.

**Escala a un episodio de 60 min [S sobre P].** El vídeo de ejemplo usa 18 hechos para 475 palabras (≈ 26 palabras de
guion por hecho) y la voz va a 124-143 palabras/min [P, `../medidas/r2-*/qa.json`]: 60 min son ≈ 7.400-8.600 palabras.
Con el embudo (2 min densos y luego ritmo de dormir, 1 hecho cada 60-100 palabras [S]) salen **≈ 80-140 hechos por
episodio: 2-3 dossieres como el de Samos**, es decir, 8-12 fuentes. Consecuencias:
- **Minutos de persona por episodio: ≈ 25-75** (12-25 × 2-3). Es el dato que usa §3.2.
- **Galipedia sola no llega:** para Samos da 43 hechos en total. Los temas del primer año necesitan fuentes largas
  con licencia abierta (artículos de acceso abierto de historiadores, como los de Carlos Barros que usa el dossier de
  irmandiños, o PDF oficiales), que tardan más en encontrarse. Los temas con poca fuente se hacen de 40 min narrados
  (con más cola) en vez de forzar datos.
- **Los conflictos entre fuentes aparecen incluso en temas tranquilos** (1835/1836 en la primera prueba): el código
  los saca del dossier, y así el guion no puede usar el dato.

## 4. Cadencia sostenible

### 4.1 Tiempo de máquina por episodio (60 min narrados + 30 de cola) en la CPU de 4 núcleos

Medido en las dos ejecuciones reales del pipeline (29-09-2026) y en una prueba de ASR sobre 16 min, y extrapolado por
unidad de escala con `../medidas/escala/extrapolacion.py` (salida en `extrapolacion.md`). Imágenes: 255-287 (una cada
14-16 s en la parte narrada, como en el vídeo de ejemplo, y una por minuto en la cola [S]).

| Paso | Medido [P] | Min de reloj para 60 + 30 min |
|---|---|---|
| Guion y escenas por API (con vueltas de control) | — | 20-60 [S] |
| Corrección (LanguageTool) | 14-20 s para 475 palabras | 4-6 |
| Voz (StyleTTS2 Brais, frase a frase, con pausas y carga del modelo) | 223 y 248 s para 193 y 231 s narrados: **0,76-1,15 s de reloj por s narrado** | **47-69** |
| Imágenes (SDXL-Turbo, 4 pasos, 1024×576) | 12,1-25,4 s por imagen (media 16,2-19,8 s); carga del modelo 24-331 s | **69-100** |
| Sonido (lluvia y mezcla) | 5,0-5,2 s | 2 |
| Montaje (Ken Burns, niebla, x264) | 1,28-1,40 s de reloj por s de vídeo | **115-126** (solo con la carga de imágenes por tramos, §5.1) |
| QA (ASR sobre mezcla y voz, LanguageTool, `ebur128`, hoja de contactos) | ASR sobre 16 min: RTF 0,20, WER 1,5 % | 29-42 |
| **Subtotal sin LLM** | | **266-346 min = 4,4-5,8 h** |
| Canarios C0 sobre el guion entero (20 inyecciones) | 52,6-55,8 s para 475 palabras | ≈ 14 [S: lineal con las palabras] |
| **Total** | | **≈ 5,0-7,0 h: una noche** |

La cifra de la v1 (voz con RTF 0,28-0,4 → 17-25 min) medía la síntesis sola en un banco de pruebas; en el pipeline,
con las pausas para dormir, la carga del modelo y la escritura frase a frase, la voz tarda 2-3 veces más.

### 4.2 Recomendación

- **Arranque:** 3 episodios en la primera semana (catálogo mínimo para que el algoritmo tenga qué encadenar). La
  referencia concentró sus 3 éxitos en una ráfaga de 8 vídeos en 10 días [F, `../referencia.md`]; aquí se copia la
  idea, no la escala. Luego 1/semana hasta publicar los 8 del stock (P1).
- **Régimen:** **1 episodio cada 2 semanas**, siempre el mismo día y hora (domingo por la noche [S]), porque es lo que
  cabe en D3 (§3.2). Techo: 1 por semana, solo si el registro de horas lo permite. La máquina daría para uno diario.
- **Nunca diario.** No por falta de máquina, sino porque: (a) la política de monetización excluye el contenido que
  da "the impression of mass production" y el de "minimal variation across videos" [F
  https://support.google.com/youtube/answer/1311392?hl=en]; que un canal automático suba a diario refuerza esa
  impresión es una **inferencia propia [S]**, no algo que diga la política ni la nota de TubeFilter; (b) el público
  galego no es una bolsa que se agote a diario; (c) más episodios = más errores publicados sin filtro; (d) D3.
- **Duración:** 60 min narrados + 20-30 min de cola de ambiente (imagen lenta, sin voz); 40 min narrados si el tema
  tiene poca fuente (§3.3). Experimento a partir del episodio 10: alternar 60 y 90 min narrados para medir AVD por
  duración [S], solo si hay dossier para ello.
- **Sin bucles ni directos 24/7 ni recopilaciones** hasta tener > 50 episodios; y entonces, con narración nueva.

---

## 5. Arquitectura del pipeline

### 5.1 Vista general

```
temas.csv (lista cerrada, §8.2)
   │
[1] Fuentes ──► dossier/ (SEMIMANUAL: el promotor elige 8-12 fuentes; un LLM extrae hechos con cita; dossier.py
   │   comprueba cada cita literal y aparta conflictos y leyendas; §3.3)
   │
[2] Escaleta (LLM A) ──► escaleta.json (actos, lugares, densidades para dormir)
   │
[3] Guion (LLM A, por capítulos, solo con el dossier en contexto) ──► guion.md + afirmacions.csv
   │                                                     (cada frase con dato → id de fragmento + cita literal)
[4] Cinturón lingüístico ──► guion_v2.md + qa_texto.json          ◄── LLM B (otra familia) + Carballo/GEC de Nós
   │                                                                     solo corrige lo marcado; no toca datos
[5] Verificación histórica ──► qa_historia.json                     ◄── extracción de citas + juez LLM C
   │   (si falla: se BORRA la frase, no se suaviza; si falla > 10 %: el episodio no sale)
[6] Voz (StyleTTS2 Brais, CPU) ──► voz.wav + tempos.json
   │
[7] QA de audio (ASR Whisper-gl por párrafo, WER, sonoridad, silencios, tartamudeos) ──► regenerar ×3 o bloquear
   │
[8] Imágenes (plan de planos del guion → prompts con estilo fijo y lista negra de anacronismos → SDXL-Turbo
   │   → filtros: seguridad, texto ilegible, duplicados, coherencia prompt-imagen) ──► planos/
   │
[9] Montaje + miniatura + subtítulos gl + metadatos + expediente ──► saída/ (privado)
   │
[10] (opcional, desde la fase 2 de §A.4) Pistas pt/en: traducción → TTS → M1-M6 → pistas .m4a (segunda noche; subida a mano en Studio)
   │
Semáforo: 14 controles (§6). Todo verde → subida en privado → 1 clic del promotor → público.
Rojo → no sale; se registra el motivo; el episodio siguiente de la cola ocupa su lugar.
```

**Qué existe de verdad el 29-09-2026** (código en `herramientas/pipeline/`, ejecutado de extremo a extremo; §4.1):

| Etapa del diagrama | Estado en el código | Diferencia con el diseño |
|---|---|---|
| [1] Fuentes → dossier | El dossier del vídeo de ejemplo (`temas/irmandinos-apertura.yaml`, 18 hechos, 8 fuentes) se escribió a mano desde las notas del guion muestra. **Nuevo en la ronda 2:** `dossier.py` (descarga, limpieza, comprobación literal de citas, conflictos, leyendas), probado con Samos: 45 hechos en 16 s de máquina (§3.3) | Falta leer PDF y fuentes que no son Wikipedia, y conectar su salida con `pipeline.py` sin copiarla a mano |
| [2]-[3] Escaleta y guion | Un solo prompt (`prompts/guion.md`) que escribe un fragmento de ≈ 440 palabras; sin escaleta ni capítulos; sin `afirmacions.csv` | Para 60 min hay que trocear en capítulos (≈ 12-14 llamadas) |
| [4] Cinturón lingüístico | LanguageTool gl-ES + hunspell y una vuelta de corrección por LLM. No hay lista de castellanismos propia ni LLM B de otra familia | T3 y la parte de LLM B de T2 sin hacer |
| [5] Verificación histórica | **Solo H1-léxico** (`ancoraxe.py`): nombres propios y cantidades del guion deben estar en el dossier, por palabra entera (corregido en la ronda 2) y ahora como puerta de `pipeline.py`. H2 (juez LLM) no existe | C0 medido: 70 % → 80 % (§6.1) |
| [6]-[7] Voz y QA de audio | StyleTTS2 Brais frase a frase; ASR Whisper-gl sobre el audio **entero**, sin regeneración; puerta WER ≤ 6 % sobre la mezcla | El Gauntlet 1 vio alucinar a Whisper sobre audio largo (WER 48-53 % en 6,6 min) [R `pipeline.md` §4.1.1]; con el Whisper-gl de Nós la prueba de escala dio WER 1,5 % en 16 min [P, `../medidas/escala/asr_longo_x4.json`]; la de 60 min no llegó a terminar. Se mantiene el diseño por párrafo (pendiente, 1-2 h) |
| [8] Imágenes | SDXL-Turbo, 4 pasos, 1024×576, 1 imagen por escena; controles solo informativos (luminancia, contraste, similitud) | I1 (NSFW), I2 (OCR) e I3 entre episodios no existen |
| [9] Montaje | Ken Burns + niebla + fundidos + subtítulos; carga **todas** las imágenes reescaladas en memoria en cada uno de los 4 procesos | A 270 imágenes serían ≈ 10 GB de RAM (270 × 9,7 MB × 4): hay que cargarlas por tramo antes de pasar de ≈ 60 imágenes (cambio pendiente; los 115-126 min de §4.1 lo suponen hecho) |
| Semáforo | 10 puertas en `pipeline.py` (`UMBRAIS` y `portas`): duración, WER, sincronía A/V y de subtítulos, LanguageTool, **H1**, estilo, sonoridad, peso, resolución. Umbrales alineados con §6.1 en la ronda 2 (WER 0,25 → 0,06; sonoridad −24/−18 → −18/−16 LUFS) | P1, C0 dentro del pipeline, H2, I1-I3, T3, T5 pendientes. Hoy hay 6 de los 14 controles, varios en versión parcial: T1, T2 (sin LLM B), T4 (parcial), H1 (léxico), A1 (sobre la mezcla, no por párrafo), A2 (solo sonoridad) |

- **Todo reanudable e idempotente**: cola en disco local, trabajos con hash de contenido (diseño de
  `../../gauntlet/piezas/pipeline.md` §4.1.1 c, reutilizado tal cual).
- **Tres LLMs distintos** (redactor A, corrector B, juez C) para que un error no se "autoapruebe": un modelo tiende a
  dar por buenos sus propios errores [S, práctica habitual].
- **El expediente de cada episodio** (dossier, versiones, informes de QA, semillas, hashes, licencias) va a git: es la
  prueba ante YouTube si hay que apelar y la base del informe a Nós.

### 5.2 Decisión de diseño clave: el guion solo puede decir lo que está en el dossier

Sin historiador, la única defensa razonable contra la alucinación es **cerrar el mundo**: el redactor recibe solo
fragmentos de fuentes y cada frase con fecha, nombre, cifra o hecho debe llevar el id del fragmento y una cita literal
que lo respalde. Lo que no se puede anclar se borra. Consecuencia: el guion será más pobre en anécdota y más
repetitivo con las fuentes; se acepta a cambio de menos invenciones.

Fuentes admisibles [R `gtm_riesgos.md` §3.4]: Galipedia (CC BY-SA, como esqueleto), obras en dominio público
(contrastadas: historiografía romántica superada), documentos y artículos con licencia abierta. **No** entran en el
dossier textos del Consello da Cultura Galega ni obras protegidas (solo verificación manual, que aquí no hay).

---

## 6. Controles automáticos que sustituyen a la revisión humana

### 6.1 Los 14 controles, con umbral y qué detectan

| # | Control | Herramienta | Umbral de bloqueo [S, calibrar en el piloto] | Qué detecta bien |
|---|---|---|---|---|
| T1 | Ortografía | Hunspell-gl | 0 palabras desconocidas fuera de la lista de nombres propios del dossier | Erratas, formas no normativas comunes |
| T2 | Gramática | LanguageTool gl-ES (sin mantenedor desde 2019 [R]) + CarvalhoChat_GEC de Nós (cuando se conceda el acceso) | Toda propuesta aceptada o rechazada con motivo por el LLM B; 0 abiertas | Concordancias, colocación del pronombre átono en casos típicos |
| T3 | Castellanismos | Lista negra propia (del DRAG y VOLGa; se amplía con cada errata) | 0 apariciones | Los castellanismos conocidos (p. ej. los que el tribunal cazó: "apagado" como sustantivo, "polo de agora") [R `tribunal.md`] |
| T4 | Densidad para dormir | Script: nombres propios nuevos/min, fechas y cifras por bloque, frases largas | Entrada ≤ 1 fecha y ≤ 2 nombres; actos ≤ 3 nombres nuevos/min [R `tribunal.md`, ronda 1] | Guion que despierta en vez de adormecer |
| T5 | Salud y tono | Regex + LLM B | 0 afirmaciones terapéuticas ("cura", "insomnio", "tratamento"); 0 preguntas retóricas de *shock* | Categoría 3 de YouTube (personas IA en salud) y categoría 2 (manipulación) |
| H1 | Anclaje de afirmaciones | `afirmacions.csv` + comprobación de que la cita literal existe en el fragmento | ≥ 95 % de frases con dato ancladas; las no ancladas se borran | Invenciones "sin fuente" |
| H2 | Coherencia con la cita | LLM C (otra familia) juzga "la frase dice lo mismo que la cita" | ≤ 5 % de "no respaldado"; si > 10 %, el episodio no sale | Fechas cambiadas, personajes mezclados, exageraciones |
| H3 | Temas vetados | Lista cerrada de temas (§8.2) + detector de palabras de zona roja | 0 | Guerra Civil, represión, política reciente, conflictos vivos |
| H4 | Lenda como lenda (nuevo en v3, por el catálogo ampliado) | `afirmacions.csv` (tipo `lenda`) + regex de marcadores + pregunta al juez H2 | 0 frases `lenda` fuera de un bloque con marcador; 0 frases `feito` que la fuente trata como leyenda | Mouras, Santa Compaña o raqueiros contados como hechos |
| A1 | Inteligibilidad | ASR Whisper-gl por párrafo, normalizado con Cotovía, WER | ≤ 6 % por párrafo tras 3 regeneraciones [R `pipeline.md` §4.1.1 a]. **En el código:** WER ≤ 0,06 sobre la mezcla entera (medido: 2,3 % y 2,5 %; la voz sola da 8,2-8,6 %, por eso aún no es puerta) | Palabras comidas, cambiadas, tartamudeos, "alucinaciones" del TTS |
| A2 | Técnica de audio | ffmpeg `ebur128`, `silencedetect`, recortes | −18 a −16 LUFS integrados; sin silencios > 8 s en la parte narrada; 0 recortes. **En el código:** solo la sonoridad; la mezcla apunta ahora a −17 LUFS (`son.py`, antes −20). **El `video/ejemplo.mp4` actual mide −20,0 LUFS y no pasa A2**; con +3 dB mide −17,0 [P, ffmpeg `ebur128`] y el pico real pasa de −5,1 a ≈ −2,1 dBTP: hay que rehacer las etapas 6-8 antes de P0 | Saltos de volumen que despiertan, cortes |
| I1 | Seguridad de imagen | Clasificador NSFW | 0 positivos | Desnudos, violencia gráfica |
| I2 | Texto en imagen | OCR (Tesseract) | 0 textos detectados con confianza > umbral | Letras inventadas y rótulos ilegibles, típicos de la IA |
| I3 | Duplicados y variedad | *Hash* perceptual + similitud entre episodios | ≤ 10 % de planos casi iguales; ≤ 5 % reutilizados de otros episodios | "Plantilla repetitiva" (política de YouTube) |
| P1 | Variedad entre episodios | Coseno de *embeddings* de guiones + n-gramas compartidos | Coseno < 0,85 y < 2 % de 8-gramas compartidos con cualquier episodio anterior [R `pipeline.md` §8] | Contenido "intercambiable" |

Con pistas de audio extra se suman **M1-M6** (control de la traducción, §A.3.4), que solo bloquean la pista afectada, no el episodio en galego.

Más un control transversal: **C0, errores canario.** En cada ejecución se inyectan en una copia del guion 20 errores
conocidos (5 castellanismos, 5 fechas cambiadas, 5 nombres intercambiados, 5 frases sin fuente) y se mide cuántos
detecta la cadena. **Si detecta < 80 %, el pipeline no publica ese día** (algo se ha roto). La tasa histórica de
detección se publica en la página de erratas.

**C0 medido (29-09-2026, guion del vídeo de ejemplo, `herramientas/pipeline/canarios.py`)** con los controles que
existen en el código (LanguageTool + hunspell, H1-léxico, estilo):

| Familia | Ronda 1 [P, `../medidas/c0-irmandinos-apertura/`] | Ronda 2, tras corregir H1 [P, `../medidas/c0-irmandinos-apertura-r3/`] | Qué falla todavía |
|---|---|---|---|
| Castellanismos | 5/5 | 5/5 | — |
| Fechas y cantidades | 3/5 | **5/5** | — |
| Nombres cambiados | 4/5 | 4/5 | Lemos y Andrade intercambiados: los dos están en el dossier |
| Frases sin fuente | **2/5** | **2/5** | Invenciones sin nombre ni cifra ("gardaba alí un tesouro de moedas de ouro", "a última pedra caeu nunha noite de lúa chea", "a revolta máis grande de toda Europa") |
| **Total** | **14/20 = 70 %: no pasa P0** | **16/20 = 80 %: en el umbral** | Falsos positivos de base: 2 en ambas |

- **Qué se corrigió:** H1 buscaba cada cantidad del guion como subcadena del dossier, así que "dous" (dous séculos) se
  daba por anclado dentro de "douscentas" y "cen" (cen anos) dentro de "cincocentos". Ahora compara palabras enteras
  (`ancoraxe.py`). No añadió falsos positivos en el guion limpio. H1 pasa además a ser puerta de `pipeline.py`.
- **Por qué el 80 % no basta todavía:** se alcanza en el mismo conjunto de 20 canarios que sirvió para encontrar el
  fallo (riesgo de ajustar el control al examen) y deja las invenciones "sin fuente" en 2/5, que es justo el error
  más dañino sin historiador.
- **Qué lo sube, y cómo se mide:** **H2**, un juez LLM de otra familia que recibe cada frase del guion con los hechos
  del dossier y responde "respaldada / no respaldada". Es el único control que puede ver una invención sin nombre ni
  cifra y un cambio de papeles entre dos nombres del dossier. Objetivo medible: **≥ 4/5 en "sin fuente" y ≥ 90 % en
  total** en este conjunto, **y ≥ 80 % en un segundo conjunto de 20 canarios nuevo** escrito para otro tema (Samos, con
  su dossier de §3.3) sin mirar los resultados antes. Se mide también su coste: falsos positivos en los dos guiones
  limpios (umbral: ≤ 1 frase de cada 50 marcada sin motivo) [S].
- **Hoy, P0 no se da por pasada** en el punto de los canarios (§9).

### 6.2 Coherencia visual (sin control fiable, solo mitigación)

- Estilo fijo por serie (paleta ámbar de vela, óleo de época fotorrealista, plano medio-general): prompt base
  constante + semilla por personaje [S].
- Lista negra de anacronismos en el prompt negativo (pelucas empolvadas, uniformes modernos, luz eléctrica,
  fuegos artificiales, vidrio moderno) derivada de los fallos de la referencia [F, `../referencia.md` §3].
- Personajes con nombre: **evitar caras reconocibles** de personajes históricos (de espaldas, a contraluz, en grupo);
  así el cambio de cara entre planos importa menos y baja el riesgo de "deepfake" de persona real.
- CLIP score prompt-imagen como filtro débil (descarta imágenes que no tienen nada que ver con el prompt) [S].

### 6.3 Lo que los controles NO detectan (lectura honesta)

| Punto ciego | Por qué no se detecta | Consecuencia esperable | Mitigación parcial |
|---|---|---|---|
| **Error histórico fluido respaldado por una fuente mala** | H1-H2 comprueban coherencia con el dossier, no la verdad; si Galipedia o un clásico del s. XIX se equivoca, el error pasa | Mitos románticos presentados como hechos (Murguía, Vicetto) | Fuentes de dominio público solo para "ambiente"; datos duros solo de fuentes modernas; lista de mitos conocidos como vetados |
| **Selección y énfasis sesgados** | Ningún control mide qué se omite | Relato plano o con sesgo identitario | Temas "canónicos" con consenso (§8.2) |
| **Castellanismos y usos no normativos sutiles** | Solo se detecta lo que está en las listas o en LanguageTool (desactualizado) | Varios por episodio [S]; en el Gauntlet 1 el tribunal encontró 3-4 en ~800 palabras ya revisadas | Lista viva de castellanismos que crece con cada errata; LLM B especializado; GEC de Nós |
| **Prosodia errónea que el ASR entiende igual** | El ASR es robusto: *porto* con /o/ abierta o cerrada se transcribe igual; un acento mal puesto no sube el WER | Vocales abiertas/cerradas mal dichas, entonación rara: lo primero que nota un galegofalante | Léxico de corrección de Cotovía (`g2p_override`, [R `pipeline.md` §3.5.3]) alimentado por erratas; **es justo lo que mide la validación de voz de D1** |
| **Anacronismo o error visual** | Ningún detector sabe que un hórreo no va en un palacio del s. XV | Imágenes "de postal" equivocadas | Lista negra; estilo evocativo más que documental |
| **Tono inadecuado** (romantizar violencia, frivolizar) | Juicio cultural | Crítica pública | Temas cerrados; regla de tono en el prompt; T5 |
| **Errores del propio control** (falsos negativos del LLM juez) | El juez también alucina | Una fracción de errores sale | Canarios C0 para medir la tasa |

**Estimación de residuos por episodio de 60 min** [S, sin medir; lo medirá el piloto con C0 y una revisión experta
puntual de un solo episodio, si alguien la ofrece gratis]:
- 3-10 errores de lengua visibles para un filólogo;
- 1-4 imprecisiones históricas que un historiador señalaría;
- decenas de detalles de prosodia mejorables.

**Esto significa que el canal publicará errores cada semana.** La defensa no es negarlo, es declararlo (§7.3) y
corregirlo rápido (erratas en ≤ 7 días en el comentario fijado y la descripción) [S].

---

## 7. Riesgos de plataforma y regulación

### 7.1 Política de YouTube de contenido inauténtico

**Qué dice:**
- Desde el 15-07-2025: no monetizable el "AI-generated content made with generic or unoriginal templates giving the
  impression of mass production **without adding the creator's original, authentic insights or perspective**" y el
  "similar or repetitive content with low educational value, commentary, narratives, or minimal variation across
  videos". Permitido: misma intro y outro con "distinct storyline, focus, or concept" [F https://support.google.com/youtube/answer/1311392?hl=en].
- Aclaración del 13-07-2026 (TubeFilter) / 16-07-2026 (TechCrunch). **No es una norma nueva ni un endurecimiento**: la
  propia nota dice que aclara la política existente, y el contenido afectado ya estaba excluido de la monetización
  desde el 15-07-2025. Lo nuevo es el detalle, en tres categorías: (1) genérico o repetitivo,
  con ejemplos como **"image slideshows and templated storylines"**; (2) contenido que busca impactar o manipular;
  (3) personas IA como expertos en salud, legal, finanzas o política. **Se aplica a nivel de canal** [F
  https://www.tubefilter.com/2026/07/13/youtube-inauthentic-content-monetization-policy-update/ ;
  https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/].
- Aplicación real: 16 canales de *slop* cerrados o vaciados en enero de 2026 (35 M de suscriptores); un canal de
  historias bíblicas con 588 K suscriptores desmonetizado por "inauthentic and mass-produced content" [F
  https://outlierkit.com/resources/youtube-ai-slop-crackdown-2026/ ; resumen de búsqueda].

**Por qué nos toca de lleno:** el canal es exactamente "presentación de imágenes + voz IA + plantilla de episodio",
sin revisión humana y **declarado como tal** (§7.3). A diferencia del plan v1, aquí no hay "perspectiva original del
creador" que mostrar más allá de la selección de temas y fuentes.

| Riesgo | Prob. [S] | Impacto | Mitigación |
|---|---|---|---|
| Solicitud al YPP rechazada por contenido inauténtico | 40-60 % si se llega a solicitar [S puro: **no** se apoya en casos comparables documentados de canales de voz IA + imágenes admitidos o rechazados en 2026; no se han encontrado datos públicos fiables, solo anécdotas de foros. Se deja como supuesto a sustituir por el resultado real si se solicita] | Sin anuncios ni fan funding; para un hobby, bajo | Variedad real entre episodios (P1, I3); series con arco; fuentes en la descripción; cadencia fija y lenta (quincenal); no copiar la plantilla de títulos de la referencia |
| Desmonetización tras entrar | 20-30 % en 12 meses | Igual | Ídem; expediente para apelar |
| Menor distribución algorítmica (no documentada como sanción) | Desconocida | Menos vistas | No controlable |
| **Cierre del canal** (spam, prácticas engañosas) | Baja, < 5 %, si se etiqueta y no se engaña | Alto: se pierde el catálogo | Etiquetado siempre; nada de metadatos engañosos; nada de subidas masivas; copia del catálogo fuera de YouTube (Internet Archive o similar, con licencia) |

**Lectura para el plan:** con D6 (hobby anónimo), el éxito del proyecto **no puede depender de monetizar**. Las puertas
(§9) miden tracción de audiencia y calidad percibida, no ingresos.

### 7.2 Etiqueta "contenido alterado o sintético" de YouTube

- Obligatoria si el contenido parece realista y "generates a realistic scene that didn't actually occur" o "alters
  footage of a real event or place"; no obligatoria para animación o escenas claramente irreales. No declararlo puede
  llevar a etiqueta manual, retirada o suspensión del YPP; YouTube puede etiquetar solo lo que detecte o lo que lleve
  metadatos C2PA [F https://support.google.com/youtube/answer/14328491?hl=en].
- El estilo que dio el promotor es **fotorrealista de época** (la referencia) ⇒ escenas realistas que no ocurrieron
  ⇒ **la etiqueta es obligatoria**. El Gauntlet 1 la evitaba con estilo pictórico; ese margen ya no existe.
- **Decisión:** se activa en cada vídeo (`status.containsSyntheticMedia` en la API). Declarar no reduce el alcance ni
  la monetización según YouTube [R `gtm_riesgos.md` §3.2].

### 7.3 AI Act, artículo 50 (aplicable desde el 2-08-2026)

| Obligación | ¿Nos aplica? | Cómo se cumple |
|---|---|---|
| **50.4, texto generado por IA publicado para informar al público sobre asuntos de interés público**: hay que declararlo, **salvo** revisión humana o control editorial con una persona que asume la responsabilidad editorial [R `gtm_riesgos.md` §3.3; https://artificialintelligenceact.eu/article/50/] | Probablemente sí (divulgación histórica) [S, interpretación]. **Sin revisión humana (D5), la excepción no se puede invocar** | Declarar que el texto es generado por IA, además de la voz y las imágenes |
| **50.4, deepfakes**: imagen, audio o vídeo que se parece a personas, lugares o hechos existentes y parecería auténtico (def. art. 3(60)) | **Sí**: escenas fotorrealistas de lugares y hechos reales; y una voz sintética que se parece a la de un locutor real (Brais = voz de un profesional identificado en la ficha de datos) [R `gtm_riesgos.md` §3.3] | Aviso claro "a más tardar en la primera exposición" (50.5): **aviso hablado en los primeros 30 s**, texto en la descripción y etiqueta de YouTube |
| Excepción de obra "evidentemente artística, creativa... o de ficción" (aviso reducido) | No: es divulgación histórica | Aviso completo |
| Marcado legible por máquina (50.2) | Es obligación del **proveedor** del sistema, no del desplegador [R] | Conservar metadatos C2PA si las herramientas los generan; no borrarlos |

- **Anonimato:** el art. 50 obliga a declarar que el contenido es artificial, no a identificar al autor. El canal puede
  seguir siendo anónimo ante el público [S, interpretación]. Ante Google (AdSense, fiscalidad) no hay anonimato.
- **España:** el anteproyecto de ley de gobernanza de la IA sigue en tramitación [R `gtm_riesgos.md` §3.3]; revisar
  cada trimestre.
- **Sanciones:** hasta 15 M€ o 3 %, con la menor de las dos para pymes [R]; riesgo práctico bajo para un canal pequeño
  que etiqueta.

**Aviso hablado propuesto (galego; lo lee la propia voz sintética al empezar, ≈ 20 s):**

> Boas noites. Antes de comezar, unha advertencia: este vídeo fíxose de forma automática con intelixencia artificial.
> O texto, a voz e as imaxes son xerados, e ningunha persoa os revisou antes de publicalos, así que pode haber erros.
> A voz é sintética e baséase nun modelo do Proxecto Nós, da Universidade de Santiago de Compostela.
> Se atopas algún erro, dínolo nos comentarios e corrixirémolo.

**Nota fija de la descripción (galego):**

> Como se fai esta canle: o guión, a voz e as imaxes xéranse de forma automática con intelixencia artificial, sen
> revisión humana antes da publicación. O texto redáctase só a partir das fontes que se citan embaixo, e uns controis
> automáticos comproban a ortografía, a gramática e que cada dato estea nas fontes; aínda así, poden quedar erros.
> Voz: modelo StyleTTS2 Brais do Proxecto Nós (USC), licenza Apache-2.0. Imaxes: xeradas con IA; non son documentos
> históricos. Erratas coñecidas: no comentario fixado.

(Texto para el público en galego normativo. Sin revisión humana, como todo lo demás: va marcado para que el tribunal
del Gauntlet 2 lo lea con ojo de filóloga.)

---

## 8. Riesgos de lengua e historia sin filtro humano

### 8.1 Riesgos y su tratamiento

| Riesgo | Prob. / impacto [S] | Tratamiento |
|---|---|---|
| Errores de lengua en cada episodio (§6.3) | Cierta / medio-alto: es lo que más castiga el público galego y lo que cita la crítica | Declararlo en el aviso; lista viva de castellanismos; erratas públicas; alimentar el léxico de Cotovía con cada error de pronunciación |
| Pronunciación mala de topónimos y vocales | Alta / alto | Léxico de topónimos del episodio pasado por Cotovía antes de sintetizar; errores reportados a Nós (§1.4) |
| Error histórico con carga identitaria (Irmandiños, Reino de Galicia, emigración) | Media / alto | Temas canónicos de consenso; zonas rojas vetadas; tono descriptivo |
| Mito presentado como hecho (celtismo romántico, leyendas); sube con el catálogo ampliado (§8.2), que hace de las lendas la mitad del bloque (b) | Media-alta / medio | Leyenda solo como leyenda ("contábase que..."), marcada en `afirmacions.csv` con tipo `lenda` y comprobada por H4 (§6.1) |
| Traducción defectuosa en las pistas pt/en/es (§A.3) | Alta si hay pistas / medio | M1-M6 (§A.3.4); la pista que no pasa no sale; el vídeo sale igual en galego |
| Guerra normativa (RAG frente a reintegracionismo) | Alta / bajo | Norma RAG/ILG declarada; no entrar en debate |
| Politización | Media / medio | Temas y tono (§8.2) |

### 8.2 Catálogo cerrado del primer año: toda Galicia, no solo historia [S]

Directriz del promotor (29-09-2026): enganchar y ser atractivo por encima de la exhaustividad, **sin perder rigor**. El
catálogo mezcla **mitad historia (nicho a) y mitad Galicia ampliada (nicho b)**; la prueba de §A.4 decide después el
reparto con datos. Temas en series con arco (control P1 y política de YouTube).

| Bloque | Series del primer año | Gancho verdadero para el primer minuto (tipo de dato, no texto final) | Cuidado específico |
|---|---|---|---|
| **Historia** (a) | *Gallaecia* castrexa e romana (vida nun castro, Lucus Augusti, as vías); o reino suevo (vida, rutas, Braga); o Camiño e Compostela medieval (peregrinos, hospitais, a catedral en obras); mosteiros (Samos, Oseira, Sobrado); os irmandiños (con el guion muestra corregido) [R `../../guion-mostra-revolta-irmandina.md`] | Detalle cotidiano sorprendente y documentado (qué comía un peregrino, cuánto duraba un viaje, cómo se dormía en un hospital de peregrinos) | Consenso historiográfico; nada de "o primeiro reino de Europa" sin matiz |
| **Lendas e mitos** (b) | A Santa Compaña; meigas, bruxas e menciñeiros; mouras e tesouros dos castros; cidades asolagadas (a lagoa de Antela) | Lo que **se contaba** y dónde, y por qué se contaba (la lenda como historia de las mentalidades) | **Siempre como lenda** (control H4, abajo); menciñeiros sin ningún remedio presentado como útil (T5, salud) |
| **O mar** (b) | Costa da Morte (naufraxios, faros, a lenda dos raqueiros), salga e conserva, baleeiros, redeiras e mariscadoras | Contraste entre la lenda y lo documentado (p. ej. raqueiros: qué se cuenta y qué consta) | Distinguir lenda y hecho en la misma frase |
| **Vida cotiá de antes** (b) | Feiras, muíños, fiadeiros e seráns, o inverno na aldea | "Así se pasaba unha noite de inverno": el tema más natural para dormir | Evitar la nostalgia inventada: solo costumbres con fuente |
| **Idiosincrasia: o porqué** (b) | Minifundio (herdanzas e foros); emigración a América 1880-1930 (indianos); retranca e morriña | "Por que Galicia está partida en millóns de leiras": causa histórica documentada | Explicaciones **atribuidas** ("unha explicación habitual é..."), nunca esencias; nada de "carácter celta" ni determinismos étnicos |

**Regla "lo legendario como leyenda", convertida en control automático (H4, §6.1):** en `afirmacions.csv` cada frase
lleva tipo `feito` o `lenda`; `dossier.py` ya aparta las leyendas de las fuentes (§3.3). Toda frase `lenda` tiene que
estar dentro de un bloque abierto por un marcador ("conta a lenda", "dicíase que", "segundo a tradición", "hai quen
di") y el juez H2 comprueba además que ninguna frase `feito` afirme algo que la fuente trata como leyenda. Los ganchos
del título y del primer minuto tampoco pueden presentar una leyenda como hecho ("A Santa Compaña existiu" no;
"Durante séculos, en Galicia houbo quen xuraba ter visto a Santa Compaña" sí).

**Vetado:** Guerra Civil y represión, franquismo, política desde 1975, personas vivas, conflictos lingüísticos
actuales, temas de salud (incluidos remedios de menciñeiros como útiles), y el celtismo presentado como hecho.

### 8.3 El riesgo que más contradice la tesis "pro lingua": contaminar el corpus

- Los modelos en galego (los de Nós incluidos) se entrenan en parte con texto de la web. El galego tiene poco texto;
  unas pocas decenas de horas de galego sintético sin revisar, con subtítulos y transcripciones públicas, **pesan
  proporcionalmente más** que en castellano [S, razonamiento; en la literatura se conoce como degradación por
  entrenamiento con datos sintéticos].
- Si el canal presume de "fomentar mejores modelos en galego", **no puede ser a la vez una fuente de galego defectuoso
  sin marcar**. Es el argumento más fácil de usar en su contra por parte de Nós, la RAG o la comunidad técnica.
- **Mitigación obligatoria:**
  1. Todo texto publicado (descripción, subtítulos, guion si se comparte) lleva la marca "texto xerado automaticamente
     con IA, sen revisión humana".
  2. Los guiones **no** se publican como corpus. Si se comparten con Nós, van en un conjunto separado y etiquetado
     como sintético, junto con los errores detectados y sus correcciones (que sí son valiosos como datos de evaluación).
  3. Subtítulos: subir el guion como subtítulo (mejor que el automático de YouTube), con la marca en la primera línea.
- Este punto debe ir a la conversación con Nós/USC (D4): preguntarles cómo prefieren que se marque. Es un gesto que
  convierte un riesgo en colaboración (detalle en la pieza de comunidad).

### 8.4 Dónde la falta de revisión choca con la comunidad (resumen; análisis completo en la pieza de comunidad)

- **Nós/USC:** el uso de la voz de un locutor identificado sin su permiso para fines comerciales es el riesgo más
  grave (LO 1/1982). Mientras no haya respuesta de Nós/USC y del locutor, **no se monetiza** (§9, puerta P0).
- **Sector de la voz y AGPTI/ADA:** un canal automático en galego es exactamente lo que temen (precedentes RTVE y
  CSAG/Caamaño, 2026) [R `gtm_riesgos.md` §3.5]. El anonimato baja el riesgo personal, pero hace que el canal parezca
  "escondido", lo contrario de la transparencia.
- **RAG, CCG, SXL, CRTVG:** difícil que apoyen públicamente un contenido sin revisión lingüística. La vía de apoyo
  realista no es "respaldar el canal" sino **usar sus datos de error** y, si hay tracción, financiar la revisión
  (lo que el plan v1 llamaba Puerta F) [R `tribunal.md`].

---

## 9. Puertas go/no-go y KPIs (incluida la D1)

Relojes: M0 = primera publicación. Las métricas salen de YouTube Studio; "a 30 días" = vistas de cada vídeo a los 30
días de publicarse.

| Puerta | Cuándo | Condición para seguir (GO) | Si falla |
|---|---|---|---|
| **P0 · Salida** | Antes de publicar el primer episodio | (1) Piloto completo pasa los 14 controles; (1a, P0-a) un episodio de 60 + 30 min sale del pipeline sin intervención en ≤ 8 h de reloj (§4.1 predice 5-7 h); (2) canarios C0 con H2: ≥ 90 % y ≥ 4/5 en "sin fuente" en el conjunto actual, y ≥ 80 % en un conjunto nuevo de otro tema (§6.1). **Hoy: 80 % y 2/5 → no se pasa**; (2a) sonoridad dentro de −18/−16 LUFS en el vídeo que se publique (el ejemplo actual mide −20); (2b) el promotor ha cronometrado 3 dossieres y la media cabe en §3.2; (3) aviso hablado y nota de descripción puestos; etiqueta sintética activada; (4) licencias archivadas (SDXL-Turbo, Apache de Nós); (5) **correo de solicitud de permiso a Nós/USC enviado** (D4). La respuesta no es necesaria para publicar como hobby **sin monetizar** [S, decisión de prudencia] | No se publica |
| **P0-bis · Voz** | En cuanto responda Nós/USC | Permiso para el uso (y, si Nós lo exige, del locutor) | Si dicen que no: cambiar a otra voz con permiso claro en ≤ 30 días (voces de proveedor gl-ES con licencia comercial) o retirar el audio [R `gtm_riesgos.md` §3.3 bis] |
| **P1 · ¿Existe el nicho?** (fase 1 de §A.4) | Día 30 del episodio 8 (≈ semana 10) | 8 episodios: 4 de historia y 4 de Galicia ampliada, solo en galego. M = mediana de vistas a 30 días; G = % de vistas desde ciudades galegas; y 0 incidentes graves (§10) | **Sin zona gris:** M < 40, **o** G < 15 % con 0 comentarios en galego → **PARADA** (nicho inexistente para este formato; se publican el código y los informes de error para Nós; coste hundido ≈ 60-95 h y < 30 €). 40 ≤ M < 150 → **MÍNIMO** (1 episodio al mes; en M6, M < 60 sobre los 4 últimos → PARADA, M ≥ 60 → sigue). M ≥ 150 → **PLAN** (régimen de §4.2 y P2) |
| **P1-bis · Pistas pt + en** (fase 2 de §A.4) | ≈ Semanas 12-17, si P1 no da PARADA | Pistas en 4 de los 8 episodios; control con los otros 4. R = cociente de vistas; L = % del tiempo en la pista gl | R < 1,3 → solo galego. R ≥ 1,3 y L ≥ 40 % → pt + en y prueba del es (fase 3). 25 % ≤ L < 40 % → pt + en, sin es. L < 25 % → solo pt |
| **P2 · Hábito** | M6 (~17 episodios), solo si P1 dio PLAN | Mediana a 30 días ≥ 200 vistas **y** ≥ 150 subs **y** ≥ 25 % de espectadores recurrentes **y** ≥ 30 % de las vistas desde listas de reproducción, página del canal o búsqueda de la canle (consumo repetido, no descubrimiento) **y** tasa de erratas señaladas por episodio decreciente | Seguir solo como banco de pruebas técnico, a 1 episodio al mes |
| **P3 · Tracción (dispara D1)** | Desde M6, revisión mensual | Ver §9.1 | No se paga la validación |
| **P4 · YPP** | Cuando se cumplan 1.000 subs y 8.000 h | Solicitar solo con P0-bis resuelto y sin alarmas abiertas | No solicitar |

### 9.1 KPIs para pagar la validación de la voz (D1: 850-1.500 €)

La validación responde a una pregunta concreta: **¿la voz es la que frena el canal o la que lo hace posible?** Solo
tiene sentido cuando hay suficiente público para que la respuesta cambie algo.

**Se paga si se cumplen las tres condiciones:**

1. **Tracción: al menos 2 de estos 3 KPIs en una ventana de 90 días**
   - ≥ 500 suscriptores (umbral de fan funding) [F];
   - ≥ 3.000 h vistas en los últimos 365 días (el otro requisito del fan funding) [F];
   - mediana a 30 días ≥ 1.000 vistas en los últimos 8 episodios [S].
2. **Permiso de Nós/USC** para la voz usada (si no, la validación se hace sobre la voz sustituta).
3. **Ninguna alarma de plataforma abierta** (A1-A2 del §10): no se invierte en la voz de un canal que YouTube está
   desmonetizando.

**Señal que adelanta la validación aunque falte un KPI** [S]: si la voz aparece como motivo principal en ≥ 20 % de los
comentarios críticos durante 2 meses **y** la retención cae en los primeros 2 minutos más que en el resto del vídeo,
la voz es el cuello de botella, y D1 se paga con 1 KPI de tracción en lugar de 2.

**Qué se compra con la validación** (del Gauntlet 1, sin cambios): panel ciego de oyentes galegofalantes y un
revisor profesional que puntúa la voz frente al listón [R `../../gauntlet/piezas/voz.md`]. Resultado posible: seguir
con Brais, cambiar de voz (D2: la más cercana al listón) o invertir en el léxico de corrección de Cotovía.

**Probabilidad de llegar a pagarla en 12 meses:** ≈ 8-12 % [S] (el escenario optimista del §1.3; con ≈ 30 episodios, el base ya no llega a 500 subs).

### 9.2 Cuadro de mando mensual (5 min al mes)

| KPI | Fuente | Umbral de alarma |
|---|---|---|
| Vistas a 30 días (mediana de los 4 últimos) | Studio | Caída > 50 % dos meses seguidos |
| Espectadores recurrentes (% de espectadores únicos) | Studio, *Audiencia* | < 10 % dos meses seguidos [S] |
| Retención a 2 min (la única parte de la curva que mide si el vídeo convence: después, la gente se duerme) | Studio | < 40 % [S] |
| AVD (solo informativo) | Studio | Sin umbral: en contenido para dormir el vídeo sigue sonando con el oyente dormido o en segundo plano, así que el AVD mide tanto el sueño como el interés |
| Suscriptores netos | Studio | Negativos dos meses seguidos |
| Erratas señaladas por episodio | Fichero de erratas | Subiendo tres meses seguidos |
| Tasa de canarios C0 detectados | Expediente | < 80 % |
| Episodios bloqueados por el semáforo | Expediente | > 25 % [S]: el pipeline no está a la altura |
| Avisos de YouTube (políticas, *limited ads*) | Studio | Cualquiera |

---

## 10. Alarmas que paran la publicación

| # | Alarma | Acción |
|---|---|---|
| A1 | Aviso o *strike* de YouTube por spam, inautenticidad o metadatos | Pausa; revisar variedad del catálogo; apelar con el expediente |
| A2 | Rechazo del YPP | Seguir como hobby; no reenviar hasta 30 días y con cambios reales |
| A3 | Crítica pública con eco (prensa, cuenta influyente, carta de una institución o de AGPTI/ADA) | Pausa de 2 semanas; responder con transparencia y datos; ofrecer el pipeline y los datos de error |
| A4 | Nós/USC o el locutor piden retirar la voz | Retirar o sustituir el audio en ≤ 30 días |
| A5 | Error histórico o lingüístico grave señalado (no una errata menor) | Corregir en ≤ 7 días; si afecta al conjunto del vídeo, despublicarlo |
| A6 | Canarios C0 < 80 % o > 25 % de episodios bloqueados | No publicar hasta reparar |

---

## 11. Supuestos que el piloto tiene que medir

1. ~~Tiempo de imagen por plano en CPU~~: medido, 12-25 s con SDXL-Turbo (§4.1). Queda la calidad frente a la referencia (pieza del vídeo)
   y el tiempo real de un episodio de 60 min completo (P0-a).
1 bis. Minutos de persona por dossier: medidos en volumen, no en reloj de persona (§3.3). Los mide el promotor en los 3 primeros.
2. Calidad del guion de un LLM frontier frente a Carballo-Instr3 en galego (ciego, con los controles T1-T3 como métrica).
3. Tasa de detección de los canarios con H2 y en un conjunto nuevo (hoy, sin H2 y sobre el conjunto conocido: 80 %), y tasa de falsos bloqueos.
4. Residuos por episodio (§6.3): solo se sabrán si una persona experta mira un episodio. Si alguien de la comunidad lo
   ofrece gratis, aceptarlo es compatible con D5 (no es revisión pagada) y es el mejor dato del proyecto.
5. Si YouTube sirve el audio en galego fuera del público galegofalante (hipótesis VaniMani). Lo mide G en la fase 1 de §A.4.
6. Si el LLM por suscripción se puede usar de forma automatizada según sus términos o hay que ir a la API (coste ≤ 10 €/mes igualmente).
7. Si el galego está en la lista de idiomas de pista de audio de YouTube, si las pistas se pueden subir por API y si
   Analytics desglosa el tiempo de visionado por pista (§A.3.1). Se comprueba en Studio antes de construir M1-M6.
8. Calidad de oído de Piper y Kokoro en pt/en/es frente a los competidores de cada idioma (no escuchada todavía; §A.3.3),
   licencia de la voz base *lessac* de Piper, y tiempos sin la CPU compartida.
9. Si Studio da el informe de ciudades (métrica G de §A.4) o solo el país.

---

## Fuentes nuevas de esta pieza (consultadas el 29-09-2026)

- YouTube, política de monetización (contenido inauténtico): https://support.google.com/youtube/answer/1311392?hl=en
- TubeFilter, aclaración de las tres categorías (13-07-2026): https://www.tubefilter.com/2026/07/13/youtube-inauthentic-content-monetization-policy-update/
- YouTube, divulgación de contenido alterado o sintético: https://support.google.com/youtube/answer/14328491?hl=en
- YouTube Data API, `videos.insert` (proyectos no auditados → privado): https://developers.google.com/youtube/v3/docs/videos/insert
- Stability AI, licencias (Community License, < 1 M$): https://stability.ai/license ; ficha SDXL-Turbo: https://huggingface.co/stabilityai/sdxl-turbo
- Nós, Llama-3.1-Carballo-Instr3: https://huggingface.co/proxectonos/Llama-3.1-Carballo-Instr3
- OutlierKit, resumen de la ofensiva contra el *slop* en 2026: https://outlierkit.com/resources/youtube-ai-slop-crackdown-2026/
- YouTube, multi-language audio (pista por defecto según el historial, descubrimiento por título traducido, > 25 % del tiempo en la lengua no principal): https://support.google.com/youtube/answer/13338784?hl=en
- TechCrunch, multi-audio para todos los creadores (10-09-2025): https://techcrunch.com/2025/09/10/youtubes-multi-language-audio-feature-for-dubbing-videos-rolls-out-to-all-creators/ ; PPC Land, vistas y horas en un solo vídeo: https://ppc.land/youtube-makes-multi-language-audio-available-to-millions-of-creators/
- Nós MT gl→es (MIT): https://huggingface.co/proxectonos/Nos_MT-CT2-gl-es ; gl→en: https://huggingface.co/proxectonos/Nos_MT-CT2-gl-en
- Kokoro-82M (Apache-2.0): https://huggingface.co/hexgrad/Kokoro-82M ; Piper, voces y fichas: https://huggingface.co/rhasspy/piper-voices
- Búsquedas de YouTube y prueba multi-audio propias: `../medidas/nicho/` (README, `busquedas-yt.txt`, `multiaudio/`).
- Listón de referencia: `../referencia.md` (yt-dlp sobre https://www.youtube.com/@HistoriaDesconocida-m4j).
- Medidas propias usadas en la v2: `../medidas/escala/extrapolacion.md` (tiempos), `../medidas/c0-irmandinos-apertura/`
  y `../medidas/c0-irmandinos-apertura-r3/` (C0), `../medidas/r2-*/qa.json` (WER, LUFS, ritmo),
  `../../../herramientas/pipeline/dossier/samos/` (dossier cronometrado).
- Reutilizado del Gauntlet 1: `../../gauntlet/investigacion/retornos.md`, `audiencia.md`, `voz_guion.md`;
  `../../gauntlet/piezas/pipeline.md`, `gtm_riesgos.md`, `voz.md`; `../../tribunal.md`.
