# Guía de sonido para la lista de planos (Gauntlet 3, pieza SON)

Para quien escriba la lista de planos del episodio (un agente Claude, hoy). Decisiones del promotor que la motivan:
**D13** (sonido por escena, tramos de voz limpia, nada de ruido constante) y **D14** (adaptarlo a la escena para que no
sea monótono; en un gentío, murmullo de voces que no se entiendan). Código: `herramientas/pipeline/son.py` (catálogo)
y `longo.py` (`son_do_plano`, `SON_PALABRAS`, etapa 6_son).

## 1. Qué poner en cada plano

Cada plano de la lista (`ESCENAS.json`) lleva un campo `son`:

```json
{"n": 12, "prompt": "Midsummer night, a small bonfire far away in a village field under a starry sky", "son": "lume+noite"}
{"n": 13, "prompt": "Close-up of an old court record on a wooden table, candlelight", "son": "limpa"}
```

- Un tipo del catálogo, o dos unidos con `+` (la segunda capa suena 3 dB más baja). Nunca más de dos.
- `"limpa"`: voz limpia, sin ambiente, garantizada (corta siempre el sonido). **Escríbelo siempre que quieras voz
  limpia.**
- Campo vacío o ausente: el pipeline deduce el sonido de las palabras del prompt (`SON_PALABRAS`) y puede poner uno
  (p. ej. "moonlight" → `noite`). Si no encuentra ninguno, el plano es **neutro**: voz limpia, salvo que sea un inserto
  de menos de 20 s entre dos planos con el mismo sonido; entonces el sonido del lugar sigue por debajo (la lluvia no
  para porque la imagen muestre unas manos). Esto evita que el ambiente se apague y vuelva en cada plano.
- El sonido tiene que estar **en la imagen**: lluvia solo si la imagen muestra lluvia (o una noche de lluvia tras la
  ventana), lareira solo si se ve fuego o brasas, gente solo si se ve un gentío. Si la imagen no tiene fuente de
  sonido: `limpa` si ahí debe oírse la voz sola; vacío si es un inserto breve dentro de una escena con sonido.

| `son` | Cuándo (lo que muestra la imagen) | Nivel bajo la voz* | Eventos (escasos y suaves al dormir) |
|---|---|---|---|
| `choiva` | lluvia sobre lousa, calle mojada, noche de lluvia tras la ventana | −18 dB | goteo del alero |
| `lume` | lareira, brasas, fuego, queimada | −21 dB | un leño que se asienta |
| `mar` | costa, ría, playa, barcas en el agua | −20 dB | de vez en cuando una ola mayor |
| `vento` | monte, carballeira o souto con viento, páramo | −23 dB (−24 al dormir) | una ráfaga más fuerte |
| `fonte` | fuente de piedra, regato, río, lavadoiro, molino de agua | −22 dB (−23 al dormir) | un gorgoteo |
| `xente` | feria, mercado, procesión, fiesta, reunión, taberna | −26 dB (−31 al dormir) | la gente "respira": más y menos voces |
| `noite` | exterior de noche: estrellas, luna, campo en verano | −25 dB (−27 al dormir) | muy de vez en cuando una curuxa lejana |
| `aldea` | aldea de día, prados con vacas, hórreos, huertas | −24 dB (−28 al dormir) | un chocallo de vaca lejano |
| `campas` | catedral (Compostela), iglesia, monasterio, campanario | −24 dB (−28 al dormir) | los toques, en grupos de 2-9 |

\* LUFS respecto a la voz (−17 LUFS), **antes** de la curva del embudo (`curva.py`, `ambiente_db`: −8 dB en el
gancho, −3 al final de la transición, 0 a mitad del episodio y +1,5 al final). Entre paréntesis, con la bajada propia
del tipo en la zona de dormir (`DURMIR_DB`). Ejemplo: `xente` en el gancho suena a −26 − 8 = −34 dB bajo la voz (se
oye en las pausas, casi nada debajo de la voz).

Combinaciones útiles: `lume+noite` (hoguera de San Xoán a lo lejos), `fonte+noite` (fuente de noche), `lume+choiva`
(cocina con lareira en noche de lluvia: la combinación que el promotor eligió en la muestra A/B), `mar+vento` (costa
con viento).

## 2. Cuándo dejar voz limpia (`"limpa"`)

1. **Aviso y reclamo** ("A voz que vas escoitar é sintética..." e "Isto é Cousas de Galiza para durmir."): siempre
   limpios.
2. **Datos clave del gancho** (el verso del conxuro con su autor, nombres, cifras): limpios o con el ambiente del plano
   anterior apagándose, para que se entiendan.
3. **Planos sin fuente de sonido que abren un tramo limpio**: legajos, manuscritos, retratos, archivo a la luz de la
   vela, interiores sin fuego (un inserto de pocos segundos dentro de una escena con sonido puede ir vacío, ver §1).
4. **Respiro**: no más de ~4 min seguidos con ambiente; tras ese tiempo, al menos un plano limpio. El pipeline avisa en
   la QA (`son.escena.avisos`) si hay más de 5 min seguidos.
5. Objetivo orientativo: **30-45 % de los planos limpios** en el conjunto del episodio (el % de voz limpia sale en la
   QA, `pct_voz_limpa`, y en `informe.md` está lo que midió cada opción).

## 3. Contra la monotonía (lo que hace el código y lo que tiene que hacer la lista)

El código ya varía cada tramo (semilla y parámetros propios, intensidad que respira, eventos al azar cada vez más
escasos y suaves, fundidos largos de 3 s en el gancho a 8 s al dormir, tramos largos partidos en trozos de 2,5 min
distintos y un tope del ambiente respecto a la voz). La lista tiene que poner la variedad **entre escenas**:

- Cambiar de tipo con el capítulo y con el lugar (aldea → fuente → costa → noche → lluvia), no repetir el mismo tipo
  en más de ~2 capítulos seguidos salvo en el cierre ("Chove na lousa").
- **Agrupar por escena**: un bloque de 3-6 planos seguidos con el mismo sonido (≈ 1 min) y 2 planos de respiro
  limpio, mejor que alternar sonido y voz limpia en cada plano. Los planos seguidos con el mismo `son` se funden en un
  solo tramo continuo, sin cortes.
- **Ritmo de cambios** (cada entrada, salida o cambio de sonido cuenta uno): hasta ~30 cada 10 min en el gancho y la
  transición (planos de 5-10 s) y **≤ 10 cada 10 min en la zona de dormir**. La QA avisa si se pasa
  (`son.escena.avisos`, `cambios_max_en_10min`). En la simulación de 30 min, una lista según esta guía dio 27 cambios
  en los 10 primeros minutos y 9,5 cada 10 min al dormir; una lista que alterna en cada plano dio 89 y 46 (un cambio
  cada ~9 s: eso ya no es variedad, es un parpadeo; ver `informe.md`).
- En la **zona de dormir** (desde la mitad del episodio) elegir los tipos más mansos: `choiva`, `lume`, `mar`,
  `fonte`, `noite`. `xente`, `campas` y `aldea` se pueden usar si la imagen lo pide (el código los baja 4-5 dB y los
  espacia), pero nunca como fondo largo.
- Nada que sobresalte al dormir: no pedir tormentas, gentío cercano ni repique de campanas. El código limita el pico
  de cada evento respecto a su fondo (5-6 dB al dormir) y el ambiente respecto a la voz (12 dB por debajo).

## 4. Si falta `son`: deducción por el prompt

`longo.son_do_prompt` busca palabras en inglés del prompt, en este orden de prioridad (gana la primera): `lume` (fire,
hearth, embers, bonfire...), `choiva` (rain, drizzle...), `mar` (sea, waves, coast, beach...), `fonte` (fountain,
stream, brook, river, washing place...), `xente` (crowd, market, village fair, procession, festival, tavern...),
`campas` (church, bells, cathedral, monastery, cloister...), `noite` (night, moon, stars...), `aldea` (village,
cows, meadow, farm, fields...), `vento` (wind, storm, forest, woods, hillside...). En un interior (kitchen, room,
table, portrait, close-up, document...) no pone `aldea` ni `vento`; a `lume`, `fonte` o `mar` de noche en exterior les
añade `noite`. En el fragmento de prueba acertó 14 de 15 planos; el fallo fue un plano que la lista quería limpio.
