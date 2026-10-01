"""Hoja de prueba de la pieza VISUAL (Gauntlet 3): N planos con la puerta de revisión y la gradación por fase.

    flock "$CPU_LOCK" $PY probas/visual_hoja_prueba.py PLANOS.json TRABALLO SAIDA [--palabras 3400]

PLANOS.json: [{"n", "fase", "prompt", "tipo", "luz"?, "negativo"?}] (prompts según la biblia visual). Para la
gradación, a cada plano se le da una posición en palabras dentro de su fase (reparto uniforme en un guion de
--palabras palabras, con los nodos de curva.py), como haría longo.py.

SAIDA recibe: contactsheet.jpg (4 columnas, fotogramas de 960x540 recortados a 16:9 como en la montaxe, sin rótulos
de fase para que el crítico juzgue a ciegas; solo el número del plano), contactsheet_320.jpg (los mismos a 320x180,
para compararla a igual tamaño con el storyboard de la referencia), prompts.json (prompt final de cada intento),
porta.md (resultado de la puerta por plano e intento, tiempos) y graduacion.json.
"""
import argparse, json, os, sys, time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import curva, imaxes


def folla(paths, out, tw, th, cols=4, numeros=True, calidade=88):
    from PIL import Image, ImageDraw
    import montaxe
    rows = (len(paths) + cols - 1) // cols
    sheet = Image.new('RGB', (tw * cols, th * rows), 'black')
    d = ImageDraw.Draw(sheet)
    for k, p in enumerate(paths):
        im = montaxe._a_16_9(Image.open(p).convert('RGB')).resize((tw, th), Image.LANCZOS)
        x, y = (k % cols) * tw, (k // cols) * th
        sheet.paste(im, (x, y))
        if numeros:
            d.text((x + 10, y + 8), str(k + 1), fill=(255, 255, 255), font_size=max(14, th // 20))
    tmp = Path(str(out) + '.tmp.jpg')
    sheet.save(tmp, quality=calidade); os.replace(tmp, out)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('planos'); ap.add_argument('traballo'); ap.add_argument('saida')
    ap.add_argument('--palabras', type=int, default=3400)
    ap.add_argument('--planos-episodio', type=int, default=150,
                    help='planos do episodio para os topes de arquetipos (a folla é unha mostra del)')
    a = ap.parse_args()
    W, S = Path(a.traballo), Path(a.saida)
    W.mkdir(parents=True, exist_ok=True); S.mkdir(parents=True, exist_ok=True)
    pl = json.loads(Path(a.planos).read_text())
    # posición en palabras de cada plano: reparto uniforme dentro do tramo da súa fase
    nos = curva.nos(a.palabras)
    for fase_i, fase in enumerate(curva.FASES):
        grupo = [p for p in pl if p['fase'] == fase]
        a0, a1 = nos[fase_i], nos[fase_i + 1]
        for j, p in enumerate(grupo):
            p['pal0'] = round(a0 + (j + 0.5) * (a1 - a0) / len(grupo))
            p['u'] = round(p['pal0'] / a.palabras, 4)
    t0 = time.time()
    paths, rex = imaxes.xerar(pl, W / 'imaxes', seed_base=f'visual-{Path(a.saida).name}', n_total=a.planos_episodio)
    t_xer = time.time() - t0
    t0 = time.time()
    grad = imaxes.graduar(paths, W / 'imaxes_graduadas', escenas=pl)
    t_grad = time.time() - t0
    folla(grad, S / 'contactsheet.jpg', 960, 540)
    folla(grad, S / 'contactsheet_320.jpg', 320, 180, numeros=True, calidade=90)
    import shutil
    shutil.copy(W / 'imaxes_graduadas' / 'graduacion.json', S / 'graduacion.json')
    from PIL import Image
    (S / 'imaxes').mkdir(exist_ok=True)
    for k, g in enumerate(grad):     # as imaxes escollidas e graduadas, en JPEG, para non ter que rexeneralas
        Image.open(g).convert('RGB').save(S / 'imaxes' / f'{k + 1:02d}.jpg', quality=85)
    # prompts e porta
    pr = []
    L = ['# Puerta de revisión de la hoja de prueba (automático)', '',
         f'Modelo `{imaxes.modelo()["nome"]}` ({imaxes.modelo()["W"]}x{imaxes.modelo()["H"]}, '
         f'{imaxes.modelo()["pasos"]} pasos), estilo `{os.environ.get("IMG_ESTILO", imaxes.ESTILO_DEFECTO)}`, '
         f'revisor versión {rex[0]["version_revisor"] if rex else "-"}. Generación + revisión: {t_xer / 60:.1f} min de reloj; '
         f'gradación {t_grad:.0f} s.', '',
         '| Plano | Fase | Tipo | Intentos | Problemas de los intentos rechazados | Escogida | s generación | s revisión |',
         '|---|---|---|---|---|---|---|---|']
    for k, (p, r) in enumerate(zip(pl, rex)):
        its = r['intentos']
        rech = '; '.join(f"{i['intento']}: {', '.join(i['problemas'])}" for i in its if i['problemas']) or '-'
        L.append(f"| {k + 1} | {p['fase']} | {p.get('tipo', '')} | {len(its)} | {rech} | {r['escollida']} "
                 f"({'ok' if r['ok'] else 'FALLA'}{', reserva' if its[r['escollida']].get('reserva') else ''}) | "
                 f"{', '.join(str(i['s']) for i in its)} | {', '.join(str(i.get('s_revision', '')) for i in its)} |")
        pr.append({'n': k + 1, 'fase': p['fase'], 'tipo': p.get('tipo'), 'prompt_axente': p['prompt'],
                   'intentos': [{'intento': i['intento'], 'prompt_final': i['prompt'], 'tokens': i.get('tokens'),
                                 'truncado': i.get('truncado'), 'seed': i['seed'], 'problemas': i['problemas'],
                                 'descricion_florence': i.get('descricion'), 'arquetipo': i.get('arquetipo'),
                                 'iconografia_clip': i.get('iconografia')} for i in its],
                   'escollida': r['escollida'], 'ok': r['ok']})
    xs = [i['s'] for r in rex for i in r['intentos']]
    rv = [i.get('s_revision', 0) for r in rex for i in r['intentos']]
    motivos = {}
    for r in rex:
        for i in r['intentos']:
            for m in i['problemas']:
                clave = m.split(' (')[0].split(':')[0]
                motivos[clave] = motivos.get(clave, 0) + 1
    L += ['', f'Imágenes generadas: {len(xs)} para {len(rex)} planos; aprobadas a la primera: '
              f'{sum(1 for r in rex if r["ok"] and len(r["intentos"]) == 1)}; tras regenerar: '
              f'{sum(1 for r in rex if r["ok"] and len(r["intentos"]) > 1)}; sin aprobar: {sum(1 for r in rex if not r["ok"])}.',
          f'Segundos por imagen (generación): mediana {sorted(xs)[len(xs) // 2]}, media {sum(xs) / len(xs):.1f}; '
          f'revisión: mediana {sorted(rv)[len(rv) // 2]}, media {sum(rv) / len(rv):.1f}.',
          f'Rechazos por motivo: {json.dumps(motivos, ensure_ascii=False)}.']
    (S / 'porta.md').write_text('\n'.join(L) + '\n')
    (S / 'prompts.json').write_text(json.dumps(pr, ensure_ascii=False, indent=1))
    print('\n'.join(L[-3:]))


if __name__ == '__main__':
    main()
