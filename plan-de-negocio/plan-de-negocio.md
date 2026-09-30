> **Sustituido (30-09-2026):** este plan v1 queda sustituido por [`plan-v2-desatendido.md`](plan-v2-desatendido.md) tras las decisiones del promotor (`decisiones.md` y `gauntlet2/contexto.md`). Se conserva como referencia histórica.

# Plan de negocio: Serán · Historia de Galicia para durmir

Canal de YouTube (y feed de audio) de historia de Galicia para quedarse dormido. Está hecho con IA y es 100 % en galego, con la calidad del galego narrado y escrito como condición no negociable.

- **Versión:** integrada (alisado del Gauntlet Loop + correcciones del tribunal final en dos rondas, Anexo A.5) · 29-09-2026
- **Idioma:** redactado en castellano. Todo lo que ve u oye el público va en galego normativo (RAG).
- **Horizonte:** octubre de 2026 a noviembre de 2029.

**Documentos que acompañan a este plan (misma carpeta):**
- `guion-mostra-revolta-irmandina.md`: guion muestra en galego, con el texto narrado y las notas de fuentes.
- `00-contexto-y-concepto.md`: el contexto y el concepto que se tomó de la conversación previa con Gemini.

**Convenciones de evidencia (las mismas en todo el documento)**
- **[F]:** dato con fuente. La URL va al lado o en el Anexo B.
- **[OBS]:** observación directa de páginas públicas, hecha el 29-09-2026.
- **[MED]:** medición propia sobre datos reales (yt-dlp, subtítulos, *storyboards*).
- **[P]:** prueba propia ejecutada el 29-09-2026 (código y resultados en el directorio de trabajo del gauntlet).
- **[S]:** supuesto o decisión de diseño. Lo sustituye el dato del piloto.
- **[INT]:** ajuste hecho en esta integración. Es aritmética sobre cifras de las piezas, con el cálculo a la vista; **no son datos nuevos**.
- **[COMP]:** comprobación técnica reproducible hecha el 29-09-2026 contra una API o unos datos abiertos (disponibilidad de un *handle* o un dominio, recuento en datos abiertos o en una instancia pública). Las plantillas de consulta están en el Anexo B.
- **[CALC]:** cálculo propio sobre las cifras que se citan al lado; hereda la etiqueta de sus entradas (por ejemplo, [CALC sobre S]).
- **[F-sec]:** dato con fuente secundaria (portal, agregador o tarifa de lista), no de la fuente original.
- **Calendario:** octubre de 2026 es el mes de arranque. Los meses del modelo van de M1 a M36, con **M1 = diciembre de 2026**: el último mes de construcción, igual que el mes 1 sin vídeos del calendario de la pieza de mercado. Así, el lanzamiento cae en M2 (enero de 2027), la P1 en M6 (mayo de 2027), la P2 en M12 (noviembre de 2027), la P3 en M18 (mayo de 2028) y el horizonte en M36 (noviembre de 2029). Ver §1.2.

---

## 0. Resumen ejecutivo

### 0.1 Qué retorno cabe esperar en cada etapa

| Etapa | Qué compra | Retorno económico esperable | Coste de caja | Horas del promotor |
|---|---|---|---|---|
| **0. Validación de voz y pipeline** (oct 2026 - ene 2027) | Saber si existe una voz en galego al nivel exigido, si hay terceros dispuestos a pagar la calidad y si el pipeline produce un episodio en las horas previstas | **0 €** | **Paso barato (Puerta V-0): ~0-10 €.** **Puerta F** (financiación de la calidad, §1.3): ~0 € y ~10 h. Validación formal, solo si V-0 da señal **y** pasa la Puerta F: **850-1.500 €** una vez (techo de 2.050 €) | ~95 h hasta el lanzamiento (~6 h/semana) + ~10 h de la Puerta F |
| **1. Piloto barato con puertas** (ene-may 2027, 12 vídeos) | Datos de audiencia, retención y hábito, y el veredicto de la comunidad sobre el galego | **0 € por diseño.** Solo se llega si hay voz **y** terceros pagan la calidad (≈ 10 % del total con la Puerta F, §1.3); en ese caso lo más probable (≈ 85 %) es parar en la Puerta 1 | **Paquete de calidad ≈ 3.680 € (2.390-5.010) en 12 episodios** (corrección de mesa íntegra de cada guion, escucha con texto de los episodios 1-6 y revisión histórica, §4.7 y §5.4): **≈ 500-1.030 €/mes, central ≈ 770 €**, en los 5 meses de la E1 (ene-may). **Con la Puerta F lo pagan terceros** y al promotor le quedan los 35 €/mes de stack. **Sin ella rompe el "< 50 €/mes": D5** | ~5 h/semana (≈ 80 h) |
| **2. Proyecto lateral** (jun 2027 - may 2028) | Llegar a ingresos recurrentes ≥ caja | **Solo en el camino optimista (P4: 10,2 % de los caminos que publican):** 66 €/mes en M12, 173 €/mes en M18 y 509 €/mes en M36. **Si el promotor paga la garantía (caja ≈ 550 €/mes) no llega al equilibrio mensual en 36 meses** y acaba en ≈ −15.750 €. **Si terceros pagan el diferencial de calidad (Puertas F y F2)**, el optimista acaba en **≈ +1.190 €** (+2.105 € con voz de pago), con una probabilidad del ≈ 0,4 % del total. **En el camino base: 0 € y sin YPP** | **~350-760 €/mes, central ≈ 550 €** con 4 episodios y la garantía (modelo: 110 €). **Fuera del rango de 50-200 €: solo se abre con la Puerta F2** (≥ 440 €/mes comprometidos por terceros) | 8,5-10 h/semana (37-44 h/mes) |
| **3. Apuesta seria / red** (desde jun 2028, solo si se pasa la P3) | Voz licenciada y localización es/pt | Valor esperado de **−2.250 € a 36 meses**, solo accesible desde el camino P4 (≈ 0,4 % del total con la Puerta F). Caso ganador (5 %): **~2.000 €/mes**. Recuperación hacia el mes ~50 | 3.000 € + 90 €/mes | ~10 h/semana |
| **Pagos únicos** (en cualquier etapa) | Premios y encargos | **Youtubeiras+:** 810 € netos, con un 4-8 % de probabilidad por edición. **CRTVG (opción):** +7.500 € netos si se gana, pero exige alta de autónomo y ceder la temporada para siempre | — | — |

**Techos.** Con solo galego y solo AdSense y Premium, el techo es de **~410-700 €/mes** capturando todo el mercado atendible. Con fuentes directas (membresías, patrocinio, audio), **~1.500-2.000 €/mes** [S].

**Valor esperado conjunto a 36 meses (M36), del árbol voz → Puerta F → audiencia del §1.3 [INT sobre S]: ≈ −340 € de caja (−230 a −495 €) y ≈ 55 h.**
- El modelo de retornos, por sí solo, da **−147 € y 328 h**, pero está condicionado a que haya voz y no paga la calidad que exige el plan.
- El árbol conjunto empieza en la voz (V-0), sigue con la **Puerta F** (compromiso de terceros que cubra al menos el diferencial de calidad de la E1, ≈ 3.680 €), la Puerta V y la vía (c), y termina en la audiencia (P1-P4), con una **Puerta F2** en la P1 (≥ 440 €/mes para la E2). A cada hoja le suma lo que paga el promotor: V-0 y construcción, validación, vía de voz y la caja del modelo. La calidad la pagan terceros o no se publica.
- **Resultados (las probabilidades suman el 100 %; P(F) = 25 % y P(F2) = 40 % [S]):**
  - **45 %:** la V-0 descarta las voces y se espera: **≈ −40 € y ~20 h**;
  - **41,3 %:** la V-0 da señal, pero nadie compromete la calidad: **presupuesto de hobby** (≤ 300 €, central 100 €) y se espera: **≈ −140 €**;
  - **3,7 %:** pasa la Puerta F, pero ni la Puerta V ni la vía (c) dan voz: **≈ −2.225 €**;
  - **8,5 %:** se publican 12 vídeos y se para en la P1 (por los KPI o porque falla la F2): **≈ −1.855 €** (−1.420 a −2.290 €);
  - **1,5 %:** se sigue a la Etapa 2 con la F2: **entre −3.180 € (P3) y +1.185 € (P4)**.
- **Probabilidad conjunta de acabar con caja positiva: ≈ 0,3 %** (el optimista con F y F2, voz de pago o de Nós). **Umbral que hace positiva la hoja más probable de las que publican (P1):** que los terceros comprometan **≈ 5.140 €** (3.520-6.800), es decir, el diferencial de la E1 más ≈ 1.460 € de validación, construcción y stack.
- **Comparación honesta de políticas:** **no gastar nada tras la V-0 es lo que menos pierde** (≈ −40 €). La Puerta F cuesta ≈ 300 € más de valor esperado, pero es la única forma de publicar que no exige al promotor pagar la calidad: condicionada a que pase, el promotor arriesga ≈ −1.930 € (sobre todo la validación). **Si el promotor paga la calidad de su bolsillo** (sin Puerta F), el valor esperado es de ≈ −3.570 € (−2.310 a −4.850) siguiendo las puertas y de ≈ −2.560 € parando siempre en la P1: esa última es solo **la menos mala de las políticas que publican sin financiación**, no la que minimiza la pérdida.

### 0.2 Recomendación go / no-go

1. **NO-GO como negocio.** Si el promotor paga la revisión cualificada que exige la calidad del galego y de la historia, **ningún camino acaba con caja positiva a M36** (§1.3). La publicidad no paga el proyecto: en el camino base el canal ni siquiera entra en el YPP. Lo que mueve la aguja es el patrocinio identitario y las membresías, y eso solo ocurre en la rama alta, que tampoco cubre ≈ 550 €/mes de Etapa 2.
2. **GO como hobby con opción, en tres pasos y con las puertas baratas delante:**
   - **GO inmediato a la Puerta V-0** (semanas 1-4; ~0-10 € y ~20 h). Incluye:
     - pedir permisos a Proxecto Nós y a los locutores;
     - prueba B0 de cómputo;
     - prueba G0 de pronunciación y ritmo;
     - criba R0;
     - preselección ciega por el promotor y su mujer frente a una grabación pública de un narrador galego.
   - **Puerta F (financiación de la calidad), en paralelo desde la semana 2 y con decisión en la semana 5** (§1.3 y §9). Antes de pagar la validación formal y el paquete de calidad, hace falta un **compromiso firme y por escrito de terceros** que cubra al menos el diferencial de calidad de la E1 (**≈ 3.680 €**, 2.390-5.010). Fuentes: servicios de normalización lingüística de concellos (línea PL400A de la SXL), mecenas y membresías fundadoras o preventa (Ko-fi o Patreon, sin umbral), patrocinio identitario prevendido y convenio con Nós/USC o con la AGPTI que cofinancie la revisión. **Si falla, presupuesto de hobby explícito:** ≤ 50 €/mes y ≤ 300 € en 6 meses, sin validación formal ni publicación; reintento con la convocatoria PL400A de 2027; si falla dos veces, cierre documentado.
   - **La excepción de 850-1.500 € (dos narradores de referencia y un revisor profesional) solo se aprueba si V-0 da señal y pasa la Puerta F** (§4.4). Si V-0 no da señal, el plan recomienda **esperar** (reevaluación trimestral de modelos) o ir directamente a una **voz humana licenciada** (1.400-2.500 €), sabiendo que eso rompe el "< 50 €/mes" de la Etapa 1.
   - **La P1 vuelve a decidir:** se sigue a la Etapa 2 solo si se cumplen los KPI de la P1 **y** la **Puerta F2** (terceros comprometen ≥ 440 €/mes, el diferencial de calidad de la E2, durante al menos 6 meses). Si no, se para con el catálogo publicado.
3. **Condición de fondo.** La calidad del galego no se negocia, así que **no se publica con una voz que no pase la Puerta V** ni sin el paquete de calidad pagado. Tampoco con la "menos mala". Hoy es probable (60-80 % [S]) que ninguna voz sintética "de fábrica" lo consiga (§4).
4. **Decisiones que necesita el promotor antes de la semana 1:**
   - **D1.** ¿Acepta la excepción de 850-1.500 € si V-0 da señal **y** pasa la Puerta F?
   - **D2.** Si no pasa ninguna voz, ¿qué orden sigue: vía intermedia (c), esperar (a) o locutor licenciado (b)?
   - **D3.** ¿Acepta ~6 h/semana hasta el lanzamiento (más ~10 h de la Puerta F) y ~5 h/semana después? Si se queda en 4 h/semana, el lanzamiento se va a marzo de 2027.
   - **D4.** ¿Acepta el doble permiso (USC y locutor) y la oferta al locutor (100 € + 10 % de los ingresos) si la voz es de Nós?
   - **D5. Presupuesto de la garantía de calidad (§4.7 y §5.4).** Pagar la corrección de mesa íntegra, la escucha con texto y el historiador cuesta ≈ 305 € por episodio de 75 min en la E1 y ≈ 120 € por episodio de 2 h en la E2 (con inspección reducida del texto). No cabe en el "< 50 €/mes" ni en los 50-200 €/mes. **El plan no rebaja la garantía.** Decide así:
     - **Etapa 1: la paga la Puerta F, no se quitan episodios.** Paquete de ≈ 3.680 € (2.390-5.010 €) para los 12 vídeos. Con menos de 12 vídeos la P1 no mide nada (§8.3).
     - **Etapa 2: no se abre por defecto.** Con 4 episodios al mes, la garantía cuesta ≈ 550 €/mes y, si la paga el promotor, ningún camino la recupera en 36 meses. Solo se abre con la **Puerta F2** o si a la P1 llega la señal de rama alta (§8.2) con ingresos directos comprometidos que cubran los ≈ 440 €/mes.
     - Bajar a 3 episodios al mes ahorra ≈ 140 €/mes, pero obliga a recalibrar la P2: con 3 al mes, la rama base del modelo llega a 91 suscriptores en M12, no a 100.
   - **D6. Presupuesto de hobby si falla la Puerta F.** Propuesta del plan: ≤ 300 € en 6 meses (≤ 50 €/mes). Pagar la calidad de su bolsillo ("hobby completo", ≈ 4.850 € de validación y paquete de la E1) es posible, pero el promotor lo decide por escrito sabiendo que su valor esperado es de ≈ −2.560 € como mínimo (§1.3).

### 0.3 El producto en cinco líneas
- **Nombre y promesa:** **"Serán · Historia de Galicia para durmir"**. Promesa: *"A historia de Galicia contada amodo, nun galego coidado, para que te deixes levar ata o sono. Sen sustos e sen présa."*
- **Episodios y ritmo:** 75 min en la Etapa 1 y 2 h en la Etapa 2, más 20-45 min de cola de ambiente. Ritmo percibido de 115 palabras/min (§3.3).
- **Estructura:** tres actos con tensión decreciente, 14 reglas de "sono seguro", paisaje sonoro gallego grabado e identidad visual "noite atlántica".
- **Pipeline:** Claude Code + Python, con cuatro puertas humanas obligatorias (escaleta, lectura íntegra del guion, escucha firmada del audio y publicación). Las citas históricas las extrae una herramienta de la fuente, no el LLM.
- **Competencia directa en galego:** ninguna. **Mercado atendible:** 2.000-20.000 oyentes habituales.

---

## 1. Retornos y modelo financiero por etapas

Esta sección es la pieza "retornos" del gauntlet (ganó en 3 rondas), ajustada al calendario y a los costes que fijan las demás piezas. El modelo es mensual y reproducible:
- `model/modelo2.py`: ramas y puertas.
- `model/arbol3.py`: árbol, tasas base de premios, opciones y distribución.
- `model/sens2.py`: sensibilidad.
- `model/puertas_gtm.py`: calendario de publicación.

Todas sus proyecciones son [S].

### 1.1 Las etapas y sus puertas

| Etapa | Meses (calendario) | Presupuesto de caja | Horas | Cadencia y formato | Objetivo económico |
|---|---|---|---|---|---|
| **0. Construcción y validación** | Oct 2026 - mediados de ene 2027 | ~35 €/mes + la excepción de voz (§4.4), solo si pasa la Puerta F | ~6 h/semana (≈ 95 h) + ~10 h de la Puerta F | 0 vídeos; 3 episodios terminados antes de publicar | Ninguno: pasar la V-0, la Puerta F, la Puerta V y la Puerta 0 |
| **1. Piloto barato con puertas** | Ene - may 2027 (M2-M6) | Stack ≤ 50 €/mes (modelo: 35 €) **+ calidad cualificada ≈ 3.680 € en 12 episodios** (≈ 500-1.030 €/mes en total, central ≈ 770 €; D5, §5.4), **pagada por terceros (Puerta F)** | ~5 h/semana | Quincenal, 75 min; **12 vídeos en la P1** | **Ninguno.** Comprar datos |
| **2. Proyecto lateral rentable** | Jun 2027 - may 2028 (M7-M18) | 50-200 €/mes pedidos (modelo: 110 €). **Con la garantía de calidad, ≈ 550 €/mes** (350-760 €, §5.4); por eso **no se abre por defecto**: solo con la **Puerta F2** (terceros cubren ≈ 440 €/mes; D5) | 8,5-10 h/semana | Semanal, ~2 h | Ingresos recurrentes ≥ caja en 12-18 meses |
| **2b. Mantenimiento** (si no se pasa la P3) | M19-M36 | ~20 €/mes en el modelo; **≈ 140 €/mes con la garantía** (1 episodio revisado al mes) | ~2 h/semana | 1 vídeo al mes | Conservar el catálogo y la elegibilidad para premios. **El árbol conjunto (§1.3) supone cierre en M18**, que es lo que ya recomendaba el §1.6 |
| **3. Apuesta seria / red** | Desde M19, solo si se pasa la P3 | 1.000-5.000 € iniciales (modelo: 3.000 €) + ~90 €/mes | ~10 h/semana | Pistas o canales es/pt y voz licenciada | Techo de cientos a miles de €/mes |

**Puertas de negocio.** Es la tabla única del plan: el modelo de retornos y el plan de pruebas (§8) usan los mismos umbrales.

| Puerta | Fecha · vídeos | Condiciones (todas) | Clónico | Estancada | **Base** | Alta |
|---|---|---|---|---|---|---|
| **P1** | **31-05-2027 · 12** | Vistas medias a 30 días **≥ 60**; **≥ 20 suscriptores**; AVD ≥ 20 min; sin quejas graves de lengua | 26 / 5 → **para** | 86-91 / 23 → pasa | **86-91 / 24 → pasa** | 294-318 / 99 → pasa |
| **P2** | **30-11-2027 · 36** | Vistas a 30 días de los vídeos nuevos **≥ 100**; **≥ 100 suscriptores**; **Youtubeiras+ 2027 presentado**; **≥ 5 propuestas de patrocinio enviadas** | — | 91 / 87 → **para** | **115 / 107 → pasa** | 459 / 475 → pasa |
| **P3** | **31-05-2028 · 60** | En el YPP con RPM medido, **o** ≥ 50 €/mes recurrentes (media de 3 meses), **o** ayuda o encargo concedido | — | — | 252 suscr., 0 € → **mantenimiento** | YPP en M17 → **pasa; abre la E3** |

- **Calendario de las cifras de esta tabla.** Salen de `puertas_gtm.py` con el **calendario real** (3 vídeos en el lanzamiento y después quincenal). El §1.6 usa el calendario del modelo (`modelo2.py`, 2 vídeos al mes desde M1), y por eso da 25 suscriptores en M6 y 108 en M12 en la rama base, frente a 24 y 107 aquí. **La diferencia es solo de calendario** [INT, tribunal final, 2.ª ronda]; las puertas se leen con esta tabla.
- **Puerta F2 en la P1** [INT, tribunal final, 2.ª ronda]: con la garantía de calidad, pasar los KPI de la P1 no basta; hace falta además que terceros comprometan ≥ 440 €/mes para la E2 (§0.2, §1.3). Sin la F2, se para con el catálogo publicado.
- Los márgenes son estrechos (24 frente a 20 suscriptores en la P1; 107 frente a 100 en la P2). **Se recalibran en la lectura temprana** (M4, vídeos 1-4, §8.3). Lo que no cambia es la regla: se sigue solo si la trayectoria se parece a la base o mejor.
- **Armonización [INT] de la P2:**
  - El modelo de retornos (v3) ya no exigía "≥ 1 solicitud de ayuda", porque la CRTVG obliga a darse de alta de autónomo.
  - La pieza de mercado aún la pedía.
  - Queda así: **Youtubeiras+ 2027 presentado**, que no exige alta ni tiene coste.
- **Control de hábito en M9 (agosto de 2027).** Solo aplica si la P1 dio un GO condicionado (§8.4). Ahorra ~330 € y ~105 h en la rama estancada. **No está recalculado en el valor esperado:** lo mejora un poco.

### 1.2 Calendario integrado [INT]

Las piezas tenían tres calendarios incompatibles:
- **Retornos:** 12 vídeos desde octubre.
- **Mercado (GTM):** lanzamiento el 22-11-2026, con el pipeline listo en la semana 7-8.
- **Pipeline:** primer episodio en la semana 10-12. **Voz:** 5-7 semanas de protocolo antes del episodio 1.

Sumadas las horas reales antes de publicar, salen ~95 h:
- MVP del pipeline: 32,5-35,5 h;
- G0 y G1: 6-8 h;
- protocolo de voz: ~20 h;
- episodios 1-3 terminados antes de publicar: ~30 h, porque los tres primeros cuestan el doble.

Por eso:

| Hito | Fecha | Mes del modelo |
|---|---|---|
| Construcción, Puerta V y Puerta 0 | 1-10 a mediados de enero de 2027 (≈ 15 semanas a ~6 h/semana) | Antes del modelo (oct-nov) y M1 (diciembre) |
| **Lanzamiento con 3 episodios** | **Domingo 17-01-2027, a las 21:30** | M2 |
| Episodios 4-12, en domingos alternos: 31-01, 14-02, 28-02, **14-03** (vídeo 7, especial del Día Mundial do Sono: es el domingo anterior al día, que en 2027 cae el **viernes 19-03** [F]), 28-03, 11-04, 25-04 y 09-05. **Única excepción a la cadencia:** el vídeo 12, de las Letras Galegas, se adelanta una semana al **domingo 16-05**, víspera del Día das Letras (lunes 17-05). Si no, tocaría el 23-05, ya pasado el día | 31-01 a 16-05-2027 | M2-M6 |
| **P1** | 31-05-2027 | M6 |
| Etapa 2, semanal | Desde junio de 2027 | M7 |
| **P2** | 30-11-2027 | M12 |
| **P3** | 31-05-2028 | M18 |
| Fin del horizonte | Noviembre de 2029 | M36 |

- **El modelo no cambia:** sus cifras dependen del número de vídeos y de los meses de vida del canal, no de la fecha del calendario. El desfase de 2-3 meses solo añade construcción previa (§1.3).
- **Si el promotor se queda en 4 h/semana:** el lanzamiento pasa a marzo de 2027 y todas las puertas se retrasan 2 meses.

### 1.3 Árbol conjunto voz → Puerta F → audiencia y valor esperado integrado [INT]

**Por qué se rehace (tribunal final, dos rondas).**
- **Primera ronda.** La versión anterior sumaba ajustes sueltos al valor esperado del modelo (−1.250 a −1.900 €). No era un valor esperado conjunto: aplicaba la validación de voz a todos los caminos, ponderaba con probabilidades condicionadas a que hubiera voz y mezclaba una fila de otro árbol, así que sus probabilidades no sumaban el 100 %. Tampoco pagaba la revisión lingüística e histórica cualificada (§4.7). Se rehízo como un solo árbol (`model/arbol_conjunto.py`).
- **Segunda ronda.** Ese árbol demostraba que ningún camino recupera la caja con la garantía de calidad, y aun así el plan mandaba gastar la validación y el paquete de calidad tras una V-0 positiva, con una política ("parar siempre en la P1") que dejaba la P1 sin decidir nada. Además, el paquete de la E1 estaba infravalorado: la revisión íntegra de los episodios 1-6 no tenía presupuesto (§5.4). Ahora el árbol lleva una **Puerta F** entre la V-0 y la validación, una **Puerta F2** en la P1 y el paquete de calidad recalculado. Es reproducible en `model/arbol_conjunto_f.py` (directorio de trabajo del gauntlet).
- **Todas sus probabilidades son [S]**, salvo las de audiencia, que vienen del modelo de retornos (§1.6).

**La Puerta F (financiación de la calidad)** [INT, tribunal final, 2.ª ronda]
- **Qué exige:** antes de pagar la validación formal (850-1.500 €) y el paquete de calidad, un **compromiso firme y por escrito de terceros** que cubra al menos el **diferencial de calidad de la E1: ≈ 3.680 €** (2.390-5.010, §5.4). El compromiso se condiciona a que haya voz: si la Puerta V y la vía (c) fallan, no se cobra.
- **Cuándo:** se prepara desde la semana 2, en paralelo a la V-0, y se decide en la **semana 5** (29-10 a 04-11-2026), antes de firmar con H1 y H2. Si el compromiso llega más tarde, todo el calendario se desplaza lo mismo.
- **Fuentes posibles:**
  - **Servicios de normalización lingüística de los concellos.** La línea **PL400A** de la Secretaría Xeral de Política Lingüística subvenciona a entidades locales de ≥ 3.000 habitantes (solas o agrupadas) para "programas e accións de dinamización lingüística". Entre los productos, cita el "formato dixital" (creaciones en galego "para seren exhibidos en páxinas web, redes sociais ou noutras plataformas dixitais") y el "formato material" (libros y **audiolibros**). En 2026: 350.000 € en total, un mes de plazo desde el DOG del 7-04-2026 y ejecución del 1-01 al 15-10-2026 [F, DOG n.º 63, 7-04-2026: https://www.xunta.gal/dog/Publicados/2026/20260407/AnuncioG0766-180326-0001_gl.html]. **La subvención es para el concello, no para el canal:** el concello tendría que encargar el servicio (episodios con su tema, o licencia de uso del catálogo en su programa) [S]. Como la convocatoria de 2027 no saldrá antes de marzo o abril, una carta de intención condicionada a ella **cuenta solo por la parte que el concello asuma sin la subvención** [S].
  - **Mecenas, membresías fundadoras o preventa** (Ko-fi o Patreon, sin umbral, §1.4). Solo cuentan los cobros o las promesas con fecha. Antes del lanzamiento no hay audiencia, así que es la fuente menos probable [S].
  - **Patrocinio identitario prevendido:** una marca gallega que compre la mención de la temporada (§1.4, A14).
  - **Convenio con Nós/USC o con la AGPTI** que cofinancie la revisión (por ejemplo, textos corregidos como corpus para Nós, o prácticas tuteladas de corrección) [S].
- **Si falla: presupuesto de hobby (D6).** ≤ 50 €/mes y **≤ 300 € en 6 meses** (central: 100 €), para mantener el pipeline de texto con Claude Pro y reevaluar voces cada trimestre, **sin validación formal ni publicación**. Se reintenta con la convocatoria PL400A de 2027; si falla dos veces, se cierra y se documenta.
- **Puerta F2 en la P1:** para abrir la E2, además de los KPI de la P1, terceros tienen que comprometer **≥ 440 €/mes** (el diferencial de calidad de la E2, §5.4) durante al menos 6 meses. **Así la P1 vuelve a decidir:** con KPI y F2 se sigue; si falta cualquiera de las dos cosas, se para.

**Probabilidades [S].** Encajan con el 60-80 % de que ninguna voz "de fábrica" pase la Puerta V (§4.1): aquí no pasa ninguna en el 69,7 % de los casos.
- **V-0 da señal:** 55 %.
- **Puerta F, si hubo señal:** 25 %. Sensibilidad abajo.
- **La Puerta V pasa:** 55 %. Dentro de ese caso, Nós con doble permiso en el 60 % y voz de pago en el 40 %.
- **La vía (c) pasa:** 40 % (el §4.4 da 30-50 %). Si falla, se espera (D2, caso central).
- **Puerta F2, si la P1 da GO:** 40 %.

```
Semanas 1-4 ─ Puerta V-0 (~0-10 € + el mes de octubre, ~35 €; ~20 h)
├─ NO (45,0 %) → esperar, con reevaluación trimestral ............................ Hoja A
└─ SÍ (55 %) → Puerta F, semana 5 (~0 €; ~10 h)
      ├─ NO (41,3 % del total) → presupuesto de hobby (≤ 300 €), sin publicar ..... Hoja F
      └─ SÍ (13,8 %) → validación formal (850-1.500 €) → Puerta V
            ├─ PASA (7,6 %): Nós con doble permiso (4,5 %) o voz de pago (3,0 %) → PUBLICA
            └─ FALLA (6,2 %) → vía (c): fine-tune con H1 o H2, 700-1.250 €
                  ├─ PASA (2,5 %): licencia T2, 300-600 € + 12,5 % de los ingresos → PUBLICA
                  └─ FALLA (3,7 %) → D2 = esperar (caso central) ....................... Hoja B

PUBLICA (10,0 %) ─ E1: 12 vídeos; el paquete de calidad lo pagan terceros ─ Puerta 1 (M6)
   ├─ NO (61,7 %) → PARAR ....................................................  6,2 % del total ┐
   └─ SÍ (38,3 %) → Puerta F2 (≥ 440 €/mes de terceros)                                          │ P1
         ├─ NO (60 %) → PARAR con el catálogo publicado .........................  2,3 % ────────┘
         └─ SÍ (40 %) → E2 ─ Puerta 2 (M12)
               ├─ NO → PARAR ....................................................  0,45 % · P2
               └─ SÍ → Puerta 3 (M18)
                     ├─ NO → cierre en M18 ......................................  0,68 % · P3
                     └─ SÍ → E2 hasta M36 (+ opción de E3, fuera del cálculo)      0,41 % · P4
```
Las probabilidades de audiencia son las del §1.6 (61,8/11,1/17,0/10,2 %), renormalizadas porque suman 100,1 %.

**Paquete de calidad de la E1 recalculado** (§4.7 y §5.4; tribunal final, 2.ª ronda): **≈ 3.680 € (2.390-5.010)**, frente a los ≈ 1.550 € de la versión anterior. Sube porque ahora se presupuesta la **corrección de mesa del 100 % del texto de los 12 episodios** antes del render (≈ 8.400 palabras a 0,015-0,025 €/palabra: 126-210 € por episodio) y la **escucha con texto de los episodios 1-6** (9-15 h a 20-35 €/h), que antes se daba por incluida en la excepción de voz.

**Qué suma cada hoja que publica** (caja a M36 en €, caso central, voz de pago). Primero, si el promotor pagara la calidad; después, con las Puertas F y F2:

| Componente | P1 | P2 | P3 | P4 | Origen |
|---|---|---|---|---|---|
| Modelo de retornos: ingresos − caja | −210 | −870 | −1.530 | +3.355 | §1.6. El P3 cierra en M18: sin los 360 € ni los 65 € de mantenimiento |
| V-0 + construcción (octubre y noviembre) | −75 | −75 | −75 | −75 | §1.2 y §4.4 |
| Validación formal de la voz | −1.175 (−850 a −1.500) | ídem | ídem | ídem | §4.4 |
| **Calidad cualificada de la Etapa 1** (RLC + historiador, 12 episodios) | **−3.680** (−2.390 a −5.015) | ídem | ídem | ídem | §4.7 y §5.4 |
| **Etapa 2 con la garantía, por encima de los 110 €/mes del modelo** | 0 | −2.650 (6 meses) | −5.305 (12 meses) | **−13.260** (30 meses) | +442 €/mes (237-648), §5.4 |
| **Resultado si el promotor paga la calidad** | **−5.140** | **−8.450** | **−11.760** | **−14.835** | |
| **Resultado con las Puertas F y F2** (terceros pagan las dos filas de calidad) | **−1.460** | **−2.120** | **−2.780** | **+2.105** | |
| Con voz de Nós: 100 € a la firma + 10 % de los ingresos | −100 | −100 | −100 | −787 | §4.5 |
| Con la vía (c): 700-1.250 € + T2 300-600 € + 12,5 % de los ingresos | −1.425 | −1.425 | −1.425 | −2.283 | §4.4 |
| Horas del promotor | 178 | 421 | 664 | 1.393 | Modelo + 61 h de construcción + 15 h de E1 (18-22 h/mes frente a 17) + 5,5 h/mes de E2 (37-44 h/mes frente a 35, §5.4); +15 h con la vía (c); +10 h con la Puerta F |

**Tabla de resultados con las Puertas F y F2** (política recomendada; las probabilidades suman el 100 %; caja a M36 sin valor de la hora):

| Resultado | Probabilidad conjunta [S] | Caja, caso central (rango) | Horas |
|---|---|---|---|
| **A.** La V-0 descarta las voces y se espera | **45,0 %** | **≈ −40 €** (−35 a −45) | ~20 |
| **F.** La V-0 da señal, pero falla la Puerta F: presupuesto de hobby | **41,3 %** | **≈ −140 €** (−35 a −345) | ~30 |
| **B.** Pasa la F; validación formal y vía (c) sin voz, y se espera | **3,7 %** | **≈ −2.225 €** (−1.620 a −2.830) | ~100 |
| **P1.** Hay voz, 12 vídeos, se para en la P1 (KPI o F2) | **8,5 %** | **≈ −1.855 €** (−1.420 a −2.290) | ~190 |
| **P2.** E2 con F2, se para en la P2 | **0,45 %** | ≈ −2.515 € (−2.080 a −2.950) | ~435 |
| **P3.** Base: cierre en M18 | **0,68 %** | ≈ −3.180 € (−2.740 a −3.610) | ~680 |
| **P4.** Optimista: Etapa 2 hasta M36 | **0,41 %** | **≈ +1.185 €** (+750 a +1.620) | ~1.405 |
| **Total** | **100 %** | **Valor esperado ≈ −340 €** (−230 a −495), con E[Youtubeiras+ 2027] | **≈ 55 h** |

Los resultados de P1-P4 son medias ponderadas de las tres vías de voz: pago, Nós y (c).

**Lectura.**
- **Probabilidad conjunta de acabar con caja positiva: ≈ 0,3 %.** Solo el optimista con F y F2 y voz de pago (+2.105 €) o de Nós (+1.320 €); con la vía (c) queda en −180 €.
- **Umbrales que hacen positiva alguna hoja:**
  - con terceros que cubran **solo el diferencial de la E1** (≈ 3.680 €), ninguna hoja es positiva: parar en la P1 le cuesta al promotor ≈ 1.460 € (voz de pago);
  - con **F + F2** (≈ 3.680 € + ≈ 440 €/mes en la E2), la hoja P4 pasa a positiva;
  - para que la hoja P1, la más probable de las que publican, salga a cero, los compromisos tienen que llegar a **≈ 5.140 €** (3.520-6.800): el diferencial de la E1 más ≈ 1.460 € de validación, V-0, construcción y stack de la E1. **Es la meta de la Puerta F; el mínimo para pasarla es el diferencial.**
- **Condicionado a que pase la Puerta F**, el valor esperado para el promotor es de **≈ −1.930 €** (−1.445 a −2.410): lo que arriesga es, sobre todo, la validación de la voz.
- **Sensibilidad a P(F):** con el 10 %, ≈ −195 €; con el 25 %, ≈ −340 €; con el 50 %, ≈ −585 €; con el 100 %, ≈ −1.080 € (probabilidad de caja positiva del 0,1 %, 0,3 %, 0,6 % y 1,2 %). Cuanto más probable es la F, más se publica y más se gasta en validación. **La F no hace rentable el proyecto: hace que la calidad la pague quien la valora y que el promotor solo arriesgue la validación.** P(F2) apenas mueve el valor esperado (≈ −340 € con el 0 % y con el 100 %), pero decide si hay E2.
- **Comparación de políticas (caso central):**

| Política | Valor esperado | Horas | Nota |
|---|---|---|---|
| **No gastar nada tras la V-0** (esperar siempre) | **≈ −40 €** | ~20 | **La que minimiza la pérdida**, y no compra ningún dato |
| **Puertas F y F2** (recomendada) | ≈ −340 € (−230 a −495) | ~55 | Compra datos de audiencia solo si terceros pagan la calidad |
| Sin Puerta F, parar siempre en la P1 | ≈ −2.560 € (−1.770 a −3.360) | ~95 | La menos mala de las que publican pagando el promotor; la P1 no decide nada |
| Sin Puerta F, seguir las puertas | ≈ −3.570 € (−2.310 a −4.850) | ~190 | Árbol de la 1.ª ronda con el paquete de calidad recalculado |
| Sin Puerta F, variante D2 = (b) | peor que la anterior (≈ −3.640 € con el paquete antiguo) | ~240 | Gasta ≈ 1.750 € más y publica en caminos que también pierden. No recalculada con el paquete nuevo |

- **Sin la revisión cualificada** (solo el revisor de escucha, 138 €/mes en la E2), el valor esperado sin Puerta F sería de **≈ −1.150 €** (−890 a −1.420) y la probabilidad de caja positiva, del **≈ 3,1 %**; el equilibrio mensual del optimista llegaría en **M18** (en M17 ingresa 135 € y la caja es de 138 €). Es la cifra que corrige el "M15" y el "+3.355 €" del modelo, que usaba una caja de 110 €/mes. **El plan no adopta esta variante**, porque rebaja la garantía de calidad.
- **Mantenimiento en lugar de cierre en M18** (como en el modelo): prácticamente igual (≈ −20 € de diferencia en el árbol de la 1.ª ronda).
- **Horas:** ≈ 55 h esperadas con la Puerta F; ≈ 190 h si el promotor pagara la calidad y siguiera las puertas; ≈ 415 h si se llega a publicar en ese árbol.

**La lectura cambia respecto al modelo por sí solo.** La entrada al proyecto ya no es "el precio de una cena al mes". Son la validación de la voz y ≈ 305 € de revisión cualificada por episodio en la E1. Por eso el plan pone delante dos puertas baratas: la **V-0** (~0-10 €), que descarta pronto las voces que no están en la liga necesaria (§4.4), y la **F**, que descarta pronto un proyecto que nadie más que el promotor está dispuesto a pagar.

### 1.4 Qué ingresos existen y cuándo se desbloquean

| Fuente | Umbral de acceso | Reparto para el creador | Encaje con "para durmir" en galego | Fuente |
|---|---|---|---|---|
| AdSense | 1.000 suscriptores + 4.000 h en 12 meses (vigente). Para solicitudes desde el **1-02-2027: 8.000 h *qualified* en 365 días** | 55 % en vídeo largo | Bajo: los mid-rolls despiertan al oyente | [F] support.google.com/youtube/answer/72851 · blog.youtube (YPP 2027) · [S] que se mantienen los 1.000 suscriptores |
| YouTube Premium | El mismo | Pool por tiempo de visionado | Alto por minuto: un vídeo de 2 h captura mucho tiempo | [F] blog de YouTube |
| Membresías / Super Thanks | 500 suscriptores + 3 subidas en 90 días + 3.000 h | 70 % | Medio | [F] support.google.com/youtube/answer/72902 |
| Spotify Partner Program (videopódcast) | En España desde el **20-10-2026**; 3 episodios, 2.000 h y 1.000 oyentes en 30 días | Premium por consumo de vídeo + 50 % de la publicidad; **tarifa no publicada** | Dudoso: quien se duerme suele apagar la pantalla | [F] Infobae/Europa Press; TechCrunch; Spotify Support |
| iVoox, Patreon, Ko-fi | Sin umbral | Patreon ~10 %; Ko-fi 0-5 % | Packs de pago único | [F] |
| Patrocinio gallego | En el modelo, desde M12 con ≥ 2.000 vistas/mes | 100 % | Alto, con una mención solo al inicio y en tono calmado | CPM de 10-40 € en España [F]; tasa de venta [S] |
| **Youtubeiras+** | ≥ 3 publicaciones en el periodo; inscripción hasta mediados de noviembre | 1.000 € brutos (Revelación, Calidade lingüística, Pódcast) | Alto como validación | [F] youtubeiras.gal |
| Encargo CRTVG (opción) | Alta en el IAE y en autónomos; **proyecto inédito** | Divulgación: hasta 26.000 € + IVA; videopódcast: 6.000 € | Alto temáticamente; **cesión exclusiva, mundial y hasta el dominio público**, incluido el doblaje | [F] bases de 2025, leídas página a página |
| "O teu Xacobeo" / Ministerio (ICC) / B2B | Alta formal | 25.000 € / 50.000 € cofinanciados / 1.000-6.000 € por encargo | Fuera de la Etapa 1 | [F] DOG, BOE |

**Lectura.** Lo primero que se desbloquea es el fan funding (500 suscriptores), no los anuncios. Lo único que no pide alta de autónomo ni audiencia son los premios, y son pequeños.

### 1.5 Supuestos por rama de audiencia

| # | Variable | Baja (clónico) | Estancada | Base | Alta | Base de la cifra |
|---|---|---|---|---|---|---|
| A1 | Vistas de un vídeo nuevo en su primer mes | 25 | 70 | 70 | 200 | [OBS] canales clónicos de "historia aburrida para dormir" (§2.3) |
| A2 | Crecimiento de las vistas por vídeo hasta M18 | +20 % | +100 % hasta M6, 0 después | +100 % | +200 % | [S] |
| A3 | Cola larga por vídeo y mes | 2 | 6 | 8 | 20 | [OBS] ≤ 3 en los clónicos fracasados; resto [S] |
| A5 | AVD | 20 min | 30 | 30 | 40 | [S] |
| A6 | Conversión de vistas a suscriptores | 1,3 % | 2,0 % | 2,0 % | 2,5 % | [OBS] 0,35-2,5 % en los clónicos; Sleepless Historian ≈ 1,8 % [F vidIQ] |
| A7 | € por 1.000 impresiones de anuncio | 0,40 | 0,60 | 0,60 | 0,90 | [S] calibrado para un RPM de ~2,5 € (rango habitual en España: 2-6 € [F]) |
| A8 | Premium, € por 1.000 h | 1,0 | 1,5 | 1,5 | 2,5 | [S] |
| A10-11 | Spotify: horas (% de YouTube) y € por 1.000 h | 10 % / 3 € | 25 % / 5 € | 25 % / 5 € | 40 % / 8 € | [S]; tarifa no publicada |
| A12-13 | Membresía: % de suscriptores y precio | 0,3 % / 2,99 € | 0,6 % | 0,6 % | 1,0 % / 3,99 € | [F] reparto del 70 %; resto [S] |
| **A14** | **Patrocinio efectivo = CPM de mercado × tasa de venta** | 0 € | 10 € (20 € × 50 %) | 10 € | 20 € (25 € × 80 %) | CPM [F] patillero.es, jezzmedia.com, euribor.com.es, Libsyn; tasa de venta [S] |
| A15-17 | Caja y horas | E1: 35 €, 17 h/mes · E2: 110 €, 35 h/mes · mantenimiento: 20 €, 8 h/mes | | | | [S]; el pipeline estima 18-24 € y 88-170 € (§5.3). **Integrado (§5.4): con la garantía de calidad, E1 ≈ 770 €/mes (paquete de ≈ 3.680 € en 5 meses) y 18-22 h/mes; E2 ≈ 550 €/mes y 37-44 h/mes.** El árbol conjunto del §1.3 aplica esas diferencias (a cargo de terceros con las Puertas F y F2) |
| A18 | Valor de la hora | 15 €/h (también se muestran 0 y 25) | | | | [S] |
| A20 | Youtubeiras+ neto | 810 € (1.000 € − 19 % de retención) | | | | [F] importe; [S] tipo de retención |

**Probabilidades de rama** [S, argumentadas]:
- **Audiencia:** baja 55 %, estancada 13 %, base 20 %, alta 12 %.
- **Tasa base [OBS]:** de más de 17 canales clónicos en castellano, ~15 % supera los 1.000 suscriptores.
- **Riesgo lingüístico o comunitario:** 15 % en el modelo. **[INT]** En la integración, la parte de voz de ese riesgo se descubre antes, en la Puerta V (§4). El 15 % queda para el rechazo de la comunidad y para un guion que no aguante 75 min.

### 1.6 Árbol, audiencia e ingresos por camino (modelo de retornos)

```
Inicio E1 ─ Puerta 1 (M6)
   ├─ NO (61,8 %): audiencia de clónico (55 %) o galego no validado (0,45 × 15 %) → PARAR          Camino P1
   └─ SÍ (38,2 %) → E2 ─ Puerta 2 (M12)
         ├─ NO (11,1 %): crecimiento estancado → PARAR                                          Camino P2
         └─ SÍ (27,2 %) ─ Puerta 3 (M18)
               ├─ NO (17,0 %): sin YPP ni 50 €/mes → MANTENIMIENTO M19-M36                        Camino P3 (base)
               └─ SÍ (10,2 %): YPP en M17 → E2 completa + opción de E3                           Camino P4 (optimista)
```

| Métrica | Camino | M6 | M12 | M18 | M36 |
|---|---|---|---|---|---|
| Vídeos | P3 / P4 | 12 / 12 | 36 / 36 | 60 / 60 | 78 / 132 |
| Vistas de un vídeo nuevo a 30 días | P3 / P4 | 91 / 318 | 115 / 459 | 140 / 600 | 175 / 800 |
| Vistas del canal al mes | P3 / P4 | 285 / 953 | 883 / 3.304 | 1.456 / 5.760 | 1.715 / 13.440 |
| Suscriptores | P3 / P4 | 25 / 99 | 108 / 475 | 253 / 1.177 | **758 / 5.486** |
| Entrada en el YPP | P3 / P4 | — | — | — / **M17** | **nunca** / ✓ |
| Total de ingresos recurrentes (€/mes) | P3 / P4 | 0 / 0 | 0 / **66** | 0 / **173** | 10 / **509** |

En el optimista, AdSense + Premium son solo el 12 % del ingreso de M36 (58 de 509 €). **Pesan el patrocinio (53 %) y las membresías (30 %).**

**Calendario de estas cifras.** Esta tabla usa el calendario del modelo (`modelo2.py`, 2 vídeos al mes desde M1). Las puertas del §1.1 usan el calendario real (`puertas_gtm.py`: 3 vídeos en el lanzamiento y después quincenal), y por eso allí la rama base tiene 24 suscriptores en la P1 y 107 en la P2, frente a 25 y 108 aquí. Solo cambia el calendario [INT, tribunal final, 2.ª ronda].

**Resultado acumulado a M36** (modelo de retornos, sin premios ni ajustes de integración; **condicionado a que haya voz**, y con la caja del modelo; el resultado integrado está en el §1.3):

| Camino | Prob. | Ingresos | Caja | Horas | Resultado de caja | € por hora |
|---|---|---|---|---|---|---|
| P1: se para en la P1 | 61,8 % | 0 | 210 | 102 | **−210** | −2,1 |
| P2: se para en la P2 | 11,1 % | 0 | 870 | 312 | −870 | −2,8 |
| P3: base → mantenimiento | 17,0 % | 65 | 1.890 | 666 | −1.825 | −2,7 |
| P4: optimista | 10,2 % | 6.865 | 3.510 | 1.152 | **+3.355** | +2,9 |

**Puntos de equilibrio.**
- **P4:** en el modelo (caja de 110 €/mes), equilibrio mensual en **M15** y acumulado en **M25**; con las horas a 15 €/h, después de M36. **[INT] Con la caja integrada:** con 138 €/mes (solo el revisor de escucha), el equilibrio mensual pasa a **M18** (en M17 ingresa 135 €); con la garantía de calidad pagada por el promotor (≈ 552 €/mes), **no llega en 36 meses** (509 € en M36). Si terceros pagan el diferencial (Puerta F2), la caja del promotor vuelve a la del modelo y el equilibrio mensual vuelve a **M15**.
- **P3:** nunca.
- **Mantenimiento del P3** (~300 € y 144 h): **sin la opción CRTVG no compensa**; es mejor cerrar en M18. El árbol conjunto (§1.3) aplica ese cierre.

### 1.7 Premios, encargos y ayudas: qué tiene tasa base

**Youtubeiras+** (entra en el caso central con su tasa base):
- **Canales presentados:** 68 (2023), 89 (2024) y **126 (2025)**, para ~6 premios de jurado [F youtubeiras.gal].
- **Ganadores:** se gana con canales pequeños (56-2.100 suscriptores). La historia de Galicia premia con regularidad. No se conoce ningún ganador con voz de IA [OBS; no comprobado vídeo a vídeo].
- **Probabilidad usada:** 4 % por edición; 6-8 % en 2027 para P3 y P4.
- **Premio neto:** 810 €.

**CRTVG** (opción, sin tasa base):
- **Lo que se sabe:**
  - 2024: 12 proyectos y 300.000 €, entre ellos **"Respira"**, meditaciones en galego, el comparable más cercano a un formato para dormir.
  - 2025: convocatoria de 15 plazas y 357.000 €, **resuelta con 12 y 339.000 €**; el videopódcast quedó desierto.
  - **No se publica el número de propuestas presentadas.**
- **Lo que piden las bases de 2025 (leídas las 23 páginas):** alta en el IAE y en autónomos; proyecto inédito; cesión exclusiva, mundial y hasta el dominio público; declaración de autoría del guion. **No mencionan la IA.**
- **Cuándo compensa:**
  - con una probabilidad de ganar **≥ 7,2 %**, el valor esperado del modelo se vuelve positivo;
  - con **≥ 23 %**, se rescata el camino base.
- **Recomendación:** ejercerla solo si se pasa la P3 y el promotor acepta darse de alta. Antes, pedir la tasa de 2025 a proxectosav@crtvg.gal.

**B2B, Xacobeo y Ministerio** (fuera del caso central):
- **B2B:** compensa con **≥ 11 % por año** de probabilidad de encargo.
- **Xacobeo:** exige alta ya en octubre de 2026.
- **Ministerio:** cofinancia gasto, no deja margen.

### 1.8 Etapa 3 (solo en el camino P4)

| Rama E3 | Prob. [S] | Vistas es+pt/mes en M36 | Ingreso E3/mes | Resultado E3 a M36 |
|---|---|---|---|---|
| Fracasa | 55 % | 5.000 | 10 € | −4.525 € |
| Modesta | 25 % | 72.000 | 144 € | −3.252 € |
| Buena | 15 % | 360.000 | 720 € | +2.220 € |
| Ganadora | 5 % | ~1.000.000 | ~2.000 € | +14.380 € |
| **Valor esperado** | | | **~250 €/mes** | **−2.250 €** |

- **Antes de licenciar voz**, conviene probar la **"E3 ligera"**: solo castellano, con un TTS maduro, por ~500 € + 60 €/mes. Con las mismas probabilidades, su valor esperado a M36 es de ~+790 € [S].
- **Una temporada vendida a la CRTVG no se puede localizar**, porque se cede el doblaje.

### 1.9 Qué variable manda (sensibilidad)

1. **Manda la probabilidad de estar en la rama alta.** Para que el valor esperado del modelo salga positivo hace falta P(alta) ≥ ~17 % (hoy es 12 %). **[INT]** En el árbol conjunto, si el promotor paga la garantía de calidad, ni siquiera una rama alta segura daría caja positiva a M36; solo con las Puertas F y F2 el optimista sale positivo (§1.3). Dentro de un camino mandan la **cola larga** (la reescucha del catálogo) y el **crecimiento**, y las dos dependen de la calidad del galego y del guion.
2. **En el modelo, el patrocinio decide el signo del camino optimista** (−720 € ↔ +3.355 €). **[INT]** Si el promotor paga la garantía de calidad ya no lo decide: el optimista es negativo incluso con patrocinio. Con las Puertas F y F2 vuelve a decidirlo (§1.3). El precio está anclado en el mercado; lo incierto es la **tasa de venta** a marcas gallegas.
3. **El RPM, los anuncios y Spotify casi no importan en galego.**
4. **El valor de la hora cambia la foto por completo** (−5.070 € con las horas a 15 €/h en el modelo): es un hobby con opción, no un negocio.
5. **[INT, tribunal final, 2.ª ronda] En la política recomendada manda P(F)**, la probabilidad de que terceros paguen la calidad: decide cuánto se publica y cuánto se gasta en validación (§1.3). Es la primera cifra que el piloto sustituye (§1.10).

### 1.10 Qué sustituye el piloto

| Supuesto crítico | Dato real que lo sustituye | Cuándo |
|---|---|---|
| A1 y la rama de audiencia | Vistas a 7 y 30 días de los vídeos 1-4 | M4 (**recalibrar la P1**) |
| A3 (cola larga) | Vistas mensuales de los vídeos con más de 60 días | M5-M6 |
| A6 (conversión) | Suscriptores / vistas | P1 |
| A14 (tasa de venta del patrocinio) | Respuestas a 5-10 propuestas | M9-M12 (condición de la P2) |
| Probabilidad de la voz | Resultado de la Puerta V-0 y de la Puerta V | Semanas 4-12 |
| P(F) y P(F2) | Compromisos firmados de terceros (Puerta F) y, en la P1, para la E2 (Puerta F2) | Semana 5 y M6 |
| Tasa de la CRTVG | Pregunta directa a la CRTVG y bases de 2027 | Antes de la P3 |

---

## 2. Mercado y audiencia

### 2.1 El mercado en cifras

| Indicador | Dato | Fuente |
|---|---|---|
| Población de Galicia (1-1-2025) | 2.714.741 | [F] INE, vía El Progreso |
| Saben hablar galego "moito" o "bastante" | 83,4 % | [F] IGE, EEF 2023 |
| Hablan habitualmente en galego | 46,2 % | [F] IGE |
| **Ven audiovisual "sempre" o "máis" en galego (16 años o más)** | **3,59 %** | [F] IGE |
| Escuchan radio "sempre" o "máis" en galego | 15,13 % | [F] IGE |
| Oyentes de pódcast que lo usan antes de dormir | 30,6 % (Prodigioso Volcán, 2025) - 37 % (NielsenIQ/Audible) | [F] |
| La historia en el ranking de géneros de iVoox | 2.º puesto, 14,08 % | [F] iVoox, 2025 |

**Lectura.** El galego se entiende y se habla, pero **no se consume en pantalla**. En radio, el consumo mayoritario en galego es 4 veces el del audiovisual online (15,13 % frente a 3,59 %). **Por eso el producto se piensa como audio que se escucha a oscuras, no como vídeo que se mira**, y se publica también en Spotify, iVoox y Apple.

**Embudo arriba-abajo** [S sobre las tasas F]:
- 2,1 M de internautas de 16 años o más;
- × 47,3 % que escucha audio largo cada semana;
- × 30,6-37 % que lo hace antes de dormir;
- × 3,6-18 % que lo aceptaría en galego;
- × 15-30 % con interés por la historia.
- **Resultado: ~2.000-20.000 oyentes habituales.**
- Pasado a reproducciones (8 noches al mes por oyente [S]): un **techo de 16.000-160.000 vistas al mes**. La cuota realista del único canal del nicho es del 10-30 %.

**Triangulación con el modelo** (M36):
- **Base:** 1.715 vistas al mes, el 11 % del techo bajo.
- **Alta:** 13.440 vistas al mes. Solo es posible si el mercado está en la mitad alta del rango o si hay desbordamiento a público no galegofalante. Por eso la rama alta pesa solo un 12 %.

**Fuera de Galicia:**
- **Diáspora:** 563.303 inscritos en el exterior, pero solo el 23 % nació en Galicia [F Praza]. Es un nicho emocional, no de volumen.
- **Quienes aprenden galego:** más de 4.000 inscripciones en las pruebas CELGA en 2025 [F débil, a confirmar].
- **Desbordamiento algorítmico:** es una hipótesis (el caso atípico de "VaniMani en galego") que se mide con el experimento E7.

### 2.2 Competencia

- **Directa (historia o relatos para dormir, en galego, para adultos): ninguna** [OBS].
  - Lo más parecido: un canal de ASMR en galego inactivo (273 suscriptores) y nanas infantiles (Galego para peques, 2,48K suscriptores).
- **Indirecta 1: historia para dormir en castellano con temas gallegos.**
  - RELATOS AL OIDO, "DUÉRMETE CON las Leyendas… de GALICIA": **107.810 vistas** en 11 meses.
  - Imperios y Misterios, "O origen dos galegos": 22.541 vistas.
  - Líderes del género: El Historiador Nocturno (304K suscriptores) y Detrás De La Historia (65K en ~13 meses).
- **Indirecta 2: divulgación en galego, que no es para dormir.** Son aliados antes que competidores:
  - Historia a Debate (9,27K suscriptores);
  - Orgullo Galego (11,5K);
  - Falemos do Reino de Galicia (2,1K);
  - Burla Negra ("O Reino Suevo da Galiza", 23.763 vistas);
  - TVG "Historias de Galicia" (670-3.900 vistas por capítulo);
  - el pódcast Descifrando a Historia.
- **Indirecta 3: apps de sueño.** No tienen catálogo en galego; Storytel España tampoco.
- **Indirecta 4: medios públicos.** La CRTVG tiene categoría de historia en su plataforma de pódcast y financió "Respira". Puede ser competidor, cliente o las dos cosas.

**Mapa de posicionamiento:**

| | Divulgación "despierta" | Para dormir |
|---|---|---|
| **Castellano** | Crónicas de la Historia, CARKI | RELATOS AL OIDO, El Historiador Nocturno, decenas de clónicos IA (saturado) |
| **Galego** | Historia a Debate, Orgullo Galego, TVG, Burla Negra | **Serán: vacío** |

Dentro de "para dormir", el eje de calidad separa la *fábrica IA* del *oficio*:
- **Fábrica IA:** Sleepless Historian ha pasado de 2-4 M a 8-31K vistas por vídeo.
- **Oficio:** History Time, History at Night.
- **Serán se coloca en galego × para dormir × oficio.**

### 2.3 Calibración con canales nuevos sin audiencia [OBS, 29-09-2026]

Búsqueda de "historia aburrida para dormir": salen más de 17 canales clónicos. La mayoría se queda en 1-60 suscriptores y en una mediana de **20-60 vistas por vídeo en toda su vida**.

Los que despegan (2-3 de más de 17, ~15 %) lo hacen con tres cosas fuera del alcance del promotor:
- volumen industrial: 80-220 vídeos, casi diarios;
- redes de colaboración;
- el mercado hispano entero.

Datos brutos: `gauntlet/model/obs_clonicos_29-09-2026.txt`.

A favor del proyecto hay tres cosas: el nicho vacío, la siembra manual en comunidades gallegas y una curaduría superior. **Eso justifica una base de 2-3 veces la del clónico, no de 10 veces.**

### 2.4 Segmentos y propuesta de valor

| Segmento | "Trabajo" que encarga | Qué le damos | Qué le haría irse |
|---|---|---|---|
| **A. Galegofalante adulto (35-70 años) con hábito de audio nocturno** (núcleo) | "Axúdame a desconectar na miña lingua" | Voz calmada, temas de su tierra, 1-2 h, cola de ambiente | Un error de lengua o una pronunciación "de castellano"; un anuncio que despierta |
| **B. Quien aprende o recupera el galego** | "Quero escoitar galego bo, amodo" | Ritmo lento, galego normativo, **subtítulos manuales exactos** (el guion) | Vocabulario demasiado culto sin contexto |
| **C. Diáspora nacida en Galicia** | "Quero volver á casa un anaco cada noite" | Paisaje, aldea, emigración, lendas | La sensación de "producto de fábrica" |
| **D. Mediadores** (docentes, bibliotecas, servicios de normalización, entidades) | "Contido en galego que poida recomendar sen vergoña" | Fuentes, créditos, transparencia, capítulos sueltos | Cualquier sospecha de errores o de engaño sobre la IA |

**Declaración de posicionamiento (interna).** Para galegofalantes adultos que se duermen escuchando audio y no encuentran nada en su lengua, Serán es el único canal de historia para dormir en galego. **El foso es la calidad lingüística e histórica, no la IA.**

**Qué NO se promete:** efectos terapéuticos. La Sociedad Española de Neurología alerta sobre productos para el insomnio "sin validez médica" [F]. Se dice "para acompañar o sono", nunca "cura o insomnio".

---

## 3. Producto y formato

Pieza "formato" del gauntlet (3 rondas, mejora marginal). **La contradicción de ritmo que dejó abierta se resuelve aquí, en la tabla única del §3.3.**

### 3.1 Listón y techo

| Papel | Vídeo | Datos [MED] | Por qué |
|---|---|---|---|
| **Listón elegido** | History at Night, "The Great Maya Collapse" (https://www.youtube.com/watch?v=hbufma0ZlUw) | 1,16 M de vistas; 47 min; 157 palabras/min; 6 vídeos en el canal; "NO AD BREAKS" | Mismo modelo de producción: IA dirigida y verificada por un humano, voz clonada con licencia, bibliografía. Demuestra que "pocos vídeos y excelentes" funciona. **No publica desde el 29-01-2026**: se toma su producto, no su cadencia |
| Techo de calidad | History Time, "After Rome" (https://www.youtube.com/watch?v=sXBgNNtEJ6M) | 27,9 M de vistas; 3 h 28 min; ~98 palabras/min; voz humana; 114 pausas de ≥ 8 s | Tema gemelo (la Gallaecia sueva). Sirve para medir la distancia, no como objetivo |
| Mercado vecino | Relatos para Dormir, "¿Cómo era un día completo en la Edad Media?" | 1,05 M de vistas; 124 palabras/min | La "vida cotidiana" funciona en una lengua románica |
| Anti-referencia | Sleepless Historian | Cambios de imagen cada ≤ 10 s; segunda persona burlona; rendimiento desplomado | Justo lo que no somos |

**En qué superamos deliberadamente al listón:**
- **Ritmo:** 110-125 palabras/min frente a 157.
- **Llamada a suscribirse:** ninguna en la voz.
- **Imagen:** luminancia de 40-70/255, frente a 86.
- **Estructura:** el conflicto se concentra en el primer 35-40 %. Es la regla de la guionista de Calm, "If there's any action, it has to start in the beginning" [F Slate].
- **Transparencia:** una "Nota sobre o proceso" en cada episodio.

### 3.2 Promesa, duración y estructura

- **Promesa del canal** (galego, pendiente de revisión lingüística): *"A historia de Galicia contada amodo, nun galego coidado, para que te deixes levar ata o sono. Sen sustos e sen présa. Cada noite, un serán."*
  - **"Sen cortes" no forma parte de la promesa del canal** (§3.5, regla 13).
  - **[INT]** La pieza de mercado lo incluía: se alinea con la de formato.
- **Duración:**
  - **Etapa 1:** 75 min narrados (rango 60-90) + 20-30 min de cola de ambiente.
  - **Etapa 2:** 2 h + 30-45 min de cola.
  - **Palabras:** ~8.400-8.600 por episodio de 75 min (el Ep. 1 presupuesta 8.435) y ~13.800 por episodio de 2 h.
- **Minutado del episodio tipo de 75 min:**

| Bloque | Tiempo | Contenido | Densidad máxima de datos |
|---|---|---|---|
| 0. Umbral | 0:00-0:15 | Solo ambiente (chuvia) y sello sonoro de 4 s | 0 |
| 1. Entrada suave | 0:15-2:30 | **Aviso de voz sintética (≤ 30 s)** → escena de lugar en presente → "Isto é Serán…" → qué se cuenta esta noche → permiso para dormirse → "acomódate". Sin CTA | 1 fecha, 2 nombres propios |
| 2. Acto I: contexto y movimiento | 2:30-28:00 (~35 %) | El "qué pasó", con **el final ya anticipado**; la violencia, con distancia | ≤ 3 nombres propios nuevos por minuto; fechas redondeadas |
| 3. Acto II: vida y paisaje | 28:00-62:00 (~45 %) | Cómo se vivía; descripción sensorial lenta; repeticiones suaves | ≤ 1 nombre nuevo por minuto; sin cifras |
| 4. Acto III: desenlace que se apaga | 62:00-73:30 (~15 %) | Qué quedó; presente contemplativo; **ritmo percibido ~9 % más lento, sobre todo con pausas más largas** (§3.3) | 0 fechas; ≤ 0,3 nombres por minuto |
| 5. Despedida | 73:30-75:00 | Relajación guiada de 60-90 s y "Boas noites" | 0 |
| 6. Cola de ambiente | 75:00-100:00 | Solo ambiente; pantalla casi negra | — |

- **[INT] Posición del aviso de voz.** La pieza de formato ponía la escena de lugar antes del saludo, y la de mercado pedía el aviso hablado en los primeros 30 s por el art. 50.5 del AI Act. Solución: una frase de aviso nada más empezar ("Boas noites. A voz que vas escoitar é sintética…") y luego la escena. Así se aplica en el guion muestra.
- **Curva de tensión:** máxima entre el 10 % y el 30 % del episodio y siempre descendente desde el 40 %. El auditor puntúa la "activación" de cada capítulo de 1 a 5; en el Ep. 1 la serie es 1-2-3-3-2-1-1-1-1-0.
- **Reglas de escritura:**
  - tercera persona narrativa; "ti" solo en la entrada y la despedida;
  - frases de 15-30 palabras;
  - sin números largos;
  - lo reconstruido se marca como tal ("podemos imaxinar");
  - nunca se inventan diálogos de personas reales;
  - topónimos en la forma oficial;
  - norma RAG con lista negra de castellanismos, sin lusismos ni hiperenxebrismos;
  - tiempos simples ("chegara");
  - sin militancia: los debates historiográficos se exponen como tales.

### 3.3 Tabla única de ritmo (manda sobre todas las secciones) [INT]

**El problema que dejaban abierto las piezas:**
- **Formato:** su brief pedía 120-135 palabras/min de habla pura en los Actos I-II; su receta (con una velocidad natural supuesta de 150) daba ~143; su checklist aceptaba 105-130 percibidas, mientras su control de calidad exigía 115 ±5 %; y en un sitio decía "+10 % de pausa" en el Acto III y en otro "+35 %".
- **Voz:** pedía ~140-155 de habla pura.
- **Pipeline:** midió **191,5 palabras/min** de habla pura en la voz Brais de Nós [P: 395,2 s para 1.263 palabras en `bench_cpu/per_sent.json`; 193,1 en `bench_tts_2.json`, 314 palabras]. Con ese dato, su control `ritmo.py` (escala de pausas k de 0,7-1,6 y `speed` ≥ 0,85) no puede llegar a 118.

**Qué se decide:**
1. **Lo único que es objetivo es el ritmo percibido**: palabras del guion ÷ minutos de audio narrado (pausas incluidas, sin la cola).
2. **El habla pura NO es objetivo:** es el resultado de la voz (r_nat ÷ V) y se mide en el paso 0 de calibración de cada voz.
3. **Las pausas se derivan con la fórmula de formato** (P_párrafo = 2,8 × P_frase; pausa de capítulo de 7-8 s). El reparto entre estiramiento de la voz (V) y silencio lo decide **una prueba ciega con audio real** (G0), no un tope escrito de antemano.

**Objetivos (los mismos en el brief, el render, la QA, la checklist, el pipeline, el guion y el kit de voz):**

| Bloque | Ritmo percibido objetivo | Tolerancia de QA | Nota |
|---|---|---|---|
| Entrada (cap. 1) | ~107 | ±5 % | Escena lenta |
| **Actos I y II** | **115** | **±5 % (109-121)** | Centro de la banda de 110-125 |
| **Acto III** | **~105** | **Entre un 8 % y un 12 % más lento que el Acto II** | Se consigue sobre todo con pausas **~30-40 % más largas** que en el Acto II y, si G0 lo permite, con +5 % de V |
| Despedida | ~100 | — | Pausas de respiración de 4-6 s |
| Media del episodio | ~112 (8.435 palabras / 75 min) | 8.000-8.900 palabras | Recuento del guion |

**Cómo se reparte con la voz medida.** Con r_nat = 191,5 y el minutado del Ep. 1, estas son las variantes que se prueban a ciegas en G0 (cálculo con la fórmula de formato §3A.3: frases de 20-22 palabras, 4-5 frases por párrafo):

| Variante de G0 | V (`DUR_SCALE`) · `speed` | Habla pura | Silencio (Actos I-II / III) | P_frase (I-II / III) | P_párrafo (I-II / III) |
|---|---|---|---|---|---|
| A: "silencio largo" | 1,10 · 0,91 | 174 | 34 % / 40 % | 2,5-2,6 s / 3,4 s | 6,9-7,4 s / 9,6 s |
| B | 1,18 · 0,85 | 162 | 29 % / 35 % | 2,1-2,2 s / 3,0 s | 5,9-6,3 s / 8,5 s |
| C | 1,25 · 0,80 | 153 | 25 % / 31 % | 1,8-1,9 s / 2,7 s | 5,0-5,3 s / 7,6 s |
| D: "voz estirada" | 1,43 · 0,70 | 134 | 14 % / 21 % | 1,0 s / 1,8 s | 2,8-2,9 s / 5,1 s |
| E | 1,0 + `atempo` 0,9 en posproducción, con pausas como en B | — | — | — | — |

**Regla de decisión de G0** [S]:
- Todas las variantes suenan a 115 percibidas, porque solo cambia el reparto entre estiramiento y silencio.
- Juzgan el promotor y su mujer a ciegas, de 1 a 5, en "durmiría con isto" y en naturalidad.
- **Gana la variante con la mejor nota en "durmiría" que no reciba ninguna marca de "vocais arrastradas"** y cuyo WER no suba más de 1 punto.
- Los topes anti-"voz de goma" (V máxima, P_frase y P_párrafo máximas) **se fijan a partir de la ganadora** y se escriben en `decision_voz.md`.
- **Precedente del género:** con silencios largos. History Time tiene 114 pausas de ≥ 8 s en 207 min [MED].

**Consecuencias en cada parte del plan:**
- **Brief del narrador:** el ritmo se juzga como "percibido, 115" más la ausencia de "vocales arrastradas". El habla pura se anota como dato, no se puntúa.
- **Kit de voz (E0, R1):** las muestras de 105, 115 y 125 percibidas se hacen **variando solo las pausas, con V fija**.
- **`ritmo.py` del pipeline:**
  - Las pausas base por acto son las de la variante ganadora.
  - La escala k se ajusta por párrafo entre 0,8 y 1,25 alrededor de esos valores, con `speed` fijo para todo el canal.
  - Si k se sale del rango, el párrafo se marca; **nunca se toca el texto**.
- **Checklist de salida:** ritmo por acto a ±5 % de su objetivo y Acto III entre un 8 % y un 12 % más lento que el II. Sustituye al "105-130".
- **Guion muestra:** las pausas de 0,6-0,9 s de su cabecera quedan anuladas.

### 3.4 La voz como render: receta ejecutable

- **Palancas reales de cada modelo de Nós** [comprobado en su código el 29-09-2026]:
  - **No hay SSML** y StyleTTS2 no expone la velocidad.
  - La velocidad se controla con un parche de una línea en la duración predicha (`DUR_SCALE`, la misma técnica que usa Kokoro).
  - Las pausas las inserta un **renderizador propio, frase a frase**, porque el script original concatena las frases sin silencio.
  - En VITS la velocidad es `length_scale` y en Matcha, `speaking_rate`.
- **Estilo:**
  - Se usa una referencia de estilo "REF-CALMA", elegida entre las frases más lentas y estables del corpus, con `beta` 0,6.
  - Se fuerza la referencia "normal" en todas las frases, para evitar saltos de estilo en `?` y `!`.
  - El estilo se guarda en cada frontera de párrafo (`s_prev`) y cada párrafo lleva su propia semilla, de modo que regenerar un párrafo no cambia los siguientes.
- **Pronunciación:** un léxico `lexico_gl.tsv` validado por el lingüista contra el *Dicionario de pronuncia da lingua galega* y el DRAG, **aplicado dentro de la fonemización de Cotovía** (`g2p_override.py`, prototipo probado [P]).
  - Incluye nombres propios (Hidacio, Hermerico, Leovixildo…) y palabras trampa de apertura vocálica y metafonía (*pedra, terra, xente, home, novo/nova/novos, porto/portos*) y de nasal velar (*unha, ningún*).
  - **Ninguna entrada se activa sin la marca `verificado`.**
- **Guion sin nombres latinos en voz** (*Aquae Flaviae* se dice "Chaves"), sin cifras escritas y sin abreviaturas.

### 3.5 "Sono seguro": 14 reglas verificables

| # | Regla | Umbral |
|---|---|---|
| 1 | Volumen constante | −16 LUFS integrados (±1); YouTube no lo sube [F] |
| 2 | Sin picos | *True peak* ≤ −1,5 dBTP; rango de sonoridad (LRA) ≤ 5 LU; ningún evento > 3 dB sobre la media móvil de 3 s |
| 3 | Ambiente por debajo de la voz | Cama 20-26 dB por debajo |
| 4 | Voz sin brillo agresivo | De-esser; caída suave por encima de 8-10 kHz |
| 5 | Sin *glitches* de TTS | Detector automático + escucha (§4.6); fundidos de 15 ms |
| 6 | Pronunciación | 0 palabras del guion fuera del léxico validado; ≥ 27/30 en las frases trampa |
| 7 | Sin llamada a suscribirse en la voz | 0 menciones; la CTA va en el comentario fijado y en una pantalla final muda |
| 8 | Sin sobresaltos narrativos | Activación decreciente; campanas a −30 dB o menos |
| 9 | Sin sobresaltos visuales | Fundidos de 2-3 s; zoom ≤ 3 % por plano |
| 10 | Tarjetas y pantallas finales mudas | Pantalla final solo al terminar la cola |
| 11 | Pre-roll y post-roll | Solo se activan o desactivan juntos [F]. La cola de 20-45 min hace de colchón para el anuncio final |
| 12 | Mid-rolls | Etapa 1: ninguno **activado por el canal**. Etapa 2 (en el YPP): 0-2, solo en los primeros 20 min |
| 13 | **Honestidad del "sen cortes"** | **[INT, corrección factual]** Fuera del YPP, YouTube **puede poner anuncios** en los vídeos sin pagar al creador (derecho a monetizar de los Términos de servicio actualizados en 2020-2021, https://www.youtube.com/t/terms). Por eso **en la Etapa 1 no se usa la etiqueta "sen cortes"** en títulos ni miniaturas: no se puede garantizar. Solo se usa en la Etapa 2, en el YPP y con los mid-rolls desactivados |
| 14 | Temporizador | Línea fija en la descripción: "Podes usar o temporizador de apagamento de YouTube" [F: la función existe]. **[INT, corrección lingüística]** "Apagado" como sustantivo es un castellanismo: en el DRAG es participio o adjetivo, y el sustantivo de acción es *apagamento* ("Acción e efecto de apagar ou apagarse", https://academia.gal/dicionario/-/termo/busca/apagamento). **Pendiente [S]:** si la interfaz de YouTube en galego tiene una etiqueta propia para la función, se cita esa entre comillas |

### 3.6 Paisaje sonoro, identidad visual y metadatos

- **Paisaje sonoro galego como sello de marca:**
  - **Ambientes:** chuvia en lousa (por defecto), carballeira, ría en calma, lareira (con los chasquidos limitados a +6 dB), río y muíño, noite de verán.
  - **Música:** mínima, un *drone* de zanfona solo en los cambios de capítulo; se evita la gaita.
  - **Origen, por prioridad:** grabaciones propias (evitan reclamaciones de Content ID, que tienen precedente [F Tubefilter]); después Freesound, solo CC0 o CC BY; después la Biblioteca de audio de YouTube.
- **Identidad visual "noite atlántica":**
  - Óleo o *matte painting* **no fotorrealista**, sin caras en primer plano.
  - Paleta noite `#0E1A22`, lousa `#2B3A42`, musgo `#3F5A4A`, néboa `#C9D1D3` y candea `#D9A05B`.
  - Luminancia de 40-70/255 en los Actos I-II y < 20 en el III.
  - Una imagen cada 40-90 s.
  - Plantilla de prompt fija: ESTILO + MOTIVO + LUZ + NEGATIVO.
  - Los monumentos reales se hacen desde foto real o de dominio público repintada, nunca "de memoria".
- **Títulos:** `[Tema en galego] ([fechas]) | Historia de Galicia para durmir`.
  - Ejemplo de la Etapa 1, **sin "sen cortes"** (regla 13): *"O Reino suevo de Gallaecia (411-585) | Historia de Galicia para durmir"*.
  - La descripción va en galego, con la línea bilingüe "(Narración en galego · Historia de Galicia para dormir, en gallego)", capítulos, fuentes y "Nota sobre o proceso".

### 3.7 Catálogo, series y derivados

- **Catálogo de 30 temas puntuados.** Puntuación de producto: P = 2·D + Dem + Fx − R, donde D es "durmibilidade", Dem la demanda medida, Fx las fuentes y los visuales, y R el riesgo. Prioridad de lanzamiento: L = P + Dem.
  - **Etapa 1, en orden:** Reino suevo (L = 20; hoja de producción completa del Ep. 1), aldea del s. XV (19), Camiño del s. XII (20), castro (18). Después, dos experimentos deliberados: **lendas amables** (la mayor demanda medida en castellano) e **irmandiños** (tema caliente, con la muestra de guion de este plan).
  - Con el calendario integrado, **el episodio de las Letras 2027** (Neira Vilas: "a aldea dos anos corenta e a emigración") entra como vídeo 12.
- **Temas excluidos:** Guerra Civil, represión y franquismo; política contemporánea, Prestige e incendios; terror folclórico como episodio propio; "misterios" especulativos.
- **Series** como defensa frente al "contenido inauténtico":
  - "Gallaecia";
  - "O mundo labrego";
  - "O mar";
  - "O Reino".
  - Cada una con su ambiente y su mapa.
- **Derivados:**
  - **Videopódcast en Spotify:** la única vía al ingreso Premium del SPP. Un solo corte de anuncio, en 00:00.
  - **Feed de audio** en Apple e iVoox.
  - **"Postais" verticales** de 60-90 s.
  - **Capítulos sueltos** (Etapa 2).
  - **Compilaciones solo con montaje nuevo:** como mucho 1 al mes y, en la Etapa 1, **solo en el pódcast**, no en el canal principal. **[INT]** La pieza de formato proponía una compilación mensual en el canal desde la Etapa 2; el pipeline y el GTM la frenaban por el riesgo de *reused content*. Se aplica la regla más prudente.
  - **Pistas de audio es/pt:** Etapa 3.
- **Nombre:** **Serán** [F, Dicionario da RAG, https://academia.gal/dicionario/-/termo/busca/serán: "Parte do día que vai desde que comeza a pórse o sol ata que se fai noite"; "Reunión de mulleres para fiar que se facía destas horas"; "Reunión nocturna de carácter festivo"].
  - **[INT, corrección de cita]** La versión anterior citaba "reunión nocturna… para contar", que no está en ninguna acepción. El vínculo con el relato nocturno es una **lectura de marca [S]**, no una definición del diccionario.
  - @seran y seran.gal libres [COMP].
  - **Pendiente:** búsqueda de la marca en la OEPM y la EUIPO.
  - Alternativas: "Á Luz do Candil" y "Historia para Durmir" (mejor como subtítulo). Se descartaron "Arrolo" (suena infantil) y "A Lareira da Historia" (espacio saturado).
- **Episodio 1 listo para producir:** *O Reino suevo de Gallaecia (411-585)*.
  - 10 capítulos, 8.435 palabras y 74 planos.
  - Fuentes primarias (Hidacio, Martiño de Dumio, *Parochiale suevorum*) y secundarias (Díaz 2011, Sánchez Pardo 2014, Fernández Calo 2015).
  - Prosa de muestra de los Actos II y III, y metadatos completos.
  - Está en la pieza de formato del gauntlet (`drafts/formato.md` §11). Su bibliografía está en el Anexo B.

---

## 4. Voz y guion en galego: estrategia y calidad

Esta sección integra dos piezas del gauntlet:
- **Voz:** se paró en 5 rondas por presupuesto, con una carencia abierta: la prueba ciega de escucha larga (§4.3).
- **Guion:** mejora marginal en 4 rondas; sus correcciones finales se aplican en la copia del guion muestra.

### 4.1 El listón

**La voz tiene que ser indistinguible de un narrador nativo profesional en una prueba ciega**, no solo "sonar bien". Si ninguna voz sintética lo consigue, **no se publica con voz sintética**; no existe la opción de "publicar con la menos mala". Así se aplica la condición de que la narración es imprescindible.

**Expectativa honesta [S]:** es **probable (60-80 %)** que hoy ninguna voz en galego "de fábrica" pase la identificación ciega frente a narradores profesionales. El plan trata ese suspenso como **escenario central**.

### 4.2 Opciones de voz

| Opción | Galego | Datos del corpus | Coste por hora publicada | Licencia | Papel |
|---|---|---|---|---|---|
| **A. Nós StyleTTS2 Brais / Celtia** | Nativo (Cotovía) | Brais: locutor profesional, ~18 h. Celtia: locutora profesional, ~25 h. Ambos **a 16 kHz** (ancho de banda útil ≤ 8 kHz). DNSMOS predicho: 3,40-3,44 [F fichas] | < 0,10 USD (0 € en CPU) | **Modelo** Apache-2.0. **Dataset:** CC-BY-4.0 declarado, pero sus términos lo restringen a investigación ("solely for research purposes") y prohíben la "public exposure" de las grabaciones [F] | **Favorito**, condicionado al doble permiso (§4.5) |
| B. Nós VITS / Matcha (Sabela-Nós, Icía, Iago, Paulo) | Nativo | Sabela-Nós: locutora de radio profesional; el resto, *amateurs* | 0 € (CPU) | Ídem | Reserva gratuita |
| C. Azure Sabela / Roi | Oficial | Sin estilos ni voz personalizada en gl-ES; salida a 48 kHz | ~0,84 USD (gratis dentro de 500k caracteres/mes) | Condiciones de Azure; hay que revelar que es sintética [F] | **Línea base**; es la voz que el promotor ya probó en Clipchamp |
| D. Gemini-TTS gl-ES | **Preview** | Control por prompt; 24 kHz | ~1,2-2,3 USD | Google Cloud | Aspirante |
| E. ElevenLabs v4 / v3 | Galego listado | Muy expresivo; acento sin comprobar | ~4,5 USD | Uso comercial desde el plan Starter | Aspirante |
| F. OpenAI | Probable acento extranjero | — | ~1,2 USD | Exige avisar de que es IA | Solo criba automática |
| G. Locutor galego con licencia (clon o *fine-tune*) | Nativo | 48 kHz | 20-60 €/h amortizados | Contrato | Plan B y Etapa 3 |
| *Excluida:* `edge-tts` | | | | Va contra los términos de Microsoft [F-sec] | — |

**Precisión de fechas [INT, corrección de la revisión].** La ficha del modelo StyleTTS2 de Nós solo indica **2026** como fecha de publicación. La mención de "junio y julio de 2026" no está en la ficha consultada.

**Lectura.** Salvo la licencia de un locutor, ninguna voz supera los 45 USD al mes. **El precio no decide la voz; lo que cuesta de verdad son las horas de escucha y corrección.**

### 4.3 Protocolo ciego de validación (Puerta V)

- **Referencias humanas con control positivo:**
  - **Dos narradores galegos profesionales (H1, un hombre, y H2, una mujer)** graban el texto trampa y ~30 min del guion piloto a 48 kHz y 24 bits.
  - En cada pantalla, uno hace de referencia y el otro **se esconde como una condición más**: tiene que pasar la misma puerta que la IA. Si no la pasa, el test está mal calibrado y no se castiga a la voz (recalibración prerregistrada con un tope).
- **Rondas:**
  - **R0:** criba automática con ASR.
  - **R1:** MUSHRA (promotor y mujer) con tres escalas: A corrección galega, B naturalidad, C calma.
  - **R2:** preferencia por pares y **2-3 noches de sueño real** en dispositivos reales.
  - **R3:** panel de **20-24 nativos con un filólogo**. Primero la **identificación ciega humano/IA en seco** (10 fragmentos de ~3 min, 5 voces × 2, con control positivo y negativo, análisis por oyente, exactitud equilibrada con *bootstrap*); después un MUSHRA ligero.
  - **R4:** repetición sobre el episodio publicado, antes de monetizar.
- **Umbrales de publicación (Puerta V-2)**, fijados y sellados antes de escuchar:
  - Δ ≤ 10 puntos (o el umbral recalibrado) frente a la referencia oculta en A, B y C, con el IC 90 % ≤ U + 5;
  - menos del 20 % del panel señala "non é galego";
  - exactitud equilibrada de identificación ≤ 0,60 (IC 90 % ≤ 0,70);
  - control negativo ≥ 0,75.
- **Potencia simulada** (con correlación dentro de cada oyente): con N = 20, una voz claramente detectable (exactitud equilibrada ≥ 0,70) se cuela en ≤ 3 % de los casos, y una indistinguible aprueba en el 88-97 %.
- **Carencia abierta (lo que el gauntlet no cerró).** El crítico de audio y doblaje pidió una **prueba ciega de escucha larga "R3-L"**, porque el producto se escucha 1-3 h seguidas y hoy solo se validan fragmentos de ~3 min. La propuesta:
  - un bloque continuo de 20-25 min por oyente, humano o candidata, en diseño entre sujetos;
  - la pregunta "¿Persoa ou IA?" y el minuto de la primera sospecha;
  - 40-60 oyentes, o un diseño cruzado con dos textos;
  - H1 y H2 grabando un bloque continuo;
  - medir por máquina la repetitividad prosódica de 60 min.
  
  **No está diseñada ni presupuestada** en este plan. Se recomienda añadirla antes de monetizar (R4), porque la Puerta V actual no demuestra por sí sola la calidad de "audiolibro profesional" en narraciones de 1-3 h.

### 4.4 Árbol de decisión de la voz y coste

**[INT] Puerta V-0: preselección barata antes de gastar**
- **Qué es:** combina piezas que ya existían:
  - el brief y la rúbrica de formato;
  - la referencia R4 de formato (60 s de un narrador galego nativo tomados de una grabación pública, solo para uso interno de evaluación);
  - la criba R0 de voz;
  - la prueba G0 del pipeline.
- **Coste:** ~0-10 € y ~15-20 h.
- **Criterio para pasar a la validación formal:**
  - alguna voz obtiene ≥ 4/5 en "durmiría con isto" y ninguna nota ≤ 2 en corrección galega;
  - la mujer del promotor, a ciegas, no la sitúa claramente por debajo de la referencia humana;
  - pasa G0: ≥ 90 % de las correcciones de pronunciación audibles y ≥ 8/10 pares é/ó distintos.
- **Es una preselección, no una puerta de publicación:** las referencias son textos distintos, así que no permite calcular Δ.
- **[INT, tribunal final, 2.ª ronda] Entre la V-0 y la excepción va la Puerta F** (§1.3): sin un compromiso de terceros que pague la calidad de la E1, no se gasta la validación, porque publicar sin esa calidad no es una opción y pagarla el promotor no se recupera en ningún camino.

```
Semana 0-1: correo a Proxecto Nós/Gradiant (permiso de uso comercial + contacto con los locutores)
            + B0 (cómputo) + kit_voz.py + R0
Semanas 2-4: G0 (50 palabras de riesgo + A/B de ritmo del §3.3) + V-0 (promotor y mujer, a ciegas)
│
├─ V-0 NO: ninguna voz está en la liga → no se gastan 850-1.500 €.
│     Opciones (D2): (a) ESPERAR y reevaluar cada trimestre con modelos nuevos;
│                    (b)/(c) voz humana licenciada ya (1.400-2.500 €), rompiendo el "< 50 €/mes"
│
└─ V-0 SÍ → Semana 5: PUERTA F (§1.3): ¿terceros comprometen ≥ el diferencial de calidad de la E1 (≈ 3.680 €)?
      ├─ NO → presupuesto de hobby (D6: ≤ 300 € en 6 meses), sin validación; reintento con la PL400A de 2027
      └─ SÍ → D1: excepción aprobada → H1 + H2 + revisor profesional (850-1.500 €)
      → R1 → R2 → R3 (5-6 semanas) → PASO 0 (¿pasan los controles?)
          ├─ Test inválido → se corrige y se repite (nunca activa el plan B)
          ├─ Pasa una voz de Nós → con DOBLE PERMISO escrito (USC + locutor) → voz del canal
          │     sin doble permiso → la mejor voz de pago que haya pasado la Puerta V, o esperar
          ├─ Pasa una de pago (ElevenLabs, Gemini, Azure) → voz del canal si cuesta < 25 €/mes
          └─ No pasa ninguna → (c) VÍA INTERMEDIA: fine-tune de StyleTTS2-GL con 30-60 min
                de H1 o H2 (opción T1 ya firmada), ~700-1.250 € hasta saber si funciona;
                si pasa la Puerta V-2, licencia T2 (300-600 € + 10-15 % de los ingresos).
                Si falla → (a) esperar o (b) locutor con licencia completa (1.000-2.500 €)
```

**Qué incluye la excepción:**
- **Narradores H1 y H2:** 300-500 € cada uno.
  - La horquilla va de la tarifa genérica española de audiolibro (185-250 € por ~3.700 palabras, Cronoshare [F-sec]) al precio de lista de una agencia con locutores galegos (500-830 € + IVA, locutortv.es [F-sec]).
  - **No hay tarifa gallega publicada:** se cierra con 3 presupuestos en la semana 1.
- **H3 opcional:** +300-500 €.
- **Revisor lingüístico profesional:** 250-500 €.
- **Variante mínima:** narradores con ~20 min (400-700 €), **sin recortar el revisor**.

**Ventaja de la vía (c) que la integración destaca.** El *fine-tune* sale de la voz de un narrador **contratado y con consentimiento firmado desde el principio**. Así resuelve a la vez la calidad y el problema de consentimiento de las voces de Nós (§4.5).

**Cuentas de (c) frente a (b)** [CALC sobre S]:
- **(c) y, si falla, (b):** coste esperado ≈ 2.060 €.
- **(b) directo:** ≈ 1.750 €.
- **La ventaja de (c) es otra:** compromete ~950 € en lugar de ~1.750 €, y en el 30-50 % de los casos cierra el problema con ~1.400 €.

### 4.5 Consentimiento y licencia de la voz (regla única del plan) [INT]

La pieza de voz exigía solo la confirmación escrita de la USC. La de mercado exigía además el consentimiento personal del locutor, porque la licencia del modelo no cubre el **derecho a la propia voz** (LO 1/1982, art. 7.6; el consentimiento es revocable, art. 2.2 [F]). **Se adopta la regla más exigente:**

1. **Voz de Nós:** hacen falta dos permisos escritos:
   - **(i)** el de la USC/Gradiant, como titulares de los datos. El silencio no cuenta.
   - **(ii)** el consentimiento firmado de la persona que prestó la voz. Brais es la voz de Gaspar González Somoza y Celtia la de Consuelo Díaz Isorna, según las fichas de los datasets [F].
   
   Oferta al locutor [S]: crédito, 100 € a la firma, 10 % de los ingresos netos, veto por tema y retirada con sustitución del catálogo en ≤ 30 días.
2. **Voz de proveedor** (Azure, Google, voces por defecto de ElevenLabs): el permiso es la licencia del servicio, que se archiva. **Solo se publica si esa voz también pasa la Puerta V.** [INT] La pieza de mercado la daba por "reserva que no bloquea el lanzamiento"; con el listón de la pieza de voz, sí puede bloquearlo.
3. **Voz licenciada (vías b y c):** contrato en tres tramos:
   - **T0:** referencia interna, sin entrenamiento, se borra a los 24 meses;
   - **T1:** opción de *fine-tune* solo para evaluación;
   - **T2:** licencia de publicación de 12-24 meses.
   
   Compatible con la cláusula PASAVE que defiende el sector.
4. **Nunca:** imitar a una persona concreta, recrear a alguien fallecido, clonar desde grabaciones públicas ni sintetizar la voz de un colaborador.
5. **Aviso hablado** en los primeros 30 s, que **dice de quién es la voz de base** y **qué revisión real tuvo el texto**. **[INT, tribunal final]** Se quita "revisárono persoas galegofalantes": ser galegofalante no es una cualificación, y en los episodios revisados por muestreo la frase prometía más de lo que había. La frase de revisión tiene dos formas, según el episodio (§4.7):
   - **revisión íntegra** (todos los episodios de la Etapa 1, y en la Etapa 2 cualquier episodio leído entero: por inspección normal o porque su muestra no pasó): *"O texto revisouno enteiro un corrector profesional de lingua galega."* **[INT, tribunal final, 2.ª ronda]** Solo se dice si hubo **corrección de mesa del 100 % del texto** antes del render (§4.7); la escucha con el texto en la mano no basta;
   - **revisión por muestreo** (inspección reducida de la Etapa 2, §4.7): *"Un corrector profesional de lingua galega revisa o texto por mostraxe."*
   
   Las dos variantes completas:
   - **variante Nós:** *"A voz que vas escoitar é sintética: está feita a partir da voz de [nome], que nos deu permiso para usala."* + la frase de revisión;
   - **variante de proveedor:** *"A voz que vas escoitar é sintética."* + la frase de revisión.
   
   Nombre y cualificación del revisor (y del historiador, cuando lo hubo) van en la descripción y en la página "Como facemos Serán".

### 4.6 Calidad episodio a episodio: el método de producción

- **"Mejor de N" con contexto:** 3-5 variantes por frase, elegidas con una puntuación automática (UTMOSv2/DNSMOS, confianza del ASR, prosodia) calibrada contra un nativo. Un humano dirige solo las frases dudosas: 15-35 min por episodio.
- **Pausas y entonación aprendidas de H1/H2:** se aplican si ganan a las pausas fijas en la comparación ciega.
- **Control automático:**
  - ASR galego por **párrafo**, nunca sobre el audio entero. Pasado de una vez, Whisper alucinó y dio un WER del 48-53 % sobre un audio correcto [P].
  - La hipótesis del ASR se normaliza con Cotovía.
  - Detector de artefactos y "mosaico de risco": 2-4 min con solo las palabras de riesgo, cortadas con los tiempos del propio TTS.
  - El ASR **no detecta el acento**: eso sigue siendo trabajo del oído.
- **Escucha de corrección firmada** por un revisor calibrado. **[INT, tribunal final]** El revisor profesional es el **revisor lingüístico cualificado (RLC)** del §4.7, y **escucha siempre con el texto en la mano**: revisa a la vez el audio y el texto de lo que escucha.
  - **Prueba de defectos sembrados:** 36 defectos por episodio de prueba. Para firmar un episodio en solitario hacen falta ≥ 90 % de acierto en los graves y ≥ 70 % en los leves; la prueba se repite cada trimestre.
  - **[INT, tribunal final, 2.ª ronda] Dos muestreos distintos, que no hay que confundir:**
    - **(1) Escucha del audio (puerta H3)**, del promotor o del revisor calibrado: en la **Etapa 1**, escucha completa de cada episodio; en la **Etapa 2**, **muestreo de aceptación del audio** de 40 bloques de 2 min (80 de los 120 min), c = 0, con ~0,5 bloques defectuosos esperados por episodio de 2 h si *p* ≤ 3 %. **No es cero, y el plan lo dice.**
    - **(2) Trabajo pagado del RLC sobre el texto** (§4.7): **corrección de mesa del 100 % del texto antes del render** en los 12 episodios de la Etapa 1; después, **escucha completa con el texto** en los episodios 1-6 (≈ 1,5-2,5 h por episodio, 9-15 h en total) y **muestra de 12 bloques de 2 min** con el texto en los episodios 7-12. En la Etapa 2, bajo inspección reducida, **muestra de 20 bloques de 2 min con el texto** (≈ 4.600 palabras); bajo inspección normal, mesa íntegra.
  - **Antes** (versión anterior), la escucha completa de los episodios 1-6 se daba por "incluida en la excepción de voz", cuyo revisor (250-500 €, §4.4) es para el panel de la Puerta V y no existe si la V-0 dice que no o si se va por la vía (b); y el texto solo recibía ~0,4 h de trabajo por episodio para ~8.400 palabras. **No era una revisión íntegra**, aunque el aviso la prometía. Ahora está presupuestada aparte (§5.4).
- **[INT] Horas.** El pipeline presupuestaba para la puerta H3 solo 0,8 h (mosaico + 10 min + 3 catas). La pieza de voz exige escucha completa. **Se adopta la escucha completa**, y las horas por episodio se recalculan en el §5.4.

### 4.7 Guion en galego: calidad y veracidad

- **Escritura directa en galego**, no traducida.
- **Cinturón lingüístico:** Hunspell-gl, LanguageTool-gl, lista negra de castellanismos y un LLM revisor distinto del redactor. CarvalhoChat_GEC entra cuando se conceda el acceso.
- **Lectura íntegra humana del guion, siempre**, repartida entre el promotor y su mujer. **Es un control de la casa, no una garantía cualificada:** la garantía la dan el RLC y el historiador (abajo).
- **Veracidad determinista:**
  - Cada afirmación lleva un **ancla** que propone el LLM. La cita exacta la **extrae una herramienta** (`extrae_cita.py`) de la instantánea de la fuente, con sus desplazamientos.
  - `verifica_citas.py` comprueba el hash, los desplazamientos y el texto exacto, y bloquea las citas inventadas.
  - Un **juez de otra familia** (Gemini frente a Claude) decide si la cita respalda la frase.
  - Revisión humana del **100 % de fechas, cifras, causas y atribuciones**, más una muestra del resto.
  - **Prototipo probado [P]:** 0 bloqueos falsos en 480 copias ruidosas; 145 de 145 falsificaciones bloqueadas o enviadas a revisión.
- **Guion muestra** (`guion-mostra-revolta-irmandina.md`, v5.1, ~770 palabras: la entrada completa y el comienzo del Acto I): todo dato concreto descansa en literatura académica, sobre todo Carlos Barros (USC). Lo que no tenía fuente académica se retiró.
  - **[INT, tribunal final]** La versión anterior (~1.180 palabras) **incumplía las densidades del §3.2**, aunque aquí se presentaba como conforme. La entrada tenía 3 fechas y 5-6 nombres propios; el Acto I, ~3,5 nombres nuevos por minuto, años completos y cifras largas.
  - La v5 se reescribió: abre con el lugar en calma, el derribo va como "final ya anticipado", Castilla queda en una frase, hay una sola fecha redondeada por bloque y como máximo 3 nombres nuevos en 60 s.
  - Lleva adjunta la **auditoría automática** (`auditoria/audita_densidade.py`): nombres por minuto, fechas y cifras por bloque y activación 1-5 por párrafo. **Pasa.**
  - Se mantienen las correcciones del crítico medievalista de la integración:
  - Pulgar deja de ser "o cronista" en 1467;
  - la Rocha Forte se reduce a lo que respaldan Barros y el Preito;
  - los asistentes a Melide se presentan como recuerdo de un testigo;
  - se añade el aviso de voz y se quita la CTA hablada.
- **Comparación ciega con el listón (G1):**
  - La prosa de muestra se compara, a igualdad de lengua, con la traducción al galego de la apertura de History at Night.
  - **Criterio unificado [INT]:** empatar o ganar en ≥ 3 de 5 criterios, sin ninguna nota ≤ 2 en lengua, y ≤ 1 error normativo por cada 1.000 palabras tras el control automático, contado por un nativo.
  - Sustituye al "2 de 4" de la pieza de mercado.
- **[INT, tribunal final] Garantía cualificada: dos roles pagados.** Antes, pasado el panel E2 de la P0, la garantía dependía de personas sin cualificación acreditada, y la revisión histórica ("como mínimo 1 de cada 4") no estaba en la caja.
  - **Revisor/a lingüístico/a cualificado/a (RLC).**
    - **Perfil [S]:** titulación en Filoloxía Galega o en Tradución e Interpretación con galego como lengua A, o ≥ 3 años de corrección profesional acreditada en galego (por ejemplo, socio/a de la AGPTI). Lo selecciona la prueba de defectos sembrados del §4.6.
    - **Qué revisa, siempre sobre el TEXTO** [INT, tribunal final, 2.ª ronda: endurecido]:
      - **Inspección normal (por defecto): corrección de mesa del 100 % del texto de cada episodio antes del render TTS** (≈ 8.400 palabras en 75 min; ≈ 13.800 en 2 h). Se aplica a **los 12 episodios de la Etapa 1**.
      - **Después, en la Etapa 1, escucha con el texto en la mano:** completa en los episodios 1-6 y en muestra de 12 bloques de 2 min en los 7-12. La escucha ya no sustituye a la mesa: comprueba lo que la voz hace con un texto ya corregido.
      - **Inspección reducida (solo en la Etapa 2):** muestra estratificada de 20 bloques de 2 min con el texto en la mano (≈ 4.600 palabras, ≈ 1/3). Los bloques los elige un script al azar dentro de cada acto, e incluyen siempre la entrada y el aviso. **Solo se pasa a la reducida tras 10 episodios seguidos "limpios" en inspección normal**: en la mesa del RLC aparecieron 0 errores graves y ≤ 1 error normativo por cada 1.000 palabras (medido sobre el texto que le llega, después del cinturón automático y de la lectura de la casa). Con los 12 de la Etapa 1 limpios, la Etapa 2 empieza en reducida; si no, empieza en normal.
      - **Vuelta a la normal:** si una muestra no pasa, ese episodio se lee entero en mesa antes de publicar y **se vuelve a la inspección normal** hasta encadenar otra vez 10 episodios limpios. También se vuelve si fallan 2 de las últimas 5 muestras. (Reglas de cambio al estilo de la ISO 2859-1; **la norma no se ha consultado** y los números son decisión de diseño [S].)
    - **Criterio de aceptación explícito:** 0 errores graves (castellanismo léxico o sintáctico, error de concordancia o de colocación del pronombre, topónimo no oficial, o cualquier error que se oiga y avergüence) y ≤ 1 error normativo por cada 1.000 palabras. Es el mismo listón que la G1.
    - **Qué garantiza la muestra y qué no** [CALC sobre S, Poisson]:
      - **Detecta un proceso que empeora:** con 4.600 palabras y el criterio de ≤ 1 por 1.000, un proceso que deja pasar 2 errores por 1.000 palabras aprueba la muestra solo en el ≈ 5 % de los casos, y uno de 3 por 1.000, en el ≈ 0,2 %. Pero uno que está justo en el límite (1 por 1.000) aprueba solo la mitad de las veces: por eso la probabilidad de lectura íntegra (10 % [S], §5.4) es optimista si el proceso va justo.
      - **No corrige los 2/3 que no se leen.** Con el proceso en el límite, la parte no leída de un episodio de 2 h (≈ 9.200 palabras) puede llevar hasta ~9 errores normativos leves. Para los graves, 10 episodios limpios (≈ 84.000 palabras sin ningún grave) acotan su tasa por debajo de ≈ 0,036 por 1.000 palabras (regla del tres, 95 %), es decir, ≤ 0,33 graves esperados en la parte no leída de cada episodio. **No es cero, y por eso el aviso dice "por mostraxe" en esos episodios** (§4.5).
      - **Antes** (versión anterior), los episodios 7-12 de la Etapa 1 pasaban solo con una muestra de 1/3 y sin racha previa demostrada: la tolerancia no tenía justificación.
    - **Tarifa [S]:** 20-35 €/h de escucha con texto, y 0,015-0,025 €/palabra en lectura de mesa. Anclas: la corrección en galego se anuncia "desde 0,010 €/palabra" (ortográfica) más "desde 0,004-0,006 €/palabra" (estilo), por "corrector titulado en traducción o lingüista" [F-sec, https://shoptexto.com/correccion-ortografica-y-de-estilo-en-gallego/, precios "desde"], y la corrección en castellano sale a 0,015-0,03 €/palabra [F-sec, §4.4]. Se cierra con 3 presupuestos en la semana 1.
  - **Revisor/a histórico/a cualificado/a (RHC).**
    - **Perfil [S]:** doctorado o docencia universitaria en historia (medieval o moderna, según el tema), o investigación publicada sobre el tema del episodio.
    - **Qué revisa: el 100 % de las afirmaciones de hecho de la "folla de afirmacións"** (fechas, cifras, causas, atribuciones y nombres), cada una con su cita extraída por la herramienta.
    - **Regla de qué episodios lo exigen:**
      - (a) **todos los de la Etapa 1**;
      - (b) en la Etapa 2, todo episodio de **tema de riesgo**: revuelta o conflicto armado; Iglesia e instituciones eclesiásticas; orígenes e identidad (castros, suevos, Santiago); personas reales identificables; debate historiográfico abierto;
      - (c) el primer episodio de cada serie;
      - (d) todo episodio en el que el juez de otra familia marque ≥ 3 afirmaciones como "no respaldadas".
      - Los demás episodios de la Etapa 2 (vida cotidiana, oficios o paisaje dentro de una serie ya revisada) salen con la verificación determinista y la revisión humana del 100 % de fechas, cifras, causas y atribuciones. El RHC **audita 1 de cada 4 después de publicar**, con corrección en < 72 h. Se estima que el RHC revisa antes de publicar ≈ 60 % de los episodios de la Etapa 2 [S].
    - **Tarifa [S]:** 50-150 € por episodio (pieza de mercado; no hay tarifa de referencia). Se cierra con 3 presupuestos. En la Etapa 2 puede ser el asesor de la USC de la serie "Gallaecia".
  - **Coste (cálculo en el §5.4):** ≈ 305 € por episodio en la Etapa 1 (200-420 €; antes, ≈ 130 €, sin la mesa íntegra) y ≈ 120 € en la Etapa 2 con inspección reducida (≈ 335 € por episodio mientras dure la normal: mesa íntegra de 207-345 € más el historiador). **No cabe en los límites del promotor. El plan no rebaja la garantía: la pagan terceros (Puertas F y F2) o no se publica (D5, §0.2).**

---

## 5. Pipeline de producción y costes

Pieza "pipeline" del gauntlet: se paró en 5 rondas por presupuesto. Su carencia de ritmo se resuelve en el §3.3, y la de evidencia del benchmark se corrige en el §5.3.

### 5.1 Principios y arquitectura

- **Principios:**
  - galego primero;
  - determinista donde se pueda, LLM donde haga falta;
  - el agente que redacta no es el que revisa;
  - todo es un fichero en git (expediente por episodio);
  - barato por defecto;
  - **nada se publica solo.** La subida por API desde proyectos sin verificar queda en privado [F], así que en la Etapa 1 la subida es manual.
- **Diez agentes y cuatro puertas humanas:**
  - **Agentes:** investigador → `extrae_cita.py` → escaleta → **[H1: el humano aprueba la escaleta]** → guionista (capítulo a capítulo, en galego) → lingüista galego → verificador (determinista + juez de otra familia) → auditor QA de texto → **[H2: revisión estratificada de afirmaciones + lectura íntegra + firma]** → director visual → imágenes → TTS y posproducción → auditor QA de audio e imagen → **[H3: escucha de corrección firmada (§4.6) + hoja de contacto]** → montaje FFmpeg → publicación.
  - **[H4]** El humano sube, marca la declaración de contenido sintético y publica.
- **Bucle del auditor QA:** como máximo 3 vueltas automáticas por etapa; a la cuarta, escala al humano. Umbrales principales:
  - castellanismos = 0;
  - citas inventadas = 0;
  - WER ≤ 6 % por párrafo;
  - −16 LUFS ±1;
  - luminancia de 40-70;
  - ritmo por acto según el §3.3.
- **Qué es siempre humano:** tema y ángulo, aprobación de la escaleta, lectura íntegra, decisión sobre las afirmaciones dudosas, publicación, respuesta a comentarios y firma editorial (AI Act, art. 50).

### 5.2 Stack por etapa

| Pieza | Etapa 1 | Etapa 2 | Etapa 3 |
|---|---|---|---|
| Orquestación | **Claude Code** (plan Pro, 20 USD/mes [F]) con subagentes y `pipeline.py`/`Makefile`; estado en ficheros | LangGraph o Claude Agent SDK con API, desatendido por la noche | Más ramas de localización |
| LLM | Dentro de la suscripción. Si no cabe, la API cuesta ≈ 3,5 USD por episodio de 75 min | API optimizada (*caching* + *batch*): ≈ 3 USD por episodio de 2 h | Ídem |
| Corpus y RAG | RAG "de carpeta" (Galipedia con `revid`, Wikidata, PDFs de Galiciana/Minerva/RUC) + SQLite FTS5 | Índice vectorial local | — |
| Voz | La ganadora de la Puerta V. Por defecto, Nós **en la CPU local** (cola `jobs/`, `voz_worker.py`); Runpod por horas como plan B, con el mismo código. **Colab queda descartado como *worker*:** su FAQ lo prohíbe en la versión gratuita [F] | CPU nocturna o GPU por horas (RTX 4090 a 0,34 USD/h) | Voz licenciada |
| ASR | `whisper-large-v3-turbo-gl` (Nós) en int8, por párrafo | Ídem | Ídem |
| Imágenes | **Nano Banana 2 Lite** en *batch* (0,0168 USD por imagen [F]). **[INT] Si se usa FLUX en Runpod, solo FLUX.1 [schnell] (Apache-2.0); nunca FLUX.1 [dev], que no permite uso comercial** (§7.4). Imagen 4 Fast se apagó el 17-08-2026 [F] | Nano Banana 2, *batch* (0,034 USD) | — |
| Montaje | FFmpeg (Ken Burns ≤ 3 %, `xfade`, `loudnorm`) | Ídem | Ídem |
| Publicación | Manual por Studio | API (`videos.insert` con `containsSyntheticMedia`) tras la auditoría; la publicación final siempre la pulsa un humano | — |

### 5.3 Medida propia en CPU [P, 29-09-2026] y corrección de evidencia

**Condiciones:** 4 vCPU Xeon sin GPU, voz Brais de Nós, guion muestra (1.263 palabras, 72 frases), `LFinference` sin parchear.

- **Arranque en frío:** 27,6 s. **RAM:** 3,65 GB para el TTS y 1,67 GB para el ASR.
- **Velocidad natural de Brais: 191,5 palabras/min de habla pura.** Sale de 395,2 s de audio para 1.263 palabras (`per_sent.json`) y lo confirma `bench_tts_2.json` (193,1 con 314 palabras). Es el dato que obliga a la tabla de ritmo del §3.3.
- **RTF del TTS.** **[INT, corrección]** La pieza citaba "RTF 0,28 con 4 hilos: 395,8 s de audio en 110,6 s", pero `bench_tts_4.json` solo contiene **una frase de 24 palabras** (6,2 s de audio, RTF 0,286). Así que:
  - el **0,28 está medido sobre una sola frase**;
  - la medida robusta es **RTF 0,38 con 2 hilos sobre 314 palabras** (`bench_tts_2.json`);
  - las proyecciones de tiempo de máquina usan 0,28-0,38, y la prueba B0 en el equipo del promotor da el dato real.
- **ASR:**
  - frase a frase, RTF 0,75 y WER mediana del 0 %;
  - sobre el audio entero, **alucina** (WER del 48-53 %);
  - de las 15 frases por encima del 6 %, 6 son solo números y 2-3 son fallos reales del TTS (un tartamudeo).
- **Proyección para un episodio de 75 min en CPU:** ~15-23 min de TTS + 34-40 min de ASR ≈ **50-65 min desatendidos**.
- **Regla de B0 (semana 1):** se queda la CPU local si RTF_TTS ≤ 0,6, RTF_ASR ≤ 1,5 y hay ≥ 8 GB de RAM libres; si no, Runpod (+3 h de montaje, ~0,6-0,8 USD por episodio).

### 5.4 Costes y horas

**Coste variable por episodio** [S sobre precios F]:

| Etapa | Stack mínimo | Stack típico | Stack "premium" |
|---|---|---|---|
| Etapa 1 (75 min) | ≈ 0,2 USD | ≈ 1,9 USD (CPU) / 2,5-2,7 USD (Runpod) | ≈ 11 USD (ElevenLabs + API) |
| Etapa 2 (2 h) | — | ≈ 9,5 USD (Nós) · 11-12,5 USD (Gemini-TTS) | ≈ 16,1 USD (ElevenLabs) |

**Incluso el stack más caro se queda por debajo de 10 USD por hora narrada.** Una hora de revisión humana a 15 €/h ya cuesta más que toda la IA de un episodio.

**Caja mensual** (cuadrada con el §1; **[INT, tribunal final]** con la garantía cualificada del §4.7):

| Partida (€/mes) | Etapa 1 (2 episodios de 75 min) | Etapa 2 (4 episodios de 2 h) |
|---|---|---|
| Claude Pro | 14,8-17,4 | 14,8-17,4 |
| GPU en Runpod (solo si B0 descarta la CPU) | 0-1,4 | 0-3 |
| IA variable | ~3,3 | ~33-56 |
| Música con licencia | 0 | 0-15,6 |
| **Subtotal del stack** | **≈ 18-24** (el modelo usa 35 € para imprevistos) | **≈ 48-92, central ≈ 70** |
| **RLC: revisión lingüística cualificada del texto** (§4.7) | **[INT, tribunal final, 2.ª ronda]** **Mesa íntegra antes del render, ep. 1-12:** 12 × ≈ 8.400 palabras × 0,015-0,025 €/palabra = 12 × 126-210 € → **1.510-2.520 €**. **Escucha con texto, ep. 1-6:** 9-15 h × 20-35 €/h → **180-525 €** (central 12 h × 27,5 € = 330 €). **Muestra de audio con texto, ep. 7-12:** 6 × 16-28 € → **96-168 €**. **Total de la E1: ≈ 1.790-3.210 € (central ≈ 2.480 €)**; antes, 260-445 €, porque la escucha de los ep. 1-6 se cargaba a la excepción de voz y no había mesa | **Inspección reducida** (tras 10 episodios limpios, §4.7): muestra de 24-42 € + 10 % [S] de lectura íntegra (207-345 €) → 45-77 € por episodio → **≈ 180-306 €/mes (central ≈ 242 €)**. En inspección normal, 4 × 207-345 € ≈ 830-1.380 €/mes. Sustituye a los 64-112 € del revisor solo de escucha |
| **RHC: revisión histórica de la hoja de afirmaciones** | 12 × 50-150 € → **≈ 600-1.800 € (central ≈ 1.200 €)** | 4 × 60 % × 50-150 € → **≈ 120-360 €/mes (central ≈ 240 €)** |
| **Total** | **Stack + ≈ 2.390-5.010 € de calidad en 12 episodios** (≈ 200-420 € por episodio, central ≈ 305 €; RLC ≈ 2.480 € + RHC ≈ 1.200 €) → **≈ 500-1.030 €/mes en los 5 meses de la Etapa 1 (ene-may, M2-M6, como en el §1.1), central ≈ 770 €** (modelo: 35 €). Los episodios 1-3 se producen en diciembre (M1), así que parte del pago cae ese mes; repartido en los 6 meses de producción (dic-may), serían ≈ 650 €/mes. **Con la Puerta F lo pagan terceros** | **≈ 350-760 €/mes, central ≈ 550 €** (modelo: 110 €; antes, 138 €) |
| Límite del promotor | < 50 € **✘: se rompe** si lo paga el promotor; **✔ con la Puerta F** (le quedan ≈ 35 €) | 50-200 € **✘: se rompe** si lo paga el promotor; **✔ con la Puerta F2** (le quedan ≈ 110 €) |

**Decisión (D5, §0.2).** La garantía no se rebaja; se financia con terceros o no se publica:
- **Etapa 1: la paga la Puerta F** y se mantienen los 12 vídeos, porque la P1 no mide nada con menos (§8.3). Coste extra: ≈ 3.680 € (2.390-5.010).
- **Etapa 2: no se abre por defecto.** Con 4 episodios al mes cuesta ≈ 550 €/mes, y el camino optimista ingresa 509 €/mes en M36: si la paga el promotor, no hay equilibrio en 36 meses (§1.3). Solo se abre con la **Puerta F2** (≥ 440 €/mes de terceros).
  - Con 3 episodios al mes, ≈ 410 €/mes, pero hay que recalibrar la P2.
  - Con 2 al mes, ≈ 280 €/mes, y los ingresos del optimista caen a la mitad (3.490 € frente a 6.865 € acumulados en el modelo).
  - Ninguna cadencia cabe en 200 €/mes con la garantía. Con 1 episodio al mes (≈ 150 €/mes) la Etapa 2 es, en la práctica, el mantenimiento.
- **Qué podría bajar el coste sin rebajar la garantía [S]:** bibliografías de serie ya revisadas, que reducen la parte de episodios con RHC. No entran en las cifras hasta tener datos. **La inspección reducida ya está en las cifras de la Etapa 2** y solo se gana tras 10 episodios limpios en mesa íntegra (§4.7): si la Etapa 1 no deja esa racha, la Etapa 2 empieza en inspección normal y el RLC cuesta ≈ 830-1.380 €/mes en lugar de ≈ 180-306 €/mes.

**Horas humanas por episodio [INT]:**

| Tarea | Etapa 1 (75 min) | Etapa 2 (2 h) |
|---|---|---|
| Brief, fuentes, escaleta (H1) | 0,8 h | 0,5 h |
| Revisión estratificada de afirmaciones y bloqueos | 0,7-0,9 h | 1,0-1,4 h |
| **Lectura íntegra del guion (H2)** (promotor + mujer) | 2,2-2,5 h | 3,5-4 h |
| Incidencias | 0,3 h | 0,4 h |
| **Escucha de corrección completa + pase de dirección + mosaico y hoja de contacto (H3)** | **1,65-2,6 h** (sustituye a los 0,8 h del pipeline, §4.6) | Muestreo: ~1,0-1,5 h [S] |
| Supervisión y sesiones de cómputo | 0,6-1,2 h | 0,4-0,55 h |
| Publicación (H4) | 0,4 h | 0,3 h |
| **Total por episodio** | **≈ 6,7-8,7 h** (los 3 primeros, el doble) | ≈ 7,1-8,8 h |

- **Etapa 1:** 2 episodios al mes + ~1 h/semana de comunidad = **~18-22 h al mes, ≈ 4,1-5,0 h/semana**. Supera las 4 h/semana del promotor: se pide aceptar ~5 h (decisión D3). El orden de recorte de la comunidad (§6.5) es la salvaguarda.
- **Etapa 2:** con 4 episodios al mes (lo que usa el modelo) salen ~28-35 h + ~9 h de comunidad ≈ **37-44 h/mes, 8,5-10 h/semana**, en el límite alto. **[INT]** El modelo de retornos usa 35 h/mes (A15-17). El árbol conjunto del §1.3 suma la diferencia (+5,5 h/mes en el centro). **Con 3 al mes hay holgura.** Si solo caben 3, el calendario de la P2 se alarga ~2 meses.
- **Construcción inicial:**
  - MVP de **32,5-35,5 h** [S] y G0/G1 (~6-8 h);
  - después, 12-20 h de controles aplazados (similitud, CLIP, ECAPA…), entre los episodios 2 y 6, **siempre antes de pedir el YPP**.

### 5.5 Controles anti-"slop" (contenido inauténtico)

La política de YouTube, aclarada el 16-07-2026, deja sin monetizar el contenido "hecho con plantillas, con poca variación entre vídeos" [F]. Controles, cada uno con evidencia en el expediente del episodio:
1. Investigación propia con bibliografía en la descripción (≥ 8 fuentes por episodio).
2. Ángulo único declarado.
3. Control de similitud entre guiones (coseno < 0,85; < 2 % de 8-gramas compartidos).
4. Aperturas distintas en cada episodio.
5. Series con arco propio.
6. Voz editorial humana (lectura íntegra y erratas públicas).
7. Imágenes nuevas por plano (≤ 10 % reutilizadas).
8. Cadencia moderada (2-4 al mes, **nunca diaria**).
9. Sin bucles ni recopilaciones sin narración nueva.
10. Nota de proceso y declaración de contenido sintético.
11. Crédito y licencia de la voz.
12. Expediente de evidencias para una apelación y para la excepción del art. 50.

---

## 6. Go-to-market y marca

Pieza "mercado, marca, lanzamiento" del gauntlet: se paró en 5 rondas. Sus correcciones finales se aplican aquí y en el §8.

### 6.1 Principios

1. **Calidad antes que alcance:** solo se promociona lo que pasó la Puerta 0.
2. **Promoción en temporada y producción constante:** 5-6 fechas gallegas al año.
3. **Sin publicidad pagada en la Etapa 1.**
4. **Hábito antes que alcance.**
5. **Audio en todas partes:** YouTube, Spotify for Creators (el SPP llega a España el 20-10-2026 [F]), iVoox y Apple.

### 6.2 Lanzamiento en tres fases (calendario integrado)

| Fase | Cuándo | Qué | Criterio para pasar |
|---|---|---|---|
| **0. Silenciosa** | Oct 2026 - mediados de ene 2027 | Voz (Puerta V-0 y Puerta V), guion (G1), permisos, **3 episodios terminados antes de publicar**; panel privado E2 (10-15 nativos, 1 filólogo, 1 historiador) | Puerta 0 (§8.2) |
| **1. Suave** | 17-01-2027 a marzo de 2027 (M2-M4) | Episodios 1-3 juntos y después **cada dos domingos a las 21:30, con estrea**. Difusión en el entorno del panel, en 2-3 entidades de la diáspora y en 1-2 servicios de normalización. Desde el día 1: "Carta do serán", Telegram, Bluesky, mastodon.gal, Podgalego y Obradoiro Dixital Galego. Sin prensa | Lectura temprana en M4 (vídeos 1-4) |
| **2. Pública** | Marzo - mayo de 2027 (M4-M6) | Nota de prensa ("primeira canle de historia para durmir en galego"), propuesta a Radio Galega, correos a la diáspora y a mediadores, colaboraciones con divulgadores. **Especiales:** Día Mundial do Sono, que en 2027 cae el **viernes 19-03** (viernes anterior al equinoccio de marzo, que es el sábado 20-03 [F]); el episodio especial se publica el **domingo anterior, 14-03**, y la nota de prensa sale esa semana. Y **Letras Galegas 2027, dedicadas a Xosé Neira Vilas: episodio el domingo 16-05**, víspera del Día das Letras (lunes 17-05) [F RAG]. Es la única excepción a la cadencia quincenal (§1.2) | Puerta 1 (31-05-2027) |

- **Samaín 2026 no:** el pipeline no está listo. Samaín 2027 será el primer gran episodio de temporada.
- **Youtubeiras+ 2026 no:** exige 3 piezas antes del 15-11-2026. Se va a **Youtubeiras+ 2027** (Revelación y Pódcast) con catálogo; es condición de la P2.

### 6.3 Llegar a cada segmento

- **A. Núcleo:**
  - título con la etiqueta fija "HISTORIA PARA DURMIR";
  - SEO en galego con una línea bilingüe. **El 61 % de quienes siempre hablan galego escribe en castellano** [F IGE];
  - radio y prensa en galego después de 3-4 episodios buenos;
  - asociaciones y clubes de lectura.
- **B. Quienes aprenden:** subtítulo manual exacto en galego en todos los episodios; profesorado de adultos y EOI.
- **C. Diáspora:**
  - **Rexistro da Galeguidade:** 202 entidades, 201 con correo público [COMP, datos abiertos de la Xunta];
  - correos personales por oleadas de 20-30, con la propuesta de un "serán compartido".
- **D. Mediadores:**
  - bibliotecas y servicios de normalización (organizan Youtubeiras+) y equipos de dinamización;
  - capítulos sueltos para el aula, nunca el producto para dormir dirigido a menores;
  - **A Mesa solo después** de tener la voz con consentimiento documentado y un historial de calidad.

### 6.4 Descubrimiento: SEO y "adyacencia"

- **Reglas de SEO:**
  - título siempre en galego;
  - línea final bilingüe que declara el idioma del audio;
  - idioma del vídeo = galego;
  - subtítulos exactos;
  - palabras clave gallegas;
  - listas por serie;
  - web mínima seran.gal con fuentes y erratas.
- **Adyacencia:** colocarse **junto a** los vídeos que hoy captan la demanda de "Galicia para dormir" en castellano, que llegan como sugeridos.
  - **Vídeos semilla:** S1 "DUÉRMETE CON las Leyendas… de GALICIA" (107.810 vistas), S6 "El Reino Suevo de Gallaecia" (165.297), S7 Burla Negra (23.763), S8 "¿Cómo era un día completo en la Edad Media?" (1,05 M), entre otros.
  - **Episodios espejo:** 1 de cada 3 en la Etapa 1, con las palabras que se escriben igual en las dos lenguas al principio del título. **Nunca se copian miniaturas ni nombres.**
  - **Test & Compare:** no exige el YPP, basta con activar las funciones avanzadas [F]; **no sirve para vídeos publicados como estrea** [F].

### 6.5 Comunidad y hábito: "o serán" como ritual

- **Día y hora fijos:** domingo a las 21:30 (hora de Galicia).
- **Estrea "co lume aceso":** el promotor está en el chat, con su nombre, los primeros 15 min.
- **Fórmulas fijas en el audio:** "Boas noites. Isto é Serán…". Dedicatorias solo con permiso escrito.
- **Ritual de la mañana:** comentario fijado *"Bos días. Ata onde chegaches onte á noite?"*
- **"Propón un serán":** votación trimestral y cierre del bucle con *"Pedíchelo, e aquí está"*. **[INT, corrección lingüística:** la forma normativa de la 2.ª persona del pretérito es *pediches*, y con el pronombre *pedíchelo*; la pieza decía "Pedístelo".]
- **"Normas do serán":** "Aquí ninguén corrixe o galego de ninguén". Respuesta humana en ≤ 48 h, nunca automatizada.
- **Carta do serán:** desde M2, con Buttondown o MailerLite en su versión gratuita.
- **Presencia en el ecosistema galegofalante:** es pequeño (la mayor cuenta "centro" de Bluesky en galego tiene < 3.000 seguidores; mastodon.gal, 1.414 cuentas [COMP]), así que **su valor es la reputación, no el volumen**.
- **Tiempo:** ≈ 1 h/semana en la Etapa 1, con un mínimo innegociable de 35 min: estrea, respuestas, publicaciones aprobadas y Telegram. Orden de recorte si falta tiempo: Reddit e intercambios → Bluesky y Mastodon → revisión de semillas.

### 6.6 Transparencia sobre la IA: de riesgo a ventaja

- **Marco:** *"a IA ao servizo do galego"*, en línea con el relato institucional del Proxecto Nós [F lingua.gal].
- **Seis compromisos públicos** (página "Como facemos Serán"):
  1. qué hace la IA y qué hacen las personas;
  2. fuentes publicadas;
  3. página de erratas;
  4. créditos completos de la voz, incluida la persona de base;
  5. ninguna voz sin consentimiento escrito;
  6. remuneración al locutor y voz licenciada en la Etapa 3.
- **Diálogo previo con ADA y AGPTI**, antes de publicar:
  - una carta y una llamada con el consentimiento del locutor en la mano y una oferta de crédito y remuneración;
  - **se pregunta, no se pide permiso.**
- **La IA no aparece en títulos ni miniaturas.** Lema interno: *"Feito con IA, coidado á man."*

---

## 7. Riesgos y cumplimiento

### 7.1 Riesgos principales

| # | Riesgo | Prob. / impacto [S] | Mitigación |
|---|---|---|---|
| R1 | **Ninguna voz pasa la Puerta V** | **Alta (60-80 %) / alto** | Puerta V-0 antes de gastar; vía intermedia (c); esperar con reevaluación trimestral |
| R2 | **Contenido inauténtico** (política de YouTube del 16-07-2026) | Media / alto | Los 12 controles del §5.5; expediente por episodio; si llega un aviso de "limited ads", se congela la producción y se apela |
| R3 | **Rechazo del sector cultural gallego a la voz IA** (ADA, AGPTI y A Mesa sobre RTVE, febrero de 2026; críticas a la CSAG por recrear a Begoña Caamaño, mayo de 2026 [F]) | Media / medio-alto | Doble permiso, aviso que nombra la voz de base, diálogo previo, voz licenciada en la Etapa 3 |
| R4 | **Voz de un profesional gallego usada sin su consentimiento comercial** | Baja con la regla / muy alto si ocurre | Doble permiso como condición de la Puerta 0 (§4.5) |
| R5 | **Errores de lengua o de historia publicados** | Media / alto | Cinturón lingüístico; **RLC cualificado sobre el texto** (corrección de mesa íntegra en toda la Etapa 1 y en inspección normal; muestra con criterio de aceptación solo tras 10 episodios limpios); citas extraídas por herramienta; **RHC sobre el 100 % de las afirmaciones** en la Etapa 1 y en los temas de riesgo (§4.7); corrección pública en < 72 h |
| R6 | **Demanda insuficiente** (3,59 % de consumo audiovisual en galego) | Alta / alto | La P1 lo mide pronto; salida hacia un modelo audio-primero o hacia la Etapa 3 |
| R7 | **Anuncios que despiertan al oyente** [F SBS] | **[INT] Existe ya antes del YPP**: YouTube puede monetizar vídeos de canales fuera del programa (Términos de servicio, "derecho a monetizar") | Sin promesa de "sen cortes" en la Etapa 1 (§3.5, regla 13); cola de ambiente de colchón; se vigila si aparecen anuncios en los vídeos propios |
| R8 | **Tiempo del promotor** (la Etapa 1 real pide ~5 h/semana) | Media-alta / alto | D3; orden de recorte; el pipeline absorbe la producción |
| R9 | **Cambios de plataforma** (8.000 h para el YPP desde febrero de 2027; precios de Gemini que se duplican en 2027; modelos retirados) | Cierta / medio-bajo | Ya está en el modelo; adaptadores por proveedor; `versions.lock` |
| R10 | **Técnicos:** StyleTTS2 inestable en tiradas largas; el contraste é/ó no llega al audio; Cotovía de otra versión; Whisper que alucina | Media | G0 de 50 palabras; Cotovía fijado por hash con canario; ASR por párrafo; voz de reserva |
| R11 | **Dependencia de una plataforma** | Media / alto | RSS propio, web y Carta desde M2 |
| R12 | **Politización y guerra normativa** | Media / medio | Tono descriptivo; temas excluidos; norma RAG declarada sin polémica; normas de comentarios |

### 7.2 Etiqueta de contenido sintético de YouTube
Es obligatoria para el contenido **realista**. Declarar no reduce ni el alcance ni la monetización; no hacerlo puede llevar a la retirada del contenido [F]. **Decisión:** estilo pictórico y **etiqueta activada siempre**, porque la voz es sintética y no cuesta nada.

### 7.3 AI Act, artículo 50
- **Vigencia:** se aplica **desde el 2-08-2026**. El Digital Omnibus no lo aplazó [F]; solo retrasó hasta el 2-12-2026 el marcado legible por máquina de los *proveedores*.
- **Nuestro papel:** somos **responsables del despliegue** [S].
  - **Texto de interés público:** está exento si hay revisión humana y responsabilidad editorial. El promotor firma como responsable y aun así se declara.
  - **Voz que se parece a una persona existente:** se trata como *deepfake* por prudencia.
- **Cómo se cumple:** **aviso hablado en los primeros 30 s** + etiqueta de YouTube + nota en la descripción. Se toma como referencia el Código de Práctica de la UE (10-06-2026), que prevé avisos hablados para el audio [F].
- **Sanciones:** para las pymes se aplica la menor de las dos cifras (art. 99.6) [F].
- **España:** el proyecto de ley orgánica de IA está en tramitación. Se revisa cada trimestre.

### 7.4 Derechos de autor y licencias

| Material | Regla |
|---|---|
| Hechos históricos | Libres. El guion es una expresión original en galego |
| Galipedia (CC BY-SA 4.0) | Esqueleto factual; se parafrasea y se contrasta con fuentes académicas |
| Consello da Cultura Galega | **Solo para verificar**: su licencia es no comercial y sin obra derivada |
| Clásicos de dominio público (Murguía, López Ferreiro, Vicetto) | Ambiente y relato. **Su historiografía está superada** |
| Autores protegidos (Neira Vilas, hasta el 31-12-2085) | Solo contexto histórico propio; no se leen ni se adaptan sus textos |
| Imágenes IA | Probablemente no protegibles (TRLPI art. 5). La marca se protege con el nombre, el estilo y el sello sonoro |
| **Generador de imágenes** | **FLUX.1 [dev] no permite uso comercial** [F]. Se usa la API de Gemini (Nano Banana), FLUX.1 [schnell] o una licencia comercial |
| Música y ambiente | Grabación propia o licencia documentada; 0 reclamaciones de Content ID en los 6 primeros episodios |
| **Voz de Nós** | **Modelo:** Apache-2.0. **Dataset:** CC-BY-4.0 declarado, restringido a investigación y con la "public exposure" de las grabaciones prohibida. **Voz de la persona:** LO 1/1982. Hace falta el doble permiso (§4.5) |
| Voz de proveedor | Se archivan los términos vigentes |
| Spotify | Prohíbe los pódcast IA que suplantan a una persona [F]. Aquí no se suplanta a nadie |
| Marca "Serán" | Búsqueda en OEPM y EUIPO en el mes 1; registro en la clase 41 tras la P1 |

### 7.5 Lista de cumplimiento previa al primer episodio
- [ ] Voz con la Puerta V superada y cadena de consentimiento documentada (doble permiso si es de Nós; términos archivados si es de proveedor; contrato T0-T2 si es licenciada).
- [ ] Aviso hablado en los primeros 30 s que dice de quién es la voz de base y qué revisión tuvo el texto (íntegra o por muestreo, §4.5).
- [ ] RLC y RHC contratados, con la cualificación acreditada archivada y el criterio de aceptación por escrito (§4.7).
- [ ] Carta a ADA y AGPTI enviada y su respuesta registrada.
- [ ] Voz de reserva validada, para poder sustituir la principal en ≤ 30 días.
- [ ] Generador de imágenes con licencia comercial (sin FLUX.1 [dev]).
- [ ] Paisaje sonoro propio o con licencia.
- [ ] Búsqueda de la marca en OEPM y EUIPO.
- [ ] Página "Como facemos Serán" y página de erratas.
- [ ] Etiqueta de contenido sintético activada.
- [ ] Canal configurado como "non dirixido a nenos".
- [ ] Ninguna afirmación de salud.
- [ ] **Ningún "sen cortes" en títulos ni miniaturas** (Etapa 1).
- [ ] Expediente del episodio completo con la firma editorial.
- [ ] Normas de comentarios publicadas y moderación configurada.
- [ ] Carta con doble confirmación y aviso de privacidad (RGPD).

---

## 8. Plan de pruebas por etapas: KPIs y puertas

### 8.1 Cadencia única

| Tramo | Fechas | Cadencia | Vídeos acumulados |
|---|---|---|---|
| Construcción y validación | Oct 2026 - mediados de ene 2027 | 0 publicados; 3 terminados | 0 |
| M2 | Ene 2027 | Lanzamiento con 3 (17-01) + 1 (31-01) | 4 |
| M3-M6 | Feb - may 2027 | Quincenal, en domingo: 14-02, 28-02, 14-03, 28-03, 11-04, 25-04, 09-05 y **16-05**. Especiales: el 14-03 (domingo anterior al Día Mundial do Sono, viernes 19-03) y el 16-05 (Letras; **única excepción a la cadencia**: adelantado una semana, del 23-05 al 16-05) | 6 · 8 · 10 · **12 → P1 (31-05)** |
| M7-M12 (Etapa 2) | Jun - nov 2027 | Semanal (26 semanas con 2 de descanso) | **36 → P2 (30-11)** |
| M13-M18 | Dic 2027 - may 2028 | Semanal | **60 → P3 (31-05-2028)** |
| Mantenimiento | Desde jun 2028 | 1 al mes | 78 en M36 |

### 8.2 Tabla única de puertas

| Puerta | Cuándo | GO si se cumple todo | NO-GO → qué se hace |
|---|---|---|---|
| **B0 (cómputo)** | Semana 1 | En el equipo del promotor: RTF_TTS ≤ 0,6, RTF_ASR ≤ 1,5 y ≥ 8 GB de RAM libres | Runpod por horas (+3 h de montaje) |
| **G0 (pronunciación y ritmo)** | Semanas 2-4 | ≥ 90 % de los ítems corregidos se oyen bien (los dos jueces); ≥ 8/10 pares é/ó audibles; 0 regresiones; una variante de ritmo del §3.3 sin "vocales arrastradas"; regenerar el párrafo 5 deja idénticos los párrafos 6-10 | Siguiente voz del kit. Si el contraste é/ó no llega al audio, es un límite del modelo |
| **V-0 (preselección de voz)** [INT] | Semanas 3-4 | §4.4 | **No se gasta la excepción.** D2: esperar o voz licenciada |
| **F (financiación de la calidad)** [INT, tribunal final, 2.ª ronda] | Semana 5 (29-10 a 04-11-2026), solo si V-0 = sí | Compromisos firmes y por escrito de terceros (concello vía PL400A, mecenas o preventa, patrocinio, convenio con Nós/USC o AGPTI) **≥ el diferencial de calidad de la E1 (≈ 3.680 €)**, condicionados a que haya voz. Meta: ≈ 5.140 €, para que parar en la P1 no le cueste nada al promotor (§1.3) | **No se gasta la excepción ni se publica.** Presupuesto de hobby (D6: ≤ 300 € en 6 meses); reintento con la PL400A de 2027; si falla dos veces, cierre |
| **Puerta V (V-1 + V-2)** | Semanas 6-12 | §4.3: control positivo y negativo válidos; Δ ≤ U; exactitud equilibrada ≤ 0,60; < 20 % "non é galego" | (c) → (a) o (b), en el orden decidido en D2. **Nunca se publica con la "menos mala"** |
| **G1 (guion)** | Semanas 4-8 | ≥ 3/5 criterios frente al listón, ninguna nota ≤ 2 en lengua, ≤ 1 error normativo por 1.000 palabras | Otro redactor o reescritura del lingüista |
| **G2 (veracidad)** | Semanas 6-10 | 0 anclas falsas plantadas aceptadas; el juez detecta ≥ 4/5 respaldos falsos; ≤ 2 % de bloqueos falsos; canarios activos | Se corrige el verificador |
| **G3 (máster)** | Semanas 10-12 | 20 min de máster sin fallos de "sono seguro"; la mujer del promotor lo aguanta sin quejas de lengua | Se corrige y se repite |
| **P0 (publicable)** | ~10-01-2027 | 3 episodios terminados; voz con la Puerta V superada y doble permiso o licencia; **panel E2 superado** (≥ 70 % "volvería a escoitalo", filólogo con 0 errores graves, historiador con 0 errores de hecho, ≤ 20 % molestos por la IA); prueba de defectos sembrados superada; lista de cumplimiento (§7.5) | Como mucho 2 iteraciones de ≤ 4 semanas; si no, parar |
| **P1 (señal de mercado)** | 31-05-2027 · 12 vídeos | Vistas a 30 días ≥ 60; ≥ 20 suscriptores; AVD ≥ 20 min; E5 cumplido (≤ 1 error verificado por hora, corregido en < 72 h); **Puerta F2: ≥ 440 €/mes comprometidos por terceros para la E2 durante ≥ 6 meses** [INT, tribunal final, 2.ª ronda]. **El hábito decide el tipo de GO (§8.4)** | **Parar**, sin prórroga. El catálogo queda publicado |
| **Control de hábito** | 31-08-2027 (M9), solo si hubo GO condicionado | Se para si H1 < 25 %, H4+H5 < 35 % **y** vistas a 30 días < 103 | Parada anticipada (ahorro de ~330 € y ~105 h) |
| **P2 (proyecto lateral viable)** | 30-11-2027 · 36 vídeos | Vistas a 30 días ≥ 100; ≥ 100 suscriptores; Youtubeiras+ 2027 presentado; ≥ 5 propuestas de patrocinio enviadas | Parar la producción; conservar el catálogo |
| **P3 (Etapa 3)** | 31-05-2028 · 60 vídeos | En el YPP, **o** ≥ 50 €/mes recurrentes, **o** ayuda o encargo concedido | Mantenimiento (o cierre si no se ejerce la opción CRTVG) |
| **Puerta roja** | En cualquier momento | — | Se congela la publicación 2 semanas si ocurre cualquiera de estas cosas: una crítica pública de una entidad relevante; un error grave señalado por un historiador; oposición o retirada del locutor, de ADA o de AGPTI; un aviso de monetización limitada; > 50 % de comentarios negativos sobre la IA en un mes |

**Señal de rama alta** (no es una puerta): ≥ 200 vistas a 30 días y ≥ 70 suscriptores en la P1, o ≥ 400 suscriptores y ≥ 8.000 h en la P2. Si aparece, se adelantan las membresías, el dossier de patrocinio y la decisión sobre la CRTVG.

### 8.3 KPIs: pocos que deciden y el resto para diagnosticar [INT]

El crítico de la última ronda de la pieza de mercado señaló un problema de tamaño de muestra. Con ~200 espectadores únicos al mes y ~700 impresiones por vídeo en la P1, las pruebas 4 + 4 deciden con saltos que caen dentro del ruido: +1 punto de CTR, +10 % de vistas, ±5 puntos de retención. Por eso:

**Solo seis KPIs deciden las puertas:**

| # | KPI decisivo | P1 | P2 | Por qué |
|---|---|---|---|---|
| K1 | Vistas medias a 30 días por vídeo | ≥ 60 | ≥ 100 | Separa las ramas del modelo |
| K2 | Suscriptores totales | ≥ 20 | ≥ 100 | Es el cuello de botella del fan funding y del YPP |
| K3 | AVD (duración media vista) | ≥ 20 min | ≥ 20 min | Horas del YPP |
| K4 | H1: % de espectadores recurrentes | ≥ 20 % | ≥ 30 % | Solo el hábito separa en M6 la base de la estancada |
| K5 | H4+H5: tráfico de hábito (listas, sugeridos propios y navegación) | ≥ 30 % | ≥ 45 % | Ídem |
| K6 | Errores verificados por hora de audio y quejas graves de lengua | ≤ 1, 0 graves | ≤ 1 | Es la condición no negociable del proyecto |

- **K4 y K5 se leen como la media de dos ventanas de 28 días.** Si Studio oculta el dato por falta de volumen, se anota como "no medible" y deciden K1-K3.
- **Solo de diagnóstico, sin decidir nada:**
  - R1-R3 (impresiones por vídeo, CTR en navegación y sugeridos, cuota de sugeridos ajenos);
  - H2-H3 (horas y vistas por espectador);
  - las métricas de comunidad (Carta, redes, % de comentarios en galego);
  - horas de audio en Spotify, iVoox y Apple;
  - geografía;
  - sentimiento sobre la IA (salvo la Puerta roja).
- **Regla de empaquetado antes que formato:** si el embudo falla (pocas impresiones o CTR < 3 %), se cambian primero la miniatura y el título, que es barato y reversible. El formato solo se toca si, con el embudo en su umbral, el hábito sigue bajo.

**Regla de tamaño mínimo para cualquier prueba A/B** [S]:
- **Mínimo por brazo:** ≥ 2.000 impresiones (para CTR) y ≥ 4 episodios comparables (para retención y vistas).
- **Decisión:** solo si la diferencia supera **2 errores estándar** o si la dirección se repite en **≥ 3 de 4 pares**.
- **Si no, es "no concluyente":** se mantiene lo actual y **no se vuelve a probar hasta tener el doble de volumen**.
- **Consecuencia:** las pruebas E4 (frase suave de despedida), E6 (metadatos traducidos), E11 (duración), E13 (estrea sí o no) y la parte comparativa de E15 **pasan a la Etapa 2** o esperan a tener ese volumen. Así se liberan horas de una Etapa 1 que va sin margen.

### 8.4 Matriz de hábito en la P1

| | Hábito alto (H1 ≥ 35 %, H4+H5 ≥ 45 %) | Hábito cumple (H1 ≥ 20 %, H4+H5 ≥ 30 %) | Hábito bajo |
|---|---|---|---|
| **Adquisición cumple** (K1-K3) | **GO + acelerar:** revisión científica en cada episodio, Carta quincenal, membresías y dossier de patrocinio adelantados. La cadencia no pasa de semanal | **GO** normal | **GO condicionado:** los 8 primeros episodios de la Etapa 2 prueban el menú de cambios (primero el empaquetado; después serializar, listas "Serán longo", duración, ritmo y hora) + control de hábito en M9 |
| **Adquisición no cumple** | **Parar** (se documenta el hábito) | **Parar** | **Parar** |

En la P2, la misma lógica con los umbrales de la P2. Con hábito bajo: segunda ronda de cambios y control en M15; si no se cumple, mantenimiento anticipado.

### 8.5 Experimentos por etapa

| # | Experimento | Etapa | KPI y criterio | ¿Decide una puerta? |
|---|---|---|---|---|
| E0 | Voz: Puerta V-0 + Puerta V (§4.3-4.4) | 0 | §4.3 | **Sí** (Puerta V) |
| E1 | Guion ciego (G1) | 0 | §8.2 | **Sí** |
| E2 | Panel privado nativo | 0 | ≥ 70 % "volvería"; 0 errores graves | **Sí** (P0) |
| E3 | Retención, hábito y rama | 1-2 | K1-K5; lectura temprana en M4 (vídeos 1-4: < 40 vistas = clónico; 50-150 = base; > 180 = alta), P1, M9 y P2 | **Sí** |
| E5 | Calidad percibida pública | Continuo | K6 | **Sí** |
| E8 | Transparencia sobre la IA | Continuo | ≤ 30 % de negativos (Puerta roja si > 50 %) | Solo la Puerta roja |
| E12 | Patrocinio | M9-M12 | ≥ 5 propuestas enviadas (A14: tasa de venta) | **Sí** (P2) |
| E16 | Financiación de la calidad | Semanas 2-5; M4-M6 | Puerta F: compromisos ≥ ≈ 3.680 € (meta ≈ 5.140 €). F2: ≥ 440 €/mes para la E2 | **Sí** (F y P1) |
| E7 | Geografía y desbordamiento | 1-2 | Si > 25 % de las horas viene de fuera de España, se abre la pregunta de las pistas es/pt | No |
| E9 | Mediadores | 1-2 | ≥ 3 de cada 20 entidades responden | No |
| E10 | Audio primero | 1-2 | Horas de audio ≥ 25 % de las de YouTube | No |
| E14 | Comunidad propia | 1-2 | Carta: 40 / 150 suscriptores; ≥ 60 % de comentarios en galego | No |
| E4, E6, E11, E13, E15 | CTA suave, metadatos traducidos, duración, estrea, espejo y Test & Compare | **Etapa 2**, con la regla de tamaño mínimo | §8.3 | No |

### 8.6 Calendario de 14 meses

| Mes | Producción | Pruebas y puertas | Go-to-market | Cumplimiento y financiación |
|---|---|---|---|---|
| **Oct 2026** | MVP, bloques 1, 6 y 11 (repositorio, capa de voz, cómputo) | B0, G0, **V-0**; D1-D6; **Puerta F** preparada (dossier y peticiones desde la semana 2) | Registrar @seran y seran.gal; alta en Spotify for Creators (SPP en España desde el 20-10); funciones avanzadas del canal; cuentas en Bluesky, mastodon.gal y Telegram; Carta preparada | Correo a Nós/Gradiant (semana 1); 3 presupuestos de narradores y revisor; OEPM y EUIPO; "O teu Xacobeo": **no** (exige alta) |
| **Nov 2026** | MVP, bloques 2-5 y 7-10 | **Decisión de la Puerta F (semana 5, hasta el 04-11)**; Puerta V formal (si V-0 = sí y F = sí): H1/H2, R1-R3; G1 | Lista de vídeos semilla con URL | Consentimiento del locutor (si la voz es de Nós); **carta a ADA y AGPTI**; Youtubeiras+ 2026: **no** |
| **Dic 2026** | Episodios 1-3 (cada uno cuesta el doble) | Paso 0 y decisión de voz; G2, G3; prueba de defectos sembrados | Web "Como facemos Serán" | Lista de cumplimiento |
| **Ene 2027 (M2)** | **Lanzamiento el 17-01 con 3 episodios**; el 4.º el 31-01 | E2 (panel) → **P0**; empiezan E3, E5 y E8 | Fase suave; ritual; Carta n.º 1; alta en Podgalego y Obradoiro (cuando haya ≥ 1 publicación al mes) | — |
| **Feb 2027 (M3)** | 2 · 6 | — | Primera oleada a la diáspora (España y Europa); 3 divulgadores | YPP: regla de 8.000 h desde el 1-02 |
| **Mar 2027 (M4)** | 2 · 8 (especial del Día Mundial do Sono el domingo 14-03; el día es el viernes 19-03) | **Lectura temprana** (vídeos 1-4): recalibrar la P1 | **Fase pública:** nota de prensa, Radio Galega | — |
| **Abr 2027 (M5)** | 2 · 10 | — | Primer intercambio con un pódcast; Reddit | Ayudas del Ministerio: no (exigen alta). **Puerta F2:** pedir compromisos para la E2 (concellos con la PL400A de 2027 resuelta, patrocinio, membresías) |
| **May 2027 (M6)** | 2 · **12** (09-05 y, como excepción a la cadencia, Letras, Neira Vilas, el domingo 16-05) | **P1 (31-05)** con la matriz de hábito | Serán das Letras; oleada a Argentina y Cuba | Revisión de derechos del episodio de las Letras |
| **Jun 2027 (M7)** | Etapa 2: 4 · 16 (2 h) | E11 y E4 con la regla de tamaño mínimo | Carta quincenal; primer tema votado | **CRTVG (~junio): solo como opción** (alta y cesión); preguntar la tasa |
| **Jul 2027 (M8)** | 4 · 20. Serie "Historias do Camiño" (Año Santo 2027) | E6 y E13 (si hay volumen) | Xacobeo; espejo de los vídeos del Camino | — |
| **Ago 2027 (M9)** | 4 · 24 | **Control de hábito** (si hubo GO condicionado) | Visitas de verano de la diáspora | — |
| **Sep 2027 (M10)** | 4 · 28 | E12: propuestas de patrocinio | Colaboración "da man de…" | — |
| **Oct 2027 (M11)** | 4 · 32. **Samaín 2027** | — | Primer gran episodio de temporada | — |
| **Nov 2027 (M12)** | 4 · **36** | **P2 (30-11)** | Balance de E14 y E15 | **Youtubeiras+ 2027 presentado** (antes de ~15-11) |

---

## 9. Próximos pasos: las primeras 5 semanas

**Objetivo: llegar a las decisiones V-0 y F gastando casi nada.** Son las puertas más baratas del plan: si no hay una voz en la liga necesaria, o si nadie más que el promotor está dispuesto a pagar la calidad, se sabe antes de gastar 850-1.500 € de validación y ≈ 3.680 € de calidad.

| Semana | Tareas concretas | Horas | Coste |
|---|---|---|---|
| **1 (1-7 oct)** | **Decisiones D1-D6** (§0.2), por escrito. **Permisos de voz:** correo a Proxecto Nós (proxecto.nos@usc.gal, con copia a Gradiant; para Sabela-Nós, Icía, Iago y Paulo, al CRPIH de la USC y al GTM de la UVigo), que pide: (a) confirmación del uso comercial en YouTube y pódcast; (b) el alcance del consentimiento de los locutores; (c) que trasladen nuestra petición a cada locutor. **Marca:** registrar @seran y seran.gal; búsqueda en OEPM y EUIPO. **Presupuestos:** pedir 3 por escrito a narradores (al menos 2 hombres y 2 mujeres) y 3 a revisores lingüísticos cualificados (directorio de la AGPTI, estudios de dobraxe), por hora de escucha con texto y por palabra, más **3 a historiadores** para la revisión de la hoja de afirmaciones (§4.7), **sin firmar nada**. **Técnica:** repositorio y subagentes vacíos (bloque 1 del MVP); **prueba B0** en el equipo del promotor (10 min de audio) | ~6 h | ~20-30 € (dominio) [S] |
| **2 (8-14 oct)** | **Capa de voz** con Claude Code (bloque 6 del MVP): Cotovía fijado por hash con el canario *eu porto*, `g2p_override.py` a partir del prototipo y parche de `DUR_SCALE` + semilla + pausas + `s_prev`. **Kit de voz** (`kit_voz.py`): texto trampa y muestras M1-M3, revisados con su mujer. **R0 automática.** Elegir la **referencia humana pública** de V-0 (60 s de un narrador galego nativo en registro tranquilo: un audiolibro o la Radio Galega; anotar la URL y el minuto; solo para uso interno). **Puerta F:** dossier de 2 páginas (qué es Serán, garantía de calidad, paquete de ≈ 3.680 € y qué recibe cada financiador) y lista de destinatarios: servicios de normalización lingüística de concellos de ≥ 3.000 habitantes (PL400A), 3-5 marcas gallegas afines, Proxecto Nós/USC y AGPTI | ~6 h (+~3 h de la F) | 0 € (+~5 USD si se prueba ElevenLabs) |
| **3 (15-21 oct)** | **G0:** 50 palabras de riesgo (línea base → léxico → ABX ciego) y **A/B de ritmo con las variantes A-E del §3.3** sobre las 2-3 voces finalistas de R0. **V-0:** escucha ciega del promotor y su mujer (rúbrica del §4.4). **Puerta F:** enviar el dossier y abrir la página de mecenas o preventa (Ko-fi, sin umbral) | ~6 h (+~2 h de ella; +~3 h de la F) | 0 € |
| **4 (22-28 oct)** | **Decisión V-0**, escrita en `decision_voz.md`. **Si es SÍ:** seguimiento de la Puerta F; dejar listos, **sin firmar**, los contratos de H1 y H2 (T0 + las opciones T1/T2) y del revisor profesional; redactar `preregistro_voz.md` y la carta a ADA y AGPTI (se envía con la voz decidida). **Si es NO:** aplicar D2 (esperar con reevaluación trimestral, o pedir presupuesto de voz licenciada) y dejar el pipeline de texto (bloques 2-5) a ritmo bajo. **En los dos casos:** empezar el investigador y `extrae_cita.py` (bloques 2-3) con las fuentes del Episodio 1 (Reino suevo) | ~6 h | 0 € (la excepción, si se aprueba, se paga en noviembre) |
| **5 (29-10 a 04-11)** | **Decisión de la Puerta F**, escrita en `decision_financiacion.md`: suma de compromisos firmes (solo cuentan los firmados y, de una carta condicionada a la PL400A de 2027, la parte que el concello asuma sin ella). **Si llega al diferencial (≈ 3.680 €):** con D1 aprobada, firmar H1, H2 y el revisor, sellar el prerregistro y programar las grabaciones. **Si no llega:** presupuesto de hobby (D6), sin validación ni publicación; calendario del reintento | ~4 h | 0 € (la excepción, si se aprueba, se paga en noviembre) |

**Entregables al final de la semana 5:**
- `decision_voz.md` (resultado de V-0 y de G0, variante de ritmo ganadora y topes);
- informe de B0;
- `lexico_gl.tsv` v0 con las entradas verificadas;
- respuestas (o no) de Nós;
- presupuestos de narradores, RLC (por palabra en mesa y por hora de escucha) e historiador, con la decisión D5;
- `decision_financiacion.md` (Puerta F: compromisos firmados, importe y condiciones);
- @seran y seran.gal registrados.

---

## Anexo A. Metodología: el Gauntlet Loop que se usó

### A.1 Qué es y cómo se aplicó

1. **Punto de partida.** Se abrió el enlace de la conversación con Gemini (https://share.gemini.google/1zO2a3MXJETr); la transcripción está en `gauntlet/gemini_conversation.md`. **Se tomó solo el concepto:**
   - canal *faceless* 100 % IA con curaduría humana;
   - adaptación a Galicia en galego, con sus tres cuellos de botella (TAM pequeño, TTS en galego inmaduro y una comunidad que castiga los errores);
   - economía de vídeo largo;
   - pipeline agéntico por etapas.
   
   Se descartó expresamente el estilo de "fábrica de engagement", que es lo contrario del contenido para dormir. Las herramientas concretas (Colab móvil, Clipchamp, créditos de NVIDIA) solo entraron como opciones a evaluar.
2. **Respuestas del promotor** (`contexto.md`): los retornos van primero; plan por etapas (<50 €/mes y ~4 h/semana → 50-200 €/mes → 1.000-5.000 € solo si funcionan); juez de la voz: él y su mujer con un kit A/B; intensidad alta.
3. **Seis piezas.** Cada una la escribió un **agente constructor** y la atacó un **agente crítico** con un perfil experto y un **listón explícito**. En cada ronda el crítico devolvía carencias y errores factuales, y el constructor rehacía la pieza.
4. **Paradas posibles:**
   - **gana:** el crítico no encuentra carencias;
   - **mejora marginal:** la ronda siguiente apenas mejora;
   - **presupuesto de rondas:** 5 como máximo.
5. **Alisado e integración (este documento):** se unifican las cifras entre piezas, se aplican las correcciones que quedaron pendientes en la última ronda cuando se podían aplicar sin datos nuevos, y **se declara lo que no se cerró**.

### A.2 Piezas, listones y resultado

| Pieza | Crítico (perfil) | Listón o referencia elegida | Rondas y resultado | Qué quedó abierto al final | Qué hizo la integración |
|---|---|---|---|---|---|
| **Retornos y modelo financiero** | Crítico del modelo financiero (perfil no registrado en la pieza) | **Solo tasas base observables:** 9 canales clónicos medidos, 126 inscritos en Youtubeiras+ 2025, bases de la CRTVG leídas página a página; las ayudas sin tasa base pasan a ser opciones | **3 rondas · GANA.** Sin carencias en la última | Nada, dentro de la pieza | Se ajusta a los costes de las demás piezas en un **árbol conjunto voz → audiencia** (§1.3, rehecho en el tribunal final): el valor esperado pasa de −147 € (condicionado a que haya voz) a **≈ −3.570 €** conjunto si el promotor paga la garantía de calidad (0 % de caja positiva), y a **≈ −340 €** con las Puertas F y F2 de la 2.ª ronda del tribunal (≈ 0,3 % de caja positiva). **Aviso:** ese ajuste es aritmética de integración con probabilidades de voz y de financiación [S] y no pasó por el crítico de la pieza |
| **Producto y formato** | Productor de un canal de historia para dormir | **History at Night, "The Great Maya Collapse"** (listón) y History Time, "After Rome" (techo) | **3 rondas · mejora marginal** | **Ritmo incoherente entre secciones:** brief a 120-135 de habla pura, receta que da ~143, checklist de 105-130 frente a una QA de 115 ±5 %, "+10 %" frente a "+35 %" de pausa en el Acto III | **Resuelto:** tabla única de ritmo (§3.3) con la velocidad real de la voz (191,5) y una decisión por prueba ciega (G0). Los topes definitivos quedan pendientes de G0 |
| **Guion muestra en galego** | Historiador medievalista | **Literatura académica** (Carlos Barros, USC, con página; ediciones documentales a través de él). Galipedia, solo de apoyo | **4 rondas · mejora marginal** | Pulgar llamado "cronista" en 1467 (anacronismo); la escena de la Rocha Forte apoyada en Galipedia; los asistentes a Melide narrados como hecho seguro | **Aplicado en la copia:** se quita "o cronista"; la Rocha Forte se reduce a Barros y el Preito; Melide pasa a recuerdo de un testigo y se retira el nombre ambiguo de Andrade. **Pendiente:** citar la memoria de excavación si se quiere recuperar la escena completa |
| **Voz y protocolo A/B** | Ingeniero de audio y director de doblaje | **"No se distingue de un narrador nativo profesional"** en una prueba ciega (MUSHRA con control positivo humano + identificación humano/IA con N ≥ 20) | **5 rondas · se paró por presupuesto (NO ganó)** | **Falta una prueba ciega de escucha larga (R3-L, 20-25 min continuos, 40-60 oyentes)**, que es el formato real del producto. Precisión menor: la fecha de publicación de Nós | **No resuelto:** se declara en el §4.3 como carencia y se recomienda antes de R4. La fecha se corrige ("2026"). Se añade la Puerta V-0 barata (§4.4) |
| **Pipeline, costes y tiempos** | Ingeniero senior de sistemas de IA generativa | **Diseño implementable sobre el código real de Nós**, con medidas propias [P] | **5 rondas · se paró por presupuesto (NO ganó)** | **El control de ritmo no funciona con los 191,5 de habla medidos** (haría falta k de 2,75-3,84 frente al rango de 0,7-1,6); el RTF de 0,28 citado solo tiene detrás una frase | **Resuelto en el diseño** (§3.3: variantes A-E y regla de G0; `ritmo.py` con las pausas base de la ganadora). **Corregida la evidencia** (§5.3: 0,28 sobre una frase; 0,38 robusto). **Pendiente:** repetir el A/B de ritmo con audio real en G0 |
| **Mercado, marca, lanzamiento, riesgos y pruebas** | Panel: sociolingüista galega + *growth marketer* | **Puertas idénticas al modelo de retornos** y KPIs con las definiciones oficiales de YouTube Studio | **5 rondas · se paró por presupuesto (NO ganó)** | **Reglas de decisión sin tamaño de muestra**; "Pedístelo" (no normativo); "sin YPP no hay anuncios" (inexacto); licencia del dataset de Nós citada de forma incompleta | **Resuelto:** 6 KPIs decisivos, regla de tamaño mínimo y resultado "no concluyente"; las pruebas pequeñas pasan a la Etapa 2 (§8.3). "Pedíchelo" corregido. Riesgo de anuncios antes del YPP y fin del "sen cortes" en la Etapa 1 (§3.5, §7.1). Licencia del dataset precisada (§4.2, §7.4) |

### A.3 Contradicciones entre piezas que resolvió la integración

| Contradicción | Piezas | Resolución |
|---|---|---|
| Calendario: lanzamiento el 22-11-2026, frente a un pipeline listo en la semana 10-12 y 5-7 semanas de protocolo de voz | GTM, pipeline, voz | Lanzamiento el **17-01-2027**; P1 el 31-05-2027, P2 el 30-11-2027, P3 el 31-05-2028 (§1.2) |
| Coste de la Etapa 1: 210 € frente a una excepción de voz de 850-1.500 € | Retornos, voz | Se suma en el §1.3, y se pone delante la Puerta V-0 barata. **Tribunal final, 2.ª ronda:** además, la Puerta F, para que la calidad la paguen terceros |
| Listón de la voz: "≥ 4/5 durmiría" (E0) frente a "indistinguible de un profesional" (Puerta V) | GTM, voz | E0 pasa a ser la **preselección V-0**; la Puerta V es la de publicación |
| Voz de reserva de proveedor "que no bloquea" frente a "solo si pasa la Puerta V" | GTM, voz | Solo si pasa la Puerta V (§4.5) |
| Consentimiento: solo la USC frente a la USC + el locutor | Voz, GTM | **Doble permiso** (§4.5) |
| Escucha H3 de 0,8 h frente a escucha completa firmada | Pipeline, voz | Escucha completa; horas recalculadas (§5.4) |
| Revisor lingüístico en la Etapa 2: 40-60 / 40-80 / 64-112 €/mes | Retornos, pipeline, voz | 64-112 €/mes y caja de ≈ 138 € en la integración. **Sustituido en el tribunal final** por el RLC sobre el texto y el RHC: ≈ 550 €/mes (§5.4, D5), a cargo de terceros (Puerta F2) |
| Condición de la P2: "≥ 1 solicitud de ayuda" (GTM) frente a nada (retornos v3) | GTM, retornos | Youtubeiras+ 2027 presentado (§1.1) |
| Promesa con "sen cortes" frente a sin él | GTM, formato | Sin él; la etiqueta solo en el YPP (§3.5) |
| Compilación mensual en el canal frente a solo en el pódcast | Formato, pipeline | En la Etapa 1, solo en el pódcast (§3.7) |
| Criterio del guion ciego: 2/4, 3/5 o ≥ 4/5 | GTM, formato, pipeline | 3/5 sin notas ≤ 2 en lengua + ≤ 1 error por 1.000 palabras (§4.7) |
| FLUX en Runpod frente a "FLUX.1 [dev] no comercial" | Pipeline, GTM | Solo FLUX.1 [schnell] o una API comercial (§5.2) |
| Posición del aviso de voz: después de una escena de 45-60 s frente a los primeros 30 s | Formato, GTM | Una frase de aviso al principio y después la escena (§3.2) |

### A.4 Lo que este plan no demuestra (honestidad)
- **Que exista hoy una voz en galego que pase la Puerta V.** Es el escenario central (60-80 % de que no).
- **Que la Puerta V valide la escucha larga.** Falta la R3-L.
- **Que los umbrales de hábito y de embudo separen las ramas.** Son supuestos derivados del modelo, sin *benchmark* de canales de sueño en galego.
- **Las tarifas gallegas** de narración, revisión lingüística y revisión histórica: no hay ninguna publicada.
- **El volumen de búsqueda en galego:** no hubo acceso a Google Trends.
- **Las probabilidades de rama del árbol** son [S], argumentadas con una tasa base de canales en castellano.
- **Los ajustes de integración del §1.3** no los revisó ningún crítico del gauntlet de su pieza; el árbol conjunto sale de la ronda del tribunal final (A.5).
- **Las probabilidades de la voz del árbol conjunto** (V-0 55 %, Puerta V 55 %, vía (c) 40 %) son [S], coherentes con el 60-80 % de suspenso del §4.1, pero sin tasa base.
- **Las tarifas del RLC y del historiador** y la tasa de fallo de muestra de la Etapa 2 (10 %) son [S]. Solo hay anclas de precio de lista de corrección, no de revisión histórica.
- **Que la Puerta F se pueda pasar.** P(F) = 25 % y P(F2) = 40 % son [S] sin tasa base. No se sabe si algún servicio de normalización ha encargado alguna vez contenido de este tipo, ni si un concello puede comprometer gasto de 2027 en noviembre de 2026; antes del lanzamiento no hay audiencia que haga preventa.
- **Que la inspección reducida de la Etapa 2 sea suficiente:** deja hasta ~9 errores normativos leves sin leer por episodio de 2 h si el proceso va justo en el límite (§4.7); lo declara el aviso.
- **Que el guion de un episodio completo cumpla las densidades:** la auditoría del §4.7 cubre ~7 min de la muestra, no un episodio de 75 min.

### A.5 Tribunal final

Después del alisado, un **tribunal** revisó el plan y el guion muestra en dos rondas. Cada juez daba carencias y errores factuales, y un agente de alisado aplicó las correcciones en esta versión (29-09-2026).

#### A.5.1 Primera ronda (tres jueces)

| Juez (perfil) | Veredicto | Qué señaló | Qué se corrigió |
|---|---|---|---|
| **Inversor** | No aprobado: el valor esperado no era un valor esperado conjunto | El "−1.250 a −1.900 €" aplicaba la validación a todos los caminos y mezclaba probabilidades condicionadas a que hubiera voz con el 60-80 % de otro árbol, así que la tabla no sumaba el 100 %. La fila optimista no descontaba el revisor de la Etapa 2. "Equilibrio en M15" y "+3.355 €" usaban una caja de 110 €/mes. El "≈ 10 %" era condicional. Las "~400 h" infravaloraban la Etapa 2 (35 frente a 37-44 h/mes) | **§1.3 rehecho** como árbol único voz → audiencia (`model/arbol_conjunto.py`). Tabla de resultados que suma el 100 %, valor esperado de caja y horas y probabilidad conjunta de caja positiva. Equilibrio del P4 con 138 €/mes en M18. Propagado a §0.1, §0.2, §1.1, §1.5, §1.6, §1.9 y A.2-A.3 |
| **Galego** (lengua y veracidad) | No aprobado: pasada la P0, la garantía dependía de personas sin cualificación acreditada, y la revisión histórica no estaba en la caja | El texto solo lo revisaban el promotor y su mujer; en los episodios 7-12, 0 € de revisión profesional. Historiador en 1 de cada 4 episodios y fuera de la tabla de caja. Aviso "revisárono persoas galegofalantes". Cita falsa del DRAG en "Serán". "Temporizador de apagado". "Polo de agora". [COMP] sin definir. Día Mundial do Sono | **Roles RLC y RHC** con perfil, alcance, criterio de aceptación y regla por temas (§4.7), costeados en el §5.4 (≈ 130 € por episodio) y metidos en el árbol. **No caben en los límites: decisión D5** (se sube el límite de la E1 y la E2 no se abre por defecto), sin rebajar la garantía. Aviso con la cualificación real (§4.5). Cita del DRAG corregida (§3.7). "Apagamento" (§3.5). "Por agora" (guion). [COMP], [CALC] y [F-sec] definidas |
| **Operador** (producción) | No aprobado: el guion muestra incumplía las densidades del §3.2 y el §4.7 lo daba por conforme | Entrada con 3 fechas y 6 nombres; Acto I con ~3,5 nombres nuevos por minuto, 8 años completos, "cento vinte e oito" y "seis de xullo"; apertura en asalto. Cadencia rota por el vídeo 12. Día Mundial do Sono mal fechado | **Guion v5 reescrito** (~770 palabras) con apertura en calma, derribo anticipado y Castilla en una frase, más la **auditoría automática** adjunta (`auditoria/audita_densidade.py`): entrada con 1 fecha y 2 nombres; Acto I con un máximo de 3 nombres nuevos en 60 s, 1 fecha redondeada y activación ≤ 3. **Calendario:** Día Mundial do Sono 2027 = viernes 19-03, con el especial el domingo anterior (14-03); vídeo 12 el 16-05 como única excepción declarada a la cadencia (§1.2, §6.2, §8.1, §8.6) |

**Qué cambió en la conclusión (primera ronda).** El NO-GO como negocio se reforzó. Con la calidad pagada por el promotor, ningún camino recupera la caja a 36 meses, y el plan recomendaba **publicar los 12 vídeos y parar en la P1** (≈ −1.715 € de valor esperado frente a ≈ −2.720 € si se seguían las puertas). **La segunda ronda corrigió esa lectura** (A.5.2): era la menos mala de las políticas que publican, no la que minimiza la pérdida, y dejaba la P1 sin decidir nada. El GO a la Puerta V-0, que casi no cuesta nada, no cambió.

**Lo que la primera ronda no cerró:** las tarifas reales del RLC y del historiador (3 presupuestos en la semana 1); la etiqueta de la interfaz de YouTube en galego para el temporizador; y la confirmación histórica de "mosteiros" y de la estación del derribo de la Rocha Forte en el guion (marcadas [S]).

#### A.5.2 Segunda ronda (dos jueces)

| Juez (perfil) | Veredicto | Qué señaló | Qué se corrigió |
|---|---|---|---|
| **Inversor** | Con carencias: la recomendación no tenía una puerta que diera valor a lo que se compra | Tras una V-0 positiva, el plan mandaba gastar ≈ 2.700-3.400 € (validación + paquete de calidad de la E1) aunque su propio árbol demostraba que ningún camino recupera la caja, y bajo una política ("parar siempre en la P1") que dejaba la P1 sin decidir nada. **Errores:** llamar "la que minimiza la pérdida" a parar en la P1 (≈ −1.715 €) cuando no gastar tras la V-0 da ≈ −40 €; 24 frente a 25 y 107 frente a 108 suscriptores entre el §1.1 y el §1.6; los 1.550 € de la E1 repartidos en 6 meses (dic-may) frente a una E1 de 5 meses (ene-may); la escucha íntegra de los episodios 1-6 (9-15 h de RLC) cargada a una excepción de voz que no la presupuesta (≈ 200-500 € de menos); "40 bloques" frente a "20 bloques" en el §4.6 sin decir que son dos muestreos distintos | **Puerta F** entre la V-0 y la validación (compromiso de terceros ≥ el diferencial de calidad de la E1; fuentes: PL400A de la SXL [F, DOG 7-04-2026], mecenas o preventa, patrocinio prevendido, convenio con Nós/USC o AGPTI) y **Puerta F2** en la P1 (≥ 440 €/mes para la E2), con lo que la P1 vuelve a decidir. **§1.3 recalculado** (`model/arbol_conjunto_f.py`): valor esperado ≈ −340 € (−230 a −495), ≈ 0,3 % de caja positiva; umbral para que la hoja P1 salga a cero, ≈ 5.140 €; **presupuesto de hobby** si falla la F (D6: ≤ 300 € en 6 meses). Tabla de políticas: **no gastar tras la V-0 (≈ −40 €) es la que minimiza la pérdida**; parar siempre en la P1 sin F (≈ −2.560 €) es solo la menos mala de las que publican. Suscriptores: se explica que el §1.1 usa el calendario real y el §1.6 el del modelo. E1 repartida en los 5 meses del §1.1 (≈ 770 €/mes; ≈ 650 €/mes en 6). Escucha de los ep. 1-6 presupuestada aparte. Los dos muestreos del §4.6 separados: audio (H3, 40 bloques) y texto del RLC (20 bloques). Propagado a §0.1, §0.2, §1.1, §1.5, §1.6, §1.9, §1.10, §4.4-§4.7, §5.4, §8.2, §8.5, §8.6, §9 y A.2-A.4 |
| **Galego** (lengua y veracidad) | Con carencias: el aviso prometía una "revisión íntegra" que no estaba hecha ni presupuestada | La "revisión íntegra" de los ep. 1-6 era la escucha con texto, sin corrección de mesa, cargada a la excepción de voz (que no existe si la V-0 dice que no o por la vía (b)) y con ~0,4 h de texto para ~8.400 palabras. La tolerancia de la muestra de los ep. 7 y siguientes (≤ 1/1.000 sobre 1/3 del texto) no estaba justificada. **Errores:** "durmiríame con isto" (el DRAG recoge *durmir* como intransitivo y transitivo, no pronominal); en el guion, "marcharon cara a Castela" (incompleto: parte de los señores fue a Portugal, y de allí vino parte de la reacción de 1469); "pouco máis de dous anos" desde el verano de 1467 (son menos de dos); "en todas partes" (*todo* ante sustantivo lleva artigo) | **Corrección de mesa del 100 % del texto antes del render** en los 12 episodios de la E1 (0,015-0,025 €/palabra, 126-210 € por episodio), seguida de la escucha con texto de los ep. 1-6. **Inspección normal por defecto** y reducida (muestra de 20 bloques) solo tras 10 episodios limpios, con vuelta a la normal al primer fallo; qué garantiza la muestra y qué no, calculado (§4.7). El aviso de "revisión íntegra" solo si hubo mesa (§4.5). **Paquete de la E1: ≈ 3.680 € (2.390-5.010), ≈ 305 € por episodio**, propagado a D5, §0.1, §1.3 y §5.4. "Durmiría con isto" (§3.3, §4.4, A.3; verificado en el DRAG). **Guion v5.1:** "cara a Castela ou a Portugal" [F-sec, con cotejo pendiente en Barros], "ata dúas primaveras despois" y "en todas as partes" ([S], a confirmar por el RLC); auditoría de densidad repetida: sigue pasando (máximo de 3 nombres nuevos en 60 s) |

**Qué cambia en la conclusión (segunda ronda).** El NO-GO como negocio no cambia: con la calidad pagada por el promotor, el paquete de la E1 casi se duplica y el valor esperado empeora a ≈ −3.570 €. Lo que cambia es la recomendación: **tras la V-0 no se gasta nada más sin un compromiso de terceros que pague la calidad (Puerta F)**, y la P1 vuelve a decidir con la Puerta F2. Con esa política, el promotor arriesga ≈ −340 € de valor esperado y, si pasa la F, ≈ −1.930 €, que es sobre todo la validación de la voz.

**Lo que la segunda ronda no cerró:** P(F) y P(F2) sin tasa base (se miden en la semana 5 y en la P1); si un concello puede comprometer en noviembre gasto de 2027 ligado a la PL400A; la norma ISO 2859-1 (no consultada; las reglas de cambio son de diseño); la corrección "en todas as partes", pendiente del RLC; y el cotejo de la huida a Portugal con Barros (hoy, fuente secundaria).

---

## Anexo B. Fuentes (URLs)

Estas son todas las URLs citadas en las seis piezas del gauntlet, sin duplicados (258 extraídas, menos las plantillas de comprobación con `<parámetro>`). Cada URL aparece una sola vez, en el grupo de la primera pieza que la cita; entre corchetes van las otras piezas que también la usan. Se consultaron el 29-09-2026, salvo que la pieza diga otra cosa. Los informes de investigación previos (`research/*.md`) y las referencias (`refs/*.md`) del directorio de trabajo tienen además sus propias URLs.

**Añadidas en la integración:**
- Conversación de origen (solo se tomó el concepto): https://share.gemini.google/1zO2a3MXJETr
- Términos de servicio de YouTube, derecho a monetizar el contenido (anuncios en vídeos de canales fuera del YPP; corrección factual de §3.5 y §7.1): https://www.youtube.com/t/terms

**Añadidas en el tribunal final (consultadas el 29-09-2026):**
- DRAG, "serán" (acepciones 1-4; corrección de la cita del §3.7): https://academia.gal/dicionario/-/termo/busca/serán
- DRAG, "apagamento" (§3.5, regla 14): https://academia.gal/dicionario/-/termo/busca/apagamento
- DRAG, "agora", locución "por agora" (guion muestra): https://academia.gal/dicionario/-/termo/busca/agora
- Día Mundial do Sono, "el viernes anterior al equinoccio de marzo": https://en.wikipedia.org/wiki/World_Sleep_Day (la página days.to/world-sleep-day/2027, ya citada, devolvió 403 en esta consulta)
- Equinoccio de marzo de 2027 (sábado 20-03): https://es.wikipedia.org/wiki/Equinoccio_de_marzo
- Tarifa de corrección en galego ("desde 0,010 €/palabra"; "corrector titulado en traducción o lingüista") [F-sec]: https://shoptexto.com/correccion-ortografica-y-de-estilo-en-gallego/

**Comprobaciones técnicas reproducibles (plantillas)**, usadas para el nombre del canal:
- `https://www.youtube.com/@<handle>`
- `https://rdap.org/domain/<dominio>`
- `https://itunes.apple.com/search?media=podcast&country=ES&term=<nombre>`
- `https://gl.wikipedia.org/w/index.php?title=<página>&action=raw`

### B.1 Retornos, monetización, ayudas y comparables (pieza "retornos")

- https://support.google.com/youtube/answer/72851 [mercado]
- https://blog.youtube/news-and-events/youtube-partner-program-updates-2027-new-opportunities-earn/ [mercado]
- https://www.sbs.com.au/news/article/sleep-videos-are-hugely-popular-but-youtube-adverts-are-disrupting-peoples-dreaming/edc0h3p1r [mercado]
- https://support.google.com/youtube/answer/72902 [mercado]
- https://en.wikipedia.org/wiki/Sleep_with_Me_(podcast
- https://www.infobae.com/america/agencias/2026/09/25/spotify-anuncia-la-llegada-a-espana-de-partner-program-iniciativa-para-convertir-los-podcast-en-negocios-sostenibles/ [formato, mercado]
- https://techcrunch.com/2026/01/07/spotify-lowers-monetization-threshold-for-video-podcasts
- https://www.shopify.com/blog/how-to-make-money-on-spotify
- https://www.ivoox.com/blog/como-ganar-dinero-con-tu-podcast/
- https://ko-fi.com/pricing
- https://youtubeiras.gal/bases-youtubeiras-2026/ [mercado]
- https://www.crtvg.es/documents/d/crtvg/convocatoriaasinada09xuno2025contidosdixitais-pdf-1
- https://www.xunta.gal/dog/Publicados/2026/20260325/AnuncioG0256-090326-0002_gl.html
- https://www.boe.es/buscar/doc.php?id=BOE-B-2026-10741
- https://www.boe.es/buscar/act.php?id=BOE-A-2017-12902
- https://vidiq.com/youtube-stats/channel/@sleeplesshistorian/
- https://monetizateonline.es/cuanto-paga-youtube-espana/
- https://aceleratusredes.com/blog/cuanto-paga-youtube-por-pais-en-2026
- https://www.prodigiosovolcan.com/pv/sismogramas/informe-voz-2025/podcast.html [mercado]
- https://patillero.es/monetizar-podcast/
- https://jezzmedia.com/publicidad-en-podcasts-numeros-reales-en-espana/
- https://euribor.com.es/2026/09/20/la-economia-de-los-influencers-asi-se-calcula-el-precio-real-de-un-post-patrocinado/
- https://advertising.libsyn.com/podcast-advertising-rates
- https://www.ige.gal/estatico/html/gl/OperacionsEstruturais/Resumo_resultados_EEF_Galego.html [mercado]
- https://www.anthropic.com/pricing
- https://elevenlabs.io/pricing [voz]
- https://elevenlabs.io/pricing/api [voz, pipeline]
- https://huggingface.co/proxectonos/Nos_StyleTTS2-Brais-GL [formato, voz, pipeline, mercado]
- https://correccionencastellano.com/tarifas-correccion-textos/ [voz]
- https://escueladedoblajedemadrid.es/blog/alerta-maxima-ante-la-cesion-de-voz-para-aprendizaje-neuronal-de-la-ia-segun-uva/ [voz]
- https://youtubeiras.gal/ix-edicion-2025/
- https://youtubeiras.gal/viii-edicion-2024/
- https://youtubeiras.gal/setima-edicion/
- https://youtubeiras.gal/palmareshistorico/
- https://www.crtvg.gal/gl/web/crtvg/w/a-crtvg-producir%C3%A1-25-novos-proxectos-nativos-dixitais-en-galego
- https://www.audiovisual451.com/crtvg-producira-doce-nuevos-proyectos-nativos-digitales-en-gallego/
- https://www.crtvg.es/documents/d/crtvg/a-corporacion-de-servizos-audiovisuais-de-galicia-pdf
- https://www.audiovisual451.com/la-crtvg-abre-una-nueva-convocatoria-para-la-produccion-de-contenidos-digitales-destinados-a-sus-plataformas/
- https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/ [pipeline, mercado]
- https://www.audiovisual451.com/tvg-abre-una-convocatoria-de-seleccion-de-proyectos-digitales-en-gallego/
- https://www.xunta.gal/dog/Publicados/2026/20260407/AnuncioG0766-180326-0001_gl.html [Puerta F: PL400A 2026, DOG n.º 63, 7-04-2026; tribunal final, 2.ª ronda]
- https://sede.xunta.gal/detalle-procedemento?codtram=PL400A&ano=2022&numpub=1 [ficha del procedimiento PL400A]

### B.2 Producto, formato, referencias de escucha, Episodio 1 y catálogo (pieza "formato")

- https://www.youtube.com/watch?v=hbufma0ZlUw
- https://www.youtube.com/watch?v=sXBgNNtEJ6M
- https://www.youtube.com/watch?v=3uBP9QaWfPM
- https://www.youtube.com/watch?v=9jnekLeHz3c
- https://github.com/coqui-ai/TTS/blob/dev/TTS/tts/models/vits.py
- https://huggingface.co/proxectonos/Nos_TTS-brais-vits-phonemes
- https://github.com/shivammehta25/Matcha-TTS/blob/main/matcha/cli.py
- https://huggingface.co/proxectonos/Nos_TTS-icia-extended-matcha-phonemes
- https://www.youtube.com/watch?v=sXBgNNtEJ6M&t=0s
- https://www.youtube.com/watch?v=sXBgNNtEJ6M&t=12313s
- https://www.youtube.com/watch?v=hbufma0ZlUw&t=102s
- https://ilg.usc.gal/gl/proxectos/dicionario-de-pronuncia-da-lingua-galega
- https://freesound.org
- https://gl.wikipedia.org/wiki/Reino_Suevo
- https://gl.wikipedia.org/wiki/Codex_Calixtinus
- https://gl.wikipedia.org/wiki/Cultura_castrexa
- https://gl.wikipedia.org/wiki/Pórtico_da_Gloria
- https://gl.wikipedia.org/wiki/Torre_de_Hércules
- https://gl.wikipedia.org/wiki/Rexurdimento
- https://gl.wikipedia.org/wiki/Ribeira_Sacra
- https://gl.wikipedia.org/wiki/Serán
- https://gl.wikipedia.org/wiki/Magosto
- https://gl.wikipedia.org/wiki/Hórreo
- https://gl.wikipedia.org/wiki/Diego_Xelmírez
- https://gl.wikipedia.org/wiki/Lucus_Augusti
- https://gl.wikipedia.org/wiki/Castro_de_Baroña
- https://gl.wikipedia.org/wiki/Revolta_irmandiña
- https://gl.wikipedia.org/wiki/Canteiro
- https://gl.wikipedia.org/wiki/Illas_Cíes
- https://gl.wikipedia.org/wiki/Muíño
- https://gl.wikipedia.org/wiki/Emigración_galega
- https://gl.wikipedia.org/wiki/Afonso_VII_de_León_e_Castela
- https://gl.wikipedia.org/wiki/Mámoa
- https://gl.wikipedia.org/wiki/Torres_de_Oeste
- https://gl.wikipedia.org/wiki/Salga
- https://gl.wikipedia.org/wiki/Prisciliano
- https://gl.wikipedia.org/wiki/Sargadelos
- https://gl.wikipedia.org/wiki/Batalla_de_Elviña
- https://gl.wikipedia.org/wiki/Pedro_Pardo_de_Cela
- https://support.spotify.com/us/creators/article/spotify-partner-program/
- https://www.youtube.com/@handle
- https://academia.gal/dicionario/-/termo/serán
- https://academia.gal/dicionario/-/termo/arrolo
- https://www.buscalibre.us/libro-cronicon-de-hidacio-o-trivium-n-13-segiundo-premio-historia-medieval-de-galicia/9788496259133/p/3323533
- https://archive.org/details/cronicndeidacio00idatgoog
- https://www.thelatinlibrary.com/martinbraga/rusticus.shtml
- https://corpus.cirp.gal/codolga/fontes/2018_de_correctione_rusticorum
- https://academia.gal/membro/-/membro/paulino-pedret-casado
- https://gl.wikipedia.org/wiki/Parochiale_suevorum
- https://www.akal.com/libro/el-reino-suevo-411-585_34123/
- https://www.iberlibro.com/9788485319114/Reino-Suevos-Galicia-Sueva-Torres-8485319117/plp
- https://gl.wikipedia.org/wiki/Hidacio
- https://gl.wikipedia.org/wiki/Marti%C3%B1o_de_Dumio
- https://gl.wikipedia.org/wiki/Suevos
- https://egu.xunta.gal/gl/termo/109948/de-correctione-rusticorum
- https://historia-hispanica.rah.es/biografias/22911-hidacio
- https://culturagalega.gal/noticia.php?id=26577
- https://support.google.com/youtube/answer/9884579
- https://slate.com/human-interest/2018/05/phoebe-smith-sleep-story-writer-for-the-calm-app-on-the-art-of-boring-people-to-sleep.html
- https://productionadvice.co.uk/stats-for-nerds/
- https://www.marketingbrew.com/stories/2023/09/08/youtube-scraps-some-creator-ad-controls-builds-out-livestream-ad-capabilities
- https://support.google.com/youtube/answer/2467968?hl=en
- https://support.google.com/youtube/answer/9884579?hl=en
- https://tech.yahoo.com/streaming/articles/youtube-sleep-timer-best-feature-191515174.html
- https://www.tubefilter.com/2018/01/05/white-noise-youtube-content-id/
- https://support.google.com/youtube/answer/15424877?hl=en
- https://variety.com/2024/digital/news/youtube-shorts-maximum-video-length-three-minutes-1236166349/
- https://techcrunch.com/2025/09/10/youtubes-multi-language-audio-feature-for-dubbing-videos-rolls-out-to-all-creators/
- https://techcrunch.com/2026/09/17/spotify-expands-its-partner-program-for-podcasts-to-35-new-countries/
- https://www.404media.co/ai-generated-boring-history-videos-are-flooding-youtube-and-drowning-out-real-history/ [voz]
- https://podgalego.agora.gal/a-lareira/
- https://huggingface.co/proxectonos/Nos_StyleTTS2-Celtia-GL [voz, pipeline]
- https://github.com/proxectonos/cotovia

### B.3 Guion muestra: historia de la Revolta Irmandiña (pieza "guion")

- https://h-debate.com/wp-content/uploads/2016/07/viva_rei.pdf
- https://cbarros.com/viva-el-rei-rei-imaxinario-e-revolta-na-galicia-baixomedieval/
- https://cbarros.com/as-orixes-medievais-da-xunta-de-galicia/
- https://cbarros.com/lo-que-sabemos-de-los-irmandinos-2006/
- https://cbarros.com/como-alcanzaron-el-poder-los-irmandinos-en-el-reino-de-galicia-1467-1469/
- https://cbarros.com/gorrions-corren-falcons-os-irmandinos-de-galicia-2024/
- https://cbarros.com/la-revuelta-gallega-de-los-irmandinos-en-su-contexto-europeo-siglos-xiv-xvi/
- https://cbarros.com/la-guerra-de-los-caballeros-en-la-galicia-medieval/
- https://cbarros.com/como-construe-a-historiografia-o-seu-obxecto-os-irmandinos-de-galicia/
- https://cbarros.com/condesa-santa-marta-e-os-irmandinos-no-ultimo-terzo-do-seculo-xv/
- https://gl.wikipedia.org/wiki/Castelo_da_Rocha_Forte
- https://gl.wikipedia.org/wiki/Irmandi%C3%B1os
- https://gl.wikipedia.org/wiki/Gran_Guerra_Irmandi%C3%B1a
- https://www.despertaferro-ediciones.com/2020/revuelta-gran-guerra-irmandina-galicia-1467-1469/
- https://es.wikipedia.org/wiki/Alfonso_de_Castilla
- https://es.wikipedia.org/wiki/Gran_Guerra_Irmandi%C3%B1a [huida a Castilla y a Portugal; tribunal final, 2.ª ronda; F-sec]
- https://academia.gal/dicionario/-/termo/busca/durmir [DRAG: *durmir*, intransitivo y transitivo]
- https://academia.gal/dicionario/-/termo/busca/parte [DRAG: *parte*, sin locución con "todas partes"]

### B.4 Voz: modelos, licencias, tarifas, protocolo y sector (pieza "voz")

- https://huggingface.co/datasets/proxectonos/Nos_Brais-GL [mercado]
- https://huggingface.co/datasets/proxectonos/Nos_Celtia-GL [mercado]
- https://huggingface.co/api/models?author=proxectonos [pipeline]
- https://huggingface.co/proxectonos/Nos_TTS-sabela-vits-phonemes
- https://github.com/gas/pronunza-tts-galego-onnx-colab
- https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts
- https://learn.microsoft.com/en-us/dotnet/api/microsoft.cognitiveservices.speech.speechsynthesisoutputformat
- https://docs.cloud.google.com/text-to-speech/docs/gemini-tts
- https://elevenlabs.io/docs/overview/models
- https://elevenlabs.io/blog/eleven-v3
- https://developers.openai.com/api/docs/guides/text-to-speech
- https://github.com/rany2/edge-tts
- https://learn.microsoft.com/en-us/answers/questions/2392491/unofficial-edge-tts-api
- https://prices.azure.com/api/retail/prices
- https://azure.microsoft.com/en-us/pricing/details/speech/
- https://cloud.google.com/text-to-speech/pricing
- https://costgoat.com/pricing/openai-tts
- https://www.cronoshare.com/cuanto-cuesta/locucion
- https://www.locutortv.es/presupuestos_y_tarifas.htm
- https://www.locutortv.es/locutores_gallegos-locutor.htm
- https://voicebros.com/en/voice-over-rates
- https://learn.microsoft.com/en-us/answers/questions/5779941/permissions-to-use-clipchamp-ai-text-to-voice-for
- https://elevenlabs.io/docs/eleven-creative/voices/payouts
- https://www.milenio.com/negocios/que-debe-contener-un-contrato-para-licenciar-una-voz-a-ia
- https://ilg.usc.es/pronuncia/ [pipeline]
- https://github.com/yl4579/StyleTTS2/blob/main/Demo/Inference_LibriTTS.ipynb
- https://elevenlabs.io/docs/api-reference/text-to-speech/convert
- https://github.com/sarulab-speech/UTMOSv2
- https://www.runpod.io/pricing [pipeline]
- https://www.agpti.org/
- https://github.com/yl4579/StyleTTS2
- https://elevenlabs.io/docs/product-guides/voices/voice-cloning/professional-voice-cloning
- https://www.nosdiario.gal/articulo/social/mesa-agpti-ada-denuncian-incumprimentos-rtve-coa-programacion-galego/20260220110723248001.html [mercado]
- https://en.wikipedia.org/wiki/MUSHRA
- https://openresearchsoftware.metajnl.com/articles/10.5334/jors.187
- https://tragoratraducciones.com/locutores-gallegos/
- https://anyvoz.com/locutores-gallegos/
- https://huggingface.co/mozilla-ai/whisper-large-v3-gl
- https://github.com/m-bain/whisperx
- https://huggingface.co/proxectonos/w2v-bert-2.0-gl
- https://arxiv.org/abs/2503.23542
- https://huggingface.co/proxectonos/Nos_ASR-wav2vec2-large-xlsr-53-gl-with-lm
- https://huggingface.co/proxectonos/Nos_TTS-icia-vits-phonemes
- https://huggingface.co/proxectonos/Nos_TTS-iago-vits-phonemes
- https://huggingface.co/proxectonos/Nos_TTS-paulo-vits-phonemes

### B.5 Pipeline: precios, código, cómputo y políticas (pieza "pipeline")

- https://ai.google.dev/gemini-api/docs/deprecations
- https://developers.google.com/youtube/v3/docs/videos/insert
- https://gitlab.com/trasno/hunspell-gl
- https://huggingface.co/proxectonos/CarvalhoChat_GEC
- https://huggingface.co/proxectonos/whisper-large-v3-turbo-gl-v1.0
- https://huggingface.co/proxectonos/stt_gl_conformer_ctc_large_v1.0
- https://github.com/NVIDIA/NeMo/tree/main/tools/nemo_forced_aligner
- https://github.com/hexgrad/kokoro/blob/main/kokoro/model.py
- https://docs.pytorch.org/docs/stable/notes/randomness.html
- https://www.sqlite.org/fts5.html
- https://rapidfuzz.github.io/RapidFuzz/Usage/distance/Levenshtein.html
- https://ai.google.dev/gemini-api/docs/pricing
- https://claude.com/pricing
- https://colab.research.google.com/signup
- https://research.google.com/colaboratory/faq.html
- https://docs.runpod.io/runpodctl/reference/runpodctl-create-pod
- https://wyzowl.com/epidemic-sound-review/
- https://www.epidemicsound.com/our-plans/creator-plan/
- https://blog.novadub.ai/blog/en/youtube-multi-audio-complete-guide-2026/
- https://support.google.com/youtube/answer/13338784?hl=en
- https://support.google.com/youtube/answer/1311392?hl=en [mercado]
- https://www.techtimes.com/articles/320629/20260715/youtube-wiped-35m-subscribers-over-ai-slop-now-its-judging-your-taste.htm [mercado]
- https://www.thundercompute.com/blog/colab-alternatives-for-cheap-deep-learning-in-2025
- https://huggingface.co/api/models?author=proxectonos&pipeline_tag=text-to-speech
- https://www.mediawiki.org/wiki/Wikimedia_APIs/Rate_limits

### B.6 Mercado, go-to-market, riesgos, cumplimiento y KPIs (pieza "mercado y riesgos")

- https://www.elprogreso.es/articulo/galicia/galicia-gana-8908-habitantes-llega-271-millones-2024/202512021326291928680.html
- https://www.que.es/2025/10/24/podcasts-vida-cotidiana-espanoles
- https://prensa.ivoox.com/2025/09/30/el-podcast-se-consolida-como-habito-diario-en-espana-8-de-cada-10-espanoles-escuchan-podcasts-y-lo-convierten-en-un-canal-de-confianza-para-las-marcas/
- https://radiogalegapodcast.gal/categorias/historia
- https://www.galiciaconfidencial.com/noticia/5837110-tes-interese-facer-as-probas-celga
- https://www.lingua.gal/o-galego/aprendelo/celga
- https://praza.gal/acontece/hai-xa-563-mil-galegos-no-estranxeiro-pero-so-o-23-naceu-en-galicia
- https://abertos.xunta.gal/catalogo/administracion-publica/-/dataset/0571/entidades-rexistro-galeguidade
- https://academia.gal/-/as-letras-galegas-2027-celebraran-a-xose-neira-vilas
- https://www.galiciaconfidencial.com/noticia/5945510-xose-neira-vilas-sera-autor-homenaxeado-nas-letras-galegas-2027
- https://www.nosdiario.gal/articulo/cultura/youtubeiras-lanza-novo-galardon-honorifico-traxectoria-creacion-dixital-celebrar-decima-edicion-dos-seus-premios/20260917171230267018.html
- https://support.google.com/youtube/answer/13861714?hl=en
- https://support.google.com/youtube/answer/9890437?hl=en
- https://support.google.com/youtube/answer/9314355?hl=en
- https://support.google.com/youtube/answer/9314486?hl=en
- https://support.google.com/youtube/answer/4792576?hl=en
- https://www.nosdiario.gal/articulo/social/que-non-deixala-falar-criticas-ia-empregada-pola-crtvg-recrear-begona-caamano/20260518160723256730.html
- https://www.lingua.gal/recursos/todos/_/promovelo/contido_607/nos-intelixencia-artificial-servizo-lingua-galega
- https://www.economistjurist.es/zbloque-1/ley-organica-de-ia-espana-aterriza-el-ai-act-con-aesia-sanciones-y-sandboxes/
- https://zenodo.org/records/8027725
- https://www.boe.es/buscar/act.php?id=BOE-A-1982-11196
- https://academia.gal/dicionario/-/termo/ser%C3%A1n
- https://support.google.com/youtube/answer/9314416?hl=en
- https://support.google.com/youtube/answer/9409631?hl=en
- https://support.google.com/youtube/answer/9483359?hl=en
- https://buttondown.com/pricing
- https://www.mailerlite.com/pricing
- https://mastodon.gal/api/v1/instance
- https://podgalego.agora.gal
- https://t.me/podgalego_episodios
- https://obradoirodixitalgalego.gal/
- https://www.vademecum.es/noticia-251216-la+sociedad+espa+ntilde+ola+de+neurolog+iacute+a+advierte+sobre+el+creciente+aumento+de+productos+y+servicios+sin+validez+m+eacute+dica+dirigidos+a+personas+con+insomnio+_644195
- https://support.google.com/youtube/answer/14328491?hl=en
- https://blog.youtube/news-and-events/disclosing-ai-generated-content/
- https://www.goodwinlaw.com/en/insights/publications/2026/08/alerts-technology-dpc-eu-ai-act-transparency-obligations-now-in-force
- https://www.joneswalker.com/en/insights/blogs/ai-law-blog/yes-august-2-still-matters-the-eu-approved-a-high-risk-ai-delay-but-most-trans.html?id=102nbon
- https://artificialintelligenceact.eu/article/50/
- https://artificialintelligenceact.eu/article/3/
- https://digital-strategy.ec.europa.eu/en/news/commission-publishes-code-practice-marking-and-labelling-ai-generated-content
- https://www.scl.org/european-commission-publishes-code-of-practice-on-marking-and-labelling-ai-generated-content/
- https://artificialintelligenceact.eu/article/99/
- https://www.lamoncloa.gob.es/consejodeministros/resumenes/paginas/2026/260526-rueda-prensa-ministros.aspx
- https://www.congreso.es/public_oficiales/L15/CONG/BOCG/A/BOCG-15-A-97-1.PDF
- https://learn.microsoft.com/en-us/legal/cognitive-services/speech-service/text-to-speech/transparency-note
- https://www.boe.es/buscar/act.php?id=BOE-A-1996-8930
- https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md
- https://artificialguy.com/blog/flux-licensing-commercial-use/
- https://variety.com/2026/digital/news/spotify-bans-ai-generated-podcasts-impersonate-verified-badges-1236752944/
- https://support.google.com/youtube/answer/7628154?hl=en
- https://editorialgalaxia.gal/xose-neira-vilas-sera-a-figura-homenaxeada-no-dia-das-letras-galegas-2027/
- https://usercentrics.com/knowledge-hub/eu-ai-act-high-risk-delay-article-50-transparency-consent/
- https://www.socialmediatoday.com/news/youtube-adds-title-testing-youtube-studio/753015/
- https://routenote.com/blog/youtube-expands-a-b-title-testing/
- https://en.wikipedia.org/wiki/World_Sleep_Day
- https://days.to/world-sleep-day/2027

**Datos propios y scripts** (directorio de trabajo `gauntlet/`): `model/*.py` (modelo financiero, árbol, puertas y sensibilidad); `model/obs_clonicos_29-09-2026.txt`; `crtvg/bases2025_extracto.txt` (bases de la CRTVG transcritas); `sim/*.py` (potencia de la prueba de identificación y muestreo de aceptación); `drafts/bench_cpu/*` (medida de TTS y ASR en CPU); `drafts/extrae_cita_prototipo.py`, `drafts/proba_extrae_cita.py`, `drafts/verifica_citas_prototipo.py` y `drafts/g2p_override_prototipo.py` (prototipos probados); `scratchpad/ritmo_int.py` (tabla de ritmo del §3.3).
