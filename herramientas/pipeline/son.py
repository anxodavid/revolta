"""Etapa SON: ambientes sintetizados por código (procedurais, sen gravacións de terceiros: sen licenza que anotar) e
mestura coa voz. Voz a -17 LUFS (medida en estéreo; porta A2 do plan: -18 a -16); fundidos de entrada e saída.

Historia. `choiva` (Gauntlet 2) era ruído branco filtrado: curtose 3,07 e case toda a enerxía entre 2 e 8 kHz; o
promotor oíuna coma "ruído branco de fondo". `choiva2` (Gauntlet 3) fai gotas de verdade. Decisións do promotor:
D13 (son por escena e tramos de voz limpa, nada de ruído continuo) e D14 (que non se faga monótono nin cansino:
adaptalo á escena; nun xentío, murmullo de voces que non se entendan).

CATÁLOGO (modo `escena` de `mesturar`). Cada tipo é unha función tipo(dur, seed, calma, **parámetros) que devolve
estéreo a 48 kHz (pico 0,5); `calma` vai de 0 (gancho) a 1 (zona de durmir). Nivel: LUFS respecto da voz
(AMBIENTES), antes da curva do embude (curva.py, `ambiente_db`) e do que baixa cada tipo ao durmir (DURMIR_DB).

  tipo    nivel  que é                                                        eventos (escasos e suaves ao durmir)
  choiva  -18    choiva mansa na lousa: leito de ruído rosa, chuvisco de      pingas do beiril (ton que sobe,
                 gotas miúdas, gotas medianas con ton, refachos lentos        coma unha burbulla)
  lume    -21    lareira: estalidos en refachos, chiado da brasa e zumbido    un leño que se asenta: golpe grave,
                 da chama que tremela                                         estalidos e chiado que medra
  mar     -20    mar en calma desde a costa: ondas irregulares (6-14 s) que   de cando en vez, unha onda maior
                 medran e rompen con escuma; rumor de fondo
  vento   -23    vento nas árbores: bandas de ruído rosa que se desprazan     un refacho máis forte
                 e follas que rumorexan cos refachos
  fonte   -22    auga que corre (fonte ou regato): burbullas con ton que      un gorgolexo
                 sobe (resonancia de Minnaert) e o chorro no pío
  xente   -26    xentío, feira ou xuntanza: 6-12 voces superpostas do banco   a xente respira: ondas lentas de
                 son_datos/xente-banco.ogg (conversa en galego coa voz de     máis e menos voces
                 Nós, son_xente.py), cada unha co seu ton e timbre, paso
                 baixo a 0,9-1,5 kHz e reverberación: xente falando lonxe
                 sen que se entenda ningunha palabra (se falta o banco,
                 murmullo de formantes sintéticos)
  noite   -25    noite de verán: grilos lonxe (4-5 kHz), aire de noite e,     moi de cando en vez, o ouveo dunha
                 nalgúns tramos, o "uuu" do sapo parteiro                     curuxa lonxana
  aldea   -24    aldea de día: brisa, chíos de pardais e cantos de merlo      un chocallo de vaca lonxano
  campas  -24    campás lonxanas (catedral, mosteiro): síntese aditiva con    os toques, en grupos de 2-9; o
                 parciais inharmónicos (hum, prima, terceira menor, quinta,   primeiro, ao comezo do tramo
                 nominal...) con batementos e reverberación grande; entre
                 toques, só o aire

Un plano pode levar dúas capas ('lume+noite'): a segunda vai 3 dB máis baixa.

CONTRA A MONOTONÍA (D14): semente e parámetros distintos en cada tramo (VARIACION); os tramos longos pártense en
anacos de ata TRAMO_MAX s que se funden entre si; intensidade que respira (±2,5 dB en 25-70 s); eventos ao chou,
cada vez máis escasos e suaves cara ao final (taxa ×(1-0,7·calma), -6 dB·calma) e co seu pico limitado respecto do
leito (RMS en 50 ms fronte a RMS en 1 s: 12 dB no gancho, 5 dB ao durmir); fundidos longos (3 s no gancho, 8 s ao
durmir) centrados no corte de plano; tope do ambiente sobre a voz (sonoridade momentánea: 8 dB baixo a voz, 12 dB ao
durmir); e voz limpa en todo plano sen son.

`mesturar` por defecto (ambiente='choiva') segue sendo o do Gauntlet 2 (pipeline.py).
"""
import json, zlib
from fractions import Fraction
from pathlib import Path
import numpy as np, soundfile as sf
from scipy import signal
from scipy.ndimage import gaussian_filter1d, minimum_filter1d, uniform_filter1d
import pyloudnorm as pyln

SR = 48000
DATOS = Path(__file__).resolve().parent / 'son_datos'


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


# ------------------------------------------------------------------ utilidades
_ROSA_B = [0.049922035, -0.095993537, 0.050612699, -0.004408786]      # filtro de ruído rosa de Paul Kellet
_ROSA_A = [1, -2.494956002, 2.017265875, -0.522189400]


def _rosa(n, rng):
    return signal.lfilter(_ROSA_B, _ROSA_A, rng.standard_normal(n)).astype(np.float32)


def _impulsos(n, taxa_s, rng, expo=3.0, rafaga=None):
    """Tren de impulsos de Poisson (taxa por segundo) con amplitudes de lei potencial: moitas gotas pequenas e
    poucas grandes. `rafaga` (array 0-1 por mostra) modula a taxa (máis gotas nos refachos)."""
    imp = np.zeros(n, np.float32)
    k = rng.poisson(max(0.0, taxa_s) * n / SR)
    pos = rng.integers(0, n, k)
    if rafaga is not None:                       # aceptación proporcional á rafaga
        pos = pos[rng.random(len(pos)) < rafaga[pos]]
    imp[pos] += (rng.random(len(pos)) ** expo).astype(np.float32)
    return imp


def _rms(x):
    return float(np.sqrt(np.mean(np.square(x, dtype=np.float64)))) + 1e-12


def _db(x):
    return 10 ** (np.asarray(x) / 20)


def _rafaga(n, rng, periodo=12.0, profundidade=0.35):
    """Envolvente lenta (refachos de vento e choiva): paseo aleatorio suavizado, entre 1-profundidade e 1."""
    m = max(4, int(n / SR / periodo * 4))
    ctrl = np.cumsum(rng.standard_normal(m)); ctrl = (ctrl - ctrl.min()) / (np.ptp(ctrl) + 1e-9)
    env = np.interp(np.arange(n), np.linspace(0, n - 1, m), ctrl)
    env = signal.sosfiltfilt(signal.butter(1, 1 / periodo, 'lowpass', fs=SR, output='sos'), env) if n > 10 * SR else env
    env = (env - env.min()) / (np.ptp(env) + 1e-9)
    return (1 - profundidade + profundidade * env).astype(np.float32)


def _ruido_lento(n, rng, periodo, sr=SR, fs_env=50):
    """Ruído gaussiano lento e estacionario (media 0, desviación 1) coa escala de tempo `periodo` s."""
    m = int(n / sr * fs_env) + 4
    s = max(1.0, periodo * fs_env / 5)
    w = rng.standard_normal(m + int(8 * s))
    x = gaussian_filter1d(w, s)[int(4 * s):int(4 * s) + m] * np.sqrt(2 * np.sqrt(np.pi) * s)
    return np.interp(np.arange(n) / sr, np.arange(m) / fs_env, x).astype(np.float32)


def _respira(n, rng, prof_db=2.5, sr=SR):
    """A intensidade respira: ganancia lenta de ±prof_db en 25-70 s."""
    x = np.clip(_ruido_lento(n, rng, rng.uniform(25, 70), sr), -2, 2) / 2
    return _db(prof_db * x).astype(np.float32)


def _tempos(dur, taxa_min, rng, calma, sep=2.0, primeiro=None):
    """Instantes (s) dos eventos: Poisson con `taxa_min` eventos por minuto ×(1-0,7·calma), separados `sep` s.
    `primeiro` (s): o primeiro evento cae ao chou antes desa marca (para que o son acompañe un plano curto)."""
    taxa = max(0.0, taxa_min) / 60 * (1 - 0.7 * calma)
    if taxa <= 0:
        return []
    t = rng.uniform(0.3, primeiro) if primeiro else rng.exponential(1 / taxa)
    ts = []
    while t < dur:
        ts.append(t); t += max(sep, rng.exponential(1 / taxa))
    return ts


def _pan(x, p):
    """Mono a estéreo con lei de potencia constante (p: 0 esquerda ... 1 dereita)."""
    return np.stack([x * np.cos(p * np.pi / 2), x * np.sin(p * np.pi / 2)], 1).astype(np.float32)


def _pon(dest, x, i):
    """Suma x en dest desde a mostra i (recorta nos bordos)."""
    a, b = max(0, i), min(len(dest), i + len(x))
    if b > a:
        dest[a:b] += x[a - i:b - i]


def _ir(rt60, sr, rng, pre=0.02, brillo=4000.0):
    """Resposta ao impulso estéreo sintética: ruído con caída exponencial (rt60) que escurece co tempo."""
    L = int(rt60 * 1.2 * sr)
    t = np.arange(L) / sr
    ir = rng.standard_normal((L, 2)) * np.exp(-6.91 * t / rt60)[:, None]
    lp = signal.sosfilt(signal.butter(2, brillo / 4, fs=sr, output='sos'), ir, axis=0)
    k = np.clip(t / rt60, 0, 1)[:, None]
    ir = signal.sosfilt(signal.butter(2, min(brillo, 0.45 * sr), fs=sr, output='sos'), (1 - k) * ir + k * lp, axis=0)
    ir = np.concatenate([np.zeros((int(pre * sr), 2)), ir])
    return (ir / np.sqrt((ir ** 2).sum(0))).astype(np.float32)


def _reverb(x, ir, mollado):
    """(1-mollado)·seco + mollado·reverberado (co mesmo RMS). x mono ou estéreo; devolve estéreo."""
    if x.ndim == 1:
        x = np.stack([x, x], 1)
    w = np.stack([signal.oaconvolve(x[:, c], ir[:, c])[:len(x)] for c in range(2)], 1)
    w *= _rms(x) / _rms(w)
    return ((1 - mollado) * x + mollado * w).astype(np.float32)


def _limitar(leito, ev, max_db):
    """Os eventos non pasan de max_db sobre o leito, en sonoridade (potencia con ponderación K, BS.1770): a dos
    eventos en 50 ms fronte á do leito en 3 s. Ataque ~20 ms e soltura 1 s (a cola dun evento baixa co seu golpe)."""
    pl = np.maximum(uniform_filter1d(_potencia_k(leito), 300, mode='nearest'), 0)
    pe = np.maximum(uniform_filter1d(_potencia_k(ev), 5, mode='nearest'), 0)
    g = minimum_filter1d(np.minimum(1.0, np.sqrt(pl / (pe + 1e-20)) * _db(max_db)), 3)
    a = np.exp(-1 / 100); out = np.empty_like(g); cur = 1.0
    for i, v in enumerate(g):
        cur = v if v < cur else a * cur + (1 - a) * v
        out[i] = cur
    gi = np.interp(np.arange(len(ev)) / SR, (np.arange(len(out)) + 0.5) / 100, out).astype(np.float32)
    return ev * (gi[:, None] if ev.ndim == 2 else gi)


# Filtro K da ITU-R BS.1770 a 48 kHz (prefiltro de estante + paso alto RLB)
_KW = np.array([[1.53512485958697, -2.69169618940638, 1.19839281085285, 1.0, -1.69065929318241, 0.73248077421585],
                [1.0, -2.0, 1.0, 1.0, -1.99004745483398, 0.99007225036621]])


def _potencia_k(x):
    """Potencia con ponderación K (BS.1770, suma das canles) en bloques de 10 ms (100 valores por segundo). Por
    anacos de 60 s: vale para pistas de 30 min sen encher a memoria."""
    x2 = x if x.ndim == 2 else x[:, None]
    zi = np.zeros((_KW.shape[0], 2, x2.shape[1]))
    blk, pw = SR // 100, []
    for a in range(0, len(x2), 60 * SR):
        y, zi = signal.sosfilt(_KW, x2[a:a + 60 * SR].astype(np.float64), axis=0, zi=zi)
        p = (y ** 2).sum(1)
        pp = np.zeros(-(-len(p) // blk) * blk); pp[:len(p)] = p
        pw.append(pp.reshape(-1, blk).mean(1))
    return np.concatenate(pw)


def sonoridade_momentanea(x, fs_out=10, fiestra=0.4):
    """Sonoridade (LUFS) en fiestras de `fiestra` s (0,4 = momentánea da BS.1770), mostrada a fs_out Hz."""
    pm = np.maximum(uniform_filter1d(_potencia_k(x), max(1, int(round(fiestra * 100))), mode='constant'), 0)
    return -0.691 + 10 * np.log10(pm[::max(1, 100 // fs_out)] + 1e-20)


def _tope(x, max_lufs, fs_g=100):
    """Baixa o ambiente onde a súa sonoridade momentánea pasa de max_lufs (ataque 50 ms, soltura 1,5 s)."""
    g = np.minimum(0.0, max_lufs - sonoridade_momentanea(x, fs_g))
    if g.min() > -0.05:
        return x
    g = minimum_filter1d(g, 5)
    a = np.exp(-1 / (1.5 * fs_g)); out = np.empty_like(g); cur = 0.0
    for i, v in enumerate(g):
        cur = v if v < cur else a * cur + (1 - a) * v
        out[i] = cur
    return x * _db(np.interp(np.arange(len(x)) / SR, np.arange(len(out)) / fs_g, out)).astype(np.float32)[:, None]


def _pico(x):
    return (x / (np.abs(x).max() + 1e-9) * 0.5).astype(np.float32)


# ------------------------------------------------------------------ choiva, lume, mar, vento
def choiva2(dur, seed=11, calma=0.0, gotas=260.0, medianas=7.0, pingas=0.35, refachos=0.35):
    """Choiva mansa sobre un tellado de lousa, estéreo. Capas (niveis RMS relativos ao leito):
    leito de ruído rosa (80 Hz-3 kHz) · chuvisco (`gotas` miúdas por segundo, 2-7 kHz) · gotas medianas con ton
    (0,9-3 kHz) · refachos lentos. Eventos: pingas do beiril (`pingas` por segundo, con ton que sobe, a un lado),
    cunha amplitude fixa por pinga (se hai menos, non soan máis fortes)."""
    rng = np.random.default_rng(seed)
    n = int(dur * SR)
    out = np.zeros((n, 2), np.float32); ev = np.zeros((n, 2), np.float32)
    sos_leito = signal.butter(2, [80, 3000], 'bandpass', fs=SR, output='sos')
    sos_fina = signal.butter(2, [2000, 7000], 'bandpass', fs=SR, output='sos')
    sos_final = signal.butter(2, 7500, 'lowpass', fs=SR, output='sos')
    t = np.arange(int(0.03 * SR)) / SR
    ker_fina = (rng.standard_normal(len(t[:int(0.003 * SR)])) * np.exp(-t[:int(0.003 * SR)] / 0.0006)).astype(np.float32)
    kers_med = [(np.sin(2 * np.pi * f0 * t[:int(0.02 * SR)]) * np.exp(-t[:int(0.02 * SR)] / tau)).astype(np.float32)
                for f0, tau in ((900, 0.006), (1400, 0.005), (2100, 0.004), (3000, 0.003))]
    fase = 2 * np.pi * np.cumsum(np.linspace(1200, 2300, len(t))) / SR          # pinga: ton que sobe (burbulla)
    ker_pinga = (np.sin(fase) * np.exp(-t / 0.012)).astype(np.float32)
    s_pinga = 0.25 / np.sqrt(0.35 / SR / 3 * np.sum(ker_pinga.astype(np.float64) ** 2))  # 0,35/s -> RMS 0,25
    prof = refachos * (1 - 0.3 * calma)
    raf_comun = _rafaga(n, rng, profundidade=prof)
    for ch in range(2):
        raf = 0.7 * raf_comun + 0.3 * _rafaga(n, rng, periodo=7.0, profundidade=prof)
        leito = signal.sosfilt(sos_leito, _rosa(n, rng)).astype(np.float32)
        leito /= _rms(leito)
        fina = signal.sosfilt(sos_fina, signal.fftconvolve(_impulsos(n, gotas, rng, 3.0, raf), ker_fina)[:n]).astype(np.float32)
        fina *= 0.6 / _rms(fina)
        med = sum(signal.fftconvolve(_impulsos(n, medianas, rng, 2.2, raf), k_)[:n] for k_ in kers_med).astype(np.float32)
        med *= 0.45 / _rms(med)
        out[:, ch] = (leito * 0.8 + fina) * raf + med
        tx = pingas * (1 - 0.7 * calma) * (1.0 if ch == 0 else 0.35)
        ev[:, ch] = signal.fftconvolve(_impulsos(n, tx, rng, 1.0), ker_pinga)[:n] * s_pinga * _db(-6 * calma)
    ev = _limitar(out, ev, 12 - 7 * calma)
    return _pico(signal.sosfilt(sos_final, out + ev, axis=0))


def _leno(rng):
    """Un leño que se asenta: golpe grave (110 -> 55 Hz), un feixe de estalidos e un chiado que medra e se apaga."""
    L = int(1.6 * SR); tt = np.arange(L) / SR
    f = np.where(tt < 0.25, 110 - 220 * tt, 55)
    golpe = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt / 0.09)
    golpe += signal.sosfilt(signal.butter(2, 500, fs=SR, output='sos'), rng.standard_normal(L)) * np.exp(-tt / 0.05) * 0.5
    imp = np.zeros(L)
    k = int(rng.integers(6, 15))
    imp[(0.05 * SR + rng.random(k) * 0.9 * SR).astype(int)] = 0.3 + 0.7 * rng.random(k)
    kl = int(0.004 * SR)
    ker = rng.standard_normal(kl) * np.exp(-np.arange(kl) / (0.0007 * SR))
    est = signal.sosfilt(signal.butter(2, [900, 6000], 'bandpass', fs=SR, output='sos'), np.convolve(imp, ker)[:L])
    chi = signal.sosfilt(signal.butter(2, [1500, 5000], 'bandpass', fs=SR, output='sos'), rng.standard_normal(L))
    chi *= np.clip(tt / 0.4, 0, 1) * np.exp(-np.clip(tt - 0.4, 0, None) / 0.5) * 0.3
    x = golpe / (np.abs(golpe).max() + 1e-9) * 0.8 + est / (np.abs(est).max() + 1e-9) + chi
    return x.astype(np.float32)


def lume(dur, seed=5, calma=0.0, estalidos=2.5, lenos=1.3):
    """Crepitar dunha lareira: estalidos en refachos (`estalidos` refachos/s de 1-6 estalidos en 20-150 ms, 1-6 kHz),
    o chiado da brasa e o zumbido grave da chama que tremela. Estéreo, preto do centro. Eventos: `lenos` leños que
    se asentan por minuto. Ao durmir, a metade de estalidos, 6 dB máis baixos e máis escuros (ata 3,5 kHz)."""
    rng = np.random.default_rng(seed)
    n = int(dur * SR)
    out = np.zeros((n, 2), np.float32)
    sos_est = signal.butter(2, [900, 6000 - 2500 * calma], 'bandpass', fs=SR, output='sos')
    sos_chi = signal.butter(2, [1500, 5000], 'bandpass', fs=SR, output='sos')
    sos_zum = signal.butter(2, 220, 'lowpass', fs=SR, output='sos')
    kl = int(0.004 * SR)
    ker = (rng.standard_normal(kl) * np.exp(-np.arange(kl) / (0.0007 * SR))).astype(np.float32)
    imp = np.zeros(n, np.float32)
    for _ in range(rng.poisson(estalidos * (1 - 0.5 * calma) * dur)):   # refachos de estalidos
        c = rng.integers(0, n); k = rng.integers(1, 7)
        p = c + (rng.random(k) * 0.15 * SR).astype(int)
        p = p[p < n]; imp[p] += (0.25 + 0.75 * rng.random(len(p)) ** 1.5).astype(np.float32)
    est = signal.sosfilt(sos_est, signal.fftconvolve(imp, ker)[:n]).astype(np.float32)
    est /= _rms(est)
    trem = _rafaga(n, rng, periodo=1.5, profundidade=0.6)
    chi = signal.sosfilt(sos_chi, rng.standard_normal(n)).astype(np.float32); chi *= 0.35 / _rms(chi)
    zum = signal.sosfilt(sos_zum, _rosa(n, rng)).astype(np.float32); zum *= 0.9 / _rms(zum)
    lado = signal.sosfilt(sos_chi, rng.standard_normal(n)).astype(np.float32); lado *= 0.1 / _rms(lado)
    brasa = (chi + zum) * trem
    out[:, 0] = brasa + lado; out[:, 1] = 0.9 * brasa - lado
    # os estalidos, coma eventos: como moito 14 dB sobre a brasa no gancho e 8 dB ao durmir
    e_st = np.stack([est, 0.9 * est], 1) * 0.8 * _db(-6 * calma)
    ev = np.zeros(n, np.float32)
    amp = _rms(brasa) * _db(10) * _db(-6 * calma)
    for t0 in _tempos(dur, lenos, rng, calma, sep=10.0):
        _pon(ev, _leno(rng) * amp * rng.uniform(0.5, 1.0), int(t0 * SR))
    if ev.any():
        e_st += _limitar(out, _pan(ev, rng.uniform(0.35, 0.65)), 12 - 7 * calma)
    out += _limitar(out, e_st.astype(np.float32), 13 - 7 * calma)
    return _pico(out)


def mar(dur, seed=17, calma=0.0, periodo=10.0):
    """Mar en calma desde a costa: ondas irregulares (periodo ±35 %) que medran, rompen nun punto da beira (esquerda
    ou dereita) e deixan escuma; rumor grave de fondo. Eventos: de cando en vez unha onda maior (menos e máis
    pequena ao durmir, e a escuma máis escura)."""
    rng = np.random.default_rng(seed)
    n = int(dur * SR)
    e_corpo = np.zeros((n, 2), np.float32); e_esc = np.zeros((n, 2), np.float32)
    t = -rng.uniform(0, periodo)
    while t < dur:
        per = periodo * rng.uniform(0.7, 1.35)
        a = rng.uniform(0.5, 1.0)
        if rng.random() < 0.12 * (1 - 0.7 * calma):
            a *= 1.6 - 0.4 * calma                                   # onda maior
        sube, baixa, tau = per * rng.uniform(0.35, 0.5), per * rng.uniform(0.6, 0.9), rng.uniform(0.6, 1.4)
        L = int((sube + baixa + 2) * SR); tt = np.arange(L) / SR
        c = np.where(tt < sube, (tt / sube) ** 2, np.exp(-(tt - sube) / (baixa / 3)))
        d = np.clip(tt - sube, 0, None)
        e = np.where(tt < sube, 0.0, (1 - np.exp(-d / (0.08 + 0.25 * calma))) * np.exp(-d / tau))
        p = rng.uniform(0.25, 0.75); w = np.array([np.cos(p * np.pi / 2), np.sin(p * np.pi / 2)]) * 1.41
        _pon(e_corpo, (a * c[:, None] * w).astype(np.float32), int(t * SR))
        _pon(e_esc, (a * e[:, None] * w).astype(np.float32), int(t * SR))
        t += per
    sos_corpo = signal.butter(2, [60, 1000], 'bandpass', fs=SR, output='sos')
    sos_esc = signal.butter(2, [600, 6000 - 2000 * calma], 'bandpass', fs=SR, output='sos')
    sos_rumor = signal.butter(2, 350, fs=SR, output='sos')
    out = np.zeros((n, 2), np.float32)
    for ch in range(2):
        corpo = signal.sosfilt(sos_corpo, _rosa(n, rng)).astype(np.float32); corpo /= _rms(corpo)
        esc = signal.sosfilt(sos_esc, rng.standard_normal(n)).astype(np.float32); esc /= _rms(esc)
        rumor = signal.sosfilt(sos_rumor, _rosa(n, rng)).astype(np.float32); rumor *= 0.35 / _rms(rumor)
        out[:, ch] = corpo * (0.25 + e_corpo[:, ch]) + esc * 0.45 * e_esc[:, ch] + rumor
    return _pico(out)


def vento(dur, seed=23, calma=0.0, refachos=0.7, follas=0.5):
    """Vento suave entre as árbores: ruído rosa en dúas bandas (150-600 e 600-1800 Hz) cuxo peso se despraza cos
    refachos, e follas que rumorexan (2,5-7 kHz, en grans rápidos) cando sopra máis. Eventos: un refacho máis
    forte (+4 dB en 5-9 s; +2 dB ao durmir)."""
    rng = np.random.default_rng(seed)
    n = int(dur * SR)
    out = np.zeros((n, 2), np.float32)
    prof = refachos * (1 - 0.3 * calma)
    sos_b = signal.butter(2, [150, 600], 'bandpass', fs=SR, output='sos')
    sos_a = signal.butter(2, [600, 1800], 'bandpass', fs=SR, output='sos')
    sos_f = signal.butter(2, [2500, 7000], 'bandpass', fs=SR, output='sos')
    for ch in range(2):
        base = _rosa(n, rng)
        baixo = signal.sosfilt(sos_b, base); alto = signal.sosfilt(sos_a, base)
        m = _rafaga(n, rng, periodo=6.0, profundidade=prof)
        x = (baixo / _rms(baixo) * (1 - 0.5 * m) + alto / _rms(alto) * 0.6 * m) * _rafaga(n, rng, periodo=15.0, profundidade=0.6)
        gran = np.abs(_ruido_lento(n, rng, 0.05)) * m ** 2                   # follas: grans de 20-80 ms
        fol = signal.sosfilt(sos_f, rng.standard_normal(n)).astype(np.float32)
        out[:, ch] = x + fol / _rms(fol) * gran * follas * 0.35 * (1 - 0.4 * calma)
    g = np.zeros(n, np.float32)
    for t0 in _tempos(dur, 1.2, rng, calma, sep=15.0):
        L = int(rng.uniform(5, 9) * SR)
        _pon(g, np.hanning(L).astype(np.float32), int(t0 * SR))
    out *= _db((4 - 2 * calma) * np.clip(g, 0, 1))[:, None]
    return _pico(out)


# ------------------------------------------------------------------ fonte
def _burbulla(f0, tau, sube, L):
    tt = np.arange(L) / SR
    f = f0 * (1 + sube * tt / (3 * tau))
    return (np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt / tau)).astype(np.float32)


def fonte(dur, seed=53, calma=0.0, caudal=1.0, chorro=0.6):
    """Auga que corre nunha fonte ou nun regato: burbullas con ton que sobe (resonancia de Minnaert: as grandes
    graves e máis fortes), 12 tamaños entre 400 Hz e 3,2 kHz, `caudal`×120 por segundo co ritmo irregular do
    gorgolexo, e o chorro que cae no pío (ruído de 300 Hz-4 kHz que tremela). Eventos: un gorgolexo (15-40 burbullas
    grandes en menos dun segundo)."""
    rng = np.random.default_rng(seed)
    n = int(dur * SR)
    L = int(0.04 * SR)
    moldes = []
    for f0 in np.geomspace(400, 3200, 12):
        tau = rng.uniform(0.004, 0.012) * np.sqrt(1000 / f0)
        moldes.append(_burbulla(f0, tau, rng.uniform(0.1, 0.6), L) * (f0 / 1000) ** -0.5)
    sos_ch = signal.butter(2, [300, 4000], 'bandpass', fs=SR, output='sos')
    out = np.zeros((n, 2), np.float32)
    for ch in range(2):
        fluxo = np.clip(0.65 + 0.35 * _ruido_lento(n, rng, 0.4), 0.05, 1).astype(np.float32)
        b = np.zeros(n, np.float32)
        for k in moldes:
            b += signal.oaconvolve(_impulsos(n, 120 * caudal / 12, rng, 2.0, fluxo), k)[:n].astype(np.float32)
        b /= _rms(b)
        chx = signal.sosfilt(sos_ch, rng.standard_normal(n)).astype(np.float32)
        chx *= (0.75 + 0.25 * np.tanh(_ruido_lento(n, rng, 0.08))) / _rms(chx)
        out[:, ch] = b + chx * chorro
    ev = np.zeros(n, np.float32)
    for t0 in _tempos(dur, 2.0, rng, calma, sep=8.0):
        g = np.zeros(int(1.2 * SR), np.float32)
        for _ in range(int(rng.integers(15, 41))):
            _pon(g, _burbulla(rng.uniform(250, 600), rng.uniform(0.01, 0.025), rng.uniform(0.2, 0.8), int(0.08 * SR)),
                 int(rng.uniform(0, 0.9) * SR))
        _pon(ev, g, int(t0 * SR))
    if ev.any():
        ev *= _rms(out) * _db(4) / (np.abs(ev).max() + 1e-9) * 4 * _db(-6 * calma)
        out += _limitar(out, _pan(ev, rng.uniform(0.3, 0.7)), 12 - 7 * calma)
    return _pico(out)


# ------------------------------------------------------------------ xente (murmullo de voces)
_BANCO = {}
TIMBRES = (0.84, 0.89, 0.94, 1.0, 1.0, 1.06, 1.19, 1.26, 1.33)   # remostraxe da voz: >1 máis aguda (muller, rapaz)


def _banco_xente():
    """Frases do banco (mono, 16 kHz) ou [] se non está."""
    if 'frases' not in _BANCO:
        f, j = DATOS / 'xente-banco.ogg', DATOS / 'xente-banco.json'
        fr = []
        if f.exists() and j.exists():
            w, sr = sf.read(str(f), dtype='float32')
            meta = json.loads(j.read_text())
            if sr == 16000:
                fr = [w[x['ini']:x['fin']] for x in meta['frases']]
        _BANCO['frases'] = fr
    return _BANCO['frases']


def _murmullo_voz(m, sr, rng, fat):
    """Reserva sen banco: unha voz de murmullo con sílabas de fonte glotal (dente de serra, F0 95-125 Hz × fat) e dous
    formantes ao chou por sílaba."""
    out = np.zeros(m, np.float32)
    t, f0b = int(rng.uniform(0, 2) * sr), rng.uniform(95, 125) * fat
    while t < m:
        for _ in range(int(rng.integers(5, 15))):
            L = int(rng.uniform(0.1, 0.28) * sr)
            if t + L >= m:
                break
            src = (np.cumsum(np.full(L, f0b * rng.uniform(0.9, 1.15) / sr)) % 1.0) - 0.5
            y = np.zeros(L)
            for fmt, bw in ((rng.uniform(300, 800) * fat, 90), (rng.uniform(900, 2200) * fat, 120)):
                r = np.exp(-np.pi * bw / sr)
                y += signal.lfilter([1 - r], [1, -2 * r * np.cos(2 * np.pi * fmt / sr), r * r], src)
            out[t:t + L] += (y * np.hanning(L)).astype(np.float32)
            t += L + int(rng.uniform(0.0, 0.06) * sr)
        t += int(rng.uniform(0.3, 1.5) * sr)
    return out / (_rms(out) + 1e-9) * 0.08


def xente(dur, seed=31, calma=0.0, voces=None, corte=None):
    """Murmullo dun xentío: `voces` (6-12) voces do banco, cada unha co seu timbre (TIMBRES), volume e posición,
    falando con pausas ao chou; paso baixo por voz arredor de `corte` Hz (0,9-1,5 kHz; máis baixo ao durmir),
    reverberación de praza (RT60 0,9-1,6 s) e ondas lentas de densidade. Faise a 16 kHz e remostréase a 48 kHz."""
    rng = np.random.default_rng(seed)
    n, sr = int(dur * SR), 16000
    frases = _banco_xente()
    k = int(voces or rng.integers(6, 13))
    fc = float(corte or rng.uniform(900, 1500)) * (1 - 0.2 * calma)
    pre = 4 * sr
    m = int(dur * sr) + 1 + pre
    mix = np.zeros((m, 2), np.float32)
    for _ in range(k):
        fat = float(rng.choice(TIMBRES)) * rng.uniform(0.98, 1.02)
        if frases:
            fr_ = Fraction(1 / fat).limit_denominator(40)
            linea = np.zeros(m, np.float32)
            t, prev = int(rng.uniform(0, 3) * sr), -1
            while t < m:
                i = int(rng.integers(len(frases)))
                i = (i + 1) % len(frases) if i == prev else i
                prev = i
                x = signal.resample_poly(frases[i], fr_.numerator, fr_.denominator).astype(np.float32)
                _pon(linea, x * _db(rng.uniform(-3, 3)), t)
                t += len(x) + int((rng.uniform(0.2, 1.4) if rng.random() > 0.15 else rng.uniform(2, 6)) * sr)
        else:
            linea = _murmullo_voz(m, sr, rng, fat)
        fcv = min(0.45 * sr, fc * rng.uniform(0.8, 1.2))
        linea = signal.sosfilt(signal.butter(4, fcv, fs=sr, output='sos'), linea).astype(np.float32)
        mix += _pan(linea * _db(rng.uniform(-9, 0)), rng.uniform(0.15, 0.85))
    mix = _reverb(mix, _ir(rng.uniform(0.9, 1.6), sr, rng, pre=0.02, brillo=2500.0), 0.55)
    mix = signal.sosfilt(signal.butter(2, [150, min(1.2 * fc, 0.45 * sr)], 'bandpass', fs=sr, output='sos'), mix, axis=0)
    mix = mix[pre:].astype(np.float32)
    mix *= _db(3.0 * (1 - 0.5 * calma) * np.clip(_ruido_lento(len(mix), rng, 12.0, sr), -1.5, 1.5) / 1.5)[:, None]
    return _pico(signal.resample_poly(mix, 3, 1, axis=0)[:n])


# ------------------------------------------------------------------ noite
def _curuxa(rng):
    """Ouveo lonxano: 'uuu' longo, pausa, 'u' curto e 'uuuu' trémulo (≈480-620 Hz, cae un pouco)."""
    f = rng.uniform(480, 620)
    notas = [(0.0, 0.9, 0.0), (0.9 + rng.uniform(2.2, 3.4), 0.18, 0.0)]
    notas.append((notas[1][0] + 0.18 + rng.uniform(0.25, 0.45), 1.3, rng.uniform(6, 8)))
    L = int((notas[-1][0] + 1.6) * SR)
    x = np.zeros(L, np.float32)
    for t0, d, trem in notas:
        M = int(d * SR); tt = np.arange(M) / SR
        fr = f * (1 - 0.06 * tt / d)
        ph = 2 * np.pi * np.cumsum(fr) / SR
        env = np.minimum(1, tt / 0.06) * np.minimum(1, (d - tt) / 0.15) * (1 + 0.35 * np.sin(2 * np.pi * trem * tt))
        _pon(x, ((np.sin(ph) + 0.12 * np.sin(2 * ph)) * env).astype(np.float32), int(t0 * SR))
    return signal.sosfilt(signal.butter(2, 1200, fs=SR, output='sos'), x).astype(np.float32)


def noite(dur, seed=41, calma=0.0, grilos=5, curuxa=0.35):
    """Noite de verán: `grilos` grilos a distancias distintas (portadora 4,2-5 kHz; chirridos de 3-5 sílabas de 18 ms
    a ~31 por segundo, 1,8-3,2 chirridos/s, con paradas ao chou), aire de noite grave e, no 40 % dos tramos, o "uuu"
    do sapo parteiro (nota pura de 1,3-1,6 kHz cada 1,5-3 s). Eventos: `curuxa` ouveos por minuto (moi poucos)."""
    rng = np.random.default_rng(seed)
    n = int(dur * SR)
    aire = np.stack([signal.sosfilt(signal.butter(2, 300, fs=SR, output='sos'), _rosa(n, rng)) for _ in range(2)], 1)
    leito = (aire / _rms(aire) * 0.3).astype(np.float32)
    cri = np.zeros((n, 2), np.float32)
    for _ in range(max(2, int(round(grilos * (1 - 0.3 * calma))))):
        f0 = rng.uniform(4200, 5000); taxa = rng.uniform(1.8, 3.2); sil = int(rng.integers(3, 6))
        sl, gap = int(0.018 * SR), int(0.014 * SR)
        tt = np.arange(sl) / SR
        syl = (np.sin(2 * np.pi * f0 * (1 - 0.02 * tt / 0.018) * tt) + 0.1 * np.sin(4 * np.pi * f0 * tt)) * np.hanning(sl)
        chirp = np.concatenate([np.concatenate([syl, np.zeros(gap)]) for _ in range(sil)]).astype(np.float32)
        imp = np.zeros(n, np.float32); t = rng.uniform(0, 1 / taxa)
        while t < dur:
            imp[int(t * SR)] = _db(rng.uniform(-1.5, 1.5))
            t += (1 / taxa) * rng.uniform(0.9, 1.1) + (rng.uniform(2, 8) if rng.random() < 0.02 else 0)
        g = signal.oaconvolve(imp, chirp)[:n].astype(np.float32) * _db(rng.uniform(-18, -4))
        cri += _pan(signal.sosfilt(signal.butter(2, 6000, fs=SR, output='sos'), g).astype(np.float32), rng.uniform(0.1, 0.9))
    leito += cri / _rms(cri) * 0.4
    if rng.random() < 0.4:                                            # sapo parteiro
        sapo = np.zeros(n, np.float32); fs_ = rng.uniform(1300, 1600); t = rng.uniform(0, 2)
        M = int(0.12 * SR); nota = (np.sin(2 * np.pi * fs_ * np.arange(M) / SR) * np.hanning(M)).astype(np.float32)
        while t < dur:
            _pon(sapo, nota, int(t * SR)); t += rng.uniform(1.5, 3.0)
        leito += _pan(sapo / (_rms(sapo) + 1e-9) * 0.12, rng.uniform(0.2, 0.8))
    ev = np.zeros(n, np.float32)
    for t0 in _tempos(dur, curuxa, rng, calma, sep=30.0):
        _pon(ev, _curuxa(rng), int(t0 * SR))
    if ev.any():
        ev = _reverb(ev * _rms(leito) / (np.abs(ev).max() + 1e-9) * 6 * _db(-6 * calma),
                     _ir(1.5, SR, rng, brillo=2500.0), 0.5)
        ev = _pan(ev.mean(1), rng.uniform(0.15, 0.85))
        leito += _limitar(leito, ev, 12 - 7 * calma)
    return _pico(leito)


# ------------------------------------------------------------------ aldea
def _chio(rng, f1):
    d = rng.uniform(0.04, 0.07); M = int(d * SR); tt = np.arange(M) / SR
    f = f1 + rng.uniform(-800, 800) * tt / d
    ph = 2 * np.pi * np.cumsum(f) / SR
    return ((np.sin(ph) + 0.25 * np.sin(2 * ph)) * np.hanning(M)).astype(np.float32)


def _merlo(rng):
    """Frase de merlo: 4-9 notas asubiadas (1,6-3,2 kHz) con glisados e vibrato."""
    partes, t = [], 0.0
    for _ in range(int(rng.integers(4, 10))):
        d = rng.uniform(0.08, 0.3); M = int(d * SR); tt = np.arange(M) / SR
        f0 = rng.uniform(1600, 3200); f = f0 * (1 + rng.uniform(-0.3, 0.3) * tt / d) * (1 + 0.02 * np.sin(2 * np.pi * rng.uniform(20, 40) * tt))
        partes.append((t, (np.sin(2 * np.pi * np.cumsum(f) / SR) * np.hanning(M)).astype(np.float32)))
        t += d + rng.uniform(0.03, 0.08)
    x = np.zeros(int((t + 0.1) * SR), np.float32)
    for t0, p in partes:
        _pon(x, p * rng.uniform(0.6, 1.0), int(t0 * SR))
    return x


def _chocallo(rng, fb):
    """Un golpe de chocallo: parciais inharmónicos de metal (1; 1,48; 2,02; 2,63; 3,4 × fb) e o clic do badalo."""
    L = int(0.8 * SR); tt = np.arange(L) / SR
    x = np.zeros(L)
    for r, a, tau in ((1, 1, 0.35), (1.48, 0.6, 0.25), (2.02, 0.5, 0.2), (2.63, 0.35, 0.15), (3.4, 0.2, 0.1)):
        x += a * np.sin(2 * np.pi * fb * r * (1 + rng.normal(0, 0.01)) * tt + rng.uniform(0, 6.3)) * np.exp(-tt / tau)
    x[:int(0.002 * SR)] += rng.standard_normal(int(0.002 * SR)) * 0.5
    return x.astype(np.float32)


def aldea(dur, seed=61, calma=0.0, paxaros=1.0, chocallo=1.5):
    """Aldea de día: brisa suave, 2-4 pardais que chían en series curtas (3-5 kHz; como moito 13 dB sobre a brisa, 6 ao
    durmir) e un merlo que canta frases cada 6-15 s (`paxaros` escala as taxas; menos ao durmir). Eventos: `chocallo` series por minuto de 1-4 golpes dun
    chocallo de vaca (380-650 Hz) lonxe, con paso baixo e un pouco de reverberación."""
    rng = np.random.default_rng(seed)
    n = int(dur * SR)
    brisa = np.stack([signal.sosfilt(signal.butter(2, [200, 1500], 'bandpass', fs=SR, output='sos'), _rosa(n, rng))
                      for _ in range(2)], 1) * _rafaga(n, rng, periodo=10.0, profundidade=0.5)[:, None]
    leito = (brisa / _rms(brisa) * 0.3).astype(np.float32)
    pax = paxaros * (1 - 0.6 * calma)
    chios = np.zeros((n, 2), np.float32)
    for _ in range(int(rng.integers(2, 5))):
        b = np.zeros(n, np.float32); f1 = rng.uniform(3200, 4200); t = rng.uniform(0, 3)
        while t < dur:
            tc = t
            for _ in range(int(rng.integers(2, 7))):
                _pon(b, _chio(rng, f1) * rng.uniform(0.5, 1.0), int(tc * SR)); tc += rng.uniform(0.12, 0.35)
            t = tc + rng.uniform(1.5, 6.0) / max(pax, 0.1)
        chios += _pan(b * _db(rng.uniform(-14, -3)), rng.uniform(0.1, 0.9))
    ref = _rms(leito)
    ev = np.zeros((n, 2), np.float32)
    leito += _limitar(leito, (chios / (_rms(chios) + 1e-9) * 0.35 * _db(-4 * calma)).astype(np.float32), 13 - 7 * calma)
    merlo = np.zeros(n, np.float32)
    for t0 in _tempos(dur, 6.0 * pax, rng, 0.0, sep=5.0, primeiro=4.0):
        _pon(merlo, _merlo(rng), int(t0 * SR))
    if merlo.any():
        ev += _pan(merlo, rng.uniform(0.2, 0.8)) * ref * _db(6) / 0.7
    fb = rng.uniform(380, 650); ch_ = np.zeros(n, np.float32)
    for t0 in _tempos(dur, chocallo, rng, calma, sep=10.0):
        tc = t0
        for _ in range(int(rng.integers(1, 5))):
            _pon(ch_, _chocallo(rng, fb) * rng.uniform(0.6, 1.0), int(tc * SR)); tc += rng.uniform(0.4, 1.2)
    if ch_.any():
        ch_ = signal.sosfilt(signal.butter(2, 3000, fs=SR, output='sos'), ch_).astype(np.float32)
        ev += _reverb(ch_ * ref * _db(4) / (np.abs(ch_).max() + 1e-9) * 4, _ir(0.8, SR, rng, brillo=3000.0), 0.35) \
            * np.array([np.cos(0.6), np.sin(0.6)], np.float32)
    if ev.any():
        leito += _limitar(leito, ev * _db(-6 * calma), 12 - 7 * calma)
    return _pico(leito)


# ------------------------------------------------------------------ campas
# (razón á prima, amplitude, T60 en s para unha prima de 300 Hz): hum, prima, terceira menor, quinta, nominal,
# décima, undécima, duodécima e oitava superior (parciais típicos dunha campá de igrexa)
_PARCIAIS = ((0.5, 0.55, 9.0), (1.0, 0.5, 6.0), (1.2, 0.7, 4.5), (1.5, 0.3, 3.5), (2.0, 1.0, 3.0),
             (2.5, 0.4, 2.0), (2.67, 0.25, 1.8), (3.0, 0.3, 1.5), (4.0, 0.2, 1.0))


def _toque(f, rng, dur=7.0):
    """Un toque de campá: parciais inharmónicos (lixeiramente desafinados) en dobletes que baten a 0,3-1,5 Hz."""
    L = int(dur * SR); tt = np.arange(L) / SR
    x = np.zeros(L)
    k = np.sqrt(300 / f)
    for r, a, t60 in _PARCIAIS:
        fr = f * r * (1 + rng.normal(0, 0.004)); d = rng.uniform(0.3, 1.5)
        x += a * np.exp(-6.91 * tt / (t60 * k)) * (np.sin(2 * np.pi * fr * tt + rng.uniform(0, 6.3))
                                                    + 0.6 * np.sin(2 * np.pi * (fr + d) * tt + rng.uniform(0, 6.3)))
    M = int(0.01 * SR)
    x[:M] += signal.sosfilt(signal.butter(2, [1500, 5000], 'bandpass', fs=SR, output='sos'), rng.standard_normal(M)) * 0.3
    return (x * np.minimum(1, tt / 0.003)).astype(np.float32)


def campas(dur, seed=71, calma=0.0, prima=None):
    """Campás lonxanas: grupos de 3-9 toques lentos (cada 2,8-4,5 s; 2-4 ao durmir) cunha campá de prima `prima` Hz
    (190-420) e, nun terzo dos tramos, unha segunda campá unha cuarta por riba que alterna; pausas de 20-60 s entre
    grupos (máis longas ao durmir). Distancia: paso baixo a 2,5 kHz e reverberación grande (RT60 2,5-3,5 s). Entre
    toques só se oe o aire. O primeiro grupo empeza nos primeiros 2 s do tramo."""
    rng = np.random.default_rng(seed)
    n = int(dur * SR)
    aire = np.stack([signal.sosfilt(signal.butter(2, 700, fs=SR, output='sos'), _rosa(n, rng)) for _ in range(2)], 1)
    leito = (aire / _rms(aire) * 0.15).astype(np.float32)
    f = float(prima or rng.uniform(190, 420))
    dobre = rng.random() < 0.33
    tq = np.zeros(n, np.float32)
    t = rng.uniform(0.3, 2.0)
    while t < dur:
        k = max(2, int(round(rng.integers(3, 10) * (1 - 0.5 * calma))))
        iv = rng.uniform(2.8, 4.5)
        for j in range(k):
            fj = f * (4 / 3 if dobre and j % 2 else 1.0)
            _pon(tq, _toque(fj, rng) * rng.uniform(0.8, 1.0) * (0.8 if dobre and j % 2 else 1.0), int((t + j * iv) * SR))
        t += k * iv + rng.uniform(20, 60) * (1 + 1.5 * calma)
    tq = signal.sosfilt(signal.butter(2, 2500, fs=SR, output='sos'), tq).astype(np.float32)
    tq = _reverb(tq, _ir(rng.uniform(2.5, 3.5), SR, rng, pre=0.04, brillo=2500.0), 0.55)
    tq = _pan(tq.mean(1), rng.uniform(0.35, 0.65)) * (_rms(leito) * _db(18) / (_rms(tq) + 1e-9)) * _db(-6 * calma)
    return _pico(leito + _limitar(leito, tq.astype(np.float32), 12 - 7 * calma))


# ------------------------------------------------------------------ catálogo e mestura por escena
AMBIENTES = {'choiva': (choiva2, -18.0), 'lume': (lume, -21.0), 'mar': (mar, -20.0), 'vento': (vento, -23.0),
             'fonte': (fonte, -22.0), 'xente': (xente, -26.0), 'noite': (noite, -25.0), 'aldea': (aldea, -24.0),
             'campas': (campas, -24.0)}
# canto baixa cada tipo na zona de durmir (dB × calma): o que ten voces, cantos ou toques baixa máis
DURMIR_DB = {'xente': -5.0, 'campas': -4.0, 'aldea': -4.0, 'noite': -2.0, 'fonte': -1.0, 'vento': -1.0}
# variación entre tramos: cada tramo colle ao chou os seus parámetros neses rangos
VARIACION = {
    'choiva': {'gotas': (180.0, 340.0), 'medianas': (4.0, 10.0), 'pingas': (0.2, 0.5), 'refachos': (0.25, 0.45)},
    'lume': {'estalidos': (1.6, 3.4), 'lenos': (0.8, 2.0)},
    'mar': {'periodo': (8.0, 12.5)},
    'vento': {'refachos': (0.5, 0.85), 'follas': (0.3, 0.8)},
    'fonte': {'caudal': (0.7, 1.4), 'chorro': (0.3, 0.9)},
    'xente': {'voces': (6, 12), 'corte': (900.0, 1500.0)},
    'noite': {'grilos': (3, 8), 'curuxa': (0.25, 0.5)},
    'aldea': {'paxaros': (0.6, 1.4), 'chocallo': (0.8, 2.0)},
    'campas': {'prima': (190.0, 420.0)},
}
TRAMO_MAX = 150.0          # s: un tramo máis longo pártese en anacos (outra semente e outros parámetros) que se funden
FUNDIDO = (3.0, 8.0)       # s: fundido no gancho e ao durmir (interpólase coa calma)
TOPE_DB = (8.0, 12.0)      # dB: o ambiente nunca pasa da voz menos isto (sonoridade momentánea), gancho e durmir


def capas(tipo):
    """'lume+noite' -> ['lume', 'noite']; None ou '' -> []."""
    return [c.strip() for c in str(tipo or '').split('+') if c.strip()]


def ambiente_escena(n, tramos, voz_lufs=-17.0, rel_db=None, calma=None, semente=0):
    """Pista de ambiente (n x 2, 48 kHz) para os tramos [(t0, t1, tipo)] (tipo pode ter dúas capas: 'lume+noite').
    rel_db e calma: un valor por segundo (curva do embude e 0-1). Devolve (pista, info)."""
    meter = pyln.Meter(SR)
    r = np.zeros((n, 2), np.float32)
    dur = n / SR
    seg = np.arange(int(dur) + 2, dtype=float)
    rel_s = np.interp(seg, np.arange(len(rel_db)), np.asarray(rel_db, float)) if rel_db is not None else 0 * seg
    cal_s = np.clip(np.interp(seg, np.arange(len(calma)), np.asarray(calma, float)), 0, 1) if calma is not None else 0 * seg
    info, avisos = {}, []
    for k, (t0, t1, tipo) in enumerate(tramos):
        cs = capas(tipo)
        mal = [c for c in cs if c not in AMBIENTES]
        if mal:
            avisos.append(f'tramo {k} ({t0:.1f}-{t1:.1f} s): tipo descoñecido {mal}, ignórase')
        cs = [c for c in cs if c in AMBIENTES]
        if not cs or t1 <= t0:
            continue
        na = max(1, int(np.ceil((t1 - t0) / TRAMO_MAX - 1e-9)))
        cortes = np.linspace(t0, t1, na + 1)
        for j in range(na):
            a0, a1 = cortes[j], cortes[j + 1]
            cm = float(np.interp((a0 + a1) / 2, seg, cal_s))
            f = FUNDIDO[0] + (FUNDIDO[1] - FUNDIDO[0]) * cm
            fi, fo = (f if j == 0 else 8.0), (f if j == na - 1 else 8.0)
            s0, s1 = max(0.0, a0 - fi / 2), min(dur, a1 + fo / 2)
            i0, i1 = int(s0 * SR), int(s1 * SR); m = i1 - i0
            if m < SR // 2:
                continue
            x = np.zeros((m, 2), np.float32)
            for ci, capa in enumerate(cs):
                fn, rel = AMBIENTES[capa]
                sd = zlib.crc32(f'{semente}-{k}-{j}-{capa}'.encode()) & 0x7fffffff
                rng = np.random.default_rng(sd)
                par = {p: (int(rng.integers(lo, hi + 1)) if isinstance(lo, int) else float(rng.uniform(lo, hi)))
                       for p, (lo, hi) in VARIACION.get(capa, {}).items()}
                y = fn(max(m / SR, 1.0), seed=sd, calma=cm, **par)[:m]
                lu = meter.integrated_loudness(y)
                if not np.isfinite(lu):
                    continue
                y *= _db(voz_lufs + rel + DURMIR_DB.get(capa, 0.0) * cm - 3.0 * ci - lu)
                x[:len(y)] += y * _respira(len(y), rng)[:, None]
                d = info.setdefault(capa, {'rel_db': rel, 'tramos': 0, 'segundos': 0.0})
                d['tramos'] += (j == 0); d['segundos'] = round(d['segundos'] + a1 - a0, 1)
            x *= _db(np.interp(np.arange(i0, i1) / SR, seg, rel_s)).astype(np.float32)[:, None]   # curva do embude
            x = _tope(x, voz_lufs - (TOPE_DB[0] + (TOPE_DB[1] - TOPE_DB[0]) * cm))
            e = np.ones(m, np.float32)                                  # fundidos de potencia constante
            ni, no = min(m // 2, int((a0 + fi / 2 - s0) * SR)), min(m // 2, int((s1 - (a1 - fo / 2)) * SR))
            if ni > 0:
                e[:ni] = np.sin(np.linspace(0, np.pi / 2, ni))
            if no > 0:
                e[m - no:] *= np.cos(np.linspace(0, np.pi / 2, no))
            r[i0:i1] += x * e[:, None]
    # cambios de ambiente (conxunto de capas activas, por segundo, sen contar os fundidos)
    act = [frozenset() for _ in range(int(dur) + 1)]
    for t0, t1, tipo in tramos:
        cs = frozenset(c for c in capas(tipo) if c in AMBIENTES)
        for s in range(int(t0), min(len(act), int(np.ceil(t1)))):
            act[s] = act[s] | cs
    cambios = sum(1 for a, b in zip(act, act[1:]) if a != b)
    info['cambios'] = cambios
    info['cambios_por_10min'] = round(cambios / max(dur, 1) * 600, 1)
    # tramos longos sen voz limpa (aviso para quen escribe a lista de planos)
    run = 0
    for s, a in enumerate(act + [frozenset()]):
        if a:
            run += 1
        else:
            if run > 300:
                avisos.append(f'{run / 60:.1f} min seguidos con ambiente (ata {s} s): deixar algún plano con voz limpa')
            run = 0
    info['avisos'] = avisos
    return r, info


def pct_voz_limpa(vt, amb, umbral_voz_db=-35.0, umbral_amb_db=-45.0):
    """% do tempo con voz (tramas de 50 ms a menos de 35 dB do máximo da voz) sen ambiente audible (o ambiente por
    debaixo de 45 dB baixo o RMS medio da voz)."""
    fr = int(0.05 * SR); m = min(len(vt), len(amb)) // fr
    if m == 0:
        return 100.0
    ev = np.sqrt(np.square(vt[:m * fr], dtype=np.float32).reshape(m, fr).mean(1) + 1e-12)
    ea = np.concatenate([np.sqrt(np.square(amb[a:a + 1200 * fr], dtype=np.float32).sum(1)[:(min(m * fr, a + 1200 * fr) - a) // fr * fr]
                                 .reshape(-1, fr).mean(1) + 1e-12) for a in range(0, m * fr, 1200 * fr)])[:m]
    act = 20 * np.log10(ev) > 20 * np.log10(ev.max()) + umbral_voz_db
    if not act.any():
        return 100.0
    ref = np.sqrt(np.mean(ev[act] ** 2))
    con = 20 * np.log10(ea) > 20 * np.log10(ref) + umbral_amb_db
    return round(100 * float((act & ~con).sum()) / float(act.sum()), 1)


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
             rel_db=None, lume_tramos=None, rel_lume=-21.0, escena_tramos=None, calma=None, semente=0, out_amb=None):
    """voz: array mono 24 kHz (sen o offset). Devolve datos de sonoridade.
    Gauntlet 3: `ambiente='choiva2'` usa a choiva nova continua; `rel_db` (un valor por segundo, en dB) fai que o
    ambiente siga o embude; `lume_tramos` [(t0, t1)] engade o crepitar da lareira neses tramos.
    `ambiente='escena'` (D13 e D14): nada de ambiente continuo; cada tramo [(t0, t1, tipo)] de `escena_tramos` soa co
    seu tipo do catálogo (AMBIENTES; dúas capas con 'a+b'), coa súa semente e variación, fundidos longos, eventos
    cada vez máis escasos segundo `calma` (un valor 0-1 por segundo) e tope sobre a voz; o resto é voz limpa.
    `ambiente='ningun'`: só a voz. `out_amb`: garda tamén a pista de ambiente só (para medir)."""
    v = signal.resample_poly(voz, 2, 1).astype(np.float32)
    n = int(dur_total * SR)
    vt = np.zeros(n, np.float32); o = int(offset * SR)
    vt[o:o + len(v)] = v[:max(0, n - o)]
    meter = pyln.Meter(SR)
    l_v = meter.integrated_loudness(np.stack([v, v], 1))   # medida en estéreo, como se escoita
    vt *= 10 ** ((voz_lufs - l_v) / 20)
    info_escena = None
    if ambiente == 'escena':
        r, info_escena = ambiente_escena(n, escena_tramos or [], voz_lufs, rel_db, calma, semente)
    elif ambiente == 'ningun':
        r = np.zeros((n, 2), np.float32)
        info_escena = {'cambios': 0, 'cambios_por_10min': 0.0, 'avisos': []}
    else:
        r = choiva2(dur_total) if ambiente == 'choiva2' else choiva(dur_total)
        l_r = meter.integrated_loudness(r)
        r *= 10 ** ((voz_lufs + rel_choiva - l_r) / 20)
        if rel_db is not None:
            g = np.interp(np.arange(n) / SR, np.arange(len(rel_db)), np.asarray(rel_db, np.float32)).astype(np.float32)
            r *= (10 ** (g / 20))[:, None]
    fi, fo = int(3 * SR), int(6 * SR)
    env = np.ones(n, np.float32); env[:fi] = np.linspace(0, 1, fi); env[-fo:] = np.linspace(1, 0, fo)
    r *= env[:, None]
    info_lume = None
    if lume_tramos:
        fl = lume(dur_total)
        l_f = meter.integrated_loudness(fl)
        fl *= 10 ** ((voz_lufs + rel_lume - l_f) / 20)
        e_l = tramos_envolvente(n, lume_tramos)
        r += fl * (e_l * env)[:, None]
        info_lume = {'rel_lume_db': rel_lume, 'tramos': len(lume_tramos),
                     'segundos': round(float(e_l.sum()) / SR, 1)}
    if info_escena is not None:
        info_escena['pct_voz_limpa'] = pct_voz_limpa(vt, r)
    mix = r + vt[:, None]
    pk = np.abs(mix).max()
    esc = 0.89 / pk if pk > 0.89 else 1.0
    mix *= esc
    sf.write(out_mix, mix, SR, subtype='PCM_16')
    sf.write(out_voz, vt, SR, subtype='PCM_16')
    if out_amb:
        sf.write(out_amb, r * esc, SR, subtype='PCM_16')
    return {'lufs_voz_obxectivo': voz_lufs, 'choiva_rel_db': rel_choiva, 'ambiente': ambiente,
            'ambiente_rel_db_min_max': [round(float(np.min(rel_db)), 1), round(float(np.max(rel_db)), 1)] if rel_db is not None else None,
            'lume': info_lume, 'escena': info_escena,
            'lufs_mestura_pyloudnorm': round(meter.integrated_loudness(mix), 1), 'pico': round(float(np.abs(mix).max()), 3)}
