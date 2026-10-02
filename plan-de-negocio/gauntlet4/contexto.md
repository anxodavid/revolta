# Gauntlet 4: "As meigas de verdade" v2 (texto con fío, imaxe que di o que se oe, movemento)

Ficheiro de contexto que **todos os axentes len ao empezar** (e ao empezar cada rolda). As decisións novas do promotor
escríbense aquí (§8). **Todo en galego normativo (RAG)** (D17): documentos, veredictos, aprendizaxes, comentarios do
código novo e mensaxes de commit.

Lecturas previas obrigatorias, por esta orde: `CLAUDE.md`; este ficheiro; `docs/HANDOFF.md` (§0);
`docs/APRENDIZAJES.md`; `plan-de-negocio/decisiones.md`; `plan-de-negocio/gauntlet3/contexto.md` (§2, §6 e §8: as
regras de rigor e os vetos seguen vixentes); `plan-de-negocio/gauntlet3/veredictos/tribunal-final.md`; e
`herramientas/pipeline/README.md`. Cada peza engade as súas lecturas.

## 1. Encargo do promotor (02-10-2026) — PRIORITARIO

Literal:

> "Quero que montemos agora unha segunda versión do vídeo das bruxas ou meigas corrixindo o seguinte:
> 1. As personas que viron o vídeo consideran o texto una colección de frases mais ou menos inconexas, non ten
>    sentido de conxunto e literariamente e algo pobre
> 2. As imaxes fixas non teñen moita correlación co que se di no texto en cada momento e non atraen a mirada.
> 3. Necesito momento nas imaxes, xente que camiña, planos que evolucionan, como o exemplo de Versalles de historia
>    desconocida.
> Monta un gauntlet loop ata ter unha versión do vídeo que mellore a v1."

E, a continuación: *"Consideremos na imaxen usar as referencias buscadas"* (as referencias gráficas libres de
`docs/referencias-graficas/`, D15).

É a **primeira opinión de persoas que viron a v1**. Pesa máis ca calquera crítico automático ou axente.

## 2. Como o interpreta o operador (Claude, orquestrador)

| Punto | Decisión operativa |
|---|---|
| Que é a v2 | O mesmo episodio ("As meigas de verdade"), co mesmo dossier verificado (`gauntlet3/dossier/feitos.yaml`, `dossier.md` coa lista "Non dicir") e as mesmas regras de rigor, pero con **guion novo**, **lista de planos nova** feita frase a frase, **imaxes novas** (con referencias semente onde SDXL falla) e **movemento en todos os planos**. **Duración: ≈ 12 min (D18, §8)**, ≈ 1.500-1.700 palabras e ≈ 60-75 planos; a v1 durou 31:22 con 3.952 palabras e 162 planos. |
| Guion | Escríbeno axentes Claude nun Gauntlet (D8 segue vixente): **non é desatendido** e declárase na QA. As portas automáticas (LanguageTool + hunspell, H1, estilo e veracidade) seguen como rede de seguridade. Cambio clave: a v1 escribiuse para que a porta de veracidade vise apoio léxico en cada frase, e iso deu un dossier recitado. Na v2 o texto **pode ter tecido narrativo** (escenas, transicións, imaxes, motivos que volven) sempre que **non afirme nada que non estea no dossier**; as frases que marque a porta xustifícaas por escrito o crítico de veracidade (`longo.py --excepcions`). |
| Imaxe | Cada plano ilustra **o que se oe nese momento** (quen, que fai, onde, con que obxecto). Os cortes saen do sentido do texto (unha frase ou un anaco de frase), non dun reloxo. Composicións que **chaman a mirada** (rostros, mans, xestos, luz motivada, primeiro termo, profundidade) e xente facendo cousas na parte esperta. Referencias semente (D15) para o que SDXL non sabe debuxar. |
| Movemento | **Ningún plano fixo.** En CPU (4 núcleos, sen GPU nin clave de API nesta sesión): (a) **imaxe a vídeo (I2V)** cun modelo aberto para os planos con persoas que camiñan ou fan algo; (b) **paralaxe 2,5D** cun mapa de profundidade (cámara que avanza ou xira con relevo de verdade); (c) **microanimacións** (lume, fume, brétema, choiva, auga, ceo, candea). A peza MOVEMENTO mide que é posible e a que custo, e pon prezo a unha alternativa con GPU alugada para que decida o promotor (unha clave nova só chega a unha sesión nova). |
| Referencias | Como semente (img2img, ControlNet ou IP-Adapter), **só CC0, dominio público ou CC BY**, co crédito na descrición. As **CC BY-SA** só se amosan tal cal e co crédito, ou úsanse como semente se o promotor o decide (estudo de monetización §3.2: a imaxe xerada sería probablemente obra derivada e tería que compartirse con BY-SA). Ninguén as mirou aínda: hai que miralas antes de usalas. |
| Gañar | O Gauntlet remata cando un **tribunal a cegas** (v1 fronte a v2, sen saber cal é cal) elixe a v2 en cada unha das tres queixas, sen defectos bloqueantes, e coas portas automáticas da QA en verde. Despois xulga o promotor. |
| Honestidade | Distinguir sempre o automático do que fixo un axente Claude. Ningún axente ve o vídeo en movemento nin o oe: xulgan tiras de fotogramas, textos e medidas. Dicilo así en cada veredicto. |

## 3. Diagnóstico da v1 (o que hai que corrixir)

**Texto** (`gauntlet3/guion/guion-r3.txt`, 3.961 palabras):
- É unha lista de feitos máis ca unha historia: "segundo" sae 15 veces; no tramo dos minutos 6-11 hai 2,0 atribucións
  por cada 100 palabras (≈ 0,5 nas referencias); os casos son resumos de declaracións, sen escena
  (`gauntlet3/veredictos/guion-r2.md`).
- Non ten fío condutor: os capítulos (conxuro, procesos, tribunal, quen eran, lareira, San Xoán, Feijoo, choiva)
  suceden sen que un leve ao seguinte; a zona de durmir é un inventario de obxectos (escano, gramalleira, lacenas,
  capoeira) e de costumes.
- Causa técnica: a porta de veracidade pedía coincidencia léxica cun feito en cada frase, así que o guionista
  escribía paráfrases do dossier.

**Imaxe** (`gauntlet3/veredictos/tribunal-final.md` §2):
- Os planos cortábanse por tempo (curva), non por sentido. En 36 de 162 a imaxe non tiña o elemento que pedía o
  prompt ("falta: …") e 35 non pasaron a porta e saíron igual.
- Persoas en 76 de 162 planos, e facendo algo só en ≈ 25 (6 % na zona de durmir); moitos bodegóns e paisaxes
  baleiras; a figura soa de costas, repetida.
- Anacronismos: bombilla e radiador (plano 84), farolas (133), casa colonial (161), maleta de rodas (56), casas
  inglesas en "Vilalba" e "Xinzo", unha catedral inventada como Santiago.

**Movemento:** só Ken Burns (zoom ≤ 1,12x) e brétema ao 6 %.

**Rolda de arranxos da v1 (PR #5, fusionado en main o 02-10-2026):** cambiou os 11 planos que pedira o tribunal (5,
31, 56, 61, 67, 84, 91, 133, 145, 153 e 161), engadiu á porta máis anacronismos (radiador, fregadeiro, billas,
maleta de rodas, apliques…), mide o pico real (−1,7 dBTP) e enche a descrición cos datos reais
(`gauntlet3/video/arranxos/LEEME.md`). **A v1 de referencia para os críticos e o tribunal é esta versión arranxada**
(a que está agora en `gauntlet3/video/`). Non sabemos se as persoas do §1 viron a primeira montaxe ou a arranxada; as
súas tres queixas valen para as dúas.

**O que funcionou e non se pode perder:** o gancho (4/5: dous feitos verdadeiros e raros nos primeiros 35 s e tres
bucles que se pagan); o embude de voz, ritmo e luz; o son por escena (D13, D14); caras dignas sen clichés de bruxa;
a queimada do arranque, o gato no burato da porta, o castro sobre o Atlántico, Feijoo na cela e os nocturnos da zona
de durmir.

## 4. Listón

- **A v1**, a cegas: a v2 ten que gañarlle en texto, en correlación e atractivo da imaxe e en movemento.
- ***Historia Desconocida*, "Versalles en 1682"** (https://youtu.be/_lnOveSTjWA): clips xerados con xente que se
  move e planos que evolucionan (o promotor viuno; o estudo de setembro só tiña o storyboard, `gauntlet2/referencia.md`).
  Se se consegue o vídeo, sacar tiras de fotogramas para uso interno do crítico; nada de terceiros no repo.
- Para o texto, ademais da v1: a boa prosa narrativa galega como horizonte (ritmo, imaxe concreta, oralidade), nunca
  para copiala.

## 5. Pezas do Gauntlet 4

| # | Peza | Carpeta | Construtor | Crítico(s) | Gaña se |
|---|---|---|---|---|---|
| 0 | Contorno | `herramientas/pipeline/` | operador | `instalar.sh verificar` | todas as etapas pasan a proba mínima |
| 1 | Guion v2 | `gauntlet4/guion/` | guionista (Claude) | A: editor literario **a cegas** (v1 e v2 como texto A e texto B); B: filólogo (RAG) e verificador de feitos | A elixe a v2 e dálle ≥ 4/5 en unidade e en calidade literaria; B: 0 erros de feito e 0 graves de lingua despois das substitucións pechadas; portas automáticas en verde |
| 2 | Movemento | `gauntlet4/movemento/` e `herramientas/pipeline/movemento.py` | enxeñeiro de VFX | director de fotografía **a cegas** (tiras de fotogramas) | movemento natural, sen deformacións graves, en ≥ 90 % dos clips de proba; mellor ca a v1 a cegas; custo por plano medido e dentro do orzamento (§6.2) |
| 3 | Imaxe: referencias, modelo e porta | `gauntlet4/imaxe/` | director de arte | crítico visual | as sementes arranxan o que SDXL non sabe (aldea galega, hórreo, carro, palloza, lareira, queimada) nunha folla A/B; a porta v6 caza os defectos bloqueantes da v1 sen rexeitar de máis |
| 4 | Lista de planos v2 | `gauntlet4/planos/` | montador e director | espectador esixente (correlación) | ≥ 90 % dos planos ilustran o que se oe nese momento (nota ≥ 4/5); ≥ 60 % dos planos da parte esperta con persoas facendo algo; ningún arquetipo repetido de máis |
| 5 | Vídeo v2 | `gauntlet4/video/` | pipeline (produción) | tribunal final **a cegas** (v1 / v2) | a v2 gaña nas tres queixas, sen defectos bloqueantes, e coa QA automática en verde |

Cada rolda: borrador + veredicto (gañou/perdeu, maior carencia) → commit e push. Tope: 3 roldas por peza; se
ningunha gaña, segue a mellor, co motivo escrito. Orde: 0 → 1 e 2 en paralelo → 3 cando 2 libere a CPU → 4 (co
guion gañador) → voz → 5.

**Materiais a cegas:** prepáraos o orquestrador en `$SCRATCH/cego/<peza>/` (A e B ao chou, a clave en
`clave.txt`). O crítico non abre `clave.txt` nin os ficheiros que delatarían cal é cal ata gardar en git o seu
veredicto a cegas.

## 6. Formatos comúns

### 6.1 Lista de planos v2 (proposta; a peza 4 péchaa e as pezas 2 e 3 implementan contra ela)

```json
{"n": 12,
 "frases": [14],
 "desde": "E viu, contaba,",
 "texto": "E viu, contaba, a Ana González en figura de gato, que andaba saltando dun lado para outro.",
 "prompt": "…", "clave": "black cat", "negativo": "…", "tipo": "plano_medio", "son": "noite",
 "referencia": {"ficheiro": "06-cocina/Lareira_rural.jpg", "modo": "img2img", "forza": 0.55},
 "animacion": {"modo": "i2v", "camara": "avanza",
               "efectos": ["candea"], "accion": "a black cat leaps from the bench to the floor"}}
```

- `frases`: índices das frases do guion (os de `pipeline.partir`, os mesmos de `frases.json`) que cobre o plano;
  `desde`: se o plano empeza a metade dunha frase, as palabras exactas onde empeza.
- `referencia.modo`: `img2img`, `profundidade` (ControlNet de profundidade) ou `ipadapter`; só sementes con licenza
  permitida (§2).
- `animacion.modo`: `i2v` (clip xerado a partir da imaxe: persoas que se moven), `paralaxe` (cámara 2,5D) ou `fixo`
  (só para rótulos); `camara`: `avanza`, `recua`, `xira_esq`, `xira_der`, `sobe`, `baixa`, `pan_esq`, `pan_der`;
  `efectos`: `lume`, `fume`, `bretema`, `choiva`, `auga`, `ceo`, `candea`, `po`; `accion`: o movemento en inglés para
  o modelo I2V.

### 6.2 Orzamento de CPU (supostos [S] para planificar; a peza MOVEMENTO mídeos)

- CPU do 02-10-2026: Intel Xeon 2,8 GHz, 4 núcleos, AVX-512 **sen bf16 nin AMX** (`/proc/cpuinfo`). Imaxe
  SDXL-Lightning: ≈ 90-150 s por intento (`docs/APRENDIZAJES.md`); ≈ 2 intentos por plano.
- Voz ≈ 16 min; montaxe ≈ 70 min (máis co movemento); QA ≈ 30 min.
- Teito razoable para o movemento: ≈ 10-12 h de reloxo para o episodio enteiro (unha noite). Con 12 min (D18) e
  ≈ 65 planos son ≈ 8-10 min de CPU por plano: o I2V pode ir na maioría dos planos con persoas, e a paralaxe, que é
  barata, no resto. Imaxe: ≈ 3-4 h para ≈ 65 planos (máis intentos por plano e revisión dun axente de cada imaxe).
- A curva do embude (`curva.py`) está pensada para 30 min (nós en palabras fixas: gancho 280, transición 950): para
  12 min hai que escalala (peza 5).

## 7. Regras de traballo para os axentes (obrigatorias)

1. **Gardar en git cada pouco** (regra de `CLAUDE.md`): ao rematar cada borrador, rolda, experimento ou medida,
   `git add <rutas concretas>` (nunca `git add -A` nin `git add .`), `git commit` e `git push -u origin
   ccr-0584aac1-xqy2si`. Se `index.lock` está ocupado (outro axente), agardar uns segundos e reintentar; se o push
   falla por cambios remotos, `git pull --rebase origin ccr-0584aac1-xqy2si` e volver empurrar. Mensaxes en galego,
   empezando por `Gauntlet 4: <peza>: ...`, e rematando con estas dúas liñas:

       Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
       Claude-Session: https://claude.ai/code/session_011Mvqh6XmuGVpmihPtorogQ

2. **Non subir** ficheiros de máis de 50 MB nin binarios a medio escribir (validar con
   `ffmpeg -v error -i f -f null -` e escribir en temporal + renomear). Nada de modelos, venvs, cachés nin material
   de terceiros (fotogramas de Versalles, imaxes BY-SA) no repo; as referencias baixan con `docs/referencias-graficas/descargar.sh`.
3. **Aprendizaxes:** cada axente anota o aprendido (que funcionou, que non, cifras) en
   `gauntlet4/aprendizaxes/<peza>.md` segundo avanza; o orquestrador intégrao en `docs/APRENDIZAJES.md`.
4. **CPU e memoria compartidas:** 4 núcleos e **13,36 GiB para todos os procesos** (non os 15,7 de `free`). Todo o
   que use CPU ou memoria de verdade (modelos, xeración, render, NLI, LanguageTool, probas) vai con
   `flock "$CPU_LOCK" <orde>`; `nice` non abonda. Coller o candado **por experimento**, non durante horas, para que
   as outras pezas poidan pasar. **Desde o 02-10-2026 (23:20 UTC), co envoltorio `herramientas/gauntlet/candado.sh`:**
   `candado.sh <orde>` para os experimentos normais e `candado.sh --prioridade <orde>` para o camiño crítico (portas
   do guion, voz, probas curtas que agardan outras pezas): cun prioritario agardando, os normais ceden a vez. **Non
   aniñar candados:** se a orde xa o colle por dentro (`instalar.sh verificar`), lanzala sen envoltorio. Disco: ≈ 30 GB libres ao empezar, e o contorno colle ≈ 16 GB: borrar o que non se
   use (modelos de probas descartadas).
5. **Contorno:** `export SCRATCH=/tmp/claude-0/-home-user-revolta/c92eba35-e89d-5d11-bb3d-f517a84dab48/scratchpad`
   e despois `source herramientas/pipeline/entorno.sh` (HF_HOME, PY, CPU_LOCK…). Se aínda non está instalado, a
   marca `$SCRATCH/.instalado/limpieza.ok` aparece ao rematar `instalar.sh`. Para modelos con dependencias novas
   (vídeo), un venv aparte no scratchpad: non tocar as versións do venv principal.
6. **Traballos longos** (> 25 min): `setsid nohup … > log 2>&1 &` e mirar o log; as tarefas en segundo plano da
   ferramenta Bash córtanse aos 30 min. `awk` é `mawk` (`awk -W interactive` nos vixiantes). O ffmpeg estático dá
   *segfault* ao ler `.ts`.
7. **Honestidade:** distinguir o automático do que fixo un axente Claude. Non maquillar veredictos.
8. **Evidencia:** cada cifra con fonte (URL) ou marcada como suposto [S].
9. Devolver ao orquestrador un resumo **curto** (≤ 15 liñas): que se fixo, onde está e que falta.
10. **Público:** galego normativo; nada inventado; a lenda como lenda; o aviso falado literal ("A voz que vas escoitar
    é sintética, e este texto preparouno un proceso automático."); vetos de imaxe de `gauntlet3/contexto.md` §8.5
    (nariz ganchuda, verrugas, sombreiro de pico, caldeiro, vasoira de bruxa, autos de fe, capirotes, chamas sobre
    persoas, partos explícitos).

## 8. Decisións novas do promotor durante o Gauntlet 4

- **02-10-2026 (D19):** usar na imaxe as referencias gráficas buscadas (§1 e §2).
- **02-10-2026, 22:58 UTC:** "Asegúrate de que se vai gardando o contido do scratchpad dos axentes e as anotacións
  parciais do Gauntlet no repo para poder relanzar se é preciso" → instantánea do scratchpad cada 20 min
  (`herramientas/gauntlet/instantanea.py`), encargos literais en `encargos/`, `estado.md` do orquestrador e un
  `estado.md` por peza.
- **02-10-2026, 23:05 UTC (D18) — PRIORITARIO:** *"Dame igual facer unha v2 máis curta (12 min) pero quero amosar
  calidade"*. A v2 dura **≈ 12 min** (≈ 1.500-1.700 palabras, 3-5 capítulos, ≈ 60-75 planos). **A calidade manda**
  sobre a cobertura e o custo: menos casos e menos nomes, escenas máis fondas; máis I2V, máis intentos por imaxe e
  revisión dun axente de cada plano. Embude comprimido: gancho ≈ 0-1:30, transición ata ≈ 5 min, calma ata ≈ 8:30 e
  peche de durmir ata o final.
- **02-10-2026, 23:05 UTC:** *"Asegúrate de rearrancar si te paras por cuota"* → revisión horaria programada que
  retoma o Gauntlet (axentes e procesos) despois dun corte por cota ou dun reinicio (`estado.md`).
