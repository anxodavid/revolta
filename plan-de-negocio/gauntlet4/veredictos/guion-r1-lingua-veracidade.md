# Guion v2 · rolda 1 · crítico B (lingua e veracidade)

Crítico B da peza GUION do Gauntlet 4: **axente Claude** con perfil de filólogo galego (norma da RAG) e verificador de
feitos. Non participei no guion. 03-10-2026. Xulgo [`guion/guion-r1.txt`](../guion/guion-r1.txt) (1.602 palabras, md5
`e14180a5ded097eefcded418b7fa6fa6`, a mesma copia conxelada que pasou a porta), co mapa
[`feitos-r1.md`](../guion/feitos-r1.md), as excepcións [`excepcions-r1.yaml`](../guion/excepcions-r1.yaml), a porta
[`porta_texto-r1.json`](../guion/porta_texto-r1.json) e as notas [`notas-r1.md`](../guion/notas-r1.md). "l. N" é a liña
de `guion-r1.txt`; "SN", a frase co número do mapa de feitos.

**Que fixo Claude e que é automático.** Todo o xuízo fíxoo este axente Claude: a lectura frase a frase; o cotexo de
cada frase co feito que cita o mapa en `gauntlet3/dossier/feitos.yaml` (busca por ID) e coa lista "Non dicir"
(`dossier.md` §5); a lectura dos pasaxes do PDF do Arquivo do Reino de Galicia (texto extraído polo construtor en
`$SCRATCH/fontes/ARG-PDF.txt`, de
https://arquivosdegalicia.xunta.gal/sites/default/files/arquivos_artividades/expo_mulleres_2020_01_C.pdf, p. 4-7, 11, 14-16);
e o dicionario da RAG con `curl` (*pensar*, *chuvia*, *medio*, *noticia*, *penso*, *condenar*). Automático: a predición
léxica de veracidade (`guion/scripts/veracidade_lexica.py`) e as portas de lingua (LanguageTool + hunspell), H1 e estilo
de `longo.py`, que pasei sobre unha copia do guion coas substitucións do §7. **A porta de veracidade con NLI non a volvín
pasar.** Ningunha persoa revisou este veredicto.

## Veredicto: **GAÑA** (aplicando a lista pechada do §7)

| Condición do encargo | Resultado |
|---|---|
| 0 erros de feito despois das substitucións | **Cúmprese.** Hai 0 G, 4 M e 4 L (§2). Todos se arranxan cunha substitución que non engade feitos nin nomes |
| 0 erros graves de lingua | **Cúmprese.** 0 G; 2 M (a reconstrución con *pensala* e un suxeito implícito que o oído lle dá á testemuña) e 2 L, todos con substitución (§5) |
| Regras do tema (`gauntlet3/contexto.md` §8) | **Cúmprense** (§4), co matiz M da frase da Inquisición (H4), que se arranxa cunha palabra |
| Excepcións da porta de veracidade | 4 aceptadas (S12, S15, S17, S19), 1 rexeitada e substituída (S13); 2 preventivas para frases novas (S16 e S23) (§6) |
| Portas sobre a copia substituída | LanguageTool e hunspell 0 avisos, H1 55 de 55, estilo correcto; veracidade con NLI pendente: vai no §8 |

**Maior carencia** (arranxada no §7): o fío "as palabras" empurra o texto a dicir máis do que din os papeis. O gancho dá
a entender que se conservan as palabras de Dorotea (S13) e a lista de Campo Lameiro (S16), e o capítulo IV remata en que
"queda a lista" (S66). Do conxuro de Dorotea o proceso só di que sabía "algunas palabras", e da lista só hai o testemuño
de que a fixeron. Dous casos máis de costura: "Nai e filla eran as de Vilalba" fai deducir que María aprendeu o oficio
da nai (S71), e a frase da Inquisición perdeu o "en Galicia" (S48).

**O que está ben e hai que conservar:** a atribución de Dorotea ("Unha testemuña declara que… dixera", nota de F008); a
confesión de Cibreira despois do tormento, nomeado unha vez e sen detalle; a Inquisición unha soa vez, sen ano, atribuída
a Valor Bravo e co contraste da xustiza ordinaria; as tres reconstrucións explícitas e xenéricas; o emblema "auga, digo,
leite", ben lido no documento; a zona de durmir sen nada inquietante; ningunha das 18 frases de "Non dicir"; e un galego
normativo e natural, sen castelanismos.

## 1. O que o construtor pediu verificar

| Afirmación do construtor | Resultado | Proba |
|---|---|---|
| O testemuño de Vilalba é "de oídas" | **Certo para as palabras de María ao gando.** No folio [3 verso] a testemuña "oyó dizir y mormurar entre algunas personas vecinas … que la dicha María do Barro, acusada, hera meyga y que no hera buena cristiana y como tal quando hesthaba su ganado al monte deçía algunas palabras…". **Para Dorotea non se pode dicir:** o folio [5 recto] empeza tras uns puntos suspensivos e o extracto non di como o soubo. O guion non depende diso (S6 atribúello á testemuña), pero o mapa e as notas (§3.6) esténdeno ás dúas | PDF, p. 15 |
| Cibreira confesou despois do tormento | **Certo.** Rótulo "Tortura:" sobre [23 recto] (a orde de tendela no potro) e "Confesión de María Cibreira despois de ser torturada:" sobre [26 recto], [26 verso], [27 recto], [27 verso] e [29 verso] | PDF, p. 4-5 |
| As reconstrucións van con "podemos pensar" ou "cómpre pensala" porque a porta veta "imaxina" | **Certo o veto** (`qa.py`, l. 103: "imaxina" como subcadea). Pero *pensala* non é unha construción do DRAG: ver L1 | `qa.py`; DRAG, *pensar* |
| F052 engadido á ficha v2 | **Certo:** `meigas-de-verdade-v2.yaml`, l. 292-293, tras un separador que nomea o ID. A cita é do mesmo testemuño de oídas, e o feito tal como está redactado perde a testemuña (H6) | ficha v2; PDF, p. 15 |

Comprobei tamén que as dúas propostas das notas (§5.1 e §5.2) están literalmente no PDF: "y con el no ableis tratéis ni
comuniquéis" na excomuñón ([52 recto]) e a resposta en galego de Inés da Maquieira no testemuño de Juan Linarinos
([22 recto]), que é unha ameaza ("bos aves de ber e desear"). Non entran nesta rolda.

## 2. Feitos

Gravidade: **G** falso, contrario ao dossier ou de "Non dicir"; **M** atribución perdida ou orde das frases que fai
deducir algo falso ou sen apoio; **L** imprecisión leve.

| # | Frase (l., S) | Problema | Fonte | Arranxo | Grav. |
|---|---|---|---|---|---|
| H1 | «As de Dorotea son vellas de verdade, e só as coñecemos porque alguén as escribiu nun proceso por bruxería.» (l. 9, S13, gancho) | O oído completa "as [palabras] de Dorotea" en paralelo con "as palabras do conxuro" e coas "unhas palabras que ela sabía" de S7, e deduce que o proceso garda o conxuro de Dorotea. **Non o garda:** só di que as sabía ("con algunas palabras que savía"). O que se conserva é o que unha testemuña dixo que ela dixera, e "as de Dorotea" quítalle esa atribución | F008, F009; PDF, p. 15 ([5 verso]) | Substitución 2 | M |
| H2 | «E hai mesmo unha lista coas mulleres…» (l. 11, S16) e «Do que elas falaban aquela noite, nestes papeis non queda nin unha palabra. Queda a lista, escrita por outros.» (l. 49, S65-S66) | **Ningún papel coñecido garda a lista.** Consta o testemuño de Joan do Campo de que os veciños "las abían escripto en una memoria" ([29 recto]). Polo tanto, "queda a lista" é un desenlace inventado. Ademais, "nestes papeis non queda nin unha palabra" afirma algo do proceso enteiro, que ninguén leu (temos catro folios en extracto, e o mesmo testemuño conta aquela noite en [30 recto], cos demos que o §8 deixa fóra). E "falaban" dá por feito que falaron | F050, F131-F133; PDF, p. 7 | Substitucións 3 e 12 | M |
| H3 | «Nai e filla eran as de Vilalba.» (l. 53, S71) | Entre "aprenderan o oficio… a miúdo das súas nais" e "maldita a nai que non ensina a súa filla a meigar", fai deducir que María aprendeu o oficio de Dorotea. O dossier non o di: Dorotea era parteira, e de María dicían que era alcaiota e murmuraban que era meiga. A transmisión de nai a filla documentada no episodio é a de Cibreira, e vén dunha confesión | F007, F012, F052, F089 | Substitución 13 (quitar a frase) | M |
| H4 | «…coas meigas a temida Inquisición foi branda: en tres séculos só condenou a morte unha meiga.» (l. 37, S48) | Perdeu o "en Galicia" de F036. Soa, a frase dise da Inquisición enteira, e iso contradí F038 (as cifras galegas son "moi baixos comparados con outros tribunais inquisitoriais nacionais e europeos", Arquivo). É a frase máis delicada do episodio (§8.1) | F036, F038; ESPANOL; PDF, p. 11 | Substitución 8 | M |
| H5 | «Abondaba con calzarlle ao home os zapatos da muller…» (l. 3, S7) | En indicativo pode oírse como explicación do narrador. Co condicional queda dentro do que dixo a testemuña, como "saltaría" (o documento di "quitaría… hecharía… aría saltar") | F008 (nota), F009, F010 | Substitución 1 | L |
| H6 | «Algúns veciños murmuraban que María era meiga, e que non era boa cristiá.» (l. 17, S22) | O murmurio só se coñece pola testemuña que o "oyó dizir y mormurar"; F052 perdeu esa atribución e o guion herdouna | F052; PDF, p. 15 ([3 verso]) | Substitucións 4 e 5 | L |
| H7 | «Alí viron e recoñeceron as mulleres, e apuntáronas nunha lista porque eran moitas.» (l. 47, S63) | O testemuño segue en frase á parte e en pretérito, como feito do narrador (como a arracada na rolda 2 da v1, P3) | F131, F133 | Substitución 11 | L |
| H8 | «As palabras dos procesos naceron noutro sitio: nos tribunais.» (l. 35, S46) | Contradí S26-S27: as palabras de María naceron no monte e de alí pasaron ao papel. "Acabaron" vale para todas | Tecido; F054 | Substitución 7 | L |

**Comprobado e correcto** (o máis delicado):
- **Conxuro:** 1967, Mariano Marcos Abalo, o vello barco amarrado no porto de Vigo, o ritual, os cinco ou seis conxuros
  "daquela época" (cita del no *Atlántico*), a empresa que vendeu copias sen o nome do autor e o rexistro de 2001
  (F002-F005, F014, F015, F018, F246).
- **Vilalba:** Dorotea, parteira (F007), cos zapatos e o poldro bravo, e "declara… dixera" ([5 recto]-[5 verso]). María,
  alcaiota (F012, [6 recto]), as palabras ao gando coa redacción da fonte ("callando y otras que se oyan") e "agua, digo,
  leche" (F053-F055, [3 verso]). Uns trinta procesos da xustiza real no Arquivo (F083, p. 11). A excomuñón: o vicario
  nomea as dúas ("en razón de ser alcahueta la dicha María do Varro y la dicha Doratea según se dize bruxa") e manda non
  darlles "pan carne sal agua ni lumbre" (F056, [52 recto]); quitar "carne" é resumir, non cambiar.
- **Tribunal:** tres xustizas (F077); Valor Bravo, unha vez e sen ano (F036, F039, F040); na Real Audiencia todas as
  acusadas eran mulleres ("Todas as reas son mulleres", p. 14; F085), sen "todas as meigas" (Non dicir n.º 14).
- **Cibreira:** 1639, Boborás (F088); oficio "de tal bruxa y echizera" despois do tormento (F089, F091); **as curas eran
  da nai** ("a su casa de ella acudían muchas personas y ella les hacía muchas curas y medezinas y ella mesma ansí lo vió
  hacer", [26 recto]; F090); san Xoán e as areas de Sevilla (F092; omitir o primeiro de maio é resumir).
- **Pousa:** as respostas nas preguntas (F093), "meigar" como cita (F119), "necesarias" (F121) e as ovellas na viña
  (F125).
- **Campo Lameiro:** 1643 (F129); dúas becerras e catro leitóns dun veciño, catro leitóns doutro e "por hestaren
  reñidos" ([22 verso]; F130); a fonte da Nogueira, o ano anterior e a lista "por ser mucho número dellas" ([29 recto];
  F131-F133). Os demos do camiño ([30 recto]) quedan fóra, ben.
- **San Xoán, queimada e peche:** F134, F135, F168, F170, F173-F175, F178, F188-F195, F199, F268-F270, F029-F031, F237 e
  F238; Feijoo (F212, F216, F217, F227, F228); e Sarmiento con "como" (F232, corrección L1 da v1).

## 3. Tecido narrativo

- **Reconstrucións** (S24, S56, S64): explícitas e xenéricas, sen nomes, datas, cifras nin diálogos. O vento, a auga fría
  e os ollos na escuridade van dentro de "pensemos" ou "podemos pensar". Correctas como feito; S24 e S56 teñen o problema
  de lingua L1.
- **Frases de tecido do mapa:** todas correctas agás S13, S65-S66 e S71 (H1-H3, M) e S46 (H8, L). S12, S15, S17, S19,
  S26, S27 ("do monte pasaron á boca da testemuña" comprime a cadea monte → veciños → testemuña, pero non di que el o
  oíse), S31-S32, S34-S37, S44-S45, S58, S69 (non explica a que foron á fonte), S81-S83 e S97-S108: correctas.
- **Lenda e costume:** "se cría" (S67), "na crenza popular" (S68), "segundo a crenza" (S85), "crese" (S89); os ramos
  "para que a protexan" (S91) din a intención, non a eficacia. **Ningún consello médico.**

## 4. Regras do tema (`gauntlet3/contexto.md` §8)

| Regra | Resultado |
|---|---|
| Frase da Inquisición unha vez, sen ano nin nome da fogueira; nunca "Galicia librouse" | Cúmprese (S48, ≈ 4:05). Falta o ámbito: H4 |
| Do conxuro, como moito o primeiro verso, co autor | Cúmprese: o verso en S1 (autor en S4) e en S96, dentro dun comentario sobre a súa orixe ("Agora xa sabes quen escribiu estas palabras…"), co autor nomeado en S4 e S39 e nos créditos |
| María Soliña só como nome e poema | Non sae |
| Nada inquietante na zona de durmir (cap. V, ≈ 7:55) | Cúmprese: só espreitar e apuntar nomes en negativo ("ninguén espreita") e o can da copla. O demo (S55) e a tortura (S52) van ≈ 4:30 |
| Aviso e fórmula literais no primeiro minuto | Cúmprese: palabra 100 (≈ 0:38); porta `aviso_literal` e `formula_literal` |
| "Non dicir" (18 frases) | Ningunha |
| Honestidade | Non se afirma ningunha revisión humana. O aviso di "proceso automático": é o texto literal obrigatorio, e non hai persoas no proceso |

## 5. Lingua

O galego é **normativo e natural**. A colocación dos pronomes átonos é correcta en todo o texto ("consérvao",
"culpábana", "apuntáronas", "espreitalas", "pasarllas", "déixao"; próclise tras *non*, *que*, *xa case*, *así*, *porque*),
e tamén as contraccións ("cara ao río", "á luz das brasas"). Están ben o CD de persoa sen *a* cos nomes comúns
("procesou alí varias mulleres") e con *a* co nome propio ("xulgou tamén a María do Barro"), *coma* nas comparacións e
*como* en Sarmiento, *si* sen acento ("Ese si é de todos") e o clítico con *haber* ("que as houbese"). No DRAG: *chuvia* (sinónimo de
*choiva*), *a medias* ("Deixar o traballo a medias"), *noticia* ("Información que se dá ou se ten sobre algo ou alguén")
e *trabucar(se)*. Non hai díxitos, siglas, preguntas nin frases de máis de 25 palabras. As 12 frases curtas son ritmo
buscado.

| # | Frase (l., S) | Problema | Arranxo | Grav. |
|---|---|---|---|---|
| L1 | «Podemos pensala alí, co gando arredor…» (l. 19, S24) e «Cómpre pensala diante de quen pregunta e de quen escribe.» (l. 39, S56) | No DRAG, *pensar* transitivo leva sempre [algo] (ac. 1-6). Para dirixir o pensamento a unha persoa é intransitivo, *pensar en alguén* (ac. 8: "Dirixir o pensamento cara a algo ou a alguén"). *Pensala* co sentido de 'imaxinala' é un decalque forzado para fuxir do veto de "imaxina", e "Cómpre" convérteo nunha obriga. S64 ("Podemos pensar nunha noite…") está ben | Substitucións 6 e 9: «Pensemos nela…» | M |
| L2 | «Unha testemuña contou que, cando tiña o gando no monte, dicía unhas palabras…» (l. 19, S23) | Co suxeito implícito, o oído atribúelle "tiña" e "dicía" ao suxeito principal, a testemuña, que abre un parágrafo novo | Substitucións 4 e 5 (nomean a María e encadean a testemuña) | M |
| L3 | «Que á casa da nai acudía moita xente, e que ela lles facía curas e menciñas.» (l. 39, S54) | *Ela* pode ser a nai ou María, que é quen confesa. O documento di que as curas eran da nai | Substitución 10: «Que á nai acudía moita xente…» (DRAG, *acudir* 3: "Botar man de algo ou alguén como axuda…", "Sempre acoden a el cando teñen algún problema") | L |
| L4 | «Para el, eran necesarias, porque…» (l. 55, S73) | O suxeito está tres frases atrás (S70), despois dunha cita | Substitución 14 | L |

**Sen cambio (L, admisibles):** as comas antes de *e* (S21, S22, S31, S33, S58), que marcan pausas para a voz; o *ela*
enfático de S7 (é Dorotea, o tema da frase); "Ese papel" (S36), que o predicado identifica; e "condenou a morte", que o
DRAG non resolve (só trae "Condenárono a dez anos…").

**Para a peza VOZ:** pausas en "auga, digo, leite" e na copla ("Salto por riba do lume de san Xoán…"); pronuncia de
*Sevilla*, *Xerónimo*, *Valor Bravo*, *Boborás* e *Cibreira*; o verso do conxuro dúas veces co mesmo ton. Lembranza da
v1: "A voz que vas escoitar" soa tras ≈ 38 s de voz, pero é o texto literal obrigatorio.

## 6. Excepcións da porta de veracidade

| Frase | Decisión | Xustificación (como queda no YAML) |
|---|---|---|
| S12 «As palabras do conxuro parecen vellas e son novas, e hai un motivo polo que semellan de ninguén.» | **Aceptada** | Tecido do gancho: resume S1-S4 (F001-F004 e F246) e anuncia o motivo que se paga en S42 (F014). Non engade feitos |
| S13 «As de Dorotea son vellas de verdade, e só as coñecemos porque alguén as escribiu nun proceso por bruxería.» | **Rexeitada** (H1) | Arránxase coa substitución 2. A frase nova vai aceptada: síntese de S5-S8 (F006, F008-F010, F055) |
| S15 «Hai unha palabra trabucada que ninguén borrou en máis de catrocentos anos.» | **Aceptada** | A emenda quedou escrita en 1617 (F055, F006) e a transcrición do Arquivo de 2020 aínda a trae ("traxese agua, digo, leche"): de 1617 a 2020 van 403 anos |
| S17 «Había mulleres de aldea detrás de todas esas palabras.» | **Aceptada** | As acusadas dos tres casos eran veciñas de parroquias rurais (F051, F088, F129). Prepara F048 |
| S19 «Esta noite imos buscalas no pouco que delas quedou escrito.» | **Aceptada** | Promesa do narrador, sen contido factual (o fío, S31 e S101) |
| S16 nova (substitución 3) | **Preventiva** | A predición léxica dáa por dubidosa (coincidencia 0,75). Bucle que se paga en S59-S66 (F050, F131-F133); di "noticia" porque consta o testemuño, non a lista |
| S23 nova (substitución 5) | **Preventiva** | Agora leva nome no relato (coincidencia 0,78). F053, con suxeito na testemuña de S22 (F052) |

O [`excepcions-r1.yaml`](../guion/excepcions-r1.yaml) queda con estas sete entradas: as cinco aceptadas (S13 coa frase
nova) e as dúas preventivas. Xa non leva a S13 antiga, así que a porta falla se non se aplica a substitución 2. As
preventivas non fan nada se o NLI aproba esas frases.

## 7. Lista pechada de substitucións

Texto exacto de `guion-r1.txt` (cada texto actual é único no guion; comprobado por script) e unha liña da ficha. Non
engaden feitos nin nomes. O guion pasa de 1.602 a **1.608 palabras**. Hai unha copia xa substituída en
`$SCRATCH/criticoB-r1/guion-r1-substituido.txt`, coa lista en JSON ao carón, só como axuda: a que vale é esta táboa.

| # | Liña (S) | Texto actual | Texto novo | Arranxa |
|---|---|---|---|---|
| 1 | l. 3 (S7) | `Abondaba con calzarlle ao home os zapatos da muller,` | `Abondaría con calzarlle ao home os zapatos da muller,` | H5 |
| 2 | l. 9 (S13) | `As de Dorotea son vellas de verdade, e só as coñecemos porque alguén as escribiu nun proceso por bruxería.` | `O que se contou de Dorotea é vello de verdade, e só o coñecemos porque alguén o escribiu nun proceso por bruxería.` | H1 |
| 3 | l. 11 (S16) | `E hai mesmo unha lista coas mulleres` | `E hai mesmo noticia dunha lista coas mulleres` | H2 |
| 4 | l. 17 (S22) | `Algúns veciños murmuraban que María era meiga, e que non era boa cristiá.` | `Unha testemuña oíu murmurar entre algúns veciños que María era meiga, e que non era boa cristiá.` | H6, L2 |
| 5 | l. 19 (S23) | `Unha testemuña contou que, cando tiña o gando no monte,` | `E contou que María, cando tiña o gando no monte,` | L2, H6 |
| 6 | l. 19 (S24) | `Podemos pensala alí,` | `Pensemos nela alí,` | L1 |
| 7 | l. 35 (S46) | `As palabras dos procesos naceron noutro sitio: nos tribunais.` | `As palabras dos procesos acabaron noutro sitio: nos tribunais.` | H8 |
| 8 | l. 37 (S48) | `coas meigas a temida Inquisición foi branda` | `coas meigas galegas a temida Inquisición foi branda` | H4 |
| 9 | l. 39 (S56) | `Cómpre pensala diante de quen pregunta e de quen escribe.` | `Pensemos nela diante de quen pregunta e de quen escribe.` | L1 |
| 10 | l. 39 (S54) | `Que á casa da nai acudía moita xente,` | `Que á nai acudía moita xente,` | L3 |
| 11 | l. 47 (S63) | `Alí viron e recoñeceron as mulleres,` | `Alí, dixo, viron e recoñeceron as mulleres,` | H7 |
| 12 | l. 49 (S65-S66) | `Do que elas falaban aquela noite, nestes papeis non queda nin unha palabra. Queda a lista, escrita por outros.` | `Do que elas dixesen aquela noite, non nos chegou nin unha palabra. Só nos chegou a noticia da lista, na voz doutros.` | H2 |
| 13 | l. 53 (S71) | `a miúdo das súas nais. Nai e filla eran as de Vilalba. Nos papeis,` | `a miúdo das súas nais. Nos papeis,` | H3 |
| 14 | l. 55 (S73) | `Para el, eran necesarias,` | `Para el, aquelas mulleres eran necesarias,` | L4 |
| 15 | ficha v2, `descricion` (texto público) | `e unha lista de mulleres vistas nunha fonte a noite de san Xoán, en Campo Lameiro` | `e a noticia dunha lista de mulleres vistas nunha fonte a noite de san Xoán, en Campo Lameiro` | H2 |

As substitucións 3 e 12 conservan o bucle: o gancho promete a "noticia dunha lista" e o capítulo IV págaa con "Só nos
chegou a noticia da lista, na voz doutros", que fai eco de S31 ("na voz doutros, e na man de quen escribía"). As 4 e 5
deixan a cadea de oídas tal como está no documento, e as 6 e 9 deixan as tres reconstrucións coa mesma familia
("Pensemos nela…", "Pensemos nela…", "Podemos pensar nunha noite…").

## 8. Portas sobre a copia coas substitucións

| Porta | Resultado | Quen |
|---|---|---|
| Lingua (`qa.lingua`: LanguageTool gl-ES + hunspell, co dossier da ficha) | **0 avisos** (`scripts/lingua_rapida.py`, co candado da CPU) | automático |
| H1 (nomes e cantidades no dossier) | **55 de 55 ancorados** | automático |
| Estilo | **Correcto:** sen díxitos, signos, preguntas nin palabras vetadas; aviso e fórmula literais; 10 frases fóra de 8-25 palabras (eran 12), todas curtas e buscadas | automático |
| Veracidade con NLI | **Non executada.** Predición léxica: no gancho dan dubidosas S12, S13 (nova), S14, S15, S16 (nova), S17 e S19, e no relato S23 (nova, con nome). S14 xa a aprobou o NLI en r1, e o resto vai xustificado no YAML | automático (predición); pendente |

**Para o orquestrador:** aplicar as substitucións 1-15 e volver pasar `guion/scripts/porta-r1.sh` (ou a súa copia r2)
con `--excepcions excepcions-r1.yaml`; a peza gaña coa porta de veracidade en verde.

## 9. Notas para o DOSSIER, o mapa e a ficha (non bloquean)

1. **F052** (`feitos.yaml`): redactalo como testemuño de oídas, por exemplo "Unha testemuña oíra murmurar entre algúns
   veciños que María do Barro era meiga e que non era boa cristiá", para que non volva saír como feito.
2. **Mapa (S27) e notas (§3.6):** o "de oídas" só se demostra para o folio [3 verso] (María); para Dorotea, o extracto
   non o di.
3. **Ficha v2:** a substitución 15 é da descrición pública. O resto da descrición está ben: atribúe o de Dorotea ("o que
   unha testemuña lle atribuíu"), di "despois do tormento" e non afirma ningunha revisión humana.
4. **Peza DOSSIER:** se se usa a resposta de Inés da Maquieira (notas §5.2), vai atribuída á testemuña e lonxe da zona
   de durmir, porque é unha ameaza.
