# ecosistema · ronda 4

### Panel: investigadora de Nós + directivo de contenidos de la CRTVG + sociolingüista activista: PIERDE/NO APRUEBA

§1.1 describe mal la postura pública de Proxecto Nós. Afirma que 'el entretenimiento no está en esa lista' de usos declarados, pero la ficha oficial de Nos_StyleTTS2-Brais-GL (https://huggingface.co/proxectonos/Nos_StyleTTS2-Brais-GL) incluye expresamente 'entertainment' entre los usos previstos. Además, la pieza no recoge que el locutor está identificado públicamente: Gaspar González Somoza, actor de dobraxe. Cómo corregirlo:
- Separar la licencia y los usos previstos del modelo, que admiten el entretenimiento, de los términos del dataset, que dicen 'solely for research… no public exposure'. La tensión real está entre esos dos textos, y hay que decirlo así.
- Añadir el riesgo de que el público reconozca la voz de un actor de dobraxe conocido y crea que respalda el canal. Llevarlo a E1/E5 y a la frase de crédito.
- Reescribir la pregunta 1 del correo en galego a partir de esa discrepancia, por ejemplo: 'a ficha do modelo menciona o entretemento entre os usos previstos, pero as condicións dos datos falan de investigación: como o interpretades para unha canle pública?'.
- Actualizar el resumen (punto 6) y la tabla §1.0 en consecuencia.

Errores factuales: §1.1: 'El entretenimiento para dormir no está en esa lista' de usos declarados. La ficha oficial del modelo StyleTTS2 Brais lista expresamente 'entertainment' entre los usos previstos (accessibility tools, virtual assistants, conversational agents, entertainment). | §1.1 cita como fuente de la evaluación de la ficha solo la categoría '> 60 s'. Es correcto, pero la pieza no menciona que la misma ficha fija los usos previstos, entre ellos el entretenimiento, y los contrapone solo al Zenodo.

He leído entero /home/user/revolta/plan-de-negocio/gauntlet2/piezas/ecosistema.md (v4) y he contrastado los hechos clave en la web. La pieza es buena en casi todo. Trata los conflictos reales sin ingenuidad: la voz de un actor de dobraxe, la denuncia de ADA, AGPTI y A Mesa contra RTVE, el decálogo de AGPTI, el caso Caamaño, el anonimato frente al apoyo institucional y la pista en castellano como vía de salida del galego. Su estrategia pro lingua es concreta y falsable: se centra en errores y evaluaciones, no en contenido, compara Carballo con el modelo cerrado, publica la métrica L y tiene alarmas A7-A10.

Hechos confirmados:
- Decálogo de AGPTI del 04-09-2026, con las citas literales.
- Críticas a la CSAG por recrear a Begoña Caamaño, el 17/18-05-2026.
- Monteagudo, presidente de la RAG desde el 04-04-2025.
- Términos del dataset Nos_Brais-GL citados literalmente.
- Brais es un actor de dobraxe profesional (Gaspar González Somoza) y Celtia es Chelo Díaz, actriz de dobraxe.
- La ayuda de YouTube dice que la pista por defecto depende del historial del espectador.
- El pipeline usa de verdad el Whisper galego de Nós (qa.py), como afirma el correo.

El correo en galego está prácticamente impecable. Solo tiene la redundancia de 'co nome da canle e sen o meu nome'.

Aun así, una investigadora de Nós detectaría enseguida un error de hecho en el actor central. En §1.1 la pieza dice que los usos declarados de las voces de Nós son accesibilidad y educación y que 'el entretenimiento para dormir no está en esa lista'. Pero la ficha oficial de Nos_StyleTTS2-Brais-GL, que la propia pieza cita como fuente, enumera entre los usos previstos 'accessibility tools, virtual assistants, conversational agents, entertainment'. Es decir, se atribuye a Nós una postura pública más restrictiva que la que tiene. La pieza tampoco recoge que Nós nombra públicamente al locutor. Eso cambia dos cosas. Primero, el riesgo de reconocimiento: la audiencia puede reconocer una voz conocida de la dobraxe y creer que el actor respalda el canal. Segundo, la pregunta 1 del correo podría apoyarse en la propia ficha. Como no puedo aprobar un análisis que describe mal la postura pública de Nós, suspendo.
