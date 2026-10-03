"""Follas de contactos lixeiras para a revisión das imaxes (Gauntlet 4, revisor de imaxes r1).

Uso: python follas.py PRIMEIRO ULTIMO POR_FOLLA SAIDA_DIR [VISTAS_DIR]
Cada plano: a imaxe escollida a 640 px, os outros intentos a 320 px ao lado, e debaixo o número, o texto que se oe,
a clave e o que dixo a porta en cada intento. Escribe JPEG <= 400 KB. Se se dá VISTAS_DIR, garda tamén recortes de
2 planos por vista (para miralos sen reducir).
"""
import json, sys, textwrap
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

SCR = Path('/tmp/claude-0/-home-user-revolta/c92eba35-e89d-5d11-bb3d-f517a84dab48/scratchpad')
IMX = SCR / 'v2' / 'w' / 'imaxes'
REV = SCR / 'revimx' / 'revision-copia.json'
ESC = Path('/home/user/revolta/plan-de-negocio/gauntlet4/planos/escenas-v2.json')
F = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
FB = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
f15, f13, fb17 = ImageFont.truetype(F, 15), ImageFont.truetype(F, 13), ImageFont.truetype(FB, 17)

_E = SCR / 'revimx' / 'etiquetas.json'
ETIQ = json.loads(_E.read_text()) if _E.exists() else {}
W_MAIN, H_MAIN, W_ALT, H_ALT, GAP = 640, 366, 320, 183, 6
W_BLOCK = W_MAIN + GAP + W_ALT
H_TEXT = 92
H_BLOCK = H_MAIN + H_TEXT + 10


def main():
    a, b, por, saida = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), Path(sys.argv[4])
    vistas = Path(sys.argv[5]) if len(sys.argv) > 5 else None
    saida.mkdir(parents=True, exist_ok=True)
    if vistas:
        vistas.mkdir(parents=True, exist_ok=True)
    esc = {e['n']: e for e in json.loads(ESC.read_text())['escenas']}
    rev = json.loads(REV.read_text())
    por_n = {int(k[:3]) + 1: (k, v) for k, v in rev.items()}
    ns = [n for n in range(a, b + 1) if n in por_n]
    for i0 in range(0, len(ns), por):
        grupo = ns[i0:i0 + por]
        H = 34 + len(grupo) * H_BLOCK
        folla = Image.new('RGB', (W_BLOCK + 16, H), (24, 24, 24))
        d = ImageDraw.Draw(folla)
        d.text((8, 8), f'Revisión de imaxes r1 (axente Claude) · planos {grupo[0]}-{grupo[-1]} · '
                       'grande = escollida pola porta; pequenas = outros intentos; revisión = decisión do axente', font=f13, fill=(200, 200, 200))
        for j, n in enumerate(grupo):
            k, r = por_n[n]
            e = esc[n]
            y = 34 + j * H_BLOCK
            esc_f = r['ficheiro']
            im = Image.open(IMX / esc_f).convert('RGB').resize((W_MAIN, H_MAIN), Image.LANCZOS)
            folla.paste(im, (8, y))
            outros = [x for x in r['intentos'] if x['ficheiro'] != esc_f]
            for m, x in enumerate(outros[:2]):
                p = IMX / x['ficheiro']
                if not p.exists():
                    continue
                al = Image.open(p).convert('RGB').resize((W_ALT, H_ALT), Image.LANCZOS)
                ya = y + m * (H_ALT)
                folla.paste(al, (8 + W_MAIN + GAP, ya))
                et = f"[{x['intento']}] " + (', '.join(x['problemas']) or 'ok')
                d.rectangle((8 + W_MAIN + GAP, ya, 8 + W_MAIN + GAP + W_ALT, ya + 18), fill=(0, 0, 0))
                d.text((12 + W_MAIN + GAP, ya + 2), et[:44], font=f13, fill=(255, 220, 120))
            # rótulo sobre a escollida
            ch = [x for x in r['intentos'] if x['ficheiro'] == esc_f][0]
            d.rectangle((8, y, 8 + 250, y + 24), fill=(0, 0, 0))
            cor = (120, 230, 120) if r['ok'] else (255, 110, 110)
            d.text((12, y + 3), f"#{n}  [{ch['intento']}] porta: {'PASA' if r['ok'] else 'NON PASA'}", font=fb17, fill=cor)
            # decisión da revisión (axente Claude), se xa existe
            et = ETIQ.get(str(n))
            if et:
                cr = (120, 230, 120) if et.startswith('VALE') else (255, 210, 90) if et.startswith('OUTRO') else (255, 110, 110)
                tw = d.textlength('Revisión: ' + et, font=fb17)
                d.rectangle((8 + W_MAIN - tw - 12, y + H_MAIN - 24, 8 + W_MAIN, y + H_MAIN), fill=(0, 0, 0))
                d.text((8 + W_MAIN - tw - 6, y + H_MAIN - 21), 'Revisión: ' + et, font=fb17, fill=cr)
            # texto debaixo
            yt = y + H_MAIN + 4
            info = (f"#{n} · {e['tipo']} · persoas: {e['persoas']} · i2v: {e['prioridade_i2v']} "
                    f"({e['animacion'].get('modo')}) · época: {e.get('epoca', 's. XVII')} · clave: {e['clave']}")
            d.text((8, yt), info[:118], font=f13, fill=(170, 200, 255))
            linhas = textwrap.wrap('Óese: ' + e['texto'], 118)
            for m, l in enumerate(linhas[:3]):
                d.text((8, yt + 18 + m * 17), l, font=f13, fill=(235, 235, 235))
            porta = ' | '.join(f"[{x['intento']}] " + (', '.join(x['problemas']) or 'ok') for x in r['intentos'])
            d.text((8, yt + 18 + min(3, len(linhas)) * 17), ('Porta: ' + porta)[:130], font=f13, fill=(255, 200, 140))
        nome = saida / f'follas-planos-{grupo[0]:02d}-{grupo[-1]:02d}.jpg'
        for q in (78, 72, 66, 60, 55):
            folla.save(nome, 'JPEG', quality=q, optimize=True, progressive=True)
            if nome.stat().st_size <= 400_000:
                break
        print(nome, folla.size, nome.stat().st_size, 'q', q)
        if vistas:
            for v in range(0, len(grupo), 2):
                y0 = 34 + v * H_BLOCK
                y1 = min(H, y0 + 2 * H_BLOCK)
                cr = folla.crop((0, y0, folla.width, y1))
                cr.save(vistas / f'vista-{grupo[v]:02d}.png')


if __name__ == '__main__':
    main()
