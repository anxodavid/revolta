# Pieza TEMA (Gauntlet 3): qué episodio da más gancho y más audiencia, compatible con dormir

Constructor: agente de la pieza TEMA (Claude), 30-09-2026. Documento de trabajo en castellano; lo que verá u oirá el
público (títulos, ganchos) va en galego.

**Qué es automático y qué hizo Claude a mano.** Las búsquedas de YouTube (yt-dlp), los metadatos y Google Trends
(pytrends) se sacaron con scripts; las cifras de las tablas salen de esos scripts. **A mano (Claude)**: la elección de
consultas, las reglas de limpieza (qué vídeo cuenta como "narrativo sobre el tema"), la revisión de qué vídeos están en
galego, la verificación de los hechos en las fuentes, las puntuaciones y la recomendación. Ninguna persona ha revisado
este documento.

> Estado: **parte 1 (datos)**. La puntuación, el ranking, la recomendación, los ganchos y el arco van en la parte 2.

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
| Samaín | 0,3 | 10,4 (79 % ceros) | 13,1 (93 % ceros) | 11,0 (84 % ceros) | octubre | Casi solo existe el 31 de octubre, y con poco volumen |
| María Pita | 0,4 | 0,45 (5a, 39 % ceros) | - | 0,06 (5a) | agosto | Nada de octubre |
| Romasanta | 0,2 | 1,13 (5a, 65 % ceros) | - | - | enero | Pequeño |
| batalla de Rande | 0,1 | ruido (94 % ceros) | - | - | - | Muy pequeño (aniversario: 23-10-1702) |
| San Xoán | 0,1 | 0,0 (5a) | - | - | junio | Fuera de temporada |
| mouras, María Soliña, San Andrés de Teixido, "brujas gallegas", "leyendas gallegas" | ≤ 0,1 | ruido | - | - | - | Sin volumen medible |

Lectura: en octubre **suben "Santa Compaña" (× 2,3-3,2) y "brujas" (× 1,7-2,4)**; "meigas" y "queimada" no se mueven.
En volumen de YouTube España, de los temas gallegos de folclore solo "Santa Compaña" y "queimada" tienen algo; "meigas"
es pequeño como palabra de búsqueda, pero "brujas" es enorme y de octubre.
