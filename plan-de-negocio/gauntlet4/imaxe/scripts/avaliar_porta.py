"""Avaliación da porta v6 fronte á anterior (VERSION 8 coa lista ampliada da rolda de arranxos) sobre as 173 imaxes
etiquetadas da v1, sen volver executar os modelos: Florence-2-base coas descricións gardadas pola produción
(revision.json, a mesma Florence-2-base), CLIP-L cos embeddings gardados por calibrar_clip.py, e o lume ao durmir
calculado nas imaxes. Uso: $PY avaliar_porta.py REVISOR_ANTERIOR.py  -> calibracion/porta-v6.json"""
import importlib.util, json, os, sys
from pathlib import Path
import numpy as np
AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
sys.path.insert(0, str(REPO / 'herramientas/pipeline')); sys.path.insert(0, str(AQUI))
import calibrar_clip as c
import revisor as v6
S = Path(os.environ['SCRATCH']) / 'imaxe4'


def cargar_modulo(p, nome):
    spec = importlib.util.spec_from_file_location(nome, p); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


class ClipGardado:
    """Os métodos de revisor.Clip cos embeddings de texto gardados (sen cargar o modelo)."""
    def __init__(self, T, ix):
        self.T, self.ix = T, ix
    def textos(self, lista):
        return np.stack([self.T[self.ix[t]] for t in lista])


def main():
    v8 = cargar_modulo(sys.argv[1], 'revisor_v8')
    E, T, ix, et = c.cargar()
    cg = ClipGardado(T, ix)
    fl = {(x['n'], x['version']): x for x in json.load(open(S / 'calib_florence_gardado.json'))}
    esc = json.load(open(REPO / 'plan-de-negocio/gauntlet3/video/escenas-montadas.json'))
    ims = dict(((d['n'], d['version']), p) for d, p in c.imaxes())
    out = []
    for i, d in enumerate(et):
        x = fl[(d['n'], d['version'])]
        e = esc[d['n'] - 1]
        prompt, fase = x['prompt'], d['fase']
        epoca = 'xx' if d['seculo_xx'] else None
        quente = v6.lume_quente(ims[(d['n'], d['version'])])
        lume = [f'lume vivo ao durmir ({quente:.1%})'] if fase == 'durmir' and quente > float(os.environ.get('REVISOR_LUME_DURMIR', '0.015')) else []
        # anterior: lista v8 + arranxos e CLIP v5 (3 recortes); o veto de lume grande xa tiña a excepción do prompt
        p8 = [et_ for et_, rx, *exc in v8.LISTA if __import__('re').search(rx, x['texto_florence']) and not (exc and __import__('re').search(exc[0], x['texto_florence']))]
        if prompt and __import__('re').search(r'\b(fire|flames?|bonfires?|blaze|queimada|burning)\b', prompt, __import__('re').I):
            p8 = [y for y in p8 if y != 'lume grande no exterior']
        c8, _ = v8.Clip.iconografia(cg, E[i, :3], None)   # sen o `negativo` do plano (non cambia na v6 e os seus textos non están gardados)
        k8, _ = v8.Clip.clave(cg, E[i, :3], e.get('clave')) if d['version'] == 'actual' else ([], {})
        # v6
        p6 = v6.filtrar_contexto(v6.lista_anacronismos(x['texto_florence']), prompt, epoca)
        c6, _ = v6.Clip.iconografia(cg, E[i], None)
        c6 = v6.filtrar_contexto(c6, prompt, epoca)
        k6, det = v6.Clip.clave(cg, E[i], e.get('clave')) if d['version'] == 'actual' else ([], {})
        out.append({'n': d['n'], 'version': d['version'], 'tribunal': d['tribunal'], 'defectos': sorted(c.defectos(d)),
                    'clave': e.get('clave') if d['version'] == 'actual' else None, 'clave_ve': d['clave_ve'],
                    'v8': sorted(set(p8 + c8 + lume)), 'v8_falta': k8, 'v6': sorted(set(p6 + c6 + lume)), 'v6_falta': k6})
    def conta(chave, cond):
        xs = [o for o in out if cond(o)]
        return f"{sum(bool(o[chave]) for o in xs)}/{len(xs)}"
    resumo = {}
    for nome, cond in [('bloquea', lambda o: o['tribunal'] == 'bloquea'), ('molesta', lambda o: o['tribunal'] == 'molesta'),
                       ('menor', lambda o: o['tribunal'] == 'menor'),
                       ('defectos de Claude', lambda o: o['tribunal'] not in ('bloquea', 'molesta', 'menor') and o['defectos']),
                       ('funciona (tribunal)', lambda o: o['tribunal'] == 'funciona' and not o['defectos']),
                       ('aceptable (falsos da v5 segundo o tribunal)', lambda o: o['tribunal'] == 'aceptable' and not o['defectos']),
                       ('limpas sen mención', lambda o: o['tribunal'] in ('sen_mencion', 'despois_dos_arranxos') and not o['defectos'])]:
        resumo[nome] = {'v8': conta('v8', cond), 'v6': conta('v6', cond)}
    acl = [o for o in out if o['version'] == 'actual' and o['clave']]
    resumo['clave: ausentes cazadas'] = {'v8': f"{sum(bool(o['v8_falta']) for o in acl if not o['clave_ve'])}/{sum(not o['clave_ve'] for o in acl)}",
                                         'v6': f"{sum(bool(o['v6_falta']) for o in acl if not o['clave_ve'])}/{sum(not o['clave_ve'] for o in acl)}"}
    resumo['clave: falsas alarmas'] = {'v8': f"{sum(bool(o['v8_falta']) for o in acl if o['clave_ve'])}/{sum(o['clave_ve'] for o in acl)}",
                                       'v6': f"{sum(bool(o['v6_falta']) for o in acl if o['clave_ve'])}/{sum(o['clave_ve'] for o in acl)}"}
    print(json.dumps(resumo, ensure_ascii=False, indent=1))
    for o in out:
        if o['tribunal'] in ('bloquea', 'molesta') and not o['v6']:
            print('escapa v6:', o['n'], o['version'], o['defectos'])
        if (not o['defectos']) and o['v6']:
            print('marca v6 sen defecto:', o['n'], o['version'], o['tribunal'], o['v6'])
    dest = AQUI.parent / 'calibracion' / 'porta-v6.json'
    dest.write_text(json.dumps({'descricion': __doc__.strip(), 'resumo': resumo, 'imaxes': out}, ensure_ascii=False, indent=1))
    print(dest)


if __name__ == '__main__':
    main()
