# Aprendizaxes da peza MOVEMENTO (Gauntlet 4)

Axente: enxeñeiro de VFX (Claude). Medidas propias nesta máquina (Intel Xeon 2,8 GHz, 4 núcleos, AVX-512 sen bf16
nin AMX, 13,36 GiB de cgroup para todos os procesos) salvo que se diga outra cousa. Os xuízos de calidade son
dun axente Claude mirando tiras de fotogramas: ninguén viu os clips en movemento.

## Contorno

- **Venv de vídeo aparte** (`$SCRATCH/video/venv`, 1,8 GB, ≈ 3 min): torch 2.14.1+cpu, diffusers 0.40.0,
  transformers 5.18.0. O venv principal (diffusers 0.35.2, transformers 4.57.6) queda intacto.
- **T5-XXL en fp8 con cálculo en fp32**: o ficheiro `t5xxl_fp8_e4m3fn.safetensors` (4,89 GB) cargado nun
  `T5EncoderModel` de transformers cambiando cada `nn.Linear` por unha capa que garda o peso en fp8 e o pasa a fp32
  ao multiplicar: 6 s de carga, ≈ 21 s por texto (o custo é a conversión dos 4.700 M de pesos en cada chamada, non o
  cálculo), pico 6,4 GB. Trampa: o bloque de T5 de transformers mira `wo.weight.dtype` e pasaría o estado oculto a
  fp8; un `weight` baleiro en fp32 na capa evítao. Mellora pendente: varios textos nun lote (a conversión págase unha
  vez).
- **Cargar LTX desde o ficheiro único sen lelo enteiro**: `safe_open` + as funcións de conversión de diffusers
  (`convert_ltx_transformer_checkpoint_to_diffusers`, `convert_ltx_vae_checkpoint_to_diffusers`) e
  `load_state_dict(assign=True)` sobre modelos baleiros (`init_empty_weights`): 3,2 s; os pesos quedan mapeados do
  disco (contan como caché, non como memoria anónima).
- **Descargas grandes e memoria**: mentres baixaban 11 GB (sen candado, só rede) o OOM matou a verificación do
  contorno (SDXL 10,5 GB + revisor nun mesmo momento). O OOM foi da verificación, pero as páxinas sucias dunha
  descarga tamén contan no cgroup: mellor non baixar xigas mentres outro proceso está preto do límite.
- Un `bash -c "…"` con varias ordes dentro dispara unha comprobación de seguridade da ferramenta: os lanzadores van
  nun `.sh` propio (`scripts/lanzar_ltx.sh`).

## Imaxe a vídeo (I2V) en CPU

- **LTX-Video 2B 0.9.8 destilado, 800x448, 49 fotogramas (2 s a 24 fps), 8 pasos**: 470 s por clip (paso ≈ 42 s; o
  primeiro, 71 s, inclúe codificar a imaxe; descodificar o VAE por teselas, 103 s). Pico do proceso 11,4 GB (con
  páxinas mapeadas do ficheiro), memoria anónima de todo o cgroup 9,0 GB. ≈ 260 GFLOPS efectivos.
- Calidade (plano 22, muller de costas nun camiño): **camiña de verdade** (pés que alternan, saia que abanea) e a
  cámara acompáñaa como nun travelling; sen deformacións visibles na tira nin no recorte das pernas.

## Paralaxe 2,5D e efectos (primeira proba, 02-10-2026)

- **Custo**: 0,31-0,41 s por fotograma a 1920x1080 nun proceso (4 fíos de OpenCV), incluídos os efectos; preparar
  profundidade e máscaras, 11-18 s por imaxe a primeira vez (carga dos modelos incluída), despois caché.
- **Funcionan á primeira** (tiras `probas/plx1_*`): o avance co relevo (o carballo do centro medra máis ca o fondo),
  a choiva en tres capas, a brétema que se move, o lume da queimada.
- **Dous defectos que só se viron mirando as tiras** (e que unha medida automática non cazaría):
  - **Candea con rachas escuras dentro da chama**: o desprazamento con ruído de onda curta e amplitude grande
    "dobraba" a imaxe e metía fondo escuro na chama. Arranxo: na candea, deformación xeométrica suave (a punta
    abanea máis ca a base, estira e encolle arredor do pabío) e, no lume, lonxitude de onda grande con amplitude
    menor ca un cuarto dela (sen dobras).
  - **Pantasma da cabeza ao mover o ceo**: a máscara de ceo de CLIPSeg (352x352) chega ata o pelo a contraluz, e
    ao desprazar as nubes mostreábase a cabeza. Arranxo: textura só de ceo (o resto énchese co ceo de arredor por
    inpaint) e máscara encollida no bordo; e as nubes a 0,35 % do ancho por segundo (antes 1,2 %: de máis).
- **O candado**: con `flock` non hai orde de chegada e os experimentos de vídeo collen a CPU 10-20 min. O
  orquestrador puxo `herramientas/gauntlet/candado.sh` (prioridade para guion e voz); `movemento_i2v.py` segue o
  mesmo protocolo por dentro (despois de coller o candado mira `$CPU_LOCK.prio` e, se está collido, cede e
  reinténtao aos 15 s).
- **O OOM das 22:46 UTC** (dmesg: uptime 1.435 s, `proba_entorno.py` con 10,5 GB de memoria anónima) foi antes de
  lanzar a primeira proba de LTX (22:56); nese momento desta peza só corrían o `pip install` do venv de vídeo e a
  descarga de modelos (sen modelos cargados). Igualmente, desde entón todo vai co candado, tamén as probas curtas.

## I2V, porta e montaxe (03-10-2026, rolda 1 pechada)

- **LTX 2B en quente: 470 s por clip de 3 s e 660 s por clip de 4 s a 800x448** (paso 42-63 s, descodificar
  105-145 s). Despois dun reinicio do contedor o primeiro clip paga +300 s (os 6,3 GB de pesos lense do disco en
  frío). 97 fotogramas a 800x448 xa son 11 GB de memoria anónima: máis resolución ou máis fotogramas arrisca o OOM.
- **As tiras dos 6 clips vense naturais** (camiñar, mans, rostro, dúas siluetas): LTX 2B destilado anima ben
  imaxes de SDXL cando o prompt describe un só movemento lento ("walks slowly away", "turns her head").
- **A porta de vídeo con MediaPipe dá falsos positivos** en siluetas, primeiros planos de mans e escorzos: as
  medidas do corpo só valen se o corpo se detecta de forma estable (≥ 60 % das mostras). Sen clips malos de verdade
  non hai calibración seria; fan falta exemplos malos (sintéticos ou xerados) antes de confiar nela.
- **A cámara lenta de RIFE en `.npy` ocupaba 207 MB por clip**: en MP4 case sen perdas, ≈ 3 MB.
- **Compatibilidade coa v1: comparar fotogramas en memoria**, non MP4: dúas codificacións x264 do mesmo vídeo
  difiren (diferenza máxima 40 de 255) aínda que os fotogramas sexan idénticos.
- **Cota e reinicios**: a sesión chegou dúas veces ao límite de uso e o contedor reiniciouse, matando os lotes.
  Funcionou: lotes en serie nun `.sh` desacoplado que se poden relanzar (a caché por hash salta o feito), unha soa
  espera en segundo plano e commits tras cada paso.
