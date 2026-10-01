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
  el final suena sereno o triste (`voz/informe.md` §4). Esa escucha no consta.

**El final.** El vídeo acaba a los 31:22. Los vídeos del género duran 1-4 h: *Relatos al Oído*, 2 h 01 min;
*Sleepless Historian*, 2-4 h (`veredictos/guion-r1-formato.md`, `gauntlet/investigacion/retornos.md`). Quien siga
despierto al terminar se encuentra con la reproducción automática del siguiente vídeo, que puede ser cualquier cosa
[S: depende de la configuración de cada usuario]. La cola de 30-60 min de lluvia sobre lousa de `contexto.md` §8.6
sigue sin decidir.
