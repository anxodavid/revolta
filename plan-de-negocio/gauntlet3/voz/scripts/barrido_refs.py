#!/usr/bin/env python
"""Barrido de referencias de estilo (peza VOZ, Gauntlet 3): a pasaxe fixa (textos.PASAXE) coa voz sintética usando
como referencia cada unha das 40 grabacións de Brais (ou vectores medios de varias), cos parámetros neutros.

    source herramientas/pipeline/entorno.sh
    PATH=$COTOVIA_NOVA_PATHBIN:$PATH PYTHONPATH=$ST2_STUBS:$SCRATCH/voz/pylib flock "$CPU_LOCK" \
        $PY plan-de-negocio/gauntlet3/voz/scripts/barrido_refs.py SAIDA.json [--refs a.wav,b.wav:c.wav ...] [--escala 1.0]

--refs: lista separada por comas; cada elemento pode ser un vector medio de varias grabacións unidas con ':'.
Mide por referencia: sílabas/s, F0 (Hz, sd e rango en semitons), enerxía, HNR/jitter/shimmer, alpha ratio, arousal
(audeering, só avaliación interna) e, con --wer, WER (Whisper galego) frase a frase. Todo automático.
"""
import argparse, json, os, sys, time
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI); sys.path.insert(0, '/home/user/revolta/herramientas/pipeline')
import csv
import numpy as np, soundfile as sf
import textos, acustica as A

ap = argparse.ArgumentParser()
ap.add_argument('saida'); ap.add_argument('--refs', default=None); ap.add_argument('--escala', type=float, default=1.0)
ap.add_argument('--beta', type=float, default=None); ap.add_argument('--alpha', type=float, default=None)
ap.add_argument('--etiqueta', default='barrido')
ap.add_argument('--wer', action='store_true', help='WER frase a frase (lento: ~6 s por frase)')
a = ap.parse_args(); a.saida = os.path.abspath(a.saida)
S = os.environ['SCRATCH']; RD = os.environ['REFS_DIR']
OUT = os.path.join(S, 'voz', a.etiqueta); os.makedirs(OUT, exist_ok=True)
if a.refs:
    refs = a.refs.split(',')
else:
    refs = [r['ficheiro'] for r in csv.DictReader(open(os.path.join(RD, 'refs.tsv'), encoding='utf-8'), delimiter='\t')]
absol = lambda r: ':'.join(p if os.path.isabs(p) else os.path.join(RD, p) for p in r.split(':'))
nome = lambda r: '+'.join(os.path.basename(p).replace('brais-norm-', '').replace('.wav', '') for p in r.split(':'))
kw = {k: v for k, v in (('alpha', a.alpha), ('beta', a.beta)) if v is not None}

import voz_st2 as V
V.cargar()
t0 = time.time()
for r in refs:
    d = os.path.join(OUT, nome(r)); os.makedirs(d, exist_ok=True)
    for k, t in enumerate(textos.PASAXE):
        p = os.path.join(d, f'{k}.wav')
        if not os.path.exists(p):
            w, _ = V.infer(t, escala=a.escala, ref=absol(r), ref_calma='', **kw)
            sf.write(p, w, 24000)
    print('tts', nome(r), round(time.time() - t0), flush=True)
V.M.clear()
import gc; gc.collect()

import modelos
em = modelos.Emocion(); asr = modelos.ASR() if a.wer else None
res = []
for r in refs:
    d = os.path.join(OUT, nome(r))
    fr = []
    for k, t in enumerate(textos.PASAXE):
        p = os.path.join(d, f'{k}.wav')
        m = A.medir(p, t); m.update(em.medir(p)); fr.append(m)
    wr = None
    if asr:     # WER frase a frase (sen o risco de que Whisper salte tramos nun audio longo)
        ws = [asr.wer(os.path.join(d, f'{k}.wav'), t) for k, t in enumerate(textos.PASAXE)]
        wr = {'wer': round(sum(w['erros'] for w in ws) / sum(w['palabras_ref'] for w in ws), 4),
              'hipotese': ' | '.join(w['hipotese'] for w in ws)}
    media = lambda x: round(float(np.mean([f[x] for f in fr if f.get(x) is not None])), 3)
    x = {'ref': nome(r), 'ficheiros': r, 'wer': wr and wr['wer'], 'hipotese': wr and wr['hipotese'],
         **{k: media(k) for k in ('sil_s', 'sil_s_articulacion', 'f0_mediana_hz', 'f0_media_st', 'f0_sd_st', 'f0_rango_st',
                                  'dinamica_db', 'rms_db', 'lufs', 'hnr_db', 'jitter_pct', 'shimmer_pct', 'alpha_ratio_db',
                                  'arousal', 'dominancia', 'valencia', 'f0_baixo_75', 'pico')},
         'dur_total_s': round(sum(f['dur_s'] for f in fr), 2), 'por_frase': fr}
    res.append(x)
    print(x['ref'], {k: x[k] for k in ('sil_s', 'f0_mediana_hz', 'f0_sd_st', 'f0_rango_st', 'arousal', 'wer', 'hnr_db')}, flush=True)
json.dump({'parametros': {'escala': a.escala, **kw}, 'resultados': res}, open(a.saida, 'w'), ensure_ascii=False, indent=1)
