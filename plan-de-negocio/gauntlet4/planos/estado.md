# Peza PLANOS (Gauntlet 4, rolda 1): estado

Montador e director: axente Claude. Actualízase en cada fito. **Se a sesión se corta, retomar desde aquí.**

Última actualización: 03-10-2026, 09:20 UTC.

## Feito

- Lido o encargo (`../encargos/construtor-planos-r1.md`), o guion pechado (`guion/guion-r2.txt`), os tempos da voz
  (`$SCRATCH/v2/w/`), a biblia v2 e o informe de IMAXE, o informe e o estado de MOVEMENTO (en curso) e `movemento.py`.
- Plan de corte por sentido: **77 planos** (gancho 19, transición 19, calma 24, durmir 15), con 2 cortes a metade de
  frase (`desde`, frases 4 e 6). Sementes en hórreo, lareira, cunca da queimada e dorna.
- **Tramo 1 da lista** (planos 1-38, frases 1-44: gancho e transición) en `escenas-v2.json`, xerado con
  `scripts/xerar_lista.py` desde `scripts/tramo1.py` (o texto que se oe sae de `frases.json` da voz).

## Falta

1. Tramo 2 (planos 39-77: calma e durmir) en `scripts/tramo2.py`.
2. Corte por sentido en `herramientas/pipeline/longo.py` (`frases`/`desde`, `ler_escenas` con `referencia`,
   `animacion`, `texto_en`, `prioridade_i2v`, `epoca`; `--so-planos`) e proba sobre `$SCRATCH/v2/w`.
3. `notas-r1.md` (decisións e medidas) e `../aprendizaxes/planos.md`.

## Como retomar

    export SCRATCH=/tmp/claude-0/-home-user-revolta/c92eba35-e89d-5d11-bb3d-f517a84dab48/scratchpad
    python3 plan-de-negocio/gauntlet4/planos/scripts/xerar_lista.py   # rexera escenas-v2.json dos tramos
