# Revisión das imaxes rexeneradas da v2 · rolda 3 (última) · 14 planos (Gauntlet 4)

**Quen:** un axente Claude (revisor de imaxes), o 04-10-2026 despois das 00:25 UTC. **Ningunha persoa revisou estas
imaxes.**

**Material:** `$SCRATCH/v2/intentos-r3.json` (00:25 UTC): os 14 planos que a r2 mandou rexenerar, cos prompts da r2
e tres intentos cada un (`IMG_MIN_INTENTOS=3`). `revision.json` só o lin; non o modifiquei nin xerei imaxes.

**Saídas:** este documento; [`revision-imaxes-r3.json`](revision-imaxes-r3.json) (mesmo formato ca na r2; probado con
`produccion.py revision` sobre copias no scratchpad: 14 escollas, 1 rexeneración e 10 accións, sen erros); follas
`follas-revision/r3-planos-*.jpg` (con `scripts/follas_revision_r2.py`, agora con `RONDA=r3`) e detalles
`follas-revision/r3-detalles-*.jpg`.

## Contas

| Decisión | Planos | Cantos |
|---|---|---|
| **Vale** | 2 [1]\*, 10 [0], 21 [2], 54 [0], 58 [1], 65 [0]\* | **6** (2 contra a porta\*) |
| **Outro intento** | 18 → [1], 29 → [2], 38 → [2]\*, 47 → [1], 48 → [2]\*, 52 → [2], 69 → [2] | **7** (2 en planos que a porta rexeitou enteiros\*) |
| **Rexenerar (gancho)** | 6, coa reserva [0] xa escollida | **1** |

Todos os planos teñen agora unha imaxe digna. Os tres intentos axudaron moito: en 7 dos 14, o mellor non era o
que escolleu a porta. Algúns quedan sen parte da clave: o 6 sen a barriga (por iso o rexenero), o 38 con lume laranxa
e non azul, o 54 sen a moza nin a fonte, o 65 sen as brasas e o 69 sen a cunca nin o cazo. Ningún intento dunha
rolda anterior era mellor ca os escollidos.

## Plano a plano

| Plano | Decisión | Por que |
|---|---|---|
| 2 | **V** [1]\* | A man verte lume **azul** dun cazo de ferro nunha cunca de barro: a clave, por fin. Fondo bege, non negro (menor). [0] e [2]: lume laranxa. |
| 6 | **R** (reserva [0]) | A parteira de pano marrón á beira da cama, á luz das velas, pero sen barriga: lese «coida a alguén», non «parto». |
| 10 | **V** [0] | Dous hórreos sobre pés con tornarratos e tella, ao solpor (a profundidade gardou a forma). Táboas grises case como chapa (menor). |
| 18 | **O** [1] | A curandeira de pano azul prepara herbas á luz dunha vela, sen fiestras; coherente co 57. O [2] (porta) ten un curandeiro con cara de home. |
| 21 | **V** [2] | A muller da capa vermella e o home á porta, de noite. A capucha lembra a Carapuchiña, pero os tres a levan e casa coa María de vermello. |
| 29 | **O** [2] | O vicario de costas, papel na man, ante a porta pechada da igrexa: «tamén podían pechar portas». |
| 38 | **O** [2]\* | Verbena con mesas longas e lapas pequenas nas cuncas: festa, non rito. Lapas laranxas. A porta rexeitou os tres por «multitude». |
| 47 | **O** [1] | Carballo de noite con lúa e brétema, sen anacronismos. O [0] (porta) ten unha pía cun lumiño que parece fogueira de rito. |
| 48 | **O** [2]\* | Tres veciños de chaleco arredor dunha becerra morta, ante a corte: a acusación enténdese. O [0] (porta) son ovellas vivas. |
| 52 | **O** [2] | Mulleres sentadas nun muro de noite, vistas de lonxe, sen lume; un farol de parede ao bordo. O [0] (porta) ten dous faroles grandes coma lámpadas. |
| 54 | **V** [0] | Dúas vellas de pano negro cunha xerra, cada unha mirando cara a un lado; sen a moza da trenza nin a fonte (ningún intento a ten). |
| 58 | **V** [1] | Sarmiento groso e de cara redonda cun cesto de herbas no horto, distinto do Feijoo do 59. Solidéu negro (menor). |
| 65 | **V** [0]\* | Prado ao solpor cunha poza e dúas figuriñas: moi calmo para o durmir, sen as brasas. A porta rexeitou por «lume vivo» (o ceo). |
| 69 | **O** [2] | A parella de vellos á mesa á luz das velas, cunha lapa azul pequena: calmo, sen cunca nin cazo. O [0] (porta) parece un mago facendo un feitizo. |

## O plano a rexenerar (6, gancho)

- **Prompt:** «close-up of an old midwife's wrinkled hands in dark brown wool sleeves resting on the big round belly of a
  heavily pregnant woman lying on a straw bed, coarse linen shift, candlelight, dark room, 17th century» (47 tokens).
- **Por que:** en tres roldas (7 intentos) ningunha imaxe ten a barriga, e o texto fala das dores do parto, que o
  plano 7 pasa ao home. As mans sobre a barriga da preñada son un motivo de foto moi común e deberían saír [S: sen
  probar]; as mangas marróns lembran a Dorotea.
- **Reserva:** se os tres novos non valen, queda o [0] da r3 (`005-35675b9d-0.png`), que xa vai en `escollas`, coa
  acción «the midwife gently strokes the brow of the woman lying in the bed while the candle flames flicker». A
  acción do JSON (`the old hands slowly move over the round belly...`) é para o prompt novo.
- Non rexenero o 2, o 10 nin o 18: os tres teñen xa unha imaxe que vale.

## Accións I2V (`accions`)

| Plano | Acción nova |
|---|---|
| 6 | the old hands slowly move over the round belly while the candlelight flickers (prompt novo) |
| 18 | the healer slowly stirs the herbs in the small bowl while the candle flame flickers |
| 21 | she raises the small lantern and the cloaked man slowly steps toward the door |
| 29 | the priest slowly lowers the paper in front of the closed church door |
| 38 | people talk softly at the long tables and the small flames flicker |
| 48 | the men kneel over the dead calf and one slowly shakes his head |
| 52 | the two seated women talk softly and one slowly turns toward the other |
| 54 | the old woman holding the jug slowly turns her head toward the dark woods |
| 58 | the friar smiles and slowly lifts the basket of herbs to look at them |
| 69 | the old couple sit quietly at the table while the small blue flame flickers |

A do 2 casa coa imaxe e queda igual; o 10, o 47 e o 65 son paralaxe.

## Elenco

Dorotea leva o pano marrón no 6 [0], e a curandeira o azul no 18 [1], coma no 57. María vai de vermello no 21, coma
no 20 e no 23. Sarmiento (58) xa non se confunde co Feijoo do 59. Os veciños do 48 levan chaleco escuro, non de pel
de ovella; os do 49 e do 50, pardo (diferenza pequena). No 54 non sae a moza da trenza; segue no 16 e no 66.

## Que fixo a porta

Aprobou 10 dos 14 planos: a súa escolla vale no 10, 21, 54 e 58 (e no 6 como reserva), e nos outros 5 (18, 29, 47,
52 e 69) escollín outro intento. Rexeitou os outros 4 (2, 38, 48 e 65), e nos catro había un intento que vale: o seu no 2 e no 65, outro no 38 e no
48. Erros: «iron pot» polo cazo do lume azul (2), «lume vivo» por un ceo vermello (65) e «multitude» nunha verbena
(38). Deixou pasar un mago con lapas azuis soltas (69 [0]), faroles coma lámpadas (52 [0]), a pía co lumiño (47 [0])
e ovellas vivas no canto da becerra morta (48 [0]).
