# Prospección de temas · Grupo 3 (fichas)

Hecho por Claude (subagente de prospección) el 01-10-2026 con WebSearch y WebFetch. **No hay revisión humana.**

**Método y límites**

- **[A]** = página abierta y leída por Claude en esta sesión (WebFetch, o PDF descargado y extraído con `pypdf`).
  **[C]** = solo vista citada en otra fuente o en un resultado de búsqueda: hay que abrirla antes de usarla en un guion.
- WebFetch resume las páginas con un modelo pequeño. Las cifras y citas marcadas [A] coinciden con lo que devolvió,
  pero las citas literales para el guion deben recopiarse de la fuente al escribir el dossier.
- No se midió la demanda en YouTube: solo se proponen consultas (sección final de cada tema).
- Puntuación 1-5: **G** gancho verdadero · **S** compatible con dormir · **V** riqueza visual y bajo riesgo con SDXL ·
  **F** fuentes fiables accesibles · **I** identidad galega · **E** estacionalidad.
- Los ganchos están en galego normativo (RAG). Las cifras, en el guion, se escriben en letra (Cotovía).

## Resumen

| # | Tema | G | S | V | F | I | E | Total | Mes ideal |
|---|---|---|---|---|---|---|---|---|---|
| 7 | O magosto e os soutos | 4 | 5 | 5 | 5 | 5 | 5 | **29** | 2.ª quincena de octubre / 1-10 de noviembre (San Martiño, 11-N) |
| 2 | O ouro dos castros | 5 | 4 | 4 | 5 | 5 | 2 | **25** | Cualquiera (julio y agosto, temporada de visitas a castros [S]) |
| 6 | O Entroido galego | 5 | 3 | 3 | 4 | 5 | 5 | **25** | 2.ª quincena de enero de 2027 (martes de Entroido: 9-2-2027) |
| 1 | Os mosteiros | 4 | 5 | 4 | 4 | 5 | 3 | **25** | Septiembre (vendimia de la Ribeira Sacra) |
| 5 | Hórreos e cruceiros | 3 | 5 | 4 | 4 | 5 | 3 | **24** | Septiembre-octubre (cosecha, maíz al hórreo) |
| 4 | Santa Marta de Ribarteme e romarías raras | 5 | 3 | 3 | 3 | 5 | 5 | **24** | 10-20 de julio (romaría el 29-7) |
| 3 | O reino suevo | 4 | 4 | 2 | 4 | 4 | 2 | **20** | Sin fecha fuerte |

Fechas de 2027 calculadas por Claude con `dateutil.easter`: Pascua el 28-3-2027, martes de Entroido el 9-2-2027 y
miércoles de Ceniza el 10-2-2027.

---

## 1. Os mosteiros: Samos, Oseira, Sobrado e a Ribeira Sacra

### Ángulo y arco (≈ 30 min)

**Ángulo:** "Mil anos de silencio": cómo vivían los monjes, qué hicieron con la tierra (viñas, soutos, granjas), cómo
lo perdieron todo en 1835 y cómo volvieron algunos un siglo después. La sorpresa la aportan los datos que desmontan
tópicos (los socalcos no son romanos, el nombre "Ribeira Sacra" quizá no signifique "ribera sagrada", un incendio que
empezó en la licorería). La calma, la regla, las horas, el claustro y la piedra.

1. **Gancho (0-2 min):** el licor de Samos y el fuego de 1951; los socalcos del siglo X.
2. **Un nome escrito en 1124:** Teresa de Portugal dona a Montederramo un lugar llamado *Rouoyra/Rivoira Sacrata*; el
   debate sobre la lectura (Yepes frente a Souza Soares). Tono sereno a partir de aquí.
3. **Un día no mosteiro:** horas canónicas, trabajo, botica (Sobrado), hospedería para peregrinos.
4. **Viño e castañas:** socalcos del Sil, rentas de soutos y viñas, el monasterio como gran propietario (Oseira llegaba
   hasta Marín).
5. **1835: as portas pechadas:** desamortización de Mendizábal, abandono, ruinas, "case un século" de silencio.
6. **A volta:** Samos en 1880, Oseira en 1929 (trapenses franceses), Sobrado desde 1954-1966. Cierre en un claustro al
   anochecer.

### Ganchos para el primer minuto

| # | Gancho (galego) | Fuente | Notas de discrepancia |
|---|---|---|---|
| 1 | «O 24 de setembro de 1951, no mosteiro de Samos, o lume naceu nun lugar inesperado: a fábrica de licor que os propios monxes tiñan nunha á do claustro grande.» | [A] Campo Galego, 10-9-2018: https://www.campogalego.es/gran-despensa-nuevo-impulso-la-tradicion-de-los-monjes-de-la-abadia-de-samos/ ; [A] Galipedia, Samos: https://gl.wikipedia.org/wiki/Mosteiro_de_San_Xuli%C3%A1n_de_Samos | Estudio académico sobre las causas [C]: "Las causas y las consecuencias del incendio de 1951…" (ResearchGate): https://www.researchgate.net/publication/309599057 . **Discrepancia:** Campo Galego dice que la licorería volvió a abrir en Viladetrés el 4-10-1971; un blog local dice 1960 [C] (memoriadesamos.blogspot.com). No dar la fecha de reapertura. Marca del licor: "Pax" (Campo Galego). No hubo muertos según las fuentes leídas, pero no está confirmado: no afirmarlo |
| 2 | «Os muros de pedra que sosteñen as viñas da Ribeira Sacra non son romanos, como tantas veces se di. As escavacións datan os socalcos máis antigos arredor do século X.» | [A] *GCiencia*, 31-3-2021 (Incipit-CSIC, Universidade do Algarve, Universidade Nova de Lisboa; Vilachá de Salvadur): https://www.gciencia.com/retro/a-orixe-dos-socalcos-da-ribeira-sacra-situase-no-seculo-x-segundo-novos-achados/ | Es **un yacimiento** (110 muestras, 5 sondeos). Decir "nunha escavación en Vilachá…", no generalizar a toda la Ribeira Sacra. Galipedia y webs turísticas siguen diciendo "época romana" |
| 3 | «En 1124, en Allariz, a raíña Teresa de Portugal doou a uns monxes "un lugar que chaman Rouoyra Sacrata". Del vén, quizais, o nome da Ribeira Sacra. Pero ese "quizais" ten historia.» | [A] es.wikipedia, Ribeira Sacra (cita la carta fundacional de Montederramo, 21-8-1124): https://es.wikipedia.org/wiki/Ribeira_Sacra | Yepes leyó "Rivoira"; Torquato de Souza Soares, sobre el facsímil, lee "Rovoyra" [C]. Manuel Vidán Torreira (1987) propone "reboira", 'robledal' [C]. Contarlo como debate abierto, sin elegir |
| 4 | «Un rapaz de catorce anos de Casdemiro entrou en 1690 no mosteiro de Samos. Chamábase Benito Xerónimo Feijoo e pasaría a vida escribindo contra as supersticións.» | [A] Galipedia, Samos (enlace de arriba); [A] Deputación de Lugo: https://turismo.deputacionlugo.gal/gl/conece/lugoinedito/mosteirosamos | Enlaza con el episodio de las meigas (R2 del gauntlet 3). La edad de 14 años sale de un resultado de búsqueda (es.wikipedia, Feijoo) [C]: comprobar antes de usarla |
| 5 | «Contan algunhas fontes antigas que en Sobrado recibiu un cardeal a noticia de que o elixiran papa, e que dende alí deu a súa primeira bendición como Calixto.» | [A] Ministerio de Cultura, ficha de Sobrado (Caminos del Norte, 2019), p. 4: https://www.cultura.gob.es/dam/jcr:a36802e8-e574-4c6f-b937-153a9644d465/2019-10-galicia-sobrado-moxesv2.pdf | **Dudoso:** la propia ficha dice "algunas fuentes antiguas sitúan"; Calixto II fue elegido en Cluny en 1119 (dato de memoria de Claude, sin comprobar). Usarlo solo como "conta a tradición" o dejarlo fuera |

### Referencias clave

- [A] Ministerio de Cultura, ficha de Sobrado dos Monxes (2019): BIC en 1931, Císter en 1142, abandono en 1835,
  restauración desde 1954 y monjes de nuevo en 1966, botica. https://www.cultura.gob.es/dam/jcr:a36802e8-e574-4c6f-b937-153a9644d465/2019-10-galicia-sobrado-moxesv2.pdf
- [A] Galipedia, Oseira: fundación en 1137, Císter en 1141, *Ursaria*, dominios hasta Marín, desamortización de 1835,
  vuelta de los trapenses en 1929, sala capitular. https://gl.wikipedia.org/wiki/Mosteiro_de_Santa_Mar%C3%ADa_de_Oseira
- [A] Galipedia, Samos: inscripción de Ermefredo, exclaustración, vuelta en 1880, incendio de 1951, claustro de
  ≈ 3.000 m². https://gl.wikipedia.org/wiki/Mosteiro_de_San_Xuli%C3%A1n_de_Samos
- [A] Deputación de Lugo, Samos (texto turístico institucional; capilla del Ciprés).
  https://turismo.deputacionlugo.gal/gl/conece/lugoinedito/mosteirosamos
- [A] *GCiencia*, socalcos del siglo X (Incipit-CSIC).
  https://www.gciencia.com/retro/a-orixe-dos-socalcos-da-ribeira-sacra-situase-no-seculo-x-segundo-novos-achados/
- [A] es.wikipedia, Ribeira Sacra: debate sobre el topónimo, con bibliografía (Souza Soares, Vidán Torreira).
  https://es.wikipedia.org/wiki/Ribeira_Sacra
- [C] DOG 29-12-2017, incoación de la Ribeira Sacra como BIC (paisaje cultural): inventario oficial de monasterios y
  bienes. https://www.xunta.gal/dog/Publicados/2017/20171229/AnuncioG0164-261217-0001_gl.html
- [C] M.ª Teresa Basalo Álvarez, "O Cister das terras centrais de Ourense na desamortización de Mendizábal:
  Montederramo e Xunqueira de Espadañedo" (1991), para el capítulo 5. https://dialnet.unirioja.es/servlet/articulo?codigo=4073061
- [C] Estudio sobre el incendio de Samos de 1951 (ResearchGate).
  https://www.researchgate.net/publication/309599057
- [A] Campo Galego, licor Pax y su historia (2018); fuente de prensa sectorial, no académica.

### Puntuación

- **G 4:** el fuego en la licorería y los socalcos medievales son sorpresas verdaderas, pero no tan llamativas como las
  del oro o el Entroido.
- **S 5:** claustros, horas, piedra, río: el tema es el sueño mismo.
- **V 4:** claustros, cañón del Sil y socalcos salen bien en SDXL; los monjes de cerca (manos, caras, hábitos) son un
  riesgo: usar planos generales y siluetas.
- **F 4:** hay fuentes institucionales y una investigación del CSIC; falta abrir bibliografía académica sobre la
  desamortización.
- **I 5:** la Ribeira Sacra y el Camino son marca galega.
- **E 3:** encaja en septiembre (vendimia) [S], o en Adviento.

### Riesgos

- "O mosteiro máis antigo de Occidente" (título de la Deputación de Lugo): es reclamo; el propio texto dice "un dos
  máis antigos". La fundación por Martiño de Dumio es una **atribución**: la primera fecha documentada es la
  inscripción de Ermefredo (Galipedia dice 665; es.wikipedia sitúa al obispo hacia 653-656) [A]. Decir "no século VII
  xa hai noticia del".
- Ciprés de Samos "de máis de mil anos" (Deputación de Lugo): edad no demostrada; no usarla.
- "O viño de Amandi chegaba a Roma" (es.wikipedia, sin fuente sólida): es un mito; no repetirlo.
- **Masacre de Oseira (1909):** seis muertos en un motín por el baldaquino (Galipedia [A]); violento, fuera del
  episodio o como una línea sin detalles.
- Fecha de la exclaustración: 1835 (decretos de Mendizábal, julio y octubre) frente a 1836 (expropiación; Samos
  "exclaustrado en 1836", según un resultado de búsqueda). Decir "en 1835 e 1836".
- Distinguir monjes (benedictinos y cistercienses) de frailes (mendicantes).

### Consultas de YouTube para medir demanda

- `mosteiros Ribeira Sacra historia` · `monasterio de Samos historia documental`
- `Ribeira Sacra monasterios documental` · `mosteiros galegos desamortización`
- `Galician monasteries history` · `mosteiros da Galiza história` (pt)

---

## 2. O ouro dos castros: castros, torques, Montefurado, Gallaecia

### Ángulo y arco

**Ángulo:** "Onde está o ouro de Galicia": de los tesoros encontrados por casualidad (un marinero, unos labradores) a
los romanos que agujerearon una montaña para secar el Sil. La sorpresa la aportan los hallazgos y la ingeniería; la
calma, la vida en el castro, la orfebrería paciente y el río.

1. **Gancho:** el casco de Leiro en una playa de Rianxo (1976); el tesoro de Caldas medio fundido.
2. **Antes dos castros:** el oro de la Edad del Bronce (Caldas, 2250-1500 a. C.; Leiro, 1000-800 a. C.).
3. **A vida no castro:** casas redondas, cientos o miles de poblados (cifras con cautela), tono tranquilo.
4. **Os torques:** el de Burela (1,8 kg) "que parecía un asa de pota"; filigrana y técnica.
5. **Roma e o ouro:** Plinio y las 20.000 libras al año; Montefurado y el meandro del Sil; la *Gallaecia*.
6. **O que queda:** el túnel hoy, la crecida de 1934, los museos (Pontevedra, Lugo, San Antón). Cierre sobre el río.

### Ganchos para el primer minuto

| # | Gancho (galego) | Fuente | Notas de discrepancia |
|---|---|---|---|
| 1 | «O 7 de abril de 1976, un mariñeiro de Rianxo cavaba para facer un galpón onde gardar a dorna e os aparellos. A sesenta centímetros, dentro dunha vasilla de barro, apareceu un casco de ouro. El pensou que era ferro.» | [A] Galicia Universal (Xunta), "50 anos dun achado histórico": https://galiciauniversal.org/gl/cincuenta-anos-de-un-hallazgo-historico-el-casco-de-leiro | Descubridor: José María Vicente Somoza. 270 g; 1000-800 a. C.; Museo de San Antón (A Coruña). Es de la **Edad del Bronce, no castrexo**: decirlo así. "Dorna" no está en la fuente (dice "embarcación"): mejor "a súa barca" |
| 2 | «En 1940, uns veciños de Caldas de Reis atoparon, traballando a terra, quince quilos de ouro. Hoxe gárdanse no Museo de Pontevedra. Pero non todo: preto de dez quilos vendéronse ás agachadas e fundíronse.» | [A] Museo de Pontevedra: https://museo.depo.gal/en/-/esencial-tesouro-de-caldas-de-reis | Peso actual 14,9 kg. Peso original: ≈ 25 kg (Museo) o 27 kg (es.wikipedia [C]); usar el del museo. Piezas: 41 (Museo) o 36 (búsqueda): usar 41. Edad del Bronce (2250-1500 a. C.) |
| 3 | «En 1954, un veciño de Burela, traballando no Chao do Castro, deu cunha peza de ouro de máis de quilo e oitocentos gramos. Durante un tempo pensaron que era a asa dunha pota.» | [A] Deputación de Lugo: https://turismo.deputacionlugo.gal/es/conece/lugoinedito/torques | **Discrepancia de año:** la Deputación dice 1954; un resultado de búsqueda dice 1945. La anécdota del asa salió en la búsqueda [C], no en la página abierta: comprobar en https://gl.wikipedia.org/wiki/Torque_de_Burela o en el Museo Provincial de Lugo antes de usarla. Peso 1.812 g (s. III-I a. C.) |
| 4 | «Os romanos furaron un monte para lle roubar o ouro ao Sil: en Montefurado abriron un túnel na rocha para desviar o río e deixar en seco a curva onde se depositaban as areas douradas.» | [A] Turismo Ribeira Sacra: https://turismo.ribeirasacra.org/tunel-de-montefurado ; [A] Astures.es sobre el estudio del CSIC (2020): https://astures.es/termina-el-estudio-arqueologico-del-tunel-de-montefurado-la-mina-romana-de-quiroga-en-galicia/ | Medidas: 120 m originales y ≈ 52 m tras la crecida de 1934 (Turismo Ribeira Sacra). 19 m de ancho y 17 de alto solo en prensa [C]. "Por orde de Traxano, no século II" **no lo confirma el CSIC**: no decir el emperador. El CSIC lo sitúa en unos dos siglos de minería tras la conquista de Augusto |
| 5 | «Plinio o Vello escribiu que, segundo algúns, Asturia, Gallaecia e Lusitania daban a Roma vinte mil libras de ouro cada ano, e que a maior parte saía de Asturia.» | [A] Plinio, *Naturalis Historia* 33.78 (texto latino en LacusCurtius): https://penelope.uchicago.edu/Thayer/L/Roman/Texts/Pliny_the_Elder/33*.html | **Mito que no hay que repetir:** *El Debate* y otras webs atribuyen las 20.000 libras a Montefurado [C]. Es la cifra de **tres regiones**, "segundo algúns" (*quidam prodiderunt*), y Plinio dice que la mayoría venía de Asturia. ≈ 6,5 t con la libra de 327 g [S] |

### Referencias clave

- [A] Plinio, *NH* 33.66-78 (ruina montium y producción), texto latino. https://penelope.uchicago.edu/Thayer/L/Roman/Texts/Pliny_the_Elder/33*.html
- [A] Museo de Pontevedra, Tesouro de Caldas (inventario, peso, datación, piezas perdidas). https://museo.depo.gal/en/-/esencial-tesouro-de-caldas-de-reis
- [A] Deputación de Lugo, Torques de Burela (y otras piezas del Museo Provincial). https://turismo.deputacionlugo.gal/es/conece/lugoinedito/torques
- [A] Galicia Universal, casco de Leiro (aniversario de 2026). https://galiciauniversal.org/gl/cincuenta-anos-de-un-hallazgo-historico-el-casco-de-leiro
- [A] Astures.es sobre el estudio del CSIC (Currás, Sánchez-Palencia, Fernández Lozano): el túnel forma parte de un
  complejo minero mayor. Nota de prensa original del CSIC [C] (no cargó):
  https://delegacion.galicia.csic.es/el-csic-concluye-el-estudio-historico-arqueologico-del-tunel-de-montefurado-quiroga-lugo/
- [A] Turismo Ribeira Sacra, Montefurado (medidas, crecida de 1934, vuelta del agua en 1941).
- [A] *El Progreso*, 22-9-2022: castros por provincia según Xabier Moure (Lugo 1.496, A Coruña 1.312, Pontevedra 703,
  Ourense 597; total ≈ 4.108 [S], suma hecha por Claude). https://www.elprogreso.es/articulo/comarcas/lugo-es-provincia-gallega-mayor-numero-castros-total-1496/202209221205161602035.html
- [C] Castro de Elviña y su tesoro (excavación de 1947), Concello da Coruña: https://www.coruna.gal/castroelvina/es/castro-excavado?argIdioma=es ;
  artículo en *Spal* (Universidad de Sevilla): https://revistascientificas.us.es/index.php/spal/article/view/28494
- [C] Galipedia, Torque de Burela, para resolver el año del hallazgo: https://gl.wikipedia.org/wiki/Torque_de_Burela

### Puntuación

- **G 5:** tesoros hallados por gente corriente y un río desviado: gancho de "non vas crer" sin exagerar nada.
- **S 4:** la conquista y la minería esclava/forzada [S] tienen dureza; se nombran sin detalle.
- **V 4:** oro, castros y el cañón del Sil son muy visuales. SDXL tiende al "celta" de fantasía (cuernos, tartán): hay
  que pedir objetos concretos (torque liso, casa redonda de piedra) y revisar.
- **F 5:** museos, CSIC y Plinio en abierto.
- **I 5:** la cultura castrexa es un pilar de la identidad galega.
- **E 2:** sin fecha natural; verano por las visitas a castros [S].

### Riesgos

- "Celtas": la etiqueta "castros celtas" es discutida en la academia; decir "a xente dos castros" o "cultura castrexa".
- El número de castros varía entre 2.000 y 5.000 según la fuente (resultados de búsqueda [C]): dar un rango y
  atribuirlo ("segundo un recento de Xabier Moure, máis de catro mil").
- Las Médulas están en León, no en Galicia: no confundirlas con Montefurado.
- Montefurado "por orde de Traxano" y "veinte mil libras de Montefurado": no repetirlo.
- El "rescate" de los tesoros (ventas clandestinas, fundición) se cuenta con calma, sin culpables con nombre.

### Consultas de YouTube

- `ouro dos castros` · `torques castrexos` · `tesouro de Caldas de Reis`
- `Montefurado túnel romano` · `oro romano Galicia Montefurado documental`
- `Roman gold mining Gallaecia` · `ouro castrejo Galiza` (pt)

---

## 3. O reino suevo: Bracara, as moedas e Martiño de Dumio

### Ángulo y arco

**Ángulo:** "O reino que case esquecemos" (409/411-585): un pueblo que llega del Danubio y del Rin y deja huella en el
calendario, en las parroquias y en una moneda que casi nadie ha visto. La sorpresa: la moneda, los días de la semana y
lo de "primero", contado con matices. La calma, Braga, el monacato y la vida rural.

1. **Gancho:** por qué en portugués (y también en galego) existe "segunda feira".
2. **409:** suevos, vándalos y alanos entran en Hispania (Hidacio); asentamiento en la *Gallaecia*; Braga.
3. **Requiario:** católico en 448, sus monedas con su nombre y su final (sin detalles violentos).
4. **O silencio (470-550):** pocas fuentes; arrianismo (Áyax, hacia 465).
5. **Martiño de Dumio:** monje, obispo, el *De correctione rusticorum*, concilios de Braga (561 y 572), el
   *Parochiale Suevum* y las parroquias.
6. **585 e o que queda:** Leovigildo; huellas en la organización parroquial. Cierre tranquilo.

### Ganchos para el primer minuto

| # | Gancho (galego) | Fuente | Notas de discrepancia |
|---|---|---|---|
| 1 | «Por que en portugués se di "segunda-feira" e non "lunes"? A culpa, en boa parte, tena un bispo do século VI que viviu en Dumio, a carón de Braga, e que non quería que os días levasen nomes de deuses pagáns.» | [A] CCG, *Lugares de memoria*, "Dumio. Martiño de": https://consellodacultura.gal/lugares-de-memoria/detalle.php?id=34417 ; [A] RAG, dicionario, "feira" (*segunda feira* = luns): https://academia.gal/dicionario/-/termo/busca/feira | La serie de *ferias* es eclesiástica y anterior; lo que se atribuye a Martiño es **su promoción** en la diócesis de Braga. Decir "en boa parte" o "segundo a tradición". El galego normativo admite *segunda feira* junto a *luns* (RAG) |
| 2 | «Hai mil cincocentos anos, un rei de Galicia mandou cuñar moedas de prata co seu nome: "por orde do rei Requiario". Hoxe coñécense só seis.» | [A] Münzkabinett de Berlín (museum-digital), leyenda *IVSSV RICHIARI REGES*, ceca Braga, 1,19 g: https://nat.museum-digital.de/object/544236 ; [C] M. J. Barroca, "Os seis exemplares da siliqua de Requiário", *Nummus* 40 (2017): https://sigarra.up.pt/fpceup/pt/pub_geral.pub_view?pi_pub_base_id=300639 | **Leyenda:** Berlín y Galipedia dan *RICHIARI REGES*; *GCiencia* [A] escribe *RECHIARI REGIS*: usar la del museo. Berlín la llama "el testimonio más antiguo del nombre de un soberano en monedas de la época de las migraciones", pero señala que la autenticidad **de su ejemplar** está discutida (¿copia fundida del de París?). "Seis" sale del título de Barroca, sin leer el artículo |
| 3 | «Cando morreu o rei suevo Requila, en 448, sucedeuno o seu fillo, Requiario, "católico", escribiu o bispo Hidacio. Medio século antes de Clodoveo.» | [A] Hidacio, *Chronicon* (latín y traducción): https://www.condadodecastilla.es/cultura-sociedad/fuentes-historicas/cronicon-de-hidacio/ | **El "primero" hay que matizarlo:** Orosio (7.32.13 [A]: https://www.attalus.org/translate/orosius7B.html) dice que los burgundios ya habían abrazado la fe católica hacia 417, aunque la crítica moderna lo descarta en general (StudyLight, citando la Gallic Chronicle [C]). Forma segura: «un dos primeiros reis xermánicos católicos, se non o primeiro». El reino volvió al arrianismo (Áyax, hacia 465) y se reconvirtió en 550-560 |
| 4 | «No ano 409, escribiu un bispo galego, Hidacio, alanos, vándalos e suevos entraron en Hispania. Os suevos quedaron aquí, no noroeste, e durante case douscentos anos Braga foi a capital dun reino.» | [A] Hidacio (enlace del gancho 3); [A] Galipedia, Reino suevo: https://gl.wikipedia.org/wiki/Reino_suevo | Hidacio data por la "era" hispánica (447 = año 409). El *foedus* con Roma es de 410-411 "probablemente" (Galipedia). Fin del reino: 585 (Leovigildo). Galipedia [A] dice que el *Parochiale Suevorum* (c. 569: 13 diócesis y 134 parroquias) "condicionó" la red parroquial posterior: la continuidad directa con las parroquias actuales es una **hipótesis** y no sirve de gancho |
| 5 | «Os suevos fundaron o primeiro reino medieval da Europa occidental continental.» (solo con matiz) | [A] Galipedia, Reino suevo: https://gl.wikipedia.org/wiki/Reino_suevo | **Afirmación discutible** (depende de cómo se cuente el *foedus* de 411 frente al reino visigodo de Tolosa de 418). Si se usa: «hai quen o considera…» |

### Referencias clave

- [A] Hidacio, *Chronicon* (fuente contemporánea única para Requiario). https://www.condadodecastilla.es/cultura-sociedad/fuentes-historicas/cronicon-de-hidacio/
- [A] Münzkabinett Berlin, silicua de Requiario (con bibliografía: Kluge 2007; Barroca 2017; Reinhart 1937). https://nat.museum-digital.de/object/544236
- [C] Barroca, M. J. (2017), *Nummus* 40, pp. 29-45: los seis ejemplares conocidos.
- [A] CCG, *Lugares de memoria*, Martiño de Dumio (c. 510-579; "descendente de panonios", no nacido en Panonia;
  concilios de 561 y 572). https://consellodacultura.gal/lugares-de-memoria/detalle.php?id=34417
- [A] Galipedia, Reino suevo y Requiario (índice; cita a Isidoro, *Historia Suevorum*). https://gl.wikipedia.org/wiki/Requiario
- [A] Orosio, *Historiae* 7.32.13 (traducción inglesa en attalus.org) para el matiz de los burgundios.
- [C] Martín de Braga, *De correctione rusticorum* (texto latino y traducción por localizar; resumen en
  https://en.wikipedia.org/wiki/De_correctione_rusticorum).
- [C] RAH, *Historia Hispánica*, "Requiario" (la página no cargó con WebFetch). https://historia-hispanica.rah.es/biografias/38639-requiario
- [C] Pablo C. Díaz, *El reino suevo (411-585)*, Akal, 2011 (monografía de referencia, citada de memoria por Claude:
  comprobar ficha).

### Puntuación

- **G 4:** la moneda y los días de la semana son buenos y verdaderos; los "primeros" exigen matices que restan pegada.
- **S 4:** guerras y la ejecución de Requiario (456): se nombran sin detalles.
- **V 2:** poca iconografía material (una moneda, Braga, Dumio); SDXL pinta "bárbaros" de cómic y cascos con cuernos:
  riesgo alto de imágenes absurdas.
- **F 4:** fuente primaria (Hidacio) y numismática seria; bibliografía académica a mano.
- **I 4:** muy galego-portugués; menos reconocible para el público general que castros o meigas.
- **E 2:** sin fecha natural (la fiesta de san Martiño de Dumio es el 20-3 [C]).

### Riesgos

- Repetir "primeiro reino católico de Europa" sin matiz (*GCiencia* y Galipedia lo afirman sin fuente académica).
- Símbolos "suevos" (escudos, banderas) inventados por genealogistas del siglo XVII (lo advierte Galipedia [A]).
- Nacionalismo retrospectivo ("o primeiro reino de Galicia"): el reino abarcaba también el norte de Portugal, con
  capital en Braga.
- El periodo 470-550 es casi oscuro: no rellenarlo con invenciones.

### Consultas de YouTube

- `reino suevo Galicia` · `suevos Gallaecia historia`
- `reino suevo documental` · `Requiario moneda`
- `reino suevo Braga história` (pt) · `Suebi kingdom Gallaecia` (en)

---

## 4. Santa Marta de Ribarteme e as romarías máis raras

### Ángulo y arco

**Ángulo:** "Ir de vivo ou ir de morto": las romerías donde se paga una promesa con el cuerpo (en ataúd, con figuras
de cera, con una piedra en el milladoiro). La sorpresa: Ribarteme y Teixido. La calma, el camino a pie, la cera, los
cantos, la comida en el campo.

1. **Gancho:** cadaleitos con vivos dentro (As Neves, 29 de julio).
2. **Santa Marta:** la devoción, la primera noticia escrita (1700) y el santuario (1805).
3. **A cera:** exvotos de cera (piernas, cabezas, casas, animales); los cereros de Covelo; Galicia como último
   lugar donde siguen vivos.
4. **Santo André de Teixido:** "vai de morto quen non foi de vivo", el testamento de 1391, las piedras, la herba de
   namorar, los sanandresiños de miga de pan.
5. **Outras romarías de exvotos:** Amil, A Franqueira, Monte Medo, San Campio, Santa Minia (lista del estudio de
   Fuentes Alende), en tono descriptivo.
6. **O presente:** la prohibición de 2022, la vuelta parcial de 2023; cierre en el camino de vuelta, al anochecer.

### Ganchos para el primer minuto

| # | Gancho (galego) | Fuente | Notas de discrepancia |
|---|---|---|---|
| 1 | «Cada 29 de xullo, nas Neves, hai xente viva que fai a procesión metida nun cadaleito, levada a ombros pola súa familia. Non é unha broma: é unha promesa a Santa Marta por saír dunha doenza grave.» | [A] Turismo de Galicia: https://www.turismo.gal/recurso/-/detalle/200312000146/romaria-de-santa-marta-de-ribarteme?langId=en_US&tp=97&ctre=261 ; [A] es.wikipedia: https://es.wikipedia.org/wiki/Procesi%C3%B3n_de_Santa_Marta_de_Ribarteme | **Estado actual:** en 2022 el párroco suprimió la procesión (Nós Diario [A]); en 2023 volvió con dos ataúdes (uno con un vivo dentro) y saliendo de la carretera, no de la iglesia (*Diario de Pontevedra* [A]). Comprobar 2024-2026 antes de decir "cada ano". Fecha de la supresión: 2021 (es.wikipedia) o 2022 (Nós Diario): usar la de la prensa |
| 2 | «A primeira noticia escrita é de 1700: un bispo de Tui mandou arranxar a capela co diñeiro das ofrendas dos romeiros.» | [A] es.wikipedia (enlace de arriba) | Solo es.wikipedia y prensa [C]; falta la fuente primaria (libro de fábrica o visita pastoral del obispado de Tui). Marcar como "segundo se conta" hasta tenerla |
| 3 | «En 1391, unha viúva de Viveiro deixou escrito no testamento que alguén fose por ela en romaxe a Santo André de Teixido. Porque, como di o refrán, "vai de morto quen non foi de vivo".» | [A] Galipedia, Santo André de Teixido: https://gl.wikipedia.org/wiki/Santo_Andr%C3%A9_de_Teixido | Buscar el documento original (citado en Galipedia). Es un gancho tierno, no macabro |
| 4 | «Galicia é a única comunidade de España onde a cera segue a cumprir a función para a que naceu: pernas, brazos, cabezas e ata casas de cera que se levan ao santo.» | [A] *Galicia Confidencial*, 14-10-2024 (entrevista a José Fuentes Alende): https://www.galiciaconfidencial.com/noticia/5485185-galicia-unico-recuncho-espana-onde-as-persoas-seguen-ofrecendo-obsequios-aos-santos-aos-encomendan | Es la opinión de un investigador (exsecretario técnico del Museo de Pontevedra), no un censo: atribuirla. La nota dice que las *Cantigas de Santa María* son del siglo XIV; son de la segunda mitad del XIII [S]: no repetir el siglo de la nota |
| 5 | «Nas Neves din que Santa Marta é a avogada dos que estiveron a piques de morrer… porque era irmá de Lázaro.» | [A] es.wikipedia (devoción a Santa Marta) | El resumen de es.wikipedia es confuso (atribuye a Marta una resurrección). En el Evangelio quien resucita a Lázaro es Jesús; Marta es su hermana. Decirlo así |

### Referencias clave

- [A] Turismo de Galicia, ficha oficial de la romería (Fiesta de Interés Turístico de Galicia).
- [A] *Nós Diario*, 29-7-2022: supresión por el párroco, con citas.
  https://www.nosdiario.gal/articulo/cultura/adeus-procesion-ataudes-nas-neves/20220729111616148782.amp.html
- [A] *Diario de Pontevedra*, 29-7-2023: vuelta con dos ataúdes.
  https://www.diariodepontevedra.es/articulo/comarcas/regresa-procesion-cadaleitos-santa-marta-ribarteme/202307291903161264508.html
- [A] Galipedia, Santo André de Teixido (testamento de 1391, ritos).
- [A] *Galicia Confidencial* (2024), Fuentes Alende y la cera votiva.
- [C] José Fuentes Alende, *Los exvotos en Galicia. Su significación en la religiosidad popular* (2 vols., prólogo de
  J. M. González Reboredo, del Museo do Pobo Galego): referencia académica principal.
  https://museo.depo.gal/en/-/actividade-presentacion-do-libro-los-exvotos-en-galicia
- [C] Campo Galego, "O patrimonio apícola cereiro en Galicia" (cereros de Covelo).
  https://www.campogalego.gal/o-patrimonio-apicola-cereiro-en-galicia/
- [C] Archivo de exvotos (revista *Sans Soleil*), Teixido. http://archivoexvotos.revista-sanssoleil.com/san-andres-de-teixido/

### Puntuación

- **G 5:** "xente viva nun cadaleito" es de los ganchos más fuertes del país, y es verdad.
- **S 3:** el tema es la muerte y la enfermedad; hay que tratarlo como gratitud y camino, nunca como terror.
- **V 3:** ataúdes y figuras de cera en SDXL pueden salir siniestros o grotescos; mejor caminos, velas, ermitas y
  milladoiros.
- **F 3:** mucha prensa y poca fuente primaria abierta (falta el documento de 1700 y el libro de Fuentes Alende).
- **I 5:** religiosidad popular muy galega.
- **E 5:** publicar entre el 10 y el 20 de julio (romería el 29-7); Teixido el 8 de septiembre sirve de segunda
  ventana.

### Riesgos

- Orígenes "precristianos" o "celtas" de la procesión (algunas webs): sin fuente, no decirlo.
- Polémica viva entre la parroquia, la diócesis de Tui-Vigo y el vecindario: contarla sin tomar partido.
- No mostrar personas reales identificables ni ataúdes con cara dentro (derechos de imagen y tono).
- **O Corpiño** y otras romerías de "endemoniados" (dato de memoria de Claude, sin comprobar): fuera del episodio por
  tono.

### Consultas de YouTube

- `Santa Marta de Ribarteme` · `procesión de los ataúdes Galicia`
- `romería de los ataúdes As Neves` · `San Andrés de Teixido vai de morto`
- `coffin procession Galicia` (en) · `romaria dos caixões Galiza` (pt)

---

## 5. Hórreos e cruceiros: a pedra que fala

### Ángulo y arco

**Ángulo:** "Un hórreo por quilómetro cadrado": el paisaje de piedra que todos ven y pocos saben leer. La sorpresa: la
pelea por el hórreo más largo, cuántos hay de verdad y el misterio de quién talló el cruceiro de Hío. La calma: la
cosecha, el maíz secándose, la piedra al atardecer. Muy apto para dormir.

1. **Gancho:** cuál es el hórreo más largo (Araño, Lira, Carnota) y una miniatura del siglo XIII.
2. **Para que serve un hórreo:** grano, ventilación, los *tornarratos*; nombres locales (cabazo, canastro, piorno…).
3. **Os gigantes:** Carnota (1768-1783), Lira (1779-1814), Araño (s. XVII).
4. **Cantos hai:** de 9.351 a 30.355 solo en la provincia de A Coruña; la declaración del Ministerio (2026).
5. **Os cruceiros:** Castelao y *As cruces de pedra na Galiza* (1950); qué representan.
6. **Hío:** el cruceiro de 1872 tallado casi en un solo bloque y la duda sobre el autor (José o Ignacio Cerviño).
   Cierre.

### Ganchos para el primer minuto

| # | Gancho (galego) | Fuente | Notas de discrepancia |
|---|---|---|---|
| 1 | «Durante moito tempo dixemos que o hórreo máis longo de Galicia era o de Carnota. Non o é. Mide trinta e catro metros e setenta e seis centímetros; o de Lira, a poucos quilómetros, trinta e seis e medio; e o do Araño, en Rianxo, trinta e sete.» | [A] Concello de Carnota: https://www.carnota.gal/tourism/patrimonio/horreos/?lang=en ; [A] Praza Pública (Marcos Pérez Pena): https://praza.gal/ducias/horreos-que-son-patrimonio-cultural-e-identidade-de-galicia | Araño 37,05 m según un resultado de búsqueda [C]; Praza dice "37 m" y "século XVII" [A]; la búsqueda decía "mediados do XVII" [C]. El Araño **no tiene pés**: se apoya en un muro, y por eso algunos no lo comparan. *El Correo Gallego* (2024) lo llama "o máis longo do mundo" [A]: no repetirlo. Ojo: el "Araújo" del encargo es el **Araño** |
| 2 | «Nun libro pintado para Afonso X hai setecentos cincuenta anos aparecen uns celeiros sobre pés de pedra que moitos len como os hórreos máis antigos debuxados.» | [A] Base de datos de las Cantigas (Oxford), cantiga 187 y sus miniaturas: https://csm.mml.ox.ac.uk/index.php?p=poemdata_view&rec=187 | La cantiga ocurre **en Jerusalén** (graneros que la Virgen llena de trigo). Lo de "primera representación de un hórreo" sale de un resultado de búsqueda [C]: es una lectura, no un hecho. Ver la miniatura antes de usarlo |
| 3 | «Ninguén sabe cantos hórreos hai en Galicia. Un investigador contou trinta mil trescentos cincuenta e cinco só na provincia da Coruña.» | [A] *El Correo Gallego*, 29-9-2024 (atlas de Carlos Regueira): https://www.elcorreogallego.es/concellos/2024/09/29/atlas-cataloga-30-000-horreos-108694518.html | Cifras para toda Galicia: 30.000 (Turismo de Galicia [C]) y 100.000 (Praza [A]). El atlas de 2017 de Regueira recogía 9.351 en toda Galicia. Decir "non hai censo oficial" |
| 4 | «O cruceiro do Hío, de 1872, está tallado case enteiro nun só bloque de granito: Adán e Eva, as ánimas, a Virxe e, arriba, o descendemento da cruz. E aínda discutimos quen o fixo.» | [A] Concello de Cangas: https://cangas.gal/es/areas/turismo/etnografico/crucero-de-o-hio ; [A] The Genealogy Corner (2013): https://thegenealogycorner.com/2013/12/08/who-really-built-the-cruceiro-de-hio/ | Autoría: José Cerviño García ("Pepe da Pena", tradición oral) frente a Ignacio Cerviño Quinteiro (historiadores desde los años 60, según el blog). El blog es de un descendiente, no académico: atribuir. El Concello de Cangas dice "maestro Cerviño" sin nombre. "En gran parte" de un bloque (Cangas), no "entero" |
| 5 | «En abril de 2026, o Ministerio de Cultura declarou os hórreos do norte peninsular patrimonio cultural inmaterial.» | [A] Telecinco, 7-4-2026: https://www.telecinco.es/noticias/galicia/20260407/expertos-propietarios-celebran-declaracion-horreos-norte-peninsular-patrimonio-cultural_18_018812985.html | Falta la resolución en el BOE [C] y el nombre exacto de la figura ("Manifestación Representativa del Patrimonio Cultural Inmaterial" [S]). Buscarla antes de usarla |

### Referencias clave

- [A] Concello de Carnota, hórreos de Carnota y Lira (fechas, medidas, 22 pares de pés, ≈ 900 hórreos en el municipio).
- [A] Praza Pública, una docena de hórreos (Araño, Poio, A Merca, Quins; Castelao y el emblema de Nós).
- [A] *El Correo Gallego*, atlas de Carlos Regueira (2024).
- [A] Concello de Cangas, cruceiro do Hío (iconografía, granito de Liméns).
- [A] Cantigas de Santa María Database (Oxford), cantiga 187.
- [C] Castelao, *As cruces de pedra na Galiza* (Buenos Aires, 1950; facsímiles de Akal, 1975, y Galaxia, 1984); estudio
  en el *Boletín da RAG*: https://publicacionsperiodicas.academia.gal/index.php/BRAG/article/view/920
- [C] horreosdegalicia.com/estudio (metodología de catálogo). https://horreosdegalicia.com/estudio/
- [C] Turismo de Galicia, "Galicia, the land of the 30,000 hórreos". https://blog.turismo.gal/galicia-the-land-of-the-30000-horreos/
- [C] es.wikipedia, José Cerviño García (autoría del Hío). https://es.wikipedia.org/wiki/Jos%C3%A9_Cervi%C3%B1o_Garc%C3%ADa

### Puntuación

- **G 3:** hay datos curiosos (ranking, censos, autoría), pero el tema es conocido y no despierta un "non vas crer".
- **S 5:** piedra, cosecha y paisaje: ideal para dormir.
- **V 4:** muy fotogénico; SDXL conoce mal la forma del hórreo galego (puede pintar casetas o graneros alpinos) y los
  cruceiros con figuras se deforman: necesita revisión o ControlNet [S].
- **F 4:** fuentes municipales y de prensa buenas; Castelao como clásico; falta un estudio académico abierto sobre
  hórreos.
- **I 5:** el hórreo y el cruceiro son iconos de Galicia.
- **E 3:** septiembre-octubre (cosecha, maíz) [S].

### Riesgos

- "O hórreo máis longo do mundo": no repetirlo. Precisar con qué criterio se mide (con pés o sin ellos).
- Constructor del hórreo de Lira: un resultado de búsqueda nombra a Gregorio Quintela [C]; la web municipal no da
  constructores. No dar nombres.
- *As cruces de pedra na Galiza* se publicó en enero de 1950 y Castelao murió el 7-1-1950: "póstumo" o no depende del
  día exacto; no decirlo.
- Cruceiros con ánimas del purgatorio: describir con calma, sin truculencia.

### Consultas de YouTube

- `hórreos de Galicia` · `hórreo de Carnota`
- `cruceiro de Hío` · `cruceiros galegos Castelao`
- `Galician hórreos history` (en) · `espigueiros e canastros Galiza` (pt)

---

## 6. O Entroido galego: peliqueiros, cigarróns, pantallas e felos

### Ángulo y arco

**Ángulo:** "O Entroido que non se deixou prohibir": las máscaras del sur de Ourense, explicadas desde dentro (cómo
se viste un peliqueiro, qué suenan las *chocas*, qué es la farrapada), con el hilo de la prohibición de 1937 que el
rural no cumplió. La sorpresa son las formigas, las vejigas, el BOE de 1937 y la palabra de 1251. La calma llega en la
segunda mitad: el silencio del miércoles de Ceniza, el pueblo que vuelve a su vida.

1. **Gancho:** formigas vivas en la plaza de Laza; una orden de 1937 que suspendía "en absoluto" el Carnaval.
2. **A palabra:** *entroido* < *introitus*, documentada en 1251; variantes (antroido, entruido…).
3. **Vestirse:** peliqueiro (Laza), cigarrón (Verín), felo (Maceda), pantalla (Xinzo): máscaras, chocas, pesos.
4. **O calendario:** los domingos de Xinzo (Fareleiro, Oleiro, Corredoiro, Piñata); el Luns Borralleiro de Laza; el
   testamento del burro.
5. **Prohibido e vivo:** 1937, 1940, la Guardia Civil que no subía a las aldeas (testimonios de Maceda).
6. **Hoxe:** BIC de 2025, fiestas de interés turístico; cierre en la Cuaresma silenciosa.

### Ganchos para el primer minuto

| # | Gancho (galego) | Fuente | Notas de discrepancia |
|---|---|---|---|
| 1 | «En Laza, o luns de Entroido, os mozos baixan á praza da Picota cunha vaca de madeira, a Morena… e con formigas vivas, que botan por riba da xente.» | [A] Galipedia, Entroido de Laza: https://gl.wikipedia.org/wiki/Entroido_de_Laza | El resumen de Galipedia dice "formigas (elementos recollidos)"; la búsqueda [C] (Vigopeques, mundo-r) dice formigas vivas con terra y fariña. Confirmar en una fuente seria (Concello de Laza o un estudio etnográfico) |
| 2 | «O 3 de febreiro de 1937, desde Valladolid, unha orde mandou "suspender en absoluto as festas de Carnaval". Nas aldeas do sur de Ourense, moitos seguiron saíndo coas máscaras.» | [A] *BOE* nº 108, 5-2-1937, orden del Gobierno General firmada por Luis Valdés (texto extraído del PDF por Claude): https://www.boe.es/gazeta/dias/1937/02/05/pdfs/BOE-1937-108.pdf ; [A] VigoÉ, 27-2-2022 (testimonios de Xinzo y Maceda): https://www.vigoe.es/actualidad/el-magico-carnaval-gallego-que-resistio-a-las-prohibiciones/ | La orden cita la guerra ("los que sufren los rigores de la guerra"): mencionarla sin detalle. La continuidad "nunca se perdeu" es testimonio oral (Maceda): atribuir. En 1940 se mantuvo la prohibición (Serrano Suñer, resultado de búsqueda [C]) |
| 3 | «As pantallas de Xinzo levan na man dúas vexigas de vaca, inchadas e secas. Coas vexigas petan, e o son que fan é o do Entroido da Limia.» | [C] Resultados de búsqueda (xinzodelimia.com, galiciadigital) | **Falta abrir una fuente.** Comprobar en https://xinzodelimia.com/o-entroido-de-xinzo/ o en el Museo Galego do Entroido. Normativo: *vexiga* (RAG) [S]; el encargo dice "bexigas" |
| 4 | «A palabra Entroido vén do latín *introitus*, a entrada. Xa aparece escrita en galego en 1251.» | [A] *GCiencia*, 27-2-2025 (Gloria Montenegro, citando a Antón Santamarina): https://www.gciencia.com/perspectivas/entroido-antroido-ou-entruido-as-formas-de-falar-en-galego-da-gran-festa-das-mascaras/ | No se nombra el documento de 1251: buscarlo (TMILG o Santamarina) antes de usar el año. "Entrada" ¿en la Cuaresma? (versión habitual) o ¿en la primavera? (otra hipótesis [C]) |
| 5 | «Dise que o Entroido de Xinzo é o máis longo de Europa: cinco semanas.» (solo con matiz) | [C] Búsqueda (varias webs) | "O máis longo de Europa" es reclamo turístico sin fuente. Galipedia dice que el de Laza es "o máis longo da provincia" [A]. Si se usa: «En Xinzo o Entroido dura cinco domingos» |

### Referencias clave

- [A] *BOE* nº 108 (5-2-1937), orden de suspensión del Carnaval (fuente primaria).
- [A] Xunta, nota del 20-1-2024 (incoación del BIC) y *Diario do Limia*, 11-3-2025 (declaración en el DOG): el
  Entroido galego es BIC inmaterial desde 2025. https://www.xunta.gal/es/notas-de-prensa/-/nova/86961/xunta-reconoce-entroido-gallego-como-ben-interese-cultural-maxima-proteccion ·
  https://www.diariodolimia.gal/articulo/cultura/entroido-gallego-es-interes-cultural-bic/20250311212019036701.html
  (falta el decreto en el DOG [C]).
- [A] Galiciapress, 24-9-2025: Xinzo es Fiesta de Interés Turístico Internacional (2019), Verín Nacional, Laza y
  Maceda de Galicia. https://www.galiciapress.es/articulo/ultima-hora/2025-09-24/5444154-gobierno-entrega-diploma-fiesta-interes-turistico-nacional-entroidos-oriente-ourensano
- [A] Galipedia, Entroido de Laza (calendario y personajes).
- [A] *GCiencia*, etimología y variantes (con Antón Santamarina, de la RAG).
- [A] VigoÉ (2022), testimonios orales sobre la prohibición.
- [C] Felos de Maceda, web de la asociación (origen y traje). https://felosdemaceda.com/felos-orixe/
- [C] Museo Galego do Entroido (Xinzo de Limia).
- [C] Expediente de la incoación del BIC en el DOG (25-1-2024): descripción etnográfica oficial, con bibliografía.

### Puntuación

- **G 5:** formigas, vejigas, una orden de 1937 y la palabra de 1251: verdaderos y muy visuales.
- **S 3:** fiesta ruidosa (chocas, látigos, fuego del Folión, harina, barro); para dormir hay que contarla desde la
  víspera o la memoria, y bajar el tono pronto.
- **V 3:** las máscaras son muy galegas, pero SDXL no conoce el peliqueiro ni el cigarrón y pintará máscaras
  venecianas o de terror; necesitará referencias o planos sin rostro (chocas, calles, harina).
- **F 4:** fuente primaria (BOE), Xunta y RAG; faltan estudios etnográficos abiertos.
- **I 5:** el Entroido de Ourense es de lo más singular de Galicia.
- **E 5:** publicar en la segunda quincena de enero de 2027 (Entroido del 7 al 9-2-2027; Xinzo empieza semanas antes).

### Riesgos

- Orígenes "prerromanos", "lupercales" o "celtas" de las máscaras: todo es hipótesis; contarlo como tal.
- Cigarrones "recaudadores del conde de Monterrei": leyenda local sin documento; "dise que…".
- No describir los golpes de látigo como violencia; es un juego ritual con normas.
- La prohibición franquista se menciona con un hecho y una fecha, sin entrar en represión.

### Consultas de YouTube

- `Entroido de Laza peliqueiros` · `cigarróns Verín`
- `Entroido Xinzo pantallas` · `carnaval ancestral Galicia documental`
- `Galician carnival masks peliqueiros` (en) · `entrudo galego caretos` (pt)

---

## 7. O magosto e os soutos: a castaña antes da pataca

### Ángulo y arco

**Ángulo:** "O pan dos pobres": la castaña fue durante siglos el alimento base de Galicia; la pataca y el millo la
desplazaron, y una enfermedad invisible (la tinta) se llevó la mayor parte de los soutos. Hoy los castiñeiros
galegos son un refugio genético europeo. La sorpresa son los datos de la pérdida y del origen autóctono; la calma, el
otoño, el lume, el souto al atardecer. Es el tema más "de dormir" del grupo.

1. **Gancho:** "a castaña era o pan dos pobres" (1903); Galicia perdió hasta el 80 % de sus castaños.
2. **Un árbore máis vello que Roma:** el castaño ya estaba aquí (refugio glaciar, Lourizán 2021); los romanos lo
   difundieron.
3. **O souto:** vida en torno al castiñeiro (madera, *ourizos*, *sequeiros*, castañas pilongas), rentas de los
   monasterios.
4. **Chega a pataca:** Lucas Labrada (1804) y el hambre de 1768; el millo en el siglo XIX.
5. **A tinta:** de la costa al interior (siglos XVIII-XIX), Petri (1917), Elorrieta (1949).
6. **O magosto:** el lume, San Martiño, la palabra (etimología discutida). Cierre al lado del fuego.

### Ganchos para el primer minuto

| # | Gancho (galego) | Fuente | Notas de discrepancia |
|---|---|---|---|
| 1 | «"A castaña era o pan dos pobres." Escribiuno en 1903 un médico de Pontevedra, Leopoldo Salgueso, cando os castiñeiros de Galicia morrían sen que ninguén soubese por que.» | [A] Viéitez Cortizo *et al.*, *O castiñeiro: bioloxía e patoloxía*, Consello da Cultura Galega, 1999, cap. "A enfermidade da tinta" (PDF leído por Claude): https://consellodacultura.gal/mediateca/extras/CCG_1999_Castineiro-O-bioloxia-e-patoloxia.pdf | La cita está en galego en el libro del CCG; el texto original de 1903 será probablemente en castellano [S]: decir "escribiu, máis ou menos, que…" o buscar el original. Salgueso culpaba a los insectos; el hongo se identificó en 1917 |
| 2 | «Na primeira metade do século vinte, Galicia perdeu ata oito de cada dez castiñeiros por unha doenza que lles podrecía as raíces: a tinta.» | [A] Mismo libro del CCG, apartado "A tinta en España" (cita a Elorrieta, 1949: "Galicia perdeu ata o 80 %") | Es una **estimación de Elorrieta (1949)**, no un censo: atribuirla. "Primera mitad del siglo XX" es la fecha de la estimación; la regresión empezó antes (costa, siglos XVII-XIX, según Bouhier). Mejor: «cando se fixo a conta, en 1949, Galicia perdera ata…» |
| 3 | «O castiñeiro non o trouxeron os romanos. Xa estaba aquí: os da Galicia atlántica están entre os máis puros de Europa, refuxio dunha árbore que sobreviviu ás glaciacións.» | [A] *GCiencia*, 19-7-2021 (Centro de Investigación Forestal de Lourizán; *Molecular Ecology*): https://www.gciencia.com/medioambiental/os-castineiros-da-galicia-atlantica-un-refuxio-xenetico-milenario/ | **Discrepancia oficial:** el pliego de la IXP Castaña de Galicia (DOG 20-12-2024 [A]) dice que el cultivo "parece estar relacionado coa chegada das lexións romanas". No se contradicen del todo: árbol autóctono, cultivo y variedades difundidos por Roma. Decirlo así |
| 4 | «Antes de 1768, ano de fame e peste en Galicia, a pataca case non se cultivaba. Despois, estendeuse.» | [A] *Diario de Pontevedra*, 21-10-2024 (cita a Lucas Labrada, *Descripción económica del Reyno de Galicia*, 1804): https://www.diariodepontevedra.es/gl/articulo/gastronomia/castana-alimento-milenario-que-reinaba-antes-pataca/202410211752521325450.html | Labrada hablaba de la provincia de Mondoñedo. Abrir el original en Galiciana [C]: http://biblioteca.galiciana.gal/es/consulta/registro.do?id=410681 |
| 5 | «Nos mosteiros medievais, despois do viño, a renda que máis daba eran os soutos.» | [A] DOG 20-12-2024, pliego de la IXP Castaña de Galicia (vínculo con el medio; ejemplo de San Vicenzo de Pombeiro): https://www.xunta.gal/dog/Publicados/2024/20241220/AnuncioG0528-111224-0002_gl.html | Es un ejemplo (Pombeiro), no una regla de todos los monasterios. Une con el tema 1 |

**De reserva:** el castiñeiro de Pumbariños (Souto de Rozavales, Manzaneda), monumento natural por el Decreto
78/2000, con ≈ 13 m de perímetro; su edad oscila entre "uns 500" y "mil anos" según la fuente [C]: decir "centenario"
y nada más. Hoy Galicia produce más de la mitad de la castaña de España (Xunta, 25-6-2024 [A]:
https://www.xunta.gal/es/notas-de-prensa/-/nova/003070/medio-rural-refuerza-colaboracion-con-indicacion-xeografica-protexida-castana).

### Referencias clave

- [A] Viéitez Cortizo, Viéitez Madriñán y Viéitez Madriñán, *O castiñeiro: bioloxía e patoloxía* (CCG, 1999): historia
  del castaño en Galicia, la tinta, Bouhier, Molina, Elorrieta. Fuente institucional principal.
- [A] DOG 20-12-2024, pliego de condiciones de la IXP Castaña de Galicia (historia, Catastro de Ensenada, Dumas,
  Pombeiro).
- [A] *GCiencia* (2021), refugio genético (Lourizán, *Molecular Ecology*).
- [A] *Diario de Pontevedra* (2024), castaña y pataca, con cita de Labrada.
- [A] Xunta, nota de prensa del 25-6-2024 (más de la mitad de la producción española).
- [A] As chaves da lingua, etimología de *magosto*: "controvertida" (*magnus ustus* frente a *agostar*). https://aschavesdalingua.gal/a-orixe-da-palabra-magosto/
- [C] Lucas Labrada, *Descripción económica del Reyno de Galicia* (Ferrol, 1804), en Galiciana (fuente primaria).
- [C] Abel Bouhier, *La Galice* (1979), y Elorrieta (1949), vistos citados en el libro del CCG.
- [C] Estudio sobre la patata en la Galicia de finales del Antiguo Régimen (ResearchGate):
  https://www.researchgate.net/publication/329806501 ; obra de Pegerto Saavedra en Dialnet:
  https://dialnet.unirioja.es/servlet/autor?codigo=37859
- [C] Galipedia, Souto de Rozavales y Árbores senlleiras (Decreto 67/2007). https://gl.wikipedia.org/wiki/Souto_de_Rozavales

### Puntuación

- **G 4:** "o pan dos pobres", el 80 % perdido y el árbol que no trajo Roma son verdaderos y sorprendentes, aunque menos
  espectaculares que un tesoro de oro.
- **S 5:** otoño, lume, souto, castañas asadas: el tono de dormir sale solo.
- **V 5:** soutos, erizos, hojas, fuego, *sequeiros*: SDXL los genera bien y sin rarezas.
- **F 5:** libro del CCG en PDF, DOG, Xunta e investigación de Lourizán.
- **I 5:** el magosto es una fiesta galega por excelencia.
- **E 5:** publicar en la segunda quincena de octubre o del 1 al 10 de noviembre (San Martiño, 11-N). Si "As meigas"
  sale en octubre de 2026, el magosto es el siguiente natural (principios de noviembre de 2026) o el de octubre de 2027.

### Riesgos

- "Raíz celta" y "culto aos mortos" del magosto (*Diario de Pontevedra*): hipótesis; decir "hai quen o relaciona…".
- "A pataca chamábase castaña da terra" (resultado de búsqueda [C]): sin fuente; no usarlo.
- Edad milenaria de castaños concretos: casi nunca está medida.
- Etimología de *magosto*: no darla como segura.
- No confundir la tinta (*Phytophthora*) con el chancro (*Cryphonectria*), que llegó más tarde [S].

### Consultas de YouTube

- `magosto Galicia` · `castañas Galicia historia`
- `souto castiñeiros documental` · `historia de la castaña en Galicia`
- `magusto tradição` (pt) · `chestnut Galicia tradition` (en)
