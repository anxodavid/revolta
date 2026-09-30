# Plan de negocio v2: *Serán*, canal desatendido de Galicia para durmir

Canal de YouTube de historia, lendas y cultura de Galicia para quedarse dormido, **100 % en galego**, hecho por un
**proceso automático sin revisión humana previa**, publicado **en anónimo** y como **hobby**. Sustituye al plan v1
(`plan-de-negocio.md`, con garantía humana de calidad), que quedó sin efecto tras las decisiones del promotor D1-D6
(`decisiones.md`) y las posteriores del 29 y 30-09-2026 (`gauntlet2/contexto.md`).

- **Versión:** v2 integrada (agente de integración del Gauntlet 2) · 30-09-2026.
- **Idioma:** plan en castellano. Todo lo que ve u oye el público va en galego normativo (RAG-ILG).
- **Piezas de origen:** `gauntlet2/piezas/plan-desatendido.md` (v4), `gauntlet2/piezas/ecosistema.md` (v4),
  `gauntlet2/referencia.md`, el vídeo de ejemplo y su QA (`gauntlet2/video/`), `../herramientas/pipeline/README.md` y los
  11 veredictos de `gauntlet2/veredictos/`. Ninguna pieza ganó su ronda: el Anexo lo cuenta, y este documento corrige
  lo que los últimos críticos señalaron.
- **Convenciones:** [F] dato con fuente (URL al lado o en la pieza citada); [R] reutilizado del Gauntlet 1 o de una
  pieza (allí están las URLs); [P] medida propia en este entorno; [S] supuesto o estimación propia, sin verificar.
  1 USD = 0,87 € [S, el mismo tipo de trabajo del Gauntlet 1].
- **Relojes:** S0 = semana del 30-09-2026. M0 = primera publicación (≈ semana 12-14, §8).

---

## 0. Resumen ejecutivo

**1. ¿Existe el nicho? Veredicto: NO HAY EVIDENCIA SUFICIENTE; lo más probable es que sea MARGINAL** (§2).
- A favor: **0** canales o vídeos para dormir en galego en 10 búsquedas [P]; "Galicia para dormir" funciona **en
  castellano** (Relatos al Oído, lendas de Galicia, **107.875** vistas [P]); el portugués tiene un género "historia para
  dormir" fuerte y **0 vídeos sobre Galicia** [P].
- En contra: solo el **3,59 %** de los mayores de 16 ve audiovisual siempre o sobre todo en galego (IGE, EEF 2023) [R];
  mercado atendible de **2.000-20.000** oyentes [R]; lo que hay de lendas en galego suma **59-1.577** vistas en años [P].
- Alcanzables el primer año sin comunidad previa: **20-1.000 personas distintas** [S]. Mediana esperada a 30 días:
  (a) historia en galego 15-100 vistas; (b) toda Galicia en galego 25-200 (**la opción del plan**); (c) (b) con pistas
  pt/en, 40-400 en total, con el galego en el 25-70 % del tiempo de visionado [S].
- **Prueba falsable** (§2.4): 8 episodios (4 de historia, 4 de lendas/mar/idiosincrasia), sembrados de forma anónima y
  declarada en 3-5 comunidades galegas, decisión a los 30 días del episodio 8. Primero se mira si hubo exposición
  (≥ 8.000 impresiones o ≥ 150 visitas sembradas); si no, es "no concluyente" y se itera (máximo 2 ventanas). Con
  exposición, **el nicho se declara inexistente y se para si fallan 2 de 3 umbrales congelados hoy: CTR < 2 %,
  retención a 2 min < 25 %, < 35 % de Galicia en el tráfico sembrado.**

**2. Retornos esperables: en dinero, el canal casi seguro pierde un poco** (§3). Ingresos esperados a 12 meses ≈
0-25 €; gasto de caja ≈ 30-150 €; ≈ 90-145 h del promotor el primer año. Solo el escenario optimista (8-12 % [S]) se
acerca al YPP. El valor está en lo cultural y en lo técnico: datos de error para Nós, un pipeline libre y horas de
escucha en galego donde hoy no hay nada.

**3. Qué demostró el vídeo de ejemplo** ([`gauntlet2/video/ejemplo.mp4`](gauntlet2/video/ejemplo.mp4), QA en
[`gauntlet2/video/qa.md`](gauntlet2/video/qa.md), hoja de contactos en
[`gauntlet2/video/contactsheet.jpg`](gauntlet2/video/contactsheet.jpg)):
- **Imagen, voz, sonido y montaje dan el pego.** 3 min 11 s, 1080p, voz StyleTTS2 Brais de Nós, WER de la mezcla
  0,037, −17,2 LUFS, subtítulos alineados al 99,7 %, 29 planos revisados por una puerta automática de imágenes (manos,
  anacronismos, multitudes, repeticiones), un solo comando desatendido, veredicto automático PUBLICABLE 13/13 [P]. El
  promotor lo vio y lo juzgó "cerca de algo publicable sin dar vergüenza ajena".
- **El guion con un LLM local no da el pego.** Con EuroLLM-9B en CPU el guion **inventa historia** ("a irmandade
  venceu", cuando fue derrotada en 1469) **y palabras** ("fortaleiras") (ronda 2). Con las puertas de verdad
  bloqueantes (ronda 3), el LLM no consiguió **ni uno** de los 18 párrafos del relato limpio en tres intentos: lo que se
  oye es el dossier casi literal, verdadero pero seco, con repeticiones ("botou abaixo moitas fortalezas" ×5) y un
  gancho sin referente [P, `gauntlet2/video/qa.md`; veredicto `video-r3.md`].
- **Decisión ya tomada por el promotor (30-09-2026):** el guion lo escribe **un LLM potente por API**; voz, imágenes,
  montaje y controles siguen siendo open source y locales, y los controles (veracidad, LanguageTool, ASR) se quedan como
  red de seguridad. Coste del guion por API: **≈ 1-3 USD por episodio de 60 min en el caso central** (0,05-0,15 USD por
  una muestra de 3 min), hasta ≈ 7 USD en el peor caso (§3.3).

**4. Recomendación: construir y hacer la prueba del nicho, con cuatro condiciones que no se negocian.**
1. **Ningún episodio con la voz de Brais sin un sí escrito de Nós/USC** (y, a través de Nós, del locutor). "Sin
   monetizar" no existe en YouTube: la cláusula *Right to Monetize* deja a YouTube poner anuncios en vídeos de canales
   fuera del YPP [F https://support.google.com/youtube/answer/10090902]. Voz de reserva lista: Sabela, Icía o Iago de
   Nós (datos donados, CC-BY 4.0) [F https://zenodo.org/records/8027725] (§6, §7).
2. **Aviso hablado veraz al empezar cada vídeo:** "a voz é sintética e este texto preparouno un proceso automático".
   Nunca afirmar una revisión humana que no existe (§7.3).
3. **Ganchos solo al principio y siempre verdaderos:** título, miniatura y primeros 60-120 s con curiosidad
   verificada contra el dossier; después, bajada al tono de dormir. Las lendas, como lendas (§4).
4. **Parar cuando lo digan los umbrales**, fijados hoy y no retocables (§2.4, §8).

Si la prueba manda parar, el coste hundido es ≈ 70-110 h y < 50 € [S], y queda lo que no depende del nicho: el código
libre y un informe de errores de voz, texto y traducción para el Proxecto Nós (§6).

---

## 1. Qué cambia respecto al plan v1 y por qué

El plan v1 era un canal con **garantía humana de calidad** (≈ 305 € por episodio de revisión lingüística e histórica,
puertas F/F2) que el tribunal final suspendió por coste frente al tamaño del mercado (`tribunal.md`). El promotor
decidió entonces (`decisiones.md`, 29-09-2026) y en los días siguientes (`gauntlet2/contexto.md`):

| # | Decisión del promotor | Qué cambia en el plan |
|---|---|---|
| D5 | No se paga la revisión humana; proceso automático que "dé el pego" | Canal **desatendido**. Los controles automáticos sustituyen a la revisión (§5), con sus puntos ciegos declarados. Desaparecen las puertas F/F2 y el paquete de revisión |
| D6 | Si nadie financia la calidad, hobby en anónimo | Éxito medido en audiencia y datos devueltos, no en ingresos. Seudónimo ante el público, identidad conocida por los socios (§6.3) |
| D1 | Validación formal de la voz (850-1.500 €) solo si el canal muestra tracción | Puerta P3 con KPIs (§8.2). Probabilidad de pagarla en 12 meses ≈ 8-12 % [S] |
| D2 | Si ninguna voz pasa el listón, la más cercana | StyleTTS2 Brais de Nós (mejor en el kit A/B y en ASR) **si Nós dice sí**; si no, la mejor de las voces de reserva (§7.1) |
| D3 | ~6 h/semana mientras se monta; ~1 h/semana después | MVP en ≈ 12-15 semanas; régimen de **1 episodio cada 2 semanas**, porque el dossier de cada episodio pide 25-75 min de persona (§3.4) |
| D4 | Pedir permiso a Nós/USC y darles crédito | El correo a Nós está listo (§6.4). **Endurecido:** sin sí escrito no se publica con Brais (condición 1 del §0) |
| 29-09 | Ritmo más vivo al principio y ganchos "con picante" como la referencia | Fórmula de **embudo**: ganchos solo en título, miniatura y primeros 60-120 s; después el ritmo baja al de dormir (§4.3). Implementado en el pipeline (voz y cortes de plano en embudo) |
| 29-09 | Temas de toda Galicia, no solo historia medieval | Catálogo con mitad historia y mitad lendas, mar, vida cotiá e idiosincrasia (§4.2) |
| 29-09 | Pregunta obligatoria: ¿el nicho existe? | Veredicto, tres nichos y prueba falsable con umbral de parada (§2) |
| 29-09 | Explorar pistas de audio gl + pt + es + en | Fase 2 de la prueba, solo si la fase 1 no manda parar; **pt y en primero, es no el primer año** (§4.4) |
| 30-09 | El guion lo escribe un LLM potente por API | Coste de 1-3 USD por episodio (§3.3); el resto del stack sigue open source y local; comparación pública trimestral con los modelos abiertos en galego (§6.2) |

**Lo que se conserva del v1:** la investigación de audiencia y retornos del Gauntlet 1, la lista de temas vetados,
el aviso de IA, la etiqueta de contenido sintético, la regla de fuentes con licencia abierta y la estrategia de
contactar con el ecosistema de menos a más.

---

## 2. ¿Existe el nicho?

### 2.1 Veredicto

**No hay evidencia suficiente de que exista un público en galego para historia y cultura de Galicia para dormir. Si
existe, lo más probable [S] es que sea marginal: decenas a pocos cientos de oyentes por vídeo.** Lo que sí está
demostrado es que **el tema** existe, en castellano. El plan no necesita que el nicho exista para tener sentido como
hobby (D6), pero sí para justificar horas: por eso la prueba de §2.4 lo decide con umbrales fijados antes de ver los
datos.

| A favor | Cifra | Fuente |
|---|---|---|
| El tema engancha en castellano | Relatos al Oído: **107.875** vistas (lendas de Galicia, 2 h), 17.264 (mosteiro), 13.904 (Compostela), 7.829 (Lugo); Misterios para Dormir Profundo 9.135; El Pergamino Mágico (Santa Compaña) 5.106 | [P `gauntlet2/medidas/nicho/busquedas-yt.txt`] |
| Hueco total en galego | **0** canales o vídeos de historia o lendas para dormir en galego en 10 búsquedas (y 0 en el censo del Gauntlet 1) | [P] [R `gauntlet/investigacion/audiencia.md` §5] |
| Hay público galego de historia en YouTube | Burla Negra 614-12.072 vistas por documental; Orgullo Galego 300-3.200; lendas en galego sin formato para dormir 522-1.577 | [R `gauntlet/investigacion/retornos.md` §4.4] [P] |
| Acepta galego más gente de la que lo prefiere | 28 % mezcla ("máis castelán") además del 3,59 % | [R `audiencia.md` §2.4] |
| El hábito de dormirse con audio es masivo | 48 % de los oyentes de pódcast lo usan para dormirse (Acast 2023) | [R `audiencia.md` §6.2] |
| **En contra** | | |
| Consumo audiovisual en galego mínimo | **3,59 %** de los mayores de 16 que ven audiovisual lo ven siempre o sobre todo en galego; 68,1 % siempre en castellano (IGE, EEF 2023) ≈ 60.000-84.000 personas [S sobre ≈ 2,34 M] | [R `audiencia.md` §2.4] |
| Mercado atendible pequeño | **2.000-20.000** oyentes habituales posibles | [R `audiencia.md` §8] |
| "0 competidores" también es mala señal | La búsqueda no distingue entre hueco y desierto | [S] |
| El galegofalante habitual encaja mal con YouTube | Mayor, rural, del interior; el uso de YouTube cae a partir de los 65 | [R `audiencia.md` §2.3 y §3] |
| Lo que hay en galego hace poco | Lendas en galego: 59-1.577 vistas **acumuladas en años**; serie de la TVG, 0,7-4 K por capítulo | [P] [R] |
| La demanda en castellano no se traslada | Quien busca "Galicia para dormir" ya lo tiene en castellano, con mejor voz | [R] [S] |

Embudo [S sobre R]: ≈ 2,34 M mayores de 16 → 3,59 % en galego ≈ 60-84 K → interesados en historia/cultura, en YouTube
y con hábito de audio para dormir: 2.000-20.000 → alcanzables el primer año sin comunidad ni prensa (1-5 %):
**20-1.000 personas**.

### 2.2 El listón de referencia es un pico, no la media

*Historia Desconocida* (la referencia de estilo, [F https://www.youtube.com/@HistoriaDesconocida-m4j]): 5.050
suscriptores, 21 vídeos, ≈ 1,0 M de vistas, pero el **67 %** viene de 3 vídeos de la semana del 20-22 de abril de 2026;
sus vídeos de agosto-septiembre hacen **1.300-6.400** vistas [F `gauntlet2/referencia.md`, yt-dlp 29-09-2026]. Un
canal equivalente en galego, sin comunidad previa, debería esperar decenas a pocos cientos de vistas por vídeo, salvo
empuje externo [S].

### 2.3 Tres nichos, estimados por separado [S]

| Nicho | Audiencia atendible | Competencia directa | Vistas por vídeo a 30 días (mediana) | Subs a 12 meses | P(no PARADA en §2.4) | P(mediana ≥ 150) | Veredicto |
|---|---|---|---|---|---|---|---|
| **(a) Historia de Galicia para dormir, en galego** (castros, suevos, Camiño, mosteiros, irmandiños) | 1.000-10.000 | 0 en galego; indirecta: divulgación en galego sin formato de dormir | **15-100** | 10-150 | 35-50 % | 5-10 % | Sin evidencia suficiente; probable marginal |
| **(b) Toda Galicia para dormir, en galego** (lendas, mar, castros, Camiño, vida cotiá, idiosincrasia) | 2.000-30.000 | 0 en galego; indirecta: Relatos al Oído y 2-3 canales en castellano | **25-200** | 15-300 | 55-70 % | 15-25 % | Sin evidencia suficiente; probable marginal, algo mayor que (a). **Opción del plan** |
| **(c) (b) + pistas pt/en (es, condicionada)** en el mismo vídeo | Teórica: cientos de millones; real: la fracción que acepta una voz open source peor que la de los competidores | pt: género fuerte, 0 vídeos de Galicia; es: Galicia ya cubierta (5-108 K); en: saturado | **40-400 en total**; el galego conserva el 25-70 % del tiempo | 20-500 | P(las pistas suben ≥ 30 % las vistas): 40-55 % | 20-30 % | El tema existe en es y hay hueco en pt; que nuestras voces lo capten: sin evidencia |

Por qué (b) puntúa más que (a): el único vídeo de "Galicia para dormir" con más de 100 K vistas es de **lendas**, y
las lendas son lo único con vistas en galego fuera de los canales con comunidad [P]. Por qué no mucho más: el público en
galego sigue siendo el mismo embudo de 2-20 K.

### 2.4 Prueba falsable con el pipeline automático

**Qué se publica.** Los 8 episodios del stock inicial: **4 de historia (a) y 4 de Galicia ampliada (b)**,
alternados, misma duración (60 min narrados + 20-30 de cola de ambiente) y misma receta de embudo. Solo galego. 3 la
primera semana y 1 por semana después.

**Siembra mínima, anónima y declarada.** Cada episodio se enlaza **una vez** en **3-5 comunidades galegas** fijadas
antes de M0 y siempre las mismas (candidatas [S, verificar que existen y admiten autopromoción]: r/Galicia, r/galego,
#galego y #Galiza en Mastodon y Bluesky, un grupo de Telegram o Discord de lingua o historia). Con la cuenta seudónima
del canal, diciendo en el mensaje que es una canle propia hecha con IA. Nunca cuentas falsas, votos propios ni mensajes
que finjan ser un oyente. El pipeline genera `sementeira.txt`; el promotor lo pega: 10-15 min por episodio.

**Métricas (Studio, a los 30 días de cada vídeo)** [F sobre impresiones y CTR: https://support.google.com/youtube/answer/7628154?hl=en]:
I = impresiones (suma de los 8; no incluyen webs externas); CTR de impresiones; S = visitas sembradas (fuente
"Externa" desde los dominios sembrados); F = % de vistas por fuente (diagnóstico); R2 = retención a 2 min (después del
minuto 2 la curva mide el sueño, no el interés); Gs = % de Galicia en el tráfico sembrado [S: verificar que Studio
cruza fuente y geografía; si no, G sobre todas las vistas]; M, Ma, Mb = medianas de vistas de los 8, de los 4 de
historia y de los 4 de Galicia ampliada.

**Decisión el día 30 del episodio 8 (≈ M0 + 10 semanas). Umbrales congelados el 30-09-2026 [S]:**

| Paso | Condición | Acción |
|---|---|---|
| **1. ¿Hubo exposición?** | I ≥ 8.000 **o** S ≥ 150 | Sí → paso 2 |
| | I < 8.000 **y** S < 150 | **NO CONCLUYENTE:** no se juzga el nicho. Ventana de 30 días: títulos y miniaturas nuevos (A/B de Studio, si las funciones avanzadas están activas, §7.1), 2 comunidades más, 1 episodio nuevo. Máximo 2 ventanas (≈ M0 + 18 semanas) |
| | Sin exposición tras 2 ventanas | **PARADA POR DISTRIBUCIÓN**, que no es "nicho inexistente": este canal anónimo no llega a su público con 1 h/semana. Única salida: un socio con público (medio, asociación, pódcast galego) |
| **2. ¿Reacciona el público?** | Fallan **2 o 3** de {CTR < 2 %, R2 < 25 %, Gs < 35 %} (el CTR no cuenta si I < 8.000 y la exposición viene solo de la siembra) | **PARADA · nicho inexistente para este formato.** Se publican el código y el informe de errores para Nós |
| | Fallan 0-1 y M < 150 | **MÍNIMO:** 1 episodio al mes con el bloque ganador; en M0 + 6 meses se repiten los dos pasos sobre los 4 últimos (exposición: I ≥ 4.000 o S ≥ 75), con PARADA también si M < 40 |
| | Fallan 0-1 y M ≥ 150 | **PLAN:** 1 episodio cada 2 semanas y puerta P2 (§8) |
| Reparto del catálogo | Mb/Ma ≥ 1,5 → 75 % Galicia ampliada; ≤ 0,67 → 75 % historia; si no, 50/50 | |

Por qué esos umbrales [S]: un CTR < 2 % está por debajo de la franja 2-10 % en que están la mitad de los vídeos
[F, URL de arriba]; perder 3 de cada 4 en el minuto 2 dice que el gancho no interesa; si ni un tercio de quien entra
desde comunidades galegas es de Galicia, el galego no encuentra su público ni llevándolo de la mano. Hay que fallar
**dos** de tres para que una miniatura mala no declare muerto el nicho. El suelo de M < 40 en el modo mínimo equivale a
menos de dos personas durmiéndose con el canal cada noche [S].

Probabilidades [S]: NO CONCLUYENTE en la primera decisión 35-50 %; al final, PARADA POR DISTRIBUCIÓN 10-15 %, PARADA
por nicho inexistente 20-30 %, MÍNIMO 40-50 %, PLAN 10-20 %.

**Añadido del ecosistema:** se cuenta también el número de errores de lengua confirmados que llegan al informe para
Nós. Si a la decisión es 0 y M < 150, la tesis *pro lingua* no se usa como argumento público (§6.2).

Ruido declarado: 8 vídeos; el reparto Ma/Mb con 4 contra 4 es orientativo; la siembra sesga el tráfico hacia el público
más galego y militante, por eso Gs prueba que el público existe, no su tamaño.

---

## 3. Retornos y costes

### 3.1 Comparables (29-09-2026)

| Canal | Idioma | Vistas por vídeo | Lectura | Fuente |
|---|---|---|---|---|
| Historia Desconocida (referencia) | es (títulos traducidos a en) | Mediana ≈ 21.000; picos de 167-331 K en abril; **1.300-6.400** en ago-sep | Éxito de ráfaga inicial; lo reciente son miles | [F `gauntlet2/referencia.md`] |
| Sleepless Historian / History Before Sleep / Boring History Bites | en, IA, sleep | 8-31 K / 1,2-48 K / **128-1.500** | La ola de 2025 ya pasó; quien llegó tarde hace cientos | [R `retornos.md` §4.1] |
| El Historiador Nocturno | es, sleep | 10-73 K | Líder en castellano | [R] |
| Burla Negra ("Historias da Galiza") | **gl**, documental humano | 614-12.072 en 4 años | El mejor comparable de mercado en galego | [R `retornos.md` §4.4] |
| Relatos al Oído, lendas de Galicia | es, sleep | 107.875 | Demanda de Galicia para dormir, en castellano | [P] |
| Histórias Chatas Para Dormir / Descanse com Histórias | pt-BR, IA, sleep | 214-440 K | El género existe en pt; 0 vídeos de Galicia | [P] |

Los casos de ingresos altos (redes de canales IA en inglés, 40-60 K$/mes; el informe Kapwing de 278 canales *slop*)
son en inglés, con RPM de primer nivel y de la ola de 2025 [R `retornos.md` §5]: no son comparables.

### 3.2 Escenarios a 12 meses desde M0 (≈ 30 episodios, catálogo ampliado) [S]

Supuestos: nicho (b), mitad historia y mitad Galicia ampliada; AVD 15-25 min; conversión a suscriptor 1-1,5 %; RPM
1,5-4 € solo dentro del YPP [R `retornos.md` §2.4]. Umbral del YPP para nuevos solicitantes desde el 1-02-2027:
**8.000 horas de visionado cualificadas en 365 días** (o 20 M de vistas de Shorts en 90 días) [F
https://blog.youtube/news-and-events/youtube-partner-program-updates-2027-new-opportunities-earn/]; esa entrada no
menciona suscriptores, así que **el requisito de 1.000 suscriptores es un supuesto [S]** (el vigente hoy). Fan funding:
500 subs + 3.000 h [F https://www.youtube.com/creators/earn/youtube-partner-program/].

| Escenario | Prob. [S] | Resultado de §2.4 | Mediana a 30 días | Vistas en 12 meses | Subs a M12 | Ingresos |
|---|---|---|---|---|---|---|
| **Pesimista:** el nicho no aparece, o YouTube lo trata como *slop* | 50-60 % | PARADA o MÍNIMO bajo | 15-100 | 0,2-4,5 K | 2-70 | 0 € |
| **Base:** hueco en galego + las lendas atraen + algún eco en redes galegas | 30-38 % | MÍNIMO o PLAN | 100-600 | 4,5-27 K | 45-400 | 0 € |
| **Optimista:** "a primeira canle para durmir en galego" sale en prensa o un vídeo de lendas se dispara | 8-12 % | PLAN | 600-4.000 | 27-180 K | 270-2.700 | 0-300 € en el año, **si la revisión del YPP no lo rechaza** (§7.1) |
| *Suplemento multi-audio (c), solo si la fase 2 da R ≥ 1,3* | 40-55 %, condicionado | — | ×1,3-2 | ×1,3-2 | ×1,3-2 | Casi igual: RPM de pt-BR bajo [S] |

**Valor esperado de ingresos en 12 meses ≈ 0-25 € [S]. Resultado esperado en caja ≈ −30 a −150 €**, más ≈ 90-145 h
del promotor el primer año natural (§3.4). Es un hobby con coste, como decidió el promotor (D6).

Qué no entra en el modelo: ayudas y premios en galego (casi todas exigen solicitante identificado, y el canal es
anónimo) [R `retornos.md` §7]; un canal espejo en castellano (descartado: partiría vistas y contradice la tesis pro
lingua); Spotify Partner Program (fuera de alcance salvo en el optimista) [R].

**Retorno no monetario** (lo que justifica el hobby): informe de errores de voz para Nós en narración larga; pares
"galego da máquina → galego corrixido" de la audiencia; un banco de preguntas de historia de Galicia con fuente (Nós
no tiene ninguno entre sus 63 conjuntos en Hugging Face [P https://huggingface.co/api/datasets?author=proxectonos]);
el pipeline libre; horas de escucha en galego (§6.2).

### 3.3 Costes por episodio y por mes

**Coste del guion por API (nuevo, decisión del 30-09-2026).** Precios por millón de tokens (MTok), API de primera
parte de Anthropic [F https://platform.claude.com/docs/en/about-claude/pricing.md; tabla de la documentación del SDK
con fecha 25-09-2026; comprobar el día de contratar]:

| Modelo | Entrada $/MTok | Salida $/MTok | Nota |
|---|---|---|---|
| Claude Opus 5.5 | 4,00 | 20,00 | Lecturas de caché 0,20 $/MTok |
| Claude Sonnet 5.5 | 2,00 | 10,00 | Lecturas de caché 0,20 $/MTok |
| Claude Haiku 4.5 | 1,00 | 5,00 | |
| API de lotes (*Batch*) | −50 % | −50 % | El pipeline trabaja de noche: no necesita respuesta inmediata |

Volumen de un episodio de 60 min narrados [S, sobre medidas P]: 7.400-8.600 palabras de guion (124-143 palabras/min
medidas en la voz); ≈ 1,6-2 tokens por palabra en galego [S, sin medir: el tokenizador está pensado para lenguas
grandes]. El pipeline escribe **por bloques** (un gancho, un resumen y un párrafo por hecho del dossier: 80-140
llamadas), con hasta 3 reintentos por bloque, y además pide ≈ 290 descripciones de plano en ≈ 30 llamadas.

| Partida | Entrada | Salida (incluye razonamiento del modelo) |
|---|---|---|
| Guion por bloques (100-140 llamadas × 3-5 K tokens de prompt y dossier; ×1,5 por reintentos) | 0,5-1,0 M | 0,1-0,2 M |
| Planos de imagen (≈ 30 llamadas) | 0,1-0,15 M | 0,05-0,08 M |
| Corrección de párrafos con avisos de LanguageTool | 0,05 M | 0,02 M |
| **Total por episodio** | **≈ 0,65-1,2 M** | **≈ 0,17-0,3 M** |

| Configuración | Coste por episodio de 60 min [S] |
|---|---|
| Opus 5.5, sin caché ni lotes (peor caso) | ≈ 6-11 USD |
| Opus 5.5 con caché del prompt fijo y del dossier + lotes | ≈ 2-3,5 USD |
| **Sonnet 5.5 con caché + lotes (caso central recomendado para empezar)** | **≈ 1-1,7 USD (≈ 0,9-1,5 €)** |
| Muestra de 3 min como la del ejemplo (≈ 20 llamadas) | ≈ 0,05-0,15 USD |

Las "céntimas por episodio" de la decisión valen para la muestra de 3 min; para un episodio de 60 min son de 1 a 3 USD
en el caso central. Qué modelo se usa se decide en la semana 2 con la muestra regenerada (§9): el más barato que pase
las puertas con menos reintentos, midiendo el coste real por episodio completo (no por llamada).

**Caja mensual (2 episodios al mes en régimen, hasta 4-5 en el arranque) [S sobre F/R]:**

| Partida | €/mes | Nota |
|---|---|---|
| Guion por API | 2-6 € (hasta ≈ 20 € en el arranque con Opus sin optimizar) | Tabla de arriba |
| Pistas pt/en (solo en la fase 2) | +0,5-2 € | Traducción gl→pt con el mismo LLM (Nós no tiene ese par); gl→en con Nós MT en local (MIT) |
| Electricidad de la CPU propia | 0,5-2 € | 2 episodios × 8-14 h × 60-100 W × 0,15-0,25 €/kWh [S] |
| Servidor alquilado (solo si el PC no puede quedarse encendido) | 0 € por defecto / 10-30 € | [S, precio sin verificar] |
| Música y ambiente | 0 € | Lluvia sintetizada por código; nada con Content ID |
| Validación de voz (D1) | 0 € | Solo tras P3: 850-1.500 € una vez |
| **Total** | **≈ 3-10 €/mes** | Frente a ≈ 305 € por episodio de la garantía humana del v1 |

**Tiempo de máquina por episodio (60 + 30 min) en la CPU de 4 núcleos [S sobre P].** Medido en la ronda 3 (3 min 11 s:
91 min de reloj, 5,17 h de CPU, de ellas 2,29 h del LLM local) [P `gauntlet2/video/qa.md`]. La extrapolación lineal a 60
min con el LLM local da **≈ 28,6 h de reloj**: con el guion en local, un episodio largo no cabe en una noche. Con el
guion y los planos por API desaparecen las etapas 1 y 4 del cálculo (≈ 15 h). Queda:

| Etapa (local) | Min de reloj para 60 + 30 min |
|---|---|
| Voz (StyleTTS2 Brais) | 20-70 (la ronda 3 midió RTF 0,31; la ronda 2, 0,76-1,15 con carga) |
| Imágenes (SDXL-Turbo + puerta de revisión y regeneraciones, ≈ 73 s por plano medidos) | 350-660 (≈ 290-320 planos con planos de hasta 12,5 s; la cifra alta es la extrapolación lineal) |
| Montaje, sonido y QA | 120-170 |
| **Total** | **≈ 8-15 h: una noche larga o dos** |

La máquina no es el límite a 1 episodio cada 2 semanas. La puerta P0-a pasa a ser "≤ 16 h sin intervención" (antes ≤ 8 h,
con una cifra de 5-7 h que no contaba la puerta de imágenes).

### 3.4 Horas del promotor (D3)

**Construcción del MVP (≈ 70-95 h a ~6 h/semana ≈ 12-15 semanas) [S]:** lo de la pieza del plan (57-85 h: orquestador y
reanudación, guion por capítulos y embudo, cinturón lingüístico, H2, QA de audio por párrafo, montaje por tramos,
canarios, piloto de 60 min, `dossier.py` con PDF, stock de 8 dossieres) **más** lo que añadieron las rondas del vídeo y
la decisión del 30-09: backend de API en `llm.py` con caché y lotes (3-5 h), puerta de coherencia narrativa (sin
n-gramas repetidos de ≥ 4 palabras, referentes introducidos antes de usarse, orden cronológico) (3-5 h), prueba de las
voces de reserva en 60 min (2-3 h) y página "Como se fai *Serán*" con la política de ganchos (2 h).

**Régimen estable:**

| Cadencia | Min/semana | ¿Cumple D3? |
|---|---|---|
| 1/semana con dossier del stock y siembra (8 primeros episodios) | 40-70 | Sí |
| 1/semana con dossier nuevo | 55-130 | **No** |
| **1 cada 2 semanas con dossier nuevo** (régimen tras el stock) | **40-90 (centro ≈ 62)** | Sí en el centro |
| 1 cada 2 semanas reutilizando dossier en series de 2 episodios | 36-75 | Sí |

Tareas fijas: semáforo de controles (5 min), comentarios y erratas (10-20, con tope), mantenimiento (10-15). Por
episodio: pasar a público (5-10; la API de YouTube deja en privado lo que suben proyectos no auditados [F
https://developers.google.com/youtube/v3/docs/videos/insert]), **dossier 25-75 min** (elegir 8-12 fuentes y leer el
informe de `dossier.py`; medido en volumen con Samos: 45 hechos, 2 fuera por conflicto de fuentes 1835/1836 [P
`../herramientas/pipeline/dossier/samos/`]) y siembra (10-15 en la fase 1). **Regla:** el promotor apunta sus minutos;
si la media de 4 semanas pasa de 70, series de 2 episodios, luego 1 cada 3 semanas, luego pausa. Nunca más horas.
**Condición de P0:** el promotor cronometra los 3 primeros dossieres.

---

## 4. Producto

### 4.1 La referencia y qué tomamos

*Historia Desconocida*, "Versalles en 1682: Lujo por fuera, suciedad por dentro" [F https://youtu.be/_lnOveSTjWA]:
36 min, 167.509 vistas, fotogramas fijos fotorrealistas de época generados con IA, un cambio de imagen cada ≤ 10 s,
narración sintética continua a ≈ 137 palabras/min, miniatura sin texto que resume la tesis del título, descripción vacía
y sin fuentes, anacronismos evidentes [F `gauntlet2/referencia.md`].

| Tomamos | Cambiamos |
|---|---|
| Imágenes IA de época, estilo evocativo | Una paleta única por episodio y sin multitudes (la puerta las veta); personajes de espaldas o en grupo pequeño, nunca caras de personas reales |
| Cambio de imagen cada 5-6 s en el gancho | Planos que se alargan hasta 12,5 s en la parte de dormir, con Ken Burns lento y fundidos de 1,2 s |
| Narración continua | 60 min narrados + 20-30 de cola; ritmo en embudo (≈ 140 palabras/min en el gancho, bajando) |
| El gancho de contraste y curiosidad | **Solo al principio** y siempre verdadero y anclado al dossier (§4.3) |
| Sin texto en pantalla | Subtítulos galegos en pista aparte (el guion, no los automáticos) |
| — | Descripción con fuentes, crédito a Nós, aviso de IA y erratas públicas |

### 4.2 Temas de toda Galicia (catálogo cerrado del primer año) [S]

Prioridad: enganchar y ser atractivo, **sin perder rigor**: nada falso ni inventado, lo legendario como leyenda, lo
dudoso se dice o se omite. Mitad historia (a), mitad Galicia ampliada (b); la prueba de §2.4 decide el reparto.

| Bloque | Series del primer año | Gancho verdadero del primer minuto (tipo de dato) | Cuidado específico |
|---|---|---|---|
| **Historia** (a) | Castros e *Gallaecia* romana; o reino suevo; o Camiño e Compostela medieval; mosteiros (Samos, Oseira, Sobrado); os irmandiños | Detalle cotidiano sorprendente y documentado (qué comía un peregrino, cómo se dormía en un hospital de peregrinos) | Consenso historiográfico; conflictos entre fuentes fuera del dossier o dichos como tales (p. ej. 183 o 204 testigos en el preito Tabera-Fonseca) |
| **Lendas e mitos** (b) | A Santa Compaña; meigas, bruxas e menciñeiros; mouras e tesouros dos castros; cidades asolagadas | Lo que **se contaba**, dónde y por qué (la lenda como historia de las mentalidades) | Siempre como lenda; ningún remedio de menciñeiro presentado como útil |
| **O mar** (b) | Costa da Morte (naufraxios, faros, a lenda dos raqueiros), salga e conserva, baleeiros, redeiras e mariscadoras | Contraste entre la lenda y lo documentado | Distinguir lenda y hecho en la misma frase |
| **Vida cotiá de antes** (b) | Feiras, muíños, fiadeiros e seráns, o inverno na aldea | "Así se pasaba unha noite de inverno" | Solo costumbres con fuente; nada de nostalgia inventada |
| **Idiosincrasia: o porqué** (b) | Minifundio (herdanzas e foros), emigración a América (indianos), retranca e morriña | "Por que Galicia está partida en millóns de leiras" | Explicaciones **atribuidas**, nunca esencias; nada de "carácter celta" |

**Vetado:** Guerra Civil y represión, franquismo, política desde 1975, personas vivas, conflictos lingüísticos
actuales, salud (incluidos remedios como útiles), celtismo como hecho.

### 4.3 Embudo: ganchos solo al principio

- **Título, miniatura y primeros 60-120 s:** ganchos claros y ritmo vivo (planos de ≈ 5,5 s, escala de voz 1,05, pausas
  de 0,55 s). **Después:** el ritmo y la intensidad bajan poco a poco (planos hasta 12,5 s, escala 1,25, pausas hasta
  1,35 s) hasta el tono de dormir, con curiosidades tranquilas y sin sobresaltos. Ya implementado en el pipeline
  (etapas 3 y 4, `../herramientas/pipeline/README.md`); en la muestra: 11 planos en el primer minuto, 139,5 palabras/min
  en el gancho frente a 131,5 de media [P].
- **Reglas de ganchos** (de `gauntlet2/piezas/ecosistema.md` §1.13, que pasan a ser controles):
  1. Solo ganchos con fuente: cada afirmación del título, la miniatura y los primeros 120 s va en `afirmacions.csv`
     como `gancho`, **100 % anclada** y aprobada por la puerta de veracidad; si no pasa, se usa el siguiente candidato
     o uno suave. El título y el texto de miniatura salen de filas `gancho` del guion, no se escriben aparte.
  2. ASR sobre el 100 % de las frases de los primeros 120 s.
  3. El contraste apunta **hacia arriba** (nobleza, alto clero, poder) o **hacia la sorpresa** (lo cotidiano que hoy
     parece raro), **nunca hacia abajo** (labregos, mariñeiras, emigrantes como objeto de burla o asco). Nada de
     "que noxo", "que atrasados", conspiraciones ni "o que che ocultaron".
  4. Galego natural, no calcos: "non vas crer" (no "non vas a crer"), "segredos" (no "secretos"); el control de
     lengua se aplica también al título y a la miniatura.
  5. Una leyenda nunca "existiu" ni "pasou": "Durante séculos, en Galicia houbo quen xuraba ter visto a Santa
     Compaña" sí; "A Santa Compaña existe" no.
- **Ejemplos permitidos** (si el dossier sostiene cada dato): *Non vas crer como se alumeaban as casas antes da luz
  eléctrica*; *Pedra nobre por fóra, fume e frío por dentro: así eran os pazos*; *A Santa Compaña: o que se contaba nas
  aldeas e por que*; *Por que emigraron tantos galegos?* **Vetados:** *Que noxo! Así vivían os galegos de antes*; *A
  Galicia máis miserable*; *A Santa Compaña existe: as probas*; *A historia que che ocultaron no colexio*.
- La lista y las reglas se publican como **política de ganchos** en la página "Como se fai *Serán*". Tensión aceptada:
  los ganchos dignos rinden algo menos en CTR que los crudos [S]; en un nicho diminuto, una polémica cuesta más.

### 4.4 Pistas de audio multilingües (explorar, no aprobado como régimen)

**Cómo funciona en YouTube.** Desde el 10-09-2025, los creadores con *funciones avanzadas* pueden añadir pistas de audio
en otros idiomas a un vídeo [F https://techcrunch.com/2025/09/10/youtubes-multi-language-audio-feature-for-dubbing-videos-rolls-out-to-all-creators/];
vistas y horas se suman en el mismo vídeo [F https://ppc.land/youtube-makes-multi-language-audio-available-to-millions-of-creators/];
**la pista por defecto la decide el historial del espectador**, no el creador [F
https://support.google.com/youtube/answer/13338784?hl=en]. Consecuencia: un gallego que ve YouTube en castellano oiría
por defecto una pista en castellano si existe. **Sin verificar [S]:** que el galego sea un idioma admitido como pista y
como idioma original del vídeo (se comprueba en Studio en la semana 1; si no lo es, el nicho (c) se descarta).

**Coste y calidad medidos** [P `gauntlet2/medidas/nicho/`]: traducción gl→es con Nós `Nos_MT-CT2-gl-es` (MIT): 126
palabras en 1,7 s, 9/11 frases bien, 2 errores ("acomódate" → "acuérdate", "Rocha Forte" → "Roca Forte"); gl→pt, con el
mismo LLM del guion (Nós no tiene ese par); voces Kokoro-82M (Apache-2.0, pt-BR/en/es, RTF 1,2-1,45 con CPU cargada) o
Piper (pt-PT/es, RTF 0,13-0,14, voz de asistente; licencia de la voz base *lessac* por revisar). Por idioma: 30-45 min
de CPU con Piper, 90-130 con Kokoro, en una segunda noche. Las voces son claramente peores que las de los competidores en
pt/es/en [S, sin escucha ciega].

**Control automático de la traducción (M1-M6):** ida y vuelta al galego frase a frase; nombres propios bloqueados; cifras
y fechas iguales; encaje en el tiempo (±1 % de la duración); ASR de la pista (WER ≤ 8 %); marcadores de lenda y
préstamos (retranca, morriña, meiga) conservados. Una pista que no pasa no sale; el vídeo en galego sale igual.

**Reglas (la versión más estricta de las dos piezas, por la tesis pro lingua, §6):**
1. El galego es siempre la pista original y el idioma declarado del vídeo; si Studio no lo admite, no hay pistas.
2. Título, miniatura y descripción principal en galego; metadatos traducidos solo a pt y en.
3. **Fase 2: solo pt y en**, en 4 de los 8 episodios de la prueba con los otros 4 de control (≈ M0 + 12-17 semanas,
   solo si la fase 1 no da PARADA, Nós ya respondió sobre la voz y no hay alarmas abiertas). Decisión: R = vistas con
   pistas / vistas de control; L = % del tiempo de visionado en galego. R < 1,3 → solo galego; R ≥ 1,3 y L ≥ 25 % →
   pt + en en los nuevos; L < 25 % → solo pt.
4. **Castellano: ninguna pista el primer año.** Es la pista que desplaza al galego entre los propios gallegos, el mercado
   donde competimos con peor voz, y la que haría insostenible la tesis pro lingua ante A Mesa y la sociolingüística.
   Revisión a los 12 meses solo con L ≥ 40 %, sin alarmas abiertas y decisión explícita del promotor.
5. **La voz de Brais, ni ninguna voz de actor de dobraxe, nunca se usa ni se clona en las pistas traducidas.** Voces con
   origen documentado o no se usan.
6. Cada pista abre con una frase fija y neutral en lo normativo: pt *"Este vídeo foi feito originalmente em galego, a
   língua da Galiza. Pode ouvi-lo em galego mudando a faixa de áudio."*; en *"This video was originally made in
   Galician, the language of Galicia. You can listen to it in Galician by switching the audio track."*
7. Cada pista dice en su lengua que la traducción y la voz son automáticas y sin revisión humana. Nunca "dobraxe".
8. **Requisito:** funciones avanzadas del canal activas (§7.1); sin ellas no hay pistas.

---

## 5. Pipeline automático y controles

### 5.1 Qué existe hoy y dónde verlo

Código: `../herramientas/pipeline/` (README con la historia honesta de las tres rondas). Un solo comando de una ficha
de tema (YAML con dossier) a un MP4 1920x1080 con informe de QA. **Muestra actual:**
[`gauntlet2/video/ejemplo.mp4`](gauntlet2/video/ejemplo.mp4) · QA automático:
[`gauntlet2/video/qa.md`](gauntlet2/video/qa.md) · hoja de contactos 4x3 a 960x540:
[`gauntlet2/video/contactsheet.jpg`](gauntlet2/video/contactsheet.jpg) · rondas anteriores archivadas en
`gauntlet2/video/ronda1/` y `ronda2/` · comparación de guiones Claude frente a EuroLLM en
`gauntlet2/video/ronda2/comparacion-llm.md`.

| # | Etapa | Software (licencia) | Estado |
|---|---|---|---|
| 0 | Dossier: el promotor elige fuentes; `dossier.py` descarga, extrae hechos con cita literal, comprueba cada cita y aparta conflictos y leyendas | Código propio; LLM para extraer | Probado con Samos; falta PDF y conexión directa con `pipeline.py` |
| 1 | Guion por bloques (gancho, resumen, un párrafo por hecho), con validación y hasta 3 intentos por bloque | **Pasa a LLM por API** (hoy EuroLLM-9B local, Apache-2.0) | Backend de API por hacer (semana 1-2) |
| 2 | Corrección: LanguageTool gl-ES + hunspell; el LLM corrige solo lo marcado | LanguageTool (LGPL-2.1) | Hecho |
| 3 | Voz frase a frase con ritmo en embudo | StyleTTS2 Brais de Nós (modelo Apache-2.0; datos con condiciones, §7.1), Cotovía | Hecho |
| 4 | Planos: el código corta con las duraciones reales de la voz; el LLM describe cada plano | Pasa a API | Hecho en local |
| 5 | Imágenes + **puerta de imágenes** (manos sin cuerpo, lista de anacronismos y vetos, multitudes, repeticiones; regenera con otra semilla) | SDXL-Turbo (Stability Community License, gratis < 1 M USD/año, registro para uso comercial) [F https://stability.ai/license]; MediaPipe (Apache-2.0); Florence-2-large (MIT) | Hecho |
| 6 | Sonido: lluvia sintetizada, voz a −17 LUFS | Código propio | Hecho |
| 7 | Montaje: Ken Burns, niebla ligera, fundidos de 1,2 s, subtítulos `glg` | ffmpeg (`imageio-ffmpeg`) | Hecho; falta cargar las imágenes por tramos para 60 min |
| 8 | QA y semáforo | faster-whisper + Whisper turbo galego de Nós, LanguageTool, `ebur128` | 13 puertas |
| 9 | (Fase 2) Pistas pt/en con M1-M6 | Nós MT (MIT), Kokoro (Apache-2.0) | Probado en fragmentos |

**Escrituras atómicas:** el pipeline solo copia a la salida un MP4 con todas las puertas en verde, vía temporal +
renombrado; si falla una puerta tras el render, queda como `rexeitado.mp4` en el directorio de trabajo.

### 5.2 Por qué el LLM local no basta hoy en galego (y qué aportaría uno mejor)

| Modelo probado en CPU (Q4_K_M) | Resultado | Evidencia |
|---|---|---|
| `proxectonos/Llama-3.1-Carballo-Instr3` (Nós) | Sin plantilla de chat; no hace la tarea (escribe un texto genérico); 1,1 tokens/s | `../herramientas/pipeline/probas/llm_carballo_instr3/` |
| `proxectonos/Carvalho-Salamandra-Instruct` (Nós, "versión preliminar") | Copia el dossier y degenera (repeticiones, portugués) | `probas/llm_carvalho_salamandra/` |
| `utter-project/EuroLLM-9B-Instruct-2512` (Apache-2.0) | Sigue la estructura en galego, pero inventa datos y palabras; con puertas bloqueantes, 0 de 18 párrafos limpios | `probas/llm_eurollm_*`, `gauntlet2/video/qa.md` |
| Claude Opus 5.5 (ronda 1, respuestas escritas fuera del pipeline) | 2 avisos de LanguageTool frente a 11; 0 nombres sin anclar frente a 1 | `gauntlet2/video/ronda2/comparacion-llm.md` |

Lectura: los modelos abiertos que caben en 4 núcleos y 15 GB **no siguen instrucciones largas en galego con fiabilidad
suficiente para escribir sin supervisión**, y además son lentos (2,29 h de CPU para 3 min; ≈ 42 h extrapoladas para 60
min [P/S]). No es un juicio sobre la calidad lingüística de fondo de los modelos de Nós, sino sobre su uso como
redactores instruccionales en CPU. **Lo que aportaría a Nós y a la comunidad un modelo abierto mejor en galego:** un
modelo instruccional de tamaño medio (7-9B) con plantilla de chat, afinado para seguir instrucciones y para reescribir
fielmente un hecho dado sin añadir datos, haría este canal 100 % abierto y local, y serviría a cualquier divulgador,
concello o docente con un PC normal. El proyecto aporta a eso **un banco de pruebas real y público** (§6.2): el mismo
dossier, los mismos prompts y las mismas puertas, con los resultados de cada modelo abierto nuevo publicados cada
trimestre. El día que un modelo abierto pase las puertas con una tasa de reintentos comparable, el guion vuelve a local.

### 5.3 Controles automáticos: qué detectan y qué no

| Control | Umbral de bloqueo | Estado |
|---|---|---|
| **Lengua** (LanguageTool gl-ES + hunspell; lista cerrada de falsos positivos de estilo, nunca de hunspell) | 0 avisos, por bloque y sobre el guion entero, antes de la voz | Bloqueante |
| **H1-léxico** (nombres propios y cantidades anclados al dossier, por palabra entera) | 0 sin anclar | Bloqueante |
| **Veracidad** (NLI mDeBERTa-v3 + coincidencia léxica + reglas de desenlace y de quién hizo qué) | 0 frases sin apoyo; gancho: todas apoyadas | Bloqueante. Rechaza "a irmandade venceu", "os señores derrubaron as fortalezas dos irmandiños" [P `probas/veracidade_calibracion.md`] |
| Estilo (sin cifras escritas, preguntas ni palabras vetadas; aviso literal) | Todo cumplido | Bloqueante |
| **Coherencia narrativa** (nuevo: sin n-gramas repetidos de ≥ 4 palabras, referentes introducidos, orden cronológico) | 0 | **Por hacer** (carencia del veredicto `video-r3.md`) |
| Imágenes (`revisor.py`) | Todas aprobadas tras ≤ 5 intentos | Bloqueante |
| ASR (Whisper galego de Nós) | WER de la mezcla ≤ 6 %; por párrafo en el diseño | Mezcla hecho; por párrafo por hacer |
| Sonoridad | −18 a −16 LUFS | Bloqueante (muestra: −17,2) |
| Sincronía A/V y subtítulos | ≤ 0,1 s; ≥ 95 % | Bloqueante |
| H2: juez LLM de otra familia sobre cada frase frente al dossier | ≤ 5 % no respaldado | Por hacer |
| H4: lenda como lenda (marcadores + tipo en `afirmacions.csv`) | 0 fuera de bloque marcado | Por hacer |
| P1: variedad entre episodios (coseno de *embeddings*, 8-gramas) | Coseno < 0,85; < 2 % compartido | Por hacer (política de YouTube, §7.1) |
| **C0, errores canario**: 20 errores inyectados por ejecución | Detecta ≥ 80 % o no se publica | Medido 70 % → 80 % sin H2; "sin fuente" 2/5 [P `gauntlet2/medidas/c0-*`] |

**Lo que no detectan (lectura honesta):** una frase falsa construida solo con palabras del dossier; errores de una
fuente mala (Galipedia, un clásico del XIX); selección y énfasis; castellanismos sutiles fuera de listas y giros
torpes que LanguageTool no marca (en la muestra: "lembrando co que viran", "vivían ao limiar"); prosodia que el ASR
entiende igual (vocales abiertas y cerradas); anacronismos visuales que Florence-2 no nombra (tejados naranjas lejanos en
1:43 y 2:46 de la muestra); tono. **Estimación de residuos por episodio de 60 min [S]:** 3-10 errores de lengua visibles
para una filóloga, 1-4 imprecisiones históricas, decenas de detalles de prosodia. **El canal publicará errores cada
semana**; la defensa es declararlo (§7.3), corregir en ≤ 7 días y publicar la tasa.

**Contaminación del corpus:** todo texto publicado (descripción, subtítulos) lleva la marca "texto xerado
automaticamente con IA, sen revisión humana"; los guiones nunca se ofrecen como corpus limpio (§6).

---

## 6. Ecosistema galego y estrategia pro lingua

### 6.1 Actores (resumen de `gauntlet2/piezas/ecosistema.md` §1)

Tres rasgos generan fricción: (A) canal automático sin revisión; (V) voz sintética hecha con la voz de una persona
real; (N) anonimato.

| Actor | Fricción | Objetivo realista a 12 meses [S] | Cómo |
|---|---|---|---|
| **Proxecto Nós** (USC: CiTIUS + ILG) y Gradiant | V (condiciones de los datos de Brais, locutor), A (galego defectuoso en la web) | **Colaboración técnica** | Correo del §6.4 antes de publicar; datos de error; crédito exacto; nunca "en colaboración con Nós" sin permiso escrito |
| CSAG (antes CRTVG) | A; sensibilidad tras la recreación con IA de Begoña Caamaño (17-05-2026) [F https://www.nosdiario.gal/articulo/social/que-non-deixala-falar-criticas-ia-empregada-pola-crtvg-recrear-begona-caamano/20260518160723256730.html] | Indiferencia | Nada de su archivo ni de su estética; **nunca recrear personas** |
| RAG | A (norma) | No oposición | Norma RAG-ILG declarada; no pedir nada |
| Consello da Cultura Galega | A, V | Ser caso de estudio | Datos agregados al año; sus textos (CC NC-ND) no entran en el dossier |
| Secretaría Xeral da Lingua | Riesgo político | No oposición | No ser escaparate; fuera de política lingüística |
| AGPTI | **A** (su decálogo del 04-09-2026 critica textos mediocres y corpus "expropiados") [F https://www.agpti.org/defender-o-noso-traballo-e-defender-unha-sociedade-humana/] | Neutralidad informada | No sustituye a nadie (no hay equivalente humano); si hay ingresos, el primer gasto es revisión profesional |
| ADA y locución | **V** (Brais es la voz de un actor de dobraxe) | Neutralidad informada | La conversación con el locutor la abre Nós; si no quiere, se cambia de voz |
| A Mesa | A, V; la pista es | Neutralidad | No contactar al inicio; sin pista es |
| AGAL y lusofonía | Solo con pista pt | Neutralidad amistosa | Frase de apertura neutral; el canal no opina de normativa; encaja en la Lei 1/2014 Paz-Andrade [F https://gl.wikipedia.org/wiki/Lei_Paz-Andrade] |
| Software libre (Trasno, GALPon, AGASOL, Common Voice gl) | Pocas | **Colaboración** | Código libre documentado en galego; invitar a revisar la lista de castellanismos |
| Divulgadores | A, uso de su trabajo | No hostilidad | El dossier no usa su trabajo; "Para saber máis" enlaza a ellos; errores agradecidos |
| Medios | Titular "IA anónima enche YouTube" | Una pieza técnica a los 6 meses | Página de transparencia lista antes de publicar |
| Comunidad de hablantes | A, N | Comunidad de correctores | Formulario de erratas, contador público de errores enviados a Nós |

**Precisión sobre Nós (corrige la pieza de ecosistema):** la ficha del modelo `Nos_StyleTTS2-Brais-GL` **incluye el
entretenimiento** entre sus usos previstos (herramientas de accesibilidad, asistentes, agentes conversacionales,
entretenimiento) [F https://huggingface.co/proxectonos/Nos_StyleTTS2-Brais-GL], mientras que las condiciones del
*dataset* `Nos_Brais-GL` dicen *"solely for research purposes"* y prohíben la *"public exposure"* de las grabaciones [F
https://huggingface.co/datasets/proxectonos/Nos_Brais-GL]. La tensión real está entre esos dos textos, y es lo que se
pregunta a Nós. Además, Nós identifica públicamente a los locutores: Brais es la voz del actor de dobraxe Gaspar
González Somoza [F tts.nos.gal, comprobado por el panel crítico, `gauntlet2/veredictos/ecosistema-r4.md`]. Riesgo
añadido: que parte del público reconozca la voz y crea que el actor respalda el canal. Por eso la frase de crédito dice
"voz sintética xerada cun modelo", nunca el nombre del actor salvo que él y Nós lo pidan.

### 6.2 La tesis del promotor, examinada

La tesis ("non é contra o galego, senón ao contrario") **es defendible en una versión concreta**: *Serán* no es
"contido en galego feito con IA", sino **un laboratorio abierto que pone a prueba la IA en galego en público y devuelve
datos**. Presentado como producto de contenido, choca de frente con lo que AGPTI, ADA y A Mesa denunciaron en 2026
(RTVE, 20-02-2026) [F https://www.agpti.org/ada-agpti-mesa-reclaman-tve-cumpra-lei-dobrando-subtitulando-galego-servizos-profesionais-calidade/].

| Aportación | Valor para el galego [S] | Condición | Horas |
|---|---|---|---|
| **Informe trimestral de errores de voz** (Cotovía + StyleTTS2) en narración larga: palabra, pronunciación esperada y producida, minuto, audio de 3-5 s | Alto: la evaluación de la ficha llega a textos de "> 60 s" | Errores confirmados por un oído galegofalante | 2-3 h/trimestre |
| Pares "galego da máquina → galego corrixido" de la audiencia, en el formato de `erros_sistematicos_traducion_es_gl` de Nós [F https://huggingface.co/datasets/proxectonos/erros_sistematicos_traducion_es_gl] | Medio-alto si hay volumen (0-250 al año) | Correcciones humanas | 1 h/mes |
| Banco de preguntas de historia de Galicia con fuente | Alto como hueco | Una persona verifica una muestra | 3-5 h/trimestre |
| **Banco de pruebas de redacción en galego** (nuevo tras el 30-09): mismo dossier, prompts y puertas para cada LLM abierto; métricas públicas (avisos de lengua, frases sin apoyo, reintentos, CPU) | Medio-alto: medida continua de lo que le falta a un modelo abierto para escribir divulgación en galego | Metodología estable; se ejecuta sobre 2 temas fijos, no en cada episodio (en CPU cuesta ≈ 40 h por episodio) | 2-3 h/trimestre |
| Errores de la MT de Nós en dominio histórico (con pistas) | Medio | Confirmados por una persona | 0,5 h/trimestre |
| Pipeline libre documentado en galego | Medio | Que funcione fuera de este entorno | 5-10 h una vez |
| Guiones | **Bajo o negativo como corpus** | Solo etiquetados como sintéticos, para evaluación | ~0 |

**Contradicciones y cómo se resuelven:**
1. **Guion con un LLM cerrado por API.** Se dice abiertamente: los modelos abiertos probados no hacen la tarea en CPU
   (§5.2). El banco de pruebas trimestral convierte la contradicción en la aportación más citable; el día que un modelo
   abierto pase, se cambia.
2. **Contaminar el corpus.** Marca de sintético en todo texto publicado; se pregunta a Nós el formato que prefieren.
3. **"Sin revisión humana" frente a "pro lingua".** No se gana en abstracto: se baja la escala (nunca diario), se
   corrige rápido y se mide en público.
4. **La voz de una persona sin su consentimiento para este uso.** Sin sí escrito, no se usa (§7.1).
5. **Pistas traducidas.** Solo pt y en, galego original, sin es el primer año, ninguna voz de actor (§4.4).

**Veredicto:** probabilidad de que la tesis se sostenga en público si se cumplen las cinco condiciones: **media [S]**;
si no: **baja**, y el canal sería un argumento más contra la IA en galego. Si la prueba manda parar, la tesis se reduce
a lo entregado (informe de voz de 8 episodios, métricas y código): poco, pero verificable. **Versión no defendible:**
"A IA fai historia de Galicia en galego para todos".

### 6.3 Anonimato frente a apoyo

Ninguna institución respalda a un anónimo y D4 exige firmar ante Nós. Solución: **seudónimo ante el público
(*Serán*), identidad conocida por los socios** (Nós y quien apoye después), con petición de no hacerla pública. Si
algún día se busca apoyo público (convocatoria, prensa), se levanta el anonimato o firma una asociación. La
verificación de identidad ante Google para las funciones avanzadas (§7.1) no es pública y es compatible con D6.

### 6.4 Correo a Proxecto Nós / USC (D4), en galego

Versión integrada: recoge la decisión del guion por API, la precisión de la ficha del modelo, la cláusula de YouTube y
las pistas; corrige la redundancia señalada en la ronda 4.

- **Para:** `proxecto.nos@usc.gal` [F https://huggingface.co/datasets/proxectonos/Nos_Brais-GL]. Copia opcional al
  equipo de Gradiant que desenvolveu os StyleTTS2 (buscar el contacto en su web; no inventarlo).
- **Asunto:** Consulta sobre o uso da voz StyleTTS2 Brais nunha canle de divulgación en galego e oferta de datos de erros

> Ola, bo día:
>
> Chámome [nome e apelidos] e escríbovos a título persoal. Estou a preparar, como afección, unha canle de YouTube de
> historia e cultura de Galicia en galego pensada para escoitar antes de durmir. Os episodios son longos e teñen forma
> de funil: o título e os primeiros un ou dous minutos son máis vivos, con curiosidades verídicas e sorprendentes da vida
> doutras épocas (sempre con fonte, sen burlarse de ninguén e sen esaxerar), e despois o ritmo baixa aos poucos ata un
> ton sereno para durmir. Os temas son de toda Galicia: castros, o Camiño, os mosteiros, os irmandiños, o mar, a vida
> cotiá de antes e as lendas, contadas sempre como lendas.
>
> A canle faise cun proceso automático, sen revisión humana previa. A voz é o modelo **Nos_StyleTTS2-Brais-GL** e o
> control de pronuncia faise co voso Whisper en galego. O guión redáctao un modelo de linguaxe comercial a través da
> súa API, a partir só dun dossier de fontes con licenza aberta. Probei primeiro modelos abertos en CPU, entre eles
> Carballo e Carvalho, pero na miña máquina non conseguín que redactasen os guións con fiabilidade; quero seguir probándoos
> cada trimestre co mesmo material e publicar os resultados, por se vos serven.
>
> Antes de publicar nada con esa voz quería preguntarvos directamente. Vexo que a ficha do modelo menciona o
> entretemento entre os usos previstos, pero as condicións dos datos de Brais falan de investigación; e, sobre todo,
> detrás hai unha persoa. Concretamente, gustaríame saber:
>
> 1. Como interpretades esas dúas cousas para unha canle pública de divulgación. Debo dicirvos que, aínda que eu non
>    monetice a canle, YouTube pode poñer anuncios nos vídeos pola súa conta; e que, se algún día a canle tivese
>    ingresos, preguntaríavos de novo antes.
> 2. Se o consentimento do locutor cobre este tipo de uso, incluído ese comezo de ton máis vivo. Se non o cobre ou non
>    está claro, pregaríavos que lle trasladásedes a consulta vós; non quero contactar con el pola miña conta. Se
>    prefire que non se use a súa voz, cambiarei de voz sen máis. Se o acepta, ofrézolle crédito co seu nome ou sen el,
>    como prefira, e unha parte dos ingresos se algún día os houbese.
> 3. Como preferides que figure o crédito (por exemplo: "Voz sintética: modelo Nos_StyleTTS2-Brais-GL do Proxecto Nós
>    (USC), desenvolvido por Gradiant, licenza Apache 2.0").
> 4. Como preferides que marque os textos (descricións, subtítulos e guións) para que non acaben nos corpus de
>    adestramento como se fosen galego revisado. Preocúpame contribuír a empeorar os datos cos que traballades.
>
> A cambio, gustaríame devolvervos algo útil:
>
> - **Un informe trimestral de erros de pronuncia** en narración longa (máis dunha hora seguida): topónimos, nomes
>   medievais, vogais abertas e pechadas, números e cambios de prosodia ao longo do audio, con fragmentos de son e a
>   forma correcta.
> - **As correccións que faga a audiencia**, en pares "texto xerado / texto corrixido".
> - **Un conxunto de preguntas de historia de Galicia con fonte**, por se vos serve para avaliar modelos.
> - **O código de todo o proceso**, con licenza libre, e as métricas de cada episodio.
>
> Quero contarvos tamén unha cousa que aínda non está decidida. Se a canle ten público en galego, nunha segunda fase
> gustaríame probar a engadir ao mesmo vídeo pistas de audio traducidas automaticamente ao portugués e ao inglés, co
> galego sempre como lingua orixinal, título en galego e sen pista en castelán. Esas pistas serían tradución e voz
> automáticas sen revisión humana, e diríase así nelas. **A voz de Brais non se usaría nunca nelas**: nin para outras
> linguas nin clonada; usaríanse outras voces sintéticas abertas que non sexan de actores de dobraxe. Se para traducir
> ao inglés uso o voso modelo de tradución, enviaríavos tamén os erros que atopen os controis automáticos (nunha
> primeira proba co voso modelo galego-castelán, por exemplo, "Rocha Forte" saíu como "Roca Forte"). Se vedes algún
> problema nesta idea, agradecería que mo dixésedes.
>
> A canle publicarase cun nome propio, sen o meu. Pídovos, se non vos importa, que non fagades público quen está
> detrás; vós si sabedes con quen falades, e contestarei a calquera cousa que precisedes.
>
> Non publicarei nada coa voz de Brais ata ter a vosa resposta. Se nun mes non sei nada de vós, volverei escribir; e se
> despois diso seguise sen resposta, usaría outra voz ata que puidésemos falalo, por exemplo algunha das voces do
> corpus CRPIH_UVigo-GL-Voices (Sabela, Icía ou Iago), se vos parece ben.
>
> Moitas grazas polo traballo que facedes. Grazas a Nós é posible pensar en facer isto en galego.
>
> Un saúdo,
>
> [Nome e apelidos]
> [Correo e teléfono]
> [Ligazón privada a unha mostra de 2-3 minutos]

**Notas para el promotor:**
- Adjuntar en enlace privado una muestra de 2-3 min **con el gancho tal como irá** y un tramo del tono sereno: Nós y el
  locutor tienen que ver lo que autorizan. La muestra actual tiene un gancho flojo (§0); mejor enviar la regenerada con
  el guion por API (semana 2), sin retrasar el correo más de una semana.
- El compromiso "non publicarei nada coa voz de Brais ata ter a vosa resposta" **obliga**. No hay plazo tras el cual se
  use Brais sin respuesta.
- Antes de enviar: escuchar Sabela, Icía e Iago en un tramo de narración (el correo las nombra) y pedir a un
  galegofalante que relea el texto.
- **Qué hacer ante cada respuesta:** sí sin condiciones → crédito con su fórmula e informe trimestral; sí para hobby
  pero no para monetizar → se publica, P4 (YPP) queda bloqueada y se pide a YouTube lo que permitan sus ajustes; sí si
  consiente el locutor → voz de reserva mientras tanto; no → Sabela, Icía o Iago preguntando a Nós, o proveedor gl-ES con
  licencia comercial; silencio tras el recordatorio → voz de reserva, nunca Brais.

### 6.5 Hoja de ruta de acercamiento

| Fase | Cuándo | Con quién | Qué se hace | Qué no |
|---|---|---|---|---|
| 0. Permiso | S0-S1 | Nós (copia a Gradiant) | Correo del §6.4 con nombre real | Contactar al locutor; publicar con su voz |
| 0-bis. Espera | S1-S5 | — | MVP; voces de reserva en 60 min; recordatorio a los 30 días | Publicar con Brais sin sí escrito |
| 1. Preparación | Antes de M0 | — | Página "Como se fai *Serán*" con política de ganchos, formulario de erratas | Buscar prensa; decir "calidade" |
| 2. Aviso previo | M0 − 1 semana | AGPTI y ADA (solo si Nós y el locutor dijeron sí) | Carta breve: qué es, qué voz y con qué permiso, compromiso de revisión profesional si hay ingresos | Pedir aval |
| 3. Comunidad técnica | M0 | Trasno, GALPon, AGASOL, Common Voice gl | Código y artículo técnico en galego | Presentarlo como producto |
| 4. Lanzamiento discreto | M0 | Público | 3 episodios, aviso, etiqueta, siembra declarada | Contactar a A Mesa, RAG, CSAG, medios |
| 4-bis. Pistas pt/en | M0 + 12-17 semanas, con condiciones (§4.4) | Público; aviso a Nós | Reglas del §4.4 | Pista es; voz de actor |
| 5. Primera devolución | M0 + 3 meses | Nós | Informe de voz, pares de corrección, banco de pruebas | Pedir respaldo público |
| 6. Caso de estudio | M0 + 6 meses, si P2 da GO | Código Cero, GCiencia; CCG | Datos agregados | Titulares de éxito |
| 7. Institucional | Con tracción y revisión humana parcial | CSAG, SXL, RAG | Solo con identidad pública o entidad | Pedir dinero para un canal sin revisión |

---

## 7. Riesgos y cumplimiento

### 7.1 Voz, licencias y plataforma (condiciones de publicación)

| Riesgo | Tratamiento |
|---|---|
| **Voz de Brais sin permiso.** El modelo es Apache-2.0, pero la voz de la persona no la cubre esa licencia (derecho a la propia voz, LO 1/1982, art. 7.6) [R `gauntlet/piezas/gtm_riesgos.md` §3.3 bis], y los datos dicen "solely for research". Con *Right to Monetize*, YouTube puede poner anuncios en vídeos de canales fuera del YPP [F https://support.google.com/youtube/answer/10090902]: el uso no es "no comercial" aunque el promotor no cobre | **P0: sin sí escrito de Nós/USC (y del locutor si Nós lo pide) no se publica con Brais.** Voz de reserva lista antes de M0: Sabela (locutora de radio), Icía o Iago (aficionados), datos donados CC-BY 4.0, modelos Apache-2.0 [F https://zenodo.org/records/8027725 ; https://huggingface.co/proxectonos/Nos_TTS-sabela-vits-phonemes], acreditadas; si ninguna aguanta 60 min, proveedor gl-ES con licencia comercial. **Plan B de fechas:** si a S5 no hay respuesta, M0 se hace con la voz de reserva y no se retrasa |
| **Funciones avanzadas de YouTube** (A/B de títulos y miniaturas, pistas multi-audio). Un teléfono no basta: hace falta documento de identidad, verificación por vídeo o historial del canal [F https://support.google.com/youtube/answer/9890437] | **Requisito de P0:** el promotor se verifica con DNI o vídeo ante Google en la semana 1 (no es público; compatible con D6). Sin ello, la ventana NO CONCLUYENTE usa solo cambios manuales de título y miniatura, y la fase 2 no existe |
| SDXL-Turbo | Stability Community License: gratis < 1 M USD/año; registro para uso comercial [F https://stability.ai/license] → registrarse antes de M0 y archivar los términos |
| API del LLM | Términos de uso automatizado del proveedor; el texto generado va marcado como IA |

### 7.2 Política de YouTube de contenido inauténtico

- Desde el 15-07-2025 no es monetizable el contenido generado con IA "made with generic or unoriginal templates giving
  the impression of mass production" ni el "similar or repetitive content with ... minimal variation across videos" [F
  https://support.google.com/youtube/answer/1311392?hl=en]. La nota del 13-07-2026 **aclara** (no endurece) esa
  política en tres categorías, con ejemplos como **"image slideshows and templated storylines"**, y la aplica a nivel de
  canal [F https://www.tubefilter.com/2026/07/13/youtube-inauthentic-content-monetization-policy-update/ ;
  https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/].
- **Nos toca de lleno:** el canal es imágenes + voz IA + plantilla, sin revisión. Probabilidad de que el YPP se deniegue
  si se solicita: **40-60 % [S puro**, sin casos comparables documentados]. Desmonetización tras entrar: 20-30 % [S].
  Cierre del canal: < 5 % si se etiqueta y no se engaña [S].
- Mitigaciones: variedad real entre episodios (control P1, I3), series con arco, fuentes en la descripción, cadencia
  lenta y fija (nunca diario: que la frecuencia refuerce la impresión de producción masiva es inferencia propia [S]),
  no copiar la plantilla de títulos de la referencia, copia del catálogo fuera de YouTube.
- **Con D6, el éxito no puede depender de monetizar.** Las puertas miden audiencia y datos devueltos.

### 7.3 Etiquetado, AI Act art. 50 y aviso hablado veraz

- **Etiqueta "contenido alterado o sintético" de YouTube: obligatoria** con escenas realistas de época que no
  ocurrieron [F https://support.google.com/youtube/answer/14328491?hl=en]; se activa en cada vídeo
  (`status.containsSyntheticMedia`).
- **AI Act, art. 50 (aplicable desde el 2-08-2026)** [F https://artificialintelligenceact.eu/article/50/]:
  - 50.4, texto generado por IA para informar al público sobre asuntos de interés público: hay que declararlo **salvo**
    revisión humana o control editorial con una persona responsable. **Sin revisión (D5), la excepción no se puede
    invocar** → se declara [S, interpretación: la divulgación histórica es probablemente "interés público"].
  - 50.4, *deepfakes*: escenas fotorrealistas de lugares y hechos reales y una voz sintética que se parece a la de un
    locutor real → aviso claro "a más tardar en la primera exposición" (50.5).
  - La excepción de obra "evidentemente artística o de ficción" no aplica: es divulgación. El art. 50 obliga a declarar
    lo artificial, no a identificar al autor [S].
- **Aviso hablado (galego, lo lee la voz sintética en los primeros segundos).** Es el que ya usa el pipeline y es
  veraz:

  > Boas noites. A voz que vas escoitar é sintética, e este texto preparouno un proceso automático.

  En la versión de 60 min se añade, tras la fórmula de entrada: *"As imaxes tamén as xerou unha intelixencia
  artificial e non son documentos históricos. Pode haber erros: se atopas algún, dínolo nos comentarios."* **Nunca** se
  dice ni se insinúa que una persona revisó el texto, la voz o las imágenes, porque no es verdad (D5). Si algún día hay
  revisión humana parcial, el aviso cambia solo para los episodios revisados.
- **Nota fija de la descripción (galego):**

  > Como se fai esta canle: o guión, a voz e as imaxes xéranse de forma automática con intelixencia artificial, sen
  > revisión humana antes da publicación. O texto redáctao un modelo de linguaxe só a partir das fontes que se citan
  > embaixo, e uns controis automáticos comproban a ortografía, a gramática e que cada dato estea nas fontes; aínda así,
  > poden quedar erros. Voz sintética: modelo [nome do modelo e crédito que indique o Proxecto Nós]. Imaxes: xeradas
  > con IA; non son documentos históricos. Erratas coñecidas: no comentario fixado.

### 7.4 Riesgos de lengua, historia y ecosistema

| # | Riesgo | Prob. / impacto [S] | Tratamiento |
|---|---|---|---|
| R1 | Errores de lengua en cada episodio | Cierta / medio-alto | Aviso; lista viva de castellanismos; erratas públicas; léxico de Cotovía |
| R2 | Error histórico con carga identitaria | Media / alto | Temas de consenso; vetos; puerta de veracidad; H2 |
| R3 | Mito presentado como hecho (sube con las lendas) | Media-alta / medio | H4; marcadores de lenda; también en ganchos |
| R4 | Gancho falso o estigmatizante (Galicia atrasada o mísera) | Media / **alto** (lo más visible) | Reglas del §4.3; alarma A9 |
| R5 | El locutor o ADA descubren la voz sin ser preguntados; reconocimiento de la voz de un actor conocido | Baja con P0 / alto | P0; crédito sin su nombre; A4 |
| R6 | Crítica de AGPTI, ADA o A Mesa ("IA contra o galego") | Media si hay eco / alto | Aviso previo; no sustitución; A7 |
| R7 | Pistas traducidas leídas como dobraxe con IA o salida del galego | Media con es; baja con las reglas / alto | Reglas del §4.4; A10 |
| R8 | Tesis pro lingua desmontada (LLM cerrado, corpus) | Media / medio | Banco de pruebas trimestral; marca de sintético |
| R9 | Los datos prometidos a Nós no se entregan (falta de horas) | **Alta** / medio | Exportación automática de errores y métricas; mínimo: informe de voz trimestral |
| R10 | YPP rechazado o canal desmonetizado | Media-alta / bajo para un hobby | §7.2 |

**Alarmas que paran la publicación:** A1 aviso o *strike* de YouTube → pausa y apelación con el expediente; A2 rechazo
del YPP → seguir como hobby; A3 crítica pública con eco → pausa de 2 semanas y respuesta con datos; A4 Nós o el locutor
piden retirar la voz → sustituir en ≤ 30 días; A5 error grave señalado → corregir en ≤ 7 días o despublicar; A6 C0 <
80 % o > 25 % de episodios bloqueados → no publicar hasta reparar; A7 una asociación o un medio cita el canal como
ejemplo negativo → pausa de 2 semanas y respuesta sin polemizar; A8 Nós pide retirar su nombre → 48 h; A9 gancho falso
o estigmatizante → título y miniatura en ≤ 24 h, tramo en ≤ 7 días, 4 semanas con ganchos suaves (dos casos en un
trimestre → sin ganchos con cifra hasta revisar reglas); A10 crítica a las pistas o L < 25 % dos meses → retirar
pistas en ≤ 48 h.

---

## 8. Puertas, KPIs y calendario

### 8.1 Puertas

| Puerta | Cuándo | Condición para seguir |
|---|---|---|
| **P0 · Salida** | Antes de M0 | (1) Piloto de 60 + 30 min pasa todos los controles bloqueantes, incluida la coherencia narrativa, sin intervención en ≤ 16 h de reloj; (2) C0 con H2: ≥ 90 % y ≥ 4/5 en "sin fuente" en el conjunto actual, y ≥ 80 % en un conjunto nuevo de otro tema (**hoy: 80 % y 2/5, no se pasa**); (3) −18/−16 LUFS; (4) el promotor ha cronometrado 3 dossieres y caben en §3.4; (5) aviso hablado, nota de descripción y etiqueta sintética; (6) licencias archivadas y registro de Stability; (7) **voz con permiso: sí escrito de Nós para Brais, o voz de reserva acreditada**; (8) funciones avanzadas activas o renuncia explícita a A/B y pistas; (9) comunidades de siembra verificadas; (10) umbrales de §2.4 congelados en el repo |
| **P1 · ¿Existe el nicho?** | Día 30 del episodio 8 (≈ M0 + 10 semanas); hasta M0 + 18 si hay ventanas | §2.4 |
| **P1-bis · Pistas pt + en** | M0 + 12-17 semanas, si P1 no da PARADA | §4.4, regla 3 |
| **P2 · Hábito** | M0 + 6 meses, solo si P1 dio PLAN | Mediana a 30 días ≥ 200 **y** ≥ 150 subs **y** ≥ 25 % de recurrentes **y** ≥ 30 % de vistas desde listas, canal o búsqueda **y** erratas por episodio decrecientes. Si no: banco de pruebas técnico a 1 episodio al mes |
| **P3 · Tracción (dispara D1)** | Desde M0 + 6 meses, mensual | 2 de 3 en 90 días: ≥ 500 subs [F], ≥ 3.000 h en 365 días [F], mediana ≥ 1.000 en los 8 últimos [S]; **y** voz con permiso; **y** sin alarmas A1-A2 abiertas. Adelanto: si la voz es el motivo de ≥ 20 % de las críticas 2 meses seguidos y la retención cae en los 2 primeros minutos, basta 1 KPI |
| **P4 · YPP** | Con 8.000 h en 365 días (+ 1.000 subs [S]) | Solo con la voz autorizada para monetizar y sin alarmas |

### 8.2 Cuadro de mando mensual (5 min)

| KPI | Umbral de alarma |
|---|---|
| Mediana de vistas a 30 días (4 últimos) | Caída > 50 % dos meses seguidos |
| Impresiones por vídeo y CTR | < 500 o CTR < 2 % dos meses → nueva ronda de títulos y miniaturas |
| Fuentes de tráfico | Explorar + Sugeridos < 20 % desde M0 + 6: el canal vive de la siembra |
| Retención a 2 min | < 40 % |
| AVD | Solo informativo (mide sueño e interés a la vez) |
| Recurrentes / subs netos | < 10 % / negativos dos meses |
| Erratas por episodio | Subiendo tres meses |
| C0 y episodios bloqueados | < 80 % / > 25 % |
| Coste de API por episodio | > 5 USD: revisar modelo, caché y lotes |
| Errores enviados a Nós por trimestre | 0 → la tesis pro lingua no se usa en público |
| Avisos de YouTube | Cualquiera |

### 8.3 Calendario (desde el 30-09-2026) [S]

| Semanas | Fechas aproximadas | Hito |
|---|---|---|
| S0-S4 | 30-09 a 27-10-2026 | Primeras 4 semanas (§9): correo a Nós, verificaciones, guion por API, muestra regenerada, voces de reserva |
| S5 | ≈ 3-11-2026 | Recordatorio a Nós si no hay respuesta; decisión de voz del piloto |
| S5-S12 | Nov-dic 2026 | Resto del MVP: H2, H4, P1, ASR por párrafo, montaje por tramos, `dossier.py` con PDF, piloto de 60 min, stock de 8 dossieres |
| S12-S14 | ≈ finales de diciembre 2026 a mediados de enero 2027 | P0. M0 si pasa (3 episodios la primera semana) |
| M0 + 5 | ≈ febrero 2027 | Episodio 8 publicado |
| M0 + 10 | ≈ marzo 2027 | **Decisión P1** (o primera ventana NO CONCLUYENTE) |
| M0 + 12-17 | Abril-mayo 2027 | Fase 2 de pistas pt/en, si procede |
| M0 + 13 | ≈ abril 2027 | Primera devolución trimestral a Nós |
| M0 + 26 | ≈ julio 2027 | P2 (si PLAN) o repetición de la prueba en modo MÍNIMO |
| M0 + 52 | ≈ enero 2028 | Revisión anual: pista es (§4.4, regla 4), balance de la tesis |

Si P0 no se pasa en S14, M0 se retrasa en bloques de 2 semanas; no se publica con puertas en rojo. El nuevo umbral del
YPP (1-02-2027) se aplica: el canal será un solicitante nuevo.

---

## 9. Primeras 4 semanas

| Semana | Tareas (≈ 6 h/semana) | Entregable verificable |
|---|---|---|
| **1** (30-09 a 6-10) | Releer y enviar el correo a Nós (§6.4) con la muestra actual o la regenerada si llega a tiempo; verificar la identidad ante Google para las funciones avanzadas; comprobar en Studio si el galego es idioma de pista y de vídeo; congelar en el repo los umbrales de §2.4; empezar el backend de API en `llm.py` (con caché de prompt, lotes y registro de coste por llamada) | Correo enviado (fecha); `umbrais-p1.md` en el repo; resultado de Studio anotado |
| **2** (7-13 oct) | Terminar el backend de API; regenerar la muestra de irmandiños con el guion por API (10-15 min, como pidió el crítico del vídeo) con las mismas puertas bloqueantes; medir coste real, reintentos por bloque y avisos; comparar con EuroLLM en la misma tabla; elegir modelo (§3.3) | Nuevo `ejemplo.mp4` y `qa.md` (con escritura atómica y comprobación de decodificación antes del commit); coste real por minuto narrado |
| **3** (14-20 oct) | Puerta de coherencia narrativa; resolver en el dossier el conflicto de testigos (183/204) del preito Tabera-Fonseca; escuchar Sabela, Icía e Iago en un tramo de 10 min y pasar el ASR; registrarse en la Community License de Stability; verificar las comunidades de siembra y sus normas | Puerta en `pipeline.py` con prueba; informe de voces de reserva; lista de comunidades |
| **4** (21-27 oct) | `dossier.py` con PDF y conectado a `pipeline.py`; el promotor cronometra el primer dossier del stock (un tema de lendas y uno de historia); página "Como se fai *Serán*" con la política de ganchos; primer tramo de 20 min del piloto para medir tiempos de máquina reales sin el LLM local | 2 dossieres con `cronometro.md`; página de transparencia en borrador; tiempos por etapa |

Al final de la semana 4 se sabe: si el guion por API pasa las puertas sin caer a texto literal (si no, el formato no da
el pego y hay que replantearlo antes de gastar más horas), cuánto cuesta de verdad, si hay voz utilizable y si YouTube
permite las funciones que la prueba necesita.

---

## Anexo: metodología del Gauntlet 2 y resultado de cada pieza

### A.1 Método

Tres piezas, cada una con un constructor y críticos adversariales con un listón fijado en `gauntlet2/contexto.md`:
- **Plan desatendido** (retornos, costes, pipeline, plataforma): crítico "operador escéptico de canales faceless".
- **Ecosistema** (actores, tesis pro lingua, anonimato, correo a Nós): panel de "investigadora de Nós + directivo de
  contenidos de la CRTVG + sociolingüista activista".
- **Vídeo de ejemplo**: "crítico visual ciego" (compara la hoja de contactos con el *storyboard* de la referencia sin
  saber cuál es cuál) y "operador de canales faceless con IA" (inspecciona el MP4, el QA y el código).

En cada ronda la pieza gana solo si todos sus críticos aprueban. Los veredictos se guardan en `gauntlet2/veredictos/` y
se suben a git al acabar cada ronda (regla del repo tras el corte del 29-09-2026). El promotor intervino como juez humano
tras ver el vídeo y cambió el listón varias veces (ganchos, temas, nicho, pistas, guion por API), lo que explica parte
de los suspensos: varias rondas perdieron por no incorporar una decisión posterior a su encargo.

### A.2 Resultado: ninguna pieza ganó

| Pieza | Rondas | Resultado | Carencia principal en cada ronda |
|---|---|---|---|
| **Plan desatendido** | 4 | **Perdió las 4** | r1: no usaba sus propias medidas (tiempos, C0 70 %) y tenía horas contradictorias; r2: no contestaba la pregunta obligatoria del nicho ni las pistas ni los temas ampliados; r3: la prueba del nicho decidía solo por vistas y confundía "sin distribución" con "sin demanda"; r4: permitía publicar con la voz de Brais sin permiso con el argumento falso de "sin monetizar" (*Right to Monetize*), y suponía que las funciones avanzadas se activan con un teléfono (`veredictos/plan-r4.md`) |
| **Ecosistema** | 4 | **Perdió las 4** | r1: errores de galego en el correo e incoherencia correo/hoja de ruta; r2: ignoraba los ganchos con picante; r3: no analizaba las pistas multilingües ni el nicho; r4: decía que el entretenimiento no está entre los usos previstos del modelo de Nós, cuando la ficha lo incluye, y no recogía que el locutor está identificado (`veredictos/ecosistema-r4.md`) |
| **Vídeo** | 3 | **Perdió las 3** | r1: no era desatendido (el guion lo escribió Claude a mano en modo `manual`) y la QA dio PUBLICABLE a un plano con cuatro manos; r2: desatendido con EuroLLM, pero con historia falsa y palabras inventadas en el gancho, y se entregó un MP4 que su propia QA rechazaba; r3: PUBLICABLE 13/13 y verdadero, pero el guion es dossier literal con repeticiones y sin picante; el crítico visual vio una **mejora marginal** (paleta coherente, sin artefactos visibles, pero luz plana y planos repetidos) y el operador pidió pasar el guion a un LLM por API, que el promotor ya había decidido (`veredictos/video-r3.md`) |

### A.3 Qué hace esta integración con las últimas carencias

| Carencia final | Tratamiento en el plan v2 | ¿Resuelta? |
|---|---|---|
| Publicar con Brais sin permiso ("sin monetizar") | P0 exige sí escrito o voz de reserva; *Right to Monetize* citada; plan B de fechas (§7.1) | Sí, en el papel |
| Funciones avanzadas por teléfono | Verificación con DNI o vídeo en la semana 1, requisito de P0 (§7.1) | Sí, en el papel |
| 1.000 subs atribuidos al blog de YouTube | Marcado [S]; solo las 8.000 h con fuente (§3.2) | Sí |
| Usos previstos del modelo de Nós y locutor identificado | Corregido en §6.1; pregunta 1 del correo reescrita; riesgo de reconocimiento (R5) | Sí |
| Guion con LLM local: sin narración, repeticiones, sin picante | Guion por API (decisión del 30-09), coste con fuente (§3.3), puerta de coherencia (§5.3) | **No demostrado:** la muestra publicada sigue siendo la del LLM local; la regenerada es la tarea de la semana 2 |
| Muestra de 3 min frente a un formato de 60 min | Piloto de 60 min como condición de P0; tiempos rehechos con la puerta de imágenes (8-15 h) | **No demostrado** |
| Dato en conflicto (183 o 204 testigos) | Tarea de la semana 3 (§9); regla de conflictos en §4.2 | Pendiente |
| C0 por debajo del umbral en "sin fuente" | P0 lo exige con H2 | Pendiente (H2 sin construir) |

**Contradicciones entre piezas eliminadas en esta versión:** publicación con Brais sin respuesta (la del plan) frente a
"nunca sin sí" (ecosistema) → gana la segunda; fase 3 de castellano condicionada (plan) frente a ninguna pista es el
primer año (ecosistema) → gana la segunda; umbral de parada antiguo del ecosistema (M < 40 o G < 15 %) → sustituido por
la prueba en dos pasos del plan v4; duración del MVP (8-10 semanas en ecosistema, 10-14 en el plan) → 12-15 semanas con el
trabajo añadido; tiempo de máquina (5-7 h del plan frente a 28,6 h extrapoladas del vídeo) → 8-15 h con el guion por API;
coste del guion (1-2 USD del plan, "céntimos" de la decisión) → 1-3 USD por episodio en el caso central y céntimos solo
para la muestra; comparación Carballo frente al modelo cerrado "en cada episodio" (≈ 40 h de CPU por episodio) → banco de
pruebas trimestral sobre 2 temas fijos.

**Lo que este plan v2 no es:** un plan aprobado por sus críticos. Es la integración honesta de tres piezas que
perdieron, con las correcciones que pidieron sus últimos veredictos, y pasa ahora al tribunal.
