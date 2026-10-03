# MOVEMENTO, rolda 1: que movemento é posible en CPU e a que custo

Construtor: enxeñeiro de VFX (axente Claude), 02-03/10-2026. Medidas en `probas/medidas-*.json`. Todo o que se di da
calidade sae de mirar tiras de fotogramas (JPEG): **ningún axente viu os clips en movemento**.

## 1. Resumo

- **Ningún plano fixo é posible en CPU** con tres modos por plano (campo `animacion` da lista de planos, §6.1 do
  contexto), xa integrados en `montaxe.py` e `longo.py`; os planos sen `animacion` saen exactamente coma na v1
  (fotogramas idénticos, diferenza 0).
- **I2V (xente que se move): LTX-Video 2B 0.9.8 destilado**, 800x448 a 24 fps, 8 pasos: **470 s por clip de 2-3 s
  e 660 s por clip de 4 s**, 11 GB de memoria. Nas tiras dos 6 clips de proba o movemento é natural: unha muller que
  camiña de verdade, dúas siluetas que saen por unha porta, mans que remexen e amasan, un rostro que xira a cabeza;
  sen deformacións graves á vista. A 1080p o clip é máis brando ca a imaxe fixa: a transferencia de detalle desde a
  imaxe orixinal (guiada polo fluxo óptico) recupera boa parte.
- **Paralaxe 2,5D** (profundidade de Depth-Anything-V2-Small, z-buffer e recheo do fondo destapado) con 8 cámaras e
  **8 microanimacións** (lume, candea, choiva, brétema, fume, auga, ceo, po): 0,3-0,4 s por fotograma a 1080p.
- **Orzamento dun episodio de 12 min (≈ 65 planos)**: ≈ 40 clips I2V + 25 planos en paralaxe ≈ **9 h de CPU**:
  cabe nunha noite (§8). Con GPU alugada, **≈ 4,5-10 $ por episodio** (Wan 2.2 I2V en Replicate) e calidade doutra
  liga; precisa clave de API e decisión do promotor (§10).
- **Demo**: `demo-gancho.mp4` (o gancho da v1, 1:55, mesmas imaxes e audio, I2V nos planos 14 e 22 e paralaxe con
  efectos nos outros 20) e `demo-durmir.mp4` (60 s da zona de durmir, sen son).
- **Límites honestos**: só tiras, ninguén o viu en movemento; a porta de vídeo rexeitou tres clips bos e hai que
  recalibrala con máis clips (§7); Wan2.2-TI2V-5B non se probou por disco (§3).

## 2. Máquina e método

- CPU Intel Xeon 2,8 GHz, 4 núcleos, AVX-512 **sen bf16 nin AMX** (`/proc/cpuinfo`), 13,36 GiB de memoria para
  todos os procesos (cgroup v1: `memory.limit_in_bytes` = 14.345.035.776). Cada medida co candado común de CPU.
- Memoria: pico do proceso (`VmHWM`, inclúe as páxinas do ficheiro de pesos mapeadas) e pico da memoria anónima de
  todo o cgroup (`total_rss` de `memory.stat`, mostraxe cada 0,5 s).

## 3. Imaxe a vídeo (I2V)

**Modelo escollido: LTX-Video 2B 0.9.8 destilado** (Lightricks), transformer e VAE con pesos en bf16 e cálculo en
fp32 capa a capa (o truco de `imaxes.bf16_rapido`), 8 pasos da táboa do propio modelo, sen CFG, condicionado na
imaxe da v1 xa graduada; T5-XXL noutro proceso (fp8, cálculo fp32). Todo a 800x448 (16:9, múltiplo de 32) e 24 fps.
Código: `herramientas/pipeline/movemento_i2v.py`; probas: `scripts/ltx_proba.py`, `scripts/lote_r*.sh`.

| Plano da v1 (o que pide) | Fotog. (s) | s por clip | s por paso (1.º) | descodificar | pico proceso / cgroup | Calidade na tira (a ollo, axente Claude) | Porta |
|---|---|---|---|---|---|---|---|
| 22 muller de costas nun camiño (JPEG sen graduar) | 49 (2,0) | **470** | 42 (71) | 103 s | 11,4 / 9,0 GB | **camiña de verdade**: pés que alternan, saia que abanea, a cámara acompaña; sen deformacións (`probas/ltx_p22_*`) | OK |
| 3 home que remexe unha cunca (mans) | 73 (3,0) | 872 (*) | 41,5 (390 *) | 192 s | 10,0 / 10,2 GB | move a man en círculos co pau mentres mira a cunca; cara estable; natural | ver §7 |
| 18 mans amasando (primeiro plano) | 81 (3,4) | **520** | 47 (70) | 119 s | 11,9 / 10,4 GB | as mans empuxan e dobran a masa; o brazo do fondo medra e encolle (escorzo) e o último fotograma ten algo de arrastre; sen dedos de máis á vista | ver §7 |
| 14 rostro dunha muller que vixía | 97 (4,0) | 938 (*) | 64 (342 *) | 143 s | 13,5 / 11,0 GB | **xira a cabeza e os ollos cara á dereita**; a mesma cara do principio á fin; o pano cambia algo de forma | OK |
| 22 (imaxe graduada) | 97 (4,0) | **658** | 62,5 (73) | 144 s | 13,5 / 11,0 GB | camiña (visto na demo, 1:52) | OK |
| 17 garda e muller que saen por unha porta (siluetas) | 73 (3,0) | **470** | 42,7 (54) | 115 s | 13,5 / 11,0 GB | **as dúas siluetas camiñan** cara á luz, pernas alternas, sombras que as seguen | ver §7 |

(*) primeiro clip despois dun reinicio do contedor: o primeiro paso le os 6,3 GB de pesos do disco en frío (+ ≈ 300 s).

- **Custo en quente**: ≈ 8 pasos x (42 s a 49-73 fotogramas, 47 s a 81, 62 s a 97) + descodificar 105-145 s + 30
  s: **470 s (2-3 s de clip) a 660 s (4 s de clip)**. ≈ 11-12 ms por token latente e paso.
- **Memoria**: 97 fotogramas a 800x448 é o máximo prudente (11,0 GB de memoria anónima en todo o cgroup, de 13,36).
  Un lote morreu ("Killed") ao empezar o segundo clip o 03-10 ás 05:08; o reinicio levou o `dmesg`, así que non se
  pode confirmar que fose o OOM [S].
- **Calidade**: nos 6 clips mirados, movemento natural e sen deformacións graves á escala das tiras (8 fotogramas
  por clip, 480 px de ancho). Iso **non** é ver o vídeo: o parpadeo fino, as mans de preto e a textura da pel a
  1080p só os ve quen o mire en movemento. A 800x448 escalado a 1080p o clip é máis brando ca a imaxe fixa; a
  transferencia de detalle (§6) recupera boa parte (fotogramas da demo ás 1:03 e 1:08).
- **Wan2.2-TI2V-5B / FastWan (3 pasos) non se probou**: o transformer son 10 GB en bf16, o VAE 2,8 GB en fp32 e o
  umT5 11,4 GB; nin convertendo ao vol a fp8 (≈ 12 GB entre os tres) cabe xunto a LTX no orzamento de ≈ 13 GB de
  disco da peza, co disco ao 96 % e a produción pedindo ≈ 8 GB libres. Estimación [S]: 2,5 veces os parámetros de
  LTX 2B e o dobre de tokens (VAE 16x16x4) dan ≈ 5 veces máis cálculo por paso; con 3 pasos en vez de 8, ≈ 2 veces o
  custo de LTX por clip (≈ 15-20 min) e a 704x1280 nativos, horas. SVD-XT 1.1 (opcional) tampouco: o repo pide
  aceptar a licenza con conta (non hai token) e é Stability Community License.

## 4. Paralaxe 2,5D

**Que fai** (`movemento.Paralaxe`): unha cámara virtual que se despraza diante da imaxe co relevo dun mapa de
profundidade, non un zoom 2D.

1. Profundidade relativa con Depth-Anything-V2-Small a 756 px de lado curto (adestrado a 518; con máis resolución
   saen bordos máis finos), normalizada (percentís 1 e 99,5) e pasada a profundidade co primeiro termo en 1 e o fondo
   en `ZFAR` = 5 (canto relevo hai). Caché por sha256 da imaxe.
2. Cada fotograma: proxección dos puntos da imaxe (a media resolución) coa cámara nova, de lonxe a preto, para que
   o máis próximo quede enriba (z-buffer); os ocos que destapa a cámara énchense coa profundidade máis lonxana da
   veciñanza (o fondo continúa por detrás do primeiro termo).
3. Inversa analítica para cada píxel de saída, `x = ((x' − sx)(Z − tz) + tx) / Z`, e `cv2.remap` da imaxe a
   resolución completa (a imaxe prepárase a 1,1 veces a saída con Lanczos e a mesma máscara de desenfoque ca na
   v1).
4. Onde a cámara destapa fondo que estaba tapado, mostréase unha copia da imaxe co primeiro termo "borrado" nunha
   banda á beira de cada salto de profundidade (inpaint de Telea a media resolución) en vez de estirar o borde.
5. Zoom mínimo calculado para que ningún bordo da saída mostree fóra da imaxe en ningún momento (coas
   profundidades que hai de verdade en cada bordo).

**Cámaras** (contexto §6.1): `avanza`/`recua` (travelling cara a dentro ou fóra: o primeiro termo medra máis ca o
fondo), `pan_esq`/`pan_der` (travelling lateral), `sobe`/`baixa` (grúa), `xira_esq`/`xira_der` (arco arredor do
suxeito: o punto de xiro, á profundidade do centro da imaxe, queda quieto e fondo e primeiro termo móvense en
sentidos contrarios). Velocidade dun travelling lento: no plano de 8 s, o primeiro termo percorre ≈ 4 % do ancho
(lateral) ou medra ≈ 9 % (avance); o fondo, un cuarto diso. `forza` escala todo.

## 5. Microanimacións

Sutís: mellor pouco que de videoxogo. Todas teñen custo cero onde non atopan nada (a máscara baleira desactívaas).

| Efecto | Máscara | Animación |
|---|---|---|
| `lume` | píxeles brillantes e quentes (R > G > B, luminancia > 0,42) × CLIPSeg "fire"/"flames"; cada compoñente conexa é unha chama | desprazamento con ruído que sobe sobre cada chama e a súa estela (linguas de lume); intensidade da chama con parpadeo 1/f (0,4-11 Hz, fases distintas por chama); **a luz do contorno tremela** (±7 %, ton quente) co mapa da chama desenfocada a gran escala |
| `candea` | igual, chamas pequenas, CLIPSeg "candle flame" | o mesmo máis suave e rápido, e a chama abanea (0,55 e 1,37 Hz); luz do contorno ±4,5 % nun raio menor |
| `choiva` | ningunha (en pantalla) | tres capas de raias (lonxe, medio, preto) a 650, 1.150 e 1.850 px/s, con antialias e algo de desenfoque nas próximas; máis visibles sobre fondos escuros |
| `bretema` | profundidade (máis densa ao lonxe) | dúas capas de ruído suave que corren a 9 e 4 px/s; cor tirada das luces lonxanas da propia imaxe; opacidade ≤ 20 % |
| `fume` | CLIPSeg "smoke"/"mist" × zonas máis claras ca o arredor | desprazamento que sobe amodo |
| `auga` | CLIPSeg "water"/"river"/"water surface" | ondas horizontais (desprazamento de ≈ 2 px) e reflexos que escintilan nos brillos |
| `ceo` | CLIPSeg "sky"/"clouds" × fondo (profundidade) | as nubes desprázanse ≈ 1,2 % do ancho por segundo |
| `po` | ningunha (en pantalla) | 90 partículas mínimas que flotan amodo, visibles só onde hai luz |

Os efectos `lume`, `candea`, `bretema`, `fume`, `auga` e `ceo` aplícanse á imaxe antes da cámara 2,5D (móvense
co relevo); `choiva` e `po`, ao fotograma.

## 6. Cámara lenta e escala

Os clips I2V duran 2-4 s e os planos 3-20 s. Como se enche un plano (`movemento.Clip`):

1. **Cámara lenta interpolada**: se o plano é máis longo ca o clip, RIFE v4 (MIT) mete un fotograma intermedio
   entre cada par (x2) ou tres (x4, se o plano dura máis do dobre); calcúlase unha vez antes da montaxe
   (`movemento.preparar`) e gárdase na caché xunto ao clip. Tope: metade de velocidade (`lento_min` = 0,5); máis
   lento, a xente camiña "baixo a auga".
2. **Se aínda sobra plano**, o último fotograma queda e segue o zoom lento do plano (non hai salto: o clip xa
   acaba case quieto).
3. **Escala a 1080p**: Lanczos desde 800x448 (x2,4) e **transferencia de detalle**: o fluxo óptico (DIS, OpenCV)
   de cada fotograma ao primeiro deforma a imaxe orixinal (1024x576 graduada, a mesma coa que se condicionou o
   clip) ata a postura dese fotograma e súmaselle ao clip o seu detalle fino (paso alto) só onde coinciden a baixa
   frecuencia; onde o clip trae contido novo (unha perna que avanza) queda o clip escalado. Real-ESRGAN descartouse
   polo custo (≈ 1-2 s por fotograma en CPU a esta escala [S]) e porque inventa textura.
4. `minterpolate` de ffmpeg non se usa: en movementos de persoas dá deformacións ("bolboretas") que RIFE non dá [S].

## 7. Porta de vídeo

`movemento.porta_video(mp4)`, automática, para cada clip I2V:

| Medida | Como | Bloquea se |
|---|---|---|
| Deriva da escena | CLIP ViT-L/14: coseno entre o primeiro fotograma e cada mostra | < 0,80 |
| Parpadeo de luz | luminancia media de cada fotograma fronte á súa media móbil de 9 | > 3,0 (0-255) |
| Cantidade de movemento | fluxo óptico Farneback medio (px/fotograma, a 800 px de ancho) | < 0,12 (quieto) ou > 4,5 (caótico) |
| Desorde do movemento | desviación local do fluxo fronte á súa media en 15x15 | > 0,85 (aviso) |
| Corpos | MediaPipe pose en 16 mostras: salto mediano dos puntos entre mostras (en torsos) e variación das proporcións brazo/perna/torso | salto > 0,45; CV > 0,30 |
| Mans | MediaPipe mans: mans lonxe de calquera pulso | aviso se > 1 mostra |

**Calibración (rolda 1).** Cos limiares de partida, a porta rexeitou **3 dos 6 clips bos** (planos 3, 17 e 18,
que se ven ben nas tiras): MediaPipe é inestable nas siluetas a contraluz (17: corpo en 3 de 16 mostras) e nos
primeiros planos de mans (18: 0-2 "corpos" ao chou), e o "salto" comparaba deteccións soltas; no plano 3, a
variación das proporcións saía alta (CV 0,49) polo escorzo do brazo que remexe cara á cámara. Arranxo no código:
as medidas do corpo só contan se MediaPipe ve o corpo en ≥ 60 % das mostras, os saltos só entre mostras seguidas e a
variación das proporcións pasa a aviso. Recalculado coas medidas gardadas (`probas/medidas-porta.json`, sen volver
pasar a porta): **6 de 6 OK**. Os 4 clips malos sintéticos (quieto, caótico, parpadeo, deriva de escena;
`scripts/porta_negativos.py`) non se chegaron a pasar: o candado estaba coa produción da v2. Mentres non se probe
con clips malos de verdade, a porta é unha rede contra fallos grosos, non un xuíz da calidade. Custo: 45-50 s por
clip (135 s o primeiro, coa carga de CLIP).

## 8. Orzamento para un episodio de 12 min (D18)

Custos medidos nesta máquina (4 núcleos, sen bf16), co candado:

| Paso | Custo medido | Fonte |
|---|---|---|
| Clip I2V 800x448, 73 fotogramas (3 s), 8 pasos | 470 s | planos 17 e 22 (49 fot.) |
| Clip I2V 800x448, 97 fotogramas (4 s), 8 pasos | 660 s | plano 22 graduado |
| Primeiro clip tras un reinicio (disco frío) | + 300 s | planos 3 e 14 |
| Embeddings de T5 (fp8), por acción | ≈ 21 s (menos en lote) + 6 s de carga | `t5_emb.py` |
| Porta de vídeo por clip (CLIP + MediaPipe + fluxo) | ver §7 | `porta_probas.py` |
| Paralaxe + efectos a 1080p, un proceso | 0,31-0,41 s por fotograma | `probas/medidas-paralaxe-plx1.json` |
| Montaxe con movemento (4 procesos, con profundidade, máscaras e RIFE) | 4,0 s por segundo de vídeo só paralaxe (demo de durmir); 6,2 s/s co gancho (2 planos I2V e 20 de paralaxe) | `demo-durmir.mp4`, `probas/medidas-demo.json` |
| Montaxe Ken Burns da v1 (referencia) | ≈ 2,2 s por segundo de vídeo (70 min para 31 min) | README do pipeline |

**Episodio de 12 min (720 s), ≈ 65 planos**, con persoas facendo algo en ≈ 40 (o 60 % da parte esperta que pide a
peza 4) e paralaxe con efectos nos ≈ 25 restantes:

| Configuración | I2V (40 clips + 20 % de repeticións pola porta) | Montaxe (≈ 6,2 s/s) | Total |
|---|---|---|---|
| **A. Recomendada**: 800x448, 97 fotog. nos planos ≥ 6 s e 73 nos curtos (20 + 20), 8 pasos, RIFE x2 e transferencia de detalle | (20 x 660 + 20 x 470) x 1,2 = **7,5 h** | **1,25 h** | **≈ 8,8 h** (+ 0,5 h de primeira carga, T5 e porta) |
| B. Todo a 97 fotogramas | 40 x 660 x 1,2 = 8,8 h | 1,25 h | ≈ 10,5 h |
| C. 1024x576, 97 fotog. (sen medir: ≈ 1,7 veces o custo por clip [S]) | ≈ 15 h | 1,3 h | non cabe |
| D. Menos I2V (só gancho e momentos clave: 15 clips) | 2,8 h | 1,2 h | ≈ 4,5 h |

A (≈ 9 h) cabe na noite de ≈ 10-12 h co que pediu o promotor en D18 (calidade por riba do custo). B tamén, xusto.
Mellor calidade que cabe = **A**; se a rolda 2 mostra que 800x448 se ve brando de máis a 1080p, a seguinte palanca
é 1024x576 só nos planos de rostro e mans (≈ 10 planos) [S].

**Disco para producir**: LTX 2B (6,3 GB) e o venv de vídeo (1,8 GB) quedan; o T5 fp8 (4,9 GB) báixase só para
calcular os embeddings de todas as accións do episodio nun lote (≈ 5 min) e bórrase despois; clips e cámara lenta
en MP4 (≈ 1,5 + 3 MB por plano); profundidade e máscaras ≈ 2 MB por imaxe. Total temporal ≈ 13 GB; despois ≈ 8,5 GB.

## 9. Licenzas

| Peza | Licenza | URL |
|---|---|---|
| LTX-Video 2B 0.9.8 destilado (Lightricks) | **LTXV Open Weights License 0.X** (15-04-2025, vale para todas as versións desde a 0.9.6): uso libre, tamén comercial, para entidades con menos de 10 M$ de ingresos anuais; as de máis teñen que mercar licenza. Restricións de uso do anexo A, entre elas (e) non difundir contido xerado sen avisar de forma expresa e intelixible de que o xerou unha máquina | https://huggingface.co/Lightricks/LTX-Video/blob/main/LTX-Video-Open-Weights-License-0.X.txt |
| T5-XXL v1.1 (codificador de texto de LTX), ficheiro fp8 de comfyanonymous | Apache-2.0 | https://huggingface.co/comfyanonymous/flux_text_encoders |
| Depth-Anything-V2-Small | Apache-2.0 (as versións Base e Large son CC BY-NC 4.0: non se usan) | https://huggingface.co/depth-anything/Depth-Anything-V2-Small-hf |
| CLIPSeg rd64 refined (máscaras por texto) | Apache-2.0 | https://huggingface.co/CIDAS/clipseg-rd64-refined |
| RIFE v4 (ECCV2022-RIFE, © Megvii), en safetensors | MIT | https://huggingface.co/TensorForger/RIFE-safetensors |
| MediaPipe (pose e mans) / CLIP ViT-L/14 (porta) | Apache-2.0 / MIT | xa no contorno principal |
| Wan2.2-TI2V-5B / FastWan2.2-TI2V-5B (non probados en CPU, ver §3) | Apache-2.0 | https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers, https://huggingface.co/FastVideo/FastWan2.2-TI2V-5B-FullAttn-Diffusers |

Consecuencia da cláusula (e) de LTXV para a canle: o aviso falado actual di que a voz é sintética e que o texto o
preparou un proceso automático, pero non fala das imaxes; ademais da etiqueta de contido sintético de YouTube, a
descrición debería dicir que imaxes e vídeo están xerados por IA (proposta para o orquestrador).

## 10. Alternativa con GPU alugada (prezos do 02-10-2026)

| Servizo e modelo | Prezo | Fonte |
|---|---|---|
| Replicate, `wan-video/wan-2.2-i2v-fast` (Wan 2.2 A14B I2V optimizado por PrunaAI; 81 fotogramas a 16 fps ≈ 5 s) | 0,05 $ por vídeo a 480p; 0,11 $ a 720p (0,065 / 0,145 $ con interpolación a 30 fps) | https://replicate.com/wan-video/wan-2.2-i2v-fast |
| fal.ai, Wan 2.2 A14B I2V | 0,04 $/s a 480p, 0,06 $/s a 580p, 0,08 $/s a 720p (segundos contados a 16 fps) | https://fal.ai/models/fal-ai/wan/v2.2-a14b/image-to-video |
| fal.ai, LTX-Video 13B 0.9.8 destilado I2V | 0,02 $/s (contado a 24 fps) | https://fal.ai/models/fal-ai/ltxv-13b-098-distilled/image-to-video |
| fal.ai, LTX-2 fast I2V | 0,04 $/s a 1080p (clips de 6 a 20 s) | https://fal.ai/models/fal-ai/ltx-2/image-to-video/fast |
| Hugging Face Inference Providers | o mesmo prezo ca o provedor, sen marxe (`docs/APRENDIZAJES.md`) | https://huggingface.co/docs/inference-providers/pricing |

**Custo dun episodio de 12 min con GPU alugada** (≈ 65 planos; supón 45 planos con persoas en I2V e dous intentos
de media por plano para escoller co ollo ou coa porta):

| Opción | Cálculo | Custo |
|---|---|---|
| Replicate `wan-2.2-i2v-fast` 720p (5 s por clip) | 90 clips x 0,11 $ | ≈ 10 $ |
| Replicate `wan-2.2-i2v-fast` 480p | 90 x 0,05 $ | ≈ 4,5 $ |
| fal Wan 2.2 A14B 720p | 90 x 5 s x 0,08 $/s | ≈ 36 $ |
| fal LTX-Video 13B 0.9.8 destilado | 90 x 5 s x 0,02 $/s | ≈ 9 $ |
| fal LTX-2 fast 1080p (mínimo 6 s) | 90 x 6 s x 0,04 $/s | ≈ 22 $ |

Os tempos de GPU son de minutos para todo o episodio (fronte ás horas de CPU de §8) e a calidade de Wan 2.2 A14B
ou LTX 13B/LTX-2 é outra liga ca a de LTX 2B. Fai falta unha clave de API (só chega a unha sesión nova) e decidir
se se acepta un servizo de pago (D5/D6: o canal quería ser local e sen suscricións). [S] os 2 intentos por plano.

## 11. Demo para o promotor e o crítico

- `demo-gancho.mp4` (1080p, 1:55, 25,4 MB, validada con ffmpeg, escrita en temporal + renomear): os planos 1-22 de
  `gauntlet3/video/escenas-montadas.json`, coas mesmas imaxes da v1 (e a súa gradación) e o audio dos primeiros 115 s
  do avance da v1. I2V nos planos 14 (rostro que xira a cabeza) e 22 (muller que camiña); paralaxe con efectos nos
  outros 20 (lume na queimada e na lareira, candeas, choiva no plano do cabalo, brétema no carballal, auga na xerra,
  po). Os clips dos planos 3, 17 e 18 existen pero quedaron fóra porque a primeira porta os rexeitou (falsos
  positivos, §7). Montaxe: 717 s (6,2 s por segundo de vídeo). Plan por plano: `demo-gancho-planos.json`.
- `demo-durmir.mp4` (60 s, 10,1 MB, sen son): planos 151, 153, 157 e 160 da v1 con fume, choiva e auga, brétema.
- Para remontar a demo cos 5 clips (≈ 12 min de CPU): `bash scripts/lote_r3.sh` (porta con malos sintéticos e
  demo).

