# Encargo: revisión das imaxes escollidas da v2 (un axente mira cada plano) · Gauntlet 4

Es o REVISOR DE IMAXES da produción da v2 de "As meigas de verdade" (Gauntlet 4), no repo /home/user/revolta (rama
ccr-0584aac1-xqy2si). Escribe en galego normativo (D17). A porta automática (v6) non ve bombillas, radiadores nin
maletas de rodas, e na v1 deixou pasar un salón moderno e unha estrada asfaltada: por iso un axente mira cada imaxe
antes do movemento e da montaxe (configuración recomendada en `plan-de-negocio/gauntlet4/imaxe/informe-r1.md` §6).

## Material
- Lista de planos: `plan-de-negocio/gauntlet4/planos/escenas-v2.json` (o `texto` que se oe, o `prompt`, a `clave`,
  a `epoca`, as `persoas`) e o veredicto do crítico de planos (`veredictos/planos-r1.md` §5: mirar primeiro os planos
  2, 8, 40, 45, 46, 54, 65, 69 e 70).
- Imaxes: `$SCRATCH/v2/w/imaxes/` (`SCRATCH=/tmp/claude-0/-home-user-revolta/c92eba35-e89d-5d11-bb3d-f517a84dab48/scratchpad`):
  todos os intentos de cada plano (`NNN-hash-K.png`, con NNN = n − 1) e `revision.json` (a escollida de cada plano,
  `ficheiro`, e o que dixo a porta en cada intento).

## Que fas
1. Fai follas de contactos lixeiras (JPEG, ≈ 6-8 planos por folla, cada imaxe a ≈ 640 px co número de plano, o texto
   que se oe e o resultado da porta debaixo; os outros intentos do plano en pequeno ao lado) e MÍRAAS.
2. Para cada plano decide: **vale** (ilustra o que se oe, época correcta, sen artefactos graves); **outro intento**
   (hai un intento mellor xa xerado: di cal); ou **rexenerar** (ningún vale: di por que e propón o prompt, o negativo
   ou a semente nova, dentro de 77 tokens co estilo que antepón a pipeline).
3. Busca sobre todo: anacronismos (luz eléctrica, ventás de vidro modernas, mobles, roupa actual, casas inglesas,
   asfalto, plástico), o que non corresponde ao que se oe (a `clave` ausente), mans e caras deformes, pseudotexto
   visible, clixés de bruxa (vetos de `gauntlet3/contexto.md` §8.5), personaxes recorrentes incoherentes e repeticións.
   Ten en conta que case todos os planos con `prioridade_i2v` van ser animados: unha imaxe con persoas ben pousadas e
   con espazo para o movemento vale máis.

## Saída
- `plan-de-negocio/gauntlet4/video/revision-imaxes-r1.md`: táboa plano a plano (n, decisión, motivo) e contas
  (cantos valen, cantos con outro intento, cantos a rexenerar).
- `plan-de-negocio/gauntlet4/video/revision-imaxes-r1.json`: `{"escollas": {"n": "ficheiro do intento"},
  "rexenerar": {"n": {"prompt": "...", "negativo": "...", "semente": 123, "motivo": "..."}}}` (o orquestrador
  aplícao).
- As follas que miraches, en `plan-de-negocio/gauntlet4/video/follas-revision/` (JPEG lixeiros, ≤ 400 KB cada unha).
Commit e push (rutas concretas; "Gauntlet 4: vídeo: revisión das imaxes r1" en galego coas dúas liñas de autoría de
`gauntlet4/contexto.md` §7). Non xeres imaxes: iso faino o orquestrador despois. Es un axente Claude: dio no
documento. Aforra cota (follas lixeiras, sen reler ficheiros grandes) e devolve un resumo de ≤ 10 liñas.

## Mensaxe de lanzamento (orquestrador, 03-10-2026 14:55 UTC)

Primeira pasada: **planos 1-42** (as imaxes 000-041 xa están; o proceso de imaxes segue cos planos 43-77 e escribe
`revision.json` despois de cada plano: só lelo, nunca modificalo). Cando rematen as imaxes (≈ 17:30 UTC) recibirás
unha mensaxe para facer os planos 43-77 nos mesmos ficheiros de saída.

Precisións para o JSON (o orquestrador aplícao con `video/scripts/produccion.py revision`):
- `escollas` leva **todos** os planos revisados que non se rexeneran: os que valen, co seu ficheiro actual, e os de
  outro intento, co ficheiro novo. Engade `motivos`: `{"n": "motivo curto"}` para cada decisión (queda en
  `revision.json` como `revision_manual`, coa túa autoría de axente Claude).
- `rexenerar`: sempre cun **prompt revisado** (un prompt novo dá sementes novas; o campo `semente` non o usa a
  pipeline: omíteo). O prompt vai sen o prefixo de estilo que antepón a pipeline ("cinematic film still, period
  drama, photorealistic, dramatic chiaroscuro," ≈ 12 tokens), así que como moito ≈ 60 tokens de CLIP, co esencial ao
  principio. `negativo` se fai falla. Se o problema é arquitectura allea (casas inglesas, ventás de vidro), propón
  `referencia` cunha semente permitida (`imaxe/referencias.json`, uso `semente`: CC0, dominio público ou CC BY) co modo
  e a forza do §4 de `imaxe/informe-r1.md`.
- O que xa viu o orquestrador nunha folla dos rexeitados (planos 7, 12, 15, 18, 19 e 21): a porta acerta no 7 (zapatos
  modernos con cordóns), no 21 (casas inglesas con cheminea) e nas ventás de vidro; rexeita de máis cando o asunto do
  plano é escritura (15, 19). Nun plano de escritura, a letra antiga ilexible vale; o que non vale son letras de
  imprenta modernas ou palabras falsas lexibles.
- Para as follas usa o Python do pipeline (`$SCRATCH/tts/venv/bin/python`, ten PIL; o python3 do sistema non) con
  `nice -n 19`; non precisa o candado (uns segundos de CPU).
