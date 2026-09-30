# guion · ronda 1 · crítico B (lingua e veracidade)

Crítico B independiente de la pieza GUION (Claude, agente con perfil de filólogo galego y verificador de hechos con
formación de historiador), 30-09-2026. Juzga `guion/guion-r1.txt` (md5 `661b07eab707de047468ce2b93d00a59`), con
`guion/notas-r1.md` y `guion/porta_texto-r1.json`. **Todas las comprobaciones las hizo Claude** (lectura frase a frase,
`curl` al diccionario de la RAG y al Portal das Palabras, render de la p. 4 del PDF del Arquivo con PyMuPDF, lectura de
las fuentes en caché del dossier y WebFetch/WebSearch para lo que no estaba en él). Ninguna persona ha revisado este
veredicto.

## Veredicto: **PIERDE**

Regla del encargo: gana solo con 0 errores de hecho y ningún error grave de lengua. Hay **5 errores de hecho** (2 graves,
2 medios, 1 leve) y **14 errores de lengua** (ninguno grave; 3 medios que cambian o enturbian el sentido). Se arregla con
una ronda de retoques sin tocar la estructura: todas las correcciones están redactadas abajo y ninguna necesita nombres
ni cantidades nuevos salvo la etimología (H2), que requiere un hecho nuevo en el dossier o quitar la frase.

**Mayor carencia:** la veracidad falla justo donde las puertas automáticas no miran: el guion cuenta como declaración
libre, y como hecho, lo que María Cibreira confesó después de ser torturada, y afirma sin fuente una etimología de
*meiga* (latín *medica*) que la propia Real Academia Galega desmiente (*magicus*).

Lo que sí está bien, y hay que conservar: el cumplimiento de la §8 del contexto (Inquisición "branda" y justicia
ordinaria "moito máis dura", una vez y sin año; María Soliña solo como nombre, juicio y poema; remedios siempre como
costumbre; zona de dormir sin intrusiones), la atribución cuidadosa en casi todo el texto («segundo declarou unha
testemuña… dixera», «segundo esa testemuña, viu»), las citas de Feijoo y de los procesos, que están bien leídas (salvo H1), y un
galego natural y normativo.

## 1. Errores de hecho

Gravedad: **G** grave (falso o mal atribuido en un punto sensible), **M** media (falso o mal atribuido, sin daño
grande), **L** leve. Entre paréntesis, el capítulo del guion (gancho = antes del cap. I).

| # | Frase del guion (capítulo) | Problema | Fuente | Corrección propuesta | Grav. |
|---|---|---|---|---|---|
| H1 | «María Cibreira declarou que exercía o oficio desde había uns doce anos, e que llo ensinara a súa nai, Guiomar Douteiro. Á casa da súa nai acudía moita xente, e ela facíalles curas e menciñas.» y a continuación «E María Cibreira confesou despois de ser torturada.» (cap. II) | **Una confesión bajo tortura contada como declaración libre y como hecho.** El fragmento de los "doce años" y de la madre (folio 26 recto) está en el panel del Arquivo bajo el rótulo «Confesión de María Cibreira despois de ser torturada»; la orden de tormento es el folio 23 recto, anterior. Además el "oficio" es «de tal bruxa y echizera», no el de curandera. El orden del guion (declarou… E confesou despois de ser torturada) hace creer que la tortura vino después, y «Á casa da súa nai acudía moita xente…» es lo que ella confesó, narrado como dato | PDF del Arquivo, p. 4 (comprobado renderizando la página: rótulos «Tortura:» sobre [23 recto] y «Confesión… despois de ser torturada:» sobre [26 recto], [26 verso] y [27 recto]); *GCiencia* 26-01-2026: «torturada para que confesase» | «Despois de ser torturada, María Cibreira confesou que había uns doce anos que exercía o oficio de bruxa e feiticeira, e que llo ensinara a súa nai, Guiomar Douteiro. Contou que á casa da nai acudía moita xente, e que ela lles facía curas e menciñas. Na mesma confesión dixo que as noites de san Xoán…» (y quitar la frase suelta «E María Cibreira confesou despois de ser torturada.») | G |
| H2 | «A etimoloxía máis común fai vir a palabra meiga do latín médica.» (cap. IV) | **Falso.** La Real Academia Galega da *meiga* < latín *magicus* ('máxico'); igual Priberam (pt. *meigo* < *magicus*) y Wiktionary. La frase sale de Galipedia, que la atribuye al CCG, pero el texto del CCG no trae ninguna etimología. El guion la dice sin atribuir y justo antes de citar a la RAG | RAG, Portal das Palabras, «meiga»: «Chegounos a través do latín *magicus, -a, -um* 'máxico', que o tomara do grego» (https://portaldaspalabras.gal/lexico/palabra-do-dia/meiga/); https://dicionario.priberam.org/meigo ; https://en.wiktionary.org/wiki/meiga ; CCG «Meigas» (sin etimología) | «Segundo a Real Academia Galega, a palabra meiga vén do latín magicus, máxico.» Requiere añadir el hecho al dossier (con la URL del Portal das Palabras) para que pase H1 y veracidad; si no, quitar la frase | G |
| H3 | «Para facer o cacho, collían auga de sete fontes, coma nas palabras que María do Barro dicía cando tiña o gando no monte.» (cap. V) | **Lo que dijo un testigo, contado como hecho.** En el cap. I está bien atribuido («Segundo unha testemuña…»), pero aquí se afirma que María do Barro decía esas palabras. El testigo, además, lo sabía de oídas: «oyó dizir y mormurar entre algunas personas vecinas» | PDF del Arquivo, p. 15 ([3 verso]); dossier §5 n.º 16 | «…coma nas palabras que, segundo unha testemuña, dicía María do Barro cando tiña o gando no monte.» | M |
| H4 | «O mesmo Arquivo garda uns trinta procesos por bruxería da xustiza real, que aínda están sen estudar.» (cap. II) | **Dato de 2020 dicho en presente en 2026, y contradicho por el propio guion.** Rodrigo Pousa (2026) estudia los pleitos civiles por brujería y rescató el documento de María Cibreira, que es uno de esos procesos del Arquivo; el guion cita sus hallazgos «nos papeis» | PDF del Arquivo, p. 11 (catálogo de 2020); *GCiencia* 26-01-2026: «documento rescatado polo historiador Rodrigo Pousa Diéguez e datado en 1638 en Pazos de Arenteiro» | «…uns trinta procesos por bruxería da xustiza real, que en dous mil vinte aínda estaban sen estudar.» | M |
| H5 | «Un día, unha veciña estaba á porta debandando, e chegou Ana González… e nese momento a arracada da veciña rompeu en tres anacos.» (cap. I) | **Testimonio contado como hecho.** Es la declaración de la propia vecina (Ana de Robles); el guion solo atribuye la causa («tiña por moi certo»), no el suceso | PDF del Arquivo, p. 9 ([12 vuelto], «Testemuño de Ana de Robles») | «Unha veciña contou que un día estaba á porta debandando… e que nese momento a arracada rompeu en tres anacos.» | L |

### 1.1 Imprecisiones leves (no cuentan como error de hecho)

| # | Frase (capítulo) | Problema | Fuente | Corrección |
|---|---|---|---|---|
| H6 | «O fiúncho ten flores amarelas e un cheiro agradable e doce» (cap. V) | Lo "doce" del diccionario es el sabor, no el olor (heredado del hecho F182) | RAG, «fiúncho»: «de cheiro agradable e gusto doce» | «…flores amarelas, un cheiro agradable e un gusto doce» |
| H7 | «E unha copla antiga di: se arraiar, se arraiará…» (cap. V) | "antiga" no está en la fuente (F200) | Galipedia, «Noite de san Xoán» (la copla, sin fecha ni "antiga") | «E outra copla di:» o «E unha copla di:» |
| H8 | «E Rodrigo Pousa di que a febre das bruxas chegou a Galiza, aínda que sen a histeria doutras partes de Europa.» (cap. II) | Atribución algo forzada: "chegou a Galicia" es de la periodista («Pese a que non cabe dúbida…»); lo que dicen Pousa y Jiménez Esquinas es que la histeria de otras partes "dista do acontecido en Galicia" | *GCiencia* 26-01-2026 | «Segundo o historiador Rodrigo Pousa, a febre das bruxas chegou a Galiza, pero sen a histeria colectiva doutras partes de Europa.» es aceptable; más fiel: «A febre das bruxas chegou a Galiza, pero, segundo Rodrigo Pousa, sen a histeria doutras partes de Europa.» |

### 1.2 Los 25 hechos fuera de la ficha

Verificados uno a uno contra su fuente (cita del dossier y texto de la fuente en caché): F018, F025, F032, F070, F086,
F116, F145, F151, F152, F159, F171, F175, F177, F180, F184, F185, F193, F198, F200, F214, F218, F220, F233, F242 y
F244. **Ninguno está mal usado**, con dos matices leves: F200 (el guion añade "antiga", H7) y F171 (la fuente dice que
amontonaban «diverso material»; "leña" es correcto por el ejemplo de la RAG en «cacharela», pero es una concreción).
F018 es cita del propio Mariano Marcos en *Atlántico* («hai outros cinco ou seis Conxuros…») y F025 lleva bien el
"probablemente" (la fuente dice «xurdiría»).

### 1.3 Comprobado y correcto (lo más delicado)

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

## 2. Errores de lengua

El galego del guion es, en conjunto, **normativo y natural**: la colocación del pronombre átono es correcta en todo el
texto (proclisis tras *que, cando, non, xa, tamén, así, ninguén*; enclisis con sujeto o complemento antepuesto), los
contractos y las formas (*tódalas* en la copla, *ca as*, *afástano*, *han ser*) están bien, y hay giros muy galegos
(«ninguén o deu collido», «non daban alcanzado», «botar a perder», «chegou a vello», «por se acaso», «volveu mirar
para»). Comprobados en el diccionario de la RAG (`curl academia.gal/dicionario/-/termo/busca/<palabra>`): *calmo*,
*sentar* (v. i.), *desconfianza*, *garrido*, *cacho*, *peitear*, *exhalación*, *amorear*, *afumar*, *alcaiote*,
*espreitar*, *bebedizo*, *acervo*, *leitón*, *hoste*, *arraiar* (existe; forma recomendada *raiar*, pero va en una
copla), *emplumamento* (no está), *desenganador* (no está; va como epíteto citado). Ningún error es grave (ninguno
impide entender la frase ni es un barbarismo grueso), pero tres cambian o enturbian el sentido.

| # | Frase del guion (capítulo) | Problema | Corrección | Grav. |
|---|---|---|---|---|
| L1 | «frei Martín Sarmiento defendeu o saber das curandeiras, as meigas, coma o de auténticos médicos e botánicos» (IV) | *coma* es 'igual ca'; aquí el valor es 'en calidade de' (defendió su saber **como** el de médicos auténticos), que pide *como* (DRAG, observación en *coma* y *como*: «Tratáronnos coma escravos / como escravos»). La fuente (CCG) dice «como». Con *coma* parece que Sarmiento defendió a la vez el saber de las curandeiras y el de los médicos | «…defendeu o saber das curandeiras, as meigas, como o de auténticos médicos e botánicos.» | M |
| L2 | «O terceiro tomo, de mil setecentos vinte e nove, dedicoullo ao abade e ao convento de Samos.» (VI) | Concordancia del clítico de complemento indirecto: el CI es plural (*o abade e o convento*), así que el clítico es *lles* (*llelo*), no *lle* (*llo*). Viene del hecho F213 | «O terceiro tomo, de mil setecentos vinte e nove, dedicouno ao abade e ao convento de Samos.» (sin duplicar el CI; más fácil para la voz que *dedicoullelo*) | M |
| L3 | «Uns veciños dicían que unha das acusadas fixera morrer as súas becerras e os seus leitóns, porque estaban rifados con ela.» (III) | Ambigüedad al oído: *súas/seus* remite al sujeto más próximo (*unha das acusadas*); se entiende que mató sus propias crías | «Uns veciños dicían que unha das acusadas lles fixera morrer as becerras e os leitóns, porque estaban rifados con ela.» | M |
| L4 | «Algúns procesos acabaron en condenas de desterro, azoutes ou emplumamento e vergonza pública.» (II) | *emplumamento* no está en el DRAG (sí *emplumar*); pasa LanguageTool/hunspell solo porque está en el dossier | «Algúns procesos acabaron en condenas de desterro, de azoutes ou de saír emplumadas á vergonza pública.» | L |
| L5 | «Tamén escribiu que a Hueste, que nalgúns lugares din que é de bruxas, era unha fábula…» (VI) | *Hueste* es la palabra castellana de Feijoo, dicha como si fuera galega (*hoste* en el DRAG solo es 'exército'). Hay que marcarla como palabra de él | «Tamén escribiu que o que el chamaba a Hueste, e que nalgúns lugares tiñan por cousa de bruxas, era unha fábula nacida de luces e exhalacións acesas.» | L |
| L6 | «dicía unhas palabras, unhas caladas e outras en voz alta» (I) | «dicir palabras caladas» choca al oído; la fuente dice «callando y otras que se oían» | «…dicía unhas palabras, unhas en voz baixa e outras que se oían.» | L |
| L7 | «exercía o oficio desde había uns doce anos» (II) | Construcción pesada, calcada de «desde hacía» | «había uns doce anos que exercía o oficio» (ver H1) | L |
| L8 | «O gato non o puideron coller: ninguén o deu collido, e escapou…» (I) | Dice dos veces lo mismo | «O gato ninguén o deu collido: escapou por un burato da porta.» | L |
| L9 | «Foi entre mil cincocentos setenta e catro e mil setecentos, e só levou unha muller á fogueira.» (gancho) | Dos sujetos implícitos distintos en la misma frase (*foi* = o procesamento; *levou* = a Inquisición) y falta «por bruxería» (el hecho F035 dice «acusada de bruxería»): suelta, la frase se puede oír como que la Inquisición de Santiago solo quemó a una persona por cualquier delito | «Foi entre mil cincocentos setenta e catro e mil setecentos. E por bruxería só levou unha muller á fogueira.» | L |
| L10 | «Tito Freire creou a tarteira de barro con patas das queimadas de hoxe.» (VII) | Genitivo forzado | «…creou a tarteira de barro con patas na que hoxe se adoita facer a queimada.» (redacción de F026) | L |
| L11 | «O Arquivo do Reino de Galicia abre a súa exposición…» / «Aquela exposición mostrou…, en dous mil vinte» (VIII) | Presente y pasado para la misma exposición | «O Arquivo do Reino de Galicia abría a súa exposición…» | L |
| L12 | «Son estas: mouchos, curuxas, sapos e bruxas, habelas, hainas, meigas fóra e María Soliña.» (VIII) | Al oído no se sabe dónde acaba cada expresión (todo va separado por comas) | «Son estas: mouchos, curuxas, sapos e bruxas; habelas, hainas; meigas fóra; e María Soliña.» (con pausas largas en la curva de voz) | L |
| L13 | «frade da orde de San Bieito» frente a «san Xoán» (VI y passim) | Mayúsculas incoherentes. El guion escribe *san* en minúscula como tratamiento (criterio defendible: ejemplos del DRAG «cacharela de san Xoán», «Polo san Xoán florean as abelurias»); con ese criterio es «orde de san Bieito»; si se trata como nombre de institución (NOMIG, cap. 4 e), «Orde de San Bieito». Importa en subtítulos y descripción | «…frade da Orde de San Bieito» o «…da orde de san Bieito» | L |
| L14 | «do latín médica» (IV) | Tilde en una palabra latina para forzar la voz: en subtítulos se lee como el galego *médica* ('doutora') | Desaparece con H2; en latín, sin tilde | L |

## 3. Honestidad pública

| Punto | Resultado |
|---|---|
| Aviso | **Literal** («Boas noites. A voz que vas escoitar é sintética, e este texto preparouno un proceso automático.»), igual que la ficha y el contexto §2; empieza en la palabra 91, dentro del primer minuto |
| Fórmula | **Literal** («Isto é Cousas de Galiza para durmir.») |
| Revisión humana | **No se afirma** en ninguna frase (buscado: *revis-, comprob-, investig-, persoa, equipo, abrimos, consultamos…*). El "nós" del narrador («volveremos», «deixamos atrás», «xa escoitamos esta noite») es inclusivo con quien escucha, no afirma trabajo de nadie |
| Conxuro | **Un solo verso y con autor** (Mariano Marcos Abalo, 1967, en el mismo párrafo). El verso vuelve una vez al final como parte de la lista de la exposición del Arquivo; es el mismo verso y el autor ya se dijo dos veces: admisible |
| Poema de Celso Emilio Ferreiro | Solo el libro y el año; ningún verso |
| Citas y atribuciones | Bien en casi todo el texto; mal en H1 (confesión bajo tortura contada como declaración), H3 y H5 (testimonios contados como hechos) |
| Fuera del guion, en la ficha (texto público) | La descripción dice «abrimos os procesos por bruxería que garda o Arquivo do Reino de Galicia». Nadie abrió los procesos: el dossier trabajó sobre el catálogo de la exposición de 2020 (extractos). Propuesta: «contamos o que din os procesos por bruxería que o Arquivo do Reino de Galicia mostrou en dous mil vinte» |

## 4. Mejoras menores

1. **«A meiga non era a bruxa dos contos. Era a que curaba…»** (gancho). Es la síntesis F048, admitida por el dossier,
   pero roza el "Non dicir" n.º 17 (hubo también alcaiotas, adiviñas y acusadas de maleficio, y el propio guion las
   cuenta). Basta un matiz: «a meiga moitas veces non era a bruxa dos contos, senón a que curaba…».
2. **«Case todo galego oíu este conxuro nunha queimada.»** La fuente dice «puido presenciar nalgún momento da súa vida».
   Mejor: «Case todo galego oíu algunha vez este conxuro nunha queimada.»
3. **«A mesma fonte, a mesma noite, e dúas maneiras de mirala.»** Es una inferencia: la fuente no dice a qué fueron las
   mujeres a la fonte da Nogueira. Como contraste retórico vale, pero no debe sonar a explicación de por qué fueron.
4. **Imprecisiones de §1.1** (H6 fiúncho, H7 «copla antiga», H8 atribución a Pousa): corregirlas cuesta una palabra.
5. **«Feijoo contou cinco causas»**: *contar* se oye como 'relatar'; mejor «Feijoo enumerou cinco causas».
6. **«explicar desgrazas que non tiñan explicación»**: repetición; «explicar desgrazas sen motivo coñecido».
7. **Comas delante de *e*** en muchas frases («excomungou as acusadas, e mandou…»): la norma no las pide cuando el
   sujeto es el mismo. Si están para marcar pausas a la voz, mejor que la pausa la ponga la curva de la pieza VOZ.
8. **Aniversario de Feijoo**: «fai trescentos cincuenta anos» solo vale si se publica en torno al 8 de octubre de 2026
   (ya lo anotan las notas).
9. **Pronunciación** (para VOZ): *Hueste*, *Castroviejo*, *Feijoa*, *Henningsen*, *Monterrei*, *arraiar*, *tódalas*.
10. **Aviso**: «A voz que vas escoitar» suena tras 40 s de voz. Es el texto literal obligatorio y no se toca; lo anoto
    solo para el promotor.

## 5. Recomendaciones para la pieza DOSSIER

El guion hereda cinco de sus fallos del dossier; si no se corrigen allí, volverán en la ronda 2:
- **F089-F090** (María Cibreira): decir que es su confesión después de la tortura y que el oficio es «de bruxa e
  feiticeira»; F090 atribuido («contou que…»).
- **F114** (etimología): sustituir por *magicus* con la fuente del Portal das Palabras de la RAG, o quitarlo.
- **F083**: «que en dous mil vinte aínda estaban sen estudar».
- **F213**: «dedicouno ao abade e ao convento de Samos».
- **F182** («gusto doce») y **F200** (sin «antiga»).

## 6. Cómo se comprobó (Claude, 30-09-2026)

| Qué | Cómo |
|---|---|
| Casos del Arquivo (Vilalba, Xinzo, Campo Lameiro, Cibreira, Benita Montero, cifras) | Texto del PDF en caché (`scratchpad/dossier/fontes/ARG-PDF.txt`) y **render de la p. 4** con PyMuPDF para ver a qué rótulo pertenece cada folio |
| Pousa, Henningsen, Jiménez Esquinas; queimada, Castro, Castroviejo | *GCiencia* 26-01-2026 y 13-01-2021 (caché del dossier), leídos enteros |
| Valor Bravo | *El Español* 09-03-2021 (caché), leído entero |
| Conxuro | *Atlántico* 07-02-2022 y *El Correo Gallego* 27-05-2019 (caché), Galipedia «Queimada» |
| Feijoo | *Teatro crítico* II, 5 en filosofia.org (caché): cada cita buscada en el texto; Galipedia «Benito Xerónimo Feijoo» |
| Costumbres de san Xoán, mal de ollo, lareira, hórreo, figa | Galipedia (caché), buscando la frase de cada hecho |
| Etimología de *meiga* | Portal das Palabras (RAG) con `curl`; Priberam; Wiktionary; texto del CCG «Meigas» (sin etimología) |
| Léxico y norma | Diccionario de la RAG con `curl` (palabras listadas en §2); DRAG *coma*/*como*; NOMIG (PDF de la RAG) para mayúsculas y contracciones (*tódalas*, *ca as*) |
| Honestidad | Búsqueda en el guion del aviso, la fórmula y verbos o palabras que afirmen trabajo humano |
