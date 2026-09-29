"""Controis automáticos (sen persoas): lingua, ASR/WER, sincronía, duración, sonoridade, imaxes, peso.

- ASR: faster-whisper co modelo galego de Nós proxectonos/whisper-large-v3-turbo-gl-v1.0
  convertido a CTranslate2 int8 (WHISPER_DIR). WER sobre a mestura final (voz + choiva) e sobre a
  voz soa. Sincronía: marcas de tempo por palabra do ASR contra os tempos de cada frase (SRT).
- Lingua: LanguageTool 6.8 gl-ES (inclúe hunspell galego) + regras de estilo do canal.
"""
import json, re, subprocess, statistics as st
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw
import imageio_ffmpeg

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()


def norm(t):
    t = t.lower().replace('’', "'")
    t = re.sub(r"[^\wáéíóúüñç ]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


# ---------------------------------------------------------------- lingua
def lingua(texto, dossier=''):
    """Avisos de LanguageTool. Os erros ortográficos (hunspell) en palabras que xa están no dossier de
    fontes (nomes propios verificados: Andrade, Lemos...) descártanse."""
    import language_tool_python as L
    tool = L.LanguageTool('gl-ES')
    ms = [m for m in tool.check(texto) if not (m.rule_id.startswith('HUNSPELL') and
          texto[m.offset:m.offset + m.error_length] in dossier)]
    res = [{'regra': m.rule_id, 'mensaxe': m.message, 'contexto': m.context,
            'suxestions': m.replacements[:3]} for m in ms]
    tool.close()
    return res


def estilo(texto, frases, aviso, palabras_obx):
    words = texto.split()
    fixas = lambda f: f['texto'] in aviso or f['texto'].startswith('Isto é Serán')
    long_ = [f['i'] for f in frases if not fixas(f) and not (8 <= len(f['texto'].split()) <= 25)]
    nomes = []
    for f in frases:
        ws = re.findall(r"\b[\wáéíóúüñç]+\b", f['texto'])
        nomes += [w for w in ws[1:] if w[0].isupper()]
    # nomes propios distintos por cada 110 palabras (≈1 min de narración)
    # nomes = secuencias de palabras en maiúscula (Rocha Forte conta como un); fóra aviso e fórmula
    vistos, fiestra, maxv, pos = set(), [], 0, 0
    for f in frases:
        ws = re.findall(r"\b[\wáéíóúüñç]+\b", f['texto'])
        if fixas(f):
            pos += len(ws); continue
        j = 0
        while j < len(ws):
            pos += 1
            if j > 0 and ws[j][0].isupper():
                k = j
                while k + 1 < len(ws) and ws[k + 1][0].isupper():
                    k += 1
                nome = ' '.join(ws[j:k + 1]); pos += k - j; j = k
                if nome not in vistos:
                    vistos.add(nome); fiestra.append(pos)
            fiestra = [p for p in fiestra if p > pos - 110]
            maxv = max(maxv, len(fiestra)); j += 1
    return {
        'palabras': len(words), 'palabras_obxectivo': palabras_obx,
        'desvio_palabras_pct': round(100 * (len(words) - palabras_obx) / palabras_obx, 1),
        'cifras': re.findall(r'\d+', texto),
        'signos_prohibidos': re.findall(r'[()\[\]"«»*#/]', texto),
        'preguntas': texto.count('?'),
        'palabras_vetadas': [w for w in ('imaxina', 'subscríbete', 'gústame', 'suscríbete') if w in texto.lower()],
        'aviso_literal': aviso in texto,
        'formula_literal': 'Isto é Serán, historia de Galicia para durmir.' in texto,
        'frases_fora_8_25': long_,
        'nomes_propios_distintos': sorted(set(nomes)),
        'max_nomes_novos_por_110_palabras': maxv,
    }


# ---------------------------------------------------------------- ASR
def asr(mix, voz, frases, tempos, whisper_dir, nth=4):
    import jiwer
    from faster_whisper import WhisperModel
    m = WhisperModel(whisper_dir, device='cpu', compute_type='int8', cpu_threads=nth)
    ref_words, ref_sent = [], []
    for f in frases:
        ws = norm(f['texto']).split()
        ref_words += ws; ref_sent += [f['i']] * len(ws)
    out = {}
    for nome, wav in (('mestura', mix), ('voz', voz)):
        segs, info = m.transcribe(wav, language='gl', beam_size=5, word_timestamps=(nome == 'mestura'),
                                  vad_filter=False, condition_on_previous_text=False)
        segs = list(segs)
        hyp_txt = ' '.join(s.text for s in segs)
        r = jiwer.process_words(' '.join(ref_words), norm(hyp_txt))
        res = {'wer': round(r.wer, 3), 'sub': r.substitutions, 'del': r.deletions, 'ins': r.insertions,
               'palabras_ref': len(ref_words), 'hipotese': hyp_txt.strip()}
        if nome == 'mestura':
            hw = []
            for s in segs:
                for w in (s.words or []):
                    for tok in norm(w.word).split():
                        hw.append((tok, w.start, w.end))
            r2 = jiwer.process_words(' '.join(ref_words), ' '.join(t for t, _, _ in hw))
            err = {f['i']: 0 for f in frases}
            dentro, total, desf = 0, 0, {}
            for ch in r2.alignments[0]:
                if ch.type == 'equal':
                    for k in range(ch.ref_end_idx - ch.ref_start_idx):
                        ri, hi = ch.ref_start_idx + k, ch.hyp_start_idx + k
                        si = ref_sent[ri]; t0, t1 = tempos[si]
                        _, ws, we = hw[hi]
                        total += 1
                        mid = (ws + we) / 2
                        if t0 - 0.5 <= mid <= t1 + 0.5:
                            dentro += 1
                        if ri == 0 or ref_sent[ri - 1] != si:
                            desf[si] = round(ws - t0, 2)
                else:
                    ri = min(ch.ref_start_idx, len(ref_sent) - 1)
                    n = max(ch.ref_end_idx - ch.ref_start_idx, ch.hyp_end_idx - ch.hyp_start_idx)
                    err[ref_sent[ri]] += n
            lens = {f['i']: len(norm(f['texto']).split()) for f in frases}
            per = {i: round(err[i] / lens[i], 2) for i in err}
            res['wer_por_frase'] = per
            res['frases_wer_mais_0_5'] = [i for i, v in per.items() if v > 0.5]
            res['sincronia'] = {
                'palabras_aliñadas': total,
                'pct_dentro_da_sua_frase': round(100 * dentro / max(total, 1), 1),
                'desfase_inicio_frase_s_mediana': round(st.median(desf.values()), 2) if desf else None,
                'desfase_inicio_frase_s_max_abs': round(max(abs(v) for v in desf.values()), 2) if desf else None,
                'frases_medidas': len(desf)}
        out[nome] = res
    return out


# ---------------------------------------------------------------- ficheiro final
def _decode_dur(mp4, stream):
    p = subprocess.run([FFMPEG, '-hide_banner', '-i', str(mp4), '-map', f'0:{stream}', '-f', 'null', '-'],
                       capture_output=True, text=True)
    ts = re.findall(r'time=(\d+):(\d+):([\d.]+)', p.stderr)
    h, m_, s = ts[-1]
    return int(h) * 3600 + int(m_) * 60 + float(s)


def ficheiro(mp4, dur_prevista):
    p = subprocess.run([FFMPEG, '-hide_banner', '-i', str(mp4)], capture_output=True, text=True).stderr
    vd, ad = _decode_dur(mp4, 'v:0'), _decode_dur(mp4, 'a:0')
    e = subprocess.run([FFMPEG, '-hide_banner', '-nostats', '-i', str(mp4), '-map', '0:a',
                        '-af', 'ebur128=peak=true', '-f', 'null', '-'], capture_output=True, text=True).stderr
    summ = e[e.rfind('Summary:'):]
    g = lambda k: float(re.search(k + r':\s+(-?[\d.]+)', summ).group(1))
    res = re.search(r'(\d{3,4})x(\d{3,4})', p)
    return {
        'mb': round(Path(mp4).stat().st_size / 1e6, 1),
        'resolucion': f'{res.group(1)}x{res.group(2)}' if res else None,
        'fps': float(re.search(r'([\d.]+) fps', p).group(1)),
        'pista_subtitulos': 'Subtitle: mov_text' in p,
        'dur_video_s': round(vd, 2), 'dur_audio_s': round(ad, 2), 'dur_prevista_s': round(dur_prevista, 2),
        'desfase_av_s': round(abs(vd - ad), 3),
        'lufs_integrado': g('I'), 'lra_lu': g('LRA'), 'pico_real_dbtp': g('Peak'),
    }


def imaxes(pngs):
    res, prev = [], None
    for p in pngs:
        a = np.asarray(Image.open(p).convert('L').resize((64, 36)), np.float32)
        sim = None
        if prev is not None:
            x, y = a.ravel() - a.mean(), prev.ravel() - prev.mean()
            sim = round(float(x @ y / (np.linalg.norm(x) * np.linalg.norm(y) + 1e-9)), 2)
        res.append({'imaxe': Path(p).name, 'luminancia': round(float(a.mean()), 1),
                    'contraste': round(float(a.std()), 1), 'similitude_coa_anterior': sim})
        prev = a
    return res


def folla_contactos(mp4, dur, out, n=12, cols=4, evitar=(), xf=0.0):
    """12 fotogramas a intervalos regulares. Se un cae dentro dun fundido encadeado (cortes `evitar`, fundido
    de `xf` s), desprázase ao fotograma limpo máis próximo (fóra do fundido) para que a folla mostre as imaxes."""
    tw, th = 480, 270
    sheet = Image.new('RGB', (tw * cols, th * (n // cols)), 'black')
    d = ImageDraw.Draw(sheet)
    for k in range(n):
        t = (k + 0.5) * dur / n
        for c in evitar:
            if abs(t - c) < xf / 2 + 0.15:
                t = c + (xf / 2 + 0.2 if t >= c else -(xf / 2 + 0.2))
        raw = subprocess.run([FFMPEG, '-loglevel', 'error', '-ss', f'{t:.2f}', '-i', str(mp4), '-frames:v', '1',
                              '-vf', f'scale={tw}:{th}', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'],
                             capture_output=True).stdout
        im = Image.frombytes('RGB', (tw, th), raw[:tw * th * 3])
        x, y = (k % cols) * tw, (k // cols) * th
        sheet.paste(im, (x, y))
        d.text((x + 8, y + 6), f'{int(t // 60)}:{int(t % 60):02d}', fill=(255, 255, 255))
    sheet.save(out, quality=88)
    return out
