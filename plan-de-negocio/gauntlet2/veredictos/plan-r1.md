# plan · ronda 1

### Operador escéptico de canales faceless: PIERDE/NO APRUEBA

Las cifras de costes y horas del modo desatendido (una noche de CPU por episodio de 60-90 min, ≈1 h/semana del promotor, 14 controles que bloquean la publicación) no están medidas y no coinciden con el pipeline real:
- No se ha producido ningún episodio: la carpeta gauntlet2/video está vacía y no existe ningún qa.json.
- El código genera vídeos de 3-5 min y sus umbrales son otros: WER 0,25 frente a ≤6 %, y −24/−18 LUFS frente a −16/−18.
- El código no implementa H1, H2, P1 ni los canarios C0.
- El dossier de fuentes, que el plan da por automático, está curado a mano.

Qué hacer:
1. Ejecutar el pipeline de extremo a extremo con el tema de los irmandiños y medir la duración real de cada etapa: segundos por imagen con SDXL-Turbo en CPU, montaje, ASR y proporción de episodios que el semáforo bloquea.
2. Extrapolar esas medidas a 60 min y rehacer §4.1 y §3.2 con datos medidos [P].
3. Presupuestar en horas (o automatizar y medir) la creación del dossier de cada episodio.
4. Alinear los umbrales del código con los del plan, o corregir el plan.
5. Añadir P0 un criterio medido: que un episodio de ≥60 min pase por el pipeline sin intervención humana en ≤8 h de reloj.

Errores factuales: La nota de TubeFilter del 13-07-2026 dice expresamente que es una aclaración de la política y no una norma nueva; el plan la presenta como un endurecimiento ('por qué YouTube endureció la política'). Es un matiz: el contenido afectado ya estaba excluido de la monetización. | Los umbrales de QA del plan (A1: WER ≤6 %; A2: −16 a −18 LUFS) no coinciden con los que aplica el código (herramientas/pipeline/pipeline.py: UMBRAIS wer_max 0,25; LUFS −24 a −18). | El plan describe la etapa [1] Fuentes→dossier como automática, pero el único dossier que existe (temas/irmandinos-apertura.yaml) se curó a mano a partir de notas de fuentes ya verificadas.

El plan (/home/user/revolta/plan-de-negocio/gauntlet2/piezas/plan-desatendido.md) es honesto con el dinero y con la plataforma. Asume que el canal pierde dinero. Toma la referencia como un pico y no como la media, y los datos de /home/user/revolta/plan-de-negocio/gauntlet2/referencia.md encajan con esa lectura. Da por probable el rechazo o la retirada del YPP, obliga a activar la etiqueta de contenido sintético, trata el art. 50 del AI Act y propone puertas con números. He comprobado en la web lo más sensible:
- El blog de YouTube confirma que, desde el 1-02-2027, los nuevos solicitantes del YPP necesitan 8.000 horas vistas cualificadas en 365 días y que los umbrales de fan funding no cambian.
- TubeFilter (13-07-2026) confirma las tres categorías, con 'image slideshows' y 'templated storylines' como ejemplos, y que la política se aplica a nivel de canal. Además dice que es una aclaración y no una norma nueva, un matiz que el plan no recoge pero que no cambia el análisis.

Un operador no lo firmaría porque todo el régimen desatendido (1 episodio de 60-90 min cada noche en 4 CPU, ≈1 h/semana, 14 controles) está sin medir y no coincide con el pipeline real:
(a) En gauntlet2/video no hay ningún vídeo ni ningún qa.json. No se ha producido ni un episodio, así que el tiempo por imagen, el tiempo de montaje y el total de 3,5-6,5 h son [S].
(b) El código real (/home/user/revolta/herramientas/pipeline/pipeline.py) está hecho para vídeos de 180-300 s. Sus umbrales contradicen los del plan: WER máx. 0,25 frente al ≤6 % del control A1, y −24 a −18 LUFS frente a −16/−18. Además no implementa H1, H2, P1, I1-I3 ni los canarios C0.
(c) La etapa [1] 'Fuentes → dossier', que el plan presenta como automática, en la práctica es un dossier curado a mano en temas/irmandinos-apertura.yaml. Viene de las notas del guion muestra ya revisado por humanos. Con 50 episodios al año, alguien tiene que construir 50 dossieres, y ese trabajo no aparece en las horas de §3.2. Si se automatiza con Galipedia y obras de dominio público, vuelve el problema de los mitos románticos que el propio plan reconoce.
Hay carencias menores:
- Los comparables anglófonos y en castellano ([R], como Sleepless Historian) no se han vuelto a verificar hoy.
- El AVD como KPI de puerta es engañoso en contenido para dormir, porque la gente se duerme con el vídeo puesto y se escucha en pestañas en segundo plano. Hace falta otra métrica de apoyo, como el porcentaje de retorno de espectadores o las sesiones repetidas.
- El 40-60 % de probabilidad de rechazo del YPP no se apoya en casos comparables de canales de voz IA con presentación de imágenes que hayan sido admitidos o rechazados en 2026.
