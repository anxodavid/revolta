#!/usr/bin/env python
"""¿Da la Cotovía instalada los mismos fonemas con los que se entrenó Nos_StyleTTS2-Brais-GL?

Compara, frase a frase, la transcripción de la Cotovía que haya en el PATH (pasada por clean_output, como hace
voz_st2.py) con la columna phonetic_transcription del corpus Nos_Brais-GL (la que vio el modelo). Muestra fija: las 21
frases de test y 1 de cada 160 de train (122 frases). Necesita los CSV que baja `instalar.sh brais` ($REFS_DIR).

    source herramientas/pipeline/entorno.sh
    PATH=$ST2_PATHBIN:$PATH $PY herramientas/pipeline/probas/comparar_cotovia.py            # Cotovía 0.5 (.deb)
    PATH=$COTOVIA_NOVA_PATHBIN:$PATH $PY herramientas/pipeline/probas/comparar_cotovia.py   # compilada (cotovia_nova)

"bruto": cadenas tal cual. "normalizado": sin los signos de apertura ¿ ¡ (el corpus no los tiene) y con los dígrafos
del corpus pasados por normalize_word (rr -> R, como hace clean_output), para contar solo diferencias de fonemas.
"""
import csv, json, os, re, sys
sys.path.insert(0, os.environ['ST2_DIR'])
from Utils.ASR.AuxiliaryASR.phonemize import run_cotovia_with_phrase, clean_output, normalize_word


def lev(a, b):
    d = list(range(len(b) + 1))
    for i, x in enumerate(a, 1):
        p, d[0] = d[0], i
        for j, y in enumerate(b, 1):
            p, d[j] = d[j], min(d[j] + 1, d[j - 1] + 1, p + (x != y))
    return d[-1]


def norm(t, corpus=False):
    t = re.sub(r'[¿¡]\s*', '', t)
    if corpus:
        t = ' '.join(normalize_word(w) for w in t.split())
    return re.sub(r'\s+', ' ', t).strip()


refs = os.environ['REFS_DIR']
filas = []
for c in ('brais_test.csv', 'brais_train.csv'):
    filas += list(csv.DictReader(open(os.path.join(refs, c), encoding='utf-8'), delimiter='\t'))
col = next(k for k in filas[0] if k.strip() == 'phonetic_transcription')
test = [f for f in filas if '/audio/test/' in f['audio']]
mostra = test + [f for f in filas if '/audio/test/' not in f['audio']][::160]
res = {k: {'identicas': 0, 'erros': 0, 'caracteres': 0} for k in ('bruto', 'normalizado')}
ab = {'corpus': 0, 'instalada': 0}
difs = []
for f in mostra:
    ref, hyp = f[col].strip(), clean_output(run_cotovia_with_phrase(f['transcripts'].strip()))
    for k, (r, h) in {'bruto': (re.sub(r'\s+', ' ', ref), re.sub(r'\s+', ' ', hyp)),
                      'normalizado': (norm(ref, True), norm(hyp))}.items():
        e = lev(r, h)
        res[k]['identicas'] += r == h; res[k]['erros'] += e; res[k]['caracteres'] += len(r)
        if k == 'normalizado' and e and len(difs) < 8:
            difs.append({'texto': f['transcripts'], 'corpus': r, 'instalada': h})
    ab['corpus'] += len(re.findall('[ÉÓ]', ref)); ab['instalada'] += len(re.findall('[ÉÓ]', hyp))
out = {'frases': len(mostra),
       **{k: {'identicas': v['identicas'], 'caracteres_distintos_pct': round(100 * v['erros'] / v['caracteres'], 2)}
          for k, v in res.items()},
       'vogais_abertas_tonicas_EO': ab, 'exemplos_diferenzas_normalizadas': difs}
print(json.dumps(out, ensure_ascii=False, indent=1))
