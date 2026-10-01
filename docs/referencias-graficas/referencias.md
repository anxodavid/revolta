# Referencias gráficas libres para el pipeline de ilustración

Documentación gráfica para semillas img2img / ControlNet / IP-Adapter. Fecha de recogida: 30-09-2026.

## Cómo se hizo y qué NO está comprobado

- **Automático:** consulta de metadatos a la API de Wikimedia Commons (licencia, autor, tamaño leídos de la página de cada fichero, no del buscador) y a la API de The Met Open Access. Filtro de licencia: CC0, dominio público, CC BY, CC BY-SA; se descartan NC, ND, GFDL-solo y similares. Ver `herramientas/referencias/` (scripts y metadatos en bruto en `datos/`).
- **No hecho:** revisión visual de las imágenes (Commons limitó las descargas de miniaturas). Las columnas `idoneidad_img2img` / `idoneidad_controlnet` son una **estimación automática** (palabras del título, resolución, categoría «Quality images»), no un juicio humano. Hay que mirar las imágenes antes de usarlas: objeto completo, fondo limpio, sin personas reconocibles.
- **No cubierto por límites de acceso:** Europeana, Flickr Commons, Library of Congress, BNE (BDH devuelve 403 desde este entorno), Galiciana, Museo do Pobo Galego, Rijksmuseum. Figuran en «Fuentes a pedir / revisar».
- Las licencias **CC BY-SA** están marcadas en `notas`. Las marcadas «Public domain» en Commons deben verificarse en su página.
- `descargar.sh` baja las elegidas una a una (pausa y reintentos). Las originales >2500 px se bajan a 1920 px de ancho.

Entregables: [`referencias.csv`](referencias.csv) (226 candidatas), [`descargar.sh`](descargar.sh).

## Mejores por concepto (3-5)

### 01. Hórreo gallego  (16 candidatas)
- [2018. Combarro, Poio. Galiza-4.jpg](https://commons.wikimedia.org/wiki/File:2018._Combarro,_Poio._Galiza-4.jpg) · Luis Miguel Bugallo Sánchez (Lmbuga) · CC BY-SA 4.0 · 3411x5122
- [Horreos-Galicien-IMG 0274a.jpg](https://commons.wikimedia.org/wiki/File:Horreos-Galicien-IMG_0274a.jpg) · Christof46 · CC0 · 4000x6000
- [Conxunto horreos.jpg](https://commons.wikimedia.org/wiki/File:Conxunto_horreos.jpg) · Anxo The original uploader was Xelo2004  · CC BY-SA 3.0 · 1184x896
- [2013. Hórreo en Cambados. Galicia (Spain).jpg](https://commons.wikimedia.org/wiki/File:2013._H%C3%B3rreo_en_Cambados._Galicia_(Spain).jpg) · Luis Miguel Bugallo Sánchez (Lmbuga) · CC BY-SA 3.0 · 5666x3777
- [Camino de Santiago, Lugo, España, 2015-09-20, DD 25.jpg](https://commons.wikimedia.org/wiki/File:Camino_de_Santiago,_Lugo,_Espa%C3%B1a,_2015-09-20,_DD_25.jpg) · Diego Delso · CC BY-SA 4.0 · 8449x5633

### 02. Carro de bois  (16 candidatas)
- [A Arnoia - Carro á beira do Miño - Galiza-3.jpg](https://commons.wikimedia.org/wiki/File:A_Arnoia_-_Carro_%C3%A1_beira_do_Mi%C3%B1o_-_Galiza-3.jpg) · Lmbuga (Luis Miguel Bugallo Sánchez) · CC BY-SA 3.0 · 5379x3587
- [Carros tradicionais na praia de Peralta. O Grove. Galiza-2.jpg](https://commons.wikimedia.org/wiki/File:Carros_tradicionais_na_praia_de_Peralta._O_Grove._Galiza-2.jpg) · Luis Miguel Bugallo Sánchez (Lmbuga) · CC BY-SA 4.0 · 5527x1690
- [Carros na praia de Peralto. Galicia. Galiza. Galicia.jpg](https://commons.wikimedia.org/wiki/File:Carros_na_praia_de_Peralto._Galicia._Galiza._Galicia.jpg) · Luis Miguel Bugallo Sánchez (Lmbuga) · CC BY-SA 4.0 · 3500x2333
- [Festa da Malla 2022, 17c.jpg](https://commons.wikimedia.org/wiki/File:Festa_da_Malla_2022,_17c.jpg) · Lameiro · CC BY-SA 4.0 · 3088x2056
- [Meaño, Coirón 01-01c.jpg](https://commons.wikimedia.org/wiki/File:Mea%C3%B1o,_Coir%C3%B3n_01-01c.jpg) · Lameiro · CC BY-SA 4.0 · 3088x2056

### 03. Palloza y casa rural de granito/lousa  (16 candidatas)
- [El Cebreiro palloza ni.JPG](https://commons.wikimedia.org/wiki/File:El_Cebreiro_palloza_ni.JPG) · Nicolás Pérez · CC BY-SA 3.0 · 3264x2448
- [El Cebreiro Lugo palloza ni.jpg](https://commons.wikimedia.org/wiki/File:El_Cebreiro_Lugo_palloza_ni.jpg) · Nicolás Pérez · CC BY-SA 3.0 · 3264x2448
- [Pallozas en Piornedo.JPG](https://commons.wikimedia.org/wiki/File:Pallozas_en_Piornedo.JPG) · Vicente Maza Gómez · CC BY-SA 3.0 · 2048x1536
- [Ancares 1976 63.jpg](https://commons.wikimedia.org/wiki/File:Ancares_1976_63.jpg) · LBM1948 · CC BY-SA 4.0 · 4421x2061
- [Conxunto etnográfico das pallozas do Cebreiro.jpg](https://commons.wikimedia.org/wiki/File:Conxunto_etnogr%C3%A1fico_das_pallozas_do_Cebreiro.jpg) · Pacopac · CC BY-SA 4.0 · 5184x3888

### 04. Pazo gallego  (16 candidatas)
- [Pazo de Mariñán, fachada capilla.jpg](https://commons.wikimedia.org/wiki/File:Pazo_de_Mari%C3%B1%C3%A1n,_fachada_capilla.jpg) · Ird ge · CC BY-SA 3.0 es · 2400x3600
- [Pazo de Mariñán, Fachada Capilla.jpg](https://commons.wikimedia.org/wiki/File:Pazo_de_Mari%C3%B1%C3%A1n,_Fachada_Capilla.jpg) · Ird ge · CC BY-SA 3.0 es · 2592x3888
- [Entrada da Capela do Pazo de Rioboo.JPG](https://commons.wikimedia.org/wiki/File:Entrada_da_Capela_do_Pazo_de_Rioboo.JPG) · Lansbricae · CC BY-SA 2.5 es · 1536x2048
- [Fachada da capela de San Xoián Nepomuceno, pazo de Antequeira.jpg](https://commons.wikimedia.org/wiki/File:Fachada_da_capela_de_San_Xoi%C3%A1n_Nepomuceno,_pazo_de_Antequeira.jpg) · Dodro · CC BY-SA 4.0 · 2964x4022
- [Fachada principal da capela de San Xoián Nepomuceno, pazo de Antequeira.jpg](https://commons.wikimedia.org/wiki/File:Fachada_principal_da_capela_de_San_Xoi%C3%A1n_Nepomuceno,_pazo_de_Antequeira.jpg) · Dodro · CC BY-SA 4.0 · 3072x4096

### 05. Cruceiro y petos de ánimas  (16 candidatas)
- [Peto de ánimas no Cruceiro do Acordo en Mañufe.jpg](https://commons.wikimedia.org/wiki/File:Peto_de_%C3%A1nimas_no_Cruceiro_do_Acordo_en_Ma%C3%B1ufe.jpg) · Varperalta · CC BY-SA 4.0 · 3456x5184
- [Peto de ánimas en Portosín - Galiza-2.jpg](https://commons.wikimedia.org/wiki/File:Peto_de_%C3%A1nimas_en_Portos%C3%ADn_-_Galiza-2.jpg) · Luis Miguel Bugallo Sánchez · CC BY-SA 3.0 · 1508x3573
- [Peto de ánimas - Vilanova dos Infantes - Celanova - Galiza VI.01.jpg](https://commons.wikimedia.org/wiki/File:Peto_de_%C3%A1nimas_-_Vilanova_dos_Infantes_-_Celanova_-_Galiza_VI.01.jpg) · Luis Miguel Bugallo Sánchez (Lmbuga) · CC BY-SA 3.0 · 3011x3809
- [36990 Noalla 03, A Revolta 02-04a.jpg](https://commons.wikimedia.org/wiki/File:36990_Noalla_03,_A_Revolta_02-04a.jpg) · Lameiro · CC BY-SA 4.0 · 3088x2056
- [Peto de ánimas, Sobreira, Ourense.jpg](https://commons.wikimedia.org/wiki/File:Peto_de_%C3%A1nimas,_Sobreira,_Ourense.jpg) · Simon Burchell · CC BY-SA 4.0 · 3096x4128

### 06. Cocina tradicional  (16 candidatas)
- [Festa da Malla 2022, 19.jpg](https://commons.wikimedia.org/wiki/File:Festa_da_Malla_2022,_19.jpg) · Lameiro · CC BY-SA 4.0 · 3088x2056
- [Lareira rural.jpg](https://commons.wikimedia.org/wiki/File:Lareira_rural.jpg) · Pedro M. Martínez Corada (www.martinezco · CC BY-SA 4.0 · 3418x2278
- [Reitoral de Beiro, Carballeda de Avia 3.jpg](https://commons.wikimedia.org/wiki/File:Reitoral_de_Beiro,_Carballeda_de_Avia_3.jpg) · José Antonio Gil Martínez · CC BY 2.0 · 3264x2448
- [Coles, Ucelle, Pazo de Fontefiz, lareira.JPG](https://commons.wikimedia.org/wiki/File:Coles,_Ucelle,_Pazo_de_Fontefiz,_lareira.JPG) · HombreDHojalata · CC BY-SA 3.0 · 3872x2592
- [Lalín, Casa do Patrón 01-15b.JPG](https://commons.wikimedia.org/wiki/File:Lal%C3%ADn,_Casa_do_Patr%C3%B3n_01-15b.JPG) · P.Lameiro · CC BY-SA 3.0 · 2848x4272

### 07. Queimada  (10 candidatas)
- [Queimada fuego.jpg](https://commons.wikimedia.org/wiki/File:Queimada_fuego.jpg) · Alain Crespo · CC BY-SA 2.5 · 2592x1944
- [Camino de Santiago, May 2008.jpg](https://commons.wikimedia.org/wiki/File:Camino_de_Santiago,_May_2008.jpg) · Alex Chang · CC BY 2.0 · 2592x1944
- [Queimada em açao.jpg](https://commons.wikimedia.org/wiki/File:Queimada_em_a%C3%A7ao.jpg) · zentolos · CC BY-SA 2.0 · 1806x2277
- [Queimada por Zentolos.jpg](https://commons.wikimedia.org/wiki/File:Queimada_por_Zentolos.jpg) · zentolos · CC BY-SA 2.0 · 1729x2281
- [Meigas de la queimada, O Grove (4005163304).jpg](https://commons.wikimedia.org/wiki/File:Meigas_de_la_queimada,_O_Grove_(4005163304).jpg) · Laura Suarez from Edinburgh, United King · CC BY-SA 2.0 · 2211x3454

### 08. Traje tradicional, zocas, coroza  (16 candidatas)
- [2026 Domingo 26 de xullo. Desfile de traxes tradicionais. Santiago de Compostela.jpg](https://commons.wikimedia.org/wiki/File:2026_Domingo_26_de_xullo._Desfile_de_traxes_tradicionais._Santiago_de_Compostela.jpg) · Luis Miguel Bugallo Sánchez · CC BY-SA 4.0 · 4549x6722
- ["Gallega, galicienne, en costume de fête" (19316007923).jpg](https://commons.wikimedia.org/wiki/File:%22Gallega,_galicienne,_en_costume_de_f%C3%AAte%22_(19316007923).jpg) · Gustave Doré · CC BY 2.0 · 1632x2484
- [Traxe tradicional galego. Santiago de Compostela.jpg](https://commons.wikimedia.org/wiki/File:Traxe_tradicional_galego._Santiago_de_Compostela.jpg) · Noel Feans · CC BY 2.0 · 2016x3024
- [Traxe tradicional galego, Santiago de Compostela.jpg](https://commons.wikimedia.org/wiki/File:Traxe_tradicional_galego,_Santiago_de_Compostela.jpg) · Noel Feans · CC BY 2.0 · 4141x2761
- [Galegos (14700300926).jpg](https://commons.wikimedia.org/wiki/File:Galegos_(14700300926).jpg) · juantiagues · CC BY-SA 2.0 · 4608x3456

### 09. Herramientas agrícolas y domésticas  (16 candidatas)
- [Arado. Vimianzo. Galiza -V11.jpg](https://commons.wikimedia.org/wiki/File:Arado._Vimianzo._Galiza_-V11.jpg) · Luis Miguel Bugallo Sánchez (Lmbuga) · CC BY-SA 4.0 · 4630x3086
- [Festa da Malla 2017, 107.jpg](https://commons.wikimedia.org/wiki/File:Festa_da_Malla_2017,_107.jpg) · Lameiro · CC BY-SA 4.0 · 2056x3088
- [Arado en Galiza.jpg](https://commons.wikimedia.org/wiki/File:Arado_en_Galiza.jpg) · IES MANUEL GARCÍA BARROS A ESTRADA- PONT · CC BY-SA 2.0 · 2048x1536
- [Arado. Galicia (Spain).jpg](https://commons.wikimedia.org/wiki/File:Arado._Galicia_(Spain).jpg) · IES MANUEL GARCÍA BARROS A ESTRADA- PONT · CC BY-SA 2.0 · 2048x1536
- [Arado, Galicia (Spain).jpg](https://commons.wikimedia.org/wiki/File:Arado,_Galicia_(Spain).jpg) · IES MANUEL GARCÍA BARROS A ESTRADA- PONT · CC BY-SA 2.0 · 1536x2048

### 10. Muíño, batán, fonte, lavadoiro  (16 candidatas)
- [Molino Batans do mosquetín.jpg](https://commons.wikimedia.org/wiki/File:Molino_Batans_do_mosquet%C3%ADn.jpg) · Javier Pais · CC BY 2.0 · 794x1194
- [Portor - Negreira - Ponte Maceira - Interior de los molinos - 01.JPG](https://commons.wikimedia.org/wiki/File:Portor_-_Negreira_-_Ponte_Maceira_-_Interior_de_los_molinos_-_01.JPG) · Xosema · CC BY-SA 4.0 · 2560x1920
- [Muiño da veiga.jpg](https://commons.wikimedia.org/wiki/File:Mui%C3%B1o_da_veiga.jpg) · Gabriel González from Boliñas-Aguasantas · CC BY 2.0 · 4000x3000
- [Rota dos muínhos do rio das Gándaras (33) - Muínho do Batám 1.jpg](https://commons.wikimedia.org/wiki/File:Rota_dos_mu%C3%ADnhos_do_rio_das_G%C3%A1ndaras_(33)_-_Mu%C3%ADnho_do_Bat%C3%A1m_1.jpg) · One2 · CC BY-SA 4.0 · 4160x3120
- [Noia - Muiño de Ponte da Traba - Molino de Ponte da Traba - Watermill of Ponte da Traba - 02.jpg](https://commons.wikimedia.org/wiki/File:Noia_-_Mui%C3%B1o_de_Ponte_da_Traba_-_Molino_de_Ponte_da_Traba_-_Watermill_of_Ponte_da_Traba_-_02.jpg) · Xosema · CC BY-SA 4.0 · 5194x3457

### 11. Embarcaciones y costa  (16 candidatas)
- [Nasa11dorna05eue.jpg](https://commons.wikimedia.org/wiki/File:Nasa11dorna05eue.jpg) · Luis Miguel Bugallo Sánchez (Lmbuga) · CC BY-SA 3.0 · 1600x1200
- [Dornas na ría de Arousa.JPG](https://commons.wikimedia.org/wiki/File:Dornas_na_r%C3%ADa_de_Arousa.JPG) · Bemilladoiro · CC BY-SA 3.0 · 3648x2736
- [2016 Dorna afundida en Muros. Galiza 273.jpg](https://commons.wikimedia.org/wiki/File:2016_Dorna_afundida_en_Muros._Galiza_273.jpg) · Luis Miguel Bugallo Sánchez (Lmbuga) · CC BY-SA 4.0 · 4206x2803
- [2017. Dorna en Palmeira. Ribeira. Galiza Galicia.jpg](https://commons.wikimedia.org/wiki/File:2017._Dorna_en_Palmeira._Ribeira._Galiza_Galicia.jpg) · Luis Miguel Bugallo Sánchez (Lmbuga) · CC BY-SA 4.0 · 3998x2665
- [2017. Dúas dornas en Palmeira. Ribeira. Galiza Galicia.jpg](https://commons.wikimedia.org/wiki/File:2017._D%C3%BAas_dornas_en_Palmeira._Ribeira._Galiza_Galicia.jpg) · Luis Miguel Bugallo Sánchez (Lmbuga) · CC BY-SA 4.0 · 5616x3744

### 12. Iconografía medieval y moderna  (22 candidatas)
- [Castelo de Pambre 2.JPG](https://commons.wikimedia.org/wiki/File:Castelo_de_Pambre_2.JPG) · AlmaGZ · CC BY-SA 3.0 · 3072x2304
- [Castelo de Pambre, Palas de Rei.jpg](https://commons.wikimedia.org/wiki/File:Castelo_de_Pambre,_Palas_de_Rei.jpg) · José Antonio Gil Martínez · CC BY 2.0 · 3264x2448
- [Villasobrosomondariz018.jpg](https://commons.wikimedia.org/wiki/File:Villasobrosomondariz018.jpg) · http://gl.wikipedia.org/w/index.php?titl · Public domain · 2580x1932
- [Dende a Fiestra (8578368554).jpg](https://commons.wikimedia.org/wiki/File:Dende_a_Fiestra_(8578368554).jpg) · amaianos from Galicia · CC BY 2.0 · 3805x3216
- [Torre da Homenaxe dende a igrexa de Santa María Gracia.jpg](https://commons.wikimedia.org/wiki/File:Torre_da_Homenaxe_dende_a_igrexa_de_Santa_Mar%C3%ADa_Gracia.jpg) · amaianos · CC BY 2.0 · 3320x3160

### 14. Samos, iglesias y aldeas antiguas  (16 candidatas)
- [Portada románica del Monasterio de San Julián de Samos.jpg](https://commons.wikimedia.org/wiki/File:Portada_rom%C3%A1nica_del_Monasterio_de_San_Juli%C3%A1n_de_Samos.jpg) · Jl FilpoC · CC BY-SA 4.0 · 2934x3911
- [2017 Mosteiro de Samos. Samos. Galiza-3.jpg](https://commons.wikimedia.org/wiki/File:2017_Mosteiro_de_Samos._Samos._Galiza-3.jpg) · Luis Miguel Bugallo Sánchez (Lmbuga) · CC BY-SA 4.0 · 5549x3699
- [2017 Portal do Mosteiro de Samos. Galiza.jpg](https://commons.wikimedia.org/wiki/File:2017_Portal_do_Mosteiro_de_Samos._Galiza.jpg) · Luis Miguel Bugallo Sánchez (Lmbuga) · CC BY-SA 4.0 · 3261x4614
- [2017 Mosteiro de Samos. Galiza-6.jpg](https://commons.wikimedia.org/wiki/File:2017_Mosteiro_de_Samos._Galiza-6.jpg) · Luis Miguel Bugallo Sánchez (Lmbuga) · CC BY-SA 4.0 · 3060x3187
- [Exhibition Ruth Anderson in Pontevedra 03.jpg](https://commons.wikimedia.org/wiki/File:Exhibition_Ruth_Anderson_in_Pontevedra_03.jpg) · Munfarid1 · CC BY-SA 4.0 · 1840x3264

### 13. Armas, armaduras y ropa s. XV-XVII  (18 candidatas)
- [Rapier of Prince-Elector Christian II of Saxony (1583–1611) (dated 1606)](https://www.metmuseum.org/art/collection/search/24860) · Israel Schuech · CC0 (The Met Open Access) · no verificada (original del Met, normalmente >2000 px)
- [Smallsword in the Spanish Style (ca. 1775)](https://www.metmuseum.org/art/collection/search/22926) · Spanish · CC0 (The Met Open Access) · no verificada (original del Met, normalmente >2000 px)
- [Sword (ca. 1500)](https://www.metmuseum.org/art/collection/search/27459) · Spanish · CC0 (The Met Open Access) · no verificada (original del Met, normalmente >2000 px)
- [Thrusting Sword (<i>Spada da Stocco</i>) (ca. 1500)](https://www.metmuseum.org/art/collection/search/35716) · probably Italian or Spanish · CC0 (The Met Open Access) · no verificada (original del Met, normalmente >2000 px)
- [Transitional Rapier (hilt, ca. 1625–50; blade, 17th century)](https://www.metmuseum.org/art/collection/search/27450) · Tomas Aiala · CC0 (The Met Open Access) · no verificada (original del Met, normalmente >2000 px)

## Huecos

- **Cocina tradicional (06):** pocas fotos nítidas de lareira + escano + pote; muchas son interiores de museos/pazos o de reconstrucciones. Falta gramalleira, lacena y cunca de barro aislados.
- **Queimada (07):** solo 10 candidatas, la mayoría en ambiente de fiesta con gente; falta una foto limpia de pota de barro + cazo + llama azul.
- **Carro de bois (02):** varias son carros en festas o monumentos; falta un carro del país completo, de lado y sin gente, que muestre bien las ruedas macizas y el xugo.
- **Herramientas (09):** buen arado; poco de rueca/fuso, tear, fouce, sacho y mallo aislados.
- **Traje (08):** casi todo son personas con traje moderno de desfile; faltan refaixo/dengue/mantelo sobre fondo neutro y la coroza. Doré (grabado de 1862) sirve para época.
- **Armas y ropa (13):** el Met cubre espadas, yelmos y adarga hispanos (CC0) pero no hay ropa de escribano, clérigo, labrador o noble del s. XV-XVII; ni armaduras completas españolas (el Met las tiene como «Spanish» pero la búsqueda dio pocas). Pendiente: grabados de trajes (p. ej. Weiditz, Vecellio) en el Met/Rijksmuseum/BNE.
- **Iconografía (12):** canecillos y capiteles hay pero sin verificar calidad; grabados gallegos de los siglos XVI-XVII no aparecieron con licencia clara.
- **Fotos antiguas (14):** Ruth Matilda Anderson (Hispanic Society) está en Commons solo en parte, con licencia por comprobar; no se incluyeron salvo que la licencia fuera libre.

## Fuentes a pedir / revisar por escrito (contactos SIN verificar; buscar el actual en cada web)

- **Hispanic Society of America** (fotografías de Ruth Matilda Anderson en Galicia, 1924-26): https://hispanicsociety.org — pedir licencia explícita para uso comercial y obra derivada.
- **Museo do Pobo Galego** (Santiago de Compostela): https://museodopobo.gal — fondos etnográficos (arados, tear, cociña, traxes); su web respondió con un reto anti-bot desde aquí.
- **Galiciana – Biblioteca Dixital de Galicia:** https://galiciana.gal — grabados, fotos antiguas y prensa; licencia por obra.
- **Arquivo do Reino de Galicia** y **Arquivo Pacheco**: comprobar licencia y titular actual.
- **Biblioteca Digital Hispánica (BNE):** https://bdh.bne.es — dominio público para obras antiguas, pero la web no fue accesible desde este entorno.
- **Europeana** (filtro CC0/PDM/CC BY) y **Flickr Commons**: requieren clave de API o navegador; pendientes.
- **Rijksmuseum y Library of Congress:** CC0/PD, pendientes de barrido (trajes y grabados europeos de época).
