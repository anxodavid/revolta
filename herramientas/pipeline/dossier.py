#!/usr/bin/env python
"""Dossier semiautomático (etapa [1] do plan, §3.3): fontes -> feitos con cita literal comprobada por código.

    python dossier.py fontes TEMA.yaml --saida DIR       # descarga e limpa o texto de cada fonte -> DIR/fontes/*.txt
    python dossier.py comprobar TEMA.yaml FEITOS.yaml --saida DIR   # comproba as citas -> DIR/dossier.yaml, informe.md

TEMA.yaml:   id, titulo, fontes: {ID: URL}   (URL de Galipedia/Wikipedia ou páxina HTML/PDF de texto)
FEITOS.yaml: lista de {fontes: [ID...], feito: "texto en galego", cita: "texto LITERAL da fonte"}
             (escríbeo un LLM co texto das fontes en contexto; prompt en prompts/dossier.md)

Regra: un feito entra no dossier só se a súa cita aparece literalmente (normalizando espazos, maiúsculas e
comiñas) nalgunha das fontes que declara. Os que fallan sepáranse en rexeitados; o dossier non os leva.
Que NON comproba: que o feito diga o mesmo ca cita (iso é H2, xuíz LLM) nin que a fonte teña razón.
"""
import argparse, html, json, re, sys, time, unicodedata, urllib.error, urllib.parse, urllib.request
from pathlib import Path
import yaml

UA = {'User-Agent': 'seran-dossier/0.1 (https://github.com/; proxecto afeccionado)'}


def abrir(url, intentos=5):
    for i in range(intentos):      # Wikimedia responde 429 a ráfagas: agardar e repetir
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30).read()
        except urllib.error.HTTPError as e:
            if e.code != 429 or i == intentos - 1:
                raise
            time.sleep(2 * (i + 1))


def baixar(url):
    u = urllib.parse.urlparse(url)
    if u.netloc.endswith('wikipedia.org') and u.path.startswith('/wiki/'):
        tit = urllib.parse.unquote(u.path[len('/wiki/'):])
        api = (f'https://{u.netloc}/w/api.php?action=parse&format=json&prop=text&disableeditsection=1&redirects=1&page='
               + urllib.parse.quote(tit))
        raw = json.loads(abrir(api))
        h = raw['parse']['text']['*']
    else:
        h = abrir(url).decode('utf-8', 'ignore')
    h = re.sub(r'(?is)<(script|style|sup|table)[^>]*>.*?</\1>', ' ', h)   # sen notas, táboas nin scripts
    t = html.unescape(re.sub(r'(?s)<[^>]+>', ' ', h))
    return re.sub(r'[ \t]+', ' ', re.sub(r'\s*\n\s*', '\n', t)).strip()


def norm(t):
    t = unicodedata.normalize('NFC', t).lower()
    t = re.sub(r'[«»“”"\'’‘]', '', t)
    return re.sub(r'\s+', ' ', t).strip()


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('modo', choices=['fontes', 'comprobar'])
    ap.add_argument('tema'); ap.add_argument('feitos', nargs='?'); ap.add_argument('--saida', required=True)
    a = ap.parse_args()
    tema = yaml.safe_load(open(a.tema)); S = Path(a.saida); F = S / 'fontes'; F.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    if a.modo == 'fontes':
        rex = {}
        for k, url in tema['fontes'].items():
            txt = baixar(url); (F / f'{k}.txt').write_text(txt)
            rex[k] = {'url': url, 'palabras': len(txt.split())}
            print(f'{k:10s} {rex[k]["palabras"]:6d} palabras  {url}')
        rex['_segundos'] = round(time.time() - t0, 1)
        (S / 'fontes.json').write_text(json.dumps(rex, ensure_ascii=False, indent=1))
        return
    fontes = {k: norm((F / f'{k}.txt').read_text()) for k in tema['fontes']}
    feitos = yaml.safe_load(open(a.feitos))
    ok, mal = [], []
    for f in feitos:
        c = norm(f['cita'])
        onde = [k for k in f['fontes'] if k in fontes and c in fontes[k]]
        (ok if onde else mal).append({**f, 'atopada_en': onde})
    dossier = '\n'.join(f"- [{', '.join(f['atopada_en'])}] {f['feito']}" for f in ok)
    (S / 'dossier.yaml').write_text(yaml.safe_dump({'id': tema['id'], 'titulo': tema['titulo'], 'dossier': dossier + '\n',
                                                     'fontes': tema['fontes']}, allow_unicode=True, sort_keys=False, width=120))
    pal_feitos = sum(len(f['feito'].split()) for f in ok)
    L = [f"# Dossier {tema['id']}: {len(ok)}/{len(feitos)} feitos coa cita atopada ({100*len(ok)/max(1,len(feitos)):.0f} %)", '',
         f"Palabras do dossier: {pal_feitos}. Comprobación: {time.time()-t0:.2f} s.", '',
         '## Rexeitados (a cita non está literalmente na fonte declarada)', '']
    L += [f"- [{', '.join(f['fontes'])}] {f['feito']} | cita: \"{f['cita']}\"" for f in mal] or ['- ningún']
    (S / 'informe.md').write_text('\n'.join(L) + '\n')
    print('\n'.join(L[:3]))


if __name__ == '__main__':
    main()
