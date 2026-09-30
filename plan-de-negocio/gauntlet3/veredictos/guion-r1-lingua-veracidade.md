# guion · ronda 1 · crítico B (lingua e veracidade)

Crítico B independiente de la pieza GUION (Claude, agente con perfil de filólogo galego y verificador de hechos con
formación de historiador), 30-09-2026. Juzga `guion/guion-r1.txt` (md5 `661b07eab707de047468ce2b93d00a59`), con
`guion/notas-r1.md` y `guion/porta_texto-r1.json`. **Todas las comprobaciones las hizo Claude** (lectura frase a frase,
`curl` al diccionario de la RAG y al Portal das Palabras, render de la p. 4 del PDF del Arquivo con PyMuPDF, lectura de
las fuentes en caché del dossier y WebFetch/WebSearch para lo que no estaba en él). Ninguna persona ha revisado este
veredicto.

> Estado: **borrador parcial** (se guarda por partes por el límite de uso). Veredicto y mayor carencia, al final del
> fichero cuando esté completo.

## 1. Errores de hecho

Gravedad: **G** grave (falso o mal atribuido en un punto sensible), **M** media (falso o mal atribuido, sin daño
grande), **L** leve (imprecisión). Párrafo = número de párrafo no vacío de `guion-r1.txt` (título de capítulo aparte).

| # | Frase del guion (párrafo) | Problema | Fuente | Corrección propuesta | Grav. |
|---|---|---|---|---|---|
| H1 | «María Cibreira declarou que exercía o oficio desde había uns doce anos, e que llo ensinara a súa nai, Guiomar Douteiro. Á casa da súa nai acudía moita xente, e ela facíalles curas e menciñas.» y a continuación «E María Cibreira confesou despois de ser torturada.» (cap. II) | **Una confesión bajo tortura contada como declaración libre y como hecho.** El fragmento de los "doce años" y de la madre (folio 26 recto) está en el panel del Arquivo bajo el rótulo «Confesión de María Cibreira despois de ser torturada»; la orden de tormento es el folio 23 recto, anterior. Además el "oficio" es «de tal bruxa y echizera», no el de curandera. El orden del guion (declarou… E confesou despois de ser torturada) hace creer que la tortura vino después, y «Á casa da súa nai acudía moita xente…» es lo que ella confesó, narrado como dato | PDF del Arquivo, p. 4 (comprobado renderizando la página: rótulos «Tortura:» sobre [23 recto] y «Confesión… despois de ser torturada:» sobre [26 recto], [26 verso] y [27 recto]); *GCiencia* 26-01-2026: «torturada para que confesase» | «Despois de ser torturada, María Cibreira confesou que había uns doce anos que exercía o oficio de bruxa e feiticeira, e que llo ensinara a súa nai, Guiomar Douteiro. Contou que á casa da nai acudía moita xente, e que ela lles facía curas e menciñas. Na mesma confesión dixo que as noites de san Xoán…» (y quitar la frase suelta «E María Cibreira confesou despois de ser torturada.») | G |
| H2 | «A etimoloxía máis común fai vir a palabra meiga do latín médica.» (cap. IV) | **Falso.** La Real Academia Galega da *meiga* < latín *magicus* ('máxico'); igual Priberam (pt. *meigo* < *magicus*) y Wiktionary. La frase sale de Galipedia, que la atribuye al CCG, pero el texto del CCG no trae ninguna etimología. El guion la dice sin atribuir y justo antes de citar a la RAG | RAG, Portal das Palabras, «meiga»: «Chegounos a través do latín *magicus, -a, -um* 'máxico', que o tomara do grego» (https://portaldaspalabras.gal/lexico/palabra-do-dia/meiga/); https://dicionario.priberam.org/meigo ; https://en.wiktionary.org/wiki/meiga ; CCG «Meigas» (sin etimología) | «Segundo a Real Academia Galega, a palabra meiga vén do latín magicus, máxico.» Requiere añadir el hecho al dossier (con la URL del Portal das Palabras) para que pase H1 y veracidad; si no, quitar la frase | G |
| H3 | «Para facer o cacho, collían auga de sete fontes, coma nas palabras que María do Barro dicía cando tiña o gando no monte.» (cap. V) | **Lo que dijo un testigo, contado como hecho.** En el cap. I está bien atribuido («Segundo unha testemuña…»), pero aquí se afirma que María do Barro decía esas palabras. El testigo, además, lo sabía de oídas: «oyó dizir y mormurar entre algunas personas vecinas» | PDF del Arquivo, p. 15 ([3 verso]); dossier §5 n.º 16 | «…coma nas palabras que, segundo unha testemuña, dicía María do Barro cando tiña o gando no monte.» | M |
| H4 | «O mesmo Arquivo garda uns trinta procesos por bruxería da xustiza real, que aínda están sen estudar.» (cap. II) | **Dato de 2020 dicho en presente en 2026, y contradicho por el propio guion.** Rodrigo Pousa (2026) estudia los pleitos civiles por brujería y «rescatou» el documento de María Cibreira, que es uno de esos procesos del Arquivo; el guion cita sus hallazgos «nos papeis» | PDF del Arquivo, p. 11 (catálogo de 2020); *GCiencia* 26-01-2026: «documento rescatado polo historiador Rodrigo Pousa Diéguez e datado en 1638 en Pazos de Arenteiro» | «…uns trinta procesos por bruxería da xustiza real, que en dous mil vinte aínda estaban sen estudar.» | M |
| H5 | «Un día, unha veciña estaba á porta debandando, e chegou Ana González… e nese momento a arracada da veciña rompeu en tres anacos.» (cap. I) | **Testimonio contado como hecho.** Es la declaración de la propia vecina (Ana de Robles); el guion solo atribuye la causa («tiña por moi certo»), no el suceso | PDF del Arquivo, p. 9 ([12 vuelto], «Testemuño de Ana de Robles») | «Unha veciña contou que un día estaba á porta debandando… e que nese momento a arracada rompeu en tres anacos.» | L |
| H6 | «O fiúncho ten flores amarelas e un cheiro agradable e doce» (cap. V) | Lo "doce" del diccionario es el sabor, no el olor (heredado del hecho F182) | RAG, «fiúncho»: «de cheiro agradable e gusto doce» | «…flores amarelas, un cheiro agradable e un gusto doce» | L |
| H7 | «E unha copla antiga di: se arraiar, se arraiará…» (cap. V) | "antiga" no está en la fuente (F200) | Galipedia, «Noite de san Xoán» (la copla, sin fecha ni "antiga") | «E outra copla di:» o «E unha copla di:» | L |
| H8 | «E Rodrigo Pousa di que a febre das bruxas chegou a Galiza, aínda que sen a histeria doutras partes de Europa.» (cap. II) | Atribución algo forzada: "chegou a Galicia" es de la periodista («Pese a que non cabe dúbida…»); lo que dicen Pousa y Jiménez Esquinas es que la histeria de otras partes "dista do acontecido en Galicia" | *GCiencia* 26-01-2026 | «Segundo o historiador Rodrigo Pousa, a febre das bruxas chegou a Galiza, pero sen a histeria colectiva doutras partes de Europa.» es aceptable; más fiel: «A febre das bruxas chegou a Galiza, pero, segundo Rodrigo Pousa, sen a histeria doutras partes de Europa.» | L |

### 1.1 Los 25 hechos fuera de la ficha

Verificados uno a uno contra su fuente (cita del dossier y texto de la fuente en caché): F018, F025, F032, F070, F086,
F116, F145, F151, F152, F159, F171, F175, F177, F180, F184, F185, F193, F198, F200, F214, F218, F220, F233, F242 y
F244. **Ninguno está mal usado**, con dos matices leves: F200 (el guion añade "antiga", H7) y F171 (la fuente dice que
amontonaban «diverso material»; "leña" es correcto por el ejemplo de la RAG en «cacharela», pero es una concreción).
F018 es cita del propio Mariano Marcos en *Atlántico* («hai outros cinco ou seis Conxuros…») y F025 lleva bien el
"probablemente" (la fuente dice «xurdiría»).

### 1.2 Comprobado y correcto (lo más delicado)

- §8.1 del contexto: 92 + 48, una sola a la hoguera, sin año ni nombre; "branda" la Inquisición y "moito máis duros" los
  jueces ordinarios según Valor Bravo (*El Español*: «La jurisdicción ordinaria persiguió y mató a muchas brujas»). En
  ningún sitio dice que Galicia se librara. Cumple.
- María Soliña: juzgada por la Inquisición, pocos datos (CCG), poema en *Longa noite de pedra* (1962), símbolo (CCG).
  Sin quema, sin fechas, sin el asalto, sin versos. Cumple.
- Conxuro: un solo verso, con autor, 1967, Vigo, barco (El Correo 2019: «Fue en esa embarcación donde, en 1967, escribió
  la letra»); «cinco ou seis conxuros» y «unha empresa… sen o nome do autor» (*Atlántico* 2022). Registro 2001. Cumple.
  El verso vuelve una vez al final dentro de la lista de la exposición del Arquivo: es el mismo verso, admisible.
- Queimada: Alonso del Real (1972) dice "imposible" por el alambique medieval (Galipedia); el guion no dice que la
  queimada sea medieval. Castro, "tradición inventada"; González Reboredo, "antropólogo" como en Galipedia; Tito Freire,
  solo la tarteira; Castroviejo y el café, vía Alonso del Real en *GCiencia*. Correcto.
- Feijoo: todas las citas del *Teatro crítico* II, 5 comprobadas en el texto de filosofia.org (hechiceros "no tantos",
  fábulas del vulgo a los libros, "suma desconfianza", cinco causas, labrador romano, brujas más veloces que las águilas
  que no alcanzan un jumento, la vieja de la limosna, ungüento y sueño, "otro extremo vicioso", Hueste = exhalaciones y
  luces). "O frade que dubidaba" es fiel. Galipedia da 1676 en el texto (Wikidata dice 1677 en la ficha lateral; 1676 es
  lo correcto).
- Casos del Arquivo: Dorotea parteira (atribuido, "dixera"), "auga, digo, leite", excomunión (la fuente dice «pan carne
  sal agua ni lumbre»: quitar "carne" es resumir, no citar), Ana González y el gato, Campo Lameiro y la lista, Benita
  Montero (sentencia e inventario). Correctos.
