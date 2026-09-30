#!/usr/bin/env python
"""Táboa por candidata e punto da curva (saída de puntos.py) e comprobación de monotonía (peza VOZ, Gauntlet 3).

    python analizar_curva.py datos/curva-rondaN.json [--md]

Obxectivo: arousal, rango da F0 e velocidade baixando de forma monótona do gancho (palabra 0) ao final (3600), con WER
<= 0,06 en todos os puntos e sen artefactos (HNR, jitter, F0 < 75 Hz, pico).
"""
import json, sys

COLS = [('pal', 'palabra'), ('palabras_min', 'pal/min (con pausas)'), ('sil_s', 'síl/s'), ('f0_media_hz', 'F0 media (Hz)'),
        ('f0_sd_st', 'F0 sd (st)'), ('f0_rango_st', 'F0 p5-p95 (st)'), ('lufs_pasaxe', 'LUFS'), ('dinamica_db', 'dinámica (dB)'),
        ('arousal', 'arousal'), ('valencia', 'valencia'), ('wer', 'WER'), ('hnr_db', 'HNR (dB)'), ('jitter_pct', 'jitter (%)'),
        ('alpha_ratio_db', 'alpha ratio (dB)'), ('f0_baixo_75', 'F0<75'), ('pico_max', 'pico')]
BAIXAN = ('arousal', 'f0_sd_st', 'f0_rango_st', 'sil_s', 'palabras_min')


def monotona(v):
    return all(b < a for a, b in zip(v, v[1:]))


def main():
    d = json.load(open(sys.argv[1]))
    md = '--md' in sys.argv
    for ca in d.get('candidatas', [d]):
        rs = ca['resultados']
        print(f"\n### {ca.get('nome', '')}  (viva: {str(ca.get('ref_wav', '')).split('/')[-1]}, calma: "
              f"{str(ca.get('ref_wav_calmo', '')).split('/')[-1]})")
        if md:
            print('| ' + ' | '.join(n for _, n in COLS) + ' |')
            print('|' + '---|' * len(COLS))
        for r in rs:
            vals = [str(r.get(k)) for k, _ in COLS]
            print(('| ' + ' | '.join(vals) + ' |') if md else '  '.join(f'{k}={v}' for (k, _), v in zip(COLS, vals)))
        print('parámetros:', [r['parametros'] for r in rs] if not md else '')
        mon = {k: monotona([r[k] for r in rs]) for k in BAIXAN if all(r.get(k) is not None for r in rs)}
        caida = {k: round(rs[0][k] - rs[-1][k], 3) for k in BAIXAN if all(r.get(k) is not None for r in rs)}
        wer_ok = all(r['wer'] is not None and r['wer'] <= 0.06 for r in rs) if all(r.get('wer') is not None for r in rs) else None
        print('monótona (baixa en cada paso):', mon, '| caída gancho→final:', caida, '| WER <= 0,06 en todos:', wer_ok)


if __name__ == '__main__':
    main()
