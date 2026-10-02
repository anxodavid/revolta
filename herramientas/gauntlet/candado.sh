#!/usr/bin/env bash
# candado.sh: o candado común de CPU ($CPU_LOCK) con prioridade cooperativa para o camiño crítico do Gauntlet.
#
#   candado.sh orde args...                # traballo normal (experimentos longos de imaxe ou vídeo)
#   candado.sh --prioridade orde args...   # camiño crítico (portas do guion, voz, probas curtas que agardan outros)
#
# Por que: `flock` non é unha cola ordenada (esperta a calquera dos que agardan) e os experimentos de vídeo collen a CPU
# 10-20 min cada vez, así que unha porta de texto de 3 min podía agardar unha hora. Cun prioritario agardando, os
# traballos normais que collen o candado devólveno de contado e volven tentalo aos 15 s; o prioritario entra en canto
# remata o que estaba correndo (non se interrompe ningún traballo xa empezado).
#
# Mecánica: o prioritario colle primeiro "$CPU_LOCK.prio" e despois "$CPU_LOCK". Un normal, despois de coller
# "$CPU_LOCK", proba sen esperar "$CPU_LOCK.prio": se o ten alguén, solta "$CPU_LOCK" e reinténtao. A orde herda o
# descritor do candado (como con `flock ficheiro orde`). Non aniñar: se a orde xa colle o candado por dentro (p. ex.
# `instalar.sh verificar`, que o colle en cada etapa), lanzala SEN este envoltorio ou haberá un interbloqueo.
set -u
L="${CPU_LOCK:?falta CPU_LOCK: source herramientas/pipeline/entorno.sh}"
P="$L.prio"
touch "$L" "$P"
if [ "${1:-}" = "--prioridade" ]; then
  shift
  exec flock "$P" flock "$L" "$@"
fi
while true; do
  exec 9>>"$L"
  flock 9
  if flock -n "$P" true; then
    break
  fi
  flock -u 9
  exec 9>&-
  sleep 15
done
"$@"
rc=$?
flock -u 9
exit $rc
