#!/usr/bin/env python3
"""Medidas dun guion de longo.py (Gauntlet 4, peza GUION). Escrito polo guionista (axente Claude), 02-10-2026.

    python3 medidas.py GUION.txt [--fases 232,640,1200] [--json saida.json]

Le o guion coas mesmas regras ca `longo.ler_guion` (parágrafos separados por liña baleira, "## " = capítulo que non
se narra, "%%" = nota que non se narra) e parte as frases coa mesma expresión ca `pipeline.partir`. Mide:

- palabras (total, por capítulo e por fase) e minutos estimados con tres modelos (ver `minutos`);
- palabras por frase (media, máxima e frases > 28 ou < 8) por fase;
- atribucións por 100 palabras (lista ATRIB, a mesma idea ca o crítico A do Gauntlet 3: segundo, di que, contou,
  escribiu, recolleu, explica, advirte...) e cantas veces sae "segundo";
- nomes propios novos por 100 palabras (secuencias en maiúscula que non abren frase, como `ancoraxe.nomes`);
- cantidades e anos en letra por 100 palabras (como `ancoraxe.cantidades`);
- controis de estilo: díxitos, interrogacións, parénteses e comiñas, subcadea "imaxina", aviso e fórmula literais.

`--fases` son as palabras onde rematan o gancho, a transición e a calma (por defecto, as do plan da rolda 1 para
12 min: 232, 640 e 1.200); `--fases-cap 1,3,5` tómaas do comezo dos capítulos (gancho = capítulo inicial,
transición = I e II, calma = III e IV, durmir = V). Todo é automático e aproximado; non substitúe a lectura dos
críticos.
"""
import argparse, json, re, sys
from pathlib import Path

AVISO = 'Boas noites. A voz que vas escoitar é sintética, e este texto preparouno un proceso automático.'
FORMULA = 'Isto é Cousas de Galiza para durmir.'
# Atribucións: verbos e expresións que atribúen unha afirmación a unha fonte ou a unha testemuña.
ATRIB = [r'\bsegundo\b', r'\bpara (?:o|a) (?:investigador|historiador|antropólogo)\b', r'\bdi que\b', r'\bdin que\b',
         r'\bdixo\b', r'\bdixera\b', r'\bcontou\b', r'\bcontaba\b', r'\bconta que\b', r'\bconta\b', r'\bdeclara\b',
         r'\bdeclarou\b', r'\bconfesou\b', r'\bescribiu que\b', r'\bescribiu,', r'\brecolleu\b', r'\badvirte\b',
         r'\bexplica\b', r'\blembra\b', r'\bpensa que\b', r'\bcre que\b', r'\bchámalle\b', r'\batopou\b',
         r'\badvertía\b', r'\bdicían que\b', r'\bcontouno\b']
FIXOS = {'Boas', 'Isto', 'Galicia', 'Galiza', 'Cousas de Galiza', 'Cousas'}
NUMERAIS = set('''un unha dous dúas tres catro cinco seis sete oito nove dez once doce trece catorce quince dezaseis
dezasete dezaoito dezanove vinte trinta corenta cincuenta sesenta setenta oitenta noventa cen cento douscentos
trescentos catrocentos cincocentos seiscentos setecentos oitocentos novecentos mil'''.split())
FEBLES = {'un', 'unha'}


def ler(path):
    pars, caps = [], []
    for b in re.split(r'\n\s*\n', Path(path).read_text().strip()):
        b = ' '.join(b.split())
        if not b:
            continue
        if b.startswith('## '):
            caps.append({'titulo': b[3:].strip(), 'par0': len(pars)})
        elif not b.startswith('%%'):
            pars.append(b)
    return pars, caps


def frases(pars):
    out, pal = [], 0
    for pi, p in enumerate(pars):
        for s in re.split(r'(?<=[.!?…])\s+', p):
            if s.strip():
                n = len(s.split())
                out.append({'i': len(out) + 1, 'par': pi, 'texto': s.strip(), 'pal0': pal, 'n': n})
                pal += n
    return out, pal


def nomes(frase):
    ws = re.findall(r"[\wáéíóúüñçÁÉÍÓÚÑ]+", frase)
    out, j = [], 1
    while j < len(ws):
        if ws[j][0].isupper():
            k = j
            while k + 1 < len(ws) and (ws[k + 1][0].isupper() or (ws[k + 1] in ('de', 'da', 'do') and k + 2 < len(ws)
                                                                     and ws[k + 2][0].isupper())):
                k += 1
            out.append(' '.join(ws[j:k + 1])); j = k + 1
        else:
            j += 1
    return [n for n in out if n not in FIXOS]


def cantidades(frase):
    ws = re.sub(r"[^\wáéíóúüñç ]", ' ', frase.lower()).split()
    out, j = [], 0
    while j < len(ws):
        if ws[j] in NUMERAIS:
            k = j
            while True:
                if k + 1 < len(ws) and ws[k + 1] in NUMERAIS and ws[k + 1] not in FEBLES:
                    k += 1
                elif k + 2 < len(ws) and ws[k + 1] == 'e' and ws[k + 2] in NUMERAIS:
                    k += 2
                else:
                    break
            exp = ' '.join(ws[j:k + 1])
            if exp not in FEBLES:
                out.append(exp)
            j = k + 1
        else:
            j += 1
    return out


def fase_de(pal0, lim):
    return ('gancho', 'transicion', 'calma', 'durmir')[sum(pal0 >= x for x in lim)]


# ritmo medido na v1 por fase, palabras/min con pausas (gauntlet3/veredictos/tribunal-final.md §4)
RITMO_V1 = {'gancho': 157.0, 'transicion': 154.5, 'calma': 136.3, 'durmir': 114.5}


def minutos(fr, tot, lim):
    """Tres estimacións: (1) media da v1 (31:22 con 3.952 palabras); (2) ritmo da v1 por fase aplicado ás fases de
    contido deste guion (`lim`); (3) a curva de curva.py tal como está (nós en palabras absolutas: 280 e 950)."""
    m1 = tot * (31 * 60 + 22) / 3952 / 60
    m2 = sum(f['n'] / RITMO_V1[fase_de(f['pal0'], lim)] for f in fr)
    t = max(tot, 950 + 200); met = max(950 + 100, t // 2)
    lim3 = (280, 950, met)
    m3 = sum(f['n'] / RITMO_V1[fase_de(f['pal0'], lim3)] for f in fr)
    return round(m1, 2), round(m2, 2), round(m3, 2)


def mmss(m):
    return f'{int(m)}:{int(round((m - int(m)) * 60)):02d}'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('guion'); ap.add_argument('--fases', default='232,640,1200'); ap.add_argument('--json')
    ap.add_argument('--fases-cap', default=None,
                    help='capítulos (1 = o primeiro "##") onde empezan a transición, a calma e o durmir, p. ex. 1,3,5')
    a = ap.parse_args()
    lim = [int(x) for x in a.fases.split(',')]
    pars, caps = ler(a.guion)
    fr, tot = frases(pars)
    if a.fases_cap:
        p0 = {}
        for f in fr:
            p0.setdefault(f['par'], f['pal0'])
        lim = [p0[caps[int(k) - 1]['par0']] for k in a.fases_cap.split(',')]
    texto = '\n\n'.join(pars)
    fixa = lambda f: f['texto'] in AVISO or f['texto'] == FORMULA
    res = {'palabras': tot, 'frases': len(fr), 'capitulos': len(caps), 'fases_palabras': lim}
    m1, m2, m3 = minutos(fr, tot, lim)
    res['minutos'] = {'media_v1': m1, 'ritmo_v1_por_fase_de_contido': m2, 'curva_actual_280_950': m3}
    # tempo acumulado (modelo 2) por frase, para o mapa
    t = 0.0
    for f in fr:
        f['t0'] = round(t, 2); t += f['n'] / RITMO_V1[fase_de(f['pal0'], lim)]
        f['fase'] = fase_de(f['pal0'], lim)
    # capítulos
    par_ini = {}
    for f in fr:
        par_ini.setdefault(f['par'], f)
    cap_rows = []
    marcas = [{'titulo': '(inicial)', 'par0': 0}] + caps
    for k, c in enumerate(marcas):
        p1 = marcas[k + 1]['par0'] if k + 1 < len(marcas) else len(pars)
        sub = [f for f in fr if c['par0'] <= f['par'] < p1]
        cap_rows.append({'titulo': c['titulo'], 'palabras': sum(f['n'] for f in sub),
                         'comeza_min': mmss(sub[0]['t0']) if sub else None})
    res['por_capitulo'] = cap_rows
    # por fase
    por_fase = {}
    vistos = set()
    for ph in ('gancho', 'transicion', 'calma', 'durmir'):
        sub = [f for f in fr if f['fase'] == ph and not fixa(f)]
        pal = sum(f['n'] for f in sub)
        txt = ' '.join(f['texto'] for f in sub)
        at = sum(len(re.findall(rx, txt, re.I)) for rx in ATRIB)
        nn = 0
        for f in sub:
            for n in nomes(f['texto']):
                if n not in vistos:
                    vistos.add(n); nn += 1
        q = sum(len(cantidades(f['texto'])) for f in sub)
        por_fase[ph] = {'palabras': pal, 'frases': len(sub),
                        'palabras_por_frase_media': round(pal / max(1, len(sub)), 1),
                        'frase_max': max((f['n'] for f in sub), default=0),
                        'atribucions': at, 'atribucions_por_100': round(100 * at / max(1, pal), 2),
                        'nomes_novos': nn, 'nomes_novos_por_100': round(100 * nn / max(1, pal), 2),
                        'cantidades': q, 'cantidades_por_100': round(100 * q / max(1, pal), 2)}
    res['por_fase'] = por_fase
    esperta = [f for f in fr if f['fase'] != 'durmir' and not fixa(f)]
    pe = sum(f['n'] for f in esperta)
    ate = sum(len(re.findall(rx, ' '.join(f['texto'] for f in esperta), re.I)) for rx in ATRIB)
    res['parte_esperta'] = {'palabras': pe, 'atribucions': ate, 'atribucions_por_100': round(100 * ate / max(1, pe), 2)}
    res['segundo'] = len(re.findall(r'\bsegundo\b', texto, re.I))
    res['frases_mais_de_28'] = [(f['i'], f['n'], f['texto']) for f in fr if f['n'] > 28]
    res['frases_menos_de_8'] = [(f['i'], f['n'], f['texto']) for f in fr if f['n'] < 8 and not fixa(f)]
    res['estilo'] = {'digitos': re.findall(r'\d+', texto), 'interrogacions': texto.count('?') + texto.count('¿'),
                     'signos': re.findall(r'[()\[\]"«»*#/]', texto), 'imaxina': 'imaxina' in texto.lower(),
                     'aviso_literal': AVISO in texto, 'formula_literal': FORMULA in texto,
                     'aviso_palabra': next((f['pal0'] for f in fr if f['texto'].startswith('Boas noites')), None),
                     'aviso_min': next((mmss(f['t0']) for f in fr if f['texto'].startswith('Boas noites')), None)}
    res['nomes_distintos'] = sorted(vistos)
    if a.json:
        Path(a.json).write_text(json.dumps({'medidas': res, 'frases': fr}, ensure_ascii=False, indent=1))
    print(json.dumps(res, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
