# Estudio de monetización: "Cousas de Galiza para durmir"

Fecha: 01-10-2026. Lo escribió Claude a petición del promotor, **solo con lo que ya está en el repo** (plan v2,
investigación del Gauntlet 1, Gauntlet 3 con el episodio largo "As meigas de verdade" y la búsqueda de referencias
gráficas de la rama `ccr-17437293-x0i276`). No se hizo investigación nueva: las cifras con fuente remiten al documento
del repo donde está la URL; lo que es estimación va marcado **[S]**. Ninguna persona lo ha revisado.

---

## 0. Resumen

1. **Los anuncios de YouTube no son el modelo del primer año.** Desde el 1-02-2027 un canal nuevo necesita
   **1.000 suscriptores + 8.000 h en 365 días** para entrar en el YPP. En el escenario base del plan v2 el canal haría
   45-400 suscriptores en 12 meses. Ingresos esperados por anuncios el primer año: **≈ 0 €**.
2. **El dinero posible está en otras cinco vías.** Por orden de calendario:
   - premios en galego (Youtubeiras+, inscripción **hasta el 15-11-2026**);
   - audio largo (Spotify Partner Program, que llega a España el **20-10-2026**, e iVoox);
   - encargos públicos (convocatoria digital de la CRTVG, hasta 26.000 € por proyecto, ≈ junio de 2027; ventanilla
     permanente de programas sonoros);
   - Camino de Santiago en el **Xacobeo 2027**;
   - encargos B2B de "historia local para durmir" (concellos, museos, turismo).

   Ninguna de ellas es segura, y casi todas chocan con una decisión vigente (ver punto 4).
3. **Lo que hay que vender es la capacidad, no las vistas.** Producir 31 minutos en galego con fuentes cuesta hoy
   **≈ 16,5 h de CPU y unos pocos euros de caja** (§2). Eso hace viable lo que ninguna productora haría por ese
   precio: series temáticas, historia de un concello concreto, versiones de 2-3 h para dormir. El canal de YouTube es
   el **escaparate** que demuestra esa capacidad.
4. **El anonimato (D6) cierra casi todas las vías de dinero.** Las ayudas exigen un solicitante identificado. La
   CRTVG selecciona personas físicas con nombre. El B2B necesita a alguien que venda y que firme. Si el canal sigue
   anónimo, el techo realista es **premios + audio + fan funding: 0-1.500 € el primer año [S]**. **Esta es la
   decisión principal que le toca al promotor** (§6).
5. **Antes de cobrar nada hay tres bloqueos:**
   - la **voz**: los datos de Brais prohíben la exposición pública sin permiso, así que hace falta el sí de
     Nós/USC o pasar a una voz CC-BY;
   - la **imagen**: el tribunal dice "no publicable tal cual" por 4 planos con objetos modernos;
   - la **política de contenido inauténtico** de YouTube.

   Las referencias gráficas (D15) arreglan parte de la imagen y, bien usadas, también ayudan con la política
   (§3.2).

---

## 1. Qué sabemos ahora que no sabía el plan v2

| Hecho | Dato | Dónde |
|---|---|---|
| Un episodio largo es factible | 31:22, 1080p, 162 planos, WER 0,031, −17,1 LUFS, embudo de voz medido (157 → 114 palabras/min) | `gauntlet3/video/qa.md` |
| Coste de máquina medido | 285,9 min de reloj y **16,55 h de CPU de núcleo** (imágenes 142 min, montaje 67, QA 31, voz 16) | `gauntlet3/video/qa.md` |
| El guion y el gancho ganan a la referencia | Gancho 4/5; zona de dormir más tranquila y veracidad muy superior | `gauntlet3/veredictos/tribunal-final.md` §7 |
| **La imagen pierde** (por poco) | 35/162 planos no pasaron la puerta; 4 planos bloquean (bombilla, farolas, casa colonial, maleta de ruedas); casas inglesas en 9 planos | idem §2 y §7 |
| Nadie lo ha visto ni oído | El sonido gana "por medidas", sin escucha | idem §5 |
| Tema con datos | "Brujas" sube × 2,0 en octubre; Camino: el mejor dato "para dormir" de un tema gallego (**182.373 vistas**, en castellano); 0 vídeos para dormir en galego en ningún tema | `gauntlet3/tema/investigacion.md` |
| Referencias gráficas | **226 candidatas** de licencia libre en 14 conceptos (hórreo, carro de bois, palloza, pazo, cruceiro, cocina, queimada, traje, aperos, muíño, dorna, iconografía, armas, Samos). **La mayoría son CC BY-SA**; ninguna se ha mirado a ojo | rama `ccr-17437293-x0i276`, `docs/referencias-graficas/referencias.md` |
| Generar imágenes fuera es barato | SDXL-Lightning en Replicate ≈ 0,0018 $/imagen; FLUX.1 [schnell] en fal 0,003 $/MP | `docs/APRENDIZAJES.md` |

---

## 2. Coste unitario: lo que hace posible el negocio

| Partida por episodio de ~30 min | Hoy | Con el guion por API e imágenes fuera [S] |
|---|---|---|
| Guion | Claude con agentes (Gauntlet, horas de sesión; no es desatendido, D8) | ≈ 0,5-1 USD (la mitad del episodio de 60 min del plan v2 §3.3) |
| Imágenes (≈ 400 intentos) | 142 min de CPU | ≈ 0,7-1,2 USD fuera; en local, gratis pero lento |
| Voz, sonido, montaje y QA | ≈ 2,3 h de reloj en local | igual |
| **Caja por episodio** | ≈ 0 € más la electricidad | **≈ 1-3 €** |
| Horas del promotor | Revisar, subir, etiquetar y sembrar: 40-100 min (plan v2 §3.4) | igual; **más una escucha entera si se vende** (§3.1) |

Comparación: la garantía humana del plan v1 costaba ≈ 305 € por episodio (`decisiones.md`, D5). Una pieza de
divulgación digital de hasta 50 min la paga la CRTVG a **hasta 20.000-26.000 €** (`gauntlet/investigacion/ingresos_alt.md`
§1.4). **El margen está entre esas dos cifras**: no en las vistas, sino en producir barato lo que otros pagan caro.

---

## 3. Condiciones previas para cobrar cualquier cosa

### 3.1 Bloqueos

| Bloqueo | Por qué importa para el dinero | Salida |
|---|---|---|
| **Voz de Brais** | Los términos del dataset `Nos_Brais-GL` prohíben exponer las grabaciones en público y limitan el uso a investigación. Con *Right to Monetize*, YouTube puede poner anuncios aunque el canal no esté en el YPP: **no existe el uso "no comercial" en YouTube** (plan v2 §7.1) | Enviar ya el correo a Nós/USC (borrador en `gauntlet2/piezas/ecosistema.md`). En paralelo, probar el embudo con una voz CC-BY 4.0 del corpus CRPIH_UVigo (Sabela, Icía, Iago, Paulo). Para el B2B y la CRTVG solo vale una voz con licencia comercial clara |
| **Imagen** | El tribunal no deja publicar así. Para premios y encargos, la imagen es lo primero que se juzga | Ronda de arreglos (≈ 3,5 h de máquina, `docs/HANDOFF.md` §0) y referencias semilla (§3.2) |
| **Contenido inauténtico** (YouTube, desde el 15-07-2025 y aclarado el 13-07-2026) | "Image slideshows and templated storylines" no se monetizan, y se juzga **a nivel de canal**. Probabilidad de que deniegue el YPP: 40-60 % [S] (plan v2 §7.2) | Un **elemento original** por episodio: tesis, fuentes citadas en voz y un documento o foto real en pantalla. Cadencia lenta. Variedad real entre episodios |
| **Escucha humana** | Un encargo pagado, un premio o una emisión no aceptan "nadie lo oyó". D5 vale para el canal, no para un cliente | Para lo que se venda: una escucha entera (≈ 1 h por episodio de 30 min) **declarada**. Para el canal, D5 sigue igual |
| **Etiqueta IA** | YouTube la exige; Spotify exige declarar la narración sintética y prohíbe suplantar voces (`ingresos_alt.md` §3.1) | Al subir: Studio → "AI use: Yes". El aviso hablado ya lo cumple |

### 3.2 Las referencias gráficas: calidad, licencia y "elemento original"

- **Calidad.** Las referencias cubren justo lo que SDXL no sabe dibujar: hórreo, carro de rueda maciza, palloza,
  pazo, lousa y granito. Con ellas como semilla (img2img, ControlNet o IP-Adapter, D15) bajarían las "casas inglesas"
  que cuestan el veredicto. **Falta probarlo:** nadie ha mirado esas imágenes, y Commons limitó las descargas de
  miniaturas.
- **Licencia, el detalle que importa para monetizar.** La mayoría son **CC BY-SA**. Usarlas como semilla hace que la
  imagen generada sea probablemente una obra derivada: exige atribución y, por el *ShareAlike*, compartir esa imagen
  con la misma licencia [S, interpretación no jurídica]. **No impide monetizar** (BY-SA permite el uso comercial),
  pero obliga a acreditar cada semilla en la descripción, y un encargo con cesión de derechos (la CRTVG) podría no
  aceptarlo [S]. Regla propuesta:
  1. Para las semillas, preferir CC0, dominio público o CC BY: Christof46 (hórreo, CC0), The Met (armas, CC0) y
     Doré (traje, 1862).
  2. Las BY-SA, mejor mostrarlas **tal cual** en pantalla, como documento real y con crédito, que transformarlas.
  3. **Fotos propias del promotor** (hórreos, cruceiros, lareiras de su entorno): licencia limpia y, además,
     **elemento original** contra la política de contenido inauténtico.
- **Lo que no cubren** (huecos del informe): queimada limpia, carro de lado sin gente, traje sobre fondo neutro, ropa
  de los siglos XV-XVII. Fuentes a pedir: Museo do Pobo Galego, Galiciana y la Hispanic Society (fotos de Ruth
  Anderson, 1924-26). Pedirlas exige identificarse: otra vez D6.

---

## 4. Vías de ingreso, una por una

Probabilidades e importes **[S]** salvo que se indique fuente. "Año 1" va de oct-2026 a sep-2027.

| # | Vía | Requisito o umbral (fuente) | Encaje | Año 1 [S] | Año 2 [S] | ¿Compatible con anonimato? |
|---|---|---|---|---|---|---|
| A | **Anuncios YouTube (YPP)** | 1.000 subs + 8.000 h/365 días desde el 1-02-2027 (`retornos.md` §1). RPM 1,5-4 € (§2.4) | Bajo: el sueño acumula horas, pero no suscriptores | 0 € | 0-300 € (solo en el optimista, 8-12 %) | Sí |
| B | **Fan funding YouTube** (membresías, Super Thanks) | 500 subs + 3.000 h; 70 % para el creador (`ingresos_alt.md` §3.5) | Medio: público identitario y diáspora | 0 € | 0-200 €/mes en el optimista | Sí |
| C | **Spotify Partner Program** | Desde el 20-10-2026 en España: 3 episodios, **2.000 h y 1.000 oyentes en 30 días** (`ingresos_alt.md` §3.1) | **El mejor encaje estructural**: el formato de dormir es audio, se repite cada noche y el máster ya existe | 0 € (umbral) | 0-60 €/mes | Sí, declarando la IA |
| D | **iVoox** (fans, pago único por packs) | Sin umbral; comisión ¿5 %? sin verificar | Medio: packs "6 h de meigas para durmir" a 3-5 € | 0-50 € | 0-300 € | Sí |
| E | **Premio Youtubeiras+ 2026** | Inscripción del 17-09 al **15-11-2026**; ≥ 3 publicaciones desde el 16-11-2025; categorías Pódcast, Revelación y Calidade lingüística, de 1.000-1.250 € cada una (`ingresos_alt.md` §2.1) | Medio en dinero, **alto como validación externa**. El jurado valora "dotes interpretativos", que penaliza la voz sintética | 0-1.000 € (P(premio) 5-15 %) | idem | Sí (es internacional y sin RETA) |
| F | **Encargo de la CRTVG/CSAG** | Convocatoria digital ≈ junio 2027: divulgación o videopodcast hasta 26.000 €; personas físicas seleccionadas en 2025 (12 proyectos). Ventanilla permanente de programas sonoros (Res. 24-11-2025) | **La única vía que cambia la escala.** Propuesta: una temporada de 6-8 episodios, no el catálogo. Encaje posible con la madrugada de Radio Galega o AGalegaAudio | 0 € (se presenta en el año 1) | 0 o 10.000-26.000 € (P 5-15 %) | **No**: solicitante con nombre y factura |
| G | **Xacobeo 2027** ("O teu Xacobeo", TU300A) | Plazo para actividades de 2027: **1-31-10-2026**; hasta 25.000 € al 60 % para autónomos o pymes, al 80 % para asociaciones (`ingresos_alt.md` §1.5) | Alto en el tema (el Camino es el mejor dato "para dormir"), pero exige RETA o asociación **este mes** | 0 € (no llegamos) | Siguiente convocatoria, si la hay | **No** |
| H | **B2B: "historia do teu concello para durmir"**, audioguías, museos | Contrato menor < 15.000 €; ticket 1.000-6.000 € [S] (`ingresos_alt.md` §6) | Medio-alto si se vende: el coste unitario (§2) permite precios que una productora no puede dar | 0-3.000 € | 3.000-15.000 € | **No** |
| I | **Patrocinio de marcas galegas** (balnearios, editoriales, descanso) | Audiencia de miles por episodio; solo mención al principio | Bajo hasta tener datos | 0 € / canje | 0-500 €/mes | Parcial |
| J | **Más idiomas** (pistas pt/en en el mismo vídeo; castellano aparte) | Pistas: funciones avanzadas (verificación con DNI ante Google, no pública). Castellano: el tema hace 5-108 K vistas | **El mayor mercado**, pero el castellano choca con la tesis pro lingua y está descartado el primer año (plan v2 §4.4) | 0 € | ×1,3-2 sobre A-C si las pistas funcionan | Sí |

**Lectura:**

- **Con anonimato (A-E, I parcial, J):** 0-1.500 € el primer año y 0-3.000 € el segundo, casi todo de un premio y,
  si hay tracción, de membresías.
- **Sin anonimato (+F, G, H):** el valor esperado sube a **≈ 1.500-5.000 € el segundo año [S]**, con una cola
  posible de 10.000-26.000 € si la CRTVG lo selecciona.

En los dos casos el valor esperado es pequeño. **La pregunta real es si el promotor quiere un hobby que se pague solo
o un pequeño negocio de producción con un canal de escaparate.**

---

## 5. Plan propuesto por fases (desde el 01-10-2026)

Cada fase tiene una puerta que decide si se sigue. Los umbrales de nicho son los del plan v2 §2.4, sin tocarlos.

### Fase 0 · Octubre a mediados de noviembre de 2026: "salir bien y a tiempo"

Objetivo: llegar al **15-11 con 3 publicaciones** (requisito de Youtubeiras+) y aprovechar el pico de "brujas" de
octubre.

1. **Esta semana:** ronda de arreglos de "As meigas de verdade" (11 planos, pico real ≤ −1 dBTP, descripción)
   y **escucha entera del promotor** (31 min).
2. **Correo a Nós/USC ya.** Si el 31-10 no han contestado, se publica con una voz CC-BY de reserva (plan v2 §7.1),
   probada antes en el embudo.
3. **Publicación 1:** meigas, en la segunda quincena de octubre, en YouTube y, el mismo día, en Spotify for Creators
   (abre el 20-10) e iVoox. El máster es el mismo.
4. **Publicación 2:** Santa Compaña o Samaín para el 1-2 de noviembre (el pico de la Santa Compaña es × 2,3-3,2).
   Ojo: su público es de terror (`tema/investigacion.md`); el embudo tiene que bajar más deprisa.
5. **Publicación 3:** primer episodio del Camino. Es la apuesta para 2027 y el mejor dato "para dormir".
6. **Probar las referencias semilla (D15)** en los planos más difíciles: hórreo, carro, lousa. Solo con semillas CC0
   o CC BY, o con fotos propias (§3.2).
7. **Inscribir el canal en Youtubeiras+** antes del 15-11 (categorías Revelación y Calidade lingüística), diciendo
   con claridad cómo está hecho.

Puerta 0 (15-11): ¿tres publicaciones sin planos bloqueantes y con una voz con permiso o con licencia CC-BY? Si no,
no hay inscripción y la fase 1 empieza con lo que haya.

### Fase 1 · Noviembre de 2026 a febrero de 2027: la prueba del nicho del plan v2

- 8 episodios en total (los 3 de la fase 0 cuentan), cadencia de 1 por semana y luego 1 cada 2 semanas, sembrados en
  3-5 comunidades galegas.
- **Novedad frente al plan v2: versión larga para el audio.** El mismo episodio más 30-60 min de cola de lluvia (la
  mejora 5 del tribunal). En Spotify y en iVoox las horas son el umbral; en YouTube, la cola sube el AVD.
- Medir CTR, retención a 2 min, % de Galicia, horas por plataforma, suscriptores por cada 1.000 vistas y comentarios.
- Puerta 1 (≈ M0 + 10 semanas): la del plan v2 §2.4 (PARADA, MÍNIMO o PLAN), más un dato nuevo: **¿qué plataforma
  da más horas por episodio?** Lo que salga decide dónde se pone el esfuerzo.

### Fase 2 · Febrero a junio de 2027: solo si la puerta 1 da MÍNIMO o PLAN

- **Serie del Camino para el Xacobeo 2027:** 4-6 episodios con fotos propias o con licencia en pantalla.
- **Pistas pt/en** en 4 episodios con 4 de control (plan v2 §4.4, fase 2).
- Si el promotor levanta el anonimato (§6): **preparar la convocatoria de la CRTVG** (≈ junio de 2027) con un piloto
  de temporada de 6-8 episodios, y una **oferta B2B de un folio** para 3-5 concellos con patrimonio y turismo
  (Combarro, O Cebreiro, Samos, Allariz...): un episodio de su historia para dormir y una audioguía, a precio cerrado.
- Fan funding en cuanto haya 500 suscriptores y 3.000 h.

Puerta 2 (junio de 2027): ¿algún ingreso que no sea un premio, o un sí de la CRTVG? Si no, el canal vuelve al
régimen MÍNIMO (1 episodio al mes) como hobby, y se publican el pipeline y el informe de errores para Nós.

### Fase 3 · Segundo semestre de 2027: escalar lo que funcionó

Solo con datos de la fase 2: patrocinio de temporada, packs de pago en iVoox y, como decisión explícita del promotor,
revisar el castellano a los 12 meses (regla del plan v2: solo si el galego conserva ≥ 40 % del tiempo de visionado).

---

## 6. Decisiones que necesita el promotor

| # | Decisión | Opciones | Lo que cambia |
|---|---|---|---|
| M1 | **Anonimato (revisa D6)** | (a) Seguir en anónimo; (b) seudónimo público con una persona identificable para ayudas y clientes; (c) con nombre | (a) Techo de 0-1.500 € al año [S]. (b)/(c) Abre F, G y H y la petición de fotos a los archivos |
| M2 | Alta en RETA o asociación | No / asociación sin ánimo de lucro / autónomo cuando haya un encargo | Xacobeo y Ministerio piden RETA o asociación; la CRTVG y el B2B, facturar |
| M3 | **Escucha humana de lo que se vende** | Sí, declarada / no | Sin ella, F, H y E son muy improbables. No toca el aviso del canal: solo cambia en los episodios que de verdad se escuchen |
| M4 | Voz | Esperar a Nós / pasar ya a una voz CC-BY | Fija la fecha de la primera publicación |
| M5 | Fotos propias como referencia y como documento | Sí / no | Licencia limpia para las semillas y "elemento original" frente a YouTube |
| M6 | Dónde archivar los másteres (333 MB por episodio) | Disco propio / nube / ninguno | Hace falta para Spotify, iVoox y cualquier cliente |

---

## 7. Riesgos que afectan al dinero

| Riesgo | Prob. [S] | Mitigación |
|---|---|---|
| YouTube deniega el YPP o desmonetiza por "contenido inauténtico" | 40-60 % si se pide | Elemento original por episodio, fotos reales, cadencia lenta. **El plan no depende del YPP** |
| Nós/USC dice que no a la voz | 20-40 % | Voz CC-BY de reserva probada en la fase 0 |
| La comunidad galega reacciona mal a "un canal de IA" | 15-30 % | Transparencia total (aviso hablado y descripción "Como se fai") y fuentes en pantalla. Nunca afirmar una revisión que no existe |
| El nicho no aparece (puerta 1 da PARADA) | 20-30 % (plan v2 §2.4) | Coste hundido acotado; queda el portafolio para F y H si M1 lo permite |
| Licencias de las semillas BY-SA mal resueltas | Bajo si se aplica §3.2 | CC0/CC BY o fotos propias para semillas; las BY-SA, solo tal cual y con crédito |
| Horas del promotor por encima de D3 (~1 h/semana) | Alto en las fases 0 y 2 | La fase 0 son 6 semanas intensas; vender B2B es trabajo de persona, no de máquina |

---

## 8. Qué mirar a los 30, 60 y 90 días

- **30 días (≈ 31-10):** meigas publicado y arreglado; respuesta de Nós; ¿las semillas quitan las casas inglesas en
  los planos de prueba? (sí o no, con una hoja de contactos).
- **60 días (≈ 30-11):** 3 publicaciones e inscripción en Youtubeiras+; primeras cifras de CTR, retención a 2 min y
  horas por plataforma.
- **90 días (≈ 31-12):** decisión M1 tomada; a mitad de la prueba del nicho; si M1 = (b) o (c), borrador de la oferta
  B2B y del piloto para la CRTVG.

---

**Quién hizo qué.** Claude escribió este estudio el 01-10-2026 leyendo los documentos citados. No hay medidas nuevas
ni consultas web nuevas. Las cifras con fuente heredan la fecha de su documento (29-09 a 01-10-2026) y conviene
comprobarlas el día de actuar, sobre todo plazos y bases (Youtubeiras+, Spotify, TU300A, CRTVG).
