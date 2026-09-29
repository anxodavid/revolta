# Medidas para la pregunta "¿existe el nicho?" (29-09-2026)

## 1. Búsquedas en YouTube (`busquedas-yt.txt`)

yt-dlp, `ytsearch15:<consulta>`, cliente `android_vr`, 29-09-2026. Columnas: vistas | canal | título | duración (s) | URL.
Consultas: "história para dormir", "história de Portugal para dormir", "Galiza para dormir", "Galicia para dormir",
"Galicia legends sleep", "lendas galegas", "Santa Compaña", "historia de Galicia", "historia de Galicia para durmir",
"boring history for sleep". Los títulos pueden salir traducidos al inglés por YouTube (el cliente pide inglés):
el vídeo es el mismo.

Lectura resumida (detalle en la pieza `../../piezas/plan-desatendido.md`, §A):
- Ningún resultado de historia o lendas **para dormir en galego** en ninguna de las 10 búsquedas.
- "Galicia para dormir" en castellano/inglés: Relatos al Oído 107.875 (lendas, 2 h), 17.264 (mosteiro), 13.904
  (Compostela), 7.829 (Lugo); Misterios para Dormir Profundo 9.135 (lendas de Galicia e Asturias); El Pergamino Mágico
  5.106 (Santa Compaña); cola larga de 16-292 vistas (Relax and Let Go, Spain Dreams ASMR, The Dreaming Atlas, Gaita Galega).
- "lendas galegas" en galego (sin formato para dormir): politicalinguistica 522-1.577; SAGA 1.396; resto 59-380.
- Portugués (pt-BR sobre todo): hay un género "história para dormir" adulto con IA y con tracción: Histórias Chatas
  Para Dormir 439.701; Descanse com Histórias 214.303 y 239.543; Historias para relaxar e dormir 31.970-227.556;
  História para Acalmar 90.586. **Ninguno sobre Galicia.** "TODA A HISTÓRIA DE PORTUGAL PARA DORMIR": 5 vistas.
- Inglés: Sleepless Historian 265-1.025 K por vídeo; saturado.

## 2. Pistas multi-audio: traducción y voces (`multiaudio/`)

Condiciones: CPU de 4 núcleos **compartida** con otro proceso del pipeline al 300 % de CPU (carga media 4,4-5,0), así
que los tiempos son pesimistas.

| Paso | Herramienta (licencia) | Entrada | Tiempo | Resultado |
|---|---|---|---|---|
| gl→es | Nós `Nos_MT-CT2-gl-es` (MIT), CTranslate2 int8, beam 4 | 11 frases, 126 palabras (`fonte_gl.txt`, apertura del guion de ejemplo) | **1,7 s** (≈ 74 palabras/s) | `nos-mt_gl-es.txt`: 9/11 frases correctas; **2 errores**: "acomódate" → "acuérdate" (cambio de sentido) y "a Rocha Forte" → "la Roca Forte" (nombre propio traducido) |
| TTS pt-PT | Piper `pt_PT-tugão-medium` (datos CC0; afinada desde la voz *lessac*) | `pt_referencia_manual.txt` (traducción manual, sustituto de la MT gl→pt que Nós no tiene) | 4,6 s con carga → 33,3 s de audio: **RTF 0,14** | `piper_pt_PT-tugao.wav` |
| TTS es | Piper `es_ES-davefx-medium` (datos CC0; afinada desde *lessac*) | salida de la MT | 5,1 s → 39,1 s: **RTF 0,13** | `piper_es_ES-davefx.wav` |
| TTS pt-BR | Kokoro-82M int8 ONNX (Apache-2.0), voz `pm_alex`, velocidad 0,9 | `pt_referencia_manual.txt` | 56,9 s → 39,3 s: **RTF 1,45** | `kokoro_pt-br.wav` |
| TTS en | Kokoro, voz `bm_george` | `en_referencia_manual.txt` (traducción manual) | 68,6 s → 47,2 s: **RTF 1,45** | `kokoro_en.wav` |
| TTS es | Kokoro, voz `em_alex` | salida de la MT | 48,7 s → 41,1 s: **RTF 1,19** | `kokoro_es.wav` |

No medido (falta disco: quedaban 1,3-3 GB libres): Nós gl→en (1,7 GB), MT gl→pt, ASR de ida y vuelta en pt/es/en.
