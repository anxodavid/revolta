import json, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
SCR = Path('/tmp/claude-0/-home-user-revolta/c92eba35-e89d-5d11-bb3d-f517a84dab48/scratchpad')
IMX = SCR / 'v2' / 'w' / 'imaxes'
rev = json.loads((IMX / 'revision.json').read_text())
f13 = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 14)
# plano: rótulo (planos que xa valían na r1, para a coherencia do elenco)
P = [(13, 'Dorotea'), (30, 'Dorotea e María?'), (23, 'María'), (5, 'escribán'), (12, 'escribán'), (28, 'escribán'),
     (43, 'Cibreira'), (57, 'curandeira chal azul'), (59, 'Feijoo'), (16, 'moza da trenza'), (66, 'moza da trenza'),
     (50, 'veciños C. Lameiro'), (71, 'vellas queimada'), (33, 'Mariano e amigos'), (34, 'Mariano e amigos'),
     (3, 'Mariano'), (4, 'barco'), (36, '?')]
W, H = 320, 183
out = Image.new('RGB', (3 * (W + 6) + 6, ((len(P) + 2) // 3) * (H + 6) + 6), (20, 20, 20))
d = ImageDraw.Draw(out)
for i, (n, rot) in enumerate(P):
    ks = [k for k in rev if k.startswith(f'{n-1:03d}-')]
    k = max(ks, key=lambda k: rev[k].get('escolla_manual', False))  # a escolla vixente
    r = rev[k]
    print(n, ks, r['ficheiro'], r.get('ok'), (r.get('revision_manual') or {}).get('decision'))
    im = Image.open(IMX / r['ficheiro']).convert('RGB').resize((W, H), Image.LANCZOS)
    x, y = 6 + (i % 3) * (W + 6), 6 + (i // 3) * (H + 6)
    out.paste(im, (x, y))
    t = f'#{n} {rot}'
    d.rectangle((x, y, x + d.textlength(t, font=f13) + 8, y + 20), fill=(0, 0, 0))
    d.text((x + 4, y + 2), t, font=f13, fill=(255, 220, 120))
out.save(sys.argv[1], 'JPEG', quality=80, optimize=True)
print(out.size)
