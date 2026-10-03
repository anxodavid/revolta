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
| Planos con correlación ≥ 4 | {{GE4}} de 77 ({{PCT}} %) | 77 de 77 (100 %) | ≥ 90 % |
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
{{TABOA}}

## 2. Contas da lista

- **Coinciden coas do construtor** (comprobadas por script): 77 planos para as frases 1-108, contiguas; 19 / 19 / 24 /
  15 planos por fase; capítulos que abren plano co rótulo en 20, 31, 39, 47 e 63; 44 de 62 planos espertos con
  `persoas: fan` (71,0 %; 47 de 62, 75,8 %, coas mans soas); 57 I2V (27 de prioridade 1 e 30 de prioridade 2) e 20 de
  paralaxe, con cámaras e efectos dentro do que admite `movemento.py`; 4 sementes (4, 10, 55, 68), as catro de uso
  `semente` (CC BY 2.0); 7 prompts > 55 palabras. Erro nas notas: o pseudotexto cita o 38, que non ten papeis (serán
  o 36 e o 37).
- **Correlación:** media {{CM}}; ≥ 4 en {{GE4}} de 77. Por baixo, só o 31 (3): o feixe de papeis non amosa "o máis
  pequeno, unha palabra trabucada". As frases abstractas atan ao fío: 9 (a candea que se acende e que se apaga no 76),
  11 (caras perdidas na sombra: "semellan de ninguén"), 14, 41 (o inquisidor pecha expedientes: "branda"), 60 (o
  murmurio do que nace unha fábula). **Atractivo:** media {{AM}}; os máis fortes, 1, 2, 13, 16, 33, 49, 54, 55, 60, 66 e
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
{{PARCHE}}
```

## 5. Para IMAXE e MOVEMENTO

- Lanzar a xeración con `REVISOR_LUME_DURMIR=0.015`, como xa suxire o comentario de `revisor.py` (o 0,25 % rexeitaba
  velas e brasas en todos os intentos): así deberían pasar 65, 72 e 76; unha queimada laranxa (6 %) segue parando, e
  por iso o 69 pide lapas azul pálido.
- Mirar primeiro a folla dos planos de risco: 2, 8, 40, 45, 46, 54, 65 e 69. Se a porta rexeita por repetición un eco
  buscado (o 70 fronte ao 4), escollelo a man (`escolla_manual`).
- O I2V máis fráxil é o dos saltos (8) e o das mans (55, 18, 44): se o primeiro clip deforma, paralaxe.
