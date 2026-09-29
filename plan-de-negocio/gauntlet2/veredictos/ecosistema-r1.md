# ecosistema · ronda 1

### Panel: investigadora de Nós + directivo de contenidos de la CRTVG + sociolingüista activista: PIERDE/NO APRUEBA

El análisis de la voz y el correo a Nós ocultan el conflicto más serio: el pipeline usa en producción una grabación humana del dataset protegido Nos_Brais-GL (REF_WAV = brais_1_human.wav en herramientas/pipeline/pipeline.py y herramientas/voz). Los términos de ese dataset, aceptados al descargarlo, lo limitan a investigación y herramientas lingüísticas, reservan el acceso a quienes colaboran con el CRPIH/USC y prohíben la 'public exposure'. El correo dice 'os datos de voz de Brais teñen condicións de uso para investigación' como si el promotor no los estuviera usando. Qué hacer:
(a) Añadir en §1.1 y §6 un riesgo explícito sobre el uso de datos protegidos en producción.
(b) Hacer una de dos cosas: sustituir REF_WAV por audio sintético del propio modelo (o por el estilo por defecto) y medir si se pierde calidad; o declararlo en el correo con una frase en galego, por ejemplo: 'Para fixar o estilo da voz usei unha gravación do conxunto Nos_Brais-GL, ao que accedín aceptando as vosas condicións; se non é compatible, deixarei de usala'.
(c) Corregir el §1.1: la ficha del modelo lista 'entertainment' entre sus usos previstos.
(d) Alinear el §4 (silencio a 45 días) con la promesa del correo y con la regla de piezas/voz.md: no publicar con Brais sin un sí por escrito.

Errores factuales: §1.1 dice que el entretenimiento no está entre los usos declarados de las voces de Nós. La ficha del modelo https://huggingface.co/proxectonos/Nos_StyleTTS2-Brais-GL lo incluye de forma expresa: 'accessibility tools, virtual assistants, conversational agents, entertainment'. | Los términos de Nos_Brais-GL también limitan el acceso a entidades que colaboran con el Centro Ramón Piñeiro/USC. La pieza no lo menciona y trata esos datos como algo que el canal no usa, cuando el pipeline sí usa una grabación del dataset como REF_WAV. | Contradicción interna: el correo (§5) promete usar otra voz si el silencio continúa, pero el §4 contempla publicar con Brais sin monetizar a los 45 días de silencio.

Es un análisis serio y en general bien informado. He comprobado en la web los hechos principales y son correctos:
- Monteagudo preside la RAG desde el 04-04-2025.
- La CRTVG pasó a ser la CSAG por la Lei 1/2025.
- El caso Caamaño fue el 17-05-2026, con la crítica de Belén Regueira y la frase 'deixala falar'.
- El decálogo de AGPTI es del 04-09-2026 y las citas son literales.
- ADA se fundó en diciembre de 2024.
- Brais es la voz de un actor de doblaje profesional, según tts.nos.gal.
- Los términos del dataset Nos_Brais-GL son los citados.

También lleva bien varios conflictos reales: el doblaje, el caso Caamaño, que el LLM cerrado es incoherente con la tesis pro lingua, y el choque entre anonimato y apoyo institucional. La estrategia de devolver errores y evaluaciones en vez de contenido es concreta.

Aun así, la investigadora de Nós no lo firmaría. El análisis de la voz trata el problema solo como 'uso del modelo Apache'. No ve que el pipeline real usa en producción una grabación humana del dataset protegido (gated) Nos_Brais-GL. Esa grabación está en pipeline.py, en REF_WAV = brais_1_human.wav, y según herramientas/voz/README.md sale del conjunto de test de Nos_Brais-GL. Cada síntesis se condiciona con esa grabación humana como referencia de estilo. Los términos que el promotor aceptó para descargar ese dataset dicen:
- 'solely for research purposes and for developing AI tools focused on linguistic objectives';
- acceso limitado a entidades que colaboran con el CRPIH/USC;
- prohibida la 'public exposure' de las grabaciones.

El correo del §5 hace lo contrario de lo que haría falta. Dice 'sei que o modelo ten licenza Apache 2.0, pero os datos de voz de Brais teñen condicións de uso para investigación', como si fueran de otros, y no cuenta que el promotor ya los descargó y los usa. Para Nós, eso invalida la sinceridad del correo en cuanto lo descubran, y en un pipeline de código abierto lo descubrirán.

Otras carencias:
1. La ficha del modelo StyleTTS2-Brais incluye expresamente 'entertainment' entre sus usos previstos, y la pieza afirma que el entretenimiento no está en la lista (usa Zenodo). Omite el argumento más favorable que tiene y cita mal la postura de Nós.
2. Hay una contradicción interna. El correo promete que, si sigue el silencio, 'usaría outra voz'. El §4 permite, a los 45 días, 'publicar sin monetizar con Brais', y además contradice la regla del Gauntlet 1 (piezas/voz.md §157: solo con confirmación escrita, porque el silencio no es consentimiento).
3. Contra AGPTI y A Mesa, 'no sustituye a nadie porque no existe equivalente humano' es un contrafactual débil que una sociolingüista activista desmontaría (ocupa espacio en el algoritmo y normaliza el galego sintético como galego por defecto). La pieza lo usa como argumento principal.
4. El galego del correo es correcto en general, pero no impecable:
   - mezcla la primera persona del singular ('escríbovos a título persoal') con el plural ('queremos probar', 'marquemos');
   - 'Se nun mes non souben de vós' es forzado; mejor 'Se nun mes non tivese noticias vosas'.
5. No menciona que el locutor está identificado con nombre en la ficha del dataset (lo recoge gtm_riesgos.md). Eso agrava el riesgo reputacional y el de deepfake del art. 50.
