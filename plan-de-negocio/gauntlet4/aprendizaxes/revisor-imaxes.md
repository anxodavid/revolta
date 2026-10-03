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
