# guion · ronda 2 · crítico combinado

Crítico de la ronda 2 del guion del Gauntlet 3 (Claude, agente con dos perfiles: operador de canales faceless de historia
y de contenido para dormir, y filólogo galego (RAG) y verificador de hechos). 30-09-2026. No participé en el guion.
Juzgo [`guion/guion-r2.txt`](../guion/guion-r2.txt) (3.983 palabras, md5 `74ee35852a655b502ae3ad3a9c5236ed`, último cambio en el commit 2ce59c6) contra los
veredictos de r1 ([formato](guion-r1-formato.md), [lengua y veracidad](guion-r1-lingua-veracidade.md)), el
[`contexto.md`](../contexto.md) §2 y §8, el [dossier](../dossier/dossier.md) (con la lista "Non dicir", §5) y la ficha
`herramientas/pipeline/temas/meigas-de-verdade.yaml`.

**Qué hizo Claude y qué es automático.** Todo este veredicto lo hizo Claude: la lectura frase a frase, el cotejo de cada
frase con `dossier/feitos.yaml` (273 hechos), la consulta de las fuentes en caché del dossier (PDF del Arquivo,
Galipedia, *Atlántico*), dos consultas en línea (el diccionario de la RAG y la página de Galipedia de O Riós) y los
recuentos con scripts de Python del scratchpad. Ninguna persona lo ha revisado. Las puertas automáticas del guion
(`porta_texto-r2.json`: LanguageTool, H1, veracidad, estilo) están en verde y **no las he vuelto a pasar**. "l. N" es
la línea de `guion-r2.txt`. Los minutos son una estimación [S] con la curva de ritmo de voz del crítico A de r1
(182 → 119 palabras/min), escalada a 30 min. Sin escalar, esa curva da 27,5 min.

## Veredicto: **GANA** (ajustado)

| Condición del encargo | Resultado |
|---|---|
| Sin errores de hecho | **Se cumple.** No hay ninguna afirmación falsa ni contraria al dossier o a su fuente. Hay 6 imprecisiones leves (§2.1): en dos casos, lo que se deduce por el orden de las frases no es verdad (el ritual de la queimada y el día de las hierbas), y en otros dos se cuenta como hecho lo que es testimonio o creencia (la arracada y las flores). Todas se arreglan con una sustitución de la lista cerrada (§4) |
| Sin errores graves de lengua | **Se cumple.** Ninguno es grave. Hay 4 medios, todos de referencia (sujeto implícito o anáfora que el oído atribuye a otra cosa), y 9 leves (§2.2) |
| Puntos mayores de r1 resueltos | **Se cumple, con un residuo.** Resueltos los 5 errores de hecho y los 14 de lengua del crítico B. Del crítico A están resueltos el gancho cargado, el cierre con datos, la duración, Feijoo con calendario y la promesa del título. "Zona de dormir enciclopédica" y "dossier anotado" quedan **resueltos donde el crítico A situó el daño** (el minuto 1 y la zona de dormir), pero no en el tramo despierto de los minutos 6 a 11 (ver mayor carencia) |

**Por qué "ajustado".** Con una lectura estricta, "dossier anotado" solo está resuelto en parte. Doy GANA por tres
motivos. El crítico A de r1 dio ese tramo por empatado con la referencia, no por perdido. Su densidad viene en parte de
lo que pidió la ronda 1: el capítulo del conxuro, el caso de Marta de Quián y que se atribuya cada testimonio. Y
bajarla ahora obligaría a reescribir los casos, con riesgo de meter errores nuevos. **Antes de producir hay que aplicar
la lista cerrada del §4**: son 16 sustituciones exactas, que no tocan la estructura ni añaden hechos ni nombres.

**Mayor carencia:** el tramo despierto de los minutos 6:27 a 11:36 sigue siendo un dossier anotado. Tiene 2,0
atribuciones por cada 100 palabras (1,4 en r1; ≈ 0,5 en las dos referencias) y ≈ 1 año por cada 100 palabras (0,5-0,6
en r1). "Segundo" sigue saliendo 15 veces, igual que en r1. Los casos siguen siendo resúmenes de declaraciones sin
escena. El peor momento es 6:27-7:24: Casa Grande de Calo, "foro mixto", 92 y 48, "uns trinta procesos" y "dous mil
vinte", con 7 cantidades en ≈ 140 palabras justo antes de Cibreira. Es el punto de abandono más probable del vídeo. No
bloquea este episodio. Para el siguiente, la plantilla debería citar la fuente una vez por caso y abrir cada caso con
una línea de escena.

## 1. Seguimiento de los veredictos de r1

### 1.1 Crítico B (lengua y veracidad): 5 errores de hecho, 14 de lengua y la honestidad

| # r1 | Punto | Estado | Línea de r2 que lo demuestra |
|---|---|---|---|
| H1 (G) | Cibreira: confesión bajo tortura contada como declaración | **Resuelto** | l. 57: «Despois de ser torturada, María Cibreira confesou que había uns doce anos que exercía o oficio de bruxa e feiticeira.» La frase suelta ya no está, y lo de la madre va como «Contou que…» |
| H2 (G) | Etimología *medica*, falsa | **Resuelto** (se quitó) | Ya no hay etimología (`grep latín\|medica\|magicus`: 0). El dossier la corrigió a *magicus* (F114) y la añade a "Non dicir" (n.º 18) |
| H3 (M) | Las sete fontes contadas como hecho | **Resuelto** | l. 123: «coma nas palabras que, segundo unha testemuña, dicía María do Barro» |
| H4 (M) | "uns trinta procesos… aínda están sen estudar" | **Resuelto** | l. 55: «que en dous mil vinte aínda estaban sen estudar» |
| H5 (L) | La arracada contada como hecho | **Resuelto en lo esencial** | l. 29: «Outra veciña… contou que un día estaba á porta debandando…». Queda sin atribuir la rotura, en frase aparte, y la veciña se nombra dos veces: sustitución C1 |
| H6 | Fiúncho: "doce" es el gusto | **Resuelto** | l. 115: «un cheiro agradable e un gusto doce» |
| H7 | "copla antiga" | **Resuelto** | La copla "se arraiar" se quitó; l. 135: «Unha copla di:» |
| H8 | Atribución forzada a Pousa | **Resuelto** | l. 53: «A febre das bruxas chegou a Galiza, pero, segundo Pousa, sen a histeria doutras partes de Europa.» |
| L1 (M) | *coma* / *como* (Sarmiento) | **Resuelto** | l. 153: «como o de auténticos médicos e botánicos» |
| L2 (M) | *dedicoullo* (complemento indirecto plural) | **Resuelto** | l. 157: «Ao abade e ao convento de Samos dedicou o terceiro tomo» |
| L3 (M) | "as súas becerras", ambiguo | **Resuelto** | l. 67: «fixera morrer as becerras e os leitóns deles» |
| L4 | *emplumamento* | **Resuelto** | l. 55: «de saír emplumadas á vergonza pública» |
| L5 | *Hueste* | **Resuelto** (se quitó) | — |
| L6 | "palabras caladas" | **Resuelto** | l. 23: «unhas en voz baixa e outras que se oían» |
| L7 | "desde había" | **Resuelto** | l. 57: «había uns doce anos que exercía» |
| L8 | El gato, dos veces | **Resuelto** | l. 27: «Ninguén o deu collido: escapou por un burato da porta.» |
| L9 | "Foi entre…" con dos sujetos | **Resuelto** | l. 13: «En máis dun século de procesos, segundo o mesmo Arquivo, a Inquisición de Santiago só levou á fogueira unha muller acusada de bruxería.» |
| L10 | Genitivo forzado (tarteira) | **Resuelto** | l. 45: «na que hoxe se adoita facer a queimada» |
| L11 | *abre* / *mostrou* (exposición) | **Resuelto** | l. 155 usa «mostrou». Aun así, pido quitar ese párrafo (C13, por el sueño) |
| L12 | La lista de expresiones | **Resuelto** (se quitó) | — |
| L13 | Mayúsculas de *san* | **Resuelto** | l. 141: «da orde de san Bieito», coherente con «san Xoán» |
| L14 | *médica* con tilde | **Resuelto** (se quitó con H2) | — |
| Honestidad | Ficha: «abrimos os procesos» | **Resuelto** | Ficha, `descricion`: «contamos o que din os procesos por bruxería que o Arquivo do Reino de Galicia mostrou en 2020». El aviso y la fórmula son literales (l. 5 y l. 7; puerta `aviso_literal` y `formula_literal`) |
| Mejoras 1-2 | "moitas veces"; "algunha vez" | **Resuelto** | l. 15: «a meiga moitas veces non era a bruxa dos contos»; l. 1: «oíu algunha vez» |
| Mejoras 5-6 | "contou cinco causas"; "explicación" repetido | **Resuelto** | l. 147: «Feijoo buscou as causas»; l. 97: «desgrazas sen motivo coñecido» |
| Mejora 8 | Aniversario que caduca | **Resuelto** (se quitó) | l. 141 solo da el año |
| Recomendaciones al DOSSIER | F089-F090, F114, F083, F213, F182, F200 | **Resuelto** | `dossier.md` §4.8 |

### 1.2 Crítico A (retención y dormir)

| # r1 | Punto | Estado | Línea de r2 que lo demuestra |
|---|---|---|---|
| Mayor carencia | "Dossier anotado, no narración" | **Parcial** | Resuelto en el gancho (1,7 atribuciones y 0,7 años por cada 100 palabras; r1: 2,0 y 1,3) y en la zona de dormir (0,7 atribuciones; un solo año absoluto en ≈ 2.200 palabras, l. 141). **Peor** en el tramo despierto de 1:50 a 11:36 (2,0 atribuciones y 1,0 años por cada 100 palabras; r1: 1,4 y 0,6). Ver mayor carencia |
| 1 | Pagar la promesa del título con el oyente despierto | **Resuelto** | Capítulo "O conxuro do barco" en 4:35-6:27 (l. 39-47); la preparación de la queimada pasa al cierre (l. 161-163). La frase de aviso de la l. 9 («E hai un motivo polo que moita xente pensou…») promete menos que la que se propuso («como chegou a parecer tan antigo»), y su pago en la l. 41 es plano: sustitución C3 |
| 2 | Gancho de 0:41 a 1:42 sin cifras amontonadas | **Resuelto** | l. 13: una sola idea, sin 92/48 y atribuida a Valor Bravo. l. 11 añade un buen avance («unha veciña que velou esperta… un gato que ninguén deu collido») |
| 2 | Bucle de la lista apuntando a "dúas maneiras de mirala" | **Parcial** | l. 17 sigue prometiendo «por que a fixeron» (respuesta floja: «porque eran moitas», l. 69), pero añade «volveremos a esa fonte». El remate «dúas maneiras de mirala» llega en l. 71, a las 9:31, dentro de la ventana 8-10 de §8.3 |
| 2 | Frase de hoja de ruta | **Resuelto** | l. 17: «Esta noite imos coñecer as meigas de verdade: as dos papeis dos xuízos, as da lareira e as das fontes.» |
| 3 | Zona de dormir: de ficha a escena | **Resuelto en lo esencial** | l. 85: «Entremos nunha cociña de aldea, á noitiña…»; se quitaron las definiciones de orballo, lousado, candea, "Meigas fóra" y las tres entradas de diccionario. Quedan: la fecha de san Xoán (l. 111), las fichas botánicas (l. 115), la tona (l. 129) y el ciclo del maíz (l. 105) |
| 3 | Permiso para dormir en la ventana de los minutos 8-10 | **Parcial** | l. 85, «non tes que lembrar nada do que escoites», al abrir la escena, pero a las ≈ 11:36 (≈ 10:40 sin escalar) |
| 4 | Cierre sin datos y el doble de largo | **Resuelto en lo esencial** | El Quixote pasa a l. 81 (11:13); la lluvia ocupa ≈ 270 palabras de imagen pura (l. 167-175). La exposición del Arquivo y el gato **no salieron: se movieron** a l. 155 (25:28, zona de dormir): sustitución C13 |
| 5 | Duración: ≈ 4.000 palabras | **Resuelto** | 3.983 palabras (entre 27,5 y 30 min según la curva). Marta de Quián está en l. 31-33 (3:24-4:02). San Xoán va en orden tarde → noche → amanecer (l. 113-137) |
| 6 | Feijoo sin calendario | **Resuelto** | Solo «mil seiscentos setenta e seis» (l. 141). Fuera el aniversario, los volúmenes, la fecha de la muerte, *Hueste* y la polémica galego-portugués. Queda la dedicatoria a Samos (l. 157), que el crítico A daba por prescindible (no bloquea) |
| 7 | Capítulo del tribunal abierto con un lugar; Benita Montero reordenada | **Resuelto** | l. 51 abre con el Hotel Compostela y explica «foro mixto» en la misma frase; l. 61: la baraja encontrada, y después la baraja al cuello |
| 7 | Transiciones habladas | **Resuelto** | l. 39 «E agora, o conxuro do barco», l. 67 «E por fin…», l. 81, l. 85, l. 141 «Deixamos atrás as fogueiras…», l. 161 «Volvamos á cociña…» |
| 8 | Menos "segundo" y menos Pousa | **Parcial** | Pousa pasa de 9 a 6 y se usa «o mesmo historiador» (l. 75); "segundo" sigue en 15 y "testemuña" pasa de 7 a 8 |
| 9 | Voz: Henningsen una vez, Reboredo, pronombres de l. 27, gato, copla "se arraiar", "abrancazadas" | **Resuelto** | Henningsen solo en l. 101; «na fonte da Nogueira» sin Reboredo (l. 69); l. 29 sin ambigüedad; la copla y "abrancazadas" se quitaron |
| 9 | "ata a emenda de quen o escribía" | **No aplicado** (leve) | l. 23 sigue con «No papel quedou escrita ata a corrección» y se entiende. Opcional |
| 10 | Línea de comunidad | No aplicado; **correcto** | Necesita el visto bueno del promotor |
| Señales para B | l. 11 sin atribuir; "Case todo galego oíu" | **Resuelto** | l. 13 (Valor Bravo) y l. 1 («algunha vez») |

## 2. Errores nuevos (pasajes nuevos o reescritos)

### 2.1 Hechos: 0 errores y 6 imprecisiones leves

Cotejé cada frase con su hecho de `feitos.yaml` y, cuando había duda, con la fuente en caché. **Ninguna frase dice algo
falso ni contrario al dossier.** No aparece ninguna de las 18 afirmaciones de "Non dicir". Se cumple el §8 del contexto:
- 8.1: el contraste de la Inquisición se dice una vez y sin año (l. 13).
- 8.3: el conxuro y Dorotea van de 0:00 a 0:32, el aviso a las 0:32, el reclamo a las 0:38, la Inquisición a la 1:01, la
  curandeira a la 1:18 y el bucle a la 1:28. Cibreira sale a las 7:24, con empatía.
- 8.4: los casos con nombre acaban a las 9:51, y María Soliña va solo como nombre y poema.
- Derechos: un solo verso del conxuro y ningún verso de Celso Emilio.

Las 6 imprecisiones:

| # | Frase (l., min) | Problema | Fuente | Corrección |
|---|---|---|---|---|
| P1 | «Así arde, pouco a pouco, ata que se esgota case todo o alcohol. Un deles ergue cun cazo o líquido en chamas…» (l. 163, 26:31) | **Orden imposible**: primero se apaga el alcohol y después alguien levanta el líquido en llamas y dice el conxuro. En el ritual, el conxuro se dice mientras arde, hacia el final | F030 y F031 («o conxuro recítase cara ao final»), F269 | C16 (se invierte el orden) |
| P2 | «Na véspera de san Xoán apáñanse as herbas… Había quen as apañaba no campo para vendelas ao día seguinte…» (l. 113, 16:14) | Por el orden de las frases se entiende que las recogían en la víspera y las vendían el día 24, cuando ya no sirven. La fuente dice que las recogían el 22 y las vendían el 23 | Galipedia, «Herbas de san Xoán», que cita a Eladio Rodríguez: «se recogen en el campo, generalmente la antevíspera… o sea el día 22, para venderlas al siguiente día» | C8 |
| P3 | «E cando Ana González saía polas portas do curral, volveu mirar para a veciña, e nese momento a arracada da veciña rompeu en tres anacos.» (l. 29, 2:59) | Resto de H5: la rotura va en una frase aparte, sin «contou». La causa sí está atribuida | PDF del Arquivo, p. 9 ([12 vuelto], testimonio de Ana de Robles); F063 | C1 (casi literal de F063) |
| P4 | «Tamén poñían cardos ou espadanas: as flores protexían polo seu recendo, os cardos polas espiñas…» (l. 137, 21:33) | Creencia contada como hecho: el narrador afirma que las flores protegían de las meigas. El §2 del contexto pide contar lo legendario como leyenda | F258 («Para protexer as casas das bruxas poñíanse…») | C11 («crían que…») |
| P5 | «porque o alambique chegou na Idade Media» (l. 43, 5:22) | Falta adónde: el alambique es antiguo, lo que llegó en la Edad Media fue su uso en Galicia | Galipedia, «Queimada» (Alonso del Real: «a destilación do augardente en Galicia non pode ser anterior á introdución do alambique… a partir do século XII ou XIII»); F020 | C4 |
| P6 | «naceu en poucos anos un ritual que parece de sempre» (l. 47, 6:15) | Desde los años cincuenta (González Reboredo), pasando por 1955 (Tito Freire), hasta 1967 (el conxuro) van unos veinte años, no "pocos" | F024, F026, F002 | C5 («en poucas décadas») |

**Comprobado y correcto** (lo más delicado de lo nuevo):

| Frase (l.) | Comprobación |
|---|---|
| l. 11, «E alí hai máis» | "Alí" es el Arquivo. El proceso de Xinzo lo abrió la justicia del conde de Monterrei (F057), pero el Arquivo lo guarda y lo expuso (F271) |
| l. 13, «En máis dun século de procesos» | De 1574 a 1700 van 126 años (F034) |
| l. 27, el gato | La fuente dice que el gato «se llegara a la cama» (PDF, p. 9). El guion lo omite, bien para §8.4. «contaba» está bien atribuido |
| l. 41, la empresa | *Atlántico*: «empezó a circular anónimo por toda Galicia, razón por la cual se asimiló un origen popular» |
| l. 55, los trinta procesos | PDF, p. 11: «uns 30 procesos xudiciais contra mulleres levados a cabo pola xustiza real, aínda sen estudar». p. 14: «Todas as reas son mulleres» |
| l. 69, la lista | PDF, p. 7 ([29 recto]): «allí las abían visto y reconosçido y las abían escripto en una memoria por ser mucho número dellas». Los «dos demonios» del [30 recto] quedan fuera, bien |
| l. 105, «O millo non agroma ata o comezo do verán» | Casi literal de Galipedia, «Hórreo», donde se contrapone al trigo y al centeno. Es un dato de divulgación y lo doy por bueno |
| l. 131, «no Riós» | Correcto: el nombre oficial es **O Riós desde 2026** (Galipedia, ficha del concello: «Nome oficial O Riós dende 2026; Riós ata 2026») |
| l. 141-143, Feijoo | Galipedia: «pouco antes de facer os 14 anos ingresou na Orde de San Bieito, polo que tivo que renunciar aos seus dereitos como morgado. Ordenouse como sacerdote no mosteiro de San Xulián de Samos». «renunciou á herdanza para facerse frade» es una paráfrasis fiel |
| l. 153, «o galego non era un dialecto do castelán» | Es parte de F231, sin la polémica galego-portugués (lo pidió el crítico A) |
| l. 161, «uns poucos grans de café» | F029. Es un guiño a la «herexía» de Castroviejo (l. 47) |

### 2.2 Lengua: ningún error grave, 4 medios y 9 leves

El galego de r2 sigue siendo normativo y natural. En todo lo nuevo:
- los pronombres átonos van bien colocados («que o afastan», «Préndeselle lume», «déixao caer», «mirábano bailar», «para
  que a protexesen», «Aos meniños poñíanlles», «Así o escribiu»);
- las contracciones son correctas («cara á cheminea», «ca as aguias», «ao carón»);
- las dos palabras dudosas que busqué en el diccionario de la RAG existen: *comisar*, «Quitar [algo] a alguén en nome do
  Estado», y *agromar*, «botar gromos»;
- hay giros orales muy buenos: «quedabas preso no asento», «ninguén o deu collido», «non daban alcanzado», «chegou a
  vello», «por se acaso».

No hay barbarismos. Los problemas son de **referencia** (a quién apunta un sujeto implícito o un "esa") y de **costura**
entre dos hechos del dossier puestos seguidos, justo lo que las puertas automáticas no ven.

| # | Frase (l., min) | Problema | Corrección | Grav. |
|---|---|---|---|---|
| N1 | «…as patas do escano podían apoiarse nela, e así quedaban sentados máis preto do lume.» (l. 89, 12:05) | Anacoluto: el sujeto de «quedaban sentados» es, por gramática, «as patas» (femenino). El oyente tiene que reconstruir «a xente» | C7 | M |
| N2 | «Foi sempre de saúde delicada, con catarros frecuentes…» (l. 157, 25:47) | Sujeto implícito tras un párrafo cuyo sujeto es «o Arquivo do Reino» (l. 155). Si se quita ese párrafo (C13), quedaría Sarmiento. Feijoo no se nombra desde la l. 145 | C14 | M |
| N3 | «Á mañá lavábase a cara con esa auga verde e recendente…» (l. 133, 20:43) | «esa» apunta al último agua nombrada, la flor da auga de la fuente (l. 129-131), que no es verde. El agua de las hierbas (el cacho) está en la l. 123, cuatro párrafos antes | C10 | M |
| N4 | «Hoxe é un símbolo do sufrimento do pobo…» (l. 63, 8:30) | Tras «un poema no libro Longa noite de pedra, publicado…», el sujeto implícito se puede oír como el poema o el libro | C6 (F110 literal) | M |
| N5 | «…a xente comía sardiñas, cachelos e broa de millo. Comían sardiñas á brasa, bebían viño…» (l. 117, 17:28) | "Sardiñas" dos veces seguidas, y "arredor do lume" / "arredor da fogueira": costura de F172 con F257 | C9 | L |
| N6 | «Así arde, pouco a pouco… déixao caer pouco a pouco no pote» (l. 163) | "Pouco a pouco" en dos frases seguidas (va con P1) | C16 | L |
| N7 | «volveu mirar para a veciña, e nese momento a arracada da veciña…» (l. 29) | "Veciña" dos veces en la misma frase (va con P3) | C1 | L |
| N8 | «Segundo contou el mesmo… El mesmo contaba…» (l. 39, 4:35) | "El mesmo" dos veces en un párrafo | C2 | L |
| N9 | «Por que moita xente o cría anónimo ten unha resposta sinxela.» (l. 41, 5:04) | Una interrogativa indirecta como sujeto pesa al oído. Además, "moita xente… anónimo" sale dos veces en dos frases (y una tercera en la l. 9). La nueva frase cierra de forma explícita el bucle abierto en la l. 9 | C3 | L |
| N10 | «Deixamos atrás as fogueiras, e imos agora cun frade…» (l. 141, 22:07) | «Ir con» de presentador («vamos con…», calco del castellano). En galego, «ir con alguén» es acompañarlo | C12 | L |
| N11 | «Volvamos á cociña do principio…» (l. 161, 26:10) | El vídeo no empezó en la cocina, sino en un barco y en Vilalba. La cocina es del minuto 11 | C15 | L |
| N12 | «O sabugueiro, pola súa banda, dá flores pequenas e brancas.» (l. 115) | Conector de registro escrito en plena zona de dormir | **Sin cambio**: quitarlo deja una frase de 7 palabras, por debajo del mínimo de 8 de la puerta de estilo | L |
| N13 | «Segundo el, a caza de bruxas…» (l. 77) | Tras «…lle comeran a viña ao outro», «el» puede oírse un instante como el vecino. El cambio de párrafo casi lo resuelve | **Sin cambio**: «Segundo Pousa» sería el séptimo Pousa | L |

Opcional, fuera de la lista: en la l. 35, «segundo Rodrigo Pousa, historiador,» esquiva el falso positivo de
LanguageTool, pero «segundo o historiador Rodrigo Pousa» dentro de la frase también pasa (dossier §3) y suena más natural.

## 3. Retención y sueño

- **Gancho, de 0:00 a 1:50: engancha.**
  - De 0:00 a 0:32 da dos datos verdaderos y sorprendentes: el conxuro es de 1967, con autor y barco, y está Dorotea con
    el «poldro bravo». El aviso llega a las 0:32, dentro de los 40 s.
  - De 0:41 a 1:50 va una idea por frase, con solo dos años absolutos en todo el gancho.
  - El mejor añadido de r2 es el avance de la l. 11: «unha veciña que velou esperta unha noite. E un gato que ninguén deu
    collido». Siguen la Inquisición en una sola frase, la curandera, la lista y la hoja de ruta.
  - Punto flojo: la l. 9, justo después de la fórmula, abre la pregunta pequeña (por qué se creyó anónimo) con una frase
    abstracta. C3 hace al menos que el pago de la l. 41 se oiga como tal.
- **Hasta el minuto 10: se sostiene, con un bache.**
  - De 1:50 a 4:35, tres casos con picante y sin violencia: Vilalba, Xinzo y Lalín.
  - De 4:35 a 6:27 se paga la promesa del título con el oyente despierto: es el gran arreglo de r2.
  - Cibreira, Benita Montero y Soliña van de 7:24 a 8:53, y el bucle se cierra de 9:13 a 9:51 con «dúas maneiras de
    mirala».
  - El bache está de 6:27 a 7:24 (la mayor carencia), con 2,0 atribuciones por cada 100 palabras en todo el tramo.
- **Zona de dormir, de 11:36 a 30:00: sirve.**
  - Abre con el permiso para dormir y el paseo de «Entremos». Siguen la lareira, el mal de ollo como costumbre y el hórreo.
  - San Xoán va en orden estricto: tarde, noche y amanecer. Feijoo es amable y con humor, sin calendario.
  - El cierre «Chove na lousa», de 26:10 a 30:00, es lo mejor del guion. La queimada se apaga, y quedan ≈ 270 palabras de
    imágenes ya oídas (lousa, brasas, escano, pote, gramalleira, lacenas, forno, gando, hórreo, cabazas, herbas, sete
    fontes, orballo), «xa non tes que lembrar nada» y la candea.
  - Quedan bolsas de ficha:
    - tres autoridades en un minuto de mal de ollo, de 13:37 a 14:26 (Mariño Ferro, Risco y Henningsen);
    - el ciclo del maíz (15:16);
    - la fecha de san Xoán (15:51);
    - las fichas botánicas (16:49);
    - la tona (19:51);
    - la exposición del Arquivo con el gato de Xinzo (25:28), que C13 quita.
  - "Amodo" sale 10 veces. Como marca de sueño, vale.
- **Duración.** Con la lista aplicada quedan 3.952 palabras (31 menos). Son 27-30 min con la curva de r1, dentro de
  25-35. Hay que confirmarlo con el render de la pieza VOZ.

## 4. Lista cerrada de correcciones mínimas (aplicar antes de producir)

Son **16 sustituciones exactas**. Cada «actual» aparece **una sola vez** en `guion-r2.txt` (lo comprobó un script). La
lista no añade nombres propios, cantidades ni hechos: solo usa palabras y nombres que ya están en el guion o en el
dossier. Las frases nuevas con nombre propio (C1, C4, C6 y C14) son copia casi literal de F063, F020, F110 y F233,
así que H1 y la veracidad deberían seguir en verde. Todas las frases que resultan tienen entre 8 y 25 palabras. **Al
aplicarla, hay que volver a pasar la puerta de texto completa** (LanguageTool, H1, veracidad y estilo).

| C | l. | Motivo | Texto actual → texto nuevo |
|---|---|---|---|
| C1 | 29 | P3, N7 | `E cando Ana González saía polas portas do curral, volveu mirar para a veciña, e nese momento a arracada da veciña rompeu en tres anacos.` → `E contou que, cando Ana González saía polas portas do curral, volveu mirar para ela, e que nese momento a arracada rompeu en tres anacos.` |
| C2 | 39 | N8 | `El mesmo contaba que houbo outros cinco ou seis conxuros daquela época` → `E contaba que houbo outros cinco ou seis conxuros daquela época` |
| C3 | 41 | N9, bucle de la l. 9 | `Por que moita xente o cría anónimo ten unha resposta sinxela.` → `O motivo do que falabamos ao principio é sinxelo.` |
| C4 | 43 | P5 | `porque o alambique chegou na Idade Media.` → `porque o alambique chegou a Galiza na Idade Media.` |
| C5 | 47 | P6 | `naceu en poucos anos un ritual que parece de sempre.` → `naceu en poucas décadas un ritual que parece de sempre.` |
| C6 | 63 | N4 | `Hoxe é un símbolo do sufrimento do pobo, e sobre todo das mulleres.` → `Hoxe, María Soliña é un símbolo do sufrimento do pobo, e sobre todo das mulleres.` |
| C7 | 89 | N1 | `e así quedaban sentados máis preto do lume.` → `e así a xente quedaba sentada máis preto do lume.` |
| C8 | 113 | P2 | `Había quen as apañaba no campo para vendelas ao día seguinte nos mercados das vilas e das cidades.` → `Había quen as apañaba no campo un día antes, para vendelas na véspera nos mercados das vilas e das cidades.` |
| C9 | 117 | N5 | `e arredor do lume a xente comía sardiñas, cachelos e broa de millo. Comían sardiñas á brasa, bebían viño, e cantaban e bailaban arredor da fogueira.` → `e a xente comía sardiñas á brasa, cachelos e broa de millo. Bebían viño, e cantaban e bailaban arredor do lume.` |
| C10 | 133 | N3 | `Á mañá lavábase a cara con esa auga verde e recendente,` → `Á mañá lavábase a cara coa auga das herbas, verde e recendente,` |
| C11 | 137 | P4 | `Tamén poñían cardos ou espadanas: as flores protexían polo seu recendo,` → `Tamén poñían cardos ou espadanas: crían que as flores protexían polo seu recendo,` |
| C12 | 141 | N10 | `Deixamos atrás as fogueiras, e imos agora cun frade que escribiu contra as fábulas de bruxería.` → `Deixamos atrás as fogueiras, e agora imos coñecer un frade que escribiu contra as fábulas de bruxería.` |
| C13 | 155 | Crítico A r1, punto 4; §8.4 | **Borrar el párrafo entero** (y la línea en blanco que lo sigue): `Na súa exposición sobre as meigas, o Arquivo do Reino mostrou o discurso de Feijoo sobre as transformacións máxicas. Púxoo na mesma páxina que o proceso de Xinzo de Limia, o do gato que ninguén deu collido.` → *(nada)*. Es una nota de museo y trae de vuelta la meiga-gato nocturna a las 25:28. El crítico A pidió sacar las dos cosas del final, y se movieron en vez de quitarse |
| C14 | 157 | N2 (necesaria tras C13) | `Foi sempre de saúde delicada, con catarros frecuentes, e aínda así chegou a vello.` → `Feijoo foi sempre de saúde delicada, con catarros frecuentes, e aínda así chegou a vello.` |
| C15 | 161 | N11 | `Volvamos á cociña do principio, que xa está en penumbra.` → `Volvamos á cociña da lareira, que xa está en penumbra.` |
| C16 | 163 | P1, N6 | `Así arde, pouco a pouco, ata que se esgota case todo o alcohol. Un deles ergue cun cazo o líquido en chamas e déixao caer pouco a pouco no pote, mentres pronuncia o conxuro.` → `Un deles ergue cun cazo o líquido en chamas e déixao caer pouco a pouco no pote, mentres pronuncia o conxuro. E así arde un bo anaco, ata que se esgota case todo o alcohol.` |

**No entran en la lista** (no bloquean y no conviene tocarlos ahora):
- l. 9: una promesa más fuerte en el gancho tendría que tener apoyo en la puerta de veracidad del primer minuto.
- l. 111: la fecha de san Xoán; si se quita, la frase siguiente se queda sin sujeto o necesita un hecho nuevo.
- N12 y N13.
- La densidad de atribuciones de los minutos 6 a 11, que es trabajo para la plantilla del próximo episodio.

## 5. Cómo se comprobó (Claude, 30-09-2026)

| Qué | Cómo |
|---|---|
| Seguimiento de r1 | Lectura de los dos veredictos punto por punto y búsqueda de cada frase en `guion-r2.txt` (`grep` y lectura) |
| Hechos | Cotejo frase a frase con `dossier/feitos.yaml` (volcado de los 273 hechos) y con las fuentes en caché de `scratchpad/dossier/fontes/`: PDF del Arquivo (p. 7, 9, 11 y 14), *Atlántico*, Galipedia («Queimada», «Hórreo», «Herbas de san Xoán», «Noite de san Xoán», «Benito Xerónimo Feijoo»). En línea: página de Galipedia de O Riós (nombre oficial desde 2026; la API de Wikimedia devolvió un límite de peticiones y se leyó la página) |
| Léxico | Diccionario de la RAG en línea (`academia.gal/dicionario/-/termo/busca/<palabra>`): *comisar* y *agromar* |
| Minutos y densidades | Script de Python en `scratchpad/critico-guion-r2/`: curva de ritmo de voz del crítico A de r1 (182 → 119 palabras/min) interpolada por palabra y escalada a 30 min [S], y recuento por regex de atribuciones y años absolutos por cada 100 palabras en r1 y r2 (mismos criterios en los dos) |
| Lista cerrada | `subs.py` en el scratchpad: comprueba que cada «actual» aparece una vez, la aplica a una copia (`guion-r2-corrixido.txt`, fuera del repo), cuenta palabras (3.983 → 3.952) y mide la longitud de cada frase resultante (8-25) |
