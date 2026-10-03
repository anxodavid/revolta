"""Follas para a segunda ollada aos planos rexenerados (Gauntlet 4, revisor de imaxes r2, axente Claude).

Uso ($SCRATCH/tts/venv/bin/python, ten PIL; con nice -n 19):
    follas_revision_r2.py INTENTOS.json POR_FOLLA SAIDA_DIR [VISTAS_DIR]
INTENTOS.json é a saída de `produccion.py intentos`. Cada plano: o intento que escolleu a porta a 640 px, os outros
intentos a 320 px ao lado, e debaixo o número, o tipo, o texto que se oe, o prompt novo, a acción I2V e o que dixo a
porta en cada intento. revision.json só se le (para saber se a porta aprobou). Escribe JPEG <= 400 KB; con
VISTAS_DIR garda tamén recortes de 2 planos (para miralos sen reducir). ETIQUETAS={n: decisión} engade a decisión.
"""
import json, os, sys, textwrap
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

SCR = Path('/tmp/claude-0/-home-user-revolta/c92eba35-e89d-5d11-bb3d-f517a84dab48/scratchpad')
IMX = SCR / 'v2' / 'w' / 'imaxes'
REV = IMX / 'revision.json'                       # só lectura
PROD = Path(__file__).resolve().parents[1] / 'escenas-v2-produccion.json'
F = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
FB = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
f13, fb17 = ImageFont.truetype(F, 13), ImageFont.truetype(FB, 17)
_E = Path(os.environ.get('ETIQUETAS', SCR / 'revimx-r2' / 'etiquetas.json'))
ETIQ = json.loads(_E.read_text()) if _E.exists() else {}
W_MAIN, H_MAIN, W_ALT, H_ALT, GAP = 640, 366, 320, 183, 6
W_BLOCK = W_MAIN + GAP + W_ALT
H_TEXT = 156
H_BLOCK = H_MAIN + H_TEXT + 10


def curto(p):
    return p.replace('negativo do plano: ', 'neg: ').replace(' (CLIP)', '')


def main():
    intentos, por, saida = json.loads(Path(sys.argv[1]).read_text()), int(sys.argv[2]), Path(sys.argv[3])
    vistas = Path(sys.argv[4]) if len(sys.argv) > 4 else None
    saida.mkdir(parents=True, exist_ok=True)
    if vistas:
        vistas.mkdir(parents=True, exist_ok=True)
    rev = json.loads(REV.read_text())
    esc = {e['n']: e for e in json.loads(PROD.read_text())['escenas']}
    ns = sorted(int(n) for n in intentos)
    for i0 in range(0, len(ns), por):
        grupo = ns[i0:i0 + por]
        H = 34 + len(grupo) * H_BLOCK
        folla = Image.new('RGB', (W_BLOCK + 16, H), (24, 24, 24))
        d = ImageDraw.Draw(folla)
        d.text((8, 8), f'Revisión de imaxes r2 (axente Claude) · planos rexenerados {grupo[0]}-{grupo[-1]} · grande = '
                       'escollida pola porta; pequenas = outros intentos', font=f13, fill=(200, 200, 200))
        for j, n in enumerate(grupo):
            r, e = intentos[str(n)], esc[n]
            ok = rev[r['clave']]['ok']
            y = 34 + j * H_BLOCK
            fs = [x['ficheiro'] for x in r['intentos']]
            esc_f = r['escollido_pola_porta']
            idx = {f: f.rsplit('-', 1)[1].split('.')[0] for f in fs}   # número do intento (o do ficheiro)
            im = Image.open(IMX / esc_f).convert('RGB').resize((W_MAIN, H_MAIN), Image.LANCZOS)
            folla.paste(im, (8, y))
            for m, x in enumerate([x for x in r['intentos'] if x['ficheiro'] != esc_f][:2]):
                al = Image.open(IMX / x['ficheiro']).convert('RGB').resize((W_ALT, H_ALT), Image.LANCZOS)
                ya = y + m * H_ALT
                folla.paste(al, (8 + W_MAIN + GAP, ya))
                et = f"[{idx[x['ficheiro']]}] " + (', '.join(curto(p) for p in x['problemas']) or 'ok')
                d.rectangle((8 + W_MAIN + GAP, ya, 8 + W_MAIN + GAP + W_ALT, ya + 18), fill=(0, 0, 0))
                d.text((12 + W_MAIN + GAP, ya + 2), et[:44], font=f13, fill=(255, 220, 120))
            d.rectangle((8, y, 8 + 250, y + 24), fill=(0, 0, 0))
            d.text((12, y + 3), f"#{n}  [{idx[esc_f]}] porta: {'PASA' if ok else 'NON PASA'}", font=fb17,
                   fill=(120, 230, 120) if ok else (255, 110, 110))
            et = ETIQ.get(str(n))
            if et:
                cr = (120, 230, 120) if et.startswith('VALE') else (255, 210, 90) if et.startswith('OUTRO') else (255, 110, 110)
                tw = d.textlength('Revisión r2: ' + et, font=fb17)
                d.rectangle((8 + W_MAIN - tw - 12, y + H_MAIN - 24, 8 + W_MAIN, y + H_MAIN), fill=(0, 0, 0))
                d.text((8 + W_MAIN - tw - 6, y + H_MAIN - 21), 'Revisión r2: ' + et, font=fb17, fill=cr)
            an = r.get('animacion') or {}
            yt = y + H_MAIN + 4
            info = (f"#{n} · {e['tipo']} · persoas: {e['persoas']} · i2v: {e['prioridade_i2v']} ({an.get('modo')}, "
                    f"{an.get('camara')}) · época: {e.get('epoca', 's. XVII')} · clave: {e['clave']}")
            d.text((8, yt), info[:125], font=f13, fill=(170, 200, 255))
            yy = yt + 18
            for l in textwrap.wrap('Óese: ' + r['texto'], 125)[:3]:
                d.text((8, yy), l, font=f13, fill=(235, 235, 235)); yy += 17
            for l in textwrap.wrap('Prompt: ' + r['prompt'], 125)[:2]:
                d.text((8, yy), l, font=f13, fill=(190, 190, 190)); yy += 17
            if an.get('accion'):
                d.text((8, yy), ('Acción I2V: ' + an['accion'])[:125], font=f13, fill=(160, 230, 230)); yy += 17
            porta = ' | '.join(f"[{idx[x['ficheiro']]}] " + (', '.join(curto(p) for p in x['problemas']) or 'ok')
                               for x in r['intentos'])
            d.text((8, yy), ('Porta: ' + porta)[:130], font=f13, fill=(255, 200, 140))
        nome = saida / f'r2-planos-{grupo[0]:02d}-{grupo[-1]:02d}.jpg'
        for q in (78, 72, 66, 60, 55):
            folla.save(nome, 'JPEG', quality=q, optimize=True, progressive=True)
            if nome.stat().st_size <= 400_000:
                break
        print(nome, folla.size, nome.stat().st_size, 'q', q)
        if vistas:
            for v in range(0, len(grupo), 2):
                y0 = 34 + v * H_BLOCK
                folla.crop((0, y0, folla.width, min(H, y0 + 2 * H_BLOCK))).save(vistas / f'vista-{grupo[v]:02d}.png')


if __name__ == '__main__':
    main()
