# Referencias escollidas para sementar as imaxes (Gauntlet 4, peza IMAXE, rolda 1)

Datos completos (licenza, autor, URL, crédito, uso e que ensina) en [`referencias.json`](referencias.json).
Material de partida: as 226 candidatas de [`docs/referencias-graficas/`](../../../docs/referencias-graficas/referencias.md)
(D15). As imaxes **non están no repo**: baixan a `$SCRATCH/referencias/` con `scripts/baixar_refs.sh` (equivalente a
`descargar.sh`; ver [`estado.md`](estado.md)).

## Como se fixo e quen fixo que

- **Automático:** baixada das 226 (02-10-2026; Wikimedia dá HTTP 429 aos orixinais, así que se piden as miniaturas
  de tamaño estándar, 960-1920 px, e reinténtase); **licenza, autor e crédito comprobados nas APIs** de Wikimedia
  Commons (`extmetadata` da páxina de cada ficheiro) e do Met (`isPublicDomain`) para as 226: **coinciden todas coa
  columna `licencia` do CSV**. Reparto: 163 BY-SA, 27 CC BY, 15 dominio público e 21 CC0 (18 do Met).
- **Claude (este axente):** mirou as 226 en follas de contactos por concepto (fóra do repo, porque levan imaxes BY-SA),
  escolleu as mellores de cada concepto e escribiu o campo `ensina`. Ningunha persoa as mirou.
- **Uso** (contexto do Gauntlet 4 §2): `semente` só CC0, dominio público ou CC BY; `tal_cal` as BY-SA (amosala enteira,
  co crédito); `non` = non usar como semente.
- Regra engadida ao miralas: **ningunha semente con persoas recoñecibles** para xerar caras (08-02, 07-03 e as de
  gaiteiros son persoas reais). E ollo co que trae cada foto do presente: cables, estradas, tubos de cheminea,
  carpintaría actual, botellas; o prompt e a porta teñen que quitalo.

## Por concepto

| Concepto | Sementes permitidas (o mellor primeiro) | Que ensinan | BY-SA que valerían (só tal cal) |
|---|---|---|---|
| 01 Hórreo | **01-01** CC0 (Christof46) · 01-02 CC BY 2.0 · 01-03 CC BY 3.0 · 01-04 dominio público | hórreo de granito enteiro con pés e tornarratos (01-01, vertical); conxunto de hórreos nun eido (01-02, horizontal); hórreo de madeira sobre esteos (01-03, con cables e estrada); millo dentro (01-04) | 01-05 Lira (hórreo longo), 01-06 Cambados, 01-07 aldea con hórreos e neve |
| 02 Carro de bois | **02-01** CC BY 2.0 (Feans, Monte Pío) · 02-02 CC BY 2.0 | **roda maciza** con travesas e treitoiro (02-01); a 02-02 ten ocos na roda: non ensina a maciza | 02-03 A Arnoia (o mellor carro de perfil), 02-04 Peralto, 02-05 roda en primeiro plano |
| 03 Palloza | **03-01** CC BY 3.0 · 03-02 CC BY 3.0 | muros de pedra e colmo (03-01 leva un tubo metálico); casa redonda restaurada (03-02) | 03-03 e 03-04 (pallozas do Cebreiro), 03-05 Ancares en 1976 |
| 04 Pazo | 04-01 CC0, **pobre** (casa torre urbana con tenda) | — | 04-02 torre do pazo de Oca, 04-03 pazo de Mos |
| 05 Cruceiro e peto | **ningunha** | (SDXL xa debuxa o cruceiro; o peto, non se probou) | 05-01 e 05-02 petos de ánimas, 05-03 cruceiro labrado |
| 06 Cociña e lareira | **06-01** CC BY 2.0 (lareira de granito con cambota, baleira) · 06-02 CC BY 3.0 (lar do XVII cun pote colgado dunha cadea e brazo de ferro, museo alemán) | esqueleto da lareira e o pote na gramalleira | 06-04 lareira rural con pote (a mellor), 06-05, 06-06 |
| | 06-03 CC BY 2.0: **non** | é unha cociña económica de ferro, o anacronismo do plano 91 da v1 | |
| 07 Queimada | **07-01** CC BY 2.0 (tarteira de barro con cuncas e cazo, sen lume) · 07-02 CC BY 2.0 (lapas azuis nunha cunca; recortar) · 07-03 dominio público (só a cunca ou a profundidade: hai persoas) | o recipiente e a lapa azul | 07-04 lapa azul enchendo a tarteira, 07-05 o cazo vertendo lume azul |
| 08 Traxe | 08-01 CC BY 2.0 (gravado de Doré, 1862) · 08-02 CC BY 2.0 (persoa real: non para caras) | traxe de festa do XIX, non o do XVII | 08-03 zocas |
| 09 Ferramentas | 09-01 CC BY 2.0 · 09-02 CC0 · 09-03 CC BY 2.0 | apeiros, gadaña, arado | — |
| 10 Muíño | **10-01** CC BY 2.0 · 10-02 CC BY 2.0 · 10-03 CC BY 2.0 | moa e moega por dentro; batán | (fonte e lavadoiro: ningunha) |
| 11 Costa | 11-01 CC BY 2.0 (dorna a vela de noite) · 11-02 CC BY 2.0 | dorna; peirao de pedra | — |
| 12 Iconografía | **12-01** CC BY 2.0 (tellados de pedra e campanario desde unha fiestra) · 12-02 CC BY 2.0 (castelo de Pambre) · 12-03 CC BY 2.0 (canecillos) · 12-04 dominio público (Cantigas) | aldea de granito vista desde dentro; torre; románico; miniaturas do XIII para amosar tal cal | — |
| 13 Armas e roupa | 13-01 CC0 do Met (cabasset do XVI) | capacete dos gardas | — |
| 14 Samos | **ningunha** | — | 14-01 mosteiro de Samos |

## Conceptos sen semente permitida (ou con unha pobre)

- **Cruceiro e peto de ánimas** (0 de 16 permitidas), **Samos** (0 de 16), **pazo** (unha CC0 urbana que non vale),
  **fonte e lavadoiro** (0), **escano** (ningunha foto o amosa claro, nin entre as BY-SA), **roupa do século XVII**
  (só traxes de festa do XIX-XXI) e **aldea de granito e lousa vista de fóra** (as permitidas teñen tella ou son
  conxuntos de hórreos; a 12-01 é unha vista desde unha fiestra).

## Que gañariamos se o promotor aceptase sementes BY-SA (decisión súa)

As BY-SA son o 72 % do lote e son, en varios conceptos, as mellores: o **carro de perfil con rodas macizas** (02-03,
02-04, 02-05: a permitida 02-01 vale, pero é unha soa e de tres cuartos), as **pallozas do Cebreiro** (03-03, 03-04),
a **lareira co pote colgado** (06-04, 06-05, 06-06: as permitidas son unha lareira baleira e un museo alemán), a
**queimada con lapa azul** (07-04, 07-05), os **hórreos longos da costa** (01-05, 01-06), o **cruceiro e o peto** e
**Samos** (sen alternativa permitida). O custo (estudo de monetización §3.2): a imaxe xerada sería probablemente obra
derivada e tería que publicarse con BY-SA e co crédito; non impide monetizar, pero pode estorbar nun encargo con
cesión de dereitos [S]. Alternativa limpa: fotos propias do promotor deses mesmos obxectos.

## Crédito (para a descrición do vídeo)

Cada referencia usada como semente ou amosada leva o seu `credito` de `referencias.json`, por exemplo:
«Hórreos de Muimenta, Carballeda de Avia, Galiza.jpg», de José Antonio Gil Martínez, CC BY 2.0
(https://creativecommons.org/licenses/by/2.0), vía Wikimedia Commons. Se é semente, engadir "imaxe xerada con IA a
partir desta fotografía" (CC BY pide indicar os cambios).
