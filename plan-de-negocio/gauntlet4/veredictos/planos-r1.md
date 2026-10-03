# Veredicto do crítico · lista de planos v2 · rolda r1 (Gauntlet 4)

Crítico: espectador esixente de documentais de historia con imaxes xeradas e montador de oficio (axente Claude, que
non participou na lista), 03-10-2026. **Xulgo prompts, non imaxes:** aínda non hai ningunha imaxe xerada e o que digo
do resultado é previsión. Ningunha persoa revisou este veredicto. **Que é automático e que é xuízo:** as contas (fases,
persoas, animación, sementes, palabras, tokens de CLIP, descricións literais dos personaxes, palabras de risco e o que
a pipeline engade ao prompt) saen de scripts do crítico en `$SCRATCH/criticoPlanos-r1/` (`medir.py`, `propostas.py`,
`escribir.py`), que compoñen o prompt final coma `imaxes.compor_prompt` e contan tokens co tokenizador CLIP de SDXL; a
correlación e o atractivo de cada plano son xuízo do crítico lendo cada parella texto-prompt.

## Veredicto: GAÑA, cos cambios da lista pechada (§4)

| Criterio | Tal como vén | Cos cambios do §4 | Obxectivo |
|---|---|---|---|
| Planos con correlación ≥ 4 | 76 de 77 (98,7 %) | 77 de 77 (100 %) | ≥ 90 % |
| Parte esperta (1-62) con persoas facendo algo | 44 de 62 (71,0 %) | 44 de 62 (71,0 %) | ≥ 60 % |
| Arquetipos repetidos | o bodegón do feixe de papeis atado, case igual en 14, 31 e 62 | resolto (31) | ningún |
| Personaxes incoherentes | o home do parto (6, 8) cambia e semella a testemuña; CLIP corta parte do inquisidor (40) e do escribán (45) | resolto | ningún |

A lista é boa: case todas as frases teñen quen, que, onde e con que; as abstractas atan ao fío do guion (o papel, a
auga, o lume); hai rostros, mans e xestos en 44 dos 62 planos espertos e ningunha figura soa de costas. Pero **sen os
cambios non cumpriría o de arquetipos nin o de personaxes**, e en tres planos (40, 45, 46) CLIP non chegaría a ler o
esencial do que se oe: o GAÑA depende de aplicar o §4.

**Maior carencia: o orzamento de tokens.** As notas contan palabras (7 prompts > 55), pero `imaxes.compor_prompt`
antepón "cinematic film still, period drama, photorealistic" e o matiz da fase (10-16 tokens) e, en 13 planos, unha
fórmula de cámara do `tipo`, porque "over-the-shoulder", "close two-shot", "high-angle", "close view" e "wide view" non
están en `CAMARA_RX` (3-7 tokens máis e dúas cámaras que se contradín: "extreme close-up detail shot of close view
of..."). Resultado: **11 prompts pasan de 77 tokens** (5, 12, 28, 29, 40, 45, 46, 54, 58, 69, 71), non 7, e en 40, 45 e
46 o que se perde é esencial. Para o prompt do plano quedan **59 tokens no gancho, 65 na transición, 62 na calma e 61
ao durmir** (≈ 40-45 palabras). Segundo risco: que a porta v6 mande á reserva o 69, a queimada ao durmir (prioridade 1),
por "lume vivo ao durmir" ou polo tope de "persoa á lareira" (§3).

## 1. Plano a plano

C = correlación e A = atractivo (1-5); F = fase (G gancho, T transición, Ca calma, D durmir). "tok" son os tokens do
prompt final que monta a pipeline, só cando pasan de 77.

| n | F | Texto (curto) | C | A | Riscos |
|---|---|---|---|---|---|
| 1 | G | Mouchos, curuxas, sapos e bruxas. | 4 | 5 | I2V dun animal: doado |
| 2 | G | Coas luces apagadas, alguén pronuncia o… | 5 | 5 | fío de lume no I2V; "flames" (arquetipo lareira) |
| 3 | G | Parece de hai séculos. Pero ten autor… | 5 | 4 | — |
| 4 | G | escribiuno Mariano Marcos Abalo nun vello… | 5 | 4 | semente 11-01; eco do 70 (porta de repetición) |
| 5 | G | Vilalba, mil seiscentos dezasete. Unha… | 5 | 4 | 80 tok (perde "17th century"); "cap" → gorra plana |
| 6 | G | que a parteira Dorotea do Barro dixera que… | 5 | 4 | o home, sen roupa e distinto do 8 |
| 7 | G | Abondaría con calzarlle ao home os zapatos da… | 5 | 4 | I2V: mans calzando un zapato |
| 8 | G | E o home saltaría coma un poldro bravo. | 5 | 4 | I2V: salto; o home, distinto do 6 |
| 9 | G | Boas noites. A voz que vas escoitar é… | 4 | 3 | aviso: candea que se apaga no 76 |
| 10 | G | Isto é Cousas de Galiza para durmir. | 4 | 4 | semente 01-02 con recorte |
| 11 | G | As palabras do conxuro parecen vellas e son… | 4 | 4 | "flames" (arquetipo lareira) |
| 12 | G | O que se contou de Dorotea é vello de… | 5 | 3 | 78 tok; mesmo cadro ca o 59 |
| 13 | G | As palabras que ela sabía, esas non as… | 5 | 5 | — |
| 14 | G | Nos papeis daqueles procesos hai moitas máis… | 4 | 3 | bodegón do feixe (1 de 3) |
| 15 | G | Hai unha palabra trabucada que ninguén borrou… | 5 | 3 | pseudotexto (é o suxeito) |
| 16 | G | E hai mesmo noticia dunha lista coas mulleres… | 4 | 5 | — |
| 17 | G | Había mulleres de aldea detrás de todas esas… | 4 | 3 | — |
| 18 | G | A meiga, moitas veces, non era a bruxa dos… | 4 | 4 | fórmula de cámara anteposta; entrega no I2V |
| 19 | G | Esta noite imos buscalas no pouco que delas… | 4 | 4 | vela na man (biblia §4) |
| 20 | T | En Vilalba, a Real Audiencia xulgou tamén a… | 5 | 4 | golilla (1623) en 1617 |
| 21 | T | Da filla dicían outra cousa: que era… | 5 | 4 | — |
| 22 | T | Unha testemuña oíu murmurar entre algúns… | 5 | 4 | — |
| 23 | T | E contou que María, cando tiña o gando no… | 5 | 4 | luz por defecto contra "grey clouds" |
| 24 | T | E, entre elas, un desexo para o gando: que… | 4 | 3 | — |
| 25 | T | Eran palabras para o gando, non para un… | 5 | 4 | — |
| 26 | T | No papel quedou ata a emenda de quen… | 5 | 3 | pseudotexto (é o suxeito) |
| 27 | T | O papel gárdao o Arquivo do Reino de Galicia… | 5 | 3 | pseudotexto (é o suxeito) |
| 28 | T | Así nos chegan as palabras daquelas mulleres… | 5 | 4 | 80 tok (perde a candea) |
| 29 | T | E as palabras tamén podían pechar portas. O… | 5 | 4 | 87 tok (perde "stand alone below him") |
| 30 | T | Auga de sete fontes para o gando. E para… | 5 | 4 | — |
| 31 | T | Aquel papel gardou ata o máis pequeno, unha… | 3 | 2 | bodegón do feixe (2 de 3) co rótulo do cap. II |
| 32 | T | Ao conxuro da queimada pasoulle ao revés… | 4 | 3 | pseudotexto |
| 33 | T | Mariano Marcos Abalo xuntábase cos amigos a… | 5 | 5 | "flames" (arquetipo lareira) |
| 34 | T | Contaba que escribira o conxuro para darlles… | 5 | 4 | — |
| 35 | T | E que houbo outros cinco ou seis conxuros… | 4 | 2 | bodegón; pseudotexto |
| 36 | T | Unha empresa vendeu copias do conxuro sen o… | 4 | 3 | pseudotexto nas tarxetas |
| 37 | T | En dous mil un, o autor rexistrouno como… | 5 | 2 | pseudotexto no formulario |
| 38 | T | Así, unhas palabras sen nome no papel… | 4 | 3 | multitude: caras clonadas; "flames" |
| 39 | Ca | O conxuro naceu entre amigos, arredor dun… | 4 | 3 | fórmula de cámara anteposta |
| 40 | Ca | As palabras dos procesos acabaron noutro… | 4 | 3 | 92 tok (perde o hábito do inquisidor); 3 personaxes |
| 41 | Ca | Para o investigador Diego Valor Bravo, coas… | 4 | 3 | — |
| 42 | Ca | Os xuíces civís foron moito máis duros. E nos… | 5 | 4 | fórmula de cámara anteposta |
| 43 | Ca | Unha delas foi María Cibreira, procesada en… | 4 | 4 | — |
| 44 | Ca | Que llo ensinara a súa nai. Que á nai acudía… | 4 | 4 | 4 ou máis persoas |
| 45 | Ca | E que as noites de san Xoán as meigas ían ás… | 4 | 4 | 94 tok (perde o escribán que escribe) |
| 46 | Ca | Rodrigo Pousa, historiador, explica que… | 4 | 4 | 86 tok (perde o aceno); quen le? |
| 47 | Ca | Unha noite de san Xoán aparece tamén nos… | 4 | 3 | paisaxe baleira (co rótulo do cap. IV) |
| 48 | Ca | En mil seiscentos corenta e tres, a Real… | 5 | 4 | — |
| 49 | Ca | Unha testemuña contou que, pola sospeita que… | 5 | 5 | fórmula de cámara anteposta |
| 50 | Ca | Alí, dixo, viron e recoñeceron as mulleres, e… | 5 | 4 | escribe sen dicir con que |
| 51 | Ca | Pensemos nunha noite curta de xuño: a auga… | 5 | 4 | ollos: monstro?; mesmo cadro ca o 63 |
| 52 | Ca | Do que elas dixesen aquela noite, non nos… | 4 | 4 | — |
| 53 | Ca | A noite de san Xoán era costume ir ás fontes… | 5 | 4 | — |
| 54 | Ca | E na crenza popular, era tamén a noite en que… | 5 | 5 | 82 tok; persignarse no I2V |
| 55 | Ca | Moitas das acusadas eran parteiras e… | 5 | 5 | I2V: catro mans; semente 06-01 |
| 56 | Ca | Moitas denuncias nacían de liortas entre… | 5 | 4 | — |
| 57 | Ca | E, con todo, para Pousa aquelas mulleres eran… | 4 | 4 | — |
| 58 | Ca | Xa no século dezaoito, frei Martín Sarmiento… | 5 | 3 | 78 tok (perde "century") |
| 59 | Ca | No mesmo século, o frade Benito Xerónimo… | 4 | 3 | mesmo cadro ca o 12 |
| 60 | Ca | Así, para el, unha fábula nacida no recuncho… | 4 | 5 | — |
| 61 | Ca | E admitía que moitas veces o voo das bruxas… | 4 | 4 | a sombra pode non saír |
| 62 | Ca | E aquí deixamos os papeis. Desde agora a… | 4 | 3 | bodegón do feixe (3 de 3) |
| 63 | D | É outra vez aquela noite de xuño, e esta vez… | 5 | 3 | fórmula anteposta; mesmo cadro ca o 51 |
| 64 | D | Para facer o cacho, alguén colle auga de sete… | 4 | 3 | — |
| 65 | D | Lonxe, cando a cacharela xa case se apaga, a… | 5 | 4 | I2V: salto; lume ao durmir; "embers" |
| 66 | D | Ao amencer, a primeira auga da fonte chámase… | 5 | 5 | I2V: auga nas mans |
| 67 | D | Despois, os ramos de herbas colgan secos… | 5 | 3 | fórmula anteposta |
| 68 | D | Outra noite, nunha cociña de aldea, tras a… | 5 | 4 | semente 07-01; luz por defecto "mist in the moonlight" |
| 69 | D | Os comensais xúntanse arredor do pote, para… | 5 | 5 | 87 tok; lume ao durmir (porta) |
| 70 | D | Mouchos, curuxas, sapos e bruxas. Agora xa… | 4 | 4 | eco do 4 (porta de repetición) |
| 71 | D | E alguén di aquel dito tan coñecido: eu non… | 5 | 4 | 86 tok; cara á cámara ao durmir |
| 72 | D | As lapas do alcohol van baixando amodo, ata… | 4 | 3 | fórmula anteposta; lume ao durmir |
| 73 | D | A outra meiga, a dos contos, saíu das fábulas… | 4 | 4 | — |
| 74 | D | Agora chove sobre as lousas do tellado, unha… | 5 | 4 | — |
| 75 | D | Lonxe, as sete fontes seguen correndo na… | 4 | 3 | fórmula anteposta |
| 76 | D | A casa descansa baixo a chuvia, e xa non tes… | 5 | 4 | fórmula anteposta; vela ao durmir; apagala no I2V |
| 77 | D | Boas noites. | 4 | 3 | fórmula anteposta |

## 2. Contas da lista

- **Coinciden coas do construtor** (comprobadas por script): 77 planos para as frases 1-108, contiguas; 19 / 19 / 24 /
  15 planos por fase; capítulos que abren plano co rótulo en 20, 31, 39, 47 e 63; 44 de 62 planos espertos con
  `persoas: fan` (71,0 %; 47 de 62, 75,8 %, coas mans soas); 57 I2V (27 de prioridade 1 e 30 de prioridade 2) e 20 de
  paralaxe, con cámaras e efectos dentro do que admite `movemento.py`; 4 sementes (4, 10, 55, 68), as catro de uso
  `semente` (CC BY 2.0); 7 prompts > 55 palabras. Erro nas notas: o pseudotexto cita o 38, que non ten papeis (serán
  o 36 e o 37).
- **Correlación:** media 4,5; ≥ 4 en 76 de 77. Por baixo, só o 31 (3): o feixe de papeis non amosa "o máis
  pequeno, unha palabra trabucada". As frases abstractas atan ao fío: 9 (a candea que se acende e que se apaga no 76),
  11 (caras perdidas na sombra: "semellan de ninguén"), 14, 41 (o inquisidor pecha expedientes: "branda"), 60 (o
  murmurio do que nace unha fábula). **Atractivo:** media 3,8; os máis fortes, 1, 2, 13, 16, 33, 49, 54, 55, 60, 66 e
  69; os máis febles, 31, 35 e 37 (dous bodegóns e unha man que asina; o 35 e o 37 quedan porque din a frase).
- **Persoas na parte esperta:** 44 de 62. En dous a imaxe é case quieta e o xesto vén do I2V (30, sentadas no limiar;
  42, o xuíz que mira): aínda sen eles, 42 de 62 (67,7 %).
- **Arquetipos:** figura soa de costas, 0; paisaxe baleira na parte esperta, 1 (o 47, que abre o capítulo IV co
  rótulo); retrato 2, 13, 25, 60 (máis os dous-planos 46 e 54); mans 7, 26, 37, 68; grupo de pé 22, 52.
  **Repetido:** o bodegón do feixe de papeis atado cun cordón nun raio de luz, case o mesmo cadro en 14, 31 e 62 (e as
  follas do 35). Motivos que son o fío e varían o encadre, pero a vixiar: alguén que escribe á luz dunha candea ou
  lanterna (3, 5, 12, 25, 28, 45, 50, 59; o 12 e o 59 son case o mesmo cadro), a cunca de lapas azuis (2, 11, 32, 33,
  38, 39, 69, 72) e a fonte de noite (16, 47, 49, 51, 52, 54, 63; o 51 e o 63 son case o mesmo cadro).
- **Personaxes:** as 18 descricións da táboa `personaxes` van literais en todos os seus planos (script). Fallan o home
  do parto, que non está na táboa e cambia (6: "a worried bearded man", sen roupa; 8: "a startled burly bearded peasant
  man in a coarse wool shirt") e semella a testemuña (5, 25: "a bearded peasant man in a coarse brown wool jacket"), e
  os cortes de CLIP: "habit and black cape" do inquisidor no 40 e "with a white collar writes beside him with a goose
  quill" do escribán no 45.
- **Época:** os 18 planos do século XX levan `epoca: "xx"` e ningún do XVII trae obxectos do XX. Leve: a golilla do
  xuíz é de 1623 en diante e o 20 pasa en 1617; SDXL tampouco coñece a palabra, e "stiff white collar" vale para 1617
  e para 1639.

## 3. Riscos técnicos de SDXL, da porta v6 e do I2V

1. **CLIP, 77 tokens** (ver o veredicto). Perdas esenciais: 40 (o hábito do inquisidor e a luz), 45 (o escribán que
   escribe: a metade da frase), 46 ("nods in silence" queda fóra, e a frase permite ler que é ela quen le), 29 ("stand
   alone below him"). Menores: 5, 12 e 58 (o século), 28 (a candea), 54 (a fogueira), 69 e 71 (o final). A pipeline
   mete unha luz por defecto cando o prompt non nomea ningunha: 23 ("low winter sun" contra "low grey clouds") e 68
   ("mist in the moonlight" nun cuarto, que convida a unha fiestra).
2. **Porta v6, lume ao durmir** (`revisor.py`: `LUME_DURMIR` = 0,25 % de píxeles cor de chama, salvo
   `REVISOR_LUME_DURMIR`; medido alí: queimada 6,0 %, fogueira 0,33 %, vela 0,40 %). O 69 (queimada ao durmir,
   prioridade 1) sae rexeitado en todos os intentos se as lapas saen laranxas, e acabaría na reserva da fase (unha
   fraga con néboa ou unhas brasas): adeus á correlación. Co limiar por defecto poden caer tamén 65 (fogueira e
   faíscas), 72 e 76 (a vela).
3. **Porta v6, arquetipo "persoa á lareira"** (só conta se o prompt di fire, flames, embers, hearth...; tope 5 con 77
   planos e 5 de separación): 2, 11, 33, 38, 55, 65 e 69 levan esas palabras e persoas. Se CLIP os ve como lareira, o
   69 queda a 4 planos do 65 e pasa do tope: outra vez á reserva.
4. **Porta v6, repetición** (CLIP ≥ 0,90 contra todas as imaxes aceptadas): case o mesmo cadro en 51 e 63, 4 e 70 (eco
   buscado), 12 e 59, e 14, 31 e 62.
5. **Palabras que SDXL fai mal.** Ben: ningún "kitchen", "street", "road" nin "door" sós; o 21 usa a forma da biblia
   ("heavy oak door of a granite house") e as casas son sempre de granito. Riscos: 5 "cap" (gorra plana ou de béisbol,
   biblia §4); 19 unha vela na man (lapas imposibles, biblia §4); 38 unha multitude (caras clonadas); 44 catro ou máis
   persoas; 50 escribe sen dicir con que (bolígrafo ou lapis). Pseudotexto: 15, 26 e 27 (a letra é o suxeito:
   aceptable), 32, 35, 36 e 37.
6. **I2V.** Saltos: 8 (o máis fráxil) e 65; mans complexas: 7 (calzar un zapato) e 55 (catro mans no morteiro); medios:
   54 (persignarse), 18 e 44 (entregar unha cunca ou un pote), 66 (auga nas mans), 76 (que a vela se apague de
   verdade), 61 (a sombra pode non saír). Duración: 23 planos I2V duran 10 s ou máis (65: 22,7 s; 66: 20,7 s) e un clip
   de LTX dura 2-4 s; xa o avisan as notas para MOVEMENTO.
7. **Vetos (`gauntlet3/contexto.md` §8.4-8.5):** cumpridos. Bruxa, vasoira, sombreiro de pico e verrugas só nos
   negativos; a tortura fóra de cadro (43); o parto sen nada explícito (6); o salto, sobre brasas baixas e lonxe (65);
   ao durmir, sen intrusións (os ollos do 51 e a sombra do 61 caen na calma).

## 4. Lista pechada de cambios

**Regra para os personaxes**, porque a descrición completa de dous ou tres personaxes non cabe en 59-65 tokens: o
personaxe con cara en foco leva a descrición da táboa; os demais, unha **sinatura curta, sempre coas mesmas palabras**
(campo novo `prompt_curto` na táboa): María "a woman of about thirty in a faded red wool headscarf"; Dorotea "an old
midwife in a dark brown wool headscarf"; o escribán "a gaunt clean-shaven scribe in a black wool doublet"; Cibreira de
costas "a woman in a grey wool headscarf". O xuíz pasa a ser en todos os seus planos (20, 40, 42, 45, 46) "a stern
grey-bearded judge in a black gown with a stiff white collar", sen golilla, e o home do parto entra na táboa. Todos os
prompts do parche están comprobados contra o prompt final da pipeline: ningún pasa de 77 tokens nin recibe fórmula de
cámara anteposta.

**Obrigatorios** (correlación < 4 ou risco serio):

1. **31** (C 3; bodegón repetido; abre o capítulo II): a lupa sobre a palabra riscada, sen mans nin feixe; `epoca:
   "xx"`, `persoas: "non"`, paralaxe que avanza cara á lente. Correlación prevista 4-5 ("ata o máis pequeno").
2. **40** (92 tok; tres xustizas nun cadro): prompt curto coas tres roupas dentro dos tokens, e paralaxe `pan_der` que
   descobre as tres mesas na orde en que se nomean (civil, eclesiástica, Inquisición) se SDXL as pon así; se non,
   `pan_esq`.
3. **45** (94 tok): o xuíz pregunta e o escribán escribe, dentro dos 77.
4. **46** (86 tok): a acción vai antes e sen ambigüidade: el le a pregunta e ela asente calada.
5. **29** (87 tok): sinaturas curtas; as dúas mulleres soas baixo o vicario; luz.
6. **69** (87 tok; lume ao durmir): lapas azul pálido, dúas persoas e as caras azuis dentro dos tokens; negativo +
   "fireplace, candles". Non poño "orange flames" no negativo: a biblia §7 desaconsella negar variantes do suxeito.
7. **65** (salto e lume ao durmir): unha silueta suspendida no aire sobre o brillo vermello apagado, sen faíscas nin
   "embers"; paralaxe que recua, con fume e néboa.
8. **6 e 8** (o home do parto): o mesmo home nos dous e distinto da testemuña; no 8, unha acción de erguerse dun pulo
   en vez dun salto.
9. **54 e 71** (82 e 86 tok): reescritos; no 54, o I2V sen persignarse (a cruz queda na imaxe); no 71, de perfil, sen
   cara á cámara ao durmir.
10. **38** (multitude): siluetas de costas contra o brillo azul, sen caras.
11. **19** (vela na man): a candea nun candeeiro de ferro.
12. **Fórmulas de cámara** (18, 39, 42, 49, 67, 72, 75, 76, 77; o 45, 46, 54 e 63 xa van arriba): empezar por unha
    expresión que `CAMARA_RX` recoñece ("over-the-shoulder medium shot", "overhead shot", "close-up", "wide shot").

**Recomendados** (non cambian o veredicto, pero aforran rexeitamentos ou dan variedade): 5 (un sombreiro de feltro
contra o peito en vez de "cap"); 7 (paralaxe que baixa da cara murmurando ás mans co zapato, en vez dun I2V de mans);
11 e 33 ("burning spirits glowing blue", coma o 39: fóra do arquetipo lareira); 20 e 42 (o xuíz sen golilla); 23 e 68
(a luz no prompt); 28 (sinatura de María e a candea dentro dos tokens); 55 (acción cunha soa man que move); 59 (Feijoo
de día nun atril, para non repetir o cadro do 12); 63 (a lúa reflectida na pía, vista desde arriba, para non repetir o
51).

O parche, listo para substituír en `escenas-v2.json` (só os campos que cambian; `texto`, `texto_en`, `frases` e `son`
quedan igual):

```json
{
 "personaxes": {
  "xuiz": {"prompt": "a stern grey-bearded judge in a black gown with a stiff white collar"},
  "home_parto": {"quen": "o home do conto de Dorotea (Vilalba, 1617)", "prompt": "a burly man with a short black beard in a coarse linen shirt"},
  "maria": {"prompt_curto": "a woman of about thirty in a faded red wool headscarf"},
  "dorotea": {"prompt_curto": "an old midwife in a dark brown wool headscarf"},
  "escriban": {"prompt_curto": "a gaunt clean-shaven scribe in a black wool doublet"},
  "cibreira": {"prompt_curto": "a woman in a grey wool headscarf"}
 },
 "escenas": {
  "5": {"prompt": "medium shot of a bearded peasant man in a coarse brown wool jacket, a felt hat held to his chest, testifying while a gaunt clean-shaven scribe of about forty in a black wool doublet with a white collar writes with a goose quill, candlelight, bare granite walls", "negativo": "electric light, light bulb, lamp, glass window, modern clothes, street lamp, glasses, framed pictures, bookshelves, flat cap, baseball cap, cowboy hat", "animacion": {"modo": "i2v", "camara": "avanza", "efectos": ["candea"], "accion": "the man speaks, holding his hat to his chest, while the scribe writes"}},
  "6": {"prompt": "medium shot of an old midwife of about sixty, lined face, grey hair under a dark brown wool headscarf, laying her hand on the brow of a heavily pregnant young woman in a straw bed, a burly man with a short black beard in a coarse linen shirt watching, side light"},
  "7": {"animacion": {"modo": "paralaxe", "camara": "baixa", "efectos": ["candea"]}, "prioridade_i2v": 3},
  "8": {"prompt": "full shot of a burly man with a short black beard in a coarse linen shirt, startled, leaping up from a low wooden bench with his arms flung wide, small women's shoes on his feet, bare granite room lit from an open doorway, 17th century", "animacion": {"modo": "i2v", "camara": "recua", "efectos": [], "accion": "he jolts upright from the bench and flings his arms wide"}},
  "11": {"prompt": "medium shot of a wide clay bowl of burning spirits glowing blue on a dark wooden table, three people around it with their faces lost in shadow, only their hands lit as they raise small clay cups toward the blue glow, darkness all around, 20th century"},
  "18": {"prompt": "over-the-shoulder medium shot of an old village healer in a dark blue wool shawl handing a steaming clay bowl of herbal infusion to a sick young woman lying under a wool blanket, bunches of dried herbs hanging behind, warm light from the side, dignified and ordinary"},
  "19": {"prompt": "medium shot of a woman in a dark wool shawl holding up a candle in an iron holder to tall wooden shelves of old bundles of papers tied with cords, searching among them in a dark archive at night, candlelight on her face"},
  "20": {"prompt": "medium shot of a woman of about thirty, dark braided hair under a faded red wool headscarf, standing before a court table in a bare granite hall while a stern grey-bearded judge in a black gown with a stiff white collar points his quill at her, light from a high opening"},
  "23": {"prompt": "medium shot of a woman of about thirty, dark braided hair under a faded red wool headscarf, standing among brown cows on a windswept hillside of heather and gorse, murmuring words to them, her scarf and the long grass blown by the wind, overcast sky"},
  "28": {"prompt": "medium shot of a gaunt clean-shaven scribe of about forty in a black wool doublet with a white collar writing with a goose quill by candlelight in the foreground, and behind him in shadow a woman of about thirty in a faded red wool headscarf, standing silent, lips closed"},
  "29": {"prompt": "wide shot of a stern priest in a black cassock and black cape reading a decree aloud on the steps of a small granite church, below him two women stand alone, an old midwife in a dark brown wool headscarf and a woman of about thirty in a faded red wool headscarf, overcast light"},
  "31": {"prompt": "extreme close-up of an old magnifying glass resting on a yellowed 17th-century page, the round lens enlarging one small handwritten word struck through with a single line of ink, soft daylight in a quiet archive", "clave": "magnifying glass", "negativo": "hands, fingers, electric lamp, printed text, typewriter, plastic, computer", "tipo": "detalle", "epoca": "xx", "persoas": "non", "arquetipo_previsto": "", "animacion": {"modo": "paralaxe", "camara": "avanza", "efectos": ["po"]}, "prioridade_i2v": 3},
  "33": {"prompt": "medium shot of a dark-haired man of about forty in a white shirt and dark wool sweater, and two friends in white shirts and dark wool sweaters, laughing on coils of rope around a clay bowl of burning spirits glowing blue on the deck of an old wooden boat in a harbour at night"},
  "38": {"prompt": "wide shot of a village festival at night seen from behind the crowd, dark silhouettes of people raising small clay cups toward a large clay bowl of burning spirits glowing blue on a stone table, the blue glow on their raised hands"},
  "39": {"prompt": "overhead shot of a wide clay bowl of burning spirits glowing blue on the wooden deck of a boat at night, the shoes and trouser legs of three men standing around it, coils of rope nearby, 1960s"},
  "40": {"prompt": "wide shot of three separate judges' tables in a bare granite hall: a stern grey-bearded judge in a black gown with a stiff white collar signing a paper, a priest in a black cassock and black cape, an elderly inquisitor in a white habit and black cape, light from a high opening", "animacion": {"modo": "paralaxe", "camara": "pan_der", "efectos": ["po"]}, "prioridade_i2v": 3},
  "42": {"prompt": "over-the-shoulder medium shot from behind a stern grey-bearded judge in a black gown with a stiff white collar, looking down at three accused village women in dark headscarves seated on a wooden bench below him, cold light from a high opening, bare granite hall"},
  "45": {"prompt": "over-the-shoulder medium shot from behind a woman in a grey wool headscarf: a stern grey-bearded judge in a black gown with a stiff white collar asks her a question, and beside him a gaunt clean-shaven scribe in a black wool doublet writes with a goose quill, candlelight"},
  "46": {"prompt": "close-up two-shot in profile: a stern grey-bearded judge in a black gown with a stiff white collar reads a question from a paper to a pale exhausted woman of about forty, dark hair under a grey wool headscarf, who nods in silence with her lips closed, candlelight"},
  "49": {"prompt": "over-the-shoulder medium shot of two village men in sheepskin vests and wool breeches, crouching behind a mossy granite wall at night, peering at distant women gathered at a stone fountain lit by a small bonfire, deep shadows"},
  "54": {"prompt": "close-up two-shot at a granite fountain at night: a young woman with a long dark braid, white linen blouse and dark shawl smiles as she fills a clay jug, and an old woman beside her makes the sign of the cross, looking warily into the darkness, moonlight", "animacion": {"modo": "i2v", "camara": "avanza", "efectos": ["auga"], "accion": "the old woman slowly turns her head toward the darkness while the young woman fills the jug"}},
  "55": {"animacion": {"modo": "i2v", "camara": "avanza", "efectos": ["lume"], "accion": "the girl slowly grinds the herbs with the pestle while her mother's hand rests on hers"}},
  "59": {"prompt": "medium shot of an elderly Benedictine monk with thin white hair and a lined face, in a black hooded habit, writing with a quill at a tall wooden lectern in a bare stone monastery cell, a pile of closed leather books beside him, soft morning light from a small shuttered opening", "animacion": {"modo": "i2v", "camara": "avanza", "efectos": [], "accion": "the monk writes, pauses and looks up thoughtfully"}},
  "63": {"prompt": "high-angle close-up of the full moon reflected in the still water of a brimming granite fountain basin, ferns and moss around its edge, a thin stream falling from the spout, soft mist, no one around"},
  "65": {"prompt": "wide shot of a dark meadow at night where, far away, small silhouettes of villagers stand around the last dull red glow of a dying Saint John's bonfire, one of them caught in mid-leap over it, thin smoke rising, calm", "animacion": {"modo": "paralaxe", "camara": "recua", "efectos": ["fume", "bretema"]}, "prioridade_i2v": 3},
  "67": {"prompt": "close-up of bunches of dried herbs and flowers hanging from a dark wooden beam beside the doorway of a granite farmhouse, dust floating in a soft sunbeam, quiet"},
  "68": {"prompt": "close-up of an earthenware jug held by an old woman's hand pouring clear spirits into a wide clay bowl holding sugar, lemon peel and coffee beans, small clay cups hanging on its rim, in a dim room after supper, faint light from a small shuttered opening"},
  "69": {"prompt": "medium shot of an old man with white stubble in a dark wool waistcoat lifting a clay ladle of pale blue flames and letting it fall slowly back into a wide clay bowl, an old woman in a black cardigan and dark headscarf watching, their faces lit blue in a dark room", "negativo": "neon, plastic, television, smartphone, light bulb, modern kitchen, glass, fireplace, candles"},
  "71": {"prompt": "medium close-up in profile of an old woman in a black cardigan and dark headscarf, smiling and raising one finger as she speaks to an old man with white stubble in a dark wool waistcoat who laughs softly, small clay cups in their hands, soft blue glow in a dark room"},
  "72": {"prompt": "close-up of the last low blue tongues of burning spirits dying in a wide clay bowl on a wooden table, the dark room behind lit only by a dim red glow, an old bundle of papers tied with a faded red cord lying beside the bowl"},
  "75": {"prompt": "wide shot of a small stream running gently down between mossy stones and ferns at night under a fine rain, toward a misty river valley, faint moonlight on the wet stones, no one around"},
  "76": {"prompt": "close-up of a single candle burning on the deep stone sill of a small open wooden shutter in the thick granite wall of a dark house at night, fine rain falling past it from the slate eaves, calm"},
  "77": {"prompt": "close-up of fine rain falling on the dark wet slates of an old granite house roof at night, drops gathering and dripping from the edge, moss between the slates, deep blue darkness, calm"}
 }
}
```

## 5. Para IMAXE e MOVEMENTO

- Lanzar a xeración con `REVISOR_LUME_DURMIR=0.015`, como xa suxire o comentario de `revisor.py` (o 0,25 % rexeitaba
  velas e brasas en todos os intentos): así deberían pasar 65, 72 e 76; unha queimada laranxa (6 %) segue parando, e
  por iso o 69 pide lapas azul pálido.
- Mirar primeiro a folla dos planos de risco: 2, 8, 40, 45, 46, 54, 65 e 69. Se a porta rexeita por repetición un eco
  buscado (o 70 fronte ao 4), escollelo a man (`escolla_manual`).
- O I2V máis fráxil é o dos saltos (8) e o das mans (55, 18, 44): se o primeiro clip deforma, paralaxe.
