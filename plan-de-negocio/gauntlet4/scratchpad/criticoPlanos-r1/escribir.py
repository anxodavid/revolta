# Escribe plan-de-negocio/gauntlet4/veredictos/planos-r1.md: táboa plano a plano (xuízo do crítico), contas
# automáticas e o parche de cambios, comprobado contra o prompt final da pipeline (tokens de CLIP).
import ast, json, re, statistics
R = '/home/user/revolta'
S = '/tmp/claude-0/-home-user-revolta/c92eba35-e89d-5d11-bb3d-f517a84dab48/scratchpad'
d = json.load(open(f'{R}/plan-de-negocio/gauntlet4/planos/escenas-v2.json'))
E = {p['n']: p for p in d['escenas']}
PL = {p['n']: p for p in json.load(open(f'{S}/v2/w/planos.json'))}
T = {int(k): v for k, v in json.load(open(f'{S}/criticoPlanos-r1/tokens.json')).items()}
FA = {'gancho': 'G', 'transicion': 'T', 'calma': 'Ca', 'durmir': 'D'}

# (correlación, atractivo, riscos): xuízo do crítico
X = {
 1: (4, 5, 'I2V dun animal: doado'), 2: (5, 5, 'fío de lume no I2V; "flames" (arquetipo lareira)'),
 3: (5, 4, ''), 4: (5, 4, 'semente 11-01; eco do 70 (porta de repetición)'),
 5: (5, 4, '80 tok (perde "17th century"); "cap" → gorra plana'), 6: (5, 4, 'o home, sen roupa e distinto do 8'),
 7: (5, 4, 'I2V: mans calzando un zapato'), 8: (5, 4, 'I2V: salto; o home, distinto do 6'),
 9: (4, 3, 'aviso: candea que se apaga no 76'), 10: (4, 4, 'semente 01-02 con recorte'),
 11: (4, 4, '"flames" (arquetipo lareira)'), 12: (5, 3, '78 tok; mesmo cadro ca o 59'),
 13: (5, 5, ''), 14: (4, 3, 'bodegón do feixe (1 de 3)'), 15: (5, 3, 'pseudotexto (é o suxeito)'),
 16: (4, 5, ''), 17: (4, 3, ''), 18: (4, 4, 'fórmula de cámara anteposta; entrega no I2V'),
 19: (4, 4, 'vela na man (biblia §4)'), 20: (5, 4, 'golilla (1623) en 1617'), 21: (5, 4, ''),
 22: (5, 4, ''), 23: (5, 4, 'luz por defecto contra "grey clouds"'), 24: (4, 3, ''), 25: (5, 4, ''),
 26: (5, 3, 'pseudotexto (é o suxeito)'), 27: (5, 3, 'pseudotexto (é o suxeito)'),
 28: (5, 4, '80 tok (perde a candea)'), 29: (5, 4, '87 tok (perde "stand alone below him")'), 30: (5, 4, ''),
 31: (3, 2, 'bodegón do feixe (2 de 3) co rótulo do cap. II'), 32: (4, 3, 'pseudotexto'),
 33: (5, 5, '"flames" (arquetipo lareira)'), 34: (5, 4, ''), 35: (4, 2, 'bodegón; pseudotexto'),
 36: (4, 3, 'pseudotexto nas tarxetas'), 37: (5, 2, 'pseudotexto no formulario'),
 38: (4, 3, 'multitude: caras clonadas; "flames"'), 39: (4, 3, 'fórmula de cámara anteposta'),
 40: (4, 3, '92 tok (perde o hábito do inquisidor); 3 personaxes'), 41: (4, 3, ''),
 42: (5, 4, 'fórmula de cámara anteposta'), 43: (4, 4, ''), 44: (4, 4, '4 ou máis persoas'),
 45: (4, 4, '94 tok (perde o escribán que escribe)'), 46: (4, 4, '86 tok (perde o aceno); quen le?'),
 47: (4, 3, 'paisaxe baleira (co rótulo do cap. IV)'), 48: (5, 4, ''), 49: (5, 5, 'fórmula de cámara anteposta'),
 50: (5, 4, 'escribe sen dicir con que'), 51: (5, 4, 'ollos: monstro?; mesmo cadro ca o 63'), 52: (4, 4, ''),
 53: (5, 4, ''), 54: (5, 5, '82 tok; persignarse no I2V'), 55: (5, 5, 'I2V: catro mans; semente 06-01'),
 56: (5, 4, ''), 57: (4, 4, ''), 58: (5, 3, '78 tok (perde "century")'), 59: (4, 3, 'mesmo cadro ca o 12'),
 60: (4, 5, ''), 61: (4, 4, 'a sombra pode non saír'), 62: (4, 3, 'bodegón do feixe (3 de 3)'),
 63: (5, 3, 'fórmula anteposta; mesmo cadro ca o 51'), 64: (4, 3, ''),
 65: (5, 4, 'I2V: salto; lume ao durmir; "embers"'), 66: (5, 5, 'I2V: auga nas mans'),
 67: (5, 3, 'fórmula anteposta'), 68: (5, 4, 'semente 07-01; luz por defecto "mist in the moonlight"'),
 69: (5, 5, '87 tok; lume ao durmir (porta)'), 70: (4, 4, 'eco do 4 (porta de repetición)'),
 71: (5, 4, '86 tok; cara á cámara ao durmir'), 72: (4, 3, 'fórmula anteposta; lume ao durmir'), 73: (4, 4, ''),
 74: (5, 4, ''), 75: (4, 3, 'fórmula anteposta'), 76: (5, 4, 'fórmula anteposta; vela ao durmir; apagala no I2V'),
 77: (4, 3, 'fórmula anteposta'),
}
assert sorted(X) == sorted(E)

def curto(t, n=46):
    if len(t) <= n: return t
    return t[:n].rsplit(' ', 1)[0].rstrip(',.:;') + '…'

rows = []
for n in sorted(E):
    c, a, r = X[n]
    rows.append(f"| {n} | {FA[T[n]['fase']]} | {curto(E[n]['texto'])} | {c} | {a} | {r or '—'} |")
corr = [X[n][0] for n in E]; atr = [X[n][1] for n in E]
ge4 = sum(c >= 4 for c in corr)
stats = dict(ge4=ge4, pct=100 * ge4 / len(E), cm=statistics.mean(corr), am=statistics.mean(atr))

# ---------- parche
P = json.load(open(f'{S}/criticoPlanos-r1/propostas.json'))
extra = {
 5: {'negativo': E[5]['negativo'] + ', flat cap, baseball cap, cowboy hat',
     'animacion': dict(E[5]['animacion'], accion='the man speaks, holding his hat to his chest, while the scribe writes')},
 7: {'animacion': {'modo': 'paralaxe', 'camara': 'baixa', 'efectos': ['candea']}, 'prioridade_i2v': 3},
 8: {'animacion': dict(E[8]['animacion'], accion='he jolts upright from the bench and flings his arms wide')},
 31: {'clave': 'magnifying glass', 'negativo': 'hands, fingers, electric lamp, printed text, typewriter, plastic, computer',
      'tipo': 'detalle', 'epoca': 'xx', 'persoas': 'non', 'arquetipo_previsto': '',
      'animacion': {'modo': 'paralaxe', 'camara': 'avanza', 'efectos': ['po']}, 'prioridade_i2v': 3},
 40: {'animacion': {'modo': 'paralaxe', 'camara': 'pan_der', 'efectos': ['po']}, 'prioridade_i2v': 3},
 54: {'animacion': dict(E[54]['animacion'], accion='the old woman slowly turns her head toward the darkness while the young woman fills the jug')},
 55: {'animacion': dict(E[55]['animacion'], accion="the girl slowly grinds the herbs with the pestle while her mother's hand rests on hers")},
 59: {'animacion': dict(E[59]['animacion'], efectos=[])},
 65: {'animacion': {'modo': 'paralaxe', 'camara': 'recua', 'efectos': ['fume', 'bretema']}, 'prioridade_i2v': 3},
 69: {'negativo': E[69]['negativo'] + ', fireplace, candles'},
}
parche = {'personaxes': {
    'xuiz': {'prompt': 'a stern grey-bearded judge in a black gown with a stiff white collar'},
    'home_parto': {'quen': 'o home do conto de Dorotea (Vilalba, 1617)',
                   'prompt': 'a burly man with a short black beard in a coarse linen shirt'},
    'maria': {'prompt_curto': 'a woman of about thirty in a faded red wool headscarf'},
    'dorotea': {'prompt_curto': 'an old midwife in a dark brown wool headscarf'},
    'escriban': {'prompt_curto': 'a gaunt clean-shaven scribe in a black wool doublet'},
    'cibreira': {'prompt_curto': 'a woman in a grey wool headscarf'}},
  'escenas': {}}
for n in sorted(set(map(int, P)) | set(extra)):
    ch = {}
    if str(n) in P: ch['prompt'] = P[str(n)]
    ch.update(extra.get(n, {}))
    parche['escenas'][str(n)] = ch

# comprobación: prompt final da pipeline <= 77 tokens e sen fórmula de cámara anteposta
src = open(f'{R}/herramientas/pipeline/imaxes.py').read()
keep = {'ESTILOS', 'ESTILO_DEFECTO', 'ESTILO_FASE', 'LUZ_FASE', 'LUZ_RX', 'TIPO_FRASE', 'CAMARA_RX', 'CORRECCION',
        'INTERIOR_RX', 'PRUDENTE', 'compor_prompt'}
nodes = [x for x in ast.parse(src).body if (isinstance(x, ast.Assign) and any(getattr(t, 'id', None) in keep for t in x.targets)) or (isinstance(x, ast.FunctionDef) and x.name in keep)]
g = {'re': re, 'os': __import__('os'), 'INTENTO_PRUDENTE': 99}
exec(compile(ast.Module(body=nodes, type_ignores=[]), 'x', 'exec'), g)
from transformers import CLIPTokenizer
tok = CLIPTokenizer.from_pretrained(f'{S}/hf/hub/models--stabilityai--stable-diffusion-xl-base-1.0/snapshots/462165984030d82259a11f4367a4eed129e94a7b/tokenizer')
ESTILO = 'cinematic film still, period drama, photorealistic'
for k, ch in parche['escenas'].items():
    n = int(k); e = dict(E[n], **ch, fase=PL[n]['fase'])
    fin = g['compor_prompt'](e, i=0)
    nt = len(tok(fin, truncation=False).input_ids)
    pre = fin[len(ESTILO):fin.find(e['prompt'][:15])]
    assert nt <= 77, (n, nt)
    assert not re.search(g['CAMARA_RX'], pre, re.I), (n, pre)
    ch_tok = nt
    parche['escenas'][k] = ch
    print(n, nt)
# personaxes literais despois do parche
lit = {'home_parto': [6, 8]}
for k, ns in lit.items():
    for n in ns:
        assert parche['personaxes'][k]['prompt'] in parche['escenas'][str(n)]['prompt'], (k, n)
for n in (20, 40, 42, 45, 46):
    assert parche['personaxes']['xuiz']['prompt'].replace('a stern ', '') in parche['escenas'][str(n)]['prompt'], n

tabla = '\n'.join(rows)
pj = '{\n "personaxes": {\n' + ',\n'.join(f'  "{k}": ' + json.dumps(v, ensure_ascii=False) for k, v in parche['personaxes'].items()) + '\n },\n "escenas": {\n' + ',\n'.join(f'  "{k}": ' + json.dumps(v, ensure_ascii=False) for k, v in parche['escenas'].items()) + '\n }\n}'
json.loads(pj)
md = open(f'{S}/criticoPlanos-r1/plantilla.md').read()
md = md.replace('{{TABOA}}', tabla).replace('{{PARCHE}}', pj)
md = md.replace('{{GE4}}', str(stats['ge4'])).replace('{{PCT}}', f"{stats['pct']:.1f}".replace('.', ','))
md = md.replace('{{CM}}', f"{stats['cm']:.1f}".replace('.', ',')).replace('{{AM}}', f"{stats['am']:.1f}".replace('.', ','))
open(f'{R}/plan-de-negocio/gauntlet4/veredictos/planos-r1.md', 'w').write(md)
print(stats, 'cambios:', len(parche['escenas']))
