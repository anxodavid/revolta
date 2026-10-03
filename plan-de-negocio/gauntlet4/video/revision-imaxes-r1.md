# Revisión das imaxes escollidas da v2 · rolda 1 · planos 1-42 (Gauntlet 4)

**Quen:** un axente Claude (revisor de imaxes), o 03-10-2026 entre as 14:55 e as 15:30 UTC. **Ningunha persoa revisou
estas imaxes.** Primeira pasada (planos 1-42). Os planos 43-77 van nunha segunda pasada cando remate o proceso de
imaxes, nos mesmos ficheiros.

**Saídas:** este documento; [`revision-imaxes-r1.json`](revision-imaxes-r1.json) (`escollas`, `motivos` e
`rexenerar`, para `video/scripts/produccion.py revision`); e as follas que mirei, en
[`follas-revision/`](follas-revision/).

## Contas (planos 1-42)

| Decisión | Planos | Cantos |
|---|---|---|
| **Vale** | 1, 4, 5, 8, 11, 12\*, 13, 14, 15\*, 16, 19\*, 23\*, 24, 27, 28, 33\*, 34, 36 | **18** (5 contra a porta\*) |
| **Outro intento** | 3 → [1], 25 → [1], 26 → [1]\*, 30 → [0], 32 → [2]\*, 35 → [1], 37 → [2]\* | **7** (3 cun intento que a porta rexeitara\*) |
| **Rexenerar** | 2, 6, 7, 9, 10, 17, 18, 20, 21, 22, 29, 31, 38, 39, 40, 41, 42 | **17** (2 con semente: 10 e 21) |

Os problemas máis repetidos:

1. **Arquitectura e interiores alleos** (10 planos): salóns palacianos con lampadario de cristal e ventás altas (20,
   40), fiestras de vidro en casas de aldea (17, 18, 22 e, pequena, no 8), casas inglesas (21), catedral (29), banco
   de parque (42) e farol de parede que parece eléctrico (10).
2. **A queimada sae como lume laranxa** (2, 38, 39 e, aceptables, 11 e 33): nunha pota negra que se le como
   caldeiro (2), unha fogueira grande con multitude que lembra unha queima (38) e un barco ardendo (39). O azul saíu no
   32 ([1] e [2]), onde o prompt dicía «a wide clay bowl of blue flames»; con «burning spirits glowing blue» saíu laranxa.
3. **Falta a clave ou a idea do plano** (6 sen preñada nin home, 29, 42, 35 [3] reserva xenérica, 30 [1] sen
   cunca), e a porta só *avisa* cando falta a clave.
4. **Obxectos e roupa** (7 zapatos de cordóns, 9 vela de bloque moderna, 41 lentes, 25 [2] chaleco e gravata do
   XIX) e **artefactos** (3 [2] pluma acendida, 26 [0] e 37 [0] dúas plumas, 31 lupa de dous aros).
5. **Texto:** nos planos de escritura a porta rexeita *todo* texto. A letra antiga ilexible vale (12, 15, 19, 26,
   32, 35, 37); non vale a pseudopalabra lexible nin a letra de imprenta nun manuscrito (31, 15 [1]).

Non vin mans nin caras deformes graves nas escollidas, nin pseudotexto lexible fóra do 31 e do 15 [1]. Vetos de
`gauntlet3/contexto.md` §8.5: vasoira no 17, caldeiro (de feito) no 2 e lume con multitude no 38-39; ningún
sombreiro de pico, nariz ganchuda nin verruga.

## Como o fixen

- **Datos:** `revision.json` do proceso de imaxes, copiado ás 14:55 UTC (só lido; non o modifiquei) e
  `planos/escenas-v2.json`. As escollas do JSON van co nome de ficheiro exacto; os de «outro intento» comprobei que
  existen en `$SCRATCH/v2/w/imaxes/`.
- **Follas** (`follas-revision/follas-planos-NN-MM.jpg`, 6 planos por folla, 300-390 KB): a escollida a 640 px co
  rótulo da porta, os outros intentos a 320 px ao lado, e debaixo o número, o tipo, as persoas, a prioridade I2V, a
  época, a clave, o texto que se oe e o que dixo a porta en cada intento. Despois de decidir engadín na esquina a
  decisión («Revisión: ...»). Mireinas en recortes de 2 planos (sen reducir).
- **Detalles** (`follas-revision/detalles-*.jpg`): recortes ampliados dos orixinais para o que non se ve a 640 px
  (a bombilla do 18, a pluma acendida do 3, a fiestra e os pés do 8, a letra do 15, 26, 31, 32, 35 e 37, as mans do
  16, 25, 30, 12, 34 e 33).
- **Prompts novos:** sen o prefixo de estilo (16 tokens CLIP), entre 43 e 55 tokens contados co tokenizador de SDXL,
  para deixar sitio ás frases que a pipeline engade nos reintentos («thick granite walls», «smoke-blackened granite
  walls, open stone hearth at floor level», «hands hidden in the sleeves...»), que no 6 e no 40 truncaron o final
  do prompt (no 6 perdeuse o home). O `negativo` vai completo (substitúe o do plano) e só o usa a porta (CLIP), xa
  que coa produción en `IMG_CFG_REINTENTO=0` non hai intentos guiados. Sen `semente`, como pide o orquestrador.

## Plano a plano

[k] = número de intento (o sufixo `-K.png`). «Contra a porta»: a porta rexeitara ese intento e eu acéptoo.

| n | Decisión | Ficheiro | Motivo |
|---|---|---|---|
| 1 | vale | `000-df6db929-1.png` | Dous mouchos sobre pedra con musgo, de noite no bosque: ilustra o que se oe. O sapo non saíu; non fai falta. |
| 2 | rexenerar | — | Lume laranxa nunha pota ou tixola negra de ferro: lese como caldeiro (veto §8.5) e falta a clave (lapas azuis, cunca de barro). Só houbo un intento e a porta aprobouno. |
| 3 | outro intento (contra a porta) | `002-53ec0878-1.png` | No [2] escollido sostén na outra man unha pluma ou un misto acendido (artefacto). O [1] é limpo: escribe nun caderno, con candeas e o porto de noite; o texto non se le (a porta rexeitouno por texto, de máis). |
| 4 | vale | `003-495417ae-0.png` | Barco vello amarrado a un peirao de granito de noite (semente da dorna): correcto. Non se ven os tres homes; non fai falta. |
| 5 | vale | `004-54589876-0.png` | Home con barba e chapeu que escribe con pluma á luz das candeas, con xente detrás: lese como unha declaración ante o tribunal. Para MOVEMENTO: o home escribe e leva o chapeu posto, así que hai que cambiar a acción I2V. |
| 6 | rexenerar | — | Non hai muller preñada nin home: unha vella sentada nunha cama e outra axeonllada diante, que se le como unha enferma. Os tres intentos fallan igual, e no [1] e [2] o prompt truncouse e perdeu o home. |
| 7 | rexenerar | — | Os tres intentos levan zapatos modernos de cordóns (a porta acerta ao rexeitalos, aínda que dea outro motivo). Prompt máis curto, cunha chinela de coiro brando como a do plano 8. |
| 8 | vale | `007-0ae28a3e-0.png` | Home dobrado sobre o banco, coma se lle petase a dor, con zapatos brandos: conta a historia. Defecto menor: ao fondo, noutro cuarto, unha fiestra de vidro pequena e desenfocada. O I2V do salto é fráxil; se deforma, paralaxe. |
| 9 | rexenerar | — | Vela de bloque moderna nun prato negro, cunha bóla escura sen sentido ao lado e sen parede de granito: parece foto de produto actual, e é o plano do aviso. |
| 10 | rexenerar | — | O hórreo sae con tellado de herba e, á dereita, unha caseta cun farol de parede aceso que parece eléctrico. Mesma semente (Muimenta) en img2img 0,5, que segundo o informe de imaxe §4 conserva o hórreo e os tornarratos. |
| 11 | vale | `010-64e96403-0.png` | Tres mozos arredor dunha cunca de barro con lume: unha queimada no século XX, encaixa. Defectos menores: lapa laranxa, contas azuis dentro da cunca e caras ben iluminadas (o prompt quería anonimato). |
| 12 | vale (contra a porta) | `011-53232142-1.png` | Escribán con pluma e candeas, papel sen texto lexible. A porta rexeitouno por texto na imaxe, que nun plano de escritura sobra. Lazo de encaixe ao pescozo algo tardío, aceptable. |
| 13 | vale | `012-c1475796-2.png` | Primeiro plano da parteira: boa calidade e sen artefactos. O pano é claro, non marrón escuro, e mira á cámara. |
| 14 | vale | `013-42727703-0.png` | Pilas de papeis vellos: ilustra o que se oe. Ao fondo hai unha fiestra de vidro desenfocada, crible nun arquivo ou tribunal. |
| 15 | vale (contra a porta) | `014-edb2132a-0.png` | Letra cursiva antiga ilexible, con riscos: vale para un plano de escritura (a porta rexeita por texto). O [1] ten pseudopalabras góticas case lexibles e o [2] parece libro impreso. |
| 16 | vale | `015-b27e8d07-0.png` | A moza da trenza nunha pía de pedra de noite, con lume ao lado e xente que mira desde o fondo: encaixa coa lista e coa noite de san Xoán. Non hai cántaro; as mans están ben. |
| 17 | rexenerar | — | Fiestras de vidro grandes, unha vasoira (veto §8.5), cofias brancas e mandís de tirantes de aspecto holandés, e marcas vermellas na parede. A porta aprobouno. |
| 18 | rexenerar | — | Os tres intentos teñen luz eléctrica ou fiestra de vidro: o [0], unha bombilla acesa no teito; o [1] e o [2], fiestras de cristais. Ademais, o [0] non ten a enferma. Plano clave (a meiga que cura). |
| 19 | vale (contra a porta) | `018-768e74a5-0.png` | Muller que busca entre papeis cunha vela nun arquivo escuro: ilustra o «imos buscalas». Moitas candeas e libros encadernados, sen anacronismos; o texto non se le (a porta rexeitouno por texto). |
| 20 | rexenerar | — | Salón palaciano con lampadario de cristal, ventás altas de vidro en arco e moita xente; María vai cun capuchón vermello de Carapuchiña. A porta aprobouno. |
| 21 | rexenerar | — | Os tres intentos teñen casas inglesas con cheminea e unha muller con capa vermella de Carapuchiña (a porta acerta). Proposta con semente: a palloza (CC BY 3.0), recortada sen a cheminea metálica, en profundidade 0,6. |
| 22 | rexenerar | — | Edificio de pedra con soportais, fiestras de vidro e baixante de canlón: non se le como igrexa de aldea. Dúas persoas separadas, sen murmurio. A porta aprobouno. |
| 23 | vale (contra a porta) | `022-63a520b1-0.png` | María (pano e bufanda vermellos) entre as vacas no monte, co vento: é xusto o que se oe. A porta rexeita por animais en grupo, pero o texto pide o gando arredor. |
| 24 | vale | `023-2e94bcd6-0.png` | Dúas vacas de cornos longos nun regato do monte: ilustra o desexo das sete fontes. Sen a muller, que era opcional. |
| 25 | outro intento (contra a porta) | `024-341e06d7-1.png` | O [2] escollido ten un segundo home de chaleco e gravata do século XIX e ninguén escribe. O [1] é a testemuña de perfil, con barba e roupa de la parda, á luz das candeas; a man sen corpo que viu a porta non se ve. |
| 26 | outro intento (contra a porta) | `025-a9288905-1.png` | O [0] ten dous instrumentos de escribir, un en cada man. O [1]: unha soa man con pluma e puño branco sobre a páxina, e o texto non se le. |
| 27 | vale | `026-7184d1ed-1.png` | Arquiveiro con luvas brancas entre feixes de papeis: encaixa. Viste chaleco e lazo de aspecto antigo; aceptable. |
| 28 | vale | `027-70e923a8-0.png` | Escribán novo con pluma e candeas e, detrás, un home (non a muller): lese como «na voz doutros, e na man de quen escribía». Para MOVEMENTO: non hai muller detrás, así que hai que cambiar a acción I2V. |
| 29 | rexenerar | — | Edificio monumental de columnas e ventás góticas (catedral, que estaba no negativo), tres mulleres e o cura de costas: non é a capela de aldea nin as dúas excomungadas soas. A porta aprobouno. |
| 30 | outro intento (contra a porta) | `029-ffcab11f-0.png` | O [1] escollido non ten a cunca (falta a clave) e ten unha fiestra de vidro. O [0] ten a cunca de barro entre as dúas mulleres no limiar, e as mans están ben (a porta viu mans de máis). |
| 31 | rexenerar | — | Os tres intentos teñen unha lupa deformada (dous aros) e letra de imprenta ou pseudopalabras lexibles dentro da lente. |
| 32 | outro intento (contra a porta) | `031-8b458fe5-2.png` | O [0] ten lume laranxa sobre contas azuis. O [2] ten lapas azuis na cunca de barro e unha folla de versos ilexible (en 1967, mecanografada, é verosímil). |
| 33 | vale (contra a porta) | `032-5d0efc36-0.png` | Tres amigos rindo no barco de noite, co porto ao fondo: é o que se oe. A porta viu un iate moderno que non hai. Defecto menor: o lume é laranxa. |
| 34 | vale | `033-e502ad3e-0.png` | Dous homes len unha folla de noite no porto, coas mans correctas. Falta o brillo azul; aceptable. |
| 35 | outro intento (contra a porta) | `034-440f5505-1.png` | O [3], que a porta aprobou, é a reserva xenérica: un labrego con boina nun prado, nada que ver co que se oe. O [1]: follas de versos espalladas, farol e vela, e texto ilexible. |
| 36 | vale | `035-7e6df055-1.png` | Tenda con mostrador, papeis e cartóns: ilustra «unha empresa vendeu copias». Roupa de mediados do século XX; aceptable. |
| 37 | outro intento (contra a porta) | `036-2831cd58-2.png` | O [0] ten dúas mans de persoas distintas con dúas plumas. O [2]: a man dun home maior asinando un formulario (2001), cunha soa pluma e texto ilexible. |
| 38 | rexenerar | — | Gran fogueira laranxa cunha multitude cos brazos en alto: lembra unha queima (veto de autos de fe) e falta a cunca da queimada. A porta aprobouno. |
| 39 | rexenerar | — | O barco arde: lume enorme na cuberta con cinco homes diante e sen pote (lapas sobre persoas). A porta aprobouno. |
| 40 | rexenerar | — | Salón palaciano con lampadario de cristal, cadros e fiestra de vidro, todos de negro: non se ven as tres xustizas (falta o inquisidor de hábito branco). A porta aprobouno. |
| 41 | rexenerar | — | Os tres intentos: ancián con lentes modernas e as bandas brancas dun xuíz inglés, vestido de negro e non co hábito branco do inquisidor. |
| 42 | rexenerar | — | Dúas figuras de negro nun banco de parque ao aire libre: non hai xuíz, nin sala, nin as tres acusadas. A porta aprobouno. |

## Planos a rexenerar: que cambia no prompt

Os prompts completos e os negativos están no JSON (`rexenerar`). Resumo dos cambios:

| n | Cambio principal | Negativo engadido (para a porta) | Semente |
|---|---|---|---|
| 2 | «pale blue flames» ao principio; cazo de madeira e cunca de barro parda («earthenware») | cauldron, iron pot, frying pan | non (o informe §4: o lume azul sae mellor sen semente) |
| 6 | só o esencial: parteira axeonllada, preñada na palla, home na porta; prompt curto para que non se trunque | metal bed, sofa | non |
| 7 | chinela de coiro brando (como a do plano 8) no canto de «zapato»; a parteira enteira, para que as mans teñan corpo | boots | non |
| 9 | vela fina de cera nun candeeiro de ferro forxado, mesa de carballo e parede de granito | pillar candle, fruit | non |
| 10 | hórreos de madeira e de granito con tornarratos, tellados de pedra, ao serán con brétema | wall lantern, grass roof | **01-02** (Muimenta, CC BY 2.0), img2img 0,5, mesmo recorte |
| 17 | encadre pechado no limiar (sen fachada nin fiestras), a vella debullando fabas | broom, white cap | non (non hai semente de porta de casa) |
| 18 | cama de palla, herbas nas trabes, luz do lume, «smoke-blackened granite walls» | shelves of bottles | non (a 06-01 xa a usa o 55: repetiríase) |
| 20 | mesa simple de madeira, paredes de granito, raio de luz estreito; sen «court» nin «hall» | chandelier, arched windows, red cloak | non |
| 21 | casa de pedra con teito de palla, porta de madeira, lanterna | chimney, red cloak, hood | **03-01** (palloza Cantexeira, CC BY 3.0), profundidade 0,6, recorte [0, 0,3, 0,54, 0,7] sen a cheminea metálica nin a fiestra actual |
| 22 | porta románica de arco de medio punto dunha igrexa pequena de granito | drainpipe, gutter | non (a 12-03 é só unha cornixa) |
| 29 | capela rústica pequena; as dúas mulleres soas | columns, crowd | non |
| 31 | lupa de latón sobre manuscrito de tinta parda, pouca profundidade de campo, letra borrosa | (sen cambios) | non |
| 38 | cunca de barro con lapas azuis pálidas, sen fogueira | bonfire | non |
| 39 | cunca con lapas azuis pálidas na cuberta, só os pés dos tres homes | bonfire, burning boat | non |
| 40 | tres xuíces sentados xuntos: xuíz de toga negra, cura de sotana, frade de hábito branco e capa negra | chandelier, crowd | non |
| 41 | frade ancián de tonsura, hábito branco e capa negra (o inquisidor do elenco), sen lentes | glasses, bookshelves | non |
| 42 | contraplano por detrás do xuíz na súa mesa alta, tres acusadas nun banco tosco | park bench, trees | non |

Créditos das sementes propostas (CC BY pide crédito): «Hórreos de Muimenta, Carballeda de Avia» de José Antonio Gil
Martínez (CC BY 2.0) e «Palloza Cantexeira» de FCPB (CC BY 3.0), vía Wikimedia Commons (URL en
`imaxe/referencias.json`). Para a palloza mirei a foto cunha grade antes de escoller o recorte; a foto non vai ao
repo (material de terceiros).

## Que fai a porta v6 nestes 42 planos

- **Aprobou 29 escollidas; destas, 12 hai que rexeneralas** (2, 6, 9, 10, 17, 20, 22, 29, 38, 39, 40, 42) e **en 4
  había un intento mellor** (3, 25, 30 e o 35, onde aprobou a reserva xenérica sen a clave). Non ve: lampadarios e
  salóns de palacio, fiestras de vidro en casas de aldea, baixantes, bancos de parque, faroles de parede, vasoiras,
  a queimada convertida en caldeiro ou fogueira e a ausencia da clave («falta: ...» só avisa).
- **Rexeitou os tres intentos en 13 planos; en 8 deles había un intento que vale** (12, 15, 19, 23, 33 o escollido;
  26, 32, 37 outro). Rexeita de máis por *texto na imaxe* nos planos de escritura (o problema era a letra lexible ou
  de imprenta, non o texto), por *animais en grupo* cando o texto pide o gando (23), por un *iate moderno* que non hai
  (33) e por *mans* que non vin (25 [1], 30 [0]). Nos outros 5 acertou: zapatos modernos (7, aínda que dixo
  «interior moderno»), bombilla e fiestras (18), casas inglesas (21), lentes (41) e pseudotexto (31).
- **Balance: rexeita de máis nos planos de texto e de gando, e deixa pasar de máis os anacronismos de arquitectura e
  de lume.** Nestas escollidas, o segundo pesa máis: 16 das 29 aprobadas tiñan un problema, fronte a 8 dos 13
  rexeitados que valían. Ideas para a peza IMAXE (non as probei): que «texto na imaxe» só avise cando a clave é de
  escritura (papers, page, quill, document, sheet); que «animais en grupo» só avise cando a clave é o gando; sondas
  CLIP para «crystal chandelier», «palace hall», «park bench», «drainpipe», «broom» e «bonfire»; e non aceptar sen
  revisión un intento con `reserva: true`.

## Notas para MOVEMENTO (acción I2V das imaxes aceptadas)

- **5:** o home leva o chapeu posto e é el quen escribe. Proposta: «the bearded man writes slowly with the quill and
  looks up, the candle flames flicker».
- **13:** mira á cámara. Proposta: «her lips move slightly as she murmurs» (sen «eyes stay lowered»).
- **16:** non hai cántaro: a auga escórrelle dos dedos á pía. Proposta: «water drips from her fingers into the stone
  basin, she slowly looks up into the darkness, the fire flickers».
- **19:** ten papeis na man diante da mesa. Proposta: «she slowly turns the old papers in the candlelight».
- **23:** as vacas están detrás dela. Proposta: «the wind blows her scarf and the grass as she speaks softly, the
  cows graze behind her».
- **25 ([1]):** non hai escribán. Proposta: «the bearded man speaks slowly in profile, the candle flames flicker».
- **28:** detrás hai un home, non a muller. Proposta: «the scribe writes slowly while the man behind him watches in
  silence».
- **8:** o I2V do salto é o máis fráxil (xa o dixo o crítico de planos); se deforma, paralaxe.

## Personaxes recorrentes

- **Dorotea:** no 13 leva pano claro (non marrón escuro) e no 30 [0] vai sen pano e co pelo branco. Os planos 6, 7 e
  29 rexenéranse co pano marrón escuro do elenco.
- **María:** a cor vermella mantense (23, 30 [0]); no 20 e no 21 saía de Carapuchiña e rexenéranse.
- **Escribán:** no 5 é un home con barba e chapeu; no 12 e no 28, un mozo barbeado (é a figura «quen escribía»;
  aceptable). O 12 e o 28 parécense (escribán novo con candeas), pero son o mesmo papel e están a ≈ 2 min.
- **Mariano e os amigos** (3 [1], 33, 34): camisa branca e sen o xersei escuro, coherentes entre si.

## Pendente

- Segunda pasada: planos 43-77, cando remate o proceso de imaxes (mirar primeiro 45, 46, 54, 65, 69 e 70, como pide o
  crítico de planos).
- Mirar os 17 rexenerados cando saian: nos de escritura (31) a porta volverá rexeitar por texto, e nos de semente
  (10, 21) hai que ver se a foto arrastra algo do presente.
