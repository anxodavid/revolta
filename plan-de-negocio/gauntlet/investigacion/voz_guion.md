# Estado del arte: VOZ y GUION en galego con IA (septiembre 2026)

Informe de investigación para el business plan del canal "historia de Galicia para durmir".
Convención: **[F]** = dato con fuente (URL al lado). **[E]** = estimación o supuesto propio, con su razonamiento. **[?]** = no verificado / hay que probarlo.
Fecha de consulta de todas las fuentes: 29-09-2026.

---

## 0. Resumen ejecutivo (lo que importa para decidir)

1. **Existen hoy al menos 6 vías de voz en galego**, y ninguna está validada para narración larga de "sleep content". El juez tiene que ser el oído nativo (kit A/B ciego), no las fichas técnicas.
   - **Proxecto Nós (abierto, gratis)**: la novedad relevante son **Nos_StyleTTS2-Brais-GL y Nos_StyleTTS2-Celtia-GL** (publicados en junio/julio de 2026, Apache-2.0), con voces de actores de doblaje profesionales y mejor prosodia que los VITS anteriores (DNSMOS predicho de 3,40-3,44 frente a 3,24-3,28). Son muy recientes (0 descargas registradas) → riesgo técnico de puesta en marcha, pero es **el candidato más "galego de verdad"** (G2P nativo con Cotovía).
   - **Azure (Microsoft) gl-ES-SabelaNeural y gl-ES-RoiNeural**: voces "Standard" neuronales, sin estilos, 15 USD/1M caracteres con 500k caracteres gratis al mes. Es lo que el promotor ya probó en Clipchamp. Estable y barato, pero plano.
   - **ElevenLabs Eleven v3 / v4**: **sí listan el galego (glg)** oficialmente. Son los más expresivos y los que tienen control de estilo (etiquetas de audio), pero su calidad en galego no está evaluada públicamente [?] y el riesgo típico es el acento castellano o portugués. Precio: unos 7 USD por episodio de 2 h a tarifa API.
   - **Google Gemini-TTS**: galego (gl-ES) en **Preview**, con estilo controlable por prompt. Es muy barato (unos 1,8 USD por 2 h con Flash). Por lo demás, Google solo tiene una voz Standard (gl-ES-Standard-B).
   - **OpenAI gpt-4o-mini-tts**: "sigue" la lista de idiomas de Whisper, que incluye el galego, pero con voces "optimizadas para inglés". Probablemente tenga acento [?].
   - **Clonación con licencia de un locutor galego**: es técnicamente viable (ElevenLabs PVC con v3/v4, o un fine-tune de StyleTTS2 sobre los scripts de Nós). Pero hay que contar con que el sector de la voz en Galicia es hoy **hostil a la IA** (ADA, AGPTI, UVA/PASAVE), así que licenciar una voz es posible pero caro y sensible en reputación. Encaja en la Etapa 3, no antes.
2. **Guion**: no hay ningún benchmark público que compare Claude, GPT y Gemini **generando** galego literario. Los benchmarks académicos (IberoBench) dicen que el galego rinde por debajo del castellano y el portugués. Los modelos de Nós (Carballo/Carvalho, 1,3B-8B) y ALIA-40b están por detrás de los frontier en calidad de redacción larga [E]. **Recomendación**: redactar con un LLM frontier (Claude Opus/Sonnet u otro; hay que elegirlo en una prueba ciega) y aplicar un **cinturón de control lingüístico** (Hunspell-gl, LanguageTool-gl, el LoRA CarvalhoChat_GEC de Nós, una lista de castelanismos, verificación contra el Dicionario RAG/VOLGa y la revisión humana nativa).
3. **Fuentes para RAG**: Galipedia (CC BY-SA 4.0, unos 235k artículos), obras de historiadores en dominio público (Murguía, López Ferreiro, Vicetto…, digitalizadas en Galiciana), revistas académicas en acceso abierto y el CCG (Álbum de Galicia) **solo como referencia factual**: su aviso legal prohíbe reutilizar contenidos con fines comerciales sin autorización.
4. **Costes variables por episodio de 2 h**: voz de 0 € (Nós) a unos 7 USD (ElevenLabs), guion LLM de unos 2-5 USD [E]. **El coste dominante no es la IA, sino las horas humanas de revisión lingüística e histórica.**
5. **Riesgo legal a aclarar antes de monetizar con Nós**: los *modelos* son Apache-2.0, pero los *datasets* de voz (Brais, Celtia) tienen T&C de "solo investigación" y prohíben la "exposición pública de las grabaciones". El audio sintético no son las grabaciones, pero conviene **pedir confirmación escrita a Proxecto Nós** para el uso comercial en YouTube y citar la autoría.

---

## 1. VOZ

### 1.1 Proxecto Nós (USC/ILG/CiTIUS, Xunta; hoy dentro de ILENIA/ALIA)

Contexto: iniciativa de la Xunta de 2021, desarrollada por el ILG y el CiTIUS (USC), integrada en ILENIA (2023) y ahora en ALIA. En TTS, según su informe de 2026, "incrementaron en catro o número de voces dispoñibles en código aberto" [F] https://zenodo.org/records/20523403 (29-05-2026, CC BY 4.0).

Inventario de modelos TTS en Hugging Face (autor `proxectonos`), obtenido con la API de HF [F] https://huggingface.co/api/models?author=proxectonos :

| Modelo | Arquitectura | Voz / corpus | Licencia modelo | Acceso | Notas |
|---|---|---|---|---|---|
| `Nos_StyleTTS2-Brais-GL` | StyleTTS2 + PL-ModernBERT-gl + Cotovía | Brais, masculino, **actor de doblaje profesional**, unas 18 h, 16.121 frases | Apache-2.0 | abierto | creado el 30-06-2026, actualizado el 22-07-2026; desarrollado por **Gradiant** |
| `Nos_StyleTTS2-Celtia-GL` | ídem | Celtia, femenino, actriz de doblaje profesional, unas 20.000 frases | Apache-2.0 | abierto | ídem |
| `Nos_TTS-celtia-vits-graphemes` / `-phonemes` | VITS (Coqui) | Celtia | Apache-2.0 | *gated* auto (aceptar T&C) | existe versión ONNX de la comunidad que no necesita Cotovía |
| `Nos_TTS-brais-vits-phonemes` / `-graphemes` | VITS | Brais | Apache-2.0 | abierto | |
| `Nos_TTS-brais-matcha-graphemes`, `Nos_TTS-celtia-matcha-graphemes` | Matcha-TTS | | | | |
| `Nos_TTS-sabela-vits-phonemes` | VITS | **Sabela (Nós)**: locutora de radio profesional, 14 h 28 min | Apache-2.0 | *gated* auto | **Ojo: no es la Sabela de Microsoft** |
| `Nos_TTS-icia-(extended-)vits/matcha-phonemes` | VITS / Matcha | Icía, amateur, 4 h 5 min (+ aumentado) | Apache-2.0 | abierto | |
| `Nos_TTS-iago-vits-phonemes` | VITS | Iago, amateur, 1 h 13 min | (sin campo) | abierto | |
| `Nos_TTS-paulo-vits-phonemes` | VITS | Paulo, amateur, 1 h 15 min | (sin campo) | abierto | |

Fuentes: fichas de modelo, p. ej. https://huggingface.co/proxectonos/Nos_StyleTTS2-Brais-GL , https://huggingface.co/proxectonos/Nos_TTS-paulo-vits-phonemes , https://huggingface.co/proxectonos/Nos_TTS-icia-extended-matcha-phonemes ; corpus CRPIH_UVigo-GL-Voices (Sabela, Icía, Iago, Paulo), CC BY 4.0 abierto: https://zenodo.org/records/8027725 ; corpus Brais: https://zenodo.org/records/14265241 y LREC 2026: https://aclanthology.org/2026.lrec-1.771/ ; demo web con 6 voces: https://tts.nos.gal/ [F].

**Calidad medida** (ficha de StyleTTS2-Brais; DNSMOS OVRL *predicho* con `speechmos`, **no es un MOS humano**) [F]:

| Longitud | VITS | StyleTTS2 | CMOS |
|---|---|---|---|
| Corta (~10 s) | 3,275 | 3,426 | +0,151 |
| Media (~30 s) | 3,257 | 3,442 | +0,185 |
| Larga (>60 s) | 3,241 | 3,397 | +0,156 |
| Grabación original (referencia) | 3,308 | | |

Lectura [E]: el StyleTTS2 supera a su propio VITS y "suena" tan limpio como el corpus original. Aun así, DNSMOS mide calidad de señal y no naturalidad prosódica ni corrección fonética galega. Para la voz de dormir importa sobre todo la **prosodia en frases largas y la ausencia de artefactos a lo largo de 1-3 h**, y eso solo lo mide el test ciego.

**Cómo se ejecutan** [F, fichas]:
- *StyleTTS2*: `git clone` del repositorio de HF y después `python inference.py --config Configs/inference_config.yml --text "..." --device 0` (o `--file`). Parámetros recomendados para Brais: `alpha 0.6, beta 1.0, t 0.6, diffusion_steps 10, embedding_scale 1.0`. Requiere Cotovía (G2P) y PyTorch. `--device cpu` es posible, pero lento [E].
- *VITS*: Coqui `pip install TTS` más Cotovía (`cotovia_0.5_amd64.deb` y `cotovia-lang-gl_0.5_all.deb` desde SourceForge) para la transcripción fonética. Los modelos de grafemas no necesitan Cotovía.
- *Matcha*: `pip install matcha-tts` más Cotovía.
- *Atajo sin Cotovía*: el cuaderno Colab "Pronunza", con la versión ONNX de Celtia-VITS (131 MB), corre en CPU [F] https://github.com/gas/pronunza-tts-galego-onnx-colab . También hay un plugin para OpenVoiceOS [F] https://github.com/OpenVoiceOS/ovos-tts-plugin-nos .
- Hardware [E]: VITS/Matcha van sobrados en CPU. StyleTTS2 con 10 pasos de difusión es razonable en una GPU modesta (Colab T4) y lento en CPU. Para 2 h de audio conviene trocear por frases o párrafos y concatenar. El parámetro `--t` (interpolación con el estilo anterior) ayuda a la continuidad entre fragmentos.

**Licencia y uso comercial (clave)**:
- Modelos: Apache-2.0, que permite el uso comercial con atribución. Las T&C *gated* (Celtia/Sabela VITS) dicen: "designed for research and development of applications" pero "made available under the Apache License 2.0, which allows its use, modification, and distribution" y prohíben la desinformación y atribuir la autoría a otros [F] (API de HF, `extra_gated_description`).
- Datasets Brais/Celtia (HF): "may be used solely for research purposes… Dissemination of the voice recordings in an open-access manner or their public exposure is strictly prohibited". En Celtia, la propiedad del habla está cedida a la USC durante 15 años y "a partir do 30/11/2037 estes datos serán eliminados" [F] (API de HF, datasets `proxectonos/Nos_Brais-GL`, `Nos_Celtia-GL`).
- Interpretación [E]: usar el *modelo* no redistribuye las grabaciones, así que la vía Apache es defendible. Pero la voz es reconocible como la de un actor de doblaje real, en un momento en que el sector está en pie de guerra contra la IA (§1.6). **Acción: escribir a Proxecto Nós (USC) pidiendo confirmación del uso en un canal monetizado, e indicar en la descripción "Voz sintética: Proxecto Nós (USC), modelo X, Apache-2.0".** Esto también suma legitimidad ante la comunidad galega.

### 1.2 Microsoft Azure AI Speech (Sabela, Roi)

- Voces gl-ES: `gl-ES-SabelaNeural` (F) y `gl-ES-RoiNeural` (M), tipo **Standard** (no HD ni multilingüe), **sin estilos ni roles** y **sin Custom/Personal Voice para gl-ES** [F] https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts
- Precio (API oficial de precios de Azure, westeurope) [F] https://prices.azure.com/api/retail/prices : "S1 Neural Text To Speech Characters" **15,00 USD/1M caracteres**; "Neural Long Audio" 100 USD/1M; Neural HD 22 USD/1M (no aplica al gl). Capa gratuita F0 de 500k caracteres/mes [F, secundaria] https://texttolab.com/blog/azure-text-to-speech-pricing y página oficial https://azure.microsoft.com/en-us/pricing/details/speech/
- Control de ritmo: SSML `<prosody rate/pitch>` y `<break time>` funcionan con voces neuronales estándar [E, práctica habitual; verificar con gl-ES].
- Valoración [E]: es la base conocida del piloto (Clipchamp usa estas voces). Pronunciación normativa razonable, prosodia de "lectura de noticias", sin registro íntimo. Es una buena **línea base del A/B**, no la voz objetivo.

### 1.3 Google Cloud Text-to-Speech

- Voces clásicas gl-ES: **solo `gl-ES-Standard-B` (F)**. No hay WaveNet, Neural2 ni Chirp 3 HD para el galego [F] https://docs.cloud.google.com/text-to-speech/docs/list-voices-and-types ; Chirp 3 HD no lista el galego [F] https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd
- **Gemini-TTS**: "Galician (Spain) | gl-ES | **Preview**" [F] https://docs.cloud.google.com/text-to-speech/docs/gemini-tts . El estilo se controla con instrucciones en lenguaje natural ("fala baixo, con calma, ritmo lento…").
- Precios [F] https://cloud.google.com/text-to-speech/pricing : Gemini 2.5 Flash TTS 0,50 USD/1M tokens de texto y **10 USD/1M tokens de audio**; Gemini 2.5 Pro TTS y Gemini 3.1 Flash TTS (Preview) 1 USD y 20 USD. "Audio tokens correspond to 25 tokens per second". Standard: 4 USD/1M caracteres (4M gratis/mes).
- Cálculo [E]: 2 h = 7.200 s × 25 = 180k tokens de audio → **1,80 USD (Flash) / 3,60 USD (Pro)** por episodio.
- Riesgo [?]: en Preview, la calidad y la deriva de acento en tiradas largas son desconocidas. Hay que incluirlo en el kit A/B.

### 1.4 ElevenLabs

- **Galician (glg) aparece en la lista de Eleven v3 y de Eleven v4 / v4 Turbo**. **No** aparece en Multilingual v2 (29 idiomas) ni en Flash v2.5 [F] https://elevenlabs.io/docs/overview/models . v4 es el buque insignia actual. Límite de 10.000 caracteres por petición en v4 y de 5.000 en v3.
- Precio API [F] https://elevenlabs.io/pricing/api : v3 **0,08 USD/1k caracteres**; v4 0,08 USD/1k (promoción de 0,022 hasta el 12-10-2026); v4 Turbo 0,04 USD.
- Planes [F] https://elevenlabs.io/pricing : Starter 6 USD/mes (30k créditos, licencia comercial, clonación instantánea); Creator 22 USD/mes (primer mes al 50 %, 11 USD; 121k créditos, **Professional Voice Cloning**); Pro 99 USD/mes (600k créditos, audio PCM de 44,1 kHz por API). Regla aproximada: 1.000 créditos ≈ 1 min de audio [F, secundaria] https://bigvu.tv/blog/elevenlabs-pricing-2026-plans-credits-commercial-rights-api-costs/
- Cálculo [E]: un episodio de 2 h ≈ 80-95k caracteres (§1.8), unos **7 USD a tarifa API**. Con Creator sale aproximadamente 1 episodio al mes. Con Pro, unos 6.
- Control: v3/v4 aceptan etiquetas de audio ([whispers], [calm], pausas…), ajuste de velocidad y *Voice Design* [F, general] https://elevenlabs.io/blog/eleven-v3 . La advertencia de ElevenLabs (vía prensa) es que las voces PVC "todavía no están totalmente optimizadas para v3" [F, secundaria] https://formacionele.com/elevenlabs-v3-el-audio-sintetico-toma-la-clase-de-espanol/
- Riesgo [?]: no hay reseñas públicas de su galego. Los riesgos típicos en idiomas minoritarios son: acento castellano (vocales abiertas/cerradas é/è, ó/ò, gheada no controlada), lectura "a la portuguesa" de ciertas grafías y mala pronunciación de topónimos. **Es imprescindible probarlo con un texto trampa** (§1.9).

### 1.5 OpenAI TTS

- `gpt-4o-mini-tts`: "The TTS model generally follows the Whisper model in terms of language support… **Galician**… despite voices being optimized for English" [F] https://developers.openai.com/api/docs/guides/text-to-speech
- Precio ≈ 0,015 USD/min, es decir, unos 1,8 USD por 2 h [F, secundaria] https://costgoat.com/pricing/openai-tts
- Valoración [E]: es controlable por instrucciones ("calm, slow"), pero lo más probable es que tenga acento extranjero. Candidato de relleno en el A/B.

### 1.6 Clonación con consentimiento y licencia de un locutor galego

**Viabilidad técnica**:
- (a) ElevenLabs PVC (desde el plan Creator) sobre v3/v4 con galego. Harían falta de 30 min a 3 h de audio limpio del locutor [E, práctica PVC].
- (b) Fine-tune de StyleTTS2-GL (Nós/Gradiant) con 1-4 h del locutor leyendo el corpus fonéticamente rico de Nós. Así se reutiliza el G2P Cotovía y el PL-ModernBERT-gl. Hace falta GPU y saber de ML [E].
- (c) Azure Custom/Personal Voice: **no disponible para gl-ES** [F, §1.2].
- No hay clonadores abiertos zero-shot (XTTS, F5…) con galego nativo documentado [F, búsqueda sin resultados; ver arXiv Cross-Lingual F5-TTS https://arxiv.org/pdf/2509.14579 como vía de investigación].

**Coste de licencia** (referencias escasas):
- La coalición United Voice Artists (UVA), que incluye a las asociaciones de Galicia, citó en 2024 tarifas de **1.000-1.500 € por la creación de demos de voz sintética de un locutor, y 5.000-7.500 € cuando hacen falta varias jornadas de grabación** [F] https://escueladedoblajedemadrid.es/blog/alerta-maxima-ante-la-cesion-de-voz-para-aprendizaje-neuronal-de-la-ia-segun-uva/ (23-07-2024). Buenas prácticas contractuales: medios y plataformas definidos, duración limitada, exclusividad opcional y tarifa por uso [F] https://www.milenio.com/negocios/que-debe-contener-un-contrato-para-licenciar-una-voz-a-ia
- Estimación para la Etapa 3 [E]: de 2.000 a 6.000 € iniciales (grabación de 2-4 h en estudio, cesión por 2-3 años, solo YouTube/podcast), más un royalty o *revenue share* del 5-15 % de los ingresos del canal. Esto último es un supuesto de negociación, sin fuente.

**Postura del sector (ético-reputacional)**:
- En febrero de 2026, **ADA (Actores e Actrices da Dobraxe Asociados)**, **AGPTI** y **A Mesa** denunciaron que RTVE usa IA generativa para doblar al galego: "só o traballo profesional garante un resultado de calidade"; la IA funcionaría "máis como freo ca como impulso para a lingua galega"; A Mesa lo califica de "bochornoso" [F] https://www.nosdiario.gal/articulo/social/mesa-agpti-ada-denuncian-incumprimentos-rtve-coa-programacion-galego/20260220110723248001.html
- La **cláusula PASAVE** (2023) prohíbe usar las grabaciones de doblaje para entrenar IA y la han aceptado RTVE, TV3, ETB, Movistar+… Hay casos de clonación no consentida (Ángel Morón, Juan Antonio Bernal) [F, síntesis de prensa] https://actualtv.es/registrar-voz-actores-ia-proteccion-legal-espana/ , https://www.elconfidencialdigital.com/articulo/cine/actores-doblaje-empiezan-exigir-contrato-que-ia-utilice-voces/20240226000000729591.html
- Implicaciones [E]:
  1. Un canal "100 % IA en galego" puede recibir críticas del ecosistema cultural (A Mesa, dobladores, prensa como Nós Diario). Conviene **transparencia** (etiqueta de contenido sintético y créditos a Proxecto Nós).
  2. Licenciar la voz de un profesional con contrato justo y *revenue share* puede **convertir el riesgo en relato** ("voz dun actor galego, con licenza e remunerado"), pero será difícil encontrar a alguien dispuesto y probablemente cueste más que la media de la UVA.
  3. **Nunca** clonar una voz sin consentimiento (ni siquiera la de Brais o Celtia fuera de los modelos publicados).

### 1.7 Control de ritmo y tono para la "voz de dormir"

| Motor | Palancas disponibles |
|---|---|
| Nós StyleTTS2 | `alpha/beta` (peso del estilo de referencia frente al generado), `t` (continuidad), `embedding_scale`, `diffusion_steps`. La velocidad no se expone en el CLI: se escalan las duraciones predichas en el código (modificación pequeña) [E]. Se pueden condicionar con un audio de referencia "tranquilo" si el script lo admite [?]. |
| Nós VITS (Coqui) | `length_scale` (>1 = más lento), `noise_scale` [E, conocimiento de Coqui] |
| Nós Matcha | `speaking_rate`, `temperature` en la CLI de matcha-tts [E] |
| Azure | SSML `prosody rate="-15%" pitch="-2st"`, `<break time="1200ms"/>` |
| Gemini-TTS | Prompt de estilo en lenguaje natural más marcadores de pausa |
| ElevenLabs v3/v4 | Etiquetas de audio, velocidad (aprox. 0,7-1,2), estabilidad alta para uniformidad |

**Post-producción común** [E, práctica de canales "sleep"]:
- Inserción programática de silencios (0,6-1,2 s entre frases; 2-4 s entre párrafos).
- Ralentización de 5-10 % con *time-stretch* de alta calidad si el motor no la da.
- Ecualización suave: bajar sibilancias (de-esser) y recortar el brillo por encima de 8-10 kHz.
- Compresión ligera y volumen constante (objetivo aproximado de −16 a −18 LUFS integrados; YouTube normaliza hacia −14).
- Fondo de ruido rosa, lluvia o mar a −30 dB, opcional.
- Ritmo objetivo del texto: unas 110-130 palabras/minuto [E; los "sleep stories" suelen estar por debajo de los 150 wpm de la locución normal].

### 1.8 Tabla comparativa y coste por episodio de 2 h

Supuesto de volumen [E]: a 115 wpm, 2 h ≈ 13.800 palabras; en galego unos 6,2 caracteres/palabra con espacio, así que **≈ 85.000 caracteres** (rango de 80-95k).

| Opción | Galego oficial | Calidad esperada [E] | Control de estilo | Coste por 2 h [E con precio F] | Licencia / riesgo |
|---|---|---|---|---|---|
| Nós StyleTTS2 Brais/Celtia | Sí (nativo) | Alta en pronunciación; la prosodia larga está por probar | Medio | 0 € + GPU (Colab gratis o ~10 €/mes) | Apache-2.0; conviene confirmar el uso comercial |
| Nós VITS/Matcha (Sabela-Nós, Icía, Iago, Paulo…) | Sí | Media (voces amateur en Icía/Iago/Paulo) | Bajo | 0 € (CPU) | Ídem |
| Azure Sabela/Roi | Sí (Standard) | Media, plana | SSML básico | ~1,3 USD (gratis dentro de 500k/mes) | Comercial estándar |
| Gemini-TTS gl-ES | Preview | Desconocida | Alto (prompt) | ~1,8 USD (Flash) / 3,6 USD (Pro) | Preview |
| ElevenLabs v3/v4 | Sí (lista) | Desconocida en gl; muy alta en expresividad | Alto | ~7 USD API (o suscripción de 22-99 USD/mes) | Comercial desde Starter |
| OpenAI gpt-4o-mini-tts | "Sigue a Whisper" | Probable acento | Medio (prompt) | ~1,8 USD | Comercial |
| Locutor galego licenciado (PVC/fine-tune) | Sí | La mejor posible | Alto | 2.000-6.000 € iniciales + royalties | Contrato; sensibilidad sectorial |

### 1.9 Diseño recomendado del kit A/B de voz (para el promotor y su mujer)

[E] Un mismo texto de unos 90 s con "trampas":
- Topónimos: Ourense, Xinzo de Limia, Betanzos, Ribadavia, Mondoñedo, Compostela, Baiona.
- Nombres históricos: Xelmírez, Pardo de Cela, Irmandiños, Suevos, Hermerico, Prisciliano.
- Vocales abiertas y cerradas: *óso* frente a *ósos*, *pé*, *festa*, *home*, *fóra*.
- Números y fechas: "no ano 1467", "século XV".
- Formas propias: *vós*, *quixera*, infinitivo conxugado *para facérmolo*, contracciones *co, coa, polo, na*.
- Una frase larga subordinada (prosodia).

Protocolo: cada motor con sus mejores ajustes de "voz calma", normalizados a igual LUFS, nombres ocultos y orden aleatorio. Puntuación de 1 a 5 en cuatro criterios (corrección galega, naturalidad, "me dormiría con esto", fatiga a los 10 min), más una escucha continua de 10-15 min de los dos finalistas (los artefactos aparecen en tiradas largas).

---

## 2. GUION

### 2.1 Calidad de los LLM en galego

- **Evidencia académica**: IberoBench (COLING 2025) evalúa 33 LLM en eu/ca/**gl**/es/pt. El rendimiento es en promedio más bajo en galego y euskera, y algunas tareas están cerca del azar [F] https://aclanthology.org/2025.coling-main.699/ . IberBench encuentra lo mismo [F] https://liner.com/review/iberbench-llm-evaluation-on-iberian-languages . Estos benchmarks miden comprensión y tareas NLP, **no la calidad literaria de una narración larga**, y en general no incluyen los modelos frontier actuales.
- **Tendencia general**: los LLM multilingües producen texto con rasgos de *translationese*, más marcados fuera del inglés [F] https://arxiv.org/html/2608.17399 . Para el galego, el riesgo específico es la **interferencia del castellano**: léxico (castelanismos), sintaxis (colocación del pronombre átono), falta de infinitivo conxugado y de futuro de subjuntivo en contextos formales, y "hiperenxebrismos" o lusismos no normativos [E, conocimiento de la problemática].
- **No existe** (que yo haya encontrado) un estudio público que compare Claude, GPT y Gemini generando galego con evaluación humana [F, búsquedas negativas]. → **Hay que hacer una prueba propia ciega.**
- Frontier disponibles y precios (por 1M tokens de entrada/salida):
  - Claude Opus 5.5: 4/20 USD. Claude Sonnet 5.5: 2/10 USD. Claude Haiku 4.5: 1/5 USD. Fuente: documentación interna de la API de Anthropic, caché del 25-09-2026. Precios oficiales en https://www.anthropic.com/pricing
  - OpenAI GPT-5.6 "sol" 5/30, "terra" 2/12 y "luna" 0,2/1,2 USD [F, secundaria; verificar] https://www.morphllm.com/openai-api-pricing , oficial https://developers.openai.com/api/docs/pricing
  - Gemini 3 Pro 2/12 USD; Flash 3.x aprox. 0,75/3,75 USD promocional [F, secundaria; verificar] https://benchlm.ai/google/api-pricing
- **Modelos abiertos con foco en galego**:
  - `proxectonos/Carvalho-Salamandra-Instruct` (7B, base BSC Salamandra-7b-instruct, MIT, "versión preliminar"; énfasis gl/pt) [F] https://huggingface.co/proxectonos/Carvalho-Salamandra-Instruct
  - `Llama-3.1-Carballo-Instr1/Instr3` (8B, continual pretraining con 340M tokens y énfasis en gl, licencia Llama 3.1; ACL Findings 2025) [F] https://huggingface.co/proxectonos/Llama-3.1-Carballo-Instr3
  - `carvalho-nos/CarvalhoChat_v4` (Llama-Carvalho-PT-GL, *gated* manual, actualizado en julio de 2026) [F] https://huggingface.co/carvalho-nos/CarvalhoChat_v4
  - Carballo-bloom/cerebras 1,3B (2023-24, históricos).
  - **BSC ALIA-40b-instruct-2606** (40B, 35 lenguas; post-entrenamiento centrado en es/ca/eu/**gl**/en) [F] https://huggingface.co/BSC-LT/ALIA-40b-instruct-2606
  - Valoración [E]: tienen mejor "sabor" galego que un 8B genérico, pero **se quedan cortos en coherencia narrativa de 15.000 palabras, en control de registro y en conocimiento histórico** frente a los frontier. Su mejor uso es como **auditores o correctores** (ver GEC abajo) o como segunda opinión estilística, no como redactores principales. ALIA-40b es el único con tamaño para competir y merece entrar en la prueba ciega si se puede servir barato (GGUF Q8 disponible) [F] https://huggingface.co/BSC-LT/ALIA-40b-instruct_Q8_0

**Estrategia de redacción recomendada** [E]:
1. Redactar **directamente en galego** (no traducir desde el castellano, porque arrastra el calco), con un *system prompt* que incluya: la guía de estilo (norma RAG 2003 revisada en 2012; registro culto pero cálido; frases largas y cadenciosas, sin cliffhangers; segunda persona suave), una **lista negra de castelanismos** frecuentes (p. ej. *entonces→entón*, *bueno*, *sin embargo→non obstante/porén*, *desde luego*, *hasta→ata*, *lograr→acadar/conseguir*, *apellido→apelido*, *antiguo→antigo*, *siglo→século*…) y ejemplos de párrafo modelo escritos o validados por nativos (*few-shot*).
2. Pipeline por capítulos (unas 1.500-2.500 palabras cada uno) con un RAG de fuentes (§2.3). Después, una pasada de "lingüista galego" con un LLM distinto al redactor. Luego, herramientas deterministas (§2.2). Por último, revisión humana nativa de las marcas que queden.
3. Selección del modelo con una **prueba ciega**: tres modelos escriben el mismo capítulo con el mismo prompt, y el promotor y su mujer (más un filólogo puntual, si se puede) puntúan corrección, naturalidad y "arrullo".

**Coste LLM por episodio de 2 h** [E]: unas 14k palabras × ~1,6 tokens/palabra ≈ 22k tokens de salida por versión; con 3-4 pasadas (borrador, revisión, corrección) ≈ 90k de salida y unos 400k de entrada (RAG más contexto). Claude Opus 5.5: 0,4 × 4 + 0,09 × 20 ≈ **3,4 USD**; Sonnet 5.5 ≈ 1,7 USD; la Batch API reduce un 50 % [F: docs de Anthropic]. En cualquier caso es irrelevante frente a las horas humanas.

### 2.2 Herramientas de corrección y norma

| Herramienta | Qué es | Utilidad en el pipeline | Fuente |
|---|---|---|---|
| **Hunspell-gl** (Proxecto Trasno) | Corrector ortográfico palabra a palabra, mantenido por voluntarios; en repositorios Linux (`hunspell-gl`) | Primer filtro automático barato (pyhunspell) | https://trasno.gal/corrector/ , https://gitlab.com/trasno/hunspell-gl [F] |
| **LanguageTool (gl-ES)** | Corrector gramatical contextual; **sin mantenedor para el galego desde 2019** | Útil pero incompleto; se puede autoalojar (servidor Java) | https://trasno.gal/corrector/ , https://forum.languagetool.org/t/gl-getting-started-writing-rules-for-galician/2349 [F] |
| **Imaxin Galgo 2.0** | Corrector ortográfico y léxico (más de 17.000 palabras y unos 5M de formas verbales), descarga gratuita de la SXPL; **complemento de MS Word para Windows** | No automatizable en Linux; útil para revisión manual final | https://www.edu.xunta.gal/portal/node/4723 , https://www.lingua.gal/recursos/para-traballar-en-galego/_/aprendelo/contido_0113/corrector-galego-galgo [F] |
| **CarvalhoChat_GEC** (Nós) | Adaptador LoRA de corrección gramatical galega (base CarvalhoChat_v4; datos CORTEGAL + sintéticos; CC BY 4.0) | Corrector frase a frase con "cambios mínimos"; es un buen "segundo corrector" automático (la base es *gated*, hay que pedir acceso) | https://huggingface.co/proxectonos/CarvalhoChat_GEC [F] |
| **Dicionario da RAG** | La norma léxica (unos 60.000 artículos); web y apps, más un *widget* "Dicionario na túa web". **No hay API pública ni licencia de reutilización documentada** | Consulta manual o de bajo volumen para dudas; no hacer *scraping* masivo | https://academia.gal/dicionario , https://academia.gal/dicionario/rag [F] |
| **VOLGa** (Vocabulario Ortográfico da RAG) | Formas normativas | Consulta de dudas | https://academia.gal [F general] |
| **Portal das Palabras** (RAG + Fundación Barrié) | Divulgación léxica, dicionario, xogos | Inspiración léxica, "palabras con sabor" para el guion | https://fundacionbarrie.org/portal-das-palabras?newlang=english [F] |
| **Dicionario de pronuncia da lingua galega** (ILG/RAG) | Unas 47.000 palabras con transcripción fonética y audio, más **topónimos, parroquias y apellidos** | **Clave para la voz**: comprobar la pronunciación de topónimos y vocales abiertas/cerradas y alimentar un léxico personalizado del TTS | https://ilg.usc.es/pronuncia/ , https://ilg.usc.gal/gl/proxectos/dicionario-de-pronuncia-da-lingua-galega [F] |
| **CORGA** (Corpus de Referencia do Galego Actual, CRPIH) | Corpus de 1975 a hoy, v4.1, con búsqueda web | Comprobar si una colocación o giro es galego real o calco | https://corpus.cirp.gal/corga/ [F] |
| **Digalego** (Imaxin) | Portal y diccionario-traductor comercial | Secundario | [?] no verificado en esta sesión |

Nota normativa [E]: el canal debe seguir la **norma oficial RAG/ILG** (la de la escuela y los medios públicos). Diccionarios reintegracionistas (p. ej. Estraviz) o lusismos confundirán al redactor LLM. Hay que fijarlo explícitamente en el prompt.

### 2.3 Fuentes fiables para el RAG de historia de Galicia

| Fuente | Tipo | Licencia / uso | Uso recomendado |
|---|---|---|---|
| **Galipedia** (gl.wikipedia.org) | Enciclopedia colaborativa, 235.214 artículos | **CC BY-SA 4.0** [F] API: https://gl.wikipedia.org/w/api.php?action=query&meta=siteinfo&siprop=statistics|rightsinfo | Esqueleto factual y galego de referencia. Si se reutilizan frases, atribución y compartir igual; lo seguro es parafrasear hechos (los hechos no tienen copyright) y **verificar** con fuentes primarias o académicas |
| **Wikidata** | Datos estructurados (fechas, personas, lugares) | CC0 [E, conocido] | Validación automática de fechas y nombres |
| **Consello da Cultura Galega**: *Álbum de Galicia* (biografías), *Álbum da Ciencia*, arquivos, publicaciones | Institucional, de alta fiabilidad | Aviso legal: copia permitida solo donde se indique expresamente; si no, **prohibido modificar o reutilizar con fines comerciales sin autorización escrita**. culturagalega.org es CC 3.0 **no comercial y sin obra derivada** [F] https://consellodacultura.gal/noticia.php?id=2601 , https://culturagalega.gal/noticia.php?id=14728 , https://consellodacultura.gal/album-de-galicia/index.php | **Solo como fuente de verificación**, sin meter su texto en el guion. Posible colaboración o permiso (contactar). *Nota: "Álbum da Memoria" no aparece como producto del CCG; puede ser una confusión con Álbum de Galicia o con proyectos de memoria histórica como "Nomes e Voces"* [?] |
| **Galiciana – Biblioteca Dixital de Galicia** (Xunta) | Digitalización de fondos históricos | Obras en dominio público (autores fallecidos antes de 1987 → vida + 80 años) [E, derecho español] | Fuentes primarias y clásicos: **Manuel Murguía** (†1923, *Historia de Galicia*), **Antonio López Ferreiro** (†1910), **Benito Vicetto** (†1878). Casi todo en castellano: se reescribe en galego como obra propia. **Ojo con su historiografía romántica o celtista, hoy superada**: usarlos para relato y ambiente, no como verdad histórica |
| **Revistas y repositorios académicos en abierto** (Minerva-USC, RUC-UDC, Investigo-UVigo; revistas *Gallaecia*, *Minius*, *Cuadernos de Estudios Gallegos* del CSIC) | Académico revisado | Normalmente CC BY / CC BY-NC [E, verificar artículo a artículo] | Contraste y matiz; un "dossier de fuentes" por episodio |
| **Real Academia Galega** (biografías del Día das Letras Galegas, publicaciones) | Institucional | Derechos reservados salvo indicación [E] | Verificación |
| **Publicaciones de la CIG / Fundación Moncho Reboiras** | Historia del movimiento obrero y nacionalista | Derechos del editor [E] | Útiles para el siglo XX, pero con **sesgo ideológico declarado**; contrastar. Para contenido de dormir conviene evitar temas conflictivos o partidistas [E] |
| **Arquivo do Reino de Galicia, Arquivo Histórico Universitario** | Documentación primaria | Consulta | Anécdotas documentadas: "o documento de 1480 conta que…" |

Regla de oro [E]: **cada afirmación histórica del guion, con su fuente en un anexo interno** (no leído en voz). El auditor QA comprueba fechas y nombres contra Wikidata/Galipedia y marca lo que no tenga fuente. En contenido de dormir los errores pasan desapercibidos al oyente dormido, pero **no a los comentaristas despiertos**, y la comunidad galega castiga los errores.

---

## 3. Costes aproximados (resumen para el plan)

| Concepto | Etapa 1 (piloto) | Etapa 2 | Etapa 3 |
|---|---|---|---|
| Voz | 0 € (Nós en Colab gratis o CPU) o Azure dentro de la capa gratuita [E] | 0-22 USD/mes (Nós con GPU alquilada puntual o ElevenLabs Creator si gana el A/B) [E] | Licencia de locutor: 2.000-6.000 € + royalties [E, ref. UVA 1.000-7.500 €] |
| Guion LLM | Suscripción que ya se tenga, o API a ~2-4 USD/episodio [E] | 10-30 USD/mes [E] | Ídem |
| Corrección automática | 0 € (Hunspell, LanguageTool, CarvalhoChat_GEC en local o Colab) | 0 € | 0 € |
| Revisión lingüística humana | Promotor y mujer (tiempo) | Revisor pagado solo para la guía de estilo y muestreos: **0,015-0,03 €/palabra** según el mercado [F, secundaria] https://correccionencastellano.com/tarifas-correccion-textos/ → un episodio completo de 14k palabras costaría 210-420 €, **inviable en cada episodio**; viable muestrear un 10-20 % (unos 40-80 €) [E] | Revisor recurrente |
| GPU | Colab gratis / Pro (unos 10 €/mes) [E] | Ídem o Runpod/Vast por horas (0,2-0,5 USD/h T4-A4000) [E] | |

---

## 4. Riesgos y preguntas abiertas

1. **Licencia comercial de Nós**: confirmar por escrito con la USC. Las T&C de los datasets y la sensibilidad del sector pesan.
2. **Robustez de StyleTTS2-GL en tiradas largas**: es un lanzamiento muy reciente, sin comunidad todavía. Probar la estabilidad en 30 min continuos.
3. **Galego de ElevenLabs v4 y Gemini-TTS**: sin evidencia pública. Solo el kit A/B lo resuelve.
4. **Galego de los LLM frontier en textos largos**: sin estudio público. Hay que hacer una prueba ciega propia.
5. **Reacción de la comunidad cultural galega** a un canal 100 % IA: mitigar con transparencia, créditos a Nós y, en la Etapa 3, voz humana licenciada y remunerada.
6. **Política de YouTube sobre contenido sintético y repetitivo** (fuera del alcance de este informe; ver el informe de retornos y audiencia): se necesita la declaración de "contenido alterado o sintético" y valor editorial propio.
