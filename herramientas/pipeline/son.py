"""Etapa SON: choiva sintetizada (procedural, sen mostras de terceiros: sen licenza que anotar)
e mestura coa voz. Voz a -21 LUFS; choiva 17 dB por debaixo; fundidos de entrada e saída."""
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


def mesturar(voz, dur_total, offset, out_mix, out_voz, voz_lufs=-21.0, rel_choiva=-17.0):
    """voz: array mono 24 kHz (sen o offset). Devolve datos de sonoridade."""
    v = signal.resample_poly(voz, 2, 1).astype(np.float32)
    n = int(dur_total * SR)
    vt = np.zeros(n, np.float32); o = int(offset * SR)
    vt[o:o + len(v)] = v[:max(0, n - o)]
    meter = pyln.Meter(SR)
    l_v = meter.integrated_loudness(v)
    vt *= 10 ** ((voz_lufs - l_v) / 20)
    r = choiva(dur_total)
    l_r = meter.integrated_loudness(r)
    r *= 10 ** ((voz_lufs + rel_choiva - l_r) / 20)
    fi, fo = int(3 * SR), int(6 * SR)
    env = np.ones(n, np.float32); env[:fi] = np.linspace(0, 1, fi); env[-fo:] = np.linspace(1, 0, fo)
    mix = r * env[:, None] + vt[:, None]
    pk = np.abs(mix).max()
    if pk > 0.89:
        mix *= 0.89 / pk
    sf.write(out_mix, mix, SR, subtype='PCM_16')
    sf.write(out_voz, vt, SR, subtype='PCM_16')
    return {'lufs_voz_obxectivo': voz_lufs, 'choiva_rel_db': rel_choiva,
            'lufs_mestura_pyloudnorm': round(meter.integrated_loudness(mix), 1), 'pico': round(float(np.abs(mix).max()), 3)}
