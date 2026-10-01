# Informe de la pieza SON (Gauntlet 3): qué ambiente sonoro llevar en el vídeo largo

Agente de sonido (Claude), 30-09-2026. **Nadie ha escuchado nada**: ni una persona ni Claude (Claude no oye). Todo lo
que sigue son medidas automáticas, que no sustituyen al oído del promotor: para eso están `mostra-opcions.m4a` (las
cuatro opciones sobre el mismo fragmento) y `mostra-catalogo.m4a` (cada sonido solo); ver [`README.md`](README.md).

Encargo: decisiones D13 y D14 del promotor (`contexto.md` §7): sonido acoplado a la escena, tramos de voz limpia,
nada de ruido blanco constante, que no se haga monótono y murmullo de voces ininteligibles en los gentíos; "que el
gauntlet mida la mejor opción".

## 1. Qué se comparó

| Opción | Qué es | Código |
|---|---|---|
| **A** | Lluvia continua (`choiva2`) con el nivel de la curva del embudo | `son.py` de 7541a9e (lo que había antes de esta pieza) |
| **B** | Solo lluvia y lareira en los planos que las muestran, fundidos de 2 s, voz limpia en el resto (D13 tal como estaba) | `son.py` de 7541a9e |
| **C** | Catálogo completo por escena (D14): 9 tipos, variación por tramo, eventos cada vez más escasos y suaves, fundidos largos, tope sobre la voz, voz limpia donde no hay sonido | `son.py` nuevo, `ambiente='escena'` |
| **D** | Sin ambiente, solo voz | — |

Dos bancos de prueba:

1. **Fragmento con voz** (2 min 14 s, las cuatro opciones en `mostra-opcions.m4a`): un episodio de 30 min
   "comprimido" en tres trozos (gancho, transición y zona de dormir), 20 frases narradas por la voz del pipeline
   (StyleTTS2 Brais, Cotovía 0.5, parámetros de la curva de cada momento) y 15 planos con imagen y sonido. El texto y la
   lista de planos los escribió Claude (agente de sonido) solo para medir: no son guion. 11 de los 15 planos llevan
   sonido para enseñar todo el catálogo, así que C cambia de sonido cada ~10 s (en un episodio, cada 1-3 min).
2. **Episodio simulado de 30 min sin voz** (solo ambiente), para lo que un fragmento no puede medir: cambios cada
   10 min, monotonía, tramos largos y picos en 15 min de zona de dormir. 163 planos con la duración de la curva
   (5 s al principio, 17 s al final) y el sonido de cada imagen del arco de "As meigas de verdade"
   (`tema/investigacion.md` §10). Tres listas de planos inventadas por Claude: **guía** (la que pide
   [`guia-son.md`](guia-son.md): bloques por escena y respiros limpios; 31 % de planos limpios), **guia1** (mi primer
   intento de seguir la guía: se quedó corto de respiros, 26 % limpios) y **alterna** (sonido y voz limpia casi en cada
   plano, 36 % limpios).

## 2. Medidas en el fragmento con voz

| Medida | A | B | C | D |
|---|---|---|---|---|
| DNSMOS SIG (calidad de la voz; 1-5) | 3,57 | 3,59 | 3,57 | 3,62 |
| DNSMOS BAK (cuánto molesta el fondo; 5 = nada) | 2,77 | 3,75 | 3,51 | 4,14 |
| DNSMOS OVRL (global) | 2,65 | 3,16 | 3,02 | 3,37 |
| OVRL en la zona de dormir | 2,45 | 2,89 | 2,74 | 3,37 |
| WER Whisper gl, texto de cada tramo (ver §4.2) | 0,022 | 0,063 | 0,070 | 0,133 |
| **WER Whisper gl, frase a frase** (errores en 271 palabras) | 0,022 (6) | 0,022 (6) | 0,026 (7) | 0,018 (5) |
| % del tiempo de voz sin ambiente (voz limpia) | 0 | 64,8 | 17,8 | 100 |
| Ambiente bajo la voz (mediana, dB) | 15,9 | 18,8 | 22,2 | — |
| Zona de dormir: pico de eventos en 50 ms sobre su fondo (dB) | 9,7 | 14,3 | 6,9 | — |
| Zona de dormir: "sustos" (arranques de +6 dB en 200 ms, >10 dB sobre el fondo) | 0 | 11 | 0 | 0 |
| Variación espectral del fondo (dB; más = más variado) | 0,5 | 2,5 | 5,7 | — |
| Monotonía (% de pares de ventanas de 5 s, separadas ≥ 60 s, que suenan igual) | 100 | 44 | 10 | — |

## 3. Medidas en el episodio simulado (30 min, solo ambiente)

| Medida | A | B (guía) | C (guía) | C (guia1) | C (alterna) |
|---|---|---|---|---|---|
| % del tiempo con ambiente | 100 | 38,5 | 71,6 | 78,2 | 76,1 |
| Tipos de sonido distintos | 1 | 2 | 9 | 9 | 9 |
| Cambios de ambiente cada 10 min (media) | 0 | 7,7 | 15,0 | 17,3 | 62,3 |
| Cambios en los 10 min más movidos / media en la zona de dormir | 0 / 0 | 13 / 6,1 | 27 / 9,5 | 28 / 12,3 | 89 / 46,4 |
| Tramo más largo con el mismo sonido (min) | 30 | 2,5 | 2,5 | 2,5 | 0,8 |
| Variación espectral (dB) | 1,2 | 3,3 | 7,7 | 6,8 | 9,0 |
| Monotonía en 30 min / en la zona de dormir (%) | 93 / 86 | 18 / 15 | 11 / 23 | 11 / 16 | 9 / 10 |
| Zona de dormir (15 min): pico de eventos en 50 ms (dB) | 13,8 | 22,1 | 8,5 | 8,8 | 8,8 |
| Zona de dormir (15 min): "sustos" | 30 | 201 | 0 | 0 | 0 |

Los sustos de B son los chasquidos de la lareira de 7541a9e, que no estaban limitados (las listas "guía" cierran con
9-10 planos de lareira y lluvia; con la lista alterna, 72 sustos). Los de A, los goteos del alero de 7541a9e.

## 4. Qué dicen las medidas

1. **La voz no se degrada con ningún ambiente** (SIG 3,57-3,62 en las cuatro). DNSMOS BAK y OVRL bajan con cualquier
   fondo por diseño (se entrenó para puntuar supresores de ruido, https://ieeexplore.ieee.org/document/9746108: el
   mejor fondo para él es el silencio), así que D gana siempre y la medida solo dice cuánto "cuesta" el ambiente, no
   si ayuda a dormir. A cuesta más (fondo en el 100 % del tiempo y el más cercano a la voz, 15,9 dB por debajo); C
   cuesta algo más que B porque tiene sonido en más tiempo, pero con cada sonido más lejos de la voz (22,2 dB de
   mediana).
2. **El WER del texto largo mide un defecto de Whisper, no el ambiente.** En la zona de dormir, Whisper se salta frases
   enteras tras los silencios largos: con voz sola (D) borra 31 de 77 palabras y solo reconoce mal una ("Pouco" →
   "ouco", igual en las cuatro opciones). Con lluvia continua (A) se salta solo 2 palabras, con B y C 11-14: el
   ambiente rellena el silencio [S]. El WER frase a frase (cada frase cortada con 0,3 s de margen) evita ese defecto
   y da **0,018-0,026 en las cuatro opciones**, muy por debajo de la puerta del pipeline (0,06): los errores son casi
   los mismos con y sin ambiente (variantes ortográficas de Whisper: "á outra", "ó pé", "alousa"). El ambiente solo
   añade 1-2 palabras átonas perdidas en 271: un "e" bajo la lareira o la lluvia (A, B y C) y "ao pé" → "OPE" bajo
   los pájaros de la aldea (C). La QA de `longo.py` ya mide así el vídeo largo (`qa.asr_por_frases`, commit
   a0cecf5), porque la pieza VOZ encontró el mismo defecto.
3. **El murmullo de gentío no se entiende**: Whisper no transcribe nada en 2 de 3 semillas de 40 s de `xente` solo (a
   −20 LUFS, más fuerte que en el vídeo) y en la tercera alucina 8 palabras sin sentido ("as causas causas causas...
   ¿non?") con confianza baja (logprob medio −1,15). Las mismas frases del banco en seco las transcribe perfectas.
4. **Monotonía: A es monótona por construcción** (93 % de pares de ventanas que suenan igual en 30 min, un solo
   sonido 30 min seguidos); **C la resuelve** (9-11 %, 9 sonidos, nunca más de 2,5 min el mismo); B queda en medio
   (2 sonidos, 18 %). En la zona de dormir C sube a 23 % con la lista corregida, porque el cierre ("Chove na lousa")
   mantiene lluvia y lareira 2,5 min: es lo que se busca al final.
5. **Lo contrario de la monotonía también se mide**: con una lista que alterna sonido y voz limpia en cada plano, C
   cambia de ambiente cada ~9 s de media (62 cambios cada 10 min, 46 en la zona de dormir): eso es un parpadeo, no
   variedad [S]. Lo decide la lista de planos, no el código; por eso la guía pide bloques por escena y respiros
   limpios, `son.tramos_de_planos` no corta el sonido en un inserto neutro de menos de 20 s entre dos planos con el
   mismo sonido, y la QA avisa con más de 30 cambios en 10 min en el gancho o más de 10 en la zona de dormir (umbrales
   fijados por Claude a la vista de estas simulaciones [S]). Hasta mi primer intento de lista "según la guía" (guia1)
   se pasó: 78 % del tiempo con sonido y 12,3 cambios cada 10 min al dormir; la QA lo avisa. La lista corregida
   (31 % de planos limpios, bloques de 3-7 planos y respiros de 3-4) queda en 9,5 al dormir.
6. **Nada sobresalta al dormir en C**: 0 sustos en 15 min de zona de dormir y picos de 7-9 dB sobre el fondo, frente
   a 30 sustos de A (goteos del alero de 7541a9e) y 72-201 de B (chasquidos de la lareira de 7541a9e).

## 5. Decisión

**Recomendación: C**, que es lo que hace ya `longo.py` por defecto (`ambiente: escena`), con la lista de planos
escrita según [`guia-son.md`](guia-son.md). Es la única opción que cumple a la vez D13 y D14: sonido de cada escena
(9 tipos), voz limpia donde la imagen no tiene sonido, sin fondo constante, sin monotonía (9-11 % frente al 93 % de
A), murmullo ininteligible en los gentíos, 0 sustos en la zona de dormir y, con una lista según la guía, un ritmo
de cambios que no parpadea (9,5 cada 10 min al dormir). Lo paga con un fondo presente más tiempo
que B (DNSMOS OVRL 3,02 frente a 3,16) y 1-2 palabras átonas de 271 que Whisper pierde (WER por frase 0,026 frente a
0,018 sin ambiente).

Condiciones y cosas abiertas:

1. **Manda el oído del promotor.** Si prefiere A (lluvia continua, que es lo que le gustó en la muestra anterior) o D,
   se cambia en la ficha del tema (`ambiente: choiva2` o `ningun`) sin tocar código. Si C le suena demasiado cambiante
   en la muestra, recordar que el fragmento está comprimido (cambia cada ~10 s; en el episodio, cada 1-3 min).
2. **Nivel**: la curva del embudo (`curva.py`, `ambiente_db`, del orquestador) deja el ambiente del gancho 8 dB por
   debajo del de la zona de dormir; con los niveles del catálogo, el gentío del gancho suena a −34 dB bajo la voz (solo
   en las pausas). Si el promotor lo quiere más presente en el gancho, subir el primer nodo de la curva (p. ej. −8 → −5),
   no los niveles del catálogo.
3. **% de voz limpia**: lo decide la lista. Objetivo de la guía: 30-45 % de planos limpios (con el 31 % de la lista
   corregida, el 28 % del tiempo queda sin ambiente) y ≤ 10 cambios cada 10 min al dormir; la QA de `longo.py` da
   `pct_voz_limpa`, `cambios_por_10min`, `cambios_max_en_10min` y avisos.
4. Si se quisiera el carácter de B (solo lluvia y lareira), hacerlo con el código nuevo (lista con solo `choiva` y
   `lume`), no con el de 7541a9e: los sustos de B vienen de su lareira sin limitar.

## 6. Límites de estas medidas

- Nadie ha escuchado nada. DNSMOS no está hecho para ambientes buscados; el WER es de un ASR, no de una persona; los
  "sustos" y la "monotonía" son métricas definidas por Claude para esta pieza (en `scripts/medidas_son.py`), sin
  validar con oyentes.
- Las listas de planos del fragmento y del episodio son inventadas; el episodio simulado no tiene voz.
- Las voces "de mujer" del murmullo son la voz de Brais con tono y formantes subidos por remuestreo (no se instalaron
  las voces VITS de Nós: ver `aprendizajes/son.md`).
- La voz del fragmento usa Cotovía 0.5 (el pipeline pasó después a la "nova"); da igual para comparar sonidos.

## 7. Ficheros

- Código: `herramientas/pipeline/son.py` (catálogo, `ambiente_escena`, `tramos_de_planos`), `son_xente.py` y
  `son_datos/xente-banco.ogg` (banco del murmullo), `longo.py` (`SON_PALABRAS`, `son_do_plano`, etapa 6_son).
- Scripts de esta pieza: `scripts/` (`fragmento.py`, `voz_fragmento.py`, `opcions.py`, `medir.py`, `medidas_son.py`,
  `episodio.py`, `catalogo.py`, `mostra.py`).
- Medidas: `medidas/fragmento.json` (incluye las transcripciones de Whisper) y `medidas/episodio.json`.
- Muestras: `mostra-opcions.m4a`, `mostra-catalogo.m4a` (índice en `README.md`).
