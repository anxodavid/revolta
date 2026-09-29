#!/usr/bin/env python
"""Control C0: erros canario. Inxecta 20 erros coñecidos, un a un, nunha copia do guion xa aprobado e mide
cantos detectan os controis de texto que o pipeline aplica de verdade:

  - LanguageTool 6.8 gl-ES con hunspell (qa.lingua, co mesmo filtro de nomes do dossier)
  - H1-léxico (ancoraxe.py): nomes propios e cantidades que non están no dossier
  - estilo (qa.estilo): cifras, signos e palabras vetadas

    python canarios.py temas/irmandinos-apertura.yaml GUION.txt --saida DIR   -> DIR/canarios.json, canarios.md

Un canario conta como detectado se algún control novo (que non saía no guion limpo) sinala un texto que
contén o fragmento inxectado. Os 20 canarios están pensados para o guion de irmandinos-apertura; para
outro tema hai que escribir outros (mesmas catro familias).
"""
import argparse, json, sys, time
from pathlib import Path
import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import ancoraxe, qa

# (familia, texto orixinal, texto con erro, fragmento que debe sinalarse)
CANARIOS = [
    # castelanismos: 2 evidentes (palabra que non existe en galego) e 3 sutís (palabras galegas válidas ou case)
    ('castelanismo', 'Hoxe só se escoita', 'Hoy só se escoita', 'Hoy'),
    ('castelanismo', 'e, lonxe, algún paxaro', 'e, lejos, algún paxaro', 'lejos'),
    ('castelanismo', 'xa cara ao final', 'xa hacia o final', 'hacia'),
    ('castelanismo', 'Os tempos, ademais, eran difíciles', 'Os tempos, sen embargo, eran difíciles', 'embargo'),
    ('castelanismo', 'á beira da pobreza', 'ao borde da pobreza', 'borde'),
    # datas e cantidades cambiadas ou inventadas
    ('data', 'metade do século quince', 'metade do século catorce', 'catorce'),
    ('data', 'Había xa un século', 'Había xa dous séculos', 'dous'),
    ('data', 'Unhas décadas antes', 'Trinta anos antes', 'Trinta'),
    ('data', 'Durante uns poucos anos,', 'Desde mil catrocentos setenta e sete,', 'setenta'),
    ('data', 'Moitos anos despois, as testemuñas', 'Cen anos despois, as testemuñas', 'Cen'),
    # nomes trocados
    ('nome', 'como a de Lemos ou a de Andrade', 'como a de Moscoso ou a de Andrade', 'Moscoso'),
    ('nome', 'como a de Lemos ou a de Andrade', 'como a de Andrade ou a de Lemos, e sobre todo a de Lemos', 'Lemos'),
    ('nome', 'e era do arcebispo de Compostela', 'e era do bispo de Lugo', 'Lugo'),
    ('nome', 'dun gran señor das Mariñas', 'dun gran señor do Morrazo', 'Morrazo'),
    ('nome', 'rendas dos señores viñan minguando en toda Europa', 'rendas dos señores viñan minguando en toda Castela', 'Castela'),
    # frases sen fonte (inventadas)
    ('sen_fonte', 'e botárona abaixo.', 'e botárona abaixo. O arcebispo gardaba alí un tesouro de moedas de ouro.', 'tesouro'),
    ('sen_fonte', 'foron castigados.', 'foron castigados. Os labregos levaban tres días sen durmir cando chegaron.', 'tres'),
    ('sen_fonte', 'e botárona abaixo.', 'e botárona abaixo. Contan que a última pedra caeu nunha noite de lúa chea.', 'lúa'),
    ('sen_fonte', 'foron castigados.', 'foron castigados. Despois, moitos señores fuxiron a Portugal.', 'Portugal'),
    ('sen_fonte', 'coma unha semente que agarda outra primavera.',
     'coma unha semente que agarda outra primavera. Aquela foi a revolta máis grande de toda Europa.', 'grande'),
]


def sinais(guion, tema, frases_fn):
    lt = qa.lingua(guion, dossier=tema['dossier'])
    an = ancoraxe.ancoraxe(guion, tema['dossier'], [tema['aviso']])
    es = qa.estilo(guion, frases_fn(guion), tema['aviso'], tema['palabras'])
    out = [('languagetool', m['contexto']) for m in lt]
    out += [('h1_lexico', f"{x['texto']} | {x['frase']}") for x in an['non_ancorados']]
    out += [('estilo', ' '.join(es['cifras'] + es['signos_prohibidos'] + es['palabras_vetadas']))] if (
        es['cifras'] or es['signos_prohibidos'] or es['palabras_vetadas']) else []
    return out


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('tema'); ap.add_argument('guion')
    ap.add_argument('--saida', required=True); a = ap.parse_args()
    from pipeline import partir
    tema = yaml.safe_load(open(a.tema)); guion = Path(a.guion).read_text().strip()
    t0 = time.time()
    base = sinais(guion, tema, partir)
    res = []
    for fam, orix, erro, frag in CANARIOS:
        assert orix in guion, f'canario non aplicable: {orix}'
        g = guion.replace(orix, erro, 1)
        novos = [s for s in sinais(g, tema, partir) if s not in base]
        det = [s for s in novos if frag.lower() in s[1].lower()]
        res.append({'familia': fam, 'erro': erro, 'fragmento': frag, 'detectado': bool(det),
                    'por': sorted({s[0] for s in det}), 'sinais_novos': novos})
        print(f"{fam:13s} {'SI ' if det else 'non'} {erro[:60]}", flush=True)
    fams = sorted({r['familia'] for r in res})
    resumo = {f: f"{sum(r['detectado'] for r in res if r['familia'] == f)}/{sum(r['familia'] == f for r in res)}"
              for f in fams}
    tot = sum(r['detectado'] for r in res)
    out = {'data': time.strftime('%Y-%m-%d'), 'tema': tema['id'], 'sinais_no_guion_limpo': base,
           'detectados': tot, 'total': len(res), 'pct': round(100 * tot / len(res), 1), 'por_familia': resumo,
           'segundos': round(time.time() - t0, 1), 'canarios': res}
    S = Path(a.saida); S.mkdir(parents=True, exist_ok=True)
    (S / 'canarios.json').write_text(json.dumps(out, ensure_ascii=False, indent=1))
    L = [f"# Control C0 (erros canario): {tema['id']}", '',
         f"Detectados **{tot}/{len(res)} ({out['pct']} %)** cos controis de texto implementados "
         '(LanguageTool gl-ES + hunspell, H1-léxico, estilo). Sinais no guion limpo (falsos positivos de base): '
         f"{len(base)}. Tempo: {out['segundos']} s.", '', '| Familia | Detectados |', '|---|---|']
    L += [f'| {f} | {v} |' for f, v in resumo.items()]
    L += ['', '| Familia | Erro inxectado | Detectado | Por |', '|---|---|---|---|']
    L += [f"| {r['familia']} | {r['erro']} | {'si' if r['detectado'] else 'NON'} | {', '.join(r['por']) or '-'} |"
          for r in res]
    (S / 'canarios.md').write_text('\n'.join(L) + '\n')
    print(json.dumps({k: out[k] for k in ('detectados', 'total', 'pct', 'por_familia')}, ensure_ascii=False))


if __name__ == '__main__':
    main()
