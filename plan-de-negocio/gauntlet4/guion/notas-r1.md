# Notas do guion v2, rolda 1 · "As meigas de verdade" (≈ 12 min)

Guionista do Gauntlet 4 (axente Claude), 02-10-2026. **Borrador das notas: a sección 4 (portas) complétase cando
remate a porta de texto**, que está na cola do candado da CPU. O texto escribiuno Claude a man; as medidas son de
`scripts/medidas.py` e `scripts/veracidade_lexica.py` (automáticos, aproximados). Ningunha persoa o revisou.

## 1. Que se entrega

| Ficheiro | Que é |
|---|---|
| [`plan-r1.md`](plan-r1.md) | Plan escrito antes do guion: pregunta, fío, arquitectura, embude, persoas e momento visible |
| [`guion-r1.txt`](guion-r1.txt) | O guion: 1.602 palabras, 109 frases, 5 capítulos + o inicial |
| [`feitos-r1.md`](feitos-r1.md) | Cada frase cos seus feitos (F###) e a lista de frases de tecido para o crítico B |
| `excepcions-r1.yaml`, `porta_texto-r1.json` | Cando remate a porta (sección 4) |
| [`scripts/`](scripts/) | `medidas.py`, `veracidade_lexica.py` (predición sen NLI), `lingua_rapida.py`, `porta-r1.sh` |
| `herramientas/pipeline/temas/meigas-de-verdade-v2.yaml` | Ficha v2: mesmo dossier da v1 + F052; `palabras: 1600`, `duracion_s: [600, 840]`, capítulo inicial, autoría e descrición novas |

## 2. Medidas (v1 e v2 co mesmo script e o mesmo criterio)

Fases por capítulos: gancho = capítulo inicial; transición = I e II; calma = III e IV; durmir = V (na v1, o durmir
empeza en "Á beira da lareira"). Minutos co ritmo medido da v1 por fase (157 / 154,5 / 136,3 / 114,5 palabras/min
con pausas, `gauntlet3/veredictos/tribunal-final.md` §4); ese modelo dá 31:08 para a v1, que durou 31:22 (−0,8 %).

| Medida | v1 (`gauntlet3/guion/guion-r3.txt`) | v2 (`guion-r1.txt`) |
|---|---|---|
| Palabras / frases / capítulos | 3.952 / 240 / 8 | **1.610 / 109 / 5** |
| Duración estimada | 31:08 (real 31:22) | **≈ 11:53** (11:44 coa curva actual; 12:47 coa media da v1) |
| Comezo dos capítulos (estimado) | — | I 1:32 · II 3:04 · III 3:52 · IV 5:18 · V 7:59 |
| Aviso | 0:35 | 0:38 (palabra 100) |
| Palabras por frase: gancho / transición / calma / durmir | 13,8 / 17,5 / 17,1 / 16,6 | **13,6 / 14,4 / 14,8 / 17,1** (sobe cara ao sono) |
| Frase máis longa | 25 | 25 (ningunha > 28) |
| Atribucións por 100 palabras, parte esperta | 2,0 (35 en 1.747) | **0,88 (10 en 1.140)** |
| "segundo" | 15 | **1** (e na zona de durmir: "segundo a crenza") |
| Nomes novos por 100 palabras: gancho / transición / calma / durmir | 4,3 / 3,2 / 2,9 / 0,8 | **2,3 / 1,9 / 1,8 / 0** |
| Nomes propios distintos | 75 | 22 |
| Cantidades e anos por 100 palabras, parte esperta | 1,8 | 1,6 (transición 2,5: 1617, 1967, catrocentos, sete, trinta, dous mil un) |

**Atribucións.** Conto como tales: segundo, para o investigador, declara, dixera, contou, contaba, confesou, explica,
atopou, advertía, dixo. As 10 da parte esperta son unha por caso ou bloque (Dorotea leva dúas palabras nunha soa
estrutura, "declara que... dixera", como pide a nota de F008). Baixar de 0,8 obrigaría a quitar a atribución dun
testemuño ou dunha opinión (Valor Bravo, Pousa, Feijoo): non o fixen. Hai ademais marcas sen verbo ("Para el",
"culpábana"), que non conto.

## 3. Decisións

1. **D18 (12 min) mandou sobre o encargo de 30 min.** Quedaron fóra, porque non servían ao fío ou repetían función:
   Xinzo de Limia (o gato e a arracada), Marta de Quián, Benita Montero, María Soliña, a biografía de Feijoo, o mal de
   ollo, a lareira descrita e as cifras de 92 e 48. Elixín tres casos en profundidade (Vilalba, Cibreira, Campo
   Lameiro), o conxuro como marco (comezo, medio e fin) e a noite de san Xoán como arrolo.
2. **Fío: as palabras e a man que as escribe**, co emblema "auga, digo, leite" e o refrán da auga de sete fontes
   (plan §b). Págase dúas veces: o mesmo verso volve na queimada do peche, pero agora sabemos quen o escribiu e por
   que semellaba de ninguén; e o episodio sobre palabras remata onde rematan as palabras ("xa non fan falta palabras:
   só a chuvia na lousa").
3. **Tres bucles no gancho, escalonados:** a emenda de catrocentos anos (paga ≈ 2:40), o motivo polo que o conxuro
   semella de ninguén (≈ 3:30) e a lista da fonte (≈ 5:40). Sen pregunta con signo: a pregunta central formúlase como
   promesa ("imos buscalas no pouco que delas quedou escrito").
4. **Escenas e non resumos:** cada caso ten lugar, xente facendo algo e as palabras literais do documento ("auga, digo,
   leite", "coma un poldro bravo", "as respostas xa ían nas preguntas", "maldita a nai...", "pan, sal, auga nin
   lume"). A confesión de Cibreira vai en letanía de "que..." dentro dun só "confesou": soa a interrogatorio e evita
   repetir verbos de atribución.
5. **Reconstrucións: tres, unha por escena, explícitas e xenéricas:** "Podemos pensala alí, co gando arredor e o vento
   levando a medias o que dicía", "Cómpre pensala diante de quen pregunta e de quen escribe" e "Podemos pensar nunha
   noite curta de xuño...". A porta de estilo veta a subcadea "imaxina" (`qa.estilo`), así que non usei "imaxina" nin
   "podemos imaxinar" malia que o encargo os propoñía: saen "podemos pensar" e "cómpre pensala".
6. **Comprobado na fonte primaria** (PDF do Arquivo): as palabras de María ao gando e as de Dorotea son do mesmo
   testemuño (Andrés da Pena) e el sabíao "de oídas" ("oyó dizir y mormurar entre algunas personas vecinas"). Por iso
   S27 di "do monte pasaron á boca da testemuña", sen afirmar que a oíse el, e por iso entrou **F052** (os veciños
   murmuraban), que estaba con `ficha: false`: engadido á ficha v2 co seu ID nunha liña separadora.
7. **Lingua:** complemento directo de persoa sen "a" cos nomes comúns ("procesou alí varias mulleres", "procesou a
   María Cibreira e outras veciñas"); "coma" nas comparacións de igualdade e "como" en Sarmiento (corrección L1 da v1);
   nada de reflexivos impersoais que LanguageTool marcaba na v1 (comíase, sentábase...); ningún "O historiador
   Rodrigo" ao comezo de frase.
8. **Descrición pública da ficha v2 reescrita**: a da v1 falaba do gato de Xinzo, o mal de ollo, a lareira e Feijoo,
   que xa non están ou están doutro xeito. Que a revise o crítico B (é texto público).

## 4. Portas automáticas

*Pendente: a porta completa (`longo.py --so-texto`, ordes en `estado.md`) está na cola do candado da CPU en modo
prioritario. A predición léxica sen NLI (`scripts/veracidade_lexica.py`) marca 6 frases, todas no gancho (as
primeiras 280 palabras, onde toda frase precisa apoio): S12, S13, S14, S15, S17 e S19, que son o tecido do fío, o bucle
da emenda e a promesa. Despois do gancho, todas as frases con nome, tempo longo ou desenlace teñen coincidencia ≥ 0,8
cun feito ou cun par. H1: todos os nomes e cantidades están na ficha v2 (comprobado a man; a porta dirao).*

## 5. Dúbidas e peticións

1. **Feito novo que reforzaría o fío (para a peza DOSSIER, non o usei):** a excomuñón de Vilalba mandaba tamén que
   ninguén falase con elas: "y con el no ableis tratéis ni comuniquéis" (PDF do Arquivo, p. 16, [52 recto]). Con el, o
   peche de I podería dicir que as palabras tamén se lles negaron.
2. **A única voz propia en galego dunha acusada** que trae o PDF está en Campo Lameiro (p. 7, [22 recto], testemuño de
   Juan Linarinos): Inés da Maquieira responde aos veciños "o sapo que dicides eu teño na casa preso, foravos mellor
   telo na boca", e ameaza ("bos aves de ber e desear"). Non está no dossier e é unha ameaza (non vale para o sono),
   pero sería o pago perfecto do fío nunha parte esperta. Se o orquestrador o quere, que o verifique a peza DOSSIER.
3. **Curva da voz para 12 min:** `curva.py` ten os nós en palabras absolutas (gancho 280, transición 950, calma na
   metade). Con 1.610 palabras a calma quedaría en 100 palabras (950-1.050). Os límites de contido deste guion son:
   gancho 0-241, transición 241-602, calma 602-1.163 e durmir 1.163-1.610. Proposta para quen faga a voz: escalar os
   nós a esas palabras.
4. **Frases curtas (< 8 palabras): 12**, a propósito: o ritmo do gancho ("Parece de hai séculos.", "Vilalba, mil
   seiscentos dezasete.") e o arrolo ("Auga de sete fontes para o gando. E para elas, nin auga."). En `longo.py` non
   bloquean (só se informan).
5. **O "demo"** sae unha vez, en S55, dentro da confesión de Cibreira (≈ 4:40), lonxe da zona de durmir.
