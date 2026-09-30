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

(pendiente)

## 4. Curva calibrada y medidas por punto

(pendiente)

## 5. Muestra de escucha

(pendiente)

## 6. Límites y qué no se pudo medir

(pendiente)
