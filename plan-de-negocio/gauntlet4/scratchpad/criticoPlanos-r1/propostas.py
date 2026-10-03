# Comproba os prompts propostos polo crítico: prompt final (coma imaxes.compor_prompt) e tokens de CLIP.
import ast, json, re
R = '/home/user/revolta'
S = '/tmp/claude-0/-home-user-revolta/c92eba35-e89d-5d11-bb3d-f517a84dab48/scratchpad'
d = json.load(open(f'{R}/plan-de-negocio/gauntlet4/planos/escenas-v2.json'))
E = {p['n']: p for p in d['escenas']}
fase = {p['n']: p['fase'] for p in json.load(open(f'{S}/v2/w/planos.json'))}
src = open(f'{R}/herramientas/pipeline/imaxes.py').read()
keep = {'ESTILOS', 'ESTILO_DEFECTO', 'ESTILO_FASE', 'LUZ_FASE', 'LUZ_RX', 'TIPO_FRASE', 'CAMARA_RX', 'CORRECCION',
        'INTERIOR_RX', 'PRUDENTE', 'INTENTO_PRUDENTE', 'compor_prompt'}
nodes = [n for n in ast.parse(src).body if (isinstance(n, ast.Assign) and any(getattr(t, 'id', None) in keep for t in n.targets)) or (isinstance(n, ast.FunctionDef) and n.name in keep)]
g = {'re': re, 'os': __import__('os')}
exec(compile(ast.Module(body=nodes, type_ignores=[]), 'x', 'exec'), g); g.setdefault('INTENTO_PRUDENTE', 99)
from transformers import CLIPTokenizer
tok = CLIPTokenizer.from_pretrained(f'{S}/hf/hub/models--stabilityai--stable-diffusion-xl-base-1.0/snapshots/462165984030d82259a11f4367a4eed129e94a7b/tokenizer')
P = json.load(open(f'{S}/criticoPlanos-r1/propostas.json'))
LUZ = [l for v in g['LUZ_FASE'].values() for l in v]
for k, newp in P.items():
    n = int(k); e = dict(E[n], prompt=newp, fase=fase[n])
    fin = g['compor_prompt'](e, i=list(E).index(n))
    ids = tok(fin, truncation=False).input_ids
    pre = fin[:fin.find(newp[:15])]
    luzdef = [l for l in LUZ if fin.endswith(l)]
    print(f"{n} [{fase[n]}] {len(newp.split())} pal, {len(ids)} tok{' PERDE: '+repr(tok.decode(ids[76:-1])) if len(ids)>77 else ''}; prefixo extra={pre.split(', ')[-1]!r}{' LUZ DEFECTO '+repr(luzdef) if luzdef else ''}")
