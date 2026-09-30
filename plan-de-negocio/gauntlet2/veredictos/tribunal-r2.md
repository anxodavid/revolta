# Tribunal · ronda 2

### operador: NO APRUEBA (lo que falta es menor)

El vídeo de ejemplo (§0.3, §5.1, §9 semana 2-3, A.4) es el mismo MP4 suspendido en r3 y r1 (commit b5ce409). Es un guion de dossier literal con unas 6 repeticiones de 'botou abaixo moitas fortalezas', un gancho sin referente y sin picante. Las imágenes no son gallegas (0:55) y tienen multitudes y caras deformes (1:43-1:44, 2:31, 2:46). Encaja exactamente con 'image slideshow with minimal narrative / templated storyline' de la política de contenido inauténtico.

Acción concreta: adelantar ya, antes del tribunal, lo que §9 deja para las semanas 2 y 3.
- (1) Backend de API en llm.py.
- (2) Regenerar la muestra de irmandiños (o de una lenda, para probar el catálogo ampliado) con el guion por Sonnet u Opus 5.5 y un gancho verdadero de contraste o detalle cotidiano en los primeros 60-120 s.
- (3) Aplicar al menos los vetos por iconografía y conteo de personas de §5.3 y regenerar los planos de 0:55, 1:43-1:44, 2:31 y 2:46.
- (4) Publicar en qa.md los umbrales (1)-(5) de P-guion medidos: ≥ 90 % de bloques del LLM, 0 n-gramas repetidos de ≥ 4 palabras, 0 avisos de LanguageTool y de veracidad, coste por minuto y gancho con referente.

Coste según el propio §3.3: 0,05-0,15 USD más ≈ 1,5 h de CPU. Mientras la única prueba del producto sea este MP4, el plan no demuestra que el canal pase el listón.

**Errores:** §4.4 marca como 'Sin verificar [S]' que el galego sea idioma admitido como pista de audio. La ayuda de YouTube sobre multi-language audio (support.google.com/youtube/answer/13338784) incluye el galego en su lista de idiomas admitidos. Se puede pasar a [F]; la comprobación en Studio de la semana 1 solo es necesaria como confirmación. | §0.3 y §5.3 describen defectos del vídeo que siguen ahí: el MP4 no se re-renderizó tras el tribunal r1 (git log del MP4: último commit b5ce409). El texto es correcto, pero el plan presenta como tratadas unas carencias que en el artefacto siguen intactas. | Subtítulo 13 ('A xente de Galicia botou abaixo moitas fortalezas dos señores') adelanta el desenlace antes del contexto cronológico, contra el 'orden cronológico' que el propio §5.3 pone como puerta de coherencia; no figura en la lista de defectos conocidos del §5.3.

He leído contexto.md entero: las secciones PRIORITARIO, la pregunta obligatoria del nicho y las decisiones del 29 y 30-09 (guion por API, ganchos solo al principio, toda Galicia, pistas gl+pt+es+en). También el plan v2 completo (1.011 líneas), qa.md, subtitulos.gl.srt, la hoja de contactos y tribunal-r1.md, y he comprobado en git el historial del MP4.

Lo que está bien, y es de lo mejor que he visto en canales faceless:
- El veredicto del nicho es explícito ('no hay evidencia suficiente, probablemente marginal'), separa los tres nichos con cifras y trae una prueba falsable en dos pasos que distingue 'sin exposición' de 'sin demanda', con umbrales congelados de antemano.
- La siembra está declarada. Asume que el YPP se puede rechazar (40-60 %) y que el canal pierde dinero.
- Tiene en cuenta el Right to Monetize y deja fuera la pista es el primer año.
- Añade la puerta P-guion con 7 umbrales y parada en la semana 4.
- Comprobado en la web:
  - Los precios de la API cuadran con la documentación: Opus 5.5 a 4/20 $, Sonnet 5.5 a 2/10 $, lecturas de caché a 0,20 $ y lotes al −50 %.
  - El coste de 1-1,7 USD por episodio es plausible.
  - La política de contenido inauténtico se evalúa por canal y pone como ejemplos 'image slideshows with minimal narrative' y 'templated storylines'.
  - La pista por defecto se elige según el historial del espectador.

Por qué no apruebo: el listón pide que el canal Y EL VÍDEO DE EJEMPLO funcionen en YouTube sin chocar con esa política, y el vídeo no ha cambiado. El ejemplo.mp4 es el del commit b5ce409, el mismo que suspendieron el crítico del vídeo en r3 y los tres jueces en r1. El propio plan lo admite (A.4: 'la muestra publicada sigue siendo la de la ronda 3').

En el SRT:
- Es el dossier casi literal: el QA muestra que 0 de 18 párrafos son del LLM y todos van a reserva literal o mixta.
- 'botou abaixo / derrubaron moitas fortalezas' sale unas 6 veces, con tautología en los subtítulos 22-24.
- El gancho 'Dicían que eran refuxios de malfeitores' no tiene referente.
- La línea 13 adelanta el desenlace antes del contexto.
- Hay errores de galego: 'ao limiar' y 'lembrando co que viran'.
- No hay ningún gancho con picante, que es justo lo que pidió el promotor el 29-09.

En la hoja de contactos:
- A 0:55, campiña llana, cipreses, carro de ruedas de radios y sombreros del XIX.
- A 1:43, multitud con caras deformes, fachadas pastel, farola con cables y obispo con casulla verde.
- A 2:31 y 2:46, multitudes de soldados.

Es literalmente el 'image slideshow with minimal narrative + templated storyline' de la política.

Todo el plan descansa en un 'se regenerará en la semana 2' (P-guion), cuando regenerar la muestra de 3 min cuesta, según el propio §3.3, 0,05-0,15 USD más ≈ 1,5 h de CPU. No hay razón para presentarlo al tribunal sin esa prueba. Un plan que no demuestra con su único artefacto que la decisión clave (guion por API más puerta de imágenes endurecida) resuelve el problema no me convence de que el canal pase la revisión del YPP ni de que retenga más de 2 min.

### ecosistema: NO APRUEBA

§5.2 (tabla 'Modelo probado en CPU' y 'Lectura'), §6.2 (Contradicción 1 y la fila 'Banco de pruebas de redacción en galego'), §3.3 y el párrafo del correo (§6.4) que empieza 'O guión redáctao un modelo de linguaxe comercial…'. La contradicción entre guion cerrado y tesis pro lingua se resuelve con ingenuidad, por tres motivos:

(a) El banco de pruebas que justifica el modelo cerrado, y que el plan quiere publicar cada trimestre como su aportación más citable, compara los modelos de Nós en condiciones que Nós no aceptaría:
- Llama-3.1-Carballo-Instr3 se probó como redactor por instrucciones, cuando su ficha dice que es 'ready-to-use only for causal language modeling'.
- Todo se cuantizó a Q4_K_M y se corrió en 4 núcleos de CPU.
- Faltan Salamandra-7b-instruct (BSC, con galego), EuroLLM-22B y los modelos abiertos grandes.

Publicar cada trimestre que 'los modelos de Nós fallan' con ese protocolo enfrentaría al canal con su socio principal.

(b) El plan nunca evalúa la opción obvia que sí respeta la decisión del promotor ('LLM potente por API', no 'cerrado'): modelos de pesos abiertos servidos por API, como Qwen, Mistral, Llama o EuroLLM-22B en un proveedor de inferencia. El §3.3 solo da precios de Anthropic.

(c) Las aportaciones de datos (pares en esquema galician-gec-corpora y conjunto de fidelidad, con CC-BY 4.0) tienen como lado fuente texto generado por Claude. Los Commercial Terms de Anthropic prohíben al cliente usar los servicios 'to build a competing product or service, including to train competing AI models'. Nós entrena LLM (Carballo, dentro de ILENIA). Ni el plan ni el correo declaran esa procedencia ni esa limitación.

Qué hacer:
1. Rehacer el §5.2 y el banco de pruebas con un protocolo justo, acordado con Nós antes de publicar nada: formato de prompt oficial de cada modelo, few-shot para los modelos base, bf16 en GPU (gratuita o alquilada por horas), e incluir Carvalho-Salamandra-Instruct, Salamandra-7b-instruct, EuroLLM-22B y 1-2 modelos abiertos grandes. Los resultados se envían primero a Nós en privado.
2. Añadir al §3.3 y a P-guion una columna 'modelo de pesos abiertos por API', con coste y resultado. Si pasa las puertas, preferirlo; eso convierte la contradicción en coherencia.
3. En el §6.2 y en el correo, declarar qué modelo generó cada texto y la cláusula de su proveedor; etiquetar los conjuntos como de evaluación, y que el valor para entrenar lo aporte el lado corregido por humanos.
4. Reescribir la frase del correo sobre Carballo/Carvalho para no presentarlos como fallidos en una tarea para la que no están hechos.

**Errores:** §5.2: 'Llama-3.1-Carballo-Instr3: sin plantilla de chat; no hace la tarea' presenta como fallo lo que es un uso fuera de alcance. Su ficha dice 'The Carballo-Llama-Instr3 model is ready-to-use only for causal language modeling' (https://huggingface.co/proxectonos/Llama-3.1-Carballo-Instr3). No es un modelo instruccional, y la conclusión 'los modelos abiertos no siguen instrucciones' no se puede apoyar en él. | §6.2 y §6.4 (correo): ofrecen a Nós pares y un conjunto de fidelidad con licencia CC-BY 4.0 cuyo texto fuente genera Claude, sin mencionar que los Commercial Terms de Anthropic prohíben al cliente 'access the Services to build a competing product or service, including to train competing AI models' (https://www.anthropic.com/legal/commercial-terms). Nós entrena LLM (Carballo, proyecto ILENIA). | §6.4, galego del correo: 'e prohiben a exposición pública das gravacións' debe ser 'prohíben' (hiato acentuado según las Normas ortográficas e morfolóxicas del idioma galego, RAG-ILG). | §5.3, conjunto de oro: omite 'Decididos os veciños da cidade e os labregos da comarca, botaron abaixo…' (subtítulos 33-34), una construcción forzada que el tribunal r1 también señaló. Además, los errores 'ao limiar' y 'lembrando co que viran' los introdujo el LLM: el dossier dice 'no limiar' y 'lembraban o que viran' (herramientas/pipeline/probas/llm_carballo_instr3). La puerta de veracidad no detecta la degradación de la lengua respecto al dossier. | Vídeo (sin corregir desde la ronda 3): la voz entra de golpe a 3,0 s (de −40 a −14,5 dBFS sin rampa) y el ASR transcribe 'as noites'. Siguen el carro de ruedas de radios y los cipreses a 0:55, las fachadas pastel y el obispo con casulla verde a 1:43, y los tejados naranjas a 2:46.

Leí contexto.md entero, con las secciones PRIORITARIO, la pregunta obligatoria del nicho y las decisiones del promotor: guion por LLM vía API, ganchos solo al principio, temas de toda Galicia y pistas gl+pt+es+en. También leí el plan v2 completo (1.011 líneas), qa.md y subtitulos.gl.srt, y miré la hoja de contactos. Medí el arranque del audio del MP4 y comprobé en la web, en la API de Hugging Face y en las fichas de los modelos lo que el plan dice de Nós, de la CSAG y de AGPTI.

Lo que está bien, y es bastante:
- El veredicto del nicho es honesto ('no hay evidencia suficiente, probablemente marginal'), con tres nichos cifrados y una prueba falsable en dos pasos que separa 'sin distribución' de 'sin demanda'.
- La voz de Brais está bien tratada. Sin un sí escrito no se publica. Se cita la cláusula Right to Monetize. Se recoge la tensión real entre la ficha del modelo, que incluye el entretenimiento, y las condiciones de Nos_Brais-GL: investigación y herramientas de IA con fines lingüísticos, sin exposición pública. El locutor está identificado y se nombran voces de reserva con crédito al CRPIH y a la UVigo.
- El aviso hablado es veraz, no hay pista es el primer año y la política de ganchos es digna, sin contrastes hacia abajo.
- Las carencias de la ronda 1 del tribunal están corregidas. Hay inventario de los 63 conjuntos de Nós y se descarta el banco de preguntas; los pares van en el esquema de galician-gec-corpora (compruebo que existen cortegal, gec_synthetic, wikipedia_breobot y demás, con CC-BY 4.0). Hay puerta de lengua medida, lectura ciega en P0 y horas de oído galegofalante.
- Hechos que comprobé y son correctos: la CSAG sustituye a la CRTVG (Lei 1/2025), la recreación de Begoña Caamaño es del 17-05-2026, el StyleTTS2 lo desarrolló Gradiant y Nós publica 63 datasets y 63 modelos.

Sobre el vídeo:
- Sigue siendo el de la ronda 3, generado con EuroLLM, y el plan lo admite. El galego tiene errores introducidos por el LLM que ni siquiera estaban en el dossier: el dossier dice 'no limiar' y el LLM escribió 'ao limiar'; el dossier dice 'lembraban o que viran' y el LLM escribió 'lembrando co que viran'. También hay una tautología en los subtítulos 22-24, un gancho sin referente y la construcción forzada 'Decididos os veciños…', que el tribunal señaló pero que no está en la lista del conjunto de oro del §5.3.
- En la imagen siguen los mismos defectos: cipreses y carro de ruedas de radios a 0:55, fachadas pastel y obispo verde a 1:43, tejados naranjas a 2:46.
- La voz entra de golpe a 3,0 s, de −40 a −14,5 dBFS sin rampa, y el ASR transcribe 'as noites'.

El correo a Nós está en un galego correcto y cuidado, salvo 'prohiben', que debe ser 'prohíben'.

Por qué no apruebo: ante una investigadora de Nós, el punto más delicado de la tesis pro lingua, un guion escrito por un LLM cerrado y comercial, se resuelve con ingenuidad, y eso afecta justo a las aportaciones que se presentan como 'las más citables' (ver la mayor carencia).

### realista: NO APRUEBA

§3.2 'Escenarios a 12 meses' no cuadra con §2.3 y §2.4. Hay que rehacer la tabla de §3.2 condicionándola a los cuatro resultados de P1: PARADA por distribución, PARADA por nicho, MÍNIMO y PLAN.
- **Probabilidades:** usar las mismas de §2.4 (10-15 / 20-30 / 40-50 / 10-20 %).
- **Episodios por rama:** 8 si hay PARADA; ≈ 15-17 en MÍNIMO (1 al mes tras el episodio 8); ≈ 30 solo en PLAN.
- **Vistas y horas:** calcularlas a partir de esos episodios y de la mediana de cada rama.

Así P(M ≥ 150) sale igual en §2.3, §2.4 y §3.2, en vez del 15-25 % frente al ≈ 35-45 % implícito de hoy. Después hay que recalcular con esa tabla el valor esperado de ingresos, las horas del primer año por rama y la probabilidad de D1/P3, y corregir la frase 'solo el optimista se acerca al YPP': el techo del base da ≈ 9.000 h. De paso, ajustar en §3.4 y §9 el presupuesto de P-guion a lo que caben 4 semanas × 6 h (o alargarlo a 5-6 semanas), cuadrar las 85-118 h del MVP con la suma de partidas (82-123 h) y corregir el 'hasta ≈ 20 €' del arranque con Opus a ≈ 21-48 €.

**Errores:** §3.3, caja mensual: 'hasta ≈ 20 € en el arranque con Opus sin optimizar' no cuadra con la propia tabla. 4-5 episodios × 6-11 USD = 24-55 USD ≈ 21-48 € (a 0,87 €/USD). | §0.2 y §3.2: 'Solo el escenario optimista se acerca al YPP' es falso con sus supuestos. El techo del base, 27 K vistas × AVD de 15-25 min, da ≈ 6.700-11.000 h, que alcanza las 8.000 h. | §2.3 frente a §3.2: P(mediana ≥ 150) = 15-25 % y PLAN = 10-20 % (§2.4), mientras que los escenarios base (30-38 %, mediana 100-600) y optimista (8-12 %) implican ≈ 35-45 %. | §3.2: las vistas a 12 meses suponen ≈ 30 episodios en todos los escenarios, aunque PARADA (8 episodios) y MÍNIMO (1 al mes) suman el 70-95 % según §2.4. | §0, §3.4 y §8.1: 'coste hundido ≈ 24-30 h' en 4 semanas con D3 = 6 h/semana (máximo 24 h). Además, las tareas de las semanas 1-4 suman ≈ 25-39 h con las propias estimaciones de §3.4. | §3.4: el MVP de '85-118 h' no coincide con la suma de sus partidas: 57-85 + 3-5 + 3-5 + 2-3 + 2 + 4-6 + 5-8 + 3-4 + 3-5 = 82-123 h. | Verificado como correcto: precios de Opus 5.5 (4/20 $), Sonnet 5.5 (2/10 $), lecturas de caché a 0,20 $ en ambos y lotes al −50 % (platform.claude.com/docs/en/about-claude/pricing); YPP con 8.000 h o 20 M de vistas de Shorts desde el 1-02-2027, sin suscriptores (blog.youtube).

Evaluación como business angel realista de hobbies con opción de negocio. Leí contexto.md entero, el plan v2 completo (1.011 líneas), qa.md, el SRT y la hoja de contactos.

Lo que convence:
(1) La pregunta obligatoria del nicho tiene una respuesta honesta y con cifras: 'no hay evidencia suficiente; probable marginal'. Separa (a), (b) y (c), da evidencia a favor y en contra con fuente, y el embudo 2,34 M → 60-84 K → 2-20 K → 20-1.000 personas.
(2) La prueba falsable es buena. Separa 'sin exposición' de 'sin demanda' y usa umbrales congelados: CTR < 2 %, R2 < 25 %, Gs < 35 %, fallando 2 de 3.
(3) La puerta P-guion de la semana 4 corta la pérdida en ≈ 24-30 h y < 5 € antes de invertir el MVP.
(4) D1 (P3) está atado a KPIs concretos (2 de 3: 500 suscriptores, 3.000 h, mediana ≥ 1.000), con voz autorizada.
(5) El vídeo se describe con franqueza. La hoja de contactos confirma los defectos citados:
- 0:55: llanura no gallega, carro de ruedas de radios.
- 1:43: casulla verde, fachadas pastel y multitud.
- 2:31 y 2:46: grupos numerosos de soldados.
El guion es dossier casi literal con 'botou abaixo moitas fortalezas' repetido. El plan admite que ningún humano ha aprobado un vídeo desatendido.

Comprobado en la web: los precios de la API (Opus 5.5 4/20 $, Sonnet 5.5 2/10 $, lecturas de caché a 0,20 $ en ambos y lotes al −50 %) y el umbral del YPP de 8.000 h desde el 1-02-2027, sin mención de suscriptores. El cálculo de 1-1,7 USD por episodio con Sonnet, caché y lotes es aritméticamente coherente con la tabla de tokens.

Por qué no apruebo: el listón pide retornos y horas coherentes en todo el documento, y el modelo de retornos (§3.2) no cuadra con el del nicho (§2.3 y §2.4).
- **Probabilidades que no cuadran.** §2.4 da PLAN (M ≥ 150) un 10-20 % y §2.3 da P(mediana ≥ 150) un 15-25 % para (b). En cambio §3.2 da al escenario base un 30-38 % con mediana 100-600 ('MÍNIMO o PLAN') y al optimista un 8-12 % con 600-4.000. Eso implica P(M ≥ 150) ≈ 35-45 %, el doble.
- **Número de episodios.** §3.2 calcula las vistas a 12 meses sobre ≈ 30 episodios en todos los escenarios. Pero §2.4 da PARADA (8 episodios) al 30-45 % y MÍNIMO (1 al mes, ≈ 15-17 episodios) al 40-50 %. Con eso, las vistas, los suscriptores y las horas del pesimista y del base están infladas.
- **YPP.** La frase 'solo el optimista se acerca al YPP' es falsa con sus propios supuestos: 27 K vistas × 20 min de AVD ≈ 9.000 h, por encima de 8.000.

Incoherencias menores de horas y costes:
- Las 4 semanas de P-guion a 6 h/semana dan como máximo 24 h, no 24-30 h. Además las tareas del §9 suman ≈ 25-39 h: backend de API 3-5, coherencia 3-5, imágenes 4-6, conjunto de oro y lengua 9-14, pruebas ciegas 3-4, voces de reserva 2-3, más correo y verificaciones. O P-guion llega en la semana 5-7 o se rompe D3.
- Las partidas del MVP suman 82-123 h, no 85-118 h.
- 'Hasta ≈ 20 € en el arranque con Opus sin optimizar': 4-5 episodios × 6-11 USD ≈ 21-48 €.

El fondo es sensato y apostaría las 24-30 h de P-guion. Pero no firmo un plan cuyo cuadro de retornos contradice sus propias probabilidades de parada.
