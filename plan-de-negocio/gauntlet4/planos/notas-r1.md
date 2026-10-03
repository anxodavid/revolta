# Lista de planos v2 · rolda 1 · notas do montador (Gauntlet 4, peza PLANOS)

Montador e director: axente Claude, 03-10-2026. **Quen fixo que:** o corte, os prompts, as accións, o son, as
sementes e as prioridades son de Claude; o `texto` de cada plano sae automaticamente de `frases.json` da voz
(`scripts/xerar_lista.py`); os tempos, de `longo.py --so-planos` (automático; Whisper por palabras nos dous `desde`);
as medidas, de `scripts/medir_lista.py`. **Ningunha persoa revisou a lista e aínda non hai ningunha imaxe xerada:**
o que se di da imaxe é previsión.

Entregas: [`escenas-v2.json`](escenas-v2.json) (77 planos), corte por sentido en
[`herramientas/pipeline/longo.py`](../../../herramientas/pipeline/longo.py), estas notas, [`estado.md`](estado.md) e
[`../aprendizaxes/planos.md`](../aprendizaxes/planos.md).

## 1. Decisións

**Corte por sentido.** Un plano = unha imaxe que di o que se oe. Xúntanse frases curtas só cando unha imaxe as cobre
enteiras (35-36 "Auga de sete fontes para o gando. E para elas, nin auga." → nai e filla nun limiar cunha xerra
baleira); pártense frases só onde teñen dous momentos visibles: a 4 (o ano 1967 / o barco amarrado, `desde`
"escribiuno Mariano Marcos Abalo") e a 6 (a testemuña / a parteira, `desde` "que a parteira Dorotea do Barro").
Os cinco capítulos abren plano co rótulo (longo.py compróbao).

**Número de planos: 77** (o encargo di ≈ 60-75; a curva propuña 78). Coas duracións por fase do encargo saen ≈ 80
(§2); quedou en 77 sen planos de dúas ideas. Se o orzamento de imaxe aperta, as fusións menos custosas para a
correlación son 14+15 (os papeis e a palabra trabucada), 60+61 (a fábula e o voo soñado) e 72+73 (as brasas e a
avoa que conta).

**Que se ve.** Persoas facendo algo en case todos os planos da parte esperta (§2); bodegóns só onde a frase fala dun
obxecto (os papeis, a folla sen nome, a candea). As frases abstractas atan ao fío do guion: as palabras (o escribán
que escribe e emenda, a folla rota onde ía a sinatura, o legaxo atado), a auga (fontes, cántaros, a cunca baleira) e
o lume (a queimada, a candea). Ao durmir, calma pero non baleiro: a fonte que reborda, as herbas no orballo, as
brasas, o gando que dorme, o regato baixo a chuvia, a candea que se apaga, a chuvia na lousa; sen caras á cámara.

**Personaxes recorrentes** (táboa `personaxes` do JSON, texto en inglés idéntico en cada prompt, comprobado por
código): Dorotea (6, 13, 29, 30; mans no 7), María (20, 21, 23, 24, 28-30), o escribán (5, 12, 25, 28, 45), a testemuña (5,
25), o xuíz (20, 40, 42, 45, 46), o vicario (29, 40), o inquisidor (40, 41), María Cibreira (43, 46; de costas no
45), Mariano e os amigos de 1967 (3, 33, 34; siluetas no 4 e no 70), os veciños de Campo Lameiro (48-50), a moza de
san Xoán (16, 54, 66), a menciñeira (18, 57), Feijoo (59), Sarmiento (58) e os da queimada do XX (69, 71). Idades,
roupa e cabelo fixos: Dorotea ≈ 60, pano marrón; María ≈ 30, trenza e pano vermello esvaído; o escribán ≈ 40, gibón
negro e colo branco.

**O que SDXL fai mal (biblia v2 §4).** Ningún "kitchen", "street", "road", "door" nin "house" sós: "bare granite room",
"smoke-blackened room", "path between mossy granite walls", "heavy oak door of a granite house", "small shuttered
opening"; luz de candea, lanterna de corno, lúa ou lume; encadres pechados (portas, muros, beirados, limiares) en vez
de casas enteiras, porque non hai semente permitida de aldea de lousa vista de fóra. Negativos por plano (luz
eléctrica, fiestras de vidro, roupa de hoxe e o que cada escena arrisca: farolas no porto, casa con cheminea de
ladrillo nos hórreos, zapato moderno, tixola de ferro).

**Rigor e vetos.** 1617, 1639 e 1643 con roupa do XVII; a queimada, o barco de 1967, as copias e o rexistro de 2001
co campo `epoca: "xx"` (tamén o arquivo de hoxe, plano 27, para que a porta non conte a roupa actual). Sen bruxas
de conto, caldeiro, vasoiras nin autos de fe; o parto de Dorotea sen nada explícito (6); a tortura de María Cibreira
non se ve (43); a súa confesión das "areas de Sevilla" vese como o interrogatorio (45, con demos no negativo); as
tres xustizas, cada xuíz na súa mesa (40), para non suxerir un tribunal común; a Inquisición "branda" sen
execucións (41); o salto de san Xoán, siluetas lonxe sobre brasas baixas (65), non lapas sobre persoas. O que a
lista engade sen estar no dossier é xenérico (roupa, luz, xestos) ou simbólico e dise como tal: as copias de
"finais do XX" nunha tenda (36: o dossier non di cando nin como se venderon) e a man maior que asina en 2001 (37: non
consta a idade do autor).

**Sementes (D19, informe de IMAXE §4).** Catro, das permitidas: a dorna amarrada ao peirao de noite (11-01) para o
vello barco (4, img2img 0,5); os hórreos de Muimenta (01-02) para o rótulo (10, profundidade 0,6, con `recorte`
que deixa fóra a casa con cheminea de ladrillo); a lareira de granito (06-01) para nai e filla ao lume (55, img2img
0,75: espazo con xente); a tarteira con cuncas (07-01) para os ingredientes da queimada (68, img2img 0,5: obxecto).
A lapa azul vai sen semente (o informe: sae mellor). Non hai semente permitida de fonte, escano, aldea de lousa
vista de fóra nin roupa do XVII. Créditos en `imaxe/referencias.json`.

**Movemento (D16).** Ningún plano fixo: 57 con I2V (27 de prioridade 1 e 30 de prioridade 2) e 20 con paralaxe 2,5D
(cámara e microanimacións). Accións curtas, físicas e lentas (falar, escribir, verter, camiñar cara á cámara, unha
vaca que bebe, unha moza que lava a cara). Ningún camiñante de costas. **Aviso para MOVEMENTO:** moitos planos
I2V da calma e do durmir duran 10-20 s e un clip de LTX dura ≈ 2 s (4 s con cámara lenta): ou clips máis longos, ou
o I2V de prioridade 2 neses planos pasa a paralaxe.

**Arquetipos previstos** (topes da porta con 77 planos: mans ≤ 5, retrato ≤ 7, persoa á lareira ≤ 5, grupo de pé ≤
4, camiñantes de costas ≤ 3; separación ≥ 5): §2. Nos planos seguidos da queimada só un nomea o lume (a porta só
conta "persoa á lareira" se o prompt di fire, flames, hearth, embers ou firelight).

**Riscos para o crítico e para IMAXE.** (1) Sete prompts pasan de 55 palabras por levar dous personaxes enteiros
(28, 29, 40, 45, 54, 69, 71): o esencial vai primeiro, pero CLIP corta aos 77 tokens. (2) Pseudotexto nos papeis
(15, 26, 27, 38, 41): a letra é o suxeito, pero pode saír rara. (3) Saltos en I2V (8, 65). (4) Os ollos na escuridade
(64) e a sombra do paxaro (61) poden saír ben ou nada. (5) 21 e 22 ilustran o que "dicían" de María, non feitos: a
imaxe amosa o rumor (vista desde detrás dun muro, os veciños que murmuran).

## 2. Medidas

Automáticas ([`medidas-r1.json`](medidas-r1.json), `scripts/medir_lista.py` sobre o `planos.json` que escribe
`longo.py --so-planos`); os campos `persoas` e `arquetipo_previsto` que conta son xuízos do montador.

| Fase | Planos | Media | Mín-máx | Obxectivo | Fóra do obxectivo |
|---|---|---|---|---|---|
| gancho | 19 | 5,2 s | 3,7-7,2 s | 3-6 s | 9 (o aviso, 7,2 s); 12, 16, 18, 19 (6,2-6,8 s: unha frase cada un) |
| transición | 19 | 7,6 s | 5,0-12,5 s | 5-9 s | 23, 27, 29 (12,0-12,5 s: dúas frases dunha soa escena) |
| calma | 24 | 10,4 s | 6,8-15,4 s | 8-14 s | 39, 50, 51, 53, 60 (6,8-7,8 s: frases soas); 55, 59 (14,2-15,4 s) |
| durmir | 15 | 17,2 s | 9,4-27,1 s | 12-20 s | 67 (9,4 s), 73 (10,9 s); 65, 66, 74, 75 (20,7-22,7 s); 77 (27,1 s, coa cola de choiva) |

- **Persoas na parte esperta** (planos 1-62): **44 de 62 facendo algo (71,0 %)**, 47 (75,8 %) contando os 3 de
  mans soas; 5 con persoas quietas e 10 sen persoas (os papeis, a letra emendada, a candea do aviso, os hórreos do
  rótulo, a folla sen nome, a fonte do capítulo IV, o legaxo co que se deixan os papeis). Ao durmir: 6 de 15 con
  persoas que fan algo (o salto de san Xoán, a moza que lava a cara, a queimada, o dito, a avoa que conta), 8 sen
  persoas.
- **Arquetipos previstos:** retrato 2, 13, 25, 60; mans 7, 26, 37, 68 (separación mínima 11 nos dous); grupo de pé
  22, 52; persoa á lareira 55. **Camiñantes de costas: ningún** (a figura soa de costas da v1 non volve).
- **Sementes:** 4 planos (4, 10, 55, 68). **Movemento:** 57 I2V (27 de prioridade 1, 30 de prioridade 2), 20
  paralaxe, 0 fixos. Cámaras: avanza 34, recua 11, pan 15, baixa 7, xira 8, sobe 2.
- **Cortes a metade de frase:** 2, os dous colocados por Whisper (plano 4: 15,87 s; plano 6: 25,19 s; a parte
  proporcional polos caracteres daría 15,89 e 25,05 s).
- **Son:** voz limpa 28, lume 9, aldea 9, noite 6, fonte e noite 6, mar 4, choiva 3, campás 2, vento 2, xente 2,
  e catro mesturas.
- **Prompts:** media de 42,8 palabras; 7 pasan de 55 (§1, riscos).
- **Correlación imaxe-texto:** sen imaxes non se pode medir; todos os planos levan `texto_en` para `correlacion.py`.

## 3. Corte por sentido en `longo.py`

- Se todos os planos da lista traen `frases`, `planos_por_sentido()` substitúe a `planos()`: cada plano empeza 0,25 s
  antes da súa primeira frase (`tempos_frases.json`), o que abre capítulo empeza co rótulo e o primeiro en 0; un
  `desde` empeza 0,12 s antes da súa palabra, coa marca de tempo de Whisper (o modelo do QA, `word_timestamps=True`,
  sobre o wav da frase; palabras aliñadas co texto con difflib; caché en `marcas_desde.json`) ou, se non a atopa, a
  parte proporcional polos caracteres. A curva segue dando fase, fundido e luz; o Ken Burns queda de reserva para os
  planos sen `animacion`.
- Comprobacións con erro explícito: `n` seguidos, frases consecutivas e existentes, cada plano onde acaba o anterior,
  o `desde` dentro da súa frase, ningún capítulo partido nin no medio dun plano, a lista ata a última frase. Probadas
  con catro listas rotas (oco, `desde` que non está, capítulo no medio, frases que faltan).
- `ler_escenas` pasa tamén `referencia`, `epoca`, `texto_en` e `prioridade_i2v` (e `animacion`, como xa facía).
- `--so-planos`: monta só ata os planos, escribe `escenas.json` e `planos.json` (con `frases`, `desde`, `t0` e o
  método) e imprime os planos e as duracións por fase. Se están todos os wav da voz, xa non lanza `voz_st2.py`.
- **Proba** (`$SCRATCH/planos/so_planos.sh`, co candado prioritario, 03-10-2026): rc 0 en 7 min 41 s, case todo
  nas portas de texto, que volveron pasar porque a súa caché non valeu (en verde, 0 frases sen xustificar); voz da
  caché sen cargar StyleTTS2; 77 planos e os 2 `desde` por Whisper. A referencia da curva quedou en
  `$SCRATCH/v2/w/planos-curva.json`.
- **A v1 non cambia:** sen `frases` na lista (ou sen lista) corre `planos()` coma sempre.

## 4. Para despois

- O crítico (correlación e atractivo) le cada parella texto-prompt; despois, imaxes coa porta v6 e o movemento.
- MOVEMENTO: decidir clips longos ou paralaxe para os I2V de 10-20 s; o orzamento escolle entre as prioridades 1 e 2.
- IMAXE: mirar primeiro os planos con risco (§1) e os de semente; se un prompt longo perde o final, levar a luz e a
  época ao `negativo`/`tipo` en vez de acurtar os personaxes.
