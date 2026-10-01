# Hoja de prueba de la pieza VISUAL, ronda 2 (Gauntlet 3)

16 planos de "As meigas de verdade" (fila 1 gancho, 2 transición, 3 calma, 4 durmir) para el crítico ciego, con los
cambios que pidió el veredicto de la r1 (`../../veredictos/visual-r1.md`): la premisa del episodio en pantalla
(escribano, edicto, partera, curandera, ordeño, fuente, era), dos personas que se relacionan en *over-the-shoulder* en
el gancho y la transición, calma más oscura y durmir sin llama viva. Este agente no la juzga.

**Quién hizo qué.** Los prompts (`planos.json`, con los campos nuevos `clave` y `son`) los escribió Claude (agente
director de arte) según la biblia de la ronda 2. Todo lo demás es automático: SDXL-Lightning 4 pasos a 1344x768,
puerta `revisor.py` versión 6 (MediaPipe, Florence-2 y CLIP, con los topes de arquetipos a escala de un episodio de
150 planos), regeneración (el 4.º y 5.º intento, guiados con prompt negativo), gradación por fase y hoja. Nadie eligió
ni retocó imágenes a mano.

Ficheros como en la r1: `contactsheet.jpg` (960x540 por fotograma), `contactsheet_320.jpg`, `imaxes/NN.jpg`,
`prompts.json`, `porta.md` y `graduacion.json`.
