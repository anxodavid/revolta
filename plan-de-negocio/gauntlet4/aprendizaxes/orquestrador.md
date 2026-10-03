# Aprendizaxes do orquestrador (Gauntlet 4)

- **Non aniñar o candado de CPU.** `instalar.sh verificar` xa o colle en cada etapa (`probas/proba_entorno.py`,
  `candado()`). Envolvelo noutro `flock "$CPU_LOCK"` (02-10-2026, 22:51 UTC) deixou o candado nas mans do `flock`
  de fóra mentres o neto agardaba polo mesmo candado: interbloqueo de ≈ 30 min con cinco traballos doutras pezas na
  cola (detectárono os axentes de guion e de imaxe en `/proc/locks`). Arranxo: matar a árbore (por PID) e lanzar a
  verificación sen envoltorio. A primeira verificación (22:59 UTC) morrera por OOM ao coincidir a súa proba de imaxe
  (10,5 GB, dentro do candado) cunha proba de LTX-Video (8 GB) que, polo tanto, corría fóra do candado.
- **`flock` non é unha cola ordenada** e os experimentos de vídeo collen a CPU 10-20 min cada vez: unha porta de texto
  do camiño crítico podía agardar unha hora. `herramientas/gauntlet/candado.sh --prioridade` fai que os traballos
  normais cedan a vez a un prioritario que agarda (proba: o prioritario entrou xusto ao rematar o traballo en curso,
  por diante dun normal que xa agardaba).
- **Disco:** a sesión ten ≈ 39 GB; o contorno do pipeline colle ≈ 16 GB e o primeiro modelo de vídeo (LTX-Video 2B
  destilado + T5-XXL en fp8) ≈ 11 GB. Aos 25 min de empezar o Gauntlet o disco xa estaba ao 95 %: repartir o orzamento
  de disco entre pezas antes de lanzalas.
- **PR abertos doutras sesións:** antes de lanzar axentes que tocan o pipeline, fusionar os PR pendentes que tocan os
  mesmos ficheiros (o PR #5 cambiaba `revisor.py`, `imaxes.py`, `son.py` e `longo.py`); con axentes traballando, a
  fusión faise nunha copia aparte (`git worktree`) e despois trese á rama cando a árbore de traballo está limpa.
- **Cota:** tres axentes en paralelo máis o orquestrador esgotaron o límite de uso da sesión en ≈ 1 h (22:34 →
  ≈ 23:30 UTC), e a cota non volveu ata as 03:10. Para avanzar máis por cada xanela de cota: menos axentes á vez, que non
  relean ficheiros grandes, que agarden os traballos longos cunha soa espera en segundo plano (sen consultas
  frecuentes) e axentes novos e curtos para os críticos. A rutina horaria retomou o traballo ao volver a cota.
