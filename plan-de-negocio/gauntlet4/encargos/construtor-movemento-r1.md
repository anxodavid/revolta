# Encargo: construtor do movemento (rolda 1) · Gauntlet 4

Texto literal co que o orquestrador lanzou o axente o 02-10-2026 (22:37 UTC). Para relanzalo noutra sesión, usar
este texto tal cal e engadir ao final: "Retoma desde o estado de `plan-de-negocio/gauntlet4/movemento/` e
`plan-de-negocio/gauntlet4/estado.md`: non repitas medidas que xa estean no repo". O contorno de vídeo (venv e
modelos) non sobrevive a unha sesión nova: reconstrúese co que diga `movemento/estado.md`.

---

Es o ENXEÑEIRO DE VFX (construtor) da peza 2 (MOVEMENTO), rolda 1, do Gauntlet 4 no repo /home/user/revolta (rama ccr-0584aac1-xqy2si). Traballa e escribe todo en galego normativo (D17): informes, aprendizaxes, comentarios do código novo e mensaxes de commit.

## O problema
O promotor viu a v1 de "As meigas de verdade" (31:22, 162 planos con imaxes fixas SDXL e só un Ken Burns de zoom ≤ 1,12x) e pide, literal: "Necesito movemento nas imaxes, xente que camiña, planos que evolucionan, como o exemplo de Versalles de Historia Desconocida" (https://youtu.be/_lnOveSTjWA, clips xerados con xente que se move). Na v2 ningún plano pode quedar fixo. Só temos CPU: Intel Xeon 2,8 GHz, 4 núcleos, AVX-512 sen bf16 nin AMX, 13,36 GiB de memoria para TODOS os procesos (cgroup), ≈ 15 GB de disco libre, sen GPU nin clave de API.

## Lecturas
`CLAUDE.md`; `plan-de-negocio/gauntlet4/contexto.md` (enteiro: §2, §6.1 formato da lista de planos con `animacion`, §6.2 orzamento, §7 regras); `herramientas/pipeline/README.md` (etapas, montaxe, episodio longo); `herramientas/pipeline/montaxe.py` e `imaxes.py` (función `bf16_rapido`: pesos en bf16 e cálculo en fp32 capa a capa, o truco que fixo usable SDXL nesta CPU); `docs/APRENDIZAJES.md` (sección de entorno: memoria, OOM, reinicios, candado); `plan-de-negocio/gauntlet3/veredictos/tribunal-final.md` §2 (que planos da v1 funcionan e cales non); `plan-de-negocio/gauntlet3/video/escenas-montadas.json` (planos da v1 con tempo, texto e prompt) e as imaxes da v1 en `plan-de-negocio/gauntlet3/video/imaxes/` (JPEG, o nome empeza polo número de plano menos un).

## Tarefas (por esta orde; garda en git cada resultado segundo saia)
1. **Contorno de vídeo aparte:** venv novo en `$SCRATCH/video/venv` (torch CPU, diffusers recente, transformers, accelerate, imageio-ffmpeg, opencv) para non tocar as versións do venv principal. Disco xusto: baixa só os ficheiros que se cargan e borra os modelos das probas descartadas.
2. **Medir imaxe a vídeo (I2V) en CPU**, cun tope de ≈ 3 h de CPU en total. Candidatos, por orde: (a) **LTX-Video 2B destilado** (Lightricks, a versión 2B destilada máis recente; comproba a licenza exacta e escríbea); (b) **Wan2.2-TI2V-5B** (Apache-2.0), mellor unha variante destilada de poucos pasos se existe (p. ex. FastWan), só se colle en disco e memoria; (c) opcional, SVD-XT 1.1 con AnimateLCM. O codificador de texto grande (T5-XXL / umT5) vai noutro proceso para calcular e gardar os embeddings, con pesos en bf16 ou fp8 e cálculo en fp32. Proba con 3-4 imaxes da v1 escollidas ollándoas: unha con persoas que camiñan (p. ex. o plano 22), unha de mans facendo algo (plano 1 ou 3, a queimada), unha con auga ou lume, e un rostro (plano 7). Mide segundos por clip e por paso, memoria pico (`/sys/fs/cgroup/memory.peak` ou mostraxe de `memory.current`), resolución, fotogramas e fps; garda tiras de 8 fotogramas por clip (JPEG) en `plan-de-negocio/gauntlet4/movemento/probas/` e MÍRAAS ti: deformacións de corpos e mans, caras que se funden, parpadeo, se a persoa camiña de verdade.
3. **Paralaxe 2,5D:** profundidade con Depth-Anything-V2-Small (Apache-2.0; as versións Base e Large son CC BY-NC: non usalas) e movementos de cámara (`avanza`, `recua`, `xira_esq`, `xira_der`, `sobe`, `baixa`, `pan_esq`, `pan_der`) con desprazamento segundo a profundidade e recheo dos ocos, a 1920x1080 e 24 fps. Mide s por fotograma.
4. **Microanimacións** (`efectos` do §6.1): como mínimo `lume` (chamas que se moven e luz que tremela no contorno), `choiva`, `bretema`/`fume` e `auga`; se dá tempo, `ceo`, `candea` e `po`. Máscaras por cor, profundidade ou un segmentador lixeiro con licenza permisiva (comproba e escribe a licenza). Sutís e críbles: mellor pouco que de videoxogo.
5. **Cámara lenta e escala:** os clips I2V duran 2-5 s e os planos 5-17 s: proba interpolación de fotogramas (RIFE, MIT, ou `minterpolate` de ffmpeg) e escalado a 1080p (Lanczos + nitidez; Real-ESRGAN só se o custo o permite). Propón como encher un plano longo (cámara lenta, clip + paralaxe do último fotograma, etc.).
6. **Porta de vídeo** automática para os clips I2V: MediaPipe (pose e mans) fotograma a fotograma, deriva de CLIP entre o primeiro e o último fotograma, parpadeo de luminancia e magnitude do fluxo óptico (nin quieto nin caótico). Calibrada coas túas probas.
7. **Código:** `herramientas/pipeline/movemento.py` (profundidade con caché, paralaxe, efectos, I2V con caché por hash de imaxe + acción + parámetros, porta de vídeo) e integración en `montaxe.py`: un plano pode ser clip ou paralaxe con efectos calculados ao voo; mantén fundidos, rótulos, brétema, viñeta e a compatibilidade co modo antigo (a v1 ten que poder volver montarse igual). Memoria: cada proceso de montaxe só carga o que precisa o seu treito.
8. **Demo para o promotor e o crítico:** o gancho da v1 animado (planos 1-21, 0:00-1:55 segundo `escenas-montadas.json`) coas mesmas imaxes da v1 e o audio da v1 tirado de `plan-de-negocio/gauntlet3/video/avance/avance-720p.mp4` (os primeiros 115 s): I2V nos 5-8 planos con persoas onde mellor saia e paralaxe con efectos no resto. `plan-de-negocio/gauntlet4/movemento/demo-gancho.mp4` (≤ 30 MB, valídao con ffmpeg e escríbeo en temporal + renomear). Se dá tempo, 60 s da zona de durmir con paralaxe e efectos (choiva na lousa, brasas, auga).
9. **Informe** `plan-de-negocio/gauntlet4/movemento/informe-r1.md`: táboa de custos (s por plano en cada modo e estimación para o episodio enteiro de ≈ 130-160 planos; como repartir o I2V para caber en ≈ 10-12 h de reloxo), calidade observada, licenzas con URL, e a alternativa con GPU alugada (prezos do día con URL en Replicate, fal ou Hugging Face para Wan 2.2 ou LTX I2V, e o custo dun episodio) para que decida o promotor. Aprendizaxes en `plan-de-negocio/gauntlet4/aprendizaxes/movemento.md`.
10. Opcional, máximo 10 min: tentar baixar o vídeo de Versalles con yt-dlp (o cliente web pide PO token; proba `android_vr`, `ios`, `tv`) para sacar tiras de fotogramas de uso interno en `$SCRATCH/referencia/`. Nunca no repo.

## Regras
As do §7 de `gauntlet4/contexto.md`. En especial: `export SCRATCH=/tmp/claude-0/-home-user-revolta/c92eba35-e89d-5d11-bb3d-f517a84dab48/scratchpad` e `source herramientas/pipeline/entorno.sh`; todo o pesado con `flock "$CPU_LOCK"` e collendo o candado POR EXPERIMENTO (outra peza, o guion, ten que pasar de cando en vez as súas portas de texto, ≈ 2 GB e uns minutos); traballos de máis de 25 min con `setsid nohup … &` e log; nada de modelos, venvs nin material de terceiros no repo; ficheiros ≤ 50 MB validados; commits "Gauntlet 4: movemento: ..." en galego coas dúas liñas de autoría do contexto, push a ccr-0584aac1-xqy2si. Se un OOM mata algo, apúntao nas aprendizaxes e baixa resolución ou fotogramas. Sé honesto: se o I2V en CPU non dá unha calidade publicable ou é lento de máis, dio con cifras e propón o mellor posible (paralaxe + efectos + I2V só onde funcione).

Despois de ti, un crítico (director de fotografía) comparará a cegas tiras de fotogramas da v1 (Ken Burns) e da túa demo e xulgará se o movemento é natural e mellor. Ao rematar, devolve un resumo de ≤ 15 liñas: modelo I2V escollido e custo por clip, calidade, que fai a paralaxe, efectos feitos, onde está a demo e que falta.

---

## Mensaxes posteriores do orquestrador

- 22:42 UTC: fusionouse o PR #5 en main e main na rama (c4fcc72). Cambiaron 11 imaxes da v1 (5, 31, 56, 61, 67,
  84, 91, 133, 145, 153, 161) e `escenas-montadas.json`; no gancho só cambia o plano 5. `son.limitar` mide o pico real.
- 22:47 UTC: disco ao 95 % (2,3 GB libres). Orzamento de MOVEMENTO: ≤ 13 GB en `$SCRATCH/video`. Wan2.2 só se cabe
  nese orzamento (borrando o de LTX que non se use; GGUF Q8 ou fp8). Borrar frames e clips intermedios. No informe,
  que ficheiros de modelo fan falta para producir e cales se poden borrar (a produción precisa ≈ 8 GB libres).
- 22:55 UTC: gardar no repo os scripts propios e as notas parciais (commit polo menos cada 30 min) e manter
  `plan-de-negocio/gauntlet4/movemento/estado.md` (feito, en curso, como reconstruír o contorno e retomar).
