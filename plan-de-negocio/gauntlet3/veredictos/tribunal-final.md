# Tribunal final · Gauntlet 3 · "As meigas de verdade" (episodio largo, 31:22)

Un solo tribunal con tres miradas (director de fotografía y editor de documentales de época; guionista de canales de
historia para dormir; responsable de cumplimiento para YouTube), en un solo agente: Claude, el 01-10-2026, por
encargo del orquestador (`gauntlet3/tribunal/encargo.md`). **Ninguna persona ha revisado nada de esto**: es el juicio
de un agente sobre hojas de fotogramas, textos y medidas automáticas. No he visto el vídeo en movimiento ni lo he
oído.

## 1. Imagen a ciegas (escrita antes de destapar)

**Montaje.** El orquestador (Claude) dejó dos hojas de 16 fotogramas a 320x180 en `$SCRATCH/tribunal/cego/` como
`imagen1.jpg` e `imagen2.jpg`, con la clave aparte en `clave.txt`. No he leído la clave hasta guardar esta sección en
git, y tampoco he mirado las hojas del repo que delatarían la nuestra (`tribunal/detalle_*.jpg`, `folla16_320.*`).
Miré cada hoja entera y después ampliada a 2x por cuadrantes (y a 4x seis fotogramas de la Imagen 2). Las medidas de
luz las sacó Claude con un script propio sobre las mismas hojas (luminancia Rec. 709 de 0 a 1 por fotograma,
porcentaje de píxeles por encima de 0,85 y saturación media); no son de la puerta automática.

**Límite del ciego: esta vez no hay ciego.** La Imagen 1 es la misma hoja de referencia de la ronda 1, y
`visual-r1.md`, que el encargo manda leer para los criterios, la describe plano a plano (la jardinera con camiseta
verde y guantes de nitrilo, la máquina hidráulica, el pozo, las damas que escriben con pluma). Además, la Imagen 2
lleva un rótulo en galego en el fotograma 11 ("Capítulo VI · A noite de san Xoán"). Supe cuál era cuál al primer
vistazo. He juzgado igualmente criterio por criterio, con las mismas escalas que la ronda 1, y dejo las medidas a la
vista para que se puedan comprobar.

| Criterio | Imagen 1 (palacio barroco, corte, sirvientes) | Imagen 2 (fuego, aldea, mar, bodegones, luna) |
|---|---|---|
| Luz y rango dramático | 3/5. Dorado alto y uniforme; nunca es de noche. Luminancia media 0,37 y 4,6 % de altas luces, sin bajada: por cuartos de la hoja, 0,35 → 0,38 → 0,33 → 0,40, y el último fotograma (16, jardín a pleno día) es el más claro de todos (0,59 y 21 % de altas luces). | **4,5/5.** Claroscuro de verdad: fuego de noche (1, 2), contraluz con niebla (3), nublado (7), crepúsculo sobre el mar (8), luna (11, 12), niebla (13). Y un arco que se mide: por cuartos, luminancia 0,30 → 0,36 → 0,23 → 0,19 y altas luces 2,6 % → 0,7 % → 0,0 % → 0,0 %. Lo que no cuadra: el segundo cuarto es más claro que el primero (calle al sol en el 4, campo en el 5) y el último fotograma es una llama viva, aunque pequeña. |
| Variedad y repeticiones | 3,5/5. Mucha escala (exterior general, masas, plano medio, detalle de manos, reflejo en espejo), pero 9 de 16 son salones dorados y 4 son alguien con papeles en una mesa (3, 8, 9, 13). | 3,5/5. El fuego baja a 3 de 16 (1, 2 y la vela del 16; la ronda 1 tenía 7). Pero 6 de 16 son bodegones (1, 6, 12, 14, 15, 16), 3 son paisajes vacíos (7, 9, 11) y la figura sola de espaldas sale 3 veces (3, 5, 8): el arquetipo que ya señaló la ronda 1. |
| Coherencia de estilo | 3,5/5. El aspecto de drama de época se sostiene, pero 2 planos van con bandas negras (6, 14) y mezcla siglos: gorgueras y armaduras del XVI con libreas y pelucas del XVIII, y un patio nazarí (11). | **4/5.** Etalonaje de cine uniforme (verde apagado, ámbar, azul de noche). Se salen el 4 (postal soleada de pueblo inglés) y el 6 (bodegón de cafetería de banco de imágenes). |
| Personas haciendo cosas | **4,5/5.** Hay gente en 14 de 16 planos y casi siempre hace algo: escriben, sirven la mesa, bañan a alguien, tiran de las cuerdas de una máquina, sacan agua, cargan fardos; hay grupos que se relacionan. | 2/5. Hay gente en 6 de 16 (2, 3, 4, 5, 8, 10). Solo el 2 muestra una relación (dos mujeres acercan las manos con una lumbre pequeña entre hogueras) y el 4, gente que pasa por una calle; el resto camina de espaldas, está de pie de espaldas o mira (10). Ningún oficio. Peor que en la ronda 1 (2,5). |
| Artefactos | 3,5/5. Caras clonadas en la multitud (4), máquina hidráulica sin sentido (6), pértiga del pozo imposible (11). | **4/5.** Nada salta a la vista a 320 px. Detalles: un apero de hierro sin forma reconocible que se funde con el asa del cesto (14); dos paletas de madera en vez de un cazo y llama naranja, no azul (1); tres llamas altas sobre trípodes, como de escenario (2); bolas de paja en mitad de la calle (4). |
| Anacronismos | 3/5. Jardinera con camiseta verde y guantes de nitrilo (14), muy evidente; vestido palabra de honor de satén (5); pareja de aspecto turista (16). | 3/5. Ya no hay luz eléctrica (la ronda 1 tenía farolas y luces de ciudad). Pero: jarra de vidrio, jarra de cerveza de cristal con espuma, granos de café y limones (6), lo más evidente; pueblo inglés de sillería con ventanas de guillotina y chimeneas en los hastiales (4); hombre con gorra plana y gabán del XIX-XX (5); vestidos de talle ajustado del XIX (2); ventana grande de muchos vidrios (13); vela de pilar moderna (16). Las luces desenfocadas del 10 pueden leerse como bombillas. |
| **Suma (máx. 30)** | **21** | **21** |

**Elección a ciegas: Imagen 1, por poco (≈55/45), la misma que en la ronda 1 y por la misma razón.** Empatan en la
suma, y la Imagen 2 gana en tres criterios de oficio (luz, coherencia, artefactos) y ha quitado lo peor de la ronda 1
(luz eléctrica, fuego en 7 de 16, el gato dentro del fuego). Pero un vídeo de historia vive de enseñar a gente de
época haciendo cosas, y ahí está la mayor distancia de la tabla (4,5 contra 2): la Imagen 2 sigue pareciendo un vídeo
de ambiente, con 9 de 16 planos sin personas y 3 figuras solas de espaldas, y sus dos anacronismos más visibles (el
pueblo inglés y el bodegón con cerveza y café) caen en la primera mitad, la que tiene que enganchar. Para la parte de
dormir elegiría la Imagen 2 sin dudarlo: es la única de las dos con un arco de luz que baja de verdad.

**Destape** (escrito después de guardar lo anterior en git, commit `e0864fe`). `clave.txt`: Imagen 1 = referencia,
Imagen 2 = episodio. A ciegas elegí la referencia, como en la ronda 1. `folla16_320.json`: los 16 fotogramas son uno
de cada 10-11 planos (planos 1, 12, 22, 33, 44, 55, 65, 76, 87, 98, 108, 119, 130, 141, 151 y 162) y se reparten así:
gancho 2, transición 4, calma 3 y dormir 7. Es decir, 7 de 16 caen en la fase de dormir (desde el plano 98, 13:55),
que por diseño lleva pocas personas, y eso explica parte del 2/5. Pero en los 9 fotogramas anteriores a dormir solo
hay acción en 2 (planos 12 y 33), así que la carencia sigue ahí aunque se descuente esa fase. Correspondencia para
las secciones siguientes: el fotograma *n* de la Imagen 2 es el plano de la lista anterior en la posición *n* (el 6,
bodegón con cerveza y café, es el plano 55, 5:48; el 4, pueblo inglés, es el 33, 3:07).

## 2. Imagen tras destapar

**Material y método.** Además de las 40 imágenes de `tribunal/detalle_1.jpg` … `detalle_5.jpg`, miré **las 162 imágenes
que usó el montaje** (`$SCRATCH/longo/w/imaxes_graduadas/`, ya graduadas; abiertas con PIL en hojas de 8, sin
ffmpeg). El Ken Burns del montaje hace como mucho un zoom de 1,12x (`montaxe.py`, `ZOOM`), así que en pantalla se ve al
menos el 89 % de cada imagen. De `qa.json` saqué lo que dijo la puerta automática en cada intento (problemas, avisos y
la descripción de Florence-2). Los recuentos "a ojo" y la clasificación son de Claude; los datos de la puerta son
automáticos. Tiempos: inicio y fin del plano según `escenas-montadas.json`; "fichero" es la hoja de detalle donde se
ve o, si no sale en ninguna, la imagen de `imaxes_graduadas/`.

**Corrección de la sección 1.** El fotograma 6 de la hoja a ciegas (plano 55, 5:48: jarra de vidrio, cerveza, café y
limones) no es un anacronismo: ilustra la queimada del siglo XX ("tradición inventada"). El defecto es otro, menor:
no se lee como queimada sino como té helado y cerveza.

### 2.1 ¿Se corrigió la mayor carencia de la ronda 1?

La carencia era: *"casi ningún plano muestra a gallegos del siglo XVII haciendo lo que narra el guion (curar,
denunciar, declarar, juzgar), y encima la luz eléctrica de los planos 2 y 13 rompe la época a la vista de
cualquiera"*. **Respuesta: a medias. La primera mitad mejora en el gancho; la segunda no se corrigió.**

| Parte de la carencia | Ronda 1 (hoja de 16) | Episodio (162 planos) | ¿Corregida? |
|---|---|---|---|
| Gente haciendo lo que se narra | 4 acciones de 16; nadie se relaciona con nadie | Hay personas en 76 de 162 planos (47 %), pero solo en ≈ 25 hacen algo o se relacionan: gancho 8 de 21 (38 %), transición 7 de 37 (19 %), calma 6 de 39 (15 %) y dormir 4 de 65 (6 %) [recuento de Claude a ojo]. Ya hay relaciones (planos 2, 6, 8, 12, 28, 57, 59, 81, 92 y 150), y el gancho enseña la premisa: la declaración (6), el lacre (13), el tribunal (15) y la puerta de la cárcel (17) | **En parte.** Mejora clara en el gancho. En la transición y la calma, casi todos los planos con persona son de una figura sola que mira, camina o posa. Además, en **36 de los 162 planos** la imagen elegida lleva el aviso de la puerta "falta: <elemento>": lo que pedía el prompt no salió. Ejemplos: 16 (un juez → una anciana con velas), 19 (una partera dando una infusión a una embarazada → una mujer sola sentada) y 20 (los vecinos espiando la fuente → un anciano con un fuego encendido encima de la mesa) |
| Luz eléctrica | Farolas (2) y luces de ciudad (13) | Bombilla desnuda y radiador (84), farolas encendidas en el rótulo del capítulo VII (133) y apliques de porche en una casa colonial (161). Probables: apliques con tulipa (91), un pueblo iluminado al fondo (105), una lámpara colgante (148) y un pie de farol victoriano con cables (82) | **No** |
| Fuego repetido | Llama en 7 de 16 | 3 de 16 en la hoja a ciegas. Más de un 1,5 % de píxeles de llama en 15 de 162 planos: gancho 24 %, transición 0 %, calma 15 %, dormir 6 % (medida `lume_quente` de la puerta) | **Sí** |
| Clichés de meiga | Caldero con poción (16) y velas rojas (4) | No hay escobas, sombreros de pico, narices ganchudas ni calderos con poción. El más cercano es el 7 (0:27): una anciana con una llama en las manos, fuegos a los lados y un cuenco que brilla | **Casi** |
| Figura sola de espaldas | Planos 2 y 5 | La puerta detecta 6 (planos 5, 22, 29, 33, 46 y 128), y hay más sin detectar (44, 76, 104) | **Igual** |

**Por qué la puerta no lo paró.** 127 planos pasaron la puerta y **35 salieron sin pasarla**: al agotar los intentos,
el pipeline se queda con el mejor. 27 de esos 35 son posteriores al plano 94, cuando se apagaron las imágenes de reserva
(`IMG_RESERVAS=0`). Leídos uno a uno, unos 11 rechazos acertaban y molestan en pantalla: 33, 77, 91, 94, 105, 116, 133,
134, 145, 153 y 161. Otros ~20 eran falsos positivos o repeticiones aceptables al dormir: 59 (es una taberna de los
años 50, y la ropa y la lámpara son de su época), 100 (un atardecer), 104, 108, 110 (un "ciprés" que no está), 113,
127, 146, 154, 160 y 162 (una vela leída como "lume grande no exterior"), entre otros. Los ajustes de la producción
(`APRENDIZAJES.md`) eran razonables: "falta: objeto", witch/hooked nose/warts y el arquetipo seguido pasaron a aviso,
y el umbral de lume en la zona de dormir subió a 1,5 %. Cortaron rechazos falsos que empeoraban el vídeo. El fallo está en
la combinación: **sin reservas, un rechazo verdadero sale igual al aire, y nadie miró los 35 rechazados antes de
montar.** El peor plano del vídeo, el 84, ni siquiera es un rechazo: lo aprobó la puerta. Florence lo describió como
"two young women in a kitchen, cooking together" y no nombró la bombilla ni el radiador, y ningún par de CLIP busca
"bare light bulb" ni "radiator".

### 2.2 Defectos visibles

**Bloquea publicar.** Un espectador los ve sin buscarlos, rompen la época que vende el canal y caen en momentos
marcados: un rótulo de capítulo, el cierre y un plano de 15 s en la parte despierta.

| Minuto | Plano | Fichero | Qué se ve | Puerta |
|---|---|---|---|---|
| 10:34-10:50 (15 s) | 84 | `detalle_3.jpg` (10:42) · `083-5779b492-3.png` | **Bombilla eléctrica desnuda** colgando en el centro, arriba, y **radiador de hierro** bajo una ventana de carpintería moderna, en la cocina de dos curanderas del XVII ("Moitas das acusadas eran parteiras e menciñeiras…") | Aprobado |
| 22:49-23:03 (14 s) | 133 | `detalle_5.jpg` (22:56) · `132-a8a95fcc-0.png` | Rótulo "Capítulo VII · O frade que dubidaba" sobre una iglesia barroca con **al menos 6 farolas encendidas** en el césped y luces en la ladera: el defecto del plano 2 de la ronda 1, ahora en un rótulo | Rechazado en los 4 intentos ("luz eléctrica (CLIP)") y usado |
| 30:41-31:02 (20 s) | 161 | `160-32b10266-0.png` | Penúltimo plano ("A casa descansa baixo a chuvia"): **casa colonial anglosajona** de dos plantas con todas las ventanas encendidas y **dos apliques de porche** junto a la puerta | Rechazado ("casas británicas", "repetida") y usado; los 4 intentos tienen luz eléctrica |
| 5:51-6:01 (10 s) | 56 | `055-93ec6c81-0.png` | Emigrantes de los años 50: el hombre lleva una **maleta de ruedas con asa extensible**, en el centro del encuadre | Aprobado |

**Molesta.** Se nota si se mira y rompe la Galicia que se cuenta o el tono del texto.

| Minuto | Plano | Fichero | Qué se ve |
|---|---|---|---|
| 0:20-0:23 | 5 | `detalle_1.jpg` (0:22) | "Vilalba, mil seiscentos dezasete" sobre una calle de **casas adosadas inglesas** con chimeneas en los hastiales: la primera imagen de la historia |
| 1:55-2:03 · 2:39-2:47 · 3:04-3:11 | 23 · 29 · 33 | `022-dffb1fc5-2.png` · `028-ebee8eb3-0.png` · `032-c7ff689c-3.png` | Casa de campo inglesa ("San Xiao de Mourence"), mansión georgiana con chimeneas ("Xinzo de Limia") y calle de pueblo de los Cotswolds, este rechazado y usado |
| 6:39-6:51 | 61 | `060-879e4f8a-1.png` | "En Santiago…" sobre una **catedral inventada**, con dos torres y agujas góticas que no son el Obradoiro: el edificio que todo gallego reconoce |
| 7:42-7:50 · 8:48-9:00 | 68 · 75 | `067-af638455-1.png` · `detalle_3.jpg` (8:54) | "Pazos de Arenteiro, en Boborás" con un pueblo inglés y su puente; "unha veciña de Cangas" con **casas de madera sobre pilotes** de aire nórdico |
| 23:03-23:14 | 134 | `133-7829ec6d-1.png` | "Feijoo naceu en Casdemiro" sobre una mansión georgiana con las ventanas encendidas (rechazado y usado) |
| 2:03-2:10 · 2:18-2:25 · 3:11-3:16 · 3:16-3:24 | 24 · 26 · 34 · 35 | `023-5369e2be-0.png` · `detalle_1.jpg` (2:21) · `detalle_2.jpg` (3:13) · `034-434064b1-0.png` | **Ropa de los siglos XIX-XXI**: abrigo entallado con bolso de mano; gorra plana y chaqueta de tweed; pañuelo tipo hiyab, abrigo moderno y un peluche en brazos (el ovillo de lana del texto); gorro de lana |
| 4:31-4:38 · 9:22-9:30 · 10:50-11:03 | 46 · 78 · 85 | `detalle_2.jpg` (4:34) · `077-d130fe97-0.png` · `084-6f2a9829-2.png` | Más ropa fuera de época: dos mujeres con bombín; un abrigo de pelo de camello actual; un sombrero vaquero |
| 2:54-2:59 | 31 | `030-ef658184-0.png` | El gato salta sobre una **encimera con fregadero y grifos** de cuello de cisne |
| 12:09-12:26 · 12:55-13:05 | 91 · 94 | `090-c464f180-1.png` · `093-3be97fdb-2.png` | "Entremos nunha cociña de aldea": cocina económica de hierro y dos apliques con tulipa de aspecto eléctrico. "O escano de castiñeiro": un cuarto con un cuadro enmarcado, un aplique y una vela en vaso, sin escano ni lareira. Los dos rechazados y usados |
| 7:32-7:42 | 67 | `detalle_3.jpg` (7:37) | Una anciana **sonriente** mientras se narran azotes y "saír emplumadas á vergonza pública", con lámpara de queroseno y retratos enmarcados |
| 10:06-10:18 · 15:39-15:54 · 26:51-27:09 · 20:25-20:42 | 82 · 105 · 148 · 123 | `081-d824e3d0-0.png` · `104-3a0177b3-1.png` · `147-a2b14153-0.png` · `122-9fe164c2-0.png` | Pie de farol victoriano de hierro con cables junto a una mujer con un globo luminoso; una casa con cinco ventanas encendidas y un **pueblo iluminado al fondo** (el "luces de ciudad" de la ronda 1, pequeño); una lámpara colgante con tulipa de cristal en "a cociña da lareira"; el estanque de un parque con dos postes de farola, en vez de una fuente de aldea |
| 1:37-1:44 | 20 | `019-7a39c792-4.png` | "Uns veciños foron espreitar a fonte": un anciano con **un fuego ardiendo encima de la mesa** de madera |
| 18:37-18:47 · 25:57-26:16 · 28:25-28:44 | 116 · 145 · 153 | `115-2fe0ff20-0.png` · `detalle_5.jpg` (26:07) · `152-179e853a-0.png` | **En la zona de dormir:** una figura con ropa ceñida actual, de brazos abiertos sobre una tarima con dos tarros luminosos, en vez de un mozo saltando las brasas; un primer plano de llamas vivas durante 19 s mientras se habla de Feijoo (el prompt pedía un libro cerrado); un tejado con un penacho de humo incandescente que parece un fuego de chimenea, cuando se dice "chove sobre as lousas". Los tres, rechazados y usados |
| 0:27-0:30 | 7 | `006-ca7c5324-0.png` | Anciana con una llama en las manos, fuegos a los dos lados y un cuenco que brilla: lo más cerca del cliché de meiga que vetan `contexto.md` §8.5 y la biblia |

**Menor.**

| Minuto | Plano | Fichero | Qué se ve |
|---|---|---|---|
| 0:35-0:40 | 9 | `detalle_1.jpg` (0:38) | Caballo negro con un rayo de aspecto de ilustración fantástica: el único plano que se sale del estilo de fotograma |
| 0:40-0:46 | 10 | `009-7d019425-1.png` | Bajo el aviso hablado, un libro abierto con pseudotexto (puerta: "texto na imaxe") |
| 0:55-1:02 | 13 | `detalle_1.jpg` (0:59) | Un lacre del tamaño de un plato, prensado con los dedos y sin sello |
| 5:45-5:51 | 55 | `detalle_2.jpg` (5:48) | Los ingredientes de la queimada parecen té helado y cerveza en vidrio |
| 21:55-22:13 · 24:44-25:01 | 129 · 141 | `detalle_4.jpg` (22:04) · `detalle_5.jpg` (24:53) | El "cribo" es un disco de metal perforado colgado de una cadena, como un incensario; el apero de hierro se funde con el asa del cesto |
| 26:37-26:51 · 27:29-27:48 · 29:23-29:42 | 147 · 150 · 156 | `146-2b940b42-0.png` · `detalle_5.jpg` (27:38) · `155-8e45ae6c-0.png` | Una línea blanca pintada en el suelo del claustro de Samos; sillas de madera curvada tipo Thonet (pasa si la escena es actual); unos zapatos brogue de hombre del XX como "os zapatos da muller" |

**Lo que funciona** (para no perderlo al arreglar): caras dignas y sin rasgos de bruja en todo el episodio (14, 64, 69,
72, 98, 143); la queimada del arranque (1, 2); el gato en el agujero de la puerta (32); el castro sobre el Atlántico
(53); Feijoo escribiendo en su celda (137-139); los dos vecinos junto al cruceiro al amanecer (128); y la serie de
bodegones y paisajes nocturnos de la zona de dormir (98-132 y 155-160), oscura y sin sobresaltos.

## 3. Gancho (0:00 a 1:55)

Texto de `video/guion.txt`, tiempos de `subtitulos.gl.srt` y planos de `escenas-montadas.json`. No he oído la voz: juzgo
el texto, las imágenes y las medidas.

| Tiempo | Qué se dice | Planos | Para qué sirve |
|---|---|---|---|
| 0:01-0:20 | «Mouchos, curuxas, sapos e bruxas.» El conxuro parece antiguo, «pero ten autor coñecido, e é de mil novecentos sesenta e sete»: lo escribió Mariano Marcos Abalo en un barco amarrado en Vigo | 1-4: cuenco con llamas, dos mujeres alrededor del fuego, hombre con un pote, cabo de amarre | Dato verdadero y sorprendente n.º 1. Paga en 10 s la promesa del título |
| 0:20-0:38 | «Vilalba, mil seiscentos dezasete.» Según una testigo, la partera Dorotea do Barro decía que podía pasarle a un hombre los dolores del parto calzándole los zapatos de la mujer: «saltaría coma un poldro bravo» | 5-9: calle inglesa, declaración ante una mesa, anciana con fuego, dos mujeres en la lumbre, caballo con rayo | Dato n.º 2, con picante y atribuido |
| 0:38-0:49 | «Boas noites.» Aviso hablado (0:40,6-0:45,3) y «Isto é Cousas de Galiza para durmir» | 10-11 | Obligatorio (decisión del promotor) |
| 0:49-1:09 | Bucle 1: por qué se creyó anónimo el conxuro. Arquivo do Reino y Real Audiencia. Avance: «unha veciña que velou esperta unha noite. E un gato que ninguén deu collido» | 12-14 | Bucles 1 y 2 |
| 1:09-1:34 | La Inquisición de Santiago llevó a la hoguera a una sola mujer; para Valor Bravo fue «branda», y la justicia ordinaria, «moito máis dura». La meiga era la que curaba | 15-18 | El giro que promete el título («de verdade») |
| 1:34-1:55 | «E hai unha lista»: Campo Lameiro, la noche de san Xoán, «volveremos a esa fonte». Hoja de ruta | 19-21 | Bucle 3 |

Los tres bucles se pagan, escalonados: el 2 a las 2:47-2:59 (María Feijoa y el gato de Ana González), el 1 a las 5:09
(«O motivo do que falabamos ao principio é sinxelo») y el 3 a las 9:18-10:12 («E por fin, a lista de Campo Lameiro»
… «dúas maneiras de mirala»), dentro de la ventana de 8-10 min que pide `contexto.md` §8.3. También se cumple el
resto del §8.3: el conxuro con un solo verso y su autor, Dorotea atribuida a una testigo, la Inquisición una sola vez y
sin año, y Cibreira fuera del primer minuto (sale a las 7:42).

### Nota: 4 / 5

**Por qué engancha.**
- **Dos hechos concretos, verdaderos y raros en 35 s.** La referencia, *Historia Desconocida* (167.509 vistas), abre en
  segunda persona con tres preguntas retóricas y la promesa de un secreto, y no da el primer dato concreto de lo que
  promete hasta el minuto 5. *Relatos al Oído* (107.875 vistas) abre con dos leyendas sin fuente y una promesa genérica.
  Fuentes: `gauntlet2/referencia.md` y `veredictos/guion-r1-formato.md`, con datos de https://youtu.be/_lnOveSTjWA y
  https://www.youtube.com/watch?v=ij7nuBjh1PQ.
- **Tres preguntas abiertas que se pagan a los 3, 5 y 9-10 min.** Es justo lo que le falta a la referencia, cuyo mapa
  de calor muestra una retención "baja y casi plana a partir del minuto 7" (`gauntlet2/referencia.md`).
- **Ritmo de gancho.** 157 palabras/min con pausas y un plano cada 5,2 s de media (`qa.md`), frente a ≈ 137
  palabras/min y una imagen distinta cada ≤ 10 s en la referencia (`gauntlet2/referencia.md`).
- **Las imágenes del gancho cuentan la premisa con gente**: la queimada (1-2), la declaración (6), el lacre (13), el
  tribunal (15), la puerta de la cárcel (17) y las manos amasando (18).

**Por qué no es un 5.**
- **De 0:55 a 1:25 hay un minuto institucional**: Arquivo do Reino de Galicia, Real Audiencia, Inquisición de Santiago
  y Diego Valor Bravo. El gancho tiene 1,7 atribuciones por cada 100 palabras (recuento de Claude con expresiones
  regulares; el crítico del guion r2 midió lo mismo), frente a ≈ 0,5 en las referencias (`veredictos/guion-r2.md`).
  Es el punto de abandono más probable del gancho [S].
- **Varias imágenes no dicen lo que se oye.** La primera imagen de lugar, «Vilalba, mil seiscentos dezasete» (plano 5),
  es un pueblo inglés, y el público galego lo nota. Los planos 16, 19 y 20 no enseñan al juez, a la partera con la
  embarazada ni a los vecinos en la fuente.
- **«Boas noites» y el aviso, de 0:38 a 0:45**, avisan pronto de que es un vídeo para dormir con voz sintética. Es
  obligatorio y honesto, pero son 7 s sin gancho dentro del primer minuto; su coste en retención no está medido [S].
- **Nadie ha oído la voz.** El arousal del tono de gancho (0,643, en el cuartil alto de las grabaciones de Brais) se
  midió sobre un pasaje de prueba (`voz/informe.md`), no sobre este episodio.

**Frente a los canales grandes.** Los grandes del género en inglés, como *Sleepless Historian* (715 K suscriptores),
publican vídeos de 2-4 h con guiones de 15.000-20.000 palabras y buscan el sueño desde el primer minuto
(`gauntlet/investigacion/retornos.md`, con https://www.aibase.com/news/21860; lo de "desde el primer minuto" es [S]).
Este episodio sigue la otra estrategia, la que pidió el promotor («más gancho atractivo los primeros minutos»), y para
eso el texto está mejor construido que las dos referencias. Si engancha de verdad solo lo dirá YouTube Studio. El
umbral del plan v2 es una retención a 2 min ≥ 25 % (`docs/HANDOFF.md` §3); no hay ningún dato propio para predecirla.

## 4. Embudo hacia dormir

Medidas por fase. Las de `qa.md` son automáticas. Las de luz, sonoridad y densidad de datos las sacó Claude con
scripts propios: luz sobre las 162 imágenes graduadas; sonoridad sobre `$SCRATCH/longo/w/mestura.wav`, con ventanas
de 3 s y ponderación K (BS.1770); densidad de datos con expresiones regulares sobre `guion.txt`.

| Medida | Gancho | Transición | Calma | Dormir |
|---|---|---|---|---|
| Tramo (planos) | 0:00-1:49 (1-21) | 1:49-6:17 (22-58) | 6:17-13:48 (59-97) | 13:48-31:22 (98-162) |
| Ritmo de la voz, palabras/min con pausas (`qa.md`) | 157,0 | 154,5 | 136,3 | 114,5 |
| Duración media de plano, s (`qa.md`) | 5,2 | 7,2 | 11,6 | 16,2 |
| Luminancia media (0-1) | 0,25 | **0,37** | 0,29 | 0,20 |
| Altas luces (% de píxeles > 0,85) | 3,0 | 2,9 | 1,1 | 0,05 |
| Saturación media | 0,38 | 0,28 | 0,30 | 0,23 |
| Planos con > 1,5 % de píxeles de llama (`lume_quente` de la puerta) | 24 % | 0 % | 15 % | 6 % |
| Sonoridad a corto plazo, mediana (LUFS) | −16,5 | −16,8 | −18,3 | −19,8 |
| Cambios de ambiente por cada 10 min (de la lista de planos) | 17 (min 0-10) | | 6 (min 10-20) | 8 (min 20-30) |
| Atribuciones / años por cada 100 palabras | 1,7 / 0,7 (hasta 1:55) | 1,8 / 1,0 (1:55-12:09) | | 0,5 / 0,05 (desde 12:09) |

**¿Baja de forma gradual y sin saltos?** **Sí en voz, montaje, sonido y contenido.** El ritmo de la voz, la duración de
plano, la sonoridad y la densidad de datos bajan en cada fase, sin escalones. El permiso para dormir («Desde aquí a
historia vai máis amodo, e non tes que lembrar nada do que escoites») llega a las 12:13, unos 2 min después de la
ventana de 8-10 min de `contexto.md` §2. Hay dos matices:

1. **La luz sube del gancho a la transición** (luminancia de 0,25 a 0,37, la más alta del episodio): de la noche y el
   fuego del arranque se pasa a aldeas y prados de día (1:49-6:17). Es la única medida que va contra la curva común
   que pide `contexto.md` §2 («voz, ritmo de cortes, luz de las imágenes y sonido siguen la misma curva»). No afecta al
   sueño, porque es la parte despierta, pero el embudo de luz no empieza a los 2 min sino a los 6:17. Después baja bien:
   desde el minuto 16, luminancia ≈ 0,20 y prácticamente sin altas luces.
2. **La voz apenas cambia del gancho a la transición** (157 → 154,5 palabras/min); la bajada fuerte empieza en la
   calma. Esto es coherente con un gancho largo (1:55).

**¿Hay tramos que despierten?** No en el texto: la zona de dormir no tiene intrusiones nocturnas, muertes, torturas
ni tribunales, solo un «demo» de pasada en Feijoo. Tampoco en el sonido medido: las subidas de 4-7 LU sobre los 30 s
anteriores que aparecen en ventanas de 3 s (19:42, 23:03, 25:21 y 27:03-27:18) son la voz que vuelve tras una pausa.
Lo comprobé ventana a ventana de 1 s contra `voz_linea.wav`, que sube igual; el ambiente no salta. **Sí en la imagen**,
con cinco planos de la sección 2: el rótulo del capítulo VII con farolas (22:49), la figura actual sobre la tarima
(18:37), las llamas vivas durante 19 s (25:57), el tejado con el penacho de humo incandescente (28:25) y la casa
colonial iluminada del cierre (30:41). Los cinco salieron sin pasar la puerta.

**¿Hay tramos monótonos (D14)?**
- **Sonido: no, según las medidas.** Hay 9 tipos de ambiente; el mismo ambiente dura como mucho 2,7 min seguidos
  (`noite`, 15:20-18:04); la voz va limpia el 38,7 % del tiempo de voz y hay 10,8 cambios cada 10 min (`qa.md`).
- **Imagen: sí, y en parte es buscado.** De los 65 planos de dormir, solo 4 tienen a alguien haciendo algo. Hay tiradas
  largas de paisajes nocturnos y bodegones (99-108, 110-115, 118-127), y la puerta marcó 6 como repetidos (CLIP ≥ 0,90).
  Para quien ya se duerme está bien; quien siga despierto en el capítulo VI (16:21-22:49, 6 min y medio de hierbas,
  fuentes y orballo) verá poca variedad.
- **Voz: no se puede saber sin oírla.** La curva estrecha a propósito la variación de la F0 (4,76 → 2,60 semitonos en
  el pasaje de prueba), y la valencia también baja (0,45 → 0,39). La propia pieza VOZ pidió al promotor que escuchara si
  el final suena sereno o triste (`voz/informe.md` §4). Esa escucha no consta en el repo.

**El final.** El vídeo acaba a los 31:22. Los vídeos del género duran 1-4 h: *Relatos al Oído*, 2 h 01 min;
*Sleepless Historian*, 2-4 h (`veredictos/guion-r1-formato.md`, `gauntlet/investigacion/retornos.md`). Quien siga
despierto al terminar se encuentra con la reproducción automática del siguiente vídeo, que puede ser cualquier cosa
[S: depende de la configuración de cada usuario]. La cola de 30-60 min de lluvia sobre lousa de `contexto.md` §8.6
sigue sin decidir.

## 5. Sonido (D13, D14)

**No lo he oído.** Claude no puede escuchar, y en el repo no consta que nadie haya escuchado la mezcla del episodio
(`qa.md`: «Ningunha persoa revisou o vídeo»). Juzgo solo lo que se comprueba con datos: el diseño (`son.py` y la lista
de planos), las medidas de `qa.md`/`qa.json` y una lectura de la mezcla que hizo Claude con un script
(`mestura.wav` y `voz_linea.wav`, sin modelos).

**Diseño frente a lo que pidió el promotor.**

| Petición | Cómo está | ¿Cumple? |
|---|---|---|
| D13: lluvia solo si la escena tiene lluvia; crepitar si hay fuego; nada de ruido blanco constante; tramos de voz limpia | Ambiente por plano (`ambiente: escena`) con 8 tipos en el episodio: `lume` 302 s, `fonte` 108 s, `noite` 526 s, `aldea` 130 s, `mar` 62 s, `xente` 22 s, `choiva` 301 s y `campas` 13 s. Voz limpia el **38,7 %** del tiempo de voz. Lo sintetiza todo el código (`son.py`, con numpy): no hay grabaciones de terceros | **Sí** |
| D14: que no sea monótono ni cansino y que se adapte a la escena; murmullo ininteligible en el gentío | 34 cambios (10,8 cada 10 min; como mucho 21 en 10 min, en el arranque) y ningún aviso de parpadeo de la QA. El mismo ambiente nunca dura más de 2,7 min. El murmullo solo suena en la taberna de Eligio (6:17-6:39), la única escena de grupo hablando | **Sí** |
| Embudo también en el sonido (`contexto.md` §2) | Sonoridad a corto plazo, mediana por fase: −16,5 / −16,8 / −18,3 / −19,8 LUFS (sección 4). El código hace los eventos más escasos y suaves hacia el final (frecuencia × (1 − 0,7 · calma) y −6 dB · calma; en `noite`, la lechuza sale 0,25-0,5 veces por minuto antes de esa reducción), y el ambiente nunca supera la voz menos 8-12 dB (`son.py`) | **Sí** |

**Coherencia de imagen y sonido** (lista de planos frente a lo que se ve, revisado por Claude):
- **Bien:** lluvia con lluvia (6:39-7:50 y 29:42-31:22); lareira con lareira (12:09-13:48 y 26:51-29:00); las
  cacharelas de san Xoán (18:04-18:58); mar con barcas y costa (4:38-5:14 y 8:48-9:14); fuentes de noche (1:37-1:49,
  9:38-10:18 y 20:25-21:22); y campanas con Santiago (6:39-6:51).
- **Huecos menores:**
  - Las llamas de la queimada del primer plano (0:00) y las dos mujeres junto al fuego (0:50) van sin crepitar
    (`limpa`), quizá a propósito para dejar limpia la voz del gancho.
  - La fiesta de emigrantes llena de gente (6:01-6:08) va sin murmullo, contra la letra de D14.
  - El caballo bajo la tormenta (0:35) va sin lluvia.

**Medidas técnicas.**

| Medida | Valor | Juicio |
|---|---|---|
| Sonoridad integrada | −17,1 LUFS (puerta: −18 a −16) | Bien. Más baja que el nivel al que YouTube normaliza (≈ −14 LUFS [S]), así que sonará algo más bajo que otros vídeos, lo que para dormir no es malo |
| Pico real del MP4 | **−0,1 dBTP** (`qa.md`) | **Ajustar.** La mezcla WAV tiene el pico de muestra en −1,0 dBFS (el limitador funciona), y todos los picos máximos están en los primeros 40 s (0:09, 0:12, 0:21, 0:24, 0:36 y 0:39). La codificación AAC añade ≈ 0,9 dB. EBU R 128 fija un pico real máximo (https://tech.ebu.ch/publications/r128); el valor habitual es −1 dBTP [S]. YouTube recodifica, así que hay riesgo de recorte en los picos del gancho |
| Rango de sonoridad (LRA) | 10,2 LU (el avance de 4:50 daba 5,5) | Esperable: la voz baja 2,3 dB por la curva y las pausas con solo ambiente quedan 20-25 dB por debajo. Sin otro dato no es un defecto |
| Saltos de nivel al dormir | Ninguno del ambiente (sección 4) | Bien. Las subidas de 4-7 LU son la voz que vuelve tras una pausa |
| Pausas en los tramos `limpa` | Silencio digital: −121 LUFS, por ejemplo a las 19:47-19:48 | Cumple D13 (voz limpia), pero entre frase y frase hay silencio absoluto. Un fondo de sala muy bajo (−45/−50 LUFS) podría hacer más suave la vuelta de la voz [S, para probar con el oído del promotor] |
| ASR de la mezcla, frase a frase | WER 0,031; el 100 % de las frases suena en su tramo; desfase A/V 0,02 s (`qa.md`) | Bien: el ambiente no tapa la voz para un ASR |

**Lo que no se puede comprobar sin oír:** si la lluvia y el fuego sintéticos suenan naturales; si la lechuza y el sapo
partero de `noite` relajan o distraen; si el murmullo hecho con nuestra propia voz TTS subida de tono
(`son/informe.md` §6) suena raro en sus 22 s; y si la mezcla, en conjunto, ayuda a dormir.

**Texto público:** la descripción dice que el ambiente es «choiva, lume, auga, vento, noite, campás». Pero `vento` no
sale en el episodio, y faltan `mar` y `aldea`.

## 6. Cumplimiento para publicar

Revisado por Claude sobre `descricion.txt`, `guion.txt`, `subtitulos.gl.srt`, `rotulos.json`, `qa.md` y las fichas de
licencia y las páginas de ayuda de YouTube consultadas hoy (URL en cada fila). No es asesoría jurídica.

| Requisito | Estado | Evidencia | Qué falta |
|---|---|---|---|
| Aviso hablado vigente, literal, en el primer minuto y tras un arranque en frío de ≤ 40 s | **Cumple** | «A voz que vas escoitar é sintética, e este texto preparouno un proceso automático» suena de 0:40,6 a 0:45,3, tras un arranque de 0:00 a 0:40 (`porta_texto`: `aviso_literal: true`) | — |
| Que el aviso sea verdad | **Cumple** | Escribieron el guion agentes Claude, sin revisión humana (`qa.md`, «Quen fixo que»), lo que encaja con la decisión vigente (`contexto.md` §2). En ningún sitio se afirma una revisión humana | — |
| Autoría y créditos | **Cumple, con dos frases que corregir** | El apartado «Como está feito» acredita la voz (Proxecto Nós/USC, Apache-2.0), el texto (Claude, «Ningunha persoa os revisou») y el conxuro | (a) «Imaxes … revisadas por unha porta automática» da a entender que pasaron la revisión, y 35 de 162 no la pasaron: decir el número o arreglar los planos. (b) La lista de ambientes es incorrecta (sección 5). (c) Opcional: nombrar el modelo de imagen y su licencia. (d) D4: pedir permiso a Nós/USC sigue pendiente (`docs/HANDOFF.md` §5.4). La licencia no lo exige; es decisión del promotor |
| Conxuro: solo el primer verso y con autor | **Cumple** | Solo «Mouchos, curuxas, sapos e bruxas.» (0:01-0:04). Autor y año a las 0:10-0:19 y en la descripción («primeiro verso, de Mariano Marcos Abalo (1967), obra rexistrada»). En el cierre (27:29) se nombra el conxuro sin recitarlo | Es una cita breve, con autor, dentro de un comentario [S] |
| Etiqueta de contenido alterado o sintético | **Pendiente: la pone una persona al subir** | YouTube exige declararlo cuando el vídeo «Generates a realistic scene that didn't actually occur» o «Alters footage of a real event or place» (https://support.google.com/youtube/answer/14328491). Aquí hay escenas realistas del siglo XVII y lugares reales (Santiago, Vilalba, Cangas). Se marca en YouTube Studio, en Attributes → «AI use» → Yes. Que lo diga la descripción no sustituye a la etiqueta; a quien no lo declara de forma reiterada YouTube le puede retirar contenido o sacar del Programa de Partners | Marcarla al subir |
| Licencias | **Cumple** | Voz: Apache-2.0 (https://huggingface.co/proxectonos/Nos_StyleTTS2-Brais-GL). Imagen: SDXL-Lightning, «openrail++» (https://huggingface.co/ByteDance/SDXL-Lightning), sobre SDXL base 1.0 con la CreativeML Open RAIL++-M: «Licensor claims no rights in the Output You generate», más las restricciones de uso del Attachment A (https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/LICENSE.md). Entre ellas está «To provide medical advice», y el guion trata las hierbas como costumbre, no como consejo (`veredictos/guion-r2.md`). La puerta usa Florence-2 y CLIP (MIT) y MediaPipe (Apache-2.0), que no se distribuyen. El ambiente es código propio y no hay música | — |
| Descripción | **Cumple, salvo (a) y (b)** | Título de 95 caracteres (YouTube admite 100 [S]), resumen fiel al guion, 28 fuentes con URL y aviso de «contido sintético» | Las dos frases de arriba |
| Capítulos | **Cumple** | 9 capítulos desde 0:00, en orden, todos de más de 10 s, con los mismos tiempos que los rótulos y `qa.md`. YouTube pide que el primero sea «00:00», al menos tres y de 10 s como mínimo (https://support.google.com/youtube/answer/9884579) | Escribir «00:00» por prudencia [S: «0:00» suele funcionar] |
| Subtítulos | **Cumple** | `subtitulos.gl.srt` y pista en el MP4; la puerta de sincronía, en verde | Subir el SRT a YouTube como galego |
| Vetos de imagen (`contexto.md` §8.5) | **Cumple casi** | No hay narices ganchudas, verrugas, sombreros de pico, escobas, autos de fe ni capirotes. El plano 7 (0:27) roza «llamas sobre personas» y «caldero» | El material no trae miniatura. Cuando se haga, aplicar los vetos y no partir del plano 7 |
| Personas reales | **Cumple** | Mariano Marcos Abalo y los investigadores se citan con fuente; las personas del XVII salen de los archivos; el Feijoo dibujado por IA queda cubierto por la etiqueta | — |
| Monetización: «contenido inauténtico» | **Riesgo del canal, no de este vídeo** | YouTube no monetiza «AI-generated content made with generic or unoriginal templates giving the impression of mass production» (https://support.google.com/youtube/answer/1311392). Este episodio aporta investigación propia con fuentes; una serie con la misma plantilla y la misma voz podría leerse así [S] | Vigilarlo al hacer serie |
| QA automática | **No pasa: NON PUBLICABLE, 12/13** | Falla `imaxes_revisadas`: 127 de 162 planos aprobados | Se resuelve con los arreglos de la sección 7 |

## 7. Veredicto

| Pieza | Frente a la referencia | Frente a la ronda anterior | Por qué |
|---|---|---|---|
| **Imagen** | **PIERDE**, por poco | **GANA**, sin cerrar la carencia | A ciegas empata en la suma (21-21) y elegí la referencia ≈ 55/45 por la misma razón que en la ronda 1: allí la gente hace cosas. Frente a la ronda 1 visual, mejoran la luz y el arco hacia el sueño, sobra menos fuego, desaparecen los clichés de meiga y el gancho enseña la premisa con personas. Pero sigue habiendo luz eléctrica y arquitectura inglesa, y 4 planos bloquean (sección 2) |
| **Guion y gancho** | **GANA** | **GANA** (frente al r2, GANA ajustado) | El gancho saca un 4/5, con dos hechos verdaderos en 35 s y tres bucles pagados. La zona de dormir es más tranquila que la de la referencia y la veracidad es muy superior. Se aplicó la lista cerrada del r2; queda su mismo residuo, el «dossier anotado» de 6:27 a 11:36 |
| **Voz y embudo** | **GANA en el embudo** (por medidas; la voz no se oyó) | **GANA** | Ritmo 157 → 114,5 palabras/min, plano de 5,2 → 16,2 s y sonoridad −16,5 → −19,8 LUFS, sin saltos. La referencia no está hecha para dormir y su retención es plana desde el minuto 7 (`gauntlet2/referencia.md`). Frente a la muestra del Gauntlet 2 (voz uniforme a 131 palabras/min, WER 0,037; `docs/APRENDIZAJES.md`, `contexto.md` §3): embudo real y WER 0,031 |
| **Sonido** | **Sin veredicto posible**: no se oyó ninguna de las dos | **GANA** (por medidas) | Ambiente por escena (D13, D14) en lugar de la lluvia continua que el promotor oyó como ruido blanco. En la simulación de la pieza SON la monotonía bajó del 93 % al 9-11 %; aquí, voz limpia el 38,7 % del tiempo y ningún salto del ambiente. Pendiente: pico real de −0,1 dBTP |

### Global: **no se puede publicar tal cual; sí con arreglos**

El texto, la voz medida, el sonido medido y el cumplimiento están listos o casi. Lo que impide publicar es la imagen:
cuatro planos con objetos del siglo XX o XXI, en momentos marcados (un rótulo de capítulo, el cierre y 15 s de
cocina con bombilla y radiador). En un canal que se defiende por el rigor ante un público galego que conoce su
historia (`gauntlet2/referencia.md` §4), eso es lo primero que se comentaría. A eso se suma la etiqueta de contenido
sintético, que solo puede marcar una persona en YouTube Studio. Coste estimado de los arreglos 1-3 [S]: 11 planos
× hasta 4 intentos × ≈ 100 s por intento en esta CPU (`docs/APRENDIZAJES.md`), ≈ 1,2 h como mucho, más el remontaje y
la QA (≈ 67 + 31 min según `qa.md`). Después hay que volver a mirar la hoja de detalle.

**Arreglos antes de publicar** (los ficheros de imagen están en `$SCRATCH/longo/w/imaxes_graduadas/`):

1. **Sustituir los 4 planos que bloquean** y mirarlos antes de montar:
   - 10:34-10:50, plano 84 (`083-5779b492-3.png`): bombilla y radiador. Prompt sin ventana, con la luz de la lareira y
     con negativos `light bulb, radiator, lamp, window`.
   - 22:49-23:03, plano 133 (`132-a8a95fcc-0.png`, fondo del rótulo del capítulo VII): farolas. Un valle oscuro bajo
     la luna, sin edificios ni luces.
   - 30:41-31:02, plano 161 (`160-32b10266-0.png`): casa colonial con apliques. Un primer plano de la lluvia goteando
     del borde de un tejado de lousa, sin ventanas.
   - 5:51-6:01, plano 56 (`055-93ec6c81-0.png`): maleta de ruedas. Una maleta de cartón llevada a mano, con negativos
     `wheels, trolley, rolling suitcase`.
2. **Sustituir 7 planos que molestan en momentos marcados**, en el mismo remontaje:
   - 0:20, plano 5 (`004-983abd46-0.png`): «Vilalba, 1617» con casas inglesas.
   - 2:54, plano 31 (`030-ef658184-0.png`): fregadero con grifos.
   - 6:39, plano 61 (`060-879e4f8a-1.png`): la catedral de Santiago inventada. Unos soportales de granito con lluvia,
     sin monumento.
   - 7:32, plano 67 (`066-1eb7df19-4.png`): la anciana sonriente mientras se narran los azotes.
   - 12:09, plano 91 (`090-c464f180-1.png`): la cocina con apliques que abre la zona de dormir.
   - 25:57, plano 145 (`144-f4f740ab-4.png`): llamas vivas al dormir. El libro cerrado que pedía el prompt.
   - 28:25, plano 153 (`152-179e853a-0.png`): tejado con el penacho incandescente.
3. **Bajar el pico real a ≤ −1 dBTP** en ese mismo remontaje. `qa.md` mide −0,1 dBTP, con los picos en el gancho
   (0:09-0:39). Hay que limitar el pico real (por ejemplo, a −1,5 dBTP) antes de codificar y volver a medir con
   `ebur128=peak=true`.
4. **Corregir `video/descricion.txt`:**
   - Que la revisión de imágenes fue automática y cuántos planos no la pasaron (o el número nuevo tras los arreglos).
   - Los ambientes reales: choiva, lume, auga, mar, aldea, noite, campás y murmurio; sin vento.
   - El primer capítulo como «00:00».
   - Opcional: «Imaxes: SDXL base 1.0 + SDXL-Lightning (CreativeML Open RAIL++-M)».
5. **Al subir el vídeo, en YouTube Studio**, cosas que solo puede hacer una persona:
   - Marcar «AI use: Yes» (contenido alterado o sintético).
   - Subir el SRT en galego.
   - Hacer una miniatura que respete los vetos de `contexto.md` §8.5 y no salga del plano 7.
   - Antes de publicar, enviar el correo de permiso a Nós/USC que pide la decisión D4.

**Mejoras para el siguiente episodio:**

1. **Ningún rechazo al aire sin mirarlo.** Si un plano agota sus intentos, que el pipeline se pare y saque una hoja de
   rechazos para elegir (agente o persona), en vez de quedarse con «el mejor». Además, añadir a la puerta lo que se
   escapó aquí: bombilla, radiador, farolas, apliques de porche, maleta de ruedas, fregadero, peluche, gorro de lana,
   bombín, sombrero vaquero, maletín, guirnaldas de luces y postes de farola. Florence ya lo escribió en varios casos:
   «briefcase» (17 y 24), «sink» (31), «teddy bear» (34), «beanie» (35), «string lights» (80) y «light poles» (123).
2. **Que salga lo que se pide.** 36 planos llevan el aviso «falta». Hay que calibrar la comprobación `clave` (CLIP) en
   vez de apagarla, y escribir la lista de planos con lo que SDXL sí dibuja: una sola acción en plano cerrado, como las
   manos que amasan, sellan o curan de los planos 13, 18, 79 y 126, mejor que composiciones de dos personas con objetos.
3. **Una Galicia reconocible.** Salieron casas inglesas o nórdicas en 5, 23, 29, 33, 68, 75, 77, 134 y 161, y el par
   CLIP «casas británicas» solo frenó 4. Hacen falta imágenes de referencia o semilla (D15) para granito, lousa, pazo y
   aldea, y no nombrar monumentos reales sin una referencia.
4. **El guion despierto.** Una sola atribución por caso y una línea de escena para abrir cada caso en 6:27-11:36
   (`veredictos/guion-r2.md`). En el gancho, condensar en una frase el minuto institucional de 0:55-1:25.
5. **El final del embudo.**
   - Decidir la cola de lluvia de 30-60 min (`contexto.md` §8.6) o un episodio más largo.
   - Que la lista de planos no pida fuego en la zona de dormir.
   - Hacer una escucha humana del episodio entero (voz y mezcla) antes de publicar. Es la única prueba del embudo que
     falta.

---
**Quién hizo qué.** Todo lo de este documento lo hizo Claude (agente tribunal) el 01-10-2026:
- la comparación a ciegas;
- la revisión a ojo de las 162 imágenes y de las hojas de detalle;
- las medidas de luz y sonido, con scripts propios (PIL, numpy, scipy; sin modelos y sin ffmpeg);
- la lectura de los textos;
- la consulta de las fichas de licencia y las páginas de ayuda de YouTube citadas.

Es automático (pipeline): la QA de `longo.py` (`qa.md`, `qa.json`), la puerta de imágenes con Florence-2 y CLIP, y las
puertas de texto. **Ninguna persona ha visto ni oído el episodio.** Una persona tendría que verlo y oírlo entero,
marcar la etiqueta en YouTube Studio, enviar el correo a Nós/USC y decidir si se publica.
