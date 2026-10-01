"""Medidas da peza SON (Gauntlet 3). Todas automáticas; ningunha substitúe a escoita.

- DNSMOS P.835 (Microsoft, licenza MIT; modelos ONNX do paquete `speechmos` 0.0.1.1, instalado fóra do venv en
  $SCRATCH/son/pylib): SIG (calidade da voz), BAK (canto molesta o fondo: 5 = nada), OVRL (global) e P.808, en
  fiestras de 9,01 s cada 1 s, a 16 kHz mono. Mide ruído como defecto: calquera ambiente baixa BAK por deseño.
- WER co Whisper galego de Nós (faster-whisper, WHISPER_DIR), coas mesmas opcións que qa.asr.
- Picos na zona de durmir sobre a pista de ambiente soa: sonoridade K (BS.1770) en 50 ms e en 400 ms fronte á
  mediana local de 400 ms (±3 s): canto sobresae un evento do seu propio fondo; e "sustos": arrinques rápidos (+6 dB
  en 200 ms) que quedan máis de 10 dB por riba do fondo local. Os fundidos desde o silencio non contan.
- Variedade do fondo: espectro en bandas de terzo de oitava (100 Hz-8 kHz) en fiestras de 5 s con ambiente;
  variación espectral = distancia RMS (dB) media de cada fiestra ao espectro medio; monotonía = % de pares de
  fiestras separadas máis de 60 s cuxo espectro difire menos de 3 dB RMS (soan igual).
"""
import os, sys
import numpy as np, soundfile as sf
from scipy import signal
from scipy.ndimage import median_filter, uniform_filter1d

REPO = '/home/user/revolta'
sys.path.insert(0, REPO + '/herramientas/pipeline')
import son  # noqa: E402


# ------------------------------------------------------------------ utilidades
def a16k_mono(x, sr):
    """Mestura mono a 16 kHz (media das canles)."""
    m = x.mean(1) if x.ndim == 2 else x
    if sr != 16000:
        from fractions import Fraction
        f = Fraction(16000, sr)
        m = signal.resample_poly(m, f.numerator, f.denominator)
    return m.astype(np.float32)


def perfil(x):
    """Sonoridade K en 50 ms e 400 ms (LUFS, 100 valores por segundo) dunha pista a 48 kHz."""
    p = son._potencia_k(x)
    l50 = -0.691 + 10 * np.log10(np.maximum(uniform_filter1d(p, 5, mode='constant'), 0) + 1e-20)
    l400 = -0.691 + 10 * np.log10(np.maximum(uniform_filter1d(p, 40, mode='constant'), 0) + 1e-20)
    return l50, l400


def picos(amb, t0=0.0, t1=None, suelo_lufs=-70.0):
    """Picos dos eventos da pista de ambiente (48 kHz) entre t0 e t1 s, só onde hai ambiente arredor (±3 s: os
    fundidos desde o silencio non contan). Fondo = mediana local da sonoridade en 400 ms (±3 s). Devolve a mediana
    (LUFS), o pico en 400 ms e en 50 ms sobre o fondo (dB) e os sustos: arrinques rápidos (+6 dB en 200 ms) que
    quedan máis de 10 dB por riba do fondo."""
    l50, l400 = perfil(amb)
    a, b = int(t0 * 100), int((t1 if t1 is not None else len(l400) / 100) * 100)
    l50, l400 = l50[a:b], l400[a:b]
    con = l400 > suelo_lufs
    if con.sum() < 100:
        return {'segundos_con_ambiente': round(float(con.sum()) / 100, 1)}
    val = con & (uniform_filter1d(con.astype(float), 601, mode='nearest') > 0.95)
    fondo = median_filter(np.maximum(l400, np.median(l400[con]) - 25), 601, mode='nearest')
    d50, d400 = l50 - fondo, l400 - fondo
    subida = l50 - np.concatenate([np.full(20, l50[0]), l50[:-20]])
    susto = val & (d50 > 10) & (subida > 6)
    arr = np.flatnonzero(np.diff(susto.astype(int)) == 1)
    if not val.any():
        return {'segundos_con_ambiente': round(float(con.sum()) / 100, 1)}
    return {'segundos_con_ambiente': round(float(con.sum()) / 100, 1), 'mediana_lufs': round(float(np.median(l400[con])), 1),
            'pico_400ms_sobre_fondo_db': round(float(d400[val].max()), 1),
            'pico_50ms_sobre_fondo_db': round(float(d50[val].max()), 1),
            'p99_50ms_sobre_fondo_db': round(float(np.percentile(d50[val], 99)), 1), 'sustos_10db': int(len(arr) + susto[0])}


def _bandas(sr):
    fc = 1000 * 2 ** (np.arange(-10, 10) / 3)                 # 100 Hz ... 8 kHz, terzos de oitava
    return fc[(fc >= 100) & (fc <= min(8000, sr / 2 / 1.13))]


def espectros(x16, sr=16000, fiestra=5.0, suelo_db=-75.0):
    """Nivel (dB) por banda de terzo de oitava en fiestras de `fiestra` s; só fiestras con ambiente."""
    fc = _bandas(sr)
    L = int(fiestra * sr); out, ts = [], []
    for k in range(0, len(x16) - L + 1, L):
        f, P = signal.welch(x16[k:k + L], sr, nperseg=4096)
        lv = []
        for c in fc:
            s = (f >= c / 2 ** (1 / 6)) & (f < c * 2 ** (1 / 6))
            lv.append(10 * np.log10(P[s].sum() + 1e-20))
        lv = np.array(lv)
        if 10 * np.log10(P.sum() + 1e-20) > suelo_db:
            out.append(lv); ts.append(k / sr)
    return np.array(out), np.array(ts)


def variedade(x16, sr=16000):
    """Variación espectral (dB) e monotonía (%) da pista de ambiente a 16 kHz mono."""
    E, ts = espectros(x16, sr)
    if len(E) < 3:
        return {'fiestras_con_ambiente': int(len(E))}
    En = E - E.mean(1, keepdims=True)                          # forma do espectro (sen o nivel)
    media = En.mean(0)
    var = float(np.sqrt(((En - media) ** 2).mean(1)).mean())
    iguais, pares = 0, 0
    for i in range(len(En)):
        for j in range(i + 1, len(En)):
            if ts[j] - ts[i] >= 60:
                pares += 1
                iguais += float(np.sqrt(((En[i] - En[j]) ** 2).mean())) < 3.0
    niv = E.mean(1)
    return {'fiestras_con_ambiente': int(len(E)), 'variacion_espectral_db': round(var, 2),
            'monotonia_pct': round(100 * iguais / pares, 1) if pares else None,
            'desviacion_nivel_db': round(float(np.std(niv)), 2)}


# ------------------------------------------------------------------ DNSMOS
class DNSMOS:
    """DNSMOS P.835 + P.808 cos ONNX de speechmos (mesmo cálculo que speechmos.dnsmos, pero devolve cada fiestra)."""

    def __init__(self, nth=2):
        import onnxruntime as ort
        import speechmos
        d = os.path.join(os.path.dirname(speechmos.__file__), 'dnsmos_models')
        o = ort.SessionOptions(); o.intra_op_num_threads = nth; o.inter_op_num_threads = 1
        self.p835 = ort.InferenceSession(os.path.join(d, 'sig_bak_ovr.onnx'), o, providers=['CPUExecutionProvider'])
        self.p808 = ort.InferenceSession(os.path.join(d, 'model_v8.onnx'), o, providers=['CPUExecutionProvider'])

    @staticmethod
    def _poly(sig, bak, ovr):
        return (np.poly1d([-0.08397278, 1.22083953, 0.0052439])(sig), np.poly1d([-0.13166888, 1.60915514, -0.39604546])(bak),
                np.poly1d([-0.06766283, 1.11546468, 0.04602535])(ovr))

    def fiestras(self, x16):
        """[(t0, SIG, BAK, OVRL, P808)] en fiestras de 9,01 s cada 1 s (audio mono a 16 kHz, -1..1)."""
        import librosa
        L = int(9.01 * 16000); out = []
        for k in range(0, max(1, len(x16) - L + 1), 16000):
            seg = x16[k:k + L]
            if len(seg) < L:
                break
            mel = librosa.feature.melspectrogram(y=seg[:-160], sr=16000, n_fft=321, hop_length=160, n_mels=120)
            mel = ((librosa.power_to_db(mel, ref=np.max) + 40) / 40).T.astype(np.float32)[None]
            p808 = float(self.p808.run(None, {'input_1': mel})[0][0][0])
            s, b, o = self.p835.run(None, {'input_1': seg.astype(np.float32)[None]})[0][0]
            s, b, o = self._poly(s, b, o)
            out.append((k / 16000, float(s), float(b), float(o), p808))
        return out

    @staticmethod
    def resumo(fs, t0=0.0, t1=1e9):
        v = np.array([f[1:] for f in fs if f[0] >= t0 and f[0] + 9.01 <= t1 + 0.5])
        if not len(v):
            return None
        m = v.mean(0)
        return {'SIG': round(float(m[0]), 3), 'BAK': round(float(m[1]), 3), 'OVRL': round(float(m[2]), 3),
                'P808': round(float(m[3]), 3), 'fiestras': int(len(v))}


# ------------------------------------------------------------------ ASR
class ASR:
    def __init__(self, nth=4):
        from faster_whisper import WhisperModel
        self.m = WhisperModel(os.environ['WHISPER_DIR'], device='cpu', compute_type='int8', cpu_threads=nth)

    def transcribir(self, x16):
        segs, _ = self.m.transcribe(x16, language='gl', beam_size=5, vad_filter=False, condition_on_previous_text=False)
        segs = list(segs)
        return ' '.join(s.text for s in segs).strip(), segs

    def wer(self, x16, ref):
        import jiwer, qa
        hip, _ = self.transcribir(x16)
        r = jiwer.process_words(qa.norm(ref), qa.norm(hip))
        return {'wer': round(r.wer, 4), 'erros': r.substitutions + r.deletions + r.insertions,
                'palabras_ref': len(qa.norm(ref).split()), 'hipotese': hip}
