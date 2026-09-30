# Pieza VOZ (Gauntlet 3): voz en embudo, del gancho al tono de dormir

Constructor: agente de voz (Claude), 30-09-2026. **Estado: terminado** (Cotovía, referencias, controles, curva
calibrada, muestra de escucha). Aprendizajes: [`../aprendizajes/voz.md`](../aprendizajes/voz.md).

**Resumen.** La voz del vídeo largo baja ahora del gancho al tono de dormir en los cinco nodos de la curva de forma
monótona en todas las medidas pedidas: arousal 0,643 → 0,432, desviación de la F0 4,76 → 2,60 semitonos, velocidad
7,56 → 5,19 sílabas/s (182 → 113 palabras/min con las pausas), con WER frase a frase ≤ 0,054 en todos los puntos.
Cambios: Cotovía de Nós en modo `-p1` por defecto, dos referencias de estilo (viva y calma) interpoladas por frase, y
control de F0, energía, `beta` y `embedding_scale` por frase en `voz_st2.py`, con los valores en `curva.py`.

**Qué es automático y qué hizo Claude.** Las voces las genera Nos_StyleTTS2-Brais-GL (Proxecto Nós/USC) en local;
las medidas son automáticas (Praat vía parselmouth, Whisper galego de Nós, modelo de emoción de audEERING). Las
frases de prueba, los criterios de elección, los valores de la curva y este informe los escribió Claude (agente).
**Nadie ha escuchado la voz**: ni Claude (no puede) ni una persona. Las medidas no sustituyen a una escucha.

## 1. Cotovía: A/B y decisión

**Decisión: la Cotovía compilada de Nós pasa a ser la de por defecto, llamada en modo `-p1`** (`entorno.sh` la pone en
`ST2_PATHBIN` si existe; si no, la 0.5 del `.deb`). Motivo: da los fonemas con los que se entrenó la voz y no es peor en
WER.

| Cotovía | WER frase a frase (33 frases × 2 semillas, 776 palabras) | Caracteres distintos del corpus de entrenamiento (122 frases) | Frases idénticas | Vocales abiertas tónicas (corpus: 135) |
|---|---|---|---|---|
| 0.5 (`.deb` de 2012, la de antes) | 0,032 (25 errores) | 7,81 % | 8 / 122 | 10 |
| Compilada de Nós, modo síntesis | 0,030 (23) | 0,92 % | 84 / 122 | 142 |
| **Compilada de Nós, modo `-p1` (nueva por defecto)** | **0,028 (22)** | **0,80 %** | **87 / 122** | 141 |

- Frases del A/B: las 21 de test del corpus Nos_Brais-GL (no usadas en el entrenamiento) y 12 escritas por Claude con
  vocales abiertas y cerradas (*porta, terra, home, pedra, óso*), monosílabos (*que, de, o, si, non, á*) y nombres
  propios (*Rosalía de Castro, Mondoñedo, Xelmírez, Fisterra, Ourense, Lalín, O Carballiño*): `scripts/textos.py`.
  Voz con `REF_WAV` de siempre, escala 1,1. WER con el Whisper galego de Nós, cada frase por separado
  (`datos/cotovia-ab-frase-a-frase.json`). Coincidencia de fonemas: `herramientas/pipeline/probas/comparar_cotovia.py`.
- **El WER no distingue las Cotovías** (±3 errores de 776, dentro del ruido): el ASR entiende igual *po^rta* que
  *pO^rta*. La diferencia está en lo que el modelo recibe: con la 0.5, 1 de cada 13 caracteres de fonemas no es como en
  el entrenamiento (vocales medias abiertas/cerradas y el acento de los monosílabos átonos: *ké, dé, ó*).
- **Por qué `-p1`.** En su modo de síntesis (el que usa el código de Nós) la Cotovía compilada aplica a propósito tres
  transformaciones (`preproc.cpp`): segunda forma del artículo tras -r/-s (*facer o lume* → *faTélo lúme*, *vas a
  casa* → *bála kása*, *sabes o que* → *sábelo ke*), *para* → *pra* (la fórmula del canal sonaría "Cousas de Galiza
  **pra** durmir") y *ao* → *Ó*. El corpus de entrenamiento (16.121 frases) no tiene ninguna de las dos primeras
  (1.929 casos de palabra en -r/-s + artículo, ninguno contraído; *para* en 1.436 frases, nunca *pra*) y sí la
  tercera. `-p1` quita las tres; el envoltorio de `instalar.sh` repone *ao(s)* → *O(s)* y quita la línea de texto
  preprocesado que añade ese modo. En 58 frases de los guiones del Gauntlet 2 cambian 4 respecto al modo síntesis.
- Una medida que **no** vale: las 33 frases seguidas en un solo audio (1 s de silencio entre ellas) dan WER 0,10-0,12,
  porque Whisper se salta frases enteras (borrados de 6-12 palabras que caen en sitios distintos en cada versión)
  (`datos/cotovia-ab.json`). Por eso todas las medidas de WER de esta pieza son frase a frase.

## 2. Referencias de estilo

**Medida de las 40 grabaciones humanas** de Brais (`REFS_DIR`, corpus Nos_Brais-GL: 21 de test y 19 de train; no se
suben al repo) con `scripts/referencias.py` (`datos/referencias-humanas.json`): velocidad en sílabas/s (contador
ortográfico de sílabas del gallego sobre la duración de la fala), F0 con Praat (mediana en Hz; desviación y rango
p5-p95 en semitonos), dinámica de energía (p95-p10 del RMS por tramos de 25 ms) y arousal (audEERING).

| Medida (40 grabaciones) | mínimo | mediana | máximo |
|---|---|---|---|
| sílabas/s | 5,16 | 7,42 | 8,70 |
| F0 mediana (Hz) | 129,6 | 154,1 | 237,3 |
| F0 desviación (st) | 2,39 | 3,93 | 6,47 |
| F0 rango p5-p95 (st) | 7,96 | 13,32 | 18,89 |
| dinámica (dB) | 18,0 | 21,3 | 26,4 |
| arousal | 0,42 | 0,58 | 0,68 |

**Lo que importa es lo que la referencia hace en la voz sintética**, así que se sintetizó el pasaje de prueba con cada
una de las 40 como referencia, con los parámetros neutros (escala 1,0, alpha 0,3, beta 0,7) (`scripts/barrido_refs.py`,
`datos/barrido-refs.json`, ordenadas con `scripts/analizar_barrido.py`): arousal 0,557-0,644, F0 desviación 3,29-4,87
st, pero velocidad casi fija (7,08-7,46 síl/s). La referencia transmite bien la variación de la F0 (correlación
humano-sintético 0,83), a medias el arousal (0,52) y casi nada la velocidad (0,16): **el ritmo lo tiene que poner
`escala`, no la referencia.**

Preseleccionadas (criterios de Claude: viva = más arousal y más desviación de F0 en la voz sintética, algo de agilidad,
sin F0 ni brillo extremos y sin preguntas; calma = menos arousal, F0 estrecha, más lenta y suave, sin voz cascada) y
medidas con WER frase a frase (`datos/variantes-refs.json`; viva con los parámetros neutros; calma con beta 0,3 y
escala 1,25, como al final de la curva):

| Referencia | Grabación humana | arousal sint. | F0 sd (st) | síl/s | WER |
|---|---|---|---|---|---|
| viva 04078 | "Ti xa sabes o que debes facer." (2,4 s) | 0,620 | 4,03 | 7,39 | 0,067 |
| viva 01372 | "A escaseza de vacinas en Europa…" (5,1 s) | 0,623 | 3,98 | 7,27 | 0,052 |
| viva 00856 | "A sentenza completa publicarase…" (3,7 s) | 0,608 | 4,04 | 7,35 | 0,067 |
| viva 11535 | "A defensa institucional… ¿non?" (3,8 s; arousal humano 0,667, el segundo más alto de las 40) | 0,644 | 4,21 | 7,37 | 0,052 |
| viva 07496 | "As autoestradas da Xunta…" (6,6 s) | 0,617 | 4,03 | 7,18 | 0,060 |
| **viva media 04078 + 01372 + 00856** | vector de estilo medio | 0,619 | 4,04 | 7,34 | **0,045** |
| calma 08964 | "¡Que fonda mudanza…!" leída baja y plana (F0 130 Hz, 2,39 st: la más estrecha de las 40) | 0,510 | 2,66 | 6,60 | 0,067 |
| calma 03720 | "O amansamento dunha fera, do vento, do mar…" (la más lenta, 5,16 síl/s, y la menos activada, 0,423) | 0,528 | 3,40 | 6,07 | 0,052 |
| calma 15278 | "Informounos de que o caso era grave…" | 0,545 | 3,10 | 6,48 | 0,105 |
| calma 08334 | "¿Que queres? -berrou el…" | 0,508 | 3,04 | 6,20 | 0,067 |
| calma media 08964 + 03720 + 15278 | vector medio | 0,523 | 3,06 | 6,41 | 0,075 |

- Con este pasaje hay un suelo de ~0,04 de WER que no es de la voz: "casa sen lareira" y "casas en lareira" suenan
  igual (4 errores por versión), "auga mansa" sale "augamansa" y "avoas" "avóas".
- **15278 queda fuera**: repite sílabas al empezar frase con beta bajo ("co contan", "di di diante", "Eh si").

(Elección final: ver §4.)

## 3. Controles de la voz en `voz_st2.py`

`voz_st2.py` lee de cada frase del JSON (el que escribe `longo.py` desde `curva.py`) estos campos opcionales; sin
ellos la voz es la de antes, así que `pipeline.py` (vídeo corto) sigue igual. También se puede importar
(`cargar()` + `infer()`), como hacen los scripts de esta pieza y los de la pieza SON.

| Campo | Qué hace | Implementación |
|---|---|---|
| `escala` | duraciones (más alto = más lento) | como antes: multiplica la duración predicha de cada fonema |
| `estilo` | 0 = referencia viva (`REF_WAV`) … 1 = calma (`REF_WAV_CALMO`) | interpola el vector de estilo de 256 (128 acústico + 128 prosódico) de las dos; se usa en la difusión del estilo y en la mezcla con `alpha`/`beta`. Sin `REF_WAV_CALMO` no hace nada |
| `f0_media` | altura media | multiplica la F0 de los tramos sonoros (> 40 Hz) |
| `f0_rango` | amplitud de la entonación | log F0 → media + rango × (log F0 − media), con la media de la frase; solo tramos sonoros |
| `enerxia` | energía que recibe el descodificador | N × valor (N es el log de la norma del espectro mel) |
| `alpha`, `beta` | cuánto manda la referencia frente al estilo predicho del texto (0,3 y 0,7 por defecto) | los de StyleTTS2 |
| `embedding_scale`, `pasos` | guía del texto y pasos de la difusión del estilo (1 y 5) | los de StyleTTS2 |

- `REF_WAV` y `REF_WAV_CALMO` admiten varias grabaciones separadas por `:` (vector de estilo medio).
- **Semilla por frase** (SEED + texto): antes el ruido de la difusión dependía de la posición de la frase y de si se
  retomaba la ejecución; ahora una frase suena igual aunque se repita el render, y dos versiones de la misma frase solo
  se diferencian por los parámetros.
- **Suelo de 80 Hz**: `f0_rango` y `f0_media` no bajan ningún tramo por debajo de 80 Hz si no lo estaba ya. Con el
  rango ampliado del gancho (1,2) entre el 1,3 y el 3,1 % de los tramos sonoros de cada frase quedaban por debajo de
  75 Hz (las 40 grabaciones de Brais: 0,14 % de media), que es donde aparece la voz cascada al final de frase.
- Límites de seguridad (fuera de ellos avisa y recorta): escala 0,7-1,6; f0_media 0,85-1,15; f0_rango 0,5-1,5;
  enerxia 0,7-1,3. Escritura atómica de cada WAV y aviso si el pico llega a 0,99.

**Efecto medido de cada control** (pasaje de la Santa Compaña, 7 frases, referencia neutra 07156, escala 1,0;
diferencia con la base; `datos/variantes-efectos.json`):

| Variante | arousal | síl/s | F0 mediana (Hz) | F0 sd (st) | F0 p5-p95 (st) | LUFS | alpha ratio (dB) | HNR (dB) | jitter (%) |
|---|---|---|---|---|---|---|---|---|---|
| base (valor) | 0.612 | 7.27 | 149.8 | 3.93 | 13.0 | -23.1 | -8.15 | 11.19 | 3.10 |
| f0_rango 1.25 | +0.019 | +0.00 | +2.9 | +0.79 | +2.7 | +0.0 | +0.08 | -0.33 | +0.18 |
| f0_rango 0.75 | -0.021 | -0.00 | -2.0 | -0.98 | -3.1 | +0.0 | -0.08 | +0.59 | -0.17 |
| f0_media 1.05 | +0.010 | +0.00 | +7.2 | -0.00 | +0.2 | +0.1 | +0.11 | +0.39 | -0.08 |
| f0_media 0.94 | -0.008 | +0.00 | -8.5 | -0.06 | -0.1 | -0.0 | +0.04 | -0.29 | +0.01 |
| enerxia 0.85 | -0.005 | -0.01 | +0.0 | +0.05 | +0.3 | -1.2 | +0.48 | -0.30 | -0.03 |
| enerxia 1.15 | +0.004 | +0.00 | -0.0 | +0.01 | +0.1 | +1.1 | -0.73 | +0.38 | -0.10 |
| escala 0.9 | +0.009 | +0.37 | -0.4 | -0.05 | -0.2 | -0.1 | +0.03 | -0.17 | +0.02 |
| escala 1.3 | -0.089 | -2.07 | -1.3 | +0.04 | +0.5 | +0.1 | -0.01 | +2.23 | -0.76 |
| beta 0.3 | +0.013 | +0.20 | +7.8 | -0.07 | +0.3 | +0.0 | -0.05 | +0.58 | -0.19 |
| beta 0.9 | -0.017 | -0.11 | -4.6 | +0.08 | +0.2 | -0.1 | +0.05 | -0.08 | +0.01 |
| embedding_scale 2.0 | -0.003 | -0.16 | +2.5 | +0.04 | +0.3 | +0.1 | +0.07 | +0.26 | -0.08 |
| alpha 0.1 | +0.003 | -0.01 | -0.1 | +0.04 | +0.4 | +0.2 | -0.22 | +0.04 | +0.01 |
| pasos 10 | +0.006 | +0.09 | +2.2 | -0.04 | -0.1 | +0.2 | -0.06 | +0.13 | +0.07 |

Lectura:
- **La palanca grande del arousal es el ritmo**: escala 1,3 baja el arousal 0,089 (y sube el HNR 2,2 dB: la voz lenta
  sale más limpia). Después, el rango de la F0 (±0,02 por ±0,25). La referencia y `beta` mueven sobre todo la altura
  (±5-8 Hz) y poco el arousal (±0,01-0,02).
- **`enerxia` no suaviza**: baja el volumen (−1,2 dB con 0,85) y la voz sale algo *más brillante* (alpha ratio +0,5 dB)
  y con menos HNR: lo contrario de una voz suave. El nivel se lleva mejor con `ganancia_db` en la mezcla; en la curva
  `enerxia` se queda cerca de 1.
- `embedding_scale`, `alpha` y `pasos`: efectos pequeños en arousal (≤ 0,006). `embedding_scale` 1,4-1,6 en el gancho
  da algo más de rango de F0 (+0,6 st en la ronda 1).

## 4. Curva calibrada y medidas por punto

**Método.** Pasaje fijo de 7 frases (111 palabras) del tema elegido, "As meigas de verdade" (el conxuro de 1967, la
parteira de Vilalba según una testigo, la meiga como curandeira, la noche de San Xoán, "Chove na lousa"; escritas por
Claude a partir de `tema/investigacion.md`, `scripts/textos.py`). Se renderiza igual en los 5 nodos de la curva
(`curva.en(pal, 3600)` con pal = 0, 280, 950, 1800 y 3600: gancho, fin del gancho, fin de la transición, mitad y final
de un guion de 3.600 palabras), con las pausas y la ganancia que pone `longo.py` (`scripts/puntos.py`). Por punto:
palabras/min con pausas (como el QA de `longo.py`), sílabas/s de la fala, F0 (media, desviación y rango p5-p95 en
semitonos), energía (LUFS del pasaje con la ganancia, dinámica), arousal/valencia (audEERING, solo evaluación
interna), WER frase a frase (Whisper galego de Nós) y controles de voz cascada y saturación (HNR, jitter, % de F0
< 75 Hz, pico). Seis candidatas en dos rondas (`datos/candidatas/`, `datos/curva-ronda1.json` y `curva-ronda2.json`,
tabla con `scripts/analizar_curva.py`).

**Rondas.** En la 1.ª (sin WER) las cuatro candidatas bajaban de forma monótona; la de `curva.py` tal como estaba
(valores provisionales del orquestador) solo estrechaba la F0 3,6 st y las demás 6,7-7,3 st. La 2.ª (con WER) comparó
dos parejas de referencias con los mismos valores: **E** (viva = media de 04078, 01372 y 00856; calma = media de 08964
y 03720) y **F** (viva = media de 11535, 01372 y 04078; calma = 03720). Las dos cumplen; se elige **F**: más arousal en
el gancho (0,643 frente a 0,631), menos al final (0,432 frente a 0,436), final más lento (113 frente a 118 pal/min) y
más limpio (HNR 13,9 frente a 12,8 dB). E tiene el final más suave de timbre (alpha ratio −9,2 frente a −8,1 dB). Las
frases de F no tienen finales ascendentes (pendiente de F0 en los últimos 400 ms: todas negativas, de −15/−35 st/s en
el gancho a −4/−11 st/s al final), así que la pregunta de 11535 no pasa su entonación a las afirmativas.

**Valores finales (`herramientas/pipeline/curva.py`)**. Nuevos: `beta` y `embedding_scale` (añadidos a `curva.VOZ`,
así que `longo.py` los pasa a la voz). **Aviso: cambia también `escala`** (antes 1,00-1,05-1,14-1,22-1,28; el gancho
algo más ágil y el final algo más lento). Pausas y `ganancia_db`, sin cambios.

| Punto (palabra, fase) | escala | estilo | f0_rango | f0_media | enerxia | beta | emb. | pausa (s) | ganancia (dB) |
|---|---|---|---|---|---|---|---|---|---|
| 0 (gancho) | 0.97 | 0.0 | 1.2 | 1.02 | 1.0 | 0.8 | 1.4 | 0.45 | +0.8 |
| 280 (fin del gancho) | 1.03 | 0.2 | 1.1 | 1.005 | 1.0 | 0.75 | 1.2 | 0.55 | +0.5 |
| 950 (fin de la transición) | 1.14 | 0.6 | 0.95 | 0.985 | 0.98 | 0.6 | 1.0 | 0.85 | +0.0 |
| 1800 (mitad) | 1.24 | 0.9 | 0.82 | 0.965 | 0.96 | 0.45 | 1.0 | 1.15 | -0.8 |
| 3600 (final) | 1.3 | 1.0 | 0.76 | 0.955 | 0.95 | 0.4 | 1.0 | 1.4 | -1.5 |

Referencias (`entorno.sh`): `REF_WAV` = `brais-norm-11535.wav:brais-norm-01372.wav:brais-norm-04078.wav` (vector
medio), `REF_WAV_CALMO` = `brais-norm-03720.wav` ("O amansamento dunha fera, do vento, do mar…", la grabación más
lenta y menos activada de las 40). Viven en `REFS_DIR`, que `instalar.sh brais` vuelve a bajar.

**Medidas por punto (curva final, candidata F; automáticas):**

| Punto | pal/min (con pausas) | síl/s | F0 media (Hz) | F0 sd (st) | F0 p5-p95 (st) | LUFS pasaje | arousal | WER frase a frase | HNR (dB) | jitter (%) | F0 < 75 Hz |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 182 | 7.56 | 155 | 4.76 | 16.0 | -22.7 | **0.643** | 0.000 (0) | 11.1 | 3.16 | 0.6 % |
| 280 | 174 | 7.37 | 151 | 4.44 | 15.2 | -23.1 | **0.611** | 0.054 (6) | 11.3 | 2.94 | 0.6 % |
| 950 | 154 | 6.95 | 146 | 3.66 | 12.4 | -24.2 | **0.568** | 0.000 (0) | 11.9 | 2.81 | 0.0 % |
| 1800 | 138 | 6.51 | 140 | 2.88 | 9.6 | -25.5 | **0.525** | 0.027 (3) | 12.5 | 2.75 | 0.0 % |
| 3600 | 113 | 5.19 | 135 | 2.60 | 8.3 | -26.6 | **0.432** | 0.000 (0) | 13.9 | 2.36 | 0.0 % |

- **Monótonas en cada paso**: arousal, F0 sd, F0 rango, síl/s y pal/min (también la F0 media, el nivel y el jitter).
  Para situarlo: el arousal del gancho está en el cuartil alto de las 40 grabaciones de Brais (mediana 0,58) y el del
  final en el de sus grabaciones más calmas (0,42-0,44).
- **WER ≤ 0,054 en todos los puntos.** De los 9 errores, 7 son del ASR y no de la voz: Whisper escribe "mil
  seiscentos dezasete" como "16 17" (cuenta como 3-4 errores). El único error de pronunciación visible es "Non o é"
  → "No Noé" en el punto 280.
- Sin saturación (pico máximo 0,65, 0 muestras ≥ 0,99) ni duraciones raras (frases de 3,5-9,5 s, crecen con la
  escala). La voz del final sale más limpia que la del gancho (HNR +2,8 dB, jitter −0,8).
- La **valencia** también baja (0,45 → 0,39): el modelo lee la voz lenta y grave como algo más "apagada". No era un
  objetivo; conviene que el promotor diga si el final suena triste en vez de sereno.

## 5. Muestra de escucha

(pendiente)

## 6. Límites y qué no se pudo medir

(pendiente)
