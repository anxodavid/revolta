"""Porta de VERACIDADE (H2 mínimo): cada frase afirmativa do guion ten que estar implicada polos feitos do dossier.

Engadida na ronda 3 do Gauntlet 2 (29-09-2026) despois de que o LLM local escribise no gancho "a irmandade venceu"
(falso: a irmandade foi derrotada en 1469) sen que ningunha porta o vise.

Como decide, por frase (premisa = feito ou par de feitos do dossier, hipótese = a frase do guion):

1. NLI multilingüe aberto en CPU: MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7 (MIT, ~560 MB).
   O galego non está entre as súas linguas de adestramento (si o portugués e o castelán): mide mal (ver
   probas/veracidade_calibracion.md), por iso non decide só.
2. Coincidencia léxica: proporción das palabras de contido da frase (raíz de 5 letras, sen acentos) que están
   nos feitos que a apoian.
3. Regras duras, deterministas, que non dependen do NLI:
   - DESENLACE: unha frase con léxico de resultado (vencer, gañar, triunfo, vitoria, derrota, fracaso, render...)
     só pasa se esa MESMA forma da palabra está nun feito do dossier ("derrotou" non se ancora en "foi
     derrotada") e o NLI dá implicación >= 0,7 dese feito. "A irmandade venceu" non pasa nunca: o dossier só di
     "foi derrotada".
   - QUEN FIXO QUE: para os verbos de acción (derrubar, reconstruír, vencer, regresar...), o actor que os precede
     na frase ten que ser da mesma clase (pobo / señores) que nalgún feito con ese verbo.
   - NOMES e TEMPO: unha frase con nome propio ou expresión de tempo longo (séculos, para sempre, nunca...)
     ten que estar implicada (NLI) ou coincidir (léxico) cun feito.
   - CONTRADICIÓN: só se usa no desenlace (contra os feitos que tamén falan de desenlaces). Contra o dossier
     enteiro o NLI dá contradicións altas mesmo entre feitos certos (ver calibración), así que alí sería ruído.

Modos:
- `gancho` (gancho e resumo, o que se escoita no primeiro minuto): TODAS as frases teñen que estar apoiadas
  (implicación >= E_MIN, ou coincidencia >= COB_MIN), e ademais pasar as regras duras.
- `relato` (parágrafos para durmir): só as frases sen nomes, sen persoas (ACTORES), sen tempo longo e sen desenlace
  quedan fóra da esixencia de apoio, pero son "de ambiente" e NON se aceptan no relato (eran o recheo sen sentido
  da ronda 2); o resto, como no gancho. E polo menos unha frase do parágrafo ten que contar o feito.

Que NON garante: o NLI non entende ben o galego e a coincidencia léxica é feble; unha frase falsa construída só
con palabras do dossier pode pasar. Rexeita de máis antes que de menos (un falso positivo custa unha
rexeneración ou o texto literal do dossier).
"""
import re
import unicodedata

MODELO = 'MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7'
E_MIN, COB_NLI, COB_NLI_GANCHO, COB_MIN = 0.6, 0.5, 0.6, 0.8

# léxico de desenlace (raíces sen acentos). Se a frase ten unha destas raíces, o dossier ten que tela.
DESENLACE = ['venc', 'venceu', 'gañ', 'gana', 'triunf', 'vitori', 'vitorio', 'derrot', 'fracas', 'rendi', 'rendeu',
             'liberou', 'liberad', 'conquist', 'perdeu', 'perderon', 'perdid', 'sometid', 'someteu', 'acabou co',
             'puxo fin', 'rematou co']
ACTORES = re.compile(r'\b(senor|labreg|xente|irmand|vasal|nobre|nobrez|campes|arcebisp|bisp|cleri|artes|marin|burgu|'
                     r'rebel|testem|famili|home|homes|muller|pobo|vecin|soldad|tropa|cabaleir|conde|rei|monx|coeng|'
                     r'escrib|malfeit|persoa|xentes|todos|eles|elas|quen)', re.I)
# ---- quen fixo que (ronda 3): "os señores ... derrubaron as fortalezas dos irmandiños" pasaba NLI e coincidencia
# léxica. Regra determinista: para cada verbo de acción da lista, o actor máis próximo á súa esquerda na frase ten
# que ser da mesma CLASE que nalgún feito do dossier que teña ese verbo.
CLASES = {'pobo': r'(irmand|labreg|vasal|xente|vecin|campes|artes|marin|burgu|clerig|coeng|monx|pobo|testem|famili)',
          'señores': r'(senor|nobre|nobrez|arcebisp|bisp|conde|cabaleir|rei)'}
VERBOS = ['derru', 'botar', 'botou', 'botab', 'derri', 'recon', 'levan', 'asalt', 'casti', 'regre', 'volve', 'volvi',
          'venc', 'derro', 'march', 'decid', 'manda', 'paga', 'xunta', 'forma', 'decla', 'esixi', 'obrig', 'gober']


def papeis(t):
    """[(verbo, clase do actor máis próximo á esquerda)] dunha frase."""
    ws = re.findall(r'[a-zñç]+', _sen_acentos(t))
    out = []
    for k, w in enumerate(ws):
        v = next((x for x in VERBOS if w.startswith(x)), None)
        if not v:
            continue
        for j in range(k - 1, -1, -1):
            cl = next((c for c, rx in CLASES.items() if re.match(rx, ws[j])), None)
            if cl:
                out.append((v, cl)); break
    return out


TEMPO_LONGO = r'\b(s[eé]culos?|para sempre|nunca|xamais|eternamente|milenios?|d[eé]cadas enteiras|toda a vida)\b'
STOP = set('''a o as os un unha uns unhas de do da dos das no na nos nas ao aos á ás e ou que se non máis mais pero
con sen por para polo pola polos polas en entre como cando onde xa moi tan tamén aínda despois antes desde ata
este esta estes estas ese esa eses esas aquel aquela iso isto aquilo seu súa seus súas meu miña teu túa lle lles
me te nos vos era foi eran foron ser estar había hai houbo tiña tiñan fixo facer moitos moitas moito moita todo
toda todos todas outro outra outros outras cada mesmo mesma alí aquí así ben dun dunha nun nunha coa co coas cos'''.split())


def _sen_acentos(t):
    return ''.join(c for c in unicodedata.normalize('NFD', t.lower()) if unicodedata.category(c) != 'Mn')


def _norm(t):
    return ' '.join(re.findall(r'[a-zñç]+', _sen_acentos(t)))


def raices(t):
    return {w[:5] for w in re.findall(r'[a-zñç]+', _sen_acentos(t)) if len(w) > 3 and w not in STOP}


def cobertura(frase, premisa):
    r = raices(frase)
    return round(len(r & raices(premisa)) / len(r), 2) if r else 1.0


def conta(feito, texto):
    """O texto conta o feito? Proporción das raíces DO FEITO que aparecen no texto (non ao revés: unha frase baleira
    como "as testemuñas lembraban" ten todas as súas palabras no feito, pero non o conta)."""
    return cobertura(feito, texto) >= 0.45


def desenlaces(t):
    s = _sen_acentos(t)
    return sorted({d for d in DESENLACE if re.search(r'\b' + re.escape(d), s)})


FIXOS = {'Serán', 'Galicia'}


def ten_nome(frase):
    ws = re.findall(r"[\wáéíóúüñçÁÉÍÓÚÑ]+", frase)
    return any(w[0].isupper() and w not in FIXOS for w in ws[1:])


class Verificador:
    def __init__(self, feitos, nth=4):
        import torch
        from transformers import AutoTokenizer, AutoModelForSequenceClassification
        torch.set_num_threads(nth)
        self.torch = torch
        self.tok = AutoTokenizer.from_pretrained(MODELO)
        self.mod = AutoModelForSequenceClassification.from_pretrained(MODELO).eval()
        self.feitos = list(feitos)
        self._cache = {}

    def nli(self, premisa, hipotese):
        k = (premisa, hipotese)
        if k not in self._cache:
            x = self.tok(premisa, hipotese, return_tensors='pt', truncation=True, max_length=384)
            with self.torch.no_grad():
                p = self.torch.softmax(self.mod(**x).logits[0], -1).tolist()
            self._cache[k] = {'E': round(p[0], 3), 'N': round(p[1], 3), 'C': round(p[2], 3)}
        return self._cache[k]

    def frase(self, f, modo='gancho', feito_propio=None):
        """Avalía unha frase. Devolve dict con 'ok', 'motivo' e as medidas."""
        nf = _norm(f)
        for i, p in enumerate(self.feitos):      # coincidencia literal cun feito (p. ex. a reserva literal): pasa
            if nf and nf in _norm(p):
                r = {'frase': f, 'E': 1.0, 'cobertura': 1.0, 'apoio': [i + 1], 'C_max': 0.0, 'contradi': None,
                     'ok': True, 'motivo': '', 'literal': True}
                if feito_propio is not None:
                    r['conta_o_feito'] = conta(feito_propio, f)
                return r
        sc = [(i, self.nli(p, f)) for i, p in enumerate(self.feitos)]
        # premisas: cada feito e pares cos 4 feitos máis prometedores (moitas frases xuntan dous feitos)
        top = sorted(range(len(self.feitos)), key=lambda i: -(sc[i][1]['E'] + cobertura(f, self.feitos[i])))[:4]
        prem = [(i,) for i in range(len(self.feitos))] + [(a, b) for k, a in enumerate(top) for b in top[k + 1:]]
        med = []
        for ap in prem:
            txt = ' '.join(self.feitos[i] for i in ap)
            e = sc[ap[0]][1]['E'] if len(ap) == 1 else self.nli(txt, f)['E']
            med.append({'apoio': [i + 1 for i in ap], 'E': e, 'cob': cobertura(f, txt)})
        # apoiada: implicación do NLI E coincidencia léxica mínima co mesmo feito, ou coincidencia léxica alta
        # (o NLI só non abonda: cun par de feitos como premisa di "implicación" a case todo, ver calibración)
        # no gancho (o que máis se escoita e se comparte) a coincidencia mínima co NLI é máis alta: 0,6
        cn = COB_NLI_GANCHO if modo == 'gancho' else COB_NLI
        ok_ap = [m for m in med if (m['E'] >= E_MIN and m['cob'] >= cn) or m['cob'] >= COB_MIN]
        mellor = max(ok_ap or med, key=lambda m: (m['E'] >= E_MIN and m['cob'] >= cn, m['cob'] >= COB_MIN, m['E'] + m['cob']))
        apoiada = bool(ok_ap)
        cmax, ic = max(((s['C'], i) for i, s in sc), key=lambda x: x[0])
        r = {'frase': f, 'E': mellor['E'], 'cobertura': mellor['cob'], 'apoio': mellor['apoio'], 'C_max': cmax,
             'contradi': ic + 1}
        motivos = []
        ds = desenlaces(f)
        tempo = re.search(TEMPO_LONGO, _sen_acentos(f).replace('seculo', 'século'))
        # relato: unha frase que fala de persoas (actores) afirma algo delas e ten que estar apoiada; só as frases
        # sen nomes, sen actores, sen tempo longo e sen desenlace (chuvia, pedra, camiños) poden ser de ambiente
        actor = bool(ACTORES.search(_sen_acentos(f)))
        esixida = modo == 'gancho' or ten_nome(f) or tempo or ds or actor
        if ds:
            dossier_ds = set(desenlaces(' '.join(self.feitos)))
            falta = [d for d in ds if d not in dossier_ds]
            # forma exacta: "derrotou" (activa) non se ancora en "foi derrotada" (pasiva); o NLI non ve a diferenza
            palabras_d = set(re.findall(r'[a-zñç]+', _sen_acentos(' '.join(self.feitos))))
            formas = [w for w in re.findall(r'[a-zñç]+', _sen_acentos(f))
                      if any(w.startswith(d) for d in DESENLACE if ' ' not in d)]
            falta = sorted(set(falta + [w for w in formas if w not in palabras_d]))
            if falta:
                motivos.append(f'desenlace que non está no dossier ({", ".join(falta)})')
            else:
                # quen gañou e quen perdeu: implicación (>= 0,7; o feito contra si mesmo dá 0,74) e contradición baixa (< 0,5) cun mesmo feito
                # que teña ese desenlace ("a irmandade derrotou os señores" non pasa: o feito di "foi derrotada")
                cands = [i for i, p in enumerate(self.feitos) if set(ds) & set(desenlaces(p))]
                if not any(sc[i][1]['E'] >= 0.7 and sc[i][1]['C'] < 0.5 for i in cands):
                    motivos.append('desenlace distinto do que di o dossier')
        if not r.get('literal'):
            dossier_pap = {x for p in self.feitos for x in papeis(p)}
            verbos_d = {v for v, _ in dossier_pap}
            mal = [f'{c} + {v}' for v, c in papeis(f) if v in verbos_d and (v, c) not in dossier_pap]
            if mal:
                motivos.append('quen fixo que non coincide co dossier (' + ', '.join(mal) + ')')
        if esixida and not apoiada:
            motivos.append('afirmación sen apoio no dossier' if modo == 'gancho' else
                           'fala de persoas, nomes, tempo longo ou desenlace sen apoio no dossier')
        r['ok'] = not motivos
        r['ambiente'] = not esixida and not apoiada
        r['motivo'] = '; '.join(motivos)
        if feito_propio is not None:
            r['conta_o_feito'] = conta(feito_propio, f)
        return r

    def texto(self, t, modo='gancho', feito_propio=None):
        fr = [s for s in re.split(r'(?<=[.!?…])\s+', ' '.join(t.split())) if s.strip()]
        rs = [self.frase(f, modo, feito_propio) for f in fr]
        prob = [f"Esta frase non se pode afirmar co dossier ({r['motivo']}): {r['frase']}" for r in rs if not r['ok']]
        # ronda 3: ningunha frase de ambiente no relato. Eran a orixe do recheo sen sentido ("o lume ardeu en
        # silencio", "a chuvia mollar a pedra"); o ambiente pono as imaxes e a choiva do son
        amb = [r['frase'] for r in rs if r.get('ambiente')]
        if modo == 'relato' and amb:
            prob.append('Quita estas frases de recheo, que non contan nada do feito: ' + ' '.join(amb))
        if feito_propio is not None and rs and not any(r.get('conta_o_feito') for r in rs):
            prob.append('O parágrafo non conta o feito que se pediu: cóntao con palabras parecidas ás do feito.')
        return prob, rs
