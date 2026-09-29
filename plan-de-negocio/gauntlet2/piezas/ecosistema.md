# Pieza del plan v2: el ecosistema galego (riesgos, apoyos y estrategia *pro lingua*)

- **Versión:** v1 (primera versión del constructor), 29-09-2026.
- **Qué cubre:** análisis de actores (Proxecto Nós/USC/CiTIUS/ILG y Gradiant, CSAG-CRTVG/TVG y Radio Galega, RAG,
  Consello da Cultura Galega, Secretaría Xeral da Lingua, AGPTI, sector de la dobraxe y la locución, comunidad
  tecnológica de software libre, divulgadores de historia, medios y comunidad de hablantes); evaluación crítica de la
  tesis del promotor ("o proxecto é pro lingua"); choque entre anonimato y búsqueda de apoyo; hoja de ruta de
  acercamiento; borrador en galego del correo a Nós/USC (D4).
- **Qué no cubre:** costes, pipeline, política de YouTube y AI Act (en `plan-desatendido.md`, al que se remite con
  §), ni el vídeo piloto.
- **Convenciones:** [F] dato con fuente (URL al lado); [R] reutilizado del Gauntlet 1 o de otra pieza (allí están las
  URLs); [P] comprobación propia en este entorno el 29-09-2026; [S] supuesto o juicio propio, sin verificar.
- **Nombre de trabajo del canal:** *Serán*. Anónimo ante el público (D6).

---

## 0. Resumen en 12 líneas

1. **La tesis del promotor es defendible, pero solo en una versión concreta:** el canal no es "contido en galego feito
   con IA", sino **un laboratorio aberto que pon a proba a IA aberta en galego en público** y devuelve datos. Si se
   presenta como producto de contenido, choca de frente con lo que AGPTI, ADA y A Mesa denuncian en 2026 (§2).
2. **Lo único que Nós puede aprovechar de verdad no son los guiones** (galego sintético sin revisar: valor de corpus
   nulo o negativo), sino **los errores y sus correcciones**: pronunciación de Cotovía/StyleTTS2 en narración larga,
   castellanismos del LLM, y las correcciones que haga la audiencia. Nós ya publica un conjunto así para la
   traducción (`erros_sistematicos_traducion_es_gl`, 6.800 pares) [F] (§2.2).
3. **Hay un hueco real que el proyecto puede cubrir:** entre los 63 conjuntos de datos de Nós en Hugging Face hay
   patrimonio, museos y arte, pero **ninguno de historia de Galicia** [P]. Un banco de preguntas de historia con fuente,
   derivado de los dossieres, es la aportación más útil, **siempre que una parte la verifique una persona** (§2.2).
4. **Contradicción interna a resolver:** el plan redacta los guiones con un LLM *frontier* cerrado por API
   (`plan-desatendido.md` §0.3). Un canal que dice "fomentar o open source en galego" y no usa el LLM de Nós
   (Carballo) es fácil de desmontar. Propuesta: **comparar en público Carballo frente al *frontier* en cada episodio**
   y publicar la métrica, aunque se emita el mejor (§2.3).
5. **El anonimato y el apoyo institucional son incompatibles tal como están planteados.** Ninguna institución firma ni
   respalda a alguien sin identidad, y el propio permiso de D4 exige firmar con nombre. Solución: **seudónimo ante el
   público, identidad conocida por los socios** (Nós, y quien apoye después) (§3).
6. **Riesgo n.º 1: la voz de Brais es la de un actor de dobraxe profesional**, en un sector que en 2026 está en pie de
   guerra (ADA fundada en dic. 2024; denuncia de ADA, AGPTI y A Mesa contra RTVE en feb. 2026) [F]. La licencia
   Apache del modelo no cubre la voz de la persona [R]. D4 tiene que incluir al locutor (§1.1, §1.7).
7. **Riesgo n.º 2: el caso Begoña Caamaño (CSAG, 17-05-2026)** ha dejado a la comunidad muy sensible a la IA que
   "suplanta" [F]. Regla: nunca recrear ni imitar a nadie real, vivo o muerto (§1.2).
8. **Mapa de apoyos realista a 12 meses:** Nós/CiTIUS y la comunidad de software libre (Trasno, GALPon, AGASOL) pueden
   **colaborar**; SXL y RAG pueden, como mucho, **no oponerse**; AGPTI, ADA y A Mesa, en el mejor caso, **neutralidad
   informada**. Apoyo público de CSAG, CCG o RAG a un canal sin revisión humana: probabilidad baja (≈ 5-10 %) [S] (§1).
9. **Qué convierte una crítica en neutralidad:** avisar antes de publicar, permiso de la voz, transparencia completa,
   erratas públicas, código y datos abiertos, y ninguna pretensión de sustituir a profesionales (§4).
10. **No publicar con la voz de Brais antes de la respuesta de Nós** (o de 30 días de silencio anunciados en el
    correo). Esto corrige la P0 de `plan-desatendido.md` §9, que permitía publicar sin respuesta. No retrasa nada: el
    MVP tarda 8-10 semanas (§4).
11. **Hoja de ruta:** correo a Nós esta semana → comunidad de software libre con el código → lanzamiento discreto →
    informe trimestral de errores a Nós → solo con tracción y revisión humana parcial, instituciones (§4).
12. **Borrador del correo en galego** listo para enviar a `proxecto.nos@usc.gal` [F], firmado con nombre real (§5).

---

## 1. Actores: qué les molestaría, qué les interesaría y cómo convertirlo en apoyo

Tres rasgos del enfoque generan fricción, y cada actor los pesa distinto:
- **(A) Canal automático sin revisión humana** (texto e historia sin filtro).
- **(V) Voz sintética** hecha con la voz de una persona real (Brais, actor de dobraxe).
- **(N) Anonimato** del responsable.

### 1.0 Tabla resumen

| Actor | Fricción principal | Interés posible | Postura esperable al lanzar [S] | Objetivo realista a 12 meses [S] |
|---|---|---|---|---|
| Proxecto Nós (USC: CiTIUS + ILG) y Gradiant | V (T&C de los datos, consentimiento del locutor), A (galego defectuoso que contamina la web) | Uso real y visible de sus modelos; informes de error en narración larga; datos de evaluación de historia | Cauta; responde si el correo es serio | **Colaboración técnica** (datos de error, crédito, quizá mención en una memoria) |
| CSAG (antes CRTVG): TVG, Radio Galega | A (calidad), V (tras el caso Caamaño), competencia simbólica | Poco: tienen archivo propio y convocatoria de contenidos digitales | Indiferencia | **Indiferencia**; no tocar su archivo |
| Real Academia Galega | A (calidad normativa) | Discurso favorable a la IA para lenguas minorizadas | Indiferencia o crítica si hay errores con eco | **No oposición** |
| Consello da Cultura Galega | A, V (trabajo creativo) | Observatorio y estudios sobre IA en la cultura | Observación | **Ser un caso de estudio**, no un respaldado |
| Secretaría Xeral da Lingua | A (imagen del galego), riesgo político | Relato "o galego na IA", que financia vía Nós | Silencio | **No oposición**; evitar ser su escaparate |
| AGPTI | **A** (texto automático = lo que denuncian), sustitución laboral | Casi ninguno; quizá un revisor remunerado si hay ingresos | **Crítica** si se entera por terceros | **Neutralidad informada** |
| ADA y sector de locución | **V** (voz de un compañero), sustitución | Crédito y remuneración al locutor; compromiso de voz humana si hay ingresos | **Crítica** | **Neutralidad informada** |
| A Mesa pola Normalización Lingüística | A, V (ya lo dijo sobre RTVE) | Más contenido en galego | Crítica si hay errores | **No contactar al inicio**; neutralidad |
| Software libre (Trasno, GALPon, AGASOL, Mancomún, comunidad Common Voice gl) | Pocas; quizá "slop" | Pipeline libre y reproducible en galego; datos abiertos | **Interés** | **Colaboración** (pruebas, correcciones, difusión técnica) |
| Divulgadores de historia | A (errores), competencia, uso de su trabajo | Enlaces y tráfico; ser fuente citada | Recelo | **No hostilidad**; algunos como fuente citada |
| Medios (Nós Diario, Praza, GCiencia, Código Cero) | Titular fácil: "IA anónima enche YouTube" | Titular positivo: "experimento aberto que mide a IA en galego" | Nada, salvo polémica | **Una pieza técnica** en un medio de ciencia, cuando haya datos |
| Comunidad de hablantes | A (castellanismos, pronunciación), N | Más contenido para dormir en galego, hoy casi inexistente [R] | Mixta: comentarios de errores | **Comunidad de correctores** |

### 1.1 Proxecto Nós (USC: CiTIUS e ILG) y Gradiant

**Quiénes son.** Proyecto de la Xunta ejecutado por la USC a través del ILG y del CiTIUS, con convenio 2021-CP080
[F https://nos.gal/en/proxecto-nos/about-us ; https://github.com/proxectonos]. Integrado en ILENIA y hoy en ALIA
(infraestructura pública estatal) [F https://zenodo.org/records/20523403]. Financiación: 3,4 M€ del Estado ya
recibidos y 480.000 € más comunicados en julio de 2026; el corpus pasó de 40 M a 2.700 M de palabras
[F vía snippet https://www.elcorreogallego.es/santiago/2026/07/11/usc-recibira-480-000-euros-132359510.html]. Los
StyleTTS2 Brais y Celtia los desarrolló **Gradiant** con fondos de ALIA (NextGenerationEU) [F
https://huggingface.co/proxectonos/Nos_StyleTTS2-Brais-GL]. Contacto oficial de los datos de voz:
`proxecto.nos@usc.gal` [F https://huggingface.co/datasets/proxectonos/Nos_Brais-GL].

**Qué podría molestarle.**
- **(V) Condiciones de los datos de Brais.** El modelo es Apache-2.0, pero los términos del *dataset* dicen: *"may be
  used solely for research purposes and for developing artificial intelligence tools focused on linguistic
  objectives"* y prohíben *"public exposure"* de las grabaciones [F, API de HF de `Nos_Brais-GL`, `extra_gated_prompt`].
  El audio sintético no son las grabaciones, pero el espíritu (investigación y herramientas lingüísticas) no es "canal
  de YouTube". Nós tiene que proteger su relación con los locutores: si un actor de dobraxe ve su voz en un canal
  anónimo sin que nadie le haya preguntado, el problema reputacional es **de Nós**, no del canal anónimo.
- **(V) Usos declarados de sus voces:** accesibilidad (voces personalizadas para personas que perdieron el habla) y
  educación (cREAgal) [F https://zenodo.org/records/20523403]. El entretenimiento para dormir no está en esa lista;
  no está prohibido, pero tampoco es el relato que defienden.
- **(A) Contaminación del corpus.** Nós entrena con texto de la web y ya advierte de la escasez de datos en galego. Un
  canal que sube horas de galego sin revisar, con subtítulos, es exactamente el tipo de dato que no quieren en su
  próximo corpus (`plan-desatendido.md` §8.3).
- **(A) Que su nombre aparezca asociado a errores de lengua:** "Voz: Proxecto Nós" en la descripción de un vídeo con
  castellanismos se lee como "a IA da USC fala mal".
- **(N) No saber con quién hablan.**

**Qué podría interesarle.**
- **Uso real y visible de sus modelos.** Los StyleTTS2 de Brais y Celtia se publicaron en junio-julio de 2026 con
  descargas mínimas [R `voz_guion.md`]. Un usuario que los lleva a narración de 60 min en CPU y documenta cómo es un
  caso de uso que no tienen: su propia evaluación llega solo a textos de "> 60 s" [F, ficha del modelo].
- **Informes de error estructurados** en dominio histórico: topónimos, antropónimos medievales, vocales abiertas y
  cerradas, homógrafos, deriva de prosodia en tramos largos. Encaja con cómo trabajan (ya publican conjuntos de
  errores sistemáticos) [F https://huggingface.co/datasets/proxectonos/erros_sistematicos_traducion_es_gl].
- **Un conjunto de evaluación de historia de Galicia**, que no tienen (§2.2).
- **Una medida pública de Carballo frente a modelos cerrados** en una tarea real (§2.3).

**Cómo convertirlo en apoyo.**
1. **Preguntar antes de publicar con la voz**, con el correo del §5, firmado con nombre real (anonimato solo ante el
   público).
2. **Ofrecer cambiar de voz** si lo prefieren (p. ej. a una voz cuyo consentimiento cubra usos públicos, si la hay), y
   dejar en sus manos la conversación con el locutor.
3. **Preguntarles cómo quieren que se marque el texto sintético** para no contaminar sus corpus: es la pregunta que
   demuestra que se entiende su trabajo.
4. **Entregar datos, no solo pedir:** informe trimestral de errores (formato del §2.2) y el código del pipeline.
5. **Crédito exacto**, con la fórmula que ellos digan, y ninguna insinuación de respaldo ("feito con modelos de Nós",
   nunca "en colaboración con Nós" sin su permiso escrito).

### 1.2 CSAG (antes CRTVG): TVG, Radio Galega, AGalega

**Contexto.** La CRTVG pasó a ser la CSAG con la Ley 1/2025 de medios audiovisuales de Galicia; entre sus proyectos de
2025 cita IA, subtitulado automático y recomendación [F https://crtvg.gal/w/a-csag-consolida-a-s%C3%BAa-transformaci%C3%B3n-no-principal-ecosistema-audiovisual-p%C3%BAblico-de-galicia].
Es ya proveedora de datos de Nós: los guiones de informativos de la TVG 2019-2022 (166.951 frases) están en el corpus
CC0 de Nós [F https://huggingface.co/datasets/proxectonos/nos_gl_CC0], y hay conjuntos restringidos
`Nos_RG-Podcast-GL` y `Nos_Telexornais-GL` [P, listado de la API de HF]. El 17-05-2026 recreó con IA la imagen y la voz
de Begoña Caamaño para el Día das Letras Galegas y recibió críticas, entre otras de la presidenta del Colexio
Profesional de Xornalistas, Belén Regueira; el argumento central fue *"por que non deixala falar?"*, con su voz real
en el archivo de Radio Galega [F https://www.nosdiario.gal/articulo/social/que-non-deixala-falar-criticas-ia-empregada-pola-crtvg-recrear-begona-caamano/20260518160723256730.html].
Tiene su propia serie *Historias de Galicia* (2007) subida a YouTube [R `audiencia.md`] y una convocatoria anual de
contenidos digitales de hasta 26.000 € por proyecto [R `ingresos_alt.md`].

**Qué podría molestarle.** Poco directamente: el canal es diminuto para ellos. Los riesgos son indirectos: (a) usar
fragmentos de su archivo (derechos: **prohibido** en el pipeline); (b) un título o miniatura que se confunda con la TVG;
(c) que un periodista compare el canal con el caso Caamaño y la CSAG tenga que desmarcarse.

**Qué podría interesarle.** Como institución, casi nada al principio. A medio plazo, **la convocatoria de contenidos
digitales** es la vía natural si el canal llega a tener revisión humana (el tribunal del Gauntlet 1 ya lo situó ahí).
Con el canal desatendido y anónimo, **no es elegible en la práctica** (se seleccionan personas o empresas
identificadas y se puntúa la calidad lingüística) [R `ingresos_alt.md` §1.4].

**Cómo convertirlo en apoyo.** No buscarlo en la fase 1. Reglas: nada de su archivo, nada que se parezca a su marca,
**nunca recrear personas** (lección Caamaño), y enlazar *Historias de Galicia* en las descripciones como "para saber
máis" (reconocimiento gratuito que no pide nada).

### 1.3 Real Academia Galega (RAG)

**Contexto.** Presidente desde abril de 2025, Henrique Monteagudo, catedrático de Filología Galega de la USC. En mayo
de 2026 dijo que la IA *"puede ser muy favorable para las lenguas minorizadas"* por la traducción y el aprendizaje
[F https://www.elespanol.com/quincemil/cultura/20260516/henrique-monteagudo-presidente-da-rag-sistema-educativo-leva-anos-funcionando-espazo-presion-castelanizadora/1003744246593_0.html].
Figura entre las instituciones colaboradoras que agradece Nós [F https://tts.nos.gal/agradecementos] y su catálogo del
museo está en un corpus de Nós [P, ficha de `corpus_dominio_museistico_patrimonio`].

**Qué podría molestarle.** (A) Galego no normativo o con castellanismos difundido como "historia de Galicia"; y que se
le atribuya al canal algún tipo de aval normativo. La RAG no suele pronunciarse sobre canales concretos: el riesgo es
bajo salvo polémica con eco [S].

**Qué podría interesarle.** Que la norma se use con coherencia (el canal declara norma RAG-ILG, `plan-desatendido.md`
§8.1) y los datos agregados de qué errores comete la IA en galego, útiles para su discurso sobre la lengua en la era
digital.

**Cómo convertirlo en apoyo.** No pedir nada. Usar sus recursos públicos de consulta (Dicionario, Portal das Palabras)
**como control automático** (comprobación de palabras contra el diccionario, dentro de lo que permitan sus términos)
y citarlos. Si al año hay un informe de errores serio, enviarlo "para información", sin pedir respaldo.

### 1.4 Consello da Cultura Galega (CCG)

**Contexto.** Ha publicado *A intelixencia artificial na cultura galega: coñecemento, usos e opinións* (2024, DOI
10.17075/iacgcuo.2024): el sector audiovisual es el que más conoce y usa la IA (63,9 %), y hay preocupación por sus
efectos en la lengua y el empleo [F https://consellodacultura.gal/publicacion.php?id=4508 ;
https://consellodacultura.gal/noticia.php?id=11587&tipo=noticia]. Colaboró en el simposio del ILG sobre IA y galego
(18-20 de noviembre de 2025), que dedicó una jornada a la síntesis de voz y otra a lenguas minoritarias y regulación
audiovisual [F idem]. Su Observatorio constata escasez de contenido digital en galego (75,2 % percibe escasa la
oferta de divulgación) [R `audiencia.md`]. Sus contenidos son CC no comercial y sin obra derivada, y el pipeline ya
los excluye del dossier [R `plan-desatendido.md` §5.2].

**Qué podría molestarle.** (A) que se usen sus textos (no se usan); (V) sustitución de trabajo creativo.

**Qué podría interesarle.** **Como objeto de estudio:** un canal 100 % automático en galego, con métricas públicas de
audiencia, errores y reacción de la comunidad, es un dato que su observatorio no tiene [S].

**Cómo convertirlo en apoyo.** Nunca "apoio"; sí **transparencia útil**: al año, ofrecer los datos agregados
(audiencia, errores, sentimiento de los comentarios) como caso de estudio. Esto exige que alguien firme (§3).

### 1.5 Secretaría Xeral da Lingua (SXL)

**Contexto.** Financia y promociona Nós con el lema "a IA ao servizo da lingua galega" [F
https://www.lingua.gal/recursos/todos/_/promovelo/contido_607/nos-intelixencia-artificial-servizo-lingua-galega]; no
tiene ayudas para creadores digitales [R `ingresos_alt.md` §1.1]; colabora con creadores en campañas (FalaRedes) sin
convocatoria pública [R idem]. La ley gallega de IA fue criticada en su tramitación por "obviar" el galego (BNG, PSdeG)
[F https://www.nosdiario.gal/articulo/politica/lei-da-xunta-intelkixencia-artificial-obvia-galego/20250211140946216318.html].

**Qué podría molestarle.** Un canal que deje en mal lugar la tecnología que financia (errores con eco).

**Qué podría interesarle.** Es el actor cuyo **relato** encaja mejor con la tesis del promotor: "a tecnoloxía de Nós
xa permite facer divulgación en galego". Justamente por eso hay un **riesgo político**: en Galicia la política
lingüística está polarizada, y un canal que parezca escaparate de la Xunta perdería a la parte más militante de su
público potencial (la que habla galego por convicción) [S].

**Cómo convertirlo en apoyo.** No buscarlo activamente. Si la SXL lo cita algún día, aceptar la mención sin
convertirla en aval. Mantener el canal **fuera de la política lingüística** (ya vetada en `plan-desatendido.md` §8.2).

### 1.6 AGPTI (profesionales de la traducción e interpretación)

**Contexto.** El 20-02-2026, junto a ADA y A Mesa, denunció que RTVE usa IA generativa para subtitular y doblar al
galego: *"a substitución do traballo humano e profesional por IA xenerativa prexudica a calidade final dos
contidos"* [F https://www.agpti.org/ada-agpti-mesa-reclaman-tve-cumpra-lei-dobrando-subtitulando-galego-servizos-profesionais-calidade/ ;
https://www.nosdiario.gal/articulo/social/mesa-agpti-ada-denuncian-incumprimentos-rtve-coa-programacion-galego/20260220110723248001.html].
El 04-09-2026 publicó un decálogo sobre IA: los modelos son *"sistemas estatísticos que imitan usos lingüísticos
humanos"*, entrenados con corpus *"expropiados sen consentimento"*, y el galego, como lengua minorizada, es
*"especialmente vulnerable"* a textos mediocres; pide legislación contra la sustitución laboral y concienciación de
medios e instituciones [F https://www.agpti.org/defender-o-noso-traballo-e-defender-unha-sociedade-humana/].

**Qué podría molestarle.** Todo lo que define el canal: **texto generado sin revisión** en galego, publicado a
escala, con un LLM *frontier* entrenado con datos sin consentimiento. Es su caso de manual [S].

**Qué podría interesarle.** Muy poco. Honestamente, **no hay versión de este canal que AGPTI apoye** mientras no haya
trabajo humano remunerado. Lo más que se puede conseguir es que no lo use como ejemplo negativo.

**Cómo convertirlo en neutralidad.**
- **No sustituye a nadie:** no existe hoy un canal humano de historia para dormir en galego [R `audiencia.md`]; ningún
  profesional deja de cobrar por él. Es el argumento principal, y hay que decirlo con humildad, no como defensa.
- **Compromiso público y medible:** si hay ingresos, el primer gasto es **revisión lingüística profesional** (la
  Puerta F del plan v1), ofrecida primero a profesionales de AGPTI [R `gtm_riesgos.md` §2.6 bis].
- **Nunca decir "calidade profesional"** ni compararse con traducción humana.
- Informar **antes de lanzar** con una carta breve (§4, fase 1), sin pedir aval.

### 1.7 Sector de la dobraxe y la locución (ADA y otros)

**Contexto.** ADA (Actores e Actrices da Dobraxe Asociados) nació en diciembre de 2024 como primer sindicato del
sector en Galicia [F https://www.nosdiario.gal/articulo/cultura/nace-ada-primeiro-sindicato-actores-actrices-dobraxe-da-galiza/20241213202608212780.html];
denuncia un convenio sin actualizar desde 2006 y firmó con AGPTI la denuncia a RTVE [F idem, y §1.6]. La cláusula
PASAVE (2023) prohíbe usar grabaciones de doblaje para entrenar IA [R `voz_guion.md` §1.6]. **Brais y Celtia son
actores de dobraxe profesionales** [R `voz_guion.md`], es decir, compañeros de los socios de ADA.

**Qué podría molestarle.** (V) Una voz de un compañero sonando en un canal anónimo, posiblemente monetizado, sin que
se sepa si él lo consintió. Es el titular "outra IA que usa a voz dun actor galego" [R `gtm_riesgos.md` §2.6 bis].

**Qué podría interesarle.** Que el locutor sea preguntado, acreditado y, si hay ingresos, remunerado; y que el canal
se comprometa a contratar voz humana si crece.

**Cómo convertirlo en neutralidad.**
1. **La conversación con el locutor la abre Nós, no el canal** (el correo del §5 lo pide así). Nunca contactar al
   locutor por vías personales.
2. **Si el locutor no quiere, se cambia de voz** sin discusión (A4 de `plan-desatendido.md` §10).
3. Mantener la **oferta al locutor** del Gauntlet 1 (crédito, 10 % de ingresos netos, veto por tema, retirada en 30
   días) [R `gtm_riesgos.md` §2.6 bis], adaptada al hobby: hoy los ingresos son 0 € y hay que decirlo.
4. Carta informativa a ADA **solo después** de tener la respuesta del locutor (con permiso en la mano la conversación
   es otra).

### 1.8 A Mesa pola Normalización Lingüística

**Contexto.** Firmó la denuncia de RTVE (feb. 2026) y en septiembre de 2026 habla de "emerxencia lingüística" en el
debate educativo [F https://www.nosdiario.gal/articulo/lingua/mesa-sinala-que-emenda-ao-plan-do-pp-sigue-vetando-galego-nas-aulas/20260924133755267588.html].
El Gauntlet 1 ya concluyó: contactarla **después**, nunca al principio [R `gtm_riesgos.md`].

**Qué podría molestarle.** Galego de baja calidad presentado como normalización; IA que "ocupa" espacio.
**Qué podría interesarle.** Que exista más contenido en galego en un formato donde hoy no hay nada.
**Cómo gestionarlo.** No contactar en la fase 1-2. Si critica, responder con datos (erratas corregidas, código
abierto, permiso de la voz) y sin polemizar.

### 1.9 Comunidad tecnológica y de software libre

**Contexto.** **Proxecto Trasno** traduce software libre al galego desde 1999 y promovió Common Voice en galego
[F https://trasno.gal/2021/02/07/proxecto-common-voice-en-galego/]. **AGASOL** agrupa empresas de software libre y
planea materiales sobre software libre y datos abiertos en la IA [F https://www.agasol.gal/ ;
https://www.conselleriadefacenda.gal/-/a-xunta-colabora-con-agasol-para-promover-o-uso-do-software-libre-no-tecido-empresarial-galego].
**GALPon** organiza talleres de software libre [F https://www.mancomun.gal/noticias/obradoiro-sobre-e-textiles-organizado-por-galpon-e-a-industriosa/].
**Mancomún** es el centro de software libre de la Xunta. Nós y Common Voice movilizaron a miles de donantes de voz
("Doa a túa voz, preserva a túa lingua", objetivo de 1.000 h) [F https://praza.gal/ciencia-e-tecnoloxia/doa-galego-o-proxecto-nos-busca-voces-para-acadar-1000-horas-de-gravacion].

**Qué podría molestarle.** Poco. Quizá el *slop* en sí, o usar un LLM cerrado.

**Qué podría interesarle.** **Es el público natural de la tesis del promotor:** un pipeline libre, que corre en CPU,
que encadena modelos de Nós (voz, ASR Whisper-gl, quizá Carballo) y publica sus métricas. Es un "caso de uso de
extremo a extremo" que la comunidad no tiene documentado [S].

**Cómo convertirlo en apoyo.** Publicar `herramientas/pipeline/` con licencia libre (Apache-2.0 o AGPL-3.0) y
documentación **en galego**; un artículo técnico en un blog de la comunidad; invitar a Trasno a revisar la lista de
castellanismos del control automático (con crédito). Esta vía no choca con el anonimato: el software libre funciona
bien con seudónimos.

### 1.10 Divulgadores de historia

**Contexto.** Hay divulgación en galego con autor: el pódcast *Descifrando a Historia* [F
https://podgalego.agora.gal/descifrando-a-historia/], la web *historiadegalicia.gal* [F
https://historiadegalicia.gal/2020/10/estes-son-os-outros-documentais-sobre-os-castros-galegos-que-podes-ver-dende-a-web/],
divulgadores como Miguel Ángel Cajigal ("El Barroquista") [F https://gl.wikipedia.org/wiki/Miguel_%C3%81ngel_Cajigal_Vera],
series web de profesores de historia [F vía snippet de búsqueda], y la comunidad de pódcast de Obradoiro Dixital
Galego y Podgalego [F https://obradoirodixitalgalego.gal/comunidade/].

**Qué podría molestarle.** (A) Errores históricos que luego tienen que desmentir; sospecha de que la IA "se alimenta"
de su trabajo sin citarlo; competencia en un nicho diminuto.

**Qué podría interesarle.** Enlaces y tráfico: el oyente que se duerme con *Serán* y quiere saber más necesita un
destino humano.

**Cómo convertirlo en apoyo.** (1) El dossier **no** usa sus contenidos (ya se limita a Galipedia CC BY-SA y dominio
público). (2) En cada descripción, una sección "Para saber máis" que enlaza a divulgadores humanos del tema, sin
pedirles nada. (3) Si alguno señala un error, corregir en ≤ 7 días y **agradecerlo en la página de erratas** con su
permiso. Posicionamiento: *Serán* es "a porta de entrada que dorme", ellos son "onde se aprende".

### 1.11 Medios

**Contexto.** *Nós Diario* cubrió críticamente la IA de la CSAG y la denuncia a RTVE; *Praza* y *GCiencia* cubren Nós
en positivo; *Código Cero* es el diario tecnológico de Galicia [F, URLs de §1.2, §1.6, §1.9 y
https://codigocero.com/Consolidase-a-transformacion-da-CRTVG-na-CSAG].

**Riesgo.** El titular malo está escrito: *"Unha canle anónima enche YouTube de historia galega feita por IA e sen
revisar"*. Con anonimato, el canal no puede responder con una cara (§3).

**Oportunidad.** El titular bueno requiere datos: *"Un experimento aberto mide canto galego sabe a IA: X erros por
hora, Y corrixidos pola comunidade"*. Es una pieza para Código Cero o GCiencia **a los 6 meses**, no antes.

**Cómo gestionarlo.** No buscar prensa en la fase 1. Tener lista la página "Como se fai *Serán*" (transparencia) antes
de publicar, porque es lo primero que mirará un periodista.

### 1.12 Comunidad de hablantes

**Contexto.** Público mayor, galegofalante, con poca oferta: el 74,9 % de las entidades culturales ve escasa la oferta
audiovisual en galego y el 90,8 % apoya crear contenido digital en galego [R `audiencia.md`]. No existe hoy
contenido "para durmir" de historia en galego [R idem].

**Qué podría molestarle.** Castellanismos, vocales abiertas y cerradas mal pronunciadas, topónimos mal acentuados:
son los errores que un galegofalante oye a la primera y que el ASR no detecta (`plan-desatendido.md` §6.3). Y el
anonimato ("quen está detrás?").

**Qué podría interesarle.** Tener algo en galego para dormir; poder **corregir** y ver la corrección aplicada.

**Cómo convertirlo en apoyo.** Convertir el comentario de error en contribución: formulario simple ("minuto, que
di, que debería dicir"), página de erratas con agradecimientos, y un contador público ("esta comunidade corrixiu N
erros que xa lle chegaron ao Proxecto Nós"). Es el mecanismo que convierte la tesis *pro lingua* en algo tangible
(§2.2).

---

## 2. La tesis del promotor, examinada

> *"Explorar esta idea non ten por que verse como algo contra o galego, senón ao contrario: promoción da historia de
> Galicia; pode fomentar mellores modelos open source en galego e bo contexto para IAs en galego."*

### 2.1 Qué tiene de cierto

1. **Hay escasez documentada** de contenido digital en galego y no hay contenido "para durmir" de historia [R].
2. **Nós existe para que su tecnología se use**: sus recursos son "de libre acceso para terceiros" para facilitar
   productos y servicios en galego [F https://nos.gal/en/proxecto-nos/news/usc-xunta-ponen-intelixencia-artificial-servizo-lingua-galega-traves-proxecto].
   Un uso real, documentado y con informes de error es lo que un proyecto así necesita para justificar su financiación.
3. **La presidencia de la RAG** ve la IA como favorable para las lenguas minorizadas [F §1.3].
4. **No sustituye trabajo existente** (no hay equivalente humano) [R].

### 2.2 Qué aportaciones concretas devolvería el proyecto (y cuánto valen)

| Aportación | Qué es exactamente | Valor para el galego [S] | Condición para que valga | Coste en horas [S] |
|---|---|---|---|---|
| **1. Informe de errores de voz** (Cotovía + StyleTTS2) | Tabla trimestral: palabra/frase, pronunciación esperada, pronunciación producida, minuto y audio de 3-5 s, tipo (vocal abierta/cerrada, acento, topónimo, número, deriva de prosodia en tramos largos) | **Alto:** narración larga en dominio histórico es un caso que Nós no evalúa (su ficha llega a "> 60 s") [F] | Que los errores los confirme un oído galegofalante (comentarios o el promotor en muestreo) | 2-3 h/trimestre |
| **2. Pares "galego da máquina → galego corrixido"** | Cada errata confirmada, con frase original y corrección, en formato como `erros_sistematicos_traducion_es_gl` [F] | **Medio-alto** si hay volumen; con 50-500 visitas por vídeo, quizá 0-5 correcciones por episodio → 0-250 al año [S] | Correcciones humanas (audiencia); etiquetar el origen | 1 h/mes |
| **3. Banco de preguntas de historia de Galicia** | Preguntas tipo test o abiertas con respuesta y fuente (Galipedia/dominio público) derivadas del `afirmacions.csv` de cada dossier | **Alto como hueco:** Nós tiene arte, patrimonio, museos, VeritasQA, pero **ningún conjunto de historia de Galicia** entre sus 63 [P, https://huggingface.co/api/datasets?author=proxectonos] | **Verificación humana de una muestra** (sin ella es "candidato", no *benchmark*); licencia CC BY-SA por venir de Galipedia | 3-5 h/trimestre |
| **4. Contexto RAG abierto** | Los dossieres por episodio: fragmentos de fuentes con licencia libre, afirmaciones con id de fuente | **Medio:** es texto humano (Galipedia) reorganizado por tema, no texto nuevo | Respetar CC BY-SA; nunca incluir CCG ni obras protegidas | ~0 (ya se genera) |
| **5. Métricas públicas del pipeline** | Por episodio: WER del control ASR, canarios detectados, castellanismos detectados, frases bloqueadas; comparación Carballo vs. *frontier* (§2.3) | **Medio:** es una medida continua y pública del estado de la IA abierta en galego | Metodología estable y publicada | ~0 (ya se genera) |
| **6. Pipeline libre** | Código en `herramientas/pipeline/`, documentado en galego | **Medio:** baja la barrera para que otros hagan contenido en galego con Nós | Licencia libre; que funcione fuera de este entorno | 5-10 h una vez |
| **7. Guiones CC BY** | Los textos de cada episodio | **Bajo o negativo como corpus:** galego sintético sin revisar | Solo si van **etiquetados como sintéticos** y separados; útiles como material de evaluación, **no** de entrenamiento | ~0 |

**Lectura honesta.** La tesis funciona si lo que se devuelve son **errores y evaluaciones** (1, 2, 3, 5), no
**contenido** (7). "Fomentar mellores modelos" no ocurre porque el canal exista; ocurre si alguien empaqueta los
errores y Nós los usa. Con ~1 h/semana en régimen estable (D3), las aportaciones 1, 2 y 5 caben (≈ 1-2 h/mes); la 3
necesita horas extra o un voluntario. **Si no se empaquetan, la tesis es solo retórica** y un crítico lo verá.

### 2.3 Dónde la tesis se contradice (y cómo arreglarlo)

1. **LLM cerrado para el guion.** `plan-desatendido.md` usa un LLM *frontier* por API (≈ 1-2 USD/episodio) y deja
   Carballo de Nós como opción peor. Un canal que dice fomentar el open source en galego y escribe con un modelo
   cerrado entrenado con datos "expropiados" (en palabras de AGPTI) es incoherente.
   **Arreglo:** en cada episodio, generar también el guion con Carballo (o el mejor LLM abierto de Nós disponible) y
   publicar una métrica comparativa sencilla (castellanismos por 1.000 palabras, afirmaciones sin fuente,
   frases bloqueadas). Se emite el mejor, pero la comparación es pública. Coste: ~1 h de CPU extra por episodio [S].
   Cuando Carballo iguale al cerrado en esas métricas, se pasa a Carballo. Esto **convierte la contradicción en la
   aportación más citable del proyecto** [S].
2. **Contaminar el corpus del que viven los modelos abiertos** (`plan-desatendido.md` §8.3). Arreglo ya previsto:
   todo texto publicado lleva marca de sintético. Añadir: **preguntar a Nós el formato de marca** que prefieren (§5).
3. **"Sen revisión humana" vs "pro lingua".** Para AGPTI y A Mesa, publicar galego sin revisar a escala es, por
   definición, contra la lengua. El canal no puede ganar ese debate en abstracto; solo puede **bajar la escala**
   (1 episodio/semana, nunca diario), **corregir rápido** y **medir en público** la tasa de error.
4. **Uso de la voz de una persona sin su consentimiento explícito para este uso.** Mientras no haya respuesta de Nós
   y del locutor, el relato *pro lingua* se cae ante cualquier actor de dobraxe (§1.7).

### 2.4 Veredicto sobre la tesis

**Versión defendible:** *"Serán é un laboratorio aberto: usa só ferramentas abertas de galego cando é posible, mide
en público o que fallan e devólvello ao Proxecto Nós e á comunidade. Non substitúe a ninguén: onde hoxe non hai nada,
proba canto se pode facer e canto falta."*

**Versión no defendible:** *"A IA fai historia de Galicia en galego para todos."* Promete calidad que no hay y se
compara con el trabajo humano.

Probabilidad de que la tesis se sostenga públicamente si se cumplen las condiciones del §2.3 y el §4: **media** [S].
Si no se cumplen (voz sin permiso, LLM cerrado sin comparación, errores sin corregir): **baja**, y el canal sería un
argumento más contra la IA en galego.

---

## 3. Anonimato frente a búsqueda de apoyo

**El choque es real:**
- **D4 obliga a identificarse ante Nós:** pedir permiso sobre unos datos con términos contractuales exige un
  interlocutor identificable; el acceso a los datos de voz de Nós se solicita con nombre y correo [F, ficha de
  `Nos_Brais-GL`].
- **Ninguna institución respalda a un anónimo** (CSAG, SXL, CCG): no pueden firmar, citar ni financiar sin saber con
  quién [S; y R `ingresos_alt.md`: las convocatorias piden persona física o jurídica].
- **Anonimato + IA = "granja de slop"** a ojos de un periodista o de ADA. La transparencia sobre el proceso compensa
  solo en parte: falta alguien que responda.
- **A favor del anonimato:** protege al promotor de la polémica personal (D6), y el software libre y los canales
  *faceless* funcionan bien con seudónimo.

**Propuesta: seudónimo público con identidad conocida por los socios.**
1. **Ante el público:** canal con nombre (*Serán*) y un seudónimo de responsable; página "Como se fai *Serán*" con
   todo el proceso; correo de contacto del canal.
2. **Ante Nós (y cualquier institución después):** nombre real, firmado, y petición explícita de no hacerlo público.
   Es un uso normal y Nós puede respetarlo.
3. **Regla de salida del anonimato:** si el canal busca apoyo **público** (convocatoria, mención institucional,
   prensa), se levanta el anonimato o se crea una entidad (asociación cultural) que firme. Mientras siga siendo
   hobby, no hace falta [S].
4. **Frase para la página de transparencia** (galego): *"Detrás de Serán hai unha persoa que prefire non aparecer. O
   Proxecto Nós sabe quen é. Para calquera cousa, escribe a [correo]."* (Solo si Nós lo acepta.)

---

## 4. Hoja de ruta de acercamiento

Relojes: S0 = esta semana (29-09-2026). M0 = primera publicación (≈ 8-10 semanas, `plan-desatendido.md` §3).

| Fase | Cuándo | Con quién | Qué se hace | Qué NO se hace | Resultado que se busca |
|---|---|---|---|---|---|
| **0. Permiso** | S0-S1 | Proxecto Nós (`proxecto.nos@usc.gal`), copia a Gradiant | Enviar el correo del §5 con nombre real | Contactar al locutor directamente; publicar con su voz | Respuesta escrita: sí / sí con condiciones / no |
| **0-bis. Espera** | S1-S5 | — | Construir el MVP; si no hay respuesta en 30 días, un recordatorio breve | Publicar con Brais antes de respuesta o de 30 días de silencio **anunciados en el correo** | Decisión de voz |
| **1. Preparación** | Antes de M0 | — | Página "Como se fai *Serán*"; formulario de erratas; métricas del §2.2; comparación Carballo vs. cerrado | Buscar prensa; usar "calidade" en textos | Todo listo para responder a una crítica el primer día |
| **2. Aviso previo** | M0 − 1 semana | AGPTI y ADA (solo si Nós y el locutor dijeron sí) | Carta informativa breve: qué es, qué voz y con qué permiso, compromiso de revisión profesional si hay ingresos | Pedir apoyo o aval | Que se enteren por el canal, no por la prensa |
| **3. Comunidad técnica** | M0 | Trasno, GALPon, AGASOL, Common Voice gl | Publicar el código y un artículo técnico en galego; invitar a revisar la lista de castellanismos | Presentarlo como "producto" | Primeros correctores y usuarios del pipeline |
| **4. Lanzamiento discreto** | M0 | Público | 3 episodios; aviso hablado; etiqueta sintética; "Para saber máis" con divulgadores humanos | Contactar a A Mesa, RAG, CSAG, medios | Primeras correcciones reales |
| **5. Primera devolución** | M0 + 3 meses | Nós | Informe de errores de voz + pares de corrección + métricas (§2.2) | Pedir respaldo público | Que Nós los use o los comente |
| **6. Caso de estudio** | M0 + 6 meses (si P2 de `plan-desatendido.md` §9 da GO) | Código Cero / GCiencia; CCG (observatorio) | Datos agregados; propuesta de pieza técnica | Titulares de éxito | Titular "experimento aberto que mide a IA en galego" |
| **7. Institucional** | Con tracción (P3) y revisión humana parcial | CSAG (convocatoria digital), SXL, RAG | Solo con identidad pública o entidad; con revisión lingüística profesional | Pedir dinero para un canal sin revisión | Financiar la revisión humana (lo que el plan v1 llamaba Puerta F) |

**Qué hacer ante cada respuesta de Nós:**
- **Sí sin condiciones:** crédito con su fórmula; informe trimestral de errores.
- **Sí para hobby, no para monetizar:** publicar sin monetización con Brais; la P4 (YPP) queda bloqueada hasta nuevo
  permiso o cambio de voz. Encaja con D6.
- **Sí si consiente el locutor:** esperar a que Nós traslade la petición; mientras, voz de reserva.
- **No:** cambiar a otra voz con permiso claro (proveedor gl-ES con licencia, `plan-desatendido.md` P0-bis) o a otra
  de Nós que ellos indiquen; agradecer y ofrecer igualmente los datos de error de ASR y texto.
- **Silencio a 30 días:** recordatorio; a 45 días, publicar **sin monetizar** con aviso en la descripción ("solicitouse
  permiso ao Proxecto Nós o [data]; retirarase a voz se o piden"), o usar la voz de reserva. Decisión del promotor;
  recomiendo la voz de reserva si la diferencia de calidad es pequeña [S].

**Cambio respecto a `plan-desatendido.md` §9 (P0):** allí la respuesta de Nós "no es necesaria para publicar como
hobby sin monetizar". Aquí se recomienda **no publicar con la voz de Brais antes de la respuesta o del plazo
anunciado**. Motivo: pedir permiso y publicar sin esperarlo es peor que no pedirlo (el mensaje recibido es "pregunto
por cortesía, pero me da igual"). Coste: ninguno, porque el MVP tarda más que el plazo.

**Alarmas nuevas para `plan-desatendido.md` §10** (propuesta):
- **A7:** una asociación profesional (AGPTI, ADA) o un medio cita el canal como ejemplo negativo → pausa de 2 semanas,
  respuesta pública con datos y oferta concreta (revisión profesional si hay ingresos), sin polemizar.
- **A8:** Nós pide retirar su nombre de los créditos → retirar en 48 h (y seguir con la licencia Apache del modelo
  solo si también autorizan el uso).

---

## 5. Borrador del correo a Proxecto Nós / USC (D4), en galego

- **Para:** `proxecto.nos@usc.gal` [F https://huggingface.co/datasets/proxectonos/Nos_Brais-GL]
- **Copia (opcional):** equipo de Gradiant que desenvolveu os StyleTTS2 (localizar o contacto na súa web; non
  inventalo).
- **Asunto:** Consulta sobre o uso da voz StyleTTS2 Brais nunha canle de divulgación en galego e oferta de datos de
  erros

> Boas tardes:
>
> Chámome [nome e apelidos] e escríbovos a título persoal. Estou a preparar, como afección e sen ánimo de lucro polo
> de agora, unha canle de YouTube e pódcast de historia de Galicia en galego pensada para escoitar antes de durmir:
> episodios longos, de ton sereno, sobre temas de consenso historiográfico (castros, a *Gallaecia*, o Camiño, os
> mosteiros, os irmandiños).
>
> A canle faise cun proceso automático construído con ferramentas abertas, e o voso traballo é a peza central: a voz
> é o modelo **Nos_StyleTTS2-Brais-GL**, o control de pronuncia faise co Whisper en galego do Proxecto Nós, e
> queremos probar tamén os vosos modelos de lingua para redactar os guións. Antes de publicar nada con esa voz
> quería preguntarvos directamente, porque sei que o modelo ten licenza Apache 2.0, pero os datos de voz de Brais
> teñen condicións de uso para investigación e, sobre todo, porque detrás hai unha persoa.
>
> Concretamente, gustaríame saber:
>
> 1. Se vedes compatible co espírito das condicións dos datos que unha canle pública de divulgación empregue o
>    modelo, primeiro sen monetizar e, se algún día chegase a ter ingresos, monetizada.
> 2. Se o consentimento que deu o locutor cobre este tipo de uso. Se non o cobre ou non está claro, pregaríavos que
>    lle trasladásedes a consulta vós; non quero contactar con el pola miña conta. Se el prefire que non se use a súa
>    voz, cambiarei de voz sen máis. Se o acepta, ofrézolle crédito co seu nome ou sen el, como prefira, e unha parte
>    dos ingresos se algún día os houbese.
> 3. Como preferides que figure o crédito (por exemplo: "Voz sintética: modelo Nos_StyleTTS2-Brais-GL do Proxecto
>    Nós (USC), desenvolvido por Gradiant, licenza Apache 2.0").
> 4. Como preferides que marquemos os textos (descricións, subtítulos e guións) para que non acaben nos corpus de
>    adestramento como se fosen galego revisado. Os guións xéraos unha IA e non hai revisión humana previa, e
>    preocúpame non contribuír a empeorar os datos cos que traballades.
>
> A cambio, gustaríame devolvervos algo útil:
>
> - **Un informe trimestral de erros de pronuncia** en narración longa (a partir de 60 minutos seguidos): topónimos,
>   nomes medievais, vogais abertas e pechadas, números, cambios de prosodia ao longo do audio, con fragmentos de
>   son e a forma correcta.
> - **As correccións que faga a audiencia**, en pares "texto xerado / texto corrixido".
> - **Un conxunto de preguntas de historia de Galicia con fonte**, por se vos serve para avaliar modelos.
> - **O código de todo o proceso**, con licenza libre, e as métricas de cada episodio, incluída unha comparación
>   entre os vosos modelos de lingua e outros pechados.
>
> A canle publicarase co nome da canle e sen o meu nome. Pídovos, se non vos importa, que non fagades público quen
> está detrás; vós si sabedes con quen falades, e contestarei a calquera cousa que precisedes.
>
> Non publicarei nada coa voz de Brais ata ter a vosa resposta. Se nun mes non souben de vós, volverei escribir; e se
> despois dese tempo seguise sen resposta, usaría outra voz ata que poidamos falalo.
>
> Moitas grazas polo traballo que facedes. Grazas a Nós é posible pensar en facer isto en galego.
>
> Un saúdo,
>
> [Nome e apelidos]
> [Correo e teléfono]
> [Ligazón privada a unha mostra de 2-3 minutos do episodio piloto]

**Notas para el promotor (en castellano):**
- Adjuntar una **muestra corta** (2-3 min) con el aviso hablado incluido, en enlace privado. No enviar el vídeo entero.
- Si Nós pide hablar por teléfono o en persona, aceptar: es la mejor señal posible.
- El compromiso "non publicarei nada coa voz de Brais ata ter a vosa resposta" **obliga**: si se envía, se cumple
  (ver §4, fase 0-bis). Si el promotor no quiere comprometerse, hay que borrar esa frase y aceptar el coste
  reputacional descrito en el §4.
- Revisar el texto con un galegofalante antes de enviarlo (es el primer "producto" que verá Nós).

---

## 6. Riesgos de la relación con el ecosistema (resumen)

| # | Riesgo | Prob. / impacto [S] | Mitigación | Sección |
|---|---|---|---|---|
| E1 | El locutor o ADA descubren la voz sin haber sido preguntados | Media sin D4 / alto | D4 antes de publicar; Nós traslada la consulta; cambio de voz en ≤ 30 días | §1.7, §4 |
| E2 | Nós pide no usar su nombre o su voz | Baja-media / medio | Voz de reserva lista; agradecer; seguir ofreciendo datos | §4 |
| E3 | Crítica pública de AGPTI/ADA/A Mesa ("IA contra o galego") | Media si hay eco / alto | Aviso previo; no sustitución; compromiso de revisión profesional; alarma A7 | §1.6-1.8 |
| E4 | Titular "canle anónima de slop" | Media / medio | Página de transparencia; seudónimo con responsable conocido por Nós | §3, §1.11 |
| E5 | Comparación con el caso Caamaño | Baja / alto | Nunca recrear personas ni voces de personas concretas | §1.2 |
| E6 | Ser visto como escaparate de la Xunta | Baja-media / medio | Fuera de política lingüística; no buscar a la SXL | §1.5 |
| E7 | Tesis *pro lingua* desmontada por incoherencia (LLM cerrado, textos que contaminan) | Media / medio | Comparación pública Carballo vs. cerrado; marca de sintético; entregar datos | §2.3 |
| E8 | Divulgadores acusan de usar su trabajo | Baja / medio | Dossier solo con Galipedia y dominio público; "Para saber máis" | §1.10 |
| E9 | Los datos prometidos nunca se entregan (falta de horas) | **Alta** con 1 h/semana / medio | Automatizar la exportación de errores y métricas en el pipeline; compromiso mínimo: informe de voz trimestral | §2.2 |

---

## 7. Supuestos que hay que comprobar

1. Que Nós responde a consultas de particulares y en qué plazo [S].
2. Que el consentimiento del locutor de Brais no cubre por defecto usos públicos de terceros [S; no hay información
   pública en la ficha].
3. Que la audiencia real corrige errores en volumen útil (≥ 1 corrección por episodio) [S].
4. Que Carballo es medible en las mismas métricas que el LLM cerrado con el pipeline actual [S].
5. Que Nós no tiene ya un conjunto de historia de Galicia fuera de Hugging Face (Zenodo, web propia) [S; solo se
   revisó Hugging Face].
6. Que la RAG permite consultar su diccionario de forma automatizada para el control de palabras [S; revisar sus
   términos antes].

---

## Fuentes nuevas de esta pieza (consultadas el 29-09-2026)

- Proxecto Nós, presentación: https://nos.gal/en/proxecto-nos/about-us ; GitHub: https://github.com/proxectonos
- Nós en ILENIA y ALIA, avances en tecnologías del habla (29-05-2026): https://zenodo.org/records/20523403
- Financiación USC 480.000 € (11-07-2026, vía snippet): https://www.elcorreogallego.es/santiago/2026/07/11/usc-recibira-480-000-euros-132359510.html
- Ficha StyleTTS2 Brais (Gradiant, ALIA, evaluación): https://huggingface.co/proxectonos/Nos_StyleTTS2-Brais-GL
- Términos y contacto de los datos de Brais: https://huggingface.co/datasets/proxectonos/Nos_Brais-GL
- Listado de conjuntos de datos de Nós (63): https://huggingface.co/api/datasets?author=proxectonos
- Errores sistemáticos ES-GL: https://huggingface.co/datasets/proxectonos/erros_sistematicos_traducion_es_gl
- Corpus CC0 (incluye guiones de la TVG): https://huggingface.co/datasets/proxectonos/nos_gl_CC0
- Agradecimientos TTS de Nós: https://tts.nos.gal/agradecementos
- Nós, "a IA ao servizo da lingua": https://www.lingua.gal/recursos/todos/_/promovelo/contido_607/nos-intelixencia-artificial-servizo-lingua-galega ; https://nos.gal/en/proxecto-nos/news/usc-xunta-ponen-intelixencia-artificial-servizo-lingua-galega-traves-proxecto
- Campaña "Doa galego": https://praza.gal/ciencia-e-tecnoloxia/doa-galego-o-proxecto-nos-busca-voces-para-acadar-1000-horas-de-gravacion
- CSAG, transformación y proyectos de IA: https://crtvg.gal/w/a-csag-consolida-a-s%C3%BAa-transformaci%C3%B3n-no-principal-ecosistema-audiovisual-p%C3%BAblico-de-galicia
- Críticas a la recreación de Begoña Caamaño (18-05-2026): https://www.nosdiario.gal/articulo/social/que-non-deixala-falar-criticas-ia-empregada-pola-crtvg-recrear-begona-caamano/20260518160723256730.html
- Monteagudo (RAG) sobre la IA (16-05-2026): https://www.elespanol.com/quincemil/cultura/20260516/henrique-monteagudo-presidente-da-rag-sistema-educativo-leva-anos-funcionando-espazo-presion-castelanizadora/1003744246593_0.html
- CCG, *A intelixencia artificial na cultura galega* (2024): https://consellodacultura.gal/publicacion.php?id=4508
- Simposio ILG-CCG sobre IA y galego (nov. 2025): https://consellodacultura.gal/noticia.php?id=11587&tipo=noticia
- Ley gallega de IA y el galego (11-02-2025): https://www.nosdiario.gal/articulo/politica/lei-da-xunta-intelkixencia-artificial-obvia-galego/20250211140946216318.html
- AGPTI, ADA y A Mesa sobre RTVE (20-02-2026): https://www.agpti.org/ada-agpti-mesa-reclaman-tve-cumpra-lei-dobrando-subtitulando-galego-servizos-profesionais-calidade/ ; https://www.nosdiario.gal/articulo/social/mesa-agpti-ada-denuncian-incumprimentos-rtve-coa-programacion-galego/20260220110723248001.html
- AGPTI, decálogo sobre IA (04-09-2026): https://www.agpti.org/defender-o-noso-traballo-e-defender-unha-sociedade-humana/
- Nacimiento de ADA (13-12-2024): https://www.nosdiario.gal/articulo/cultura/nace-ada-primeiro-sindicato-actores-actrices-dobraxe-da-galiza/20241213202608212780.html
- A Mesa, "emerxencia lingüística" (24-09-2026): https://www.nosdiario.gal/articulo/lingua/mesa-sinala-que-emenda-ao-plan-do-pp-sigue-vetando-galego-nas-aulas/20260924133755267588.html
- Trasno y Common Voice: https://trasno.gal/2021/02/07/proxecto-common-voice-en-galego/ ; AGASOL: https://www.agasol.gal/ ; https://www.conselleriadefacenda.gal/-/a-xunta-colabora-con-agasol-para-promover-o-uso-do-software-libre-no-tecido-empresarial-galego
- Divulgación: https://podgalego.agora.gal/descifrando-a-historia/ ; https://historiadegalicia.gal/ ; https://gl.wikipedia.org/wiki/Miguel_%C3%81ngel_Cajigal_Vera ; https://obradoirodixitalgalego.gal/comunidade/
- Reutilizado: `../../gauntlet/investigacion/voz_guion.md`, `audiencia.md`, `ingresos_alt.md`;
  `../../gauntlet/piezas/gtm_riesgos.md`; `plan-desatendido.md`.
