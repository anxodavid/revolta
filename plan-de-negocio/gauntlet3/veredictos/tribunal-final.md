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

**Destape.** Pendiente: se escribe después de guardar esta sección y leer `clave.txt`.
