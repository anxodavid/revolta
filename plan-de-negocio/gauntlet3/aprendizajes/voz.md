# Aprendizajes: voz en embudo (Gauntlet 3, pieza 4)

Agente de voz (Claude), 30-09-2026. Todo lo que sigue son medidas automáticas (Praat vía parselmouth, Whisper galego
de Nós, modelo de emoción de audEERING) y decisiones de Claude a partir de ellas. **Nadie ha escuchado la voz.**
Informe completo: [`../voz/informe.md`](../voz/informe.md).

## Resultado en una línea

Curva final (candidata F de 6 probadas): en los 5 nodos, arousal 0,643 → 0,432, F0 sd 4,76 → 2,60 st y 7,56 → 5,19
síl/s (182 → 113 pal/min con pausas), bajando en cada paso, con WER frase a frase ≤ 0,054. Viva = media de 3
grabaciones de Brais (11535, 01372, 04078); calma = 03720. Muestra: `../voz/mostra-embude.m4a`.

## Cotovía (fonemas de la voz)

- **La Cotovía compilada de Nós tiene dos modos y el bueno para esta voz no es el de por defecto.** En modo síntesis
  (el que usa el phonemizer de Nos_StyleTTS2, `cotovia -n -S -A0`) aplica tres transformaciones deliberadas
  (`preproc.cpp`, `transformAloformoArtigo` y `transformPrepositions`): segunda forma del artículo tras -r/-s
  ("facer o lume" → *faTélo lúme*, "ver os castros" → *Bélos*, "vas a casa" → *bála kása*, "sabes o que" → *sábelo
  ke*), "para" → *pra* (también "Cousas de Galiza **pra** durmir", la fórmula del canal) y "ao" → *Ó*. Las
  transcripciones del corpus con que se entrenó Brais (16.121 frases) **no** tienen las dos primeras (1.929 casos de
  palabra en -r/-s + artículo, ninguno contraído; "para" en 1.436 frases, nunca *pra*) y **sí** la tercera (*O*).
- Con `-p1` (modo "reconocimiento") desaparecen las tres; el envoltorio de `instalar.sh cotovia_nova` añade `-p1`,
  quita la línea de texto preprocesado que escribe ese modo (sin tabulador: el phonemizer la tomaría por una palabra)
  y devuelve "ao(s)" → *O(s)* con awk. Coincidencia con el corpus (122 frases, `probas/comparar_cotovia.py`): 0.5 del
  `.deb` 7,81 % de caracteres distintos (8 frases idénticas); compilada en modo síntesis 0,92 % (84); **modo -p1
  0,80 % (87)**. En 58 frases de los guiones del Gauntlet 2 cambian 4 (las dos fórmulas "para durmir" y un
  "lembraremos o que" → *lembrarémolo ke*).
- WER (Whisper galego) frase a frase, 33 frases × 2 semillas: 0.5 = 0,032 (25/776), compilada = 0,030 (23/776). Es un
  empate: el ASR no distingue *pO^rta* de *po^rta*. El motivo para cambiar es la coincidencia con el entrenamiento,
  no el WER.

## Referencias de estilo

- **La referencia pesa poco con los parámetros de siempre** (alpha 0,3, beta 0,7). Con cada una de las 40 grabaciones
  de Brais como referencia, el mismo pasaje sale con arousal 0,557-0,644 y 7,08-7,46 síl/s, aunque las grabaciones
  van de 0,42 a 0,68 y de 5,2 a 8,7 síl/s. Lo que sí pasa es la variación de la F0 (correlación humano-sintético 0,83);
  el arousal a medias (0,52) y la velocidad casi nada (0,16).
- Las grabaciones "calmas" (la más lenta, la de F0 más estrecha) bajan el arousal sintético ~0,05-0,11 frente a las
  "vivas" solo si además se baja `beta` (0,3-0,4) y se ralentiza (`escala`).
- Una referencia puede meter artefactos con beta bajo: con 15278 ("Informounos de que o caso era grave…"), beta 0,3 y
  escala 1,25 la voz repite sílabas al empezar frase ("di di diante", "co contan"): WER 0,105. Probar el WER de cada
  referencia en su punto de la curva, no solo con los parámetros neutros.
- Los vectores medios de varias grabaciones funcionan y son más estables: la media de 3 vivas dio el mejor WER de las
  vivas (0,045).

## Qué mueve el arousal (modelo de audEERING, 7 frases)

- **El ritmo es la palanca grande**: escala 1,3 → arousal −0,089 (y HNR +2,2 dB, jitter −0,8: la voz lenta sale más
  limpia). El rango de F0: ±0,02 por ±0,25. `f0_media`, `beta`: ±0,01. `enerxia`, `embedding_scale`, `alpha`, `pasos`:
  casi nada. El modelo normaliza el volumen, así que la ganancia no cuenta.
- Con todo junto (curva de la ronda 1) el arousal baja de 0,63 a 0,44 de forma monótona en los 5 puntos, igual que la
  desviación de la F0 (4,5 → 2,5 st), la velocidad (7,6 → 5,4 síl/s) y las palabras/min con pausas (183 → 119).
- Ampliar el rango de la F0 (1,2) mete tramos por debajo de 75 Hz en los finales de frase (1-3 % frente al 0,14 % de
  las grabaciones humanas): riesgo de voz cascada. Solución en `voz_st2.py`: la manipulación no baja ningún tramo de
  80 Hz si no lo estaba ya.

## Qué funcionó y qué no (curva)

- **Funcionó**: juntar varias palancas pequeñas en el mismo sentido (ritmo + rango de F0 + referencia calma con
  `beta` bajo + algo de altura). Ninguna sola basta: la referencia sola mueve el arousal ±0,03 con beta 0,7.
- **Funcionó**: medir con el mismo texto y la misma semilla en todos los puntos; así cualquier diferencia es de los
  parámetros y las curvas salen monótonas sin ruido (6 candidatas, todas monótonas).
- **Funcionó**: un suelo de 80 Hz en la manipulación de la F0; con él, el gancho con rango 1,2 baja del 1,8 % al
  0,6 % de tramos por debajo de 75 Hz.
- **No aportó**: `enerxia` (volumen, no suavidad), `alpha`, `pasos` de difusión. `embedding_scale` 1,4 en el gancho
  da un poco más de rango de F0 y de arousal (+0,006): se deja, pero es marginal.
- **La valencia baja con la calma** (0,45 → 0,39): el modelo oye la voz lenta y grave algo "apagada". Hay que
  preguntar al oído del promotor si el final suena sereno o triste.
- **La referencia más activada no mete entonación de pregunta**: 11535 termina en "¿non?", pero en la media con dos
  afirmativas todas las frases acaban bajando (pendiente de F0 negativa en los últimos 400 ms).
- **Cambiar de pasaje cambia el suelo de WER**: con el de la Santa Compaña había ~0,04 de homófonos; con el de las
  meigas, 0-0,054 y casi todo son cifras que Whisper escribe en números ("16 17").

## Medir con Whisper

- **Whisper se salta frases enteras en audio largo con silencios** (33 frases seguidas con 1 s entre ellas, sin VAD y
  sin condicionar al texto anterior, como el QA): WER 0,10-0,12 frente a 0,03 frase a frase, con borrados de 6-12
  palabras seguidas que caen en sitios distintos en cada versión. Para comparar voces, WER **frase a frase**. Ojo con
  el QA de `longo.py`, que mide sobre la mezcla entera: puede dar WER altos que no son de la voz.
- Una frase corta cuesta lo mismo que 30 s (la ventana fija de Whisper): ~6,5 s de CPU por frase en este contenedor.
- El WER tiene un suelo que no es de la voz: homófonos en habla continua ("casa sen lareira" / "casas en lareira",
  "quen a atopa" / "quen atopa", "auga mansa" / "augamansa"). Con un pasaje de 120 palabras son ~0,04 de WER fijo;
  conviene revisar las hipótesis antes de culpar a la voz.

## Controles de la voz (StyleTTS2)

- **N (energía) mueve sobre todo el volumen**: N × 0,8 → −1,8 dB; N − 2 → −1,9 dB; y el timbre va al revés de lo
  natural (alpha ratio de −9,7 a −9,2 dB: más brillante al bajar N) con algo menos de HNR (11,8 → 11,1 dB). No
  suaviza la voz: para el nivel es mejor `ganancia_db` (limpio, en la mezcla).
- La F0 predicha va en Hz, con los tramos sordos cerca de 0 (mínimo −1 Hz); el generador toma como sonoro todo lo que
  sea > 0 (`voiced_threshold = 0`). Al escalar la F0 hay que tocar solo los tramos sonoros (> 40 Hz).
- El muestreador de difusión (ADPM2) usa ruido en cada paso: sin semilla por frase, una misma frase suena distinta
  según su posición o si se retoma la ejecución. `voz_st2.py` ahora siembra por frase (SEED + texto).

## Entorno

- CPU compartida con los agentes visual, de sonido y de guion: los trabajos esperan el candado 10-40 min por turno (y
  `flock` no respeta el orden de llegada). **Juntar en un solo lote bajo un solo candado** todo lo que se pueda (varias
  candidatas por ejecución, la muestra en el mismo lote): el reloj se va esperando, no calculando (una candidata en 5
  puntos: ~1 min de voz + ~4 min de WER frase a frase).
- La sesión se cortó por el límite de uso a media tarea (16:30); el lote que corría terminó y el coordinador subió
  los datos. Subir cada resultado en cuanto sale.
- `voz_st2.py` cambia de directorio (`os.chdir(ST2_DIR)`) al cargar el modelo: las rutas de salida relativas de los
  scripts que lo importan se rompen (se perdió una vez el JSON del A/B). Usar siempre rutas absolutas.
- Disco: quedaban 4,2 GB libres a media tarde (la caché de HF creció a 21 GB con los modelos del agente visual).
