"""Calibración das portas novas da versión 6 de revisor.py coas imaxes da folla r1 (Gauntlet 3, peza VISUAL, ronda 2).

    flock "$CPU_LOCK" $PY probas/visual_calibrar_r2.py [--saida CALIB.json]

As etiquetas saen do veredicto do crítico ciego (`plan-de-negocio/gauntlet3/veredictos/visual-r1.md`, táboa por
plano) e do que viu Claude nas imaxes: farolas no plano 2 (catro intentos), cidade no 13, salón no 12, patio no 11,
casas británicas no 5 (e as aldeas "inglesas" da comparativa), caldeiro no 16; e, para o campo `clave`, o que se
pedía e (non) se ve en cada plano. Imprime, para cada porta, os valores das malas e das boas e o umbral que as separa.
"""
import argparse, glob, json, os, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import revisor

S = Path(os.environ['SCRATCH']) / 'visual'
R1 = S / 'r1' / 'imaxes'


def f(pref):
    x = sorted(glob.glob(str(R1 / f'{pref}*.png')))
    return x[0] if x else None


def c(nome):
    return str(S / 'comp' / nome)


PARES = {   # etiqueta: (malas, boas)
    'luz eléctrica (CLIP)': (['001-79e06ef0-0', '001-79e06ef0-1', '001-79e06ef0-2', '001-79e06ef0-3'],
                             ['000-c72c8803-1', '002-', '003-', '013-', '014-abc2335a-0', '014-abc2335a-5', '015-',
                              '011-9bb98628-0', '009-', '008-', '006-', '004-', '005-a32aa205-1', '007-42a6336c-2']),
    'luces de cidade (CLIP)': (['012-'], ['014-abc2335a-5', '013-', '015-', '000-c72c8803-1', '002-', '003-',
                                           '014-abc2335a-0', '008-', '009-']),
    'salón moderno (CLIP)': (['011-9bb98628-0', '011-9bb98628-1'], ['002-', '015-', '000-c72c8803-1', '003-',
                                                                    '005-a32aa205-1', '009-', '014-abc2335a-0']),
    'patio mediterráneo (CLIP)': (['010-'], ['001-79e06ef0-3', '004-', '005-a32aa205-1', '008-', '011-9bb98628-0',
                                             '002-', '003-', '006-', '012-', '013-', '014-abc2335a-5']),
    'casas británicas (CLIP)': (['004-', c('lightning-filme-2-horreo.png'), c('lightning-pintura-2-horreo.png'),
                                 c('lightning8-filme-2-horreo.png'), c('turbo-filme-2-horreo.png'),
                                 c('turbo-pintura-2-horreo.png')],
                                [c('lightning-filme-106-galicia.png'), str(S / 'icono' / 'lightning-filme-6-cruceiro_a.png'),
                                 str(S / 'icono' / 'lightning-filme-7-palloza_a.png'), '008-', '010-', '012-',
                                 '006-', '011-9bb98628-6']),
    'caldeiro de meiga (CLIP)': (['015-'], [c('lightning-filme-7-brasas.png'), c('lightning-filme-0-lareira.png'),
                                             c('turbo-filme-7-brasas.png'), '000-c72c8803-1', '011-9bb98628-0', '002-']),
}
CLAVE = [   # (imaxe, concepto pedido, ¿vese?)
    ('000-c72c8803-1', 'blue flames', False), ('000-c72c8803-1', 'wooden ladle', True),
    ('001-79e06ef0-3', 'hand-held lantern', False), ('002-', 'fire', True),
    ('003-', 'red wax seal', False), ('003-', 'candle', True), ('004-', 'maize', False), ('004-', 'slate roofs', True),
    ('005-a32aa205-1', 'dried herbs hanging from beams', False), ('006-', 'wooden yoke', False), ('006-', 'oxen', True),
    ('008-', 'boat', True), ('009-', 'iron oil lamp', False), ('009-', 'bread', True), ('010-', 'rain', False),
    ('010-', 'clay jugs', True), ('011-9bb98628-0', 'open stone hearth at floor level', False),
    ('011-9bb98628-0', 'cat', True), ('012-', 'stone cross', False), ('012-', 'bonfire', True),
    ('013-', 'bowl of water', False), ('013-', 'wild flowers', True), ('015-', 'embers', True),
    ('014-abc2335a-5', 'monk', False), ('014-abc2335a-5', 'oak trees', True), ('014-abc2335a-0', 'monk', True),
    ('014-abc2335a-0', 'candle', True),
]
DURMIR = {'012-': True, '013-': False, '014-abc2335a-5': False, '015-': True, '014-abc2335a-0': True,
          '014-abc2335a-1': True}   # True = ten lume vivo (mal na fase de durmir)
ARQ = {   # arquetipo: (si, non)
    'camiñantes de costas': (['001-79e06ef0-3', '004-', str(S / 'calib/g2/r3_00.png'), str(S / 'calib/g2/r3_05.png'),
                              str(S / 'calib/g2/r3_11.png'), str(S / 'calib/g2/r1_09.png'), str(S / 'calib/g2/r2_06.png')],
                             ['000-c72c8803-1', '002-', '003-', '005-a32aa205-1', '006-', '007-42a6336c-2', '008-',
                              '009-', '010-', '011-9bb98628-0', '012-', '013-', '014-abc2335a-5', '015-']),
    'persoa á lareira': (['002-', '011-9bb98628-0', c('lightning-filme-0-lareira.png'), c('turbo-filme-0-lareira.png'),
                          c('lightning-pintura-0-lareira.png'), c('turbo-pintura-0-lareira.png')],
                         ['014-abc2335a-0', '014-abc2335a-1', '003-', c('lightning-filme-7-brasas.png'),
                          c('turbo-filme-7-brasas.png'), '015-', '009-']),
}


def ruta(x):
    return x if x.startswith('/') else f(x)


def mellor(bos, malos, maior_e_malo=True):
    """Umbral con menos erros (un falso positivo conta dobre)."""
    vals = sorted(set(bos + malos))
    best = None
    for t in vals + [vals[-1] + 1e-3]:
        if maior_e_malo:
            fp, fn = sum(v > t for v in bos), sum(v <= t for v in malos)
        else:
            fp, fn = sum(v < t for v in bos), sum(v >= t for v in malos)
        k = (2 * fp + fn, fp)
        if best is None or k < best[0]:
            best = (k, round(t, 3), fp, fn)
    return best[1:]


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--saida', default=None)
    a = ap.parse_args()
    cl = revisor.Clip()
    cache = {}

    def E(x):
        p = ruta(x)
        if p not in cache:
            cache[p] = cl.analizar(p)
        return cache[p]
    out = {'pares': {}, 'clave': {}, 'durmir': {}, 'arquetipos': {}}
    print('== Pares novos: marxe (sim malo − sim bo, peor recorte) e pertinencia')
    for et, (malas, boas) in PARES.items():
        k = [p[0] for p in revisor.PARES].index(et)
        T = cl.textos([revisor.PARES[k][1], revisor.PARES[k][2]])
        val = lambda x: (round(float((E(x)[0] @ T[0] - E(x)[0] @ T[1]).max()), 3),
                         round(float(max((E(x)[0] @ T[0]).max(), (E(x)[0] @ T[1]).max())), 3))
        vm = [(val(x), Path(ruta(x)).name[:24]) for x in malas]
        vb = sorted(((val(x), Path(ruta(x)).name[:24]) for x in boas), reverse=True)
        u = mellor([v[0][0] for v in vb], [v[0][0] for v in vm])
        print(f'\n{et}\n  malas: {vm}\n  boas (máis altas): {vb[:5]}\n  umbral (marxe, FP, FN): {u}')
        out['pares'][et] = {'malas': vm, 'boas_top': vb[:6], 'umbral': u}
    print('\n== clave: sim("a photo with X") − sim("a photo"), mellor recorte')
    base = cl.textos(['a photo'])[0]
    si, no = [], []
    for x, conc, ve in CLAVE:
        e = E(x)[0]
        v = round(float((e @ cl.textos([f'a photo with {conc}'])[0] - e @ base).max()), 3)
        (si if ve else no).append((v, conc, Path(ruta(x)).name[:16]))
    si.sort(); no.sort(reverse=True)
    u = mellor([v for v, *_ in si], [v for v, *_ in no], maior_e_malo=False)
    print(f'  vense: {si}\n  non se ven: {no}\n  umbral (clave, FP=vese e falla, FN=non se ve e pasa): {u}')
    out['clave'] = {'vense': si, 'non_se_ven': no, 'umbral': u}
    print('\n== Altas luces (> 0,85) na fase de durmir')
    for x, lume in DURMIR.items():
        v = revisor.altas_luces(ruta(x))
        print(f'  {Path(ruta(x)).name[:24]}: {v:.4f} lume vivo={lume}')
        out['durmir'][Path(ruta(x)).name] = [round(v, 4), lume]
    print('\n== Arquetipos cambiados')
    for et, (sis, nons) in ARQ.items():
        textos = [t for e_, t, *_ in revisor.ARQUETIPOS if e_ == et][0]
        T = cl.textos(textos)
        vs = sorted((round(float((T @ E(x)[1]).max()), 3), Path(ruta(x)).name[:22]) for x in sis)
        vn = sorted(((round(float((T @ E(x)[1]).max()), 3), Path(ruta(x)).name[:22]) for x in nons), reverse=True)
        u = mellor([v for v, _ in vn], [v for v, _ in vs])
        print(f'{et}: si {vs}\n   non (máis altas) {vn[:5]}\n   umbral {u}')
        out['arquetipos'][et] = {'si': vs, 'non_top': vn[:6], 'umbral': u}
    if a.saida:
        Path(a.saida).write_text(json.dumps(out, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
