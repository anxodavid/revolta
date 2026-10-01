"""Constrúe as catro opcións de son sobre o mesmo fragmento con voz (peza SON, Gauntlet 3).

    source herramientas/pipeline/entorno.sh
    $PY plan-de-negocio/gauntlet3/son/scripts/opcions.py

  A  choiva continua: `choiva2` en todo o fragmento, co nivel da curva do embude (a versión que oíu o promotor na
     mostra A/B, sen lareira). Código de son.py do commit 7541a9e (antes desta peza).
  B  só choiva e lareira por escena (D13 tal como estaba en 7541a9e): `choiva` e `lume` nos planos que os teñen,
     fundidos de 2 s, sen variación nin límite de eventos.
  C  catálogo completo por escena (D14, son.py novo): o son de cada plano, con variación, eventos cada vez máis
     escasos, fundidos longos, tope sobre a voz e voz limpa nos planos sen son.
  D  sen ambiente.

Voz: frases de voz_fragmento.py ($SCRATCH/son/voz), coa ganancia e as pausas da curva (coma longo.py). Saída en
$SCRATCH/son/opcions: X_mestura.wav, X_voz.wav, X_amb.wav (48 kHz) e fragmento.json (tempos, planos, tramos, info).
"""
import importlib.util, json, os, subprocess, sys
from pathlib import Path
import numpy as np, soundfile as sf

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
sys.path.insert(0, str(REPO / 'herramientas/pipeline')); sys.path.insert(0, str(HERE))
import curva, son, fragmento as FR

S = Path(os.environ['SCRATCH']) / 'son'
OUT = S / 'opcions'
OFFSET, COLA = 1.5, 6.0
COMMIT_ANTES = '7541a9e'           # son.py antes da peza SON (D13 tal como estaba)


def son_antes():
    """Módulo son.py do commit COMMIT_ANTES (para reproducir A e B tal como eran)."""
    p = S / 'son_d13.py'
    if not p.exists():
        p.write_text(subprocess.run(['git', '-C', str(REPO), 'show', f'{COMMIT_ANTES}:herramientas/pipeline/son.py'],
                                    capture_output=True, text=True, check=True).stdout)
    spec = importlib.util.spec_from_file_location('son_d13', p)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


def calma_de(pal, tot):
    """0 ata o fin do gancho, 1 desde a metade do episodio (onde empeza o ton de durmir), lineal entre medias."""
    xs = curva.nos(tot)
    return float(np.clip((pal - xs[1]) / max(1, xs[3] - xs[1]), 0, 1))


def montar_voz():
    frases = FR.frases_con_pal0()
    sr = 24000
    partes, tempos, t = [], {}, OFFSET
    plano_de = {i: k for k, p in enumerate(FR.PLANOS) for i in p['frases']}
    inicio_seccion = {}
    for k, f in enumerate(frases):
        c = curva.en(f['pal0'], FR.TOT)
        w, _ = sf.read(S / 'voz' / f"frag_{f['i']:02d}.wav")
        w = w * 10 ** (c['ganancia_db'] / 20)
        tempos[f['i']] = (round(t, 3), round(t + len(w) / sr, 3))
        partes.append(w); t += len(w) / sr
        if k + 1 < len(frases):
            seg = frases[k + 1]
            if seg['tramo'] != f['tramo']:
                g = FR.PAUSA_SECCION
                inicio_seccion[seg['i']] = round(t + 0.35, 3)
            else:
                g = c['pausa_frase'] + min(0.3, max(-0.15, 0.02 * (len(seg['texto'].split()) - 14)))
                if plano_de[seg['i']] != plano_de[f['i']]:
                    g += c['pausa_parrafo']
            partes.append(np.zeros(int(g * sr))); t += g
    voz = np.concatenate(partes).astype(np.float32)
    return frases, voz, tempos, inicio_seccion, OFFSET + len(voz) / sr + COLA


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    frases, voz, tempos, ini_sec, dur = montar_voz()
    # planos: empezan 0,25 s antes da súa primeira frase (ou no inicio de sección) e acaban onde empeza o seguinte
    pl = []
    for k, p in enumerate(FR.PLANOS):
        i0 = p['frases'][0]
        b0 = 0.0 if k == 0 else ini_sec.get(i0, tempos[i0][0] - 0.25)
        pl.append(dict(p, n=k + 1, b0=round(b0, 3)))
    for k, p in enumerate(pl):
        p['b1'] = pl[k + 1]['b0'] if k + 1 < len(pl) else round(dur, 3)
    # curva por segundo (coma longo.py): nivel do ambiente e calma
    ini = sorted((tempos[f['i']][0], f['pal0']) for f in frases)
    rel_db, calma = [], []
    for s in range(int(dur) + 1):
        p0 = next((pal for t0_, pal in reversed(ini) if t0_ <= s), 0)
        rel_db.append(round(curva.en(p0, FR.TOT)['ambiente_db'], 2)); calma.append(round(calma_de(p0, FR.TOT), 3))

    def tramos(filtro):
        tr = []
        for p in pl:
            tipo = filtro(p['son'])
            if not tipo:
                continue
            if tr and tr[-1][2] == tipo and p['b0'] - tr[-1][1] < 0.5:
                tr[-1] = (tr[-1][0], p['b1'], tipo)
            else:
                tr.append((p['b0'], p['b1'], tipo))
        return tr

    tr_b = tramos(lambda s_: next((c for c in son.capas(s_) if c in ('choiva', 'lume')), None))
    tr_c = tramos(lambda s_: s_)
    antes = son_antes()
    info = {}
    for op in 'ABCD':
        mix, vz, amb = (str(OUT / f'{op}_{x}.wav') for x in ('mestura', 'voz', 'amb'))
        if op == 'A':
            info[op] = antes.mesturar(voz, dur, OFFSET, mix, vz, ambiente='choiva2', rel_db=rel_db)
        elif op == 'B':
            info[op] = antes.mesturar(voz, dur, OFFSET, mix, vz, ambiente='escena', rel_db=rel_db, escena_tramos=tr_b)
        elif op == 'C':
            info[op] = son.mesturar(voz, dur, OFFSET, mix, vz, ambiente='escena', rel_db=rel_db, escena_tramos=tr_c,
                                    calma=calma, semente='as-meigas-de-verdade', out_amb=amb)
        else:
            info[op] = son.mesturar(voz, dur, OFFSET, mix, vz, ambiente='ningun', out_amb=amb)
        if op in 'AB':      # pista de ambiente = mestura - voz (a voz entra co mesmo factor de pico)
            m_, _ = sf.read(mix, dtype='float32'); v_, _ = sf.read(vz, dtype='float32')
            esc = float(np.dot(m_.mean(1), v_) / np.dot(v_, v_))
            sf.write(amb, m_ - esc * v_[:, None], son.SR, subtype='PCM_16')
            info[op]['factor_voz'] = round(esc, 4)
            m_ = v_ = None
        print(op, json.dumps(info[op], ensure_ascii=False)[:300], flush=True)
    sec = {}
    for f in frases:
        a, b = tempos[f['i']]
        s_ = sec.setdefault(f['tramo'], [a, b]); s_[0] = min(s_[0], a); s_[1] = max(s_[1], b)
    json.dump({'dur': round(dur, 3), 'offset': OFFSET, 'tempos': tempos, 'seccions': sec,
               'frases': [{'i': f['i'], 'tramo': f['tramo'], 'pal0': f['pal0'], 'texto': f['texto']} for f in frases],
               'planos': [{k: p[k] for k in ('n', 'b0', 'b1', 'son', 'prompt', 'frases')} for p in pl],
               'tramos': {'B': tr_b, 'C': tr_c}, 'rel_db': rel_db, 'calma': calma, 'info': info},
              open(OUT / 'fragmento.json', 'w'), ensure_ascii=False, indent=1)
    print('dur', round(dur, 1), 's; planos', len(pl), '; tramos C', tr_c, flush=True)


if __name__ == '__main__':
    main()
