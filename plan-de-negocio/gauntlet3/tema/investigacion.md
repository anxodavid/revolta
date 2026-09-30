# Pieza TEMA (Gauntlet 3): qué episodio da más gancho y más audiencia, compatible con dormir

Constructor: agente de la pieza TEMA (Claude), 30-09-2026. Documento de trabajo en castellano; lo que verá u oirá el
público (títulos, ganchos) va en galego.

**Qué es automático y qué hizo Claude a mano.** Las búsquedas de YouTube (yt-dlp), los metadatos y Google Trends
(pytrends) se sacaron con scripts; las cifras de las tablas salen de esos scripts. **A mano (Claude)**: la elección de
consultas, las reglas de limpieza (qué vídeo cuenta como "narrativo sobre el tema"), la revisión de qué vídeos están en
galego, la verificación de los hechos en las fuentes, las puntuaciones y la recomendación. Ninguna persona ha revisado
este documento.

> **Recomendación (detalle en §6):** el episodio de octubre debe ser **"As meigas de verdade"**: la brujería real en
> Galicia según los papeles de la Inquisición y de la Real Audiencia, más la lenda contada como lenda, con el conxuro
> de la queimada (escrito en 1967) como arranque en frío. Gana en el ranking (39 puntos ponderados; §5) por tener los
> **ganchos verdaderos más fuertes**, una segunda mitad **serena de verdad** y el **pico de octubre** de "brujas" en
> YouTube; su punto débil es que "meigas" como palabra se busca poco. **Segundo: Camiño de Santiago** (37; el mejor dato
> "para dormir" de un tema gallego: 182.379 vistas). **Alternativa de temporada para el 1-2 de noviembre: Santa
> Compaña** (la más buscada y la más estacional, pero su público es de terror).

## 1. Método y límites

**Fuentes de datos (30-09-2026):**

| Qué | Cómo | Dónde están los datos crudos |
|---|---|---|
| Búsquedas de YouTube | yt-dlp 2026.08.19, cliente `android_vr`, `--flat-playlist`, sin descargar vídeos. **65 consultas por relevancia** (`ytsearch20:`) en gl, es, pt y en, y **18 consultas ordenadas por vistas** (filtro `sp=CAM%3D`, 20 resultados): 1.660 resultados | [`busquedas-yt.txt`](busquedas-yt.txt) (mismo formato que el del Gauntlet 2 + columna de fecha) |
| Fecha exacta de 42 vídeos clave | `yt-dlp -j --skip-download` (clientes `android_vr` y `mweb`) | final de [`busquedas-yt.txt`](busquedas-yt.txt) |
| Estacionalidad y volumen relativo | Google Trends vía pytrends: España (ES) y Galicia (ES-GA), búsqueda web y **búsqueda en YouTube**; series semanales de 5 años y mensuales largas | [`tendencias-google.txt`](tendencias-google.txt) |
| Scripts | `buscar.py`, `formatear.py`, `limpiar.py`, `trends*.py` | [`scripts/`](scripts/) |

**Limpieza (a mano, reglas en `scripts/limpiar.py`).** Para cada tema se juntan los resultados de todas sus consultas
(sin duplicados) y se cuentan solo los **vídeos narrativos sobre el tema**: documental, pódcast, lenda narrada,
explicación, reportaje, historia para dormir. Se excluyen canciones y videoclips (p. ej. Mägo de Oz, Luar na Lubre),
películas y tráilers, homónimos (el otorrino "Dr. Michael Teixido", la cantante brasileña "Maria Pita"), guías prácticas
del Camino (mochila, albergues) y vídeos de otras regiones (bruxas vascas, Salem). En "meigas" solo cuentan los vídeos
sobre Galicia; las bruxas en general van aparte como **comparables**.

**Límites (importantes para leer las cifras):**
- La búsqueda de YouTube es una **muestra** (20 resultados por consulta, sesgada por el algoritmo y por el cliente, que
  pide inglés: muchos títulos salen traducidos al inglés, pero el vídeo es el mismo).
- Las **vistas son acumuladas**: los vídeos viejos llevan ventaja. Por eso se da la antigüedad y el vídeo reciente.
  Las vistas de un mismo vídeo pueden variar unas decenas entre la tabla 2 (búsqueda) y la 3 (metadatos): se
  tomaron con horas de diferencia.
- La fecha de la búsqueda es **aproximada** (YouTube dice "hace 2 años"): error de hasta un año en los vídeos viejos.
  Las fechas exactas solo están en los 42 vídeos de la tabla 3.
- Google Trends da **índices relativos** (0-100 dentro de cada consulta), no búsquedas absolutas. Con términos pequeños
  muchas semanas salen a cero y el índice estacional es ruido (se marca).
- YouTube empezó a pedir verificación anti-bot tras ~15 consultas de metadatos completos con `android_vr`; se siguió con
  el cliente `mweb` (ver [`../aprendizajes/tema.md`](../aprendizajes/tema.md)).

## 2. Demanda en YouTube por tema (vídeos narrativos, tras la limpieza)

Columnas: **n** = vídeos narrativos únicos sobre el tema en los resultados; **>10K / >100K** = cuántos pasan de
10.000 / 100.000 vistas; **mediana** y **máximo** de vistas; **para dormir** = vídeos con formato de dormir (título o
canal con dormir/sleep/ASMR/lluvia) y su máximo; **antigüedad** = año mediano de los vídeos >10K y el >10K más
reciente; **en galego** = vídeos en galego (revisados a mano) y su máximo. Ordenado por nº de vídeos >10K.

| Tema | n | >10K | >100K | Mediana | Máximo | Para dormir | Antigüedad (año mediano >10K; >10K más reciente) | En galego |
|---|---|---|---|---|---|---|---|---|
| Camiño de Santiago | 31 | 22 | 9 | 36.835 | 474.395 (Planet Doc, 2015) https://youtu.be/iL5EB3zRFRg | 10; máx 182.373 https://youtu.be/XLIu6OW72T8 | 2025; 182.373 (2026-04) https://youtu.be/XLIu6OW72T8 | 0 |
| Santa Compaña | 44 | 15 | 7 | 3.113 | 1.839.176 (TikTak Draw, 2018) https://youtu.be/l1cwV1oCYCE | 6; máx 206.344 (terror con lluvia) https://youtu.be/cXw-N2aY23Q | 2020; 46.727 (2026-08) https://youtu.be/TchD_3COhSs | 0 |
| Queimada e conxuro | 45 | 15 | 2 | 5.172 | 210.797 (Lagarto Rojo, 2013) https://youtu.be/QONcI27KoIg | 0 | 2013; 20.055 (2022) https://youtu.be/JrDYWnqm84U | 11 (recitados del conxuro); máx 149.829 https://youtu.be/z7o44OvfwIM |
| Castros e celtas (extra) | 17 | 14 | 6 | 79.801 | 980.413 (Fundación Juan March, 2018) https://youtu.be/m8XirXeRitc | 0 | 2024; 22.670 (2026-06) https://youtu.be/XR9oFKRklUA | 0 |
| Lobishome / Romasanta | 31 | 13 | 8 | 2.257 | 1.011.932 (canal ruso, 2024) https://youtu.be/DsyIyXZlYnE | 0 | 2021; 34.634 (2025) https://youtu.be/GcTrZvvrtd4 | 0 |
| Noite de San Xoán | 17 | 8 | 2 | 8.224 | 287.145 (Alanna, 2022; San Juan en general) https://youtu.be/gLGtv9oDTto | 0 | 2022; 47.046 (2026-06) https://youtu.be/ahzco8sWwEs | 1; máx 2.938 https://youtu.be/Tftte-0ltSA |
| María Pita | 21 | 5 | 1 | 945 | 448.049 (Crónicas de la Historia, 2024) https://youtu.be/-Sq4722iH7w | 0 | 2020; 47.680 (2026-07) https://youtu.be/cr3J3j4MPI8 | 0 |
| Costa da Morte (extra) | 14 | 5 | 0 | 2.326 | 31.822 (Mega Buques, 2019) https://youtu.be/SvTTBhlwcvk | 0 | 2019; 11.113 (2020) https://youtu.be/KfAZ2h49qVw | 0 (1 corto de 523 en "xeral") |
| **Meigas / bruxería (Galicia)** | 52 | 3 | 0 | 508 | 69.936 (Cuarto Milenio, subido el 23-08-2026) https://youtu.be/x4cwzm5IKmw | 1; máx 173 https://youtu.be/hjpHxrf5A6M | 2025; 69.936 (2026-08) https://youtu.be/x4cwzm5IKmw | 2; máx 1.578 https://youtu.be/zSmLrnJm75g |
| Santo André de Teixido (extra) | 18 | 3 | 0 | 1.237 | 43.154 (2016) https://youtu.be/THESeoQ1vBg | 0 | 2016; 14.603 (2021) https://youtu.be/YAANo1rdv-E | 1; máx 1.899 https://youtu.be/98k5ggXIIGQ |
| Samaín (galego) | 21 | 2 | 0 | 2.000 | 14.902 (Suso Souto, 2017) https://youtu.be/IOxGboP7V1k | 0 | 2019; 10.091 (TVG, 31-10-2020) https://youtu.be/0uOZUEFTHPo | 6; máx 10.091 https://youtu.be/0uOZUEFTHPo |
| Muiñeira / gaita (narrativo) | 11 | 1 | 1 | 3.541 | 415.097 (ARTE, 2025) https://youtu.be/UgNeHf0xQyw | 0 | 2025; 415.097 (2025) https://youtu.be/UgNeHf0xQyw | 7 (TVG, TradiGaita); máx 7.934 https://youtu.be/O8geUBOoZ18 |
| Mouras e tesouros dos castros | 33 | 1 | 0 | 389 | 10.608 (ab origine, 2021) https://youtu.be/8j1VNZk4nig | 0 | 2021; 10.608 (2021) https://youtu.be/8j1VNZk4nig | 7; máx 1.714 https://youtu.be/cBknUDdol0E |
| Galeóns de Rande | 24 | 1 | 0 | 734 | 29.854 (Batallas Navales, 26-10-2025) https://youtu.be/rbIRFeLiokQ | 0 | 2025; 29.854 (2025-10) https://youtu.be/rbIRFeLiokQ | 4 pequeños (máx 990) https://youtu.be/yNxZed3Cn5g |
| Magosto (extra) | 5 | 0 | 0 | 1.040 | 7.479 (Turismo de Galicia, 2018) https://youtu.be/XzmW3XpRzaE | 0 | - | 0 |

Notas de lectura:
- **Muiñeira**: la demanda real es **musical**, no narrativa (la "Muiñeira de Chantada" de Carlos Núñez y The
  Chieftains tiene 3.222.769 vistas, https://youtu.be/uJ1ynTMUj0c); como relato para dormir apenas hay nada.
- **Queimada**: la demanda es de **recitados del conxuro** y recetas, casi toda de 2007-2013 (año mediano 2013).
- **Romasanta y Costa da Morte**: la demanda es de **crimen y naufragio** (true crime, "Draw My Life", pódcast de
  terror), mal casada con dormir.
- **Samaín**: las cifras grandes son del **Samhain irlandés/celta** en general (p. ej. 338.217,
  https://youtu.be/2Enjdd2arqs); del Samaín galego, lo máximo es un corto de la TVG (10.091).
- **Meigas**: poca oferta y pocas vistas específicas de Galicia, pero **demanda adyacente enorme** en castellano
  (brujas, tabla 3) y una señal reciente fuerte: el programa de *Cuarto Milenio* "Las últimas brujas de Galicia" hizo
  69.964 vistas en 5 semanas en un canal de resubidas de 15.700 suscriptores.
- **En galego no hay nada para dormir en ningún tema**: lo que hay en galego son cortos (TVG, politicalinguistica) y
  **cuentos infantiles** (p. ej. Taxi Roberto Burela, 110.180 vistas, https://youtu.be/CfzEpFwj1_E). Mismo resultado que
  en el Gauntlet 2.

## 3. Referencias clave con fecha exacta (formato para dormir, lendas y brujas)

| Vídeo | Canal (suscr.) | Subido | Vistas a 30-09-2026 | Duración | Lectura |
|---|---|---|---|---|---|
| "DUÉRMETE CON las Leyendas Más Antiguas y Misteriosas de GALICIA" https://youtu.be/ij7nuBjh1PQ | Relatos al Oído (66.000) | **09-10-2025** | 108.105 | 2 h 01 min | El listón del nicho: lendas de Galicia para dormir, en castellano, **publicado en octubre**. Es su 3.er vídeo más visto de los encontrados |
| "Duérmete con HISTORIAS y LEYENDAS olvidadas de España" https://youtu.be/Bisff-SGAh0 | Relatos al Oído | 21-08-2025 | 155.506 | 1 h 34 min | El más visto del canal en la muestra |
| "DUÉRMETE con LEYENDAS REALES de BRUJAS de ESPAÑA" https://youtu.be/1hFkW_rACQ8 | Relatos al Oído | 14-08-2025 | 36.121 | 1 h 11 min | Brujas en formato para dormir: funciona, pero menos que las lendas de Galicia |
| "DUÉRMETE CON LA HISTORIA OCULTA DE LUGO" https://youtu.be/bPTZWLWZJf8 | Relatos al Oído | 26-09-2026 | 9.233 en 4 días | 1 h 29 min | El competidor sigue activo con Galicia |
| "Camino de Santiago: Mil Doscientos Años de Fe, Cultura y Transformación Humana" https://youtu.be/XLIu6OW72T8 | Grandes Relatos para Dormir (20.800) | 02-04-2026 | 182.379 | 39 min | El mejor dato "para dormir" de un tema gallego, en un canal pequeño |
| "Ánimas del Purgatorio, Santa Compaña y Genti di Muerti" https://youtu.be/cXw-N2aY23Q | Noche de Lluvia Podcast (432.000) | **15-10-2024** | 206.343 | 1 h 11 min | Terror con lluvia de fondo; **publicado en octubre** |
| "La Santa Compaña: el misterio gallego que une la vida y la muerte" https://youtu.be/HiIs26_3adw | Historias antes de dormir | 25-10-2025 | 6.036 | 1 h 22 min | La Santa Compaña **en formato para dormir rinde poco** |
| "LEYENDAS DE GALICIA 🌙 Cuentos de la Santa Compaña para Calmar la Mente" https://youtu.be/BOEOz6yLI2I | El Pergamino Mágico (16.700) | 03-05-2026 | 5.141 | 1 h 27 min | Idem |
| "La Santa Compaña: El Camino de los Muertos (Leyenda Gallega de Terror)" https://youtu.be/TchD_3COhSs | SAGA-TV España (1.300) | 29-08-2026 | 46.734 en 1 mes | 18 min | Empuje reciente del algoritmo a la Santa Compaña **como terror** |
| "CUARTO MILENIO / Las Últimas Brujas de Galicia" https://youtu.be/x4cwzm5IKmw | Doctor Siniestro (15.700) | 23-08-2026 | 69.964 en 5 semanas | 1 h 58 min | Señal reciente para **meigas** |
| "Diez leyendas gallegas sobre almas, meigas y caminos nocturnos" https://youtu.be/FI4IUrLtQeA | Cofre de Leyendas (61.200) | 11-11-2025 | 14.980 | 45 min | Lendas de Galicia narradas, publicado en la temporada de difuntos |
| "ESPECIAL DE NOCHE DE BRUJAS 2025 (RELATOS DE TERROR)" https://youtu.be/1DzRUG5JnoA | Relatos de la Noche (2,4 M) | **31-10-2025** | 817.728 | 1 h 00 min | Comparable: "bruxas" + Halloween en castellano |
| "What REALLY happened during the Salem Witch Trials" https://youtu.be/hwfHJp05KdI | Sleepless Historian | 31-10-2025 | 39.863 | 1 h 49 min | Comparable en inglés: juicios de brujas para dormir, publicado en Halloween |
| "Bruxas: da construção do mito ao controle social — História para dormir com som de chuva" https://youtu.be/Rbn3yZHh20k | Contando Carneiros | 14-02-2026 | 6.178 | 2 h 00 min | Comparable en portugués: historia real de las bruxas para dormir |
| "Desmontando Mitos: A queimada; así se inventou unha tradición" https://youtu.be/RSG68gQSktE | GCiencia (1.510) | 13-02-2021 | 6.824 | 4 min | En galego: el "mito" de la queimada ya interesa |

Comparables en castellano de "bruxas" (sin ser de Galicia): pódcast de terror de 1,8-2,3 M vistas
(https://youtu.be/JaciBwcAvcQ, https://youtu.be/09cGfnUjCQU) y "El terrible caso de las brujas de Zugarramurdi"
(Flisflisher, 129.778, https://youtu.be/Qhw81b8LtIE). **La brujería histórica española tiene público de sobra**;
lo que falta es la versión galega, verdadera y para dormir.

## 4. Google Trends: volumen relativo y estacionalidad (octubre)

Datos completos y método en [`tendencias-google.txt`](tendencias-google.txt). **Índice de octubre** = búsquedas medias
de octubre / media del año (> 1: se busca más en octubre). Serie mensual 2019-2026 cuando el término tiene volumen; si
no, semanal de 5 años (marcado).

| Término | Vol. relativo en YouTube, España (Santa Compaña = 2,9; 5 años) | Índice oct. web España | Índice oct. YouTube España | Índice oct. web Galicia | Mes pico | Lectura |
|---|---|---|---|---|---|---|
| Camino de Santiago | 135,5 | 0,77 | 0,80 | 1,03 | agosto | Enorme y **de verano** |
| muiñeira | 47,2 | 0,86 (5a) | 0,93 (5a) | 0,98 (5a) | mayo | Grande en YouTube, pero **es música** |
| queimada | 4,3 | 1,07 | 1,16 | 0,97 | junio (San Xoán) | Estable, no de octubre |
| **Santa Compaña** | 2,9 | **2,26** | **2,39** | **3,23** | **octubre** | El término gallego **más estacional de octubre** con volumen |
| magosto | 2,5 | 5,0 (5a, 74 % ceros) | 2,8 (5a, 95 % ceros) | 4,7 (5a) | noviembre | Pico de noviembre |
| meigas | 0,4 | 1,14 | 0,93 (58 % ceros) | 1,14 | agosto/junio | El término "meigas" **no** es estacional y en YouTube es pequeño (≈ 1/4-1/7 de Santa Compaña) |
| **brujas** (comparable) | ≈ 34 × Santa Compaña (lote aparte) | **1,69** | **1,99** | **1,82** | **octubre** | Término enorme y **de octubre** (Halloween = "noche de brujas") |
| Samaín | 0,3 | 10,4 (79 % ceros) | 13,1 (93 % ceros) | 11,0 (84 % ceros) | octubre | Casi solo se busca en torno al 31 de octubre, y con poco volumen |
| María Pita | 0,4 | 0,45 (5a, 39 % ceros) | - | 0,06 (5a) | agosto | Nada de octubre |
| Romasanta | 0,2 | 1,13 (5a, 65 % ceros) | - | - | enero | Pequeño |
| batalla de Rande | 0,1 | ruido (94 % ceros) | - | - | - | Muy pequeño (aniversario: 23-10-1702) |
| San Xoán | 0,1 | 0,0 (5a) | - | - | junio | Fuera de temporada |
| mouras, María Soliña, San Andrés de Teixido, "brujas gallegas", "leyendas gallegas" | ≤ 0,1 | ruido | - | - | - | Sin volumen medible |

Lectura: en octubre **suben "Santa Compaña" (× 2,3-3,2) y "brujas" (× 1,7-2,4)**; "meigas" y "queimada" no se mueven.
En volumen de YouTube España, de los temas gallegos de folclore solo "Santa Compaña" y "queimada" tienen algo; "meigas"
es pequeño como palabra de búsqueda, pero "brujas" es enorme y de octubre.

## 5. Puntuación (1-5) y ranking

Criterios del encargo: **D** demanda medida (§2-§4); **G** gancho verdadero para los primeros 60-120 s; **S**
compatibilidad con dormir (sin terror ni violencia explícita; segunda mitad serena posible); **V** riqueza visual con
iconografía galega y poco riesgo de imágenes absurdas; **F** fuentes fiables accesibles; **I** identidad galega y
afinidad con "Cousas de Galiza"; **E** estacionalidad de octubre. **Ponderada** = suma con D y G contados dos veces,
porque el objetivo es "más gancho y más audiencia". Regla para D (a mano, sobre la tabla 2): 5 = ≥ 10 vídeos > 10 K y
≥ 5 > 100 K; 4 = ≥ 10 > 10 K; 3 = 5-9 > 10 K; 2 = 1-4 > 10 K; 1 = ninguno.

| # | Tema | D | G | S | V | F | I | E | Suma | Ponderada |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Meigas: historia real + lenda** | 3* | 5 | 4 | 5 | 5 | 5 | 4 | **31** | **39** |
| 2 | Camiño de Santiago | 5 | 4 | 5 | 4 | 5 | 3 | 2 | 28 | 37 |
| 2 | Queimada e conxuro | 4 | 5 | 4 | 3 | 4 | 5 | 3 | 28 | 37 |
| 4 | Santa Compaña | 5 | 3 | 2 | 3 | 4 | 5 | 5 | 27 | 35 |
| 5 | Santo André de Teixido (extra) | 2 | 4 | 4 | 5 | 4 | 5 | 2 | 26 | 32 |
| 5 | Castros e celtas (extra) | 5 | 3 | 4 | 3 | 3 | 4 | 2 | 24 | 32 |
| 7 | Lobishome / Romasanta | 5 | 4 | 1 | 2 | 4 | 3 | 3 | 22 | 31 |
| 7 | Costa da Morte (extra) | 3 | 4 | 2 | 4 | 4 | 5 | 2 | 24 | 31 |
| 9 | Mouras e tesouros dos castros | 2 | 2 | 5 | 4 | 4 | 5 | 2 | 24 | 28 |
| 9 | Galeóns de Rande | 2 | 4 | 3 | 3 | 4 | 3 | 3 | 22 | 28 |
| 9 | Noite de San Xoán | 3 | 3 | 3 | 4 | 4 | 4 | 1 | 22 | 28 |
| 12 | Magosto (extra) | 1 | 2 | 5 | 4 | 3 | 5 | 4 | 24 | 27 |
| 12 | Samaín | 2 | 3 | 3 | 2 | 3 | 4 | 5 | 22 | 27 |
| 14 | María Pita | 3 | 3 | 2 | 2 | 4 | 4 | 1 | 19 | 25 |
| 14 | Muiñeira / gaita | 2 | 2 | 3 | 3 | 4 | 5 | 2 | 21 | 25 |

\* **Meigas, D = 3 en vez de 2** por demanda adyacente: por la regla estricta tendría 2 (solo 3 vídeos gallegos > 10 K),
pero "brujas" es ≈ 34 veces "Santa Compaña" en YouTube España y sube × 2,0 en octubre, y la historia real de brujas ya
funciona en formato para dormir (tabla 3). Que ese público llegue a un vídeo en galego es un **supuesto [S]**.
**Sensibilidad:** con D = 2, meigas queda en 30 / 37 y **empata** con Camino y queimada; gana el desempate por
estacionalidad (4 frente a 2 y 3) y compatibilidad con dormir. Sin ponderar, gana igual (31 o 30 frente a 28).

**Justificación por tema** (gancho de ejemplo verificado entre paréntesis):
- **Meigas**: D 3 (tabla 2: 3 vídeos > 10 K, máx. 69.964 en 5 semanas; demanda adyacente enorme); G 5 (actas reales
  con detalles sorprendentes y cifras contraintuitivas, §8); S 4 (hay tortura y una hoguera en la historia: se nombran
  una vez y sin detalle; la meiga como curandeira y parteira da una segunda mitad tranquila); V 5 (lareira, candeas,
  fontes, hórreos, carballeiras, herbas, papeles de archivo; luz variada); F 5 (Arquivo do Reino de Galicia con
  transcripciones, Consello da Cultura Galega, historiador de la UVigo/USC); I 5; E 4 ("brujas" × 1,7-2,4 en octubre,
  aunque "meigas" no sube).
- **Camiño de Santiago**: D 5 (22 vídeos > 10 K; 182.379 en formato para dormir); G 4 (el *Códice Calixtino*, del
  s. XII, lo robó en 2011 un electricista que trabajó 25 años en la catedral y apareció en 2012 en un garaje del
  Milladoiro: https://gl.wikipedia.org/wiki/Códice_Calixtino); S 5; V 4 (riesgo de paisaje genérico de España); F 5;
  I 3 (es más europeo y católico que "cousa de Galiza"); E 2 (pico en agosto; octubre × 0,8).
- **Queimada**: D 4 (15 > 10 K, pero de 2007-2013); G 5 (conxuro de 1967, §8); S 4; V 3 (fuego y pota de barro durante
  30 min se repiten); F 4; I 5; E 3 (pico en junio, San Xoán). **Se integra en el episodio de meigas como arranque en
  frío**, así que su demanda también se aprovecha.
- **Santa Compaña**: D 5 (15 > 10 K, 7 > 100 K; pico de octubre × 2,3-3,2); G 3 (es lenda; lo verificable es
  etnográfico o literario; que aparezca en documentos de la Inquisición del s. XVI-XVII lo dice Galipedia,
  https://gl.wikipedia.org/wiki/Santa_Compaña, sin fuente primaria comprobada); S 2 (procesión de muertos que anuncia
  la muerte: su público es de terror; en formato para dormir hace 5-6 K frente a 100-200 K en terror); V 3 (procesiones
  encapuchadas en la niebla = la composición repetida que penalizó el juez del Gauntlet 2); F 4; I 5; E 5.
- **Santo André de Teixido**: D 2; G 4 ("vai de morto quen non foi de vivo"; primera mención en un testamento de
  Viveiro de 1391: https://gl.wikipedia.org/wiki/Santo_André_de_Teixido); S 4; V 5 (acantilados, santuario, mar); F 4;
  I 5; E 2. Buen tema para otro episodio.
- **Castros e celtas**: D 5 (14 > 10 K, sobre todo "celtas" en general); G 3 (el celtismo está discutido y los
  "ganchos" que circulan son de clic fácil, p. ej. "40.000 años de ADN celta"); S 4; V 3 (riesgo de druidas y
  Stonehenge genéricos); F 3; I 4; E 2.
- **Romasanta**: D 5 (13 > 10 K, 8 > 100 K); G 4 (Isabel II le conmutó la pena de muerte en 1854 tras la carta de un
  médico francés que alegaba licantropía clínica: https://gl.wikipedia.org/wiki/Manuel_Blanco_Romasanta); **S 1**
  (nueve asesinatos probados; es *true crime*); V 2; F 4; I 3; E 3.
- **Costa da Morte**: D 3; G 4 (naufragio del *HMS Serpent* el 10-11-1890: 172 muertos y 3 supervivientes;
  https://gl.wikipedia.org/wiki/HMS_Serpent_(1887)); S 2 (tragedias); V 4; F 4; I 5; E 2.
- **Mouras**: D 2 (máx. 10.608); G 2 (no encontré un dato verdadero que sorprenda en 10 s); S 5; V 4; F 4; I 5; E 2.
- **Rande**: D 2; G 4 (Jules Verne llevó los tesoros de Rande a *Vinte mil leguas*; la batalla fue el 23-10-1702:
  https://gl.wikipedia.org/wiki/Batalla_de_Rande); S 3 (batalla naval); V 3 (galeones de IA con aparejos imposibles);
  F 4; I 3; E 3 (aniversario en octubre, pero volumen ínfimo).
- **San Xoán**: D 3 (demanda de San Juan en general); G 3; S 3; V 4; F 4; I 4; **E 1** (junio).
- **Magosto**: D 1; G 2; S 5; V 4; F 3; I 5; E 4 (pico en noviembre).
- **Samaín**: D 2 (el Samaín galego: máx. 10.091, TVG); G 3 (lo verdadero es que su recuperación empezó en los años
  noventa en Cedeira: https://gl.wikipedia.org/wiki/Samaín; eso desinfla el gancho "Halloween es gallego"); S 3; V 2
  (calabazas = iconografía de Halloween americano); F 3; I 4; E 5.
- **María Pita**: D 3; G 3 (se casó cuatro veces; la frase "Quen teña honra, que me siga" es solo tradición:
  https://gl.wikipedia.org/wiki/María_Pita); S 2 (asedio y batalla); V 2 (multitudes: caras deformes); F 4; I 4; E 1.
- **Muiñeira**: D 2 (la demanda es musical); G 2 (el nombre viene de "muíño"; del baile antiguo casi no hay
  documentación: https://gl.wikipedia.org/wiki/Muiñeira); S 3; V 3 (manos, pies y gaitas deformes); F 4; I 5; E 2.

## 6. Recomendación: "As meigas de verdade"

**Tema y ángulo.** Quiénes eran de verdad las meigas en Galicia, contado desde **los papeles que se conservan**
(procesos de la Inquisición de Santiago y de la Real Audiencia de Galicia) y, en la segunda mitad, desde **la lenda y
la costumbre, contadas como lenda** ("din que", "contaban"). El tono pasa de la sorpresa ("non vas crer o que
declaraban as testemuñas") a la calma: la meiga no era la bruja de los cuentos, sino la **curandeira, la parteira, la
que sabía de herbas**, y Galicia, "terra de meigas", **quedó al margen de la gran caza de brujas europea**. La
**queimada** entra como arranque en frío: el conxuro que todos creen ancestral se escribió en Vigo en 1967.

**Por qué este y no otro (cifras):**
1. **Gancho**: es el tema con **más ganchos verdaderos, documentados y sorprendentes** (cinco en §8, y tres de reserva), sacados de actas
   reales publicadas por el Arquivo do Reino de Galicia. Justo lo que pidió el promotor ("non vas crer o que facían as
   persoas daquela") y lo que le faltó a la muestra anterior.
2. **Audiencia**: "brujas" es un término enorme en YouTube España (≈ 34 × "Santa Compaña") que **sube × 2,0 en
   octubre**; la historia real de brujas ya funciona para dormir (Relatos al Oído 36.121, Sleepless Historian 39.863,
   Contando Carneiros 6.178); hay señal reciente sobre Galicia (*Cuarto Milenio*, 69.964 en 5 semanas), y el listón del
   nicho, las lendas de Galicia para dormir (108.105), **se publicó un 9 de octubre**. **En galego no hay nada**: ni de
   meigas ni para dormir.
3. **Dormir**: la segunda mitad sale serena sin forzarla (herbas, fontes, lareira, noche de San Xoán, un fraile
   escribiendo a la luz de una vela). Con la Santa Compaña cuesta y con Romasanta es imposible.
4. **Imagen**: la iconografía gallega aparece sola (aldeas de granito y lousa, hórreos, lareiras, fontes, carballeiras,
   soportales de Compostela) con **luz variada** (lumbre y vela frente a niebla azul, hogueras de San Xoán, amanecer), lo
   que corrige la luz plana de la ronda 3.
5. **Encargo**: "meigas" es el primer tema que citó el promotor, y el reclamo "Cousas de Galiza" le va como anillo al
   dedo.
6. **Calendario**: octubre ("noite de bruxas") y un aniversario redondo y verdadero dentro del episodio: **Feijoo nació
   el 8-10-1676** (350 años el 8-10-2026: https://gl.wikipedia.org/wiki/Benito_Xerónimo_Feijoo).

**Punto débil (sin maquillar).** "meigas" como palabra se busca poco (en YouTube España, ≈ 1/4-1/7 de "Santa
Compaña") y no sube en octubre; los vídeos gallegos de meigas tienen pocas vistas (3 pasan de 10 K). **Mitigación**:
"meigas" en el título con una promesa de historia real, "bruxas" en la descripción y los capítulos, y, **si el promotor
lo aprueba** (no decidido), título y descripción traducidos al castellano como puerta de entrada ("Las meigas de
verdad…") [S]. Expectativa realista: con un canal nuevo en galego, cientos o pocos miles de vistas [S].

**Publicación.** Entre el **8 y el 17 de octubre** [S]: deja 2-3 semanas para acumular antes del pico de Halloween y
coincide con cuando publicaron sus éxitos Relatos al Oído (9-10-2025), Crónicas de la Historia (12-10-2025) y Noche de
Lluvia (15-10-2024). El 8 de octubre coincide con el aniversario de Feijoo.

**Segundo candidato: Camiño de Santiago** (37). Es el mejor tema "para dormir" medido (182.379 vistas en un canal de
20.800 suscriptores) y es de fondo de catálogo, pero no de octubre. **Alternativa de temporada: Santa Compaña** para el
1-2 de noviembre (Defuntos), si se acepta contar una lenda de terror en tono sereno; tiene la mayor demanda y el pico de
octubre-noviembre, pero en formato para dormir rinde poco (5-6 K) y exige vigilar la imagen (procesiones repetidas).

## 7. Título de trabajo (galego, con el reclamo)

1. **"As meigas de verdade: o que contan os papeis da Inquisición | Cousas de Galiza para durmir"** (principal: promesa
   de verdad + documento; 90 caracteres, bajo el límite de 100).
2. "Por que en Galicia case non se queimaron meigas? | Cousas de Galiza para durmir" (pregunta contraintuitiva y
   verdadera: una sola condenada a la hoguera por la Inquisición de Santiago; "case" cubre las fuentes que hablan de
   "algúns casos").
3. "Habelas, hainas: a historia real das meigas galegas | Cousas de Galiza para durmir" (la frase que todos conocen).

En la lista de YouTube solo se ven ~60-70 caracteres: lo primero es el gancho y el reclamo puede quedar cortado; el
reclamo va también en la miniatura (opcional) y al principio de la descripción. Fechas y cifras de los títulos: todas
verificadas en §8.

## 8. Ganchos verdaderos para el primer minuto (con fuente)

Todos se dicen como **hechos documentados** y con su atribución ("segundo contou unha testemuña", "confesou"), nunca
como si el narrador lo supiera de primera mano. Las cifras van en letra en el guion (Cotovía).

| # | Gancho (texto público, galego) | Fuente | Notas |
|---|---|---|---|
| 1 | «*Mouchos, curuxas, sapos e bruxas…* Seguramente oíches este conxuro nunha queimada e pensas que é antiquísimo. Non o é: escribiuno en Vigo, en 1967, Mariano Marcos Abalo, para unha festa nun barco amarrado no porto.» | https://gl.wikipedia.org/wiki/Queimada (cita a *La Voz de Galicia*, 19-10-2008); *Atlántico Diario*, 7-2-2022: https://www.atlantico.net/articulo/vigo/conxuro-queda-padre-fallece-vigo-mariano-marcos/20220207232642892177.html | El conxuro tiene **propiedad intelectual registrada** (2001; el autor murió en 2022): citar solo el primer verso, con autoría. "curuxa" es la forma normativa (RAG), aunque el texto popular diga "coruxas". Galipedia añade que el origen celta de la queimada es imposible (el alambique llegó en la Edad Media; Alonso del Real, *Grial*, 1972) |
| 2 | «Segundo o Arquivo do Reino de Galicia, entre 1574 e 1700 a Inquisición de Santiago procesou por bruxería noventa e dúas mulleres e corenta e oito homes, e só levou unha á fogueira. Mentres noutras terras de Europa ardían as fogueiras, Galicia, a terra das meigas, quedou á marxe da caza de bruxas.» | Arquivo do Reino de Galicia (Xunta), exposición "Meigas, feitizos das menciñeiras", 2020, p. "Galicia: a Inquisición e a Real Audiencia": https://arquivosdegalicia.xunta.gal/sites/default/files/arquivos_artividades/expo_mulleres_2020_01_C.pdf | **No decir el año** de la única hoguera: el Arquivo dice 1627; *El Español* (citando a Diego Valor Bravo) dice María Rodríguez, 30-11-1579: https://www.elespanol.com/mujer/mujeres-historia/20210309/verdad-caza-meigas-perseguidas-justicia-ordinaria-inquisicion/564444343_0.html. El CCG habla de condenas a la hoguera cumplidas "nalgúns casos" (https://consellodacultura.gal/album-de-galicia/detalle.php?persoa=29953): el dossier debe resolverlo; mientras, "case ningunha" es la forma segura |
| 3 | «En Vilalba, en 1617, unha testemuña declarou que a parteira Dorotea do Barro dicía que lle podía quitar as dores do parto a unha muller e pasarllas a un home: abondaba con calzarlle a el os zapatos dela e dicir unhas palabras. E que o home saltaría coma un poldro bravo.» | Mismo PDF del Arquivo do Reino, proceso de Dorotea do Barro e María do Barro (Real Audiencia de Galicia, 1617, sig. 19602/96), testimonio de Andrés da Pena | Divertido, cotidiano y sin violencia: el mejor "non vas crer". El extracto publicado no deja del todo claro si la parteira es Dorotea (la madre) o María (la hija, acusada también de "alcaiota"); el dossier debe confirmarlo en el expediente o decir "unha das acusadas, parteira" |
| 4 | «En 1639, en Boborás, María Cibreira confesou —despois de ser torturada— que as noites de San Xoán e as do primeiro de maio as meigas ían ás xuntanzas do demo… nas areas de Sevilla.» | Mismo PDF (María Cibreira e outras, Real Audiencia, 1639, sig. 24667/29); *GCiencia*, 26-01-2026: https://www.gciencia.com/retro/a-persecucion-das-bruxas-na-galicia-de-hai-400-anos-eran-apreciadas-e-necesarias-para-o-pobo/ | La tortura se nombra y no se describe (el PDF detalla los garrotes: no usarlos) |
| 5 | «Na Galicia de hai catrocentos anos, a meiga non era a bruxa dos contos: era a que curaba, a que axudaba a parir, a que sabía de herbas. "Figuras apreciadas e necesarias para o pobo", resume o historiador Rodrigo Pousa.» | *GCiencia*, 26-01-2026 (enlace de arriba); CCG, Álbum de Galicia, "Meigas" (Anxos Sumai, 2007): https://consellodacultura.gal/album-de-galicia/detalle.php?persoa=29953 | Es el giro que abre la bajada hacia el tono de dormir |

**De reserva** (para el cuerpo o el cierre):
- R1. «Aínda en 1826, en Compostela, unha adiviña, Benita Montero, foi condenada a saír do cárcere emplumada e montada
  nunha besta, un día de mercado, coa baralla colgada do pescozo.» Fuente: mismo PDF (Real Audiencia, 1826, sig.
  49054/5).
- R2. «O 8 de outubro de 2026 fai 350 anos que naceu en Casdemiro o frade Benito Xerónimo Feijoo, "o desenganador das
  Españas", que pasou a vida escribindo contra as supersticións.» Fuente:
  https://gl.wikipedia.org/wiki/Benito_Xerónimo_Feijoo
- R3. «A frase "eu non creo nas meigas, pero habelas, hainas" atribúese ás veces ao Quixote. Non está nel.» Fuente:
  búsqueda en el texto completo del *Quijote* (Project Gutenberg, https://www.gutenberg.org/cache/epub/2000/pg2000.txt,
  0 apariciones; comprobación hecha por Claude con `grep`). Su origen **no** está documentado: no afirmar que sea
  gallega (Ciberdúvidas solo dice que se le "atribuye" origen gallego:
  https://ciberduvidas.iscte-iul.pt/consultorio/perguntas/a-frase-eu-nao-acredito-em-bruxas-mas/16796).

## 9. Miniatura (concepto)

- **Una sola imagen con la tesis del título**, como la de Versalles: **la curandeira querida y el papel que la
  acusa**. Interior de una casa de **granito** de noche; una **mujer mayor** (menciñeira) sentada junto a la
  **lareira**, luz cálida de lumbre y candea en la cara de perfil, un **manojo de herbas** en las manos; en primer plano,
  sobre una mesa de castaño, un **papel doblado con sello de lacre** (el proceso); por una ventana pequeña, **niebla
  azul** y la silueta de un **hórreo**. Contraste ámbar/azul; plano medio (evita caras deformes).
- Texto opcional, 2-3 palabras en galego y grandes: **"MEIGAS DE VERDADE"**.
- **Evitar** (vetos para la pieza visual): sombrero de pico, caldero, escoba, piel verde, calabazas, gatos negros de
  Halloween, castillos, cipreses, tejados de teja naranja.
- Variante B (si el arranque en frío es la queimada): primer plano de una **pota de barro con lume azul** en una cocina
  de piedra a oscuras y unas manos viejas removiendo; texto "1967". Solo si el vídeo cuenta lo de 1967 en el primer
  minuto (no inducir a error).

## 10. Arco de ≈ 30 min (≈ 3.400 palabras), del gancho al tono de dormir

Tipo: **H** = historia documentada (con fuente en el dossier); **L** = lenda o creencia popular, contada como tal
("din que", "contaban", "cría a xente"); **A** = ambiente, sin datos. Ritmo orientativo de la voz en palabras por minuto
(ppm), bajando con el embudo. Títulos de capítulo en galego (sirven para la descripción de YouTube).

| Tiempo | Capítulo | Contenido | Tipo | Palabras (ppm) | Imagen y luz |
|---|---|---|---|---|---|
| 0:00-0:40 | Arranque en frío: "Un conxuro de 1967" | Ganchos 1 y 2: el conxuro no es antiguo; la Inquisición de Santiago apenas quemó meigas | H | ≈ 95 (140) | Noche, lume azul de queimada, soportales de piedra mojados; cortes de 6-8 s |
| 0:40-0:55 | Aviso y reclamo | "A voz que vas escoitar é sintética, e este texto preparouno un proceso automático." "Isto é Cousas de Galiza para durmir." | - | ≈ 30 | Título sobre niebla y aldea |
| 0:55-2:00 | "Os papeis que falan" | Ganchos 3, 4 y 5: la parteira de Vilalba, las "areas de Sevilla", la meiga como curandeira; promesa: "esta noite imos abrir eses papeis, a modo" | H | ≈ 150 (135) | Legajos, pluma, archivo a la luz de vela; parteira en una cocina de piedra |
| 2:00-6:00 | 1. "Quen eran as meigas" | Curandeiras, parteiras, menciñeiras; viudas y solteras, las más denunciadas; los nombres (meiga, bruxa, feiticeira, menciñeira); lo que la gente creía que hacían: volar a las xuntanzas dejando un cuerpo fingido en la cama, volverse gato, sapo o lobo | H (etnografía documentada) + L (las creencias, como creencias) | ≈ 480 (125) | Aldea de granito y lousa al atardecer, carballeira, herbas colgadas en la lareira |
| 6:00-10:00 | 2. "O tribunal de Santiago" | El tribunal (1574), las cifras (92 + 48), una sola hoguera, el supuesto "racionalismo" de los inquisidores hispanos, más escépticos que los europeos (así lo presenta el Arquivo, que pide estudiarlo mejor); la justicia ordinaria (unos 30 procesos en el Arquivo do Reino) y sus penas (destierro, azotes, emplumamento), dichas sin detalle | H | ≈ 470 (120) | Compostela de noche, lluvia en la piedra, sala de audiencia con velas. **Desde aquí baja el ritmo** |
| 10:00-16:00 | 3. "Catro aldeas, catro papeis" | Marta de Quián (Lalín, 1611: la leche de las vacas y los remedios contra las meigas); Ana González (Xinzo de Limia, 1612: la mujer que, decían, entraba como un gato); Inés de Maquieira (Campo Lameiro, 1643: los vecinos que apuntaron a las mujeres de la fuente la noche de San Xoán); Dorotea y María do Barro (Vilalba, 1617: según un testigo, María, cuando llevaba el ganado al monte, decía que bebiese "auga de sete fontes" y trajese "leite de sete cortes e de sete montes") | H (lo que declararon los testigos; sin decidir si era verdad) | ≈ 680 (115) | Vacas, hórreos, una fonte de piedra de noche, gatos en la lareira; planos detalle y generales alternos |
| 16:00-19:00 | 4. "María Soliña e o mar de Cangas" | El ataque turco a Cangas (1617), el símbolo, el poema de Celso Emilio Ferreiro en *Longa noite de pedra* (1962); **"dela sabemos moi pouco"** (no hay documentos del juicio, según el CCG) | H (el ataque y el poema) + símbolo (la vida, como incierta) | ≈ 330 (110) | Ría de Vigo con mar calmo, barcas, costa atlántica al amanecer |
| 19:00-24:00 | 5. "A noite de San Xoán" | Herbas de San Xoán, hogueras, agua de siete fuentes, "meigas fóra"; el mal de ollo y el meigallo, y cómo se "desfacían" | L / tradición (contada como costumbre; el dossier fija cada práctica con fuente) | ≈ 530 (105) | Hogueras lejanas, herbas en agua bajo las estrellas, rocío; luz muy baja y cálida |
| 24:00-27:30 | 6. "O frade que non cría nas meigas" | Feijoo (Casdemiro, 8-10-1676; benedictino; *Teatro crítico universal*, 1726-1739), que escribió contra las supersticiones: la calma de la razón; 350 años este mes | H | ≈ 360 (100) | Celda de monasterio, vela, pluma, lluvia en la ventana, soutos de castaños de Ourense |
| 27:30-30:00 | Peche: "Chove na lousa" | "Habelas, hainas?" como sonrisa; la aldea duerme, lluvia en los tejados de lousa, brasas; sin llamadas a suscribirse o una sola línea suave | A | ≈ 240 (95) | Brasas, tejados de lousa bajo la lluvia, fundidos largos a negro |

**Reglas del arco para las piezas de guion y dossier:**
- **Sin terror ni violencia explícita**: tortura y hoguera se nombran una vez cada una, sin detalles (nada de garrotes,
  potro ni llamas sobre personas). Nada de "chuchonas" que chupan sangre en la segunda mitad.
- **No inventar**: ningún diálogo ni pensamiento de las procesadas; las citas de los procesos, traducidas al galego y
  atribuidas ("segundo declarou…").
- **Dudoso = se dice o se omite**: el año de la única hoguera; la biografía de María Soliña (¿nació en 1551 o en 1601?, ¿murió de "loucura, fame e miseria"?);
  el origen de "habelas, hainas"; que la Santa Compaña aparezca en papeles de la Inquisición (no usar sin fuente
  primaria).
- **Queimada**: nada de "tradición celta"; como mucho "a súa orixe non está clara" (Galipedia) y el conxuro de 1967.
- Lo que tiene que verificar el dossier: todo lo marcado H, contra el PDF del Arquivo do Reino, el CCG, GCiencia,
  Galipedia y, si se puede, Contreras (*El Santo Oficio de la Inquisición en Galicia 1560-1700*, 1982) y Lisón
  Tolosana para lo etnográfico.

## 11. Supuestos [S] y riesgos

- [S] Que el público de "brujas" en castellano llegue a un vídeo en galego: no hay datos; es la principal incertidumbre
  de la recomendación.
- [S] La ventana de publicación (8-17 de octubre) depende de que el vídeo esté listo; 30 min son ≈ 50 h de CPU de
  núcleo con el pipeline actual (CLAUDE.md: 3 min ≈ 5 h), unas 14 h de reloj con los 4 núcleos (HANDOFF: 60 min ≈
  28,6 h), más las rondas de guion e imagen.
- Riesgo de imagen: la palabra "bruxa" arrastra el cliché de Halloween (sombrero de pico, caldero); la pieza visual
  debe vetarlo y usar la lista positiva de iconografía gallega.
- Riesgo de rigor: las fuentes discrepan en fechas (§8, gancho 2; María Soliña). El dossier decide o se omite.
- Riesgo legal menor: el texto del conxuro está registrado; citar solo un verso con autoría.
- Los datos de YouTube son una muestra y las vistas son acumuladas (§1): sirven para ordenar temas, no para prever
  vistas.
