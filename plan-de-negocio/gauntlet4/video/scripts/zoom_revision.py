"""Recortes ampliados dos orixinais para mirar detalles. Uso: zoom_revision.py SAIDA.png 'fich:x0,y0,x1,y1:rótulo' ...
(coordenadas en fracción da imaxe). Grade de 2 columnas, cada recorte a 600x400 como moito."""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

IMX = Path('/tmp/claude-0/-home-user-revolta/c92eba35-e89d-5d11-bb3d-f517a84dab48/scratchpad/v2/w/imaxes')
f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 14)
CW, CH = 600, 400
saida, specs = sys.argv[1], sys.argv[2:]
rows = (len(specs) + 1) // 2
out = Image.new('RGB', (2 * CW + 12, rows * (CH + 22) + 4), (20, 20, 20))
d = ImageDraw.Draw(out)
for i, s in enumerate(specs):
    fich, caixa, rot = s.split(':', 2)
    im = Image.open(IMX / fich).convert('RGB')
    x0, y0, x1, y1 = [float(v) for v in caixa.split(',')]
    W, H = im.size
    cr = im.crop((int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H)))
    cr.thumbnail((CW, CH), Image.LANCZOS) if cr.width > CW or cr.height > CH else None
    if cr.width < CW and cr.height < CH:
        k = min(CW / cr.width, CH / cr.height)
        cr = cr.resize((int(cr.width * k), int(cr.height * k)), Image.LANCZOS)
    x, y = (i % 2) * (CW + 6) + 3, (i // 2) * (CH + 22) + 2
    out.paste(cr, (x, y + 20))
    d.text((x, y + 2), f'{rot} ({fich})', font=f, fill=(255, 220, 120))
out.save(saida)
print(saida, out.size)
