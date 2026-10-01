"""Simulación a escala de episodio (peza SON): 30 min de ambiente só (sen voz) coas opcións A, B e C, para medir o
que un fragmento de 2 min non pode: cambios de ambiente cada 10 min, variedade espectral, monotonía, tramos longos
co mesmo son e picos dos eventos na zona de durmir.

    source herramientas/pipeline/entorno.sh
    OMP_NUM_THREADS=1 nice -n 15 $PY plan-de-negocio/gauntlet3/son/scripts/episodio.py [guia] [alterna]

As listas de planos son inventadas (Claude, axente de son) pero seguen o arco de 30 min de "As meigas de verdade"
(gauntlet3/tema/investigacion.md §10): duración dos planos segundo a curva (5 s no gancho, 17 s ao final) e o son que
lle tocaría a cada imaxe descrita no arco. Tres listas: "guia" (a que pide guia-son.md: bloques por escena e
respiros), "guia1" (primeiro intento, aínda con demasiado son) e "alterna" (case cada plano cambia). Os tramos fanse con son.tramos_de_planos, coma longo.py.

  A  choiva2 continua (xerador de 7541a9e) co nivel da curva, por anacos de 150 s cruzados (estatisticamente igual
     que unha soa realización longa).
  B  choiva e lume de 7541a9e só nos planos que os teñen, fundidos de 2 s, sen variación nin ponte (D13 en 7541a9e).
  C  son.ambiente_escena (catálogo completo, variación, calma, voz limpa).
  D  sen ambiente (non se mide: todo cero).
Saída: plan-de-negocio/gauntlet3/son/medidas/episodio.json.
"""
import json, os, sys, time
from pathlib import Path
import numpy as np, pyloudnorm as pyln

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import medidas_son as MS, opcions
son = MS.son
import curva

DUR, TOT = 1800.0, 3400
SEMENTE = 20260930
# (inicio, fin) en minutos e patrón de son dos planos seguidos; o patrón repítese. None = plano neutro (sen fonte de
# son: a ponte de 20 s pode encher o oco), 'limpa' = voz limpa pedida.
# Lista "alterna": case cada plano cambia (primeira simulación: medía a lista, non o código).
ARCO_ALTERNA = [
    (0.0, 0.67, 'Un conxuro de 1967', ['lume', 'choiva', None, 'lume', 'choiva', None]),
    (0.67, 0.92, 'Aviso e reclamo', [None]),
    (0.92, 2.0, 'Os papeis que falan', [None, 'lume', None, 'campas', None, 'lume']),
    (2.0, 6.0, 'Quen eran as meigas', ['aldea', None, 'vento', 'lume', None, 'aldea', 'fonte', None]),
    (6.0, 10.0, 'O tribunal de Santiago', ['campas', 'choiva', None, 'xente', None, 'choiva', None]),
    (10.0, 16.0, 'Catro aldeas, catro papeis', ['aldea', None, 'fonte+noite', 'lume', None, 'aldea', 'xente', None, 'fonte']),
    (16.0, 19.0, 'María Soliña e o mar de Cangas', ['mar', None, 'mar', 'vento', None]),
    (19.0, 24.0, 'A noite de San Xoán', ['lume+noite', None, 'noite', 'xente', 'fonte+noite', None, 'noite']),
    (24.0, 27.5, 'O frade que non cría nas meigas', [None, 'choiva', 'campas', None, 'vento', 'choiva']),
    (27.5, 30.0, 'Chove na lousa', ['choiva', 'lume', 'choiva', 'choiva']),
]
# Lista "guia1": o primeiro intento de seguir a guía (bloques de 2-6 planos, respiros de 2): aínda con demasiado son
# (78 % do tempo) e 12 cambios cada 10 min ao durmir. Consérvase para comparar.
L = 'limpa'
ARCO_GUIA1 = [
    (0.0, 0.67, 'Un conxuro de 1967', ['lume'] * 3 + ['choiva'] * 3 + [L]),
    (0.67, 0.92, 'Aviso e reclamo', [L]),
    (0.92, 2.0, 'Os papeis que falan', [L] * 3 + ['lume'] * 3 + [None] + ['lume'] + ['campas'] * 2),
    (2.0, 6.0, 'Quen eran as meigas', ['aldea'] * 5 + [L] * 2 + ['vento'] * 4 + [L] * 2 + ['lume'] * 5 + [None]
     + ['lume'] * 2 + [L] * 2 + ['fonte'] * 4 + [L] * 2),
    (6.0, 10.0, 'O tribunal de Santiago', ['campas'] * 3 + ['choiva'] * 5 + [L] * 3 + ['xente'] * 3 + [L] * 2
     + ['choiva'] * 6 + [L] * 2),
    (10.0, 16.0, 'Catro aldeas, catro papeis', ['aldea'] * 5 + [L] * 2 + ['fonte+noite'] * 5 + [L] * 2 + ['lume'] * 6
     + [L] * 2 + ['fonte'] * 5),
    (16.0, 19.0, 'María Soliña e o mar de Cangas', ['mar'] * 6 + [L] * 2 + ['mar+vento'] * 4),
    (19.0, 24.0, 'A noite de San Xoán', ['lume+noite'] * 6 + [L] * 2 + ['noite'] * 5 + [L] * 2 + ['fonte+noite'] * 5),
    (24.0, 27.5, 'O frade que non cría nas meigas', [L] * 3 + ['choiva'] * 6 + [L] * 2 + ['vento'] * 3),
    (27.5, 30.0, 'Chove na lousa', ['lume+choiva'] * 10),
]
# Lista "guia" (guia-son.md, corrixida): bloques dun son por escena de 3-7 planos, respiros de 3-4 planos limpos,
# ~30 % de planos limpos, ≤ 10 cambios cada 10 min ao durmir, sen xente na zona de durmir.
ARCO_GUIA = [
    (0.0, 0.67, 'Un conxuro de 1967', ['lume'] * 3 + ['choiva'] * 2 + [L] * 2),
    (0.67, 0.92, 'Aviso e reclamo', [L]),
    (0.92, 2.0, 'Os papeis que falan', [L] * 3 + ['lume'] * 4 + [L] * 2 + ['campas'] * 2),
    (2.0, 6.0, 'Quen eran as meigas', ['aldea'] * 6 + [L] * 3 + ['vento'] * 5 + [L] * 3 + ['lume'] * 6 + [L] * 3
     + ['fonte'] * 4),
    (6.0, 10.0, 'O tribunal de Santiago', ['campas'] * 3 + ['choiva'] * 5 + [L] * 4 + ['xente'] * 4 + [L] * 3
     + ['choiva'] * 4),
    (10.0, 16.0, 'Catro aldeas, catro papeis', ['aldea'] * 6 + [L] * 3 + ['fonte+noite'] * 6 + [L] * 3 + ['lume'] * 7
     + [L] * 4),
    (16.0, 19.0, 'María Soliña e o mar de Cangas', ['mar'] * 7 + [L] * 3 + ['mar+vento'] * 3),
    (19.0, 24.0, 'A noite de San Xoán', ['lume+noite'] * 7 + [L] * 3 + ['noite'] * 6 + [L] * 4),
    (24.0, 27.5, 'O frade que non cría nas meigas', [L] * 2 + ['choiva'] * 7 + [L] * 4),
    (27.5, 30.0, 'Chove na lousa', ['lume+choiva'] * 9),
]
LISTAS = {'guia': ARCO_GUIA, 'guia1': ARCO_GUIA1, 'alterna': ARCO_ALTERNA}


def pal_de(t):
    return t / DUR * TOT


def planos_episodio(rng, arco):
    pl, t = [], 0.0
    for m0, m1, cap, pat in arco:
        k = 0
        while t < m1 * 60 - 1:
            d = curva.en(pal_de(t), TOT)['plano_s'] * rng.uniform(0.8, 1.2)
            b1 = min(t + d, m1 * 60) if m1 * 60 - (t + d) > 3 else m1 * 60
            pl.append({'b0': round(t, 2), 'b1': round(b1, 2), 'son': pat[k % len(pat)], 'capitulo': cap})
            t, k = b1, k + 1
    return pl


def tramos_de(pl, filtro, ponte_s):
    """Tramos cos mesmos criterios ca longo.py (son.tramos_de_planos); B, coma en 7541a9e, sen ponte (ponte_s=0)."""
    return son.tramos_de_planos([(p['b0'], p['b1'], filtro(p['son'])) for p in pl], ponte_s=ponte_s)


def a16(x):
    return MS.a16k_mono(x, son.SR)


def continua(antes, n, rel_s, voz_lufs=-17.0):
    """A: choiva2 de 7541a9e en anacos de 150 s con fundidos cruzados de 2 s, a -17 dB da voz e coa curva."""
    m = pyln.Meter(son.SR)
    r = np.zeros((n, 2), np.float32); an, cf = 150 * son.SR, 2 * son.SR
    for k, a in enumerate(range(0, n, an)):
        L = min(an + cf, n - a)
        x = antes.choiva2(L / son.SR + 0.01, seed=11 + k)[:L]
        x *= 10 ** ((voz_lufs - 17.0 - m.integrated_loudness(x)) / 20)
        e = np.ones(L, np.float32)
        if k > 0:
            e[:cf] = np.sin(np.linspace(0, np.pi / 2, cf))
        if a + L < n:
            e[-cf:] *= np.cos(np.linspace(0, np.pi / 2, cf))
        r[a:a + L] += x * e[:, None]
    r *= (10 ** (np.interp(np.arange(n) / son.SR, np.arange(len(rel_s)), rel_s) / 20)).astype(np.float32)[:, None]
    return r


def escena_d13(antes, n, tramos, rel_s, voz_lufs=-17.0):
    """B: choiva e lume de 7541a9e nos seus tramos, con fundidos de 2 s (coma o modo 'escena' de entón, que
    enmascaraba unha realización longa: aquí cada tramo colle a súa parte cunha semente segundo o seu inicio)."""
    m = pyln.Meter(son.SR)
    r = np.zeros((n, 2), np.float32)
    for t0, t1, tipo in tramos:
        fn, rel = antes.AMBIENTES[tipo]
        a, b = max(0, int((t0 - 2) * son.SR)), min(n, int((t1 + 2) * son.SR))
        x = fn((b - a) / son.SR + 0.01, seed=int(t0 * 10) + 7)[:b - a]
        x *= 10 ** ((voz_lufs + rel - m.integrated_loudness(x)) / 20)
        e = son.tramos_envolvente(b - a, [(t0 - a / son.SR, t1 - a / son.SR)], fundido=2.0)
        r[a:b] += x * e[:, None]
    r *= (10 ** (np.interp(np.arange(n) / son.SR, np.arange(len(rel_s)), rel_s) / 20)).astype(np.float32)[:, None]
    return r


def medir(nome, r, pl, tr, t_durmir, cal_s):
    x16 = a16(r)
    con = son.sonoridade_momentanea(r, 1) > -70
    act = [frozenset() for _ in range(int(DUR) + 1)]
    for t0, t1, tipo in tr:
        for s in range(int(t0), min(len(act), int(np.ceil(t1)))):
            act[s] = act[s] | frozenset(son.capas(tipo))
    ch = np.array([a != b for a, b in zip(act, act[1:])], float)
    cambios = int(ch.sum())
    cam10 = np.convolve(ch, np.ones(600), 'valid')
    cam10_durmir = cam10[int(t_durmir):] if len(cam10) > t_durmir else cam10[-1:]
    mesmo, run, prev, sen_limpa, run2 = 0, 0, None, 0, 0
    for a in act:
        run = run + 1 if (a and a == prev) else (1 if a else 0); mesmo = max(mesmo, run); prev = a
        run2 = run2 + 1 if a else 0; sen_limpa = max(sen_limpa, run2)
    res = {'pct_tempo_con_ambiente': round(100 * float(con.mean()), 1),
           'cambios_por_10min': round(cambios / DUR * 600, 1) if tr else 0.0,
           'cambios_max_en_10min': int(cam10.max()) if tr else 0,
           'cambios_10min_zona_durmir_media': round(float(cam10_durmir.mean()), 1) if tr else 0.0,
           'tramo_max_mesmo_son_min': round(mesmo / 60, 1) if tr else round(DUR / 60, 1),
           'tramo_max_sen_voz_limpa_min': round(sen_limpa / 60, 1) if tr else round(DUR / 60, 1),
           'tipos_distintos': len({c for _, _, t in tr for c in son.capas(t)}) if tr else 1,
           'variedade': MS.variedade(x16),
           'variedade_zona_durmir': MS.variedade(x16[int(t_durmir * 16000):]),
           'picos_zona_durmir': MS.picos(r, t_durmir, DUR),
           'picos_gancho_2min': MS.picos(r, 0, 120)}
    if nome == 'A':
        res.update(cambios_por_10min=0.0, cambios_max_en_10min=0, cambios_10min_zona_durmir_media=0.0)
    print(nome, json.dumps(res, ensure_ascii=False), flush=True)
    return res


def main():
    t_ini = time.time()
    n = int(DUR * son.SR)
    rel_s = [round(curva.en(pal_de(s_), TOT)['ambiente_db'], 2) for s_ in range(int(DUR) + 1)]
    cal_s = [round(opcions.calma_de(pal_de(s_), TOT), 3) for s_ in range(int(DUR) + 1)]
    t_durmir = float(next(s_ for s_, c in enumerate(cal_s) if c >= 0.999))
    antes = opcions.son_antes()
    out = HERE.parent / 'medidas'; out.mkdir(exist_ok=True)
    f_ = out / 'episodio.json'
    res = json.load(open(f_)) if f_.exists() else {}
    res.update({'nota': 'Simulación sen voz: ambiente só. Listas de planos inventadas polo axente de son seguindo o arco.',
                'inicio_zona_durmir_s': t_durmir})
    ops = res.setdefault('opcions', {})
    if 'A' not in ops:      # A non depende da lista (choiva continua)
        ops['A'] = medir('A', continua(antes, n, rel_s), [], [(0.0, DUR, 'choiva')], t_durmir, cal_s)
    for lista in sys.argv[1:] or ['guia', 'alterna']:
        rng = np.random.default_rng(SEMENTE)
        pl = planos_episodio(rng, LISTAS[lista])
        res[f'lista_{lista}'] = {'planos': len(pl), 'planos_con_son': sum(1 for p in pl if p['son'] not in (None, L)),
                                 'duracion_media_plano_s': round(float(np.mean([p['b1'] - p['b0'] for p in pl])), 1)}
        tr_b = tramos_de(pl, lambda s_: next((c for c in son.capas(s_) if c in ('choiva', 'lume')), None)
                         if s_ not in (None, L) else None, 0.0)
        tr_c = tramos_de(pl, lambda s_: s_, son.PONTE_S)
        for nome, tr in ((f'B ({lista})', tr_b), (f'C ({lista})', tr_c)):
            t = time.time()
            if nome.startswith('B'):
                r = escena_d13(antes, n, tr, rel_s)
            else:
                r, info = son.ambiente_escena(n, tr, -17.0, rel_s, cal_s, SEMENTE)
                fi, fo = int(3 * son.SR), int(6 * son.SR)
                r[:fi] *= np.linspace(0, 1, fi, dtype=np.float32)[:, None]; r[-fo:] *= np.linspace(1, 0, fo, dtype=np.float32)[:, None]
                res[f'lista_{lista}']['avisos_C'] = info.get('avisos')
                res[f'lista_{lista}']['tramos_C'] = [(round(a, 1), round(b_, 1), ti) for a, b_, ti in tr]
            ops[nome] = medir(nome, r, pl, tr, t_durmir, cal_s)
            ops[nome]['segundos_calculo'] = round(time.time() - t, 1)
            r = None
    for k in ('B', 'C', 'planos', 'planos_con_son_C', 'duracion_media_plano_s', 'tramos_C', 'avisos_C'):
        ops.pop(k, None) if k in ('B', 'C') else res.pop(k, None)      # primeira simulación (sen ponte): substituída
    res['segundos_total_ultima_execucion'] = round(time.time() - t_ini, 1)
    tmp = out / '.episodio.json.tmp'
    tmp.write_text(json.dumps(res, ensure_ascii=False, indent=1)); os.replace(tmp, f_)
    print('feito', res['segundos_total_ultima_execucion'], 's', flush=True)


if __name__ == '__main__':
    main()
