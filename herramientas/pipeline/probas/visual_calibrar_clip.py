"""Calibración das portas de CLIP de revisor.py (Gauntlet 3, peza VISUAL): iconografía, repetición e arquetipos.

    flock "$CPU_LOCK" $PY probas/visual_calibrar_clip.py ETIQUETAS.json [--saida CALIB.json]

ETIQUETAS.json: [{"f": ruta, "malos": ["tellados laranxas (CLIP)", ...], "arq": "camiñantes de costas" | null,
"grupo": "nome do prompt" | null, "dudosa": true (fóra do cálculo dos umbrais)}]. As etiquetas púxoas Claude (axente) mirando as imaxes: fotogramas da ronda 1,
2 e 3 do Gauntlet 2 (cos defectos que viu o crítico visual), as imaxes da comparativa de modelos e escenas alleas
feitas adrede (Toscana, Andalucía, oliveiras, palmeiras, rodas de raios, eucaliptos).

Para cada par malo/bo de revisor.PARES imprime a marxe (sim malo - sim bo, no peor recorte) das imaxes malas e das
boas, e o umbral que as separa mellor; para a repetición, a similitude entre imaxes do mesmo prompt (mesma escena,
outro modelo ou estilo) e entre prompts distintos; para os arquetipos, a similitude de cada imaxe co seu texto.
"""
import argparse, json, sys
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import revisor


def mellor_umbral(bos, malos):
    """Umbral que minimiza erros (falsos positivos + falsos negativos); en empate, o máis alto."""
    cands = sorted(set(bos + malos))
    mellor = None
    for t in cands + [max(cands) + 1e-3]:
        fp = sum(x > t for x in bos); fn = sum(x <= t for x in malos)
        if mellor is None or fp + fn < mellor[1] + mellor[2] or (fp + fn == mellor[1] + mellor[2] and t > mellor[0]):
            mellor = (t, fp, fn)
    return mellor


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('etiquetas'); ap.add_argument('--saida', default=None)
    a = ap.parse_args()
    et = json.loads(Path(a.etiquetas).read_text())
    cl = revisor.Clip()
    T = cl.textos([t for _, x, y in revisor.PARES for t in (x, y)])
    TA = cl.textos([t for _, t, _ in revisor.ARQUETIPOS])
    rows = []
    for x in et:
        E, emb = cl.analizar(x['f'])
        pares = {}
        for k, (lab, _, _) in enumerate(revisor.PARES):
            sb, sg = E @ T[2 * k], E @ T[2 * k + 1]
            pares[lab] = (float((sb - sg).max()), float(max(sb.max(), sg.max())))
        sa = TA @ emb
        rows.append({**x, 'pares': pares, 'emb': emb, 'arq_sims': {revisor.ARQUETIPOS[j][0]: round(float(sa[j]), 3)
                                                                   for j in range(len(sa))}})
    out = {'pares': {}, 'repeticion': {}, 'arquetipos': {}}
    print('== Iconografía: marxe (sim malo - sim bo) e pertinencia')
    for lab, _, _ in revisor.PARES:
        malos = [r for r in rows if lab in r.get('malos', []) and not r.get('dudosa')]
        bos = [r for r in rows if not r.get('malos') and not r.get('dudosa')]
        dud = [(round(r['pares'][lab][0], 3), Path(r['f']).name) for r in rows if r.get('dudosa')]
        mm = sorted((round(r['pares'][lab][0], 3), Path(r['f']).name) for r in malos)
        bb = sorted((round(r['pares'][lab][0], 3), Path(r['f']).name) for r in bos)[::-1]
        u = mellor_umbral([v for v, _ in bb], [v for v, _ in mm]) if mm else None
        print(f'\n{lab}: malas {mm}\n   boas (as 6 máis altas) {bb[:6]}\n   dubidosas {dud}\n   umbral óptimo {u}')
        out['pares'][lab] = {'malas': mm, 'boas_top': bb[:10], 'umbral': u}
    # conceptos do campo `negativo`: sim("a photo with X") nas imaxes que o teñen e nas que non
    NEG = {'tellados laranxas (CLIP)': 'orange roof tiles', 'ciprés (CLIP)': 'cypress trees', 'palmeiras (CLIP)': 'palm trees',
           'rodas de raios (CLIP)': 'spoked wheels', 'oliveiras (CLIP)': 'olive trees',
           'muros encalados (CLIP)': 'whitewashed walls', 'eucaliptos (CLIP)': 'eucalyptus trees'}
    print('\n== Campo negativo: sim("a photo with X") (máx. dos 3 recortes)')
    out['negativo'] = {}
    todos_bos, todos_malos, rel_bos, rel_malos = [], [], [], []
    base = cl.textos(['a photo'])[0]
    Es = {r['f']: cl.analizar(r['f'])[0] for r in rows}
    for lab, x in NEG.items():
        t = cl.textos([f'a photo with {x}'])[0]
        val = lambda r: float((Es[r['f']] @ t).max())
        rel = lambda r: float((Es[r['f']] @ t - Es[r['f']] @ base).max())   # fronte a "a photo" (mesmo recorte)
        con = [r for r in rows if lab in r.get('malos', []) and not r.get('dudosa')]
        sen = [r for r in rows if not r.get('malos') and not r.get('dudosa')]
        si, no = sorted(round(val(r), 3) for r in con), sorted(round(val(r), 3) for r in sen)
        rsi, rno = sorted(round(rel(r), 3) for r in con), sorted(round(rel(r), 3) for r in sen)
        todos_bos += no; todos_malos += si; rel_bos += rno; rel_malos += rsi
        print(f'{x}: con {si} | sen: máx {no[-3:]} p95 {round(float(np.percentile(no, 95)), 3)}')
        print(f'   relativo a "a photo": con {rsi} | sen: máx {rno[-3:]}')
        out['negativo'][x] = {'con': si, 'sen_top': no[-5:], 'rel_con': rsi, 'rel_sen_top': rno[-5:]}
    u = mellor_umbral(todos_bos, todos_malos); ur = mellor_umbral(rel_bos, rel_malos)
    print('umbral común óptimo (absoluto)', u, '| (relativo a "a photo")', ur)
    out['negativo']['umbral_comun'] = u; out['negativo']['umbral_relativo'] = ur
    # repetición
    grupos = {}
    for k, r in enumerate(rows):
        if r.get('grupo'):
            grupos.setdefault(r['grupo'], []).append(k)
    mesmo, distinto = [], []
    for i in range(len(rows)):
        for j in range(i + 1, len(rows)):
            if not rows[i].get('grupo') or not rows[j].get('grupo'):
                continue
            s = float(rows[i]['emb'] @ rows[j]['emb'])
            (mesmo if rows[i]['grupo'] == rows[j]['grupo'] else distinto).append(
                (round(s, 3), Path(rows[i]['f']).name, Path(rows[j]['f']).name))
    mesmo.sort(); distinto.sort()
    q = lambda v, p: round(float(np.percentile([x[0] for x in v], p)), 3) if v else None
    print('\n== Repetición (coseno dos embeddings medios)')
    print('mesmo prompt: n', len(mesmo), 'mín', mesmo[:3], 'p10', q(mesmo, 10), 'mediana', q(mesmo, 50))
    print('prompts distintos: n', len(distinto), 'máx', distinto[-5:], 'p99', q(distinto, 99), 'mediana', q(distinto, 50))
    out['repeticion'] = {'mesmo_p10': q(mesmo, 10), 'mesmo_mediana': q(mesmo, 50), 'distinto_p99': q(distinto, 99),
                         'distinto_max': distinto[-5:], 'mesmo_min': mesmo[:5]}
    # arquetipos
    print('\n== Arquetipos (sim co texto)')
    for lab, _, _ in revisor.ARQUETIPOS:
        si = sorted((r['arq_sims'][lab], Path(r['f']).name) for r in rows if r.get('arq') == lab)
        no = sorted((r['arq_sims'][lab], Path(r['f']).name) for r in rows if r.get('arq') != lab)[::-1]
        u = mellor_umbral([v for v, _ in no], [v for v, _ in si]) if si else None
        print(f'{lab}: si {si}\n   non (as 5 máis altas) {no[:5]}\n   umbral óptimo {u}')
        out['arquetipos'][lab] = {'si': si, 'non_top': no[:8], 'umbral': u}
    # arquetipo asignado a cada imaxe co umbral actual
    print('\n== Arquetipo asignado (ARQ_SIM actual =', revisor.ARQ_SIM, ')')
    for r in rows:
        best = max(r['arq_sims'].items(), key=lambda kv: kv[1])
        asig = best[0] if best[1] >= revisor.ARQ_SIM else None
        if asig or r.get('arq'):
            print(f"{Path(r['f']).name}: etiqueta {r.get('arq')} | asignado {asig} ({best[1]})")
    if a.saida:
        for r in rows:
            r.pop('emb')
        out['filas'] = rows
        Path(a.saida).write_text(json.dumps(out, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
