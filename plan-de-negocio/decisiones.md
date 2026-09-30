# Decisiones del promotor (29-09-2026)

Respuestas a las decisiones D1-D6 del §0.2 de `plan-de-negocio.md`, tomadas tras el tribunal final del Gauntlet.
**Cambian el enfoque del plan:** de un canal con garantía humana de calidad a un canal **desatendido** y 100 % automático.

| # | Decisión | Respuesta |
|---|---|---|
| D5 | Coste de la garantía de calidad (~305 €/episodio) | **No se paga.** Se hace un test de baja calidad con el mejor modelo open source y un proceso automático más o menos sofisticado que "dé el pego", **sin revisión humana**. Canal desatendido. Referencia: [Historia Desconocida, "Versalles en 1682…"](https://youtu.be/_lnOveSTjWA) |
| D6 | Si nadie financia la calidad | **Hobby publicando en anónimo.** |
| D1 | Validación formal de la voz (850-1.500 €) | **Sí, aunque no haya terceros**, pero **solo si el canal muestra tracción** (aclaración posterior). El piloto sale con la mejor voz disponible. |
| D2 | Si ninguna voz pasa el listón | **Quedarse con la que esté más cerca de pasarlo.** |
| D3 | Dedicación | **~6 h/semana mientras se monta el pipeline; ~1 h/semana después** (vigilancia). |
| D4 | Licencia de las voces de Nós | **Pedir permiso a Nós/USC** mientras se monta; crédito a Nós en la descripción aunque el canal sea anónimo. |

## Consecuencias para el plan (pendientes de rehacer)
- La condición inicial "la calidad del galego es imprescindible" pasa a ser **"lo mejor que dé un proceso automático"**. Las puertas F/F2 y el paquete de revisión humana dejan de aplicarse.
- Nuevo listón del producto: canales faceless de historia hechos con IA (tipo *Historia Desconocida*), en galego y en formato para dormir.
- Riesgos que suben: política de YouTube de contenido inauténtico/masivo (canal 100 % automático), errores de lengua e historia sin filtro humano y reacción de la comunidad galega. En anónimo, el riesgo reputacional personal baja.
- Voz del piloto: la mejor en el kit A/B y en el control ASR (hoy, StyleTTS2 Brais de Nós: WER 0,26).

# Decisiones del promotor (30-09-2026, segunda sesión)

| # | Decisión | Respuesta |
|---|---|---|
| D7 | Siguiente muestra | **Vídeo largo** siguiendo la estela de la muestra más madura (ronda 3 del Gauntlet 2). El operador fija ≈ 30 min, como la referencia. |
| D8 | Guion sin LLM por API "de momento" | **Lo escribe Claude con agentes y un proceso de Gauntlet.** No es desatendido: se declara en la QA. Los controles automáticos se mantienen como red de seguridad. |
| D9 | Imagen | Mejorar la parte visual a partir de los problemas que vio el juez (luz plana y monótona, composiciones repetidas, iconografía no gallega, imágenes blandas). |
| D10 | Tono de la voz | **Más gancho y más atractivo los primeros minutos**, y bajada gradual hacia el tono de dormir. |
| D11 | Reclamo | **"Cousas de Galiza para durmir"**. Temas posibles: meigas, queimadas, capítulos de la historia, muiñeira o lo que el Gauntlet vea con más gancho y audiencia. |
| D12 | Método | Trabajar con agentes, guardando el trabajo parcial en git cada poco y documentando los aprendizajes cada poco. |

Contexto y reglas del Gauntlet 3: `plan-de-negocio/gauntlet3/contexto.md`.
| D13 | Ambiente sonoro (tras oír la muestra, 30-09-2026) | **Nada de ruido constante.** La lluvia solo cuando la escena tiene lluvia; el crepitar solo cuando hay fuego; **tramos de voz limpia**. "En cualquier caso, que el Gauntlet mida la mejor opción." |
| D14 | Ambiente sonoro (tras la muestra A/B, 30-09-2026) | De los tres fondos, **el mejor es el tercero (lluvia nueva + lareira)**, pero **no debe volverse monótono ni cansino**: adaptarlo a la escena. **Si la escena es de un gentío, murmullo de voces ininteligibles.** Que el Gauntlet mida la mejor opción (D13). |
| D15 | Imágenes de referencia (30-09-2026) | El promotor quiere **imágenes de referencia o semilla** para lo que el modelo no conoce (carros de bois, hórreos...) y generar variaciones a partir de ellas. Pendiente de probar (img2img, ControlNet, IP-Adapter), con fotos propias o de licencia libre. |
| D16 | Animación (30-09-2026) | Para **futuras versiones**: un modelo que anime la imagen para que las personas se muevan. Pendiente de evaluar coste y licencia (image-to-video en GPU alquilada; en CPU, paralaje 2,5D y microanimaciones). |

