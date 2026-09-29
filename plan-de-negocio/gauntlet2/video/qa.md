# QA automático: A Revolta Irmandiña, contada para durmir (irmandinos-apertura)

Informe xerado por `herramientas/pipeline/pipeline.py` (etapa 8). Ningunha persoa revisou o vídeo, o guion nin as imaxes.

**Veredicto automático: NON PUBLICABLE** (10/12 portas)

| Porta | Resultado |
|---|---|
| llm_local_desatendido | pasa |
| duracion | pasa |
| wer_mestura | pasa |
| sincronia_av | pasa |
| sincronia_subtitulos | pasa |
| lingua_lt | FALLA |
| h1_ancoraxe | FALLA |
| estilo | pasa |
| imaxes_revisadas | pasa |
| sonoridade | pasa |
| peso | pasa |
| resolucion | pasa |

## Execución

Backend LLM: `openai`; modelo(s): `eurollm-9b-instruct-2512-q4km`. Chamadas ao LLM: 28, das que 0 feitas nesta execución e 28 lidas da caché do directorio de traballo. Todas as respostas do LLM veñen do servidor local (ningunha escrita a man nin por un LLM externo).

Nota sobre esta execución: execución desatendida nun directorio de traballo baleiro co LLM local (un só comando). Relanzouse o mesmo comando no mesmo directorio catro veces por cambios de código, sen tocar ningún resultado a man: (1) ás 22:29 UTC, tras a etapa 3, para corrixir o corte de planos da etapa 4 (quedaban planos de 30 s); a chamada de escenas interrompida, uns 9 min de parede, non está contabilizada; (2) ás 23:01 UTC, tras a etapa 5, para engadir á porta de imaxes intentos de reserva co prompt xenérico e non contar as vidreiras góticas (stained glass) como xanelas modernas; (3) ás 23:17 UTC, porque a montaxe quedou bloqueada ao facer fork dun proceso con SDXL e Florence-2 cargados (a etapa de imaxes pasou a un proceso fillo; ata tres intentos de reserva); (4) ás 23:22 UTC, porque ao mirar as imaxes aprobadas vimos dous esqueletos xigantes e unha fogueira grande que a lista de anacronismos non cubría: engadíronse esqueletos, caveiras, cadáveres e lumes grandes no exterior, e todas as imaxes gardadas volvéronse revisar coa lista nova. As etapas xa feitas lense da caché do directorio (xeradas nesta execución polo LLM local) e os seus tempos consérvanse en tempos.json; as montaxes interrompidas (uns 20 min) non están contabilizadas.


## Ficheiro

| Medida | Valor |
|---|---|
| mb | 30.4 |
| resolucion | 1920x1080 |
| fps | 24.0 |
| pista_subtitulos | True |
| dur_video_s | 203.83 |
| dur_audio_s | 203.86 |
| dur_prevista_s | 203.85 |
| desfase_av_s | 0.03 |
| lufs_integrado | -17.1 |
| lra_lu | 6.2 |
| pico_real_dbtp | -1.0 |
| ritmo global (palabras/min, pausas incluídas) | 151.5 |
| ritmo do gancho (primeiras 150 palabras) | 142.3 |
| planos no primeiro minuto | 9 |
| planos en total | 24 |

## ASR (Whisper large-v3-turbo galego de Nós, CTranslate2 int8)

| Audio | WER | Subst. | Borr. | Ins. | Palabras ref. |
|---|---|---|---|---|---|
| mestura | 0.026 | 5 | 4 | 4 | 492 |
| voz | 0.102 | 5 | 45 | 0 | 492 |

Sincronía subtítulos-voz (marcas de tempo por palabra do ASR contra o SRT): 100.0 % das 483 palabras aliñadas caen dentro da súa frase (±0,5 s); desfase no inicio de frase: mediana -0.36 s, máximo 0.59 s (25 frases medidas).

Frases con WER > 0,5 (candidatas a erro de pronuncia): ningunha.

<details><summary>Transcrición ASR da mestura</summary>

Boas noites. A voz que vas escoitar é sintética e este texto preparouno un proceso automático. Os campesiños, mariñeiros e artesáns uníronse contra os señores das fortaleiras. A xente común botou abaixo torres con paus e pedras. Os nobres tiñan poder, pero a irmandade venceu. A rocha forte caeu baixo as súas mans. Un exército de xente diversa derrubou castelos. as fortaleiras perderon fronte á Unión Popular. Isto é serán, historia de Galicia para durmir. Esta noite viaxamos no tempo para descubrir unha historia esquecida de Galicia, a Revolta dos Irmandiños, un movemento sen precedentes que entre mil catrocentos sesenta e sete e mil catrocentos sesenta e nove botou abaixo moitas das fortalezas que dominaban o territorio. Xuntáronse labregos, artesáns, mariñeiros, burgueses, clérigos e parte da pequena nobreza para derrubar os castelos do señeño.  os señores, acusados de abusos e violencia. Estás a punto de embarcarche nunha viaxe tranquila pola historia de Galicia. Acomódate, apaga as luces e deixa que o aire che acompañe mentres escoitas esta historia dos irmandiños. Na primavera de 1467, un grupo diverso de xente, labregos, artesáns, mariñeiros e algúns nobres uníronse para derrubar os castelos que dominaban o país. Botaron abaixo moitas fortalezas, aproveitando a chuvia e o vento que mollan as pedras. as. A luz do sol rompe entre as ruínas, mentres o lume arde nos camiños abandonados. As pedras molladas polo chuvia e o vento caeron baixo as ferramentas dos irmandiños. A luz do sol filtraba entre os escombros, iluminando camiños esquecidos onde o lume ardeu en silencio. Cando o ceo se fundía coas chairas, os homes labraban a terra con ferramentas de ferro e madeira baixo un sol que filtraba entre as herbas altas. as. Algunhas casas tiñan tellados de lousa ou palla e os teitos goteaban lentamente sobre as pedras dos chans onde o lume ardeu en silencio durante séculos, deixando pegadas nas paredes como cicatrices da historia. O vento arrastraba o cheiro á terra mollada entre as pedras, mentres os homes camiñaban xuntos baixo un ceo que parecía esvarar sobre os tellados de palla. as chaves da rocha forte caeron unha tras outra e cada golpe soaba como se o tempo mesmo se desfacía en anacos. A auga goteaba das teituras rachadas, mesturándose coa area dos camiños, mentres as sombras alongábanse entre os muros derrubados. Os labregos con aixadas e picos, os artesáns coas súas ferramentas de ferro, os mariñeiros co seu remos convertidos en armas, os burgueses coa súa contabilidade de loitas, os clérigos coas súas mans sobre as campás das igrexas e ata algúns da pequena nobreza que souberon guiar o lume dos fachós entre as pedras xuntáronse nunha soa voz. O vento arrastraba a chuvia polos camiños empedrados, mentres o lume das antorchas iluminaba os rostros cansos de todos eles, unidos baixo un mesmo ceo roto polo ruído constante da caída dos tellados e as paredes que se esgadanaban coma se o mundo tentase esquecer o seu propio peso.

</details>

## Guion: validación automática e revisións do LLM

- bloque_gancho: 2 intento(s); problemas por intento: [1, 0]
- bloque_resumo: 3 intento(s); problemas por intento: [5, 1, 3]; quedan: Parte esta frase, que é longa de máis: Esta noite viaxamos no tempo para descubrir unha historia esquecida de Galicia: a revolta dos irmandiños, un movemento sen precedentes que entre mil catrocentos sesenta e sete e mil catrocentos sesenta e nove botou abaixo moitas das fortalezas que dominaban o territorio. | Parte esta frase, que é longa de máis: A súa loita marcou unha época na que a unión entre clases sociais foi clave para desafiar un sistema opresor, deixando pegada en testemuños como o Preito Tabera-Fonseca, onde centos de vellos recordaron os feitos de mozos. | Parte esta frase, que é longa de máis: Aínda que os señores recuperaron o control e as fortalezas volveron erguerse, a memoria da revolta quedou gravada na paisaxe e na historia oral dunha terra que buscaba xustiza entre pedras caídas.
- bloque_invitacion: 2 intento(s); problemas por intento: [1, 0]
- bloque_parrafo (feito 5): 3 intento(s); problemas por intento: [1, 1, 1]; quedan: seiscentos setenta e nove non está nos feitos: quítao.
- bloque_parrafo (feito 7): 3 intento(s); problemas por intento: [1, 1, 0]
- bloque_parrafo (feito 10): 3 intento(s); problemas por intento: [2, 1, 1]; quedan: Parte esta frase, que é longa de máis: As casas, con tellados que goteaban lentamente sobre os chans onde arderon fogueiras en noites sen nome, seguían alí, testemuñas mudas dunha revolta que fixo caer fortalezas baixo marteladas e ferramentas dos irmandiños.
- bloque_parrafo (feito 4): 1 intento(s); problemas por intento: [0]
- bloque_parrafo (feito 6): 3 intento(s); problemas por intento: [3, 3, 3]; quedan: Non repitas frases que xa se dixeron antes: Os labregos con aixadas e picos, os artesáns coas súas ferramentas de ferro, os mariñeiros cos seus remos convertidos en armas, os burgueses coa súa contabilidade de loitas, os clérigos coas súas mans sobre as campás das igrexas, e ata algúns da pequena nobreza que souberon guiar o lume dos fachós entre as pedras, xuntáronse nunha soa voz. As chaves da Rocha Forte caeron unha tras outra, e cada golpe soaba como se o tempo mesmo se desfacía en anacos. | Parte esta frase, que é longa de máis: O lume das candeas e as antorchas iluminaba os rostros cansos de todos eles, unidos baixo un mesmo ceo roto polo ruído constante da caída dos tellados e as paredes que se esgadanaban coma se o mundo tentase esquecer o seu propio peso. | Parte esta frase, que é longa de máis: Os labregos con aixadas e picos, os artesáns coas súas ferramentas de ferro, os mariñeiros cos seus remos convertidos en armas, os burgueses coa súa contabilidade de loitas, os clérigos coas súas mans sobre as campás das igrexas, e ata algúns da pequena nobreza que souberon guiar o lume dos fachós entre as pedras, xuntáronse nunha soa voz.

Feitos do dossier escollidos polo LLM para o gancho: {'resposta_llm': 'Aquí tes os tres feitos que máis poderían sorprender a unha persoa de hoxe e que mellor fan un contraste entre o pasado e o presente:  \n\n**3, 6, 17**  \n\n### **Explicación:**  \n- **3.', 'usados': [3, 6, 17]}.

Feitos do dossier escollidos polo LLM para o relato: {'resposta_llm': '5, 7, 10, 4, 6', 'escollidos_llm': [5, 7, 10, 4, 6], 'usados': [5, 7, 10, 4, 6], 'reserva': False}.

O código engadiu ou fixou o aviso e a fórmula literais: si.

## Lingua (LanguageTool 6.8 gl-ES, con hunspell galego)

Avisos antes da corrección automática: 11. Despois: 11. Corrección do LLM: [{'parrafo': 1, 'avisos_antes': 2, 'avisos_despois': 8, 'aceptada': False}, {'parrafo': 2, 'avisos_antes': 2, 'avisos_despois': 2, 'aceptada': False}, {'parrafo': 6, 'avisos_antes': 1, 'avisos_despois': 6, 'aceptada': False}, {'parrafo': 7, 'avisos_antes': 2, 'avisos_despois': 4, 'aceptada': False}, {'parrafo': 8, 'avisos_antes': 4, 'avisos_despois': 24, 'aceptada': False}].

- antes: `HUNSPELL_RULE` Atopouse un posíbel erro ortográfico — "...artesáns uníronse contra os señores das fortaleiras. A xente común botou abaixo torres con ..."
- antes: `HUNSPELL_RULE` Atopouse un posíbel erro ortográfico — "... de xente diversa derrubou castelos. As fortaleiras perderon fronte á unión popular.  Isto ..."
- antes: `GENERAL_VERB_AGREEMENT_ERRORS` Posíbel erro de concordancia verbal. — "...Serán, historia de Galicia para durmir. Esta noite viaxamos no tempo para descubrir unha historia e..."
- antes: `GENERAL_NUMBER_AGREEMENT_ERRORS` Posíbel erro de concordancia de número. — "... a revolta dos irmandiños, un movemento sen precedentes que entre mil catrocentos sesenta e set..."
- antes: `GL_BARBARISM_REPLACE` 'ceo' é un xenismo. É preferíbel dicir "director executivo" — "...onde o lume ardeu en silencio.  Cando o ceo se fundía coas chairas, os homes labrab..."
- antes: `GL_BARBARISM_REPLACE` 'ceo' é un xenismo. É preferíbel dicir "director executivo" — "...tres os homes camiñaban xuntos baixo un ceo que parecía esvarar sobre os tellados d..."
- antes: `HUNSPELL_RULE` Atopouse un posíbel erro ortográfico — "... desfacía en anacos. A auga goteaba das teituras rachadas, mesturándose coa area dos cam..."
- antes: `HUNSPELL_RULE` Atopouse un posíbel erro ortográfico — "...a nobreza que souberon guiar o lume dos fachós entre as pedras, xuntáronse nunha soa v..."
- antes: `HUNSPELL_RULE` Atopouse un posíbel erro ortográfico — "... camiños empedrados, mentres o lume das antorchas iluminaba os rostros cansos de todos el..."
- antes: `GL_BARBARISM_REPLACE` 'ceo' é un xenismo. É preferíbel dicir "director executivo" — "...os de todos eles, unidos baixo un mesmo ceo roto polo ruído constante da caída dos ..."
- antes: `HUNSPELL_RULE` Atopouse un posíbel erro ortográfico — "... caída dos tellados e as paredes que se esgadanaban coma se o mundo tentase esquecer o seu ..."
- despois: `HUNSPELL_RULE` Atopouse un posíbel erro ortográfico — "...artesáns uníronse contra os señores das fortaleiras. A xente común botou abaixo torres con ..."
- despois: `HUNSPELL_RULE` Atopouse un posíbel erro ortográfico — "... de xente diversa derrubou castelos. As fortaleiras perderon fronte á unión popular.  Isto ..."
- despois: `GENERAL_VERB_AGREEMENT_ERRORS` Posíbel erro de concordancia verbal. — "...Serán, historia de Galicia para durmir. Esta noite viaxamos no tempo para descubrir unha historia e..."
- despois: `GENERAL_NUMBER_AGREEMENT_ERRORS` Posíbel erro de concordancia de número. — "... a revolta dos irmandiños, un movemento sen precedentes que entre mil catrocentos sesenta e set..."
- despois: `GL_BARBARISM_REPLACE` 'ceo' é un xenismo. É preferíbel dicir "director executivo" — "...onde o lume ardeu en silencio.  Cando o ceo se fundía coas chairas, os homes labrab..."
- despois: `GL_BARBARISM_REPLACE` 'ceo' é un xenismo. É preferíbel dicir "director executivo" — "...tres os homes camiñaban xuntos baixo un ceo que parecía esvarar sobre os tellados d..."
- despois: `HUNSPELL_RULE` Atopouse un posíbel erro ortográfico — "... desfacía en anacos. A auga goteaba das teituras rachadas, mesturándose coa area dos cam..."
- despois: `HUNSPELL_RULE` Atopouse un posíbel erro ortográfico — "...a nobreza que souberon guiar o lume dos fachós entre as pedras, xuntáronse nunha soa v..."
- despois: `HUNSPELL_RULE` Atopouse un posíbel erro ortográfico — "... camiños empedrados, mentres o lume das antorchas iluminaba os rostros cansos de todos el..."
- despois: `GL_BARBARISM_REPLACE` 'ceo' é un xenismo. É preferíbel dicir "director executivo" — "...os de todos eles, unidos baixo un mesmo ceo roto polo ruído constante da caída dos ..."
- despois: `HUNSPELL_RULE` Atopouse un posíbel erro ortográfico — "... caída dos tellados e as paredes que se esgadanaban coma se o mundo tentase esquecer o seu ..."

## H1: nomes e cantidades ancorados no dossier

4 elementos, 75.0 % ancorados. Sen ancorar: "mil catrocentos sesenta e sete un".

## Estilo e densidade (regras do canal)

| Control | Valor |
|---|---|
| palabras | 492 |
| palabras_obxectivo | 500 |
| desvio_palabras_pct | -1.6 |
| cifras | [] |
| signos_prohibidos | [] |
| preguntas | 0 |
| palabras_vetadas | [] |
| aviso_literal | True |
| formula_literal | True |
| frases_fora_8_25 | [7, 8, 10, 14, 19, 20, 21, 24, 25] |
| nomes_propios_distintos | ['Forte', 'Galicia', 'Rocha', 'Serán'] |
| max_nomes_novos_por_110_palabras | 2 |

## Son

| Medida | Valor |
|---|---|
| lufs_voz_obxectivo | -17.0 |
| choiva_rel_db | -17.0 |
| lufs_mestura_pyloudnorm | -17.1 |
| pico | 0.89 |

## Porta de imaxes (revisor.py: MediaPipe mans/corpo + Florence-2 e lista de anacronismos)

24 planos, 43 imaxes xeradas (19 rexeneracións). Aprobadas á primeira: 18; aprobadas tras rexenerar: 6; sen aprobar: 0.

| Plano | Intentos | Problemas nos intentos rexeitados | Escollida |
|---|---|---|---|
| 0 | 1 | - | 0 (ok) |
| 1 | 1 | - | 0 (ok) |
| 2 | 2 | 0: armas | 1 (ok) |
| 3 | 1 | - | 0 (ok) |
| 4 | 1 | - | 0 (ok) |
| 5 | 1 | - | 0 (ok) |
| 6 | 6 | 0: lume grande no exterior; 1: lume grande no exterior; 2: lume grande no exterior; 3: lume grande no exterior; 4: lume grande no exterior | 5 (ok) |
| 7 | 2 | - | 0 (ok) |
| 8 | 1 | - | 0 (ok) |
| 9 | 2 | 0: morte | 1 (ok) |
| 10 | 1 | - | 0 (ok) |
| 11 | 1 | - | 0 (ok) |
| 12 | 1 | - | 0 (ok) |
| 13 | 1 | - | 0 (ok) |
| 14 | 1 | - | 0 (ok) |
| 15 | 1 | - | 0 (ok) |
| 16 | 8 | 0: interior moderno, texto na imaxe; 1: obxectos modernos, texto na imaxe; 2: texto na imaxe; 3: texto na imaxe; 4: texto na imaxe; 5: tellados laranxas; 6: tellados laranxas | 7 (ok) |
| 17 | 1 | - | 0 (ok) |
| 18 | 1 | - | 0 (ok) |
| 19 | 1 | - | 0 (ok) |
| 20 | 1 | - | 0 (ok) |
| 21 | 5 | - | 0 (ok) |
| 22 | 1 | - | 0 (ok) |
| 23 | 1 | - | 0 (ok) |

## Planos e imaxes

| # | Inicio | Frases | Dur. (s) | Mov. | Lum. | Contr. | Simil. ant. | Descrición do revisor (Florence-2) | Prompt do LLM |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 0:00 | 1-2 | 10.4 | zoom_in | 85.3 | 31.3 | None | The image shows a group of medieval knights gathered in a field with a castle in the background. The castle is made of stone and has a flagpole with a flag flying in front of it. The sky is cloudy and the ground is covered in green grass. The knights are dressed in traditional medieval clothing, with helmets and armor, and some are holding swords and shields. They appear to be engaged in a conversation. There are baskets of food and other items scattered around the field. The overall mood of the image is tense and somber. | **A diverse group of peasants, artisans, and nobles gather to dismantle a fortress under stormy skies** |
| 1 | 0:10 | 3-3 | 5.2 | pan_right | 89.7 | 41.0 | 0.24 | The image shows a group of men standing in a ruined street. The street is covered in rubble and debris, with wooden planks and rubble scattered around. In the background, there is a large stone building with a tower and a cloudy sky. The men are dressed in medieval-style clothing and appear to be engaged in a conversation. One of the men is holding a wooden cross, while the others are looking at it intently. The overall mood of the image is somber and desolate. | **Laborers with wooden beams and stone hammers demolish the tower’s base in a rain-soaked courtyard** |
| 2 | 0:15 | 4-5 | 7.3 | zoom_out | 76.7 | 30.9 | 0.39 | The image shows a group of men dressed in medieval clothing and helmets, engaged in a battle. They are standing in front of a stone wall, which appears to be part of a fort or a castle. The men are holding wooden sticks and ropes, and some are using them to secure themselves to the wall. The sky is blue and there are mountains in the background. The overall mood of the image is tense and action-packed. | **Multitudes toppling granite walls with ropes, sledgehammers, and pickaxes at dawn** |
| 3 | 0:22 | 6-7 | 6.8 | pan_left | 112.7 | 41.7 | 0.25 | The image shows a group of medieval knights on horseback in front of a castle. The knights are dressed in full armor and helmets, and some are holding swords and shields. The castle is made of stone and has multiple towers and arches. The sky is cloudy and there is a dust cloud in the air, suggesting that the knights are in the midst of a battle. The ground is covered in rocks and there are trees in the background. The overall mood of the image is tense and action-packed. | **Armed villagers scale a crumbling keep while nobles flee on horseback through mist** |
| 4 | 0:29 | 8-9 | 8.4 | zoom_in | 111.1 | 48.1 | 0.21 | The image shows a group of medieval knights marching on a hill with a castle in the background. The knights are dressed in full armor and helmets, and some are holding flags and banners. The hill is covered in greenery and there are several buildings and structures scattered around. The sky is blue and the overall mood of the image is one of strength and determination. The image appears to be a scene from a medieval battle or battle. | **A fractured fortress looms over a village square where rebels hoist banners of unity** |
| 5 | 0:38 | 10-10 | 7.0 | pan_up | 96.7 | 39.4 | 0.14 | The image shows a group of people walking through an old, dilapidated castle ruins. The ruins are made of stone and appear to be in a state of disrepair, with broken windows and crumbling walls. The sky is a hazy orange color, indicating that the photo was taken at sunrise or sunset. The people in the image are dressed in medieval-style clothing, with some wearing long robes and others wearing cloaks. They are walking on a cobblestone path, and there are a few people visible in the background. The overall mood of the image is somber and desolate | **Time-travelers stand before the ruins as dusk paints the sky in amber and slate gray** |
| 6 | 0:45 | 10-10 | 7.2 | zoom_in | 106.3 | 41.7 | 0.32 | The image shows a group of people walking on a cobblestone street in a medieval village. The street is lined with stone buildings on both sides and there is a tall tower in the background. The tower appears to be made of stone and has a pointed top. The people are dressed in long robes and are walking in a line, with some walking towards the tower. The sky is overcast and there are trees and hills in the distance. The overall mood of the image is somber and contemplative. | **Crowds surround a burning keep, torches casting jagged shadows on mossy stones at nightfall** |
| 7 | 0:52 | 11-11 | 4.7 | pan_right | 50.5 | 26.8 | 0.18 | The image shows a group of people gathered in a large room with arches and stained glass windows. The room appears to be a medieval or medieval castle with a high ceiling and stone floor. The people are dressed in dark robes and are gathered around a table with a fire burning on it. Some of them are holding candles, while others are looking at the fire. The overall mood of the image is somber and contemplative. | **A council of rebels debates strategy by candlelight inside a half-ruined chapel’s nave** |
| 8 | 0:57 | 11-11 | 5.1 | zoom_out | 82.6 | 44.3 | 0.21 | The image shows a group of men dressed in medieval clothing standing in a courtyard with stone walls and arches. The men are dressed in red robes and helmets, and some are holding swords and shields. They appear to be engaged in a conversation, with one man in the center holding a sword and another holding a shield. The courtyard is cobblestone and there are other people in the background. The overall mood of the image is tense and somber. | **Nobles in chainmail and velvet cloaks surrender keys to masons armed with sledgehammers** |
| 9 | 1:02 | 12-12 | 4.9 | pan_left | 78.4 | 32.4 | 0.28 | The image shows the ruins of an old, dilapidated building with arches and pillars. The building appears to be in a state of disrepair, with broken walls and debris scattered around the area. The sky is orange and yellow, indicating that it is either sunrise or sunset. In the background, there is a cityscape with buildings and a bridge visible. The overall mood of the image is one of destruction and devastation. | **Sunrise glints off rainwater pooling around the collapsed keep’s skeletal remains** |
| 10 | 1:07 | 13-13 | 6.9 | zoom_in | 64.5 | 46.2 | 0.38 | The image is a photograph of a castle on top of a hill at sunset. The sky is a beautiful orange and pink color, with the sun setting in the background. The castle is made of stone and has two towers with pointed roofs and turrets. The hill is covered in trees and shrubs, and there are a few other buildings scattered around the base of the castle. The overall mood of the image is peaceful and serene. | **A lone figure sketches the fortress’s silhouette against a blood-orange horizon at dusk** |
| 11 | 1:13 | 14-14 | 5.0 | pan_up | 125.9 | 45.4 | 0.53 | The image shows a group of men on a longboat on a river. The boat is made of wood and has multiple masts and rigging. The men are dressed in traditional clothing and hats, and some are sitting on the deck while others are standing on the bow of the boat. They appear to be engaged in a conversation. In the background, there is a foggy landscape with a castle-like structure on a hill and trees on the other side of the river. On the left side, there are stacks of logs and a wooden pier. The sky is overcast and the overall | **Boatmen unload timber from sloops in a fog-draped estuary where stone towers jut like teeth** |
| 12 | 1:19 | 14-14 | 5.2 | zoom_in | 84.9 | 38.0 | 0.39 | The image shows a group of monks gathered around a large wooden structure made of sticks and ropes. The structure appears to be a medieval castle or fort, with a stone facade and a tower in the background. The monks are wearing traditional robes and are gathered around the structure, which is made up of multiple wooden poles and ropes that are tied together to form a structure. The sky is cloudy and the ground is covered in dirt and debris. The overall mood of the image is somber and contemplative. | **Fisherfolk haul nets while monks chant psalms beside a half-demolished watchtower’s base** |
| 13 | 1:24 | 15-15 | 6.0 | pan_right | 85.7 | 42.0 | -0.02 | The image shows a group of men gathered around a stone archway in an old stone building. The archway is made of stone and has a medieval-style design. The men are dressed in medieval clothing and are engaged in a conversation. They are standing around a table with various tools and equipment on it, including a large pot, a bucket, and a wooden bench. In the background, there is a castle-like structure with a tower and a hill in the distance. The sky is blue and the overall mood of the image is peaceful and serene. | **A blacksmith forges weapons under the fortress’s shattered archway as villagers watch in silence** |
| 14 | 1:30 | 16-17 | 12.1 | zoom_out | 90.3 | 37.0 | 0.24 | The image shows a group of children walking through an old, dilapidated church with arches and ruins. The children are dressed in medieval-style clothing and are carrying weapons, including swords and shields. The church appears to be in ruins, with broken windows and debris scattered on the ground. The sky is overcast and the overall mood of the image is somber. | **Children chase crows through rubble where once stood a lord’s throne room and torture rack** |
| 15 | 1:42 | 18-18 | 7.6 | pan_left | 53.0 | 32.2 | 0.2 | The image shows a group of men dressed in black robes standing in a large room with high ceilings and arched windows. The room appears to be a church or cathedral with stone walls and arches. The men are gathered around a wooden table with a lit candle on it, and there are several other candles on the table. Some of the men are holding candles in their hands, while others are looking at the candle. The floor is covered in fallen leaves and there is a chandelier hanging from the ceiling. The overall mood of the image is somber and contemplative. | **Monks tend to wounded rebels by lantern-light inside a chapel strewn with broken siege gear** |
| 16 | 1:49 | 19-19 | 9.7 | zoom_in | 100.7 | 33.9 | 0.07 | The image shows a group of people walking on a cobblestone pathway in a medieval village. The pathway is lined with stone buildings on both sides, with a stone tower on the left side. The buildings appear to be old and weathered, with some of them having a sloping roof. In the background, there is a green landscape with rolling hills and fields. The sky is overcast and the overall mood of the image is somber. The people in the image are dressed in dark robes, suggesting that they are monks or nuns. | **A scribe records the rebellion in a candlelit scriptorium surrounded by torn parchment maps** |
| 17 | 1:59 | 20-20 | 13.8 | pan_up | 82.7 | 31.5 | 0.45 | The image shows a group of people gathered around a large stone castle. The castle appears to be old and weathered, with multiple towers and arches. The sky is blue and the ground is covered in rubble and debris. The people are dressed in medieval clothing and some are holding swords and shields. There are clothes hanging out to dry on a clothesline in front of the castle, suggesting that it is being used for a battle or demonstration. The overall mood of the image is tense and somber. | **Weavers stitch banners of defiance beneath a fortress’s collapsed gatehouse at twilight** |
| 18 | 2:13 | 21-21 | 9.8 | zoom_in | 82.6 | 35.8 | 0.3 | The image shows a group of people gathered in a courtyard with a stone building in the background. There are six people in the image, all dressed in medieval clothing, standing in front of a stone archway. They are holding baskets of plants and appear to be engaged in a conversation.

In the center of the group, there is an elderly woman with white hair and a white headscarf, who is holding a basket of plants. She is smiling and seems to be explaining something to the group. To her left, there are two men, one wearing a black hat and the | **An old woman sells herbs to rebels outside a half-standing tower where vines now choke the stones** |
| 19 | 2:23 | 22-23 | 18.9 | pan_right | 104.3 | 34.7 | 0.08 | The image shows a group of knights on horseback in a medieval battle scene. The knights are dressed in full armor and helmets, and are riding on a dirt path that winds through a grassy field. In the background, there is a large stone castle with a tower and a moat. The sky is blue and there are trees and bushes on either side of the path. The castle appears to be old and weathered, with some of the walls crumbling and others still intact. The horses are brown and white, and the riders are wearing helmets and armor. The scene is bustling with | **A lord in silver armor watches from horseback as peasants hurl boulders into a keep’s moat** |
| 20 | 2:42 | 24-24 | 9.3 | zoom_out | 74.1 | 38.5 | 0.15 | The image shows a group of men dressed in medieval clothing standing in a large room with arched windows. They are holding swords and appear to be engaged in a battle. The room is made of stone and has a wooden floor. The men are dressed in dark clothing and are standing in front of a wooden bench. The background shows a stone wall and a stone archway. The overall mood of the image is tense and intense. | **Carpenters nail planks across broken windows of a fortress chapel while guards surrender their swords** |
| 21 | 2:51 | 24-24 | 10.5 | pan_left | 51.5 | 26.7 | 0.13 | The image shows a group of people gathered in a large room with arches and stained glass windows. The room appears to be a medieval or medieval setting with stone walls and arches. The floor is made of stone and there are several tables and benches scattered throughout the room. On the left side of the image, there is a large table with a few people sitting at it, and on the right side, there are a few standing.

In the center of the room, a man is standing and holding a lit candle, casting a warm glow on the scene. He is wearing | **Burgesses tally spoils in ledgers by torchlight inside the keep’s vaulted treasury chamber** |
| 22 | 3:01 | 25-25 | 8.2 | zoom_in | 72.3 | 32.9 | 0.16 | The image shows a group of people gathered in a large room with high ceilings and arches. The room appears to be a church or cathedral, as there are large windows on the walls and a large pile of rubble in the center of the room. The people are dressed in medieval-style clothing, with some wearing red robes and others wearing blue robes. In the center, there is a man wearing a blue robe and a gold crown, standing in front of a large altar. He is holding a book and appears to have a serious expression on his face. On the left side of the | **A bishop blesses the rubble where once stood a lord’s throne room, now trampled like common soil** |
| 23 | 3:09 | 25-25 | 13.9 | pan_up | 93.3 | 39.5 | 0.16 | The image shows a group of medieval knights marching on a cobblestone street in front of a castle. The knights are dressed in full armor and helmets, and some are carrying swords and shields. The castle walls are made of stone and there is a flagpole with a flag flying in the background. The sky is blue and the overall mood of the image is tense and action-packed. | **Rebels march past a crumbling keep as dawn bleeds gold through gaps in its shattered walls** |

## Tempos (CPU: 4 núcleos, sen GPU)

| Etapa | Parede (s) | CPU (s) | dos que servidor LLM (s) |
|---|---|---|---|
| 1_guion | 1229.6 | 3927.0 | 3926.5 |
| 2_corrixir | 538.4 | 1535.3 | 1081.9 |
| 3_voz | 329.2 | 313.7 |  |
| 4_escenas | 351.5 | 1068.2 | 1068.2 |
| 5_imaxes | 2643.8 | 8699.1 |  |
| 6_son | 37.1 | 37.0 |  |
| 7_montaxe | 279.9 | 1047.3 |  |
| 8_qa | 94.4 | 243.8 |  |
| **Total** | **5503.9** | **16871.4** | **6076.6** |

Tempo total de CPU: 4.69 h de núcleo (das que LLM local: 1.69 h); parede: 91.7 min. Inclúe o LLM local e o arranque do seu servidor; non inclúe a descarga de modelos.

## LLM (chamadas)

| Chamada | Caché | Segundos | Tokens entrada/saída | Tokens/s saída | CPU servidor (s) |
|---|---|---|---|---|---|
| bloque_seleccion_gancho_1 | `bloque_seleccion_gancho-09e6427ede81.txt` (da caché) | 87.8 | 703/60 | 0.68 | 320.0 |
| bloque_gancho_1 | `bloque_gancho-e1846f753038.txt` (da caché) | 36.6 | 369/110 | 3.01 | 109.0 |
| bloque_gancho_2 | `bloque_gancho-b4f5163146b7.txt` (da caché) | 26.6 | 405/83 | 3.12 | 78.7 |
| bloque_resumo_1 | `bloque_resumo-4051c9a393d0.txt` (da caché) | 104.9 | 814/315 | 3.0 | 325.9 |
| bloque_resumo_2 | `bloque_resumo-695a69d768dc.txt` (da caché) | 188.0 | 1027/113 | 0.6 | 680.5 |
| bloque_resumo_3 | `bloque_resumo-466b8cd35705.txt` (da caché) | 113.0 | 904/285 | 2.52 | 347.5 |
| bloque_invitacion_1 | `bloque_invitacion-02dbaed5de01.txt` (da caché) | 19.2 | 174/58 | 3.03 | 57.5 |
| bloque_invitacion_2 | `bloque_invitacion-608c9275c53e.txt` (da caché) | 15.9 | 209/48 | 3.01 | 45.9 |
| bloque_seleccion_1 | `bloque_seleccion-9773347bef2f.txt` (da caché) | 36.7 | 799/14 | 0.38 | 124.4 |
| bloque_parrafo_1 | `bloque_parrafo-1935d76d5be6.txt` (da caché) | 48.4 | 460/89 | 1.84 | 157.5 |
| bloque_parrafo_2 | `bloque_parrafo-b410fe5e14d3.txt` (da caché) | 32.1 | 497/89 | 2.77 | 91.2 |
| bloque_parrafo_3 | `bloque_parrafo-9a205757d14a.txt` (da caché) | 45.2 | 512/107 | 2.37 | 140.8 |
| bloque_parrafo_4 | `bloque_parrafo-7404892dffde.txt` (da caché) | 41.0 | 391/46 | 1.12 | 134.8 |
| bloque_parrafo_5 | `bloque_parrafo-5e9f97986436.txt` (da caché) | 25.1 | 467/60 | 2.39 | 81.2 |
| bloque_parrafo_6 | `bloque_parrafo-07ef84b8c6c5.txt` (da caché) | 30.8 | 447/49 | 1.59 | 101.1 |
| bloque_parrafo_7 | `bloque_parrafo-798f64e4108d.txt` (da caché) | 45.7 | 415/143 | 3.13 | 141.9 |
| bloque_parrafo_8 | `bloque_parrafo-d3bfad040f95.txt` (da caché) | 34.1 | 555/88 | 2.58 | 102.8 |
| bloque_parrafo_9 | `bloque_parrafo-c09ca4418e94.txt` (da caché) | 53.0 | 495/185 | 3.49 | 156.8 |
| bloque_parrafo_10 | `bloque_parrafo-1bc637d9ba50.txt` (da caché) | 34.0 | 444/104 | 3.06 | 110.1 |
| bloque_parrafo_11 | `bloque_parrafo-82e734598aaf.txt` (da caché) | 41.7 | 442/162 | 3.89 | 134.1 |
| bloque_parrafo_12 | `bloque_parrafo-14137d14a507.txt` (da caché) | 69.7 | 816/191 | 2.74 | 222.9 |
| bloque_parrafo_13 | `bloque_parrafo-4319ee1fb1fe.txt` (da caché) | 65.3 | 770/219 | 3.35 | 211.7 |
| corrixir_parrafo_1 | `corrixir_parrafo-6e8ec15a5bff.txt` (da caché) | 37.0 | 343/135 | 3.65 | 119.3 |
| corrixir_parrafo_2 | `corrixir_parrafo-bc9262d32f76.txt` (da caché) | 46.3 | 385/124 | 2.68 | 137.7 |
| corrixir_parrafo_6 | `corrixir_parrafo-5d5382f10933.txt` (da caché) | 94.4 | 284/172 | 1.82 | 326.5 |
| corrixir_parrafo_7 | `corrixir_parrafo-d264a498a7e9.txt` (da caché) | 46.3 | 373/138 | 2.98 | 140.4 |
| corrixir_parrafo_8 | `corrixir_parrafo-0017b4a3f611.txt` (da caché) | 117.2 | 561/363 | 3.1 | 358.0 |
| escenas_1 | `escenas-99eda97ad201.txt` (da caché) | 327.3 | 1984/690 | 2.11 | 1068.2 |

## Extrapolación a un episodio de 60 min [S: escala lineal dos tempos medidos]

Supostos: mesma densidade de texto e de planos que esta mostra (o gancho só está ao principio, así que un episodio longo ten planos máis longos de media e isto sobreestima as imaxes), custo proporcional á duración en todas as etapas (tamén o LLM: guion e escenas por bloques), carga dos modelos unha vez.

| Etapa | Parede (min) | CPU (h de núcleo) |
|---|---|---|
| 1_guion | 362 | 19.27 |
| 2_corrixir | 158 | 7.53 |
| 3_voz | 97 | 1.54 |
| 4_escenas | 103 | 5.24 |
| 5_imaxes | 778 | 42.68 |
| 6_son | 11 | 0.18 |
| 7_montaxe | 82 | 5.14 |
| 8_qa | 28 | 1.20 |
| **Total** | **1620** (27.0 h) | **82.77** |

## Guion final narrado

Boas noites. A voz que vas escoitar é sintética, e este texto preparouno un proceso automático.

Os campesiños, mariñeiros e artesáns uníronse contra os señores das fortaleiras. A xente común botou abaixo torres con paus e pedras. Os nobres tiñan poder, pero a irmandade venceu. A Rocha Forte caeu baixo as súas mans. Un exército de xente diversa derrubou castelos. As fortaleiras perderon fronte á unión popular.

Isto é Serán, historia de Galicia para durmir. Esta noite viaxamos no tempo para descubrir unha historia esquecida de Galicia: a revolta dos irmandiños, un movemento sen precedentes que entre mil catrocentos sesenta e sete e mil catrocentos sesenta e nove botou abaixo moitas das fortalezas que dominaban o territorio. Xuntáronse labregos, artesáns, mariñeiros, burgueses, clérigos e parte da pequena nobreza para derrubar os castelos dos señores, acusados de abusos e violencia.

Estás a punto de embarcarche nunha viaxe tranquila pola historia de Galicia. Acomódate, apaga as luces e deixa que o aire che acompañe mentres escoitas esta historia dos irmandiños.

Na primavera de mil catrocentos sesenta e sete, un grupo diverso de xente, labregos, artesáns, mariñeiros e algúns nobres, uníronse para derrubar os castelos que dominaban o país. Botaron abaixo moitas fortalezas, aproveitando a chuvia e o vento que mollan as pedras. A luz do sol rompe entre as ruínas, mentres o lume arde nos camiños abandonados.

As pedras, molladas polo chuvia e o vento, caeron baixo as ferramentas dos irmandiños. A luz do sol filtraba entre os escombros, iluminando camiños esquecidos onde o lume ardeu en silencio.

Cando o ceo se fundía coas chairas, os homes labraban a terra con ferramentas de ferro e madeira baixo un sol que filtraba entre as herbas altas. Algunhas casas tiñan tellados de lousa ou palla, e os teitos goteaban lentamente sobre as pedras dos chans, onde o lume ardeu en silencio durante séculos, deixando pegadas nas paredes como cicatrices da historia.

O vento arrastraba o cheiro a terra mollada entre as pedras, mentres os homes camiñaban xuntos baixo un ceo que parecía esvarar sobre os tellados de palla. As chaves da Rocha Forte caeron unha tras outra, e cada golpe soaba como se o tempo mesmo se desfacía en anacos. A auga goteaba das teituras rachadas, mesturándose coa area dos camiños, mentres as sombras alongábanse entre os muros derrubados.

Os labregos, con aixadas e picos, os artesáns coas súas ferramentas de ferro, os mariñeiros cos seus remos convertidos en armas, os burgueses coa súa contabilidade de loitas, os clérigos coas súas mans sobre as campás das igrexas, e ata algúns da pequena nobreza que souberon guiar o lume dos fachós entre as pedras, xuntáronse nunha soa voz. O vento arrastraba a chuvia polos camiños empedrados, mentres o lume das antorchas iluminaba os rostros cansos de todos eles, unidos baixo un mesmo ceo roto polo ruído constante da caída dos tellados e as paredes que se esgadanaban coma se o mundo tentase esquecer o seu propio peso.
