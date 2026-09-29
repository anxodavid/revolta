# QA automático: A Revolta Irmandiña, contada para durmir (irmandinos-apertura)

Informe xerado por `herramientas/pipeline/pipeline.py` (etapa 8). Ningunha persoa revisou o vídeo.

**Veredicto automático: NON PUBLICABLE**

| Porta | Resultado |
|---|---|
| duracion | pasa |
| wer_mestura | pasa |
| sincronia_av | FALLA |
| sincronia_subtitulos | pasa |
| lingua_lt | pasa |
| estilo | pasa |
| sonoridade | pasa |
| peso | pasa |
| resolucion | pasa |

## Ficheiro

| Medida | Valor |
|---|---|
| mb | 31.0 |
| resolucion | 1920x1080 |
| fps | 24.0 |
| pista_subtitulos | True |
| dur_video_s | 203.37 |
| dur_audio_s | 203.52 |
| dur_prevista_s | 209.53 |
| desfase_av_s | 0.15 |
| lufs_integrado | -18.0 |
| lra_lu | 5.7 |
| pico_real_dbtp | -2.0 |
| ritmo (palabras/min sobre a narración, pausas incluídas) | 142.8 |

## ASR (Whisper large-v3-turbo galego de Nós, CTranslate2 int8)

| Audio | WER | Subst. | Borr. | Ins. | Palabras ref. |
|---|---|---|---|---|---|
| mestura | 0.023 | 5 | 2 | 4 | 475 |
| voz | 0.082 | 6 | 32 | 1 | 475 |

Sincronía subtítulos-voz (marcas de tempo por palabra do ASR contra o SRT): 99.8 % das 468 palabras aliñadas caen dentro da súa frase (±0,5 s); desfase no inicio de frase: mediana -0.26 s, máximo 1.39 s (31 frases medidas).

Frases con WER > 0,5 (candidatas a erro de pronuncia): ningunha.

<details><summary>Transcrición ASR da mestura</summary>

as noites, a voz que vas escoitar é sintética e este texto preparouno un proceso automático. Ao sur de Compostela hai un outeiro verde e nas mañás do outono a brétema queda alí moito tempo. Dentro as árbores asoman unhas pedras vellas, cubertas de musgo e de follas molladas. Son os restos dunha fortaleza, uns anacos de muralla e a planta dos muros debuxada no chan. árona do mar. Hoxe só se escoita a choiva lenta sobre as follas e, lonxe, algún paxaro. Aquela fortaleza chamábase a Rocha Forte e era do arcebispo de Compostela. Desde ela vixiábanse os camiños que baixaban cara ao mar. Un día, a xente da cidade e os labregos da comarca decidiron que aquela torre xa non tiña que seguir en pé e botárona abaixo. Isto é serán, historia de Galicia para durmir.  Esta noite imos contar a historia dos irmandiños. Durante uns poucos anos labregos, artesáns, mariñeiros, clérigos e mesmo algúns fidalgos xuntáronse nunha irmandade e botaron abaixo moitas das torres do país. Falaremos da vida baixo aquelas torres e dos tempos difíciles que viñeran antes. E, xa cara ao final, lembrarémolo que contaron moito despois os vellos que o viran de mozos.  Non tes que lembrar nada do que che conte. Acomódate, apaga a luz aínda está acesa e deixa que o corpo pese un pouco máis. Deixa tamén que a respiración vaia máis amodo e imos alá, a aquel tempo. Arredor da metade do século XV, Galicia era unha terra de labregos, de artesáns, de mariñeiros e de mercadores. Moitos deles vivían nas terras dun señor e eran os seus vasalos. Pagábanlle tributos en diñeiro e en especie e debíanlle traballo nas obras da fortaleza e servizo coas armas. E eran cargas pesadas e moitas familias labregas vivían sempre á beira da pobreza. O señor era tamén o xuíz na súa terra. Había xa un século que mandaba unha nobreza nova, máis violenta ca a de antes, e o país enchérase de fortalezas. Algunhas eran das grandes casas nobres, como a de Lemos ou a de Andrade.  Outras eran dos bispos e, sobre todo, do arcebispo de Compostela. Desde aquelas torres, dicían os vasalos, viñan os males e os danos. Moitos anos despois, as testemuñas aínda lles chamaban refuxios de malfeitores. Non era a primeira vez que a xente se xuntaba contra os señores. Unhas décadas antes, os vasalos dun gran señor das Mariñas formaran unha irmandade e camiñaran xuntos cara a Compostela.  Aquela primeira irmandade foi vencida e os que a formaran foron castigados. Os tempos, ademais, eran difíciles porque desde a peste negra as rendas dos señores viñan minguando en toda Europa. E, como cobraban menos, moitos señores esixían cada vez máis aos seus vasalos. Así, pouco a pouco, nas casas e nos camiños, ía medrando a memoria daquelas irmandades, coma unha semente que agarda outra primavera.

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
| lufs_voz_obxectivo | -21.0 |
| choiva_rel_db | -17.0 |
| lufs_mestura_pyloudnorm | -18.0 |
| pico | 0.792 |

## Escenas e imaxes

| # | Frases | Dur. (s) | Mov. | Lum. | Contr. | Simil. ant. | Prompt |
|---|---|---|---|---|---|---|---|
| 0 | 1-3 | 19.0 | zoom_in | 117.1 | 47.1 | None | wide view at dawn of a green wooded hill south of Santiago de Compostela, thick morning fog lying in the valley, oak and chestnut trees, faint grey stones on the hilltop, pale golden light |
| 1 | 4-6 | 18.8 | pan_right | 86.9 | 37.5 | 0.39 | ruins of a medieval granite wall among oak trees, stones covered in green moss and wet fallen leaves, low foundations of walls outlined on the ground, light rain, soft grey daylight |
| 2 | 7-8 | 9.8 | zoom_out | 101.5 | 46.6 | 0.24 | a stone castle with two square towers on a hill, seen from far away, dirt roads winding down through green valleys toward a distant estuary and the Atlantic sea, calm late afternoon light |
| 3 | 9-10 | 13.6 | pan_up | 133.7 | 59.7 | 0.65 | a large crowd of peasants and townspeople seen from behind, walking slowly up a misty hillside path at dawn carrying wooden tools, a dark castle silhouette above them in the fog |
| 4 | 11-12 | 14.0 | pan_left | 108.6 | 37.9 | 0.38 | a medieval village square of granite houses with slate roofs, small groups of peasants, craftsmen, fishermen and a monk in a brown habit gathered and talking quietly, seen from a distance, overcast morning |
| 5 | 13-14 | 13.4 | zoom_in | 35.1 | 22.9 | 0.0 | interior of a humble stone house at night, an old man seen from behind sitting by the hearth fire, warm orange firelight on rough granite walls, wooden bench, clay pots |
| 6 | 15-17 | 15.5 | zoom_in | 35.5 | 25.8 | -0.1 | a quiet medieval bedroom at night, simple wooden bed with wool blankets, a single candle on a stool, small window with rain drops and blue night outside, warm dim light |
| 7 | 18-19 | 12.2 | pan_right | 133.1 | 49.0 | -0.14 | wide landscape of the Galician countryside in the fifteenth century, small fields and stone walls, a hamlet with thatched roofs and a granite granary on stilts, a river estuary with small fishing boats in the distance, soft morning mist |
| 8 | 20-21 | 13.8 | pan_left | 102.0 | 41.0 | 0.09 | peasants seen from behind carrying sacks of grain and baskets along a muddy track toward a stone tower house, oxen cart, autumn trees, overcast grey sky |
| 9 | 22-23 | 11.1 | zoom_out | 95.6 | 42.1 | 0.07 | a tall square stone tower house of a lord dominating a green valley at dusk, small peasant houses below, smoke from chimneys, cold blue and violet evening light |
| 10 | 24-25 | 10.9 | pan_right | 98.2 | 43.7 | 0.66 | a great medieval castle with high granite walls and towers on a rocky hill above a river, and far away the towers of a Romanesque cathedral in a walled city, golden evening light, clouds |
| 11 | 26-27 | 11.3 | zoom_in | 63.9 | 38.4 | 0.64 | a dark stone fortress tower at night under a cloudy sky with a pale moon, below it a few peasant houses with small warm lit windows, quiet and still, fog on the ground |
| 12 | 28-30 | 18.4 | pan_left | 136.6 | 53.5 | 0.46 | a long line of peasants walking together along a muddy road through fog, seen from behind and far away, toward a distant walled medieval city with cathedral towers, grey morning light |
| 13 | 31-32 | 13.7 | zoom_out | 104.3 | 32.6 | 0.59 | empty autumn fields and an abandoned farmhouse of granite with a collapsed roof, bare trees, grey low clouds, crows in the sky, melancholic quiet atmosphere |
| 14 | 33-33 | 14.0 | zoom_in | 76.1 | 38.8 | 0.02 | close view of weathered hands of a peasant woman placing seeds into a small clay jar on a wooden table, warm hearth light, a window showing a spring morning with blossoming trees |

## Tempos de render (CPU: 4 núcleos, sen GPU)

| Etapa | Parede (s) | CPU (s) |
|---|---|---|
| 1_guion | 0.0 | 0.0 |
| 2_corrixir | 19.5 | 43.0 |
| 3_escenas | 0.0 | 0.0 |
| 4_voz | 222.7 | 202.9 |
| 5_imaxes | 321.2 | 1167.6 |
| 6_son | 5.2 | 5.1 |
| 7_montaxe | 284.9 | 1062.6 |
| 8_qa | 128.3 | 237.0 |
| **Total** | **981.8** | **2718.2** |

Tempo total de CPU: 0.76 h de núcleo; parede: 16.4 min. Non inclúe a descarga de modelos nin o tempo do LLM externo (ver LLM).

## LLM

| Etapa | Caché | Metadatos |
|---|---|---|
| guion | `guion-86cb43ec62b3.txt` | backend: manual, model: Claude Opus 5.5 (claude-opus-5-5) actuando como LLM do pipeline, data: 2026-09-29, nota: Resposta escrita seguindo literalmente o prompt renderizado (llm_pending/guion-86cb43ec62b3.prompt.md), sen edición humana. |
| corrixir | `corrixir-29a6ee9f9e7b.txt` | backend: manual, model: Claude Opus 5.5 (claude-opus-5-5) actuando como LLM do pipeline, data: 2026-09-29, nota: Resposta ao prompt renderizado llm_pending/corrixir-29a6ee9f9e7b.prompt.md: acepta REFLEXIVOS (demorarse -> queda); considera falsos positivos a concordancia de Esta noite imos, e camiñaran xuntos (suxeito os vasalos). |
| escenas | `escenas-11c8e046d451.txt` | backend: manual, model: Claude Opus 5.5 (claude-opus-5-5) actuando como LLM do pipeline, data: 2026-09-29, nota: Resposta ao prompt renderizado llm_pending/escenas-11c8e046d451.prompt.md, sen edición humana. |

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
