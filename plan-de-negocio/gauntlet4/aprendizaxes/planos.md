# Aprendizaxes da peza PLANOS (Gauntlet 4)

Axente: montador e director (Claude). Medidas propias salvo que se diga outra cousa. Ningunha imaxe xerada aínda:
todo o que se di da imaxe é previsión, non resultado.

## Lista de planos

- **As duracións por fase e o número de planos chocan.** Co guion r2 (99 s de gancho, 144 de transición, 250 de calma
  e 258 de durmir coa cola) e os obxectivos do encargo (3-6, 5-9, 8-14 e 12-20 s), o corte por sentido dá ≈ 80
  planos, non 60-75; a curva dera 78. Quedou en 77 xuntando só frases que unha imaxe cobre enteiras; para baixar de
  aí hai que aceptar planos de dúas ideas (peor correlación) ou planos máis longos ca o obxectivo.
- **Escribir a lista como datos e xerar o JSON** (`planos/scripts/xerar_lista.py`): o `texto` de cada plano sae de
  `frases.json` da voz (sen erros de copia) e o script comproba a continuidade (cada frase nun plano, os `desde`
  dentro da súa frase). Os personaxes recorrentes van nun dicionario e entran no prompt por nome: o mesmo texto en
  todos os planos sen depender da memoria do axente.
- **Gardar por tramos** (gancho e transición, despois o resto): o 03-10-2026 un corte por cota e un reinicio do
  contedor pararon esta peza antes do primeiro commit e houbo que volver empezar a escritura.

## O que a porta de imaxes vai mirar e convén planificar xa na lista

- **Topes de arquetipos** (`revisor.ARQUETIPOS`, tope = ceil(fracción × planos), separación mínima de 5 planos): con
  77 planos, mans en primeiro plano ≤ 5, retrato ≤ 7, persoa á lareira ≤ 5, grupo de pé ≤ 4, camiñantes de costas ≤ 3.
  Os primeiros planos de mans (os que máis chaman a mirada segundo a biblia) hai que racionalos e separalos.
- **"Persoa á lareira" só conta se o prompt nomea lume** (`fire|hearth|fireplace|embers|flames|firelight`): dous
  planos seguidos da queimada con "flames" poden caer por "arquetipo seguido". Nos planos de lapas azuis seguidos,
  só un nomea o lume; os outros din "blue glow" ou "burning spirits".
- **CLIP le 77 tokens**: un prompt con dous personaxes recorrentes descritos enteiros pasa de 55 palabras e o final
  pérdese. Primeiro o tipo de plano, os personaxes e a acción; a luz e a época ao final.
- **A semente manda na composición** (img2img 0,5 mantén o encadre da foto): escoller a semente polo plano que se
  quere (a dorna amarrada ao peirao de noite para "un vello barco amarrado no porto", a tarteira con cuncas para o
  primeiro plano dos ingredientes) e non forzar unha semente nun encadre distinto. Con só 29 sementes permitidas e
  ningunha de fonte nin de aldea de lousa vista de fóra, mellor encadres pechados (portas, muros, beirados).

## Corte por sentido en longo.py

- Os cortes a metade de frase (`desde`) colocanse coas marcas de tempo por palabra de Whisper sobre o wav da propia
  frase (o modelo do QA, `word_timestamps=True`), aliñadas co texto con difflib; se a palabra non aparece aliñada, a
  parte proporcional polos caracteres. Caché en `marcas_desde.json` do traballo.
- `--so-planos` só precisa as portas de texto da caché e os wav da voz: se están todos, longo.py xa non lanza
  `voz_st2.py` (antes cargaba StyleTTS2 aínda que non houbese nada que sintetizar).
