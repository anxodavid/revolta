"""Etapa SON: choiva sintetizada (procedural, sen mostras de terceiros: sen licenza que anotar)
e mestura coa voz. Voz a -17 LUFS (medida en estéreo; porta A2 do plan: -18 a -16); choiva 17 dB por debaixo; fundidos de entrada e saída.

Gauntlet 3 (30-09-2026): o promotor oíu na mostra un "ruído branco de fondo". Medido: a `choiva` orixinal ten a maior
parte da enerxía entre 2 e 8 kHz e curtose 3,07 (a dun ruído gaussiano): é ruído branco filtrado, as "gotas" case non
se notan. `choiva2` fai a choiva con gotas de verdade (impulsos de moitos tamaños, pingas do beiril con ton que sobe,
coma as burbullas), un leito de ruído rosa sen chiado agudo e refachos lentos; `lume` fai o crepitar dunha lareira.
`mesturar` acepta unha curva de nivel do ambiente (máis baixo no gancho, máis presente ao durmir) e tramos con lume."""
import numpy as np, soundfile as sf
from scipy import signal
import pyloudnorm as pyln

SR = 48000


def choiva(dur, seed=7):
    rng = np.random.default_rng(seed)
    n = int(dur * SR)
    out = np.zeros((n, 2), np.float32)
    sos_bed = signal.butter(2, [350, 7000], 'bandpass', fs=SR, output='sos')
    sos_rum = signal.butter(2, 180, 'lowpass', fs=SR, output='sos')
    sos_drop = signal.butter(2, [1200, 6000], 'bandpass', fs=SR, output='sos')
    sos_soft = signal.butter(2, 9000, 'lowpass', fs=SR, output='sos')
    t = np.arange(n) / SR
    for ch in range(2):
        bed = signal.sosfilt(sos_bed, rng.standard_normal(n)) * 0.5
        rum = signal.sosfilt(sos_rum, np.cumsum(rng.standard_normal(n)) * 0.02)
        rum = rum - signal.sosfilt(signal.butter(1, 20, 'lowpass', fs=SR, output='sos'), rum)
        # gotas: tren de impulsos de Poisson convolucionado cun ruído curto con caída exponencial
        imp = np.zeros(n)
        k = rng.poisson(35 * dur)
        imp[rng.integers(0, n, k)] = rng.uniform(0.2, 1.0, k) ** 2
        kl = int(0.012 * SR)
        ker = rng.standard_normal(kl) * np.exp(-np.arange(kl) / (0.0025 * SR))
        drops = signal.sosfilt(sos_drop, signal.fftconvolve(imp, ker)[:n]) * 0.35
        mod = 0.85 + 0.15 * np.sin(2 * np.pi * t / (17 + 4 * ch) + ch)
        out[:, ch] = signal.sosfilt(sos_soft, bed * mod + drops) + rum * 0.6
    return out / np.abs(out).max() * 0.5


# ------------------------------------------------------------------ choiva 2 e lume (Gauntlet 3)
_ROSA_B = [0.049922035, -0.095993537, 0.050612699, -0.004408786]      # filtro de ruído rosa de Paul Kellet
_ROSA_A = [1, -2.494956002, 2.017265875, -0.522189400]


def _rosa(n, rng):
    return signal.lfilter(_ROSA_B, _ROSA_A, rng.standard_normal(n)).astype(np.float32)


def _impulsos(n, taxa_s, rng, expo=3.0, rafaga=None):
    """Tren de impulsos de Poisson (taxa por segundo) con amplitudes de lei potencial: moitas gotas pequenas e
    poucas grandes. `rafaga` (array 0-1 por mostra) modula a taxa (máis gotas nos refachos)."""
    imp = np.zeros(n, np.float32)
    k = rng.poisson(taxa_s * n / SR)
    pos = rng.integers(0, n, k)
    if rafaga is not None:                       # aceptación proporcional á rafaga
        pos = pos[rng.random(len(pos)) < rafaga[pos]]
    imp[pos] += (rng.random(len(pos)) ** expo).astype(np.float32)
    return imp


def _rms(x):
    return float(np.sqrt(np.mean(np.square(x, dtype=np.float64)))) + 1e-12


def _rafaga(n, rng, periodo=12.0, profundidade=0.35):
    """Envolvente lenta (refachos de vento e choiva): paseo aleatorio suavizado, entre 1-profundidade e 1."""
    m = max(4, int(n / SR / periodo * 4))
    ctrl = np.cumsum(rng.standard_normal(m)); ctrl = (ctrl - ctrl.min()) / (np.ptp(ctrl) + 1e-9)
    env = np.interp(np.arange(n), np.linspace(0, n - 1, m), ctrl)
    env = signal.sosfiltfilt(signal.butter(1, 1 / periodo, 'lowpass', fs=SR, output='sos'), env) if n > 10 * SR else env
    env = (env - env.min()) / (np.ptp(env) + 1e-9)
    return (1 - profundidade + profundidade * env).astype(np.float32)


def choiva2(dur, seed=11):
    """Choiva mansa sobre un tellado de lousa, estéreo. Capas (niveis RMS relativos ao leito):
    leito de ruído rosa (80 Hz-3 kHz) · chuvisco (moitas gotas miúdas, 2-7 kHz) · gotas medianas con ton (0,9-3 kHz)
    · pingas do beiril (poucas, con ton que sobe, a un lado) · todo con refachos lentos."""
    rng = np.random.default_rng(seed)
    n = int(dur * SR)
    out = np.zeros((n, 2), np.float32)
    sos_leito = signal.butter(2, [80, 3000], 'bandpass', fs=SR, output='sos')
    sos_fina = signal.butter(2, [2000, 7000], 'bandpass', fs=SR, output='sos')
    sos_final = signal.butter(2, 7500, 'lowpass', fs=SR, output='sos')
    t = np.arange(int(0.03 * SR)) / SR
    ker_fina = (rng.standard_normal(len(t[:int(0.003 * SR)])) * np.exp(-t[:int(0.003 * SR)] / 0.0006)).astype(np.float32)
    kers_med = [(np.sin(2 * np.pi * f0 * t[:int(0.02 * SR)]) * np.exp(-t[:int(0.02 * SR)] / tau)).astype(np.float32)
                for f0, tau in ((900, 0.006), (1400, 0.005), (2100, 0.004), (3000, 0.003))]
    fase = 2 * np.pi * np.cumsum(np.linspace(1200, 2300, len(t))) / SR          # pinga: ton que sobe (burbulla)
    ker_pinga = (np.sin(fase) * np.exp(-t / 0.012)).astype(np.float32)
    raf_comun = _rafaga(n, rng)
    for ch in range(2):
        raf = 0.7 * raf_comun + 0.3 * _rafaga(n, rng, periodo=7.0)
        leito = signal.sosfilt(sos_leito, _rosa(n, rng)).astype(np.float32)
        leito /= _rms(leito)
        fina = signal.sosfilt(sos_fina, signal.fftconvolve(_impulsos(n, 260, rng, 3.0, raf), ker_fina)[:n]).astype(np.float32)
        fina *= 0.6 / _rms(fina)
        med = sum(signal.fftconvolve(_impulsos(n, 7, rng, 2.2, raf), k_)[:n] for k_ in kers_med).astype(np.float32)
        med *= 0.45 / _rms(med)
        pingas = signal.fftconvolve(_impulsos(n, 0.35 if ch == 0 else 0.12, rng, 1.0), ker_pinga)[:n].astype(np.float32)
        pingas *= 0.25 / _rms(pingas) if pingas.any() else 0
        out[:, ch] = signal.sosfilt(sos_final, (leito * 0.8 + fina) * raf + med + pingas)
    return out / (np.abs(out).max() + 1e-9) * 0.5


def lume(dur, seed=5):
    """Crepitar dunha lareira: estalidos en refachos (1-6 estalidos en 20-150 ms, 1-6 kHz), o chiado da brasa e o
    zumbido grave da chama que tremela. Estéreo, preto do centro."""
    rng = np.random.default_rng(seed)
    n = int(dur * SR)
    out = np.zeros((n, 2), np.float32)
    sos_est = signal.butter(2, [900, 6000], 'bandpass', fs=SR, output='sos')
    sos_chi = signal.butter(2, [1500, 5000], 'bandpass', fs=SR, output='sos')
    sos_zum = signal.butter(2, 220, 'lowpass', fs=SR, output='sos')
    kl = int(0.004 * SR)
    ker = (rng.standard_normal(kl) * np.exp(-np.arange(kl) / (0.0007 * SR))).astype(np.float32)
    imp = np.zeros(n, np.float32)
    for _ in range(rng.poisson(2.5 * dur)):                        # refachos de estalidos
        c = rng.integers(0, n); k = rng.integers(1, 7)
        p = c + (rng.random(k) * 0.15 * SR).astype(int)
        p = p[p < n]; imp[p] += (0.25 + 0.75 * rng.random(len(p)) ** 1.5).astype(np.float32)
    est = signal.sosfilt(sos_est, signal.fftconvolve(imp, ker)[:n]).astype(np.float32)
    est /= _rms(est)
    trem = _rafaga(n, rng, periodo=1.5, profundidade=0.6)
    chi = signal.sosfilt(sos_chi, rng.standard_normal(n)).astype(np.float32); chi *= 0.35 / _rms(chi)
    zum = signal.sosfilt(sos_zum, _rosa(n, rng)).astype(np.float32); zum *= 0.9 / _rms(zum)
    mono = est + (chi + zum) * trem
    lado = signal.sosfilt(sos_chi, rng.standard_normal(n)).astype(np.float32); lado *= 0.1 / _rms(lado)
    out[:, 0] = mono + lado; out[:, 1] = 0.9 * mono - lado
    return out / (np.abs(out).max() + 1e-9) * 0.5


def tramos_envolvente(n, tramos, fundido=1.5):
    """Envolvente 0-1 (por mostra) que vale 1 dentro dos tramos [(t0, t1)] con fundidos de `fundido` s."""
    env = np.zeros(n, np.float32)
    f = int(fundido * SR)
    for t0, t1 in tramos:
        a, b = max(0, int(t0 * SR)), min(n, int(t1 * SR))
        if b <= a:
            continue
        env[a:b] = 1.0
        env[max(0, a - f):a] = np.maximum(env[max(0, a - f):a], np.linspace(0, 1, a - max(0, a - f)))
        env[b:min(n, b + f)] = np.maximum(env[b:min(n, b + f)], np.linspace(1, 0, min(n, b + f) - b))
    return env


def mesturar(voz, dur_total, offset, out_mix, out_voz, voz_lufs=-17.0, rel_choiva=-17.0, ambiente='choiva',
             rel_db=None, lume_tramos=None, rel_lume=-21.0):
    """voz: array mono 24 kHz (sen o offset). Devolve datos de sonoridade.
    Gauntlet 3: `ambiente='choiva2'` usa a choiva nova; `rel_db` (un valor por segundo, en dB, sumado a rel_choiva)
    fai que o ambiente siga o embude; `lume_tramos` [(t0, t1)] engade o crepitar da lareira neses tramos."""
    v = signal.resample_poly(voz, 2, 1).astype(np.float32)
    n = int(dur_total * SR)
    vt = np.zeros(n, np.float32); o = int(offset * SR)
    vt[o:o + len(v)] = v[:max(0, n - o)]
    meter = pyln.Meter(SR)
    l_v = meter.integrated_loudness(np.stack([v, v], 1))   # medida en estéreo, como se escoita
    vt *= 10 ** ((voz_lufs - l_v) / 20)
    r = choiva2(dur_total) if ambiente == 'choiva2' else choiva(dur_total)
    l_r = meter.integrated_loudness(r)
    r *= 10 ** ((voz_lufs + rel_choiva - l_r) / 20)
    if rel_db is not None:
        g = np.interp(np.arange(n) / SR, np.arange(len(rel_db)), np.asarray(rel_db, np.float32)).astype(np.float32)
        r *= (10 ** (g / 20))[:, None]
    fi, fo = int(3 * SR), int(6 * SR)
    env = np.ones(n, np.float32); env[:fi] = np.linspace(0, 1, fi); env[-fo:] = np.linspace(1, 0, fo)
    mix = r * env[:, None] + vt[:, None]
    info_lume = None
    if lume_tramos:
        fl = lume(dur_total)
        l_f = meter.integrated_loudness(fl)
        fl *= 10 ** ((voz_lufs + rel_lume - l_f) / 20)
        e_l = tramos_envolvente(n, lume_tramos)
        mix += fl * (e_l * env)[:, None]
        info_lume = {'rel_lume_db': rel_lume, 'tramos': len(lume_tramos),
                     'segundos': round(float(e_l.sum()) / SR, 1)}
    pk = np.abs(mix).max()
    if pk > 0.89:
        mix *= 0.89 / pk
    sf.write(out_mix, mix, SR, subtype='PCM_16')
    sf.write(out_voz, vt, SR, subtype='PCM_16')
    return {'lufs_voz_obxectivo': voz_lufs, 'choiva_rel_db': rel_choiva, 'ambiente': ambiente,
            'ambiente_rel_db_min_max': [round(float(np.min(rel_db)), 1), round(float(np.max(rel_db)), 1)] if rel_db is not None else None,
            'lume': info_lume,
            'lufs_mestura_pyloudnorm': round(meter.integrated_loudness(mix), 1), 'pico': round(float(np.abs(mix).max()), 3)}
