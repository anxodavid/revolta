#!/usr/bin/env bash
# instalar.sh: reconstruye en $SCRATCH todo el entorno local del pipeline de vídeo (voz, imágenes, revisión, QA,
# montaje). Idempotente: cada paso deja una marca en $SCRATCH/.instalado/<paso>.ok y se salta si ya está hecho.
#
#   bash herramientas/pipeline/instalar.sh                  # todo (ver tiempos y tamaños en el README)
#   bash herramientas/pipeline/instalar.sh verificar        # pruebas mínimas de cada etapa (probas/proba_entorno.py)
#   bash herramientas/pipeline/instalar.sh st2 brais        # solo esos pasos
#   FORZAR=1 bash herramientas/pipeline/instalar.sh whisper # rehace un paso aunque tenga marca
#   SCRATCH=/otra/ruta bash herramientas/pipeline/instalar.sh
#
# Pasos (en este orden):
#   sistema      apt: libegl1, libgles2 (MediaPipe), libgl1 (cv2), libportaudio2 (sounddevice); Java si falta
#   cotovia      Cotovía 0.5 (.deb de SourceForge) extraído en $SCRATCH/cotovia + envoltorio en bench/pathbin
#   venv_base    venv con Python 3.11 del sistema en tts/venv + huggingface-hub (para empezar a descargar ya)
#   --- en paralelo (registros en $SCRATCH/logs/instalar-<paso>.log):
#   paquetes     torch/torchaudio CPU y el resto de paquetes (lista PAQUETES)
#   st2          proxectonos/Nos_StyleTTS2-Brais-GL en bench/st2 (sin el checkpoint de la 1.ª etapa)
#   brais        grabaciones humanas de Nos_Brais-GL: referencia de estilo (tts/kit/t1) y 40 variadas (tts/refs)
#   revisor      tareas de MediaPipe (manos y pose) en revisor/
#   sdxl florence nli clip whisper_hf   modelos de Hugging Face (solo los ficheros que se cargan)
#                (sdxl = SDXL-Lightning 4 pasos + VAE de SDXL base + codificadores de texto; sdxl_turbo, opcional, aparte)
#   ---
#   stubs        módulos stub para importar el código de StyleTTS2 en CPU (bench/stubs)
#   whisper      conversión del Whisper galego a CTranslate2 int8 (bench/wgl_ct2) y borrado del original
#   languagetool LanguageTool (descarga de language_tool_python en $LTP_PATH) y prueba gl-ES
#   cotovia_nova (opcional; si falla, solo avisa) compila la Cotovía de Nos_StyleTTS2 en bench/pathbin_nova
#   limpieza     borra temporales y la caché de pip; resumen de tamaños
#
# Requisitos: Ubuntu 24.04 con Python 3.11 (/usr/bin/python3.11), acceso a PyPI, download.pytorch.org,
# huggingface.co, sourceforge.net, storage.googleapis.com y el servidor de descargas de LanguageTool.
# Ejecutar como root (apt) o con sudo disponible. Los pasos pesados de CPU usan el candado $CPU_LOCK.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=entorno.sh
source "$HERE/entorno.sh"
MARCAS="$SCRATCH/.instalado"
LOGS="$SCRATCH/logs"
mkdir -p "$SCRATCH" "$MARCAS" "$LOGS" "$SCRATCH/tmp"
touch "$CPU_LOCK"
export PIP_NO_CACHE_DIR=1 PIP_DISABLE_PIP_VERSION_CHECK=1 PIP_PROGRESS_BAR=off
SUDO=""; [ "$(id -u)" -ne 0 ] && SUDO="sudo"
PYSIS="${PYSIS:-/usr/bin/python3.11}"     # Python del sistema con el que se crea el venv
TORCH_VER="2.10.0"                        # la versión que fija requirements.txt de Nos_StyleTTS2 (torchaudio igual)

# Paquetes del venv, además de torch/torchaudio (CPU). Versiones exactas usadas: requisitos-entorno.txt
PAQUETES=(
  "diffusers==0.35.2" "huggingface-hub>=0.34,<1.0" "transformers>=4.56,<5" accelerate safetensors  # SDXL-Turbo, Florence-2, NLI, CLIP
  faster-whisper ctranslate2 jiwer                          # ASR (QA) y conversión del Whisper galego
  language_tool_python                                      # LanguageTool gl-ES (Java)
  pyloudnorm imageio-ffmpeg soundfile scipy pyyaml pillow numpy   # son, montaxe, pipeline
  mediapipe sentencepiece protobuf                          # revisor (trae opencv-contrib-python), tokenizadores
  munch nltk einops einops-exts librosa matplotlib          # código de StyleTTS2 (inferencia)
  yt-dlp                                                    # agentes de tema y referencia
)

log() { printf '[%(%H:%M:%S)T] %s\n' -1 "$*"; }
hecho() { [ -z "${FORZAR:-}" ] && [ -f "$MARCAS/$1.ok" ]; }

# baixar DESTINO URL: descarga con reintentos a un .part y renombra al final (nunca deja ficheros a medias)
baixar() {
  local dest="$1" url="$2"
  [ -s "$dest" ] && return 0
  mkdir -p "$(dirname "$dest")"
  curl -fL --retry 6 --retry-all-errors --retry-delay 5 -sS -o "$dest.part" "$url"
  mv "$dest.part" "$dest"
}

# hf_baixar REPO [DIR_LOCAL] [PATRÓNS...]: snapshot de Hugging Face (a la caché HF_HOME o a DIR_LOCAL si no es "-")
hf_baixar() {
  "$PY" - "$@" <<'EOF'
import sys, time
from huggingface_hub import snapshot_download
repo, local, pats = sys.argv[1], sys.argv[2], sys.argv[3:]
allow = [p for p in pats if not p.startswith('!')] or None
ignore = [p[1:] for p in pats if p.startswith('!')] or None
for intento in range(5):          # el proxy corta a veces transferencias largas: se reintenta (reanuda)
    try:
        p = snapshot_download(repo, local_dir=None if local == '-' else local, allow_patterns=allow,
                              ignore_patterns=ignore, max_workers=4)
        print(repo, '->', p, flush=True); break
    except Exception as e:
        print(f'{repo}: intento {intento + 1} fallou: {e!r}', flush=True); time.sleep(10 * (intento + 1))
else:
    sys.exit(f'{repo}: non se puido descargar')
EOF
}

# ------------------------------------------------------------------------------------------------- pasos
paso_sistema() {
  local faltan=() p
  for p in libegl1 libgles2 libgl1 libportaudio2; do dpkg -s "$p" >/dev/null 2>&1 || faltan+=("$p"); done
  command -v java >/dev/null || faltan+=(openjdk-21-jre-headless)   # LanguageTool 6.x necesita Java >= 17
  if [ ${#faltan[@]} -gt 0 ]; then
    $SUDO apt-get update -qq
    DEBIAN_FRONTEND=noninteractive $SUDO apt-get install -y -qq --no-install-recommends "${faltan[@]}"
  fi
  [ -x "$PYSIS" ] || { echo "Falta $PYSIS (Python 3.11 del sistema)"; return 1; }
}

paso_cotovia() {
  # Cotovía 0.5 (GPL; SourceForge, proyecto cotovia): no se instala en el sistema, se extrae en $SCRATCH/cotovia.
  # El código de Nos_StyleTTS2 llama a "cotovia -n -S -A0" por el PATH: el envoltorio de bench/pathbin añade
  # el directorio de datos (-D), que en el .deb es /usr/share/cotovia/data.
  local d="$SCRATCH/deb" f
  for f in cotovia_0.5_amd64.deb cotovia-lang-gl_0.5_all.deb; do
    baixar "$d/$f" "https://downloads.sourceforge.net/project/cotovia/Debian%20packages/$f"
    dpkg-deb -x "$d/$f" "$SCRATCH/cotovia"
  done
  mkdir -p "$ST2_PATHBIN"
  cat > "$ST2_PATHBIN/cotovia" <<EOF
#!/bin/sh
# Envoltorio de Cotovía 0.5 extraído en \$SCRATCH/cotovia (generado por instalar.sh). Acepta UTF-8 en la entrada y
# escribe ISO-8859-1 (phonemize.py de Nos_StyleTTS2 descodifica con respaldo latin-1).
exec "$SCRATCH/cotovia/usr/bin/cotovia" -D "$SCRATCH/cotovia/usr/share/cotovia/data" "\$@"
EOF
  chmod +x "$ST2_PATHBIN/cotovia"
  # prueba: transcripción fonética de una frase con tildes y eñe
  local saida
  saida="$(echo "Os mariñeiros saíron á mar." | "$ST2_PATHBIN/cotovia" -n -S -A0 2>/dev/null | iconv -f latin1 -t utf-8)"
  [[ "$saida" == *'mariJe^jros'* ]] || { echo "Cotovía non transcribe: $saida"; return 1; }
}

paso_venv_base() {
  [ -x "$PY" ] || "$PYSIS" -m venv "$SCRATCH/tts/venv"
  "$PY" -m pip install -q --upgrade pip wheel setuptools
  "$PY" -m pip install -q "huggingface-hub>=0.34,<1.0"
}

paso_paquetes() {
  "$PY" -m pip install -q "torch==$TORCH_VER" "torchaudio==$TORCH_VER" --index-url https://download.pytorch.org/whl/cpu
  # requisitos-entorno.txt (pip freeze de la instalación probada) fija las versiones si existe; torch va aparte
  local restr=()
  if [ -f "$HERE/requisitos-entorno.txt" ]; then
    grep -v -E '^(torch|torchaudio)==' "$HERE/requisitos-entorno.txt" > "$SCRATCH/tmp/restricions.txt"
    restr=(-c "$SCRATCH/tmp/restricions.txt")
  fi
  "$PY" -m pip install -q "${restr[@]}" "${PAQUETES[@]}"
  "$PY" -m pip check || log "aviso: pip check con conflictos (ver arriba)"
  "$PY" -m pip freeze > "$LOGS/pip-freeze.txt"
  "$PY" -c "import torch, diffusers, transformers, mediapipe, faster_whisper, ctranslate2, librosa, language_tool_python; print('torch', torch.__version__, 'diffusers', diffusers.__version__, 'transformers', transformers.__version__, 'mediapipe', mediapipe.__version__, 'ctranslate2', ctranslate2.__version__)"
}

paso_st2() {
  # Código + Models/galician (ASR, PLBERT, brais 2.ª etapa). Sin epoch_1st_00095.pth (1,7 GB): solo sirve para entrenar.
  hf_baixar proxectonos/Nos_StyleTTS2-Brais-GL "$ST2_DIR" '!Models/galician/brais/epoch_1st_*'
  # Los tres checkpoints traen el estado del optimizador (2,1 GB de 3,2 GB), que solo sirve para seguir entrenando:
  # se guardan de nuevo sin él (escritura atómica). El código de inferencia solo lee 'net' (brais, PLBERT) y 'model'
  # (ASR). Ojo: con FORZAR=1 st2, huggingface_hub ve los ficheros cambiados y los vuelve a bajar enteros (~2 min).
  (cd "$ST2_DIR" && "$PY" - <<'EOF'
import os, torch
for f in ('Models/galician/brais/epoch_2nd_00057.pth', 'Models/galician/PLBERT/step_1000000.t7',
          'Models/galician/ASR/epoch_00080.pth'):
    c = torch.load(f, map_location='cpu')          # weights_only=True basta: solo tensores y números
    if 'optimizer' not in c:
        continue
    antes = os.path.getsize(f)
    torch.save({k: v for k, v in c.items() if k not in ('optimizer', 'scheduler')}, f + '.tmp')
    os.replace(f + '.tmp', f)
    print(f'{f}: {antes / 1e6:.0f} MB -> {os.path.getsize(f) / 1e6:.0f} MB (sin optimizer)', flush=True)
EOF
  )
}

paso_brais() {
  # Nos_Brais-GL (CC-BY-4.0 con términos de uso de Nós/USC: prohibido difundir las grabaciones). Solo se guardan en
  # el scratchpad como referencia de estilo de StyleTTS2; nunca se suben al repo ni se publican.
  python3 - <<'EOF'
import csv, io, os, re, shutil, subprocess, wave
S = os.environ['SCRATCH']; refs = os.environ['REFS_DIR']; os.makedirs(refs, exist_ok=True)
BASE = 'https://huggingface.co/datasets/proxectonos/Nos_Brais-GL/resolve/main/'
def baixar(url, dest):
    if os.path.exists(dest) and os.path.getsize(dest) > 0: return
    subprocess.run(['curl', '-fL', '--retry', '6', '--retry-all-errors', '-sS', '-o', dest + '.part', url], check=True)
    os.replace(dest + '.part', dest)
for c in ('brais_test.csv', 'brais_train.csv'):
    baixar(BASE + c, os.path.join(refs, c))
def filas(c):
    return list(csv.DictReader(open(os.path.join(refs, c), encoding='utf-8'), delimiter='\t'))
test, train = filas('brais_test.csv'), filas('brais_train.csv')
def cat(t):
    n = len(t.split())
    if '¡' in t or '!' in t: return 'exclamacion'
    if '¿' in t or '?' in t: return 'pregunta'
    if '...' in t or '…' in t: return 'suspensivos'
    if n >= 20 and t.endswith('.'): return 'longa'
    return None
# 21 de test (no usadas para entrenar) + 19 de train elegidas de forma determinista por categoría (repartidas)
elixidas = [(r, 'test', cat(r['transcripts']) or 'test') for r in test]
for categoria, n in (('exclamacion', 5), ('pregunta', 5), ('suspensivos', 4), ('longa', 5)):
    cand = sorted([r for r in train if cat(r['transcripts']) == categoria and 4 <= len(r['transcripts'].split()) <= 40],
                  key=lambda r: r['file_name'])
    paso = max(1, len(cand) // n)
    elixidas += [(r, 'train', categoria) for r in cand[::paso][:n]]
out = []
for r, split, categoria in elixidas:
    dest = os.path.join(refs, r['file_name'])
    baixar(r['audio'].strip(), dest)
    with wave.open(dest) as w:
        s = w.getnframes() / w.getframerate(); sr = w.getframerate()
    out.append((r['file_name'], split, categoria, f'{s:.2f}', r['transcripts'].strip()))
with open(os.path.join(refs, 'refs.tsv'), 'w', encoding='utf-8') as f:
    f.write('ficheiro\tsplit\tcategoria\tsegundos\ttexto\n')
    f.writelines('\t'.join(x) + '\n' for x in out)
# referencia de estilo del pipeline (REF_WAV): la frase 1 del kit A/B (test), como en el Gauntlet 2
t1 = os.path.join(S, 'tts/kit/t1'); os.makedirs(t1, exist_ok=True)
ref = [r for r in test if r['transcripts'].startswith('As medidas afectan en Galicia')][0]
shutil.copy(os.path.join(refs, ref['file_name']), os.path.join(t1, 'brais_1_human.wav'))
print(len(out), 'grabaciones en', refs, '| frecuencia', sr, 'Hz | REF_WAV =', ref['file_name'])
EOF
}

paso_revisor() {
  local u=https://storage.googleapis.com/mediapipe-models
  baixar "$REVISOR_DIR/hand_landmarker.task" "$u/hand_landmarker/hand_landmarker/float16/latest/hand_landmarker.task"
  baixar "$REVISOR_DIR/pose_landmarker_full.task" "$u/pose_landmarker/pose_landmarker_full/float16/latest/pose_landmarker_full.task"
}

# Modelos en la caché de HF: solo los ficheros que carga el código (sin fp32, onnx, flax, tf ni duplicados).
paso_sdxl() {   # imaxes.py, modelo por defecto IMG_MODEL=lightning (Gauntlet 3): SDXL base + UNet SDXL-Lightning 4 pasos
  # codificadores de texto: os do repo de Turbo (mesmo sha256 que os de SDXL base; ver imaxes.py)
  hf_baixar stabilityai/sdxl-turbo - model_index.json 'tokenizer/*' 'tokenizer_2/*' LICENSE.md \
    text_encoder/config.json text_encoder/model.fp16.safetensors \
    text_encoder_2/config.json text_encoder_2/model.fp16.safetensors
  hf_baixar stabilityai/stable-diffusion-xl-base-1.0 - model_index.json 'scheduler/*' 'tokenizer/*' 'tokenizer_2/*' \
    unet/config.json vae/config.json vae/diffusion_pytorch_model.fp16.safetensors LICENSE.md
  hf_baixar ByteDance/SDXL-Lightning - sdxl_lightning_4step_unet.safetensors LICENSE.md
}
paso_sdxl_turbo() {   # opcional (IMG_MODEL=turbo, o modelo do Gauntlet 2): UNet e VAE de SDXL-Turbo (5,3 GB)
  hf_baixar stabilityai/sdxl-turbo - 'scheduler/*' unet/config.json unet/diffusion_pytorch_model.fp16.safetensors \
    vae/config.json vae/diffusion_pytorch_model.fp16.safetensors
}
paso_florence() { hf_baixar florence-community/Florence-2-large -; }          # revisor.py (MIT)
paso_nli() {      # veracidade.py (MIT): sin pytorch_model.bin ni onnx (duplicados del safetensors)
  hf_baixar MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7 - '*.json' spm.model model.safetensors LICENSE
}
paso_clip() {     # puerta de iconografía del agente visual (MIT): solo el safetensors
  hf_baixar openai/clip-vit-large-patch14 - '*.json' '*.txt' model.safetensors
}
paso_whisper_hf() {   # original de Nós a un temporal (sin optimizer.pt de 6,5 GB ni estado de entrenamiento)
  if [ -z "${FORZAR:-}" ] && [ -s "$WHISPER_DIR/model.bin" ]; then echo "ya convertido en $WHISPER_DIR"; return 0; fi
  hf_baixar proxectonos/whisper-large-v3-turbo-gl-v1.0 "$SCRATCH/tmp/whisper-hf" \
    config.json generation_config.json model.safetensors preprocessor_config.json tokenizer.json \
    tokenizer_config.json special_tokens_map.json added_tokens.json vocab.json merges.txt normalizer.json
}

paso_stubs() {
  # El código de Nos_StyleTTS2 importa al cargarse (utils.py, inference.py) dos paquetes que solo usa para entrenar o
  # evaluar. En vez de instalarlos (el monotonic_align de StyleTTS2 se instala desde GitHub y compila Cython; el
  # "monotonic-align" de PyPI es otro paquete con otra API; speechmos arrastra onnxruntime y modelos DNSMOS), se ponen
  # módulos vacíos en bench/stubs (PYTHONPATH del subproceso de voz). Si algo los llamase, fallaría con claridad.
  local s="$ST2_STUBS"
  mkdir -p "$s/monotonic_align" "$s/speechmos"
  cat > "$s/monotonic_align/__init__.py" <<'EOF'
"""STUB de monotonic_align (Cython de StyleTTS2/VITS). utils.py de Nos_StyleTTS2 importa maximum_path y
mask_from_lens al cargarse, pero solo se usan para entrenar (alineamiento monótono). En inferencia no se llaman."""


def maximum_path(*a, **k):
    raise NotImplementedError('monotonic_align es un stub (solo para entrenar): ver instalar.sh')


def mask_from_lens(*a, **k):
    raise NotImplementedError('monotonic_align es un stub (solo para entrenar): ver instalar.sh')
EOF
  cat > "$s/monotonic_align/core.py" <<'EOF'
"""STUB de monotonic_align.core (extensión Cython). Solo se usa para entrenar."""


def maximum_path_c(*a, **k):
    raise NotImplementedError('monotonic_align.core es un stub (solo para entrenar): ver instalar.sh')
EOF
  cat > "$s/speechmos/__init__.py" <<'EOF'
"""STUB de speechmos. inference.py de Nos_StyleTTS2 hace "from speechmos import dnsmos" al cargarse, pero solo lo usa
en su main para puntuar el audio con DNSMOS (el paquete real arrastra onnxruntime y modelos). El pipeline no lo usa."""
EOF
  cat > "$s/speechmos/dnsmos.py" <<'EOF'
"""STUB de speechmos.dnsmos (ver __init__.py)."""


def run(*a, **k):
    raise NotImplementedError('speechmos.dnsmos es un stub: ver instalar.sh')
EOF
  # st2_sleep.py (kit de voz, herramientas/voz) espera estar en bench/ junto a st2/: enlace, como en el Gauntlet 2
  ln -sf "$HERE/../voz/st2_sleep.py" "$SCRATCH/bench/st2_sleep.py"
  # prueba: el código de StyleTTS2 se importa con los stubs (sin cargar pesos)
  (cd "$ST2_DIR" && PATH="$ST2_PATHBIN:$PATH" PYTHONPATH="$ST2_STUBS" "$PY" -c \
    "import sys; sys.path.insert(0, '.'); import models, utils, inference, text_utils_gal; from Utils.ASR.AuxiliaryASR.phonemize import run_cotovia_with_phrase, clean_output; print('StyleTTS2 importa:', clean_output(run_cotovia_with_phrase('Boa noite.')))")
}

paso_whisper() {
  local orixe="$SCRATCH/tmp/whisper-hf"
  hecho whisper_hf || paso_whisper_hf
  rm -rf "$WHISPER_DIR.tmp"
  flock "$CPU_LOCK" "$SCRATCH/tts/venv/bin/ct2-transformers-converter" --model "$orixe" --output_dir "$WHISPER_DIR.tmp" \
    --quantization int8 --copy_files tokenizer.json preprocessor_config.json
  rm -rf "$WHISPER_DIR"; mv "$WHISPER_DIR.tmp" "$WHISPER_DIR"
  rm -rf "$orixe"     # el original (3,2 GB) ya no hace falta
}

paso_languagetool() {
  mkdir -p "$LTP_PATH"
  "$PY" - <<'EOF'
import language_tool_python as L
t = L.LanguageTool('gl-ES')
texto = 'Os rapaces foi á praia. Había moitas fortaleiras.'
m = t.check(texto)
print('LanguageTool gl-ES:', [(x.rule_id, texto[x.offset:x.offset + x.error_length]) for x in m])
assert any(x.rule_id.startswith('HUNSPELL') for x in m), 'falta hunspell galego'
t.close()
EOF
}

paso_cotovia_nova() {
  # OPCIONAL. Compila la Cotovía que trae Nos_StyleTTS2 (Utils/cotovia, la de proxectonos/cotovia) y usa sus datos de
  # lengua. A diferencia del .deb 0.5 de SourceForge, marca las vocales abiertas (pÓrta, tÉrra) y deja átonos los
  # monosílabos (a, de, que), como las transcripciones con las que se entrenó el modelo. Medido con
  # probas/comparar_cotovia.py en 122 frases del corpus: 0,9 % de caracteres distintos (Cotovía 0.5: 7,8 %).
  # NO es la de por defecto (la voz de la ronda 3 se midió con la 0.5); para usarla: ST2_PATHBIN=$COTOVIA_NOVA_PATHBIN.
  # cmake baja string_theory de GitHub y PCRE 8.45 de SourceForge y los compila; se compila solo el ejecutable cotovia.
  local faltan=() p b="$SCRATCH/cotovia_nova/build" saida
  for p in build-essential cmake bison flex libfl-dev libasound2-dev libexpat1-dev; do
    dpkg -s "$p" >/dev/null 2>&1 || faltan+=("$p")
  done
  if [ ${#faltan[@]} -gt 0 ]; then
    $SUDO apt-get update -qq
    DEBIAN_FRONTEND=noninteractive $SUDO apt-get install -y -qq --no-install-recommends "${faltan[@]}"
  fi
  mkdir -p "$b"
  (cd "$b" && flock "$CPU_LOCK" cmake -DCMAKE_BUILD_TYPE=Release "$ST2_DIR/Utils/cotovia/src" > "$LOGS/cotovia_nova_cmake.log" 2>&1 \
     && flock "$CPU_LOCK" make -j"$(nproc)" cotovia > "$LOGS/cotovia_nova_make.log" 2>&1) \
    || { tail -20 "$LOGS"/cotovia_nova_*.log; return 1; }
  mkdir -p "$COTOVIA_NOVA_PATHBIN"
  cat > "$COTOVIA_NOVA_PATHBIN/cotovia" <<EOF
#!/bin/sh
# Cotovía compilada desde Nos_StyleTTS2/Utils/cotovia (generado por instalar.sh cotovia_nova), con sus datos de lengua.
exec "$b/cotovia/cotovia" -D "$ST2_DIR/Utils/cotovia/data" "\$@"
EOF
  chmod +x "$COTOVIA_NOVA_PATHBIN/cotovia"
  saida="$(echo "A porta da terra." | "$COTOVIA_NOVA_PATHBIN/cotovia" -n -S -A0 2>/dev/null | iconv -f latin1 -t utf-8)"
  [[ "$saida" == *'pO^rta'* ]] || { echo "La Cotovía compilada no marca la vocal abierta: $saida"; return 1; }
}

paso_limpieza() {
  rm -rf "$SCRATCH/tmp"/* "$SCRATCH/insp"
  "$PY" -m pip cache purge >/dev/null 2>&1 || true
  resumen
}

paso_verificar() {
  "$PY" "$HERE/probas/proba_entorno.py"
}

resumen() {
  log "Tamaños en $SCRATCH:"
  du -sh "$SCRATCH/tts/venv" "$HF_HOME" "$ST2_DIR" "$WHISPER_DIR" "$SCRATCH/cotovia" "$SCRATCH/cotovia_nova" "$LTP_PATH" \
    "$REVISOR_DIR" "$REFS_DIR" 2>/dev/null || true
  du -sh "$SCRATCH" 2>/dev/null || true
  df -h "$SCRATCH" | tail -1
}

# ------------------------------------------------------------------------------------------------- ejecución
correr() {   # correr PASO: ejecuta paso_PASO si no tiene marca y la deja al acabar
  local p="$1" t0=$SECONDS
  if hecho "$p"; then log "== $p: ya hecho ($(cat "$MARCAS/$p.ok"))"; return 0; fi
  log "== $p: empieza"
  "paso_$p"
  [ "$p" = limpieza ] || [ "$p" = verificar ] || date -Is > "$MARCAS/$p.ok"
  log "== $p: hecho en $((SECONDS - t0)) s"
}

en_paralelo() {   # en_paralelo PASO...: lanza los pasos a la vez, cada uno con su registro, y espera a todos
  local pids=() p i fallos=0
  for p in "$@"; do
    ( correr "$p" ) > "$LOGS/instalar-$p.log" 2>&1 &
    pids+=("$!")
  done
  for i in "${!pids[@]}"; do
    p="${@:$((i + 1)):1}"
    if wait "${pids[$i]}"; then log "   $p: ok ($(tail -1 "$LOGS/instalar-$p.log"))"
    else log "   $p: FALLO; últimas líneas de $LOGS/instalar-$p.log:"; tail -15 "$LOGS/instalar-$p.log"; fallos=1; fi
  done
  return $fallos
}

T0=$SECONDS
log "SCRATCH=$SCRATCH  HF_HOME=$HF_HOME  (libre: $(df -h "$SCRATCH" | awk 'NR==2{print $4}'))"
if [ $# -gt 0 ]; then
  for p in "$@"; do correr "$p"; done
else
  for p in sistema cotovia venv_base; do correr "$p"; done
  en_paralelo paquetes st2 brais revisor sdxl florence nli clip whisper_hf
  for p in stubs whisper languagetool; do correr "$p"; done
  # opcional: en otro proceso para que un fallo no pare la instalación (la voz por defecto usa Cotovía 0.5)
  bash "$HERE/instalar.sh" cotovia_nova || log "aviso: cotovia_nova falló (opcional; ver $LOGS/cotovia_nova_*.log)"
  correr limpieza
fi
log "instalar.sh: terminado en $(((SECONDS - T0) / 60)) min $(((SECONDS - T0) % 60)) s"
