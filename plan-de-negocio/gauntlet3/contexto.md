# Gauntlet 3: vídeo largo "Cousas de Galiza para durmir"

Fichero de contexto que **todos los agentes leen al empezar** (y al empezar cada ronda). Las decisiones nuevas del
promotor se escriben aquí. Documentos de trabajo en **castellano**; todo lo que ve u oye el público en **galego
normativo (RAG)**.

Lecturas previas obligatorias: `CLAUDE.md`, `docs/HANDOFF.md`, `docs/APRENDIZAJES.md`,
`plan-de-negocio/decisiones.md`, las secciones PRIORITARIO de `plan-de-negocio/gauntlet2/contexto.md`, los veredictos
del vídeo `plan-de-negocio/gauntlet2/veredictos/video-r1.md`, `video-r2.md`, `video-r3.md` y
`herramientas/pipeline/README.md`.

## 1. Encargo del promotor (30-09-2026) — PRIORITARIO

Literal: *"Vamos a intentar elaborar un vídeo largo cogiendo la estela del vídeo de muestra más maduro del último
gauntlet. No quiero hacerlo de momento con LLM API, así que haz tú el guión con un agente y con un proceso de gauntlet.
Vamos a intentar mejorar la parte visual, el juez encontró problemas en la última muestra. El tono de voz debe ser más
gancho atractivo los primeros minutos y gradualmente debe irse hacia 'dormir'. El reclamo es 'Cousas de Galiza para
durmir' por lo que el capítulo puede ir de las meigas, queimadas, capítulos de la historia, la muiñeira o lo que creas
en tu gauntlet que vaya a dar más gancho y más audiencia. Trabaja mediante agentes y que guarden el trabajo parcial
cada poco por si se llega al límite de sesión. Documenta los aprendizajes cada poco también."*

## 2. Cómo lo interpreta el operador (Claude, orquestador)

| Punto | Decisión operativa |
|---|---|
| Base | El pipeline de la ronda 3 (`herramientas/pipeline/`, vídeo `gauntlet2/video/ejemplo.mp4`): voz Nós StyleTTS2 Brais, imágenes con puerta de revisión, lluvia, montaje, QA. Se mejora, no se rehace. |
| Duración | **≈ 30 min (25-35)**, como la referencia *Historia Desconocida* (36 min; media del canal 33 min). 60 min es el mismo proceso con el doble de cómputo. Guion de **≈ 3.300-3.900 palabras** (ronda 3: 131 palabras/min; aquí el ritmo baja con el embudo). |
| Guion | **Lo escribe Claude mediante agentes** (constructor + críticos independientes, Gauntlet), **no** un LLM por API ni el LLM local. **No es desatendido**: hay que declararlo en la QA, el README y los mensajes al promotor. Los controles automáticos (LanguageTool + hunspell, H1, veracidad contra el dossier, ASR) se pasan igual, como red de seguridad. |
| Lista de planos | Los prompts de imagen también los escribe un agente Claude (declararlo). Voz, imágenes, montaje y controles: open source y locales. |
| Reclamo | **"Cousas de Galiza para durmir"**. Fórmula hablada: *"Isto é Cousas de Galiza para durmir."* (sustituye a "Isto é Serán, historia de Galicia para durmir."). El título del vídeo lleva el reclamo. |
| Aviso hablado | Sigue vigente y es veraz (ninguna persona escribe ni revisa el texto): *"A voz que vas escoitar é sintética, e este texto preparouno un proceso automático."* Va **dentro del primer minuto**, tras un arranque en frío de ≤ 40 s (gancho). Nunca afirmar revisión humana. |
| Tono | **Embudo**: 0-2 min gancho vivo (curiosidad, contraste, "non vas crer…", todo verdadero); 2-8 min transición; desde ~8-10 min tono de dormir, cada vez más lento, suave y previsible; final sin sobresaltos. Voz, ritmo de cortes, luz de las imágenes y sonido siguen la misma curva. |
| Tema | Lo decide la pieza TEMA con evidencia de audiencia (vistas en YouTube de temas equivalentes en gl/es/pt, búsquedas) y de gancho: meigas, queimada, Santa Compaña, muiñeira, un capítulo de la historia... |
| Rigor | Nada inventado. Lo legendario se cuenta **como lenda** ("din que", "contan"). Lo dudoso se dice o se omite. Cifras con fuente o fuera. Ganchos verdaderos. |

## 3. Qué falló en la última muestra (a corregir)

**Imagen** (`gauntlet2/veredictos/video-r3.md` y HANDOFF):
- Plana y monótona: la misma luz gris de día nublado en casi todos los planos; paleta apagada y uniforme (la
  igualación de color `imaxes.graduar` hacia la media del episodio y el estilo fijo "muted oil painting, soft overcast
  light, grey-green and slate palette" la aplanaron).
- Composiciones repetidas: "figuras con capa alejándose por un camino" 3-4 veces; caras de multitudes genéricas.
- Se lee como "pintura al óleo genérica de IA", con poco rango emocional y dramático. La referencia gana por luz
  variada (contraluces, velas, pasillo con antorcha, jardín luminoso), variedad de planos (detalle, grupo, medio,
  general) y aspecto de drama de época.
- Iconografía no gallega: cipreses toscanos, carros con ruedas de radios, fachadas mediterráneas, tejados naranjas;
  multitudes con caras deformes. Falta una **lista positiva de iconografía galega** (granito, lousa, hórreo, cruceiro,
  carro de bois de roda maciza, palloza, lareira, carballos e castiñeiros, costa atlántica...).
- Imágenes generadas a 1024x576 y reescaladas: blandas en pantalla grande.

**Guion** (ronda 3): dossier recitado, seco, repetitivo, gancho sin referente, sin "picante" en los primeros
60-120 s. **Voz**: correcta (WER 0,037), pero el promotor quiere más gancho al principio y bajada gradual.

## 4. Listón (referencias reales)

- *Historia Desconocida*, "Versalles en 1682: Lujo por fuera, suciedad por dentro" (https://youtu.be/_lnOveSTjWA),
  36 min, 167.509 vistas; ver `plan-de-negocio/gauntlet2/referencia.md`.
- *Relatos al Oído*, "DUÉRMETE CON las Leyendas Más Antiguas y Misteriosas de GALICIA"
  (https://www.youtube.com/watch?v=ij7nuBjh1PQ), 107.875 vistas: demanda del tema en castellano
  (`gauntlet2/medidas/nicho/busquedas-yt.txt`).
- Los críticos comparan **a ciegas** contra la referencia cuando sea posible (A/B sin decir cuál es cuál).

## 5. Piezas del Gauntlet 3

| # | Pieza | Carpeta | Constructor | Crítico(s) |
|---|---|---|---|---|
| 0 | Entorno | `herramientas/` (script de instalación) | agente de entorno | prueba mínima de cada etapa |
| 1 | Tema | `gauntlet3/tema/` | investigador de audiencia y gancho | operador de canales faceless |
| 2 | Dossier | `gauntlet3/dossier/` | investigador de fuentes | verificador de hechos |
| 3 | Guion | `gauntlet3/guion/` | guionista (Claude) | operador faceless a ciegas vs referencia; revisor de lengua y veracidad |
| 4 | Voz | `gauntlet3/voz/` | ingeniero de voz | medidas (ritmo, F0, energía, *arousal*, WER) |
| 5 | Visual | `gauntlet3/visual/` | director de arte | crítico visual ciego vs referencia |
| 6 | Vídeo | `gauntlet3/video/` | pipeline | tribunal final (3 jueces) |

Cada ronda: borrador + veredicto (ganó/perdió, mayor carencia) → commit y push. Tope: 3 rondas por pieza.

## 6. Reglas de trabajo para los agentes (obligatorias)

1. **Guardar en git cada poco** (regla de `CLAUDE.md`): al terminar cada borrador, ronda, experimento o medida,
   `git add <rutas concretas>` (nunca `git add -A` ni `git add .`), `git commit` y `git push -u origin
   ccr-691a2e7c-82f2t8`. Si `index.lock` está ocupado (otro agente), esperar unos segundos y reintentar. Mensajes de
   commit en castellano, empezando por `Gauntlet 3: <pieza>: ...`, y terminando con estas dos líneas:

       Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
       Claude-Session: https://claude.ai/code/session_01BD94yPJF6iT3xx11HfzUbG

2. **No subir** ficheros de más de 50 MB, ni binarios a medio escribir (validar con `ffmpeg -v error -i f -f null -`
   y escritura atómica: temporal + renombrado). Nada de modelos, venvs ni cachés en el repo.
3. **Aprendizajes**: cada agente anota lo aprendido (qué funcionó, qué no, cifras) en
   `gauntlet3/aprendizajes/<pieza>.md` según avanza; el orquestador lo integra en `docs/APRENDIZAJES.md`.
4. **CPU y memoria compartidas** (4 núcleos, 15 GB, sin GPU): todo trabajo pesado (generar imágenes, TTS, ASR,
   Florence-2, NLI, render) va con el candado común:
   `flock /tmp/claude-0/-home-user-revolta/a8c9798c-edc6-5719-beda-018861fa4d7d/scratchpad/cpu.lock <comando>`.
   Las descargas y la escritura no lo necesitan. Disco: ~30 GB libres en total; borrar lo que no se use.
5. **Scratchpad** (no sobrevive entre sesiones): `SCRATCH=/tmp/claude-0/-home-user-revolta/a8c9798c-edc6-5719-beda-018861fa4d7d/scratchpad`.
   Entornos y modelos van ahí; `HF_HOME=$SCRATCH/hf`.
6. **Honestidad**: distinguir siempre lo automático de lo que hizo Claude (agente) a mano. No maquillar veredictos.
7. **Evidencia**: cada cifra con fuente (URL) o marcada como supuesto [S].
8. Devolver al orquestador un resumen **corto** (≤ 15 líneas): qué se hizo, dónde está, qué falta.

## 7. Decisiones nuevas del promotor durante el Gauntlet

(ninguna todavía)
