#!/usr/bin/env python
"""Ordena as 40 referencias polo que fan na voz sintética (datos/barrido-refs.json) e xunta as medidas das
grabacións humanas (datos/referencias-humanas.json). Criterios (feitos por Claude, axente de voz):

- VIVA: máis arousal e máis desviación da F0 na voz sintética, e algo de axilidade (sílabas/s), sen ser "gritona":
  penalízase a F0 mediana ou o alpha ratio (brillo, esforzo) moi por riba do resto (z > 1,5) e as preguntas (a
  entoación interrogativa pásase ás frases afirmativas).
- CALMA: menos arousal, menos desviación da F0, máis lenta e máis suave (alpha ratio baixo), sen voz cascada
  (penalízase HNR baixo, z < -1,5, e F0 < 75 Hz).

    python analizar_barrido.py [datos/barrido-refs.json]
"""
import json, os, sys
import numpy as np

AQUI = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(AQUI, '..', 'datos')
b = json.load(open(sys.argv[1] if len(sys.argv) > 1 else os.path.join(D, 'barrido-refs.json')))['resultados']
h = {r['ficheiro'].replace('brais-norm-', '').replace('.wav', ''): r for r in json.load(open(os.path.join(D, 'referencias-humanas.json')))}
z = lambda k: (lambda v: (v - v.mean()) / (v.std() + 1e-9))(np.array([r[k] for r in b], dtype=float))
Z = {k: z(k) for k in ('arousal', 'f0_sd_st', 'sil_s', 'f0_mediana_hz', 'alpha_ratio_db', 'hnr_db', 'f0_baixo_75')}
preg = np.array([h[r['ref']]['categoria'] == 'pregunta' for r in b])
viva = Z['arousal'] + Z['f0_sd_st'] + 0.5 * Z['sil_s'] - 2 * (Z['f0_mediana_hz'] > 1.5) - 2 * (Z['alpha_ratio_db'] > 1.5) - 1.0 * preg
calma = -Z['arousal'] - Z['f0_sd_st'] - Z['sil_s'] - 0.5 * Z['alpha_ratio_db'] - 2 * (Z['hnr_db'] < -1.5) - 2 * (Z['f0_baixo_75'] > 1.5)
cols = ('arousal', 'f0_sd_st', 'f0_rango_st', 'sil_s', 'f0_mediana_hz', 'alpha_ratio_db', 'hnr_db', 'jitter_pct', 'wer')


def fila(i, sc):
    r = b[i]; hu = h[r['ref']]
    return (f"| {r['ref']} | {hu['categoria']} | {sc[i]:+.2f} | " + ' | '.join(str(r.get(k)) for k in cols) +
            f" | {hu['arousal']:.3f} | {hu['sil_s']} | {hu['texto'][:60]} |")


print('Medias da voz sintética coas 40 referencias:',
      {k: round(float(np.mean([r[k] for r in b])), 3) for k in cols if b[0].get(k) is not None})
print('Rangos:', {k: (min(r[k] for r in b), max(r[k] for r in b)) for k in ('arousal', 'f0_sd_st', 'sil_s')})
cab = '| ref | categoría | puntuación | ' + ' | '.join(cols) + ' | arousal humano | sil/s humano | texto |'
for nome, sc in (('VIVA', viva), ('CALMA', calma)):
    print(f'\n{nome}\n' + cab + '\n' + '|---' * (len(cols) + 6) + '|')
    for i in np.argsort(-sc)[:8]:
        print(fila(i, sc))
# correlación entre o humano e o sintético (canto transmite a referencia)
for k in ('arousal', 'f0_sd_st', 'sil_s'):
    x = [h[r['ref']][k] for r in b]; y = [r[k] for r in b]
    print(f'correlación humano-sintético {k}: {np.corrcoef(x, y)[0, 1]:.2f}')
