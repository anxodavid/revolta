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
