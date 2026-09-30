# Aprendizajes de la pieza TEMA (Gauntlet 3), 30-09-2026

Agente constructor de la pieza TEMA (Claude). Qué funcionó, qué no y cifras, para repetir la medida en otra sesión.
Scripts en `plan-de-negocio/gauntlet3/tema/scripts/` (el scratchpad no sobrevive).

## Datos de YouTube (yt-dlp 2026.08.19, venv propio en el scratchpad)

- **Búsqueda plana**: `yt-dlp --flat-playlist -j --extractor-args "youtube:player_client=android_vr" "ytsearch20:<consulta>"`
  da vistas, canal, título, duración y URL en ~1,5 s por consulta. 83 consultas seguidas sin bloqueo.
- **Fecha en la búsqueda plana**: añadir `--extractor-args "youtubetab:approximate_date"`. Da una fecha aproximada a
  partir de "hace 2 años" (error de hasta una unidad: mes o año). Sin ese argumento, la fecha sale vacía.
- **Ordenar por vistas**: pasar la URL de resultados con el filtro: `"https://www.youtube.com/results?search_query=<q>&sp=CAM%253D"`
  y `--playlist-end 20`. Útil para ver el techo de un tema, pero con palabras sueltas mete mucho ruido (p. ej. "meigas"
  saca un tutorial de un garaje y un grupo de hockey): usar consultas de 2-3 palabras.
- **Metadatos completos** (fecha exacta, suscriptores, "me gusta"): `-j --skip-download` con `android_vr` funcionó
  **15 veces** y luego YouTube pidió "Sign in to confirm you're not a bot". Siguió funcionando con
  `--extractor-args "youtube:player_client=mweb" --ignore-no-formats-error` y 3 s entre peticiones (27 vídeos más).
  Sin `--ignore-no-formats-error`, `mweb`/`web_safari`/`web_embedded` fallan con "Requested format is not available".
- **Autocompletado de YouTube** (sugerencias de búsqueda) accesible sin clave:
  `https://suggestqueries.google.com/complete/search?client=youtube&ds=yt&hl=gl&gl=ES&q=<término>`.
- **El cliente pide inglés**: muchos títulos salen traducidos al inglés ("The Holy Company"); el vídeo es el mismo.
  Para saber si un vídeo está en galego hay que mirarlo a mano: el filtro por palabras del título confunde galego y
  portugués ("lenda", "da", "dos") y cuela canales castellanos con nombre galego ("Meigas do Lume").

## Limpieza de resultados (lo que más tiempo llevó)

- Los resultados de folclore gallego están **dominados por música** (Mägo de Oz "La Santa Compaña" y "Conxuro", Luar
  na Lubre "María Soliña", Carlos Núñez "Muiñeira de Chantada") y por **homónimos** (el otorrino Michael Teixido, la
  cantante brasileña Maria Pita, la fadista Ana Moura, la banda de metal Romasanta). Sin limpiar, las cifras engañan:
  "Santa Compaña" parecía tener 20 M vistas (un "Top 5 leyendas" latinoamericano).
- Reglas de limpieza por tema en `limpiar.py` (incluir por título, excluir música/películas/homónimos/guías de viaje).
  Error cazado: la expresión "rain" (lluvia) casaba con "Efrain"; usar límites de palabra (`\brain\b`).

## Google Trends (pytrends 4.9)

- Funciona a través del proxy con `TrendReq(..., requests_args={"verify": "/root/.ccr/ca-bundle.crt"})`.
- **No pasar `retries` ni `backoff_factor`** a `TrendReq`: con el urllib3 actual lanza un error que, si se captura,
  convierte el script en un bucle silencioso de reintentos (10 min perdidos).
- Con 8 s entre consultas salieron 2 errores 429 en 28 consultas; reintentar a los 30 s basta.
- `gprop="youtube"` da el índice de **búsquedas en YouTube**: más útil que el de la web para este proyecto.
- Términos pequeños ("mouras", "María Soliña", "leyendas gallegas") salen casi siempre a cero en la serie semanal de 5
  años. Para estacionalidad, usar la **serie mensual larga** (`timeframe="all"` en web; `"2008-01-01 2026-09-29"` en
  YouTube) y el índice de los meses desde 2019. Comparar lotes con un término ancla común ("Santa Compaña").

## Fuentes para verificar ganchos

- **Joya**: el PDF de la exposición "Meigas, feitizos das menciñeiras" del Arquivo do Reino de Galicia (Xunta, 2020),
  19 páginas con **transcripciones de procesos reales** por brujería de la Real Audiencia de Galicia y cifras de la
  Inquisición de Santiago:
  https://arquivosdegalicia.xunta.gal/sites/default/files/arquivos_artividades/expo_mulleres_2020_01_C.pdf (25 MB;
  texto extraíble con `pypdf`).
- **Álbum de Galicia del Consello da Cultura Galega** (entradas "Meigas" y "María Soliña"): fiable y prudente. La de
  María Soliña avisa de que **no hay documentos del juicio**: lo que circula sobre ella es en parte lenda.
- **Galipedia** es buena como índice de fuentes (cita *Grial*, *La Voz de Galicia*…), pero hay que ir a la fuente:
  resúmenes y fechas a veces no cuadran (María Soliña: nacida en 1551 según Galipedia, "1601-1680" según el CCG).
- **Fuentes que se contradicen**: la única mujer quemada por la Inquisición de Santiago fue en **1627** según el
  Arquivo do Reino y en **1579** (María Rodríguez) según *El Español* citando a Diego Valor Bravo; el CCG habla de
  "algúns casos". Coinciden en que fue **una sola** (o casi): decirlo sin el año.
- El API de Galipedia (`/w/api.php`) devuelve error sin cabecera User-Agent: usar uno genérico.
- El diccionario de la RAG (`https://academia.gal/dicionario/-/termo/busca/<palabra>`) responde con curl: sirve para
  comprobar formas ("coruxa" → forma correcta "curuxa").
- Texto completo del *Quijote* en Project Gutenberg (https://www.gutenberg.org/cache/epub/2000/pg2000.txt): permite
  comprobar con `grep` que "que las hay, las hay" **no está** en la novela.

## Lo que dicen los datos (para las próximas piezas y episodios)

- **La Santa Compaña es el tema gallego con más demanda y más estacional (octubre × 2,3-3,2)**, pero su público es de
  terror: sus versiones "para dormir" hacen 5-6 K vistas frente a 100-200 K las de terror.
- **"meigas" es pequeña como palabra de búsqueda**, pero "brujas" es enorme en YouTube España (≈ 34 veces "Santa
  Compaña") y sube en octubre (× 2,0).
- **Nada en galego para dormir** en ningún tema; en galego solo hay cortos de la TVG y cuentos infantiles.
- **Competidor directo**: *Relatos al Oído* (castellano, 66.000 suscriptores). Su vídeo de lendas de Galicia (108.105
  vistas) se publicó el **9 de octubre** de 2025, y el 26-09-2026 subió otro de Lugo.
- El mejor dato "para dormir" de un tema gallego es del **Camino de Santiago** (182.379 vistas en 6 meses, canal de
  20.800 suscriptores).
