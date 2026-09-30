# entorno.sh: variables del entorno local del pipeline (voz, imágenes, QA, montaje).
#
#   source herramientas/pipeline/entorno.sh          # SCRATCH = scratchpad de la sesión más reciente
#   SCRATCH=/otra/ruta source herramientas/pipeline/entorno.sh
#
# Todo cuelga de SCRATCH (el scratchpad no sobrevive entre sesiones: se reconstruye con instalar.sh).
# Si SCRATCH no está definida, se toma el scratchpad de Claude Code modificado más recientemente
# (/tmp/claude-*/<proyecto>/<sesión>/scratchpad) y, si no hay ninguno, /tmp/revolta-scratch.
# El resto de rutas se derivan siempre de SCRATCH: si se cambia SCRATCH, hay que volver a hacer source.

if [ -z "${SCRATCH:-}" ]; then
  SCRATCH="$(ls -dt /tmp/claude-*/*/*/scratchpad 2>/dev/null | head -1)"
  SCRATCH="${SCRATCH:-/tmp/revolta-scratch}"
fi
export SCRATCH

# Modelos de Hugging Face (SDXL-Turbo, Florence-2, NLI, CLIP) en la caché estándar dentro de SCRATCH.
export HF_HOME="$SCRATCH/hf"
# Descarga por HTTP normal (puente xet de HF) y no por el protocolo xet: el primero funciona tras el proxy.
export HF_HUB_DISABLE_XET=1
export HF_HUB_DISABLE_TELEMETRY=1 TOKENIZERS_PARALLELISM=false

# Un solo venv (Python 3.11 del sistema) para todo el pipeline: voz, imágenes, revisión, QA y montaje.
export PY_TTS="$SCRATCH/tts/venv/bin/python"
export PY="$PY_TTS"

# Voz: Nos_StyleTTS2-Brais-GL (código + Models/galician) y stubs para importar el código.
export ST2_DIR="$SCRATCH/bench/st2"
export ST2_STUBS="$SCRATCH/bench/stubs"
# Cotovía (fonemas de la voz). Por defecto, la compilada desde Nos_StyleTTS2 (instalar.sh cotovia_nova, en modo -p1):
# da los fonemas con los que se entrenó el modelo (vocales abiertas, monosílabos átonos, sin "pra" ni "facelo lume").
# A/B y medidas: plan-de-negocio/gauntlet3/voz/informe.md. Si no está compilada, la 0.5 del .deb (bench/pathbin).
# Para forzar la 0.5 después de este source: export ST2_PATHBIN="$COTOVIA_05_PATHBIN"
export COTOVIA_05_PATHBIN="$SCRATCH/bench/pathbin"
export COTOVIA_NOVA_PATHBIN="$SCRATCH/bench/pathbin_nova"
if [ -x "$COTOVIA_NOVA_PATHBIN/cotovia" ]; then
  export ST2_PATHBIN="$COTOVIA_NOVA_PATHBIN"
else
  export ST2_PATHBIN="$COTOVIA_05_PATHBIN"
fi
# Referencia de estilo (grabación humana del corpus Nos_Brais-GL, test) y banco de referencias variadas.
export REF_WAV="$SCRATCH/tts/kit/t1/brais_1_human.wav"
export REFS_DIR="$SCRATCH/tts/refs"

# QA: Whisper galego de Nós convertido a CTranslate2 int8 (faster-whisper).
export WHISPER_DIR="$SCRATCH/bench/wgl_ct2"
# Puerta de imágenes: tareas de MediaPipe (Florence-2 se carga por nombre desde HF_HOME).
export REVISOR_DIR="$SCRATCH/revisor"
# LanguageTool (language_tool_python lo busca y lo descarga en LTP_PATH).
export LTP_PATH="$SCRATCH/languagetool"
# Puerta de iconografía (agente visual): CLIP ViT-L/14 por transformers (MIT).
export CLIP_MODEL="openai/clip-vit-large-patch14"

# Candado común de CPU: todo trabajo pesado va con  flock "$CPU_LOCK" <orden>
export CPU_LOCK="$SCRATCH/cpu.lock"
