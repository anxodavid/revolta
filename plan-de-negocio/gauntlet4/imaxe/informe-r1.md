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
| Sementes | 7 escenas x 4 técnicas: a semente arranxa a forma (roda maciza, hórreo, palloza, lareira) en 5 de 7; img2img 0,5 para obxectos, 0,75 para espazos con xente, profundidade para recompoñer; **non encarece** (53-94 s fronte a 66-91 s) |
| Biblia v2 | 10 prompts reescritos (mesmo modelo e semente): ilustran o que se oe 6-8 de 10 (v1: 1-2); persoas facendo algo 9 de 10 (v1: 5); z de correlación 0,55 → 1,52. Seguen anacronismos (zapato, casas inglesas, cadros) que a porta v6 marca |

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
ferro) **non separan** nin con recortes pequenos (AUC 0,6-0,9 cun só exemplo e moitos falsos): non se usan. **Florence-2-base
`<OPEN_VOCABULARY_DETECTION>` tampouco serve**: preguntado por "light bulb", "radiator", "rolling suitcase",
"faucet", "cast iron stove", "street lamp", "wall lamp" e "framed picture", devolve unha caixa en 33 de 33 imaxes
(10 malas e 23 limpas): sempre atopa o que se lle pide (`scripts/florence_ovd.py`, ≈ 19 s por imaxe).

**Custo:** 10,5 s por imaxe (mediana de 48 revisións coa v6: MediaPipe, Florence-2-base e CLIP-L con 9
recortes); a produción da v1 medía 9,0 s coa VERSION 8.

**Coas imaxes novas** (as 28 da folla A/B e as 20 da biblia, `scripts/revisar_ab.py`): marca 6 dos 10 prompts da v1 e
7 dos 10 da v2; nas da v2 colle o que Claude viu mal (o zapato e o pantalón actuais do 8 como "tweed", as casas
inglesas do 37, o cadro e a fiestra do 84, a luz como de farola do 20) e deixa pasar as tres boas (16, 26, 33).
Falsos ou discutibles: "man sen corpo" nos primeiros planos de mans (19 e 48 da v2), "interior moderno" na vista desde
unha fiestra (aldea) e "muros encalados" na campá encalada da lareira da semente. A `clave` non distingue un hórreo
dunha cabana nin de pedras con forma de cogomelo (z alto en imaxes sen hórreo): para a iconografía, a garantía é a
semente e a mirada do axente, non a porta.

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

Folla: [`ab-sementes.jpg`](ab-sementes.jpg) (a primeira columna é a semente, todas CC BY ou CC0; script
`scripts/sementes_ab.py`, o mesmo código ca produción: campo `referencia` de `imaxes.py`). Mesmo prompt e mesma
semente en cada fila; SDXL-Lightning 4 pasos a 1024x576 (a configuración da produción da v1 nesta CPU sen bf16).

**Tempo por imaxe** (CPU de 4 núcleos, co candado; dúas máquinas: antes e despois do reinicio do 03-10, a segunda
≈ 20 % máis rápida): texto só 66-91 s (122 s a primeira, en frío); img2img 0,5 (2 pasos) 53-94 s; img2img 0,75
(3 pasos) 64-105 s; ControlNet de profundidade small a 0,6: 68-102 s, **≈ 3-10 % máis ca o texto**, e 1-2,4 s de
mapa de profundidade. **A semente non encarece: img2img 0,5 é a opción máis barata** (≈ 20 % menos ca o texto).

Que sae (xuízo de Claude mirando a folla; o crítico visual decide):

| Escena (semente) | Texto só | img2img 0,5 | img2img 0,75 | Profundidade 0,6 |
|---|---|---|---|---|
| Lareira (06-01) | cheminea de salón á altura da cintura | lar de granito correcto, muller medio transparente | **lar ao nivel do chan e campá de granito, anciá sentada ao lume: a mellor da folla** | cara xigante na campá |
| Carro (02-01) | rodas de raios | **roda maciza da semente**, pero buratos redondos na caixa | rodas de raios | rodas de raios |
| Palloza (03-01) | cabana de colmo "escocesa" | **palloza da semente** (planta redonda, colmo)... co tubo metálico da foto | paredes brancas (encalado) | silueta correcta entre néboa |
| Queimada (07-02, recortada) | lapas laranxas e azuis enormes arredor dun cazo negro | mesa de restaurante con "tea" azul | vermes azuis no cuncón | **cunca de barro con lume e cazo**, lapa laranxa |
| Hórreos (01-02) | patio con barrís de pedra: sen hórreo | **hórreos sobre pés con tornarratos**, e a casa moderna do fondo da foto | os pés convertidos en estatuas | **hórreo correcto e un home traballando ao lado** |
| Hórreo vertical (01-01, encaixado con bandas desenfocadas) | muller ante unha cabana | pila de bloques entre bandas borrosas | muller cun cesto, bandas borrosas | figura con capucha dentro dunha caseta: **fallo do encadre** |
| Aldea desde a fiestra (12-01) | rúa de granito verosímil, figura de costas | marco e tellados da semente e a vila moderna do val | aldea de pedra, figura de costas | composición rara |

**Conclusións:**
1. **A semente arranxa a forma que SDXL non sabe** (roda maciza, hórreo, palloza, lareira ao nivel do chan): en 5 de
   7 escenas a mellor imaxe é unha das tres técnicas con semente; o texto só non deu ningún hórreo nin ningunha roda
   maciza (como na v1).
2. **A técnica depende do que se pide:** img2img 0,5 para un obxecto que ten que saír igual (carro, hórreo,
   palloza); img2img 0,75 para un espazo onde se engade xente (lareira); profundidade 0,6 para recompoñer cun
   personaxe novo (hórreos con home traballando, cunca da queimada). Non hai unha forza que valla para todo.
3. **A semente arrastra o presente da foto** (tubo de cheminea, vila moderna, mesa de restaurante, casa con
   cheminea de ladrillo): hai que recortala (`recorte`) ou escoller outra. **O encadre con bandas desenfocadas
   (`"encadre": "encaixar"`) fallou**: o modelo pinta as bandas como bandas; para unha semente vertical, recortar
   unha parte 16:9 ou usar outra horizontal.
4. A lapa azul da queimada sae mellor sen semente (o lume é o que SDXL sabe facer); a semente serve para a cunca.
5. **Sen probar** (falta de disco, orde do orquestrador): IP-Adapter e ControlNet de bordos (canny); o de
   profundidade "small" pode ser o motivo das formas pobres (rodas, cara na campá) [S].

**Créditos das sementes que aparecen na folla** (CC BY pide o crédito; xeradas con IA a partir delas):
«Dende a Fiestra» de amaianos (CC BY 2.0); «Horreos-Galicien-IMG 0274a» de Christof46 (CC0); «Carro, Monte Pío,
Santiago de Compostela» de Feans (CC BY 2.0); «Palloza Cantexeira» de FCPB (CC BY 3.0); «Reitoral de Beiro,
Carballeda de Avia 3» de José Antonio Gil Martínez (CC BY 2.0); «Pequena queimada» de Kimia Solutions (CC BY 2.0);
«Hórreos de Muimenta, Carballeda de Avia» de José Antonio Gil Martínez (CC BY 2.0); todas vía Wikimedia Commons
(URL en `referencias.json`).

## 5. Biblia v2: proba de 10 prompts

Folla: [`biblia-v1-v2.jpg`](biblia-v1-v2.jpg) (esquerda o prompt da v1, dereita o reescrito por Claude segundo
[`biblia-v2.md`](biblia-v2.md); mesmo modelo, mesma semente, 1024x576; `scripts/biblia_proba.py`). Planos 8, 16, 19,
20, 26, 33, 37, 48, 84 e 92 da v1, escollidos entre os que o tribunal ou Claude viron desconectados ou baleiros.

Xuízo de Claude mirando a folla (o crítico visual decide):

| Plano (o que se oe) | v1 | v2 |
|---|---|---|
| 8 (calzarlle ao home os zapatos da muller) | dúas mulleres xunto ao lume; nin zapatos nin home | **o xesto: unha man calza un zapato**, pero o zapato é masculino e moderno e a imaxe sae case en branco e negro |
| 16 (os xuíces foron moito máis duros) | xuíz con perruca e libro aberto | xuíz que mira cara abaixo coas mans sobre un pano vermello; segue o papel aberto e non sae o selo |
| 19 (a que curaba, a que axudaba nos partos) | muller deitada e outra mirándoa; un cadro na parede | **primeiro plano das mans que ofrecen unha cunca de herbas**: di a frase |
| 20 (os veciños espreitan a fonte) | dúas figuras ante un templo clásico inventado | o mesmo templo, agora con tres mulleres e un home que mira; unha luz que parece unha lámpada |
| 26 (o gando bebe auga de sete fontes) | val baleiro | **moza con dúas vacas bebendo nun regato** |
| 33 (estaba á porta debandando cando chegou Ana) | rúa "inglesa", muller de costas | anciá sentada na soleira, cara e manto vermello; sen o fío nin a segunda muller |
| 37 (a Real Audiencia procesou a Marta) | igrexa nun prado, baleiro | un home de negro lendo un papel na rúa, **pero con casas inglesas e chemineas** |
| 48 (as queimadas cos amigos nos anos 60) | dous homes sorrindo con cuncas | **catro amigos rindo arredor da cunca en chamas** |
| 84 (a nai que ensina á filla) | mans moendo nun pote | **dúas mulleres traballando xuntas as herbas**, pero cun cadro e unha fiestra de cuarterolas |
| 92 (a cociña onde se recibía e se falaba) | dous vellos á mesa cunha lámpada colgada | sala escura con xente arredor do lume do lar |

- **Correlación:** a v2 amosa a acción do texto en 6 dos 10 (8, 19, 26, 48, 84, 92) e en parte noutros 2 (33, 37);
  a v1, en 1-2. **Persoas facendo algo:** v2 en 9 de 10, v1 en 5 de 10.
- **Atractivo:** máis caras e mans, acento de cor (manto vermello, lume na mesa dos amigos), primeiro termo (mans no
  19 e no 8). A v2 non mellora a luz, que xa era boa na v1.
- **O que segue saíndo mal:** anacronismos que a v2 non evita (zapato moderno, casas inglesas, cadros e fiestras de
  cuarterolas cando hai "room" ou "street"), e os edificios inventados (o templo do 20). A porta v6 ten que mirar
  estas 20 imaxes (§5.1) e a lista negativa da biblia v2 xa nomea eses casos.
- **Medida automática** (CLIP-L fronte ao `texto_en`, banco dos 140 textos da v1; `calibracion/correlacion-biblia.json`):
  **z medio 0,55 → 1,52; ilustran (z ≥ 1) 4 → 7 de 10; desconectados (z < 0,5) 4 → 2.** Coincide co xuízo de Claude
  salvo no 33 e no 37, que a medida dá por desconectados nas dúas versións.
- **Porta v6:** marca 10 de 10 imaxes da v1 e 7 de 10 da v2 (§2); as tres da v2 que pasan (16, 26, 33) son das boas.

## 6. Configuración recomendada para a v2 (D18: ≈ 65 planos, ≈ 3-4 h de CPU)

**Custos medidos nesta CPU** (Xeon 2,8 GHz, 4 núcleos, sen bf16; `calibracion/perfil-tempos.json`): a 1024x576,
texto 1,4 s + UNet 4 pasos 48 s + VAE 22 s ≈ **72 s**; a 1344x768, 1,3 + 74,5 + 39 ≈ **115 s** (1,6x); img2img 0,5
≈ 20 % menos ca o texto; profundidade small +3-10 %; porta v6 10,5 s por intento; carga do modelo 12-32 s (≈ 10 min
co disco frío tras un reinicio).

| Elemento | Recomendación | Por que |
|---|---|---|
| Modelo | SDXL base + UNet Lightning 4 pasos (o da v1) | 8 pasos custa 1,7x e ten os mesmos fallos (Gauntlet 3); o afinado fotorrealista e o IP-Adapter quedan sen probar (disco) |
| Resolución | **1344x768** na parte esperta (gancho, transición, calma: caras, mans, xente); **1024x576** ao durmir (escuro, pouco detalle) | D18 pide calidade; a 1344 é máis nítida (comparativa do Gauntlet 3) e a montaxe leva todo a 1920x1080 |
| Intentos | ata **3** por plano, parando no primeiro que pasa a porta | ≈ 40 planos espertos x 1,8 x (115 + 11) s + ≈ 25 de durmir x 1,5 x (72 + 11) s ≈ **3,4 h** [S: 1,8 e 1,5 intentos de media son supostos; a v1 medía 2,38 coa porta anterior, máis estrita] |
| Prompts | biblia v2: a frase visual (quen, que fai, con que), composición, sen as palabras trampa; `texto_en` en cada plano | proba §5 |
| Sementes | en **todos** os planos de iconografía galega, só `semente` de `referencias.json`, limpas (recorte sen cables nin tubos): **img2img 0,5** para un obxecto que ten que saír igual (carro, hórreo, palloza); **img2img 0,75** para un espazo con xente (lareira); **profundidade 0,6** para recompoñer cun personaxe novo (hórreos con alguén traballando, a cunca da queimada); a lapa da queimada, sen semente | §4; non encarecen |
| Porta | v6 (`revisor.py` VERSION 9) con `IMG_RESERVAS=0`, `epoca: "xx"` nos planos do século XX | §2 |
| Revisión dun axente | **todas as imaxes escollidas**, en follas de 12 a 960 px antes de montar, e os planos que esgotan os 3 intentos: escolle outro intento (`escolla_manual`) ou reescribe o prompt | a porta non ve a bombilla, o radiador, a maleta de rodas nin un hórreo falso; ≈ 30-40 min de axente [S] |
| Correlación | `correlacion.py` sobre a v2 e a v1 co mesmo banco, como medida para os críticos | §3 |

**Sen probar e pendente:** refinar a 1344x768 unha imaxe xerada a 1024 (`scripts/refinar_proba.py`, preparado) e un
descodificador TAESD-XL (≈ 10 MB, MIT) para os intentos: o VAE é o 31-34 % do tempo, así que daría ≈ 1 intento máis
por plano co mesmo custo [S].

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
