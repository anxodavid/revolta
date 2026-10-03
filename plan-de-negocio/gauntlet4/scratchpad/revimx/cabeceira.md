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
   caldeiro (2), unha fogueira grande con multitude que lembra unha queima (38) e un barco ardendo (39). O azul só
   saíu no 32 [2], cando o prompt dicía «blue flames» sen máis.
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

[ou] = número de intento (o sufixo `-K.png`). «Contra a porta»: a porta rexeitara ese intento e eu acéptoo.

| n | Decisión | Ficheiro | Motivo |
|---|---|---|---|
