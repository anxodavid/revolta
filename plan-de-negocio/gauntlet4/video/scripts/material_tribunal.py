"""Material do tribunal final do Gauntlet 4 (encargos/tribunal-final.md): v1 fronte a v2 a cegas.

Uso (Python do pipeline, que ten PIL; co candado se hai vídeo ou correlación):
    candado.sh $PY material_tribunal.py [--sen-video] [--sen-correlacion]

Escribe en plan-de-negocio/gauntlet4/tribunal/:
- cego/A-texto.txt, cego/B-texto.txt: os dous guions (A/B ao chou; a clave en $SCRATCH/tribunal4/clave.txt, fóra do repo
  ata o veredicto).
- cego/A-imaxes-K.jpg, cego/B-imaxes-K.jpg: 24 planos de cada versión ás mesmas fraccións do episodio (o plano que se
  ve en (i + 0,5)/24 da duración), a imaxe escollida (16:9) coas palabras que se oen nese plano debaixo.
- tiras-movemento-K.jpg (v2): catro fotogramas do vídeo ao longo de cada plano con movemento I2V e dalgúns de paralaxe.
- detalle-K.jpg (v2): o fotograma do medio de cada plano co número e o minuto:segundo.
- medidas.json: correlación CLIP-L (z) fronte ao texto en inglés da v1 e da v2 cun banco común, planos por modo de
  movemento, clips I2V na montaxe e duración media por fase.
"""
import argparse, json, os, random, subprocess, sys, textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

RAIZ = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(RAIZ / 'herramientas' / 'pipeline'))
import produccion as P                                                       # noqa: E402

G3V = RAIZ / 'plan-de-negocio' / 'gauntlet3' / 'video'
G4 = RAIZ / 'plan-de-negocio' / 'gauntlet4'
SAIDA = G4 / 'tribunal'
V2S = P.SCR / 'v2' / 's'
CLAVE = P.SCR / 'tribunal4' / 'clave.txt'
N_CEGO, POR_FOLLA = 24, 6
FONTE = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'


def fonte(t):
    try:
        return ImageFont.truetype(FONTE, t)
    except OSError:
        return ImageFont.load_default()


def hms(t):
    return f'{int(t // 60)}:{int(t % 60):02d}'


def v1():
    pl = json.loads((G3V / 'escenas-montadas.json').read_text())
    ims = {int(f.name[:3]) + 1: f for f in (G3V / 'imaxes').glob('[0-9][0-9][0-9]-*.jpg')}
    en = {p['n']: p['texto_en'] for p in json.loads((G4 / 'imaxe' / 'v1-texto-en.json').read_text())['planos']}
    return [dict(n=p['n'], b0=p['b0'], b1=p['b1'], texto=p['texto'], imaxe=ims.get(p['n']), texto_en=en.get(p['n']),
                 fase=p.get('fase')) for p in pl]


def v2():
    f = V2S / 'escenas-montadas.json'
    pl = json.loads((f if f.exists() else P.W / 'escenas.json').read_text())
    prod = {e['n']: e for e in P.ler(P.PROD)['escenas']}
    rev = P.ler(P.W / 'imaxes' / 'revision.json', {}); fs = P.fases()
    out = []
    for p in pl:
        e = prod[p['n']]
        r = rev.get(P.clave(e, fs.get(p['n'])))
        out.append(dict(n=p['n'], b0=p['b0'], b1=p['b1'], texto=p['texto'], fase=p.get('fase'),
                        imaxe=(P.W / 'imaxes' / r['ficheiro']) if r else None, texto_en=e.get('texto_en'),
                        animacion=e.get('animacion') or {}))
    return out


def no_tempo(pl, t):
    for p in pl:
        if p['b0'] <= t < p['b1']:
            return p
    return pl[-1]


def mostra(pl):
    dur = pl[-1]['b1']
    vistos, out = set(), []
    for i in range(N_CEGO):
        p = no_tempo(pl, (i + 0.5) / N_CEGO * dur)
        if p['n'] not in vistos:
            vistos.add(p['n']); out.append(p)
    return out


def tesela(im_path, texto, ancho=560):
    alto = round(ancho * 9 / 16)
    im = Image.open(im_path).convert('RGB')
    w, h = im.size
    c = min(w, round(h * 16 / 9)), min(h, round(w * 9 / 16))
    im = im.crop(((w - c[0]) // 2, (h - c[1]) // 2, (w + c[0]) // 2, (h + c[1]) // 2)).resize((ancho, alto), Image.LANCZOS)
    liñas = textwrap.wrap(texto, 62)[:5]
    t = Image.new('RGB', (ancho, alto + 8 + 18 * 5), 'white')
    t.paste(im, (0, 0))
    d = ImageDraw.Draw(t); f = fonte(14)
    for k, l in enumerate(liñas):
        d.text((6, alto + 4 + 18 * k), l, fill='black', font=f)
    return t


def follas_cego(nome, pl, dest):
    m = mostra(pl)
    for k in range(0, len(m), POR_FOLLA):
        ts = [tesela(p['imaxe'], p['texto']) for p in m[k:k + POR_FOLLA] if p['imaxe']]
        W, H = ts[0].size
        folla = Image.new('RGB', (2 * W + 10, 3 * (H + 10)), 'white')
        for j, t in enumerate(ts):
            folla.paste(t, ((j % 2) * (W + 10), (j // 2) * (H + 10)))
        folla.save(dest / f'{nome}-imaxes-{k // POR_FOLLA + 1}.jpg', quality=78, optimize=True)
    return [p['n'] for p in m]


def fotograma(mp4, t, ancho):
    import imageio_ffmpeg
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    alto = round(ancho * 9 / 16)
    r = subprocess.run([ff, '-v', 'error', '-ss', f'{t:.2f}', '-i', str(mp4), '-frames:v', '1', '-vf',
                        f'scale={ancho}:{alto}', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True)
    return Image.frombytes('RGB', (ancho, alto), r.stdout) if len(r.stdout) == ancho * alto * 3 else None


def tiras(pl, mp4, dest):
    sel = [p for p in pl if p['animacion'].get('modo') == 'i2v']
    sel += [p for p in pl if p['animacion'].get('modo') == 'paralaxe'][::3]
    sel.sort(key=lambda p: p['n'])
    A, por = 300, 8
    f = fonte(13)
    for k in range(0, len(sel), por):
        filas = sel[k:k + por]
        folla = Image.new('RGB', (4 * A + 150, len(filas) * (round(A * 9 / 16) + 6)), 'white')
        d = ImageDraw.Draw(folla)
        for j, p in enumerate(filas):
            y = j * (round(A * 9 / 16) + 6)
            d.text((4, y + 4), f"plano {p['n']}\n{hms(p['b0'])}\n{p['animacion'].get('modo')}", fill='black', font=f)
            for c, u in enumerate((0.1, 0.37, 0.63, 0.9)):
                im = fotograma(mp4, p['b0'] + u * (p['b1'] - p['b0']), A)
                if im:
                    folla.paste(im, (150 + c * A, y))
        folla.save(dest / f'tiras-movemento-{k // por + 1}.jpg', quality=78, optimize=True)


def detalle(pl, mp4, dest):
    A, por, cols = 320, 16, 4
    alto = round(A * 9 / 16)
    f = fonte(13)
    for k in range(0, len(pl), por):
        g = pl[k:k + por]
        folla = Image.new('RGB', (cols * A, ((len(g) + cols - 1) // cols) * (alto + 20)), 'white')
        d = ImageDraw.Draw(folla)
        for j, p in enumerate(g):
            x, y = (j % cols) * A, (j // cols) * (alto + 20)
            im = fotograma(mp4, (p['b0'] + p['b1']) / 2, A)
            if im:
                folla.paste(im, (x, y + 20))
            d.text((x + 4, y + 3), f"plano {p['n']} · {hms((p['b0'] + p['b1']) / 2)} · {p['fase']}", fill='black', font=f)
        folla.save(dest / f'detalle-{k // por + 1}.jpg', quality=78, optimize=True)


def correlacion(pa, pb):
    """z de cada plano co banco común (os textos das dúas versións), co correlacion.py da peza IMAXE."""
    import correlacion as C
    tmp = P.SCR / 'tribunal4'
    planos = {}
    for nome, pl in (('v1', pa), ('v2', pb)):
        f = tmp / f'planos-{nome}.json'
        f.write_text(json.dumps([{'n': p['n'], 'texto_en': p['texto_en'], 'ficheiro': str(p['imaxe'])}
                                 for p in pl if p['texto_en'] and p['imaxe']], ensure_ascii=False))
        planos[nome] = f
    res = {}
    for nome, outro in (('v1', 'v2'), ('v2', 'v1')):
        s = tmp / f'correlacion-{nome}.json'
        subprocess.run([sys.executable, str(Path(C.__file__)), '--planos', str(planos[nome]), '--imaxes', str(tmp),
                        '--banco', str(planos[outro]), '--saida', str(s)], check=True)
        res[nome] = json.loads(s.read_text())
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--sen-video', action='store_true')
    ap.add_argument('--sen-correlacion', action='store_true')
    a = ap.parse_args()
    cego = SAIDA / 'cego'; cego.mkdir(parents=True, exist_ok=True)
    CLAVE.parent.mkdir(parents=True, exist_ok=True)
    pa, pb = v1(), v2()
    if CLAVE.exists():
        A = CLAVE.read_text().split()[1]          # "A=v1" ou "A=v2" na primeira liña
        A = A.split('=')[1] if '=' in A else A
    else:
        A = random.SystemRandom().choice(['v1', 'v2'])
        CLAVE.write_text(f"clave A={A} B={'v2' if A == 'v1' else 'v1'}\n")
    vers = {'v1': (pa, G3V / 'guion.txt'), 'v2': (pb, G4 / 'guion' / 'guion-r2.txt')}
    mostras = {}
    for letra, nome in (('A', A), ('B', 'v2' if A == 'v1' else 'v1')):
        pl, guion = vers[nome]
        (cego / f'{letra}-texto.txt').write_text(guion.read_text())
        mostras[nome] = follas_cego(letra, pl, cego)
    med = {'mostra_cego': mostras,
           'planos': {'v1': len(pa), 'v2': len(pb)},
           'duracion_s': {'v1': round(pa[-1]['b1'], 1), 'v2': round(pb[-1]['b1'], 1)}}
    fases = {}
    for nome, pl in (('v1', pa), ('v2', pb)):
        d = {}
        for p in pl:
            d.setdefault(p['fase'], []).append(p['b1'] - p['b0'])
        fases[nome] = {k: {'planos': len(v), 'duracion_media_s': round(sum(v) / len(v), 1)} for k, v in d.items()}
    med['por_fase'] = fases
    modos = {}
    for p in pb:
        modos[p['animacion'].get('modo', 'ken burns')] = modos.get(p['animacion'].get('modo', 'ken burns'), 0) + 1
    med['v2_modo_na_lista'] = modos
    porta = P.ler(P.PORTA, {})
    med['v2_porta_video'] = {'clips_medidos': len(porta), 'pasaron': sum(1 for r in porta.values() if r.get('ok'))}
    mp4 = V2S / 'video.mp4'
    if not a.sen_video and mp4.exists():
        tiras(pb, mp4, SAIDA)
        detalle(pb, mp4, SAIDA)
    if not a.sen_correlacion:
        c = correlacion(pa, pb)
        med['correlacion'] = {k: v['resumo'] for k, v in c.items()}
    (SAIDA / 'medidas.json').write_text(json.dumps(med, ensure_ascii=False, indent=1) + '\n')
    print(json.dumps({k: med[k] for k in ('planos', 'duracion_s', 'v2_modo_na_lista', 'v2_porta_video')}, ensure_ascii=False))


if __name__ == '__main__':
    main()
