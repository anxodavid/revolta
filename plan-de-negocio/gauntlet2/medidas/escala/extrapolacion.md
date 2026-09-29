# Extrapolación a 60 min narrados + 30 min de cola

Xerado por `extrapolacion.py` a partir das medidas do 29-09-2026.

| Etapa | Medido [P] | Escala | 60 + 30 min (min de reloxo) | Nota |
|---|---|---|---|---|
| 4 voz (StyleTTS2 Brais, frase a frase) | 223 s e 248 s para 193 e 231 s narrados; na 2.ª, 176 s de síntese + 73 s de carga | s de liña narrada | 47-69 | 0.76-1.15 s de reloxo por s narrado |
| 5 imaxes (SDXL-Turbo, 4 pasos, 1024x576, CPU) | 12.1-25.4 s por imaxe (media 19.8 e 16.2 s; 30 imaxes); carga do modelo 24-331 s | imaxes (255-287) | 69-100 | a carga de 5,4 min foi en frío (disco) |
| 6 son (choiva e mestura) | 5.2 e 5.0 s | s de vídeo | 2-2 |  |
| 7 montaxe (Ken Burns, brétema, x264) | 285 e 309 s (1.28-1.40 s por s de vídeo) | s de vídeo | 115-126 | só se se cambia a carga de imaxes por treitos (RAM, §5.1) |
| 8 QA (ASR mestura e voz, LanguageTool, ebur128, follas) | 128 e 135 s; ASR sobre 16 min: RTF 0.201, WER 0.015 | ASR: s narrados; resto: s de vídeo | 29-42 | 1 ou 2 pasadas de ASR (mestura / mestura + voz soa) |
| 2 corrección (LanguageTool) | 14-20 s para 475 palabras | palabras (x15,6) | 4-6 |  |
| **Subtotal sen LLM** | | | **266-346** (**4.4-5.8 h**) | |
