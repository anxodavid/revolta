# Encargo: construtor da lista de planos v2 (rolda 1) · Gauntlet 4

Es o MONTADOR E DIRECTOR (construtor) da peza 4 (PLANOS v2), rolda 1, do Gauntlet 4 no repo /home/user/revolta (rama
ccr-0584aac1-xqy2si). Traballa e escribe todo en galego normativo (D17); os prompts de imaxe e as accións de vídeo,
en inglés.

## O problema que resolves
Persoas que viron a v1 dixeron, literal: "as imaxes fixas non teñen moita correlación co que se di no texto en cada
momento e non atraen a mirada", e piden "movemento nas imaxes, xente que camiña, planos que evolucionan". Na v1 os
planos cortábanse por tempo; a medida automática de correlación da peza IMAXE (CLIP-L fronte ao texto en inglés,
AUC 0,90) di que só o 59 % dos planos da v1 ilustraban o que se oía, e no gancho só o 29 %. O promotor quere unha v2
de ≈ 12 min que **amose calidade** (D18).

## Entradas
- Guion final: `plan-de-negocio/gauntlet4/guion/guion-r2.txt` (1.628 palabras; pechado: non se cambia). O anexo de
  `guion/plan-r1.md` dá o momento visible de cada parágrafo; `guion/feitos-r2.md` di que feito sostén cada frase.
- Voz xa sintetizada, en `$SCRATCH/v2/w/` (`SCRATCH=/tmp/claude-0/-home-user-revolta/c92eba35-e89d-5d11-bb3d-f517a84dab48/scratchpad`):
  `frases.json` (índice `i` de cada frase, `texto`, `par`, `pal0`), `tempos_frases.json` (inicio e fin de cada frase
  en s), `rotulos.json` e `planos.json` (o corte por tempo da curva, só como referencia de duracións).
- Imaxe: `plan-de-negocio/gauntlet4/imaxe/biblia-v2.md` (regras de composición), `imaxe/informe-r1.md` (§4: que
  técnica de semente para que caso; §2 a porta v6), `imaxe/referencias.json` e `referencias-escollidas.md` (só as
  de uso `semente` se poden usar como semente: CC0, dominio público ou CC BY), `imaxe/biblia-v1-v2.jpg` (exemplos).
- Movemento: `plan-de-negocio/gauntlet4/movemento/informe-r1.md` e `estado.md` (modos, custos e que funciona),
  `herramientas/pipeline/movemento.py` (que valores admite `animacion`).
- Contexto: `plan-de-negocio/gauntlet4/contexto.md` (§6.1 formato da lista; §8 D18 e D19) e os vetos de
  `plan-de-negocio/gauntlet3/contexto.md` §8.5.

## Que entregas
1. **`plan-de-negocio/gauntlet4/planos/escenas-v2.json`** (≈ 60-75 planos) co formato do §6.1, máis `texto_en`
   (o que se oe nese plano, en inglés, para a medida de correlación) e `prioridade_i2v` (1 = imprescindible, 2 = se
   cabe, 3 = non) nos planos con persoas que se moven. Cada plano: `n`, `frases`, `desde` (se empeza a metade dunha
   frase), `texto`, `texto_en`, `prompt`, `clave`, `negativo`, `tipo`, `son`, `referencia` (se procede) e
   `animacion` (`modo`, `camara`, `efectos`, `accion`).
2. **Corte por sentido en `herramientas/pipeline/longo.py`**: se a lista trae `frases`, os tempos de cada plano
   saen de `tempos_frases.json` (inicio da primeira frase; con `desde`, a parte proporcional da frase polos
   caracteres ou, mellor, as marcas de tempo por palabra do Whisper que xa usa o QA), en vez de `planos()`. Que
   `ler_escenas` pase `referencia`, `animacion`, `texto_en` e `prioridade_i2v`. Engade `--so-planos` (para despois de
   montar a lista e escribir `escenas.json` e `planos.json`, sen imaxes) para validar o corte. A v1 ten que seguir
   montándose igual (sen `frases` na lista, o camiño de sempre). Proba con `--so-planos` sobre `$SCRATCH/v2/w`
   (lixeiro; se precisa a CPU, `herramientas/gauntlet/candado.sh --prioridade`).
3. `plan-de-negocio/gauntlet4/planos/notas-r1.md` (decisións, medidas: planos por fase, duración media, % con
   persoas facendo algo na parte esperta, arquetipos, planos con semente e con I2V) e `planos/estado.md`; aprendizaxes
   en `gauntlet4/aprendizaxes/planos.md`.

## Regras (o crítico comprobará cada unha)
- **O que se oe é o que se ve.** Cada plano ilustra literalmente o que din as súas palabras: quen, que fai, onde,
  con que obxecto. Se a frase é abstracta, unha imaxe concreta atada ao fío do guion (as palabras: mans que escriben,
  tinta, papel, beizos que murmuran; a auga: fontes, cántaros, choiva na lousa), nunca unha paisaxe de recheo.
- **Corte por sentido**, cunha duración por fase aproximada de 3-6 s no gancho, 5-9 s na transición, 8-14 s na
  calma e 12-20 s ao durmir. Os capítulos abren plano co rótulo.
- **Chamar a mirada** (`biblia-v2.md`): rostros e mans, xesto, luz motivada, primeiro termo, profundidade, escalas
  variadas. Na parte esperta, ≥ 60 % dos planos con persoas facendo algo; sen arquetipos repetidos (a figura soa de
  costas, como moito unha vez); ao durmir, calma pero non baleiro: auga que corre, choiva na lousa, brasas, néboa no
  val, mans que repousan.
- **Personaxes recorrentes descritos sempre igual** (Dorotea, a parteira vella; María, a filla; o escribán; os
  amigos de 1967 no barco; Feijoo): mesma idade, roupa e cabelo en todos os seus planos.
- **O que SDXL fai mal** (aprendizaxes da v1 e da rolda de arranxos): "lane/street + night/dusk" → aldeas inglesas con
  farolas; "kitchen" → salón moderno; "road" → asfalto; "door" → corredor moderno; ventás de vidro, lámpadas que
  colgan, cociñas económicas. Nada de hórreo nin carro como suxeito sen semente; vetos de `gauntlet3/contexto.md`
  §8.5 (nada de clixés de bruxa).
- **Sementes** (D19): para iconografía galega (aldea de granito e lousa, hórreo, palloza, lareira, carro, muíño),
  `referencia` cunha semente permitida, co modo e a forza que recomenda o informe de imaxe (img2img 0,5 para obxectos;
  0,75 para espazos con xente; profundidade 0,6 para recompoñer) e `recorte` se a foto trae presente.
- **Movemento** (D16): ningún plano fixo. `i2v` para persoas que se moven ou fan algo (accións físicas simples e
  lentas: camiñar amodo, virar a cabeza, mans que traballan, lapas, auga), cunha `accion` curta e concreta en
  inglés; `paralaxe` con `camara` e `efectos` no resto. O número de planos I2V depende do custo que mida MOVEMENTO:
  marca a prioridade e deixa que o orzamento decida.
- **Son** por plano (D13 e D14): `choiva`, `lume`, `mar`, `vento`, `fonte`, `xente`, `noite`, `aldea`, `campas` ou
  `limpa`, segundo o que hai na escena.
- **Rigor**: nada que contradiga o guion nin o dossier (sen xuízos con autos de fe, sen fogueiras con persoas, sen
  partos explícitos); a época de cada escena ben (1617 non é 1967).

## Despois de ti
Un crítico (espectador esixente) lerá cada parella texto-prompt e puntuará a correlación (1-5) e o atractivo; gañas
se ≥ 90 % dos planos levan ≥ 4/5 en correlación, ≥ 60 % dos planos da parte esperta teñen persoas facendo algo e
non hai arquetipos repetidos nin personaxes incoherentes. Despois xeraranse as imaxes (porta v6) e o movemento.

## Regras de traballo
As do §7 de `gauntlet4/contexto.md`: commit e push de cada entrega con rutas concretas, mensaxes "Gauntlet 4:
planos: ..." en galego coas dúas liñas de autoría; o pesado con `herramientas/gauntlet/candado.sh`; non toques os
ficheiros doutras pezas agás `longo.py` (o corte por sentido). Aforra cota: non volvas ler enteiros ficheiros
grandes, e fai resumos curtos. Ao rematar, devolve un resumo de ≤ 12 liñas.
