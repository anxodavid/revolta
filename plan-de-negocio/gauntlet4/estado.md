# Estado do Gauntlet 4 e como relanzalo

Ficheiro do orquestrador (Claude). Actualízase en cada cambio de fase. **Se a sesión se corta, retomar desde aquí.**
Última actualización: 03-10-2026, 09:55 UTC. **D18: a v2 dura ≈ 12 min e a calidade manda** (contexto §8).

## Que hai en marcha

| Peza | Estado | Axente | Onde deixa o traballo | Encargo para relanzar |
|---|---|---|---|---|
| 0 Contorno | Instalado (6 min); verificación en curso | operador | `$SCRATCH/logs/instalar-*.log`, `verificar.log` | `bash herramientas/pipeline/instalar.sh` e `… verificar` |
| 1 Guion v2 | **PECHADA: GAÑOU.** r1: A a cegas elixe a v2 (31/35 fronte a 18); B gaña con 15 substitucións. r2 (B + melloras de A): B r2 gaña sen substitucións. **Texto final: `guion/guion-r2.txt`** (1.628 palabras, ≈ 12 min; portas en verde; 5 excepcións aceptadas en `excepcions-r2.yaml`) | — | `gauntlet4/guion/`, `veredictos/guion-r*.md` | — |
| 2 Movemento | Rolda 1: medindo I2V (LTX-Video 2B destilado, T5 en fp8) | enxeñeiro VFX | `gauntlet4/movemento/` e `herramientas/pipeline/movemento.py` | `encargos/construtor-movemento-r1.md` |
| 3 Imaxe | **Rolda 1 pechada** (fd68860, `imaxe/informe-r1.md`): 29 sementes permitidas; as sementes arranxan a forma en 5 de 7 escenas; a biblia v2 ilustra o que se oe en 6-8 de 10 (antes 1-2; z 0,55 → 1,52); porta v6 (VERSION 9): 25/29 molestas e 2/4 bloqueantes, sen ver bombilla, radiador nin maleta. Configuración para a produción no §6 (≈ 3,4 h, 3 intentos, revisión dun axente de cada imaxe). **Sen crítico visual propio para aforrar cota: as imaxes xúlgaas o tribunal final no vídeo** | — | `gauntlet4/imaxe/` | — |
| 4 Planos v2 | **Rolda 1 entregada** (7df0834): `planos/escenas-v2.json`, 77 planos por sentido (19/19/24/15 por fase); 71 % da parte esperta con persoas facendo algo; 57 I2V (27 prioridade 1) e 20 paralaxe; 4 sementes. `longo.py` corta pola lista (`frases`, `desde` con Whisper) e ten `--so-planos` (proba rc 0). **Crítico (espectador esixente) traballando** | crítico | `gauntlet4/planos/`, `veredictos/planos-r1.md` | `encargos/construtor-planos-r1.md`, `encargos/critico-planos-r1.md` |
| 5 Vídeo v2 | Pendente | — | `gauntlet4/video/` | (por escribir) |

Críticos do guion: `encargos/critico-guion-A-cego.md` (a cegas: o orquestrador copia a v1, que é
`gauntlet3/guion/guion-r3.txt`, e a v2 a `$SCRATCH/cego/guion-rN/A.txt` e `B.txt` ao chou, coa clave en
`clave.txt`) e `encargos/critico-guion-B-lingua-veracidade.md`.

## Cortes

- **02-10-2026 ≈ 23:30 UTC: límite de uso da sesión** (os tres construtores e o orquestrador; volveu a cota ás 03:10)
  e **reinicio do contedor** (03:53). Morreron a porta de texto do guion r1 e os lotes de paralaxe e I2V de
  MOVEMENTO; o feito estaba en git (últimos commits d86e250, f5eddf7 e bf5f0d4). Ás 03:55 retomáronse os tres axentes
  co seu contexto (SendMessage) e relanzouse a instantánea.
- **03-10-2026 ≈ 06:30 UTC: segundo límite de uso** (planos, movemento e imaxe en paralelo, ≈ 2,5 h despois do
  anterior; volveu a cota ás 08:50) e **reinicio do contedor** (08:53). Retomáronse os tres co seu contexto ás 08:55,
  con tarefas acoutadas: PLANOS (camiño crítico) garda a lista por tramos; MOVEMENTO pecha con 2-3 clips I2V máis, a
  integración en `montaxe.py` e o informe; IMAXE pecha o informe sen experimentos novos.

## Procesos de fondo desta sesión

- **Instantánea do scratchpad e autogardado** cada 20 min: `herramientas/gauntlet/instantanea.py --bucle 1200
  --autogardar` (log en `$SCRATCH/logs/instantanea.log`). Copia a `gauntlet4/scratchpad/` os ficheiros de texto
  pequenos que deixan os axentes no scratchpad (scripts, notas, medidas, rexistros recortados) e, ademais, fai commit
  do traballo en curso de `gauntlet4/` e `herramientas/` (texto e imaxes pequenas quedos ≥ 2 min; vídeo e audio non,
  que os validan os axentes). Se o contedor se reinicia, relanzala:
  `SCRATCH=… setsid nohup python3 herramientas/gauntlet/instantanea.py --bucle 1200 --autogardar >> $SCRATCH/logs/instantanea.log 2>&1 &`
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
- Curva do embude para 12 min: feito (commit 562ed3c, `curva_capitulos` na ficha; a v1 queda igual). Para o dossier, dous feitos do PDF que aínda non están (a excomuñón prohibía tamén falar
  con elas; Inés da Maquieira responde en galego): non se usaron.
- Pendente do promotor: GPU alugada para o movemento (requiriría unha clave e unha sesión nova) e sementes CC BY-SA.

## Mensaxe da rolda 2 do guion (03-10-2026, 05:08 UTC; para relanzala)

Aplicar exacta a lista pechada do §7 de `veredictos/guion-r1-lingua-veracidade.md`; aplicar as melloras do crítico A
sen feitos novos (polo menos: Sarmiento fundido co argumento de que eran necesarias e a viraxe nun parágrafo propio; a
tese do gancho "só as coñecemos"; fóra "podemos pensar" e "cómpre pensala"; un só nome para cada xustiza); ≈ 1.600
palabras; `curva_capitulos` na ficha v2; gardar `guion-r2.txt`, `feitos-r2.md`, `excepcions-r2.yaml`, `notas-r2.md`
(táboa B1-B15 e A1-A10) e `porta_texto-r2.json` (portas con `candado.sh --prioridade`).

