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
