"""Control H1-léxico: ancoraxe de nomes propios e cantidades no dossier de fontes.

Versión mínima e determinista do control H1 do plan (plan-de-negocio/gauntlet2/piezas/plan-desatendido.md §6):
cada nome propio (secuencia de palabras en maiúscula que non abre frase) e cada expresión de cantidade
(numerais escritos en letra, "século ..." ) que aparece no guion ten que aparecer tamén no dossier.
O que non está no dossier márcase como "non ancorado".

Que detecta: datas e cifras cambiadas ou inventadas, nomes propios que non están nas fontes.
Que NON detecta: frases inventadas sen nomes nin cifras, nomes do dossier trocados entre si
(Lemos <-> Andrade), cambios de sentido (quen fixo que). Iso sería H2 (xuíz LLM), sen implementar.
"""
import re
import unicodedata

# nomes que o canal usa sempre e non veñen do dossier
FIXOS = {'Serán', 'Boas', 'Isto', 'Galicia', 'Galiza', 'Cousas de Galiza'}
NUMERAIS = {
    'un', 'unha', 'dous', 'dúas', 'tres', 'catro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'once', 'doce',
    'trece', 'catorce', 'quince', 'dezaseis', 'dezasete', 'dezaoito', 'dezanove', 'vinte', 'trinta', 'corenta',
    'cincuenta', 'sesenta', 'setenta', 'oitenta', 'noventa', 'cen', 'cento', 'douscentos', 'duascentas',
    'douscentas', 'trescentos', 'trescentas', 'catrocentos', 'catrocentas', 'cincocentos', 'cincocentas',
    'seiscentos', 'setecentos', 'oitocentos', 'novecentos', 'mil', 'primeiro', 'segundo', 'terceiro'}
# un/unha só contan dentro dunha cantidade longa (mil ... e un); soltos son artigos
FEBLES = {'un', 'unha', 'primeiro', 'segundo'}


def _n(t):
    t = unicodedata.normalize('NFC', t.lower())
    return re.sub(r'\s+', ' ', re.sub(r"[^\wáéíóúüñç ]", ' ', t)).strip()


def _frases(texto):
    return [s for p in texto.split('\n\n') for s in re.split(r'(?<=[.!?…])\s+', ' '.join(p.split())) if s.strip()]


def nomes(frase):
    ws = re.findall(r"[\wáéíóúüñçÁÉÍÓÚÑ]+", frase)
    out, j = [], 1   # a primeira palabra da frase vai sempre en maiúscula
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
    ws = _n(frase).split()
    out, j = [], 0
    while j < len(ws):
        if ws[j] in NUMERAIS or ws[j] in ('século', 'séculos'):
            k = j
            # "un"/"unha" só continúan unha cantidade despois de "e" (mil ... e un): en "sesenta e sete un
            # movemento" o "un" é artigo (falso positivo de H1 na ronda 2)
            while True:
                if k + 1 < len(ws) and ws[k + 1] in NUMERAIS and ws[k + 1] not in FEBLES:
                    k += 1
                elif k + 2 < len(ws) and ws[k + 1] == 'e' and ws[k + 2] in NUMERAIS:
                    k += 2
                else:
                    break
            exp = ' '.join(ws[j:k + 1])
            if exp not in FEBLES and exp not in ('século', 'séculos'):
                out.append(exp)
            j = k + 1
        else:
            j += 1
    return out


def ancoraxe(guion, dossier, ignorar=()):
    """Devolve {'items': n, 'non_ancorados': [...], 'pct_ancorado': x}. `ignorar`: frases fixas (aviso)."""
    d = _n(dossier)
    items, fallos = 0, []
    for f in _frases(guion):
        if any(f in ig for ig in ignorar):
            continue
        for tipo, xs in (('nome', nomes(f)), ('cantidade', cantidades(f))):
            for x in xs:
                items += 1
                # palabra enteira: "dous" non se ancora en "douscentas" nin "cen" en "cincocentos"
                if not re.search(r'(?<!\w)' + re.escape(_n(x)) + r'(?!\w)', d):
                    fallos.append({'tipo': tipo, 'texto': x, 'frase': f})
    return {'items': items, 'non_ancorados': fallos,
            'pct_ancorado': round(100 * (items - len(fallos)) / items, 1) if items else 100.0}
