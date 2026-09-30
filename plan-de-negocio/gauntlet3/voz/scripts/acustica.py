"""Medidas acústicas da voz (peza VOZ do Gauntlet 3), sen modelos grandes: velocidade, F0, enerxía, calidade.

Todo é automático. Úsase para as 40 grabacións humanas de referencia (REFS_DIR) e para a voz sintética.
Necesita praat-parselmouth (GPL-3.0, só para medir; instalado á parte: pip install --target $SCRATCH/voz/pylib
praat-parselmouth, e PYTHONPATH=$SCRATCH/voz/pylib).

- Sílabas: contador ortográfico do galego (núcleos vocálicos; hiato entre dúas vogais fortes ou con í/ú tónicas).
- Velocidade: sílabas/s sobre a duración da fala (sen silencios de inicio e fin) e "de articulación" (sen as pausas
  internas de >= 150 ms).
- F0 (Praat, autocorrelación, 60-400 Hz): mediana en Hz e, en semitons, desviación típica e rango p5-p95.
- Enerxía: RMS por tramas de 25 ms (paso 10 ms) nas tramas de fala: media en dBFS e dinámica p95-p10 (dB); LUFS.
- Calidade (voz cascada ou rouca): HNR medio (dB), jitter e shimmer locais (Praat), fracción de F0 < 75 Hz.
- Inclinación espectral (alpha ratio, dB): enerxía 1-5 kHz fronte a 50 Hz-1 kHz nas tramas sonoras. Máis baixa =
  voz máis suave (menos esforzo vocal).
"""
import re, math
import numpy as np
import soundfile as sf

VOG = 'aeiouáéíóúü'
FORTES = set('aeoáéóíú')


def silabas(texto):
    n = 0
    for pal in re.findall(r"[a-záéíóúüñç]+", texto.lower()):
        for g in re.findall(f'[{VOG}]+', pal):
            n += 1 + sum(1 for a, b in zip(g, g[1:]) if a in FORTES and b in FORTES)
    return n


def palabras(texto):
    return len(re.findall(r"[\wáéíóúüñç]+", texto))


def _tramas_rms(w, sr, win=0.025, hop=0.010):
    n, h = int(win * sr), int(hop * sr)
    if len(w) < n:
        w = np.pad(w, (0, n - len(w)))
    fr = np.lib.stride_tricks.sliding_window_view(w, n)[::h]
    return 10 * np.log10(np.mean(fr ** 2, axis=1) + 1e-12), fr


def medir(path, texto=None, f0_min=60, f0_max=400):
    import parselmouth
    from parselmouth.praat import call
    import pyloudnorm as pyln
    w, sr = sf.read(path, dtype='float32')
    if w.ndim > 1:
        w = w.mean(1)
    db, fr = _tramas_rms(w, sr)
    fala = db > db.max() - 35                      # tramas de fala (35 dB baixo o máximo)
    idx = np.where(fala)[0]
    i0, i1 = (idx[0], idx[-1]) if len(idx) else (0, len(db) - 1)
    dur_fala = (i1 - i0 + 1) * 0.010 + 0.015
    # pausas internas: >= 150 ms seguidos por debaixo de max-40 dB
    baixo = db[i0:i1 + 1] < db.max() - 40
    pausas, run = 0.0, 0
    for b in list(baixo) + [False]:
        if b:
            run += 1
        else:
            if run * 0.010 >= 0.150:
                pausas += run * 0.010
            run = 0
    r = {'dur_s': round(len(w) / sr, 3), 'dur_fala_s': round(dur_fala, 3), 'pausas_internas_s': round(pausas, 3),
         'pico': round(float(np.abs(w).max()), 4), 'mostras_saturadas': int(np.sum(np.abs(w) >= 0.99))}
    seg = w[int(i0 * 0.010 * sr): int((i1 + 1) * 0.010 * sr + 0.015 * sr)]
    if texto:
        sil, pal = silabas(texto), palabras(texto)
        r.update(silabas=sil, palabras=pal, sil_s=round(sil / dur_fala, 2),
                 sil_s_articulacion=round(sil / max(0.3, dur_fala - pausas), 2),
                 pal_min_fala=round(60 * pal / dur_fala, 1))
    d = db[fala]
    r.update(rms_db=round(float(10 * np.log10(np.mean(10 ** (d / 10)))), 2),
             dinamica_db=round(float(np.percentile(d, 95) - np.percentile(d, 10)), 2))
    try:
        r['lufs'] = round(float(pyln.Meter(sr).integrated_loudness(seg if len(seg) > sr * 0.5 else w)), 2)
    except Exception:
        r['lufs'] = None
    snd = parselmouth.Sound(seg.astype(np.float64), sampling_frequency=sr)
    pitch = snd.to_pitch_ac(time_step=0.01, pitch_floor=f0_min, pitch_ceiling=f0_max)
    f0 = pitch.selected_array['frequency']; f0 = f0[f0 > 0]
    if len(f0) > 5:
        st = 12 * np.log2(f0 / 100.0)
        r.update(f0_mediana_hz=round(float(np.median(f0)), 1), f0_media_st=round(float(st.mean()), 2),
                 f0_sd_st=round(float(st.std()), 2),
                 f0_rango_st=round(float(np.percentile(st, 95) - np.percentile(st, 5)), 2),
                 f0_baixo_75=round(float(np.mean(f0 < 75)), 3), sonoro_frac=round(len(f0) / max(1, pitch.n_frames), 3))
    try:
        hnr = snd.to_harmonicity_cc(time_step=0.01, minimum_pitch=75)
        hv = hnr.values[hnr.values > -200]
        r['hnr_db'] = round(float(hv.mean()), 2) if len(hv) else None
        pp = call(snd, 'To PointProcess (periodic, cc)', f0_min, f0_max)
        r['jitter_pct'] = round(100 * call(pp, 'Get jitter (local)', 0, 0, 0.0001, 0.02, 1.3), 3)
        r['shimmer_pct'] = round(100 * call([snd, pp], 'Get shimmer (local)', 0, 0, 0.0001, 0.02, 1.3, 1.6), 3)
    except Exception as e:
        r['erro_praat'] = str(e)[:80]
    # alpha ratio sobre as tramas de fala con enerxía (espectro de potencia medio)
    fr_f = fr[fala] * np.hanning(fr.shape[1])
    if len(fr_f):
        P = np.mean(np.abs(np.fft.rfft(fr_f, n=2048, axis=1)) ** 2, axis=0)
        fq = np.fft.rfftfreq(2048, 1 / sr)
        alto = P[(fq >= 1000) & (fq < min(5000, sr / 2))].sum(); baixo_ = P[(fq >= 50) & (fq < 1000)].sum()
        r['alpha_ratio_db'] = round(float(10 * np.log10(alto / baixo_)), 2)
    return r
