# Handoff: canal "Serán · Historia de Galicia para durmir"

Estado a 30-09-2026. Resume la primera sesión de trabajo (29 y 30 de septiembre de 2026) para poder retomarla en otra.
Los aprendizajes están en [`APRENDIZAJES.md`](APRENDIZAJES.md).

## 0. Gauntlet 3 (30-09 a 01-10-2026): vídeo largo "Cousas de Galiza para durmir"

**Si la sesión se corta, retomar desde aquí.** Encargo y decisiones (D7-D14) en
[`plan-de-negocio/gauntlet3/contexto.md`](../plan-de-negocio/gauntlet3/contexto.md) y en `decisiones.md`.

| Pieza | Estado | Dónde |
|---|---|---|
| Entorno | Hecho: `instalar.sh` en una orden (≈6 min, ≈16 GB) | `herramientas/pipeline/instalar.sh`, `entorno.sh` |
| Tema | Hecho: **"As meigas de verdade"**, GANA condicionado (ajustes en `contexto.md` §8) | `gauntlet3/tema/`, `veredictos/tema-r1.md` |
| Dossier | Hecho: 244 hechos con cita comprobada; ficha de 180 | `herramientas/pipeline/temas/meigas-de-verdade.yaml`, `gauntlet3/dossier/` |
| Guion | **r1 hecho** (3.503 palabras ≈ 26 min, puertas en verde); críticos A y B de la r1 en curso | `gauntlet3/guion/`, `veredictos/guion-r1-*.md` |
| Voz (embudo) | Hecho: Cotovía de Nós `-p1`, referencias viva/calma, curva calibrada (arousal 0,64 → 0,43) | `voz_st2.py`, `curva.py`, `gauntlet3/voz/` |
| Son | Hecho: ambiente por escena, opción C (D13, D14) | `son.py`, `gauntlet3/son/` |
| Visual | Hoja de prueba r1 en curso; después, crítico ciego | `imaxes.py`, `revisor.py`, `gauntlet3/visual/` |
| Vídeo | Pendiente | `herramientas/pipeline/longo.py` |

**Estado (01-10-2026, 18:10 UTC): episodio terminado.** "As meigas de verdade", 31:22, 1080p, 162 planos. QA
automático (`gauntlet3/video/qa.md`): 12/13 puertas; falla `imaxes_revisadas` (127/162 planos aprobados por la puerta;
el resto se quedó con su mejor intento). −17,1 LUFS, WER 0,031, subtítulos 100 % en su sitio, ritmo 157 → 114
palabras/min, planos de 5 a 16 s. Nadie lo ha revisado a mano.
- **Verlo:** página https://claude.ai/artifact/6hXeH9wqWbHCWqwVW5K5EX (en galego normativo por petición del promotor;
  copia 720p en HLS fMP4, capítulos, faja del embudo, QA, descripción para YouTube). Avance de 4:50 en
  `gauntlet3/video/avance/`.
- **Imágenes elegidas** (162, JPEG) y la caché de la puerta en `gauntlet3/video/imaxes/` (su LEEME explica cómo rehacer
  solo los planos que pide el tribunal sin volver a generar el resto).
- **Máster 1080p (333 MB):** NO está en git (pendiente de que el promotor decida dónde archivarlo: 333 MB en el
  historial pesan en cada clon). Está en `$SCRATCH/longo/w/video.mp4` y partido sin recodificar en
  `$SCRATCH/entrega/mestre-partes/` (10 anacos, se reúnen con `ffmpeg -f concat -safe 0 -i partes.txt -c copy`).
  **El scratchpad se pierde al acabar la sesión:** si el promotor no elige dónde archivarlo, el máster se rehace en la
  ronda de arreglos (las imágenes ya están en el repo; voz ≈ 16 min, montaje ≈ 70 min, QA ≈ 30 min).
- **Tribunal final (agente Claude, 01-10-2026; nadie ha visto ni oído el episodio entero):** `veredictos/tribunal-final.md`.
  **No publicable tal cual; sí con arreglos.** Gancho 4/5. Imagen: la comparación "a ciegas" no fue ciega de verdad
  (la referencia ya estaba descrita en `visual-r1.md`); empate 21-21 y elige la referencia ≈55/45 porque allí la gente
  hace más cosas; la carencia de la ronda 1 queda corregida a medias (sigue la luz eléctrica). Sonido: gana por
  medidas, sin escucha. Arreglos: (1) sustituir los planos 84 (bombilla y radiador, aprobado por la puerta), 133
  (farolas tras el rótulo VII), 161 (casa colonial) y 56 (maleta de ruedas); (2) en el mismo remontaje, los planos 5,
  31, 61, 67, 91, 145 y 153; (3) pico real ≤ −1 dBTP (mide −0,1: limitar antes de codificar); (4) `descricion.txt`:
  decir que 35/162 imágenes no pasaron la puerta (o arreglarlas), ambientes reales y primer capítulo «00:00»; (5) para
  una persona en YouTube Studio: etiqueta de contenido sintético, subir el SRT, miniatura y correo a Nós/USC (D4).
- **Ronda de arreglos en una sesión nueva** (≈ 3,5 h de máquina, casi todo desatendido):
  1. `bash herramientas/pipeline/instalar.sh` y `source herramientas/pipeline/entorno.sh`.
  2. Restaurar la caché de imágenes según `gauntlet3/video/imaxes/LEEME.md` (162 JPEG → PNG + `revision.json` en
     `$SCRATCH/longo/w/imaxes/`) y copiar `gauntlet3/guion/guion-r3.txt` a `$SCRATCH/longo/guion-producion.txt`.
  3. Reescribir en `gauntlet3/video/escenas.json` el prompt de los planos 84, 133, 161, 56, 5, 31, 61, 67, 91, 145 y
     153 (solo esos se regeneran). Evitar lo que cayó: farolas, bombillas y apliques, casas inglesas, maleta.
  4. Pico real ≤ −1 dBTP: bajar el tope de `son.limitar` (0,89 de muestra dio −0,1 dBTP tras AAC; probar 0,80 y
     medir). Descripción: frase de las imágenes con el dato real (35/162 sin pasar la puerta, o 0 si se arreglan),
     lista real de ambientes y primer capítulo «00:00» (`temas/meigas-de-verdade.yaml` y `longo.descricion`).
  5. `setsid nohup herramientas/pipeline/lanzar-longo.sh produccion1 &` con un Monitor armado todo el rato; después
     `entregar.sh` y `paxina_episodio.py`, y republicar la página en la misma URL (desde otra conversación: leerla con
     `action: read` y publicar con `url`).
- **Cómo se produjo:** `herramientas/pipeline/lanzar-longo.sh` (reintentos, memoria, puerta ajustada por variables de
  entorno: `IMG_RESERVAS=0`, `REVISOR_LUME_DURMIR=0.015`), `longo.py --ata-plano N` para avances, `entregar.sh`
  (validar, partir, 720p HLS fMP4) y `paxina_episodio.py` (página). Detalles y tropiezos en `docs/APRENDIZAJES.md`
  (memoria del cgroup 13,36 GiB, reinicios por sesión ociosa, puerta demasiado estricta, sonoridad, tipos de las
  páginas).

**Ideas del promotor para después de este vídeo (D15, D16):**
- **Imágenes de referencia o semilla** para lo que SDXL no conoce (carro de bois, hórreo, pazo, palloza, traje
  tradicional, armaduras, herramientas): biblioteca de referencias con licencia libre o fotos propias, usadas con
  img2img, ControlNet (bordes o profundidad) o IP-Adapter, y la puerta CLIP con el campo `clave` para comprobar que el
  objeto aparece. Búsqueda de la biblioteca: el promotor lanzará un agente barato con el prompt que le pasó Claude.
- **Animación:** en CPU, paralaje 2,5D con un mapa de profundidad (Depth-Anything-V2-Small, Apache-2.0) y
  microanimaciones (lume, vela, lluvia, niebla, agua); personas en movimiento con *image-to-video* en GPU alquilada
  (candidato: Wan 2.2 TI2V-5B, Apache-2.0 [S, verificar]), solo en el gancho, con una puerta de revisión de vídeo.

**Cortes por límite de uso:** el 30-09-2026 a las 16:30 UTC (5 agentes a la vez). Se retomó con `SendMessage` a
cada agente; lo que estaba en git o en disco no se perdió.

## 1. Qué es el proyecto

Un canal de YouTube de vídeos hechos con IA sobre **historia y cultura de Galicia**, pensados para **quedarse dormido**
escuchándolos, **100 % en galego**. El punto de partida fue una conversación con Gemini
(https://share.gemini.google/1zO2a3MXJETr) sobre canales *faceless* de historia hechos con IA. Se tomó solo el
concepto; está resumido en [`plan-de-negocio/00-contexto-y-concepto.md`](../plan-de-negocio/00-contexto-y-concepto.md).

El promotor lo plantea como **hobby con opción de negocio**, motivado por curiosidad, afán emprendedor y ganas de
experimentar con la tecnología. Tiene poco tiempo y no quiere gastar en suscripciones.

## 2. Qué se hizo, en orden

| # | Qué | Resultado | Dónde |
|---|---|---|---|
| 1 | Lectura de la conversación de Gemini | Extraída por su RPC interna, porque la página se carga con JS | `plan-de-negocio/00-contexto-y-concepto.md` |
| 2 | Kit A/B de voces en galego | Página privada con test ciego: 8 parejas humano/sintético y 6 voces de Nós leyendo el guion. Los votos se guardan en la página. **Aún no hay votos** | https://claude.ai/artifact/MTsjYNFmH5WaWYqAEJ7HGH · `herramientas/voz/` |
| 3 | **Gauntlet 1**: plan con garantía humana de calidad | 6 piezas (retornos, formato, guion, voz, pipeline, riesgos) + integración + tribunal de 3 jueces. Tribunal: 1/3 aprueba | `plan-de-negocio/plan-de-negocio.md` (v1, **sustituido**), `tribunal.md`, `gauntlet/` |
| 4 | Decisiones D1-D6 del promotor | Giro a **canal desatendido**: sin revisión humana, open source, en anónimo, como hobby | `plan-de-negocio/decisiones.md` |
| 5 | **Gauntlet 2**: canal desatendido | Referencia (*Historia Desconocida*), 3 piezas (vídeo, plan, ecosistema galego), integración y tribunal | `plan-de-negocio/gauntlet2/`, `plan-de-negocio/plan-v2-desatendido.md` |
| 6 | Pipeline automático de vídeo | De una ficha de tema a MP4 1080p en galego, con QA automática | `herramientas/pipeline/` |
| 7 | Vídeo de ejemplo | Ronda 3: 3:11, 100 % desatendido, QA PUBLICABLE 13/13, pero guion seco y con imágenes no gallegas | `plan-de-negocio/gauntlet2/video/ejemplo.mp4` |

## 3. Estado actual

**Documento vigente:** [`plan-de-negocio/plan-v2-desatendido.md`](../plan-de-negocio/plan-v2-desatendido.md). El
tribunal lo suspendió en sus dos rondas (0/3), aunque en la segunda el operador vio que lo que faltaba era menor.
Veredictos en `plan-de-negocio/gauntlet2/veredictos/tribunal-r1.md` y `tribunal-r2.md`.

**Conclusiones del plan v2:**
- **Nicho:** no hay evidencia suficiente de que exista en galego; lo más probable es que sea marginal (20-1.000
  personas alcanzables el primer año). El tema sí funciona en castellano (lendas de Galicia para dormir: 107.875
  vistas). La opción del plan es **toda Galicia** (lendas, mar, castros, Camino, idiosincrasia), no solo historia.
- **Dinero:** casi seguro pierde un poco (0-25 € de ingresos el primer año frente a 30-150 € de caja y 105-175 h). El
  valor está en lo cultural y en lo técnico.
- **Prueba falsable del nicho:** 8 episodios (4 de historia y 4 de Galicia ampliada) sembrados en 3-5 comunidades
  galegas, en dos pasos: ¿hubo exposición? (≥ 8.000 impresiones o ≥ 150 visitas sembradas) y ¿reacciona el público?
  (se para si fallan 2 de 3: CTR < 2 %, retención a 2 min < 25 %, < 35 % de Galicia). Decide hacia la semana 10.
- **Pistas de audio:** explorar gl (original) + pt + es + en en el mismo vídeo, con una fase de prueba controlada.

**Vídeos de ejemplo:**

| Versión | Guion | Enlace |
|---|---|---|
| Ronda 1 (4:00) | Escrito por Claude a mano dentro del pipeline: **no era desatendido**. Es el que vio el promotor | [descarga](https://github.com/anxodavid/revolta/raw/76793956612eaf4383cfe919017500d613c38131/plan-de-negocio/gauntlet2/video/ejemplo.mp4) |
| Ronda 3 (3:11, vigente) | 100 % desatendido con EuroLLM-9B local; dossier casi literal, seco y repetitivo | `plan-de-negocio/gauntlet2/video/ejemplo.mp4` |

## 4. Decisiones del promotor vigentes

Todas en [`plan-de-negocio/decisiones.md`](../plan-de-negocio/decisiones.md) y en las secciones "PRIORITARIO" de
[`plan-de-negocio/gauntlet2/contexto.md`](../plan-de-negocio/gauntlet2/contexto.md).

- **Canal desatendido**, sin revisión humana pagada, en **anónimo**, como hobby (D5, D6).
- **Guion con un LLM potente por API** (el LLM local no basta); voz, imágenes, montaje y controles, open source y locales.
- **Voz:** la más cercana al listón (hoy StyleTTS2 Brais de Nós). Pedir permiso a Nós/USC y darles crédito (D2, D4).
- **Validación formal de la voz (850-1.500 €)** solo si el canal muestra tracción (D1).
- **Dedicación:** ~6 h/semana mientras se monta y ~1 h/semana después (D3).
- **Temas:** toda Galicia. **Ganchos solo al principio** (título, miniatura, primeros 60-120 s) y después tono de dormir.
  Atractivo audiovisual por encima de la exhaustividad, **sin inventar nada**.
- **Aviso hablado veraz:** "A voz que vas escoitar é sintética, e este texto preparouno un proceso automático". Nunca
  afirmar una revisión humana que no existe.
- **Pistas multilingües** gl + pt + es + en: aprobado explorarlas.

## 5. Próximos pasos

1. **Puerta P-guion** (siguiente paso acordado): regenerar una muestra de 10-15 min con el guion escrito por un LLM
   potente por API y juzgarla con umbrales numéricos: ≥ 90 % de bloques escritos por el LLM, 0 n-gramas repetidos de
   ≥ 4 palabras, 0 avisos de lengua y veracidad, coste acotado, y escucha ciega del promotor frente a la referencia de
   Versalles. **Hace falta una clave de API** para el LLM (no la hay en el entorno). Hasta tenerla, se puede generar
   con Claude haciendo de LLM con los mismos prompts, **declarándolo** en la QA.
2. **Endurecer la puerta de imágenes** (`herramientas/pipeline/revisor.py`): hoy deja pasar cipreses toscanos, carros
   con ruedas de radios, multitudes con caras deformes y fachadas mediterráneas. Añadir una **lista positiva de
   iconografía galega** (granito, lousa, hórreo, carro de rueda maciza) además de los vetos.
3. **Votos del kit A/B:** que el promotor y su mujer hagan la escucha ciega
   (https://claude.ai/artifact/MTsjYNFmH5WaWYqAEJ7HGH) y leerlos con la herramienta de datos del artefacto
   (colección `escoitas`). La clave del test está en el scratchpad de la sesión anterior, que ya no existe: si hace
   falta desciframiento, regenerar el kit.
4. **Correo a Nós/USC** pidiendo permiso para la voz (borrador en galego en `plan-de-negocio/gauntlet2/piezas/ecosistema.md`).
   Incluir en el crédito al Centro Ramón Piñeiro y a la UVigo si se usan voces del corpus CRPIH_UVigo-GL-Voices.
5. Corregir en el plan v2 las carencias del tribunal ronda 2 (`veredictos/tribunal-r2.md`): escenarios de §3.2
   condicionados a los resultados de la prueba, aportaciones a Nós a partir de su inventario real de datasets, etc.
6. **Cómputo para producir:** un episodio de 60 min tardaría ≈ 28,6 h de reloj en la CPU de este entorno (4 núcleos).
   Para producir en serio hace falta GPU (alquilada por horas) o episodios más cortos.
