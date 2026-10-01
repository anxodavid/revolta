# Hoja de prueba de la pieza VISUAL, ronda 1 (Gauntlet 3)

16 planos del tema **"As meigas de verdade"** (4 por fase: fila 1 gancho, fila 2 transición, fila 3 calma, fila 4
durmir), para que la juzgue **un crítico ciego** frente al storyboard de la referencia. Este agente no la juzga.

**Quién hizo qué.** Los 16 prompts (`planos.json`) los escribió Claude (agente director de arte) siguiendo la biblia
(`../biblia.md`) y el arco del tema (`../../tema/investigacion.md`). Todo lo demás es **automático**: generación
(SDXL base + UNet SDXL-Lightning 4 pasos, 1344x768, estilo `filme`), puerta de revisión (`revisor.py` versión 5:
MediaPipe, Florence-2 y CLIP), regeneración de los rechazados, gradación por fase (`imaxes.graduar`) y montaje de la
hoja. **Nadie eligió ni retocó imágenes a mano**: en cada plano está la primera imagen que aprobó la puerta (o, si
ninguna, la de menos problemas, marcada en `porta.md`).

Orden: `probas/visual_hoja_prueba.py planos.json TRABALLO visual/r1` con el candado de CPU.

| Fichero | Qué es |
|---|---|
| `contactsheet.jpg` | 4x4 fotogramas de 960x540 (recortados a 16:9 como en el montaje), graduados, solo con el número del plano |
| `contactsheet_320.jpg` | los mismos a 320x180, para compararla al mismo tamaño que el storyboard de la referencia (320x180) |
| `planos.json` | entrada: prompt, fase, tipo de plano, `negativo` y `son` de cada plano |
| `prompts.json` | prompt final de cada intento (con el estilo y la luz que añade el código), tokens, semilla, problemas de la puerta, descripción de Florence-2, arquetipo y medidas de CLIP |
| `porta.md` | resultado de la puerta por plano e intento, segundos por imagen y rechazos por motivo |
| `graduacion.json` | lo que la gradación aplicó a cada imagen (luminancia antes y después, gamma, contraste, brillo, saturación) |

Referencia para el A/B (fuera del repo, imágenes de terceros): 220 miniaturas de 320x180 del storyboard de
https://youtu.be/_lnOveSTjWA en `$SCRATCH/visual/ref/tiles/` y 16 repartidas por el vídeo en
`$SCRATCH/visual/ref/ref_16_320.jpg`.
