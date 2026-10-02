# Estado da peza 1 (guion v2) · Gauntlet 4

Ficheiro do construtor (guionista, axente Claude). Actualízase en cada fito. **Se a sesión se corta, retomar desde
aquí.** Última actualización: 02-10-2026, 23:20 UTC.

## Encargo vixente

- Encargo literal: `plan-de-negocio/gauntlet4/encargos/construtor-guion-r1.md`.
- **D18 (02-10-2026, 23:05 UTC), prioritaria sobre o encargo:** a v2 dura ≈ 12 min, ≈ 1.500-1.700 palabras, 3-5
  capítulos; calidade por riba de cobertura; embude comprimido (gancho ≈ 0-1:30, transición ata ≈ 5:00, calma ata
  ≈ 8:30, peche de durmir ata o final). Na ficha v2: `palabras: 1600`, `duracion_s: [600, 840]`.
- Ficha da v1 actualizada en c4fcc72 (créditos con `{imaxes}` e `{ambientes}`): a ficha v2 cópiaos.

## Feito

| Fito | Onde | Commit |
|---|---|---|
| Lecturas (CLAUDE.md, contextos G4 e G3 §2 e §8, v1, veredictos, dossier, ficha, portas) | — | — |
| Este ficheiro | `gauntlet4/guion/estado.md` | (este) |

## En curso

- `plan-r1.md` para 12 min (pregunta, fío, arquitectura, embude, persoas, momento visible por parágrafo).

## Falta (orde)

1. `plan-r1.md` → commit.
2. Ficha `herramientas/pipeline/temas/meigas-de-verdade-v2.yaml` (copia da v1 + autoría G4, `capitulo_inicial`,
   `palabras: 1600`, `duracion_s: [600, 840]`, feitos `ficha: false` que use o guion, co seu ID).
3. `guion-r1.txt` → commit.
4. Scripts de medida en `gauntlet4/guion/scripts/` (palabras por fase, atribucións, "segundo", nomes novos).
5. Portas: `qa.lingua` rápido e despois `longo.py --so-texto` (ordes abaixo) → `porta_texto-r1.json`,
   `excepcions-r1.yaml`.
6. `feitos-r1.md`, `notas-r1.md`, `gauntlet4/aprendizaxes/guion.md` → commit.

## Como retomar (ordes exactas)

    export SCRATCH=/tmp/claude-0/-home-user-revolta/c92eba35-e89d-5d11-bb3d-f517a84dab48/scratchpad
    source /home/user/revolta/herramientas/pipeline/entorno.sh
    cd /home/user/revolta/herramientas/pipeline
    # copia conxelada do guion para non editar o que está a pasar a porta
    cp ../../plan-de-negocio/gauntlet4/guion/guion-r1.txt $SCRATCH/guion/guion-r1-conxelado.txt
    flock "$CPU_LOCK" "$PY" longo.py temas/meigas-de-verdade-v2.yaml --guion $SCRATCH/guion/guion-r1-conxelado.txt \
      --traballo $SCRATCH/guion/w-r1 --saida $SCRATCH/guion/s-r1 --so-texto \
      --excepcions ../../plan-de-negocio/gauntlet4/guion/excepcions-r1.yaml
    cp $SCRATCH/guion/w-r1/porta_texto.json ../../plan-de-negocio/gauntlet4/guion/porta_texto-r1.json

Entradas: `gauntlet3/dossier/feitos.yaml` e `dossier.md` (só se pode afirmar o que está aí), a ficha v2 e a v1
(`gauntlet3/guion/guion-r3.txt`). Saídas: os ficheiros de `gauntlet4/guion/` listados arriba.
