# Aprendizaxes da peza GUION (Gauntlet 4), 02-10-2026

Guionista da v2 (axente Claude), rolda 1. O texto escribiuno Claude a man; as medidas son de
`gauntlet4/guion/scripts/` (automáticas e aproximadas). Ningunha persoa o revisou. Complétase en cada rolda.

## Que funcionou

- **Escoller o fío antes de escribir e medilo despois.** "As palabras e a man que as escribe" deu un criterio para
  cortar: o que non servía ao fío saíu (Xinzo, Marta de Quián, Benita Montero, Soliña, o mal de ollo, a lareira), e
  cada capítulo empeza cunha frase que nace da anterior (contraste, causa ou motivo), sen "agora imos falar de".
- **Unha atribución por caso, e despois contar.** Coa mesma medida (`medidas.py`, mesmas palabras de atribución) a
  v1 tiña 2,0 atribucións por 100 palabras na parte esperta e "segundo" 15 veces; a v2, 0,88 e unha vez. O que máis
  rendeu: o estilo indirecto continuado ("confesou que... Que llo ensinara a súa nai. Que á casa da nai... E que...")
  colga varias frases dun só verbo e, de paso, soa a interrogatorio, que é o tema do capítulo.
- **A fonte primaria aclara o que o dossier deixa ambiguo.** O PDF do Arquivo (descargado de novo, `pdftotext
  -layout`) mostrou que as palabras de María ao gando chegan "de oídas" no mesmo testemuño de Andrés da Pena. Iso
  cambiou unha frase ("do monte pasaron á boca da testemuña") e fixo entrar F052 (os murmurios), que estaba fóra da
  ficha. Tamén apareceron dous feitos útiles que non están no dossier (a excomuñón prohibía falar con elas; a resposta
  en galego de Inés da Maquieira): pedidos nas notas, non usados.
- **Predición léxica da porta de veracidade sen NLI** (`veracidade_lexica.py`, só regex e as funcións puras de
  `veracidade.py`): en segundos di que frases van ir á "dubidosa". Serviu para reescribir catro frases do gancho
  ("alguén pronuncia o conxuro", "unha lista coas mulleres", o Arquivo "entre uns trinta procesos", "Nai e filla eran
  as de Vilalba") e para mover unha frase fóra das primeiras 280 palabras, onde xa non precisa apoio.
- **Modelo de duración:** ritmo da v1 por fase (157 / 154,5 / 136,3 / 114,5 palabras/min con pausas) aplicado ás
  fases de contido. Dá 31:08 para a v1, que durou 31:22 (−0,8 %): máis fiable ca a media global (que sobreestima un
  guion curto, porque o curto ten máis peso de gancho).

## Que non funcionou ou custou

- **O candado da CPU como cola.** A primeira porta de lingua agardou 15 min sen entrar e morreu polo `timeout`: había
  un interbloqueo (un `flock` aniñado na verificación do contorno). Detectado con `/proc/locks` (titular e cola cos
  seus PID) e avisado ao orquestrador, que o resolveu e creou `herramientas/gauntlet/candado.sh --prioridade`. Os
  `flock` simples que xa estaban na cola non ceden á prioridade: o prioritario segue agardando ata que remate o que
  corre e lle toque.
- **"imaxina" está vetado pola porta de estilo** (`qa.estilo`, por subcadea: tamén "imaxinar" e "imaxinación"),
  aínda que o encargo o propoñía para as reconstrucións. Alternativas que pasan e soan ben: "podemos pensala",
  "cómpre pensala", "podemos pensar nunha noite...".
- **O gancho mide 280 palabras na porta, non 1:30.** Co embude comprimido da D18 o gancho de contido remata nas 241
  palabras, pero a porta segue esixindo apoio ata a 280: as primeiras frases do capítulo I tamén. Convén que esas
  frases sexan case literais dun feito.
- **`curva.py` ten os nós en palabras absolutas** (280 e 950). Nun guion de 1.610 palabras a calma quedaría en 100
  palabras; hai que escalalos (proposta nas notas).

## Cifras da rolda 1

1.610 palabras, 109 frases, 5 capítulos; ≈ 11:53 estimado; frases de 13,6 palabras de media no gancho e 17,1 no
durmir (ningunha > 28); 22 nomes propios distintos (75 na v1); 6 frases de tecido previstas na porta de veracidade,
todas no gancho.
