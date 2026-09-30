# Aprendizajes: voz en embudo (Gauntlet 3, pieza 4)

Agente de voz (Claude), 30-09-2026. Todo lo que sigue son medidas automáticas (Praat vía parselmouth, Whisper galego
de Nós, modelo de emoción de audEERING) y decisiones de Claude a partir de ellas. **Nadie ha escuchado la voz.**
Informe completo: [`../voz/informe.md`](../voz/informe.md).

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

## Medir con Whisper

- **Whisper se salta frases enteras en audio largo con silencios** (33 frases seguidas con 1 s entre ellas, sin VAD y
  sin condicionar al texto anterior, como el QA): WER 0,10-0,12 frente a 0,03 frase a frase, con borrados de 6-12
  palabras seguidas que caen en sitios distintos en cada versión. Para comparar voces, WER **frase a frase**. Ojo con
  el QA de `longo.py`, que mide sobre la mezcla entera: puede dar WER altos que no son de la voz.
- Una frase corta cuesta lo mismo que 30 s (la ventana fija de Whisper): ~6,5 s de CPU por frase en este contenedor.

## Controles de la voz (StyleTTS2)

- **N (energía) mueve sobre todo el volumen**: N × 0,8 → −1,8 dB; N − 2 → −1,9 dB; y el timbre va al revés de lo
  natural (alpha ratio de −9,7 a −9,2 dB: más brillante al bajar N) con algo menos de HNR (11,8 → 11,1 dB). No
  suaviza la voz: para el nivel es mejor `ganancia_db` (limpio, en la mezcla).
- La F0 predicha va en Hz, con los tramos sordos cerca de 0 (mínimo −1 Hz); el generador toma como sonoro todo lo que
  sea > 0 (`voiced_threshold = 0`). Al escalar la F0 hay que tocar solo los tramos sonoros (> 40 Hz).
- El muestreador de difusión (ADPM2) usa ruido en cada paso: sin semilla por frase, una misma frase suena distinta
  según su posición o si se retoma la ejecución. `voz_st2.py` ahora siembra por frase (SEED + texto).

## Entorno

- CPU compartida con el agente visual: los trabajos esperan el candado decenas de minutos. Conviene juntar en un solo
  proceso (una sola carga de modelos) todo lo que se pueda medir de una vez.
- `voz_st2.py` cambia de directorio (`os.chdir(ST2_DIR)`) al cargar el modelo: las rutas de salida relativas de los
  scripts que lo importan se rompen (se perdió una vez el JSON del A/B). Usar siempre rutas absolutas.
- Disco: quedaban 4,2 GB libres a media tarde (la caché de HF creció a 21 GB con los modelos del agente visual).
