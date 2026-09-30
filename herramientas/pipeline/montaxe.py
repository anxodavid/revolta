"""Etapa MONTAXE: Ken Burns + brétema animada lixeira + viñeta + fundidos curtos, 1920x1080 a 24 fps.

Ronda 2: fundidos de 1,2 s (antes 3 s: a dobre exposición víase moito tempo) e brétema ao 6 % (antes 13 %,
que lavaba todas as imaxes cun ton verde-gris uniforme).

Gauntlet 3 (vídeo longo): cada proceso só carga as imaxes do seu treito (antes cargaba todas: ~10 MB por imaxe
e proceso), o fundido pode ser distinto en cada plano (`xf`, máis longo cara ao final: curva.py) e hai rótulos
(título do episodio e capítulos) debuxados con PIL e fundidos sobre a imaxe.

Os fotogramas xéranse en Python (PIL + numpy) en 4 procesos en paralelo, cada un codifica o seu
treito sen perdas visibles (x264 crf 14) e logo concaténanse e codifícase a versión final co audio
e cos subtítulos galegos como pista aparte (mov_text, lingua glg) ou queimados (--queimar-subtitulos).
"""
import os, subprocess, math
from multiprocessing import Pool
from pathlib import Path
import numpy as np
from PIL import Image, ImageFilter
import imageio_ffmpeg

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
OW, OH, FPS = 1920, 1080, 24
SW, SH = 2400, 1350          # imaxe fonte reescalada (1,25x a saída) para o movemento
ZOOM = 1.12                   # percorrido máximo do zoom/paneo
XF = 1.2                      # fundido encadeado entre escenas (s)
NEBOA = 0.06                  # opacidade máxima da brétema

_G = {}


def _fog(seed=3):
    rng = np.random.default_rng(seed)
    w = OW * 3
    acc = np.zeros((OH, w), np.float32)
    for (gh, gw, amp) in [(6, 48, 1.0), (12, 96, 0.5), (24, 192, 0.25)]:
        small = Image.fromarray((rng.random((gh, gw)) * 255).astype(np.uint8))
        acc += np.asarray(small.resize((w, OH), Image.BICUBIC), np.float32) / 255 * amp
    acc = (acc - acc.min()) / (acc.max() - acc.min())
    acc = np.clip((acc - 0.35) / 0.65, 0, 1) ** 1.5
    grad = np.linspace(0.45, 1.0, OH, dtype=np.float32)[:, None]
    return acc * grad


def _vignette():
    y, x = np.mgrid[0:OH, 0:OW].astype(np.float32)
    r = np.sqrt(((x - OW / 2) / (OW / 2)) ** 2 + ((y - OH / 2) / (OH / 2)) ** 2)
    return np.clip(1 - 0.28 * np.clip(r - 0.55, 0, None) ** 1.6, 0, 1)


def _init(imgs, idxs=None, rotulos=()):
    """Carga (reescaladas para o movemento) só as imaxes `idxs` (todas se é None) e prepara os rótulos."""
    _G['src'] = {}
    for i, p in enumerate(imgs):
        if idxs is not None and i not in idxs:
            continue
        im = Image.open(p).convert('RGB').resize((SW, SH), Image.LANCZOS)
        _G['src'][i] = im.filter(ImageFilter.UnsharpMask(radius=2, percent=40, threshold=2))
    _G['fog'] = _fog(); _G['vig'] = _vignette()[..., None]
    _G['rot'] = [(r, _rotulo(r)) for r in rotulos]


FONTES = ['/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf', '/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf']


def _fonte(tam, fonte=None):
    from PIL import ImageFont
    for f in ([fonte] if fonte else []) + [os.environ.get('MONTAXE_FONTE', '')] + FONTES:
        if f and os.path.exists(f):
            return ImageFont.truetype(f, tam)
    return ImageFont.load_default()


def _rotulo(r):
    """Capa RGBA (OHxOW) co texto do rótulo: liña pequena opcional (r['sub'], p. ex. "Capítulo II") e o título
    (r['texto']), centrados, en branco cálido cunha sombra suave para que se lean sobre calquera imaxe."""
    from PIL import ImageDraw
    capa = Image.new('RGBA', (OW, OH), (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    tam = r.get('tam', 64)
    f1, f2 = _fonte(tam, r.get('fonte')), _fonte(int(tam * 0.5), r.get('fonte'))
    liñas = [(r['sub'], f2)] if r.get('sub') else []
    liñas.append((r['texto'], f1))
    alto = sum(d.textbbox((0, 0), t, font=f)[3] + 18 for t, f in liñas)
    y = int(OH * r.get('y', 0.5)) - alto // 2
    sombra = Image.new('RGBA', (OW, OH), (0, 0, 0, 0)); ds = ImageDraw.Draw(sombra)
    for t, f in liñas:
        w = d.textbbox((0, 0), t, font=f)[2]
        x = (OW - w) // 2
        ds.text((x + 3, y + 3), t, font=f, fill=(0, 0, 0, 200))
        d.text((x, y), t, font=f, fill=(245, 238, 225, 255))
        y += d.textbbox((0, 0), t, font=f)[3] + 18
    sombra = sombra.filter(ImageFilter.GaussianBlur(6))
    return np.asarray(Image.alpha_composite(sombra, capa), np.float32)


def _crop(mov, u):
    """Caixa de recorte (x0, y0, x1, y1) na fonte para o progreso u en [0, 1]."""
    full_w, full_h = SW, SH
    if mov == 'zoom_in':
        z = 1 + (ZOOM - 1) * u
    elif mov == 'zoom_out':
        z = ZOOM - (ZOOM - 1) * u
    else:
        z = ZOOM
    w, h = full_w / z, full_h / z
    cx, cy = full_w / 2, full_h / 2
    mx, my = (full_w - w) / 2, (full_h - h) / 2
    if mov == 'pan_left':
        cx = full_w / 2 + mx * (1 - 2 * u)
    elif mov == 'pan_right':
        cx = full_w / 2 - mx * (1 - 2 * u)
    elif mov == 'pan_up':
        cy = full_h / 2 + my * (1 - 2 * u)
    return (cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2)


def _frame(t, esc, dur):
    acc = None
    for k, e in enumerate(esc):
        a0, a1 = e['vis']
        if not (a0 <= t < a1):
            continue
        u = (t - a0) / (a1 - a0)
        im = np.asarray(_G['src'][k].transform((OW, OH), Image.EXTENT, _crop(e['movemento'], u),
                                               resample=Image.BILINEAR), np.float32)
        alpha = 1.0
        xf = e.get('xf', XF)
        if k > 0 and t < e['b0'] + xf / 2:
            alpha = (t - (e['b0'] - xf / 2)) / xf
        acc = im if acc is None else acc * (1 - alpha) + im * alpha
    fog = _G['fog'][:, int(t * 10) % (OW * 2): int(t * 10) % (OW * 2) + OW]
    a = NEBOA * (0.75 + 0.25 * math.sin(t / 9.0))
    f = fog[..., None] * a
    out = acc * (_G['vig'] * (1 - f)) + f * np.array([215, 220, 226], np.float32)
    for r, capa in _G.get('rot', ()):
        if r['t0'] <= t < r['t1']:
            fd = r.get('fundido', 0.8)
            op = min(1.0, (t - r['t0']) / fd, (r['t1'] - t) / fd) * r.get('opacidade', 1.0)
            a_ = capa[..., 3:4] / 255 * op
            out = out * (1 - a_) + capa[..., :3] * a_
    fade = min(1.0, t / 2.5, (dur - t) / 4.0)
    if fade < 1:
        out *= max(fade, 0)
    return np.clip(out, 0, 255).astype(np.uint8)


def _chunk(args):
    idx, f0, f1, esc, dur, imgs, out, rotulos = args
    t0, t1 = f0 / FPS, f1 / FPS
    _init(imgs, {k for k, e in enumerate(esc) if e['vis'][0] <= t1 and e['vis'][1] >= t0},
          [r for r in rotulos if r['t0'] <= t1 and r['t1'] >= t0])
    cmd = [FFMPEG, '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{OW}x{OH}',
           '-r', str(FPS), '-i', '-', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '14',
           '-pix_fmt', 'yuv420p', out]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for fr in range(f0, f1):
        p.stdin.write(_frame(fr / FPS, esc, dur).tobytes())
    p.stdin.close(); p.wait()
    return out


def render(escenas, imgs, dur, audio, srt, out, work, procs=4, queimar=False, vbr='1100k', rotulos=(),
           bufsize=None):
    """escenas: [{'b0': inicio, 'b1': fin, 'movemento': ..., 'xf': fundido opcional}] sobre a liña de tempo final.
    rotulos: [{'t0', 't1', 'texto', 'sub' opcional, 'y' (0-1), 'tam'}] debuxados enriba da imaxe."""
    work = Path(work); work.mkdir(parents=True, exist_ok=True)
    esc = []
    for k, e in enumerate(escenas):
        xf_in = e.get('xf', XF)
        xf_out = escenas[k + 1].get('xf', XF) if k + 1 < len(escenas) else XF
        a0 = max(0.0, e['b0'] - xf_in / 2); a1 = min(dur, e['b1'] + xf_out / 2)
        esc.append({**e, 'vis': (a0, a1)})
    nf = int(round(dur * FPS))
    step = math.ceil(nf / procs)
    jobs = [(i, i * step, min(nf, (i + 1) * step), esc, dur, imgs, str(work / f'treito_{i}.mp4'), list(rotulos))
            for i in range(procs) if i * step < nf]
    with Pool(len(jobs)) as pool:
        parts = pool.map(_chunk, jobs)
    lst = work / 'treitos.txt'
    lst.write_text(''.join(f"file '{p}'\n" for p in parts))
    vf = []
    if queimar:
        vf = ['-vf', f"subtitles={srt}:force_style='FontSize=20,Outline=1,Shadow=0,MarginV=40'"]
    cmd = [FFMPEG, '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', str(lst), '-i', audio]
    if not queimar:
        cmd += ['-i', srt]
    cmd += ['-map', '0:v', '-map', '1:a'] + ([] if queimar else ['-map', '2:s']) + vf + [
        '-c:v', 'libx264', '-preset', 'slow', '-crf', '22', '-maxrate', vbr, '-bufsize', bufsize or '2200k',
        '-pix_fmt', 'yuv420p', '-r', str(FPS), '-c:a', 'aac', '-b:a', '128k', '-ar', '48000']
    if not queimar:
        cmd += ['-c:s', 'mov_text', '-metadata:s:s:0', 'language=glg']
    cmd += ['-metadata:s:a:0', 'language=glg', '-movflags', '+faststart', str(out)]
    subprocess.run(cmd, check=True)
    for p in parts:
        os.remove(p)
    return out
