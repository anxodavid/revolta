"""Medida automática de correlación imaxe-texto (Gauntlet 4, peza IMAXE): ¿ilustra cada imaxe o que se oe no seu plano?

CLIP ViT-L/14 (MIT, o mesmo da porta) entre a imaxe de cada plano (media dos 3 recortes cadrados) e a versión en
inglés do que se oe nese plano (`texto_en`, tradución fiel, non descrición da imaxe). A cifra de cada plano é un z:
canto se parece a imaxe ao seu texto fronte a canto se parece aos demais textos dun banco común
(z = (sim(propio) - media(banco)) / desviación(banco)). Para comparar dous episodios (v1 fronte a v2) úsase o MESMO
banco: os textos dos dous.

Calibración (02-10-2026, 162 planos da v1, etiquetas de Claude "ilustra o que se oe" 2/1/0): z medio 1,89 nos que
ilustran, 0,57 nos de ambiente e 0,39 nos desconectados; AUC 0,90 entre os que ilustran e os desconectados. O 79 % dos
que ilustran teñen z >= 1; dos desconectados, o 21 %. Limitacións: CLIP premia a coincidencia literal (calquera muller
"casa" cunha frase sobre mulleres), non entende negacións nin quen fai que a quen, e trunca o texto aos 77 tokens.
É unha medida de apoio para os críticos, non un xuízo.

    flock "$CPU_LOCK" $PY correlacion.py --planos PLANOS.json --imaxes DIR [--banco OUTRO.json ...] [--saida X.json]

PLANOS.json: lista (ou {"planos": [...]}) de {"n", "texto_en", opcional "ficheiro"}. Sen "ficheiro", as imaxes de DIR
(.png/.jpg) ordenadas por nome son os planos 1, 2, 3...
"""
import argparse, json, os, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
Z_ILUSTRA, Z_DESCONECTADO = 1.0, 0.5


def ler_planos(p):
    d = json.loads(Path(p).read_text())
    d = d.get('planos', d) if isinstance(d, dict) else d
    return [x for x in d if x.get('texto_en')]


def medir(planos, imaxes, banco_textos, clip):
    import numpy as np
    banco = list(dict.fromkeys(banco_textos))
    B = clip.textos(banco)
    out = []
    for x, f in zip(planos, imaxes):
        _, emb = clip.analizar(f)
        s_banco = B @ emb
        propio = float(clip.textos([x['texto_en']])[0] @ emb)
        outros = np.array([v for t, v in zip(banco, s_banco) if t != x['texto_en']])
        z = (propio - outros.mean()) / (outros.std() + 1e-6)
        out.append({'n': x['n'], 'imaxe': Path(f).name, 'sim': round(propio, 4), 'z': round(float(z), 3),
                    'texto_en': x['texto_en'][:200]})
    return out


def resumo(res):
    import numpy as np
    z = np.array([r['z'] for r in res])
    return {'planos': len(res), 'z_medio': round(float(z.mean()), 3), 'z_mediana': round(float(np.median(z)), 3),
            'ilustran (z >= 1)': round(float((z >= Z_ILUSTRA).mean()), 3),
            'desconectados (z < 0,5)': round(float((z < Z_DESCONECTADO).mean()), 3),
            'peores': [(r['n'], r['z']) for r in sorted(res, key=lambda r: r['z'])[:10]]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--planos', required=True)
    ap.add_argument('--imaxes', required=True)
    ap.add_argument('--banco', nargs='*', default=[], help='outros ficheiros de planos con texto_en (o banco común)')
    ap.add_argument('--saida')
    a = ap.parse_args()
    import revisor
    planos = ler_planos(a.planos)
    d = Path(a.imaxes)
    if all(x.get('ficheiro') for x in planos):
        imaxes = [d / x['ficheiro'] for x in planos]
    else:
        fs = sorted(f for f in d.iterdir() if f.suffix.lower() in ('.png', '.jpg', '.jpeg') and f.name[:3].isdigit())
        imaxes = [fs[x['n'] - 1] for x in planos]
    banco = [x['texto_en'] for x in planos] + [x['texto_en'] for b in a.banco for x in ler_planos(b)]
    clip = revisor.Clip()
    res = medir(planos, imaxes, banco, clip)
    r = {'resumo': resumo(res), 'banco': len(set(banco)), 'planos': res}
    print(json.dumps(r['resumo'], ensure_ascii=False, indent=1))
    if a.saida:
        Path(a.saida).write_text(json.dumps(r, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
