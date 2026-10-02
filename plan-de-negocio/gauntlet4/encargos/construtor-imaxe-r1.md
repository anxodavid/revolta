# Encargo: construtor da imaxe (referencias, modelo e porta; rolda 1) · Gauntlet 4

Texto literal co que o orquestrador lanzou o axente o 02-10-2026 (22:38 UTC). Para relanzalo noutra sesión, usar
este texto tal cal e engadir ao final: "Retoma desde o estado de `plan-de-negocio/gauntlet4/imaxe/` e
`plan-de-negocio/gauntlet4/estado.md`: non repitas o que xa está no repo".

---

Es o DIRECTOR DE ARTE (construtor) da peza 3 (IMAXE: referencias, modelo e porta), rolda 1, do Gauntlet 4 no repo /home/user/revolta (rama ccr-0584aac1-xqy2si). Traballa e escribe todo en galego normativo (D17).

## O problema
Persoas que viron a v1 de "As meigas de verdade" dixeron que "as imaxes fixas non teñen moita correlación co que se di no texto en cada momento e non atraen a mirada". O tribunal da v1 (`plan-de-negocio/gauntlet3/veredictos/tribunal-final.md` §2) atopou ademais: casas inglesas en "Vilalba" e "Xinzo", bombilla e radiador (plano 84), farolas (133), casa colonial (161), maleta de rodas (56), catedral inventada, 36 planos sen o elemento que pedía o prompt, poucas persoas facendo cousas, moitos bodegóns. SDXL-Lightning non sabe debuxar o hórreo nin o carro de bois de roda maciza (`plan-de-negocio/gauntlet3/aprendizajes/visual.md`). O promotor pide agora: "Consideremos na imaxe usar as referencias buscadas" (D15): as 226 referencias libres de `docs/referencias-graficas/` (CSV, `referencias.md`, `descargar.sh`), que ninguén mirou aínda.

## Lecturas
`CLAUDE.md`; `plan-de-negocio/gauntlet4/contexto.md` (enteiro: §2 a regra de licenzas, §6.1 o formato da lista de planos co campo `referencia`, §7 regras); `plan-de-negocio/estudo-monetizacion.md` §3.2 (licenzas das sementes); `docs/referencias-graficas/referencias.md` e `referencias.csv`; `plan-de-negocio/gauntlet3/visual/biblia.md`; `plan-de-negocio/gauntlet3/aprendizajes/visual.md`; `herramientas/pipeline/imaxes.py` e `revisor.py` (porta v5) e a súa sección no README; `tribunal-final.md` §2 (lista de planos malos e bos da v1, cos ficheiros); as 162 imaxes da v1 en `plan-de-negocio/gauntlet3/video/imaxes/` e o seu `LEEME.md`.

## Tarefas (garda en git cada resultado segundo saia)
A. Parte lixeira (sen candado de CPU):
1. Baixa as referencias a `$SCRATCH/referencias/` (NON ao repo) con `descargar.sh` ou equivalente, con pausa entre peticións. Fai follas de contactos por concepto e MÍRAAS ti. Para cada concepto escolle as mellores e escribe `plan-de-negocio/gauntlet4/imaxe/referencias-escollidas.md` e `referencias.json` (id, ficheiro, concepto, licenza comprobada na páxina de Commons ou do Met, autor, URL, texto de crédito, uso permitido: `semente` só se é CC0, dominio público ou CC BY; `tal_cal` se é CC BY-SA; e que ensina: hórreo enteiro, roda maciza, lousa, lareira con escano…). Sinala os conceptos sen ningunha semente permitida e que gañariamos se o promotor aceptase sementes BY-SA (decisión súa, non túa).
2. **Porta v6** (`revisor.py`, sobe `VERSION`): engade o que a v5 deixou pasar e o tribunal viu (bombilla, radiador, farolas acesas, maleta de rodas, casas inglesas, xeorxianas ou coloniais, aldea dos Cotswolds, billa e fregadoiro modernos, cociña económica de ferro, roupa actual) e mellora a comprobación de que está o elemento `clave` do plano (CLIP con recortes ou Florence-2 con grounding). Calibra coas 162 imaxes da v1 e a lista do tribunal: ten que cazar os de "Bloquea publicar" e a maioría dos de "Molesta" sen marcar os de "Lo que funciona". Os modelos de CLIP e Florence si usan CPU: córreos con `flock "$CPU_LOCK"`.
3. **Medida automática de correlación** imaxe-texto: proba un CLIP multilingüe con licenza permisiva (p. ex. `sentence-transformers/clip-ViT-B-32-multilingual-v1`) entre cada imaxe da v1 e a frase galega que se oe nese plano (`escenas-montadas.json`), e mira se separa os planos que o tribunal deu por desconectados (16, 19, 20…) dos bos. Se serve, déixaa como medida para os críticos (v1 fronte a v2); se non, dio.
B. Parte pesada (SDXL, sempre con `flock "$CPU_LOCK"`; a peza MOVEMENTO tamén usa a CPU e o disco: colle o candado por experimento, non por horas, e deixa sempre ≥ 4 GB de disco libre; se non hai sitio, prioriza):
4. **Sementes:** para 5-6 conceptos (aldea de granito e lousa fronte ás casas inglesas, hórreo, lareira con escano, queimada, carro de bois e palloza se hai semente permitida), compara a mesma escena con texto só (prompt da v1), img2img (forza 0,4-0,7) e ControlNet de profundidade ou bordos para SDXL (licenza permisiva; o modelo de profundidade, Depth-Anything-V2-Small, Apache-2.0, é o mesmo que usa a peza MOVEMENTO) e, se cabe, IP-Adapter SDXL. Con persoas facendo algo na escena cando teña sentido. Mide tempo por imaxe e se aparece o elemento clave, e fai unha folla A/B en `plan-de-negocio/gauntlet4/imaxe/` (JPEG, sen as referencias BY-SA dentro). Implementa o campo `referencia` en `imaxes.py` (compatibilidade: sen ese campo, todo igual ca na v1).
5. **Atractivo:** escribe `plan-de-negocio/gauntlet4/imaxe/biblia-v2.md` (regras de composición que chaman a mirada para este canal: escala e rostro, mans e xesto, luz motivada, primeiro termo e profundidade, acento de cor, mirada e dirección, espazo para o movemento da cámara e das persoas nos planos I2V; e as listas do que SDXL fai mal e de como evitalo) e próbaa con 8-10 prompts reescritos fronte aos da v1 (mesmo modelo, mesma semente). Se o disco o permite e a licenza é clara, proba tamén un SDXL afinado fotorrealista con UNet Lightning (mesmo custo) contra o actual; se non, dio.
6. `plan-de-negocio/gauntlet4/imaxe/informe-r1.md` (que funciona, cifras, custos, licenzas con URL, decisións que lle tocan ao promotor) e `plan-de-negocio/gauntlet4/aprendizaxes/imaxe.md`.

## Regras
As do §7 de `gauntlet4/contexto.md`: `export SCRATCH=/tmp/claude-0/-home-user-revolta/c92eba35-e89d-5d11-bb3d-f517a84dab48/scratchpad` e `source herramientas/pipeline/entorno.sh`; candado de CPU para todo o pesado; traballos > 25 min con `setsid nohup`; nada de modelos nin de imaxes BY-SA no repo; JPEG lixeiros; commits "Gauntlet 4: imaxe: ..." en galego coas dúas liñas de autoría do contexto e push a ccr-0584aac1-xqy2si; non toques os ficheiros doutras pezas (`movemento.py`, `montaxe.py`, guion). Sé honesto con que mirou un axente e que é automático. Despois de ti, un crítico visual xulgará as follas A/B. Ao rematar, devolve un resumo de ≤ 15 liñas: referencias usables por concepto e licenza, que técnica de semente funciona e canto custa, estado da porta v6 coa súa calibración, a medida de correlación, e as decisións pendentes do promotor.

---

## Mensaxes posteriores do orquestrador

- 22:42 UTC: fusionouse o PR #5 en main e main na rama (c4fcc72): `revisor.py` ten máis anacronismos sen subir
  VERSION; `imaxes.py` respecta a caché restaurada e `escolla_manual`; cambiaron 11 planos da v1 (5, 31, 56, 61, 67,
  84, 91, 133, 145, 153, 161) e hai `gauntlet3/video/arranxos/LEEME.md`. Construír a v6 enriba disto; as imaxes vellas
  que viu o tribunal están no historial (3636c85..919402b).
- 22:47 UTC (disco ao 95 %): baixar só ControlNet depth small e Depth-Anything-V2-Small a `$SCRATCH/hf`; NON o CLIP
  multilingüe: medir a correlación con CLIP-L contra unha versión en inglés de cada anaco de narración
  (`imaxe/v1-texto-en.json`; a lista de planos v2 levará `texto_en`). Calibrar a v6 con Florence-2-base (a da
  produción) e despois borrar Florence-2-large (≈ 1 GB). Nin SDXL afinado nin IP-Adapter (pendentes por disco).
  Gardar ≥ 1,5 GB libres.
- 22:55 UTC: gardar no repo os scripts propios e as notas parciais (commit polo menos cada 30 min) e manter
  `plan-de-negocio/gauntlet4/imaxe/estado.md` (feito, en curso, como retomar).
