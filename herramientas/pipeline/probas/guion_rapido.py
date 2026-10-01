"""Gauntlet 3 (guion): Comprobación rápida (sin NLI ni LanguageTool) del guion: palabras, capítulos, minuto estimado, H1, estilo y
cobertura léxica de la veracidad (misma regla que veracidade.py sin el NLI). Uso: python rapido.py GUION [--lt]"""
import sys, re, yaml
sys.path.insert(0, '/home/user/revolta/herramientas/pipeline')
import pipeline as P, ancoraxe, qa, curva, veracidade as V
import longo
tema = yaml.safe_load(open('/home/user/revolta/herramientas/pipeline/temas/meigas-de-verdade.yaml'))
texto, caps = longo.ler_guion(sys.argv[1])
frases = P.partir(texto)
pal = 0
for f in frases:
    f['pal0'] = pal; pal += len(f['texto'].split())
tot = pal
# tiempo estimado: modelo simple (s/palabra) interpolado por la curva
def spw(w):
    c = curva.en(w, tot)
    return 0.43 * c['escala'] + c['pausa_frase'] / 15 + c['pausa_parrafo'] / 60
t, tiempos = 1.5, {}
for f in frases:
    tiempos[f['i']] = t
    t += sum(spw(f['pal0'] + k) for k in range(len(f['texto'].split())))
print(f'PALABRAS {tot}  frases {len(frases)}  duración estimada {t/60:.1f} min')
# capítulos
pars = [p for p in texto.split('\n\n')]
par_ini = {}
for f in frases:
    par_ini.setdefault(f['par'], f)
bounds = [('(gancho)', 0)] + [(c['titulo'], c['par0']) for c in caps]
for k, (tit, p0) in enumerate(bounds):
    p1 = bounds[k + 1][1] if k + 1 < len(bounds) else len(pars)
    fs = [f for f in frases if p0 <= f['par'] < p1]
    if not fs: continue
    w = sum(len(f['texto'].split()) for f in fs)
    t0 = tiempos[fs[0]['i']]
    print(f"  {tit:40s} pal {w:5d}  desde pal {fs[0]['pal0']:5d}  min {t0/60:5.1f}  fase {curva.en(fs[0]['pal0'], tot)['fase']}")
anc = P.ancora(tema)
h1 = ancoraxe.ancoraxe(texto, anc, [tema['aviso'], longo.FORMULA])
print('H1 non ancorados:', [(x['tipo'], x['texto']) for x in h1['non_ancorados']])
e = qa.estilo(texto, frases, tema['aviso'], tema['palabras'], formula=longo.FORMULA)
print('ESTILO cifras', e['cifras'], 'signos', e['signos_prohibidos'], 'preguntas', e['preguntas'], 'vetadas', e['palabras_vetadas'],
      'aviso', e['aviso_literal'], 'formula', e['formula_literal'], 'max_nomes_110', e['max_nomes_novos_por_110_palabras'])
fl = [f for f in frases if f['i'] in e['frases_fora_8_25']]
print('frases fóra 8-25:', len(fl))
for f in fl:
    print('   ', len(f['texto'].split()), 'pal0', f['pal0'], '|', f['texto'])
# aviso dentro do primeiro minuto
for f in frases:
    if f['texto'].startswith('Boas noites'):
        print(f"AVISO en pal0={f['pal0']} t≈{tiempos[f['i']]:.0f} s")
# cobertura léxica
fs = [P.literal(x) for x in P.feitos(tema)]
print('--- veracidade léxica (req = frase esixida; cob<0.8 necesita NLI) ---')
for f in frases:
    tx = f['texto']
    if tx in tema['aviso'] or tx == longo.FORMULA: continue
    gancho = f['pal0'] < curva.GANCHO
    lit = any(V._norm(tx) in V._norm(p) for p in fs)
    ds = V.desenlaces(tx)
    tempo = re.search(V.TEMPO_LONGO, V._sen_acentos(tx).replace('seculo', 'século'))
    req = gancho or V.ten_nome(tx) or bool(tempo) or bool(ds)
    dossier_pap = {x for p in fs for x in V.papeis(p)}
    verbos_d = {v for v, _ in dossier_pap}
    mal = [f'{c} + {v}' for v, c in V.papeis(tx) if v in verbos_d and (v, c) not in dossier_pap]
    if lit:
        est, cob, ap = 'LIT', 1.0, ''
    else:
        top = sorted(range(len(fs)), key=lambda i: -V.cobertura(tx, fs[i]))[:4]
        best = max([(V.cobertura(tx, fs[i]), (i + 1,)) for i in range(len(fs))] +
                   [(V.cobertura(tx, fs[a] + ' ' + fs[b]), (a + 1, b + 1)) for k, a in enumerate(top) for b in top[k + 1:]])
        cob, ap = best
        est = 'ok' if cob >= 0.8 else ('NLI?' if cob >= (0.6 if gancho else 0.5) else 'FALLA')
    if not req and not ds and not mal: 
        continue
    if est == 'LIT' or (est == 'ok' and not ds and not mal):
        if '-v' not in sys.argv: continue
    print(f"{'G' if gancho else 'R'} {est:5s} cob={cob:.2f} ap={ap} ds={ds} mal={mal} :: {tx}")
