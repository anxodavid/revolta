"""Produción da v2 (Gauntlet 4, peza 5): lista de produción, revisión das imaxes e clips I2V.

Uso (python3 do sistema, sen dependencias, desde calquera sitio):
    produccion.py lista                      # planos/escenas-v2.json + video/axustes-produccion.json
                                             #   -> video/escenas-v2-produccion.json (a lista que usa longo.py)
    produccion.py revision video/revision-imaxes-r1.json [--quen "..."]
                                             # escollas -> revision.json (escolla_manual); rexenerar -> axustes
    produccion.py i2v SAIDA.json [--prioridade 1,2] [--fases gancho,transicion] [--accions]
                                             # traballos para movemento_i2v.py, por prioridade e orde do plano
    produccion.py porta [--aplicar]          # clips que non pasan a porta de vídeo: outra semente unha vez, logo paralaxe
    produccion.py estado                     # por plano: imaxe escollida, quen a aprobou, clip I2V e porta

A clave da caché de imaxes dun plano é a de imaxes.xerar: índice + sha256(prompt + modelo + fase + referencia). Un
prompt novo nos axustes dá unha clave nova (intentos novos, sementes novas); a escolla feita na revisión queda en
revision.json con `escolla_manual` e `revision_manual` (quen a fixo: un axente Claude, non unha persoa).
`revision` non se aplica mentres corre longo.py: o proceso de imaxes garda revision.json despois de cada plano co
que ten en memoria e borraría as escollas.
"""
import argparse, hashlib, json, os, subprocess, sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[4]
G4 = RAIZ / 'plan-de-negocio' / 'gauntlet4'
BASE = G4 / 'planos' / 'escenas-v2.json'
AXUSTES = G4 / 'video' / 'axustes-produccion.json'
PROD = G4 / 'video' / 'escenas-v2-produccion.json'
PORTA = G4 / 'video' / 'porta-i2v.json'
SCR = Path(os.environ.get('SCRATCH', '/tmp/claude-0/-home-user-revolta/c92eba35-e89d-5d11-bb3d-f517a84dab48/scratchpad'))
W = SCR / 'v2' / 'w'
MODELO = 'lightning'                     # IMG_MODEL da produción (imaxes.sh)
F_CURTO, CURTO_S = 73, 6.0               # informe de movemento §8 (configuración A): 73 fotogramas nos planos < 6 s
SEMENTE_REINTENTO = 43                   # I2V_PARAMS ten semente 42


def ler(f, defecto=None):
    return json.loads(Path(f).read_text()) if Path(f).exists() else defecto


def gardar(f, d):
    f = Path(f); tmp = f.with_name(f.name + '.tmp')
    tmp.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n'); os.replace(tmp, f)


def fases():
    return {e['n']: e.get('fase') for e in ler(W / 'escenas.json', [])}


def clave(e, fase):
    ref = json.dumps(e['referencia'], sort_keys=True) if e.get('referencia') else ''
    h = hashlib.sha256((e['prompt'] + MODELO + str(fase) + ref).encode()).hexdigest()[:8]
    return f"{e['n'] - 1:03d}-{h}"


def lista():
    d = ler(BASE); ax = ler(AXUSTES, {})
    dur = {p['n']: p['dur_s'] for p in ler(W / 'planos.json', [])}
    cambios = 0
    for e in d['escenas']:
        a = ax.get(str(e['n']), {})
        for k in ('prompt', 'negativo', 'referencia', 'clave'):
            if k in a:
                e[k] = a[k]
        an = e.get('animacion')
        if an and a.get('modo'):         # p. ex. paralaxe cando o clip I2V non pasa a porta
            an['modo'] = a['modo']
        if an and a.get('accion'):       # a acción I2V que casa coa imaxe aceptada (revisión das imaxes)
            an['accion'] = a['accion']
        if an and an.get('modo') == 'i2v':
            i2v = dict(an.get('i2v') or {})
            if dur.get(e['n'], 99) < CURTO_S:
                i2v.setdefault('F', F_CURTO)
            i2v.update(a.get('i2v') or {})
            if i2v:
                an['i2v'] = i2v
        if a:
            e['axuste_produccion'] = a.get('motivo', '')
            cambios += 1
    d['descricion'] = ('Lista de produción da v2: a lista pechada da peza 4 (planos/escenas-v2.json) cos axustes de '
                       'video/axustes-produccion.json (revisión das imaxes e porta de vídeo). Xerada por '
                       'video/scripts/produccion.py lista.')
    gardar(PROD, d)
    print(f'lista de produción: {len(d["escenas"])} planos, {cambios} con axustes -> {PROD.relative_to(RAIZ)}')


def corre_longo():
    return subprocess.run(['pgrep', '-f', 'longo.py'], capture_output=True).returncode == 0


def revision(fich, quen, so_axustes=False):
    """so_axustes: só as rexeneracións (axustes e lista), sen tocar revision.json: pódese facer con longo.py en marcha."""
    if not so_axustes and corre_longo():
        sys.exit('longo.py está a correr: agarda a que remate (gardaría revision.json por riba das escollas)')
    R = ler(fich); revf = W / 'imaxes' / 'revision.json'; rev = ler(revf)
    motivos = R.get('motivos', {})
    for n, f in ({} if so_axustes else R.get('escollas', {})).items():
        k = f.rsplit('-', 1)[0]
        r = rev[k]
        idx = [x['ficheiro'] for x in r['intentos']].index(f)
        decision = 'vale' if idx == r['escollida'] else 'outro intento'
        r.update(ficheiro=f, escollida=idx, escolla_manual=True,
                 revision_manual={'quen': quen, 'decision': decision, 'motivo': motivos.get(n, '')})
    ax = ler(AXUSTES, {})
    for n, a in R.get('rexenerar', {}).items():
        x = ax.setdefault(str(n), {})
        x.update({k: v for k, v in a.items() if k in ('prompt', 'negativo', 'referencia', 'clave')})
        x['motivo'] = f"rexenerar ({quen}): {a.get('motivo', '')}"
    if not so_axustes:
        gardar(revf, rev)
    gardar(AXUSTES, ax)
    print(f"revisión aplicada: {0 if so_axustes else len(R.get('escollas', {}))} escollas, "
          f"{len(R.get('rexenerar', {}))} planos a rexenerar")
    lista()


def imaxe_aprobada(e, rev, fs):
    r = rev.get(clave(e, fs.get(e['n'])))
    if not r:
        return None, 'sen imaxe'
    if not (r['ok'] or r.get('revision_manual')):
        return None, 'imaxe sen aprobar (nin a porta nin a revisión)'
    return str(W / 'imaxes' / r['ficheiro']), ('porta' if r['ok'] and not r.get('revision_manual') else
                                               r['revision_manual']['quen'])


def i2v(saida, prioridades, fases_ok, accions):
    prod = ler(PROD)['escenas']; rev = ler(W / 'imaxes' / 'revision.json', {}); fs = fases()
    out, fora = [], []
    for e in prod:
        an = e.get('animacion') or {}
        if an.get('modo') != 'i2v' or not an.get('accion'):
            continue
        if prioridades and e.get('prioridade_i2v') not in prioridades:
            continue
        if fases_ok and fs.get(e['n']) not in fases_ok:
            continue
        im, por = imaxe_aprobada(e, rev, fs)
        if not im and not accions:
            fora.append(f"{e['n']} ({por})"); continue
        out.append({'n': e['n'], 'prioridade_i2v': e.get('prioridade_i2v'), 'imaxe': im or '-',
                    'accion': an['accion'], 'i2v': an.get('i2v') or {}})
    out.sort(key=lambda x: (x['prioridade_i2v'] or 9, x['n']))
    gardar(saida, out)
    print(f'{len(out)} traballos I2V -> {saida}' + (f'; fóra: {", ".join(fora)}' if fora else ''))


def porta(aplicar):
    res = ler(PORTA, {}); ax = ler(AXUSTES, {})
    for n, r in sorted(res.items(), key=lambda x: int(x[0])):
        if r.get('ok'):
            continue
        x = ax.setdefault(n, {})
        if (r.get('i2v') or {}).get('semente') == SEMENTE_REINTENTO:
            acc = 'paralaxe'
            x.update(modo='paralaxe', motivo=f"o clip I2V non pasou a porta de vídeo dúas veces: {r.get('problemas')}")
        else:
            acc = f'outra semente ({SEMENTE_REINTENTO})'
            x['i2v'] = dict(x.get('i2v') or {}, semente=SEMENTE_REINTENTO)
            x['motivo'] = f"o clip I2V non pasou a porta de vídeo: {r.get('problemas')}"
        print(f'plano {n}: {r.get("problemas")} -> {acc}')
    if aplicar:
        gardar(AXUSTES, ax); lista()
    else:
        print('(sen aplicar: engade --aplicar)')


def estado():
    prod = ler(PROD) or ler(BASE)
    rev = ler(W / 'imaxes' / 'revision.json', {}); fs = fases(); pt = ler(PORTA, {})
    sys.path.insert(0, str(RAIZ / 'herramientas' / 'pipeline'))
    for e in prod['escenas']:
        an = e.get('animacion') or {}
        im, por = imaxe_aprobada(e, rev, fs)
        clip = ''
        if an.get('modo') == 'i2v':
            p = pt.get(str(e['n']))
            clip = 'sen clip' if not p else ('porta ok' if p.get('ok') else f"porta: {p.get('problemas')}")
        print(f"{e['n']:3d} {str(fs.get(e['n'])):10s} p{e.get('prioridade_i2v')} {an.get('modo', '-'):8s} "
              f"{Path(im).name if im else '-':22s} {por:30s} {clip}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('orde', choices=['lista', 'revision', 'i2v', 'porta', 'estado'])
    ap.add_argument('ficheiro', nargs='?')
    ap.add_argument('--quen', default='axente Claude (revisión r1 das imaxes da v2)')
    ap.add_argument('--prioridade', default='')
    ap.add_argument('--fases', default='')
    ap.add_argument('--accions', action='store_true', help='tamén os planos sen imaxe aprobada (para os embeddings)')
    ap.add_argument('--aplicar', action='store_true')
    ap.add_argument('--so-axustes', action='store_true', help='revision: só as rexeneracións, sen tocar revision.json')
    a = ap.parse_args()
    if a.orde == 'lista':
        lista()
    elif a.orde == 'revision':
        revision(a.ficheiro, a.quen, a.so_axustes)
    elif a.orde == 'i2v':
        i2v(a.ficheiro, [int(x) for x in a.prioridade.split(',') if x], [x for x in a.fases.split(',') if x],
            a.accions)
    elif a.orde == 'porta':
        porta(a.aplicar)
    else:
        estado()


if __name__ == '__main__':
    main()
