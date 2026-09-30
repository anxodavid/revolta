# Biblia visual de "Cousas de Galiza para durmir" (Gauntlet 3, ronda 1)

Autor: agente director de arte e ingeniero de imagen (Claude), 30-09-2026. Documento de trabajo en castellano; los
prompts van en **inglés** (SDXL y CLIP se entrenaron en inglés). Nadie la ha revisado; se apoya en lo que dijo el
crítico visual del Gauntlet 2 (`gauntlet2/veredictos/video-r1.md`, `video-r2.md`, `video-r3.md`), en el storyboard
de la referencia (*Historia Desconocida*, https://youtu.be/_lnOveSTjWA, 220 miniaturas de 320x180, fuera del repo) y
en las pruebas de esta ronda (`aprendizajes/visual.md`).

**Para quién.** Para el agente que escriba la lista de planos del episodio (~130-160 prompts, uno por plano de
`planos.json`) y para quien toque `imaxes.py` o `revisor.py`. Cada entrada de la lista:

```json
{"n": 12, "prompt": "medium shot of ...", "tipo": "plano_medio", "luz": "lit only by firelight, deep black shadows",
 "negativo": "orange roof tiles", "movemento": "zoom_in", "son": "lume"}
```

Solo `n` y `prompt` son obligatorios. `tipo` (sección 3) se recomienda siempre. `luz` es opcional: si falta y el
prompt no trae ninguna palabra de luz, el código pone la luz por defecto de la fase. `negativo` (1-3 conceptos
separados por comas) no se usa para generar (SDXL-Lightning va sin CFG y no admite prompt negativo), sino para
**revisar**: la puerta de CLIP rechaza la imagen si se parece a esos conceptos. `movemento` es el Ken Burns
(`zoom_in`, `zoom_out`, `pan_left`, `pan_right`, `pan_up`).

`son` (decisiones D13 y D14 del promotor, `contexto.md` §7): el ambiente sonoro va **por escena**. Las reglas son de
la pieza SON y mandan: **`plan-de-negocio/gauntlet3/son/guia-son.md`**. Resumen: un tipo del catálogo (`choiva`,
`lume`, `mar`, `vento`, `fonte`, `xente`, `noite`, `aldea`, `campas`) o dos unidos con `+` (p. ej. `lume+noite`, la
segunda capa más baja), o **`limpa`** (voz limpia). Escribir `limpa` siempre que se quiera voz limpia: si el campo
falta, `longo.py` deduce el sonido de las palabras del prompt y puede poner uno. El sonido tiene que **estar en la
imagen** (lluvia solo si se ve llover, lareira solo si se ve fuego); 30-45 % de planos limpios; aviso, reclamo y
datos clave del gancho, limpios. Imagen y sonido se escriben juntos: para un gentío, la imagen sigue siendo de 3-4
figuras lejos o un detalle (sección 5) y el gentío lo pone el sonido (`son: xente`).

**Qué hace el código y no hay que repetir en el prompt:** el estilo común (sección 1) va delante de cada prompt; la
luz por defecto de la fase si el prompt no trae luz; al reintentar, las correcciones según el motivo del rechazo
("dark grey slate roofs, bare granite stone walls" delante si salieron tejados naranjas); la reserva de la fase (un
plano sin personas) si un prompt falla cinco veces o repite arquetipo; la gradación de color por fase.

Comprobar la lista antes de generar (segundos, sin modelos pesados):

    $PY herramientas/pipeline/probas/visual_validar_escenas.py ESCENAS.json --planos TRABALLO/planos.json

## 1. Estilo común

**Modelo:** SDXL base + UNet SDXL-Lightning de 4 pasos a **1344x768** (ver la comparativa en
`aprendizajes/visual.md`). **Estilo** (lo antepone `imaxes.py`, no escribirlo):

    cinematic film still, period drama, photorealistic

Qué significa para quien escribe: fotograma de película de época, no cuadro. Luz con **fuente visible o
justificada** (lume, vela, candil, ventana, puerta, luna, cielo de tormenta), sombras profundas cuando la fase lo
pide, profundidad de campo corta en los primeros planos, texturas reales (granito, lana, madera, musgo). La
referencia gana por eso: interiores con velas, contraluces en ventanas, un pasillo con antorcha, un jardín luminoso,
exteriores fríos de nieve o piedra.

Palabras que **no** se escriben (dan el "aspecto IA" genérico o confunden al modelo): `masterpiece, 8k, 4k, HDR,
trending on artstation, hyperdetailed, ultra realistic, epic, vibrant, neon, fantasy, magical glow, unreal engine`;
ni negaciones (`no people`, `without roofs`): CLIP no entiende la negación y tiende a pintar lo negado. `Galicia,
Spain` se puede usar (en la prueba dio una aldea de piedra verosímil y no la Galitzia centroeuropea), pero no basta:
lo que identifica el lugar se **describe** (sección 4).

## 2. Guion de luz y color por fase

La luz sigue la misma curva que la voz (`curva.py`): gancho vivo y dramático, bajada gradual, final oscuro y quieto.
`imaxes.graduar` aplica además, por plano, el contraste y el brillo de la curva (`contraste` 1,08 → 0,90; `brillo`
1,00 → 0,88), un rango de luminancia por fase y una saturación por fase, suavizados entre planos vecinos (no hay
saltos al cambiar de fase). **No iguala a la media del episodio** (eso aplanó la ronda 3): cada imagen conserva su luz.

| Fase (min aprox.) | Fuentes de luz (rotar, ≥ 3 distintas por fase) | Paleta y contraste | Frases de luz en inglés |
|---|---|---|---|
| **gancho** (0-2) | lume de la lareira, vela, antorcha o facho, noche, tormenta con relámpago, contraluz duro | claroscuro: ámbar contra negro profundo, o azul frío de tormenta; contraste alto | `lit only by firelight, deep black shadows` · `a single candle flame in darkness, chiaroscuro` · `night, flickering torchlight` · `storm clouds, cold flash of lightning, rain` · `harsh backlight from a doorway, silhouette` |
| **transición** (2-8) | día variado: sol de mañana entre la niebla, sol bajo de invierno, cielo cubierto luminoso, rayos por una puerta o ventana, amanecer | verdes de prado, gris del granito, cielos con claros; contraste natural | `morning sunlight through mist` · `low winter sun, long shadows` · `bright overcast daylight, soft shadows` · `shafts of daylight through a doorway` · `dawn light over the hills` |
| **calma** (8-18) | atardecer, lluvia mansa al anochecer, candil en interior, hora azul | cálidos suaves o azul-gris de lluvia; contraste medio-bajo | `warm sunset light, golden hour` · `soft rain, grey-blue dusk` · `warm light of an oil lamp` · `blue hour twilight, first stars` |
| **durmir** (18-final) | luna, brasas, una vela casi consumida, noche estrellada, niebla nocturna | oscuro, poco saturado, contraste bajo; nada de destellos | `pale moonlight, deep blue night, soft and dim` · `faint glow of embers in darkness` · `starry night sky, faint mist, very dim` · `a single dim candle, soft darkness` |

Reglas:
- **Gancho**: ≥ 60 % de los planos de noche, lume, vela, antorcha o tormenta. Es donde se juega el "¿me quedo?":
  caras iluminadas por el fuego, manos y objetos en primer término, contraluces.
- **Transición**: ≥ 70 % de día, con al menos 4 luces de día distintas. Aquí caben los planos generales de lugar.
- **Calma**: se alternan exterior al atardecer o con lluvia e interior con candil; menos personas.
- **Durmir**: nada de relámpagos, fuegos que crecen, caras mirando a cámara ni movimiento brusco; más paisaje,
  bodegón y detalle quieto. El último tercio, casi sin personas.
- Nunca más de **dos planos seguidos con la misma frase de luz**.

## 3. Gramática de planos

Tipos (`tipo`) y la fórmula que añade el código si el prompt no trae ninguna palabra de cámara:

| `tipo` | Fórmula | Uso |
|---|---|---|
| `detalle` | `extreme close-up detail shot of` | un objeto o unas manos: pote, vela, rueca, llave, pan, agua |
| `primeiro_plano` | `close-up of` | **una** cara iluminada por una fuente (fuego, vela, ventana) |
| `plano_medio` | `medium shot of` | una o dos personas haciendo algo concreto |
| `xeral` | `wide establishing shot of` | el lugar: aldea, costa, iglesia, castro, puerto |
| `contraluz` | `backlit silhouette shot of` | figuras o arquitectura contra la luz (puerta, ventana, cielo) |
| `bodegon` | `still life of` | objetos en una mesa o junto al lume, sin personas |
| `paisaxe` | `wide landscape of` | naturaleza sin personas: carballeira, río, monte, mar |

Otras palabras de cámara útiles: `low angle`, `high angle`, `over-the-shoulder`, `seen through a doorway`,
`reflection in water`, `shallow depth of field`.

Reglas de rotación:
- Nunca dos planos seguidos del mismo `tipo` (salvo `paisaxe` en durmir). En cada bloque de 6 planos, al menos 4
  tipos distintos.
- Reparto orientativo: gancho 35 % detalle y primer plano, 30 % plano medio, 15 % contraluz, 20 % general o
  paisaje; durmir 40 % paisaje, 30 % bodegón y detalle, 30 % resto.
- Una acción concreta por plano (remover el pote, encender una vela, cerrar una puerta, hilar, amasar, mirar al
  mar), no "gente de pie". La referencia gana porque cada plano hace algo.
- **Personas en pantalla** (con el tope de la sección 5: una a tres): en el gancho y la transición, **≥ 70 %** de los
  planos con alguien haciendo algo (o sus manos); en calma, ≥ 50 %; en durmir, ≤ 30 % (paisaje, bodegón, detalle).
  El crítico ciego de la ronda 1 del Gauntlet 2 dio la victoria a la referencia porque en nuestra hoja "8 de 12
  fotogramas eran paisajes o B-roll vacío"; en la referencia hay personas en ~14 de cada 16 (storyboard).

**Topes por arquetipo** (los cuenta la puerta de CLIP en todo el episodio, `revisor.ARQUETIPOS`; además, dos planos
del mismo arquetipo tienen que estar al menos a 5 planos de distancia):

| Arquetipo | Tope (fracción del episodio; ≈ en 130 planos) |
|---|---|
| figuras con capa alejándose de espaldas por un camino (el que el crítico vio 3-4 veces) | 3 % (≈ 4) |
| castillo o torre en un otero, lejos | 3 % (≈ 4) |
| grupo de pie en fila | 4 % (≈ 6) |
| calle de aldea con gente | 5 % (≈ 7) |
| persona sentada junto al fuego | 6 % (≈ 8) |
| bosque con niebla sin personas | 6 % (≈ 8) |
| manos en primer plano | 6 % (≈ 8) |
| retrato en primer plano | 8 % (≈ 11) |

## 4. Iconografía galega

SDXL no conoce las palabras gallegas: hay que **describir** el objeto. Poner lo que identifica el lugar (granito,
lousa) **al principio** del trozo de lugar, porque el modelo pesa más lo primero.

**Lista positiva** (usar; en inglés tal cual):

| Qué | Cómo pedirlo |
|---|---|
| granito | `grey granite stone walls`, `rough granite blocks`, `moss-covered granite` |
| lousa (tejado de pizarra) | `dark grey slate roofs` (en la montaña de Lugo y Ourense; en la costa la teja era de barro oscuro y con musgo: pedirla como `weathered dark brown clay tiles covered with moss`, nunca "red" ni "orange") |
| hórreo | `a long narrow granite granary raised on stone pillars, with a small cross on the roof` |
| cruceiro | `a tall granite wayside cross on a stepped stone base` |
| palloza | `a round stone house with a conical thatched straw roof` |
| lareira con pote | `an open stone hearth at floor level with an iron pot hanging from a chain, smoke-blackened walls` |
| escano, lar | `a wooden high-backed bench beside the hearth` |
| carballeira | `an ancient oak grove with thick mossy trunks` |
| souto | `old chestnut trees with huge hollow trunks` |
| costa atlántica | `rugged Atlantic coast, dark granite rocks, rough grey sea`, `a small fishing harbour with wooden boats` |
| carro de bois | `an ox cart with solid wooden disc wheels pulled by two golden-brown oxen` |
| muíño | `a small stone watermill beside a stream` |
| castro | `the ruins of round stone houses of an Iron Age hillfort` |
| igrexa | `a small Romanesque granite church with a bell gable` |
| pazo | `a granite manor house with a stone coat of arms` |
| paleiro | `a conical haystack built around a wooden pole` |
| corredoira | `a sunken lane between mossy stone walls, oak trees` |
| ropa (s. XV-XIX, rural) | `wool cloak`, `a cape made of straw` (coroza), `wooden clogs` (zocos), `dark wool headscarf`, `long dark wool skirt`, `linen shirt`; ajustar a la época del tema |
| luces | `a small iron oil lamp` (candil), `a straw torch` (facho), `a tallow candle`, `a horn lantern` |
| queimada | `a clay bowl with blue flames of burning spirits` |
| paisaje | `green meadows and dry-stone walls`, `misty hills`, `a river with an old stone bridge` |
| vacas y bueyes | `golden-brown cattle` (rubia galega), no toros de lidia |

**Lista negativa** (no pedirla y ponerla en `negativo` cuando el plano la roce: aldea, campo, costa, carro):
- cipreses, olivos, palmeras, eucaliptos (en Galicia desde el s. XIX: anacrónicos antes), viñas en espaldera,
  chumberas, cactus, agaves, paisaje seco o amarillo;
- tejas de barro **naranja** brillantes, muros **encalados** o blancos, fachadas de estuco mediterráneas, balcones
  de hierro, ventanas de cristal (según la época);
- carros con **ruedas de radios** (el carro del país tiene rueda maciza) y carros tirados por caballos en el campo;
- castillos de cuento, catedrales góticas francesas, armaduras completas de caballero en escenas rurales;
- clichés "celtas": kilt, tartán, gaita escocesa (tres roncos; la gallega tiene uno), druidas de túnica blanca,
  trisqueles luminosos, nudos celtas;
- meigas de Halloween y estereotipos (vetos del crítico del tema, `contexto.md` §8): sombrero puntiagudo, escoba,
  caldero, piel verde, **nariz ganchuda, verrugas**; tampoco autos de fe, capirotes, llamas sobre personas ni partos
  explícitos. La meiga del episodio es curandeira o partera: una mujer mayor corriente, digna, con su ropa de lana;
  poner `negativo: "witch, hooked nose, warts"` en sus primeros planos;
- en **durmir**, nada de intrusiones nocturnas (gatos en la cama, demonios en el camino), calaveras ni torturas;
- multitudes, ejércitos, procesiones largas (ver sección 5); texto, letreros, libros abiertos legibles, mapas.

## 5. Caras, manos y multitudes

- **Como mucho tres personas** por plano (mejor una o dos). Para "la aldea", "la procesión" o "los vecinos": 3-4
  figuras **lejos**, a contraluz o en silueta, o un detalle (velas en fila, pies en el camino, manos). La puerta
  rechaza más de 5 cuerpos (MediaPipe) y las palabras de multitud (Florence-2).
- **Caras**: o **una** cara grande y bien iluminada (primer plano con fuego, vela o ventana: SDXL hace bien una cara
  grande), o figuras lejos, de espaldas o en silueta. Evitar 2-6 caras medianas en el mismo plano: es donde salen
  deformes.
- **Manos**: una acción simple con un objeto (sostener una vela, hilar, amasar, remover el pote, verter agua). Evitar
  apretones de manos, dedos entrelazados, plumas de escribir, agujas, contar monedas, manos que sostienen objetos
  finos. La puerta rechaza manos sin cuerpo y más de dos manos por cuerpo.
- Sin niños (deformidades y sensibilidad) y sin animales en grupo (una o dos vacas, un perro, un gato).
- Sin texto: `a closed leather-bound book`, nunca `open book`, `letter`, `map`, `sign`.

## 6. Plantilla de prompt

    [tipo de plano] of [sujeto concreto + acción], [lugar: 1-2 elementos de la lista positiva], [luz de la fase], [atmósfera]

- **≤ 45 palabras** (≈ 60 tokens). El código añade ~10 tokens de estilo y CLIP corta en 77: lo que pase de ahí no
  existe para el modelo. `visual_validar_escenas.py` avisa de los prompts truncados.
- Lo importante primero: plano, sujeto y acción. La luz, justo después del lugar.
- Concretar: `an old woman in a dark wool headscarf stirring an iron pot` y no `a peasant cooking`.

Ejemplos (uno por fase y tipo; en la hoja de prueba `visual/r1/` hay 16):

| Fase | `tipo` | Prompt |
|---|---|---|
| gancho | `primeiro_plano` | `close-up of an old woman's face lit from below by the open hearth fire, deep wrinkles, dark wool headscarf, smoke, deep black shadows` |
| gancho | `detalle` | `extreme close-up detail of a hand holding a tallow candle in a dark stone corridor, the flame lighting rough granite, darkness around` |
| gancho | `contraluz` | `backlit silhouette of a man in a wool cloak standing in the doorway of a granite house, storm outside, cold flash of lightning, rain` |
| transición | `xeral` | `wide establishing shot of a hamlet of grey granite houses with dark grey slate roofs and a long narrow granite granary raised on stone pillars, morning sunlight through mist` |
| transición | `plano_medio` | `medium shot of a woman in a long dark wool skirt carrying a basket of chestnuts along a sunken lane between mossy stone walls, low winter sun, long shadows` |
| calma | `paisaxe` | `wide landscape of the rugged Atlantic coast at sunset, dark granite rocks, waves breaking, a small stone chapel on the headland, warm low sun` |
| calma | `bodegon` | `still life of a small iron oil lamp, a loaf of rye bread and a clay jug on a rough oak table, warm light of the oil lamp, dark stone wall` |
| durmir | `paisaxe` | `wide landscape of an ancient oak grove at night, thick mossy trunks, mist drifting between the trees, pale moonlight, very dim` |
| durmir | `detalle` | `extreme close-up detail of glowing embers in a stone hearth, an iron pot in shadow, faint red glow, soft darkness` |

## 7. Lo que la puerta revisa (versión 5 de `revisor.py`)

1. Manos sin cuerpo, más de dos manos por cuerpo y más de 5 cuerpos (MediaPipe).
2. Descripción de Florence-2 contra la lista de anacronismos y vetos (ventanas de cristal, tejados naranjas,
   multitudes, texto, fuego grande en exterior...) y, desde esta versión, iconografía mediterránea (cipreses, olivos,
   palmeras, eucaliptos, encalado, estuco, ruedas de radios). El candil (`oil lamp`) y la hoguera pequeña y lejana
   ya no cuentan como fallo; el fuego de la lareira tampoco.
3. CLIP: pares "malo/bueno" (teja naranja/lousa, encalado/granito, ciprés/carballo, olivo/prado, palmera/carballo,
   rueda de radios/rueda maciza, paisaje seco/atlántico, eucalipto/carballeira) en tres recortes de la imagen; los
   conceptos de `negativo`; repetición contra **todas** las imágenes aceptadas del episodio; topes de arquetipos.
   Calibrado con 72 imágenes (`aprendizajes/visual.md`): caza los casos claros (una aldea toscana, un olivar) pero no
   los sutiles (un tejado naranja pequeño y apagado): **el prompt sigue siendo la primera defensa**.

Si un prompt falla por el prompt y no por la semilla (repite arquetipo o imagen dos veces seguidas), el código pasa
directamente a la reserva de la fase: mejor escribir bien el prompt que gastar cinco intentos. Cada intento cuesta
~50 s de generación y ~20 s de revisión en esta máquina.
