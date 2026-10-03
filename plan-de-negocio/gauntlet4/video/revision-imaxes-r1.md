# Revisión das imaxes escollidas da v2 · rolda 1 · planos 1-77 (Gauntlet 4)

**Quen:** un axente Claude (revisor de imaxes), o 03-10-2026, en dúas pasadas: planos 1-42 entre as 14:55 e as 15:30
UTC (o orquestrador xa a aplicou) e planos 43-77 entre as 17:55 e as 19:15 UTC. **Ningunha persoa revisou estas
imaxes.**

**Saídas:** este documento; [`revision-imaxes-r1.json`](revision-imaxes-r1.json) (`escollas`, `motivos` e
`rexenerar`, para `video/scripts/produccion.py revision`); e as follas que mirei, en
[`follas-revision/`](follas-revision/).

## Contas

| Decisión | Planos 1-42 | Planos 43-77 | **Total 1-77** |
|---|---|---|---|
| Vale | 18 | 11 | **29** |
| Outro intento | 7 | 3 | **10** |
| Rexenerar | 17 | 21 | **38** |

**Primeira pasada (planos 1-42):**

| Decisión | Planos | Cantos |
|---|---|---|
| **Vale** | 1, 4, 5, 8, 11, 12\*, 13, 14, 15\*, 16, 19\*, 23\*, 24, 27, 28, 33\*, 34, 36 | **18** (5 contra a porta\*) |
| **Outro intento** | 3 → [1], 25 → [1], 26 → [1]\*, 30 → [0], 32 → [2]\*, 35 → [1], 37 → [2]\* | **7** (3 cun intento que a porta rexeitara\*) |
| **Rexenerar** | 2, 6, 7, 9, 10, 17, 18, 20, 21, 22, 29, 31, 38, 39, 40, 41, 42 | **17** (2 con semente: 10 e 21) |

**Segunda pasada (planos 43-77):**

| Decisión | Planos | Cantos |
|---|---|---|
| **Vale** | 43, 50, 53, 55, 56\*, 57, 59\*, 60, 62\*, 66, 75 | **11** (3 contra a porta\*) |
| **Outro intento** | 71 → [0]\*, 73 → [2]\*, 76 → [0]\* | **3** (os tres cun intento que a porta rexeitara\*) |
| **Rexenerar** | 44, 45, 46, 47, 48, 49, 51, 52, 54, 58, 61, 63, 64, 65, 67, 68, 69, 70, 72, 74, 77 | **21** (2 con semente: 68 e 70) |

Os problemas máis repetidos na primeira pasada (1-42):

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

Na segunda pasada (43-77):

1. **Fontes de xardín e de parque** no canto da fonte de aldea (47, 51, 63 e, pequena, no 66), e ningunha fonte onde
   facía falta (49, 54). Os prompts novos piden en todos a mesma fonte rústica: un cano de pedra nun muro de granito
   con musgo e unha pía.
2. **Lume:** a queimada laranxa (69; no 72, nunha pota negra de ferro), un incendio no canto das brasas da cacharela
   (65) e luz de día cando o texto di «apáganse as luces» (68).
3. **Xente doutro tempo ou doutro sitio:** damas e xuíces do XIX (45, e o 46 cunha viñeta branca de retrato
   antigo), labregos irlandeses con tellados de herba (48 e, ao fondo, o 57), paredes encaladas mediterráneas (44) e
   un rito de túnicas con capucha arredor dun lume (52, que lembra os vetos).
4. **Falta a clave ou a idea:** sen talla (64), sen a herba nin a curandeira de Sarmiento (58), sen o soño do voo e
   cunha muller tendida coma amortallada (61), ninguén espreitando (49).
5. **Anacronismos:** vacas frisoas e lámpadas de parede (74), fiestras de vidro (67), unha bufarda inglesa con
   fiestras acesas na última imaxe (77) e un vaso que parece de papel (44). No 76 a porta volveu aprobar a reserva
   xenérica (un bosque) sen a candea.

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
- **Segunda pasada:** `revision.json` copiado ás 17:53 UTC (77 entradas; só lido), coas mesmas follas
  (`follas-planos-43-48.jpg` … `follas-planos-73-77.jpg`) e detalles (`detalles-43-44-50-59`, `detalles-44-62`,
  `detalles-68-71-73-76`). O JSON leva agora os planos 1-77. As entradas dos planos 1-42 non cambiaron: se xa están
  aplicadas, abonda coas dos planos 43-77, e aplicar o JSON enteiro repite as mesmas escollas e os mesmos prompts.

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
| 43 | vale | `042-8f6f62a0-0.png` | María Cibreira co pano gris, sentada, e as outras veciñas agardando detrás: é o que se oe. As luces da parede son candeas; sen anacronismos. |
| 44 | rexenerar | — | Paredes encaladas e talladas grandes de aspecto mediterráneo, e a visitante leva unha cunca que parece un vaso de papel con tapa. Non hai pote de unguento nin neno, e a curandeira non leva o pano negro. Os outros dous intentos tamén son mediterráneos. |
| 45 | rexenerar | — | Os tres intentos: unha dama vitoriana con vestido negro e pendentes diante dun xuíz do XIX entre candelabros. Non é María Cibreira (no 43, campesiña de pano gris) e falta o escribán. |
| 46 | rexenerar | — | Retrato de tres caras con marco branco esvaído (viñeta) e roupa do XIX; sen papel nin pregunta, e a muller non é a Cibreira do 43. A porta aprobouno. |
| 47 | rexenerar | — | Os tres intentos: fonte ornamental nun parque urbano, con farolas eléctricas e un edificio coas fiestras acesas (a porta acerta). |
| 48 | rexenerar | — | Tres homes do XIX discutindo diante de casas de tellado de herba de aspecto irlandés, cun animal que parece unha ovella; falta a muller acusada. A porta aprobouno. |
| 49 | rexenerar | — | Dous vellos de pé diante dun muro cun lume nun oco: ninguén espreita, e non hai fonte nin mulleres (a porta só avisou de que faltaba a fonte). |
| 50 | vale | `049-36108886-1.png` | Dous veciños agachados ao pé dun muro de noite, cun papel e candeas no chan: apuntan a lista. Mans correctas; chalecos de la, coherentes cos outros veciños. |
| 51 | rexenerar | — | Fonte de xardín con pía de pé e un cano metálico coma unha billa: non é unha fonte de aldea. Os ollos na escuridade non saíron e quítoos do prompt (risco de monstro); a escuridade das follas abonda. |
| 52 | rexenerar | — | Tres figuras con túnicas e capuchas vermellas arredor dun lume dentro dunha pía, cunha arcada e unha luz eléctrica ao fondo: parece un rito sectario, non tres veciñas rindo. A porta aprobouno. |
| 53 | vale | `052-d27a5209-0.png` | Dúas mozas camiñan cara á cámara cos caldeiros da auga ao serán: é o que se oe. Os caldeiros metálicos no canto de cántaros de barro son verosímiles; a casa do fondo é pequena e está desenfocada. |
| 54 | rexenerar | — | Os tres intentos son dúas mulleres nunha mesa dentro da casa, sen fonte nin noite, e a vella sorrí en vez de mirar con receo: perdeuse a idea das dúas maneiras de mirar a mesma fonte. |
| 55 | vale | `054-e88400da-0.png` | Nai e filla axeonlladas á lareira de granito (semente da lareira), co lume pequeno e as olas: ilustra o oficio que pasa de nai a filla. Non se ve o morteiro; aceptable. |
| 56 | vale (contra a porta) | `055-a569b84c-0.png` | Un vello coas ovellas xunto a un muro de pedra no outono: a porta rexeita por animais en grupo, pero as ovellas son o asunto. Non se ve a viña nin a liorta entre dous; aceptable. |
| 57 | vale | `056-71584a1c-0.png` | A curandeira do chal azul (a mesma do 18) e un labrego axeonllados xunto a un becerro deitado: a saúde e o gando, xusto o que se oe. Defecto menor: ao fondo, casas con tellado de herba. |
| 58 | rexenerar | — | Monxe vello e fraco lendo un libro nun xardín: non aparecen a herba nin a curandeira que defendía Sarmiento. Ademais, Sarmiento é robusto e de cara redonda, e este confúndese co Feijoo do 59. |
| 59 | vale (contra a porta) | `058-4344e708-2.png` | Dous monxes beneditinos escribindo á luz dunha vela (Feijoo co capucho): encaixa. A fiestra de vidro é verosímil nun mosteiro do XVIII e o libro non ten texto lexible; a porta rexeitouno por texto, de máis. |
| 60 | vale | `059-7bd4a5fa-0.png` | Un mozo murmura á orella dunha muller pensativa contra un muro con musgo: le como o rumor que corre. Os papeis están invertidos con respecto ao prompt; aceptable. |
| 61 | rexenerar | — | Muller tendida de costas, ríxida e cos brazos estirados sobre unha esteira: semella un corpo amortallado, e non hai a sombra do paxaro do soño. |
| 62 | vale (contra a porta) | `061-b0307b2c-1.png` | Feixes e rolos de papeis con cordón vermello e dúas velas: pecha os papeis. A folla aberta ten letra miúda ilexible; a porta rexeitouno por repetición co 26, un eco aceptable. |
| 63 | rexenerar | — | Fonte ornamental redonda con remate de estatua e luz de día gris: nin noite, nin lúa, nin fonte de aldea. Rexenérase coa mesma fonte rústica do 47 e do 51. |
| 64 | rexenerar | — | Non hai talla nin auga: unha planta nun recanto de muros que parecen de formigón. A porta aprobouno sen a clave. |
| 65 | rexenerar | — | Os tres intentos: unha fila de siluetas diante dun incendio enorme que ocupa o horizonte. Non son as brasas da cacharela (a porta acerta: lume vivo ao durmir). |
| 66 | vale | `065-00feb3af-0.png` | A moza da trenza e a blusa branca (a mesma do 16) nunha pía de pedra coa primeira luz e unha cunca verde: ilustra a flor da auga. Defecto menor: unha fonte ornamental á esquerda. |
| 67 | rexenerar | — | Os tres intentos levan fiestras de vidro modernas, contraventás con macetas ou portas de cristal (a porta acerta, aínda que diga casas británicas). |
| 68 | rexenerar | — | A cunca coas cuncas no bordo e os grans de café está ben (semente 07-01), pero os tres intentos teñen luz de día forte e o texto di «apáganse as luces». A porta rexeitou por lume vivo (é o barro laranxa). Proposta: a mesma semente en profundidade 0,6, que mantén a forma e deixa escurecer. Se volve fallar, o [0] (a xerra vertendo) vale. |
| 69 | rexenerar | — | Lume laranxa grande nunha cunca no chan e un só vello: o crítico pedira lapas azul pálido para o durmir, e faltan os comensais. |
| 70 | rexenerar | — | Dous veleiros grandes de tres mastros e unha cidade ao fondo: perdeuse o eco buscado co plano 4 (o barco vello e pequeno no peirao). Proposta: a mesma semente do 4. Se a porta rexeita por repetición co 4, escollelo a man, como dixo o crítico de planos. |
| 71 | outro intento (contra a porta) | `070-bad0884c-0.png` | O [1] ten dúas vellas sorrindo, sen o xesto. O [0]: a vella do pano escuro e o chaleco negro ergue o dedo ao dicir o dito, e a outra ri. Os cadros da parede son verosímiles no XX; a porta viu obxectos modernos e unha catedral que non hai. |
| 72 | rexenerar | — | Os tres intentos teñen lapas laranxas grandes; o escollido, ademais, unha pota negra de ferro (veto do caldeiro) e unha lareira acesa. O texto pide as últimas lapas azuis, que se apagan. |
| 73 | outro intento (contra a porta) | `072-94d8ba76-2.png` | O [1] ten dúas vellas lendo. O [2] ten a avoa e unha nena co libro: é o conto que pasa do libro á aldea. A lareira do fondo dá lume vivo (4,6 %), pero é ambiente; aceptable. |
| 74 | rexenerar | — | Vacas frisoas brancas e negras (raza leiteira moderna) e faroles de parede; os outros intentos teñen lámpadas eléctricas. Rexenérase con dúas vacas pardas. |
| 75 | vale | `074-c548270e-0.png` | Regato con musgo entre a brétema do bosque: é o que se oe, calmo para durmir. |
| 76 | outro intento (contra a porta) | `075-066ce0c5-0.png` | O [3], que pasou a porta, é a reserva xenérica: un bosque con brétema, que repite o 75 e non ten candea. O [0]: velas no peitoril de pedra dun muro groso. A porta rexeitouno por repetición co 9, pero é o eco buscado (a candea do principio e a do final). |
| 77 | rexenerar | — | Tellado de lousa con musgo, pero cunha bufarda de fiestras de vidro acesas e cheminea de aspecto inglés; é a última imaxe do vídeo. Encadre pechado nas lousas, sen casa. |

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
| 44 | casa de granito rústica, pote pequeno de unguento e muller cun neno; a curandeira co pano negro do elenco | plastered walls, amphora, olive trees, paper cup | non |
| 45 | de costas, a campesiña de pano gris (a Cibreira do 43); o xuíz e o escribán do elenco | chandelier, ball gown, earrings | non |
| 46 | dous perfís: o xuíz le a pregunta e a Cibreira asente calada | vignette, white frame, bonnet | non |
| 47 | fonte de aldea: cano de pedra nun muro de granito con musgo e pía, castiñeiros e o brillo lonxano da fogueira | statue, ornamental fountain, park, buildings | non |
| 48 | a porta da corte (sen casas á vista), a muller acusada e os animais mortos na palla | turf roof, thatched cottage, sheep | non |
| 49 | os dous veciños agachados tras o muro, mirando as mulleres na fonte | ornamental fountain, houses | non |
| 51 | cano de pedra e pía de noite, entre follas escuras; sen os ollos | metal tap, ornamental fountain | non |
| 52 | tres veciñas con mantón e pano rindo arredor da fonte, vistas de lonxe entre ramas | hooded robes, cloaks, ritual, arcade, columns | non |
| 54 | na fonte de noite: a moza enche o cántaro e a vella de pano negro persígnase mirando á escuridade | table, teapot | non |
| 58 | Sarmiento robusto e de cara redonda (elenco), coa curandeira do chal azul (a do 18 e do 57) e a herba | skullcap | non |
| 61 | durmindo de lado baixo unha manta, coa sombra do paxaro na parede | corpse, coffin | non |
| 63 | a lúa na auga da pía da mesma fonte rústica, de noite | statue, ornamental fountain, daylight | non |
| 64 | a talla de barro ao principio do prompt, enriba do muro, de noite | concrete | non |
| 65 | un anel baixo de brasas case apagadas e siluetas pequenas | wildfire, big flames | non |
| 67 | só a trabe afumada e o muro de granito, sen porta nin fiestra | flowerpots, shutters | non |
| 68 | o mesmo prompt, de noite | daylight | **07-01** («Camino de Santiago, May 2008», CC BY 2.0), profundidade 0,6 (antes img2img 0,5) |
| 69 | lapas azul pálido no cazo e na cunca, o vello e a vella xuntos | orange fire, cauldron | non |
| 70 | barco vello e pequeno no peirao, brillo azul e tres figuras | tall ship | **11-01** (dorna de Rianxo, CC BY 2.0), img2img 0,5: a mesma do 4 |
| 72 | cunca de barro parda coas últimas lapas azuis e o brillo vermello das brasas | cauldron, iron pot, fireplace, orange flames | non |
| 74 | dúas vacas pardas, corte de pedra escura e unha lanterna pequena | black and white cows, wall lamp | non |
| 77 | encadre pechado nas lousas molladas, sen casa | window, dormer, chimney | non |

Créditos das sementes propostas (CC BY pide crédito): «Hórreos de Muimenta, Carballeda de Avia» de José Antonio Gil
Martínez (CC BY 2.0), «Palloza Cantexeira» de FCPB (CC BY 3.0), «Camino de Santiago, May 2008» de Alex Chang (CC BY
2.0) e «Dorna a vela. Rianxo de noite» de Xoan Anton (CC BY 2.0), vía Wikimedia Commons (URL en
`imaxe/referencias.json`). Para a palloza mirei a foto cunha grade antes de escoller o recorte; a foto non vai ao
repo (material de terceiros).

## Que fai a porta v6 (planos 1-77)

| | Planos 1-42 | Planos 43-77 | Total |
|---|---|---|---|
| Escollidas que aprobou | 29 | 24 | 53 |
| … destas, a rexenerar | 12 | 14 | 26 |
| … destas, cun intento mellor | 4 | 2 | 6 |
| Planos onde rexeitou todos os intentos | 13 | 11 | 24 |
| … destes, cun intento que vale | 8 | 4 | 12 |

- **Deixa pasar de máis, e é o que máis pesa:** 32 das 53 escollidas que aprobou tiñan un problema. Non ve
  lampadarios nin salóns de palacio, fiestras de vidro en casas de aldea, baixantes, bancos de parque, faroles de
  parede, vasoiras, fontes de xardín, roupa do XIX, tellados de herba, paredes encaladas, ritos de capucha, bufardas
  nin vacas frisoas, nin a queimada convertida en caldeiro ou fogueira. Tampouco bloquea cando falta a clave («falta:
  ...» só avisa), e aproba as reservas xenéricas (35 [3] e 76 [3]), que non teñen nada do que se oe.
- **Rexeita de máis:** en 12 dos 24 planos que rexeitou había un intento que vale.
  - Por *texto na imaxe* nos planos de escritura (12, 15, 19, 26, 32, 37 e 59). O problema era a letra lexible ou de
    imprenta, non o texto.
  - Por *animais en grupo* cando o texto pide o gando ou as ovellas (23, 56).
  - Por *repetición* nos ecos buscados (62 co 26; tamén o intento [0] do 76 co 9).
  - Por un *iate moderno* que non hai (33) e por *mans* que non vin (25 [1], 30 [0]).
  - Por *lume vivo ao durmir* cando era unha lareira ao fondo (73) ou o barro laranxa da cunca (68, que si hai que
    rexenerar, pero pola luz de día).
- **Acerta ao rexeitar** en 12 planos, ás veces polo motivo equivocado: zapatos modernos (7, dixo «interior
  moderno»), bombilla e fiestras (18, 67), casas inglesas (21), lentes (41), pseudotexto (31), farolas (47), sen fonte
  (54), incendio (65), luz de día (68, dixo «lume vivo»), caldeiro (72) e lámpadas (74).
- **Ideas para a peza IMAXE** (non as probei):
  - Que «texto na imaxe» só avise cando a clave é de escritura (papers, page, quill, document, sheet), e «animais en
    grupo» cando a clave é o gando.
  - Sondas CLIP para «crystal chandelier», «palace hall», «park bench», «drainpipe», «broom», «bonfire», «ornamental
    fountain», «turf roof» e «Holstein cow».
  - Que «lume vivo ao durmir» mida só as lapas e non o barro.
  - Non aceptar sen revisión un intento con `reserva: true`.

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
- **53:** levan caldeiros metálicos, non cántaros. Proposta: «the women walk slowly toward the camera carrying their
  water pails».
- **55:** non hai morteiro. Proposta: «the mother slowly crushes herbs between her hands while the girl watches the
  small fire».
- **56 ([0]):** hai un só home. Proposta: «the sheep graze slowly while the old man watches them».
- **57:** o becerro está deitado. Proposta: «the healer slowly moves her hands over the calf and the calf lifts its
  head».
- **60:** é un mozo quen murmura. Proposta: «the young man whispers into her ear and she slowly raises her eyes».
- **66:** ten unha cunca na man. Proposta: «she slowly lowers the bowl and brings the herb water to her face».
- **71 ([0]):** son dúas vellas. Proposta: «she wags her raised finger as she speaks and the other old woman laughs
  softly».
- **73 ([2]):** a nena está esperta lendo. Proposta: «the grandmother turns a page and speaks softly while the child
  leans against her».
- **76 ([0]):** hai dúas velas. Proposta: «the two candle flames tremble and slowly go out, leaving thin threads of
  smoke».

## Personaxes recorrentes

- **Dorotea:** no 13 leva pano claro (non marrón escuro) e no 30 [0] vai sen pano e co pelo branco. Os planos 6, 7 e
  29 rexenéranse co pano marrón escuro do elenco.
- **María:** a cor vermella mantense (23, 30 [0]); no 20 e no 21 saía de Carapuchiña e rexenéranse.
- **Escribán:** no 5 é un home con barba e chapeu; no 12 e no 28, un mozo barbeado (é a figura «quen escribía»;
  aceptable). O 12 e o 28 parécense (escribán novo con candeas), pero son o mesmo papel e están a ≈ 2 min.
- **Mariano e os amigos** (3 [1], 33, 34): camisa branca e sen o xersei escuro, coherentes entre si. O barco do 70
  rexenérase coa semente do 4, para o eco buscado.
- **María Cibreira:** no 43 leva o pano gris do elenco; no 45 e no 46 saía unha dama do XIX, e rexenéranse co pano
  gris. A súa nai (44) rexenérase co pano negro e o pelo branco do elenco.
- **A curandeira do chal azul:** o 57 é coherente co 18, que se rexenera co mesmo chal; o 58 rexenérase con ela.
- **A moza da trenza:** o 16 e o 66 son coherentes (blusa branca e trenza longa); o 54 rexenérase con ela.
- **Os veciños de Campo Lameiro:** no 50 levan chalecos de la parda; o 48 e o 49 rexenéranse cos de pel de ovella do
  elenco (diferenza pequena).
- **Feijoo e Sarmiento:** o 59 [2] ten dous monxes vellos (Feijoo, co capucho); o 58 rexenérase cun Sarmiento robusto
  e de cara redonda, para non confundilos.
- **Os vellos da queimada:** o 71 [0] ten dúas vellas e non o vello; o 69 rexenérase coa parella.

## Pendente

- Mirar os 38 rexenerados cando saian (17 da primeira pasada e 21 da segunda). Nos de escritura (31) a porta volverá
  rexeitar por texto. Nos de semente (10, 21, 68 e 70), ver se a foto arrastra algo do presente. Se a porta rexeita o
  70 por repetición co 4, escollelo a man. Se o 68 volve saír de día, vale o [0].
- Levar á lista de produción as accións I2V da segunda pasada (sección de MOVEMENTO).
