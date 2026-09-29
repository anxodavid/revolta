# Herramientas de voz (kit A/B)

Generan las muestras del test ciego de voces en galego con los modelos abiertos del
[Proxecto Nós](https://huggingface.co/proxectonos) (Apache-2.0, USC). Las grabaciones humanas
de referencia salen de los corpus `Nos_Brais-GL` y `Nos_Celtia-GL` (CC-BY-4.0, conjunto de test,
no usado en el entrenamiento).

| Script | Qué hace |
| --- | --- |
| `synth.py VOZ TEXTO.txt SALIDA.wav [length_scale]` | Narra un texto por frases con pausas largas (ritmo para dormir). Voces: brais, celtia, icia, iago, paulo. |
| `make_t1.py` | Test 1: frases idénticas, locutor humano vs. su voz sintética. |
| `asr.py` | Control automático: transcribe con Whisper (medium) y calcula WER. |
| `nos_front.py` | Front-end oficial de Nós (normalización + fonemas con Cotovía). |

Requisitos: `coqui-tts[codec]`, `transformers<5`, `torch` (CPU basta: factor de tiempo real ~0,13),
Cotovía 0.5 (`cotovia_0.5_amd64.deb` + `cotovia-lang-gl_0.5_all.deb`) para las voces de fonemas,
`faster-whisper` y `jiwer` para el control ASR. Los checkpoints (~1 GB cada uno) se descargan de Hugging Face.

Nota: escribe las cifras en letra en el guion. Cotovía normalizó "1467" como "mil catrocentas…".

## StyleTTS2 (Nós, junio 2026)

`st2_sleep.py` renderiza un texto con **Nos_StyleTTS2-Brais-GL** por frases, con escala de duraciones
(`SCALE`, por defecto 1,2) y pausas. Se ejecuta dentro de una copia del repo del modelo (carpeta `st2/`),
con `REF_WAV` apuntando a una grabación humana de referencia de estilo (p. ej. del corpus Nos_Brais-GL):

    TXT=texto_guion_v2.txt OUT=st2.wav REF_WAV=ref.wav python st2_sleep.py

## Control ASR sobre el fragmento del guion (29-09-2026)

WER con Whisper medium (menos es mejor; las cifras están infladas porque Whisper escribe el gallego con
grafías portuguesas, así que sirven solo para comparar voces entre sí):

| Voz | WER |
| --- | --- |
| StyleTTS2 Brais (escala 1,2) | 0,26 |
| VITS Icía | 0,38 |
| VITS Brais | 0,44 |
| VITS Iago | 0,45 |
| VITS Paulo | 0,46 |
| VITS Celtia | 0,50 |

Las grabaciones humanas de referencia (test 1) salen con un WER de 0–0,28 por frase.
