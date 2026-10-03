#!/usr/bin/env python3
"""Xera plan-de-negocio/gauntlet4/planos/escenas-v2.json (Gauntlet 4, peza PLANOS, rolda 1).

Os planos (frases, prompt, clave, son, animación...) escribiunos o montador (axente Claude) en tramo1.py e tramo2.py;
este script só os xunta, enche `texto` coas palabras exactas que se oen (de frases.json da voz, para non trabucar
nada) e comproba a continuidade: cada frase do guion nun plano e só un corte a metade de frase por `desde`.

    python3 xerar_lista.py [FRASES_JSON]     # por defecto $SCRATCH/v2/w/frases.json
"""
import json, os, re, sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
SAIDA = AQUI.parent / 'escenas-v2.json'
FJ = Path(sys.argv[1] if len(sys.argv) > 1 else
          os.environ.get('SCRATCH', '/tmp/claude-0/-home-user-revolta/c92eba35-e89d-5d11-bb3d-f517a84dab48/scratchpad')
          + '/v2/w/frases.json')

# Personaxes recorrentes: descritos sempre coas mesmas palabras (regra da lista de planos)
PERS = {
    'dorotea': 'an old midwife of about sixty, lined face, grey hair under a dark brown wool headscarf',
    'maria': 'a woman of about thirty, dark braided hair under a faded red wool headscarf',
    'escriban': 'a gaunt clean-shaven scribe of about forty in a black wool doublet with a white collar',
    'testemuna': 'a bearded peasant man in a coarse brown wool jacket',
    'xuiz': 'a stern grey-bearded judge in a black gown with a stiff white golilla collar',
    'vicario': 'a stern priest in a black cassock and black cape',
    'inquisidor': 'an elderly inquisitor in a white habit and black cape',
    'cibreira': 'a pale exhausted woman of about forty, dark hair under a grey wool headscarf, worn grey wool dress',
    'nai_cibreira': 'an old healer with white hair under a black wool headscarf',
    'curandeira': 'an old village healer in a dark blue wool shawl',
    'mariano': 'a dark-haired man of about forty in a white shirt and dark wool sweater',
    'amigos': 'two friends in white shirts and dark wool sweaters',
    'vecinos': 'two village men in sheepskin vests and wool breeches',
    'moza': 'a young woman with a long dark braid, white linen blouse and dark shawl',
    'feijoo': 'an elderly Benedictine monk with thin white hair and a lined face, in a black hooded habit',
    'sarmiento': 'a stout Benedictine friar of about fifty with a round face, in a black habit',
    'vella_q': 'an old woman in a black cardigan and dark headscarf',
    'vello_q': 'an old man with white stubble in a dark wool waistcoat',
}
NOMES = {
    'dorotea': 'Dorotea do Barro, a parteira (Vilalba, 1617)', 'maria': 'María do Barro, a filla (Vilalba, 1617)',
    'escriban': 'o escribán do proceso (1617 e 1639: o mesmo papel, "quen escribía")',
    'testemuna': 'a testemuña de Vilalba (1617)', 'xuiz': 'o xuíz da Real Audiencia (xustiza civil)',
    'vicario': 'o vicario xeral de Mondoñedo', 'inquisidor': 'o inquisidor (Santiago)',
    'cibreira': 'María Cibreira (Boborás, 1639)', 'nai_cibreira': 'a nai de María Cibreira',
    'curandeira': 'a menciñeira xenérica (a meiga que cura)', 'mariano': 'Mariano Marcos Abalo (1967)',
    'amigos': 'os amigos do barco (1967)', 'vecinos': 'os veciños de Campo Lameiro (1642-1643)',
    'moza': 'a moza da noite de san Xoán', 'feijoo': 'Benito Xerónimo Feijoo (s. XVIII)',
    'sarmiento': 'frei Martín Sarmiento (s. XVIII)', 'vella_q': 'a vella da queimada (s. XX)',
    'vello_q': 'o vello que ergue o cazo (s. XX)',
}
NEG = 'electric light, light bulb, lamp, glass window, modern clothes, street lamp'
NEG_XX = 'neon, plastic, television, smartphone'
P = []


def pl(frases, en, tipo, prompt, clave, son, anim, prio, persoas, desde=None, ref=None, epoca=None, neg='',
       arq=None):
    """Un plano. anim = (modo, camara, [efectos], accion ou None)."""
    modo, cam, ef, acc = anim
    a = {'modo': modo, 'camara': cam, 'efectos': ef}
    if acc:
        a['accion'] = acc
    x = {'n': len(P) + 1, 'frases': frases}
    if desde:
        x['desde'] = desde
    x.update(texto=None, texto_en=en, prompt=prompt.format(**PERS), clave=clave,
             negativo=', '.join(v for v in ((NEG_XX if epoca else NEG), neg) if v),
             tipo=tipo, son=son)
    if ref:
        x['referencia'] = ref
    x['animacion'] = a
    x['prioridade_i2v'] = prio
    if epoca:
        x['epoca'] = epoca
    x['persoas'] = persoas
    if arq:
        x['arquetipo_previsto'] = arq
    P.append(x)


def norm(s):
    return re.sub(r'[^\wáéíóúñü]+', ' ', s.lower()).strip()


def pos_desde(texto, desde):
    """Posición (en caracteres) de `desde` no texto da frase, sen contar maiúsculas nin puntuación."""
    m = re.search(r'\W+'.join(map(re.escape, desde.split())), texto, re.I)
    if not m:
        raise SystemExit(f'desde non atopado: {desde!r} en {texto!r}')
    return m.start()


def main():
    F = {x['i']: x['texto'] for x in json.load(open(FJ))}
    for t in ('tramo1.py', 'tramo2.py'):
        if (AQUI / t).exists():
            exec((AQUI / t).read_text(), {'pl': pl, 'PERS': PERS})
    # continuidade: cada plano empeza onde acabou o anterior (frase seguinte, ou a mesma frase con `desde`)
    for k, x in enumerate(P):
        fr = x['frases']
        assert fr == list(range(fr[0], fr[-1] + 1)), f"plano {x['n']}: frases non consecutivas {fr}"
        if k == 0:
            assert fr[0] == 1 and 'desde' not in x
        else:
            prev = P[k - 1]['frases'][-1]
            assert (fr[0] == prev + 1 and 'desde' not in x) or (fr[0] == prev and 'desde' in x), \
                f"plano {x['n']}: empeza na frase {fr[0]} e o anterior acaba na {prev}"
    for k, x in enumerate(P):
        partes = []
        for i in x['frases']:
            a, b = 0, len(F[i])
            if i == x['frases'][0] and x.get('desde'):
                a = pos_desde(F[i], x['desde'])
            if i == x['frases'][-1] and k + 1 < len(P) and P[k + 1].get('desde') and P[k + 1]['frases'][0] == i:
                b = pos_desde(F[i], P[k + 1]['desde'])
            assert a < b, f"plano {x['n']}: corte baleiro na frase {i}"
            partes.append(F[i][a:b].strip())
        x['texto'] = ' '.join(partes)
    ult = P[-1]['frases'][-1] if P else 0
    d = {'descricion': 'Lista de planos v2 de "As meigas de verdade" (Gauntlet 4, peza PLANOS, rolda 1). Escribiuna '
                       'o montador (axente Claude) frase a frase sobre guion/guion-r2.txt; ningunha persoa a revisou. '
                       'Formato: gauntlet4/contexto.md §6.1, máis texto_en, prioridade_i2v, persoas e '
                       'arquetipo_previsto (metadatos para medir; o pipeline non os usa). Xerada con '
                       'scripts/xerar_lista.py.',
         'personaxes': {k: {'quen': NOMES[k], 'prompt': v} for k, v in PERS.items()},
         'frases_cubertas': f'1-{ult} de {len(F)}',
         'escenas': P}
    tmp = SAIDA.with_suffix('.tmp')
    tmp.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n')
    os.replace(tmp, SAIDA)
    print(f'{len(P)} planos, frases 1-{ult} de {len(F)} -> {SAIDA}')


if __name__ == '__main__':
    main()
