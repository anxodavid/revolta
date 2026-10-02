"""Folla de contactos: python folla.py SAIDA.jpg ANCHO COLUMNAS imaxe1[::etiqueta] imaxe2[::etiqueta] ..."""
import sys, textwrap
from PIL import Image, ImageDraw, ImageFont
out, W, C = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
items = [a.split('::', 1) if '::' in a else (a, a.rsplit('/', 1)[-1]) for a in sys.argv[4:]]
try:
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 15)
except OSError:
    font = ImageFont.load_default()
ims = []
for f, lab in items:
    try:
        im = Image.open(f).convert('RGB')
    except Exception as ex:
        im = Image.new('RGB', (W, W * 9 // 16), (80, 0, 0)); lab += f' [ERRO {ex}]'
    im.thumbnail((W, W), Image.LANCZOS)
    ims.append((im, lab))
cellh = max(i.size[1] for i, _ in ims) + 40
R = (len(ims) + C - 1) // C
sheet = Image.new('RGB', (C * (W + 8), R * cellh), (25, 25, 25))
d = ImageDraw.Draw(sheet)
for k, (im, lab) in enumerate(ims):
    x, y = (k % C) * (W + 8), (k // C) * cellh
    sheet.paste(im, (x + (W - im.size[0]) // 2, y))
    for j, line in enumerate(textwrap.wrap(lab, W // 8)[:2]):
        d.text((x + 2, y + cellh - 40 + j * 18), line, fill=(255, 255, 160), font=font)
sheet.save(out, quality=85)
print(out, sheet.size)
