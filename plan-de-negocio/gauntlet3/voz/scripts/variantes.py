#!/usr/bin/env python
"""Variantes da voz sobre a pasaxe fixa (peza VOZ, Gauntlet 3): cada variante é un xogo de parámetros de
voz_st2.infer (ref, ref_calma, estilo, escala, f0_media, f0_rango, enerxia, alpha, beta, embedding_scale, pasos).

    source herramientas/pipeline/entorno.sh
    PATH=$ST2_PATHBIN:$PATH PYTHONPATH=$ST2_STUBS:$SCRATCH/voz/pylib flock "$CPU_LOCK" \
        $PY plan-de-negocio/gauntlet3/voz/scripts/variantes.py VARIANTES.json SAIDA.json

VARIANTES.json: [{"nome": "viva_rango12", "ref": "brais-norm-13260.wav", "f0_rango": 1.2, "wer": true}, ...]
(as referencias relativas van contra REFS_DIR; varias unidas con ':' dan o vector medio). Mide por variante o mesmo
ca barrido_refs.py (media das 7 frases) e, se "wer" é true, o WER frase a frase. Todo automático.
"""
import hashlib, json, os, sys, time
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI); sys.path.insert(0, '/home/user/revolta/herramientas/pipeline')
import numpy as np, soundfile as sf
import textos, acustica as A

PARAM = ('escala', 'estilo', 'f0_media', 'f0_rango', 'enerxia', 'alpha', 'beta', 'embedding_scale', 'pasos')
MEDIAS = ('sil_s', 'sil_s_articulacion', 'f0_mediana_hz', 'f0_media_st', 'f0_sd_st', 'f0_rango_st', 'dinamica_db',
          'rms_db', 'lufs', 'hnr_db', 'jitter_pct', 'shimmer_pct', 'alpha_ratio_db', 'arousal', 'dominancia',
          'valencia', 'f0_baixo_75', 'pico')


def main():
    vs = json.load(open(sys.argv[1])); saida = os.path.abspath(sys.argv[2])
    RD = os.environ['REFS_DIR']; OUT = os.path.join(os.environ['SCRATCH'], 'voz', 'variantes')
    absol = lambda r: r and ':'.join(p if os.path.isabs(p) else os.path.join(RD, p) for p in r.split(':'))
    import voz_st2 as V
    V.cargar()
    t0 = time.time()
    for v in vs:
        kw = {k: v[k] for k in PARAM if k in v}
        kw['ref'] = absol(v.get('ref')) or os.environ['REF_WAV']
        kw['ref_calma'] = absol(v.get('ref_calma')) or ''
        chave = hashlib.sha256(json.dumps([kw, os.environ['PATH'].split(':')[0]], sort_keys=True).encode()).hexdigest()[:10]
        v['_dir'] = os.path.join(OUT, chave); os.makedirs(v['_dir'], exist_ok=True)
        for k, t in enumerate(textos.PASAXE):
            p = os.path.join(v['_dir'], f'{k}.wav')
            if not os.path.exists(p):
                w, _ = V.infer(t, **kw)
                sf.write(p, w, 24000)
        print('tts', v['nome'], round(time.time() - t0), flush=True)
    V.M.clear()
    import gc; gc.collect()
    import modelos
    em = modelos.Emocion()
    asr = modelos.ASR() if any(v.get('wer') for v in vs) else None
    res = []
    for v in vs:
        fr = []
        for k, t in enumerate(textos.PASAXE):
            p = os.path.join(v['_dir'], f'{k}.wav')
            m = A.medir(p, t); m.update(em.medir(p)); fr.append(m)
        x = {k: v[k] for k in v if not k.startswith('_')}
        x.update({k: round(float(np.mean([f[k] for f in fr if f.get(k) is not None])), 3) for k in MEDIAS})
        x['dur_total_s'] = round(sum(f['dur_s'] for f in fr), 2)
        x['pico_max'] = max(f['pico'] for f in fr)
        if asr and v.get('wer'):
            ws = [asr.wer(os.path.join(v['_dir'], f'{k}.wav'), t) for k, t in enumerate(textos.PASAXE)]
            x['wer'] = round(sum(w['erros'] for w in ws) / sum(w['palabras_ref'] for w in ws), 4)
            x['hipotese'] = ' | '.join(w['hipotese'] for w in ws)
        x['por_frase'] = fr
        res.append(x)
        print(x['nome'], {k: x.get(k) for k in ('sil_s', 'f0_mediana_hz', 'f0_sd_st', 'f0_rango_st', 'arousal',
                                                 'hnr_db', 'jitter_pct', 'alpha_ratio_db', 'wer')}, flush=True)
        json.dump(res, open(saida, 'w'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
