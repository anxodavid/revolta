# Estado da peza 1 (guion v2) · Gauntlet 4

Ficheiro do construtor (guionista, axente Claude). Actualízase en cada fito. **Se a sesión se corta, retomar desde
aquí.** Última actualización: 02-10-2026, 23:40 UTC.

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

- Porta de texto completa (`scripts/porta-r1.sh`, longo.py --so-texto) lanzada ás 23:33 UTC con
  `herramientas/gauntlet/candado.sh --prioridade`, sobre `$SCRATCH/guion/guion-r1-conxelado.txt`; rexistro en
  `$SCRATCH/guion/porta-r1.log`. Ao rematar: copiar `$SCRATCH/guion/w-r1/porta_texto.json` a `porta_texto-r1.json`,
  escribir `excepcions-r1.yaml` coas frases marcadas e volver pasala.
- Feitos: `feitos-r1.md` (mapa por frase) e `notas-r1.md` (borrador; falta a sección 4, portas).

## Falta (orde)

1. ~~`plan-r1.md`~~ feito.
2. ~~Ficha `herramientas/pipeline/temas/meigas-de-verdade-v2.yaml` (copia da v1 + autoría G4, `capitulo_inicial`,
   `palabras: 1600`, `duracion_s: [600, 840]`, feitos `ficha: false` que use o guion, co seu ID)~~ feito.
3. ~~`guion-r1.txt`~~ borrador feito; pendente das portas.
4. ~~Scripts de medida en `gauntlet4/guion/scripts/` (palabras por fase, atribucións, "segundo", nomes novos)~~ feito.
5. Portas: `qa.lingua` rápido e despois `longo.py --so-texto` (ordes abaixo) → `porta_texto-r1.json`,
   `excepcions-r1.yaml`.
6. `feitos-r1.md`, `notas-r1.md`, `gauntlet4/aprendizaxes/guion.md` → commit.

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
