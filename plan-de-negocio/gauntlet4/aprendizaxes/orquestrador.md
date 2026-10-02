# Aprendizaxes do orquestrador (Gauntlet 4)

- **`instalar.sh verificar` non colle o candado de CPU** (liña 364: `"$PY" probas/proba_entorno.py` directo). O
  02-10-2026 ás 22:59 UTC a súa proba de imaxe (SDXL, 10,5 GB) coincidiu coa primeira proba de LTX-Video da peza
  MOVEMENTO (8 GB) e o OOM do cgroup (13,36 GiB) matou a verificación. Lanzala sempre como
  `flock "$CPU_LOCK" bash herramientas/pipeline/instalar.sh verificar`.
- **Disco:** a sesión ten ≈ 39 GB; o contorno do pipeline colle ≈ 16 GB e o primeiro modelo de vídeo (LTX-Video 2B
  destilado + T5-XXL en fp8) ≈ 11 GB. Aos 25 min de empezar o Gauntlet o disco xa estaba ao 95 %: repartir o orzamento
  de disco entre pezas antes de lanzalas.
- **PR abertos doutras sesións:** antes de lanzar axentes que tocan o pipeline, fusionar os PR pendentes que tocan os
  mesmos ficheiros (o PR #5 cambiaba `revisor.py`, `imaxes.py`, `son.py` e `longo.py`); con axentes traballando, a
  fusión faise nunha copia aparte (`git worktree`) e despois trese á rama cando a árbore de traballo está limpa.
