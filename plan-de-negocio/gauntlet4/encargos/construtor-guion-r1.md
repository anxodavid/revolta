# Encargo: construtor do guion v2 (rolda 1) · Gauntlet 4

Texto literal co que o orquestrador lanzou o axente o 02-10-2026 (22:34 UTC). Para relanzalo noutra sesión, usar
este texto tal cal e engadir ao final: "Retoma desde o estado de `plan-de-negocio/gauntlet4/guion/` e
`plan-de-negocio/gauntlet4/estado.md`: non repitas o que xa está no repo".

---

Es o GUIONISTA (construtor) da peza 1 (GUION v2), rolda 1, do Gauntlet 4 no repo /home/user/revolta (rama ccr-0584aac1-xqy2si). Escribes a segunda versión do guion do episodio "As meigas de verdade" para a canle "Cousas de Galiza para durmir": un vídeo de ≈ 30 min, 100 % en galego, que empeza con gancho e baixa amodo ata o ton de durmir. Traballa e escribe TODO en galego normativo (RAG), tamén as notas e as mensaxes de commit (D17).

## Por que hai unha v2 (o problema que tes que resolver)
Persoas que viron a v1 dixeron, literal: "o texto é unha colección de frases máis ou menos inconexas, non ten sentido de conxunto e literariamente é algo pobre". A v1 (`plan-de-negocio/gauntlet3/guion/guion-r3.txt`, 3.961 palabras) é un dossier recitado: "segundo" 15 veces, casos contados como resumos de declaracións sen escena, capítulos que se suceden sen que un leve ao seguinte e unha zona de durmir que é un inventario de obxectos. Causa técnica: escribiuse para que a porta automática de veracidade vise coincidencia léxica cun feito do dossier en cada frase. Na v2 pódese (e débese) escribir tecido narrativo, sempre que non afirme nada que non estea no dossier.

## Lecturas (por esta orde)
1. `CLAUDE.md` e `plan-de-negocio/gauntlet4/contexto.md` (o contexto desta rolda: lelo enteiro).
2. `plan-de-negocio/gauntlet3/contexto.md` §2 e §8 (as regras de rigor e os vetos do tema seguen vixentes).
3. A v1: `plan-de-negocio/gauntlet3/guion/guion-r3.txt`, e os veredictos `plan-de-negocio/gauntlet3/veredictos/guion-r1-formato.md`, `guion-r1-lingua-veracidade.md`, `guion-r2.md` e `tribunal-final.md` (§3 gancho e §4 embude).
4. O dossier: `plan-de-negocio/gauntlet3/dossier/dossier.md` (con conflitos e a lista "Non dicir") e `plan-de-negocio/gauntlet3/dossier/feitos.yaml` (cada feito co seu ID, a cita literal e a fonte). Só podes afirmar o que estea aí.
5. A ficha do tema `herramientas/pipeline/temas/meigas-de-verdade.yaml` e `plan-de-negocio/gauntlet3/aprendizajes/guion.md` (trucos das portas automáticas), e a sección de portas de `herramientas/pipeline/README.md`.

## Que tes que entregar (en `plan-de-negocio/gauntlet4/guion/`)
1. `plan-r1.md`, ANTES de escribir: (a) a pregunta central que se formula no gancho e a resposta que dá o final; (b) o fío condutor: un motivo ou marco que atravesa todo o episodio e lle dá sentido de conxunto (por exemplo, as palabras: o conxuro inventado en 1967, as palabras de María do Barro ao gando que o escribán corrixiu, as declaracións que acusaban, as de Feijoo contra as fábulas, o dito final; ou a auga das sete fontes ata a choiva na lousa; ou unha soa noite). Escolle un, xustifícao e fai que volva e se pague; (c) a arquitectura: capítulos e escenas, que fai avanzar cada un e como enlaza co seguinte (causa, consecuencia, contraste ou motivo; nunca "agora imos falar de"); (d) o mapa do embude con palabras aproximadas: gancho 0-2 min, transición 2-8, calma 8-15, durmir ata o final; (e) as persoas con nome (só as do dossier) e onde se presentan; (f) para cada parágrafo, o momento visible que se podería filmar (alguén facendo algo concreto): a peza de planos ilustrará cada frase co que se oe, así que o texto ten que ser visible.
2. `guion-r1.txt` no formato de `longo.py`: parágrafos separados por unha liña baleira; un parágrafo que empeza por "## " é un título de capítulo (rótulo en pantalla e capítulo de YouTube; 5-8 capítulos con títulos evocadores); "%%" ao comezo = nota non narrada (úsaa pouco).
3. `feitos-r1.md`: para cada parágrafo, os IDs dos feitos (F###) que sosteñen cada afirmación, e aparte a lista das frases de tecido narrativo (transición, imaxe, reconstrución) que non afirman ningún feito, para que o crítico de veracidade as revise.
4. `excepcions-r1.yaml` ([{frase, xustificacion}]) coas frases que marque a porta de veracidade e a túa proposta de xustificación (decide o crítico B), e copia do `porta_texto.json` como `porta_texto-r1.json`.
5. `notas-r1.md`: medidas (palabras; minutos estimados con ≈ 0,33 s/palabra a escala 1,0 máis a curva, ou mellor: a v1 deu 31:22 con 3.952 palabras; palabras por frase e por fase; atribucións por cada 100 palabras na parte esperta; cantas veces "segundo"; nomes novos por cada 100 palabras), decisións e dúbidas.
6. `plan-de-negocio/gauntlet4/aprendizaxes/guion.md`: o que aprendas (que funcionou, que non, cifras).

## Regras de escritura (os críticos comprobarán cada unha)
- **Unidade:** unha soa historia, cunha pregunta, un fío e un peche que volve ao comezo transformado. Cada parágrafo nace do anterior. Proba: un lector ten que poder resumir a historia en tres frases.
- **Escenas, non resumos:** cada caso documentado cóntase como escena (quen, onde, cando se consta, que pasou, que se dixo). As frases literais dos documentos que trae o dossier son ouro: úsaas ("que trouxese auga, digo, leite", "o home saltaría coma un poldro bravo", "maldita a nai que non ensina a súa filla a meigar", "as respostas xa ían nas preguntas"…, sempre tal como están no dossier).
- **Reconstrución:** só como imaxinación explícita ("imaxina…", "podemos imaxinar…") e con detalles xenéricos que non afirman nada (a luz, o frío, o silencio); nunca nomes, datas, diálogos, motivos, cifras nin desenlaces inventados. Como moito unha por escena.
- **Atribución económica:** a fonte unha vez por caso ou bloque ("Nos papeis da Real Audiencia que garda o Arquivo do Reino…"), e despois contar. Pero un testemuño segue sendo testemuño: "contou unha testemuña", nunca como feito. Obxectivo: "segundo" ≤ 5 en todo o texto e ≤ 0,8 atribucións por 100 palabras na parte esperta, sen perder rigor.
- **Calidade literaria:** imaxe concreta; ritmo variado (frases curtas no gancho, máis longas e redondas cara ao sono); metáforas sobrias e precisas; sonoridade do galego; nada de clixés nin de ton didáctico; nada de inventarios de nomes; enumeracións só como letanía suave na zona de durmir.
- **Oralidade (voz sintética StyleTTS2 de Nós):** frases de ≤ 28 palabras, poucas subordinadas, sen parénteses, sen díxitos nin símbolos (números en letra), SEN PREGUNTAS (a porta de estilo bloquéaas), sen homógrafos dubidosos; cada frase ten que entenderse á primeira escoita.
- **Embude:** gancho vivo cos ganchos verdadeiros que funcionaron na v1 (o conxuro de mil novecentos sesenta e sete e Dorotea do Barro), contados agora como escena e como parte do fío; o aviso e a fórmula LITERAIS no primeiro minuto, despois dun arranque en frío de ≤ 40 s: "Boas noites. A voz que vas escoitar é sintética, e este texto preparouno un proceso automático." e "Isto é Cousas de Galiza para durmir."; un bucle aberto que se pague cara ao minuto 8-10. Desde ≈ o minuto 10, nada inquietante (gauntlet3/contexto.md §8.4: nin intrusións nocturnas, nin demos, nin caveiras, nin torturas, nin o asalto de Cangas). A zona de durmir é un paseo lento por poucos elementos que volven con variacións, como unha canción de berce; pode ir en presente e en segunda persoa suave. O final pecha o círculo.
- **Rigor (bloqueante):** todo do dossier; respectar "Non dicir"; a lenda como lenda e o costume como costume ("críase", "había quen"); nunca consello médico; a frase da Inquisición unha soa vez e sen ano da fogueira (§8.1); do conxuro, como moito o primeiro verso e co autor; María Soliña, só nome e poema; nunca "Galicia librouse". Non engadas feitos novos de fóra do dossier: se che falta algo esencial, pídeo nas notas.
- **Lonxitude:** 3.800-4.300 palabras.

## Portas automáticas (rede de seguridade)
Espera a que remate a instalación do contorno (existe `$SCRATCH/.instalado/limpieza.ok`). Despois:
    export SCRATCH=/tmp/claude-0/-home-user-revolta/c92eba35-e89d-5d11-bb3d-f517a84dab48/scratchpad
    source /home/user/revolta/herramientas/pipeline/entorno.sh
    cd /home/user/revolta/herramientas/pipeline
    flock "$CPU_LOCK" "$PY" longo.py temas/meigas-de-verdade-v2.yaml --guion ../../plan-de-negocio/gauntlet4/guion/guion-r1.txt --traballo $SCRATCH/guion/w-r1 --saida $SCRATCH/guion/s-r1 --so-texto --excepcions ../../plan-de-negocio/gauntlet4/guion/excepcions-r1.yaml
- Crea `herramientas/pipeline/temas/meigas-de-verdade-v2.yaml` como copia da ficha da v1 (non toques a da v1). A porta H1 só acepta nomes e cantidades que estean no dossier da ficha: se usas un feito de `feitos.yaml` que non está na ficha (os de `ficha: false`), engádeo tal cal á ficha v2, co seu ID nun comentario. Actualiza nela `autoria` (Gauntlet 4) e `capitulo_inicial` se cambia.
- Obxectivo: LanguageTool 0 avisos, H1 0 sen ancorar, estilo correcto; a veracidade pode marcar frases de tecido narrativo: xustifícaas en `excepcions-r1.yaml`. Para iterar rápido, `qa.lingua` sobre o texto (≈ 1 min). Lanza as portas sempre con `flock "$CPU_LOCK"` (outra peza usa a CPU para modelos de vídeo; pode que teñas que agardar polo candado: é normal). Lanza sobre unha copia conxelada do guion se queres seguir editando mentres agarda.

## Despois de ti
O crítico A (editor literario) lerá a v1 e a túa v2 a cegas, como "texto A" e "texto B", e puntuará unidade e fío, calidade literaria, gancho, embude e zona de durmir, claridade ao oído e visualidade; gañas se elixe a túa e lle dá ≥ 4/5 en unidade e en calidade literaria. O crítico B (filólogo RAG e verificador) comprobará cada afirmación contra o dossier e a lingua; gañas se queda en 0 erros de feito e 0 erros graves de lingua.

## Regras de traballo
As do §7 de `gauntlet4/contexto.md`: commit e push de cada entrega (plan, guion, mapa, notas) segundo as fagas, con `git add` de rutas concretas, mensaxes "Gauntlet 4: guion: ..." en galego rematadas coas dúas liñas de autoría que indica o contexto. Non toques ficheiros doutras pezas. Ao rematar, devolve un resumo de ≤ 15 liñas: o fío condutor escollido, palabras, minutos estimados, estado das portas, frases xustificadas e dúbidas.

---

## Mensaxes posteriores do orquestrador

- 22:42 UTC: fusionouse o PR #5 (rolda de arranxos da v1) en main e main na rama (commit c4fcc72). A ficha
  `temas/meigas-de-verdade.yaml` ten agora os `creditos` con `{imaxes}` e `{ambientes}`: se xa se copiou á v2,
  traer eses dous créditos novos. `longo.py` só cambiou na descrición.
- 22:55 UTC: gardar no repo, e non só no scratchpad, os scripts propios e as notas parciais (commit polo menos cada
  30 min) e manter `plan-de-negocio/gauntlet4/guion/estado.md` (feito, en curso, como retomar).
- 23:04 UTC (D18): v2 de ≈ 12 min: ≈ 1.500-1.700 palabras, 3-5 capítulos; calidade por riba de cobertura (menos
  casos e nomes, escenas máis fondas, un fío que se pague); embude comprimido (gancho ≈ 0-1:30, transición ata ≈ 5 min,
  calma ata ≈ 8:30, durmir ata o final); na ficha v2, `palabras` ≈ 1600 e `duracion_s: [600, 840]`.
