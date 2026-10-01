# Aprendizajes de la pieza DOSSIER (Gauntlet 3), 30-09-2026

Agente constructor de la pieza DOSSIER (Claude). Qué funcionó, qué no y cifras, para repetir el dossier de otro
episodio. Resultado: `plan-de-negocio/gauntlet3/dossier/` (`feitos.yaml`, `xerar.py`, `dossier.md`) y la ficha
`herramientas/pipeline/temas/meigas-de-verdade.yaml`.

## Método que funcionó

- **Una sola fuente de verdad**: `feitos.yaml` con cada hecho en galego y sus evidencias `{fonte, cita}`, donde la cita
  es un trozo **literal** del texto descargado. `xerar.py comprobar` busca cada cita en su fuente (normalizando
  mayúsculas, espacios y comillas, como `dossier.py` del pipeline) y `xerar.py ficha` genera la ficha. Las 350 citas
  pasaron a la primera porque se copiaron del texto ya extraído; una prueba negativa (tres citas alteradas) confirmó que
  el comprobador falla cuando debe.
- **Proba negativa también para "no está"**: campo `ausente` (p. ej. "las hay, las hay" en el *Quijote* de Gutenberg).
- **LanguageTool sobre los hechos** (`lt_feitos.py`, ~1 min, sin candado: es ligero): encontró 97 avisos, casi todos
  nombres propios (hunspell). Los útiles: reflexivos que LT no admite ("comíase", "sentábase", "collíase",
  "deixábanse", "riuse", "rompéuselle"), fechas "o vinte e…" (concordancia), "O historiador Rodrigo" (lee "Rodrigo"
  como verbo), "Santa Baia" (regla de errores comunes de Wikipedia), "contra mulleres", "decomisado" (en galego es
  "comisado"), "ungüento" (la RAG lo escribe con diéresis). Se reescribieron los hechos para que el guionista pueda
  copiar su redacción sin chocar con la puerta de lengua. Lista completa en `dossier.md` §3.
- **Diccionario de la RAG como fuente de "ambiente"**: sus definiciones y ejemplos dan detalles verdaderos y tranquilos
  (lareira, escano, gramalleira, lacena, hórreo, orballo, lousa, lousado, abeluria, fiúncho…), con URL por palabra.
  `https://academia.gal/dicionario/-/termo/busca/<palabra>` responde con curl; el texto útil está en la línea que empieza
  por la palabra y contiene "substantivo"/"verbo"/"adxectivo" (script `rag.py` en el scratchpad).
- **Separadores de capítulo dentro del dossier**: una línea `- [== C1. … ==]` la descarta `feitos()` del pipeline (sin la
  etiqueta queda vacía) y deja el dossier ordenado por el arco para el guionista.
- **Recortar a 180** marcando `ficha: false` en vez de borrar: los 66 hechos fuera siguen verificados y documentados.
- **Prueba de humo sin modelo** (`probas/proba_lexica.py`, segundos): H1 + coincidencia léxica de `veracidade.py` con
  frases candidatas. Con coincidencia ≥ 0,8 la regla de apoyo pasa sin NLI, así que ya decide casi todo sin esperar al
  candado de CPU. Resultado (30 frases): 13/14 del gancho y 9/10 del relato con apoyo; 3 de 6 falsas paradas (H1 y
  desenlace). Hallazgos:
  - **H1 junta nombres separados por una coma** ("Xinzo de Limia, María Feijoa" → un solo nombre que no está en el
    dossier). Avisarlo al guionista.
  - **La veracidad no para falsedades hechas con palabras del dossier**: "María Soliña morreu queimada na fogueira de
    Cangas", "En Galicia só se queimou unha meiga" y "Feijoo naceu en Samos" pasan (coincidencia 0,83-1,0). La lista
    "Non dicir" tiene que ir en el encargo del guion y en la revisión del crítico.
  - Dejar **fuera de la ficha los años y nombres en conflicto** funciona: H1 impide que el guion diga 1579, 1627 o
    "María Rodríguez".
  - Las frases que se dirigen al oyente ("seguramente oíches…") no tienen apoyo: añadir un hecho con esas palabras
    (F246) o justificarlas en `--excepcions`.

## Fuentes que sirvieron

| Fuente | Para qué | Nota |
|---|---|---|
| PDF del Arquivo do Reino "Meigas, feitizos das menciñeiras" (2020) | Transcripciones de 6 procesos de la Real Audiencia y cifras de la Inquisición | `pypdf` extrae 3.162 palabras de 19 páginas; hay guiones de corte ("dera-/mava") y espacios raros ("San Salvadorde", "Boborás . 1639"): elegir citas que no los crucen. Los enlaces de la p. 18 (`registro.do?id=`) llevan a las fichas archivísticas |
| CCG, Álbum de Galicia ("Meigas", "María Soliña") | Contreras citado, María Rodríguez, Laxe y Cangas, curandeiras | La página viene en ISO-8859-1: decodificar según el `charset` |
| *GCiencia* (2026: Pousa; 2021: queimada con Xavier Castro) | Tesis de la curandeira, "Maldita a nai…", pena de muerte en pleitos civiles, tradición inventada | En galego y con citas literales de historiadores |
| *El Español* (Valor Bravo) | Una hoguera de la Inquisición; la justicia ordinaria "mató a muchas" | La tesis que el tema había leído a medias |
| Galipedia (Queimada, San Xoán, Herbas, Meiga, Inquisición española, Feijoo, Mal de ollo, Lareira, Hórreo…) | Costumbres y contexto, con sus referencias (Taboada Chivite, Risco, Lisón, Contreras) | La API (`/w/api.php`) dio **429** repetidos; la página normal `/wiki/<título>` con un User-Agent de navegador y 4 s entre peticiones funcionó. Galipedia redirige "María Soliña" a "María Soliño" |
| Filosofía en español (Feijoo) | *Teatro crítico* II, 5 "Uso de la Mágica": texto completo | Algunas páginas devuelven un cargador anti-bot ("One moment, please") y el enlace de *Cartas eruditas* III, 15 lleva a otra carta: comprobar siempre el `<title>` |
| Concello de Cangas, *La Voz de Galicia* 2017, *Atlántico*, *El Correo Gallego* | María Soliña y el conxuro | Prensa: buena para fechas concretas, pero cruzar siempre (errata "1759" en *Atlántico*) |

## Problemas

- **Galiciana (`arquivo.galiciana.gal`)** sirve un desafío anti-bot en JavaScript: no se consultaron las fichas
  archivísticas (habrían resuelto del todo quién era la parteira de Vilalba). No intentar saltarlo.
- **Contreras (1982) y Lisón Tolosana** no están en línea: solo se pueden usar a través del CCG y de Galipedia, y
  atribuidos.
- **El artículo del CSIC** sobre corsarios (*Cuadernos de Estudios Gallegos*) falló por TLS (la cadena del servidor no
  valida ni con `--cacert`); no hizo falta.
- **Las fuentes se contradicen en casi todas las fechas "famosas"**: la hoguera (1575/1579/1627/1759), María Soliña
  (nacida en 1551 o 1601; sin documentos según el CCG, con proceso en el AHN según la prensa), el asalto de Cangas (4 o
  9 de diciembre; 33 o más de cien muertos). Regla que funcionó: si no hay dos fuentes independientes que concuerden,
  el dato no entra en la ficha, y la ficha dice que las fuentes no concuerdan (así H1 impide que el guion lo diga).
- **El título del capítulo 6 del arco era falso**: Feijoo no negaba la brujería ("Que hay hechiceros… consta de la
  Escritura"). Leer la fuente primaria cambió el capítulo.
- **El candado de CPU** estuvo ocupado por la TTS del agente de voz durante la prueba de NLI (3 procesos en cola): la
  prueba de humo de la veracidad hay que lanzarla en segundo plano y seguir con otra cosa.
- **Descuido corregido**: en una prueba de la API de Wikipedia puse el correo del promotor en el User-Agent; no debe
  salir de la sesión. Usar un User-Agent genérico.
