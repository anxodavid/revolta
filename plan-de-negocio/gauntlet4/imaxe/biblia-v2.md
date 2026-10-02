# Biblia visual v2 de "Cousas de Galiza para durmir" (Gauntlet 4, peza IMAXE, rolda 1)

Autor: o director de arte (axente Claude), 02-10-2026. **Substitúe as seccións 3, 5, 6 e 8 da biblia v1**
([`gauntlet3/visual/biblia.md`](../../gauntlet3/visual/biblia.md)); o resto da v1 (estilo común, guion de luz por fase,
iconografía e listas) segue vixente salvo o que se di aquí. Os prompts van en inglés. Nada disto o revisou unha
persoa: sae do tribunal da v1, da queixa das persoas que viron a v1 ("as imaxes non teñen moita correlación co que se
di e non atraen a mirada") e das probas desta rolda (`informe-r1.md`).

**Para quen:** o montador e director que escribe a lista de planos v2 (peza 4) e quen toque `imaxes.py`/`revisor.py`.

## 0. A regra que manda: a imaxe di a frase

Cada plano ilustra **o que se oe nese momento**: quen, que fai, onde e con que obxecto. Antes de escribir o prompt,
escribe a **frase visual** en galego: "unha muller vella ofrécelle unha cunca de auga a unha moza preñada á luz do
lume". Se a frase non ten suxeito nin verbo concreto, o plano acabará nun bodegón ou nunha paisaxe baleira (o 47 % dos
planos da v1 non tiñan persoas e só ≈ 25 de 162 tiñan alguén facendo algo).

- O **suxeito** e a **acción** van ao principio do prompt (CLIP le 77 tokens e pesa máis o primeiro).
- Se a narración é abstracta ("son cifras terribles", "unha tradición inventada"), ilustra **o obxecto ou o xesto
  que a fai concreta** (un escribán pecha un legaxo, unha man bota grans de café na queimada), non un ambiente.
- Se o texto nomea un lugar real (Santiago, Samos), **non inventes o monumento**: usa unha foto real tal cal, un
  detalle sen identidade (pedra mollada, un arco) ou a xente do lugar (o tribunal da v1: "catedral inventada").
- A `clave` do plano é o elemento que ten que verse e que se nomea no texto (a cunca, o gato, o carro). Debe ser un
  obxecto grande e recoñecible (ver §7).

## 1. Composicións que chaman a mirada

| Recurso | Regra | Como se pide (inglés) |
|---|---|---|
| **Escala e rostro** | Unha cara grande e ben iluminada (primeiro plano) ou figuras enteiras nun lugar que dá escala. Nunca 3-6 caras medianas (saen deformes) | `close-up of an old woman's face lit by the fire`; `a tiny figure walking past a huge granite wall` |
| **Mans e xesto** | A acción vese nas mans: amasar, fiar, remover o pote, verter auga, pechar un legaxo, coller herbas. Un xesto simple e grande no cadro | `her hands kneading rye dough on a wooden board`, `pouring water from a clay jug into a bowl` |
| **Luz motivada** | A fonte vese ou xustifícase (lume, candea, porta, fiestra, lúa) e ten dirección: de lado ou de contra, non de fronte | `lit from the side by the hearth fire`, `rim light from the open door behind her` |
| **Primeiro termo e profundidade** | Tres termos: algo preto (marco da porta, póla, pote, muro, ombreiro), o suxeito no medio e o fondo. Dá relevo á paralaxe 2,5D da peza MOVEMENTO | `seen past the dark edge of a doorway`, `over the shoulder of`, `a clay jug in the blurred foreground` |
| **Acento de cor** | Unha cor cálida pequena nunha paleta apagada: o lume, un pano vermello, as lapas azuis da queimada, unha cinta vermella no corno dunha vaca | `a small red woollen scarf`, `the only colour is the orange glow of the embers` |
| **Mirada e dirección** | O suxeito mira cara ao que se narra ou cara ao interior do cadro; deixar aire diante da mirada e do paso | `looking towards the fountain at the left of the frame` |
| **Espazo para o movemento** | Nos planos de imaxe a vídeo (I2V): o suxeito enteiro e lonxe dos bordos, aire na dirección do paso, nada fino que cruce diante (reixas, pólas finas), fondo simple; nos de paralaxe: termos ben separados e un fondo sen detalles finos | `a woman walking from left to right along a wide stone path, plenty of space ahead of her` |

**Relación entre persoas:** na parte esperta, 1 de cada 4 planos con dúas persoas que se relacionan, resolto con
*over-the-shoulder* (unha cara grande enfocada, a outra de costas en primeiro termo). Xa estaba na v1 e funcionou
(planos 6, 28, 81 da v1).

## 2. Plantilla de prompt v2

    [tipo de plano e composición] of [suxeito + acción coas mans ou a mirada], [primeiro termo], [lugar: 1-2 elementos
    galegos], [luz motivada e dirección], [acento de cor]

- **≤ 50 palabras.** Concreto: `an old woman in a dark wool headscarf pouring water from a clay jug` e non
  `a peasant woman doing chores`.
- Unha soa acción por plano e un só foco de atención.
- Na zona de durmir (fase `durmir`) seguen as regras da v1: sen lume vivo, máis paisaxe e detalle quieto, sen caras
  mirando á cámara; pero **o plano segue a ilustrar a frase** (as lousas cando chove nas lousas, o escano baleiro
  cando se di que está baleiro).

## 3. Sementes (referencias) para o que SDXL non sabe

Campo `referencia` da lista de planos (implementado en `imaxes.py`; formato en `gauntlet4/contexto.md` §6.1, ver
`informe-r1.md` para a técnica que gañou e o seu custo). Usalas en **todos os planos de iconografía galega** (D18):
hórreo, carro de bois, palloza, lareira con pote, queimada, muíño, aldea de granito. Só as `semente` de
[`referencias.json`](referencias.json) (CC0, dominio público, CC BY). Regras:

- O prompt describe **a mesma escena que a semente** (o mesmo obxecto, o mesmo punto de vista); a semente pon a
  forma, o prompt pon a luz, a hora, a xente e a época.
- Unha semente vertical (o hórreo 01-01) vai con `"encadre": "encaixar"` e modo `profundidade`.
- Unha semente con cousas do presente (cables, estrada, botellas) recórtase (`recorte`) ou vai en `profundidade`,
  que só copia a forma.
- Nunca sementes con persoas recoñecibles para xerar caras.

## 4. O que SDXL-Lightning fai mal e como evitalo

| Se pides... | SDXL-Lightning pinta... | Pide no canto |
|---|---|---|
| hórreo, carro do país, palloza (sen semente) | cabana, casa de dous pisos, rodas de raios | **semente** (§3) |
| `kitchen` | un salón moderno con estufa de ferro (4 de 4 intentos do plano 91 da v1) | `smoke-blackened room with an open stone hearth at floor level` |
| `lane`/`street` + noite ou serán | aldea inglesa con farolas (4 de 4 do plano 5, 2 de 2 do 61) | `a narrow path between mossy granite walls`, a luz dunha lanterna de corno na man |
| `road` | estrada asfaltada con liñas pintadas (plano 67) | `a muddy cart track`, `a sunken lane between stone walls` |
| `door` só | un corredor moderno con felpudo (plano 31) | `the heavy oak door of a granite house, iron studs` e o que hai a cada lado |
| `house`/`cottage`/`village` sen máis | casas inglesas con chemineas nos hastiais e fiestras de guillotina (5, 23, 29, 33, 68, 134 da v1) | `low granite farmhouse with small openings and a slate roof`, ou semente |
| casa ou igrexa de noite | fiestras acesas con luz eléctrica, farolas (133, 161, 105) | a casa escura e unha soa fonte de luz visible (lanterna, fogueira pequena) |
| persoas sen roupa descrita | roupa do XIX-XXI: abrigo entallado, gorra plana, gorro de la, bombín, sombreiro vaqueiro (24, 26, 34, 35, 46, 78, 85) | `long dark wool skirt`, `coarse wool jacket`, `dark wool headscarf`, `straw cape`; e o campo `epoca` se o plano é do XX |
| `witch`, `meiga` | bruxa de conto | `an ordinary old village woman, dignified` (vetos de `gauntlet3/contexto.md` §8.5) |
| cuartos con mobles | cadros enmarcados, apliques, paredes pintadas (67, 94, 148) | `bare smoke-blackened granite walls`, `a wooden shelf with clay pots` |
| un xuíz, un escribán, un tribunal | pseudotexto en papeis, libros abertos | o selo de lacre, un legaxo pechado, a man que asina fóra de foco |
| lume nunha mesa ou nas mans | lapas imposibles (planos 7 e 20) | a candea nun candeeiro de ferro; o lume só na lareira |
| moitas persoas | caras clonadas e deformes | 1-3 persoas; a multitude, co son |
| `oxen` | cornos longos, rabaño | as cabezas de dous bois co xugo, ou semente do carro |
| unha catedral ou un mosteiro concreto | un edificio inventado | foto real tal cal ou un detalle sen identidade |

## 5. Topes e variedade (sen cambios fronte á v1)

Os topes de arquetipos de `revisor.ARQUETIPOS` seguen (figura soa de costas ≤ 3 %, retrato ≤ 8 %...). Novidade: nun
episodio de ≈ 65 planos (D18) cada arquetipo cabe 2-5 veces; a lista de planos ten que repartilos.

## 6. Porta e revisión

A porta v6 (`revisor.py`, VERSION 9) caza o que listou o tribunal da v1 (ver `informe-r1.md`, calibración). Pero **a
porta non abonda**: na rolda de arranxos dous planos aprobados eran anacrónicos. Con D18 (≈ 65 planos), un axente
mira cada imaxe escollida antes de montar (folla de 4-6 intentos por plano) e escolle a man se a porta erra
(`escolla_manual` en `revision.json`).

## 7. `clave` e `negativo`: o que funciona

- `clave`: un obxecto grande que se nomea no texto (`cat`, `ox cart`, `clay bowl`, `stone cross`, `old woman`). A porta
  v6 compárao cos demais obxectos do episodio (§ calibración no informe); conceptos pequenos ou abstractos (`maize`,
  `bandage`, `earring`) non se recoñecen ben: mellor un plano de detalle no que o obxecto enche o cadro.
- `negativo`: só obxectos que nunca deben aparecer e que non se parecen ao suxeito (`street lamps` nunha rúa, `sofa`
  nun cuarto); nunca variantes do propio suxeito (`cauldron` nunha queimada, `stove` nun pote).
- `epoca` (novo, opcional): `"xx"` nos planos do século XX (a queimada dos anos 50, o conxuro de 1967): a porta non
  conta como fallo a roupa e os obxectos dese século.
