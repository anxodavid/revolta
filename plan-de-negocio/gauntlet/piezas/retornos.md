# Sección 1. Escenarios de retorno y modelo financiero por etapas

Business plan del canal de historia de Galicia para durmir, hecho con IA y 100 % en galego.
Versión 4 (constructor, respuesta al crítico de esta ronda) · 29-09-2026 · Horizonte: octubre de 2026 a septiembre de 2029.

**Convenciones**
- **[F]**: dato con fuente; la URL va al lado o en la tabla de supuestos (§3).
- **[OBS]**: observación directa de páginas públicas (YouTube, youtubeiras.gal, PDF de la CRTVG) el 29-09-2026. Datos brutos: `gauntlet/model/obs_clonicos_29-09-2026.txt` (vida entera de 9 clónicos) y **`gauntlet/model/obs_nuevos_1mes_29-09-2026.txt`** (64 canales hallados por búsqueda de subidas recientes; scripts `model/chans.py` y `model/vids.py`).
- **[S]**: supuesto propio. No está verificado y el piloto lo sustituirá por datos reales.
- Todas las proyecciones son [S]. Salen de un modelo mensual reproducible: `model/modelo2.py` (trayectorias por rama), **`model/arbol4.py` + `model/arbol4_final.py`** (árbol con **puertas ruidosas**, matriz de confusión, umbrales, premios y distribución; sustituye a `arbol3.py`), `model/sens2.py` (sensibilidad dentro de un camino).
- Calendario: mes 1 = octubre de 2026. M6 = marzo de 2027, M12 = septiembre de 2027, M18 = marzo de 2028, M36 = septiembre de 2029.

**Qué cambia respecto a la versión 3** (registro completo y respuesta punto por punto al crítico en el §12):
- **Las puertas ya no clasifican las ramas "por arte de magia".** En la v3 cada rama pasaba o no pasaba cada puerta con certeza. Ahora el modelo simula el ruido real vídeo a vídeo (dispersión medida en 13 canales nuevos: desviación típica del logaritmo de las vistas ≈ 1,0-1,4) y calcula **la probabilidad de que cada rama pase cada puerta** (matriz de confusión, §5.1).
- **Resultado incómodo que obliga a cambiar la P1:** con el umbral de la v3 (≥ 60 vistas y ≥ 20 suscriptores), la trayectoria mediana del escenario base pasaba por los pelos (91/25), pero con ruido **la rama base fallaba la P1 el 24 % de las veces y la estancada la pasaba el 76 %**: la puerta no separaba nada. Como la rama base **pierde dinero a M36 en cualquier caso** (−1.825 €), el umbral que maximiza el valor esperado es el que deja pasar a la rama alta y para a la base. **P1 nueva: mediana ≥ 100 vistas a 30 días en los vídeos 9-12 y ≥ 30 suscriptores. P2 nueva: ≥ 150 / ≥ 150** (§1, §5.1).
- **Coherencia escenario-puerta, dicha sin rodeos:** la trayectoria mediana del escenario base (91 vistas y 25 suscriptores en M6) **no pasa la P1 nueva**. Lo realista para el base es **parar en el mes 6 con −210 € y ~100 h** (le pasa en el 55 % de sus realizaciones; en otro 28 % para en la P2 con −870 €). Ya no se presenta el base como camino hasta M36.
- **A1 contrastado con los primeros 30 días de canales nuevos** (no con vistas acumuladas ni con canales con marca): 13 canales de historia/relatos para dormir en castellano con vídeos de 1 día a 4 semanas. Mediana por canal: **0-35 vistas en 5 de 13** (canales "muertos") y **85-340 en 7 de 13**; mediana de medianas ≈ 109 (§3.1). El A1 base de 70 queda **por debajo** de un canal nuevo vivo en castellano, como corresponde a un mercado ~100 veces menor.
- **La AVD entra también por la vía que más pesa:** además de impresiones de anuncios, Premium por horas, umbral de horas del YPP y horas de Spotify, se añade una variante en que la AVD alimenta la recomendación (crecimiento y cola larga con elasticidad 0,5 [S]). En el camino optimista, pasar de 20 a 60 min mueve el resultado de **+549 € a +6.281 €** (§9.3).
- **Verificado de nuevo hoy:** el post del YPP 2027 solo menciona 8.000 h cualificadas (o 20 M de vistas de Shorts) y no dice nada de suscriptores; los 1.000 suscriptores siguen marcados como [S]. Los umbrales de Spotify (3 episodios, 2.000 h de consumo y 1.000 oyentes comprometidos en 30 días) son de TechCrunch, que **no distingue** si las horas son de audio o vídeo; Infobae solo da la fecha de llegada a España (§2).
- **Resultado:** valor esperado de caja a M36 de **+50 €** (v3: −147 €) con 242 h esperadas. No es que el proyecto haya mejorado: es que **las puertas bien calibradas cortan antes la rama que pierde dinero**. El signo sigue colgando de un hilo (§9).

---

## 0. La respuesta corta: dónde están los retornos

1. **Lo más probable (~78 %) es parar en el mes 6 habiendo gastado ~210 € y ~100 h.** Es el destino del 100 % de la rama "clónico", del 15 % de riesgo lingüístico y también **de la mayoría de las realizaciones del escenario base** (55 %), que en la mediana no llega al umbral de la P1. Es el resultado **mediano** del plan, y es un buen resultado: compra información barata.
2. **Valor esperado a M36, caso central** (árbol con puertas ruidosas; ingresos recurrentes + Youtubeiras+ con tasa base; sin CRTVG ni B2B):
   - **+50 € de caja** (+9 € sin ningún premio): en la práctica, **cero**; el intervalo razonable va de −340 € (sin patrocinios) a +280 € (P(rama alta) = 20 %);
   - **242 h esperadas** del promotor, es decir, **+0,21 €/h**;
   - con las horas valoradas a 15 €/h, **−3.582 €**.
   - **Como negocio no se sostiene en ningún escenario ponderado. Como hobby con opción, sí:** la pérdida probable es de 210 € y la máxima con disciplina, de ~1.900 € (3,7 % de probabilidad).
3. **Solo un 12,7 % de probabilidad de acabar en positivo de caja a M36.**
   - El 9,5 % es el camino optimista (+3.355 €, sin ayudas).
   - El 3,2 % es parar pronto pero ganar un Youtubeiras+ (+600 €).
4. **La publicidad de YouTube en galego no paga el proyecto.**
   - La rama base **no entra en el YPP en 36 meses** en mantenimiento (758 suscriptores en M36); aunque siguiera en E2 todo el tiempo, entraría en M35, perdiendo ~3.070 € por el camino.
   - En el optimista entra en M17, pero AdSense + Premium solo suman **~58 €/mes en M36**.
   - Techo publicitario con todo el mercado galego capturado: **~410-700 €/mes** (§4).
5. **Lo que mueve la aguja es lo que no es AdSense:**
   - patrocinio identitario (~270 €/mes en M36 en el optimista; sin él, el valor esperado cae a **−339 €**);
   - membresías (~150 €/mes);
   - y, si la AVD alimenta la recomendación, **la retención del oyente** (§9.3).
   - Las ayudas públicas son una **opción**, no una previsión:
     - La **CRTVG** con un 10 % de probabilidad subiría el valor esperado de +50 € a ~+150 €. Para rescatar el camino base que llegue a mantenimiento haría falta **≥ 23 %**.
     - No hay ninguna tasa pública que permita saber si esas probabilidades son mucho o poco (§6.2).
     - Además, la convocatoria exige alta de autónomo, un proyecto inédito y ceder en exclusiva y para siempre la temporada producida.
6. **La Etapa 3 tiene valor esperado negativo a 36 meses** (−2.250 € si se abre en M19). Baja el total a −164 €. Se recupera hacia el mes ~50 y su valor es de opción: el caso ganador da ~2.000 €/mes. Confirma la regla del promotor: solo si 1 y 2 funcionan, y con un horizonte de 4-5 años (§7).

---

## 1. Las tres etapas y sus puertas de decisión

| Etapa | Meses | Presupuesto caja | Horas del promotor | Cadencia y formato | Objetivo económico |
|---|---|---|---|---|---|
| **1. Piloto barato con puertas** | 1-6 (oct-2026 a mar-2027) | ≤ 50 €/mes (modelo: 35 €) | ~4 h/semana (≈ 17 h/mes) | 1 vídeo cada 2 semanas, 60-90 min | **Ninguno.** Comprar datos: vistas, retención, conversión y veredicto del galego |
| **2. Proyecto lateral rentable** | 7-18 (abr-2027 a mar-2028) | 50-200 €/mes (modelo: 110 €) | 6-10 h/semana (≈ 35 h/mes) | Semanal, ~2 h | Ingresos recurrentes ≥ coste de caja en 12-18 meses |
| **2b. Mantenimiento** (si no se pasa la Puerta 3) | 19-36 | ~20 €/mes | ~2 h/semana (8 h/mes) | 1 vídeo al mes | Conservar el catálogo y la elegibilidad para premios |
| **3. Apuesta seria / red** | Desde el mes 19, solo si se pasa la Puerta 3 | 1.000-5.000 € iniciales (modelo: 3.000 €) + ~90 €/mes incrementales | ~10 h/semana | Pistas o canales es/pt y voz licenciada | Techo de cientos a miles de €/mes |

Cadencias y duraciones: `research/formato.md` §0 y §3.9. Horas y presupuestos: respuestas del promotor (`contexto.md`).

### Puertas cuantificadas, con ruido y coherentes con los escenarios

**Para qué sirve cada puerta.** La rama base pierde dinero a M36 en cualquier caso (−1.825 € si llega a mantenimiento, §5.4); la única que paga el proyecto es la alta. Por tanto la P1 no debe preguntar "¿esto se parece a la base?", sino **"¿esto se parece a la alta?"**. La v3 hacía lo primero; la v4 hace lo segundo.

**Cómo se evalúan.** Las vistas de cada vídeo tienen mucho ruido: en 13 canales nuevos de historia o relatos para dormir, la desviación típica del logaritmo de las vistas a 1-30 días va de 0,6 a 2,2 (típico 1,0-1,4; §3.1) [OBS]. El modelo (`arbol4.py`) simula 20.000 veces cada rama con σ = 1,2 y aplica la regla sobre la **mediana** de los 4 últimos vídeos (la media la arrastra un solo vídeo viral). De ahí sale la probabilidad de pasar cada puerta:

| Puerta | Cuándo | Condiciones (todas) | Trayectoria mediana en la puerta (vistas a 30 d / suscr.) | P(para aquí) por rama: baja · estancada · **base** · alta |
|---|---|---|---|---|
| **P1** | M6, tras 12 vídeos | Mediana de vistas a 30 días de los vídeos 9-12 **≥ 100**; **≥ 30 suscriptores**; AVD ≥ 20 min; A/B ciego y comentarios sin quejas graves del galego (esto último falla en el 15 % de los casos, independiente de la audiencia) | baja 26/5 · estancada 91/24 · **base 91/25 → no pasa** · alta 318/99 | 100 % · 57 % · **55 %** · 3 % |
| **P2** | M12 | Mediana de vistas a 30 días de los vídeos nuevos **≥ 150**; **≥ 150 suscriptores**; Youtubeiras+ presentado; ≥ 5 propuestas de patrocinio enviadas | estancada 91/88 · **base 115/108 → no pasa** · alta 459/475 | – · 35 % · **28 %** · 3 % |
| Pasa P1 y P2 | | | | 0 % · 8 % · **17 %** · 93 % |
| **P3** | M18 | En el YPP con RPM real medido, **o** ≥ 50 €/mes de ingreso recurrente (media de 3 meses), **o** ayuda o encargo concedido | base: 253 suscr., 0 € → **mantenimiento o cierre** · alta: YPP desde M17, 173 €/mes → **pasa; abre la opción de la E3** | base y estancada: 100 % a mantenimiento · alta: 0 % |

**Lectura honesta de la tabla.**
- **El escenario base, en su trayectoria mediana, no pasa la P1.** Solo sigue cuando tiene un arranque mejor que su mediana (45 % de las veces), y esa suerte no cambia su futuro: el ruido es de cada vídeo, no del canal. Por eso **el camino realista del base es parar en M6 con −210 €** (55 %), o en M12 con −870 € (28 %). Solo el 17 % de las realizaciones del base llega a mantenimiento.
- **La rama alta pasa las dos puertas el 93 % de las veces.** Perder un 7 % de la rama buena es el precio de no financiar a la base.
- **Por qué estos umbrales y no otros** (valor esperado de caja a M36 según el umbral de la P1, con P2 = 100/100; `arbol4.py`):

| Umbral P1 (vistas / suscr.) | 60 / 20 (v3) | 80 / 25 | **100 / 30** | 150 / 40 | 200 / 50 | 250 / 60 |
|---|---|---|---|---|---|---|
| P(la base para en P1) | 24 % | 40 % | **55 %** | 79 % | 91 % | 96 % |
| P(la alta para en P1) | 0 % | 2 % | **3 %** | 11 % | 22 % | 33 % |
| Valor esperado a M36 | −69 € | −17 € | **+28 €** | +80 € | +79 € | +56 € |

  El máximo está en 150/40, pero la curva es plana entre 100 y 200 y a partir de 150 se empieza a matar la rama alta, que es la única que importa y cuya probabilidad es la más incierta del modelo. Se elige **100/30**. Endurecer después la P2 de 100/100 a **150/150** suma +22 € (de +28 € a +50 €) y apenas toca la alta (3 %).
- Los umbrales se **recalibran con los datos reales** de los vídeos 1-4 (§11), pero la regla no: **se sigue solo si la trayectoria se parece a la alta**, no a la base.
- La P2 ya no exige "≥ 1 solicitud de ayuda": presentarse a la CRTVG obliga a darse de alta (§6.2), y eso es una decisión aparte.

---

## 2. Qué ingresos existen y cuándo se desbloquean

| Fuente | Umbral de acceso | Reparto para el creador | Encaje con "para durmir" en galego | Fuente |
|---|---|---|---|---|
| AdSense (anuncios) | **1.000 suscriptores** + 4.000 h qualified en 12 meses (regla vigente). Para quien solicite desde el **1-feb-2027**: **8.000 h qualified en 365 días** | 55 % del ingreso neto de anuncios en vídeo largo | Bajo: los mid-rolls despiertan al oyente y los mejores del género venden "sin cortes" | [F] 1.000 suscr. + 4.000 h: https://support.google.com/youtube/answer/72851 · [F] 8.000 h desde 2027 (el post **no menciona** suscriptores): https://blog.youtube/news-and-events/youtube-partner-program-updates-2027-new-opportunities-earn/ · **[S]** que el requisito de 1.000 suscriptores se mantiene en 2027 · [F] https://www.sbs.com.au/news/article/sleep-videos-are-hugely-popular-but-youtube-adverts-are-disrupting-peoples-dreaming/edc0h3p1r |
| YouTube Premium | El mismo que AdSense | Pool del 30 % del neto de Premium (60 % en Lite), repartido "según el tiempo de visionado y las vistas de los miembros"; 55 % para vídeo largo | Alto por minuto: un vídeo de 2 h captura mucho tiempo de cada usuario Premium | [F] blog de YouTube (arriba) |
| Membresías / Super Thanks | 500 suscriptores + 3 subidas en 90 días + 3.000 h en 12 meses | 70 % | Medio: comunidad identitaria, pero la conversión a pago en sleep es baja (caso "Sleep With Me") | [F] https://support.google.com/youtube/answer/72902 ; [F] https://en.wikipedia.org/wiki/Sleep_with_Me_(podcast) |
| Spotify Partner Program (**videopódcast**) | Llega a España el **20-oct-2026**. Umbrales del programa (desde ene-2026): **3 episodios, 2.000 h de consumo y 1.000 oyentes comprometidos en los últimos 30 días** (antes: 12, 10.000 h y 2.000). TechCrunch **no precisa** si las horas son de audio o de vídeo; como el pago va por usuarios Premium que **ven** los vídeos, el modelo cuenta solo horas de vídeo (lo conservador) y no modela el requisito de 1.000 oyentes. Infobae solo aporta la fecha de llegada, no los umbrales | Pago según los usuarios Premium que **ven** los vídeos, más un reparto de la publicidad a usuarios free. **Tarifa no publicada** | Dudoso: quien se duerme suele apagar la pantalla | [F] fecha: https://www.infobae.com/america/agencias/2026/09/25/spotify-anuncia-la-llegada-a-espana-de-partner-program-iniciativa-para-convertir-los-podcast-en-negocios-sostenibles/ · [F] umbrales y pago: https://techcrunch.com/2026/01/07/spotify-lowers-monetization-threshold-for-video-podcasts · [F] tarifa no publicada: https://www.shopify.com/blog/how-to-make-money-on-spotify |
| iVoox, Patreon, Ko-fi | Sin umbral | Patreon: ~10 % + procesamiento. Ko-fi: 0-5 % | Packs temáticos de pago único y "episodio sin cortes" | [F] https://www.ivoox.com/blog/como-ganar-dinero-con-tu-podcast/ ; [F] https://ko-fi.com/pricing |
| Patrocinios gallegos | Sin umbral formal; en el modelo, desde M12 y con ≥ 2.000 vistas/mes | 100 % | Alto si la mención va solo al inicio y en tono calmado (balnearios, editoriales, textil del hogar, marcas identitarias) | Precio de mercado [F] en A14 (§3); candidatos en `research/ingresos_alt.md` §5 |
| **Premios Youtubeiras+** | Edición 2026: inscripción hasta el **15-nov-2026**, con ≥ 3 publicaciones desde el 16-nov-2025 | **Revelación, Calidade lingüística y Pódcast: 1.000 €** cada uno. Canle y Creación de contidos: 1.250 €. Sujetos a retención | Alto como validación | [F] https://youtubeiras.gal/bases-youtubeiras-2026/ |
| Encargo CRTVG (contenidos digitales) | Convocatoria anual (jun-sep). Se presentan personas físicas o jurídicas "dadas de alta no IAE", y la persona física seleccionada debe acreditar el **alta en autónomos** | Divulgación: hasta **26.000 € + IVA** (3 plazas). Videopódcast: hasta **6.000 € + IVA** (3 plazas). A cambio, **cesión exclusiva, mundial y hasta el dominio público** | Alto temáticamente, pero solo como temporada inédita aparte (§6.2) | [F] bases 2025, leídas página a página: https://www.crtvg.es/documents/d/crtvg/convocatoriaasinada09xuno2025contidosdixitais-pdf-1 |
| "O teu Xacobeo" (TU300A) | Plazo para actividades de 2027: **1-31 oct 2026**. Hay que ser autónomo o pyme (60 %) o asociación (80 %) | Hasta 25.000 € | Solo con una serie del Camino y alta formal. **Fuera de la Etapa 1** | [F] https://www.xunta.gal/dog/Publicados/2026/20260325/AnuncioG0256-090326-0002_gl.html |
| Ministerio de Cultura (innovación ICC) | Autónomo RETA o micropyme; ~abril | Hasta 50.000 € (70-80 %, cofinanciado) | Etapa 3 ("pipeline IA para lengua cooficial"). **No se suma al valor esperado:** financia gasto, no deja margen | [F] https://www.boe.es/buscar/doc.php?id=BOE-B-2026-10741 |
| Encargos B2B (concellos, museos) | Contrato menor < 15.000 € sin IVA | 1.000-6.000 € por encargo [S] | Etapas 2-3; necesita venta activa y facturar | [F] https://www.boe.es/buscar/act.php?id=BOE-A-2017-12902 |

**Lectura.**
- Lo primero que se desbloquea es el fan funding (500 suscriptores), no los anuncios.
- Lo único que no pide alta de autónomo ni audiencia son los **premios**, y son pequeños.
- **La CRTVG también exige alta.** La v2 decía que no, a partir de los seleccionados que eran personas físicas. Las bases lo aclaran: persona física, pero dada de alta en el IAE y como autónoma.

---

## 3. Tabla de supuestos (por rama de audiencia)

La audiencia se modela como **cuatro ramas** que el piloto revela. "Estancada" es la base hasta M6 y después deja de crecer. Las probabilidades de cada rama están en el §5.1.

| # | Variable | Baja (clónico) | Estancada | Base | Alta | Fuente / justificación |
|---|---|---|---|---|---|---|
| A1 | Vistas de un vídeo nuevo en su primer mes (mes 1 del canal) | **25** | 70 | **70** | **200** | [OBS] clónicos nuevos, §3.1. Baja = mediana de vida de los clónicos que fracasan (23-61 vistas en ~15 meses). Base = 2-3 veces eso [S], por tres motivos: nicho vacío en galego, siembra del promotor en comunidades gallegas y curaduría. Alta ≈ lo que logra en castellano el mejor clónico reciente en sus 3 primeros meses (107-467 vistas por vídeo a 1-4 semanas). **Contrastado con los primeros 30 días de 13 canales nuevos (§3.1 bis):** muertos 0-35, vivos 85-700, mediana de medianas ~109 |
| A2 | Crecimiento de las vistas por vídeo (autoridad del canal) hasta M18; después, la mitad | +20 % | +100 % hasta M6 y **0 después** | +100 % | +200 % | [S]. Partiendo de 0 suscriptores se crece en proporción más que un canal maduro. El mejor clónico pasó de 0 a ~200-400 vistas por vídeo en 3,5 meses [OBS] |
| A3 | Vistas de cola larga por vídeo de catálogo y mes | 2 | 6 | 8 | 20 | [OBS] en los clónicos fracasados, ~40 vistas de vida en ~15 meses equivalen a ≤ 3 al mes. Por encima es [S]: hábito de reescucha del contenido para dormir (`research/ingresos_alt.md` §3.1) |
| A4 | Cadencia | 2/mes (E1) | 2 → 4/mes | 2 → 4/mes → 1/mes en mantenimiento | 2 → 4/mes | [F] recomendación de `research/formato.md` §3.9 |
| A5 | AVD (duración media vista) | 20 min | 30 min | 30 min | 40 min | [S]. `research/retornos.md` §1 usa 20-60 min en vídeos de 2 h. El sector no publica la AVD de los vídeos sleep. **Canales por los que actúa en el modelo:** (1) impresiones de anuncios por vista (A7b); (2) Premium, pagado por **hora** (A8); (3) horas para el umbral del YPP y de las membresías; (4) horas de Spotify; (5) **variante [S]**: crecimiento y cola larga × (AVD / AVD de la rama)^0,5, porque la retención alimenta la recomendación (§9.3) |
| A6 | Conversión de vistas a suscriptores | 1,3 % | 2,0 % | 2,0 % | 2,5 % | [OBS] canales clónicos: 0,35 % a 2,5 % (mediana ~1,5 %; §3.1). Sleepless Historian ≈ 1,8 % [F] https://vidiq.com/youtube-stats/channel/@sleeplesshistorian/ . Rama alta [S]: la comunidad identitaria se suscribe "para apoyar" |
| A7 | **Anuncios** (€ para el creador por 1.000 impresiones) | 0,40 € | 0,60 € | 0,60 € | 0,90 € | [S] calibrado para que el RPM total del base sea ~2,5 €, dentro del rango habitual en España (2-6 €): https://monetizateonline.es/cuanto-paga-youtube-espana/ ; https://aceleratusredes.com/blog/cuanto-paga-youtube-por-pais-en-2026 |
| A7b | **Impresiones por vista = f(AVD)** | 1 pre-roll + un mid-roll cada 8 min **solo en los primeros 24 min**, que ve el 67 % | = | = | = | [S] política de anuncios recomendada para sleep (`research/formato.md` §2). Con AVD de 20 min salen 2,7 impresiones por vista; con AVD ≥ 24 min, 3,0 (tope) |
| A8 | **Premium** (€ por cada 1.000 **horas** vistas) | 1,0 € | 1,5 € | 1,5 € | 2,5 € | [S]. YouTube reparte Premium por tiempo de visionado y vistas [F, blog del YPP 2027]. No hay tarifa pública. Premium supone el 24 % (baja), el 29 % (base) y el 38 % (alta) del RPM total |
| A7+A8 | **RPM total efectivo resultante** | 1,40 € | 2,56 € | 2,56 € | 4,38 € | Salida del modelo, no un supuesto aparte |
| A9 | Umbral del YPP | 1.000 suscr. + 8.000 h/365 días (desde feb-2027) | = | = | = | [F] ver el §2 |
| A10 | Horas de **vídeo** en Spotify, como % de las horas de YouTube | 10 % | 25 % | 25 % | 40 % | [S]. YouTube (54,3 %) supera a Spotify (49,6 %) como plataforma de pódcast en España [F] https://www.prodigiosovolcan.com/pv/sismogramas/informe-voz-2025/podcast.html |
| A11 | Pago de Spotify por cada 1.000 h | 3 € | 5 € | 5 € | 8 € | [S]. **Tarifa no publicada** [F] Shopify (arriba) |
| A12 | Suscriptores que pagan membresía | 0,3 % | 0,6 % | 0,6 % | 1,0 % | [S]. `research/ingresos_alt.md` §4 estima un 0,5-2 % de la audiencia recurrente |
| A13 | Precio de la membresía / neto | 2,99 € / 70 % | = | = | 3,99 € / 70 % | [F] reparto del 70 %: https://support.google.com/youtube/answer/72902 ; precio [S] |
| **A14** | **Patrocinio efectivo** (€ por 1.000 vistas del canal; desde M12 y con ≥ 2.000 vistas/mes) **= CPM de mercado × tasa de venta** | 0 € | 10 € (20 € × 50 %) | **10 € (20 € × 50 %)** | **20 € (25 € × 80 %)** | **CPM de mercado [F]:** "15-25 € por cada mil escuchas en pódcast pequeños y medianos" (https://patillero.es/monetizar-podcast/ , 26-08-2026); "entre los 15 y los 40 euros" de CPM en pódcast en España, y "superiores a 50" en nichos comprometidos (https://jezzmedia.com/publicidad-en-podcasts-numeros-reales-en-espana/ , sin fecha); "entre los 10 y los 40 euros por cada mil visualizaciones" para creadores (https://euribor.com.es/2026/09/20/la-economia-de-los-influencers-asi-se-calcula-el-precio-real-de-un-post-patrocinado/ , 20-09-2026). Referencia de EE. UU. para cuñas leídas por el locutor: 18-26 USD (https://advertising.libsyn.com/podcast-advertising-rates). **Tasa de venta [S]**: fracción de las vistas que llevan una mención pagada. Ver la comprobación por vídeo debajo |
| A15-17 | Caja y horas | E1: 35 € y 17 h/mes · E2: 110 € y 35 h/mes · mantenimiento: 20 € y 8 h/mes | | | | Desglose en el §5.4; horas según las respuestas del promotor |
| A18 | Valor de la hora del promotor | 15 €/h (también se muestran 0 y 25 €/h) | | | | [S] coste de oportunidad neto |
| A19 | Primer cobro | El mes siguiente a desbloquear cada fuente | | | | [S] simplificación |
| A20 | Premio Youtubeiras+ neto | 810 € (1.000 € brutos − 19 % de retención) | | | | [F] importe y "suxeitas ás retencións": bases 2026 · tipo del 19 % [S] |

**Comprobación del patrocinio por vídeo (A14).** Es la variable que decide el signo del camino optimista, así que se contrasta con precios por pieza:
- En el optimista, M36 = 13.440 vistas/mes con 4 vídeos. A 20 € efectivos salen ~270 €/mes, es decir, **~67 € por vídeo**. Encaja con los nanocreadores (1.000-10.000 seguidores), que "suelen cobrar en especie o con tarifas simbólicas de entre 50 y 200 euros por publicación" [F euribor.com.es, arriba].
- En M12 del optimista salen ~16 € por vídeo, por debajo de ese rango. Es verosímil **solo como canje o patrocinio local**.
- **Dónde está el riesgo.** Los mínimos de campaña de las marcas grandes (3.000-10.000 € por campaña) y las productoras "competitivas" (10.000-50.000 oyentes por episodio) quedan lejos de este canal [F jezzmedia]. Por eso el riesgo **no está en el precio** (10-20 € efectivos está en el suelo o por debajo del mercado), **sino en la tasa de venta**: encontrar marcas gallegas que compren un nanocanal. La P2 lo mide: 5 propuestas enviadas antes de M12.

### 3.1 Calibración con canales nuevos sin audiencia

Búsqueda de canales "historia aburrida para dormir" en YouTube el 29-09-2026 [OBS]. Salen **más de 17 canales clónicos**. La mayoría se quedan en 1-60 suscriptores. Se midieron los vídeos de los que tenían más de 5:

| Canal (castellano, IA) | Alta en YouTube | Vídeos | Vistas totales | Suscr. | Vistas por vídeo (mediana, **en toda su vida**) | Suscr./vistas |
|---|---|---|---|---|---|---|
| @HistoriaAburridaparaDormir68 | 17-jun-2025 | 21 | 2.554 | 50 | 61 | 2,0 % |
| @HistoriaAburridaparaDormir-f9w | 5-jun-2025 | 18 | 1.594 | 24 | 51 | 1,5 % |
| @ElHistoriadordelaHoradeDormir (cuenta reciclada) | vídeos de hace ~1 año | 22 | 2.418 | 31 | 38 | 1,3 % |
| @HistoriaAburridaparaDormir-r7k | 6-jul-2025 | 16 | 8.388 | 29 | 24 | 0,35 % |
| @Histor.IAs.para.Dormir (vídeos de 8-26 min) | hace 2-3 meses | 10 | ~284 | 3 | 17 | 1 % |
| @HistoriaAburridaParaDormir11 | hace ~1 año | 5 | ~51 | 4 | 6 | 8 % (n minúsculo) |
| **@HistoriaparaDormir-o2n** ("Historis Aburrida para Dormir"), casi diario y de ~3 h, en red con The Nodding Historian | **17-jun-2026** (3,5 meses) | 82 | 76.170 | 1.890 | 107-467 **a 1-4 semanas** (mediana ~210) | 2,5 % |
| @HistoriaAburridaparaDormiry | 5-oct-2025 | 224 | 86.487 | 1.540 | 30-470 recientes (mediana ~74) | 1,8 % |
| @historiaparadormir-l4x (The Nodding Historian) | 19-ago-2025 | 79 | 931.852 | 4.370 | 0,7-20K a 1-4 semanas | 0,47 % |

URLs: `https://www.youtube.com/<handle>/videos` y `/about`.

**Qué se deduce:**
- **El canal nuevo típico de IA, en un mercado ~100 veces mayor que el galego, consigue 20-60 vistas por vídeo en toda su vida.** Esa es la rama baja.
- Los que despegan (2-3 de más de 17, ~15 %) lo hacen con volumen industrial (80-220 vídeos, casi diarios), redes de colaboración y el mercado hispano. Ninguna de las tres cosas está al alcance del promotor en galego.
- A favor del proyecto hay tres cosas:
  - el nicho galego está vacío (no hay ningún canal de historia para durmir en galego [OBS, `research/retornos.md` §4.4]);
  - el promotor puede sembrar a mano en comunidades gallegas;
  - la curaduría puede ser muy superior.
- Eso justifica una base de 2-3 veces la del clónico, no de 10 veces.

### 3.1 bis Contraste directo: los primeros 30 días de canales nuevos (29-09-2026)

La tabla anterior mide vistas **de vida**. Para calibrar el A1 hace falta lo que consigue un canal **sin audiencia** en el **primer mes** de cada vídeo. Se buscaron en YouTube subidas de este mes y esta semana ("historia aburrida para dormir", "historia para dormir", "historia relajante para dormir", "historia medieval para dormir"; filtros de fecha), salieron 64 canales y se midieron los que son nuevos o pequeños [OBS; datos en `model/obs_nuevos_1mes_29-09-2026.txt`]. Solo cuentan vídeos de 1 día a 4 semanas.

| Canal (castellano) | Suscr. / vídeos | n vídeos ≤ 4 sem. | Mediana de vistas | P25-P75 | σ log | Nota |
|---|---|---|---|---|---|---|
| @ViejosCuentos | ? / 24 | 24 | **0** | 0-1 | 0,7 | Clónico puro, historia medieval 2 h |
| @SecretosHistoriaAburrida | ? / 7 | 6 | **1** | 0-4 | 1,6 | Clónico puro |
| @duermeconlaciencia4 | 1 / 28 | 28 | **4** | 2-10 | 0,9 | Clónico puro, casi diario |
| @EstacióndeDescanso | 1 / 6 | 6 | **35** | 4-52 | 1,1 | Historia, 57 min |
| @HistoriaaMediaLuz | 3 / 2 | 2 | 12 y 130 | – | – | Historia, 47-60 min |
| @HistoriasparaDormirconFuji | 12 / 6 | 6 | 85 | 33-207 | 1,5 | Cuentos, 5 h |
| @HistoriaAntesdeDormir-z2x | 155 / 70 | 29 | **109** | 76-174 | 1,2 | Diario, 3 h, en red con The Nodding Historian |
| @undiaenlaedadmedia_tv | 36 / 58 | 5 | 144 | 118-150 | 0,6 | Historia medieval |
| @15historiasextraordinarias | 162 / 7 | 7 | 171 | 137-468 | 2,2 | Un vídeo de 52K |
| @HistoriaParaDormirYT | 211 / 57 | 30 | **284** | 152-392 | 1,0 | Diario, biografías 1,5 h |
| @AdormirconTremendaHistoria | 26 / 6 | 4 | 338 | 317-517 | 0,3 | Historia, 1-2 h |
| @citaparadormir (lote nuevo) | 168 / 11 | 6 | 367 | 96-1.100 | 1,5 | Historia medieval |
| @SusurrosdelMedievo | 446 / 309 | 30 | 694 | 302-1.500 | 1,4 | Red de colaboraciones, 3 h |

**Qué se deduce para el A1 y las puertas:**
- **La distribución es bimodal.** 4-5 de 13 canales están **muertos** (mediana 0-35 vistas por vídeo en su primer mes): el algoritmo no los recomienda. El resto consigue 85-700, casi siempre con cadencia diaria, redes de colaboración o ambas cosas. La mediana de las medianas es **~109**.
- **Sesgo a favor de los vivos:** estos canales salieron en la búsqueda, y YouTube muestra antes lo que tiene vistas. La fracción real de canales muertos es mayor que 5/13; es coherente con el 55 % de rama baja del §5.1.
- **A1 base = 70** queda por debajo de la mediana de un canal nuevo vivo en castellano (109-284). Es lo que corresponde a un mercado ~100 veces menor, compensado en parte por un nicho vacío y la siembra manual. **A1 baja = 25** cae en el grupo de los muertos. **A1 alta = 200** exige comportarse como un canal vivo **en castellano**; por eso la rama alta pesa solo un 12 %.
- **σ ≈ 1,0-1,4** dentro de cada canal: un vídeo puede hacer 4 veces más o menos que su mediana sin que el canal haya cambiado. Esto es lo que obliga a evaluar las puertas por mediana y con probabilidades (§1).
- **Conversión:** @HistoriaParaDormirYT tiene 211 suscriptores con ~57 vídeos de mediana ~280 (≈ 1 %); @HistoriaAntesdeDormir-z2x, 155 con 70 de ~110 (≈ 2 %). Dentro del rango de A6 (1,3-2,5 %).
- **Ya no hay vistas de cola larga "supuestas" a lo grande.** A3 (base) = 8 vistas por vídeo de catálogo y mes: con los 12 vídeos de la E1, ~100 vistas al mes en M6, no ~4.000.

---

## 4. Triangulación: arriba-abajo (mercado galego) y abajo-arriba (comparables)

### 4.1 Arriba-abajo: cuántas personas pueden escuchar esto en galego

Embudo de `research/audiencia.md` §8:
- 2,1 M de internautas de 16 años o más en Galicia;
- × 47,3 % que escucha pódcast o audio largo cada semana [F Prodigioso Volcán];
- × 30,6-37 % que lo usa antes de dormir [F Prodigioso Volcán; NielsenIQ/Audible];
- × **3,6-18 % que acepta consumirlo en galego** [F IGE, EEF 2023, https://www.ige.gal/estatico/html/gl/OperacionsEstruturais/Resumo_resultados_EEF_Galego.html ; el 3,6 % es audiovisual; el 15-18 %, radio y TV];
- × 15-30 % con interés por la historia [S; iVoox: 14 %, 2.º género].

→ **Mercado atendible: unos 2.000-20.000 oyentes habituales** [S].

Pasado a vistas [S: un oyente habitual pone el vídeo unas 8 noches al mes]: **techo físico de 16.000-160.000 reproducciones al mes**. La cuota realista del único canal del nicho es de un **10-30 %**: **1.600-4.800 vistas al mes si el mercado está en el extremo bajo** y 16.000-48.000 si está en el alto.

### 4.2 Abajo-arriba: comparables

| Comparable | Dato | Qué implica |
|---|---|---|
| Clónicos IA nuevos en castellano (§3.1) | 20-60 vistas por vídeo en toda su vida; ~15 % despega | **Suelo y probabilidad base del árbol** |
| Historia en galego en YouTube (TVG, Orgullo Galego, Burla Negra, Carlos Barros) | 300-12.000 vistas por vídeo **acumuladas en 1-4 años y con marca**; canales de 1,7-11,5K suscriptores tras 4-15 años [OBS] | Techo de vida por vídeo a 3 años, **no** punto de partida |
| Historia a Debate (el canal de historia más fuerte en galego) | 9,27K suscriptores desde 2010 [OBS] | El techo de suscriptores en 3 años son unos pocos miles |
| "DUÉRMETE CON las Leyendas… de GALICIA" (castellano, 2 h) | 107.810 vistas en 11 meses [OBS] | Hay demanda de "Galicia para dormir", **pero en castellano** (argumento para la E3) |
| Canales sleep nuevos en castellano (Detrás De La Historia, Historias Para Dormir Oficial) | 59-65K suscriptores y 10-13 M de vistas en 10-13 meses [OBS] | Caso ganador de la E3 |

### 4.3 Cruce (M36)

| M36 | Baja (parada en M6) | Base (mantenimiento) | Base si siguiese en E2 | Alta |
|---|---|---|---|---|
| Vistas/mes del modelo | ~75 (en M6) | 1.715 | 3.260 | 13.440 |
| Cuota del techo **bajo** (16.000) | < 1 % | **11 %** | **20 %** | 84 % |
| Cuota del techo **alto** (160.000) | < 0,1 % | 1 % | 2 % | **8 %** |
| ¿Dentro de la cuota realista del 10-30 %? | – | **Sí**, con el mercado en el extremo bajo | **Sí**, con el mercado en el extremo bajo | Solo si el mercado tiene ≥ 45.000 vistas/mes (≥ 5.600 oyentes habituales, la mitad alta del rango) o si hay desbordamiento a público no galegofalante |
| Vistas de vida por vídeo a ~3 años | ~40 | ~400-650 | ~650 | ~1.500-2.500 |
| ¿Coherente con los comparables galegos? | Sí (= clónico) | Sí: en el extremo bajo de Burla Negra (614-12.072) | Sí | Sí, a la par que TVG u Orgullo Galego, pero sin marca |

**Conclusión de la triangulación.**
- La base es coherente por los dos lados **con el mercado en el extremo bajo**.
- La alta exige un mercado en la mitad superior del rango o desbordamiento. Es un techo plausible, no una previsión. Por eso pesa solo un 10 % en el árbol.
- **Techo publicitario solo-galego** (160.000 vistas × RPM efectivo de 2,56-4,38 €): **~410-700 €/mes**. Todo lo realista queda muy por debajo.

---

## 5. El árbol de decisión

### 5.1 Probabilidades de rama [S, argumentadas]

- **Tasa base [OBS]:** de más de 17 clónicos en castellano, ~15 % supera los 1.000 suscriptores; el resto se queda por debajo de 60.
- **Ajustes para el galego:**
  - a favor: nicho vacío, siembra manual y curaduría;
  - en contra: mercado ~100 veces menor, rechazo cultural a la IA y una cadencia 20 veces menor que la de los clónicos que despegan.
- **Priors de audiencia:** baja 55 %, estancada 13 %, base 20 %, alta 12 %.
- **Riesgo lingüístico o comunitario** (voz o guion que no aguantan 60-90 min, o rechazo de la comunidad al canal IA): **15 %**, independiente de la audiencia. Si se materializa, se para en la P1.
- **Las ramas no se observan directamente:** lo que se observa en cada puerta es la mediana de 4 vídeos con ruido (σ = 1,2, §3.1 bis). De ahí sale la probabilidad de pasar cada puerta en cada rama.

**Árbol con puertas ruidosas** (P1 = 100/30, P2 = 150/150, σ = 1,2; `arbol4_final.py`). Cada hoja indica de qué rama viene:

```
Inicio E1 (−210 €, 102 h)
└─ Puerta 1 (M6)
   ├─ NO (77,7 %) → PARAR con −210 €.                                         Camino P1
   │     = baja 55,0 % (toda la rama + su parte de riesgo lingüístico)
   │     + base 12,4 % + estancada 8,2 % + alta 2,1 % (ruido o galego no validado)
   └─ SÍ (22,3 %) → E2 (110 €/mes)
      └─ Puerta 2 (M12)
         ├─ NO (9,0 %) → PARAR con −870 €.                                   Camino P2
         │     = base 4,8 % + estancada 3,9 % + alta 0,3 %
         └─ SÍ (13,3 %)
            └─ Puerta 3 (M18)
               ├─ NO (3,7 %) → MANTENIMIENTO M19-36 (o cierre), −1.825/−1.890 €. Camino P3
               │     = base 2,8 % + estancada 0,9 %
               └─ SÍ (9,5 %) → YPP en M17, E2 completa + opción de E3, +3.355 €.  Camino P4
                     = alta 9,5 %                └─ ¿abrir E3 en M19? (§7)
Premios y encargos: nodos de azar independientes sobre cada camino (§6).
```

**Probabilidad de pasar cada puerta, condicionada a la rama** (para quien quiera rehacer el árbol a mano): ver la tabla del §1. Con el 15 % de riesgo lingüístico, P(pasar P1) = 0 % (baja), 36 % (estancada), 38 % (base) y 82 % (alta).

**Comparación con la v3 (puertas perfectas):** allí P1 = 61,8 %, P2 = 11,1 %, P3 = 17,0 %, P4 = 10,2 % y valor esperado −147 €. El cambio no viene de ser más optimista con la audiencia (los priors son los mismos), sino de que **el 17 % de probabilidad de llegar a mantenimiento perdiendo ~1.850 € baja al 3,7 %**.

### 5.2 Audiencia por camino

Cada camino muestra la **trayectoria mediana** de la rama que lo recorre. El camino P3 es la rama base **en el 17 % de las realizaciones en que pasa P1 y P2**; su trayectoria mediana no pasaría la P1 (91 vistas / 25 suscr. frente a 100 / 30), y se muestra para saber qué ocurre si la suerte del arranque la deja seguir.

| Métrica | Camino | M6 (mar-27) | M12 (sep-27) | M18 (mar-28) | M36 (sep-29) |
|---|---|---|---|---|---|
| Vídeos publicados | P1 | 12 | parado | – | – |
| | P2 | 12 | 36 | parado | – |
| | P3 base | 12 | 36 | 60 | 78 (1/mes desde M19) |
| | P4 opt. | 12 | 36 | 60 | 132 |
| Vistas de un vídeo nuevo a 30 días | P1 | 26 | – | – | – |
| | P2 | 91 | 91 | – | – |
| | P3 | 91 | 115 | 140 | 175 |
| | P4 | 318 | 459 | 600 | 800 |
| Vistas/mes del canal | P1 / P2 | 74 / 259 | – / 611 | – | – |
| | P3 | 285 | 883 | 1.456 | 1.715 |
| | P4 | 953 | 3.304 | 5.760 | 13.440 |
| Horas de visionado/mes | P3 | 142 | 441 | 728 | 858 |
| | P4 | 635 | 2.202 | 3.840 | 8.960 |
| Horas en 12 meses (umbral 8.000) | P3 | 628 | 2.696 | 5.687 | 9.057 ✓ (desde M32) |
| | P4 | 2.643 | 12.673 ✓ | 28.756 | 86.726 |
| Suscriptores | P1 / P2 | 5 / 24 | – / 88 | – | – |
| | P3 | 25 | 108 | 253 | **758** |
| | P4 | 99 | 475 | 1.177 | 5.486 |
| **Entrada en el YPP** | P3 | – | – | – | **nunca en 36 m** (sin mantenimiento, en M35) |
| | P4 | – | – | **M17 (feb-2028)** | ✓ |
| Fan funding (500 suscr. + 3.000 h) | P3 / P4 | – | – / – | – / M13 | M28 / ✓ |
| Spotify SPP (2.000 h de vídeo en 30 días) | P3 / P4 | – | – | – | nunca / M23 |

**En la P3 el cuello de botella son los suscriptores:** las horas llegan a 8.000, los suscriptores no llegan a 1.000.

### 5.3 Ingresos por fuente (€/mes en el mes indicado)

P1 y P2 tienen 0 € recurrentes en todos los cortes (paran antes de desbloquear nada).

| Fuente | Camino | M6 | M12 | M18 | M36 |
|---|---|---|---|---|---|
| AdSense (anuncios) | P3 | 0 | 0 | 0 | 0 |
| | P4 | 0 | 0 | 16 | 36 |
| YouTube Premium (por horas) | P3 | 0 | 0 | 0 | 0 |
| | P4 | 0 | 0 | 10 | 22 |
| Spotify (videopódcast) | P3 | 0 | 0 | 0 | 0 |
| | P4 | 0 | 0 | 0 | 29 |
| Membresías | P3 | 0 | 0 | 0 | 10 |
| | P4 | 0 | 0 | 33 | 153 |
| Patrocinios (efectivo de 10-20 €/1.000; A14) | P3 | 0 | 0 | 0 | 0 (< 2.000 vistas/mes) |
| | P4 | 0 | 66 | 115 | 269 |
| **Total recurrente** | P3 | **0** | **0** | **0** | **10** |
| | P4 | **0** | **66** | **173** | **509** |
| Premios y encargos | – | Fuera de la tabla: pagos únicos (§6) | | | |

Incluso en el optimista, **AdSense + Premium son el 12 % del ingreso de M36** (58 de 509 €). Lo que pesa es el patrocinio (53 %) y las membresías (30 %).

### 5.4 Costes

**Desglose de caja** [los precios con [F]; la asignación es S]:

| Partida | Etapa 1 (€/mes) | Etapa 2 (€/mes) | Fuente del precio |
|---|---|---|---|
| Guion LLM (frontier + pasadas de revisión) | 7-20 (API a ~3,4 USD por episodio de 2 h, o la suscripción que ya se tenga) | 15-30 | [F] cálculo con precios de la API en `research/voz_guion.md` §2 ; https://www.anthropic.com/pricing |
| Voz TTS | 0 (Nós StyleTTS2 / VITS, Apache-2.0) o 10 (ElevenLabs Creator, 11 USD/mes, 121K créditos ≈ 2 episodios de 60-90 min) | 0-30 (Nós, o ElevenLabs por API a 0,08 USD por 1K caracteres ≈ 7 USD por episodio de 2 h) | [F] https://elevenlabs.io/pricing ; https://elevenlabs.io/pricing/api ; https://huggingface.co/proxectonos/Nos_StyleTTS2-Brais-GL |
| GPU (Colab o alquiler por horas) | 0-10 | 10-20 | [S] con precios de `research/voz_guion.md` §3 |
| Imágenes y montaje | 0-10 | 10-20 | [S] |
| Revisión lingüística humana externa (muestreo del 10-20 % de un episodio al mes) | 0 (promotor y su mujer) | 40-60 | [F secundaria] 0,015-0,03 €/palabra https://correccionencastellano.com/tarifas-correccion-textos/ |
| **Total del modelo** | **35** (rango 25-50) | **110** (rango 75-160); mantenimiento: 20 | |
| Etapa 3 | Inversión inicial de 3.000 € (voz de locutor licenciada: 2.000-6.000 € según la referencia UVA de 1.000-7.500 €) + ~90 €/mes incrementales | | [F] https://escueladedoblajedemadrid.es/blog/alerta-maxima-ante-la-cesion-de-voz-para-aprendizaje-neuronal-de-la-ia-segun-uva/ ; importe del modelo [S] |

No se incluyen la cuota de autónomo ni la fiscalidad: solo aplican si se formaliza la actividad, que es condición de las opciones del §6.2.

**Resultado acumulado por camino a M36** (sin premios ni encargos):

| Camino | Prob. | Ingresos | Caja | Horas | Resultado de caja | Con horas a 15 €/h | € por hora |
|---|---|---|---|---|---|---|---|
| P1 Parada en P1 (M6) | 77,7 % | 0 | 210 | 102 | **−210** | −1.740 | −2,1 |
| P2 Parada en P2 (M12) | 9,0 % | 0 | 870 | 312 | **−870** | −5.550 | −2,8 |
| P3 Base → mantenimiento (estancada: −1.890) | 3,7 % | 65 | 1.890 | 666 | **−1.825** | −11.815 | −2,7 |
| P4 Optimista (E2 completa) | 9,5 % | 6.865 | 3.510 | 1.152 | **+3.355** | −13.925 | +2,9 |

Coste de **no** tener disciplina: la rama baja sin parar en la P1 pierde **−3.510 €** y 1.152 h a M36, sin llegar a 120 suscriptores.

---

## 6. Premios, encargos y subvenciones: qué tiene tasa base y qué no

La crítica a la v2 era correcta: el signo del valor esperado dependía de probabilidades de ayudas sin tasa base. En esta versión solo entra en el caso central lo que tiene una tasa observable.

### 6.1 Youtubeiras+: con tasa base → entra en el caso central

**Datos de ediciones anteriores** [F, páginas de cada edición: https://youtubeiras.gal/ix-edicion-2025/ , https://youtubeiras.gal/viii-edicion-2024/ , https://youtubeiras.gal/setima-edicion/ ; palmarés: https://youtubeiras.gal/palmareshistorico/]:

| Edición | Canales presentados | Premios de jurado con dotación | Canales por premio | Finalistas |
|---|---|---|---|---|
| VII (2023) | 68 | 7 (+ premio del público) | ~10 | – |
| VIII (2024) | 89 (40 de TikTok y 49 de YouTube) | 6 (+ público) | ~15 | – |
| IX (2025) | **126** (récord) | 6 (+ público) | **21** | 28 (4 por categoría) [F titular de El Correo Gallego del 21-01-2026, "Youtubeiras+ bate récords de concurrencia con 126 canales y un total de 28 finalistas", visto en Google News sin URL directa; cuadra con 7 categorías × 4 finalistas] |
| X (2026) | ¿~150-175? [S: tendencia de +30-40 % al año] | 6 (+ público y el honorífico) | ~25-30 | 4 por categoría [F bases 2026] |

No se publican los inscritos **por categoría**: la inscripción es por canal y el jurado asigna las categorías [F bases 2026, §4-5]. Por eso la tasa se calcula por canal.

**Perfil de los ganadores** [OBS, búsqueda de canales en YouTube el 29-09-2026; coincidencia por nombre, sin verificar la identidad canal a canal]:
- O Faiado Podcast (Revelación 2023): **515 suscriptores**.
- Exército Mekemeke (Canle YouTube 2024): **803**.
- Luís do Río Pena (Calidade lingüística 2024): **2,1K**.
- Galiactiva (Revelación 2024): **56** en YouTube (su actividad principal parece estar en otra red).
- **Se gana con canales pequeños.** Al jurado no le pesa el tamaño: valora la calidad lingüística, el contenido, la calidad técnica y las "dotes interpretativos e/ou comunicativos" [F bases 2026, §7].
- **La historia de Galicia premia con regularidad:**
  - "Falemos do Reino de Galicia" (Calidade lingüística 2022);
  - "Histérikas Histórikas" (Revelación 2022);
  - Orgullo Galego (Público 2021 y 2024, con vídeos de historia medieval y de 1846).
- **Voz sintética:** no se ha encontrado ningún ganador con voz de IA. No se ha comprobado vídeo a vídeo [S]. El criterio de "dotes interpretativos" juega en contra de una voz TTS mediocre.

**Probabilidades que usa el modelo:**
- **Edición 2026** (fallo en febrero de 2027, con el contenido publicado hasta el 15-nov-2026):
  - Tasa bruta: 6 premios / 126-150 canales = **4,0-4,8 %** de ganar alguno. Para las cuatro categorías a las que opta este canal (Revelación, Calidade lingüística, Pódcast y Canle), **2,7-3,2 %**.
  - Ajuste a favor: tema de historia con historial de premios; formato inédito en galego, que es justo lo que valora Revelación.
  - Ajuste en contra: voz IA y solo ~3 piezas publicadas.
  - **Modelo: 4 %, igual en todos los caminos**, porque el jurado juzga antes de que se revele la audiencia.
- **Edición 2027** (solo P3 y P4, que siguen publicando): **6 % en el base y 8 % en el optimista** [S]. Es la tasa bruta de ~4 %, algo mejorada por tener un año de catálogo y audiencia; se cuida de no pasar de 2 veces la tasa base.
- **Premio neto: 810 €** (1.000 € − 19 % de retención) [A20]. Ser **finalista** (~24 plazas de jurado / 126 canales ≈ 19 %) no tiene premio en metálico, pero da visibilidad en prensa gallega. No se modela.
- **E[Youtubeiras+] por camino:** 32 € (P1 y P2), 81 € (P3), 97 € (P4). **+41 € en el valor esperado global** (v3: +47 €; baja porque ahora siguen publicando menos caminos). Poco, pero real.

### 6.2 Encargo de la CRTVG: sin tasa base → opción aparte

**Lo que se sabe** [F]:

| Edición | Plazas y dotación | Resultado | Fuente |
|---|---|---|---|
| 2023 | "Máis de 300.000 €"; piezas largas a 20.000 € y cortas a 6.000 € | **25 proyectos** seleccionados; no se publican los presentados | https://www.crtvg.gal/gl/web/crtvg/w/a-crtvg-producir%C3%A1-25-novos-proxectos-nativos-dixitais-en-galego (26-12-2023) |
| 2024 | Hasta 25.000 € por proyecto | **12 proyectos y 300.000 €**. Entre ellos, **"Respira", de Margherita Morello: una serie de meditaciones guiadas en galego** (persona física). Es el comparable más cercano a un formato para dormir | https://www.audiovisual451.com/crtvg-producira-doce-nuevos-proyectos-nativos-digitales-en-gallego/ (22-10-2024) |
| 2025 | **15 plazas y 357.000 €** en 5 categorías: ficción 3 × 35.000; entretenimiento, divulgación e infantil 3 × 26.000; **videopódcast 3 × 6.000** | **12 seleccionados y 339.000 €**: 3 de ficción, 3 de entretenimiento, 3 de divulgación y 3 de infantil. **Ningún videopódcast.** La suma cuadra exactamente: 3 × 35.000 + 9 × 26.000 = 339.000. En divulgación, 2 de 3 son sociedades y la tercera es la T2 de un seleccionado anterior | Bases: https://www.crtvg.es/documents/d/crtvg/convocatoriaasinada09xuno2025contidosdixitais-pdf-1 ; resolución (PDF del 04-12-2025): https://www.crtvg.es/documents/d/crtvg/a-corporacion-de-servizos-audiovisuais-de-galicia-pdf ; convocatoria: https://www.audiovisual451.com/la-crtvg-abre-una-nueva-convocatoria-para-la-produccion-de-contenidos-digitales-destinados-a-sus-plataformas/ (11-06-2025) |

**Número de propuestas presentadas:** **no se publica** en ninguna de las tres ediciones. Se han revisado las notas de la CRTVG de 2023, audiovisual451 de 2022, 2024 y 2025, el PDF de la resolución de 2025 y la prensa agregada en Google News. **No hay tasa base.**

**Lo que dicen las bases de 2025.** El PDF de 23 páginas está escaneado; se renderizó página a página y se transcribió. Extracto literal en `gauntlet/crtvg/bases2025_extracto.txt`.

| Aspecto | Texto de las bases [F] | Consecuencia para el plan |
|---|---|---|
| **Quién puede presentarse** | "persoas físicas ou xurídicas constituídas como produtoras independentes e dadas de alta no IAE"; tras la selección, "en caso de persoa física, o xustificante de alta en autónomos" (pp. 2 y 6) | **Exige alta formal.** No encaja en la Etapa 1. En la Etapa 2 supone la cuota de autónomo y la gestión fiscal |
| **Inédito** | "ineditos, integramente orixinais e que non foran postos a disposición do público a través de internet", salvo nuevas temporadas de proyectos ya seleccionados (p. 2) | Ni el catálogo del canal ni un episodio ya publicado sirven. Tiene que ser una **temporada aparte, sin publicar** |
| **Derechos** | Reproducción y comunicación pública (incluidos internet, VOD y redes) "en exclusiva, con facultade de cesión exclusiva a terceiros, para todo o mundo e polo tempo máximo … ata a entrada da obra no dominio público", más el derecho de transformación, "incluída a dobraxe e/ou subtitulación a todas as linguas" (pp. 10-11) | La temporada **no podrá publicarse en el canal ni localizarse a es/pt en la E3**. Se vende, entera y para siempre |
| **Autoría** | Anexo III: declarar ser "única titular en réxime de exclusiva … dos dereitos de propiedade intelectual sobre o argumento e guión" | Con un guion generado por IA, la autoría humana tiene que ser real y demostrable (reescritura y curaduría del promotor). Si no, la declaración es arriesgada [S, interpretación] |
| **IA** | **No se menciona en ninguna página** (pp. 1-23 revisadas) | Ni prohibida ni regulada. El riesgo está en los criterios: "presenza no elenco … de persoas que constitúan un reclamo" (Calidade, 25 puntos) y la aprobación de la "calidade lingüística" del primer programa, que la productora corrige a su costa (pp. 7 y 14) |
| **Baremo** | Calidade 25; **Xestión responsable 40**, que incluye "adecuación orzamentaria en comparanza cos outros concorrentes"; Cultura 7; Galicia 7; Lingua 4; Talento 5; Comercialización 5; Innovación 5; Accesibilidade 2; mínimo 51 (pp. 8-9) | Un presupuesto bajo y creíble puntúa. **Es la ventaja de un pipeline IA**: poder ofrecer divulgación por debajo de 26.000 € |
| **Entrega** | ≤ 6 meses; MXF 1080p50 XAVC 50 Mbps, EBU R128, pistas separadas (M+E, locución, músicas libres de derechos), teaser, tráiler y extra para redes (pp. 12-14) | Hace falta un coste técnico y horas que el modelo no tiene; de ahí que el neto del encargo sea ~50 % del bruto |

**La CRTVG como opción.** Supuestos del valor si se gana [S]: divulgación a ~15.000 € brutos y **7.500 € netos** tras producción extra, alta de autónomo, entregables técnicos e impuestos; ~60 h extra. Solo optan P3 y P4, que siguen activos en la convocatoria de jun-sep 2027.
- **Probabilidad mínima para que compense (`arbol4_final.py`):**
  - el valor esperado global ya es ≈ 0 (+50 €) sin ella; la opción solo lo sube;
  - **≥ 23 %** rescata el camino base que llegue a mantenimiento (de −1.744 € a 0).
- **Valor esperado global si la probabilidad fuese** (solo optan los caminos P3 y P4, que suman el 13,3 %):
  - 5 % → +100 €;
  - 10 % → +149 €;
  - 25 % → +298 €.
  - Es ilustrativo: **no hay dato para elegir entre ellas.** Con puertas más estrictas, la opción CRTVG vale menos en el global (v3: +57 € al 10 %, pero partiendo de −147 €) porque llegan menos caminos a ejercerla.
- **Lectura sin tasa base:**
  - Ganar supone ser 1 de 3 plazas en divulgación, frente a productoras con equipo y presentador.
  - La categoría de videopódcast quedó desierta en 2025. Puede significar poca competencia o un listón que nadie pasó; no se sabe.
  - Una referencia **no equivalente** es Youtubeiras+, donde gana ~1 de cada 21 canales. Si la CRTVG fuese parecida (~5 %), la opción añadiría ~+50 € al global y no rescataría el camino base (necesita ≥ 23 %).
  - **Recomendación:** tratarla como una opción que se ejerce **solo si se pasa la P3** y el promotor acepta darse de alta. Hay que preguntar a proxectosav@crtvg.gal el número de propuestas de 2025 antes de invertir horas.

### 6.3 B2B, Xacobeo y Ministerio: sin tasa base o fuera de alcance

| Vía | Por qué no entra en el caso central | Umbral para que compense |
|---|---|---|
| B2B concellos / museos (1.000-6.000 € por encargo; neto ~2.450 €; ~30 h) | No hay ninguna tasa de conversión observada. Requiere venta activa y facturar (alta) | Ya no hace falta para un valor esperado ≥ 0; con 10 %/año sería +115 € y con 20 %/año, **+180 €** (20 % × 3.500 € brutos = 700 €/año brutos, ~490 €/año netos por camino activo; solo P3 y P4, 13,3 %) |
| O teu Xacobeo (oct-2026) | Alta formal ya en octubre de 2026 y serie del Camino | – (no aplica a la E1) |
| Ministerio: innovación ICC | Cofinanciado al 70-80 %: financia gasto, no deja margen | – (E3) |

**Corrección de la v2 que se mantiene:** el B2B a 20 %/año × 3.500 € equivale a 700 €/año brutos, no a ~300 €. Pero ya no se suma al caso central.

---

## 7. Etapa 3 superpuesta (solo en el camino P4)

Supuestos [S]:
- Se reutilizan la investigación y el guion; se traduce al castellano y al portugués.
- Se publica en pistas de audio multilingües o en canales espejo.
- Rampa lineal desde M19.
- RPM mixto España/LatAm/Portugal de 2 € [F: LatAm paga mucho menos, https://aceleratusredes.com/blog/cuanto-paga-youtube-por-pais-en-2026].
- 3.000 € de inversión, 90 €/mes y +8 h/mes.
- Aviso: una temporada vendida a la CRTVG **no se puede localizar** (cesión del derecho de doblaje, §6.2). La E3 solo usa el catálogo propio.

| Rama E3 | Prob. condicionada [S] | Vistas es+pt/mes en M36 | Ingreso E3/mes en M36 | Ingreso E3 acumulado | Resultado E3 a M36 |
|---|---|---|---|---|---|
| Fracasa (un clónico más, §3.1) | 55 % | 5.000 | 10 € | 95 € | **−4.525 €** |
| Modesta | 25 % | 72.000 | 144 € | 1.368 € | **−3.252 €** |
| Buena | 15 % | 360.000 | 720 € | 6.840 € | **+2.220 €** |
| Ganadora (como Detrás De La Historia, ~1 M vistas/mes al año) | 5 % | ~1.000.000 | ~2.000 € | 19.000 € | **+14.380 €** |
| **Valor esperado** | | | **~250 €/mes** | | **−2.250 €** |

- Las probabilidades salen de la tasa de éxito de los clónicos (~15 %), mejorada por un pipeline ya validado y la voz licenciada. Aun así, la mayoría fracasa.
- **Valor esperado negativo a 36 meses.** Con ~250 €/mes esperados frente a 90 €/mes de caja, se recupera hacia el **mes ~50**. Es una opción con cola larga (el caso ganador da ~2.000 €/mes), no una inversión que se pague dentro del horizonte.
- **Variante "E3 ligera"** [S]: localizar primero solo al castellano con TTS maduro, sin licenciar voz (~500 € + 60 €/mes). Con las mismas probabilidades, el valor esperado a M36 sería de ~+790 €. Es probable que baje la tasa de éxito, así que se propone como experimento previo a licenciar voz, no como caso base.
- En el total del plan, abrir la E3 en M19 cambia el valor esperado central a M36 de +50 € a **−164 €** (el 9,5 % del camino P4 × −2.250 €).

---

## 8. Valor esperado, punto de equilibrio y retorno por hora

### 8.1 Valor esperado ponderado a M36

| Concepto | Caso central (v4, puertas ruidosas) | Referencia: sin premios | Opción: + CRTVG al 10 % [ilustrativo] | v3 (puertas perfectas) |
|---|---|---|---|---|
| Ingresos recurrentes esperados | 656 € | 656 € | 656 € | 711 € |
| Caja gastada esperada | 647 € | 647 € | 647 € | 905 € |
| E[premios y encargos] | +41 € (Youtubeiras+) | 0 | +140 € | +47 € |
| **Resultado de caja** | **+50 €** | +9 € | +149 € | −147 € |
| Horas del promotor esperadas | 242 h | 242 h | 243 h | 328 h |
| **Retorno por hora** | **+0,21 €/h** | +0,04 €/h | +0,61 €/h | −0,45 €/h |
| Con horas a 15 €/h | −3.582 € | −3.622 € | −3.496 € | −5.070 € |
| Abriendo la E3 en P4 | −164 € | −205 € | −65 € | −376 € |

**Distribución del caso central** (enumerando premios ganados y no ganados; `arbol4_final.py`):

| Indicador | Valor |
|---|---|
| Resultado mediano | **−210 €** (parar en la P1) |
| P(resultado > 0) | **12,7 %** (P4: 9,5 %; P1 o P2 + Youtubeiras+: 3,2 %) |
| P(resultado ≥ +3.000 €) | 9,5 % (solo P4) |
| P(pérdida ≥ 800 €) | 12,4 % (P2 y P3; en la v3, 27,6 %) |
| Pérdida máxima con disciplina de puertas | −1.890 € (estancada que llega a mantenimiento sin premio; 0,9 %) |

**Cómo leer el +50 €.** No es "el proyecto da dinero". Es **cero con ruido**: el intervalo de sensibilidad va de −339 € a +279 € (§9.2), y la mediana es perder 210 €. Lo que sí ha cambiado es la **forma** del riesgo: la probabilidad de perder más de 800 € baja del 27,6 % al 12,4 % porque la P1 estricta corta la rama base, que es la que más pierde. Ni la v3 (−147 €) ni la v4 (+50 €) permiten decir que el canal sea rentable en valor esperado; las dos dicen que **es un experimento de ~200 € con una cola derecha del ~10 %**.

**Comparación con la v2.** El +796 € y el 24,5 % de probabilidad de acabar en positivo siguen descartados: salían de dar a la CRTVG un 10-25 % y al B2B un 20-50 %/año sin ninguna tasa base.

### 8.2 Punto de equilibrio

| Punto de equilibrio | P1 | P2 | P3 base | P4 opt. |
|---|---|---|---|---|
| **Mensual de caja** (ingresos del mes ≥ caja del mes) | – | – | Nunca | **M15 (dic-2027)** |
| **Acumulado de caja** | – (salvo que gane Youtubeiras+: +600 €) | Nunca | Nunca en el caso central; solo si se ejerce y se gana la opción CRTVG | **M25 (oct-2028)** |
| Con horas a 15 €/h | Nunca | Nunca | Nunca | Después de M36 (2,9 €/h) |

Solo el camino optimista cumple el objetivo de la Etapa 2 ("recurrente ≥ caja en 12-18 meses"), y lo hace en M15. Es coherente con la Puerta 3: la base no la pasa y baja a mantenimiento (solo el 3,7 % de los casos llega hasta aquí; lo normal es que la base ya haya parado en P1 o P2).

**¿Compensa el mantenimiento del P3?** Cuesta ~300 € y 144 h en M19-36. En el caso central solo compra un 6 % de probabilidad de ganar Youtubeiras+ 2027 (~49 €) y la opción CRTVG. **Sin la opción CRTVG no compensa: es mejor cerrar en M18** y ahorrar ~250 €. Con la opción, compensa solo si la probabilidad de ganarla es ≥ ~3,3 % [cálculo: ~250 € ahorrados / 7.500 € netos]. El ahorro de ~250 € sale de 360 € de caja, menos 65 € de ingresos recurrentes y menos 49 € de E[Youtubeiras+ 2027]. La decisión va en la P3 (§11).

---

## 9. Sensibilidad: qué variable manda

### 9.1 Dentro de un camino (una variable cada vez, entre sus valores de rama baja y alta; E2 continua a M36)

| Variable (rango) | Base: mes del YPP | Base: ingreso M36 | Base: caja M36 (−3.071 €) | Optimista: ingreso M36 | Optimista: caja M36 (+3.355 €) |
|---|---|---|---|---|---|
| **Cola larga** (2 → 20 vistas por vídeo y mes) | nunca → M26 | 7 → 117 € | −3.503 → −2.102 | 166 → 509 € | **−958 → +3.355** |
| **Crecimiento del canal** (+20 % → +200 %) | nunca → M29 | 8 → 87 € | −3.480 → −2.528 | 165 → 509 € | **−1.311 → +3.355** |
| **Patrocinio efectivo** (0 → 20 € por 1.000 vistas; es decir, tasa de venta de 0 → 80 % con CPM de 25 €) | = | 22 → 87 € | −3.390 → −2.752 | 241 → 509 € | **−720 → +3.355** |
| Vistas de un vídeo nuevo (×0,5 → ×2) | nunca → M30 | 41 → 68 € | −3.213 → −2.710 | 440 → 648 € | +2.028 → +5.977 |
| Conversión a suscriptor (1,3 % → 2,5 %) | nunca → M32 | 42 → 58 € | −3.151 → −3.004 | 436 → 509 € | +2.307 → +3.355 |
| Membresías (0,3 % → 1 %) | = | 48 → 64 € | −3.127 → −2.996 | 402 → 509 € | +2.153 → +3.355 |
| **AVD** (20 → 60 min), solo vías de monetización (ver §9.3 para la vía de recomendación) | = | 53 → 57 € | −3.072 → −3.068 | 466 → 535 € | **+2.858 → +3.779** |
| Anuncios (0,40 → 0,90 € por 1.000 impresiones) | = | 53 → 58 € | −3.073 → −3.068 | 489 → 509 € | +3.087 → +3.355 |
| Premium (1,0 → 2,5 € por 1.000 h) | = | 54 → 56 € | ≈ | 496 → 509 € | +3.177 → +3.355 |
| Horas de vídeo en Spotify (10 % → 40 %) | = | = | = | 481 → 509 € | +3.060 → +3.355 |

### 9.2 Sobre el árbol (valor esperado de caja a M36; caso central +50 €)

| Variable | Rango | Valor esperado a M36 | P(> 0) |
|---|---|---|---|
| **P(rama alta)** | 5 % ↔ 20 % (equilibrio: ~10,3 %) | **−151 € ↔ +279 €** | 7,3 % ↔ 18,8 % |
| **Patrocinios** | ninguno ↔ modelo | **−339 € ↔ +50 €** | 4,2 % ↔ 12,7 % |
| **Umbral de la P1** | 60/20 (v3) ↔ 100/30 ↔ 150/40 (con P2 = 100/100) | −69 € ↔ +28 € ↔ +80 € | – |
| Ruido por vídeo (σ) | 0,6 ↔ 1,2 ↔ 1,5 | +155 € ↔ +50 € ↔ 0 € | 13,6 % ↔ 12,7 % ↔ 12,0 % |
| P(rama baja) | 70 % ↔ 40 % | −26 € ↔ +126 € | 9,8 % ↔ 15,5 % |
| Riesgo lingüístico | 30 % ↔ 5 % | +10 € ↔ +77 € | 11,1 % ↔ 13,7 % |
| Youtubeiras+ | ×0 ↔ ×2 de la tasa base | +9 € ↔ +90 € | 9,5 % ↔ 15,8 % |
| **Opción CRTVG** (si se ejerce) | 0 % ↔ 10 % ↔ 25 % | +50 € ↔ +149 € ↔ +298 € | 12,7 % ↔ 13,0 % ↔ 13,6 % |
| Opción B2B (si se ejerce) | 0 ↔ 10 % ↔ 20 %/año | +50 € ↔ +115 € ↔ +180 € | 12,7 % ↔ 13,4 % ↔ 14,0 % |
| Abrir la E3 en M19 | no ↔ sí | +50 € ↔ −164 € | – |
| Valor de la hora | 0 ↔ 15 ↔ 25 €/h | +50 € ↔ −3.582 € ↔ −6.000 € | – |

### 9.3 La AVD, modelada por tiempo de visionado y por recomendación

En la v1 la AVD salía "sin efecto" porque Premium se pagaba por vista. Desde la v2, Premium se paga **por hora** (A8), los anuncios por impresión en función de la AVD (A7b), y las horas cuentan para los umbrales del YPP, las membresías y Spotify. Aun así, la AVD pesaba poco (tabla §9.1) porque **en la rama base nunca se entra en el YPP**: sin YPP, la AVD no cobra nada. Falta la vía por la que la retención más importa en YouTube: **la recomendación**. Se añade como variante [S] con elasticidad 0,5 (crecimiento y cola larga × (AVD / AVD de la rama)^0,5), sin fuente publicada que dé la elasticidad real:

| Camino (siguiendo el plan de puertas) | AVD 20 min | 30 min | 40 min | 60 min |
|---|---|---|---|---|
| Base (P3 → mantenimiento), **sin** acoplar: resultado a M36 | −1.825 € | −1.825 € (ref.) | −1.825 € | −1.825 € |
| Base, **con** AVD → recomendación | −1.869 € (594 suscr.) | −1.825 € | −1.735 € | **−1.299 €** (YPP en M33) |
| Optimista (P4), **sin** acoplar | +2.858 € (AdSense + Premium M36: 44 €/mes) | +3.120 € | +3.355 € (ref.) | +3.779 € (70 €/mes) |
| Optimista, **con** AVD → recomendación | **+549 €** | +1.884 € | +3.355 € | **+6.281 €** |

**Lectura.** Por las vías de monetización, la AVD vale ~900 € en 36 meses en el optimista y nada en la base. Por la vía de recomendación, **la AVD pasa a ser, con el patrocinio, la variable que más mueve el camino que paga** (de +549 € a +6.281 €). Y la AVD depende de lo que el promotor controla: la calidad de la voz y del guion en galego durante 60-90 min. Por eso la P1 exige AVD ≥ 20 min y el piloto la mide desde el primer vídeo (§11).

**Qué dicen las tablas:**

1. **Manda la probabilidad de estar en la rama alta, y eso lo decide la audiencia, no la plataforma.** El valor esperado cruza el cero con P(alta) ≈ 10 % (prior: 12 %). Dentro de un camino mandan la **cola larga** (reescucha del catálogo), el **crecimiento** y, si la retención alimenta la recomendación, la **AVD**. Las tres dependen de la calidad del galego y del guion: es la palanca económica, no un coste.
2. **El patrocinio decide el signo** (−339 € sin él). Tiene un precio anclado en el mercado (10-40 €/1.000 [F]); lo incierto es la **tasa de venta** a marcas gallegas, que se mide antes de M12.
3. **La disciplina de puertas vale ~120-230 €** de valor esperado (de −69 € con la P1 blanda de la v3 a +50/+80 € con la estricta) y **reduce a la mitad la probabilidad de perder más de 800 €**. Es la decisión más barata y más rentable de todo el plan.
4. **Las ayudas grandes (CRTVG, B2B) no cambian el veredicto.** Suben el valor esperado ~100-250 € si se ejercen, pero solo en el 13 % de los caminos que siguen activos tras M12 y sin tasa base.
5. **El RPM, los anuncios y Spotify casi no importan en galego.** Optimizar mid-rolls no cambia el resultado de las Etapas 1-2.
6. **El valor de la hora cambia la foto por completo.** Es un hobby con opción de negocio, no un negocio.

---

## 10. Conclusión honesta: el techo

| Configuración | Ingreso recurrente plausible en M24-36 | Techo teórico | Qué hace falta |
|---|---|---|---|
| **Solo galego, solo YouTube (AdSense + Premium)** | Base: **0 €** (sin YPP en 36 m). Optimista: ~35-60 €/mes | ~410-700 €/mes capturando todo el mercado atendible alto (§4.3) | Nada más; es el mínimo |
| **Solo galego + fuentes directas** (membresías, Spotify/iVoox, patrocinios) | Base: ~10 €/mes. Optimista: ~275-510 €/mes | ~1.500-2.000 €/mes [S: techo publicitario + 300 mecenas + 2 patrocinadores] | Audiencia de la rama alta, comunidad y venta activa a marcas gallegas |
| **Solo galego + premios** (con tasa base) | E[Youtubeiras+] de 32-97 € por camino; 810 € si toca | ~1.600 €/año (dos premios por edición como máximo) | Publicar 3 piezas antes del 15-nov y cuidar la lengua |
| **Solo galego + encargos públicos o B2B** (opción, sin tasa base) | 0 € en el caso central; **+7.500 € netos de golpe si toca la CRTVG** | Encargo CRTVG anual (≤ 26.000 € brutos en divulgación) + B2B | **Alta de autónomo**, una temporada inédita, **ceder los derechos para siempre**, entregables de emisión; con ~5-10 % de probabilidad añade +50-100 € al valor esperado global, y para rescatar el camino base haría falta ≥ 23 % |
| **Etapa 3 (es/pt + voz licenciada)** | Valor esperado de **−2.250 € a M36**; ~250 €/mes esperados en M36 | **~2.000 €/mes o más** (caso ganador en castellano, 5 %) | Pasar las Puertas 1-3 y un horizonte de 4-5 años |

**Veredicto.**
1. **El resultado más probable (78 %) es parar en el mes 6 con −210 €, y eso incluye a la mayoría de los escenarios "base".** No es un fracaso del plan: es el plan funcionando. La Etapa 1 compra, por el precio de una cena al mes, la respuesta a tres incógnitas: si hay audiencia en galego, si la voz y el guion aguantan 60-90 min, y si la comunidad acepta un canal de IA declarado.
2. **El valor esperado a 36 meses es cero: +50 € de caja (intervalo −340 € a +280 €) y ~240 h.** La v2 decía +800 € (ayudas sin base) y la v3, −147 € (puertas que no separaban la base de la alta). Con puertas que solo dejan pasar a lo que se parece a la rama alta, la pérdida es pequeña y está acotada (probable, 210 €; más de 800 €, solo un 12 %; máxima, ~1.900 €). Encaja con la regla del promotor ("inversión perfectamente viable") **como experimento, no como inversión rentable**.
3. **Como negocio, el canal solo-galego se paga a sí mismo únicamente en el ~10 % optimista:** ~500 €/mes en M36 y +3.355 € de caja, sostenidos por el patrocinio y las membresías, no por AdSense. La base no entra ni en el YPP en 36 meses, y por eso el plan la corta pronto.
4. **El dinero público es una opción, no un plan.** La CRTVG es la única pieza que cambia la escala (+7.500 € netos), pero exige alta, una temporada inédita y ceder los derechos para siempre. Y no hay dato para saber si 1 de cada 5 o 1 de cada 50 propuestas gana. Se ejerce en la P3, con la tasa preguntada a la CRTVG antes.
6. **Techo en una frase.** Solo-galego con YouTube: decenas de €/mes. Solo-galego con patrocinio y comunidad: ~500 €/mes en el 10 % bueno y un techo teórico de ~1.500-2.000 €/mes. Con subvenciones: pagos únicos de 810 € (Youtubeiras+) a ~7.500 € netos (CRTVG) que no cambian el valor esperado más de ~250 €. Con Etapa 3: la única vía a miles de €/mes, al 5 %, y a 4-5 años.
5. **La Etapa 3 es una opción de cola larga, no una promesa.** Con valor esperado negativo a 36 meses, solo se abre si se pasa la P3 y se acepta un horizonte de 4-5 años. Antes conviene probar la "E3 ligera" (§7).

---

## 11. Qué sustituye el piloto (y cuándo recalibrar)

| Supuesto crítico | Dato real que lo sustituye | Cuándo |
|---|---|---|
| A1 y la rama de audiencia | **Mediana** de vistas a 7 y 30 días de los vídeos 1-4, comparada con 25 (clónico) / 70 (base) / 200 (alta), y dispersión real (σ) entre vídeos | Tras 4 vídeos (mes 2). **Recalibrar aquí los umbrales de la P1 con la regla "¿se parece a la alta?"**: si la mediana de los vídeos 1-4 es < 40 y no crece, la P1 casi seguro fallará y se puede parar antes, en M4, ahorrando ~70 € |
| A3 (cola larga): la variable que más manda | Vistas mensuales de los vídeos con más de 60 días | M4-M6 |
| A6 (conversión a suscriptor) | Suscriptores ganados / vistas por vídeo | P1 |
| A5 (AVD) y su efecto en la recomendación | Retención y AVD en Studio desde el vídeo 1; relación entre AVD y tráfico de "vídeos sugeridos"/"Explorar" entre vídeos del propio canal (estima la elasticidad del §9.3) | Desde el vídeo 1; primera lectura en la P1 |
| A7b (efecto de los mid-rolls) | Test A/B de 0 frente a 2 mid-rolls | Tras entrar en el YPP |
| Desbordamiento a no galegofalantes | Geografía e idioma de la audiencia en Studio | Desde el primer vídeo |
| **A14: tasa de venta del patrocinio** | Respuestas y precios cerrados en 5-10 propuestas a marcas gallegas (el CPM ya está anclado) | M9-M12 (condición de la P2) |
| Probabilidad de Youtubeiras+ | Resultado de la edición 2026: finalista sí o no | Listado de finalistas (~ene-2027) y gala (feb-2027) |
| **Tasa de la CRTVG** | Pedir a proxectosav@crtvg.gal el número de propuestas por categoría de 2025; leer las bases de 2027 (¿mencionan la IA?) | Antes de la P3 (mar-2028); convocatoria ~jun-2027 |
| ¿Mantenimiento o cierre en la P3? | Si la tasa de la CRTVG es < ~3 % o el promotor no quiere darse de alta → **cerrar** en M18 | P3 |

**Riesgos que el modelo no cuantifica** (ver la sección de riesgos del plan):
- Desmonetización por "contenido inauténtico" [F] https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/.
- Confirmación del uso comercial de las voces de Nós (`research/voz_guion.md` §0.5).
- Autoría del guion generado con IA. La CRTVG exige declarar la titularidad exclusiva del guion (Anexo III); el mismo problema aparecería en cualquier cesión o encargo.
- Rechazo de la comunidad cultural galega a la IA (solo entra como el 15 % de riesgo lingüístico o comunitario).
- Cambios de reparto de las plataformas.
- Que el requisito de 1.000 suscriptores del YPP cambie en 2027.

---

## 12. Registro de cambios

### v3 → v4 (respuesta punto por punto al crítico de esta ronda)

Parte de lo señalado ya estaba corregido en la v2 o la v3 (se indica). Donde el crítico tenía razón de fondo, se ha ido más lejos.

| Carencia señalada | Estado en la v4 | Dónde |
|---|---|---|
| El base (103 suscr. en M6) no pasaba la P1 (≥ 150) y aun así se proyectaba a M36 | Los números citados eran de la v1. En la v3 la P1 se había bajado a 60/20 para que el base pasara; **eso era la mitad mala del arreglo**: con ruido, esa puerta no separaba la base de la estancada (24 % frente a 24 % de parada). La v4 hace lo contrario: **P1 = 100/30, la trayectoria mediana del base no pasa** y el camino realista del base es **parar en M6 con −210 €** (55 %) o en M12 con −870 € (28 %) | §0, §1, §5.1 |
| A1 anclado en vistas acumuladas de canales con marca (450 → 855) y ~4.000 vistas/mes de cola larga | Ya corregido en la v2 (A1 base = 70, cola = 8 vistas por vídeo y mes). **Nuevo:** contraste con los **primeros 30 días** de 13 canales nuevos (muertos 0-35, vivos 85-700, σ ≈ 1,2) | §3, §3.1 bis |
| Faltaba un árbol con probabilidades explícitas de pasar cada puerta | La v3 las tenía por rama, pero deterministas. **Nuevo:** matriz de confusión simulada (20.000 realizaciones por rama) y árbol con la composición de cada hoja | §1, §5.1 |
| Faltaba el valor esperado ponderado a M36 | **+50 € de caja**, 242 h, +0,21 €/h, −3.582 € con horas a 15 €/h; distribución completa y comparación con la v3 | §8.1 |
| Premium y anuncios por vista; "AVD sin efecto" | Premium por hora y anuncios por impresión = f(AVD) desde la v2. **Nuevo:** se explica por qué la AVD pesaba poco (sin YPP no cobra) y se añade la vía de recomendación: en el optimista mueve el resultado de +549 € a +6.281 € | §3 (A5), §9.3 |
| B2B mal calculado (~300 €/año en vez de ~700 €/año) | Corregido desde la v3: 20 % × 3.500 € = 700 €/año brutos (~490 € netos). En la v4: +180 € de valor esperado con 20 %/año | §6.3 |
| "El base queda justo por suscriptores" en la P1 | La frase ya no existe. La v4 dice lo contrario y lo cuantifica: el base **no pasa** la P1 en su mediana | §1 |
| Spotify: umbrales atribuidos a Infobae y modelados como horas de audio | TechCrunch verificado hoy: 3 episodios, 2.000 h de consumo y 1.000 oyentes comprometidos en 30 días; **no precisa audio o vídeo**. Infobae solo da la fecha. El modelo usa solo horas de vídeo | §2 |
| 1.000 suscriptores atribuidos al post del YPP 2027 | Verificado hoy: el post solo menciona 8.000 h cualificadas o 20 M de vistas de Shorts. Los 1.000 suscriptores se citan de la ayuda vigente de YouTube y su continuidad en 2027 es **[S]** | §2 |
| La cuota de techo del base (7-67 %) caía fuera del 10-30 % | Con la calibración de la v2, la base en mantenimiento supone el 11 % del techo bajo (dentro) y la alta, el 84 % (fuera: solo cabe con mercado alto o desbordamiento; por eso pesa un 12 %) | §4.3 |

**Qué cambia en el veredicto:** nada en la conclusión de fondo (experimento barato con cola derecha del ~10 %), y mucho en la mecánica: el escenario base ya no es "un camino hasta M36", sino una rama que el plan corta en la P1 la mayoría de las veces.


### v2 → v3 (respuesta al crítico de la ronda 2)

| Carencia señalada | Cómo se resuelve |
|---|---|
| El signo del valor esperado (−194 € frente a +796 €) dependía de probabilidades de ayudas inventadas (CRTVG 5/10/25 %, Youtubeiras+ 8-40 %, B2B 20-50 %) | **Caso central solo con tasas observables.** Youtubeiras+ con tasa base de 126 canales / 6 premios (2025): 4 % en 2026, 6-8 % en 2027. La CRTVG y el B2B pasan a **opciones** con umbral de equilibrio (7,2 % y 11 %/año). Valor esperado central: **−147 €**; P(> 0): **12,7 %** (§6, §8) |
| Faltaban las propuestas presentadas a la CRTVG en 2024 y 2025 | Buscadas en las notas de la CRTVG (2023), audiovisual451 (2022, 2024 y 2025), el PDF de la resolución de 2025 y prensa. **No se publican.** Se documenta la ausencia y se aplica la instrucción: el caso central va sin la CRTVG (§6.2) |
| Faltaban los inscritos y ganadores de Youtubeiras+ y su perfil | 68 / 89 / 126 canales (2023-2025), 28 finalistas en 2025, palmarés completo y tamaño de 4 ganadores (56-2.1K suscriptores). No se sabe de ninguno con voz de IA (§6.1) |
| Bases de la CRTVG sin leer (PDF escaneado) | **Leídas y transcritas las 23 páginas**: requisito de IAE y autónomos; inédito; cesión exclusiva, mundial y hasta el dominio público, con doblaje; declaración de autoría del guion; **ningún texto sobre IA**; baremo con 40 puntos de "xestión responsable"; entregables de emisión (§6.2; `crtvg/bases2025_extracto.txt`) |
| CPM del patrocinio de 10-20 € sin anclaje | Anclado en tres fuentes españolas de 2026 (10-40 €, 15-25 € en pódcast pequeños y medianos) y una de EE. UU. (18-26 USD). Se separa en precio [F] × tasa de venta [S] y se contrasta por vídeo con la tarifa de los nanocreadores (50-200 € por publicación) (A14) |
| Error: "12 seleccionados en 2025" atribuido a la convocatoria de 2024 | Corregido y ampliado: 2024 = 12 proyectos y 300.000 € (nota del 22-10-2024). 2025 = convocatoria para 15 y 357.000 €, **resuelta con 12 y 339.000 €** (PDF del 04-12-2025), con el videopódcast desierto. Las dos cifras de "12" son ciertas, pero de convocatorias distintas |
| Error: Youtubeiras+ a 1.100 € "medio" | 1.000 € brutos (Revelación, Calidade lingüística y Pódcast) y 810 € netos tras retención (A20) |
| Error: bases de la CRTVG citadas como [F] sin haberlas leído | Ahora sí se leyeron; cada afirmación lleva su página |

### v1 → v2 (se mantiene)

| Carencia señalada | Cómo se resolvió |
|---|---|
| El base no pasaba la P1 y aun así se proyectaba a M36 | Puertas recalibradas y **evaluadas dentro del modelo**. El base pasa P1 y P2 y **no pasa la P3 → mantenimiento** |
| A1 anclado en canales con marca | Recalibrado con 9 canales clónicos nuevos: base de 450 → **70**; cola larga de 30 → **8** |
| Faltaban el árbol, las probabilidades y el valor esperado | §5.1 y §8 |
| Premium y anuncios calculados por vista | Premium por horas (A8) y anuncios por impresiones = f(AVD) (A7b) |
| Umbrales del Spotify SPP y del YPP mal atribuidos | Corregidos con TechCrunch y support.google.com |

### Fuentes verificadas en esta ronda (29-09-2026)
- **Ronda 4:** post del YPP 2027 (releído: 8.000 h o 20 M de Shorts, sin mención a suscriptores; Premium 30 % / Lite 60 %, 55 % para vídeo largo): https://blog.youtube/news-and-events/youtube-partner-program-updates-2027-new-opportunities-earn/ · Spotify SPP (releído: 3 episodios, 2.000 h de consumo, 1.000 oyentes en 30 días; antes 12 / 10.000 / 2.000): https://techcrunch.com/2026/01/07/spotify-lowers-monetization-threshold-for-video-podcasts · 64 canales de YouTube de historia/relatos para dormir, 13 medidos en su primer mes: `model/obs_nuevos_1mes_29-09-2026.txt` (URLs `https://www.youtube.com/<handle>/videos`)
- Bases CRTVG 2025 (leídas las 23 páginas): https://www.crtvg.es/documents/d/crtvg/convocatoriaasinada09xuno2025contidosdixitais-pdf-1
- Resolución CRTVG 2025, 12 seleccionados y 339.000 € (PDF creado el 04-12-2025): https://www.crtvg.es/documents/d/crtvg/a-corporacion-de-servizos-audiovisuais-de-galicia-pdf
- CRTVG 2024, 12 proyectos, 300.000 € y "Respira": https://www.audiovisual451.com/crtvg-producira-doce-nuevos-proyectos-nativos-digitales-en-gallego/
- Convocatoria CRTVG 2025, 15 proyectos y 357.000 €: https://www.audiovisual451.com/la-crtvg-abre-una-nueva-convocatoria-para-la-produccion-de-contenidos-digitales-destinados-a-sus-plataformas/
- CRTVG 2023, 25 proyectos: https://www.crtvg.gal/gl/web/crtvg/w/a-crtvg-producir%C3%A1-25-novos-proxectos-nativos-dixitais-en-galego
- CRTVG 2022, 330.000 € y hasta 42 proyectos: https://www.audiovisual451.com/tvg-abre-una-convocatoria-de-seleccion-de-proyectos-digitales-en-gallego/
- Youtubeiras+: https://youtubeiras.gal/ix-edicion-2025/ (126 canales) · https://youtubeiras.gal/viii-edicion-2024/ (89) · https://youtubeiras.gal/setima-edicion/ (68) · https://youtubeiras.gal/palmareshistorico/ · https://youtubeiras.gal/bases-youtubeiras-2026/
- Patrocinio: https://patillero.es/monetizar-podcast/ · https://jezzmedia.com/publicidad-en-podcasts-numeros-reales-en-espana/ · https://euribor.com.es/2026/09/20/la-economia-de-los-influencers-asi-se-calcula-el-precio-real-de-un-post-patrocinado/ · https://advertising.libsyn.com/podcast-advertising-rates
- Rondas anteriores: YPP 2027 (https://blog.youtube/news-and-events/youtube-partner-program-updates-2027-new-opportunities-earn/), requisito vigente de 1.000 suscriptores (https://support.google.com/youtube/answer/72851), Spotify SPP (Infobae y TechCrunch, arriba), canales clónicos (§3.1). El resto de URLs vienen de los informes `research/*.md`, citados en cada fila.
