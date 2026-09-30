# Comparación de guiones: LLM local desatendido (ronda 2) frente a Claude en modo manual (ronda 1)

Fecha: 29-09-2026. Mismo tema (`herramientas/pipeline/temas/irmandinos-apertura.yaml`), mismos controles automáticos.
La tabla la genera `herramientas/pipeline/comparar.py` (LanguageTool, estilo y H1 se miden de nuevo sobre cada guion;
el ASR es el que midió la etapa QA de cada ejecución sobre su propia mezcla).

- **Ronda 1**: guion, corrección y guion visual escritos por Claude Opus 5.5 en modo `manual` (no desatendido;
  ver `ronda1/qa.md`). Prompt único (`prompts/guion.md` de entonces), 440 palabras pedidas.
- **Ronda 2**: `pipeline.py --llm openai` con **EuroLLM-9B-Instruct-2512 Q4_K_M** (Apache-2.0) en llama-cpp-python,
  arrancado por el propio pipeline, en CPU, guion por bloques (`prompts/bloque_*.md`), 500 palabras pedidas.
  Prompts, respuestas y metadatos de las 28 llamadas: `execucion/llm_cache/`.

| Control | Ronda 1: Claude Opus 5.5 (manual) | Ronda 2: EuroLLM-9B local (desatendido) |
|---|---|---|
| Palabras | 475 | 492 |
| Avisos LanguageTool gl-ES (medidos agora sobre o guion final) | 2 | 11 |
| Nomes/cantidades sen ancorar no dossier (H1) | 0 | 1 |
| Cifras / signos prohibidos / preguntas | 0 / 0 / 0 | 0 / 0 / 0 |
| Aviso e fórmula literais | True / True | True / True |
| Frases fóra de 8-25 palabras | 0 | 9 |
| Máx. nomes propios novos por 110 palabras | 4 | 2 |
| WER ASR mestura (voz + choiva) | 0.025 | 0.026 |
| WER ASR voz soa | 0.086 | 0.102 |
| Frases con WER > 0,5 | 0 | 0 |
| Sincronía subtítulos (%) | 100.0 | 100.0 |
| Duración do vídeo (s) | 240.79 | 203.83 |
| Ritmo global (palabras/min) | 123.5 | 151.5 |

**Avisos LanguageTool, Ronda 1: Claude Opus 5.5 (manual):**

- `GENERAL_VERB_AGREEMENT_ERRORS` Posíbel erro de concordancia verbal. — "...erán, historia de Galicia para durmir.  Esta noite imos contar a historia dos irmandiños. Duran..."
- `GENERAL_GENDER_AGREEMENT_ERRORS` Posíbel erro de concordancia de xénero. — "...ñas formaran unha irmandade e camiñaran xuntos cara a Compostela. Aquela primeira irmandade..."

**Sen ancorar (H1), Ronda 1: Claude Opus 5.5 (manual):** ningún

**Avisos LanguageTool, Ronda 2: EuroLLM-9B local (desatendido):**

- `HUNSPELL_RULE` Atopouse un posíbel erro ortográfico — "...artesáns uníronse contra os señores das fortaleiras. A xente común botou abaixo torres con ..."
- `HUNSPELL_RULE` Atopouse un posíbel erro ortográfico — "... de xente diversa derrubou castelos. As fortaleiras perderon fronte á unión popular.  Isto ..."
- `GENERAL_VERB_AGREEMENT_ERRORS` Posíbel erro de concordancia verbal. — "...Serán, historia de Galicia para durmir. Esta noite viaxamos no tempo para descubrir unha historia e..."
- `GENERAL_NUMBER_AGREEMENT_ERRORS` Posíbel erro de concordancia de número. — "... a revolta dos irmandiños, un movemento sen precedentes que entre mil catrocentos sesenta e set..."
- `GL_BARBARISM_REPLACE` 'ceo' é un xenismo. É preferíbel dicir "director executivo" — "...onde o lume ardeu en silencio.  Cando o ceo se fundía coas chairas, os homes labrab..."
- `GL_BARBARISM_REPLACE` 'ceo' é un xenismo. É preferíbel dicir "director executivo" — "...tres os homes camiñaban xuntos baixo un ceo que parecía esvarar sobre os tellados d..."
- `HUNSPELL_RULE` Atopouse un posíbel erro ortográfico — "... desfacía en anacos. A auga goteaba das teituras rachadas, mesturándose coa area dos cam..."
- `HUNSPELL_RULE` Atopouse un posíbel erro ortográfico — "...a nobreza que souberon guiar o lume dos fachós entre as pedras, xuntáronse nunha soa v..."
- `HUNSPELL_RULE` Atopouse un posíbel erro ortográfico — "... camiños empedrados, mentres o lume das antorchas iluminaba os rostros cansos de todos el..."
- `GL_BARBARISM_REPLACE` 'ceo' é un xenismo. É preferíbel dicir "director executivo" — "...os de todos eles, unidos baixo un mesmo ceo roto polo ruído constante da caída dos ..."
- `HUNSPELL_RULE` Atopouse un posíbel erro ortográfico — "... caída dos tellados e as paredes que se esgadanaban coma se o mundo tentase esquecer o seu ..."

**Sen ancorar (H1), Ronda 2: EuroLLM-9B local (desatendido):** "mil catrocentos sesenta e sete un"


## Lectura (hecha después, por Claude, fuera del pipeline)

Los números dicen menos de lo que parece. El ASR y la sincronía salen iguales porque miden la voz, no el texto. Lo que
separa los dos guiones es la calidad del texto, y ahí la diferencia es grande:

1. **Gallego.** 11 avisos de LanguageTool frente a 2. Unos 7 son errores reales: *fortaleiras* (dos veces, no
   existe), *teituras*, *fachós*, *antorchas* (castellanismo; en gallego, *fachos*), *esgadanaban* y una
   concordancia. Los 3 avisos por *ceo* son falsos positivos de LanguageTool, que lo toma por "CEO". La corrección
   automática por párrafo **se rechazó las 5 veces**: el LLM devolvía textos con más avisos que el original (de 4
   pasó a 24 en un caso). El control funcionó, pero no arregló nada.
2. **Datos inventados que H1 no ve.** "Botou abaixo torres con paus e pedras", "os nobres tiñan poder, pero a
   irmandade venceu" (el dossier dice que los señores volvieron en 1469), "os mariñeiros cos seus remos convertidos
   en armas", "os burgueses coa súa contabilidade de loitas", "as chaves da Rocha Forte caeron" y "unidos por un
   segredo". No llevan nombres ni cifras, así que el control H1 no puede cazarlas. Haría falta un juez H2, que no
   está implementado. El único "no anclado" que marca H1 ("mil catrocentos sesenta e sete un") es un **falso
   positivo** del tokenizador de `ancoraxe.py`, que junta la fecha con el "un" de "un grupo".
3. **Estructura y ritmo.** El gancho es pobre ("A Rocha Forte caeu baixo as súas mans. Un exército de xente
   diversa derrubou castelos") y el relato no cuenta lo que pedía el fragmento (la vida bajo los señores, los
   tributos, el señor juez), porque el LLM eligió los hechos 5, 7, 10, 4 y 6. Los párrafos repiten imágenes
   (lluvia, viento, piedras, fuego) y 9 frases quedan fuera de 8-25 palabras (7 pasan de 25; la más larga tiene 58). El ritmo global
   sale en 151 palabras/min frente a 123: hay menos frases y, por tanto, menos pausas. Para dormir es demasiado
   rápido.
4. **Guion visual.** Aquí el LLM local sí cumplió la instrucción nueva ("personas haciendo cosas"): 24 prompts con
   gente en acción. Coló escenas violentas o absurdas ("Crowds surround a burning keep", "Time-travelers stand
   before the ruins", "torture rack") y la puerta de imágenes las filtró en parte (hoguera, esqueletos). Ver
   `qa.md`.

**Conclusión:** con un LLM abierto de 9B en CPU, el pipeline ya es desatendido de verdad (un comando, 28 llamadas
al LLM local, 1,7 h de CPU de LLM para 3,4 min). El resultado lo rechazan sus propias puertas: NON PUBLICABLE por
lengua (11 avisos) y por H1 (un falso positivo). El guion no llega al nivel de la ronda 1. Es el cuello de botella
del canal desatendido: hace falta un modelo instruccional gallego mejor, un juez H2 y otra vuelta de prompts
antes de publicar nada. Esto encaja con la tesis de "fomentar mejores modelos en gallego" (reportar estos errores a
Nós).
