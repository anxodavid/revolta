"""H1 e coincidencia léxica (sen NLI) das frases candidatas contra a ficha. Aproximación: sen o NLI non se sabe se
unha frase con coincidencia 0,5-0,8 pasa; con coincidencia >= 0,8 (un feito ou un par) pasa sempre a regra de apoio."""
import sys, re, yaml
sys.path.insert(0, '/home/user/revolta/herramientas/pipeline')
import ancoraxe, veracidade as V
tema = yaml.safe_load(open('/home/user/revolta/herramientas/pipeline/temas/meigas-de-verdade.yaml'))
def feitos(t):
    out = []
    for l in t['dossier'].strip().splitlines():
        l = re.sub(r'^\s*-\s*', '', l).strip(); l = re.sub(r'^\[[^\]]*\]\s*', '', l)
        if l: out.append(re.sub(r'\s*\((non |sen )[^)]*\)', '', l))
    return out
fs = feitos(tema)
anc = '\n'.join([tema['dossier'], tema['titulo'], tema['tema']])
for l in open(sys.argv[1]):
    if not l.strip() or l.startswith('#'): continue
    modo, f = [x.strip() for x in l.split('|', 1)]
    h1 = [x['texto'] for x in ancoraxe.ancoraxe(f, anc)['non_ancorados']]
    top = sorted(range(len(fs)), key=lambda i: -V.cobertura(f, fs[i]))[:4]
    best = max([(V.cobertura(f, fs[i]), (i + 1,)) for i in range(len(fs))] +
               [(V.cobertura(f, fs[a] + ' ' + fs[b]), (a + 1, b + 1)) for k, a in enumerate(top) for b in top[k + 1:]])
    lit = any(V._norm(f) in V._norm(p) for p in fs)
    estado = 'LITERAL' if lit else ('PASA(cob>=0.8)' if best[0] >= 0.8 else ('NLI?' if best[0] >= (0.6 if modo in 'GF' else 0.5) else 'FALLA(cob)'))
    if h1: estado = 'FALLA(H1)'
    print(f"[{modo}] {estado:14s} cob={best[0]:.2f} apoio={best[1]} h1={h1} :: {f}")
