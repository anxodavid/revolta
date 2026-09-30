"""Proba de fume do dossier contra as portas do pipeline (H1 e veracidade), con frases candidatas de guion.
Non é o guion: son frases escritas por Claude para medir se o dossier as apoia (e se rexeita as falsas)."""
import sys, json, yaml
sys.path.insert(0, '/home/user/revolta/herramientas/pipeline')
import pipeline as P, veracidade, ancoraxe
tema = yaml.safe_load(open('/home/user/revolta/herramientas/pipeline/temas/meigas-de-verdade.yaml'))
anc = P.ancora(tema)
fs = [P.literal(f) for f in P.feitos(tema)]
print('feitos:', len(fs), flush=True)
v = veracidade.Verificador(fs)
frases = [l.split('|', 1) for l in open(sys.argv[1]).read().strip().split('\n') if l.strip() and not l.startswith('#')]
res = []
for modo, f in frases:
    modo, f = modo.strip(), f.strip()
    h1 = ancoraxe.ancoraxe(f, anc)['non_ancorados']
    import time; t0 = time.time()
    r = v.frase(f, 'gancho' if modo in ('G', 'F') else 'relato', actores=(modo in ('G', 'F')))
    ok = r['ok'] and not h1
    esperado = modo != 'F'
    print(f"{'OK ' if ok else 'MAL'} {'(esperado)' if ok == esperado else '(!!)'} [{modo}] E={r['E']} cob={r['cobertura']} apoio={r['apoio']} "
          f"h1={[x['texto'] for x in h1]} motivo={r['motivo']} t={time.time()-t0:.1f}s :: {f}", flush=True)
    res.append({'modo': modo, 'frase': f, 'ok': ok, 'E': r['E'], 'cob': r['cobertura'], 'apoio': r['apoio'],
                'h1': [x['texto'] for x in h1], 'motivo': r['motivo']})
json.dump(res, open(sys.argv[2], 'w'), ensure_ascii=False, indent=1)
