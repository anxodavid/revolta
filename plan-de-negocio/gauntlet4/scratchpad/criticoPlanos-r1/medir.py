# Contas do crítico de planos r1 (Gauntlet 4). Le escenas-v2.json unha vez e planos.json (fase), compón o prompt
# final coma imaxes.compor_prompt (extraído por ast, sen importar torch) e conta tokens co tokenizador CLIP de SDXL.
import ast, json, re, sys, collections
R = '/home/user/revolta'
S = '/tmp/claude-0/-home-user-revolta/c92eba35-e89d-5d11-bb3d-f517a84dab48/scratchpad'
d = json.load(open(f'{R}/plan-de-negocio/gauntlet4/planos/escenas-v2.json'))
E = d['escenas']; PX = d['personaxes']
fase = {p['n']: p for p in json.load(open(f'{S}/v2/w/planos.json'))}
src = open(f'{R}/herramientas/pipeline/imaxes.py').read()
tree = ast.parse(src)
keep = {'ESTILOS', 'ESTILO_DEFECTO', 'ESTILO_FASE', 'LUZ_FASE', 'LUZ_RX', 'TIPO_FRASE', 'CAMARA_RX', 'CORRECCION',
        'INTERIOR_RX', 'PRUDENTE', 'INTENTO_PRUDENTE', 'compor_prompt'}
nodes = []
for n in tree.body:
    if isinstance(n, ast.Assign) and any(getattr(t, 'id', None) in keep for t in n.targets): nodes.append(n)
    if isinstance(n, ast.FunctionDef) and n.name in keep: nodes.append(n)
g = {'re': re, 'os': __import__('os')}
exec(compile(ast.Module(body=nodes, type_ignores=[]), 'imaxes_ext', 'exec'), g)
g.setdefault('INTENTO_PRUDENTE', 99)
from transformers import CLIPTokenizer
tok = CLIPTokenizer.from_pretrained(f'{S}/hf/hub/models--stabilityai--stable-diffusion-xl-base-1.0/snapshots/462165984030d82259a11f4367a4eed129e94a7b/tokenizer')
out = {}
for i, p in enumerate(E):
    n = p['n']; f = fase[n]['fase']
    e = dict(p, fase=f)
    final = g['compor_prompt'](e, i=i)
    ids = tok(final, truncation=False).input_ids
    perdido = tok.decode(ids[76:-1]) if len(ids) > 77 else ''
    pre = final[:final.find(p['prompt'][:20])] if p['prompt'][:20] in final else '?'
    out[n] = dict(fase=f, dur=fase[n]['dur_s'], cap=fase[n].get('capitulo'), pal=len(p['prompt'].split()),
                  tok=len(ids), prefixo=pre, perdido=perdido, final=final)
json.dump(out, open(f'{S}/criticoPlanos-r1/tokens.json', 'w'), ensure_ascii=False, indent=0)
# fases e capítulos
cnt = collections.Counter(o['fase'] for o in out.values()); print('fases', dict(cnt))
caps = []; prev = None
for n in sorted(out):
    if out[n]['cap'] != prev: caps.append((n, out[n]['cap'])); prev = out[n]['cap']
print('capitulos (plano, nome):', caps)
fr = [f for p in E for f in p['frases']]; print('frases', fr[0], fr[-1], 'contiguas', fr == list(range(1, 109)) or sorted(set(fr)) == list(range(1,109)))
esp = [p for p in E if out[p['n']]['fase'] != 'durmir']
c = collections.Counter(p.get('persoas') for p in esp); print('esperta', len(esp), dict(c), 'fan %.1f' % (100*c['fan']/len(esp)), 'fan+mans %.1f' % (100*(c['fan']+c['mans'])/len(esp)))
print('animacion', collections.Counter(p['animacion']['modo'] for p in E), 'sementes', [p['n'] for p in E if p.get('referencia')])
print('>55 palabras', [p['n'] for p in E if len(p['prompt'].split()) > 55])
print('prioridade', collections.Counter(p.get('prioridade_i2v') for p in E if p['animacion']['modo']=='i2v'))
bad = [(p['n'], p['animacion']) for p in E if p['animacion'].get('camara') not in ('avanza','recua','xira_esq','xira_der','sobe','baixa','pan_esq','pan_der') or any(x not in ('lume','candea','choiva','bretema','fume','auga','ceo','po') for x in p['animacion'].get('efectos',[]))]
print('animacion fóra do admitido', bad)
print('i2v sen accion', [p['n'] for p in E if p['animacion']['modo']=='i2v' and not p['animacion'].get('accion')])
# tokens
print('\nTOKENS (final > 77):')
for n, o in out.items():
    if o['tok'] > 77: print(f" {n} [{o['fase']}] {o['pal']} pal, {o['tok']} tok; prefixo={o['prefixo']!r}; PERDE: {o['perdido']!r}")
print(' planos > 77 tokens:', sum(o['tok'] > 77 for o in out.values()))
# personaxes: texto literal en cada plano
print('\nPERSONAXES (literal no prompt):')
for k, v in PX.items():
    s = v['prompt']; ns = [p['n'] for p in E if s in p['prompt']]
    print(f' {k}: {ns}')
    for n in ns:
        o = out[n]
        if o['perdido'] and s[-25:] in o['final'] and o['final'].find(s) + len(s) > len(o['final']) - len(o['perdido']) - 2:
            print(f'   ! no plano {n} a descrición de {k} cae (en parte) despois do token 77')
# palabras de risco no prompt (non no negativo)
RISCO = r'\b(kitchen|street|lane|road|door|doors|window|windows|lamp|lamps|house|houses|cottage|village|town|city|chimney|witch|broom|cauldron|hat|warts?|devil|demon|fire|flames?|embers?|hearth|firelight|candle|bonfire|crowd|book|books|cap)\b'
print('\nPALABRAS DE RISCO nos prompts:')
for p in E:
    w = sorted(set(m.lower() for m in re.findall(RISCO, p['prompt'], re.I)))
    if w: print(f" {p['n']} [{out[p['n']]['fase']}]: {', '.join(w)}")
