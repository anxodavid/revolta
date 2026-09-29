#!/usr/bin/env python
"""Proba de escala do ASR (etapa 8): ¿o WER e o tempo aguantan nun audio longo?

Concatena N veces a mestura final dun episodio xa producido (voz + choiva) e o seu guion, e pasa o
mesmo qa.asr() do pipeline sobre o audio longo. Mide tempo de parede, RTF e WER. Serve para
comprobar se Whisper alucina en audios de decenas de minutos (o Gauntlet 1 mediu WER 48-53 % sobre
6,6 min cun axuste distinto) antes de confiar no control A1 para episodios de 60 min.

    python probas/proba_asr_longo.py TRABALLO N SAIDA.json

TRABALLO: directorio de traballo do pipeline (frases.json, tempos_frases.json, mestura.wav, voz_linea.wav).
Só se mide a mestura (a pasada sobre a voz soa é igual de cara e non engade información de escala).
"""
import json, sys, time, os
from pathlib import Path
import numpy as np, soundfile as sf

HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import qa

W, N, out = Path(sys.argv[1]), int(sys.argv[2]), Path(sys.argv[3])
frases = json.loads((W / 'frases.json').read_text())
tempos = {int(k): v for k, v in json.loads((W / 'tempos_frases.json').read_text()).items()}
mix, sr = sf.read(W / 'mestura.wav')
D = len(mix) / sr
fr2, t2 = [], {}
for k in range(N):
    for f in frases:
        i = k * 1000 + f['i']
        fr2.append({**f, 'i': i}); t2[i] = (tempos[f['i']][0] + k * D, tempos[f['i']][1] + k * D)
longo = np.concatenate([mix] * N)
tmp = out.with_suffix('.wav'); sf.write(tmp, longo, sr)

import faster_whisper  # noqa: F401  (comproba o contorno antes de medir)
t0, c0 = time.time(), os.times()
# qa.asr pasa mestura e voz; para medir só a mestura, a "voz" é 1 s de silencio (custo desprezable)
sil = out.with_suffix('.sil.wav'); sf.write(sil, np.zeros(sr), sr)
r = qa.asr(str(tmp), str(sil), fr2, t2, os.environ.get('WHISPER_DIR'))
par = time.time() - t0
c = os.times(); cpu = (c.user - c0.user) + (c.system - c0.system)
res = {'n_copias': N, 'dur_audio_s': round(N * D, 1), 'parede_s': round(par, 1),
       'rtf': round(par / (N * D), 3), 'nota': 'inclúe a carga do modelo (unha vez)',
       'cpu_s': round(cpu, 1),
       'wer_mestura': r['mestura']['wer'], 'sub': r['mestura']['sub'], 'del': r['mestura']['del'],
       'ins': r['mestura']['ins'], 'palabras_ref': r['mestura']['palabras_ref'],
       'sincronia': r['mestura']['sincronia'],
       'frases_wer_mais_0_5': len(r['mestura']['frases_wer_mais_0_5']),
       'hipotese_inicio': r['mestura']['hipotese'][:400], 'hipotese_final': r['mestura']['hipotese'][-400:]}
out.write_text(json.dumps(res, ensure_ascii=False, indent=1))
tmp.unlink(); sil.unlink()
print(json.dumps({k: v for k, v in res.items() if not k.startswith('hipotese')}, ensure_ascii=False))
