# Guion r1: "As meigas de verdade (e por que o conxuro da queimada é de 1967)"

Constructor: agente guionista (Claude), Gauntlet 3, pieza GUION, ronda 1, 30-09-2026. Documento de trabajo en
castellano; el guion ([`guion-r1.txt`](guion-r1.txt)) está en galego.

**Qué hizo Claude y qué es automático.** El texto lo escribió Claude a mano (no es un LLM por API ni el LLM local ni
una ejecución desatendida), a partir de la ficha `herramientas/pipeline/temas/meigas-de-verdade.yaml` y de
`dossier/dossier.md`. Son automáticos: las puertas de `longo.py --so-texto` (LanguageTool gl-ES + hunspell, H1, estilo y
veracidad con NLI), el comprobador rápido `herramientas/pipeline/probas/guion_rapido.py` y cinco scripts auxiliares
del scratchpad (duración con dos modelos, pares de hechos, densidad de nombres, LanguageTool suelto y mapa de hechos
por frase). La asignación de hechos a cada capítulo la propuso un script por coincidencia léxica y Claude la revisó a
mano. **Ninguna persona ha revisado este guion.**

## 1. Resumen

| Medida | Valor |
|---|---|
| Palabras narradas (cuenta de `longo.py`, sin títulos) | **3.503** (objetivo 3.400-3.700) |
| Frases / párrafos / capítulos | 208 / 58 / gancho sin título + 8 capítulos |
| Duración estimada, modelo A (`guion_rapido.py`: 0,43 s/palabra × escala + pausas) | 35,0-35,2 min |
| Duración estimada, modelo B (ritmo **medido** por la pieza VOZ con esta misma curva, `voz/datos/curva-ronda1.json`) | **25,9 min** |
| Límites de la ficha (`duracion_s`) | 25-35 min |
| LanguageTool + hunspell | **0 avisos** |
| H1 (nombres y cantidades sin anclar) | **0** |
| Estilo (cifras, signos, preguntas, palabras vetadas, aviso y fórmula literales) | **verde** |
| Frases fuera de 8-25 palabras | 6, todas en el gancho (permitido) |
| Veracidad léxica (comprobador rápido) | 0 frases exigidas sin apoyo |
| Veracidad con NLI (`longo.py --so-texto`) | **0 frases marcadas de 208** (0 sin justificar) |

**Las dos estimaciones de duración no concuerdan** (§7, duda 1). El modelo B sale de sintetizar de verdad un pasaje de
111 palabras en 7 frases con la curva actual (182 palabras/min con pausas en el gancho, 145 al empezar el tramo de
dormir y 119 al final), así que es el más fiable: el episodio duraría unos 26 min. Con 3.400-3.450 palabras las dos
estimaciones caen dentro de 25-35 min; con 3.503 el modelo A roza los 35.

## 2. Estructura

Minutos: A = modelo del comprobador rápido; B = ritmo medido de la voz. Fases de `curva.py` por palabras: gancho 0-280,
transición 280-950, calma 950-1.751, dormir 1.751-3.503. Hechos: F-id de `dossier/dossier.md`; con asterisco, hechos
verificados del dossier que están **fuera de la ficha** (`ficha: false`; lista en §6).

| Capítulo | Palabras | Desde palabra | Min A | Min B | Fase | Contenido | Hechos del dossier |
|---|---|---|---|---|---|---|---|
| (gancho, sin título; capítulo de YouTube 0:00 "Un conxuro de 1967") | 281 | 0 | 0,0 | 0,0 | gancho | Conxuro de 1967, con un verso y su autor; la parteira de Vilalba, atribuido; aviso y fórmula; el testimonio está en el Arquivo; adelanto de la vecina que veló y del gato; Inquisición "branda" y jueces ordinarios "moito máis duros" (una vez, sin año); la meiga curandeira; bucle de la lista de Campo Lameiro | F001, F246, F003, F002, F004; F006, F007, F008, F009, F010; F083, F241; F058, F060; F034, F035, F039, F040; F048, F047; F050, F131 |
| I. Sete fontes e un gato | 337 | 281 | 2,3 | 1,7 | transición | Vilalba: María do Barro, alcaiota; las palabras al ganado ("auga de sete fontes"), la corrección del escribano ("auga, digo, leite"), la excomunión. Xinzo de Limia: Ana González, el gato que nadie pudo coger, la arracada rota "polo mal mirar". Creencias contadas como creencias; sin escoba | F051, F006, F012, F053, F054, F055, F056, F057, F058, F059, F060, F061, F063, F064, F068, F067, F069, F071, F072 |
| II. O tribunal e os xuíces | 376 | 618 | 5,2 | 3,8 | transición | Foro mixto; tribunal de 1574 y su última sede, hoy Hotel Compostela; las cifras, "terribles pero moi baixas"; la fiebre llegó sin histeria; la justicia real (uns trinta procesos, todas mujeres, penas en una sola mención); María Cibreira, con empatía (tortura nombrada una vez); Benita Montero, 1826; María Soliña: nombre, juicio, pocos datos, poema y símbolo | F077, F074, F076, F034, F038, F044, F083, F085, F087, F088, F089, F090, F091, F092, F093, F097, F099, F100, F101, F108, F110 |
| III. Quen eran de verdade | 331 | 994 | 8,6 | 6,2 | calma | **Cierre del bucle**: Campo Lameiro, 1643, la lista "porque eran moitas", la costumbre de ir a la fuente y la creencia de esa noche. Quiénes eran: solteras y viudas, parteiras y menciñeiras, "maldita a nai…", necesarias, xenreiras, las ovejas y la viña. Declive tras el primer tercio del XVII y el maíz. "Deixamos atrás os tribunais" | F129, F130, F131, F132, F133, F135, F134, F115, F116\*, F118, F119, F121, F122, F124, F125, F137, F138 |
| IV. O mal de ollo | 512 | 1.325 | 11,8 | 8,5 | calma → dormir (desde la palabra 1.751) | La palabra meiga (latín *medica*, RAG); menciñeira y parteira; Sarmiento; tipos de meigas y "meiga feiticeira"; frases en galego en los procesos; mal de ollo como creencia (eco de la arracada); Risco, Mariño Ferro; meigallo; amuletos, figa, fotos de Henningsen; la cocina, la lareira, la pedra do lar, el escano, la gramalleira, las lacenas; el hórreo y el maíz | F114, F111, F113, F232, F070\*, F086\*, F128, F144, F145\*, F064, F057, F146, F147, F148, F149, F150, F151\*, F152\*, F153, F154, F156, F158, F159\*, F160, F161, F162, F163, F164, F165, F138 |
| V. A noite de san Xoán | 627 | 1.837 | 17,0 | 12,1 | dormir | Invitación a no recordar nada; fecha y solsticio; leña, cacharelas, sardiñas, cachelos y broa; leña verde; saltos impares y su copla; el ganado y el orballo; las siete hierbas y sus flores; "auga de sete fontes" como estribillo de Vilalba; el orballo; el lavado de la cara; ramos en las puertas; refrán y coplas; "meigas fóra"; flor da auga; la moura de la fonte da Moza; el sol que baila; las nueve olas de A Lanzada | F168, F171\*, F170, F172, F177\*, F173, F175\*, F174, F176, F198\*, F178, F179, F180\*, F181, F182, F183, F184\*, F185\*, F186, F187, F188, F053, F054, F189, F190, F191, F192, F193\*, F194, F195, F196, F200\*, F197, F199, F245, F201, F202, F203 |
| VI. O frade que dubidaba | 508 | 2.464 | 23,5 | 16,8 | dormir | Feijoo: nacimiento y 350 años; San Bieito, Samos, Oviedo; *Teatro crítico*; "desenganador das Españas"; el discurso sobre la magia (hay hechiceros, pero no tantos); fábulas que van del pueblo a los libros; cinco causas; el labrador romano; la vieja de la limosna; las brujas más rápidas que las águilas que no alcanzan un burro; el vuelo soñado; no negaba las brujas; la Hueste como luces; mujeres y entendimiento; galego y portugués; salud, muerte y estatua | F205, F206, F207, F208, F209, F210, F212, F213, F214\*, F215, F216, F217, F218\*, F219, F220\*, F221, F222, F223, F224, F225, F226, F227, F228, F229, F230, F231, F233\*, F234, F235 |
| VII. O conxuro do barco | 307 | 2.972 | 29,0 | 20,9 | dormir | La queimada a fuego lento y con las luces apagadas; Castroviejo y el café; no es celta (Alonso del Real, 1972); "tradición inventada" (Xavier Castro); los años cincuenta y la emigración (González Reboredo); conxuros para la ocasión (con "probablemente", porque la fuente dice "xurdiría"); la tarteira de Tito Freire (1955); la taberna de Eligio; el conxuro del barco; otros cinco o seis; copias sin el nombre del autor; registro en 2001 | F029, F028, F030, F031, F032\*, F033, F020, F021, F024, F025\*, F026, F027, F002, F004, F005, F018\*, F014, F015 |
| VIII. Chove na lousa | 224 | 3.279 | 32,3 | 23,5 | dormir | "Habelas, hainas": sin autor conocido y no está en el *Quixote*; Feijoo "á súa maneira"; la exposición del Arquivo y sus expresiones (el verso del conxuro vuelve dentro de esa lista); recapitulación sin datos nuevos; lousado y lousa; lluvia, siete fuentes, brasas, candea; "Boas noites." | F237, F238, F239, F215, F240, F241, F243, F242\*, F190, F244\* |

Posiciones clave (palabra de inicio; tiempo A / B):
- Aviso: palabra 89 (44 s / 32 s). Fórmula: 105 (52 s / 37 s). Las dos van dentro del primer minuto.
- Último caso con nombre (Campo Lameiro): palabras 994-1.090 (8,6-9,4 min / 6,2-6,8 min).
- Cierre del bucle: termina en la 1.138 (9,8 / 7,1 min).
- Fin del bloque de juicios ("deixamos atrás os tribunais e as testemuñas"): 1.315 (11,6 / 8,4 min).
- Empieza el tramo de dormir de la curva: 1.751 (15,9 / 11,3 min).

## 3. Ganchos y bucle

| Orden | Palabra | Qué | Hechos |
|---|---|---|---|
| 1 | 0-42 | El verso "Mouchos, curuxas, sapos e bruxas" (único verso citado) y el golpe: "ten autor coñecido, e é de mil novecentos sesenta e sete", con Mariano Marcos Abalo y el barco de Vigo | F001, F246, F003, F002, F004 |
| 2 | 43-88 | "Vilalba, mil seiscentos dezasete." La parteira Dorotea do Barro, **"segundo declarou unha testemuña"**, "dixera" (un solo testimonio): pasar los dolores del parto a un hombre calzándole los zapatos de la mujer; "saltaría coma un poldro bravo" | F006-F010 |
| - | 89-111 | Aviso literal y fórmula literal | - |
| 3 | 112-145 | El testimonio está en el Arquivo do Reino (credibilidad) y adelanto: "unha veciña que velou esperta unha noite. E un gato que ninguén deu collido" | F083, F241, F058, F060 |
| 4 | 146-204 | Inquisición corregida (§8.1 de `contexto.md`): 92 + 48, una sola a la hoguera, **"segundo o mesmo Arquivo"** y sin año; "Coas meigas, a temida Inquisición foi branda"; los jueces ordinarios, "segundo o investigador Diego Valor Bravo, foron moito máis duros". Se dice una vez | F034, F035, F039, F040 |
| 5 | 205-245 | El giro: la meiga no era la bruja de los cuentos, "era a que curaba…"; Pousa: "figuras apreciadas e necesarias" | F048, F047 |
| 6 | 246-280 | **Bucle abierto**: "E hai unha lista." Campo Lameiro, las mujeres que fueron a la fuente la noche de san Xoán; "Unha testemuña contou por que a fixeron, e volveremos a esa fonte." | F050, F131 |

- **Cierre del bucle**: al empezar el capítulo III ("E por fin, a lista de Campo Lameiro"), palabras 994-1.138: la
  sospecha por las becerras y los leitóns, el espionaje en la fonte da Nogueira, "apuntáronas nunha lista porque eran
  moitas", la costumbre de ir a las fuentes esa noche y la creencia de que las meigas andaban libres: "A mesma fonte,
  a mesma noite, e dúas maneiras de mirala." Minuto 8,6-9,8 con A; 6,2-7,1 con B.
- **Promesa del título**: el 1967 llega en los primeros 10 s; el "por qué" completo (tradición inventada, años
  cincuenta, copias sin el nombre del autor) está en el capítulo VII, que en YouTube aparece como "O conxuro do barco"
  y se puede buscar.
- **Ganchos pequeños del cuerpo**, para sostener la transición: "auga, digo, leite" (F055); "pan, sal, auga nin lume"
  (F056); el gato por el agujero de la puerta (F060); la arracada en tres trozos (F063); nada de escobas (F072); el
  Hotel Compostela sobre la última sede de la Inquisición (F076); Benita Montero en 1826 con la baraja al cuello
  (F097); "maldita a nai que non ensina a súa filla a meigar" (F119); las ovejas que se comieron la viña (F125).
- **La confesión de Cibreira** (las areas de Sevilla) va en el minuto 5-7 (palabra 830), fuera del primer minuto, sin
  pausa cómica y seguida de la explicación de Pousa ("as respostas xa ían nas preguntas").

## 4. Decisiones de estilo

- **Galiza** para el país en la narración (coherente con el reclamo); se mantienen los nombres oficiales (Arquivo do
  Reino de Galicia, Real Audiencia de Galicia, Real Academia Galega, Consello da Cultura Galega). "san Xoán" con
  minúscula, como el diccionario de la RAG («Xuntaron leña para a cacharela de san Xoán», «Polo san Xoán florean as
  abelurias») y el dossier.
- **Voz**: números y años en letra, sin cifras, paréntesis, comillas, exclamaciones ni preguntas. Las citas (el
  verso, "maldita a nai…", refranes y coplas) van tras dos puntos y sin comillas. "do latín médica" lleva tilde para
  que la voz acentúe como en latín (en la comprobación por normalización sigue siendo literal a F114).
- **Atribución siempre**: lo de los juicios con "segundo declarou unha testemuña", "dixera", "segundo esa testemuña,
  viu", "confesou despois de ser torturada"; lo legendario con "crían", "contaban", "críase", "segundo a crenza",
  "contan"; lo de los historiadores con su nombre y su profesión como en la fuente (investigador Valor Bravo,
  historiador Pousa y Castro, antropólogo Henningsen y González Reboredo). Ningún diálogo ni pensamiento inventado.
- **Violencia**: hoguera una vez (la de la Inquisición, en el gancho) y tortura una vez (Cibreira). Quité "tormento"
  de la lista de penas y "torturadas" de la frase de Pousa para no repetirla. Nada de horca, "mataron", garrotes ni
  llamas sobre personas. Las penas de la Real Audiencia van en una sola frase, sin detalle.
- **Embudo en la escritura**:
  - Gancho: 24 frases, media de 11,6 palabras, cortes de 4-7 palabras ("Vilalba, mil seiscentos dezasete." "E hai
    unha lista."), un "ti" ("parece levarte moitos séculos atrás") y el bucle.
  - Transición: relato con nombres, lugares y años (media de 17,9 palabras).
  - Calma: definiciones y vida de la casa (16,9).
  - Dormir: frases más largas y regulares (media de 18,0, mediana de 18), sin nombres nuevos inquietantes y con
    imágenes sensoriales verdaderas (lume, fume, orballo, herbas, auga de sete fontes, lousa, chuvia, brasas,
    candea). Al entrar en dormir hay una invitación: "non tes que lembrar nada do que escoites".
- **Zona de dormir limpia**: ni intrusiones nocturnas, ni gatos en la cama, ni demonios en el camino, ni calaveras, ni
  el asalto de Cangas. El "corpo finxido" en la cama y el gato de Xinzo van en la transición (minuto 2-5). "demo"
  solo aparece en la zona de dormir dentro de la explicación racional de Feijoo. La Hueste se cuenta por sus luces, no
  como procesión (nota del dossier a F229).
- **Remedios solo como costumbre**: amuletos, ramos, lavado de la cara, flor da auga y orballo van siempre con "críase",
  "crían" o "era costume". Nada de eficacia. "moitas delas medicinais" es la descripción del dossier (F178), no un
  consejo.
- **Estribillos y ecos** para una segunda mitad previsible: las "sete fontes" de Vilalba vuelven en el cacho de san
  Xoán y en la última imagen; la arracada de Xinzo vuelve en el mal de ollo; el maíz de Pousa vuelve en el hórreo;
  Feijoo vuelve en "habelas, hainas"; la lista del Arquivo recoge el verso, "habelas, hainas", "meigas fóra" y María
  Soliña, que ya se oyeron.
- **Nombres por minuto**: como máximo 9 nombres nuevos en 110 palabras (en el gancho). Recorté nombres donde se
  amontonaban: la Virxe do Carme, "ou María Soliño", Laxeiro, Lugrís y Blanco Amor, Santa Mariña das Fragas y el
  título del poema.
- **Frases que no usé** aunque están en el dossier:
  - Marta de Quián (Lalín, 1611): es un juicio con nombre. El arco del crítico la ponía después del minuto 10, pero
    `contexto.md` §8.4 cierra los juicios en el 10, y antes no cabía.
  - F036 (Valor Bravo, "en tres séculos"), F041-F043 (horca y hoguera de la justicia ordinaria): violencia; basta la
    mención del gancho.
  - F081: quemas colectivas.
  - F079: racionalismo; lo sustituí por F038 y F044.
  - F103-F106 (María Soliña): se queda en nombre y poema.
  - F112: el pacto con el demonio.

## 5. Salida de las puertas

**Comprobaciones rápidas, sin candado** (versión final del guion):
- `probas/guion_rapido.py`: 3.503 palabras, H1 sin anclar = `[]`; estilo: cifras `[]`, signos `[]`, 0 preguntas,
  vetadas `[]`, aviso y fórmula literales; 6 frases fuera de 8-25, todas en el gancho; veracidad léxica: **0 frases
  exigidas sin apoyo**.
- LanguageTool gl-ES + hunspell (`qa.lingua`, la misma función de la puerta): **0 avisos**. Dos avisos intermedios se
  corrigieron sin estropear el texto:
  - "con el facían vasoiras": `GENERAL_VERB_AGREEMENT_ERRORS`, que toma "el" por sujeto. Quedó "co que se facían
    vasoiras".
  - "o orballo lles daba ás herbas": `GENERAL_NUMBER_AGREEMENT_ERRORS`, falso positivo con el doblado del
    complemento indirecto. Volví a la redacción del dossier (F191), que es igual de natural.

**Puerta completa** (`longo.py --so-texto`, código de la rama con el commit 2d829b5 de la veracidad rápida). Guion con
md5 `661b07eab707de047468ce2b93d00a59`, igual que [`guion-r1.txt`](guion-r1.txt). Salida copiada en
[`porta_texto-r1.json`](porta_texto-r1.json):

```
portas de texto: {'lingua_lt': True, 'h1_ancoraxe': True, 'veracidade': True, 'estilo': True} | palabras: 3503 | frases marcadas pola veracidade: 0 | sen xustificar: 0
```

| Puerta | Resultado |
|---|---|
| Lengua (LanguageTool gl-ES + hunspell, bloqueante) | 0 avisos |
| H1 (bloqueante) | 192 nombres y cantidades, 0 sin anclar (100 %) |
| Estilo (bloqueante) | 0 cifras, 0 signos prohibidos, 0 preguntas, 0 palabras vetadas; aviso y fórmula literales; 6 frases fuera de 8-25, todas en el gancho; máximo de 9 nombres nuevos por 110 palabras |
| Veracidad (NLI mDeBERTa + coincidencia léxica + reglas duras) | 208 frases evaluadas, **0 marcadas**. No hace falta fichero de excepciones |
| Tiempo | 144 s de reloj, 481 s de CPU |

Cómo se ejecutó:
- Primer intento con el candado de CPU y el código anterior (NLI contra los 180 hechos en cada frase). Esperó ~15 min
  en la cola y lo canceló el orquestador tras 43 min de reloj (≈ 155 min de CPU), porque bloqueaba al agente visual.
  No llegó a escribir resultados.
- Segundo intento, el que vale: por indicación del orquestador, sin candado, con `nice -n 5` y `OMP_NUM_THREADS=2`,
  y el NLI solo contra los hechos con coincidencia ≥ 0,5.

## 6. Hechos del dossier fuera de la ficha

Son 25 hechos que están en `dossier/feitos.yaml` y en la tabla de `dossier.md`, con cita comprobada, pero con
`ficha: false`: F018, F025, F032, F070, F086, F116, F145, F151, F152, F159, F171, F175, F177, F180, F184, F185, F193,
F198, F200, F214, F218, F220, F233, F242 y F244. Los usé solo en frases **sin nombres propios ni cantidades nuevas**
(H1 no los puede comprobar y la veracidad no los exige), casi todos en calma y dormir: costumbres de san Xoán,
amuletos, la lousa, la candea, las causas de Feijoo. Cambios de redacción:
- F152: "bolsiña" pasa a "bolsa pequena", para que hunspell no la marque.
- F185: "facíanse" pasa a "se facían".
- F025: lleva "probablemente", porque la fuente dice "xurdiría".
- F180: sin el nombre de Taboada Chivite.

**Sugerencia para la pieza DOSSIER**: reactivarlos en la ficha (quitar `ficha: false` y regenerar), para que la
auditoría automática también los cubra.

## 7. Dudas para los críticos

1. **Duración.** Con el ritmo medido de la voz (modelo B), 3.503 palabras dan unos 26 min, cerca del mínimo de 25; con
   el modelo del comprobador rápido (A) dan 35,2, en el máximo. El rango de 3.400-3.700 palabras del encargo solo es
   compatible con las dos estimaciones hacia 3.400-3.450. Si el primer render de voz sale por debajo de 26 min, la
   ronda 2 puede añadir 150-250 palabras verdaderas: Marta de Quián antes del minuto 10 (con B hay sitio) o más
   costumbre de san Xoán. También puede hacerlo la curva de la pieza VOZ, con más escala o pausas al final.
2. **Capítulo VII, "O conxuro do barco".** Lo añadí entre Feijoo y el cierre. El arco del crítico no lo tenía, pero el
   dossier coloca la queimada "arranque en frío ou peche". Motivo: la promesa del título se cumple en un capítulo
   que aparece en YouTube con su nombre, y es una escena de fuego y amigos con las luces apagadas, apta para dormir.
   Alternativa: fundirlo con "Chove na lousa".
3. **Nombres en la zona de dormir.** Feijoo y la queimada traen nombres nuevos (Castroviejo, Alonso del Real, Xavier
   Castro, González Reboredo, Tito Freire, Eligio, Cunqueiro). Ninguno inquieta, pero son datos nuevos al final.
4. **María Soliña.** El encargo dice "solo nombre y poema"; el guion añade una frase que dice que la juzgó la
   Inquisición, que hay pocos datos (CCG) y que hoy es un símbolo. Sin fechas, sin quema y sin biografía.
5. **Benita Montero (1826, emplumada y montada en una bestia).** Es humillación pública, no violencia física, y va en
   el minuto 5-7. ¿Demasiado para la transición?
6. **Juicios y minuto 10.** El último caso con nombre termina en la palabra 1.090 (A 9,4 min; B 6,8). El resto del
   capítulo III habla de denuncias en general (quiénes eran, xenreiras, declive) hasta la palabra 1.315 (A 11,6;
   B 8,4). ¿Cuenta como "juicios" para la regla?
7. **Frases de ambiente sin dato.** Hay unas pocas, en calma y dormir: "É unha noite de lume e de auga…", "mentres o
   fume subía amodo na noite", "lonxe as sete fontes seguen correndo na escuridade", "a casa descansa baixo a
   chuvia", "Xa se pode apagar a candea…". Van siempre dentro de párrafos con hechos. ¿Relleno aceptable?
8. **Pronunciación (para la pieza VOZ).** Nombres con riesgo de WER: Feijoo y María Feijoa (la "j"), Castroviejo,
   Henningsen, Hueste, Alonso del Real, Monterrei, Maquieira; y "arraiar", "tódalas" y "abrancazadas".
9. **Aniversario de Feijoo.** "O oito de outubro de dous mil vinte e seis fai trescentos cincuenta anos que naceu" vale
   si se publica en torno al 8-17 de octubre (nota de F206). Después habría que cambiar el tiempo verbal.
10. **Galiza frente a Galicia en la coincidencia léxica.** La veracidad compara raíces: "Galiza" (galiz) no coincide
    con "Galicia" (galic) de los hechos. No marca ninguna frase, pero rebaja algo la coincidencia en las que la
    llevan.

## 8. Pistas para imagen y sonido (propuesta, las decide cada pieza)

| Tramo | Imagen | Sonido (catálogo D14) |
|---|---|---|
| Gancho: conxuro | Pota de barro con lume azul en una cocina de piedra a oscuras; puerto de Vigo de noche | lume + noite |
| Gancho: Vilalba, Arquivo | Aldea de granito; legajos y pluma a la luz de la vela | aldea / limpa |
| Gancho: Inquisición | Compostela de noche, piedra mojada | campas / choiva |
| I | Ganado en el monte, fuentes de piedra, una vecina hilando en la puerta, un gato en un curral (sin cama) | aldea, fonte, noite |
| II | Sala de audiencia con velas; mercado de Compostela (Benita); costa de Cangas en calma (sin barcos turcos) | campas, xente (mercado), mar |
| III | Fonte da Nogueira de noche, mujeres con cántaros, una lista escrita | fonte + noite |
| IV | Lareira, escano, gramalleira, lacenas; amuletos (figa de azabache, castaña, ajo); vacas; hórreo | lume, aldea |
| V | Cacharelas lejanas, sardinas y broa; hierbas en una talla al rocío; lavado de cara al amanecer; mar de A Lanzada | lume + xente (murmullo), fonte, noite, mar |
| VI | Monasterio de Samos, claustro, libros, lluvia en la ventana; castaños | campas, choiva |
| VII | Queimada con las luces apagadas; taberna; barco viejo en el puerto de Vigo | lume + xente, mar |
| VIII | Tejados de lousa bajo la lluvia; brasas; una candea que se apaga; fundido a negro | choiva + lume |
