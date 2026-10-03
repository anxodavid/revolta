# Aprendizaxes · revisor de imaxes (Gauntlet 4, axente Claude)

## Rolda 1, planos 1-42 (03-10-2026)

- **Método que funcionou:** follas de 6 planos (escollida a 640 px, outros intentos a 320 px, texto e porta debaixo)
  e miralas en recortes de 2 planos sen reducir (≈ 980x940 px); despois, grades de 4 recortes ampliados dos
  orixinais para o que non se ve a 640 px (bombillas, plumas, letra, mans). Ferramentas en
  `video/scripts/follas_revision.py` e `zoom_revision.py`. 42 planos ≈ 35 min de axente.
- **A porta v6 erra nos dous sentidos:** rexeita de máis por «texto na imaxe» nos planos de escritura, por «animais
  en grupo» cando o texto pide o gando e por un «iate moderno» que CLIP imaxina; deixa pasar salóns palacianos con
  lampadario de cristal, fiestras de vidro, baixantes, bancos de parque, faroles, vasoiras e a queimada como fogueira
  ou caldeiro. 16 de 29 escollidas aprobadas tiñan un problema; 8 de 13 planos rexeitados tiñan un intento que vale.
- **«falta: clave» só avisa**, así que a reserva xenérica (`reserva: true`, un labrego nun prado) pasou no plano 35
  sen nada do que se oe: revisar sempre as reservas.
- **As frases que engade a pipeline nos reintentos** («smoke-blackened granite walls, open stone hearth at floor
  level», «hands hidden in the sleeves or out of frame») poden pasar dos 77 tokens e truncar o final do prompt (no 6
  perdeuse o home): os prompts revisados van a ≤ 55 tokens sen o prefixo de estilo (16 tokens).
- **Lume da queimada:** os 5 planos con «burning spirits» (2, 11, 33, 38, 39) deron lume laranxa, mesmo co «blue» ao
  lado; «a wide clay bowl of blue flames» deu lapas azuis no 32 (2 de 3 intentos). Os prompts novos levan «pale blue
  flames» [S: sen probar].
- **Palabras que chaman a SDXL a sitios alleos:** «court/hall» → salón de palacio con lampadario; «granite house at
  dusk» → casas inglesas; «church» → catedral; «red headscarf» + capa → Carapuchiña.

## Rolda 1, segunda pasada, planos 43-77 (03-10-2026)

- **«fountain» dá fontes de xardín ou de parque** (pía de pé, estatua, billa metálica, farolas) en 5 dos 7 planos que a pedían (47, 51, 52, 63, 66),
  e nos outros dous non saíu fonte (49, 54). Para
  a fonte de aldea, describila: «a simple rustic spring: water pouring from a stone spout set in a mossy granite wall
  into a stone trough» [S: sen probar].
- **Outros atallos de SDXL:** un tribunal con muller dá unha dama vitoriana (45, 46); «village men» dá labregos
  irlandeses con tellados de herba (48, 57); «cows» nunha corte dá vacas frisoas (74); «slate roof of a house» dá unha
  bufarda inglesa con fiestras acesas (77).
- **A porta no durmir:** «lume vivo» salta co barro laranxa da cunca (68) e coa lareira do fondo (73), mentres deixa
  pasar lume laranxa grande se ocupa pouca área (69). Unha semente de foto de día en img2img 0,5 trae a luz de día ao
  plano nocturno (68): para escurecer, profundidade.
- **A reserva xenérica volveu pasar** (76: un bosque no plano da candea). Na rolda 1 pasou en 2 de 77 planos.
- **Cifras da rolda:** a revisión deu 29 valen, 10 outro intento e 38 rexenerar sobre 77. A porta aprobou 53
  escollidas, das que 32 tiñan un problema, e en 12 dos 24 planos que rexeitou había un intento que vale.

## Rolda 2, os 38 planos rexenerados (03-10-2026)

- **Cifras:** 16 valen, 8 outro intento e 14 rexenerar outra vez (o gancho, 4 de 7). A porta aprobou 28: 14 valían, 3
  tiñan outro intento mellor e 11 non valían; dos 10 que rexeitou, en 7 había un intento que vale. ≈ 30 min de
  axente, con `video/scripts/follas_revision_r2.py` (le `intentos-r2.json`).
- **Un só intento é o maior risco:** a pipeline para no primeiro intento sen problemas; 18 planos tiveron un só e 8
  deles non valían. Para os planos importantes convén pedir 2-3 intentos sempre.
- **O lume azul con persoas non sae:** «pale blue flames», «blue fire» e «faces lit blue» deron laranxa en 2, 39 e 69;
  o azul só saíu cando a cunca é o tema (32). Proposta da r2: só man e cunca (2), siluetas (69) [S: sen probar].
- **O lume arredor de mulleres de noite volve dar rito** (52) e unha festa con fogueira, multitude (38): quitar o lume
  e poñer a lúa ou mesas de verbena.
- **O negativo non protexe:** a porta non marcou «turf roof, sheep» (48), «hooded robes, ritual» (52) nin «orange fire,
  fireplace» (69) aínda que estaban na imaxe; o que cambia o resultado é o prompt.
- **Cores que viaxan:** o «red» do pano de María vestiu de cardeal ao cura (29) e o azul do chal da curandeira vestiu
  ao frade (58). Con dúas persoas de cores distintas, mellor unha soa persoa no cadro.
- **Sementes:** o hórreo de Muimenta en img2img 0,5 perdeu os pés (10) e a palloza en profundidade 0,6 comeu a xente
  (21): para obxectos con forma, profundidade; para escenas con persoas, sen semente.
