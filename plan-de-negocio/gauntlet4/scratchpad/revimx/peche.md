
## Planos a rexenerar: que cambia no prompt

Os prompts completos e os negativos están no JSON (`rexenerar`). Resumo dos cambios:

| n | Cambio principal | Negativo engadido (para a porta) | Semente |
|---|---|---|---|
| 2 | «pale blue flames» ao principio; cazo de madeira e cunca de barro parda («earthenware») | cauldron, iron pot, frying pan | non (o informe §4: o lume azul sae mellor sen semente) |
| 6 | só o esencial: parteira axeonllada, preñada na palla, home na porta; prompt curto para que non se trunque | metal bed, sofa | non |
| 7 | chinela de coiro brando (como a do plano 8) no canto de «zapato»; a parteira enteira, para que as mans teñan corpo | boots | non |
| 9 | vela fina de cera nun candeeiro de ferro forxado, mesa de carballo e parede de granito | pillar candle, fruit | non |
| 10 | hórreos de madeira e de granito con tornarratos, tellados de pedra, ao serán con brétema | wall lantern, grass roof | **01-02** (Muimenta, CC BY 2.0), img2img 0,5, mesmo recorte |
| 17 | encadre pechado no limiar (sen fachada nin fiestras), a vella debullando fabas | broom, white cap | non (non hai semente de porta de casa) |
| 18 | cama de palla, herbas nas trabes, luz do lume, «smoke-blackened granite walls» | shelves of bottles | non (a 06-01 xa a usa o 55: repetiríase) |
| 20 | mesa simple de madeira, paredes de granito, raio de luz estreito; sen «court» nin «hall» | chandelier, arched windows, red cloak | non |
| 21 | casa de pedra con teito de palla, porta de madeira, lanterna | chimney, red cloak, hood | **03-01** (palloza Cantexeira, CC BY 3.0), profundidade 0,6, recorte [0, 0,3, 0,54, 0,7] sen a cheminea metálica nin a fiestra actual |
| 22 | porta románica de arco de medio punto dunha igrexa pequena de granito | drainpipe, gutter | non (a 12-03 é só unha cornixa) |
| 29 | capela rústica pequena; as dúas mulleres soas | columns, crowd | non |
| 31 | lupa de latón sobre manuscrito de tinta parda, pouca profundidade de campo, letra borrosa | (sen cambios) | non |
| 38 | cunca de barro con lapas azuis pálidas, sen fogueira | bonfire | non |
| 39 | cunca con lapas azuis pálidas na cuberta, só os pés dos tres homes | bonfire, burning boat | non |
| 40 | tres xuíces sentados xuntos: xuíz de toga negra, cura de sotana, frade de hábito branco e capa negra | chandelier, crowd | non |
| 41 | frade ancián de tonsura, hábito branco e capa negra (o inquisidor do elenco), sen lentes | glasses, bookshelves | non |
| 42 | contraplano por detrás do xuíz na súa mesa alta, tres acusadas nun banco tosco | park bench, trees | non |

Créditos das sementes propostas (CC BY pide crédito): «Hórreos de Muimenta, Carballeda de Avia» de José Antonio Gil
Martínez (CC BY 2.0) e «Palloza Cantexeira» de FCPB (CC BY 3.0), vía Wikimedia Commons (URL en
`imaxe/referencias.json`). Para a palloza mirei a foto cunha grade antes de escoller o recorte; a foto non vai ao
repo (material de terceiros).

## Que fai a porta v6 nestes 42 planos

- **Aprobou 29 escollidas; destas, 12 hai que rexeneralas** (2, 6, 9, 10, 17, 20, 22, 29, 38, 39, 40, 42) e **en 4
  había un intento mellor** (3, 25, 30 e o 35, onde aprobou a reserva xenérica sen a clave). Non ve: lampadarios e
  salóns de palacio, fiestras de vidro en casas de aldea, baixantes, bancos de parque, faroles de parede, vasoiras,
  a queimada convertida en caldeiro ou fogueira e a ausencia da clave («falta: ...» só avisa).
- **Rexeitou os tres intentos en 13 planos; en 8 deles había un intento que vale** (12, 15, 19, 23, 33 o escollido;
  26, 32, 37 outro). Rexeita de máis por *texto na imaxe* nos planos de escritura (o problema era a letra lexible ou
  de imprenta, non o texto), por *animais en grupo* cando o texto pide o gando (23), por un *iate moderno* que non hai
  (33) e por *mans* que non vin (25 [1], 30 [0]). Nos outros 5 acertou: zapatos modernos (7, aínda que dixo
  «interior moderno»), bombilla e fiestras (18), casas inglesas (21), lentes (41) e pseudotexto (31).
- **Balance: rexeita de máis nos planos de texto e de gando, e deixa pasar de máis os anacronismos de arquitectura e
  de lume.** Nestas escollidas, o segundo pesa máis: 16 das 29 aprobadas tiñan un problema, fronte a 8 dos 13
  rexeitados que valían. Ideas para a peza IMAXE (non as probei): que «texto na imaxe» só avise cando a clave é de
  escritura (papers, page, quill, document, sheet); que «animais en grupo» só avise cando a clave é o gando; sondas
  CLIP para «crystal chandelier», «palace hall», «park bench», «drainpipe», «broom» e «bonfire»; e non aceptar sen
  revisión un intento con `reserva: true`.

## Notas para MOVEMENTO (acción I2V das imaxes aceptadas)

- **5:** o home leva o chapeu posto e é el quen escribe. Proposta: «the bearded man writes slowly with the quill and
  looks up, the candle flames flicker».
- **13:** mira á cámara. Proposta: «her lips move slightly as she murmurs» (sen «eyes stay lowered»).
- **16:** non hai cántaro: a auga escórrelle dos dedos á pía. Proposta: «water drips from her fingers into the stone
  basin, she slowly looks up into the darkness, the fire flickers».
- **19:** ten papeis na man diante da mesa. Proposta: «she slowly turns the old papers in the candlelight».
- **23:** as vacas están detrás dela. Proposta: «the wind blows her scarf and the grass as she speaks softly, the
  cows graze behind her».
- **25 ([1]):** non hai escribán. Proposta: «the bearded man speaks slowly in profile, the candle flames flicker».
- **28:** detrás hai un home, non a muller. Proposta: «the scribe writes slowly while the man behind him watches in
  silence».
- **8:** o I2V do salto é o máis fráxil (xa o dixo o crítico de planos); se deforma, paralaxe.

## Personaxes recorrentes

- **Dorotea:** no 13 leva pano claro (non marrón escuro) e no 30 [0] vai sen pano e co pelo branco. Os planos 6, 7 e
  29 rexenéranse co pano marrón escuro do elenco.
- **María:** a cor vermella mantense (23, 30 [0]); no 20 e no 21 saía de Carapuchiña e rexenéranse.
- **Escribán:** no 5 é un home con barba e chapeu; no 12 e no 28, un mozo barbeado (é a figura «quen escribía»;
  aceptable). O 12 e o 28 parécense (escribán novo con candeas), pero son o mesmo papel e están a ≈ 2 min.
- **Mariano e os amigos** (3 [1], 33, 34): camisa branca e sen o xersei escuro, coherentes entre si.

## Pendente

- Segunda pasada: planos 43-77, cando remate o proceso de imaxes (mirar primeiro 45, 46, 54, 65, 69 e 70, como pide o
  crítico de planos).
- Mirar os 17 rexenerados cando saian: nos de escritura (31) a porta volverá rexeitar por texto, e nos de semente
  (10, 21) hai que ver se a foto arrastra algo do presente.
