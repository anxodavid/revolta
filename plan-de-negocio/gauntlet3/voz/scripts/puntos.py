#!/usr/bin/env python
"""A pasaxe fixa (textos.PASAXE_MEIGAS, do tema elixido) en 5 puntos da curva do embude, con medidas por punto (peza VOZ, Gauntlet 3).

    source herramientas/pipeline/entorno.sh
    PATH=$COTOVIA_NOVA_PATHBIN:$PATH PYTHONPATH=$ST2_STUBS:$SCRATCH/voz/pylib flock "$CPU_LOCK" \
        $PY plan-de-negocio/gauntlet3/voz/scripts/puntos.py SAIDA.json [--curva CANDIDATA.json] [--etiqueta nome]

Puntos: curva.en(pal, 3600) con pal = 0, 280, 950, 1800 e 3600 (gancho, fin do gancho, fin da transición, metade,
final). A curva é a de herramientas/pipeline/curva.py, ou esa mesma cos valores que traia cada --curva
({clave: [5 valores]}, tamén claves novas como beta ou embedding_scale; _ref_wav e _ref_wav_calmo cambian as
referencias). Varias candidatas nunha soa execución: unha soa carga dos modelos e unha soa vez o candado. As frases van xuntas coas pausas de
longo.py (pausa_frase + axuste pola lonxitude da seguinte; pausa_parrafo antes da frase textos.PARRAFO) e coa
ganancia_db.
REF_WAV (viva) e REF_WAV_CALMO (calma) veñen do contorno.

Medidas por punto: palabras/min (pausas incluídas, como o QA de longo.py), sílabas/s da fala, F0 (media en Hz,
desviación e rango p5-p95 en semitons), enerxía (LUFS da pasaxe tras a ganancia e dinámica), HNR, jitter,
shimmer, alpha ratio, fracción de F0 < 75 Hz, pico, arousal/dominancia/valencia (audeering, só avaliación interna) e
WER (Whisper galego de Nós) frase a frase (e, con --wer-pasaxe, da pasaxe enteira). Todo automático: ninguén
escoitou os audios.
"""
import argparse, copy, json, os, sys, time
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI); sys.path.insert(0, '/home/user/revolta/herramientas/pipeline')
import numpy as np, soundfile as sf
import textos, acustica as A
import curva

PUNTOS = (0, 280, 950, 1800, 3600)
TOTAL = 3600
VOZ_KW = ('escala', 'estilo', 'f0_media', 'f0_rango', 'enerxia', 'alpha', 'beta', 'embedding_scale', 'pasos')
SR = 24000


def curva_candidata(path):
    base = copy.deepcopy(curva.CURVA)
    if path:
        base.update(json.load(open(path)))
    return base


def en(pal, cv):
    vello = curva.CURVA
    try:
        curva.CURVA = {k: v for k, v in cv.items() if not k.startswith('_')}
        return curva.en(pal, TOTAL)
    finally:
        curva.CURVA = vello


def render(V, cv, pal, d, frases, parrafo):
    """Frases no punto pal: WAV por frase e pasaxe montada coas pausas e a ganancia. Devolve (c, kw, tempos, wavs)."""
    import hashlib
    c = en(pal, cv)
    kw = {k: round(c[k], 4) for k in VOZ_KW if k in c}
    chave = hashlib.sha256(json.dumps([kw, os.environ.get('REF_WAV'), os.environ.get('REF_WAV_CALMO'),
                                       os.environ.get('PATH', '').split(':')[0]]).encode()).hexdigest()[:8]
    os.makedirs(d, exist_ok=True)
    partes, tempos, wavs, t = [], [], [], 0.0
    for k, tx in enumerate(frases):
        p = os.path.join(d, f'{k}-{chave}.wav'); wavs.append(p)
        if not os.path.exists(p):
            w, _ = V.infer(tx, **kw)
            sf.write(p, w, SR)
        w = sf.read(p)[0] * 10 ** (c['ganancia_db'] / 20)
        tempos.append((t, t + len(w) / SR)); partes.append(w); t += len(w) / SR
        if k + 1 < len(frases):
            nw = len(frases[k + 1].split())
            g = c['pausa_frase'] + min(0.3, max(-0.15, 0.02 * (nw - 14))) + (c['pausa_parrafo'] if k + 1 == parrafo else 0)
            partes.append(np.zeros(int(g * SR))); t += g
    sf.write(os.path.join(d, 'pasaxe.wav'), np.concatenate(partes).astype(np.float32), SR)
    return c, kw, tempos, wavs


def refs_de(cv):
    """REF_WAV / REF_WAV_CALMO da candidata (claves _ref_wav e _ref_wav_calmo; relativas a REFS_DIR, varias con ':')."""
    RD = os.environ['REFS_DIR']
    absol = lambda r: ':'.join(p if os.path.isabs(p) else os.path.join(RD, p) for p in r.split(':'))
    return {k: absol(cv[c]) for k, c in (('REF_WAV', '_ref_wav'), ('REF_WAV_CALMO', '_ref_wav_calmo')) if cv.get(c)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('saida'); ap.add_argument('--curva', nargs='*', default=[None],
                                              help='unha ou varias candidatas (JSON); sen ela, curva.py tal cal')
    ap.add_argument('--etiqueta', default='puntos')
    ap.add_argument('--sen-medir', action='store_true')
    ap.add_argument('--pasaxe', default='PASAXE_MEIGAS', choices=('PASAXE_MEIGAS', 'PASAXE'))
    ap.add_argument('--wer-pasaxe', action='store_true', help='WER tamén sobre a pasaxe enteira, como o QA')
    ap.add_argument('--sen-wer', action='store_true', help='sen ASR (exploración rápida)')
    a = ap.parse_args(); a.saida = os.path.abspath(a.saida)
    frases, parrafo = getattr(textos, a.pasaxe), textos.PARRAFO[a.pasaxe]
    env0 = {k: os.environ.get(k) for k in ('REF_WAV', 'REF_WAV_CALMO')}
    cands = []
    for path in a.curva:
        cv = curva_candidata(path)
        cands.append({'nome': os.path.basename(path).replace('.json', '') if path else 'curva.py',
                      'cv': cv, 'env': dict(env0, **refs_de(cv)), 'info': {}})
    base = os.path.join(os.environ['SCRATCH'], 'voz', a.etiqueta)
    import voz_st2 as V
    V.cargar()
    t0 = time.time()
    for ca in cands:
        for k, v in ca['env'].items():
            if v:
                os.environ[k] = v
            else:
                os.environ.pop(k, None)
        for pal in PUNTOS:
            c, kw, tempos, wavs = render(V, ca['cv'], pal, os.path.join(base, ca['nome'], f'p{pal:04d}'), frases, parrafo)
            ca['info'][pal] = (c, kw, tempos, wavs)
            print('tts', ca['nome'], pal, kw, round(time.time() - t0), flush=True)
    V.M.clear()
    import gc; gc.collect()
    if a.sen_medir:
        return
    import modelos, pyloudnorm as pyln
    em = modelos.Emocion(); asr = None if a.sen_wer else modelos.ASR()
    saida = {'pasaxe': a.pasaxe, 'candidatas': []}
    for ca in cands:
        res = []
        for pal in PUNTOS:
            c, kw, tempos, wavs = ca['info'][pal]
            d = os.path.join(base, ca['nome'], f'p{pal:04d}')
            fr = []
            for p, tx in zip(wavs, frases):
                m = A.medir(p, tx); m.update(em.medir(p)); fr.append(m)
            pas = os.path.join(d, 'pasaxe.wav')
            # WER frase a frase (Whisper nun audio longo ás veces salta tramos enteiros: ver informe) e, con
            # --wer-pasaxe, tamén sobre a pasaxe enteira coas pausas, como o QA
            ws = [asr.wer(p, tx) for p, tx in zip(wavs, frases)] if asr else []
            wr = {'wer': round(sum(x['erros'] for x in ws) / sum(x['palabras_ref'] for x in ws), 4) if ws else None,
                  'erros': sum(x['erros'] for x in ws) if ws else None, 'hipotese': ' | '.join(x['hipotese'] for x in ws)}
            if a.wer_pasaxe and asr:
                wr['wer_pasaxe'] = asr.wer(pas, ' '.join(frases))['wer']
            w = sf.read(pas)[0]
            pal_tot = sum(A.palabras(t) for t in frases)
            media = lambda x: round(float(np.mean([f[x] for f in fr if f.get(x) is not None])), 3)
            r = {'pal': pal, 'fase': c['fase'], 'parametros': kw,
                 'pausa_frase': round(c['pausa_frase'], 3), 'ganancia_db': round(c['ganancia_db'], 2),
                 'palabras_min': round(60 * pal_tot / (tempos[-1][1] - tempos[0][0]), 1),
                 'lufs_pasaxe': round(float(pyln.Meter(SR).integrated_loudness(w)), 2),
                 'wer': wr['wer'], 'erros_asr': wr['erros'], 'wer_pasaxe': wr.get('wer_pasaxe'), 'hipotese': wr['hipotese'],
                 **{k: media(k) for k in ('sil_s', 'sil_s_articulacion', 'pal_min_fala', 'f0_mediana_hz', 'f0_media_st',
                                          'f0_sd_st', 'f0_rango_st', 'dinamica_db', 'hnr_db', 'jitter_pct', 'shimmer_pct',
                                          'alpha_ratio_db', 'f0_baixo_75', 'arousal', 'dominancia', 'valencia')},
                 'pico_max': round(max(f['pico'] for f in fr), 4), 'saturadas': sum(f['mostras_saturadas'] for f in fr),
                 'dur_frases_s': [f['dur_s'] for f in fr], 'por_frase': fr}
            r['f0_media_hz'] = round(100 * 2 ** (r['f0_media_st'] / 12), 1)
            res.append(r)
            print(ca['nome'], pal, {k: r[k] for k in ('palabras_min', 'sil_s', 'f0_media_hz', 'f0_sd_st', 'f0_rango_st',
                                                     'lufs_pasaxe', 'arousal', 'wer', 'hnr_db')}, flush=True)
        saida['candidatas'].append({'nome': ca['nome'], 'curva': {k: ca['cv'][k] for k in ca['cv']},
                                    'ref_wav': ca['env'].get('REF_WAV'), 'ref_wav_calmo': ca['env'].get('REF_WAV_CALMO'),
                                    'resultados': res})
        json.dump(saida, open(a.saida, 'w'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
