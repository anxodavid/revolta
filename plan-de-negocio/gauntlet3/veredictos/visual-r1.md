# visual · ronda 1

Crítico visual ciego (director de fotografía y editor de documentales de época). Revisión hecha por Claude
(agente crítico, sin intervención humana) el 30-09-2026, mirando las hojas de contacto a ojo; no es una prueba
automática.

## 1. Comparación a ciegas (escrita antes de destapar)

**Montaje.** Un script (`random.random() < 0.5`) copió las dos hojas de 16 fotogramas a 320x180 como
`imagen1.jpg` e `imagen2.jpg` en el scratchpad y guardó la clave en un fichero aparte, sin leerlo hasta terminar
esta sección. Las dos se miraron enteras y después ampliadas a 2x por cuadrantes, a la misma resolución de origen.
**Límite del ciego:** el ciego es parcial. El tema (fuego, caldero, hierbas, ancianas) y los números 1-16 impresos en
una de las hojas delatan cuál es la nuestra; el juicio se ha hecho igualmente criterio por criterio.

| Criterio | Imagen 1 (palacio barroco, corte, sirvientes) | Imagen 2 (fuego, ancianas, aldea, niebla) |
|---|---|---|
| Luz y rango dramático | 3/5. Dorado cálido y alto uniforme en casi todo; bonito, pero sin noche ni arco. | **4,5/5.** Claroscuro real (fuego, velas, crepúsculo, niebla, luna) y un arco claro de caliente-contrastado a tenue. |
| Variedad y repeticiones | **4/5.** Planos generales, masas, planos medios, detalle de manos, reflejo en espejo, simetrías. Repite dos damas escribiendo con pluma (3, 8) y muchos salones dorados. | 3,5/5. Buena escala (detalle, retrato, general), pero hay llama en 7 de 16 (1, 3, 4, 10, 12, 13, 16), cuencos o recipientes en 4 (1, 10, 14, 16) y anciana sola en 3 (3, 8, 12). |
| Coherencia de estilo | 3,5/5. El look de drama de época se sostiene, pero 2 planos van con bandas negras (6, 14) y se mezclan épocas: gorgueras y armaduras del XVI con libreas y pelucas del XVIII y un patio nazarí (11). | **4/5.** Etalonaje de cine uniforme. 10 y 14 se van a bodegón de stock. |
| Personas haciendo cosas | **4,5/5.** Escriben, sirven la mesa, se bañan, tiran de las cuerdas de una máquina, sacan agua, cargan fardos, pasean; hay grupos que interactúan. | 2,5/5. Casi siempre una figura sola y pasiva (mira, camina, está sentada). Acciones: remover el fuego (1), lacrar (4), coger hierbas (8), llenar cántaros (11). Nadie se relaciona con nadie. |
| Artefactos | 3,5/5. Caras clonadas en la multitud (4), máquina hidráulica sin sentido (6), pértiga del pozo imposible (11). | 3,5/5. Llama que sale del mango de una cuchara (10), animal dentro de la chimenea (12), cuernos dudosos (7), "cristales" azules en el cuenco (1). |
| Anacronismos | 3/5. Jardinera con camiseta verde y guantes de nitrilo (14), muy evidente; vestido palabra de honor de satén (5); pareja de aspecto turista (16). | 2,5/5. Farolas en fila (2) y luces de ciudad en el valle (13), muy evidentes; apliques de aspecto eléctrico (11); banco tapizado con cojines y chimenea de salón (12); vela en vaso de cristal y pan de molde en rebanadas (10). |

**Elección a ciegas: Imagen 1, por poco (≈55/45).** Un vídeo de historia vive de mostrar a gente de época haciendo
cosas, y la Imagen 1 lo hace en casi todos los planos: engancha por el espectáculo y la sucesión de acciones, y su
dorado plano, sin sobresaltos, no molesta para dormir (es la estética de los canales de historia para dormir que
funcionan). La Imagen 2 tiene claramente mejor fotografía y el único arco de luz pensado para ir del gancho al sueño,
pero parece más un vídeo de ambiente que un documental: bodegones y paisajes vacíos, figuras solas, fuego repetido y
dos anacronismos de luz eléctrica que se ven a la primera (2 y 13), justo en el gancho y en el cierre. Si el vídeo
fuera solo para dormir, elegiría la 2; como vídeo de historia que tiene que enganchar, elijo la 1.

**Destape.** Imagen 1 = referencia (`scratchpad/visual/ref/ref_16_320.jpg`); Imagen 2 = la nuestra
(`gauntlet3/visual/r1/contactsheet_320.jpg`). A ciegas elegí la referencia.

## 2. Veredicto: **PIERDE**

Pierde por las dos condiciones. (a) A ciegas no es igual ni mejor que la referencia para un vídeo de historia que
tiene que enganchar: gana en luz y en arco hacia el sueño, pero pierde en personas haciendo cosas, que es lo que
sostiene un documental. (b) Tiene defectos que un espectador notaría sin buscarlos: farolas en fila en el plano 2,
luces de ciudad en el valle en el 13, una llama que sale de una cuchara en el 10 y un salón con banco tapizado y
chimenea de obra en el 12.

**Mayor carencia:** la hoja crea ambiente pero no cuenta la historia del episodio, porque casi ningún plano muestra
a gallegos del siglo XVII haciendo lo que narra el guion (curar, denunciar, declarar, juzgar), y encima la luz
eléctrica de los planos 2 y 13 rompe la época a la vista de cualquiera.

## 3. Revisión específica de la nuestra (después de destapar)

Material: `r1/contactsheet.jpg` (960x540 por plano), `planos.json`, `prompts.json` (prompt final y descripción de
Florence-2 de cada intento), `porta.md`, `graduacion.json`, la biblia y el veredicto anterior (`gauntlet2/veredictos/video-r3.md`).
Las medidas de luz de esta sección las sacó Claude con un script propio sobre la hoja; no son de la puerta.

**Frente a la ronda anterior.** Lo que pidió el crítico del Gauntlet 2 (luz gris plana, "óleo IA" genérico) está
resuelto: hay claroscuro real y aspecto de fotograma. Lo que no está resuelto es el arquetipo de figuras de espaldas
alejándose, que sigue apareciendo dos veces en cuatro planos (2 y 5).

**Balance de los 16 planos.** Solo 4 pasarían a un editor exigente: 3, 8, 9 y 15 (y el 15 es la reserva, no lo
pedido). Hay 8 con anacronismos o elementos no gallegos (2, 4, 5, 6, 10, 11, 12, 13), 5 con artefactos (1, 4, 7, 10,
12) y 2 con clichés de bruja (16 claro; 4 por las velas rojas de ritual). Además, 12 de 16 no muestran el elemento
clave que pedía el prompt: la queimada (1), el farol (2), el sello (4), la era y el maíz (5), las hierbas colgando
(6), el yugo (7), el bote empujado (9), el candil (10), la lluvia (11), la lareira (12), las hogueras lejanas (13) y el
agua (14). La puerta no comprueba esto.

**Guion de color por fase** (luminancia media / desviación / % de píxeles > 0,85, medido en la hoja graduada):

| Fase | Planos | Luminancia | Contraste (desv.) | Altas luces | ¿Cumple? |
|---|---|---|---|---|---|
| gancho | 1-4 | 0,20-0,27 | 0,18-0,21 | 0,3-3,8 % | **Sí**: noche, fuego y vela, contraste alto. |
| transición | 5-8 | 0,28-0,37 | 0,15-0,21 | 0-2,4 % | **Sí**: cuatro luces de día distintas. |
| calma | 9-12 | 0,20-**0,46** | 0,14-0,21 | 0-0,3 % | **No del todo**: el 9 es el plano más luminoso de la hoja y rompe la bajada. |
| dormir | 13-16 | 0,21-0,28 | 0,11-0,15 | 0-**0,97 %** | **No**: de media es tan luminosa como el gancho (≈0,24 frente a ≈0,24); el 13 y el 16 tienen llamas vivas y el 14 y el 16 van tan saturados como el gancho (0,36-0,37). Solo el 15 cumple. |

La gradación baja el contraste (1,08 → 0,90) y la saturación (1,0 → 0,65), pero no puede quitar una hoguera ni
oscurecer lo que el generador pintó claro: el arco de dormir se decide en el prompt y en la puerta.

### Tabla por plano

| # | Fase y tipo | Problema | Corrección (prompt o puerta) |
|---|---|---|---|
| 1 | gancho · detalle | La queimada no sale: el azul son cristales o hielo en un cuenco metido en un hoyo de brasas (Florence: "mortar and pestle... fire pit"; el intento 0, "molten metal, blacksmith"). La mano se funde con el cazo, que no tiene mango. Y como el conxuro es de 1967 (`tema/investigacion.md`), ponerlo en una "dark stone kitchen" lo presenta como si fuera del XVII. | Prompt: `extreme close-up of a wooden ladle lifting burning spirits above a wide clay bowl, translucent blue flames pouring back into the bowl, darkness around`, con la mano fuera de cuadro o en el borde y sin cocina de época; `negativo: molten metal, ice`. Puerta: si Florence dice "molten metal / blacksmith / mortar / crystals" en un plano con `blue flames`, rechazar. |
| 2 | gancho · general | **Farolas de fundición en fila** y apliques eléctricos, fachadas de ciudad del XIX y una figura con pantalón ceñido y botas. Dos figuras de espaldas alejándose (el arquetipo repetido). Nadie lleva el farol pedido y no llueve. Tres intentos cayeron por "obxectos modernos" y el cuarto pasó porque Florence lo describió como "lanterns hanging from the ceiling". | Prompt sin "old town", sin "arcades" y sin "puddles reflecting the light" (piden muchas luces): `medium shot of a woman in a dark wool cloak holding a horn lantern, the only light, in a narrow granite lane at night, rain, faint glow on wet stones, deep black shadows`; `negativo: street lamps, lamp posts`. Puerta: regex y par CLIP de luz eléctrica (§4). |
| 3 | gancho · primer plano | El mejor plano: cara digna, sin rasgos de bruja, bien iluminada por el fuego. Pero el fuego está en una chimenea alta con parrilla, no en una lareira, y el chal parece una rebeca de punto. | Prompt: `open stone hearth at floor level, smoke-blackened walls` (la biblia lo dice y el prompt no lo usó) y `coarse brown wool shawl`. |
| 4 | gancho · plano medio | No sella nada: tiene un hilo rojo entre los dedos. Hay cinco velas rojas y **velas de té en cazoletas metálicas** (modernas), lo que da aire de ritual y no de escribano. Los papeles abiertos llevan renglones de pseudotexto que el Ken Burns acercará. Hay ventanales de cuarterones. Florence dijo "a book open" y la puerta no lo veta. | Plano de detalle sin papel legible: `extreme close-up detail of a brass seal pressed into a blob of red wax on folded parchment, a single tallow candle, deep black shadows`; `negativo: red candles, open book`. Puerta: `open book|book open|pages|document` en "texto na imaxe" y `tea ?lights?` en "obxectos modernos". |
| 5 | transición · general | Casitas británicas: chimeneas en los hastiales y ventanas de guillotina con cristal. No hay era ni maíz. La mujer de espaldas alejándose por el camino repite el arquetipo del 2 a 3 planos de distancia, y la puerta no lo vio (arquetipo `None`). | Prompt con la acción primero: `wide shot of a woman in a dark wool skirt spreading maize cobs on a granite threshing floor, low granite houses with dark slate roofs and small shuttered openings, morning mist`; `negativo: chimneys, sash windows`. Puerta: segundo texto CLIP para el arquetipo (§4). |
| 6 | transición · contraluz | Parece un agroturismo toscano: ventanal panorámico sobre un valle, ventanas de cuarterones, macetas y parra. No cuelga hierbas. Lo provocó la corrección del reintento, que puso "dark slate roofs, granite walls, green hills" delante de un interior y hace que el modelo abra una ventana para enseñar las colinas. | Prompt: `backlit silhouette of a woman hanging bundles of dried herbs from smoke-blackened oak beams, the small doorway of a granite kitchen, shafts of daylight, dust`; `negativo: large window, potted plants`. Código: corrección del reintento según sea interior o exterior (en interior, `thick granite walls, small shuttered window`; nunca `green hills`). |
| 7 | transición · primer plano | Tres reses (la biblia admite una o dos), sin yugo ni labrador. **A la de la derecha un cuerno le atraviesa la cabeza como un palo**, y los cuernos de la del centro se cruzan con su cara. Tampoco es un primer plano. | Prompt cerrado sobre el yugo: `close-up of the heads of two golden-brown oxen with short horns under a carved wooden yoke, leather straps, muddy lane between mossy stone walls, overcast daylight`; `negativo: long horns, herd`. Puerta: regex de animales en grupo (§4). |
| 8 | transición · plano medio | Buena luz y cara digna. Pero no huele hierbas en una carballeira: está de rodillas en un prado con las manos juntas, como rezando, y la capucha negra la acerca a una monja o a la bruja encapuchada. | Prompt: `dark wool headscarf and brown wool shawl, holding a bunch of wild herbs to her face, ancient oak grove with mossy trunks`; `negativo: hood, nun, witch`. |
| 9 | calma · paisaje | Tranquilo y bonito, pero es el plano más luminoso de la hoja (0,46) y el relieve es de fiordo o de lago escocés, no de ría. Dos hombres de pie en sus botes; nadie empuja. | Luz de la calma (`warm sunset light` o `blue hour`), no `soft pink morning light`; relieve `low rounded green hills`. Código: techo de luminancia por fase en `graduar` (§4). |
| 10 | calma · bodegón | Nada es un candil. Hay una **vela en vaso de cristal**, **pan de molde en rebanadas**, una cafetera metálica con asa (siglos XIX-XX) en vez de la jarra de barro y una pared lisa enlucida. **Una llama sale del extremo de una cuchara de madera** dentro del cuenco (artefacto). | Describir el candil, que SDXL no conoce: `a small iron oil lamp shaped like a shallow dish with a spout and a hanging hook, one small flame at the spout, a round uncut loaf of dark rye bread, a brown clay jug, rough granite wall`; `negativo: candle in a glass jar, sliced bread, kettle`. Puerta: esos objetos en "obxectos modernos" (§4). |
| 11 | calma · plano medio | Patio porticado con farolillos encendidos de aspecto eléctrico y macetas: parece un claustro italiano o un patio andaluz, no una fuente de aldea. Salen tres mujeres jóvenes (se pidieron dos). No llueve y no es anochecer. Las manos están bien. | Fuente gallega descrita: `two women in dark wool skirts and headscarves filling clay jugs at a granite wall fountain with a stone spout and a long stone trough, grey granite houses, soft rain at dusk`; `negativo: arcades, lanterns, potted plants`. |
| 12 | calma · contraluz | Es un salón del XIX-XX: banco tapizado con cojines y manta, ventanal de cuarterones y chimenea de obra con repisa y hogar de fundición. **Hay un gato negro sentado sobre los troncos, dentro del fuego**, que se ve incluso a 320 px; el gato gris tiene una oreja roja. La mujer no dormita, y el plano no es un contraluz. | Prompt: `an open stone hearth at floor level, smoke-blackened walls, a wooden high-backed bench`, sin gato (el modelo lo duplica) o `a grey cat curled on the stone floor`; `negativo: fireplace mantel, cushions, sofa`. Puerta: `cushions?|upholstered|mantel(piece)?|window seat` en "interior moderno" y par CLIP salón/lareira (§4). |
| 13 | dormir · paisaje | **El anacronismo más grave: luces eléctricas de una ciudad en el valle.** En vez de hogueras pequeñas y lejanas hay una hoguera grande en primer término, con llama viva, en la fase de dormir (la biblia: "nada de fuegos que crecen"). El cielo es de crepúsculo naranja y no de noche, y la hierba está seca. Florence no mencionó la ciudad y por eso pasó. | "Small bonfires glowing far away on dark hills" es justo como SDXL pinta una ciudad de noche. Prompt: `wide landscape of dark wooded hills at night, one small bonfire on a distant hilltop, a granite stone cross in silhouette in the foreground, starry sky, very dim`; `negativo: city lights, town`. Puerta: par CLIP de luces de ciudad en toda escena exterior de noche (§4). |
| 14 | dormir · bodegón | La idea es buena (el agua de San Xoán) pero sale mal: una jardinera gigante de flores en mitad de un valle alpino, sin agua visible y con una escala imposible. Es tan luminoso como el gancho. | `extreme close-up detail of a clay bowl of water with floating wild flowers and fennel on a granite windowsill at night, moonlight on the water surface, very dim`: tipo `detalle`, sin paisaje detrás. |
| 15 | dormir · plano medio → reserva | La carballeira con niebla es el mejor cierre para dormir de la hoja. Pero es la reserva: el Feijoo pedido (un monje en su celda con una vela) cayó dos veces como "persoa á lareira", un falso positivo (una vela no es una lareira), y se perdió el único plano de Feijoo. El aviso dice "xa no plano 11" cuando es el 12 (`revisor.py` imprime el índice desde 0). | Puerta: arquetipo "persoa á lareira" con texto más estrecho y sin aplicarlo si el prompt no nombra fuego (§4); imprimir `prev[-1]+1` y `j+1`. Guion de planos: Feijoo en calma y no en dormir (en dormir ≤ 30 % de personas), con `a closed leather-bound book`. |
| 16 | dormir · detalle | Es el cliché que la biblia veta, en el último plano: caldero negro con un líquido rojo que brilla (Florence: "a potion") y llamas vivas a los lados, no brasas. Es el plano con más altas luces de la fase de dormir (0,97 %, más que el 4 del gancho). | Sin olla en el centro: `extreme close-up detail of dying embers and grey ash on a granite hearth stone, the black iron leg of a pot at the edge of the frame, faint red glow, soft darkness`; `negativo: cauldron, potion`. Puerta: veto de clichés de bruja y de llama en dormir (§4). |
