#!/usr/bin/env python3
"""Predición barata da porta de veracidade (sen NLI) para un guion de longo.py. Guionista do Gauntlet 4 (axente
Claude), 02-10-2026.

    python3 veracidade_lexica.py GUION.txt TEMA.yaml [--todas]

Usa as mesmas funcións ca `veracidade.py` (raíces de 5 letras, coincidencia léxica, nomes, tempo longo e desenlaces)
e as mesmas regras ca `longo.porta_texto`: no gancho (palabras < curva.GANCHO) todas as frases teñen que ter apoio;
despois, só as que levan nome propio, tempo longo ou desenlace. Non carga o modelo NLI: unha frase con coincidencia
< 0,8 sae como "dubidosa" (a porta real pode aprobala se o NLI dá implicación ≥ 0,6 con coincidencia ≥ 0,6 no
gancho ou ≥ 0,5 no relato). Serve para reescribir antes de lanzar a porta de verdade, que é a que conta.
"""
import argparse, itertools, re, sys
from pathlib import Path
import yaml

PIPE = Path(__file__).resolve().parents[4] / 'herramientas' / 'pipeline'
sys.path.insert(0, str(PIPE))
import veracidade as V  # noqa: E402  (só regex e funcións puras; non carga torch ata crear o Verificador)
import curva  # noqa: E402

AVISO = 'Boas noites. A voz que vas escoitar é sintética, e este texto preparouno un proceso automático.'
FORMULA = 'Isto é Cousas de Galiza para durmir.'


def ler(path):
    pars = []
    for b in re.split(r'\n\s*\n', Path(path).read_text().strip()):
        b = ' '.join(b.split())
        if b and not b.startswith('## ') and not b.startswith('%%'):
            pars.append(b)
    return pars


def feitos(tema):
    out = []
    for l in tema['dossier'].strip().splitlines():
        l = re.sub(r'^\s*-\s*', '', l).strip()
        l = re.sub(r'^\[[^\]]*\]\s*', '', l)
        if l:
            out.append(l)
    return out


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('guion'); ap.add_argument('tema'); ap.add_argument('--todas', action='store_true')
    a = ap.parse_args()
    tema = yaml.safe_load(open(a.tema))
    F = feitos(tema)
    Fn = [V._norm(x) for x in F]
    pal = 0; n_dub = 0; filas = []
    for pi, par in enumerate(ler(a.guion)):
        for s in re.split(r'(?<=[.!?…])\s+', par):
            s = s.strip()
            if not s:
                continue
            n = len(s.split()); p0 = pal; pal += n
            if s in AVISO or s == FORMULA:
                continue
            gancho = p0 < curva.GANCHO
            nf = V._norm(s)
            literal = bool(nf) and any(nf in x for x in Fn)
            cobs = sorted(((V.cobertura(s, x), i) for i, x in enumerate(F)), reverse=True)
            top = [i for _, i in cobs[:4]]
            par_best = max(((V.cobertura(s, F[i] + ' ' + F[j]), (i, j)) for i, j in itertools.combinations(top, 2)),
                           default=(0, None))
            best = max(cobs[0][0], par_best[0])
            tempo = bool(re.search(V.TEMPO_LONGO, V._sen_acentos(s).replace('seculo', 'século')))
            ds = V.desenlaces(s)
            esixida = gancho or V.ten_nome(s) or tempo or bool(ds)
            ok_lex = literal or best >= V.COB_MIN
            estado = 'ok' if (not esixida or ok_lex) and not ds else ('DESENLACE' if ds else 'DUBIDOSA')
            if estado != 'ok':
                n_dub += 1
            if a.todas or estado != 'ok':
                apoio = f'F{cobs[0][1] + 1}' if cobs[0][0] >= par_best[0] else f'par {par_best[1]}'
                filas.append(f"{estado:9s} {'gancho' if gancho else 'relato'} pal {p0:4d} cob {best:.2f} "
                             f"(mellor {apoio}) nome={V.ten_nome(s)} tempo={tempo} | {s}")
    print('\n'.join(filas))
    print(f'frases dubidosas ou con desenlace: {n_dub} (a porta real con NLI pode aprobar parte das dubidosas)')


if __name__ == '__main__':
    main()
