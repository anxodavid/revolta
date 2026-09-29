# plan · ronda 1

### Operador escéptico de canales faceless: PIERDE/NO APRUEBA

El plan no incorpora las medidas que ya tiene. Hay que hacer cuatro cosas:
(a) Rehacer §0, §3.1 y §4.1 con los tiempos medidos que da medidas/escala/extrapolacion.py: voz 47-69 min, imágenes 69-100 min, montaje 115-126 min, subtotal sin LLM 4,4-5,8 h. También hay que unificar las horas del MVP, que hoy son 45-60 h en el resumen y 62-92 h en la tabla.
(b) Escribir la §3.3, que falta, midiendo con un cronómetro los minutos por episodio que exige el dossier semimanual, y sumarlos al régimen estable de §3.2. Si el total pasa de 1 h/semana, hay que decir cómo se cumple la D3: bajando la cadencia o reutilizando dossieres.
(c) Declarar que el C0 real es del 70 % (solo 2 de 5 invenciones 'sen_fonte' detectadas), es decir, que hoy no se pasa P0, y decir qué control (H2 u otro) lo sube al 80 % y con qué medida.
(d) Alinear los umbrales de pipeline.py con los del plan: WER ≤ 6 % y sonoridad de −16 a −18 LUFS.

Errores factuales: §4.1: voz con RTF 0,28-0,4 = 17-25 min para 60 min; lo medido en el pipeline (extrapolacion.py, ronda r2) es 0,76-1,15 s de reloj por segundo narrado, es decir, 47-69 min | §0, punto 4: MVP de 45-60 h y 8-10 semanas; la tabla de §3.1 del mismo documento dice 62-92 h y 11-15 semanas | §3.1, §3.3 y §5.1 remiten a una §3.3 que no existe | §5.1 dice 'Ver C0 medido en §6.1', pero §6.1 no da ninguna cifra; la medida real (medidas/c0-irmandinos-apertura/canarios.md) es del 70 %, por debajo del umbral del 80 % del P0 | §4.2(a) atribuye a TubeFilter (13-07-2026) que la frecuencia de subida es una señal de contenido inauténtico; el artículo no lo dice | §3.1 habla de un 'pipeline de 8 etapas'; §0 y §5.1 dicen 9 | A2 exige −16 a −18 LUFS; el código acepta −24 a −18 y el vídeo publicable mide −20 LUFS; el código acepta un WER de hasta 0,25 frente al ≤6 % del plan

He leído entera /home/user/revolta/plan-de-negocio/gauntlet2/piezas/plan-desatendido.md y la he contrastado con las medidas reales que hay en gauntlet2/medidas/, con el código de /home/user/revolta/herramientas/pipeline/ y con la web.

Lo que está bien:
- Es honesto con el dinero: la pérdida esperada es de 30 a 120 € y los ingresos esperados de 0 a 30 €.
- Trata la referencia como un pico y no como la media. referencia.md lo respalda: los vídeos de ago-sep de Historia Desconocida hacen 1.300-6.400 vistas.
- Verificado en el blog de YouTube: desde el 1-02-2027 los nuevos solicitantes del YPP necesitan 8.000 horas vistas cualificadas, y los umbrales de fan funding no cambian.
- Verificado en TubeFilter: la nota del 13-07-2026 es una aclaración y no una norma nueva, recoge los ejemplos 'image slideshows and templated storylines' y se aplica a nivel de canal.
- La etiqueta de contenido sintético y el art. 50 del AI Act están bien razonados, y hay puertas cuantificadas (P1, P2 y P3).

Aun así, un operador no lo firmaría, porque el plan contradice sus propias medidas y no presupuesta el trabajo manual recurrente:

(1) La §4.1 sigue siendo un supuesto [S] y se queda corta, aunque ya hay medidas [P] en el repo. Según medidas/escala/extrapolacion.py y las ejecuciones r2:
- La voz tarda 0,76-1,15 s de reloj por cada segundo narrado (47-69 min), no el RTF 0,28-0,4 (17-25 min) que dice el plan.
- El montaje tarda 115-126 min.
- El subtotal sin LLM es de 4,4-5,8 h, frente a los 3,5-6,5 h del plan con el tramo bajo sin base.

(2) El resumen (§0, punto 4) dice 45-60 h y 8-10 semanas, pero la tabla de §3.1 dice 62-92 h y 11-15 semanas. Además, §3.3 se cita cuatro veces y no existe.

(3) La prueba C0 medida detecta 14 de 20 errores (70 %), por debajo del umbral del 80 % que el propio plan fija en P0 y A6. La familia 'sen_fonte' solo detecta 2 de 5: pasan invenciones plausibles como 'a revolta máis grande de toda Europa'. El plan no lo menciona, aunque en §5.1 remite a 'C0 medido en §6.1' y ahí no hay ninguna cifra. Con la cadena actual, el P0 no se cumple.

(4) El régimen de ≈1 h/semana de §3.2 no incluye el dossier de cada episodio. El diagrama lo describe como semimanual: el promotor elige de 3 a 6 fuentes. El único dossier que existe (18 hechos) se hizo a mano. Para 50 episodios al año, eso es trabajo humano recurrente sin medir que puede romper la D3.

(5) Los umbrales del código siguen sin coincidir con los del plan:
- pipeline.py admite un WER de hasta 0,25 y una sonoridad de −24 a −18 LUFS; el plan fija WER ≤ 6 % y −16 a −18 LUFS.
- El vídeo publicable mide −20 LUFS, fuera del rango del plan.
- El código solo acepta vídeos de 180-300 s.

(6) En §4.2(a) se cita a TubeFilter para decir que la frecuencia de subida es una señal de contenido inauténtico, y el artículo no dice eso.

Carencias menores:
- Los comparables anglófonos y en castellano ([R]) no se han vuelto a verificar hoy.
- La probabilidad de rechazo del YPP (40-60 %) sigue siendo un supuesto puro.
