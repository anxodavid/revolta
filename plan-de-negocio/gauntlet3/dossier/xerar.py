#!/usr/bin/env python
"""Dossier "As meigas de verdade": comproba as citas de feitos.yaml e xera a ficha de longo.py e a táboa de traballo.

    python xerar.py comprobar --fontes DIR            # cada cita ten que estar LITERALMENTE no texto da súa fonte
    python xerar.py ficha --fontes DIR --saida herramientas/pipeline/temas/meigas-de-verdade.yaml
    python xerar.py taboa --saida taboa.md            # táboa de feitos para dossier.md

DIR é o cartafol cos textos descargados das fontes (fontes/*.txt, rag/*.txt), no scratchpad: non se suben ao repo
porque son textos con dereitos de autor (artigos de prensa). Mesma regra de normalización ca dossier.py do
pipeline: maiúsculas, espazos e comiñas non contan. `ausente` comproba que un texto NON está na fonte.
Automático: a comprobación. Feito a man por Claude: a escolla dos feitos, a súa redacción en galego e as citas.
"""
import argparse, re, sys, unicodedata
from pathlib import Path
import yaml

AQUI = Path(__file__).resolve().parent


def norm(t):
    t = unicodedata.normalize('NFC', t).lower()
    t = re.sub(r'[«»“”"\'’‘]', '', t)
    return re.sub(r'\s+', ' ', t).strip()


def ler():
    return yaml.safe_load((AQUI / 'feitos.yaml').read_text())


def texto_fonte(d, fontes_dir, tag):
    base, _, palabra = tag.partition(':')
    f = d['fontes'][base]['texto']
    if palabra:
        f = f.replace('{palabra}', palabra)
    p = (Path(fontes_dir) / f).resolve()
    return norm(p.read_text(errors='ignore')) if p.exists() else None


def comprobar(d, fontes_dir):
    cache, mal, n_ev = {}, [], 0
    for f in d['feitos']:
        for ev in f['evidencias']:
            n_ev += 1
            tag = ev['fonte']
            if tag not in cache:
                cache[tag] = texto_fonte(d, fontes_dir, tag)
            t = cache[tag]
            if t is None:
                mal.append((f['id'], tag, 'sen texto local da fonte'))
            elif 'cita' in ev and norm(ev['cita']) not in t:
                mal.append((f['id'], tag, 'cita non atopada: ' + ev['cita'][:90]))
            elif 'ausente' in ev and norm(ev['ausente']) in t:
                mal.append((f['id'], tag, 'o texto que debía estar ausente aparece: ' + ev['ausente']))
    return n_ev, mal


def etiquetas(f):
    vistas = []
    for ev in f['evidencias']:
        b = ev['fonte'].split(':')[0]
        if b not in vistas:
            vistas.append(b)
    return vistas


CABECEIRA = '''\
# Ficha de tema para longo.py (Gauntlet 3): "As meigas de verdade".
# Xerada por plan-de-negocio/gauntlet3/dossier/xerar.py a partir de feitos.yaml (cada feito ten a súa cita literal
# comprobada por código na fonte; táboa, conflitos e "Non dicir" en plan-de-negocio/gauntlet3/dossier/dossier.md).
# O dossier escribiuno Claude (axente constructor da peza DOSSIER); ningunha persoa o revisou.
#
# Notas para o guionista (non van no texto do dossier):
# - As liñas "- [== ... ==]" son separadores de capítulo do arco (contexto.md §8): feitos() do pipeline sáltaas
#   porque, sen a etiqueta, quedan baleiras.
# - Os anos e cifras van en letra (porta H1). Non hai ano para a única fogueira da Inquisición: as fontes non
#   concordan (1579 / 1627). Por iso ningún dos dous anos está no dossier e o guion non pode dicilos.
# - Nunca dicir que Galicia "se librou" ou "quedou á marxe" da caza de bruxas: a Inquisición foi branda; a xustiza
#   ordinaria, máis dura (F040-F043).
# - O conxuro da queimada está rexistrado (2001; o autor morreu en 2022): como moito o primeiro verso, co autor.
#   O poema "María Soliña" de Celso Emilio Ferreiro (morto en 1979) está protexido: nomealo, non recitalo.
# - Lenda e costume contados como tales ("críase", "contan", "segundo a tradición"); remedios nunca como consello.
# - Na zona de durmir (desde o minuto dez) nada de intrusións nocturnas, demos, caveiras nin o asalto de Cangas.
# - Títulos alternativos (contexto.md §8.2, proba A/B): "1617: a meiga que dicía poder pasarlle ao home as dores do
#   parto | Cousas de Galiza para durmir" (proposta do crítico; máis fiel ao único testemuño sería "…que dixo que
#   podía…") e "Lendas e verdades das meigas galegas | Cousas de Galiza para durmir".
id: meigas-de-verdade
titulo: "As meigas de verdade"
titulo_youtube: "As meigas de verdade (e por que o conxuro da queimada é de 1967) | Cousas de Galiza para durmir"
titulo_rotulo: "As meigas de verdade"
tema: "As meigas de verdade: o que contan os procesos por bruxería da Real Audiencia de Galicia e as cifras da Inquisición de Santiago, e despois as crenzas e os costumes, contados como lenda, desde o conxuro da queimada de mil novecentos sesenta e sete ata a noite de san Xoán e o frade Feijoo"
palabras: 3500
duracion_s: [1500, 2100]
aviso: "Boas noites. A voz que vas escoitar é sintética, e este texto preparouno un proceso automático."
capitulo_inicial: "Un conxuro de 1967"
autoria:
  guion: "Claude (Anthropic), con axentes no Gauntlet 3: un axente constructor escribe e críticos independentes revisan. Non é unha execución desatendida nin un LLM por API. Ningunha persoa o revisou."
  dossier: "Claude (Anthropic), axente constructor do dossier: escolleu as fontes, redactou os feitos en galego e comprobou por código que cada cita está literalmente na súa fonte. Ningunha persoa o revisou."
  escenas: "Claude (Anthropic), un axente escribe un prompt por plano."
  automatico: "voz (Nós StyleTTS2), imaxes e a súa porta de revisión, son, montaxe e controis automáticos"
descricion: |
  Quen eran de verdade as meigas galegas? Neste episodio para durmir abrimos os procesos por bruxería que garda o Arquivo do Reino de Galicia: unha parteira de Vilalba, un gato que ninguén deu collido en Xinzo de Limia, unhas veciñas que foron á fonte a noite de san Xoán en Campo Lameiro. Tamén as cifras da Inquisición de Santiago, que coas meigas foi máis branda ca a xustiza ordinaria. Despois, amodo, as herbas, o mal de ollo, a noite de san Xoán e o frade Feijoo, que dubidaba das historias de bruxas. E unha sorpresa ao comezo: o conxuro da queimada escribiuse en Vigo en 1967.
  Eu non creo nas meigas, mais habelas, hainas: as lendas cóntanse como lendas, e os datos levan fonte.
  As imaxes están xeradas con intelixencia artificial e representan lugares reais: son contido sintético.
creditos:
  - "Voz sintética: modelo Nos_StyleTTS2-Brais-GL do Proxecto Nós (Universidade de Santiago de Compostela), licenza Apache-2.0."
  - "Texto e dossier de fontes preparados con intelixencia artificial (Claude, de Anthropic) a partir das fontes citadas. Ningunha persoa os revisou."
  - "Imaxes xeradas con intelixencia artificial e revisadas por unha porta automática: contido sintético, non son fotografías. Choiva sintetizada por código."
  - "Conxuro da queimada: primeiro verso, de Mariano Marcos Abalo (1967), obra rexistrada."
'''


def ficha(d, saida):
    L = [CABECEIRA, '# Dossier: un feito por liña, en galego, coa etiqueta das fontes entre corchetes (as etiquetas non se len).',
         '# Todo nome propio e toda cantidade que diga o guion ten que estar aquí (porta H1).', 'dossier: |']
    cap_act = None
    for f in d['feitos']:
        if f.get('ficha') is False:
            continue
        if f['cap'] != cap_act:
            cap_act = f['cap']
            L.append(f"  - [== {cap_act}. {d['capitulos'][cap_act]} ==]")
        L.append(f"  - [{', '.join(etiquetas(f))}] {f['feito']}")
    L.append('fontes:')
    usadas = []
    for f in d['feitos']:
        if f.get('ficha') is False:
            continue
        for t in etiquetas(f):
            if t not in usadas:
                usadas.append(t)
    for t in d['fontes']:
        if t in usadas:
            L.append(f"  {t}: {d['fontes'][t]['url']}")
    Path(saida).write_text('\n'.join(L) + '\n')
    n = sum(1 for f in d['feitos'] if f.get('ficha') is not False)
    print(f'ficha: {n} feitos, {len(usadas)} fontes -> {saida}')


def taboa(d, saida):
    L = []
    cap_act = None
    for f in d['feitos']:
        if f['cap'] != cap_act:
            cap_act = f['cap']
            L += ['', f"### {cap_act}. {d['capitulos'][cap_act]}", '',
                  '| id | tipo | feito (galego) | evidencia: cita literal da fonte | nota |', '|---|---|---|---|---|']
        ev = []
        for e in f['evidencias']:
            base, _, pal = e['fonte'].partition(':')
            url = d['fontes'][base]['url'] + (f'/-/termo/busca/{pal}' if pal else '')
            if 'cita' in e:
                ev.append(f"[{e['fonte']}]({url}): «{e['cita']}»")
            else:
                ev.append(f"[{e['fonte']}]({url}): NON aparece «{e['ausente']}»")
        fora = ' (fóra da ficha)' if f.get('ficha') is False else ''
        L.append(f"| {f['id']}{fora} | {f['tipo']} | {f['feito']} | {'<br>'.join(ev)} | {f.get('nota', '')} |")
    Path(saida).write_text('\n'.join(L).strip() + '\n')
    print(f'táboa: {len(d["feitos"])} feitos -> {saida}')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modo', choices=['comprobar', 'ficha', 'taboa'])
    ap.add_argument('--fontes', default='.')
    ap.add_argument('--saida')
    a = ap.parse_args()
    d = ler()
    if a.modo == 'comprobar':
        n_ev, mal = comprobar(d, a.fontes)
        print(f'{len(d["feitos"])} feitos, {n_ev} evidencias, {len(mal)} con problemas')
        for m in mal:
            print(' -', *m)
        sys.exit(1 if mal else 0)
    if a.modo == 'ficha':
        n_ev, mal = comprobar(d, a.fontes)
        if mal:
            sys.exit(f'{len(mal)} citas sen comprobar: primeiro `comprobar`')
        ficha(d, a.saida)
    if a.modo == 'taboa':
        taboa(d, a.saida)


if __name__ == '__main__':
    main()
