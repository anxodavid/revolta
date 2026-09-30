# QA automático: A Revolta Irmandiña, contada para durmir (irmandinos-apertura)

Informe xerado por `herramientas/pipeline/pipeline.py` (etapa 8). Ningunha persoa revisou o vídeo, o guion nin as imaxes.

**Veredicto automático: PUBLICABLE** (13/13 portas)

| Porta | Resultado |
|---|---|
| llm_local_desatendido | pasa |
| duracion | pasa |
| wer_mestura | pasa |
| sincronia_av | pasa |
| sincronia_subtitulos | pasa |
| lingua_lt | pasa |
| h1_ancoraxe | pasa |
| veracidade | pasa |
| estilo | pasa |
| imaxes_revisadas | pasa |
| sonoridade | pasa |
| peso | pasa |
| resolucion | pasa |

## Execución

Backend LLM: `openai`; modelo(s): `eurollm-9b-instruct-2512-q4km`. Chamadas ao LLM: 64, das que 1 feitas nesta execución e 63 lidas da caché do directorio de traballo. Todas as respostas do LLM veñen do servidor local (ningunha escrita a man nin por un LLM externo).

Servidor LLM arrancado polo propio pipeline: {'arranque_s': 20.1, 'arranque_cpu_s': 32.3, 'comando': '/tmp/claude-0/-home-user-revolta/2e7d1051-da1e-54e9-bb2d-6cd0b746c55a/scratchpad/llm/venv/bin/python -m llama_cpp.server --model /tmp/claude-0/-home-user-revolta/2e7d1051-da1e-54e9-bb2d-6cd0b746c55a/scratchpad/llm/eurollm-9b-instruct-2512.Q4_K_M.gguf --model_alias eurollm-9b-instruct-2512-q4km --n_ctx 8192 --n_threads 4 --use_mmap false --host 127.0.0.1 --port 8080'}.

Nota sobre esta execución: Ronda 3: execución desatendida nun directorio de traballo baleiro co LLM local (un só comando). Relanzouse unha vez o mesmo comando no mesmo directorio porque a etapa 3 (voz) morreu por falta de memoria (o servidor LLM, o NLI e LanguageTool seguían cargados); corrixiuse o código para paralos antes da voz. As etapas 1 e 2 lense da caché desta mesma execución (xeradas polo LLM local) e os seus tempos consérvanse en tempos.json; ningún texto nin imaxe se tocou a man.


## Ficheiro

| Medida | Valor |
|---|---|
| mb | 28.3 |
| resolucion | 1920x1080 |
| fps | 24.0 |
| pista_subtitulos | True |
| dur_video_s | 191.0 |
| dur_audio_s | 191.01 |
| dur_prevista_s | 191.01 |
| desfase_av_s | 0.01 |
| lufs_integrado | -17.2 |
| lra_lu | 7.9 |
| pico_real_dbtp | -0.7 |
| ritmo global (palabras/min, pausas incluídas) | 131.5 |
| ritmo do gancho (primeiras 150 palabras) | 139.5 |
| planos no primeiro minuto | 11 |
| planos en total | 29 |

## ASR (Whisper large-v3-turbo galego de Nós, CTranslate2 int8)

| Audio | WER | Subst. | Borr. | Ins. | Palabras ref. |
|---|---|---|---|---|---|
| mestura | 0.037 | 6 | 4 | 5 | 400 |
| voz | 0.172 | 8 | 58 | 3 | 400 |

Sincronía subtítulos-voz (marcas de tempo por palabra do ASR contra o SRT): 99.7 % das 390 palabras aliñadas caen dentro da súa frase (±0,5 s); desfase no inicio de frase: mediana -0.31 s, máximo 2.07 s (25 frases medidas).

Frases con WER > 0,5 (candidatas a erro de pronuncia): ningunha.

<details><summary>Transcrición ASR da mestura</summary>

as noites, a voz que vas escoitar é sintética e este texto preparouno un proceso automático. Dicían que eran refuxios de malfeitores. Ás fortalezas derrubadas non se volveron levantar todas. Isto é serán, historia de Galicia para durmir. Acomódate, apaga a luz e respira amodo. Non tes que lembrar nada do que escoites, deixa que a historia pase coma a chuvia na xanela.  Desde a peste negra as rendas dos señores minguaban en toda Europa e a presión señorial sobre os vasalos aumentaba. Arredor da metade do século XV, Galicia era unha sociedade de labregos, artesáns, mariñeiros e mercadores, moitos eran vasalos dun señor. A xente de Galicia botou abaixo moitas fortalezas dos señores. Os vasalos pagaban tributos en diñeiro e en especie e debían servizos persoais, traballo nas fortalezas e servizo de armas. as familias labregas vivían ao limiar da pobreza. O señor era tamén xuíz no seu señorío. Desde había un século mandaba unha nobreza nova, máis violenta e o reino encheirase de fortalezas. Había fortalezas das grandes casas nobres, como Lemos ou Andrade, de bispos e, sobre todo do arcebispo de Compostela. Botáronse abaixo moitas fortalezas por mandato dunha irmandade que, entre as primaveras de mil catrocentos sesenta e sete e mil catro  no catrocentos sesenta e nove, botou abaixo moitas fortalezas. Unhas décadas antes, os vasalos dun gran señor das Mariñas formaran unha irmandade e marcharan cara a Compostela, foi vencida e castigada. Despois houbo outras irmandades locais e comarcais e algunha derrubou fortalezas. Desde a rocha forte asegurábanse os camiños que ían cara a Pontevedra, Padrón, Muros, Noia e Fisterra cara ao mar. A rocha forte era do arcebispo de Compostela. Na Irmandade xuntáronse labregos, artesáns, mariñeiros, burgueses, clérigos, cóengos e monxes e parte da pequena nobreza que achegou experiencia militar. Decididos os veciños da cidade e os labregos da comarca botaron abaixo a rocha forte. Para os Irmandiños derrubaron moitas das fortalezas do reino.  En 1469 houbo unha reacción armada dos señores, que regresaron. Os señores regresaron coas súas tropas e a irmandade foi derrotada. Despois da derrota, o castigo non foron tanto as execucións como os tributos e o traballo que os vasalos tiveron que dar durante anos para reconstruír as fortalezas derrubadas. as. En entre mil cincocentos vinte e seis e mil cincocentos vinte e sete, douscentas catro testemuñas vellas declararon ante escribáns no preito Taveira Fonseca, lembrando co que viran de mozos.

</details>

## Guion: validación automática e revisións do LLM

- bloque_gancho: 1 intento(s); problemas por intento: [0]
- bloque_resumo: 3 intento(s); problemas por intento: [2, 2, 2]; **rexeitado o texto do LLM, vai a reserva (omitido)**. Problemas do mellor intento: Parte esta frase, que é longa de máis: Esta noite imos escoitar un episodio sobre a irmandade dos irmandiños, que entre as primaveras de mil catrocentos sesenta e sete e mil catrocentos sesenta e nove botou abaixo moitas fortalezas de Galicia. | Esta frase non se pode afirmar co dossier (fala de persoas, nomes, tempo longo ou desenlace sen apoio no dossier): Esta noite imos escoitar un episodio sobre a irmandade dos irmandiños, que entre as primaveras de mil catrocentos sesenta e sete e mil catrocentos sesenta e nove botou abaixo moitas fortalezas de Galicia.
- invitacion: 0 intento(s); problemas por intento: [0]
- bloque_parrafo (feito 1): 3 intento(s); problemas por intento: [4, 2, 5]; **rexeitado o texto do LLM, vai a reserva (mixta (frases do LLM que pasan + feitos literais))**. Problemas do mellor intento: Galiza non está nos feitos: quítao. | Esta frase non se pode afirmar co dossier (quen fixo que non coincide co dossier (señores + xunta); fala de persoas, nomes, tempo longo ou desenlace sen apoio no dossier): Os labregos de Galiza, fartos da tiranía dos señores, xuntáronse en irmandade e derruíron moitas fortalezas.
- bloque_parrafo (feito 2): 3 intento(s); problemas por intento: [2, 1, 2]; **rexeitado o texto do LLM, vai a reserva (mixta (frases do LLM que pasan + feitos literais))**. Problemas do mellor intento: Ten que ter polo menos 2 frases.
- bloque_parrafo (feito 3): 3 intento(s); problemas por intento: [1, 1, 1]; **rexeitado o texto do LLM, vai a reserva (mixta (frases do LLM que pasan + feitos literais))**. Problemas do mellor intento: Ten que ter polo menos 2 frases.
- bloque_parrafo (feito 4): 3 intento(s); problemas por intento: [1, 2, 2]; **rexeitado o texto do LLM, vai a reserva (mixta (frases do LLM que pasan + feitos literais))**. Problemas do mellor intento: Ten que ter polo menos 2 frases.
- bloque_parrafo (feito 5): 3 intento(s); problemas por intento: [1, 4, 5]; **rexeitado o texto do LLM, vai a reserva (mixta (frases do LLM que pasan + feitos literais))**. Problemas do mellor intento: Ten que ter polo menos 2 frases.
- bloque_parrafo (feito 6): 3 intento(s); problemas por intento: [3, 3, 3]; **rexeitado o texto do LLM, vai a reserva (literal)**. Problemas do mellor intento: Ten que ter polo menos 2 frases. | Esta frase non se pode afirmar co dossier (fala de persoas, nomes, tempo longo ou desenlace sen apoio no dossier): Os irmandiños botaron abaixo moitas fortalezas en Galicia entre as primaveras de mil catrocentos sesenta e sete e mil catrocentos sesenta e nove. | O parágrafo non conta o feito que se pediu: cóntao con palabras parecidas ás do feito.
- bloque_parrafo (feito 7): 3 intento(s); problemas por intento: [2, 1, 3]; **rexeitado o texto do LLM, vai a reserva (mixta (frases do LLM que pasan + feitos literais))**. Problemas do mellor intento: Ten que ter polo menos 2 frases.
- bloque_parrafo (feito 9): 3 intento(s); problemas por intento: [2, 2, 2]; **rexeitado o texto do LLM, vai a reserva (literal)**. Problemas do mellor intento: Esta frase non se pode afirmar co dossier (desenlace que non está no dossier (vencidos)): Os vasalos dunha xurisdición das Mariñas formaron unha irmandade e marcharan cara a Compostela, pero foron vencidos e castigados. | Esta frase non se pode afirmar co dossier (fala de persoas, nomes, tempo longo ou desenlace sen apoio no dossier): Despois houbo outras conxuncións locais e comarcais que derrubaron fortalezas de señores e bispos en Galicia.
- bloque_parrafo (feito 10): 3 intento(s); problemas por intento: [1, 2, 2]; **rexeitado o texto do LLM, vai a reserva (mixta (frases do LLM que pasan + feitos literais))**. Problemas do mellor intento: Ten que ter polo menos 2 frases.
- bloque_parrafo (feito 11): 3 intento(s); problemas por intento: [1, 4, 4]; **rexeitado o texto do LLM, vai a reserva (mixta (frases do LLM que pasan + feitos literais))**. Problemas do mellor intento: Esta frase non se pode afirmar co dossier (fala de persoas, nomes, tempo longo ou desenlace sen apoio no dossier): Os campesiños derrubaron os castelos dos señores.
- bloque_parrafo (feito 12): 3 intento(s); problemas por intento: [2, 1, 1]; **rexeitado o texto do LLM, vai a reserva (omitido)**. Problemas do mellor intento: Non repitas frases que xa se dixeron antes: Os irmandiños derrubaron moitas fortalezas en Galicia entre as primaveras de mil catrocentos sesenta e sete e mil catrocentos sesenta e nove. A Rocha Forte era do arcebispo de Compostela.
- bloque_parrafo (feito 13): 3 intento(s); problemas por intento: [1, 1, 1]; **rexeitado o texto do LLM, vai a reserva (literal)**. Problemas do mellor intento: O parágrafo non conta o feito que se pediu: cóntao con palabras parecidas ás do feito.
- bloque_parrafo (feito 14): 3 intento(s); problemas por intento: [1, 1, 1]; **rexeitado o texto do LLM, vai a reserva (mixta (frases do LLM que pasan + feitos literais))**. Problemas do mellor intento: Ten que ter polo menos 2 frases.
- bloque_parrafo (feito 15): 3 intento(s); problemas por intento: [2, 1, 1]; **rexeitado o texto do LLM, vai a reserva (mixta (frases do LLM que pasan + feitos literais))**. Problemas do mellor intento: Ten que ter polo menos 2 frases.
- bloque_parrafo (feito 16): 3 intento(s); problemas por intento: [3, 3, 3]; **rexeitado o texto do LLM, vai a reserva (literal)**. Problemas do mellor intento: Ten que ter polo menos 2 frases. | Esta frase non se pode afirmar co dossier (quen fixo que non coincide co dossier (señores + derru)): Os señores regresaron co seu exército e derrubaron as fortalezas dos irmandiños. | O parágrafo non conta o feito que se pediu: cóntao con palabras parecidas ás do feito.
- bloque_parrafo (feito 17): 3 intento(s); problemas por intento: [1, 5, 4]; **rexeitado o texto do LLM, vai a reserva (mixta (frases do LLM que pasan + feitos literais))**. Problemas do mellor intento: Ten que ter polo menos 2 frases.
- bloque_parrafo (feito 18): 3 intento(s); problemas por intento: [1, 1, 1]; **rexeitado o texto do LLM, vai a reserva (mixta (frases do LLM que pasan + feitos literais))**. Problemas do mellor intento: Ten que ter polo menos 2 frases.
- bloque_parrafo (feito 20): 3 intento(s); problemas por intento: [1, 3, 3]; **rexeitado o texto do LLM, vai a reserva (mixta (frases do LLM que pasan + feitos literais))**. Problemas do mellor intento: Esta frase non se pode afirmar co dossier (desenlace que non está no dossier (sometid, sometidas); fala de persoas, nomes, tempo longo ou desenlace sen apoio no dossier): As fortalezas derrubadas, os castelos esnaquizados e as terras sometidas volveron erguerse baixo o peso do traballo forzado dos vasalos.
- bloque_parrafo (feito 21): 3 intento(s); problemas por intento: [1, 1, 1]; **rexeitado o texto do LLM, vai a reserva (omitido)**. Problemas do mellor intento: Non repitas frases que xa se dixeron antes: Os irmandiños derrubaron moitas fortalezas de Galicia entre as primaveras do ano catrocentos sesenta e sete e o ano catrocentos sesenta e nove. Ao sur de Compostela hai un outeiro con restos da fortaleza da Rocha Forte: anacos de muralla e a planta dos muros entre a vexetación; o sitio está en ruínas.

Feitos do dossier escollidos polo LLM para o gancho: {'resposta_llm': '8, 19', 'usados': [8, 19]}.

Feitos do dossier escollidos polo LLM para o relato: {'resposta_llm': '9, 12, 4, 7, 8  \n\n**Explicación:**  \nOs feitos seleccionados abarcan a orixe do conflito (fortalezas como símbolos de opresión), o contexto histórico previo (nobreza violenta e presión señorial) e os eventos clave da revolta irmandiña. A cronoloxía mantense desde as raíces medievais ata', 'escollidos_llm': [9, 12, 4, 7, 8], 'usados': [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21], 'reserva': True, 'engadidos_pola_extension': [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12]}.

O código engadiu ou fixou o aviso e a fórmula literais: si.

## Lingua (LanguageTool 6.8 gl-ES, con hunspell galego)

Avisos antes da corrección automática: 0. Despois: 0. Corrección do LLM: non fixo falta.


## H1: nomes e cantidades ancorados no dossier

17 elementos, 100.0 % ancorados. Sen ancorar: ningún.

## Veracidade (veracidade.py: NLI mDeBERTa-v3 multilingüe + coincidencia léxica + regras de desenlace)

24 frases avaliadas; con problemas: 0. Modo gancho: todas as frases apoiadas nun feito (NLI >= 0,6 e coincidencia >= 0,6, ou coincidencia >= 0,8, ou frase literal do dossier). Modo relato: as frases con persoas, nomes, tempo longo ou desenlace, apoiadas (coincidencia >= 0,5 co NLI); sen frases de ambiente; o parágrafo conta o seu feito. En todos: desenlace coa mesma forma ca no dossier e quen fixo que (clase do actor de cada verbo de acción) coma no dossier.

| Par. | Modo | Frase | NLI | Coincid. | Feitos de apoio | Resultado |
|---|---|---|---|---|---|---|
| 1 | gancho | Dicían que eran refuxios de malfeitores. | 0.996 | 1.0 | [8, 12] | ok |
| 1 | gancho | As fortalezas derrubadas non se volveron levantar todas. | 0.999 | 1.0 | [19, 18] | ok |
| 3 | invitacion | Acomódate, apaga a luz e respira amodo. | 0.981 | 0.0 | [17, 2] | ok |
| 3 | invitacion | Non tes que lembrar nada do que escoites: deixa que a historia pase coma a chuvia na xanela. | 0.493 | 0.0 | [14] | ok |
| 4 | relato | Desde a peste negra as rendas dos señores minguaban en toda Europa e a presión señorial sobre os vasalos aumentaba. | 1.0 | 1.0 | [1] | ok |
| 5 | relato | Arredor da metade do século quince, Galicia era unha sociedade de labregos, artesáns, mariñeiros e mercadores; moitos eran vasalos dun señor. | 1.0 | 1.0 | [2] | ok |
| 5 | relato | A xente de Galicia botou abaixo moitas fortalezas dos señores. | 0.901 | 0.5 | [18, 2] | ok |
| 6 | relato | Os vasalos pagaban tributos en diñeiro e en especie e debían servizos persoais: traballo nas fortalezas e servizo de armas. | 1.0 | 1.0 | [3] | ok |
| 7 | relato | As familias labregas vivían ao limiar da pobreza. | 0.98 | 1.0 | [4, 14] | ok |
| 8 | relato | O señor era tamén xuíz no seu señorío. | 1.0 | 1.0 | [5] | ok |
| 9 | relato | Desde había un século mandaba unha nobreza nova, máis violenta, e o reino enchérase de fortalezas. | 1.0 | 1.0 | [6] | ok |
| 10 | relato | Había fortalezas das grandes casas nobres, como Lemos ou Andrade, de bispos e, sobre todo, do arcebispo de Compostela. | 1.0 | 1.0 | [7] | ok |
| 10 | relato | Botáronse abaixo moitas fortalezas por mandato dunha irmandade que, entre as primaveras de mil catrocentos sesenta e sete e mil catrocentos sesenta e nove, botou abaixo moitas fortalezas. | 0.977 | 0.55 | [12, 20] | ok |
| 11 | relato | Unhas décadas antes, os vasalos dun gran señor das Mariñas formaran unha irmandade e marcharan cara a Compostela; foi vencida e castigada. | 1.0 | 1.0 | [9] | ok |
| 11 | relato | Despois houbo outras irmandades locais e comarcais, e algunha derrubou fortalezas. | 1.0 | 1.0 | [9] | ok |
| 12 | relato | Desde a Rocha Forte asegurábanse os camiños que ían cara a Pontevedra, Padrón, Muros, Noia e Fisterra, cara ao mar. | 1.0 | 1.0 | [10] | ok |
| 13 | relato | A Rocha Forte era do arcebispo de Compostela. | 1.0 | 1.0 | [11] | ok |
| 14 | relato | Na irmandade xuntáronse labregos, artesáns, mariñeiros, burgueses, clérigos, cóengos e monxes, e parte da pequena nobreza, que achegou experiencia militar. | 1.0 | 1.0 | [13] | ok |
| 15 | relato | Decididos os veciños da cidade e os labregos da comarca, botaron abaixo a Rocha Forte. | 0.984 | 0.89 | [14, 10] | ok |
| 16 | relato | Os irmandiños derrubaron moitas das fortalezas do reino. | 1.0 | 1.0 | [15] | ok |
| 17 | relato | En mil catrocentos sesenta e nove houbo unha reacción armada dos señores, que regresaron. | 1.0 | 1.0 | [16] | ok |
| 18 | relato | Os señores regresaron coas súas tropas e a irmandade foi derrotada. | 0.996 | 1.0 | [17, 16] | ok |
| 19 | relato | Despois da derrota o castigo non foron tanto as execucións como os tributos e o traballo que os vasalos tiveron que dar durante anos para reconstruír as fortalezas derrubadas. | 1.0 | 1.0 | [18] | ok |
| 20 | relato | Entre mil cincocentos vinte e seis e mil cincocentos vinte e sete, douscentas catro testemuñas vellas declararon ante escribáns no Preito Tabera-Fonseca, lembrando co que viran de mozos. | 0.969 | 1.0 | [20] | ok |

## Estilo e densidade (regras do canal)

| Control | Valor |
|---|---|
| palabras | 399 |
| palabras_obxectivo | 500 |
| desvio_palabras_pct | -20.2 |
| cifras | [] |
| signos_prohibidos | [] |
| preguntas | 0 |
| palabras_vetadas | [] |
| aviso_literal | True |
| formula_literal | True |
| frases_fora_8_25 | [3, 6, 16, 26, 27] |
| nomes_propios_distintos | ['Andrade', 'Compostela', 'Europa', 'Fisterra', 'Fonseca', 'Forte', 'Galicia', 'Lemos', 'Mariñas', 'Muros', 'Noia', 'Padrón', 'Pontevedra', 'Preito', 'Rocha', 'Serán', 'Tabera'] |
| max_nomes_novos_por_110_palabras | 7 |

## Son

| Medida | Valor |
|---|---|
| lufs_voz_obxectivo | -17.0 |
| choiva_rel_db | -17.0 |
| lufs_mestura_pyloudnorm | -17.2 |
| pico | 0.89 |

## Porta de imaxes (revisor.py: MediaPipe mans/corpo + Florence-2 e lista de anacronismos)

29 planos, 63 imaxes xeradas (34 rexeneracións). Aprobadas á primeira: 18; aprobadas tras rexenerar: 11; sen aprobar: 0.

| Plano | Intentos | Problemas nos intentos rexeitados | Escollida |
|---|---|---|---|
| 0 | 6 | 0: balcóns, tellados laranxas, obxectos modernos; 1: tellados laranxas, obxectos modernos; 2: tellados laranxas; 3: tellados laranxas; 4: tellados laranxas | 5 (ok) |
| 1 | 1 | - | 0 (ok) |
| 2 | 1 | - | 0 (ok) |
| 3 | 1 | - | 0 (ok) |
| 4 | 1 | - | 0 (ok) |
| 5 | 1 | - | 0 (ok) |
| 6 | 1 | - | 0 (ok) |
| 7 | 5 | 0: tellados laranxas; 1: tellados laranxas; 2: tellados laranxas; 3: tellados laranxas | 4 (ok) |
| 8 | 1 | - | 0 (ok) |
| 9 | 1 | - | 0 (ok) |
| 10 | 1 | - | 0 (ok) |
| 11 | 2 | 0: interior moderno | 1 (ok) |
| 12 | 1 | - | 0 (ok) |
| 13 | 1 | - | 0 (ok) |
| 14 | 2 | 0: tellados laranxas | 1 (ok) |
| 15 | 6 | 0: lume grande no exterior; 1: obxectos modernos, multitude, lume grande no exterior; 2: multitude, lume grande no exterior; 3: violencia, multitude, lume grande no exterior; 4: violencia, multitude | 5 (ok) |
| 16 | 1 | - | 0 (ok) |
| 17 | 2 | 0: tellados laranxas | 1 (ok) |
| 18 | 1 | - | 0 (ok) |
| 19 | 1 | - | 0 (ok) |
| 20 | 3 | 0: man sen corpo (1), texto na imaxe; 1: man sen corpo (1) | 2 (ok) |
| 21 | 5 | 0: texto na imaxe; 1: texto na imaxe; 2: texto na imaxe; 3: interior moderno, texto na imaxe | 4 (ok) |
| 22 | 1 | - | 0 (ok) |
| 23 | 1 | - | 0 (ok) |
| 24 | 6 | 0: multitude; 1: multitude; 2: multitude, lume grande no exterior; 3: multitude; 4: multitude | 5 (ok) |
| 25 | 2 | 0: armas | 1 (ok) |
| 26 | 6 | 0: interior moderno, texto na imaxe; 1: interior moderno, texto na imaxe; 2: texto na imaxe; 3: texto na imaxe; 4: texto na imaxe | 5 (ok) |
| 27 | 1 | - | 0 (ok) |
| 28 | 1 | - | 0 (ok) |

## Planos e imaxes

| # | Inicio | Frases | Dur. (s) | Mov. | Lum. | Contr. | Simil. ant. | Descrición do revisor (Florence-2) | Prompt do LLM |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 0:00 | 1-2 | 10.3 | zoom_in | 105.6 | 30.5 | None | The image shows a group of people walking down a cobblestone street in a medieval village. The street is lined with stone buildings on both sides, with a stone wall on the left side and a stone building on the right side. In the background, there is a tall tower with a pointed roof and a cross on top. The sky is overcast and the overall mood of the image is gloomy. The people in the image appear to be dressed in medieval clothing, with some wearing cloaks and others wearing cloaking. | Peaceful village with a few figures walking along a dirt path, carrying tools and looking toward distant stone towers. |
| 1 | 0:10 | 3-4 | 7.4 | pan_right | 100.2 | 29.1 | 0.18 | The image is a painting of an old castle ruins on a hill. The castle is made of stone and is covered in ivy and greenery. The walls of the castle are made of cobblestones and there are two arches on either side of the entrance. The entrance is made up of stone pillars and arches, and there is a stone pathway leading up to it. In the background, there are rolling hills and fields, and the sky is cloudy. The overall mood of the image is gloomy and abandoned. | Abandoned fortress under stormy skies, weathered walls with ivy creeping up, no people visible. |
| 2 | 0:17 | 5-5 | 4.4 | zoom_out | 102.7 | 32.2 | 0.06 | The image is a painting of a group of people gathered around a table in a garden. The table is set up on a stone patio with a stone wall on the left side and a stone archway on the right side. In the background, there is a beautiful landscape with a river and a village on a hill. The sky is blue and there are mountains in the distance.

In the center of the painting, there are several people dressed in traditional clothing, including monks, nuns, and other religious figures. Some of the people are standing and some are sitting, while others are | Serán logo on screen with title text in Galician: "Historia de Galicia para durmir" (History of Galicia to sleep). |
| 3 | 0:22 | 6-6 | 3.6 | pan_left | 67.8 | 26.6 | -0.22 | The image is a painting of an old man sitting in a room with a fireplace. The man is wearing a long robe and has a long beard and is sitting on the floor in front of the fireplace. He is looking down at a small fire that is burning brightly in the center of the room. The room has a stone floor and a large window on the left side of the image. The walls are painted in a light green color and there is a wooden shelf on the right side with various items on it. The fireplace is lit with a warm glow and there are a few pieces of | A dimly lit room with a person sitting cross-legged by a hearth, candle flickering, no windows visible. |
| 4 | 0:25 | 7-7 | 5.6 | zoom_in | 100.0 | 33.1 | 0.01 | The image is a painting of a dirt road in a mountainous landscape. The road is surrounded by trees and shrubs on both sides, with a stone wall on the left side. The sky is cloudy and the overall mood of the painting is peaceful and serene. In the distance, there are rolling hills and valleys. Two people can be seen walking on the road, one wearing a hat and the other wearing a coat. The painting is done in a realistic style, with loose brushstrokes and vibrant colors. The overall mood is one of tranquility and serenity. | Autumn forest path at dusk, three figures walking silently toward a distant hilltop ruin. |
| 5 | 0:31 | 8-8 | 7.3 | pan_up | 92.3 | 30.0 | 0.15 | The image is a painting of a group of people gathered around a fire pit in an old stone building. The people are dressed in medieval clothing, with some wearing green robes and hats, and others wearing brown robes. The fire pit is made of metal and is burning brightly, with flames visible. The building in the background is made up of stone and has arched windows and arches. The sky is blue and there are mountains in the distance. The scene appears to be taking place in a medieval town or village. The overall mood of the image is one of reverence and devotion. | Crowd of peasants in woolen cloaks and tunics gathering outside a stone keep, some holding torches. |
| 6 | 0:38 | 9-9 | 4.3 | zoom_in | 103.6 | 31.1 | 0.3 | The image is a painting of a medieval castle gate. The gate is made of stone and has two arches, one on each side. The walls of the castle are made of cobblestones and there are two towers on either side of the gate. In the center of the image, there is a man standing with his arms outstretched, looking up at the sky. He is wearing a long robe and appears to be in a peaceful and contemplative pose. The sky is overcast and the overall mood of the painting is one of serenity and tranquility. | A lone figure standing before a weathered castle gate, arms raised as if swearing an oath. |
| 7 | 0:42 | 9-9 | 4.3 | pan_right | 103.1 | 31.4 | 0.04 | The image is a painting of a group of men working in an old town. The painting is done in a realistic style with loose brushstrokes and vibrant colors. The men are dressed in traditional clothing and hats, and some are holding tools such as hammers, saws, and a bucket. They are gathered around a small table with a fire burning on it. In the background, there are several buildings with thatched roofs and arched windows. The sky is blue and there are a few clouds in the sky. The ground is covered in cobblestones and there is a large | Muddy village square with a blacksmith hammering iron, smoke rising from his forge. |
| 8 | 0:47 | 10-10 | 5.0 | zoom_out | 105.5 | 28.1 | 0.28 | The image is a painting of a group of people walking on a cobblestone street. The street is lined with old stone buildings and there is a stone tower in the background. The people are dressed in traditional clothing, with some wearing hats and others wearing long robes. Some of them are carrying baskets of fruit or vegetables, while others are walking with their backs to the camera. The sky is overcast and the overall mood of the painting is peaceful and serene. The painting appears to be done in a realistic style, with vibrant colors and intricate details. | Peasants dragging stones toward a collapsed tower, shovels and baskets in hand. |
| 9 | 0:52 | 11-11 | 3.8 | pan_left | 107.8 | 27.5 | 0.17 | The image is a painting of a group of men walking on a dirt road in a rural area. The men are wearing traditional clothing and hats, and some are carrying a cart full of hay. The cart is pulled by two white oxen, and the oxen are pulling it along the road. The road is lined with tall green fields on both sides, and there are trees and hills in the background. The sky is cloudy and the overall mood of the painting is peaceful and serene. | A farmer leading oxen through a field of barley under an overcast sky, wooden cart loaded with grain. |
| 10 | 0:56 | 11-11 | 4.2 | zoom_in | 104.2 | 29.7 | 0.27 | The image is a painting of a group of men standing in front of a stone castle. The castle appears to be old and weathered, with broken walls and ruins. The men are dressed in traditional clothing, with some wearing hats and carrying bags. They are standing on a rocky hillside, with a dirt path leading up to the entrance of the castle. In the background, there are hills and a cloudy sky. The overall mood of the painting is one of abandonment and neglect. | Three laborers carrying sacks up a hill to a half-ruined watchtower, one leaning on a spade. |
| 11 | 1:00 | 12-13 | 8.1 | pan_up | 71.7 | 31.0 | 0.08 | The image is a painting of an elderly woman sitting at a table in a room with a fireplace. She is wearing a green robe and has white hair. The woman is holding a pair of knitting needles and appears to be working on a piece of fabric. The table is covered with a blue cloth and there is a lit candle on the left side of the table. The room has a stone wall and a window on the right side. The overall mood of the painting is peaceful and serene. | An old woman weaving cloth by candlelight in a stone cottage, woven fabric draped over her shoulder. |
| 12 | 1:08 | 14-14 | 6.4 | zoom_in | 94.6 | 32.5 | -0.06 | The image is a painting of a religious scene in a church. It shows three monks sitting on the floor of the church, reading a book together. The room is filled with high ceilings and arches, with large stained glass windows at the top. The walls are made of stone and there are several columns on either side of the room. The monks are wearing dark robes and are holding books in their hands. In the background, there is a monk sitting at a table with a book in front of him. The overall atmosphere of the image is peaceful and serene. | A monk reading from a parchment scroll inside a vaulted church, stained glass casting colored light. |
| 13 | 1:14 | 15-15 | 7.6 | pan_right | 97.0 | 28.6 | 0.05 | The image is a painting of a group of four men standing in front of a stone castle. The castle appears to be old and weathered, with a large stone wall and a doorway in the center. The men are dressed in medieval clothing, with green robes and hats. They are gathered around the entrance of the castle, which is made of large stones and has a small window on the right side.

On the left side of the image, there is a man holding a staff and pointing towards the entrance. He is wearing a green robe and a hat, and is standing on | Two men arguing near a half-buried watchtower, one pointing at its crumbling wall. |
| 14 | 1:22 | 16-16 | 5.1 | zoom_out | 108.9 | 31.8 | 0.22 | The image is a painting of two men on horseback in front of a castle. The castle is made of stone and has multiple towers with turrets and a flag on top. The sky is blue and there are trees and bushes on either side of the castle. In the foreground, there is a dirt path leading up to the castle, and in the background, there are several people sitting on the grass and walking around. The men are dressed in medieval clothing, with helmets and armor. One of the men is riding a brown horse, while the other is riding white horse. The painting is | A lord in chainmail riding a white horse past a fortified manor, banner of red and gold fluttering. |
| 15 | 1:27 | 16-16 | 6.1 | pan_left | 106.2 | 30.1 | 0.21 | The image shows a group of people walking on a cobblestone street in a medieval village. The street is lined with old stone buildings on both sides, with a stone wall on the left side and a stone building on the right side. The buildings have a sloping roof and chimneys, and there are trees and bushes scattered throughout the street. The sky is overcast and the overall mood of the image is gloomy and gloomy. The people in the image appear to be dressed in medieval clothing, with some wearing long robes and hats. They are walking in a line, and one person | Ivory tower under siege by peasants with torches, smoke filling the air but no fire visible. |
| 16 | 1:33 | 17-17 | 8.4 | zoom_in | 101.6 | 28.1 | -0.09 | The image is a painting of a group of people working on a building. The building appears to be old and dilapidated, with peeling paint and crumbling walls. There are several people on ladders and scaffolding around the building, some of them are climbing up the stairs while others are standing on the windows. The people are dressed in colorful clothing and some are wearing hats and carrying bags. The sky is blue and there are mountains in the background. The overall mood of the painting is one of urgency and determination. | A group of villagers climbing a ladder to break into a lord’s keep, one holding an iron crowbar. |
| 17 | 1:41 | 18-18 | 6.9 | pan_up | 102.2 | 33.4 | 0.11 | The image is a painting of a group of people gathered on a cobblestone street in a small town. The street is lined with old buildings and there is a church in the background. The people are dressed in traditional clothing, with some wearing white robes and hats, while others are wearing black robes.

In the center of the image, there are two men, one wearing a green robe and the other wearing a black robe. The man in the green robe is holding a book and appears to be explaining something to the other man, who is standing in front of him. The | A bishop in miter and cope standing before a crowd at a village crossroads, hand raised in blessing. |
| 18 | 1:48 | 19-20 | 6.7 | zoom_in | 103.1 | 29.8 | -0.02 | The image is a painting of a group of men dressed in medieval clothing, engaged in a archery practice. The men are standing on a cobblestone street, with a tree and a building in the background. They are all holding bows and arrows and appear to be in the middle of a hunt. Some of the men are wearing helmets and carrying bags, while others are holding bows. The painting is done in a realistic style, with detailed facial features and clothing. The colors used in the painting are mostly earthy tones, with hints of green and brown. The overall mood of the | Archery practice in a courtyard with targets nailed to oak trees, archers wearing leather jerkins. |
| 19 | 1:55 | 19-20 | 6.7 | pan_right | 102.0 | 30.8 | 0.25 | The image is a painting of a group of people walking on a dirt path in a rural area. The path is lined with trees and bushes on both sides, and there are mountains in the background. The people are dressed in traditional clothing, with some wearing headscarves and others wearing long dresses. They are carrying baskets of fruit and vegetables, and some are carrying shovels. The sky is blue and the overall mood of the painting is peaceful and serene. The painting is done in a realistic style, with vibrant colors and intricate details. | A peasant family fleeing through a forest path as arrows whiz overhead, one child clutching a loaf of bread. |
| 20 | 2:02 | 21-21 | 10.9 | zoom_out | 70.2 | 28.2 | -0.01 | The image is a painting of four men sitting around a table in a room with a window in the background. The men are dressed in medieval clothing and appear to be engaged in a conversation. The table is covered with coins and there are several lit candles on it. The man on the left is holding a small candle and appears to be lighting it, while the man in the middle is looking at it intently. The other two men are sitting on either side of the table, also looking at the coins. All four men have long white hair and beards. The room is dimly | A lord’s steward counting coins in a candlelit stone chamber, ledger open on oak desk. |
| 21 | 2:13 | 22-23 | 6.7 | pan_left | 71.7 | 29.3 | 0.2 | The image is a painting of a group of five men sitting around a wooden table in a room with stone walls and arches. The room appears to be a workshop or a workshop with various tools and equipment scattered around. The men are dressed in medieval-style clothing and are engaged in a conversation.

On the left side of the image, there is a man standing in front of the table, holding a lit candle and looking at a piece of paper. He is wearing a long robe and has a beard. On the right side, there are two men sitting at the table with | A scribe writing by firelight inside a tower cellar, wax seal and quill visible on table. |
| 22 | 2:19 | 22-23 | 6.7 | zoom_in | 90.5 | 32.1 | 0.33 | The image is a painting of a group of five men working in an old-fashioned blacksmith shop. The shop is made of stone and has a wooden roof with a chimney. The men are wearing aprons and hats, and are gathered around a wooden workbench. They are working on various tools and materials, including a hammer, a saw, a hammerhead, and a pair of tongs. There are several pots and pans on the workbench, and some of the men are holding tools in their hands. The background shows a stone wall and a window, and there are | A blacksmith striking anvil with hammer while apprentices watch from shadows in the forge. |
| 23 | 2:26 | 24-25 | 7.4 | pan_up | 97.7 | 29.9 | -0.12 | The image is a painting of a group of men in medieval clothing, standing in front of a stone wall with arches. The men are dressed in armor and helmets, and some are holding chains. One man is holding a large chain, which appears to be a symbol of strength and power. The other men are standing around him, some of them are holding swords and shields, suggesting that they are engaged in a battle. The background shows a stone building with arched windows and a stone pathway leading up to it. The overall mood of the image is tense and action-packed. | A lord’s men dragging chains toward a broken keep wall, iron links clinking against stone. |
| 24 | 2:33 | 24-25 | 7.4 | zoom_in | 104.6 | 30.4 | 0.31 | The image is a painting of a group of people walking on a cobblestone street in a medieval village. The street is lined with old stone buildings with thatched roofs and stone walls. On the left side of the street, there is a stone building with a chimney and a small porch. In the background, there are mountains and a cloudy sky. The people in the painting are dressed in medieval clothing, with some wearing long robes and hats. They appear to be walking towards the buildings, possibly on their way to a destination. The overall mood of the painting is peaceful and se | Armed knights riding past a burning watchtower at dawn, smoke curling into misty air. |
| 25 | 2:41 | 26-26 | 6.3 | pan_right | 107.6 | 31.2 | 0.25 | The image is a painting of a group of men dressed in medieval clothing walking on a cobblestone street. The street is lined with stone buildings and there is a castle in the background. The men are carrying baskets of food and appear to be engaged in conversation. The sky is blue and there are mountains in the distance. The painting is done in a realistic style with loose brushstrokes and vibrant colors. The overall mood of the image is lively and lively. | Peasants hauling stones to rebuild a fortress under the watchful eyes of armored guards. |
| 26 | 2:47 | 26-26 | 6.3 | zoom_out | 107.2 | 31.1 | 0.29 | The image shows a group of people walking on a cobblestone street in a village. The street is lined with old stone buildings on both sides, with a stone wall on the left side and a row of houses on the right side. The houses are painted in a light green color and have a sloping roof. The sky is overcast and the overall mood of the image is gloomy and gloomy. The people in the image appear to be dressed in medieval-style clothing, with long robes and hats. They are walking in a line, with some carrying bags or baskets. The overall | A scribe in a candlelit scriptorium copying legal documents with quill and inkwell. |
| 27 | 2:53 | 27-27 | 8.5 | pan_left | 101.5 | 29.6 | 0.17 | The image is a painting of three men sitting at a wooden table in front of a stone building. The building appears to be a medieval castle or fort, with a large stone archway in the center. The men are dressed in green robes and hats, and one of them is holding a book or a pen. The man on the left is sitting on a bench, while the man in the middle is sitting at the table, and the other two are standing on either side of him. The table is set up on a stone patio, and there is a small wooden bench next to it | An old man pointing at a weathered tower while another listens, both seated on wooden benches outside. |
| 28 | 3:02 | 27-27 | 8.5 | zoom_in | 109.5 | 34.6 | 0.22 | The image is a painting of a group of six people walking on a dirt path in a mountainous landscape. The path is surrounded by rocky cliffs and hills, with a castle perched on top of one of the cliffs. The sky is cloudy and the overall mood of the painting is peaceful and serene. The people in the painting are dressed in traditional clothing, with some wearing hats and carrying bags, and one person is holding a staff. The painting is done in a realistic style, with loose brushstrokes and vibrant colors. The overall mood is one of tranquility and serenity. | Two figures walking through a misty valley toward a distant ruined keep, dawn light breaking over hills. |

## Tempos (CPU: 4 núcleos, sen GPU)

| Etapa | Parede (s) | CPU (s) | dos que servidor LLM (s) |
|---|---|---|---|
| 1_guion | 2551.4 | 8073.4 | 7139.9 |
| 2_corrixir | 5.9 | 0.0 |  |
| 2b_porta_texto | 9.5 | 32.6 |  |
| 3_voz | 59.9 | 141.8 |  |
| 4_escenas | 352.5 | 1106.9 | 1106.8 |
| 5_imaxes | 2111.8 | 7950.6 |  |
| 6_son | 8.0 | 7.9 |  |
| 7_montaxe | 261.6 | 988.5 |  |
| 8_qa | 116.4 | 315.0 |  |
| **Total** | **5477.0** | **18616.7** | **8246.7** |

Tempo total de CPU: 5.17 h de núcleo (das que LLM local: 2.29 h); parede: 91.3 min. Inclúe o LLM local e o arranque do seu servidor; non inclúe a descarga de modelos.

## LLM (chamadas)

| Chamada | Caché | Segundos | Tokens entrada/saída | Tokens/s saída | CPU servidor (s) |
|---|---|---|---|---|---|
| bloque_seleccion_gancho_1 | `bloque_seleccion_gancho-824f8474525c.txt` (da caché) | 87.0 | 832/5 | 0.06 | 323.7 |
| bloque_gancho_1 | `bloque_gancho-b9ac986124c8.txt` (da caché) | 18.3 | 369/27 | 1.47 | 59.5 |
| bloque_resumo_1 | `bloque_resumo-b91261940eec.txt` (da caché) | 74.2 | 935/91 | 1.23 | 262.8 |
| bloque_resumo_2 | `bloque_resumo-e670383fb752.txt` (da caché) | 84.8 | 1094/155 | 1.83 | 290.3 |
| bloque_resumo_3 | `bloque_resumo-a11d81b4a9bc.txt` (da caché) | 91.0 | 1104/164 | 1.8 | 283.1 |
| bloque_seleccion_1 | `bloque_seleccion-312cd705dbd4.txt` (da caché) | 160.9 | 893/80 | 0.5 | 595.6 |
| bloque_parrafo_1 | `bloque_parrafo-a37f3748c630.txt` (da caché) | 30.7 | 419/30 | 0.98 | 99.7 |
| bloque_parrafo_2 | `bloque_parrafo-9c63a1996c11.txt` (da caché) | 40.3 | 552/63 | 1.56 | 117.1 |
| bloque_parrafo_3 | `bloque_parrafo-10f9e31b1804.txt` (da caché) | 22.9 | 520/17 | 0.74 | 70.5 |
| bloque_parrafo_4 | `bloque_parrafo-a2d31f33b34b.txt` (da caché) | 68.7 | 460/15 | 0.22 | 256.7 |
| bloque_parrafo_5 | `bloque_parrafo-fabced0c917b.txt` (da caché) | 36.3 | 513/66 | 1.82 | 106.8 |
| bloque_parrafo_6 | `bloque_parrafo-0687083448d7.txt` (da caché) | 16.9 | 488/30 | 1.78 | 54.3 |
| bloque_parrafo_7 | `bloque_parrafo-67d4fa41b9a8.txt` (da caché) | 25.5 | 479/30 | 1.18 | 83.3 |
| bloque_parrafo_8 | `bloque_parrafo-44476e181d47.txt` (da caché) | 39.9 | 507/30 | 0.75 | 141.8 |
| bloque_parrafo_9 | `bloque_parrafo-44476e181d47.txt` (da caché) | 39.9 | 507/30 | 0.75 | 141.8 |
| bloque_parrafo_10 | `bloque_parrafo-cffefb01357b.txt` (da caché) | 25.9 | 444/44 | 1.7 | 79.0 |
| bloque_parrafo_11 | `bloque_parrafo-18ff70f4dbf0.txt` (da caché) | 40.8 | 472/33 | 0.81 | 132.0 |
| bloque_parrafo_12 | `bloque_parrafo-871449af2068.txt` (da caché) | 41.2 | 531/66 | 1.6 | 123.7 |
| bloque_parrafo_13 | `bloque_parrafo-8067d9e4d721.txt` (da caché) | 19.8 | 424/11 | 0.55 | 65.4 |
| bloque_parrafo_14 | `bloque_parrafo-895c6e0be660.txt` (da caché) | 27.7 | 452/38 | 1.37 | 84.8 |
| bloque_parrafo_15 | `bloque_parrafo-ff2ce4ab0e47.txt` (da caché) | 42.3 | 593/69 | 1.63 | 134.2 |
| bloque_parrafo_16 | `bloque_parrafo-ad3874cf8c32.txt` (da caché) | 30.1 | 436/66 | 2.19 | 96.2 |
| bloque_parrafo_17 | `bloque_parrafo-9f89f442b5e3.txt` (da caché) | 30.1 | 552/37 | 1.23 | 95.9 |
| bloque_parrafo_18 | `bloque_parrafo-9f89f442b5e3.txt` (da caché) | 30.1 | 552/37 | 1.23 | 95.9 |
| bloque_parrafo_19 | `bloque_parrafo-e1e1b8fa5d63.txt` (da caché) | 35.0 | 458/47 | 1.34 | 93.6 |
| bloque_parrafo_20 | `bloque_parrafo-7ed88ae4dc12.txt` (da caché) | 19.9 | 511/33 | 1.66 | 60.7 |
| bloque_parrafo_21 | `bloque_parrafo-93b7f6dcbab1.txt` (da caché) | 29.2 | 486/57 | 1.95 | 86.8 |
| bloque_parrafo_22 | `bloque_parrafo-e5b2459effa1.txt` (da caché) | 35.0 | 537/61 | 1.74 | 103.6 |
| bloque_parrafo_23 | `bloque_parrafo-80fa3c0de89f.txt` (da caché) | 44.4 | 665/60 | 1.35 | 124.7 |
| bloque_parrafo_24 | `bloque_parrafo-7c5077710a15.txt` (da caché) | 34.9 | 664/61 | 1.75 | 99.4 |
| bloque_parrafo_25 | `bloque_parrafo-850d00938490.txt` (da caché) | 43.2 | 492/67 | 1.55 | 122.3 |
| bloque_parrafo_26 | `bloque_parrafo-b5f297af7adf.txt` (da caché) | 29.8 | 520/67 | 2.25 | 88.7 |
| bloque_parrafo_27 | `bloque_parrafo-0e1519e477c0.txt` (da caché) | 74.0 | 595/68 | 0.92 | 261.6 |
| bloque_parrafo_28 | `bloque_parrafo-65552d4a7eaf.txt` (da caché) | 17.0 | 446/29 | 1.7 | 54.9 |
| bloque_parrafo_29 | `bloque_parrafo-b6d7b94904e2.txt` (da caché) | 20.8 | 506/48 | 2.31 | 66.5 |
| bloque_parrafo_30 | `bloque_parrafo-0ad403fbbac8.txt` (da caché) | 41.8 | 616/60 | 1.43 | 138.7 |
| bloque_parrafo_31 | `bloque_parrafo-38182b11a034.txt` (da caché) | 19.1 | 442/39 | 2.05 | 61.5 |
| bloque_parrafo_32 | `bloque_parrafo-6831c9ad7b9c.txt` (da caché) | 21.3 | 520/52 | 2.44 | 69.9 |
| bloque_parrafo_33 | `bloque_parrafo-ea964fbbf1fa.txt` (da caché) | 31.2 | 522/50 | 1.6 | 92.3 |
| bloque_parrafo_34 | `bloque_parrafo-a5bf8b9763a9.txt` (da caché) | 19.5 | 457/41 | 2.1 | 61.6 |
| bloque_parrafo_35 | `bloque_parrafo-b5733354091c.txt` (da caché) | 37.8 | 501/85 | 2.25 | 117.2 |
| bloque_parrafo_36 | `bloque_parrafo-8de646551152.txt` (da caché) | 27.5 | 485/46 | 1.67 | 76.7 |
| bloque_parrafo_37 | `bloque_parrafo-651c6fa22a62.txt` (da caché) | 43.4 | 471/22 | 0.51 | 152.8 |
| bloque_parrafo_38 | `bloque_parrafo-a8af58ef51fc.txt` (da caché) | 38.5 | 499/20 | 0.52 | 136.3 |
| bloque_parrafo_39 | `bloque_parrafo-a8af58ef51fc.txt` (da caché) | 38.5 | 499/20 | 0.52 | 136.3 |
| bloque_parrafo_40 | `bloque_parrafo-2acebb8e8afc.txt` (da caché) | 28.9 | 441/37 | 1.28 | 79.0 |
| bloque_parrafo_41 | `bloque_parrafo-b64faed85c0f.txt` (da caché) | 33.3 | 532/40 | 1.2 | 112.0 |
| bloque_parrafo_42 | `bloque_parrafo-64972d15841a.txt` (da caché) | 22.4 | 469/38 | 1.7 | 68.5 |
| bloque_parrafo_43 | `bloque_parrafo-4a412ee33545.txt` (da caché) | 15.0 | 437/22 | 1.46 | 49.4 |
| bloque_parrafo_44 | `bloque_parrafo-b16a2caf7428.txt` (da caché) | 18.4 | 537/38 | 2.07 | 60.5 |
| bloque_parrafo_45 | `bloque_parrafo-b16a2caf7428.txt` (da caché) | 18.4 | 537/38 | 2.07 | 60.5 |
| bloque_parrafo_46 | `bloque_parrafo-e8d961d098da.txt` (da caché) | 14.3 | 447/17 | 1.19 | 48.1 |
| bloque_parrafo_47 | `bloque_parrafo-db04760f541f.txt` (da caché) | 34.2 | 475/65 | 1.9 | 113.6 |
| bloque_parrafo_48 | `bloque_parrafo-ea09d1b49ed6.txt` (da caché) | 37.5 | 764/64 | 1.71 | 124.1 |
| bloque_parrafo_49 | `bloque_parrafo-5d6a08f12daf.txt` (da caché) | 35.7 | 457/41 | 1.15 | 126.4 |
| bloque_parrafo_50 | `bloque_parrafo-ecffd8ecbde6.txt` (da caché) | 27.8 | 485/78 | 2.8 | 91.3 |
| bloque_parrafo_51 | `bloque_parrafo-ecffd8ecbde6.txt` (da caché) | 27.8 | 485/78 | 2.8 | 91.3 |
| bloque_parrafo_52 | `bloque_parrafo-ad4baad08f5f.txt` (da caché) | 30.4 | 496/89 | 2.93 | 97.3 |
| bloque_parrafo_53 | `bloque_parrafo-96d7456186dd.txt` (da caché) | 29.2 | 592/41 | 1.41 | 100.0 |
| bloque_parrafo_54 | `bloque_parrafo-18fe78e0a4cd.txt` (da caché) | 39.3 | 600/94 | 2.39 | 130.0 |
| bloque_parrafo_55 | `bloque_parrafo-aec0510e6730.txt` (da caché) | 30.0 | 490/78 | 2.6 | 93.1 |
| bloque_parrafo_56 | `bloque_parrafo-dcd00fdd2c6e.txt` (da caché) | 28.8 | 598/68 | 2.36 | 91.7 |
| bloque_parrafo_57 | `bloque_parrafo-07446cce53e9.txt` (da caché) | 27.6 | 588/70 | 2.53 | 88.6 |
| escenas_1 | `escenas-0e04da903d05.txt` | 332.4 | 2013/862 | 2.59 | 1074.5 |

## Extrapolación a un episodio de 60 min [S: escala lineal dos tempos medidos]

Supostos: mesma densidade de texto e de planos que esta mostra (o gancho só está ao principio, así que un episodio longo ten planos máis longos de media e isto sobreestima as imaxes), custo proporcional á duración en todas as etapas (tamén o LLM: guion e escenas por bloques), carga dos modelos unha vez.

| Etapa | Parede (min) | CPU (h de núcleo) |
|---|---|---|
| 1_guion | 801 | 42.27 |
| 2_corrixir | 2 | 0.00 |
| 3_voz | 19 | 0.74 |
| 4_escenas | 111 | 5.80 |
| 5_imaxes | 663 | 41.63 |
| 6_son | 3 | 0.04 |
| 7_montaxe | 82 | 5.18 |
| 8_qa | 37 | 1.65 |
| **Total** | **1718** (28.6 h) | **97.30** |

## Guion final narrado

Boas noites. A voz que vas escoitar é sintética, e este texto preparouno un proceso automático.

Dicían que eran refuxios de malfeitores. As fortalezas derrubadas non se volveron levantar todas.

Isto é Serán, historia de Galicia para durmir.

Acomódate, apaga a luz e respira amodo. Non tes que lembrar nada do que escoites: deixa que a historia pase coma a chuvia na xanela.

Desde a peste negra as rendas dos señores minguaban en toda Europa e a presión señorial sobre os vasalos aumentaba.

Arredor da metade do século quince, Galicia era unha sociedade de labregos, artesáns, mariñeiros e mercadores; moitos eran vasalos dun señor. A xente de Galicia botou abaixo moitas fortalezas dos señores.

Os vasalos pagaban tributos en diñeiro e en especie e debían servizos persoais: traballo nas fortalezas e servizo de armas.

As familias labregas vivían ao limiar da pobreza.

O señor era tamén xuíz no seu señorío.

Desde había un século mandaba unha nobreza nova, máis violenta, e o reino enchérase de fortalezas.

Había fortalezas das grandes casas nobres, como Lemos ou Andrade, de bispos e, sobre todo, do arcebispo de Compostela. Botáronse abaixo moitas fortalezas por mandato dunha irmandade que, entre as primaveras de mil catrocentos sesenta e sete e mil catrocentos sesenta e nove, botou abaixo moitas fortalezas.

Unhas décadas antes, os vasalos dun gran señor das Mariñas formaran unha irmandade e marcharan cara a Compostela; foi vencida e castigada. Despois houbo outras irmandades locais e comarcais, e algunha derrubou fortalezas.

Desde a Rocha Forte asegurábanse os camiños que ían cara a Pontevedra, Padrón, Muros, Noia e Fisterra, cara ao mar.

A Rocha Forte era do arcebispo de Compostela.

Na irmandade xuntáronse labregos, artesáns, mariñeiros, burgueses, clérigos, cóengos e monxes, e parte da pequena nobreza, que achegou experiencia militar.

Decididos os veciños da cidade e os labregos da comarca, botaron abaixo a Rocha Forte.

Os irmandiños derrubaron moitas das fortalezas do reino.

En mil catrocentos sesenta e nove houbo unha reacción armada dos señores, que regresaron.

Os señores regresaron coas súas tropas e a irmandade foi derrotada.

Despois da derrota o castigo non foron tanto as execucións como os tributos e o traballo que os vasalos tiveron que dar durante anos para reconstruír as fortalezas derrubadas.

Entre mil cincocentos vinte e seis e mil cincocentos vinte e sete, douscentas catro testemuñas vellas declararon ante escribáns no Preito Tabera-Fonseca, lembrando co que viran de mozos.
