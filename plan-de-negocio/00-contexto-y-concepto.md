# Contexto del proyecto (leer antes de trabajar)

## Objetivo
Business plan para un canal de YouTube de vídeos hechos íntegramente con IA sobre HISTORIA DE GALICIA,
pensados para un público que quiere QUEDARSE DORMIDO escuchándolos ("history for sleep" / "historia para durmir").
100% en galego. La calidad de la NARRACIÓN en galego y de los GUIONES en galego es IMPRESCINDIBLE (no negociable).

## Concepto tomado de una conversación previa con Gemini (tomar solo el concepto, no literal)
Transcripción completa: gemini_conversation.md (misma carpeta). Concepto:
- Canales "faceless" de historia 100% IA (guion LLM -> TTS -> imágenes/clips IA -> montaje automático) con curaduría humana como filtro anti-"AI slop".
- Adaptación a Galicia en galego: nicho identitario (residentes + diáspora), pero 3 cuellos de botella: TAM pequeño, TTS en galego inmaduro, comunidad lingüística que castiga errores de lengua/historia.
- Economía de vídeo largo (watch time, mid-rolls, coste marginal bajo), lógica de cartera/localización (gl -> es/pt).
- El promotor: curiosidad + afán emprendedor + experimentación tecnológica; poco tiempo; no quiere suscripciones caras; primero MVP barato con puertas de decisión; luego pipeline agéntico (investigador -> lingüista galego -> director -> prompts visuales -> productor -> montador -> auditor QA con bucle de retorno), montado con Claude Code (Python/LangGraph). Ya hizo un mini piloto con Clipchamp (voz Sabela de Microsoft) y a su mujer (muy crítica) no le pareció una locura, pero era demasiado manual.
- LO QUE NO SE TOMA: el estilo "fábrica de engagement" (ganchos viscerales, curiosity gaps, segunda persona agresiva) es lo OPUESTO a contenido para dormir: aquí voz calmada, ritmo lento, sin sobresaltos, larga duración (1-3 h). Las herramientas concretas de esa charla (Colab móvil, créditos NVIDIA, Clipchamp) son solo opciones a evaluar.

## Respuestas del promotor
- Ambición: lo PRIMERO es ubicar los posibles RETORNOS. Plan por etapas:
  Etapa 1 "piloto barato con puertas" (<50 €/mes, ~4 h/semana) y Etapa 2 "proyecto lateral rentable" (50-200 €/mes, 6-10 h/semana, ingresos recurrentes en 12-18 meses) -> inversión perfectamente viable.
  Etapa 3 "apuesta seria/red" (1.000-5.000 € iniciales, p.ej. licenciar voz de locutor galego, escalar gl->es/pt) SOLO si 1 y 2 funcionan.
- Juez de la voz: el promotor y su mujer (nativos) harán de críticos ciegos con un kit A/B de muestras de voz (se genera aparte con modelos abiertos del Proxecto Nós: StyleTTS2 Brais/Celtia, VITS/Matcha Icía, Sabela, Iago, Paulo...).
- Referencia de calidad: "vídeos divulgativos de consumo antes de dormir"; qué referencia concreta encaja mejor lo decide el propio plan y se comprueba en las pruebas.
- Intensidad: alta.

## Idioma de trabajo
El business plan se redacta en CASTELLANO (el promotor escribe en castellano). Todo guion/muestra/nombre de canal para el público va en GALEGO normativo (RAG) de alta calidad.
Fecha actual: 29 de septiembre de 2026. Verifica datos con fuentes web actuales; marca claramente qué es dato con fuente (URL) y qué es supuesto.
