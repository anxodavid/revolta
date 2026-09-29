# plan · ronda 3

### Operador escéptico de canales faceless: PIERDE/NO APRUEBA

La prueba falsable del nicho (§A.4 y puerta P1) decide solo por vistas a 30 días (parada si la mediana es menor de 40), sin impresiones, CTR, fuentes de tráfico ni un plan de siembra. En un canal nuevo, anónimo y en galego, menos de 40 vistas es el resultado por defecto por falta de distribución, así que la prueba no distingue entre 'no hay demanda' y 'YouTube no lo enseña'. Cómo arreglarlo:
1. Meter en la regla de decisión las impresiones por vídeo, el CTR de impresiones, el % de tráfico por fuente y la retención a 2 min.
2. Añadir una siembra mínima y anónima de cada episodio en 3-5 comunidades galegas, con minutos acotados dentro de D3.
3. Definir un estado 'no concluyente': con menos de unas 1.000 impresiones o menos de N visitas sembradas, se itera título y miniatura, no se para.
4. Declarar el nicho inexistente solo cuando haya exposición suficiente y el CTR, la retención a 2 min y el % de espectadores de Galicia del tráfico sembrado queden por debajo de umbrales numéricos fijados de antemano.

Errores factuales: §7.1 fecha la nota de TechCrunch el 16-07-2026, pero la URL citada es del 20-07-2026 (techcrunch.com/2026/07/20/...). | §4.2 da como hecho, sin fuente, que 3 episodios en la primera semana dan al algoritmo 'qué encadenar'; es una inferencia no marcada como [S].

He leído el contexto y la pieza entera (931 líneas) y he contrastado los datos con el repositorio y con la web. No he leído veredictos anteriores.

**Lo que se sostiene:**
- **Comparables.** Las búsquedas de busquedas-yt.txt existen y coinciden con lo citado (Relatos al Oído 107.875; Misterios 9.135; Pergamino 5.106; Histórias Chatas 439.701).
- **Tiempos de máquina.** La extrapolación (4,4-5,8 h sin LLM) está en medidas/escala y es coherente.
- **Umbrales del código.** Los UMBRAIS de pipeline.py coinciden con el plan (WER 0,06; −18/−16 LUFS; H1 = 0).
- **Política de monetización.** La aclaración de TubeFilter del 13-07-2026 dice lo que cita el plan: tres categorías, 'image slideshows and templated storylines', aplicación a nivel de canal y que es una aclaración, no una norma nueva.
- **YPP 2027.** Las 8.000 h desde el 1-02-2027 salen en el blog oficial. El plan también es honesto con la economía (valor esperado ≈ 0 €), con que el YPP puede denegarse (40-60 % [S], sin comparables) y con que P0 no se pasa hoy (C0 80 %, 'sin fuente' 2/5).

**Falla en lo que un operador de canales faceless mira primero: la prueba del nicho.** La puerta P1/§A.4 declara el nicho inexistente si la mediana a 30 días es menor de 40 vistas. Pero en un canal nuevo, anónimo, sin historial, con 8 vídeos y en una lengua con casi ningún volumen de búsqueda, las vistas de los primeros 30 días miden sobre todo si YouTube le da impresiones, no si hay demanda. El propio plan cita Boring History Bites (inglés, mercado enorme) con 128-1.500 vistas por vídeo. Menos de 40 vistas es el resultado por defecto de casi cualquier canal nuevo, haya nicho o no, así que la prueba no puede falsar lo que dice falsar.

Faltan tres cosas:
- **Métricas de embudo en la regla de decisión.** Impresiones, CTR de impresiones y fuentes de tráfico (búsqueda, navegación, sugeridos, externas) no entran en la regla. La retención a 2 min aparece en el cuadro de mando, pero no en P1.
- **Un plan mínimo de siembra**, compatible con D3 y D6: difundir cada vídeo en 3-5 comunidades galegas (r/galicia, Mastodon/Bluesky en galego, foros o grupos de lendas) desde una cuenta anónima, con horas acotadas.
- **Separar 'sin distribución' de 'sin demanda'.** Por ejemplo: si las impresiones son menos de unas 1.000 por vídeo, el resultado es no concluyente y se cambian título y miniatura o se siembra otra vez. PARADA solo si, con exposición suficiente (impresiones ≥ X o ≥ N visitas externas sembradas), el CTR y la retención a 2 min del tráfico sembrado quedan por debajo de umbrales fijados de antemano.

Sin esto, las probabilidades de PARADA (35-50 %) y los escenarios de §1.3 descansan en una métrica que confunde el algoritmo con el mercado. Es justo la ingenuidad sobre el algoritmo que el listón prohíbe.

**Problemas menores:**
- En §4.2, '3 episodios la primera semana para que el algoritmo tenga qué encadenar' es un supuesto sin base.
- La fecha de TechCrunch no es coherente: el texto dice 16-07-2026 y la URL es del 20-07-2026.
- Que el galego exista como idioma de pista multi-audio sigue sin verificar. El plan lo reconoce; la búsqueda en la web tampoco lo confirma.
