# Aprendizaxes: peza IMAXE (Gauntlet 4, rolda 1)

Director de arte (axente Claude), 02-10-2026. As medidas son automáticas; os xuízos sobre imaxes ("vese", "sae") son
de Claude mirando as imaxes, non dunha persoa. Detalle e cifras en `gauntlet4/imaxe/informe-r1.md`.

## Referencias (D15)

- **Wikimedia dá HTTP 429 aos orixinais** de `upload.wikimedia.org` ("use thumbnail images in sizes listed on
  https://w.wiki/GHai", `retry-after: 600`). As miniaturas de tamaño estándar (20, 40, 60, 120, 250, 330, 500, 960,
  1280, 1920, 3840 px) si baixan, con algún 429 solto que se arranxa reintentando aos 20 s. Non se pode pedir unha
  miniatura igual ou máis grande ca o orixinal. `scripts/urls_refs.py` fai a conversión. As 226 baixaron en ≈ 15 min
  (101 MB); as do Met, en `web-large` (≈ 70 KB) no canto do orixinal.
- **A API de Commons responde ben en lotes de 40 títulos** (`prop=imageinfo&iiprop=extmetadata`): as 226 licenzas
  comprobadas en 7 peticións; coinciden todas co CSV. O Met ten `isPublicDomain` na súa API de obxectos.
- **O 72 % das referencias son BY-SA**, e son as mellores en carro, palloza, lareira con pote e queimada. As
  permitidas como semente (CC0, dominio público, CC BY) cobren ben o hórreo (unha CC0 de Christof46), o carro (unha
  soa, de tres cuartos), a palloza (dúas), a lareira baleira, a queimada (tarteira e lapa azul) e o muíño; non hai
  ningunha de cruceiro, peto, Samos, fonte, escano nin roupa do XVII.
- Moitas fotos das referencias levan o presente dentro (cables, estradas, tubos metálicos, botellas, xente con roupa
  actual) e varias levan **persoas recoñecibles**: hai que miralas antes de usalas, como dicía `referencias.md`.

## Porta (Florence-2-base, que é a da produción)

- **Florence-2-base describe con palabras propias que delatan o anacronismo**: "lit up with warm lights" aparece en
  6 imaxes da v1 e as 6 son malas (pobo iluminado, igrexa con farolas, casa colonial, catedral, aldeas inglesas);
  "cottages", "english architectural styles", "two-story building", "framed pictures hanging on the wall", "walls
  are painted", "string lights", "beanie", "teddy bear", "briefcase".
- **E palabras que confunden**: chama "sweater" á roupa de la, "hoodie" ao capucho dun frade, "countertop" a calquera
  mesa de madeira, "sink" a unha pía de pedra, "chandelier" aos lampadarios de velas do XVII, "living room" a
  calquera fondo desenfocado. Ningunha delas pode vetar.
- **Non nomea** a bombilla nin o radiador do plano 84 nin as rodas da maleta do 56: iso só o pode ver CLIP (ou
  ninguén).
- A roupa e os obxectos do XX dependen da época do plano (a taberna dos anos 50 da v1 caía por un "glass jar"): campo
  `epoca` novo.

## Sementes (7 escenas x 4 técnicas, `imaxe/ab-sementes.jpg`)

- **A semente arranxa a forma** que SDXL-Lightning non sabe (roda maciza, hórreo, palloza, lareira ao nivel do chan):
  o texto só non deu ningún hórreo nin ningunha roda maciza. Pero a forza depende do que se pide: 0,5 conserva o
  obxecto, 0,75 deixa meter xente nun espazo, a profundidade (ControlNet small a 0,6) recompón e ás veces inventa
  (unha cara na campá, rodas de raios).
- **A semente arrastra o presente da foto** (tubo de cheminea, vila moderna no val, mesa de restaurante): recortala.
  O encadre dunha semente vertical con bandas desenfocadas fallou (o modelo pinta as bandas).
- **Non encarece:** img2img 0,5 fai 2 dos 4 pasos e sae ≈ 20 % máis barato ca o texto só.

## Tempos nesta CPU sen bf16 (`calibracion/perfil-tempos.json`)

- 1024x576: UNet 4 pasos 48 s, VAE 22 s, texto 1,4 s. 1344x768: 74,5 + 39 + 1,3 s. O VAE é un terzo do tempo.
- Despois do reinicio do 03-10 a máquina foi ≈ 20 % máis rápida (mesmo modelo de CPU): os tempos varían por máquina.
- Tras un reinicio, a primeira carga tarda ≈ 10 min (disco frío, presión de E/S ≈ 89 %), como no Gauntlet 3.

## Porta e medida

- Florence-2 `<OPEN_VOCABULARY_DETECTION>` atopa sempre o que se lle pregunta (33 de 33 imaxes con "light bulb"): non
  serve para detectar obxectos pequenos. Os pares de CLIP para obxectos pequenos tampouco (AUC 0,6-0,9 con moitos
  falsos).
- A `clave` por z fronte a 73 distractores non dá falsas alarmas na v1 (0/144) pero non distingue un hórreo dunha
  cabana: para a iconografía, a garantía é a semente e a mirada dun axente.
- CLIP-L fronte á tradución inglesa do texto separa ben os planos que ilustran dos desconectados (AUC 0,90 na v1) e
  premia a coincidencia literal (calquera muller "casa" cunha frase sobre mulleres).

## Entorno

- Un candado aniñado (un `flock` por fóra dun script que colle o mesmo candado por dentro) bloqueou a CPU 30 min:
  `/proc/locks` amosa quen o ten e quen agarda. Agora `herramientas/gauntlet/candado.sh`.
- Commons dá 429 aos orixinais: miniaturas de tamaño estándar.
