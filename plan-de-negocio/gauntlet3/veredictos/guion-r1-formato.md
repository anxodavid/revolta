# guion · ronda 1 · crítico A (retención y dormir)

Crítico A del guion (Claude, agente con perfil de operador de canales faceless de historia hechos con IA y de
productor de contenido para dormir), Gauntlet 3, 30-09-2026. No participé en el guion. Juzgo
[`guion/guion-r1.txt`](../guion/guion-r1.txt) (3.503 palabras) con sus notas [`guion/notas-r1.md`](../guion/notas-r1.md),
contra las dos referencias del §4 de [`contexto.md`](../contexto.md).

**Qué hizo Claude y qué es automático.** Todo este veredicto lo hizo Claude: la lectura, la descarga de los subtítulos
automáticos de las referencias con yt-dlp y los recuentos con scripts de Python del scratchpad. Ninguna persona lo ha
revisado. **La comparación no es a ciegas**: las referencias están en castellano y el guion en galego, así que se
distinguen al leerlas. Los subtítulos de terceros se quedan en el scratchpad y no se suben al repo.

Minutos: los del modelo B de las notas (ritmo medido de la voz; 25,9 min en total), interpolados por párrafo. "l. N" es
la línea de `guion-r1.txt`. HD = *Historia Desconocida*, "Versalles en 1682..." (36 min). RO = *Relatos al Oído*,
"DUÉRMETE CON las Leyendas Más Antiguas y Misteriosas de GALICIA" (2 h 01 min).

## Veredicto: PIERDE (ajustado)

| Tramo | Frente a HD | Frente a RO |
|---|---|---|
| 0:00-0:40, arranque en frío (l. 1-7) | **Gana.** Dos datos verdaderos, concretos y sorprendentes en 32 s: el conxuro es de 1967 y tiene autor, y la parteira decía poder pasarle al hombre los dolores del parto ("saltaría coma un poldro bravo"). HD tarda 5 min en dar el primer dato de lo que promete (el olor y la orina en los pasillos, 5:00-6:00); antes solo hay promesa, preguntas retóricas y contexto general. | **Gana.** RO abre con dos leyendas sin fuente (los soldados cegados por una luz del arca en 1820, los lobos de San Andrés) y una promesa genérica ("Hoy conocerás estas y más leyendas..."). |
| 0:41-1:42 (l. 9-15) | **Pierde.** Tras el aviso llegan 60 s de instituciones, cifras y atribuciones (Arquivo, Real Audiencia, Inquisición, 92, 48, 1574, 1700, Valor Bravo, Pousa), a 182 palabras/min. En ese minuto HD sigue construyendo una sola promesa ("Hay algo sobre Versalles que casi nadie sabe...") en segunda persona y con imágenes. | Empata. RO también se enfría (historia del monasterio desde 1:00), pero en registro narrativo y con paisaje ("entre montes húmedos y praderas cubiertas de niebla"). |
| 1:42-10:00 (l. 19-69) | Empata. El material es mejor: seis casos con nombre y detalles de archivo que ningún competidor tiene ("auga, digo, leite", la arracada en tres anacos, la baralla colgada do pescozo, "maldita a nai que non ensina a súa filla a meigar"). La narración es peor: son resúmenes de declaraciones, con atribución en casi cada frase y sin escena (lugar, luz, hora, tiempo). HD, en cambio, monta escenas ("Es una mañana de enero de 1683... Son las 6 de la madrugada"). | **Pierde en flujo.** RO cuenta una sola historia continua, con suspense y desenlace. El guion encadena casos de 30-60 s y abre el cap. II con "Para entender aqueles papeis, cómpre saber quen xulgaba as meigas. A bruxería era un delito de foro mixto" (l. 33, 3:48), que es el punto típico de abandono. |
| Zona de dormir (8:30-25:53, l. 63-131) | **Gana en calma del contenido.** HD no es de dormir: entre los min 20 y 24 cuenta enemas, fístulas y dientes arrancados. | Mixto. **Gana en calma del contenido**: RO cuenta asesinatos, un envenenamiento con sangre, peste, un cadalso e incendios. **Pierde en registro**: el guion mete definiciones de diccionario, una biografía con fechas y siete nombres nuevos donde RO mantiene un flujo narrativo uniforme. |
| Duración | Pierde: 25,9 min frente a 36. | Pierde: 25,9 min frente a 2 h 01 min. |
| Veracidad | **Gana con mucho.** No encontré nada que suene inventado y no tenga apoyo literal en el dossier. | **Gana con mucho.** La historia de RO de "la mujer de las hierbas de Mondoñedo", ejecutada en 1803 tras un proceso de la Inquisición, suena a leyenda contada como historia [S: no lo he verificado]. |

**Balance.** El guion gana los primeros 40 s y la veracidad. Pierde en lo que más pesa en este formato: el minuto 1, el
registro de la zona de dormir y la duración. Es un borrador fuerte en material y débil en escritura, y con una ronda 2
bien hecha puede ganar a las dos referencias. Es mucho mejor que el guion de la muestra del Gauntlet 2
(`gauntlet2/veredictos/video-r3.md`: "dossier recitado", gancho sin referente, sin picante). Aquí sí hay picante en los
primeros 60 s y un hilo coherente.

**Mayor carencia:** está escrito como un dossier anotado y no como una narración. Casi cada párrafo lleva atribuciones,
años o definiciones de diccionario, con unas tres o cuatro veces la densidad de atribuciones de las referencias. Eso
enfría el gancho a partir del segundo 53 y hace que la zona de dormir sea enciclopédica en vez de envolvente.

## Medidas (Claude, con scripts; aproximadas)

Son recuentos con expresiones regulares sobre el guion y sobre los subtítulos automáticos (`es-orig`) de las
referencias. Como "atribuciones" cuentan en galego *segundo, di que, contou, escribiu, recolleu, advirte...* y en
castellano *según, las crónicas, los registros, escribió, decían, se cuenta...*. Los "años" son años absolutos (en el
guion van en letra).

| Tramo | Palabras/min | Atribuciones por 100 palabras | Años por 100 palabras |
|---|---|---|---|
| Guion, gancho (0:00-1:42) | 182 (voz medida) | 1,8 | 1,4, y dos cantidades más (92 y 48) |
| Guion, 1:42-10:00 | 174-158 | 1,4 (2,1 en el cap. III) | 0,6 |
| Guion, zona de dormir (palabras 1.751-3.503) | 145-119 | 0,8 | 0,7 (1,8 en el cap. VI: 9 años y 3 fechas con día y mes) |
| HD: 0-2 min / 2-10 / 20-30 | 140 / 133 / 140 | 0,0 / 0,5 / 0,3 | 1,1 / 0,4 / 0,5 |
| RO: 0-2 min / 2-10 / 60-75 / 105-121 | 126 / 144 / 143 / 144 | 0,4 / 0,5 / 0,4 / 0,4 | 0,4 / 0,0 / 0,2 / 0,2 |

Otros recuentos del guion: "segundo" aparece 15 veces, "Pousa" 9, "testemuña" 7 y "Arquivo" 5. Los capítulos no se
narran (`longo.py`: "non se narra: vai nun rótulo"), mientras que RO dice en voz alta el título de cada historia.

## Mejoras, por orden de impacto

### 1. Pagar la promesa del título con el oyente despierto (l. 115-121 pasan al minuto 4-5)

- **Problema.** El título vende "por que o conxuro da queimada é de 1967". El gancho da el *qué* a los 10 s, pero el
  *porqué* llega en las l. 117-121, entre el 21:43 y el 23:30, en la fase más lenta de la voz. Es el barco, los amigos,
  los otros cinco o seis conxuros, las copias vendidas sin el nombre del autor, la "tradición inventada", los años
  cincuenta fuera de Galiza y el origen que no es celta. Quien entró por la queimada se va en el minuto 1-2. Quien se
  queda dormido recibe un desmentido ("iso é imposible") y siete nombres nuevos (Castroviejo, Alonso del Real, Xavier
  Castro, González Reboredo, Tito Freire, Eligio y Cunqueiro). Es la duda 3 de las notas, y va contra el espíritu de
  §8.4: los nombres, antes del minuto 10.
- **Propuesta.**
  - Pasar las l. 117-121 (sin la preparación) a un capítulo nuevo, "O conxuro do barco", justo después de "Sete fontes e
    un gato" (≈ 3:50-5:20). Las historias con nombre siguen acabando antes del minuto 10 y el cierre del bucle pasa a
    ≈ 7:40.
  - En la zona de dormir dejar solo la preparación sensorial de la l. 115 (augardente, lapas, "reméxese amodo", luces
    apagadas), sin nombres ni fechas, fundida con el cierre. La llama azul que se apaga "ata que se esgota case todo o
    alcohol" es la mejor última imagen posible: funde a sueño y cierra el círculo con el primer segundo del vídeo.
  - En la l. 1, usar la redacción del propio dossier (F246, "tradición milenaria") para afilar el contraste, y añadir
    una señal para que el espectador sepa que la historia llega pronto:

    > Mouchos, curuxas, sapos e bruxas. Case todo galego oíu este conxuro nunha queimada, e parece levarnos moitos
    > séculos atrás, a unha tradición milenaria. Pero ten autor coñecido, e é de mil novecentos sesenta e sete.
    > Escribiuno Mariano Marcos Abalo, en Vigo, nun vello barco amarrado no porto. E como chegou a parecer tan antigo,
    > tamén o contaremos.

### 2. Gancho de 0:41 a 1:42: una cifra y un nombre por idea, y dentro el mejor dato del guion (l. 9-15)

- **l. 11 (0:53-1:14).** Mete dos cantidades, dos años y dos atribuciones en 21 s a 182 palabras/min, y las cantidades se
  repiten en la l. 35 (4:14). Hay que llevar las cantidades al cap. II y dejar en el gancho solo el contraste:

  > Segundo o mesmo Arquivo, entre mil cincocentos setenta e catro e mil setecentos, a Inquisición de Santiago só levou
  > unha muller á fogueira por bruxería. Para o investigador Diego Valor Bravo, coas meigas a temida Inquisición foi
  > branda, e os xuíces da xustiza ordinaria foron moito máis duros.

  Esto corrige además un matiz para el crítico B. En r1, "Coas meigas, a temida Inquisición foi branda" va sin
  atribuir justo después de "segundo o mesmo Arquivo", así que se oye como si lo dijera el Arquivo. El dossier se lo
  atribuye a Valor Bravo (F039).
- **l. 13.** Hay que traer aquí la etimología, que ahora está en la l. 63 (8:30), enterrada entre definiciones. Es el
  mejor dato para un título "As meigas de verdade":

  > Na Galiza de hai catrocentos anos, a meiga non era a bruxa dos contos. A propia palabra vén, segundo a etimoloxía
  > máis común, do latín médica. Era a que curaba, a que axudaba nos partos, a que sabía de herbas. Rodrigo Pousa,
  > historiador, di que eran figuras apreciadas e necesarias para o pobo.

- **l. 15 (el bucle).** Ahora promete "por que a fixeron", y esa respuesta es floja: "porque eran moitas" (l. 51). El
  remate fuerte es el de la l. 53, "A mesma fonte, a mesma noite, e dúas maneiras de mirala", así que el bucle tiene
  que apuntar ahí:

  > E hai unha lista. Unha noite de san Xoán, en Campo Lameiro, uns veciños foron espreitar a fonte e apuntaron nunha
  > lista as mulleres que viron alí. Que foran facer aquelas mulleres á fonte, e por que os veciños viron outra cousa,
  > contarémolo antes de que chegue o sono.

- **Después de la fórmula (l. 7).** Falta una frase de hoja de ruta, como la de RO ("Hoy conocerás estas y más
  leyendas..."), que guíe al oyente. Es un recurso clásico del contenido para dormir:

  > Esta noite imos coñecer as meigas de verdade: as dos papeis dos xuízos, as das fontes e as da lareira.

### 3. Zona de dormir: de ficha a escena (l. 63, 73-75, 79, 87, 91 y 129)

Los temas de la zona de dormir son los buenos: lume, herbas, orballo, fontes y lareira. Lo que falla es el registro, por
dos motivos:

- **Definiciones de palabras que el público galego ya conoce.**
  - "Orballo chámase á humidade do aire que, co frío da noite, se condensa en pingas pequenas" (l. 87).
  - "O lousado é o tellado dunha casa cuberto de lousas, e a lousa é unha pedra gris ou negra..." (l. 129).
  - "a candea, esa vela de cera cunha torcida por dentro que servía para alumar": es la última frase del vídeo (l. 129).
  - "o hórreo, onde se garda o millo" (l. 75).
  - "A noite de san Xoán é a noite entre os días vinte e tres e vinte e catro de xuño" (l. 79).
  - "Meigas fóra é, aínda hoxe, unha expresión de sobra coñecida en Galiza" (l. 91).
  - Tres entradas de diccionario seguidas en la l. 63: meiga, menciñeira y parteira.

  Para este público suena a manual para extranjeros, y para dormir una definición es una pequeña tarea mental, no una
  imagen. Sospecho que algunas están para llegar al mínimo de 8 palabras por frase de la puerta de estilo ("Xa se pode
  apagar a candea" tiene 6). Si es así, la frase se alarga con una imagen, no con una definición.
- **Descripción de cartel de museo.** Las l. 73-75 son una lista de "X era Y, que servía para Z".

**Propuesta.** Quitar las definiciones y dejar la imagen. Convertir las l. 73-75 en un paseo lento con los mismos hechos
del dossier. HD usa "Imagina" 8 veces, pero la puerta de estilo del canal veta "imaxina", así que el paseo se hace con
"entremos":

> Entremos agora nunha cociña de aldea, á noitiña. A cociña era a estancia máis importante e acolledora da casa: alí
> recibían as visitas, comían e facían faladoiros. Na lareira arde o lume, sobre a pedra do lar. A carón do lume está o
> escano de castiñeiro, onde a xente sentaba a quentarse ou a matar o tempo. O pote colga da gramalleira, e nas lacenas
> da parede gárdanse os alimentos. Fóra, o hórreo descansa sobre os seus pés, e o aire corre polas súas aberturas.

Hay que adelantar también la invitación de la l. 79 ("non tes que lembrar nada do que escoites") al principio de esta
escena (≈ 10:00, donde empieza la fase de calma). Así el permiso para dormirse llega dentro de la ventana de §2
(minutos 8-10) y no en el 12.

### 4. El cierre "Chove na lousa": sin datos y el doble de largo (l. 125-131)

- **Problema.** Los últimos 2:30 traen:
  - un desmentido, "non aparece no Quixote de Cervantes" (l. 125, 23:30);
  - una nota institucional sobre la exposición, "en dous mil vinte, polo Día Internacional da Muller", con "seis
    procesos" (l. 127, 24:14);
  - una recapitulación con "o gato que ninguén deu collido": la meiga-gato de noche, a 45 s del final;
  - un solo párrafo de calma (l. 129), que además empieza y acaba con una definición.

  En un vídeo para dormir, los últimos 2-3 min tienen que ser lo más previsible: nada nuevo, solo imágenes que vuelven.
  Ninguna referencia sirve de modelo: RO acaba con su última historia y música, y HD pide la suscripción. Aquí se puede
  ganar a las dos.
- **Propuesta.**
  - Llevar "non aparece no Quixote" al final del cap. III (≈ 9:00, todavía despiertos) o quitarlo. "habelas, hainas" se
    queda como frase familiar y cálida.
  - Quitar la exposición (l. 127) y sacar el gato de la recapitulación. Quedan "a parteira, as sete fontes e a lista da
    fonte".
  - Fundir aquí la preparación sensorial de la queimada (mejora 1).
  - Alargar la lluvia hasta ~200-250 palabras con imágenes que ya se han oído (chuvia, lousa, orballo, brasas, escano,
    pote, gando na corte, hórreo, sete fontes, candea). Principio de ejemplo, con frases de 8-25 palabras y sin
    definiciones:

    > Agora chove sobre as lousas do tellado da casa. É unha chuvia miúda e mansa, coma o orballo. Na lareira quedan as
    > brasas, quentes e calmas, e o escano xa está baleiro. Na mesa, a queimada xa non arde, porque se esgotou case todo
    > o alcohol. Na corte, o gando dorme, e no hórreo repousa o millo. Lonxe, as sete fontes seguen correndo na
    > escuridade. A casa descansa baixo a chuvia, e xa non tes que lembrar nada. E agora, amodo, xa se pode apagar a
    > candea.
    >
    > Boas noites.

### 5. Duración: ≈ 500 palabras netas más, sobre todo al final (el guion está en el suelo)

- **Cifras.** Son 25,9 min con el modelo B (voz medida): 0,9 min por encima del mínimo y 4 min por debajo del objetivo.
  Las mejoras 2, 3, 4 y 6 quitan ~200 palabras de cifras y definiciones, casi todas en la zona lenta (≈ −1,5 min).
  Hay que apuntar a **≈ 4.000 palabras** (≈ 30 min con B). El modelo A diría ~40 min, así que hay que confirmarlo con un
  render real de voz antes de cerrar la ronda 2. El rango de 3.300-3.900 palabras de §2 se calculó a 131 palabras/min;
  la curva medida va de 182 a 113 (media ≈ 135) y conviene recalcularlo con ella. Lo decide el orquestador.
- **Dónde añadir.**
  - **Marta de Quián (Lalín, 1611)** en el cap. I, antes del minuto 10 (F139-F143; las notas, §7.1, ya ven sitio con
    B). Es el picante que pidió el promotor y no tiene violencia. Queda fuera la "cabeza de muerto".

    > En mil seiscentos once, na parroquia de Palio, en Lalín, a Real Audiencia procesou a Marta de Quián, que tiña fama
    > de meiga feiticeira. Unha veciña queixábase de que o leite das súas vacas se lle derramaba. Marta díxolle que
    > faría unha menciña para que as meigas non llo derramasen nin llo levasen. Outra testemuña declarou que Marta lle
    > dixera que, por catro ou cinco reais, faría que unha moza deixase de mirar para un home. Para iso pedía terra da
    > pegada que el deixaba ao pisar, e cabelos da moza, dos que quedaban no peite.

  - **El cierre largo** (mejora 4): +150-200 palabras a ~115 palabras/min, ≈ 1,5 min.
  - **San Xoán en orden estricto "desde a tarde ata o amencer"**, como promete la l. 79. Ahora va y viene: la l. 85
    vuelve a la víspera, la l. 93 salta del amanecer a la moura de noche y la l. 95 vuelve al amanecer y acaba en A
    Lanzada. Orden propuesto:
    - tarde: la leña y las hierbas que se cogen la víspera;
    - noche: cacharelas, sardiñas, saltos, el ganado ahumado, las hierbas al orballo y la moura de la fonte;
    - amanecer: flor da auga, lavarse la cara, el sol que baila y los ramos en las puertas.

    Si el dossier da para más, se añaden una o dos costumbres suaves. El orden previsible también ayuda a dormir.
  - Si el render sigue por debajo de 28 min, se completa con la cola de lluvia (§8.6, la decide el promotor) o con más
    pausa en la curva, nunca con relleno.

### 6. Feijoo sin calendario (l. 99-111, 16:48-20:54)

- **Problema.** Hay 9 años y 3 fechas con día y mes en 508 palabras, dentro de la zona de dormir: unas 3 fechas por
  minuto. Es el capítulo con más números de todo el guion, donde las referencias ponen 0,2-0,5 años por cada 100
  palabras. La guía de estilo del canal en el Gauntlet 2 (prompt del guion, commit 6bacfd9) pedía "como moito unha data
  absoluta por minuto, sempre redondeada". Las ideas sí sirven, porque son suaves, algo graciosas y cierran bien el
  tema: las fábulas que van de la aldea a los libros y vuelven, el labrador romano, la vieja que quería la fama por la
  limosna, las brujas más rápidas que las águilas que no alcanzan un burro y el vuelo soñado. Lo que sobra es el
  calendario.
- **Qué quitar o cambiar.**
  - l. 99: fuera "O oito de outubro de dous mil vinte e seis fai trescentos cincuenta anos que naceu". En dos semanas
    deja viejo un vídeo que debe durar años (notas, §7.9). El aniversario va en la descripción y en el post de
    comunidad. La fecha de nacimiento se queda en "en mil seiscentos setenta e seis".
  - l. 101: fuera "desde mil setecentos nove", "oito volumes publicados entre..." y "O terceiro tomo, de mil setecentos
    vinte e nove, dedicoullo ao abade e ao convento de Samos", que no aporta nada al relato.
  - l. 103: "No segundo tomo, de mil setecentos vinte e oito, hai un discurso..." pasa a ser:

    > Nun discurso sobre a maxia, Feijoo escribiu que había feiticeiros, pero non tantos como cría o vulgo.

  - l. 105: dice "Feijoo contou cinco causas" y luego da tres. O se dan las cinco, o se dice "Feijoo buscou as causas de
    que houbese tantas fábulas de bruxería".
  - l. 111: la frase "Xa no primeiro tomo, en mil setecentos vinte e seis, defendera..." pasa a "Defendeu tamén que as
    mulleres tiñan a mesma capacidade de entendemento ca os homes". La muerte, sin fecha:

    > Foi sempre de saúde delicada, con catarros frecuentes, e aínda así chegou a vello e morreu en Oviedo.

- **Opcional.**
  - l. 109: "a Hueste, que nalgúns lugares din que é de bruxas" trae de vuelta la procesión nocturna a la zona de dormir,
    aunque sea para desmentirla, y "Hueste" es una palabra castellana que la voz puede leer mal. Mejor quitarla.
  - l. 111: "o galego e o portugués eran unha mesma lingua" es verdad, pero en Galiza es un tema de polémica. Si se busca
    calma, basta con "e non un dialecto do castelán".

### 7. El cap. II y las transiciones habladas (l. 33-45 y la primera frase de cada capítulo)

- **l. 33 (3:48).** Abre con jerga ("delito de foro mixto") justo cuando terminan las primeras historias. Hay que abrir
  con el lugar concreto, y poner una sola vez, en la l. 35, las cantidades que salen del gancho:

  > En Santiago, onde se levantou o Hotel Compostela, estivo a última sede da Inquisición, a Casa Grande de Calo,
  > derrubada en mil novecentos trece. Pero a Inquisición non era a única que xulgaba as meigas: tamén as podían xulgar
  > a xustiza civil e a da Igrexa.

  Sobra también la fecha de 1574 de esta línea, que ya da el gancho.
- **l. 43 (Benita Montero).** Conviene invertir el orden: la baraja encontrada prepara el golpe y la baraja al cuello
  lo remata.

  > Aínda en mil oitocentos vinte e seis, en Santiago de Compostela, a Real Audiencia condenou a adiviña Benita Montero.
  > Na súa casa atoparan unha baralla vella, un rosario e un escapulario cunha figa de acibeche. A pena foi saír do
  > cárcere emplumada e montada nunha besta, un día de mercado, coa baralla colgada do pescozo.

- **Transiciones.** Los títulos `##` no se narran, así que quien escucha con los ojos cerrados solo tiene la primera
  frase de cada capítulo. RO resuelve esto diciendo el título en voz alta.
  - Aperturas que funcionan: l. 49 ("E por fin, a lista de Campo Lameiro"), l. 59 ("deixamos atrás os tribunais e as
    testemuñas") y l. 79.
  - Aperturas que no funcionan: l. 63 (una etimología; con la mejora 2 pasa al gancho), l. 99 (una fecha de nacimiento)
    y l. 115 (una receta).
  - Propuesta: que la primera frase sea una señal hablada y tranquila.
    - Para Feijoo:

      > Deixamos a noite de san Xoán, e imos agora cun frade que escribiu contra as fábulas de bruxería.

    - Para el capítulo nuevo de la mejora 1:

      > E agora, o conxuro do barco: como unhas palabras escritas en Vigo en mil novecentos sesenta e sete chegaron a
      > parecer tan antigas.

    - Para el cap. IV basta con abrir con la escena de la cocina de la mejora 3. Los tipos de meigas, la "meiga
      feiticeira" y las frases en galego de los procesos (l. 65) encajan mejor al final del cap. III, que habla de los
      papeles.

### 8. Menos "segundo" y menos Pousa (l. 49-59, sobre todo 55-59)

El rigor es nuestra ventaja sobre RO, pero no hace falta decir en voz alta la nota al pie de cada frase. En las l. 55-59
(7:12-8:30) hay seis atribuciones en 186 palabras: "Segundo o Consello da Cultura Galega", "Rodrigo Pousa atopou",
"Para Pousa", "O investigador Diego Valor Bravo di", "Pousa conta" y "Segundo Pousa". Pousa sale 9 veces en el guion y
"segundo", 15. La propuesta es presentar cada fuente una vez por bloque, con su profesión, y después seguir con "o mesmo
historiador" o un pronombre, juntando en una frase dos ideas del mismo autor. Antes hay que comprobar con la puerta de
veracidad que cada frase sigue apoyándose en su hecho: H1 ancla nombres, y no hace falta atribuir cada frase.

### 9. Para la voz sintética

- **Velocidad del gancho.** Va a 182 palabras/min (curvas r1 y r2 de la pieza VOZ): un 30 % más rápido que HD (137) y
  RO (144). Con la densidad actual, no se puede seguir. En el guion lo arregla la mejora 2 (menos números en el
  gancho). Para la pieza VOZ: considerar ≤ 160 palabras/min en el gancho [S].
- **Nombres con riesgo.**
  - Henningsen sale dos veces (l. 71 y 95): mejor una o ninguna.
  - Castroviejo y Alonso del Real salen de la zona lenta con la mejora 1.
  - Riesgo de pronunciación: Feijoo y María Feijoa, Hueste, Colmenero, Guiomar Douteiro, Mourence y Maquieira.
  - "Reboredo" es un lugar (l. 51) y también el apellido de un antropólogo (l. 119), y con la mejora 1 quedan a 2-3 min
    uno del otro. Basta "na fonte da Nogueira": sobra "no lugar de Reboredo".
- **l. 27: pronombres ambiguos al oído.** En "chegou Ana González a dicirlle que o home dela, Rodrigo Colmenero,
  andaba chamándoa meiga" no se sabe quién es "dela" ni a quién se refiere "-a". Es la testigo misma (F061), y el
  dossier tiene su respuesta (F062, sin nombres nuevos), que añade un momento humano:

  > O home dunha veciña, Rodrigo Colmenero, andaba chamando meiga a Ana González. Un día, esa veciña estaba á porta
  > debandando, e chegou Ana González a dicirllo. A veciña respondeulle que se fose con Deus, e que se entendese con el.

- **l. 25.** "O gato non o puideron coller: ninguén o deu collido" dice lo mismo dos veces. Basta con "Ninguén o deu
  collido, e escapou por un burato da porta."
- **l. 21.** El lapsus del papel solo funciona si el oído sabe que es una corrección escrita:

  > No papel quedou escrita ata a emenda de quen o escribía: que trouxese auga, digo, leite.

- **l. 91.** La copla "se arraiar, se arraiará, tódalas meigas levará" es difícil de decir y de entender. Si falla la
  prueba de ASR, se deja solo el refrán "en san Xoán, as bruxas fuxirán". En la l. 85, "abrancazadas" es una palabra
  rara para la voz.

### 10. Para el promotor, no para la ronda 2 sin su visto bueno: una línea suave de comunidad

Los canales de dormir en inglés (*Sleepless Historian*, por ejemplo) piden la interacción antes de que el oyente se
duerma, no al final [S: patrón del nicho, no medido aquí]. Al final nadie la oye, y en los primeros 2 min perjudica la
retención. Si el promotor quiere, puede ir una línea al final de la parte despierta (≈ 9:30), sin pedir la suscripción
ni el "gústame", que están vetados:

> Se che gustan estas historias, en Cousas de Galiza para durmir haberá máis. E se queres, cóntanos nun comentario desde
> que recuncho nos escoitas.

## Qué conservar

- Los primeros 32 s (l. 1-3), casi tal cual: son lo mejor del guion y mejores que los arranques de las dos referencias.
- Los detalles de archivo del cap. I: "auga, digo, leite", "pan, sal, auga nin lume", el gato por el burato de la
  porta, y la arracada "polo mal mirar" con su eco en el mal de ollo.
- Cibreira contada con empatía, con el marco de Pousa: "as respostas xa ían nas preguntas".
- "A mesma fonte, a mesma noite, e dúas maneiras de mirala" (la mejor frase del guion), "maldita a nai que non ensina a
  súa filla a meigar" y "as ovellas dun veciño lle comeran a viña ao outro".
- Las dos frases bisagra, "E aquí, amodo, deixamos atrás os tribunais e as testemuñas" y "non tes que lembrar nada do
  que escoites", el marco "desde a tarde ata o amencer" y el estribillo de las sete fontes.
- Las líneas sensoriales de san Xoán (sardiñas, cachelos e broa; el humo que sube; el salto sobre las últimas lapas;
  "esa auga verde e recendente"; la moura que se peina; el sol que baila). Son aburridas en el buen sentido.
- Nada de violencia ni de intrusiones nocturnas en la zona de dormir, nada inventado y todas las puertas en verde.

## Señales para el crítico B (no las he verificado a fondo)

- **l. 11.** "Coas meigas, a temida Inquisición foi branda" va sin atribuir. En el dossier es de Valor Bravo (F039), y
  al oído queda pegada al Arquivo, que se cita en la frase anterior. La mejora 2 lo corrige.
- **l. 1.** "Case todo galego oíu este conxuro". La fuente (*GCiencia*) dice "puido presenciar nalgún momento" y F246
  dice "oíron algunha vez": el guion lo refuerza un poco.
- **Suena exagerado, pero es literal** (comprobado en `dossier/feitos.yaml` y, en el caso de Feijoo, en su texto):
  - "coma un poldro bravo";
  - "máis rápido ca as aguias [...] un burro": Feijoo escribió "excediendo la velocidad de las águilas, no pudiesen dar
    alcance a un jumento";
  - "ser solteira ou viúva xa sinalaba unha muller como diferente" (CCG);
  - "recoñécese a cultura galega en boa parte de España e de Portugal" (Galipedia).
- **l. 75.** No verifiqué "que chegou a Galiza no século dezasete".

## Anexo: cómo se midió (Claude, 30-09-2026)

| Qué | Cómo | Resultado |
|---|---|---|
| Subtítulos de HD | yt-dlp 2026.08.19 del venv del scratchpad. `mweb` solo dio imágenes y descartó los subtítulos por falta de PO token; `android_vr`, `tv_simply` e `ios` pidieron "Sign in to confirm you're not a bot" (HTTP 429 desde la IP). Funcionó `web_embedded` con `--dump-single-json` y la pista `es-orig` en json3 | 4.979 palabras en 36,3 min (137 palabras/min, igual que `gauntlet2/referencia.md`) |
| Subtítulos de RO | La URL de subtítulos de los metadatos que la pieza TEMA dejó en caché (`scratchpad/tema/full/ij7nuBjh1PQ.json`, válida hasta las 18:58 UTC del 30-09-2026), pista `es-orig` en json3 | 17.445 palabras en 120,8 min (144 palabras/min) |
| Lectura y medidas | `json3_txt.py` (bloques de 30 s), `medir.py` y `medir_ref.py` en `scratchpad/criticoA-guion-r1/`. Los textos de terceros no se suben al repo | Tablas de "Medidas" |
| Tiempos por párrafo | Interpolación lineal entre las anclas del modelo B de `notas-r1.md` §2 | Los minutos citados |
| Hechos y puerta de estilo | `grep` en `dossier/feitos.yaml`, en el texto de Feijoo del scratchpad y en `herramientas/pipeline/qa.py` (veta "imaxina", las cifras, los signos y las preguntas) | Las propuestas en galego no usan "imaxina" ni signos vetados y tienen frases de 8-25 palabras fuera del gancho |
| Lengua de las propuestas | `qa.lingua` (LanguageTool gl-ES + hunspell, la función de la puerta) sobre los 17 bloques en galego de este veredicto | **0 avisos**. Hubo un falso positivo en "O historiador Rodrigo Pousa" (lee "Rodrigo" como el verbo *rodrigar*) y se quitó escribiendo "Rodrigo Pousa, historiador", como en r1. La veracidad NLI no se pasó: la pasa la ronda 2 |
