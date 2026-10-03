# Guion v2 · rolda 2 · crítico B (lingua e veracidade)

Crítico B da peza GUION do Gauntlet 4: **axente Claude** con perfil de filólogo galego (norma da RAG) e verificador de
feitos. Non participei no guion nin no veredicto da rolda 1. 03-10-2026. Rolda curta: xulgo só as 29 frases novas ou
cambiadas de [`guion/guion-r2.txt`](../guion/guion-r2.txt) (1.628 palabras, 108 frases, md5
`24aed495d9f779807b5b4d7fd5844548`, o mesmo da copia conxelada que pasou a porta), co mapa
[`feitos-r2.md`](../guion/feitos-r2.md), as notas [`notas-r2.md`](../guion/notas-r2.md), as excepcións
[`excepcions-r2.yaml`](../guion/excepcions-r2.yaml) e a porta [`porta_texto-r2.json`](../guion/porta_texto-r2.json).
"SN" é o número de frase de `pipeline.partir`, o mesmo que usa a porta.

**Que fixo Claude e que é automático.**
- **Este axente Claude:** a comprobación das 15 substitucións (un script compara a táboa do §7 do veredicto r1 con
  `scripts/aplicar_r2.py`, rexenera r2 a partir de r1 e compara os md5); a comparación frase a frase de r1 e r2 (saen
  29 frases novas ou cambiadas, as mesmas do mapa); o cotexo de cada frase cos feitos de
  `gauntlet3/dossier/feitos.yaml` (busca por ID) e coa lista "Non dicir" (`dossier.md` §5); a lectura das fontes: o
  texto do PDF do Arquivo (p. 4-5, 11, 14 e 15, en `$SCRATCH/fontes/ARG-PDF.txt`) e os artigos de *El Español* (Valor
  Bravo) e *GCiencia* (Pousa), que baixei de novo con `curl` o 03-10-2026 e que gardo fóra do repo
  (`$SCRATCH/tmp/criticoB-r2-fontes/`) porque son material de terceiros; e o DRAG con `curl` (*civil*, *ordinario*,
  *preguntar*).
- **Automático:** as portas de texto (LanguageTool + hunspell, H1, estilo e veracidade con NLI), que pasou o construtor
  co candado sobre a copia conxelada (`$SCRATCH/guion/porta-r2.log`: md5 idéntico, lingua sen avisos, H1 57 de 57,
  estilo correcto, 5 frases marcadas e 0 sen xustificar). **Non as volvín pasar:** no YAML só cambio textos de
  xustificación, e a porta busca as excepcións pola frase.
- Ningunha persoa revisou este veredicto.

## Veredicto: **GAÑA** (sen substitucións)

| Condición | Resultado |
|---|---|
| As 15 substitucións do crítico B, literais | **Si.** B1-B14 no guion e B15 na ficha, letra por letra (§1). Despois, o construtor cambiou B9 e B14 por melloras do crítico A (A3 e A1), e as dúas manteñen o arranxo |
| 0 erros de feito nas 29 frases | **Cúmprese:** 0 G, 0 M e 0 L (§2) |
| 0 erros graves de lingua | **Cúmprese:** 0 G e 0 M; 3 L admisibles, que non piden cambio (§4) |
| Dúbida A4 | **"Civil" vale nas tres frases** (§3); "a ordinaria" sería peor |
| Excepcións | As 5 marcadas, aceptadas; reescribo 3 xustificacións pola numeración de r2 (§5) |
| Regras do tema | Cúmprense (final do §2) |

**Maior carencia** (non bloquea): en S56, «Diante dela, alguén preguntaba, e alguén escribía», o *ela* anterior é a
nai (S54). O oído resólveo ben, porque toda a serie depende de *confesou* e só Cibreira foi interrogada, pero é o único
pronome do bloque que obriga a pensar.

**O que melloraron as melloras de A sen custo de rigor:** a tese do gancho xa non promete palabras que non temos
(S13-S14); a pregunta central (S20) págase en S32 e S100; Sarmiento vai co argumento ao que serve e Feijoo queda como
charneira; hai un só nome para cada xustiza; e A8 quedou fóra con razón, porque volvería contar a lista como feito.

## 1. As 15 substitucións do crítico B

Proba (script deste axente): as 14 parellas B1-B14 de `scripts/aplicar_r2.py` son idénticas carácter a carácter ás da
táboa do §7 de [`guion-r1-lingua-veracidade.md`](guion-r1-lingua-veracidade.md); cada texto actual aparece unha soa vez
en `guion-r1.txt` (md5 `e14180a5…`, o que xulgou o crítico B r1); `aplicar_r2.py --so-b` dá un ficheiro idéntico á
copia do crítico (`$SCRATCH/criticoB-r1/guion-r1-substituido.txt`, md5 `bfdbd097…`); e a saída completa é idéntica a
`guion-r2.txt` (md5 `24aed495…`). En r2 non queda ningún texto "actual" de B.

| # | Estado en r2 |
|---|---|
| B1-B8, B10-B13 | O texto novo está unha vez, literal |
| B9 | Substituída por A3: «Diante dela, alguén preguntaba, e alguén escribía.» Mantén o arranxo L1 de r1 (sen *pensala* nin *cómpre*); xuízo da frase no §2 |
| B14 | Movida por A1 detrás das liortas, con «para Pousa» no canto de «Para el»: mellor ca B14, porque nomea o suxeito (L4 de r1) |
| B15 | Ficha v2, `descricion`: «e a noticia dunha lista de mulleres vistas nunha fonte…», literal |

## 2. Feitos das 29 frases

Gravidade como no encargo (G falso; M atribución perdida ou orde que fai deducir algo falso; L leve). Resultado:
**0 G, 0 M e 0 L.**

| S | Frase (orixe) | Fonte | Resultado |
|---|---|---|---|
| 7 | Abondaría con calzarlle… (B1) | F009; PDF p. 15, [5 verso] | Correcta: o condicional queda dentro do testemuño |
| 13 | O que se contou de Dorotea é vello de verdade… (B2) | F006, F008-F010 | Correcta (excepción, §5) |
| 14 | As palabras que ela sabía, esas non as coñecemos. (A2) | F009: o folio [5 verso] só di «con algunas palabras que savía» | Correcta: fala do que sabemos nós, non do que garda o proceso enteiro (o erro que corrixiu B12 en r1) |
| 17 | …noticia dunha lista… (B3) | F050, F131-F133 | Correcta |
| 20 | …e preguntarnos de quen son, de verdade, esas palabras. (A5) | — | Sen contido factual; págase en S32 e S100 (excepción, §5) |
| 23-25 | Unha testemuña oíu murmurar… / E contou que María… / Pensemos nela alí… (B4-B6) | F052, F053; PDF p. 15, [3 verso] | Correctas: a cadea de oídas, como no documento; S25 é reconstrución explícita e xenérica |
| 30 | O papel gárdao o Arquivo…, con outros procesos por bruxería da Real Audiencia. (A4) | F006, F083, F241; PDF p. 11 («conserva uns 30 procesos xudiciais contra mulleres levados a cabo pola xustiza real») | Correcta. Quitar «uns trinta» só resume |
| 37-38 | Aquel papel gardou ata o máis pequeno… / …quedou sen o máis importante, o nome de quen o escribiu. (A7) | F055, F014 | Correctas: «o máis pequeno» e «o máis importante» son valoración do narrador, non feito |
| 40 | …para darlles un pouco de ritual a aquelas queimadas. (A10) | F005 (*Atlántico*: «dotar de cierta ritualidad a las queimadas que organizaba Marcos y un grupo de amigos») | Correcta |
| 42 | Unha empresa vendeu copias do conxuro… (A10) | F014, literal | Correcta |
| 46 | …acabaron noutro sitio: nos tribunais. (B7) | Tecido | Correcta |
| 48 | …coas meigas galegas a temida Inquisición foi branda… (B8) | F036 (*El Español*: «la Inquisición en Galicia solo condenó a muerte a una de las famosas y legendarias meigas»), F039 | Correcta, sen ano nin nome (Non dicir n.º 2) |
| 49 | Os xuíces civís foron moito máis duros. (A4) | F040 | Correcta: son os mesmos xuíces que a «jurisdicción ordinaria» de Valor Bravo (§3) |
| 50 | E nos procesos civís da Real Audiencia, todas as acusadas eran mulleres. (A4) | F085 (PDF p. 14, epígrafe «Os procesos xudiciais por bruxería da Real Audiencia de Galicia» e «Todas as reas son mulleres»); *GCiencia*: «procesos civís por bruxería» | Correcta; o ámbito é a Real Audiencia, como pide Non dicir n.º 14 |
| 54 | Que á nai acudía moita xente… (B10) | F090; PDF [26 recto] | Correcta |
| 56 | Diante dela, alguén preguntaba, e alguén escribía. (A3) | F089 e PDF p. 4-5 (rótulos «Tortura» e «Confesión de María Cibreira despois de ser torturada»); F093 («No interrogatorio as respostas estaban incluídas nas preguntas») | Correcta. Xa non leva marca de imaxinación, pero non a precisa: non engade ningún detalle imaxinado (nin vento, nin auga, nin ollos), só o que proban os papeis, que houbo interrogatorio e que a confesión quedou escrita. Sen nomes, cifras nin diálogo |
| 63 | Alí, dixo, viron… (B11) | F133 | Correcta |
| 64 | Pensemos nunha noite curta de xuño… (A3) | F168 (xuño); reconstrución | Correcta: explícita e xenérica, e fóra da zona de durmir |
| 65-66 | …non nos chegou nin unha palabra. Só nos chegou a noticia da lista… (B12) | F131-F133 | Correctas |
| 74 | E, con todo, para Pousa aquelas mulleres eran necesarias… (B14 + A1) | F121 (*GCiencia*: «Por iso eran necesarias as figuras de mulleres que solucionasen os problemas cotiás») | Correcta. «Aquelas mulleres» volve ás parteiras e menciñeiras de P23, que son as de Pousa |
| 75 | Xa no século dezaoito, frei Martín Sarmiento… (A1) | F232 (CCG: «No século XVIII, Martín Sarmiento reivindicaría o saber das curandeiras, as meigas, como o de auténticos médicos e botánicos») | Correcta, con *como* |
| 76 | No mesmo século, o frade Benito Xerónimo Feijoo… (A1) | F212, F210 (1726-1739) | Correcta: Sarmiento e Feijoo son os dous do século XVIII |
| 91 | Outra noite, nunha cociña de aldea… (A6) | F268; tecido | Correcta |
| 93 | …para animar os corazóns. (clixé fóra) | F268 | Correcta |
| 101 | …e dos libros outra vez á aldea. (A9) | F216 (Feijoo: «del Vulgo a los Escritores, y de los Escritores al Vulgo») | Correcta como tecido de peche: fala o narrador, e a idea de Feijoo xa vai atribuída en P25 |

**Regras do tema** (`gauntlet3/contexto.md` §8) nas frases cambiadas: a frase da Inquisición segue unha soa vez,
atribuída e sen ano (S48); do conxuro non hai ningún verso novo; María Soliña non sae; na zona de durmir só cambian
S91, S93 e S101, e as tres son mansas; o aviso e a fórmula non cambian (a porta dáos por literais). Non hai ningunha
das 18 frases de "Non dicir".

## 3. A dúbida A4: «civil» ou «a ordinaria»

**Decisión: «civil» nas tres frases (S47, S49 e S50), como está.** Non é un cambio de atribución:

1. **O referente é o mesmo.** No artigo de *El Español*, a «jurisdicción ordinaria» de Valor Bravo é a xustiza
   secular: o artigo preséntaa como «la justicia penal», e o subtítulo resume que as meigas «fueron ajusticiadas
   principalmente por los tribunales penales y algunos vecinos». Na tríade do Arquivo (F077: «pertencía tanto á
   xurisdición civil como eclesiástica e inquisitorial»), *civil* é esa mesma xustiza, a que non é da Igrexa nin da
   Inquisición. «Os xuíces civís foron moito máis duros» nomea, pois, os mesmos xuíces que Valor Bravo, e a frase
   segue no parágrafo que se lle atribúe a el, como en r1.
2. **As dúas fontes galegas din *civil*.** O Arquivo, xusto despois da tríade: «conserva uns 30 procesos xudiciais
   contra mulleres levados a cabo pola xustiza real» (p. 11). Pousa, en *GCiencia*: «rescata documentación dos
   procesos civís por bruxería», «analiza só os procesos civís e non entra nos da Inquisición», «polos tribunais
   civís». «Procesos civís da Real Audiencia» é a palabra do especialista, e o dossier xa trata as dúas como a mesma
   xustiza (Non dicir n.º 1: «la justicia ordinaria condenó a muerte (Valor Bravo, Pousa, CCG)»).
3. **O DRAG avala *civil* e non *ordinario*.** *Civil*, ac. 2: «Que non ten carácter militar nin relixioso»
   («Matrimonio civil»). *Ordinario* só ten 'conforme á norma', 'de pouca calidade' e 'que non ten delicadeza', así
   que «os xuíces ordinarios» pode oírse como 'groseiros'. Ademais, en dereito canónico o *Ordinario* é o bispo da
   diocese (Código de Dereito Canónico, c. 134), e «a ordinaria» ao lado de «a eclesiástica» sería ambigua. En S47,
   por último, desfaría a tríade literal do Arquivo.
4. **Risco que acepto (L, sen cambio):** para un xurista, «procesos civís» pode querer dicir 'non penais', e *El
   Español* chama a eses tribunais «penales». No texto, S47 define *civil* dúas frases antes, e o oínte enténdeo así.

## 4. Lingua

As 29 frases están en galego normativo e natural: **0 G e 0 M.** Comprobado: *preguntarse* pronominal (S20; DRAG
*preguntar*, ac. 4: «Ter dúbida sobre algo. Pregúntome que sería del»); o tópico co demostrativo e o clítico de S14
(«As palabras que ela sabía, esas non as coñecemos», correcto como «Iso non o sei»); *gárdao* con til, porque co
clítico é esdrúxula; «a aquelas queimadas» sen contracción, porque a preposición non se contrae co demostrativo;
«pasoulle ao revés», «quedou sen», «E, con todo,»; *civís*, *xuíces*, *dezaoito*; e *como* en Sarmiento
(identificación, non comparación). Sen díxitos, siglas nin preguntas (porta de estilo).

| # | Frase (S) | Observación | Grav. |
|---|---|---|---|
| L1 | «Diante dela, alguén preguntaba, e alguén escribía.» (S56) | O último *ela* (S54) é a nai. O oínte resólveo ben: toda a serie depende de *confesou*, Cibreira é o tema do parágrafo e só ela foi interrogada. Non pido cambio, porque calquera arranxo perde a imaxe que buscou A3 | L, sen cambio |
| L2 | «para Pousa aquelas mulleres eran necesarias» (S74) | *Para* + persoa ao comezo óese como opinión ('segundo Pousa'); a lectura 'necesarias para el' é absurda | L, sen cambio |
| L3 | «As palabras que ela sabía, esas non as coñecemos. / Nos papeis daqueles procesos hai moitas máis palabras.» (S14-S15) | Despois de A2, *máis* compara con palabras que acabamos de dicir que non coñecemos; óese como 'moitas outras palabras', e o cambio de parágrafo axuda | L, sen cambio |

**Para a peza VOZ:** *civís* é aguda; *gárdao*; pausas nas comas de S56 e de S20 («de quen son, de verdade, esas
palabras», sen entoación de pregunta).

## 5. Excepcións da porta de veracidade

Acepto as cinco frases que marcou a porta. O [`excepcions-r2.yaml`](../guion/excepcions-r2.yaml) queda coas mesmas sete
entradas (as cinco e as dúas preventivas, que o NLI non precisou), con tres xustificacións reescritas pola numeración
de r2, porque A2 engadiu unha frase en S14:

| S | Frase | Decisión | Cambio na xustificación |
|---|---|---|---|
| S12 | As palabras do conxuro parecen vellas e son novas… | Aceptada | Ningún (S1-S4 e S42 seguen valendo) |
| S13 | O que se contou de Dorotea é vello de verdade… | Aceptada | Ningún (S5-S8) |
| S16 | Hai unha palabra trabucada… | Aceptada | O bucle págase en **S29-S31** (en r1 eran S28-S30) |
| S18 | Había mulleres de aldea… | Aceptada | Prepara F048 en **S19** (dicía S18, que é ela mesma) |
| S20 | Esta noite imos buscalas…, e preguntarnos de quen son, de verdade, esas palabras. | Aceptada | Nova: promesa e pregunta central sen contido factual, que se pagan en **S32** («na voz doutros, e na man de quen escribía») e en **S100** («todas quedaron escritas por outra man»); dicía S31 e S101 |
| S17, S24 | (preventivas) | Quedan | Ningún (S59-S66 segue valendo) |

## 6. Lista pechada de substitucións

**Ningunha.** As 29 frases quedan como están.

## 7. Notas (non bloquean)

1. **Mapa `feitos-r2.md`, fila S20:** a pregunta págase en S100, non en S99 (numeración de `pipeline.partir`).
2. **Dossier, F040:** engadir como evidencia «Estas mujeres fueron ajusticiadas principalmente por los tribunales
   penales» (*El Español*), para que quede escrito que a «ordinaria» de Valor Bravo é a xustiza secular. **F042 e
   F137:** engadir «O historiador documenta decenas de procesos civís por bruxería na época» (*GCiencia*): o feito F042
   di «preitos civís», pero a súa cita non leva a palabra.
