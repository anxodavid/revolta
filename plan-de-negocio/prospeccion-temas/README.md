# Prospección de temas para "Cousas de Galiza para durmir" (01-10-2026)

Encargo del promotor (en galego): "unha ronda de prospección de asuntos que poideran encaixar en Cousas de Galiza para
durmir e clasificalas por orde de interese, temas que dean para divulgación de 30 min pero que teñan algo de gancho,
unha lista de 12 a 20 temas con ponderación por cada temática, busca de referencias e deixalas anotadas".

**Qué es automático y qué hizo Claude.** Las búsquedas de YouTube (yt-dlp) y Google Trends salieron de scripts
(`scripts/`); las cifras de demanda salen de ahí. Las reglas de limpieza de resultados, la lista de temas, la
calibración final de las notas y el orden los decidió **Claude a mano**. Las fichas de cada tema (ganchos, referencias,
arcos) las escribieron **tres agentes Claude** con búsqueda web; cada fuente lleva **[A]** si el agente abrió la página y
**[C]** si solo la vio citada. **Ninguna persona ha revisado este documento ni las fichas.** "As meigas de verdade" no
entra en la lista porque ya está producido.

## 1. Clasificación (21 temas)

Criterios (1-5), los mismos del Gauntlet 3 (`../gauntlet3/tema/investigacion.md` §5) con un cambio en E:
- **D** demanda medida en YouTube (§3). Regla: 5 = ≥ 10 vídeos narrativos > 10 K y ≥ 5 > 100 K; 4 = ≥ 10 > 10 K;
  3 = 5-9 > 10 K; 2 = 1-4 > 10 K; 1 = ninguno.
- **G** gancho verdadero y documentado para los primeros 60-120 s.
- **S** compatibilidad con dormir (sin terror ni violencia en el núcleo; segunda mitad serena posible).
- **V** riqueza visual galega con **bajo riesgo de imágenes absurdas en SDXL** (lo que el modelo no conoce baja nota).
- **F** fuentes fiables y accesibles en línea.
- **I** identidad galega ("cousa de Galiza").
- **E** ventana de publicación clara (fiesta, aniversario, estación). En el Gauntlet 3 E era "octubre"; aquí es la
  fuerza de su mejor ventana, que se indica.
- **Ponderada = 2·D + 2·G + S + V + F + I + E** (máximo 45): pesa el doble lo que trae público (demanda y gancho).

Las notas de los agentes eran generosas (p. ej. magosto 30/30); **Claude las recalibró** con la escala del Gauntlet 3
(allí magosto tenía G 2 y Camiño I 3). Las de los agentes están en cada ficha, para comparar.

| # | Tema | D | G | S | V | F | I | E | **Pond.** | Ventana | Ficha |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Camiño de Santiago e o Códice roubado** | 5 | 4 | 5 | 4 | 5 | 4 | 5 | **41** | Mediados de dic. 2026 (abre el Ano Santo 2027 el 31-12) | [G1 §1](fichas/grupo-1.md) |
| 2 | **Os indianos e a emigración a América** | 4 | 4 | 5 | 4 | 4 | 5 | 3 | **37** | Diciembre (himno, 1907) | [G2 §4](fichas/grupo-2.md) |
| 3 | **Santo André de Teixido** | 3 | 4 | 5 | 4 | 4 | 5 | 4 | **36** | ≈ 25 ago. (romería del 8-9); o ≈ 25 nov. | [G1 §3](fichas/grupo-1.md) |
| 4 | **O magosto e os soutos** | 2 | 3 | 5 | 5 | 4 | 5 | 5 | **34** | **1-10 nov. 2026** (San Martiño) | [G3 §7](fichas/grupo-3.md) |
| 4 | Torre de Hércules | 3 | 4 | 5 | 4 | 4 | 5 | 2 | **34** | 27 jun. (UNESCO) o invierno | [G1 §7](fichas/grupo-1.md) |
| 4 | Santa Compaña | 5 | 3 | 2 | 3 | 3 | 5 | 5 | **34** | 20-25 oct. / noviembre | [G1 §2](fichas/grupo-1.md) |
| 4 | O Entroido galego | 4 | 4 | 2 | 2 | 4 | 5 | 5 | **34** | 2.ª quincena ene. 2027 (Entroido 7-9 feb.) | [G3 §6](fichas/grupo-3.md) |
| 8 | Cidades asolagadas | 2 | 4 | 5 | 5 | 3 | 5 | 3 | **33** | ≈ 15 jun. (San Xoán) | [G1 §4](fichas/grupo-1.md) |
| 8 | Costa da Morte: faros e naufraxios | 3 | 4 | 3 | 4 | 4 | 5 | 3 | **33** | Noviembre (temporales; *Serpent* 10-11-1890) | [G2 §3](fichas/grupo-2.md) |
| 8 | Os mosteiros e a Ribeira Sacra | 4 | 3 | 5 | 4 | 4 | 4 | 2 | **33** | Septiembre (vendimia) o Adviento | [G3 §1](fichas/grupo-3.md) |
| 8 | O ouro dos castros | 3 | 4 | 4 | 3 | 5 | 5 | 2 | **33** | Verano | [G3 §2](fichas/grupo-3.md) |
| 8 | Santa Marta de Ribarteme e as romarías raras | 3 | 5 | 3 | 2 | 3 | 5 | 4 | **33** | 10-20 jul. (romería 29-7) | [G3 §4](fichas/grupo-3.md) |
| 13 | Os viquingos en Galicia | 4 | 4 | 2 | 3 | 4 | 3 | 4 | **32** | ≈ 20 jul. (Romaría Vikinga, 1.er domingo de ago.) | [G1 §6](fichas/grupo-1.md) |
| 14 | Seráns e fiadeiros | 1 | 3 | 5 | 5 | 3 | 5 | 4 | **30** | Diciembre-enero | [G2 §7](fichas/grupo-2.md) |
| 15 | Os irmandiños | 2 | 4 | 3 | 3 | 4 | 5 | 2 | **29** | Abril | [G2 §1](fichas/grupo-2.md) |
| 15 | Os galeóns de Rande | 2 | 4 | 3 | 3 | 4 | 3 | 4 | **29** | ≈ 15 oct. (batalla 23-10-1702) | [G2 §2](fichas/grupo-2.md) |
| 15 | Linguas secretas dos oficios | 1 | 4 | 5 | 3 | 4 | 5 | 2 | **29** | Mayo (Letras Galegas) | [G2 §6](fichas/grupo-2.md) |
| 15 | O reino suevo | 4 | 3 | 4 | 2 | 4 | 4 | 1 | **29** | Ninguna | [G3 §3](fichas/grupo-3.md) |
| 15 | Hórreos e cruceiros | 2 | 3 | 5 | 3 | 4 | 5 | 2 | **29** | Septiembre-octubre | [G3 §5](fichas/grupo-3.md) |
| 20 | Prisciliano | 2 | 4 | 3 | 2 | 4 | 4 | 2 | **27** | Noviembre | [G1 §5](fichas/grupo-1.md) |
| 20 | Os baleeiros de Galicia | 2 | 4 | 2 | 3 | 4 | 4 | 2 | **27** | ≈ 21 oct. (última ballena, 1985) | [G2 §5](fichas/grupo-2.md) |

**Sensibilidad.** El primero (Camiño, 41) gana con cualquier peso razonable: sin ponderar suma 32, también el primero.
Del 4.º al 12.º hay **nueve temas en 2 puntos (33-34)**: ahí el orden lo decide más el calendario que la nota. Sin
ponderar (suma simple) suben los temas de calma con poca demanda: magosto 29, Teixido 29, asolagadas 27, seráns 26.

## 2. Ficha corta por tema (el mejor gancho y 2-3 referencias)

Los ganchos van en galego (texto público posible). **Todos necesitan pasar por el dossier antes de un guion**: los
agentes señalan discrepancias que aquí se resumen. Arcos de 30 min, más ganchos y 6-10 referencias por tema, en las
fichas.

1. **Camiño de Santiago e o Códice roubado (41).** Gancho: «En 2011 desapareceu da catedral o Códice Calixtino, un
   libro do século XII. Apareceu un ano despois nun garaxe, envolto en xornais. Levárao o electricista que traballara
   para a catedral.» No dar la pena (9 años u 8 y 2 meses según la fuente). Ángulo: el robo como entrada; después la
   *inventio*, el Pórtico, el botafumeiro y el camino nocturno. Es el **mejor dato de "para dormir" de un tema
   gallego** (183 K, Grandes Relatos para Dormir) y el Ano Santo 2027 le da ventana. Riesgo: tema saturado en
   castellano. Ref.: [Infobae, 15 años del robo](https://www.infobae.com/espana/2026/07/05/fui-yo-quien-robo-el-libro-se-cumplen-15-anos-del-robo-del-codice-calixtino-de-la-catedral-de-santiago-que-disparo-las-replicas-de-esta-guia-de-peregrinos/) [A];
   [Xunta, el Codex Calixtinus](https://www.caminodesantiago.gal/en/discover/origins-and-evolution/the-codex-of-calixtinus) [A];
   [Museo das Peregrinacións, *inventio*](https://museoperegrinacions.xunta.gal/es/visita/que-ver-en-tu-visita/descubrimiento-e-identificacion-del-cuerpo-apostolico) [A].
2. **Os indianos (37).** Gancho: «O himno galego estreouse na Habana, en decembro de 1907, lonxe de Galicia.» (20 o 27
   de diciembre según la fuente: no dar el día). Ángulo: emigración, remesas, escuelas pagadas desde América (220-318
   según el catálogo), casas de indianos; muy sereno. El competidor Grandes Relatos acaba de publicar "The Secret of
   the Indianos" (21-09-2026): conviene ver cómo le va. Ref.: [Xunta, Emigración: Cuba y Galicia](https://emigracion.xunta.gal/es/actualidad/noticia/cuba-y-galicia-decadas-simbiosis) [A];
   [RAG, publicación sobre el himno](https://publicacions.academia.gal/index.php/rag/catalog/book/209) [A].
3. **Santo André de Teixido (36).** Gancho: «"Vai de morto quen non foi de vivo." En 1391 unha señora de Viveiro deixou
   escrito no testamento que alguén fose por ela en romaría.» (Cal Pardo 1991, vía Galipedia: [C] para el libro). Muerte
   amable, pan, fuentes, acantilados, "non mates o bichiño". Ref.: [Maciñeira, *San Andrés de Teixido* (1921), texto completo](https://archive.org/details/sanandrsdeteix00maci) [A];
   [Galipedia, Santo André de Teixido](https://gl.wikipedia.org/wiki/Santo_Andr%C3%A9_de_Teixido) [A];
   [Concello de Cedeira](https://turismo.cedeira.gal/conece-cedeira/san-andres-de-teixido/) [A].
4. **O magosto e os soutos (34).** Gancho: «A castaña foi o pan dos pobres: antes da pataca, era o que mataba a fame
   en Galicia. E no século XX a tinta levou ata o oitenta por cento dos castiñeiros.» (Cita de un médico de 1903 recogida
   por el CCG; original sin localizar. El 80 % es una estimación de Elorrieta, 1949.) El mejor tema "para dormir" de la
   lista y el **único con ventana inmediata** (San Martiño, 11-11). Poca demanda medida. Ref.:
   [CCG, *O castiñeiro: bioloxía e patoloxía* (1999, PDF)](https://consellodacultura.gal/mediateca/extras/CCG_1999_Castineiro-O-bioloxia-e-patoloxia.pdf) [A];
   [GCiencia, refugio genético](https://www.gciencia.com/medioambiental/os-castineiros-da-galicia-atlantica-un-refuxio-xenetico-milenario/) [A].
5. **Torre de Hércules (34).** Gancho: «É o único faro romano que segue aceso, e coñecemos o nome de quen o fixo: Caio
   Sevio Lupo, arquitecto de Aeminium, a actual Coímbra.» Y el nombre de A Coruña (*Crunia*, 1208) sacado,
   según Navaza (2016), del Carlomagno del Códice. Visual (mar, noche, haz de luz). Relatos al Oído ya lo hizo
   (≈ 6 K). Ref.: [Galipedia, Torre de Hércules](https://gl.wikipedia.org/wiki/Torre_de_H%C3%A9rcules) [A];
   [web oficial](https://torredeherculesacoruna.com/index.php?l=es&s=58) [C, 403 desde aquí]; Navaza, *Revista Galega de Filoloxía* 2016 (enlace en la ficha) [A].
6. **Santa Compaña (34).** Gancho: «Nas aldeas case ninguén lle chamaba Santa Compaña: dicían a Compaña, a Estadea, a
   Hoste.» (Galipedia citando a Cuba et al. 2008 y Gondar 1989; Risco opina distinto.) Máxima estacionalidad
   (octubre × 2,3-3,2, Gauntlet 3), pero su público es de terror y en "para dormir" rinde poco (5-6 K). Ref.:
   [Galipedia, Santa Compaña](https://gl.wikipedia.org/wiki/Santa_Compa%C3%B1a) [A]; Lisón Tolosana, *La Santa Compaña* (Akal) [C];
   Cuba, Reigosa y Miranda, *Dicionario dos seres míticos galegos* (Xerais) [C].
7. **O Entroido galego (34).** Gancho: «O 3 de febreiro de 1937 unha orde suspendeu "en absoluto" o Entroido.» (Leída en el
   [BOE nº 108, 5-2-1937](https://www.boe.es/gazeta/dias/1937/02/05/pdfs/BOE-1937-108.pdf) [A]; que en Laza, Verín o
   Xinzo se siguiera celebrando lo dice la prensa local: pasarlo por el dossier antes de usarlo). Ojo con el veto del plan v2 (franquismo): la orden se
   nombra como dato, sin política. **SDXL no conoce las máscaras** (peliqueiro, cigarrón): necesita referencias (D15).
   Fiesta ruidosa: la segunda mitad, desde la víspera y la memoria.
8. **Cidades asolagadas (33).** Gancho: «Na seca de 2022 a auga baixou e volveu verse Aceredo, unha aldea afogada en
   1992. Durante séculos, Galicia contou o mesmo de cidades enteiras baixo as lagoas.» Mezcla verdad (encoros) y lenda
   (Antela, Doniños, Lucerna del Códice). Ideal para dormir y para SDXL (agua, niebla, campanas). La etimología
   popular de Doniños ("dous meniños") es falsa. Ref.: [Euronews, Aceredo](https://es.euronews.com/2022/02/09/la-sequia-deja-al-descubierto-la-aldea-gallega-de-aceredo-en-ourense) [A];
   [Galipedia, Vilas asolagadas](https://gl.wikipedia.org/wiki/Vilas_asolagadas) [A]; [Xacopedia, Lucerna Ventosa](https://xacopedia.com/Lucerna_Ventosa) [A].
9. **Costa da Morte (33).** Gancho: «Despois do naufraxio do *Serpent* (1890), a raíña Victoria mandou un barómetro a
   Camariñas. Aínda está nunha fachada.» Y desmontar la lenda de los raqueiros (ningún caso documentado). Muertos: 172
   o 173 según la fuente. Ref.: [AEMET Blog, el naufragio del *Serpent*](https://aemetblog.es/2020/12/27/el-naufragio-del-hms-serpent-en-la-costa-da-morte/) [A];
   [Galipedia, HMS Serpent](https://gl.wikipedia.org/wiki/HMS_Serpent_(1887)) [A].
10. **Os mosteiros e a Ribeira Sacra (33).** Gancho: «En 1951 ardeu o mosteiro de Samos. O lume empezou na licoraría
    dos propios monxes.» Y los socalcos datados en el s. X por el CSIC (un solo yacimiento: no generalizar). El tema
    es el sueño mismo (claustros, horas, río). Relatos al Oído: "lost monastery in Galicia" ≈ 17 K. Ref.:
    [Galipedia, Mosteiro de Samos](https://gl.wikipedia.org/wiki/Mosteiro_de_San_Xuli%C3%A1n_de_Samos) [A]; ficha del Ministerio de Cultura de Sobrado y CSIC (en la ficha).
11. **O ouro dos castros (33).** Gancho: «En 1976 un mariñeiro de Rianxo cavaba para facer un galpón e atopou un casco
    de ouro. Pensou que era ferro.» (El casco de Leiro es **de la Edad del Bronce, no castrexo**: decirlo.) Montefurado,
    el río desviado por los romanos. No repetir las "20.000 libras de oro" como dato galego (Plinio las da para tres
    regiones y "segundo algúns"). Ref.: [Galicia Universal, casco de Leiro](https://galiciauniversal.org/gl/cincuenta-anos-de-un-hallazgo-historico-el-casco-de-leiro) [A];
    [Plinio, *NH* 33](https://penelope.uchicago.edu/Thayer/L/Roman/Texts/Pliny_the_Elder/33*.html) [A];
    [Museo de Pontevedra, Tesouro de Caldas](https://museo.depo.gal/en/-/esencial-tesouro-de-caldas-de-reis) [A].
12. **Santa Marta de Ribarteme (33).** Gancho: «Cada 29 de xullo, en As Neves, había xente viva que ía en procesión
    dentro dun cadaleito, para agradecerlle á santa que a salvara.» El gancho más fuerte de la lista, pero **el párroco
    suprimió la procesión en 2022** y en 2023 volvió con dos ataúdes: hay que comprobar 2024-2026 y contarlo en pasado
    si hace falta. Ataúdes y exvotos de cera en SDXL: riesgo de imágenes siniestras. Ref.:
    [Nós Diario, 29-7-2022](https://www.nosdiario.gal/articulo/cultura/adeus-procesion-ataudes-nas-neves/20220729111616148782.amp.html) [A];
    [Turismo de Galicia](https://www.turismo.gal/recurso/-/detalle/200312000146/romaria-de-santa-marta-de-ribarteme?langId=en_US&tp=97&ctre=261) [A].
13. **Os viquingos (32).** Gancho: «Cara a 1014 os viquingos saquearon Tui. Quen os mandaba era, seguramente, Olaf, o
    futuro rei e santo de Noruega.» ("seguramente": Sánchez Pardo 2010). Mucha demanda en castellano ("vikingos" es
    enorme en YouTube España), pero el núcleo es violento y SDXL pinta cascos con cuernos. Ref.:
    [Sánchez Pardo, *Anuario Brigantino* 2010 (PDF)](https://anuariobrigantino.betanzos.net/Ab2010PDF/2010%20057_086%20VIKINGOS%20EN%20GALICIA.pdf) [A];
    [Concello de Catoira](https://catoira.gal/en/turismo/romaria-vikinga/) [A].
14. **Seráns e fiadeiros (30).** Gancho: «En 1751 o bispo de Lugo prohibiu que as mozas fiasen onde houbese mozos.»
    (fuente: prensa, [El Independiente](https://www.elindependiente.com/tendencias/cultura/2023/11/12/el-filandon-la-hoguera-de-los-cuentos-que-fraguo-el-cervantes-y-que-la-iglesia-intento-prohibir/) [A]: buscar la primaria). Demanda casi nula,
    pero es **el nombre del canal**: buen episodio fundacional o de invierno, muy de dormir. Ref.:
    [RAG, "serán"](https://academia.gal/dicionario/-/termo/ser%C3%A1n) [A]; [CCG, Lugares de memoria](https://consellodacultura.gal/lugares-de-memoria/detalle.php?id=34417) [A].
15. **Os irmandiños (29).** Gancho: «"Os pardais habían de correr tras os falcóns", declarou un testemuña de Betanzos no
    preito de 1526.» Fortalezas derribadas: 130, 140 o 251 según la fuente. Ref.:
    [Carlos Barros, "Los gorriones corren tras los halcones"](https://cbarros.com/gorriones-corren-halcones-los-irmandinos-de-galicia/) [A].
16. **Os galeóns de Rande (29).** Gancho: «O capitán Nemo, en *Vinte mil leguas de viaxe submarina*, vai buscar ouro
    á ría de Vigo.» (comprobado en el [texto de Verne](https://www.gutenberg.org/cache/epub/5097/pg5097.txt) [A]).
    No decir que la expedición de 1870 "inspiró a Verne" (la novela ya salía en 1869). Kamen: ≈ 2.000 kg de plata a la
    Ceca de Londres [C].
17. **Linguas secretas dos oficios (29).** Gancho: «En 1952 Alan Lomax gravou un afiador de Nogueira de Ramuín tocando o
    chifre. Esa melodía acabou nun disco de Miles Davis: "The Pan Piper".» Ref.:
    [Library of Congress, blog Folklife](https://blogs.loc.gov/folklife/2015/01/carlos-nunez-concert-honors-alan-lomaxs-spanish-fieldwork/) [A];
    [Cultural Equity, Galicia](https://www.culturalequity.org/album/galicia) [A]. No usar "latín dos zoqueiros" (sin fuente).
18. **O reino suevo (29).** Gancho: la silicua «IVSSV RICHIARI REGES», moneda con el nombre de un rey suevo (seis
    ejemplares conocidos según Barroca 2017 [C]). Los "primeros" (primer reino católico…) hay que matizarlos.
    Visualmente pobre y con riesgo de "bárbaros" de cómic. Ref.: [Münzkabinett Berlin](https://nat.museum-digital.de/object/544236) [A];
    [Hidacio, *Chronicon*](https://www.condadodecastilla.es/cultura-sociedad/fuentes-historicas/cronicon-de-hidacio/) [A].
19. **Hórreos e cruceiros (29).** Gancho: «O hórreo máis longo non é o de Carnota: é o do Araño, en Rianxo, duns
    trinta e sete metros.» Muy de dormir, pero **SDXL no sabe hacer un hórreo galego** (D15: hace falta referencia).
    Ref.: [Praza, hórreos](https://praza.gal/ducias/horreos-que-son-patrimonio-cultural-e-identidade-de-galicia) [A];
    [Concello de Carnota](https://www.carnota.gal/tourism/patrimonio/horreos/?lang=en) [A].
20. **Prisciliano (27).** Gancho: «Un escritor do seu tempo, que non o quería ben, conta que chegou a terse "xurar por
    Prisciliano" polo máis sagrado.» (Sulpicio Severo, [*Chronica* II, 46-51](https://www.newadvent.org/fathers/35052.htm) [A].)
    La hipótesis "Prisciliano está en el sepulcro de Santiago" es solo hipótesis; tema sensible.
20. **Os baleeiros (27).** Gancho: «A última balea cazada en España descargouse en Caneliñas, en Cee, o 21 de outubro de
    1985.» Ref.: [GCiencia, Caneliñas](https://www.gciencia.com/destinos/canelinas-ultima-baleeira-galicia/) [A]. El
    núcleo (caza, despiece) casa mal con dormir.

## 3. Demanda medida (YouTube y Trends)

**YouTube** (`scripts/demanda.py`, 01-10-2026; datos en `datos/busquedas-yt.tsv` y `datos/demanda-resumen.json`): 3-5
consultas por tema en es/gl/en, 20 resultados por consulta, por relevancia; cuentan los vídeos cuyo título casa con el
tema, sin música, películas ni homónimos (reglas a mano tras revisar los listados).

| Tema | Vídeos | > 10 K | > 100 K | Máximo | Formato "para dormir" |
|---|---|---|---|---|---|
| Camiño | 69 | 31 | 7 | 474.479 (Planet Doc) | 20 vídeos; máx. 183.225 (Grandes Relatos) |
| Entroido | 68 | 17 | 0 | 56.978 | 0 |
| Suevos | 27 | 15 | 4 | 376.443 (Fundación Juan March) | 1 |
| Viquingos | 52 | 13 | 1 | 262.428 (Fundación Juan March) | 0 |
| Mosteiros | 77 | 13 | 1 | 143.934 | 1; 17.317 (Relatos al Oído) |
| Santa Compaña | 45 | 12 | 4 | 1.839.268 (TikTak Draw) | 5; máx. 6.054 |
| Indianos | 49 | 11 | 3 | 351.049 (BBC Mundo) | 0 |
| Ouro dos castros | 40 | 6 | 2 | 179.771 (Montefurado) | 0 |
| Costa da Morte | 44 | 6 | 0 | 31.824 | 0 |
| Teixido | 35 | 5 | 1 | 213.241 (noticia) | 0 |
| Torre de Hércules | 37 | 5 | 2 | 141.565 | 6.085 (Relatos al Oído, en la búsqueda de canal) |
| Ribarteme | 40 | 5 | 0 | 26.379 (EFE) | 0 |
| Magosto | 44 | 3 | 1 | 1.409.205 (oficios: las castañas) | 0 |
| Hórreos | 61 | 3 | 0 | 48.687 | 0 |
| Irmandiños | 31 | 2 | 0 | 17.758 | 0 |
| Prisciliano | 21 | 2 | 0 | 15.348 | 0 |
| Rande | 37 | 1 | 0 | 29.869 | 0 |
| Baleeiros | 31 | 1 | 0 | 12.051 | 0 |
| Asolagadas | 22 | 1 | 0 | 11.062 | 0 |
| Seráns | 12 | 0 | 0 | 4.179 | 0 |
| Linguas secretas | 35 | 0 | 0 | 3.725 | 0 |

**Competidores "para dormir"** (`datos/competidores-canles.tsv`, vistas redondeadas por YouTube):
- *Relatos al Oído* (305 vídeos): lendas de Galicia 108 K; Compostela 14 K; "lost monastery in Galicia" 17 K; Lugo
  11 K; Torre de Hércules 6 K. Lo que más le rinde: misterio, crímenes, Vaticano; en lo marítimo, "misterios
  marítimos" 87 K y "piratas, naufragios" 60 K (apoya Costa da Morte y Rande en clave serena).
- *Grandes Relatos para Dormir* (64 vídeos, todos de ~30-40 min, como los nuestros): Camino 183 K; **pueblos y
  enigmas** rinden mucho (gitanos 475 K, vascos 209 K, agotes 18 K, pasiegos 17 K); indianos recién publicado.
  Señal: "o pobo que…" funciona; candidato futuro: un oficio o grupo galego contado como "pobo" (afiadores, canteiros) [S, sin medir].
- **En galego no hay nada para dormir en ningún tema** (igual que en los Gauntlet 2 y 3).

**Google Trends** (`datos/tendencias.txt`, búsqueda en YouTube, España, 5 años, ancla "Santa Compaña" = 2,9): solo
"Camino de Santiago" (155) y "vikingos" (154) tienen volumen alto; "entroido" 6,9 (pico en febrero), "Ribeira Sacra"
4,5, "magosto" 3,0 (pico en noviembre), "castros" 1,9, "indianos" 1,7 (pico en febrero: carnaval de indianos de La
Palma, no Galicia). El resto sale a cero casi todas las semanas: **Trends no sirve para temas tan pequeños**.

## 4. Propuesta de calendario (si se produce uno al mes) [S]

| Mes | Tema | Por qué |
|---|---|---|
| Nov. 2026 (1-10) | **O magosto e os soutos** | Única ventana inmediata; el más fácil para dormir y para SDXL; casa con "As meigas" (otoño) |
| Dic. 2026 (≈ 15) | **Camiño e o Códice roubado** | Ano Santo 2027 (Puerta Santa el 31-12-2026); mejor demanda medida |
| Ene. 2027 | Seráns e fiadeiros **o** indianos | Invierno; el primero da nombre al canal; el segundo, demanda y calma |
| Ene.-feb. 2027 | Entroido | Solo si antes hay imágenes de referencia para las máscaras (D15) |
| Primavera 2027 | Mosteiros, ouro dos castros, Torre de Hércules | Sin fecha: fondo de catálogo |
| Jun.-ago. 2027 | Asolagadas (San Xoán), Ribarteme y viquingos (julio), Teixido (agosto) | Fiestas de verano |
| Oct.-nov. 2027 | Santa Compaña, Rande, Costa da Morte | Temporada de difuntos y temporales |

Con el pipeline actual un episodio de 30 min son ≈ 16,5 h de CPU de núcleo (CLAUDE.md): el magosto para primeros de
noviembre es factible si se empieza en octubre.

## 5. Límites

- La demanda es una **muestra** de 60-100 resultados por tema y vistas acumuladas; sirve para ordenar, no para prever.
- Las notas G-E son juicio de Claude sobre lo que escribieron los agentes; nadie las ha contrastado. Los ganchos
  marcados [C] o con discrepancias no se pueden usar sin pasar por el dossier.
- Desde este entorno fallaron UNESCO, ResearchGate y la web oficial de la Torre de Hércules (403).
- No se midió la demanda en portugués ni en inglés por separado (las consultas en/pt van mezcladas en la tabla).
