#!/usr/bin/env python3
"""Medidas da lista de planos v2 (peza PLANOS, Gauntlet 4): planos e duracións por fase (do corte que fai longo.py
--so-planos, `planos.json` do traballo), persoas facendo algo, arquetipos previstos, sementes, I2V, son, cámaras e
personaxes. Automático: só conta campos da lista; os xuízos (persoas, arquetipo previsto) son os do montador.

    python3 medir_lista.py [PLANOS_JSON_DO_TRABALLO]    # por defecto $SCRATCH/v2/w/planos.json
"""
import collections, json, os, sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
L = json.load(open(AQUI.parent / 'escenas-v2.json'))
E, PERS = L['escenas'], L['personaxes']
PJ = Path(sys.argv[1] if len(sys.argv) > 1 else os.environ.get(
    'SCRATCH', '/tmp/claude-0/-home-user-revolta/c92eba35-e89d-5d11-bb3d-f517a84dab48/scratchpad') + '/v2/w/planos.json')
T = {x['n']: x for x in json.load(open(PJ))} if PJ.exists() else {}
FASES = ['gancho', 'transicion', 'calma', 'durmir']
OBX = {'gancho': (3, 6), 'transicion': (5, 9), 'calma': (8, 14), 'durmir': (12, 20)}
r = {'planos': len(E)}
fase = {x['n']: T[x['n']]['fase'] for x in E} if T else {}
if T:
    r['por_fase'] = {}
    for f in FASES:
        ds = [T[x['n']]['dur_s'] for x in E if fase[x['n']] == f]
        lo, hi = OBX[f]
        r['por_fase'][f] = {'planos': len(ds), 'media_s': round(sum(ds) / len(ds), 1), 'min_s': min(ds),
                            'max_s': max(ds), 'obxectivo_s': [lo, hi],
                            'fora': [n for n in (x['n'] for x in E if fase[x['n']] == f)
                                     if not lo <= T[n]['dur_s'] <= hi]}
    esp = [x for x in E if fase[x['n']] != 'durmir']
    c = collections.Counter(x['persoas'] for x in esp)
    r['parte_esperta'] = {'planos': len(esp), 'persoas': dict(c),
                          'pct_persoas_facendo_algo': round(100 * c['fan'] / len(esp), 1),
                          'pct_con_mans_que_fan': round(100 * (c['fan'] + c['mans']) / len(esp), 1)}
    r['durmir_persoas'] = dict(collections.Counter(x['persoas'] for x in E if fase[x['n']] == 'durmir'))
    r['desde'] = {n: {'t0': T[n].get('t0'), 'metodo': T[n].get('metodo_desde')} for n in T if T[n].get('desde')}
arq = collections.defaultdict(list)
for x in E:
    if x.get('arquetipo_previsto'):
        arq[x['arquetipo_previsto']].append(x['n'])
r['arquetipos_previstos'] = {k: {'planos': v, 'separacion_min': min((b - a for a, b in zip(v, v[1:])), default=None)}
                             for k, v in arq.items()}
r['sementes'] = {x['n']: f"{x['referencia']['ficheiro'].split('/')[-1]} ({x['referencia']['modo']} "
                         f"{x['referencia']['forza']})" for x in E if x.get('referencia')}
r['animacion'] = dict(collections.Counter(x['animacion']['modo'] for x in E))
r['i2v_por_prioridade'] = {p: [x['n'] for x in E if x['animacion']['modo'] == 'i2v' and x['prioridade_i2v'] == p]
                           for p in (1, 2)}
r['camaras'] = dict(collections.Counter(x['animacion']['camara'] for x in E))
r['efectos'] = dict(collections.Counter(e for x in E for e in x['animacion']['efectos']))
r['son'] = dict(collections.Counter(x['son'] for x in E))
r['epoca_xx'] = [x['n'] for x in E if x.get('epoca')]
r['personaxes'] = {k: [x['n'] for x in E if v['prompt'] in x['prompt']] for k, v in PERS.items()}
pal = [len(x['prompt'].split()) for x in E]
r['prompt_palabras'] = {'media': round(sum(pal) / len(pal), 1), 'max': max(pal),
                        'mais_de_55': [x['n'] for x in E if len(x['prompt'].split()) > 55]}
print(json.dumps(r, ensure_ascii=False, indent=1))
