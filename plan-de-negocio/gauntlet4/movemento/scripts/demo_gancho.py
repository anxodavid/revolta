"""Demo do gancho da v1 animado (planos 1-22, 0:00-1:55 de `gauntlet3/video/escenas-montadas.json`): as mesmas
imaxes (coa mesma gradación da v1) e o mesmo audio (tirado de `gauntlet3/video/avance/avance-720p.mp4`), pero sen
Ken Burns: I2V nos planos con persoas onde mellor saíu e paralaxe 2,5D con efectos no resto. A animación de cada
plano está en `demo-gancho-planos.json` (dato, non código).

Uso (venv principal; a montaxe colle o candado de CPU por fóra):
    python demo_gancho.py preparar      # imaxes graduadas (PNG) e lista de traballos I2V (i2v.json)
    python demo_gancho.py montar        # profundidade, máscaras e montaxe -> demo-gancho.mp4 (temporal + renomear)
Os clips I2V fanse entre os dous pasos con herramientas/pipeline/movemento_i2v.py (texto e xerar) sobre i2v.json.
"""
import glob, json, os, subprocess, sys, time
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(RAIZ / 'herramientas' / 'pipeline'))
G3 = RAIZ / 'plan-de-negocio' / 'gauntlet3' / 'video'
AQUI = RAIZ / 'plan-de-negocio' / 'gauntlet4' / 'movemento'
SCR = Path(os.environ.get('SCRATCH', '/tmp/revolta-scratch'))
W = SCR / 'video' / 'demo'
ULTIMO = int(os.environ.get('DEMO_ULTIMO', '22'))


def escenas():
    esc = json.loads((G3 / 'escenas-montadas.json').read_text())
    return esc


def preparar():
    from PIL import Image
    import imaxes
    W.mkdir(parents=True, exist_ok=True)
    (W / 'orixe').mkdir(exist_ok=True)
    esc = escenas()
    pngs = []
    for e in esc:                                   # todas, para que a gradación (suavizada) sexa a da v1
        j = sorted(glob.glob(str(G3 / 'imaxes' / f"{e['n'] - 1:03d}-*.jpg")))[0]
        p = W / 'orixe' / (Path(j).stem + '.png')
        if not p.exists():
            Image.open(j).convert('RGB').save(p)
        pngs.append(str(p))
    grad = imaxes.graduar(pngs, W / 'graduadas', escenas=esc)
    plan = json.loads((AQUI / 'demo-gancho-planos.json').read_text())
    i2v = []
    for e, g in zip(esc, grad):
        an = plan.get(str(e['n']))
        if e['n'] <= ULTIMO and an and an.get('modo') == 'i2v':
            i2v.append({'n': e['n'], 'imaxe': g, 'accion': an['accion'], 'i2v': an.get('i2v')})
    (W / 'i2v.json').write_text(json.dumps(i2v, ensure_ascii=False, indent=1))
    print(f'{len(grad)} imaxes graduadas; {len(i2v)} clips I2V en {W / "i2v.json"}')


def montar():
    import imageio_ffmpeg
    import montaxe
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    esc = [e for e in escenas() if e['n'] <= ULTIMO]
    plan = json.loads((AQUI / 'demo-gancho-planos.json').read_text())
    grad = []
    for e in esc:
        grad.append(sorted(glob.glob(str(W / 'graduadas' / f"{e['n'] - 1:03d}-*.png")))[0])
    dur = round(esc[-1]['b1'], 3)
    # audio da v1 (os primeiros `dur` segundos do avance), cun fundido curto ao final
    wav = W / 'audio.wav'
    subprocess.run([ff, '-y', '-v', 'error', '-i', str(G3 / 'avance' / 'avance-720p.mp4'), '-t', str(dur), '-vn',
                    '-af', f'afade=t=out:st={dur - 1.2}:d=1.2', '-ar', '48000', '-ac', '2', str(wav)], check=True)
    # subtítulos da v1 ata `dur`
    bloques = (G3 / 'subtitulos.gl.srt').read_text().strip().split('\n\n')
    def seg(ts):
        h, m, s = ts.split(':'); return int(h) * 3600 + int(m) * 60 + float(s.replace(',', '.'))
    sel = [b for b in bloques if seg(b.split('\n')[1].split(' --> ')[0]) < dur]
    srt = W / 'subtitulos.srt'
    srt.write_text('\n\n'.join(sel) + '\n')
    rot = [r for r in json.loads((G3 / 'rotulos.json').read_text()) if r['t0'] < dur]
    for r in rot:
        r['t1'] = min(r['t1'], dur)
    planos = []
    for e in esc:
        x = {'b0': e['b0'], 'b1': min(e['b1'], dur), 'movemento': e['movemento'], 'xf': e['xf'], 'n': e['n']}
        an = plan.get(str(e['n']))
        if an:
            an = dict(an)
            if an.get('modo') == 'i2v':
                an.setdefault('i2v', None)
            x['animacion'] = an
        planos.append(x)
    out = AQUI / 'demo-gancho.mp4'
    tmp = W / 'demo-gancho.tmp.mp4'
    t0 = time.time()
    montaxe.render(planos, grad, dur, str(wav), str(srt), str(tmp), W / 'montaxe', procs=4, vbr='1700k',
                   rotulos=rot, bufsize='3400k')
    t_render = time.time() - t0
    r = subprocess.run([ff, '-v', 'error', '-i', str(tmp), '-f', 'null', '-'], capture_output=True, text=True)
    if r.stderr.strip():
        raise SystemExit(f'o MP4 non descodifica limpo: {r.stderr[:300]}')
    mb = tmp.stat().st_size / 1e6
    if mb > 30:
        raise SystemExit(f'{mb:.1f} MB: máis de 30 MB')
    os.replace(tmp, out)
    info = {'dur_s': dur, 'mb': round(mb, 1), 's_montaxe': round(t_render, 1),
            's_por_segundo_de_video': round(t_render / dur, 2)}
    (AQUI / 'probas' / 'medidas-demo.json').write_text(json.dumps(info, indent=1))
    print(json.dumps(info))


if __name__ == '__main__':
    {'preparar': preparar, 'montar': montar}[sys.argv[1]]()
