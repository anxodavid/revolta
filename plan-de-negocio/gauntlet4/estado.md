# Estado do Gauntlet 4 e como relanzalo

Ficheiro do orquestrador (Claude). Actualízase en cada cambio de fase. **Se a sesión se corta, retomar desde aquí.**
Última actualización: 02-10-2026, 23:06 UTC. **D18: a v2 dura ≈ 12 min e a calidade manda** (contexto §8).

## Que hai en marcha

| Peza | Estado | Axente | Onde deixa o traballo | Encargo para relanzar |
|---|---|---|---|---|
| 0 Contorno | Instalado (6 min); verificación en curso | operador | `$SCRATCH/logs/instalar-*.log`, `verificar.log` | `bash herramientas/pipeline/instalar.sh` e `… verificar` |
| 1 Guion v2 | Rolda 1: construtor traballando | guionista | `gauntlet4/guion/` (+ `estado.md` da peza) | `encargos/construtor-guion-r1.md` |
| 2 Movemento | Rolda 1: medindo I2V (LTX-Video 2B destilado, T5 en fp8) | enxeñeiro VFX | `gauntlet4/movemento/` e `herramientas/pipeline/movemento.py` | `encargos/construtor-movemento-r1.md` |
| 3 Imaxe | Rolda 1: referencias baixadas; porta v6 e sementes | director de arte | `gauntlet4/imaxe/` | `encargos/construtor-imaxe-r1.md` |
| 4 Planos v2 | Pendente (precisa o guion gañador e a voz) | — | `gauntlet4/planos/` | (por escribir) |
| 5 Vídeo v2 | Pendente | — | `gauntlet4/video/` | (por escribir) |

Críticos do guion: `encargos/critico-guion-A-cego.md` (a cegas: o orquestrador copia a v1, que é
`gauntlet3/guion/guion-r3.txt`, e a v2 a `$SCRATCH/cego/guion-rN/A.txt` e `B.txt` ao chou, coa clave en
`clave.txt`) e `encargos/critico-guion-B-lingua-veracidade.md`.

## Procesos de fondo desta sesión

- **Instantánea do scratchpad** cada 20 min: `herramientas/gauntlet/instantanea.py --bucle 1200` (log en
  `$SCRATCH/logs/instantanea.log`). Copia a `gauntlet4/scratchpad/` os ficheiros de texto pequenos que deixan os
  axentes (scripts, notas, medidas, rexistros recortados) e fai commit só desa carpeta. Se o contedor se reinicia,
  relanzala:
  `SCRATCH=… setsid nohup python3 herramientas/gauntlet/instantanea.py --bucle 1200 > $SCRATCH/logs/instantanea.log 2>&1 &`
- **Revisión horaria e rearranque** (rutina `trig_01CHFESbR8j5JWtTkAhQsCDN`, ao minuto 53 de cada hora, nesta mesma
  sesión): mira `uptime`, os axentes, o disco e a instantánea, e retoma o que parase por cota ou por reinicio. Bórrase
  cando se entregue a v2.

## Como relanzar nunha sesión nova

1. `bash herramientas/pipeline/instalar.sh` e `source herramientas/pipeline/entorno.sh` (≈ 6 min, ≈ 16 GB). O
   contorno de vídeo (venv aparte e modelos de I2V) reconstrúese segundo `gauntlet4/movemento/estado.md`.
2. Ler este ficheiro, `contexto.md` e o `estado.md` de cada peza; mirar `git log` da rama e `gauntlet4/scratchpad/`
   (scripts e medidas dos axentes que non chegaran a pasar ao seu sitio).
3. Relanzar cada peza sen rematar co seu encargo de `encargos/`, engadindo "retoma desde o estado do repo". Non
   confiar en `resumeFromRunId` (CLAUDE.md).

## Decisións e datos para lembrar

- Disco: ≈ 39 GB por sesión; o contorno colle ≈ 16 GB e LTX-Video + T5 fp8 ≈ 11 GB. A produción precisa ≈ 8 GB libres.
- PR #5 (rolda de arranxos da v1) fusionado en main e na rama (c4fcc72): a v1 de referencia é a arranxada.
- PR #4 (prospección de temas) sen fusionar: non é necesario para a v2; queda para o promotor.
- D18 (23:05 UTC): v2 de ≈ 12 min (≈ 1.500-1.700 palabras, ≈ 60-75 planos), calidade por riba de cobertura e custo.
- Pendente do promotor: GPU alugada para o movemento (requiriría unha clave e unha sesión nova) e sementes CC BY-SA.
