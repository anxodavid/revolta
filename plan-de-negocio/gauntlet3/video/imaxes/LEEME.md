# Imágenes elegidas del episodio "As meigas de verdade"

Las 162 imágenes del montaje vigente (SDXL-Lightning 4 pasos, 1024x576), en JPEG de calidad 92 para que quepan en el
repo, y `revision.json`, la caché de la etapa de imágenes de `longo.py` (prompt, semilla, intentos y problemas de la
puerta de cada plano). Sirven para rehacer el máster o cambiar planos sueltos sin volver a generar las 162 (≈8 h de CPU).

**Historia:** producción del 01-10-2026 (tarde) y ronda de arreglos del tribunal final (01-10-2026, noche), que
cambió los planos 5, 31, 56, 61, 67, 84, 91, 133, 145, 153 y 161 (`escenas.json`). Claude miró cada intento de esos
11 planos; en el 91 y el 145 eligió a mano el intento 0 en vez del de la puerta (campos `escolla_manual` y
`escollida_porta` en `revision.json`). `revision.json` conserva también las entradas de los prompts anteriores.

**Restaurar la caché en una sesión nueva:**

1. Copiar `revision.json` a `$SCRATCH/longo/w/imaxes/` y convertir cada `NNN-xxxxxxxx-K.jpg` a PNG con el mismo nombre
   en esa carpeta (PIL: `Image.open(jpg).save(png)`).
2. Para rehacer un plano, cambiar su prompt en `video/escenas.json`: cambia la clave de la caché y solo ese se genera
   otra vez. Los demás salen de la caché aunque no pasaran la puerta: `imaxes.py` da por hecho un plano si faltan los
   ficheiros de sus otros intentos (caché restaurada) o si tiene `escolla_manual`.
3. Relanzar `lanzar-longo.sh`: la voz se regenera (≈10-16 min) y el resto sale de la caché.
