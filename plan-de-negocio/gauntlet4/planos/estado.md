# Peza PLANOS (Gauntlet 4, rolda 1): estado

Montador e director: axente Claude. Actualízase en cada fito. **Se a sesión se corta, retomar desde aquí.**

Última actualización: 03-10-2026, 09:40 UTC. **Rolda 1 entregada; á espera do crítico.**

## Feito

- **Lista de planos v2** en `escenas-v2.json`: 77 planos cortados por sentido para as 108 frases do guion r2
  (gancho 19, transición 19, calma 24, durmir 15), con `texto_en`, `prioridade_i2v`, sementes, animación, son,
  `epoca` e personaxes descritos sempre igual. Xerada con `scripts/xerar_lista.py` desde `scripts/tramo1.py` e
  `scripts/tramo2.py` (o texto que se oe sae de `frases.json` da voz).
- **Corte por sentido en `herramientas/pipeline/longo.py`** (`frases`/`desde`, Whisper por palabras, comprobacións,
  `ler_escenas` con `referencia`, `epoca`, `texto_en`, `prioridade_i2v`, `--so-planos`, voz da caché sen cargar o
  modelo). Probado con `scripts/so_planos.sh` sobre `$SCRATCH/v2/w`: rc 0, 77 planos, os 2 `desde` por Whisper.
- Decisións e medidas en `notas-r1.md` e `medidas-r1.json` (`scripts/medir_lista.py`); aprendizaxes en
  `../aprendizaxes/planos.md`.

## Falta (despois do crítico)

- Veredicto do crítico (correlación e atractivo de cada parella texto-prompt) e, se perde, rolda 2.
- Imaxes (porta v6) e movemento coa lista; MOVEMENTO decide que I2V de prioridade 2 entran no orzamento.

## Como retomar

    export SCRATCH=/tmp/claude-0/-home-user-revolta/c92eba35-e89d-5d11-bb3d-f517a84dab48/scratchpad
    python3 plan-de-negocio/gauntlet4/planos/scripts/xerar_lista.py        # rexera escenas-v2.json dos tramos
    bash plan-de-negocio/gauntlet4/planos/scripts/so_planos.sh              # valida o corte (candado prioritario)
    python3 plan-de-negocio/gauntlet4/planos/scripts/medir_lista.py > plan-de-negocio/gauntlet4/planos/medidas-r1.json
