# Peza IMAXE · rolda 1 · informe do director de arte (Gauntlet 4)

Axente Claude, 02-03/10/2026. **Quen fixo que:** as medidas, as licenzas, a xeración e a porta son automáticas; a
escolla das referencias, as etiquetas das imaxes da v1, a tradución ao inglés, os prompts reescritos e todos os xuízos
sobre imaxes ("vese", "sae") son de Claude mirando follas de contactos. **Ningunha persoa mirou nada disto.** Despois
xulga as follas un crítico visual.

## 0. Resumo

| Tarefa | Resultado |
|---|---|
| Referencias (D15) | 226 baixadas e miradas; 226/226 licenzas comprobadas nas APIs (coinciden co CSV). **29 sementes permitidas** (CC0, dominio público, CC BY) en 12 conceptos; **ningunha** para cruceiro e peto, Samos, pazo (unha pobre), fonte, escano nin roupa do XVII. O 72 % do lote é BY-SA |
| Porta v6 | Nas 173 imaxes etiquetadas da v1: molestas 25/29 (antes 14/29), bloqueantes 2/4 (igual), boas marcadas 1/35 (antes 4/35); `clave` 8/18 ausencias con **0/144 falsas alarmas** (antes 14/18 con 25/144) |
| Correlación imaxe-texto | CLIP-L fronte ao texto en inglés: AUC 0,90 entre planos que ilustran e desconectados. Liña de base da v1: z medio 1,29; o 59 % dos planos "ilustran" (z ≥ 1); no gancho só o 29 % |
| Sementes | ver §4 (pendente) |
| Biblia v2 | [`biblia-v2.md`](biblia-v2.md); proba en §5 (pendente) |

## 1. Referencias

Detalle en [`referencias-escollidas.md`](referencias-escollidas.md) e [`referencias.json`](referencias.json).

- Baixada: Wikimedia dá **HTTP 429 aos orixinais** ("use thumbnail images in sizes listed on https://w.wiki/GHai",
  `retry-after: 600`); co tamaño estándar de miniatura (960-1920 px) baixaron as 226 en ≈ 15 min (101 MB), con 18
  reintentos por 429 soltos. As do Met, en `web-large`.
- Licenzas, por concepto e uso: 163 BY-SA (72 %), 27 CC BY, 15 dominio público, 21 CC0 (18 do Met). Escollidas: 29
  `semente`, 21 `tal_cal` (BY-SA) e 1 `non` (unha cociña económica de ferro: o anacronismo do plano 91 da v1).
- **Decisión do promotor:** ¿sementes BY-SA? Gañariamos o carro de perfil (A Arnoia, Peralto), as pallozas do
  Cebreiro, a lareira co pote colgado, a queimada con lapa azul, os hórreos longos da costa, o cruceiro, o peto e
  Samos. Custo: a imaxe xerada sería probablemente obra derivada BY-SA (estudo de monetización §3.2) [S]. Alternativa
  limpa: fotos propias do promotor deses obxectos.

## 2. Porta v6 (`herramientas/pipeline/revisor.py`, VERSION 9)

**Cambios.** (1) Florence-2-base por defecto (a da produción; a large borrouse por disco). (2) Lista de palabras
nova, sacada do que Florence-2-base dixo das imaxes malas da v1: luz eléctrica (`lit up with … lights`, 6 de 6
imaxes que o din son malas), casas alleas (`cottages`, `english`, `georgian`, `two-story building`…), roupa do XX
(`beanie`, `teddy bear`, `briefcase`, `bowler hat`…) e cousas do XX (cadros enmarcados, paredes pintadas, luces de
feira); sen `sinks`, `countertop`, `sweater`, `hoodie`, `chandelier` nin `living room`, que Florence-2-base usa para
cousas de época. (3) Campo `epoca` (`"xx"`): nun plano do século XX non contan a roupa nin as cousas do XX (a taberna
dos anos 50 da v1 caía por un "glass jar"). (4) CLIP-L con 9 recortes (os 3 grandes da v5 e unha grella 3x2) e seis
pares novos con 0 falsos nas imaxes limpas: catedral inventada, abrigo moderno, tweed e gorra plana, sombreiro
moderno, cadros na parede, farol victoriano. (5) `clave` comparada con 73 obxectos e escenas comúns (z en cada
recorte; falla se z < 1,5).

**Calibración** (`calibracion/porta-v6.json`; scripts `etiquetas_v1.py`, `calibrar_clip.py`, `avaliar_porta.py`).
Etiquetas: o tribunal da v1 (Bloquea, Molesta, Menor, Lo que funciona e os seus falsos positivos), sobre as imaxes que
viu (as 11 cambiadas nos arranxos recuperáronse de git `4f43fb5`), e Claude (defectos que o tribunal non listou,
`clave` visible ou non). **Calibrada e avaliada sobre as mesmas 173 imaxes: as cifras son optimistas.** Florence vai
coas descricións que gardou a produción (Florence-2-base); o `negativo` de cada plano non entra (non cambia).

| Grupo (imaxes) | Porta anterior (VERSION 8 + lista dos arranxos) | Porta v6 |
|---|---|---|
| Bloquea (4) | 2 (133, 161) | 2 (133, 161) |
| Molesta (29) | 14 | **25** |
| Menor (10) | 3 | 4 |
| Defectos que viu Claude e non o tribunal (10) | 4 | 6 |
| Funciona, segundo o tribunal (35 sen defectos) | 4 marcadas | **1** (o castro do 53, por "casas británicas") |
| Rexeitamentos da v5 que o tribunal deu por falsos (11) | 4 | 2 (104, 110) |
| Limpas sen mención (74) | 6 | 6 (17, 86, 88, 95 teñen defectos ao mirar de novo: aplique, casas alleas, cadros) |
| `clave`: ausencias cazadas (18) | 14 | 8 |
| `clave`: falsas alarmas (144) | 25 | **0** |

**O que segue escapando:** a bombilla e o radiador do plano 84 e as rodas da maleta do 56 (os dous bloqueantes que
faltan), o lume encima dunha mesa (20), o abrigo de pelo de camelo (78), o sombreiro vaqueiro (85) e a anciá coa
chama nas mans (7). Os pares de CLIP para obxectos pequenos (bombilla, radiador, maleta de rodas, billa, cociña de
ferro) **non separan** nin con recortes pequenos (AUC 0,6-0,9 cun só exemplo e moitos falsos): non se usan. Proba con
Florence-2-base `<OPEN_VOCABULARY_DETECTION>`: §2.1 (pendente).

**Custo:** a revisión pasa de ≈ 9 s (mediana da produción da v1) a ≈ 14 s por imaxe [S: medido o CLIP de 9
recortes, ≈ 7 s por imaxe na calibración].

**Con D18 (≈ 65 planos) a porta non abonda:** a rolda de arranxos xa viu dous aprobados anacrónicos. Un axente
mira cada imaxe escollida antes de montar.

## 3. Medida de correlación imaxe-texto

`herramientas/pipeline/correlacion.py`: CLIP ViT-L/14 entre a imaxe de cada plano e a versión en inglés do que se oe
(`texto_en`), normalizada fronte a un banco común de textos (z). O CLIP multilingüe non se baixou (orde do
orquestrador, disco); no seu lugar, Claude traduciu os 162 anacos da v1 (`v1-texto-en.json`, tradución fiel; na v2
a lista de planos levará `texto_en`).

Contra as etiquetas de Claude (2 = ilustra o que se oe: 91 planos; 1 = ambiente: 52; 0 = desconectado: 19):

| Medida | Media 0 / 1 / 2 | AUC 2 fronte a 0 | AUC 1+2 fronte a 0 |
|---|---|---|---|
| similitude (cos) | 0,173 / 0,173 / 0,214 | 0,85 | 0,72 |
| **z fronte ao banco** | 0,39 / 0,57 / 1,89 | **0,90** | 0,77 |
| percentil no banco | 0,63 / 0,64 / 0,91 | 0,89 | 0,76 |

- Dos que ilustran, o 79 % teñen z ≥ 1; dos desconectados, o 21 %. Os do tribunal: 16 (z 0,10) e 20 (0,34) baixos;
  o 19 (1,72) non, porque a imaxe é "unha muller" e o texto fala de mulleres: **CLIP premia a coincidencia literal**.
- **Liña de base da v1** (`calibracion/correlacion-v1.json`): z medio 1,29 e mediana 1,35; ilustran (z ≥ 1) o 59 %;
  desconectados (z < 0,5) o 28 %. Por fase: gancho 0,38 (29 % ilustran), transición 1,00 (41 %), calma 1,15 (54 %),
  durmir 1,84 (83 %). **A queixa das persoas cadra coa medida: a parte esperta é a que menos ilustra.**
- **Uso para os críticos:** medir a v1 e a v2 co mesmo banco (os textos das dúas):
  `herramientas/gauntlet/candado.sh $PY herramientas/pipeline/correlacion.py --planos V2.json --imaxes DIR_V2 --banco plan-de-negocio/gauntlet4/imaxe/v1-texto-en.json`
  (e o mesmo coa v1 e `--banco V2.json`). É unha medida de apoio, non un xuízo: non entende quen fai que, e as etiquetas
  coas que se calibrou son dun axente.

## 4. Sementes: texto só, img2img e ControlNet de profundidade

(pendente)

## 5. Biblia v2: proba de 10 prompts

(pendente)

## 6. Configuración recomendada para a v2 (D18: ≈ 65 planos, ≈ 3-4 h de CPU)

(pendente)

## 7. Decisións que lle tocan ao promotor

1. **Sementes BY-SA** (§1): si/non. Sen elas, o carro de perfil, a palloza do Cebreiro, a lareira co pote, a
   queimada con lapa azul, o cruceiro, o peto e Samos quedan sen semente.
2. **Fotos propias** de hórreos, carros, lareiras e cruceiros do seu contorno: licenza limpa e "elemento orixinal"
   fronte á política de contido inauténtico de YouTube.
3. **SDXL fotorrealista afinado e IP-Adapter:** sen probar por falta de disco (5-7 GB e 3,2 GB). Se se libera sitio
   ou se aluga GPU, é a seguinte proba.

## 8. Licenzas (con URL)

- SDXL base 1.0 + UNet SDXL-Lightning 4 pasos: CreativeML OpenRAIL++-M
  (https://huggingface.co/ByteDance/SDXL-Lightning).
- ControlNet depth SDXL small (`diffusers/controlnet-depth-sdxl-1.0-small`): OpenRAIL++-M
  (https://huggingface.co/diffusers/controlnet-depth-sdxl-1.0-small).
- Depth-Anything-V2-Small (`depth-anything/Depth-Anything-V2-Small-hf`): Apache-2.0
  (https://huggingface.co/depth-anything/Depth-Anything-V2-Small-hf).
- Florence-2-base (`florence-community/Florence-2-base`): MIT (https://huggingface.co/florence-community/Florence-2-base).
- CLIP ViT-L/14 (`openai/clip-vit-large-patch14`): MIT (https://huggingface.co/openai/clip-vit-large-patch14).
- Referencias: a de cada unha en `referencias.json` (comprobada en Commons ou no Met o 02-10-2026).
