"""Proba A/B das sementes (Gauntlet 4, peza IMAXE): a mesma escena con texto só, img2img (forza 0,5 e 0,75) e
ControlNet de profundidade (escala 0,6), coa mesma semente e o mesmo prompt. Usa o campo `referencia` de imaxes.py
(o mesmo código que a produción). Só referencias CC0, dominio público ou CC BY (referencias.json).

    flock "$CPU_LOCK" $PY sementes_ab.py xerar aldea,horreo,carro     # unha tanda por experimento (≈ 20 min)
    $PY sementes_ab.py folla                                          # folla A/B (JPEG) no repo

Saída: $SCRATCH/imaxe4/ab/<concepto>-<tecnica>.png e ab.json (tempos); a folla vai a ../ab-sementes.jpg.
"""
import json, os, sys, time
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
sys.path.insert(0, str(REPO / 'herramientas/pipeline'))
OUT = Path(os.environ.get('SCRATCH', '/tmp')) / 'imaxe4' / 'ab'

CONCEPTOS = {   # id: (escena para compor_prompt, referencia base, semente)
    'aldea': ({'fase': 'transicion', 'tipo': 'xeral', 'clave': 'stone church', 'prompt':
               'wide shot through a small granite window of a Galician hamlet, grey granite houses with dark weathered tile '
               'roofs, a Romanesque granite church with a bell gable, green hills, a woman in a dark wool shawl walking '
               'in the lane below, bright overcast daylight'},
              {'ficheiro': '12-iconografia/04-dende-a-fiestra-8578368554.jpg', 'centro': [0.5, 0.45]}, 1101),
    'horreo': ({'fase': 'calma', 'tipo': 'plano_medio', 'clave': 'granary on stone pillars', 'prompt':
                'medium shot of a woman in a long dark wool skirt and headscarf carrying a basket of maize cobs to a '
                'Galician horreo, a granary of granite blocks raised on stone pillars with flat round capstones, '
                'green meadow, warm sunset light'},
               {'ficheiro': '01-horreo/02-horreos-galicien-img-0274a.jpg', 'encadre': 'encaixar'}, 1102),
    'carro': ({'fase': 'transicion', 'tipo': 'plano_medio', 'clave': 'ox cart', 'prompt':
               'medium shot of an old Galician ox cart with solid wooden disc wheels made of joined oak planks, resting '
               'on mossy granite rocks, a farmer in a coarse wool jacket leaning on the cart, low winter sun, long shadows'},
              {'ficheiro': '02-carro-bois/15-carro-monte-pio-santiago-de-compostela.jpg', 'centro': [0.4, 0.55]}, 1103),
    'palloza': ({'fase': 'transicion', 'tipo': 'xeral', 'clave': 'thatched roof', 'prompt':
                 'wide shot of a round palloza house of dry-stone walls with a steep conical thatched rye straw roof in '
                 'the misty mountains of Os Ancares, a woman in a dark wool shawl carrying firewood to the low wooden '
                 'door, grey morning light'},
                {'ficheiro': '03-palloza-casa/10-palloza-cantexeira.jpg', 'centro': [0.5, 0.45]}, 1104),
    'lareira': ({'fase': 'gancho', 'tipo': 'plano_medio', 'clave': 'wooden bench', 'prompt':
                 'medium shot of an old woman in a dark wool headscarf sitting on a high-backed wooden bench beside an '
                 'open stone hearth at floor level, a small fire burning, smoke-blackened granite hood above, lit only '
                 'by firelight, deep black shadows'},
                {'ficheiro': '06-cocina/03-reitoral-de-beiro-carballeda-de-avia-3.jpg'}, 1105),
    'queimada': ({'fase': 'gancho', 'tipo': 'detalle', 'clave': 'blue flames', 'prompt':
                  'extreme close-up of a wide clay bowl of burning spirits, translucent blue flames, a wooden ladle '
                  'lifting fire above the bowl, small clay cups on the rim, darkness around'},
                 {'ficheiro': '07-queimada/09-pequena-queimada.jpg', 'recorte': [0.05, 0.3, 0.9, 1.0]}, 1106),
    'horreos': ({'fase': 'transicion', 'tipo': 'xeral', 'clave': 'granary on stone pillars', 'prompt':
                 'wide shot of several Galician horreos, long granaries of granite and wood raised on stone pillars with '
                 'round capstones, in a farmyard, an old man carrying a sack of grain, low winter sun, long shadows'},
                {'ficheiro': '01-horreo/16-horreos-de-muimenta-carballeda-de-avia-galiza.jpg', 'centro': [0.5, 0.6]}, 1107),
    'pote': ({'fase': 'calma', 'tipo': 'detalle', 'clave': 'iron pot', 'prompt':
              'close-up of a black iron pot hanging from an iron chain over a small fire on a raised stone hearth, '
              'smoke-blackened granite walls, a woman stirring with a wooden spoon, warm light of the fire'},
             {'ficheiro': '06-cocina/14-rfk-005-feuerstelle-im-17-jh.jpg', 'encadre': 'encaixar'}, 1108),
}
TECNICAS = [('texto', None), ('img2img_050', ('img2img', 0.5)), ('img2img_075', ('img2img', 0.75)),
            ('profundidade_060', ('profundidade', 0.6))]


def xerar(ids):
    import torch
    import imaxes
    torch.set_num_threads(int(os.environ.get('NTH', '4')))
    OUT.mkdir(parents=True, exist_ok=True)
    rexf = OUT / 'ab.json'
    rex = json.loads(rexf.read_text()) if rexf.exists() else {}
    m = imaxes.modelo()
    t0 = time.time(); pipe = imaxes.cargar_pipe(); carga = round(time.time() - t0, 1)
    print('carga', carga, 's', m, flush=True)
    for cid in ids:
        e, base, seed = CONCEPTOS[cid]
        pr = imaxes.compor_prompt(e, 0, 0, (), m)
        for tec, modo in TECNICAS:
            k = f'{cid}-{tec}-{m["nome"]}'
            f = OUT / f'{k}.png'
            if f.exists() and k in rex:
                continue
            ref = None
            try:
                t = time.time()
                if modo:
                    ref = imaxes.preparar_referencia(dict(base, modo=modo[0], forza=modo[1]), m)
                tprep = round(time.time() - t, 1)
                t = time.time()
                im = imaxes.xerar_unha(pipe, pr, seed, m, ref=ref)
                s = round(time.time() - t, 1)
            except Exception as ex:      # unha técnica que falla non para a tanda
                import traceback; traceback.print_exc()
                rex[k + '-erro'] = {'concepto': cid, 'tecnica': tec, 'erro': repr(ex)[:500]}
                rexf.write_text(json.dumps(rex, ensure_ascii=False, indent=1))
                continue
            tmp = f.with_suffix('.tmp.png'); im.save(tmp); os.replace(tmp, f)
            if ref is not None and not (OUT / f'{cid}-referencia.jpg').exists():
                ref['imaxe'].save(OUT / f'{cid}-referencia.jpg', quality=90)
            if ref is not None and ref.get('control') is not None:
                ref['control'].save(OUT / f'{cid}-profundidade.jpg', quality=90)
            rex[k] = {'concepto': cid, 'tecnica': tec, 'modelo': m['nome'], 'W': m['W'], 'H': m['H'], 'semente': seed,
                      'prompt': pr, 'clave': e.get('clave'), 'referencia': base['ficheiro'] if modo else None,
                      's_xeracion': s, 's_preparacion': tprep, 'carga_pipe_s': carga}
            rexf.write_text(json.dumps(rex, ensure_ascii=False, indent=1))
            print(f'{k}: {s} s (+{tprep} s de preparación)', flush=True)
            imaxes._liberar()


def folla():
    from PIL import Image, ImageDraw, ImageFont
    rex = json.loads((OUT / 'ab.json').read_text())
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 17)
    cids = [c for c in CONCEPTOS if any(v['concepto'] == c for v in rex.values())]
    cols = ['referencia'] + [t for t, _ in TECNICAS]
    w, h = 480, 270
    sheet = Image.new('RGB', (len(cols) * (w + 6), len(cids) * (h + 30) + 34), (20, 20, 20))
    d = ImageDraw.Draw(sheet)
    d.text((6, 6), 'Gauntlet 4 · imaxe · A/B de sementes (mesmo prompt e semente; SDXL-Lightning 4 pasos)', fill=(255, 255, 255), font=font)
    for r, cid in enumerate(cids):
        y = 34 + r * (h + 30)
        for c, col in enumerate(cols):
            x = c * (w + 6)
            if col == 'referencia':
                p = OUT / f'{cid}-referencia.jpg'; lab = f'{cid}: semente ({CONCEPTOS[cid][1]["ficheiro"].split("/")[0]})'
            else:
                ks = [k for k, v in rex.items() if v['concepto'] == cid and v['tecnica'] == col]
                p = OUT / f'{ks[0]}.png' if ks else None
                lab = f'{col} · {rex[ks[0]]["s_xeracion"]:.0f} s' if ks else col
            if p and p.exists():
                im = Image.open(p).convert('RGB'); im.thumbnail((w, h)); sheet.paste(im, (x, y))
            d.text((x + 4, y + h + 4), lab, fill=(255, 255, 160), font=font)
    dest = AQUI.parent / 'ab-sementes.jpg'
    sheet.save(dest, quality=82, optimize=True)
    print(dest, sheet.size)


if __name__ == '__main__':
    if sys.argv[1] == 'xerar':
        xerar(sys.argv[2].split(','))
    else:
        folla()
