# Imágenes elegidas del episodio "As meigas de verdade"

Las 162 imágenes que entraron en el montaje del 01-10-2026 (SDXL-Lightning 4 pasos, 1024x576), en JPEG de calidad 92
para que quepan en el repo, y `revision.json`, la caché de la etapa de imágenes de `longo.py` (prompt, semilla,
intentos y problemas de la puerta de cada plano). Sirven para la ronda de arreglos sin volver a generar las 162
imágenes (≈8 h de CPU):

1. Copiar `revision.json` a `$SCRATCH/longo/w/imaxes/` y convertir cada `NNN-xxxxxxxx-K.jpg` a PNG con el mismo nombre
   en esa carpeta (PIL: `Image.open(jpg).save(png)`).
2. Cambiar en `video/escenas.json` el prompt de los planos que hay que rehacer (tribunal final: 84, 133, 161, 56, 5,
   31, 61, 67, 91, 145 y 153): al cambiar el prompt cambia la clave de la caché y solo esos se generan otra vez.
3. Relanzar `lanzar-longo.sh`: la voz se regenera (≈16 min) y el resto de imágenes sale de la caché.
