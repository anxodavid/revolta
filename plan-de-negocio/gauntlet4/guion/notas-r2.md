# Notas do guion v2, rolda 2 · "As meigas de verdade" (≈ 12 min)

Guionista do Gauntlet 4 (axente Claude), 03-10-2026. Rolda curta pedida polo orquestrador despois de que a r1 gañase:
o crítico A elixiu a cegas a v2, con 31 puntos fronte a 18 (`veredictos/guion-r1-cego.md`), e o crítico B deu GAÑA
condicionado a 15 substitucións (`veredictos/guion-r1-lingua-veracidade.md` §7). As substitucións aplicounas un script
(`scripts/aplicar_r2.py`), e o resultado das de B é idéntico byte a byte á copia que deixou o crítico
(`$SCRATCH/criticoB-r1/guion-r1-substituido.txt`). As melloras de A escribinas eu. Ningunha persoa o revisou.

## 1. Cambios

### Lista pechada do crítico B (aplicada literal)

| # | Onde | Aplicada | Nota |
|---|---|---|---|
| B1 | S7 "Abondaría…" | Si | — |
| B2 | S13 "O que se contou de Dorotea…" | Si | Despois engado S14 (A2) |
| B3 | S17 "noticia dunha lista" | Si | Por iso non se aplica A8 |
| B4 | S23 "Unha testemuña oíu murmurar…" | Si | — |
| B5 | S24 "E contou que María…" | Si | — |
| B6 | S25 "Pensemos nela alí…" | Si | — |
| B7 | S46 "acabaron noutro sitio" | Si | — |
| B8 | S48 "meigas galegas" | Si | — |
| B9 | S56 "Pensemos nela diante de quen pregunta…" | Si, e despois substituída | A3 cámbiaa por "Diante dela, alguén preguntaba, e alguén escribía": así non hai dous "Pensemos nela" seguidos, e a escena queda concreta sen fórmula |
| B10 | S54 "Que á nai acudía…" | Si | — |
| B11 | S63 "Alí, dixo,…" | Si | — |
| B12 | S65-S66 "non nos chegou… a noticia da lista" | Si | — |
| B13 | Quitar "Nai e filla eran as de Vilalba" | Si | — |
| B14 | S74 "aquelas mulleres eran necesarias" | Si | A1 move a frase detrás das liortas, co mesmo texto ("para Pousa" en vez de "Para el") |
| B15 | Descrición da ficha v2: "a noticia dunha lista" | Si | — |

### Melloras do crítico A

| # | Mellora | Aplicada | Como ou por que non |
|---|---|---|---|
| A1 | Remate documental: Sarmiento co argumento das mulleres necesarias, Feijoo como última peza e a viraxe en parágrafo propio | Si | P24 remata nas liortas → "E, con todo, para Pousa aquelas mulleres eran necesarias…" → Sarmiento ("Xa no século dezaoito…"); P25: "No mesmo século, o frade Benito Xerónimo Feijoo…"; P26 só: "E aquí deixamos os papeis. Desde agora…" |
| A2 | A tese do gancho di máis do que sabemos | Si, sobre B2 | B2 xa a arranxa ("O que se contou de Dorotea…"); engado "As palabras que ela sabía, esas non as coñecemos", que anuncia o que confirma o peche. O documento só di "algunas palabras que savía" |
| A3 | A fórmula de imaxinar | Si | S25: "Pensemos nela alí…" (B6). S56: "Diante dela, alguén preguntaba, e alguén escribía". S64: "Pensemos nunha noite curta de xuño: a auga fría da fonte, e uns ollos…". Non uso "imaxinémola": a porta de estilo veta a familia de "imaxinar" e o orquestrador pediu a forma de B |
| A4 | Un só nome para cada xustiza | Si | "Civil" para a secular, como en F077 (Arquivo), F137 e F042 (Pousa): "a civil, a eclesiástica e a Inquisición" → "Os xuíces civís foron moito máis duros" → "nos procesos civís da Real Audiencia". Fóra "xustiza ordinaria", "xustiza do rei" e "xustiza real" (S30 di agora "con outros procesos por bruxería da Real Audiencia", sen o "uns trinta", que era da "xustiza real"). Dúbida para o crítico B en §3 |
| A5 | A pregunta central en voz alta | Si | "…e preguntarnos de quen son, de verdade, esas palabras" (sen signo de interrogación). Págase en "todas quedaron escritas por outra man" |
| A6 | A orde do tempo na zona de durmir | Si | "Outra noite, nunha cociña de aldea…" |
| A7 | A ponte cara ao conxuro | Si, con cambio | "…quedou sen o máis importante" en vez de "perdeu": a porta de veracidade trata "perdeu" como léxico de desenlace (`veracidade.DESENLACE`) e marcaría a frase |
| A8 | O anzol da lista con tensión | Non | Volvería contar o testemuño como feito ("uns veciños espreitaron… e apuntaron"), o que B3 e B12 corrixen ("noticia dunha lista") |
| A9 | Peche que arrola: "…e dos libros outra vez á aldea" | Si | — |
| A10 | Antecedentes: "a aquelas queimadas", "copias do conxuro" | Si | — |
| (fóra da lista) | Clixé "estreitar os lazos de amizade" | Si | Queda "para animar os corazóns" (F268) |
| (fóra da lista) | Clixé "a temida Inquisición" | Non | É a formulación de F039 (Valor Bravo) e B pediu non tocala salvo o ámbito (B8) |

### Ficha v2

- B15 aplicada na descrición.
- `curva_capitulos: ["Auga, digo, leite", "As respostas nas preguntas", "Chove na lousa"]`: os capítulos que abren a
  transición, a calma e o durmir (commit 562ed3c). Os nomes dos capítulos non cambian.

## 2. Medidas (`scripts/medidas.py --fases-cap 1,3,5`)

| Medida | r1 | r2 |
|---|---|---|
| Palabras / frases | 1.602 / 109 | 1.628 / 108 |
| Duración estimada (ritmo da v1 por fase) | 11:50 | 12:00 |
| Comezo dos capítulos | 1:32 · 3:04 · 3:52 · 5:15 · 7:55 | 1:41 · 3:13 · 4:02 · 5:22 · 8:04 |
| Atribucións por 100 palabras, parte esperta | 0,88 | 1,04 (B4 e B11 engaden "oíu murmurar" e "dixo", que pide o rigor; a v1 tiña 2,0) |
| "segundo" | 1 | 1 |
| Frases > 28 palabras | 0 | 0 |

## 3. Portas e dúbidas

- **Portas:** ver [`porta_texto-r2.json`](porta_texto-r2.json) e a sección 4.
- **Dúbida para o novo crítico B (A4):** "Os xuíces civís foron moito máis duros" reformula F040, que di "xustiza
  ordinaria" (Valor Bravo: "La jurisdicción ordinaria persiguió y mató a muchas brujas"). Para o público, "civil" e
  "ordinaria" nomean aquí a mesma xustiza secular fronte á eclesiástica e á Inquisición. Se o crítico o ve como cambio
  de atribución, a alternativa é "a ordinaria" nas tres frases (S47, S49 e S50).

## 4. Resultado das portas (`longo.py --so-texto`, 03-10-2026, 05:21 UTC, con `candado.sh --prioridade`)

| Porta | Resultado |
|---|---|
| Lingua (LanguageTool gl-ES + hunspell) | **0 avisos** |
| H1 | **57 de 57** nomes e cantidades no dossier da ficha v2 |
| Estilo | **Correcto**: sen díxitos, signos, preguntas nin "imaxina"; aviso e fórmula literais |
| Veracidade | 108 frases; **5 marcadas, 0 sen xustificar**: S12, S13 (B2), S16, S18 e S20 (A5), todas tecido do gancho con entrada en [`excepcions-r2.yaml`](excepcions-r2.yaml). As preventivas de B (S17 e S24) non fixeron falta: o NLI aprobou as dúas frases |
| Curva | `curva_capitulos` atopa os tres capítulos: nós en [0, 263, 628, 1.177, 1.628] palabras |
