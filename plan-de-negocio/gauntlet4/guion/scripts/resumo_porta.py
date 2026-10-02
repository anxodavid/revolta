#!/usr/bin/env python3
"""Resumo lexible de porta_texto.json (saída de `longo.py --so-texto`). Guionista do Gauntlet 4 (axente Claude).

    python3 resumo_porta.py porta_texto.json

Imprime: as catro portas (lingua, H1, estilo, veracidade), os avisos de LanguageTool, os nomes ou cantidades sen
ancorar, o resumo do estilo e cada frase marcada pola veracidade co seu motivo, as medidas (implicación E,
coincidencia léxica, feitos de apoio) e se ten xustificación no ficheiro de excepcións.
"""
import json, sys


def main():
    d = json.load(open(sys.argv[1]))
    print('portas_texto:', d['portas_texto'], '| palabras:', d.get('palabras'))
    print(f"lingua: {len(d['lingua'])} avisos")
    for a in d['lingua']:
        print(f"  - [{a['regra']}] «{a['palabra']}»: {a['mensaxe']} | …{a['contexto']}…")
    h = d['h1_ancoraxe']
    print(f"H1: {h['items']} elementos, {h['pct_ancorado']} % ancorados, {len(h['non_ancorados'])} sen ancorar")
    for f in h['non_ancorados']:
        print(f"  - {f['tipo']}: {f['texto']} | {f['frase']}")
    e = d['estilo']
    print('estilo:', {k: e[k] for k in ('cifras', 'signos_prohibidos', 'preguntas', 'palabras_vetadas', 'aviso_literal',
                                         'formula_literal', 'max_nomes_novos_por_110_palabras')},
          '| frases fóra de 8-25 palabras:', len(e['frases_fora_8_25']))
    v = d['veracidade']
    print(f"veracidade: {v['frases_avaliadas']} frases, {len(v['marcadas'])} marcadas, {len(v['sen_xustificar'])} sen xustificar")
    for m in v['marcadas']:
        x = 'XUSTIFICADA' if m.get('xustificacion') else 'SEN XUSTIFICAR'
        print(f"  - S{m['i']} [{m['modo']}] {x} | E {m['E']} cob {m['cobertura']} apoio {m['apoio']} | {m['motivo']}\n    {m['frase']}")


if __name__ == '__main__':
    main()
