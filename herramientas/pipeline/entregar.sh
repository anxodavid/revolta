#!/bin/bash
# entregar.sh: entrega dun vídeo longo de longo.py.
#
#   bash herramientas/pipeline/entregar.sh DIR_SAIDA     # DIR_SAIDA = carpeta con video.mp4 (p. ej. plan-de-negocio/gauntlet3/video)
#
# 1. Comproba que video.mp4 se decodifica enteiro e que ningún proceso do pipeline segue a escribir.
# 2. Parte o mestre en anacos < 50 MB SEN recodificar (DIR_SAIDA/mestre/parteNN.mp4): cada anaco vese só e
#    reúnense sen perda con  ffmpeg -f concat -safe 0 -i partes.txt -c copy video.mp4  (proba feita aquí mesmo).
# 3. Copia 720p en HLS (segmentos de 30 s) para a páxina de visionado, en $SCRATCH/entrega/hls (non vai ao repo).
#    Cada versión dunha páxina admite 256 MB en total: con CRF 26 e teito de 800 kbit/s, 31 min quedan en ~150-190 MB.
# 4. Mostra do gancho (primeiros 3,5 min, 720p, < 30 MB) para mandala ao chat: $SCRATCH/entrega/mostra-gancho.mp4.
# O traballo pesado vai baixo o candado de CPU (flock $CPU_LOCK).
set -euo pipefail
AQUI="$(cd "$(dirname "$0")" && pwd)"
source "$AQUI/entorno.sh"
D="$(realpath "$1")"; V="${VIDEO:-$D/video.mp4}"   # longo.py deixa o mestre en TRABALLO/video.mp4: VIDEO=... para usalo de alí
FF="$("$PY" -c 'import imageio_ffmpeg; print(imageio_ffmpeg.get_ffmpeg_exe())')"
E="$SCRATCH/entrega"; H="$E/hls"; M="$D/mestre"
SEG=${SEG:-200}            # segundos por anaco do mestre (1,5 Mbit/s * 200 s ~ 38 MB; o corte vai ao keyframe seguinte)
MAXMB=${MAXMB:-49}

dur() { { "$FF" -hide_banner -i "$1" 2>&1 || true; } | sed -n 's/.*Duration: \([0-9:.]*\).*/\1/p' | awk -F: '{print $1*3600+$2*60+$3}'; }
valida() { local err; err="$("$FF" -v error -i "$1" -f null - 2>&1 | head -5)"; [ -z "$err" ] || { echo "ERRO decodificando $1: $err"; exit 1; }; }

[ -f "$V" ] || { echo "non hai $V"; exit 1; }
if pgrep -f "longo.py|montaxe" > /dev/null; then echo "AVISO: hai procesos do pipeline en marcha"; pgrep -af "longo.py|montaxe"; exit 1; fi
echo "== 1 validar mestre ($(du -m "$V" | cut -f1) MB, $(dur "$V") s)"
flock "$CPU_LOCK" bash -c "$(declare -f valida); FF='$FF'; valida '$V'"

echo "== 2 partir o mestre en anacos de ~${SEG} s sen recodificar"
rm -rf "$M"; mkdir -p "$M" "$E"
flock "$CPU_LOCK" "$FF" -v error -i "$V" -map 0 -c copy -f segment -segment_time "$SEG" -reset_timestamps 1 \
  -segment_format mp4 -segment_format_options movflags=+faststart "$M/parte%02d.mp4"
( cd "$M" && for p in parte*.mp4; do echo "file '$p'"; done > partes.txt )
for p in "$M"/parte*.mp4; do
  mb=$(du -m "$p" | cut -f1); [ "$mb" -le "$MAXMB" ] || { echo "ERRO: $p ten $mb MB (> $MAXMB)"; exit 1; }
done
( cd "$M" && flock "$CPU_LOCK" "$FF" -v error -y -f concat -safe 0 -i partes.txt -map 0 -c copy "$E/reunido.mp4" )
flock "$CPU_LOCK" bash -c "$(declare -f valida); FF='$FF'; valida '$E/reunido.mp4'"
d0=$(dur "$V"); d1=$(dur "$E/reunido.mp4")
awk -v a="$d0" -v b="$d1" 'BEGIN { if ((a - b) ^ 2 > 0.04) { print "ERRO: o reunido dura " b " s e o mestre " a " s"; exit 1 } }'
echo "   $(ls "$M"/parte*.mp4 | wc -l) anacos, $(du -cm "$M"/parte*.mp4 | tail -1 | cut -f1) MB; reunidos duran $d1 s (mestre $d0 s)"
rm -f "$E/reunido.mp4"

echo "== 3 copia 720p en HLS para a páxina de visionado"
rm -rf "$H"; mkdir -p "$H"
flock "$CPU_LOCK" "$FF" -v error -i "$V" -map 0:v -map 0:a -vf scale=1280:720:flags=lanczos -c:v libx264 -preset medium \
  -crf "${CRF720:-26}" -maxrate "${MAX720:-800k}" -bufsize 1600k -g 50 -keyint_min 50 -sc_threshold 0 -pix_fmt yuv420p \
  -c:a aac -b:a 96k -ac 2 -ar 48000 -f hls -hls_time 30 -hls_playlist_type vod -hls_segment_filename "$H/s%03d.ts" "$H/index.m3u8"
if [ -f "$D/subtitulos.gl.srt" ]; then
  { echo WEBVTT; echo; sed 's/\r$//; s/\([0-9][0-9]:[0-9][0-9]:[0-9][0-9]\),\([0-9][0-9][0-9]\)/\1.\2/g' "$D/subtitulos.gl.srt"; } > "$H/subtitulos.gl.vtt"
fi
echo "   $(ls "$H"/s*.ts | wc -l) segmentos, $(du -cm "$H"/s*.ts | tail -1 | cut -f1) MB, o maior $(du -m "$H"/s*.ts | sort -n | tail -1 | cut -f1) MB"

echo "== 4 mostra do gancho (3,5 min, 720p)"
flock "$CPU_LOCK" "$FF" -v error -y -i "$V" -t 210 -map 0:v -map 0:a -vf scale=1280:720:flags=lanczos -c:v libx264 \
  -preset medium -crf 24 -maxrate 1100k -bufsize 2200k -pix_fmt yuv420p -c:a aac -b:a 128k -movflags +faststart \
  "$E/mostra-gancho.tmp.mp4"
mv "$E/mostra-gancho.tmp.mp4" "$E/mostra-gancho.mp4"
echo "   $(du -m "$E/mostra-gancho.mp4" | cut -f1) MB"
echo "feito"
