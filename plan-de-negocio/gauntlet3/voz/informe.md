# Pieza VOZ (Gauntlet 3): voz en embudo, del gancho al tono de dormir

Constructor: agente de voz (Claude), 30-09-2026. **Estado: en curso** (Cotovía hecho; referencias, controles y curva
pendientes).

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

(pendiente)

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

(pendiente)

## 5. Muestra de escucha

(pendiente)

## 6. Límites y qué no se pudo medir

(pendiente)
