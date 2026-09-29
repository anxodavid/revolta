# QA automático: A Revolta Irmandiña, contada para durmir (irmandinos-apertura)

Informe xerado por `herramientas/pipeline/pipeline.py` (etapa 8). Ningunha persoa revisou o vídeo.

**Veredicto automático: PUBLICABLE**

| Porta | Resultado |
|---|---|
| duracion | pasa |
| wer_mestura | pasa |
| sincronia_av | pasa |
| sincronia_subtitulos | pasa |
| lingua_lt | pasa |
| estilo | pasa |
| sonoridade | pasa |
| peso | pasa |
| resolucion | pasa |

## Ficheiro

| Medida | Valor |
|---|---|
| mb | 36.6 |
| resolucion | 1920x1080 |
| fps | 24.0 |
| pista_subtitulos | True |
| dur_video_s | 240.79 |
| dur_audio_s | 240.78 |
| dur_prevista_s | 240.78 |
| desfase_av_s | 0.01 |
| lufs_integrado | -20.0 |
| lra_lu | 9.6 |
| pico_real_dbtp | -5.1 |
| ritmo (palabras/min sobre a narración, pausas incluídas) | 123.5 |

## ASR (Whisper large-v3-turbo galego de Nós, CTranslate2 int8)

| Audio | WER | Subst. | Borr. | Ins. | Palabras ref. |
|---|---|---|---|---|---|
| mestura | 0.025 | 5 | 1 | 6 | 475 |
| voz | 0.086 | 10 | 30 | 1 | 475 |

Sincronía subtítulos-voz (marcas de tempo por palabra do ASR contra o SRT): 100.0 % das 469 palabras aliñadas caen dentro da súa frase (±0,5 s); desfase no inicio de frase: mediana -0.3 s, máximo 0.57 s (32 frases medidas).

Frases con WER > 0,5 (candidatas a erro de pronuncia): ningunha.

<details><summary>Transcrición ASR da mestura</summary>

Boas noites. A voz que vas escoitar é sintética e este texto preparouno un proceso automático. Ao sur de Compostela hai un outeiro verde e nas mañás do outono a brétema queda alí moito tempo. Nentre as árbores asuman unhas pedras vellas, cubertas de musgo e de follas molladas. as. Son os restos dunha fortaleza, uns anacos de muralla e a planta dos muros debuxada no chan. Hoxe só se escoita a choiva lenta sobre as follas e, lonxe, algún paxaro. Aquela fortaleza chamábase a Rocha Forte e era do arcebispo de Compostela. Desde ela vixiábanse os camiños que baixaban cara ao mar.  Un día, a xente da cidade e os labregos da comarca decidiron que aquela torre xa non tiña que seguir en pé e botárona abaixo. Isto é serán, historia de Galicia para durmir. Esta noite imos contar a historia dos irmandiños. Durante uns poucos anos labregos, artesáns, mariñeiros, clérigos e mesmo algúns fidalgos xuntáronse nunha irmandade e botaron abaixo.  dixo moitas das torres do país. Falaremos da vida baixo aquelas torres e dos tempos difíciles que viñeran antes. E, xa cara ao final, lembrarémolo que contaron moito despois os vellos que o viran de mozos. Non tes que lembrar nada do que che conte. Acomódate, apaga a luz se aínda está acesa e deixa que o corpo pese un pouco máis.  deixa tamén que a respiración vaia máis amodo e imos alá a aquel tempo. Arredor da metade do século XV, Galicia era unha terra de labregos, de artesáns, de mariñeiros e de mercadores. Moitos deles vivían nas terras dun señor e eran os seus vasalos. Pagábanlle tributos en diñeiro e en especie e debíanlle traballo nas obras da fortaleza e servizo coas armas. as. E eran cargas pesadas, e moitas familias labregas vivían sempre á beira da pobreza. O señor era tamén o xuíz na súa terra. Había xa un século que mandaba unha nobreza nova, máis violenta ca a de antes, e o país enchérase de fortalezas. Algunhas eran das grandes casas nobres, como a de Lemos ou a de Andrade.  Outras eran dos bispos e, sobre todo, do arcebispo de Compostela. Desde aquelas torres, dicían os vasalos, viñan os males e os danos. Moitos anos despois, as testemuñas aínda lles chamaban refuxios de malfeitores. Non era a primeira vez que a xente se xuntaba contra os señores. Unhas décadas antes, os vasalos dun gran señor das Mariñas formaran unha irmandade e camiñaran xuntos cara a Compostela. Aquela primeira irmandade foi vencida e os que a formaran foron castigados. Os tempos, ademais, eran difíciles porque desde a peste negra as rendas dos señores viñan minguando en toda Europa.  en Europa. E, como cobraban menos, moitos señores esixían cada vez máis aos seus vasalos. Así, pouco a pouco, nas casas e nos camiños ía medrando a memoria daquelas irmandades, coma unha semente que agarda outra primavera.

</details>

## Lingua (LanguageTool 6.8 gl-ES, con hunspell galego)

Avisos antes da corrección automática: 3. Despois: 2.

- antes: `REFLEXIVOS` Algúns verbos non admiten nunca construcións reflexivas. Será mellor "demora"? — "... verde, e nas mañás de outono a brétema demórase alí moito tempo. Entre as árbores asoma..."
- antes: `GENERAL_VERB_AGREEMENT_ERRORS` Posíbel erro de concordancia verbal. — "...erán, historia de Galicia para durmir.  Esta noite imos contar a historia dos irmandiños. Duran..."
- antes: `GENERAL_GENDER_AGREEMENT_ERRORS` Posíbel erro de concordancia de xénero. — "...ñas formaran unha irmandade e camiñaran xuntos cara a Compostela. Aquela primeira irmandade..."
- despois: `GENERAL_VERB_AGREEMENT_ERRORS` Posíbel erro de concordancia verbal. — "...erán, historia de Galicia para durmir.  Esta noite imos contar a historia dos irmandiños. Duran..."
- despois: `GENERAL_GENDER_AGREEMENT_ERRORS` Posíbel erro de concordancia de xénero. — "...ñas formaran unha irmandade e camiñaran xuntos cara a Compostela. Aquela primeira irmandade..."

## Estilo e densidade (regras do canal)

| Control | Valor |
|---|---|
| palabras | 475 |
| palabras_obxectivo | 440 |
| desvio_palabras_pct | 8.0 |
| cifras | [] |
| signos_prohibidos | [] |
| preguntas | 0 |
| palabras_vetadas | [] |
| aviso_literal | True |
| formula_literal | True |
| frases_fora_8_25 | [] |
| nomes_propios_distintos | ['Andrade', 'Compostela', 'Europa', 'Forte', 'Galicia', 'Lemos', 'Mariñas', 'Rocha', 'Serán'] |
| max_nomes_novos_por_110_palabras | 4 |

## Son

| Medida | Valor |
|---|---|
| lufs_voz_obxectivo | -20.0 |
| choiva_rel_db | -17.0 |
| lufs_mestura_pyloudnorm | -20.0 |
| pico | 0.558 |

## Escenas e imaxes

| # | Frases | Dur. (s) | Mov. | Lum. | Contr. | Simil. ant. | Prompt |
|---|---|---|---|---|---|---|---|
| 0 | 1-3 | 21.9 | zoom_in | 115.5 | 53.3 | None | A green wooded hill rising from thick morning fog, oak and chestnut trees, a few grey granite stones on its top, pale dawn light, wide view of a quiet valley |
| 1 | 4-6 | 21.6 | pan_right | 88.6 | 33.5 | 0.16 | Moss-covered granite ruins of a medieval wall among oak trees, low stone foundations outlined on the ground, wet fallen leaves, light rain, soft grey daylight |
| 2 | 7-8 | 11.4 | zoom_out | 97.6 | 34.1 | 0.21 | A small granite castle with a square keep on a green hill, seen from far away, muddy roads winding down through wooded valleys toward a distant grey estuary, overcast afternoon |
| 3 | 9-10 | 15.5 | pan_up | 139.0 | 61.1 | 0.52 | A crowd of peasants seen from behind walking slowly up a misty green hillside at dawn with wooden tools on their shoulders, a dark stone tower above them in the fog |
| 4 | 11-12 | 16.0 | pan_left | 111.4 | 35.4 | 0.57 | A small Galician hamlet of grey granite houses with dark slate roofs, peasants, fishermen and a monk in a brown habit talking quietly, seen from a distance, drizzle, overcast morning |
| 5 | 13-14 | 15.3 | zoom_in | 35.1 | 19.8 | -0.22 | An old man seen from behind sitting by a hearth fire inside a humble granite house at night, warm orange firelight on rough stone walls, wooden bench, clay pots |
| 6 | 15-17 | 18.1 | zoom_in | 41.5 | 28.1 | -0.01 | A quiet medieval bedroom at night, simple wooden bed with wool blankets, one candle on a stool, a small window with raindrops and blue darkness outside, warm dim light |
| 7 | 18-19 | 14.0 | pan_right | 120.7 | 35.7 | -0.08 | Green rainy Galician countryside, small fields bordered by stone walls, a hamlet of granite houses with thatched roofs and a stone hórreo granary, a misty estuary with small fishing boats |
| 8 | 20-21 | 15.8 | pan_left | 109.5 | 41.7 | 0.45 | Peasants seen from behind carrying sacks of grain along a muddy lane toward a square granite tower house, an ox cart, chestnut trees in autumn, grey sky |
| 9 | 22-23 | 13.0 | zoom_out | 85.2 | 37.8 | 0.44 | A tall square granite tower house dominating a green valley at dusk, a few small peasant houses with smoking chimneys below, cold blue evening light, light rain |
| 10 | 24-25 | 12.8 | pan_right | 104.9 | 37.4 | 0.43 | A great granite castle with high walls and towers above a green river valley, far away the towers of a Romanesque cathedral, low clouds, soft evening light |
| 11 | 26-27 | 13.5 | zoom_in | 80.3 | 31.8 | 0.67 | A dark granite fortress tower at night under a cloudy sky with a pale moon, a few peasant houses below with small warm lit windows, fog on the ground |
| 12 | 28-30 | 21.5 | pan_left | 155.2 | 62.7 | 0.69 | A long line of peasants seen from behind walking together along a muddy road through fog and green fields toward the distant towers of a walled medieval city, grey morning |
| 13 | 31-32 | 16.0 | zoom_out | 108.2 | 37.9 | 0.82 | Empty autumn fields and an abandoned granite farmhouse with a collapsed slate roof, bare chestnut trees, low grey clouds, crows in the sky, rainy melancholic quiet |
| 14 | 33-33 | 14.3 | zoom_in | 89.8 | 42.3 | 0.21 | Weathered hands of a peasant woman placing seeds into a small clay jar on a wooden table, warm hearth light, a window showing a green spring morning with blossoming trees |

## Tempos de render (CPU: 4 núcleos, sen GPU)

| Etapa | Parede (s) | CPU (s) |
|---|---|---|
| 1_guion | 0.0 | 0.0 |
| 2_corrixir | 13.7 | 9.8 |
| 3_escenas | 0.0 | 0.0 |
| 4_voz | 248.3 | 202.7 |
| 5_imaxes | 574.4 | 1010.2 |
| 6_son | 5.0 | 4.9 |
| 7_montaxe | 308.9 | 1149.7 |
| 8_qa | 135.3 | 262.8 |
| **Total** | **1285.6** | **2640.1** |

Tempo total de CPU: 0.73 h de núcleo; parede: 21.4 min. Non inclúe a descarga de modelos nin o tempo do LLM externo (ver LLM).

## Extrapolación a un episodio de 60 min [S: escala lineal dos tempos medidos]

Supostos: mesma densidade de texto, unha imaxe cada 15 s (240 imaxes), custo de voz, montaxe e QA proporcional á duración (nas imaxes a carga do modelo cóntase unha vez), e LLM local non incluído.

| Etapa | Parede (min) | CPU (h de núcleo) |
|---|---|---|
| 4_voz | 62 | 0.84 |
| 5_imaxes | 70 | 2.06 |
| 6_son | 1 | 0.02 |
| 7_montaxe | 77 | 4.77 |
| 8_qa | 34 | 1.09 |
| 2_corrixir | 3 | 0.04 |
| **Total** | **248** (4.1 h) | **8.83** |

## LLM

| Etapa | Caché | Metadatos |
|---|---|---|
| guion | `guion-86cb43ec62b3.txt` | backend: manual, model: Claude Opus 5.5 (claude-opus-5-5) actuando como LLM do pipeline, data: 2026-09-29, nota: Resposta escrita seguindo literalmente o prompt renderizado (llm_pending/guion-86cb43ec62b3.prompt.md), sen edición humana. |
| corrixir | `corrixir-29a6ee9f9e7b.txt` | backend: manual, model: Claude Opus 5.5 (claude-opus-5-5) actuando como LLM do pipeline, data: 2026-09-29, nota: Resposta ao prompt renderizado llm_pending/corrixir-29a6ee9f9e7b.prompt.md: acepta REFLEXIVOS (demorarse -> queda); considera falsos positivos a concordancia de Esta noite imos, e camiñaran xuntos (suxeito os vasalos). |
| escenas | `escenas-57d1738aae30.txt` | backend: manual, model: Claude Opus 5.5 (claude-opus-5-5) actuando como LLM do pipeline, data: 2026-09-29, nota: Resposta ao prompt renderizado llm_pending/escenas-57d1738aae30.prompt.md (versión 2 do prompt de escenas: prompts máis curtos e regra de paisaxe atlántica), sen edición humana. |

## Guion final narrado

Boas noites. A voz que vas escoitar é sintética, e este texto preparouno un proceso automático.

Ao sur de Compostela hai un outeiro verde, e nas mañás de outono a brétema queda alí moito tempo. Entre as árbores asoman unhas pedras vellas, cubertas de musgo e de follas molladas. Son os restos dunha fortaleza: uns anacos de muralla e a planta dos muros, debuxada no chan. Hoxe só se escoita a choiva lenta sobre as follas e, lonxe, algún paxaro.

Aquela fortaleza chamábase a Rocha Forte, e era do arcebispo de Compostela. Desde ela vixiábanse os camiños que baixaban cara ao mar. Un día, a xente da cidade e os labregos da comarca decidiron que aquela torre xa non tiña que seguir en pé, e botárona abaixo.

Isto é Serán, historia de Galicia para durmir.

Esta noite imos contar a historia dos irmandiños. Durante uns poucos anos, labregos, artesáns, mariñeiros, clérigos e mesmo algúns fidalgos xuntáronse nunha irmandade e botaron abaixo moitas das torres do país. Falaremos da vida baixo aquelas torres e dos tempos difíciles que viñeran antes. E, xa cara ao final, lembraremos o que contaron moito despois os vellos que o viran de mozos.

Non tes que lembrar nada do que che conte. Acomódate, apaga a luz se aínda está acesa e deixa que o corpo pese un pouco máis. Deixa tamén que a respiración vaia máis amodo, e imos alá, a aquel tempo.

Arredor da metade do século quince, Galicia era unha terra de labregos, de artesáns, de mariñeiros e de mercadores. Moitos deles vivían nas terras dun señor, e eran os seus vasalos. Pagábanlle tributos en diñeiro e en especie, e debíanlle traballo nas obras da fortaleza e servizo coas armas. Eran cargas pesadas, e moitas familias labregas vivían sempre á beira da pobreza.

O señor era tamén o xuíz na súa terra. Había xa un século que mandaba unha nobreza nova, máis violenta ca a de antes, e o país enchérase de fortalezas. Algunhas eran das grandes casas nobres, como a de Lemos ou a de Andrade. Outras eran dos bispos e, sobre todo, do arcebispo de Compostela.

Desde aquelas torres, dicían os vasalos, viñan os males e os danos. Moitos anos despois, as testemuñas aínda lles chamaban refuxios de malfeitores.

Non era a primeira vez que a xente se xuntaba contra os señores. Unhas décadas antes, os vasalos dun gran señor das Mariñas formaran unha irmandade e camiñaran xuntos cara a Compostela. Aquela primeira irmandade foi vencida, e os que a formaran foron castigados.

Os tempos, ademais, eran difíciles, porque desde a peste negra as rendas dos señores viñan minguando en toda Europa. E, como cobraban menos, moitos señores esixían cada vez máis aos seus vasalos. Así, pouco a pouco, nas casas e nos camiños, ía medrando a memoria daquelas irmandades, coma unha semente que agarda outra primavera.

---

## Notas del constructor (añadidas a mano, fuera del informe automático; en castellano)

- **Ejecución**: `pipeline.py temas/irmandinos-apertura.yaml --saida plan-de-negocio/gauntlet2/video --traballo <vacío>`,
  un solo comando, sin intervención humana entre la ficha y el MP4. `time` del proceso completo: 21 min 31 s de
  reloj; 38 min 43 s user + 5 min 20 s sys = **0,73 h de CPU** (coincide con la suma por etapas). Máquina: 4 núcleos,
  15 GB, sin GPU. Coste económico: 0 € en licencias; la electricidad no se ha medido [S].
- **LLM**: las tres llamadas (guion, corrección, escenas) las respondió Claude Opus 5.5 en modo `manual`, siguiendo
  literalmente los prompts renderizados de `herramientas/pipeline/llm_pending/`; las respuestas quedan en
  `llm_cache/` con su hash. No es un modelo abierto ni se ha medido su tiempo: en producción hay que sustituirlo por un
  LLM local (p. ej. Carballo de Nós) y repetir este QA.
- **Versión anterior**: la primera ejecución (19:19) salió NON PUBLICABLE por desfase A/V de 0,15 s (el `-shortest`
  de ffmpeg recortaba el vídeo) y con ritmo de 143 palabras/min. Corregido: sin `-shortest`, pausas más largas y
  escala 1,25; ahora desfase 0,01 s y 124 palabras/min, dentro del objetivo 110-125 de `referencia.md`.
- **Lo que las puertas automáticas no ven** (revisado a ojo en la hoja de contactos, no bloquea el veredicto):
  anacronismos leves en las imágenes (ventanas de cristal y cortinas en el dormitorio, tejados de teja roja y algún
  ciprés en el castillo de 0:50 y la aldea de 2:10), la multitud de 1:10 lleva útiles que pueden leerse como picas, y
  el castillo cambia de forma entre escenas (coherencia débil, como en la referencia). WER ASR 0,025 mide que se
  entiende, no que la prosodia sea natural; la naturalidad de la voz sigue pendiente del test ciego humano (D1/D2).
- **Si se regenera** con `--so-informe`, esta sección se pierde: volver a añadirla.
