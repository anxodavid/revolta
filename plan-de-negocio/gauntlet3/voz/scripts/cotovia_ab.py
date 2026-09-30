#!/usr/bin/env python
"""A/B de Cotovía para a voz (peza VOZ, Gauntlet 3): 0.5 do .deb (ST2_PATHBIN) fronte á compilada de Nós
(COTOVIA_NOVA_PATHBIN).

    source herramientas/pipeline/entorno.sh
    PYTHONPATH=$ST2_STUBS:$SCRATCH/voz/pylib flock "$CPU_LOCK" $PY plan-de-negocio/gauntlet3/voz/scripts/cotovia_ab.py SAIDA.json

Frases: as 21 de test do corpus Nos_Brais-GL (non usadas no adestramento; teñen a transcrición fonética da Cotovía
coa que se adestrou o modelo) e 12 propias con vogais abertas/pechadas, monosílabos e nomes propios (textos.py).
Por frase e Cotovía: fonemas (e diferenza en caracteres coa transcrición do corpus, normalizada como
probas/comparar_cotovia.py), voz con voz_st2.infer (REF_WAV, escala 1,1, dúas sementes) e WER co Whisper galego.
Todo automático; ninguén escoitou os audios.
"""
import csv, json, os, re, sys, time
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI); sys.path.insert(0, '/home/user/revolta/herramientas/pipeline')
import numpy as np, soundfile as sf
import textos

S = os.environ['SCRATCH']; OUT = os.path.join(S, 'voz', 'cotovia'); os.makedirs(OUT, exist_ok=True)
COT = {'0.5': os.environ['ST2_PATHBIN'], 'nova': os.environ['COTOVIA_NOVA_PATHBIN']}
PATH0 = os.environ['PATH']
SEMENTES = (11, 22)

refs = os.environ['REFS_DIR']
test = list(csv.DictReader(open(os.path.join(refs, 'brais_test.csv'), encoding='utf-8'), delimiter='\t'))
col = next(k for k in test[0] if k.strip() == 'phonetic_transcription')
frases = [{'texto': f['transcripts'].strip(), 'corpus': f[col].strip(), 'orixe': 'test'} for f in test]
frases += [{'texto': t, 'corpus': None, 'orixe': 'propia'} for t in textos.COTOVIA_PROPIAS]


def lev(a, b):
    d = list(range(len(b) + 1))
    for i, x in enumerate(a, 1):
        p, d[0] = d[0], i
        for j, y in enumerate(b, 1):
            p, d[j] = d[j], min(d[j] + 1, d[j - 1] + 1, p + (x != y))
    return d[-1]


import voz_st2 as V
V.cargar()
from Utils.ASR.AuxiliaryASR.phonemize import normalize_word


def nrm(t, corpus=False):
    """Como probas/comparar_cotovia.py: sen ¿ ¡; no corpus, dígrafos pasados por normalize_word (rr -> R...)."""
    t = re.sub(r'[¿¡]\s*', '', t)
    if corpus:
        t = ' '.join(normalize_word(w) for w in t.split())
    return re.sub(r'\s+', ' ', t).strip()


t0 = time.time()
for k, f in enumerate(frases):
    for c, pb in COT.items():
        os.environ['PATH'] = f'{pb}:{PATH0}'
        f.setdefault('fonemas', {})[c] = V.M['fonemas'](f['texto'])
        if f['corpus']:
            f.setdefault('dif_corpus', {})[c] = lev(nrm(f['corpus'], True), nrm(f['fonemas'][c]))
        for s in SEMENTES:
            p = os.path.join(OUT, f'{c}_{s}_{k:02d}.wav')
            if not os.path.exists(p):
                w, _ = V.infer(f['texto'], escala=1.1, semente=s * 1000 + k)
                sf.write(p, w, 24000)
    print(k, round(time.time() - t0), f['texto'][:50], f.get('dif_corpus'), flush=True)
os.environ['PATH'] = PATH0
V.M.clear()
import gc; gc.collect()

import modelos
asr = modelos.ASR()
for k, f in enumerate(frases):
    f['asr'] = {}
    for c in COT:
        for s in SEMENTES:
            f['asr'][f'{c}_{s}'] = asr.wer(os.path.join(OUT, f'{c}_{s}_{k:02d}.wav'), f['texto'])
    print(k, {x: v['wer'] for x, v in f['asr'].items()}, flush=True)

res = {}
for c in COT:
    for grupo in ('test', 'propia', 'todas'):
        fs = [f for f in frases if grupo == 'todas' or f['orixe'] == grupo]
        err = sum(f['asr'][f'{c}_{s}']['erros'] for f in fs for s in SEMENTES)
        pal = sum(f['asr'][f'{c}_{s}']['palabras_ref'] for f in fs for s in SEMENTES)
        res.setdefault(c, {})[f'wer_{grupo}'] = round(err / pal, 4)
        res[c][f'erros_{grupo}'] = err
    ft = [f for f in frases if f['corpus']]
    res[c]['caracteres_distintos_corpus_pct'] = round(100 * sum(f['dif_corpus'][c] for f in ft) /
                                                      sum(len(nrm(f['corpus'], True)) for f in ft), 2)
    res[c]['frases_identicas_corpus'] = sum(f['dif_corpus'][c] == 0 for f in ft)
    res[c]['vogais_abertas_EO'] = sum(len(re.findall('[ÉÓ]', f['fonemas'][c])) for f in frases)
res['vogais_abertas_EO_corpus_test'] = sum(len(re.findall('[ÉÓ]', f['corpus'])) for f in frases if f['corpus'])
res['frases'] = len(frases); res['sementes'] = SEMENTES
json.dump({'resumo': res, 'frases': frases}, open(sys.argv[1], 'w'), ensure_ascii=False, indent=1)
print(json.dumps(res, ensure_ascii=False, indent=1))
