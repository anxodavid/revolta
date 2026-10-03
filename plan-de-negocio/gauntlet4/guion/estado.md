# Estado da peza 1 (guion v2) · Gauntlet 4

Ficheiro do construtor (guionista, axente Claude). Actualízase en cada fito. **Se a sesión se corta, retomar desde
aquí.** Última actualización: 03-10-2026, 05:25 UTC.

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
| Este ficheiro | `gauntlet4/guion/estado.md` | 9f956b8 |
| Plan para 12 min | `gauntlet4/guion/plan-r1.md` | 9f956b8 |
| Ficha v2 (mesmo dossier + F052) | `herramientas/pipeline/temas/meigas-de-verdade-v2.yaml` | ccebb9e e seguintes |
| Borrador do guion (1.602 palabras, ≈ 11:40-12:45) | `gauntlet4/guion/guion-r1.txt` | ccebb9e e seguintes |
| Scripts: medidas e lingua rápida | `gauntlet4/guion/scripts/` | ccebb9e e seguintes |
| Comprobación na fonte primaria (PDF do Arquivo, p. 4-7 e 15) dos pasaxes de Vilalba, Cibreira e Campo Lameiro | `$SCRATCH/fontes/ARG-PDF.txt` (non se sobe: dereitos) | — |

## En curso

- Nada: **rolda 2 entregada** (05:25 UTC): `guion-r2.txt` (1.628 palabras), `feitos-r2.md`, `excepcions-r2.yaml`,
  `notas-r2.md` (táboa B1-B15 e A1-A10) e `porta_texto-r2.json` (todo en verde). A r1 gañou (crítico A a cegas: 31
  fronte a 18; crítico B: GAÑA coas 15 substitucións, aplicadas literais por `scripts/aplicar_r2.py`). Agarda un novo
  crítico B que revise só as frases cambiadas.

## Falta

- Se o novo crítico B pide cambios: aplicalos a `guion-r2.txt` e volver pasar `scripts/porta-r2.sh` (mesmas ordes, r2).

## Como retomar (ordes exactas)

    export SCRATCH=/tmp/claude-0/-home-user-revolta/c92eba35-e89d-5d11-bb3d-f517a84dab48/scratchpad
    source /home/user/revolta/herramientas/pipeline/entorno.sh
    cd /home/user/revolta/herramientas/pipeline
    # copia conxelada do guion para non editar o que está a pasar a porta
    cp ../../plan-de-negocio/gauntlet4/guion/guion-r1.txt $SCRATCH/guion/guion-r1-conxelado.txt
    ../gauntlet/candado.sh --prioridade "$PY" longo.py temas/meigas-de-verdade-v2.yaml \
      --guion $SCRATCH/guion/guion-r1-conxelado.txt --traballo $SCRATCH/guion/w-r1 --saida $SCRATCH/guion/s-r1 \
      --so-texto --excepcions ../../plan-de-negocio/gauntlet4/guion/excepcions-r1.yaml
    # ou, desacoplado: setsid nohup bash ../../plan-de-negocio/gauntlet4/guion/scripts/porta-r1.sh > $SCRATCH/guion/porta-r1.log 2>&1 &
    cp $SCRATCH/guion/w-r1/porta_texto.json ../../plan-de-negocio/gauntlet4/guion/porta_texto-r1.json

Entradas: `gauntlet3/dossier/feitos.yaml` e `dossier.md` (só se pode afirmar o que está aí), a ficha v2 e a v1
(`gauntlet3/guion/guion-r3.txt`). Saídas: os ficheiros de `gauntlet4/guion/` listados arriba.
