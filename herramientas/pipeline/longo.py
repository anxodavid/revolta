#!/usr/bin/env python
"""Vídeo longo (Gauntlet 3): guion e lista de planos escritos fóra do pipeline, curva de embude e capítulos.

    python longo.py temas/TEMA.yaml --guion GUION.txt --traballo DIR --saida DIR [--escenas ESCENAS.json]

Reutiliza as etapas do pipeline curto (pipeline.py): voz StyleTTS2 de Nós, imaxes con porta de revisión, choiva,
montaxe e QA. Cambia o que é propio dun episodio longo:

- O guion NON o escribe o LLM do pipeline: é un ficheiro de texto (no Gauntlet 3, escrito por Claude con axentes;
  a ficha do tema declara a autoría en `autoria` e o QA repíteo). Parágrafos separados por liñas baleiras; un
  parágrafo que empeza por "## " é un título de capítulo (non se narra: vai nun rótulo e nos capítulos de YouTube).
- Curva de embude (curva.py): voz, pausas, duración dos planos, fundidos, nivel da voz e luz van do gancho vivo
  ao ton de durmir segundo a posición no guion.
- A lista de planos tamén vén de fóra: se falta --escenas, o pipeline escribe <traballo>/planos.json (o texto que
  se escoita en cada plano, a súa duración, capítulo e fase) e sae co código 3; un axente escribe un prompt por
  plano nun JSON [{"n": 1, "prompt": "..."}, ...] e vólvese lanzar o mesmo comando.
- Son (decisións D13 e D14 do promotor): nada de ambiente continuo. Cada plano pode levar `son` na lista de planos:
  un tipo do catálogo de son.py (choiva, lume, mar, vento, fonte, xente, noite, aldea, campas), dous unidos con '+'
  ('lume+noite') ou 'limpa' (voz limpa); se falta, dedúcese das palabras do prompt (SON_PALABRAS). Regra e niveis en
  plan-de-negocio/gauntlet3/son/guia-son.md. `ambiente` na ficha do tema: 'escena' (por defecto), 'choiva2' (choiva
  continua, para comparar) ou 'ningun'.
- Portas de texto: lingua (LanguageTool + hunspell), H1 (nomes e cantidades no dossier) e estilo son bloqueantes;
  a veracidade (veracidade.py) márcase por frase e cada frase marcada ten que ter unha xustificación escrita no
  ficheiro de excepcións (`--excepcions`, YAML [{frase, xustificacion}]); se queda algunha sen xustificar, non hai vídeo.

Cada etapa garda o seu resultado en --traballo e non se repite se xa está feita.
"""
import argparse, hashlib, inspect, json, math, os, re, shutil, subprocess, sys, time
from pathlib import Path
import numpy as np, soundfile as sf, yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import pipeline as P
import curva

FORMULA = 'Isto é Cousas de Galiza para durmir.'
RECLAMO = 'Cousas de Galiza para durmir'
OFFSET, COLA = 1.5, 25.0          # choiva antes da primeira frase e despois da última (o final esvaece amodo)
UMBRAIS = {'wer_max': 0.06, 'desfase_av_max_s': 0.1, 'pct_sincronia_min': 95.0, 'lufs': (-18, -16),
           'kbps_max': 1600}
ROMANOS = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']


def hms(t):
    t = int(round(t)); h, r = divmod(t, 3600); m, s = divmod(r, 60)
    return f'{h}:{m:02d}:{s:02d}' if h else f'{m}:{s:02d}'


# ------------------------------------------------------------------ 1 texto
def ler_guion(path):
    """(texto narrado, capítulos). Capítulo = {'titulo', 'num', 'par0': índice do primeiro parágrafo narrado}."""
    pars, caps = [], []
    for b in re.split(r'\n\s*\n', Path(path).read_text().strip()):
        b = ' '.join(b.split())
        if not b:
            continue
        if b.startswith('## '):
            caps.append({'titulo': b[3:].strip(), 'num': ROMANOS[len(caps)] if len(caps) < len(ROMANOS) else str(len(caps) + 1),
                         'par0': len(pars)})
        elif not b.startswith('%%'):          # %% = nota para o equipo, non se narra
            pars.append(P.normalizar(b))
    return '\n\n'.join(pars), caps


def porta_texto(texto, frases, tema, excepcions):
    """Portas de texto do vídeo longo. Bloqueantes: lingua, H1, estilo e veracidade sen xustificar."""
    import qa, ancoraxe
    anc = P.ancora(tema)
    res = {'lingua': qa.lingua(texto, dossier=anc),
           'h1_ancoraxe': ancoraxe.ancoraxe(texto, anc, [tema['aviso'], FORMULA]),
           'estilo': qa.estilo(texto, frases, tema['aviso'], tema['palabras'], formula=FORMULA)}
    v = P.verificador(tema)
    xust = {' '.join(x['frase'].split()): x.get('xustificacion', '') for x in (excepcions or [])}
    marcadas = []
    for f in frases:
        if f['texto'] in tema['aviso'] or f['texto'] == FORMULA:
            continue
        gancho = f['pal0'] < curva.GANCHO
        r = v.frase(f['texto'], 'gancho' if gancho else 'relato', actores=gancho)
        if not r['ok']:
            marcadas.append({'i': f['i'], 'frase': f['texto'], 'modo': 'gancho' if gancho else 'relato',
                             'motivo': r['motivo'], 'E': r['E'], 'cobertura': r['cobertura'], 'apoio': r['apoio'],
                             'xustificacion': xust.get(' '.join(f['texto'].split()))})
    res['veracidade'] = {'frases_avaliadas': len(frases), 'marcadas': marcadas,
                         'sen_xustificar': [m for m in marcadas if not m['xustificacion']]}
    e = res['estilo']
    res['portas_texto'] = {
        'lingua_lt': not res['lingua'],
        'h1_ancoraxe': not res['h1_ancoraxe']['non_ancorados'],
        'veracidade': not res['veracidade']['sen_xustificar'],
        'estilo': not (e['cifras'] or e['signos_prohibidos'] or e['palabras_vetadas'] or e['preguntas'])
                  and e['aviso_literal'] and e['formula_literal'],
    }
    return res


# ------------------------------------------------------------------ 3 planos
def planos(frases, tempos, dur, inicio_cap, tot):
    """Planos cortados polas duracións reais da voz, coa duración obxectivo da curva (curtos no gancho, longos ao
    durmir). Un capítulo novo abre sempre un plano novo, que empeza co rótulo."""
    out, cur = [], None
    for f in frases:
        t0, t1 = tempos[f['i']]
        c = curva.en(f['pal0'], tot)
        obx, pmax = c['plano_s'], 1.35 * c['plano_s']
        if f['i'] in inicio_cap:
            if cur: out.append(cur); cur = None
            cur = {'frases': [f['i']], 't0': inicio_cap[f['i']], 'texto': f['texto'], 'pal0': f['pal0']}
        elif cur and t1 - cur['t0'] > 1.3 * obx:
            out.append(cur); cur = None
        if cur is None and (t1 - t0) > 1.25 * obx:
            k = max(2, round((t1 - t0) / obx))
            for j in range(k):
                out.append({'frases': [f['i']], 't0': t0 + j * (t1 - t0) / k, 'texto': f['texto'], 'pal0': f['pal0'],
                            'parte': f'{j + 1}/{k}'})
            continue
        if cur is None:
            cur = {'frases': [f['i']], 't0': t0, 'texto': f['texto'], 'pal0': f['pal0']}
        elif f['i'] not in cur['frases']:
            cur['frases'].append(f['i']); cur['texto'] += ' ' + f['texto']
        if t1 - cur['t0'] >= obx * 0.85:
            out.append(cur); cur = None
    if cur:
        out.append(cur)
    for k, p in enumerate(out):
        lead = 0.0 if (k == 0 or p['frases'][0] in inicio_cap or 'parte' in p and not p['parte'].startswith('1/')) else 0.25
        p['b0'] = 0.0 if k == 0 else max(0.0, p['t0'] - lead)
    for k, p in enumerate(out):
        p['b1'] = out[k + 1]['b0'] if k + 1 < len(out) else dur
    # tope: ningún plano pasa de 1,35 veces a súa duración obxectivo (pártese en planos con imaxes distintas)
    fin = []
    for p in out:
        c = curva.en(p['pal0'], tot)
        d = p['b1'] - p['b0']; k = math.ceil(d / (1.35 * c['plano_s']) - 1e-9)
        if k <= 1:
            fin.append(p); continue
        for j in range(k):
            fin.append(dict(p, b0=p['b0'] + j * d / k, b1=p['b0'] + (j + 1) * d / k, parte=f'{j + 1}/{k}'))
    movs = ['zoom_in', 'pan_right', 'zoom_out', 'pan_left', 'zoom_in', 'pan_up']
    for k, p in enumerate(fin):
        c = curva.en(p['pal0'], tot)
        p.update(n=k + 1, movemento=movs[k % len(movs)], xf=round(c['fundido_s'], 2), fase=c['fase'], u=c['u'])
    return fin


# Son dun plano a partir das palabras (en inglés) do seu prompt, se a lista de planos non trae `son`. A orde é a
# prioridade: gaña o primeiro tipo que apareza. Os tipos de exterior (aldea, vento) non se poñen nun interior; a
# noite engádese como segunda capa a lume, fonte ou mar se o plano é de noite e de exterior.
SON_PALABRAS = [
    ('lume', r'\b(fire|firelight|fireplace|hearth|embers|flames?|bonfires?|campfire|burning logs?|queimada)\b'),
    ('choiva', r'\b(rain|raining|rainy|rainfall|drizzle|downpour|raindrops)\b'),
    ('mar', r'\b(sea|seas|waves?|shore|surf|seashore|ocean|breakers|coast|coastal|beach|harbou?r|estuary)\b'),
    ('fonte', r'\b(fountains?|streams?|brook|creek|rivulet|river|running water|spring water|water springs?|watermill|'
              r'mill race|washing place|waterfall)\b'),
    ('xente', r'\b(crowds?|crowded|market|marketplace|village fair|cattle fair|country fair|fairground|gathering|gathered|'
              r'people talking|procession|festival|feast|tavern|throng|dancers|dancing)\b'),
    ('campas', r'\b(church|churches|bells?|belfry|bell tower|cathedral|monaster(y|ies)|cloisters?|abbey|chapel|convent)\b'),
    ('noite', r'\b(night|nighttime|nightfall|moon|moonlight|moonlit|stars|starry|starlit|midnight)\b'),
    ('aldea', r'\b(village|hamlet|cows?|cattle|oxen|meadows?|pastures?|farm|farmyard|fields?|granary|orchard|'
              r'countryside|sheep|goats?|hens|chickens)\b'),
    ('vento', r'\b(wind|windy|storm|stormy|gale|gusts?|breeze|forest|woods|woodland|oak trees|chestnut trees|hillside|'
              r'moor|mountains?)\b'),
]
INTERIOR = r'\b(interior|inside|indoors?|kitchen|room|table|bed|close-up|portrait|hands|document|manuscript|book|desk)\b'
LIMPA = ('limpa', 'ningun', 'ningún', 'nada', 'non', '-')


def son_do_prompt(prompt):
    """Son dun plano a partir do seu prompt (se a lista de planos non trae `son`): o primeiro tipo de SON_PALABRAS
    que apareza (en interiores, sen aldea nin vento), con 'noite' de segunda capa se é lume, fonte ou mar de noite
    en exterior. Se non hai ningún, None (voz limpa)."""
    interior = bool(re.search(INTERIOR, prompt, re.I))
    atopados = [t for t, rx in SON_PALABRAS if re.search(rx, prompt, re.I) and not (interior and t in ('aldea', 'vento'))]
    if not atopados:
        return None
    tipo = atopados[0]
    if tipo in ('lume', 'fonte', 'mar') and 'noite' in atopados and not interior:
        tipo += '+noite'
    return tipo


def son_do_plano(p):
    """Son dun plano: o campo `son` da lista de planos ou, se falta, o do seu prompt. Só capas do catálogo de son.py
    (como moito dúas). Devolve 'tipo' ou 'tipo+tipo'; 'limpa' se a lista pide voz limpa (corta sempre o ambiente); ou
    None se o plano é neutro (sen fonte de son: voz limpa, agás un inserto curto entre dous planos co mesmo son)."""
    import son
    s_ = p.get('son')
    if s_ is not None and str(s_).strip().lower() in LIMPA:
        return 'limpa'
    if s_ is None or not str(s_).strip():
        s_ = son_do_prompt(p.get('prompt', ''))
    if not s_:
        return None
    return '+'.join([c for c in son.capas(str(s_).lower()) if c in son.AMBIENTES][:2]) or None


def ler_escenas(path, pl):
    d = json.loads(Path(path).read_text())
    d = d.get('escenas', d) if isinstance(d, dict) else d
    por_n = {int(x['n']): x for x in d}
    faltan = [p['n'] for p in pl if p['n'] not in por_n or len(str(por_n[p['n']].get('prompt', '')).split()) < 6]
    if faltan:
        raise SystemExit(f'A lista de planos {path} non ten prompt para os planos {faltan[:20]}... ({len(faltan)})')
    for p in pl:
        x = por_n[p['n']]
        p['prompt'] = re.sub(r'[*_#`]+', '', str(x['prompt'])).strip().strip('"')
        for k in ('movemento', 'luz', 'tipo', 'negativo', 'son', 'clave'):
            if x.get(k):
                p[k] = x[k]
    return pl


# ------------------------------------------------------------------ descrición de YouTube
def descricion(tema, caps_t, dur):
    L = [tema.get('titulo_youtube', tema['titulo']), '']
    if tema.get('descricion'):
        L += [tema['descricion'].strip(), '']
    L += ['Capítulos', f"0:00 {tema.get('capitulo_inicial', 'Comezo')}"]
    L += [f"{hms(c['t0'])} {c['num']}. {c['titulo']}" for c in caps_t]
    L += ['', 'Fontes']
    L += [f'- {v}' for v in (tema.get('fontes') or {}).values()]
    L += ['', 'Como está feito']
    L += [f'- {x}' for x in tema.get('creditos', [])]
    L += ['', f'Duración: {hms(dur)}.']
    return '\n'.join(L) + '\n'


# ------------------------------------------------------------------ principal
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('tema'); ap.add_argument('--guion', required=True); ap.add_argument('--saida', required=True)
    ap.add_argument('--traballo', required=True); ap.add_argument('--escenas', default=None)
    ap.add_argument('--excepcions', default=None, help='YAML [{frase, xustificacion}] para as frases que marca a veracidade')
    ap.add_argument('--so-texto', action='store_true', help='só as portas de texto (para o Gauntlet do guion)')
    a = ap.parse_args()
    t_inicio = time.time()
    tema = yaml.safe_load(open(a.tema))
    W = Path(a.traballo); W.mkdir(parents=True, exist_ok=True)
    S = Path(a.saida); S.mkdir(parents=True, exist_ok=True)
    tp = W / 'tempos.json'
    if tp.exists():
        P.TEMPOS.update(json.loads(tp.read_text()))
    save_t = lambda: tp.write_text(json.dumps(P.TEMPOS, indent=1))
    import qa

    # 1 texto
    with P.Etapa('1_texto'):
        texto, caps = ler_guion(a.guion)
        frases = P.partir(texto)
        pal = 0
        for f in frases:
            f['pal0'] = pal; pal += len(f['texto'].split())
        tot = pal
        exc = yaml.safe_load(open(a.excepcions)) if a.excepcions and Path(a.excepcions).exists() else []
        pt = porta_texto(texto, frases, tema, exc)
        pt['palabras'] = tot; pt['capitulos'] = caps
        (W / 'guion.txt').write_text(texto + '\n')
        (W / 'porta_texto.json').write_text(json.dumps(pt, ensure_ascii=False, indent=1))
    save_t()
    print('portas de texto:', pt['portas_texto'], '| palabras:', tot, '| frases marcadas pola veracidade:',
          len(pt['veracidade']['marcadas']), '| sen xustificar:', len(pt['veracidade']['sen_xustificar']), flush=True)
    if a.so_texto:
        return
    if not all(pt['portas_texto'].values()):
        print('NON PUBLICABLE (texto): ver', W / 'porta_texto.json'); sys.exit(4)
    P.VER.clear(); qa.pechar_lt()
    # produción do 30-09-2026: o servidor Java de LanguageTool seguía vivo (0,55 GB) e, co NLI sen liberar, a etapa de
    # imaxes (12,3 GB) pasou do límite de memoria do cgroup e o OOM matouna. Péchase á forza.
    subprocess.run(['pkill', '-f', 'languagetool-server.jar'], check=False)
    import gc; gc.collect()

    # 2 voz, coa curva do embude
    inicio_par = {}
    for f in frases:
        inicio_par.setdefault(f['par'], f['i'])
    cap_frase = {inicio_par[c['par0']]: c for c in caps if c['par0'] in inicio_par}
    with P.Etapa('3_voz'):
        for f in frases:
            c = curva.en(f['pal0'], tot)
            f['escala'] = round(c['escala'], 3)
            for k in curva.VOZ:
                f[k] = round(c[k], 3)
            f['ganancia_db'] = round(c['ganancia_db'], 2)
            clave = json.dumps([f['texto'], f['escala']] + [f[k] for k in curva.VOZ])
            f['wav'] = f"{f['i']:04d}-{hashlib.sha256(clave.encode()).hexdigest()[:8]}.wav"
        fj = W / 'frases.json'; fj.write_text(json.dumps(frases, ensure_ascii=False, indent=1))
        env = dict(os.environ, PATH=f"{P.CFG['st2_path']}:{os.environ['PATH']}", PYTHONPATH=P.CFG['st2_stubs'],
                   ST2_DIR=P.CFG['st2_dir'], REF_WAV=P.CFG['ref_wav'], SCALE=str(curva.CURVA['escala'][-1]))
        if tema.get('ref_wav_calma') or os.environ.get('REF_WAV_CALMO'):
            env['REF_WAV_CALMO'] = os.environ.get('REF_WAV_CALMO') or tema['ref_wav_calma']
        vdir = W / 'voz'
        subprocess.run([P.CFG['python_tts'], str(HERE / 'voz_st2.py'), str(fj), str(vdir)], env=env, check=True)
        sr = 24000; parts = []; tempos = {}; t = OFFSET; inicio_cap = {}; rot = []
        for k, f in enumerate(frases):
            w, _ = sf.read(vdir / f['wav'])
            w = w * 10 ** (f['ganancia_db'] / 20)
            tempos[f['i']] = (round(t, 3), round(t + len(w) / sr, 3))
            parts.append(w); t += len(w) / sr
            if k + 1 < len(frases):
                c = curva.en(f['pal0'], tot); seg = frases[k + 1]
                nw = len(seg['texto'].split())
                g_ = c['pausa_frase'] + min(0.3, max(-0.15, 0.02 * (nw - 14)))
                if seg['par'] != f['par']:
                    g_ += c['pausa_parrafo']
                if f['texto'] == FORMULA:
                    g_ += 0.6
                if seg['i'] in cap_frase:
                    t_cap = t + 0.35
                    g_ += c['pausa_capitulo']
                    inicio_cap[seg['i']] = round(t_cap, 3)
                    cp = cap_frase[seg['i']]
                    rot.append({'t0': round(t_cap, 3), 't1': round(t_cap + g_ + 2.4, 3), 'texto': cp['titulo'],
                                'sub': f"Capítulo {cp['num']}", 'y': 0.46, 'tam': 64, 'fundido': 0.9})
                parts.append(np.zeros(int(g_ * sr))); t += g_
        voz = np.concatenate(parts).astype(np.float32)
        dur = OFFSET + len(voz) / sr + COLA
        # rótulo do reclamo cando se di a fórmula
        for f in frases:
            if f['texto'] == FORMULA:
                t0_, t1_ = tempos[f['i']]
                rot.insert(0, {'t0': round(t0_ - 0.2, 3), 't1': round(t1_ + 3.6, 3), 'texto': tema.get('titulo_rotulo', tema['titulo']),
                               'sub': RECLAMO, 'y': 0.46, 'tam': 60, 'fundido': 0.8})
        (W / 'tempos_frases.json').write_text(json.dumps(tempos, indent=1))
        caps_t = [dict(cap_frase[i], t0=inicio_cap[i]) for i in inicio_cap]
        (W / 'rotulos.json').write_text(json.dumps(rot, ensure_ascii=False, indent=1))
    save_t()

    # 3 planos e lista de planos (escrita fóra)
    with P.Etapa('4_escenas'):
        pl = planos(frases, tempos, dur, inicio_cap, tot)
        titulo_de = {}
        for c in caps_t:
            titulo_de[c['t0']] = f"{c['num']}. {c['titulo']}"
        cap_actual = 'Comezo'
        for p in pl:
            for t0c in sorted(titulo_de):
                if p['b0'] >= t0c - 0.01:
                    cap_actual = titulo_de[t0c]
            p['capitulo'] = cap_actual
        export = [{'n': p['n'], 'b0': round(p['b0'], 1), 'dur_s': round(p['b1'] - p['b0'], 1), 'fase': p['fase'],
                   'u': p['u'], 'capitulo': p['capitulo'], 'parte': p.get('parte'), 'texto': p['texto']} for p in pl]
        (W / 'planos.json').write_text(json.dumps(export, ensure_ascii=False, indent=1))
        if not a.escenas or not Path(a.escenas).exists():
            save_t()
            print(f'PENDENTE: escribir a lista de planos ({len(pl)} planos) a partir de {W / "planos.json"} en '
                  f'{a.escenas or "ESCENAS.json"} e volver lanzar o comando con --escenas'); sys.exit(3)
        pl = ler_escenas(a.escenas, pl)
        P.srt(frases, tempos, W / 'subtitulos.srt')
        (W / 'escenas.json').write_text(json.dumps(pl, ensure_ascii=False, indent=1))
    save_t()

    # 4 imaxes + porta de revisión
    with P.Etapa('5_imaxes'):
        import multiprocessing as mp_, imaxes
        from concurrent.futures import ProcessPoolExecutor
        # ProcessPoolExecutor e non Pool: se o OOM mata o proceso das imaxes, Pool queda colgado para sempre
        # (visto o 30-09-2026); o executor lanza BrokenProcessPool e lanzar.sh volve empezar (o feito queda na caché)
        with ProcessPoolExecutor(1, mp_context=mp_.get_context('spawn')) as ex_:
            imgs, rex = ex_.submit(imaxes.xerar, pl, W / 'imaxes', seed_base=tema['id']).result()
        kw = {'escenas': pl} if 'escenas' in inspect.signature(imaxes.graduar).parameters else {}
        imgs = imaxes.graduar(imgs, W / 'imaxes_graduadas', **kw)
    save_t()

    # 5 son (decisións D13 e D14 do promotor): o son de cada escena (campo `son` de cada plano ou, se falta, palabras
    # do prompt) co catálogo de son.py, variado e con eventos cada vez máis escasos; voz limpa no resto. O nivel segue
    # a curva (case nada no gancho) e a calma (0 ata o fin do gancho, 1 desde a metade: zona de durmir)
    with P.Etapa('6_son'):
        import son
        ini = sorted((tempos[f['i']][0], f['pal0']) for f in frases)
        xs = curva.nos(tot)
        rel_db, calma = [], []
        for seg in range(int(dur) + 1):
            p0 = next((pal for t0_, pal in reversed(ini) if t0_ <= seg), 0)
            rel_db.append(round(curva.en(p0, tot)['ambiente_db'], 2))
            calma.append(round(min(1.0, max(0.0, (p0 - xs[1]) / max(1, xs[3] - xs[1]))), 3))
        son_planos = [{'n': p['n'], 'b0': p['b0'], 'b1': p['b1'], 'son': son_do_plano(p),
                       'orixe': 'lista' if p.get('son') else 'prompt'} for p in pl]
        escena_tramos = son.tramos_de_planos([(x['b0'], x['b1'], x['son']) for x in son_planos])
        modo = tema.get('ambiente', 'escena')
        info_son = son.mesturar(voz, dur, OFFSET, str(W / 'mestura.wav'), str(W / 'voz_linea.wav'),
                                ambiente=modo, rel_db=rel_db, escena_tramos=escena_tramos, calma=calma,
                                semente=tema['id'])
        info_son['tramos'] = escena_tramos
        info_son['son_por_plano'] = son_planos
    save_t()

    # 6 montaxe (escritura atómica)
    with P.Etapa('7_montaxe'):
        import montaxe
        mp4 = W / 'video.mp4'; tmp = W / '.video.tmp.mp4'
        montaxe.render([{'b0': p['b0'], 'b1': p['b1'], 'movemento': p['movemento'], 'xf': p['xf']} for p in pl], imgs, dur,
                       str(W / 'mestura.wav'), str(W / 'subtitulos.srt'), tmp, W / 'montaxe', rotulos=rot,
                       vbr=f"{UMBRAIS['kbps_max'] - 200}k", bufsize='3000k')
        os.replace(tmp, mp4)
    save_t()

    # 7 qa
    with P.Etapa('8_qa'):
        res = {'umbrais': UMBRAIS, 'autoria': tema.get('autoria'), 'son': info_son, 'porta_texto': pt,
               'palabras': tot, 'capitulos': caps_t, 'rotulos': rot, 'nota_execucion': os.environ.get('QA_NOTA')}
        res['asr'] = qa.asr_por_frases(str(W / 'mestura.wav'), frases, tempos, P.CFG['whisper_dir'])
        res['ficheiro'] = qa.ficheiro(mp4, dur)
        res['ficheiro']['kbps'] = round(Path(mp4).stat().st_size * 8 / 1000 / res['ficheiro']['dur_video_s'])
        res['imaxes'] = qa.imaxes(imgs)
        res['revision_imaxes'] = rex
        res['escenas'] = [{'n': p['n'], 'b0': round(p['b0'], 1), 'dur_s': round(p['b1'] - p['b0'], 1), 'fase': p['fase'],
                           'movemento': p['movemento'], 'xf': p['xf'], 'prompt': p['prompt']} for p in pl]
        # ritmo por fase (palabras por minuto de narración, pausas incluídas)
        ritmo = {}
        for fase in curva.FASES:
            fs_ = [f for f in frases if curva.en(f['pal0'], tot)['fase'] == fase]
            if len(fs_) > 1:
                ritmo[fase] = round(sum(len(f['texto'].split()) for f in fs_) /
                                    ((tempos[fs_[-1]['i']][1] - tempos[fs_[0]['i']][0]) / 60), 1)
        res['ritmo_palabras_min_por_fase'] = ritmo
        res['planos_por_fase'] = {fase: sum(1 for p in pl if p['fase'] == fase) for fase in curva.FASES}
        res['duracion_media_plano_por_fase_s'] = {
            fase: round(float(np.mean([p['b1'] - p['b0'] for p in pl if p['fase'] == fase])), 1)
            for fase in curva.FASES if any(p['fase'] == fase for p in pl)}
        cortes = [p['b0'] for p in pl[1:]]
        qa.folla_contactos(mp4, dur, W / 'contactsheet.jpg', n=24, cols=6, evitar=cortes, xf=3.0)
        (W / 'descricion.txt').write_text(descricion(tema, caps_t, dur))
    save_t()
    res['tempos'] = P.TEMPOS
    res['parede_total_desta_execucion_s'] = round(time.time() - t_inicio, 1)
    f = res['ficheiro']
    dmin, dmax = tema.get('duracion_s', (1500, 2100))
    res['portas'] = {
        'autoria_declarada': bool(tema.get('autoria')),
        'duracion': dmin <= f['dur_video_s'] <= dmax,
        'wer_mestura': res['asr']['mestura']['wer'] <= UMBRAIS['wer_max'],
        'sincronia_av': f['desfase_av_s'] <= UMBRAIS['desfase_av_max_s'],
        'sincronia_subtitulos': res['asr']['mestura']['sincronia']['pct_dentro_da_sua_frase'] >= UMBRAIS['pct_sincronia_min'],
        **{k: v for k, v in pt['portas_texto'].items()},
        'imaxes_revisadas': all(r['ok'] for r in rex),
        'sonoridade': UMBRAIS['lufs'][0] <= f['lufs_integrado'] <= UMBRAIS['lufs'][1],
        'bitrate': f['kbps'] <= UMBRAIS['kbps_max'],
        'resolucion': f['resolucion'] == '1920x1080',
    }
    res['publicable'] = all(res['portas'].values())
    for nome in ('contactsheet.jpg', 'descricion.txt', 'subtitulos.srt', 'escenas.json', 'porta_texto.json',
                 'rotulos.json', 'guion.txt'):
        dest = 'subtitulos.gl.srt' if nome == 'subtitulos.srt' else nome
        shutil.copy(W / nome, S / f'.{dest}.tmp'); os.replace(S / f'.{dest}.tmp', S / dest)
    (S / 'qa.json').write_text(json.dumps(res, ensure_ascii=False, indent=1))
    (S / 'qa.md').write_text(informe(res, tema))
    print('publicable:', res['publicable'], res['portas'])


def informe(r, tema):
    f, a = r['ficheiro'], r['asr']['mestura']
    t = r['tempos']
    cpu = sum(v['cpu_s'] for v in t.values()); par = sum(v['parede_s'] for v in t.values())
    au = r.get('autoria') or {}
    L = [f"# QA automático: {tema['titulo']} ({tema['id']})", '',
         'Informe xerado por `herramientas/pipeline/longo.py`. Ningunha persoa revisou o vídeo, o guion nin as imaxes.', '',
         f"**Veredicto das portas automáticas: {'PUBLICABLE' if r['publicable'] else 'NON PUBLICABLE'}** "
         f"({sum(r['portas'].values())}/{len(r['portas'])}).", '',
         '## Quen fixo que', '',
         f"- Guion: {au.get('guion', '(sen declarar)')}",
         f"- Lista de planos (prompts das imaxes): {au.get('escenas', '(sen declarar)')}",
         f"- Automático e local: {au.get('automatico', 'voz, imaxes, porta de imaxes, son, montaxe e controis')}",
         '', '## Portas', '', '| Porta | Resultado |', '|---|---|']
    L += [f"| {k} | {'✅' if v else '❌'} |" for k, v in r['portas'].items()]
    ve = r['porta_texto']['veracidade']
    L += ['', '## Medidas', '',
          f"- Duración: {hms(f['dur_video_s'])} ({f['dur_video_s']} s), {f['resolucion']} a {f['fps']} fps, {f['mb']} MB, {f['kbps']} kb/s.",
          f"- Palabras do guion: {r['palabras']}. Ritmo por fase (palabras/min, pausas incluídas): {r['ritmo_palabras_min_por_fase']}.",
          f"- Planos por fase: {r['planos_por_fase']}; duración media por fase (s): {r['duracion_media_plano_por_fase_s']}.",
          f"- ASR (Whisper galego de Nós) sobre a mestura, frase a frase no seu treito: WER {a['wer']}; frases que soan no seu treito {a['sincronia']['pct_dentro_da_sua_frase']} %.",
          f"- Sonoridade: {f['lufs_integrado']} LUFS, LRA {f['lra_lu']} LU, pico real {f['pico_real_dbtp']} dBTP; desfase A/V {f['desfase_av_s']} s.",
          f"- Ambiente sonoro (D13): modo {r['son'].get('ambiente')}; "
          + (', '.join(f"{k} {v['segundos']} s" for k, v in (r['son'].get('escena') or {}).items() if isinstance(v, dict))
             or 'ningún') + f"; voz limpa {(r['son'].get('escena') or {}).get('pct_voz_limpa', '?')} % do tempo de voz.",
          f"- Lingua (LanguageTool gl-ES + hunspell): {len(r['porta_texto']['lingua'])} avisos. H1: {len(r['porta_texto']['h1_ancoraxe']['non_ancorados'])} sen ancorar.",
          f"- Veracidade: {ve['frases_avaliadas']} frases, {len(ve['marcadas'])} marcadas polo verificador automático, "
          f"{len(ve['sen_xustificar'])} sen xustificación (as xustificacións escribiunas o crítico de veracidade, un axente Claude).",
          f"- Imaxes: {len(r['revision_imaxes'])} planos; {sum(1 for x in r['revision_imaxes'] if x['ok'])} aprobados pola porta; "
          f"{sum(len(x['intentos']) for x in r['revision_imaxes'])} imaxes xeradas.",
          f"- Tempo: {round(par / 60, 1)} min de reloxo e {round(cpu / 3600, 2)} h de CPU de núcleo (etapas: "
          + ', '.join(f"{k} {round(v['parede_s'] / 60, 1)} min" for k, v in t.items()) + ').',
          '', '## Capítulos', '']
    L += [f"- {hms(c['t0'])} {c['num']}. {c['titulo']}" for c in r['capitulos']]
    if ve['marcadas']:
        L += ['', '## Frases marcadas pola porta de veracidade e a súa xustificación', '']
        L += [f"- «{m['frase']}» ({m['motivo']}) → {m['xustificacion'] or '**SEN XUSTIFICAR**'}" for m in ve['marcadas']]
    if r.get('nota_execucion'):
        L += ['', '## Nota da execución', '', r['nota_execucion']]
    return '\n'.join(L) + '\n'


if __name__ == '__main__':
    main()
