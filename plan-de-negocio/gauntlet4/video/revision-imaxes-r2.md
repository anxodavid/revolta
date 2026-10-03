# Revisión das imaxes rexeneradas da v2 · rolda 2 · 38 planos (Gauntlet 4)

**Quen:** un axente Claude (revisor de imaxes), o 03-10-2026 entre as 22:17 e as 22:45 UTC. **Ningunha persoa revisou
estas imaxes.**

**Material:** `$SCRATCH/v2/intentos-r2.json` (xerado ás 22:16 UTC con `produccion.py intentos`: 38 planos e 72
intentos), as imaxes de `$SCRATCH/v2/w/imaxes/` e `revision.json`, que só lin para saber que aprobou a porta. Non
modifiquei `revision.json` nin xerei imaxes.

**Saídas:** este documento; [`revision-imaxes-r2.json`](revision-imaxes-r2.json) (`escollas`, `motivos`, `rexenerar`
e `accions`, para `video/scripts/produccion.py revision`); e as follas que mirei, en
[`follas-revision/`](follas-revision/) (`r2-*.jpg`).

## Contas

| Decisión | Planos | Cantos |
|---|---|---|
| **Vale** | 7, 9, 17, 20, 22, 40, 44\*, 46, 49, 51, 61, 67, 68, 72\*, 74, 77 | **16** (2 contra a porta\*) |
| **Outro intento** | 31 → [2]\*, 39 → [1]\*, 41 → [2]\*, 42 → [2]\*, 45 → [0], 63 → [0], 64 → [2]\*, 70 → [1] | **8** (5 en planos que a porta rexeitou enteiros\*) |
| **Rexenerar outra vez** | 2, 6, 10, 18, 21, 29, 38, 47, 48, 52, 54, 58, 65, 69 | **14** (o 10 cambia de técnica de semente e o 21 quédase sen semente) |

Dos 38 planos que mandou rexenerar a r1, **24 xa teñen unha imaxe que vale** e 14 hai que rexeneralos outra vez. Por
fases (valen / outro intento / rexenerar): gancho 3 / 0 / 4 (2, 6, 10 e 18), transición 2 / 1 / 3, calma 6 / 4 / 5
e durmir 5 / 3 / 2. O gancho é o que peor queda, e é o que máis se ve.

Os problemas máis repetidos:

1. **Un só intento:** a porta aprobou o primeiro intento en 18 planos e a pipeline parou aí. En 8 deles (6, 10, 38,
   48, 52, 54, 58, 69) ese único intento non vale, e non había onde escoller.
2. **O lume da queimada segue laranxa** cando hai persoas: «pale blue flames» deu lume laranxa no 2 (nunha cunca negra
   que se le como caldeiro, e no [1] cun coitelo), no 39 e no 69 (aquí coma un fogón, cunha fiestra de día). No 38
   saíron fachos azuis enriba dunha fogueira. O azul segue saíndo só cando a cunca é o tema (o 32 da r1).
3. **Rito ou multitude arredor do lume** (veto de `gauntlet3/contexto.md` §8.5): a fogueira cunha multitude cos brazos
   en alto no 38, as mulleres con mantos e veos coma de monxa arredor do lume, cun can coma lobo, no 52, e unha aldea
   que parece arder no 65.
4. **Arquitectura e luces doutro tempo:** fiestras de vidro (grande no 18, emplomada no 6, pequena e tolerable no 17),
   casas inglesas coas fiestras acesas (47 e 65), tellado de herba irlandés (48), lámpadas colgadas das árbores (47) e
   un candil con forma de bombilla (54).
5. **Falta a idea do plano:** sen home nin preñez visible (6), sen hórreo (10: pés perdidos e tornarratos soltos), sen
   becerra morta nin liorta (48), sen fonte nin contraste entre as dúas mulleres (54), e o frade e a curandeira
   fundidos nunha persoa de capucho azul (58).
6. **Pequenos:** letra lexible ou de imprenta nos tres intentos do 31 (o [2] é o menos malo) e lentes metálicas de
   patillas no frade do 41 ([0] e [1]).

## Como o fixen

- **Follas** (`follas-revision/r2-planos-NN-MM.jpg`, 6 planos por folla, 130-385 KB), feitas con
  [`scripts/follas_revision_r2.py`](scripts/follas_revision_r2.py) (novo, a partir de `follas_revision.py`): o intento
  que escolleu a porta a 640 px, os outros a 320 px ao lado e, debaixo, o tipo, a prioridade e o modo de animación, o
  texto que se oe, o prompt novo, a acción I2V e o que dixo a porta de cada intento. Mireinas en recortes de 2 planos sen reducir e,
  despois de decidir, engadín a etiqueta «Revisión r2: ...».
- **Detalles** (`follas-revision/r2-detalles-*.jpg`, con `scripts/zoom_revision.py`): a cunca e o coitelo do 2, a
  fiestra e a deitada do 6, os zapatos do 7, a vela do 9, as fiestras do 17 e do 18, as figuras do 20, 22 e 29, a
  letra do 31, o barco do 39, as lentes do 41, os intentos do 42, 45 e 49, as mans do 44 e do 58, as luces do 40, 47,
  54, 63 e 74, a talla do 64, o barco do 70 e a lapa do 72.
- **Elenco** (`follas-revision/r2-elenco-planos-que-valian.jpg`): os planos que xa valían na r1 cos personaxes
  recorrentes (13, 30, 23, 5, 12, 28, 43, 57, 59, 16, 66, 50, 71, 33, 34, 3, 4 e 36), para comparar.
- **Comparación** (`follas-revision/r2-comparacion-68-10-63.jpg`): o 68 vello e o novo, o 10 do plano base, a semente
  de Muimenta co recorte que se usa e os dous intentos do 63. Crédito da semente: «Hórreos de Muimenta, Carballeda de
  Avia, Galiza.jpg», de José Antonio Gil Martínez, CC BY 2.0 (https://creativecommons.org/licenses/by/2.0), vía
  Wikimedia Commons.
- **Prompts novos:** sen o prefixo de estilo, entre 39 e 52 tokens contados co tokenizador de SDXL (como na r1, para
  deixar sitio ás frases que a pipeline engade nos reintentos). O `negativo` vai completo e só o usa a porta (CLIP):
  na r2 a porta non marcou negativos que xa describían o fallo (48 «turf roof, sheep», 52 «hooded robes, ritual», 69
  «orange fire, fireplace»), así que o negativo non protexe; o que cambia o resultado é o prompt.
- **Proba do JSON:** apliqueino con `produccion.py revision` sobre copias de `revision.json`, dos axustes e da lista
  no scratchpad: 24 escollas, 14 rexeneracións e 17 accións, sen erros (o 10 queda en profundidade e o 21 sen
  semente). Os ficheiros reais non os toquei.

## Plano a plano

V = vale; O = outro intento; R = rexenerar. «[n]» é o número do intento (o do ficheiro). «Porta» é o que escolleu ela.

| Plano | Fase | Decisión | Por que |
|---|---|---|---|
| 2 | gancho | **R** | Os tres, lume laranxa grande nunha cunca negra ou tixola (caldeiro); o [1] cun coitelo no canto do cazo. |
| 6 | gancho | **R** | Un intento: dúas mulleres novas sen pano (ningunha é Dorotea), sen home nin barriga, fiestra emplomada. |
| 7 | gancho | **V** [1] | Mans calzando a zapatilla parda; detrás, o zapato negro do home. O [0] é un vello sen zapato. |
| 9 | gancho | **V** [0] | Vela de cera e dúas candeas finas en ferro: a grande segue sendo de bloque, pero xa non parece de catálogo. |
| 10 | gancho | **R** | O hórreo de granito queda no chan coma unha caseta e os tornarratos andan soltos; de día. |
| 17 | gancho | **V** [1] | Dúas vellas no poio da porta. Fiestra pequena na esquina e parede revocada (menor). Nova acción. |
| 18 | gancho | **R** | Fiestra grande de vidro e ladrillo; falta a moza enferma (o [0] tamén ten fiestra). |
| 20 | transición | **V** [1] | María de pano e vestido vermellos ante o xuíz que a sinala coa pluma; sala grande sen lampadario. |
| 21 | transición | **R** | Casas encaladas con balcóns e a xente desaparece; no [2], unha figuriña co farol contra a parede. |
| 22 | transición | **V** [0] | Unha veciña con capucha e un vello ante a porta dunha igrexa de pedra; separados: nova acción. |
| 29 | transición | **R** | [1] cun cardeal de vermello e sen as mulleres; [0] con figuras de aire colonial, carros e farol de parede. |
| 31 | transición | **O** [2] | Letra cursiva case ilexible; o [0] ten gótica de imprenta e o [1] pseudopalabras inglesas na lente. |
| 38 | transición | **R** | Un intento: fogueira grande, multitude cos brazos en alto e fachos azuis (rito ou queima). |
| 39 | calma | **O** [1] | Cinco homes arredor dunha cunca de lume na cuberta, co porto detrás; o [0] e o [2] son fogueiras. |
| 40 | calma | **V** [0] | Tribunal de clérigos de negro, sala de madeira con candelabros de velas (non de cristal). Paralaxe. |
| 41 | calma | **O** [2] | Frade de hábito negro entre feixes de papeis, sen lentes; o [0] e o [1] levan lentes de patillas. Nova acción. |
| 42 | calma | **O** [2] | Mulleres de negro ante homes de barba e hábito negro; o [0] é un tribunal moderno con mulleres rubias. Nova acción. |
| 44 | calma | **V** [0]\* | A curandeira dálle a ola a unha muller cun cesto; a «man sen corpo» da porta é falsa. Sen neno: nova acción. |
| 45 | calma | **O** [0] | O xuíz pregunta á muller do pano gris e ao fondo alguén escribe; o [1] (porta) non ten escribán. Nova acción. |
| 46 | calma | **V** [0] | Xuíz e Cibreira de perfil á luz das velas, coherente co elenco. Sen papel: nova acción. |
| 47 | calma | **R** | [0] con lámpadas colgadas das árbores e velas no chan; [1] e [2] con casas inglesas acesas. |
| 48 | calma | **R** | Un intento: dous homes tranquilos con ovellas e tellado de herba; sen becerra, sen leitóns, sen liorta. |
| 49 | calma | **V** [2] | Tres veciños de chaleco pardo contra un muro, de noite, co lume ao lado; o [1] ten unha casa ardendo. Nova acción. |
| 51 | calma | **V** [0] | Auga fría entre pedras e fentos: fonte natural, sen estatuas nin billas. |
| 52 | calma | **R** | Un intento: mulleres con mantos e veos coma de monxa arredor do lume e un can coma lobo (rito). |
| 54 | calma | **R** | Un intento: dúas mulleres rindo nun interior, candil con forma de bombilla, sen fonte nin contraste. |
| 58 | calma | **R** | Un intento: un vello fraco de capucho azul cun cesto; frade e curandeira nunha persoa, parecido ao Feijoo. |
| 61 | calma | **V** [0] | Unha moza durmindo baixo unha manta de la («só soñado»); sen sombra de paxaro: nova acción. |
| 63 | durmir | **O** [0] | Pía de pedra baixo a lúa chea, sen ninguén; o [2] (porta) ten dúas lúas e o [1] repite o 51. |
| 64 | durmir | **O** [2] | A talla con auga e herbas ao pé dun muro, cun farol de vela; o [1] (porta) ten un boneco e un testo, o [0] unha billa. |
| 65 | durmir | **R** | [2] casas inglesas e lumes arredor (aldea ardendo); [0] fogueira con multitude; [1] casas acesas. |
| 67 | durmir | **V** [0] | Ramos de herbas secas colgados dunha vara; fondo gris de estudo, sen anacronismos. |
| 68 | durmir | **V** [0] | A cunca coas cuncas no bordo e unha man botando café; luz clara (defecto), sen o laranxa forte. Nova acción. |
| 69 | durmir | **R** | Un intento: lume laranxa coma de fogón ao lado da cunca, fiestra de día e sen a vella. |
| 70 | durmir | **O** [1] | O barco vello no peirao, eco buscado do plano 4; o [3] (porta) é un bosque sen barco. |
| 72 | durmir | **V** [0]\* | A cunca cun fío de fume e unha lapa pequena: o lume que se apaga. A porta rexeitou por «lume vivo». |
| 74 | durmir | **V** [0] | Tres vacas pardas deitadas na palla; espertas, e un brillo branco arriba que pode ser un farol (menor). |
| 77 | durmir | **V** [0] | Lousas escuras molladas, con musgo, de noite. |

## Planos a rexenerar: que cambia no prompt

Os prompts completos, os negativos e os motivos están no JSON. Se non houbese tempo de rexenerar, indico **o menos
malo** de cada un (ningún vale de verdade).

- **2** (gancho, I2V 1): só a man, o cazo e a cunca, sen cara: «close-up in the dark of a hand lifting a clay ladle
  of pale blue flames above a wide brown clay bowl of blue flames...». Cando hai cara, SDXL ilumina con lume laranxa;
  o azul saíu no 32, onde a cunca é o tema. O texto di «alguén», así que a cara non fai falta. Menos malo: [0].
- **6** (gancho): un só xesto claro, a man da vella parteira de pano marrón escuro na barriga da preñada; sen o home,
  que xa sae no 7. Menos malo: [0].
- **10** (gancho): o mesmo prompt e a mesma semente de Muimenta co mesmo recorte, pero en **profundidade 0,6** en
  vez de img2img 0,5: no plano base, a profundidade conservou os pés do hórreo, e o tellado de herba daquela viña do
  «moss» do prompt vello, que o actual xa non leva [S: sen probar con este prompt]. Menos malo: [0].
- **18** (gancho, I2V 1): primeiro plano da curandeira levando a cunca aos beizos da moza, co fondo escuro: sen
  arquitectura non hai fiestras. Menos malo: [1].
- **21**: plano medio na porta, de noite, coa muller do pano vermello e o farol de corno e o home da capa, e **sen
  semente** (`"referencia": null`): coa palloza en profundidade mandaba a casa e perdíase a xente. Menos malo: [1].
- **29**: só o vicario lendo o decreto na porta dunha capela de granito; nai e filla xa saen soas no 30 (a xerra
  baleira). O «red» do pano de María pasaba ao home (un cardeal). Menos malo: [0].
- **38**: unha verbena dos anos oitenta con mesas longas e unha cunca de lume azul en cada mesa, sen fogueira: a
  queimada xa «de todos». Menos malo: [0].
- **47**: o souto de castiñeiros de noite, con lúa chea e brétema, un muro baixo e unha pía, sen fogueira nin casas
  (a «orange glow of a distant bonfire» deu as lámpadas nas árbores). Menos malo: [0].
- **48** (I2V 1): dentro da corte, a becerra morta na palla e os dous veciños de pel de ovella acusando; a muller
  queda fóra de cadro. Fóra, a corte trae o tellado de herba. Menos malo: [0].
- **52** (I2V 1): as tres mulleres sentadas no muro da fonte, rindo, á luz da lúa e vistas de lonxe entre as ramas,
  sen lume: o lume é o que as converte en rito. Menos malo: [0].
- **54** (I2V 1): a vella de pano negro en primeiro termo persignándose e mirando a escuridade, e detrás a moza da
  trenza enchendo a xerra na fonte. Menos malo: [0].
- **58** (I2V 1): só Sarmiento, groso e de cara redonda, de hábito negro, estudando unha póla de herba cun cesto no
  brazo; a curandeira fóra (o seu azul pasaba ao frade). Menos malo: [0].
- **65**: o prado aberto e sen casas, coas brasas pequenas lonxe e tres siluetas, unha saltando: «villagers» trae a
  aldea. Menos malo: [1] (calmo, aínda que sen lume e con casas acesas).
- **69** (durmir, I2V 1): as siluetas escuras do vello e da vella e a cunca de lume azul como única luz. «faces lit
  blue» non chega [S: o azul con persoas está sen resolver; se volve saír laranxa, ver o punto de Pendente]. Menos
  malo: [0].

## Accións I2V (`accions` do JSON)

Cambio a acción onde non casa coa imaxe escollida e, nos planos a rexenerar, onde o prompt novo xa non ten o que
dicía a vella (2, 6, 18, 29, 48, 52 e 58). Todas son simples e lentas; as demais quedan como estaban (20 e 21, 38,
54 e 69 casan co prompt ou coa imaxe).

| Plano | Acción nova |
|---|---|
| 2 | the hand slowly raises the ladle and pours a thin stream of blue fire back into the bowl |
| 6 | the old midwife slowly moves her hand over the young woman's belly |
| 17 | the two old women sit quietly and one slowly turns her head toward the other |
| 18 | the healer slowly brings the steaming bowl to the young woman's lips |
| 22 | the hooded woman slowly turns her head and whispers to the old man |
| 29 | the priest slowly reads aloud from the decree and lowers the paper |
| 41 | he slowly closes the small book in his hands and bows his head |
| 42 | the women stand still and slowly lower their heads while the bearded judge speaks |
| 44 | the old healer slowly hands the clay pot to the woman with the basket |
| 45 | the judge leans over the table and speaks slowly while the woman lowers her eyes |
| 46 | the judge leans closer and speaks softly, and the woman slowly nods in silence |
| 48 | one man points at the dead calf while the other shouts toward the door |
| 49 | the three men sit still in the dark and slowly turn their heads toward the firelight |
| 52 | the women talk and laugh softly and one gestures with her hand |
| 58 | the friar slowly turns the sprig in his fingers and smiles |
| 61 | she sleeps peacefully, breathing slowly under the blanket |
| 68 | the hand slowly lets a few coffee beans fall into the bowl |

## Personaxes recorrentes

- **Dorotea:** o 6 rexenérase co pano marrón escuro do elenco; no 7 [1] só se ven as mans; o 29 pasa a ser só o
  vicario. Segue a diferenza da r1 (pano claro no 13, sen pano no 30 [0]).
- **María:** no 20 [1] leva pano e vestido vermellos, máis vermella ca no 23, pero sen capa nin capucha; o 21
  rexenérase co pano vermello desvaído.
- **Xuíces:** barba branca longa no 20, barba gris no 45, barba branca e gorro no 46 e homes de barba e hábito negro no
  42. Vilalba (1617) e Boborás (1639) son procesos distintos, así que non teñen que ser o mesmo xuíz.
- **María Cibreira:** pano gris no 43, no 45 [0] e no 46 [0] (no 46 parece máis nova). A súa nai (44 [0]) leva pano
  branco e non negro, pero só sae aí.
- **Inquisidor:** o 41 [2] vai de hábito negro (o elenco dicía hábito branco e capa negra) e no 40 todos van de negro.
- **A curandeira do chal azul:** o 18 rexenérase co chal azul; o 58 rexenérase sen ela, porque o seu azul pasaba ao
  frade.
- **Mariano e os amigos:** no 39 [1] son cinco homes de camisa clara, coherentes co 33 (camisas brancas), aínda que o
  texto pensa en tres.
- **Os veciños de Campo Lameiro:** no 49 [2] levan chalecos pardos, coma no 50; o 48 rexenérase cos de pel de ovella
  do elenco.
- **A moza da trenza:** o 54 rexenérase coa trenza longa. **Sarmiento:** o 58 rexenérase groso e de cara redonda, para
  non confundilo co Feijoo do 59.
- **Os vellos da queimada:** o 69 rexenérase coa parella en silueta; o 71 [0] (dúas vellas) segue valendo.

## Que fai a porta (38 planos rexenerados)

- **Aprobou 28 planos:** 14 escollas valen tal cal, en 3 había un intento mellor (45, 63 e 70) e 11 hai que
  rexeneralas. Deixou pasar fiestras de vidro (6, 18), o tellado de herba (48), o candil con forma de bombilla (54),
  o rito arredor do lume (38, 52), a aldea ardendo (65), o cardeal (29), o lume laranxa coma de fogón (69) e un hórreo
  sen pés (10).
- **Rexeitou os outros 10** (2, 21, 31, 39, 41, 42, 44, 47, 64 e 72), e en 7 había un intento que vale: o seu no 44 e
  no 72, outro no 31, 39, 41, 42 e 64. Falsos positivos: «man sen corpo» (44), «lume vivo ao durmir» nunha lapa
  pequena (72), «interior moderno» nunha pía baixo a lúa (63 [0]) e «bonfire» nunha cunca de lume (39 [1]).
- **No 70** marcou ben a repetición co plano 4, pero o eco é buscado, e escolleu un bosque sen barco.
- **Para no primeiro intento sen problemas:** 18 planos tiveron un só intento, e 8 deles hai que rexeneralos.

## Pendente

- Mirar os 14 rexenerados (rolda 3). No 10, ver se a profundidade mantén os pés do hórreo e se volven o tellado de
  herba ou un farol. No 2 e no 69, se o lume volve saír laranxa: o 2 pode quedar co [0] e o 69 co [0], ou buscar o
  azul noutro paso (p. ex. corrección de cor só na cunca) [S: sen probar].
- Proposta para o orquestrador (decide el): nos planos do gancho e nos de I2V de prioridade 1, pedir sempre 2 ou 3
  intentos aínda que a porta aprobe o primeiro. A pipeline para no primeiro sen problemas, e esta rolda 8 dos 14
  rexenerar viñeron de planos cun só intento.
