"""Mide as opcións A-D do fragmento (peza SON). Todo automático; ningunha persoa escoitou nada.

    source herramientas/pipeline/entorno.sh
    PYTHONPATH=$SCRATCH/son/pylib OMP_NUM_THREADS=1 nice $PY plan-de-negocio/gauntlet3/son/scripts/medir.py sinal
    flock "$CPU_LOCK" $PY plan-de-negocio/gauntlet3/son/scripts/medir.py asr

Le $SCRATCH/son/opcions (opcions.py) e escribe plan-de-negocio/gauntlet3/son/medidas/fragmento.json:
DNSMOS (total e por tramo do embude), WER do Whisper galego por tramo, % de voz limpa, picos da pista de ambiente
na zona de durmir, variedade espectral e unha proba de intelixibilidade do murmullo de xente só (sen voz).
"""
import json, os, sys, time
from pathlib import Path
import numpy as np, soundfile as sf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import medidas_son as MS
son = MS.son

S = Path(os.environ['SCRATCH']) / 'son'
OP = S / 'opcions'
SAIDA = HERE.parent / 'medidas'


def fase_sinal(res, fr, sec):
    """DNSMOS e medidas de sinal (lixeiro: un fío, sen o candado)."""
    dn = MS.DNSMOS(nth=1)
    for op in 'ABCD':
        mix, sr = sf.read(OP / f'{op}_mestura.wav', dtype='float32')
        amb, _ = sf.read(OP / f'{op}_amb.wav', dtype='float32')
        voz, _ = sf.read(OP / f'{op}_voz.wav', dtype='float32')
        fs = dn.fiestras(MS.a16k_mono(mix, sr))
        r = res['opcions'].setdefault(op, {})
        r['dnsmos_total'] = dn.resumo(fs)
        for k, (a, b) in sec.items():
            r[f'dnsmos_{k}'] = dn.resumo(fs, a - 0.5, b + 0.5)
        r['pct_voz_limpa'] = son.pct_voz_limpa(voz, amb)
        a, b = sec['durmir']
        r['picos_durmir'] = MS.picos(amb, a - 2, b + 6)
        r['picos_gancho'] = MS.picos(amb, 0, sec['gancho'][1] + 1)
        r['variedade'] = MS.variedade(MS.a16k_mono(amb, sr))
        lm = son.sonoridade_momentanea(amb, 10)
        lv = son.sonoridade_momentanea(voz, 10)
        con = (lm > -70) & (lv > -40)
        r['ambiente_baixo_voz_db_mediana'] = round(float(np.median(lv[con] - lm[con])), 1) if con.any() else None
        print(op, json.dumps(r, ensure_ascii=False), flush=True)


def fase_asr(res, fr, sec):
    """WER do Whisper galego por tramo e intelixibilidade do murmullo (pesado: co candado de CPU)."""
    textos = {k: ' '.join(f['texto'] for f in fr['frases'] if f['tramo'] == k) for k in sec}
    asr = MS.ASR(nth=4)
    for op in 'ABCD':
        mix, sr = sf.read(OP / f'{op}_mestura.wav', dtype='float32')
        x16 = MS.a16k_mono(mix, sr)
        r = res['opcions'].setdefault(op, {})
        erros, pal, hip = 0, 0, {}
        for k, (a, b) in sec.items():       # cortado 0,4 s antes e despois das frases do tramo
            w = asr.wer(x16[int((a - 0.4) * 16000):int((b + 0.4) * 16000)], textos[k])
            r[f'wer_{k}'] = w['wer']; erros += w['erros']; pal += w['palabras_ref']; hip[k] = w['hipotese']
        r['wer_total'] = round(erros / pal, 4); r['erros_asr'] = erros; r['hipotese'] = hip
        print(op, 'WER', r['wer_total'], {k: r[f'wer_{k}'] for k in sec}, flush=True)
    # intelixibilidade do murmullo: 40 s de xente só, forte (-20 LUFS), con 3 sementes
    import pyloudnorm as pyln
    m = pyln.Meter(son.SR)
    xs = []
    for sd in (1, 2, 3):
        x = son.xente(40.0, seed=sd, calma=0.0)
        x *= 10 ** ((-20 - m.integrated_loudness(x)) / 20)
        tx, segs = asr.transcribir(MS.a16k_mono(x, son.SR))
        xs.append({'semente': sd, 'palabras_transcritas': len(tx.split()), 'texto': tx,
                   'no_speech_prob_media': round(float(np.mean([s_.no_speech_prob for s_ in segs])), 3) if segs else None,
                   'avg_logprob_media': round(float(np.mean([s_.avg_logprob for s_ in segs])), 3) if segs else None})
        print('xente só', xs[-1], flush=True)
    res['xente_so_intelixibilidade'] = xs
    b = son._banco_xente()                   # referencia: dúas frases do banco sen procesar
    tx, _ = asr.transcribir(np.concatenate([b[0], np.zeros(8000, np.float32), b[1]]))
    res['xente_banco_seco_referencia'] = {'transcricion': tx, 'texto': 'Este ano as castañas viñeron cedo e son ben '
                                          'grandes. Mira que caro está o millo, non hai quen o compre.'}
    print('banco seco:', tx, flush=True)


def main():
    fase = sys.argv[1] if len(sys.argv) > 1 else 'todo'
    SAIDA.mkdir(exist_ok=True)
    fr = json.load(open(OP / 'fragmento.json'))
    sec = fr['seccions']
    f_ = SAIDA / 'fragmento.json'
    res = json.load(open(f_)) if f_.exists() else {}
    res['nota'] = 'Medidas automáticas (DNSMOS, Whisper gl, sinal). Ningunha persoa escoitou as opcións.'
    res.setdefault('opcions', {})
    t_ini = time.time()
    if fase in ('sinal', 'todo'):
        fase_sinal(res, fr, sec)
    if fase in ('asr', 'todo'):
        fase_asr(res, fr, sec)
    res[f'segundos_{fase}'] = round(time.time() - t_ini, 1)
    tmp = SAIDA / '.fragmento.json.tmp'
    tmp.write_text(json.dumps(res, ensure_ascii=False, indent=1)); os.replace(tmp, f_)
    print('feito', fase, res[f'segundos_{fase}'], 's', flush=True)


if __name__ == '__main__':
    main()
