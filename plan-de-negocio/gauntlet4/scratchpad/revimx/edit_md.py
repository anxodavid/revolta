"""Engade a segunda pasada (planos 43-77) a video/revision-imaxes-r1.md (axente Claude, revisor de imaxes)."""
from pathlib import Path

SCR = Path('/tmp/claude-0/-home-user-revolta/c92eba35-e89d-5d11-bb3d-f517a84dab48/scratchpad/revimx')
P = Path('/home/user/revolta/plan-de-negocio/gauntlet4/video/revision-imaxes-r1.md')
s = P.read_text()


def rep(old, new):
    global s
    assert s.count(old) == 1, old[:80]
    s = s.replace(old, new)


rep('# Revisión das imaxes escollidas da v2 · rolda 1 · planos 1-42 (Gauntlet 4)',
    '# Revisión das imaxes escollidas da v2 · rolda 1 · planos 1-77 (Gauntlet 4)')
rep('''**Quen:** un axente Claude (revisor de imaxes), o 03-10-2026 entre as 14:55 e as 15:30 UTC. **Ningunha persoa revisou
estas imaxes.** Primeira pasada (planos 1-42). Os planos 43-77 van nunha segunda pasada cando remate o proceso de
imaxes, nos mesmos ficheiros.''',
    '''**Quen:** un axente Claude (revisor de imaxes), o 03-10-2026, en dúas pasadas: planos 1-42 entre as 14:55 e as 15:30
UTC (o orquestrador xa a aplicou) e planos 43-77 entre as 17:55 e as 19:15 UTC. **Ningunha persoa revisou estas
imaxes.**''')

rep('''## Contas (planos 1-42)

| Decisión | Planos | Cantos |''', '''## Contas

| Decisión | Planos 1-42 | Planos 43-77 | **Total 1-77** |
|---|---|---|---|
| Vale | 18 | 11 | **29** |
| Outro intento | 7 | 3 | **10** |
| Rexenerar | 17 | 21 | **38** |

**Primeira pasada (planos 1-42):**

| Decisión | Planos | Cantos |''')

rep('''| **Rexenerar** | 2, 6, 7, 9, 10, 17, 18, 20, 21, 22, 29, 31, 38, 39, 40, 41, 42 | **17** (2 con semente: 10 e 21) |

Os problemas máis repetidos:''', '''| **Rexenerar** | 2, 6, 7, 9, 10, 17, 18, 20, 21, 22, 29, 31, 38, 39, 40, 41, 42 | **17** (2 con semente: 10 e 21) |

**Segunda pasada (planos 43-77):**

| Decisión | Planos | Cantos |
|---|---|---|
| **Vale** | 43, 50, 53, 55, 56\\*, 57, 59\\*, 60, 62\\*, 66, 75 | **11** (3 contra a porta\\*) |
| **Outro intento** | 71 → [0]\\*, 73 → [2]\\*, 76 → [0]\\* | **3** (os tres cun intento que a porta rexeitara\\*) |
| **Rexenerar** | 44, 45, 46, 47, 48, 49, 51, 52, 54, 58, 61, 63, 64, 65, 67, 68, 69, 70, 72, 74, 77 | **21** (2 con semente: 68 e 70) |

Os problemas máis repetidos na primeira pasada (1-42):''')

rep('''sombreiro de pico, nariz ganchuda nin verruga.
''', '''sombreiro de pico, nariz ganchuda nin verruga.

Na segunda pasada (43-77):

1. **Fontes de xardín e de parque** no canto da fonte de aldea (47, 51, 63 e, pequena, no 66), e ningunha fonte onde
   facía falta (49, 54). Os prompts novos piden en todos a mesma fonte rústica: un cano de pedra nun muro de granito
   con musgo e unha pía.
2. **Lume:** a queimada laranxa (69; no 72, nunha pota negra de ferro), un incendio no canto das brasas da cacharela
   (65) e luz de día cando o texto di «apáganse as luces» (68).
3. **Xente doutro tempo ou doutro sitio:** damas e xuíces do XIX (45, e o 46 cunha viñeta branca de retrato
   antigo), labregos irlandeses con tellados de herba (48 e, ao fondo, o 57), paredes encaladas mediterráneas (44) e
   un rito de túnicas con capucha arredor dun lume (52, que lembra os vetos).
4. **Falta a clave ou a idea:** sen talla (64), sen a herba nin a curandeira de Sarmiento (58), sen o soño do voo e
   cunha muller tendida coma amortallada (61), ninguén espreitando (49).
5. **Anacronismos:** vacas frisoas e lámpadas de parede (74), fiestras de vidro (67), unha bufarda inglesa con
   fiestras acesas na última imaxe (77) e un vaso que parece de papel (44). No 76 a porta volveu aprobar a reserva
   xenérica (un bosque) sen a candea.
''')

rep('''  do prompt (no 6 perdeuse o home). O `negativo` vai completo (substitúe o do plano) e só o usa a porta (CLIP), xa
  que coa produción en `IMG_CFG_REINTENTO=0` non hai intentos guiados. Sen `semente`, como pide o orquestrador.
''', '''  do prompt (no 6 perdeuse o home). O `negativo` vai completo (substitúe o do plano) e só o usa a porta (CLIP), xa
  que coa produción en `IMG_CFG_REINTENTO=0` non hai intentos guiados. Sen `semente`, como pide o orquestrador.
- **Segunda pasada:** `revision.json` copiado ás 17:53 UTC (77 entradas; só lido), coas mesmas follas
  (`follas-planos-43-48.jpg` … `follas-planos-73-77.jpg`) e detalles (`detalles-43-44-50-59`, `detalles-44-62`,
  `detalles-68-71-73-76`). O JSON leva agora os planos 1-77. As entradas dos planos 1-42 non cambiaron: se xa están
  aplicadas, abonda coas dos planos 43-77, e aplicar o JSON enteiro repite as mesmas escollas e os mesmos prompts.
''')

taboa2 = (SCR / 'taboa2.md').read_text()
fila42 = [l for l in s.splitlines() if l.startswith('| 42 | rexenerar | — |')][0]
rep(fila42 + '\n', fila42 + '\n' + taboa2)

rex2 = '''| 44 | casa de granito rústica, pote pequeno de unguento e muller cun neno; a curandeira co pano negro do elenco | plastered walls, amphora, olive trees, paper cup | non |
| 45 | de costas, a campesiña de pano gris (a Cibreira do 43); o xuíz e o escribán do elenco | chandelier, ball gown, earrings | non |
| 46 | dous perfís: o xuíz le a pregunta e a Cibreira asente calada | vignette, white frame, bonnet | non |
| 47 | fonte de aldea: cano de pedra nun muro de granito con musgo e pía, castiñeiros e o brillo lonxano da fogueira | statue, ornamental fountain, park, buildings | non |
| 48 | a porta da corte (sen casas á vista), a muller acusada e os animais mortos na palla | turf roof, thatched cottage, sheep | non |
| 49 | os dous veciños agachados tras o muro, mirando as mulleres na fonte | ornamental fountain, houses | non |
| 51 | cano de pedra e pía de noite, entre follas escuras; sen os ollos | metal tap, ornamental fountain | non |
| 52 | tres veciñas con mantón e pano rindo arredor da fonte, vistas de lonxe entre ramas | hooded robes, cloaks, ritual, arcade, columns | non |
| 54 | na fonte de noite: a moza enche o cántaro e a vella de pano negro persígnase mirando á escuridade | table, teapot | non |
| 58 | Sarmiento robusto e de cara redonda (elenco), coa curandeira do chal azul (a do 18 e do 57) e a herba | skullcap | non |
| 61 | durmindo de lado baixo unha manta, coa sombra do paxaro na parede | corpse, coffin | non |
| 63 | a lúa na auga da pía da mesma fonte rústica, de noite | statue, ornamental fountain, daylight | non |
| 64 | a talla de barro ao principio do prompt, enriba do muro, de noite | concrete | non |
| 65 | un anel baixo de brasas case apagadas e siluetas pequenas | wildfire, big flames | non |
| 67 | só a trabe afumada e o muro de granito, sen porta nin fiestra | flowerpots, shutters | non |
| 68 | o mesmo prompt, de noite | daylight | **07-01** («Camino de Santiago, May 2008», CC BY 2.0), profundidade 0,6 (antes img2img 0,5) |
| 69 | lapas azul pálido no cazo e na cunca, o vello e a vella xuntos | orange fire, cauldron | non |
| 70 | barco vello e pequeno no peirao, brillo azul e tres figuras | tall ship | **11-01** (dorna de Rianxo, CC BY 2.0), img2img 0,5: a mesma do 4 |
| 72 | cunca de barro parda coas últimas lapas azuis e o brillo vermello das brasas | cauldron, iron pot, fireplace, orange flames | non |
| 74 | dúas vacas pardas, corte de pedra escura e unha lanterna pequena | black and white cows, wall lamp | non |
| 77 | encadre pechado nas lousas molladas, sen casa | window, dormer, chimney | non |
'''
fila42r = [l for l in s.splitlines() if l.startswith('| 42 | contraplano')][0]
rep(fila42r + '\n', fila42r + '\n' + rex2)

rep('''Martínez (CC BY 2.0) e «Palloza Cantexeira» de FCPB (CC BY 3.0), vía Wikimedia Commons (URL en
`imaxe/referencias.json`).''', '''Martínez (CC BY 2.0), «Palloza Cantexeira» de FCPB (CC BY 3.0), «Camino de Santiago, May 2008» de Alex Chang (CC BY
2.0) e «Dorna a vela. Rianxo de noite» de Xoan Anton (CC BY 2.0), vía Wikimedia Commons (URL en
`imaxe/referencias.json`).''')

# sección da porta: substitúese enteira
ini = s.index('## Que fai a porta v6 nestes 42 planos')
fin = s.index('## Notas para MOVEMENTO')
s = s[:ini] + '''## Que fai a porta v6 (planos 1-77)

| | Planos 1-42 | Planos 43-77 | Total |
|---|---|---|---|
| Escollidas que aprobou | 29 | 24 | 53 |
| … destas, a rexenerar | 12 | 14 | 26 |
| … destas, cun intento mellor | 4 | 2 | 6 |
| Planos onde rexeitou todos os intentos | 13 | 11 | 24 |
| … destes, cun intento que vale | 8 | 4 | 12 |

- **Deixa pasar de máis, e é o que máis pesa:** 32 das 53 escollidas que aprobou tiñan un problema. Non ve
  lampadarios nin salóns de palacio, fiestras de vidro en casas de aldea, baixantes, bancos de parque, faroles de
  parede, vasoiras, fontes de xardín, roupa do XIX, tellados de herba, paredes encaladas, ritos de capucha, bufardas
  nin vacas frisoas, nin a queimada convertida en caldeiro ou fogueira. Tampouco bloquea cando falta a clave («falta:
  ...» só avisa), e aproba as reservas xenéricas (35 [3] e 76 [3]), que non teñen nada do que se oe.
- **Rexeita de máis:** en 12 dos 24 planos que rexeitou había un intento que vale.
  - Por *texto na imaxe* nos planos de escritura (12, 15, 19, 26, 32, 37 e 59). O problema era a letra lexible ou de
    imprenta, non o texto.
  - Por *animais en grupo* cando o texto pide o gando ou as ovellas (23, 56).
  - Por *repetición* nos ecos buscados (62 co 26; tamén o intento [0] do 76 co 9).
  - Por un *iate moderno* que non hai (33) e por *mans* que non vin (25 [1], 30 [0]).
  - Por *lume vivo ao durmir* cando era unha lareira ao fondo (73) ou o barro laranxa da cunca (68, que si hai que
    rexenerar, pero pola luz de día).
- **Acerta ao rexeitar** en 12 planos, ás veces polo motivo equivocado: zapatos modernos (7, dixo «interior
  moderno»), bombilla e fiestras (18, 67), casas inglesas (21), lentes (41), pseudotexto (31), farolas (47), sen fonte
  (54), incendio (65), luz de día (68, dixo «lume vivo»), caldeiro (72) e lámpadas (74).
- **Ideas para a peza IMAXE** (non as probei):
  - Que «texto na imaxe» só avise cando a clave é de escritura (papers, page, quill, document, sheet), e «animais en
    grupo» cando a clave é o gando.
  - Sondas CLIP para «crystal chandelier», «palace hall», «park bench», «drainpipe», «broom», «bonfire», «ornamental
    fountain», «turf roof» e «Holstein cow».
  - Que «lume vivo ao durmir» mida só as lapas e non o barro.
  - Non aceptar sen revisión un intento con `reserva: true`.

''' + s[fin:]

rep('''- **8:** o I2V do salto é o máis fráxil (xa o dixo o crítico de planos); se deforma, paralaxe.
''', '''- **8:** o I2V do salto é o máis fráxil (xa o dixo o crítico de planos); se deforma, paralaxe.
- **53:** levan caldeiros metálicos, non cántaros. Proposta: «the women walk slowly toward the camera carrying their
  water pails».
- **55:** non hai morteiro. Proposta: «the mother slowly crushes herbs between her hands while the girl watches the
  small fire».
- **56 ([0]):** hai un só home. Proposta: «the sheep graze slowly while the old man watches them».
- **57:** o becerro está deitado. Proposta: «the healer slowly moves her hands over the calf and the calf lifts its
  head».
- **60:** é un mozo quen murmura. Proposta: «the young man whispers into her ear and she slowly raises her eyes».
- **66:** ten unha cunca na man. Proposta: «she slowly lowers the bowl and brings the herb water to her face».
- **71 ([0]):** son dúas vellas. Proposta: «she wags her raised finger as she speaks and the other old woman laughs
  softly».
- **73 ([2]):** a nena está esperta lendo. Proposta: «the grandmother turns a page and speaks softly while the child
  leans against her».
- **76 ([0]):** hai dúas velas. Proposta: «the two candle flames tremble and slowly go out, leaving thin threads of
  smoke».
''')

rep('''- **Mariano e os amigos** (3 [1], 33, 34): camisa branca e sen o xersei escuro, coherentes entre si.
''', '''- **Mariano e os amigos** (3 [1], 33, 34): camisa branca e sen o xersei escuro, coherentes entre si. O barco do 70
  rexenérase coa semente do 4, para o eco buscado.
- **María Cibreira:** no 43 leva o pano gris do elenco; no 45 e no 46 saía unha dama do XIX, e rexenéranse co pano
  gris. A súa nai (44) rexenérase co pano negro e o pelo branco do elenco.
- **A curandeira do chal azul:** o 57 é coherente co 18, que se rexenera co mesmo chal; o 58 rexenérase con ela.
- **A moza da trenza:** o 16 e o 66 son coherentes (blusa branca e trenza longa); o 54 rexenérase con ela.
- **Os veciños de Campo Lameiro:** no 50 levan chalecos de la parda; o 48 e o 49 rexenéranse cos de pel de ovella do
  elenco (diferenza pequena).
- **Feijoo e Sarmiento:** o 59 [2] ten dous monxes vellos (Feijoo, co capucho); o 58 rexenérase cun Sarmiento robusto
  e de cara redonda, para non confundilos.
- **Os vellos da queimada:** o 71 [0] ten dúas vellas e non o vello; o 69 rexenérase coa parella.
''')

ini = s.index('## Pendente')
s = s[:ini] + '''## Pendente

- Mirar os 38 rexenerados cando saian (17 da primeira pasada e 21 da segunda). Nos de escritura (31) a porta volverá
  rexeitar por texto. Nos de semente (10, 21, 68 e 70), ver se a foto arrastra algo do presente. Se a porta rexeita o
  70 por repetición co 4, escollelo a man. Se o 68 volve saír de día, vale o [0].
- Levar á lista de produción as accións I2V da segunda pasada (sección de MOVEMENTO).
'''
P.write_text(s)
print('ok', len(s))
