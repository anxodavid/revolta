"""Mide as opcións A-D do fragmento (peza SON). Todo automático; ningunha persoa escoitou nada.

    source herramientas/pipeline/entorno.sh
    PYTHONPATH=$SCRATCH/son/pylib flock "$CPU_LOCK" $PY plan-de-negocio/gauntlet3/son/scripts/medir.py

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


def main():
    SAIDA.mkdir(exist_ok=True)
    fr = json.load(open(OP / 'fragmento.json'))
    sec = fr['seccions']
    textos = {k: ' '.join(f['texto'] for f in fr['frases'] if f['tramo'] == k) for k in sec}
    t_ini = time.time()
    dn = MS.DNSMOS(nth=4)
    asr = MS.ASR(nth=4)
    res = {'nota': 'Medidas automáticas (DNSMOS, Whisper gl, sinal). Ningunha persoa escoitou as opcións.', 'opcions': {}}
    for op in 'ABCD':
        mix, sr = sf.read(OP / f'{op}_mestura.wav', dtype='float32')
        amb, _ = sf.read(OP / f'{op}_amb.wav', dtype='float32')
        voz, _ = sf.read(OP / f'{op}_voz.wav', dtype='float32')
        x16 = MS.a16k_mono(mix, sr)
        fs = dn.fiestras(x16)
        r = {'dnsmos_total': dn.resumo(fs)}
        for k, (a, b) in sec.items():
            r[f'dnsmos_{k}'] = dn.resumo(fs, a - 0.5, b + 0.5)
        # WER por tramo (cortado 0,4 s antes e despois das frases do tramo)
        erros, pal, hip = 0, 0, {}
        for k, (a, b) in sec.items():
            w = asr.wer(x16[int((a - 0.4) * 16000):int((b + 0.4) * 16000)], textos[k])
            r[f'wer_{k}'] = w['wer']; erros += w['erros']; pal += w['palabras_ref']; hip[k] = w['hipotese']
        r['wer_total'] = round(erros / pal, 4); r['erros_asr'] = erros; r['hipotese'] = hip
        r['pct_voz_limpa'] = son.pct_voz_limpa(voz, amb)
        a, b = sec['durmir']
        r['picos_durmir'] = MS.picos(amb, a - 2, b + 6)
        r['picos_gancho'] = MS.picos(amb, 0, sec['gancho'][1] + 1)
        r['variedade'] = MS.variedade(MS.a16k_mono(amb, sr))
        lm = son.sonoridade_momentanea(amb, 10)
        lv = son.sonoridade_momentanea(voz, 10)
        con = (lm > -70) & (lv > -40)
        r['ambiente_bajo_voz_db_mediana'] = round(float(np.median(lv[con] - lm[con])), 1) if con.any() else None
        res['opcions'][op] = r
        print(op, json.dumps({k: v for k, v in r.items() if k != 'hipotese'}, ensure_ascii=False), flush=True)
        mix = amb = voz = x16 = None
    # intelixibilidade do murmullo: 40 s de xente só, forte (-20 LUFS), con 3 sementes
    import pyloudnorm as pyln
    m = pyln.Meter(son.SR)
    xs = []
    for sd in (1, 2, 3):
        x = son.xente(40.0, seed=sd, calma=0.0)
        x *= 10 ** ((-20 - m.integrated_loudness(x)) / 20)
        tx, segs = asr.transcribir(MS.a16k_mono(x, son.SR))
        xs.append({'semente': sd, 'palabras_transcritas': len(tx.split()), 'texto': tx,
                   'no_speech_prob_media': round(float(np.mean([s.no_speech_prob for s in segs])), 3) if segs else None,
                   'avg_logprob_media': round(float(np.mean([s.avg_logprob for s in segs])), 3) if segs else None})
        print('xente só', xs[-1], flush=True)
    res['xente_so_intelixibilidade'] = xs
    # referencia: unha frase do banco sen procesar (para ver que Whisper si entende a voz seca)
    b = son._banco_xente()
    seca = np.concatenate([b[0], np.zeros(8000, np.float32), b[1]])
    tx, _ = asr.transcribir(seca)
    res['xente_banco_seco_referencia'] = tx
    print('banco seco:', tx, flush=True)
    res['segundos_de_medida'] = round(time.time() - t_ini, 1)
    tmp = SAIDA / '.fragmento.json.tmp'
    tmp.write_text(json.dumps(res, ensure_ascii=False, indent=1)); os.replace(tmp, SAIDA / 'fragmento.json')
    print('feito en', res['segundos_de_medida'], 's', flush=True)


if __name__ == '__main__':
    main()
