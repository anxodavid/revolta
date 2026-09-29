#!/usr/bin/env python
"""Pipeline automático de "Serán": ficha de tema (YAML) -> MP4 1920x1080 en galego, sen revisión humana.

    python pipeline.py temas/irmandinos-apertura.yaml --saida DIR --traballo DIR_BALEIRO --llm openai

Etapas (cada unha garda o seu resultado en --traballo e non se repite se xa existe):
  1 guion      LLM local (prompts/guion.md) co dossier; validación automática e ata 2 revisións (prompts/revisar.md)
  2 corrixir   LanguageTool gl-ES; se hai avisos, LLM (prompts/corrixir.md); só se acepta se non empeora
  3 voz        Nos_StyleTTS2-Brais-GL frase a frase (voz_st2.py), ritmo en embude (máis vivo ao principio)
  4 escenas    o código corta os planos coas duracións reais da voz (curtos ao principio, longos despois);
               o LLM (prompts/escenas.md) escribe un prompt de imaxe por plano
  5 imaxes     SDXL-Turbo en CPU (imaxes.py) + porta de revisión (revisor.py) que rexenera con outra semente
  6 son        choiva procedural e mestura (son.py)
  7 montaxe    Ken Burns + brétema lixeira + fundidos curtos, subtítulos SRT (montaxe.py)
  8 qa         ASR/WER, sincronía, lingua, H1, duración, sonoridade, imaxes, peso (qa.py) -> qa.json, qa.md
"""
import argparse, hashlib, json, math, os, re, shutil, subprocess, sys, time
from pathlib import Path
import numpy as np, soundfile as sf, yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import llm

SCRATCH = os.environ.get('SCRATCH', '/tmp/claude-0/-home-user-revolta/2e7d1051-da1e-54e9-bb2d-6cd0b746c55a/scratchpad')
CFG = {
    'python_tts': os.environ.get('PY_TTS', f'{SCRATCH}/tts/venv/bin/python'),
    'st2_dir': os.environ.get('ST2_DIR', f'{SCRATCH}/bench/st2'),
    'st2_path': os.environ.get('ST2_PATHBIN', f'{SCRATCH}/bench/pathbin'),
    'st2_stubs': os.environ.get('ST2_STUBS', f'{SCRATCH}/bench/stubs'),
    'ref_wav': os.environ.get('REF_WAV', f'{SCRATCH}/tts/kit/t1/brais_1_human.wav'),
    'whisper_dir': os.environ.get('WHISPER_DIR', f'{SCRATCH}/bench/wgl_ct2'),
}
OFFSET, COLA = 3.0, 6.0   # segundos de choiva antes da primeira frase e despois da última
FORMULA = 'Isto é Serán, historia de Galicia para durmir.'
# Ritmo en embude (feedback do promotor, 29-09-2026): ata GANCHO palabras, ritmo vivo; de GANCHO a
# CALMA palabras transición lineal; despois, ritmo de durmir.
GANCHO, CALMA = 150, 320
PAUSA = {'frase': (0.55, 1.35), 'paragrafo': (0.45, 1.0)}      # (inicio, calma), en segundos
PLANO_S = (5.5, 12.5)                                            # duración obxectivo dun plano (inicio, calma)
# Umbrais aliñados co plan (plan-de-negocio/gauntlet2/piezas/plan-desatendido.md §6.1): A1 WER <= 6 %,
# A2 sonoridade integrada entre -18 e -16 LUFS, H1 0 nomes/cantidades sen ancorar no dossier.
UMBRAIS = {'dur_min_s': 180, 'dur_max_s': 300, 'wer_max': 0.06, 'desfase_av_max_s': 0.1,
           'pct_sincronia_min': 95.0, 'mb_max': 50, 'lt_max': 2, 'lufs': (-18, -16), 'h1_non_ancorados_max': 0}
REVISIONS_GUION, INTENTOS_ESCENAS = 2, 3

TEMPOS = {}


class Etapa:
    def __init__(self, nome): self.nome = nome

    def __enter__(self):
        self.t, self.c = time.time(), os.times(); print(f'== {self.nome}', flush=True)

    def __exit__(self, *a):
        c = os.times()
        cpu = (c.user - self.c.user) + (c.system - self.c.system) + (c.children_user - self.c.children_user) \
            + (c.children_system - self.c.children_system)
        # etapas con caché (1-6): súmase o traballo de cada execución; montaxe e QA refanse sempre
        prev = TEMPOS.get(self.nome, {'parede_s': 0, 'cpu_s': 0}) if self.nome < '7' else {'parede_s': 0, 'cpu_s': 0}
        TEMPOS[self.nome] = {**prev, 'parede_s': round(prev['parede_s'] + time.time() - self.t, 1),
                             'cpu_s': round(prev['cpu_s'] + cpu, 1)}


def cpu_llm(etapa, meta):
    """O servidor LLM é outro proceso: o seu tempo de CPU (medido en /proc) súmase á etapa que o usou."""
    if meta.get('da_cache') or not meta.get('cpu_s_servidor'):
        return
    e = TEMPOS.setdefault(etapa, {'parede_s': 0, 'cpu_s': 0})
    e['cpu_s'] = round(e['cpu_s'] + meta['cpu_s_servidor'], 1)
    e['cpu_s_llm'] = round(e.get('cpu_s_llm', 0) + meta['cpu_s_servidor'], 1)


def partir(texto):
    frases, i = [], 0
    for pi, par in enumerate([p.strip() for p in texto.split('\n\n') if p.strip()]):
        for s in re.split(r'(?<=[.!?…])\s+', ' '.join(par.split())):
            if s.strip():
                i += 1; frases.append({'i': i, 'par': pi, 'texto': s.strip()})
    return frases


def rampa(x, a, b, x0=GANCHO, x1=CALMA):
    u = min(1.0, max(0.0, (x - x0) / (x1 - x0)))
    return a + (b - a) * u


# ------------------------------------------------------------------ guion: validación e texto fixo
def limpar_saida_llm(t):
    """Quita o que un LLM pequeno adoita engadir arredor do texto (títulos, marcas, notas finais)."""
    t = t.replace('\r', '').strip()
    t = re.sub(r'^\s*(#+ .*|\*\*[^*]+\*\*|Título:.*|Texto( narrado)?:)\s*\n', '', t)
    t = re.sub(r'\n\s*(Nota|Notas|---)\b.*$', '', t, flags=re.S)
    t = re.sub(r'[*_#]+', '', t)
    return re.sub(r'\n{3,}', '\n\n', t).strip()


def texto_fixo(g, aviso):
    """O aviso e a fórmula son texto fixo do canal: o código garante que están literais (non o LLM)."""
    pars = [p.strip() for p in g.split('\n\n') if p.strip()]
    if not g.startswith(aviso):
        sen = [s for s in re.split(r'(?<=[.!?…])\s+', ' '.join(pars[0].split()))
               if not re.search(r'boas noites|sintétic|proceso automático', s, re.I)] if pars else []
        pars = [aviso] + ([' '.join(sen)] if sen else []) + pars[1:]
    if FORMULA not in g:
        v = [k for k, p in enumerate(pars) if re.search(r'Isto é Serán', p)]
        if v:
            pars[v[0]] = re.sub(r'Isto é Serán[^.!?]*[.!?]', FORMULA, pars[v[0]], count=1)
        else:
            pars.insert(min(2, len(pars)), FORMULA)
    return '\n\n'.join(pars)


def validar_guion(g, tema):
    import qa, ancoraxe
    fr = partir(g)
    e = qa.estilo(g, fr, tema['aviso'], tema['palabras'])
    h1 = ancoraxe.ancoraxe(g, tema['dossier'], [tema['aviso']])
    p = []
    if abs(e['desvio_palabras_pct']) > 15:
        p.append(f"Ten {e['palabras']} palabras e debe ter arredor de {tema['palabras']}.")
    if e['cifras']:
        p.append(f"Escribe estes números en letra: {', '.join(e['cifras'])}.")
    if e['signos_prohibidos']:
        p.append(f"Quita estes signos, que a voz non le: {' '.join(sorted(set(e['signos_prohibidos'])))}.")
    if e['preguntas']:
        p.append('Quita as preguntas: convérteas en frases afirmativas.')
    if e['palabras_vetadas']:
        p.append(f"Quita estas palabras: {', '.join(e['palabras_vetadas'])}.")
    longas = [f['texto'] for f in fr if len(f['texto'].split()) > 30]
    for f in longas:
        p.append(f'Parte esta frase, que é longa de máis: "{f}"')
    vistos = set()
    for x in h1['non_ancorados']:
        if x['texto'] not in vistos:
            vistos.add(x['texto'])
            p.append(f"\"{x['texto']}\" non está no dossier: quítao ou cámbiao por un dato do dossier. Frase: \"{x['frase']}\"")
    return p, e, h1


# ------------------------------------------------------------------ subtítulos
def srt(frases, tempos, out, maxc=84, min_s=1.3):
    def ts(x):
        h, r = divmod(x, 3600); m, s = divmod(r, 60)
        return f'{int(h):02d}:{int(m):02d}:{int(s):02d},{int(round((s % 1) * 1000)):03d}'.replace(',1000', ',999')

    def dividir(ws, n):   # n anacos de lonxitude parecida, en límites de palabra
        tot = len(' '.join(ws)); out, cur = [], []
        for w in ws:
            cur.append(w)
            if len(out) < n - 1 and len(' '.join(cur)) >= tot / n:
                out.append(cur); cur = []
        return out + ([cur] if cur else [])

    lines, n = [], 0
    for f in frases:
        for (t0, t1), txt in zip(f.get('tramos', [tempos[f['i']]]), f.get('tramos_texto', [f['texto']])):
            ws = txt.split()
            k = max(1, math.ceil(len(txt) / maxc))
            while k > 1 and (t1 - t0) / k < min_s:     # sen anacos orfos de medio segundo
                k -= 1
            parts = [' '.join(p) for p in dividir(ws, k)]
            tot = sum(len(p) for p in parts); acc = t0
            for p in parts:
                d = (t1 - t0) * len(p) / tot
                l1, l2 = dividir(p.split(), 2) if len(p) > 42 else (p.split(), [])
                txt2 = ' '.join(l1) + ('\n' + ' '.join(l2) if l2 else '')
                n += 1; lines.append(f'{n}\n{ts(acc)} --> {ts(acc + d)}\n{txt2}\n')
                acc += d
    Path(out).write_text('\n'.join(lines))


# ------------------------------------------------------------------ planos
def planos(frases, tempos, dur):
    """Corta a narración en planos segundo as duracións reais da voz: curtos no gancho, longos despois.
    Unha frase moito máis longa ca o plano obxectivo repártese en varios planos."""
    out, cur, pal = [], None, 0
    for f in frases:
        t0, t1 = tempos[f['i']]
        obx = rampa(pal, *PLANO_S)
        pal += len(f['texto'].split())
        if (t1 - t0) > 1.7 * obx:
            if cur: out.append(cur); cur = None
            k = round((t1 - t0) / obx)
            for j in range(k):
                out.append({'frases': [f['i']], 't0': t0 + j * (t1 - t0) / k, 'texto': f['texto'],
                            'parte': f'{j + 1}/{k}'})
            continue
        if cur is None:
            cur = {'frases': [f['i']], 't0': t0, 'texto': f['texto']}
        else:
            cur['frases'].append(f['i']); cur['texto'] += ' ' + f['texto']
        if t1 - cur['t0'] >= obx * 0.85:
            out.append(cur); cur = None
    if cur:
        if out and tempos[cur['frases'][-1]][1] - cur['t0'] < PLANO_S[0]:
            out[-1]['frases'] += [i for i in cur['frases'] if i not in out[-1]['frases']]
            out[-1]['texto'] += ' ' + cur['texto']
        else:
            out.append(cur)
    movs = ['zoom_in', 'pan_right', 'zoom_out', 'pan_left', 'zoom_in', 'pan_up']
    for k, p in enumerate(out):
        p['b0'] = 0.0 if k == 0 else max(0.0, p['t0'] - (0.25 if 'parte' not in p or p['parte'].startswith('1/') else 0))
        p['movemento'] = movs[k % len(movs)]
    for k, p in enumerate(out):
        p['b1'] = out[k + 1]['b0'] if k + 1 < len(out) else dur
    return out


def escenas_llm(tema, pl, backend):
    """O LLM escribe un prompt por plano. Se faltan liñas, reintenta; o que siga faltando énchese cun
    prompt xenérico (queda anotado no QA)."""
    import imaxes
    txt = '\n'.join(f"{k + 1}. ({p['b1'] - p['b0']:.0f} s{', same sentence, part ' + p['parte'] if 'parte' in p else ''}) "
                    f"{p['texto']}" for k, p in enumerate(pl))
    metas, prompts = [], {}
    for intento in range(INTENTOS_ESCENAS):
        extra = '' if intento == 0 else f'\n(Attempt {intento + 1}: write exactly {len(pl)} numbered lines.)'
        raw, meta = llm.complete('escenas', backend, titulo=tema['titulo'], escenas=txt + extra, n_escenas=len(pl))
        metas.append(meta)
        for l in raw.splitlines():
            m = re.match(r'^\s*(?:shot\s*)?(\d+)\s*[.):-]\s*(.+)$', l.strip(), re.I)
            if m and 1 <= int(m.group(1)) <= len(pl) and int(m.group(1)) not in prompts:
                pr = re.sub(r'^\(?\d+ ?s[^)]*\)\s*', '', m.group(2)).strip().strip('"')
                if len(pr.split()) >= 6:
                    prompts[int(m.group(1))] = pr
        if len(prompts) == len(pl):
            break
    faltan = [k for k in range(1, len(pl) + 1) if k not in prompts]
    for k in faltan:
        prompts[k] = imaxes.XENERICO
    return [prompts[k + 1] for k in range(len(pl))], metas, faltan


# ------------------------------------------------------------------ principal
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('tema'); ap.add_argument('--saida', required=True)
    ap.add_argument('--traballo', default=None); ap.add_argument('--queimar-subtitulos', action='store_true')
    ap.add_argument('--llm', default=os.environ.get('LLM_BACKEND', 'openai'), choices=['manual', 'openai'])
    a = ap.parse_args()
    t_inicio = time.time()
    tema = yaml.safe_load(open(a.tema))
    W = Path(a.traballo or f"{SCRATCH}/pipeline_work/{tema['id']}"); W.mkdir(parents=True, exist_ok=True)
    S = Path(a.saida); S.mkdir(parents=True, exist_ok=True)
    if 'LLM_CACHE' not in os.environ:
        llm.CACHE = W / 'llm_cache'; llm.PENDING = W / 'llm_pending'
    tp = W / 'tempos.json'
    if tp.exists():
        TEMPOS.update(json.loads(tp.read_text()))
    save_t = lambda: tp.write_text(json.dumps(TEMPOS, indent=1))
    info = {'tema': tema['id'], 'llm': {}, 'backend_llm': a.llm}
    import qa
    try:
        # 1 guion (LLM + validación automática + revisións)
        with Etapa('1_guion'):
            g, meta = llm.complete('guion', a.llm, titulo=tema['titulo'], tema=tema['tema'],
                                   fragmento=tema['fragmento'], palabras=tema['palabras'],
                                   aviso=tema['aviso'], dossier=tema['dossier'].strip())
            info['llm']['guion'] = meta; cpu_llm('1_guion', meta)
            if 'arranque_cpu_s' in llm._SERVER and not llm._SERVER.get('contado'):
                TEMPOS['1_guion']['cpu_s'] = round(TEMPOS['1_guion']['cpu_s'] + llm._SERVER['arranque_cpu_s'], 1)
                llm._SERVER['contado'] = True
            orixinal = limpar_saida_llm(g)
            g = texto_fixo(orixinal, tema['aviso'])
            info['guion_llm_bruto'] = orixinal
            info['texto_fixo_engadido_polo_codigo'] = g != orixinal
            probs, _, _ = validar_guion(g, tema)
            historial = [{'versión': 0, 'problemas': probs}]
            mellor = (len(probs), g)
            for k in range(REVISIONS_GUION):
                if not probs:
                    break
                g2, meta = llm.complete('revisar', a.llm, guion=g, problemas='\n'.join(f'- {x}' for x in probs),
                                        aviso=tema['aviso'], dossier=tema['dossier'].strip())
                info['llm'][f'revisar_{k + 1}'] = meta; cpu_llm('1_guion', meta)
                g = texto_fixo(limpar_saida_llm(g2), tema['aviso'])
                probs, _, _ = validar_guion(g, tema)
                historial.append({'versión': k + 1, 'problemas': probs})
                if len(probs) < mellor[0]:
                    mellor = (len(probs), g)
            g = mellor[1]
            info['revisions_guion'] = historial
            (W / 'guion_1.txt').write_text(g + '\n')
        # 2 corrección lingüística
        with Etapa('2_corrixir'):
            lt1 = qa.lingua(g, dossier=tema['dossier'])
            info['lt_antes'] = lt1
            guion = g
            if lt1:
                avisos = '\n'.join(f"- [{m['regra']}] {m['mensaxe']} | contexto: \"{m['contexto']}\" | "
                                   f"suxestións: {', '.join(m['suxestions']) or '-'}" for m in lt1)
                gc, meta = llm.complete('corrixir', a.llm, guion=g, avisos=avisos)
                info['llm']['corrixir'] = meta; cpu_llm('2_corrixir', meta)
                gc = texto_fixo(limpar_saida_llm(gc), tema['aviso'])
                p0, _, _ = validar_guion(g, tema); p1, _, _ = validar_guion(gc, tema)
                lt2 = qa.lingua(gc, dossier=tema['dossier'])
                aceptada = len(p1) <= len(p0) and len(lt2) <= len(lt1)
                info['correccion'] = {'aceptada': aceptada, 'avisos_lt': [len(lt1), len(lt2)],
                                      'problemas_validacion': [len(p0), len(p1)]}
                if aceptada:
                    guion = gc
        (W / 'guion.txt').write_text(guion + '\n')
        save_t()
    except llm.PendingLLM as e:
        save_t(); print(e); sys.exit(3)
    frases = partir(guion)

    # 3 voz, ritmo en embude
    esc_min, esc_max = tema.get('escala_inicio', 1.05), tema.get('escala', 1.25)
    with Etapa('3_voz'):
        pal = 0
        for k, f in enumerate(frases):
            f['pal0'] = pal; pal += len(f['texto'].split())
            f['escala'] = round(rampa(f['pal0'], esc_min, esc_max), 3)
            f['wav'] = f"{f['i']:03d}-{hashlib.sha256((f['texto'] + str(f['escala'])).encode()).hexdigest()[:8]}.wav"
        fj = W / 'frases.json'; fj.write_text(json.dumps(frases, ensure_ascii=False, indent=1))
        env = dict(os.environ, PATH=f"{CFG['st2_path']}:{os.environ['PATH']}", PYTHONPATH=CFG['st2_stubs'],
                   ST2_DIR=CFG['st2_dir'], REF_WAV=CFG['ref_wav'], SCALE=str(esc_max))
        vdir = W / 'voz'
        subprocess.run([CFG['python_tts'], str(HERE / 'voz_st2.py'), str(fj), str(vdir)], env=env, check=True)
        sr = 24000; parts = []; tempos = {}; t = OFFSET
        for k, f in enumerate(frases):
            w, _ = sf.read(vdir / f['wav'])
            tempos[f['i']] = (round(t, 3), round(t + len(w) / sr, 3))
            parts.append(w); t += len(w) / sr
            if k + 1 < len(frases):
                nw = len(frases[k + 1]['texto'].split())
                g_ = rampa(f['pal0'], *PAUSA['frase']) + min(0.3, max(-0.15, 0.02 * (nw - 14)))
                if frases[k + 1]['par'] != f['par']:
                    g_ += rampa(f['pal0'], *PAUSA['paragrafo'])
                if FORMULA in f['texto']:
                    g_ += 0.6
                parts.append(np.zeros(int(g_ * sr))); t += g_
        voz = np.concatenate(parts).astype(np.float32)
        dur = OFFSET + len(voz) / sr + COLA
        (W / 'tempos_frases.json').write_text(json.dumps(tempos, indent=1))
    save_t()

    # 4 escenas: planos polo código, prompts polo LLM
    with Etapa('4_escenas'):
        pl = planos(frases, tempos, dur)
        prompts, metas, faltan = escenas_llm(tema, pl, a.llm)
        for k, m in enumerate(metas):
            info['llm'][f'escenas_{k + 1}'] = m; cpu_llm('4_escenas', m)
        for p, pr in zip(pl, prompts):
            p['prompt'] = pr
        info['escenas_prompts_xenericos'] = faltan
        (W / 'escenas.json').write_text(json.dumps(pl, ensure_ascii=False, indent=1))
        # subtítulos: as frases partidas en varios planos seguen sendo un só subtítulo
        srt(frases, tempos, W / 'subtitulos.srt')
    llm.parar()
    info['llm_servidor'] = {k: v for k, v in llm._SERVER.items() if k != 'proc'}
    save_t()

    # 5 imaxes + porta de revisión
    with Etapa('5_imaxes'):
        import imaxes
        imgs, rex = imaxes.xerar(pl, W / 'imaxes', seed_base=tema['id'])
        info['imaxes_rexistro'] = rex
        info['imaxes_xeracion_s'] = sum(i['s'] for r in rex for i in r['intentos'] if 's' in i)
        info['imaxes_revision_s'] = sum(i.get('s_revision', 0) for r in rex for i in r['intentos'])
    save_t()

    # 6 son
    with Etapa('6_son'):
        import son
        info['son'] = son.mesturar(voz, dur, OFFSET, str(W / 'mestura.wav'), str(W / 'voz_linea.wav'))
    save_t()

    # 7 montaxe (escritura atómica: o MP4 final só aparece cando está completo)
    with Etapa('7_montaxe'):
        import montaxe
        mp4 = S / 'ejemplo.mp4'; tmp = S / '.ejemplo.tmp.mp4'
        montaxe.render([{'b0': p['b0'], 'b1': p['b1'], 'movemento': p['movemento']} for p in pl], imgs, dur,
                       str(W / 'mestura.wav'), str(W / 'subtitulos.srt'), tmp, W / 'montaxe',
                       queimar=a.queimar_subtitulos)
        os.replace(tmp, mp4)
        shutil.copy(W / 'subtitulos.srt', S / 'subtitulos.gl.srt')
    save_t()

    # 8 qa
    with Etapa('8_qa'):
        import ancoraxe
        res = {'umbrais': UMBRAIS, 'son': info['son'], 'llm': info['llm'], 'backend_llm': a.llm,
               'llm_servidor': info.get('llm_servidor'),
               'imaxes_xeracion_s': info.get('imaxes_xeracion_s'), 'imaxes_revision_s': info.get('imaxes_revision_s'),
               'revisions_guion': info['revisions_guion'], 'correccion': info.get('correccion'),
               'texto_fixo_engadido_polo_codigo': info['texto_fixo_engadido_polo_codigo'],
               'guion_llm_bruto': info['guion_llm_bruto'],
               'escenas_prompts_xenericos': info['escenas_prompts_xenericos']}
        res['lingua_antes_correccion'] = info['lt_antes']
        res['lingua'] = qa.lingua(guion, dossier=tema['dossier'])
        res['h1_ancoraxe'] = ancoraxe.ancoraxe(guion, tema['dossier'], [tema['aviso']])
        res['estilo'] = qa.estilo(guion, frases, tema['aviso'], tema['palabras'])
        res['asr'] = qa.asr(str(W / 'mestura.wav'), str(W / 'voz_linea.wav'), frases, tempos, CFG['whisper_dir'])
        res['ficheiro'] = qa.ficheiro(mp4, dur)
        res['imaxes'] = qa.imaxes(imgs)
        res['revision_imaxes'] = info['imaxes_rexistro']
        res['escenas'] = [{'escena': k, 'frases': p['frases'], 'b0': round(p['b0'], 1), 'dur_s': round(p['b1'] - p['b0'], 1),
                           'movemento': p['movemento'], 'prompt': p['prompt']} for k, p in enumerate(pl)]
        nw = res['estilo']['palabras']
        res['ritmo_palabras_min'] = round(nw / ((tempos[frases[-1]['i']][1] - OFFSET) / 60), 1)
        lim = [f for f in frases if f['pal0'] < GANCHO]
        res['ritmo_gancho_palabras_min'] = round(sum(len(f['texto'].split()) for f in lim) /
                                                 ((tempos[lim[-1]['i']][1] - OFFSET) / 60), 1)
        res['planos_primeiro_minuto'] = sum(1 for p in pl if p['b0'] < 60)
        cortes = [p['b0'] for p in pl[1:]]
        qa.folla_contactos(mp4, dur, S / 'contactsheet.jpg', evitar=cortes, xf=montaxe.XF)
    TEMPOS['8_qa']['nota'] = 'inclúe a folla de contactos'
    save_t()
    res['tempos'] = TEMPOS
    res['parede_total_desta_execucion_s'] = round(time.time() - t_inicio, 1)
    f = res['ficheiro']
    metas = list(res['llm'].values())
    res['portas'] = {
        'llm_local_desatendido': a.llm == 'openai' and all(m.get('backend') == 'openai' for m in metas),
        'duracion': UMBRAIS['dur_min_s'] <= f['dur_video_s'] <= UMBRAIS['dur_max_s'],
        'wer_mestura': res['asr']['mestura']['wer'] <= UMBRAIS['wer_max'],
        'sincronia_av': f['desfase_av_s'] <= UMBRAIS['desfase_av_max_s'],
        'sincronia_subtitulos': res['asr']['mestura']['sincronia']['pct_dentro_da_sua_frase'] >= UMBRAIS['pct_sincronia_min'],
        'lingua_lt': len(res['lingua']) <= UMBRAIS['lt_max'],
        'h1_ancoraxe': len(res['h1_ancoraxe']['non_ancorados']) <= UMBRAIS['h1_non_ancorados_max'],
        'estilo': not (res['estilo']['cifras'] or res['estilo']['signos_prohibidos'] or res['estilo']['palabras_vetadas']
                       or res['estilo']['preguntas'])
                  and res['estilo']['aviso_literal'] and res['estilo']['formula_literal'],
        'imaxes_revisadas': all(r['ok'] for r in res['revision_imaxes']),
        'sonoridade': UMBRAIS['lufs'][0] <= f['lufs_integrado'] <= UMBRAIS['lufs'][1],
        'peso': f['mb'] <= UMBRAIS['mb_max'],
        'resolucion': f['resolucion'] == '1920x1080',
    }
    res['publicable'] = all(res['portas'].values())
    (S / 'qa.json').write_text(json.dumps(res, ensure_ascii=False, indent=1))
    (S / 'qa.md').write_text(informe(res, tema, guion))
    print('publicable:', res['publicable'], res['portas'])


def informe(r, tema, guion):
    f, a, e, t = r['ficheiro'], r['asr'], r['estilo'], r['tempos']
    cpu = sum(v['cpu_s'] for v in t.values()); par = sum(v['parede_s'] for v in t.values())
    cpu_llm = sum(v.get('cpu_s_llm', 0) for v in t.values())
    L = [f"# QA automático: {tema['titulo']} ({tema['id']})", '',
         'Informe xerado por `herramientas/pipeline/pipeline.py` (etapa 8). Ningunha persoa revisou o vídeo, o guion nin as imaxes.', '',
         f"**Veredicto automático: {'PUBLICABLE' if r['publicable'] else 'NON PUBLICABLE'}** "
         f"({sum(r['portas'].values())}/{len(r['portas'])} portas)", '',
         '| Porta | Resultado |', '|---|---|']
    L += [f'| {k} | {"pasa" if v else "FALLA"} |' for k, v in r['portas'].items()]
    ms = list(r['llm'].values())
    mod = sorted({m.get('modelo') or m.get('model') or '?' for m in ms})
    L += ['', '## Execución', '',
          f"Backend LLM: `{r['backend_llm']}`; modelo(s): {', '.join(f'`{x}`' for x in mod)}. "
          f"Chamadas ao LLM: {len(ms)}, das que {sum(1 for m in ms if not m.get('da_cache'))} feitas nesta execución "
          f"e {sum(1 for m in ms if m.get('da_cache'))} lidas da caché do directorio de traballo. "
          + ('Todas as respostas do LLM veñen do servidor local (ningunha escrita a man nin por un LLM externo).'
             if r['portas']['llm_local_desatendido'] else
             '**Hai respostas do LLM que non veñen do servidor local: esta execución NON é desatendida.**'), '']
    if r.get('llm_servidor'):
        L += [f"Servidor LLM arrancado polo propio pipeline: {r['llm_servidor']}.", '']
    L += ['', '## Ficheiro', '', '| Medida | Valor |', '|---|---|']
    L += [f'| {k} | {v} |' for k, v in f.items()]
    L += [f"| ritmo global (palabras/min, pausas incluídas) | {r['ritmo_palabras_min']} |",
          f"| ritmo do gancho (primeiras {GANCHO} palabras) | {r['ritmo_gancho_palabras_min']} |",
          f"| planos no primeiro minuto | {r['planos_primeiro_minuto']} |", f"| planos en total | {len(r['escenas'])} |"]
    L += ['', '## ASR (Whisper large-v3-turbo galego de Nós, CTranslate2 int8)', '',
          '| Audio | WER | Subst. | Borr. | Ins. | Palabras ref. |', '|---|---|---|---|---|---|']
    for k in ('mestura', 'voz'):
        L.append(f"| {k} | {a[k]['wer']} | {a[k]['sub']} | {a[k]['del']} | {a[k]['ins']} | {a[k]['palabras_ref']} |")
    s = a['mestura']['sincronia']
    L += ['', f"Sincronía subtítulos-voz (marcas de tempo por palabra do ASR contra o SRT): {s['pct_dentro_da_sua_frase']} % "
          f"das {s['palabras_aliñadas']} palabras aliñadas caen dentro da súa frase (±0,5 s); desfase no inicio de frase: "
          f"mediana {s['desfase_inicio_frase_s_mediana']} s, máximo {s['desfase_inicio_frase_s_max_abs']} s "
          f"({s['frases_medidas']} frases medidas).", '',
          f"Frases con WER > 0,5 (candidatas a erro de pronuncia): {a['mestura']['frases_wer_mais_0_5'] or 'ningunha'}.", '',
          '<details><summary>Transcrición ASR da mestura</summary>', '', a['mestura']['hipotese'], '', '</details>', '',
          '## Guion: validación automática e revisións do LLM', '']
    for h in r['revisions_guion']:
        L.append(f"- versión {h['versión']}: {len(h['problemas'])} problemas" +
                 (': ' + ' | '.join(h['problemas'][:8]) if h['problemas'] else ''))
    L += ['', f"O código engadiu ou fixou o aviso e a fórmula literais: {'si' if r['texto_fixo_engadido_polo_codigo'] else 'non'}.", '',
          '## Lingua (LanguageTool 6.8 gl-ES, con hunspell galego)', '',
          f"Avisos antes da corrección automática: {len(r['lingua_antes_correccion'])}. Despois: {len(r['lingua'])}. "
          f"Corrección do LLM: {r.get('correccion') or 'non fixo falta'}.", '']
    for m in r['lingua_antes_correccion']:
        L.append(f"- antes: `{m['regra']}` {m['mensaxe']} — \"{m['contexto']}\"")
    for m in r['lingua']:
        L.append(f"- despois: `{m['regra']}` {m['mensaxe']} — \"{m['contexto']}\"")
    h1 = r['h1_ancoraxe']
    L += ['', f"## H1: nomes e cantidades ancorados no dossier", '',
          f"{h1['items']} elementos, {h1['pct_ancorado']} % ancorados. Sen ancorar: "
          + (', '.join(f"\"{x['texto']}\"" for x in h1['non_ancorados']) or 'ningún') + '.']
    L += ['', '## Estilo e densidade (regras do canal)', '', '| Control | Valor |', '|---|---|']
    L += [f'| {k} | {v} |' for k, v in e.items()]
    L += ['', '## Son', '', '| Medida | Valor |', '|---|---|'] + [f'| {k} | {v} |' for k, v in r['son'].items()]
    rv = r['revision_imaxes']
    nint = sum(len(x['intentos']) for x in rv)
    L += ['', '## Porta de imaxes (revisor.py: MediaPipe mans/corpo + Florence-2 e lista de anacronismos)', '',
          f"{len(rv)} planos, {nint} imaxes xeradas ({nint - len(rv)} rexeneracións). Aprobadas á primeira: "
          f"{sum(1 for x in rv if x['ok'] and len(x['intentos']) == 1)}; aprobadas tras rexenerar: "
          f"{sum(1 for x in rv if x['ok'] and len(x['intentos']) > 1)}; sen aprobar: {sum(1 for x in rv if not x['ok'])}.", '',
          '| Plano | Intentos | Problemas nos intentos rexeitados | Escollida |', '|---|---|---|---|']
    for k, x in enumerate(rv):
        rex = '; '.join(f"{i['intento']}: {', '.join(i['problemas'])}" for i in x['intentos'] if i['problemas']) or '-'
        L.append(f"| {k} | {len(x['intentos'])} | {rex} | {x['escollida']} ({'ok' if x['ok'] else 'FALLA'}) |")
    if r.get('escenas_prompts_xenericos'):
        L += ['', f"Planos co prompt xenérico porque o LLM non deu liña: {r['escenas_prompts_xenericos']}."]
    L += ['', '## Planos e imaxes', '', '| # | Inicio | Frases | Dur. (s) | Mov. | Lum. | Contr. | Simil. ant. | Descrición do revisor (Florence-2) | Prompt do LLM |',
          '|---|---|---|---|---|---|---|---|---|---|']
    for sc, im, x in zip(r['escenas'], r['imaxes'], rv):
        desc = x['intentos'][x['escollida']].get('descricion', '').replace('|', '/')
        L.append(f"| {sc['escena']} | {int(sc['b0'] // 60)}:{int(sc['b0'] % 60):02d} | {sc['frases'][0]}-{sc['frases'][-1]} | "
                 f"{sc['dur_s']} | {sc['movemento']} | {im['luminancia']} | {im['contraste']} | "
                 f"{im['similitude_coa_anterior']} | {desc} | {sc['prompt']} |")
    L += ['', '## Tempos (CPU: 4 núcleos, sen GPU)', '',
          '| Etapa | Parede (s) | CPU (s) | dos que servidor LLM (s) |', '|---|---|---|---|']
    L += [f"| {k} | {v['parede_s']} | {v['cpu_s']} | {v.get('cpu_s_llm', '')} |" for k, v in t.items()]
    L += [f'| **Total** | **{round(par, 1)}** | **{round(cpu, 1)}** | **{round(cpu_llm, 1)}** |', '',
          f"Tempo total de CPU: {round(cpu / 3600, 2)} h de núcleo (das que LLM local: {round(cpu_llm / 3600, 2)} h); "
          f"parede: {round(par / 60, 1)} min. Inclúe o LLM local e o arranque do seu servidor; non inclúe a descarga de modelos.", '']
    L += ['## LLM (chamadas)', '', '| Chamada | Caché | Segundos | Tokens entrada/saída | Tokens/s saída | CPU servidor (s) |',
          '|---|---|---|---|---|---|']
    for k, v in r['llm'].items():
        u = v.get('usage') or {}
        L.append(f"| {k} | `{v.get('cache')}`{' (da caché)' if v.get('da_cache') else ''} | {v.get('segundos')} | "
                 f"{u.get('prompt_tokens')}/{u.get('completion_tokens')} | {v.get('tokens_saida_por_s')} | {v.get('cpu_s_servidor')} |")
    L += ['']
    L += extrapolacion(r)
    L += ['## Guion final narrado', '', guion, '']
    return '\n'.join(L)


def extrapolacion(r, minutos=60):
    """Extrapola linealmente os tempos medidos a un episodio longo [S: supón custo proporcional]."""
    t, f = r['tempos'], r['ficheiro']
    dur = f['dur_video_s']; D = minutos * 60; fac = D / dur
    g = lambda k: t.get(k, {'parede_s': 0, 'cpu_s': 0})
    L = [f'## Extrapolación a un episodio de {minutos} min [S: escala lineal dos tempos medidos]', '',
         'Supostos: mesma densidade de texto e de planos que esta mostra (o gancho só está ao principio, así que '
         'un episodio longo ten planos máis longos de media e isto sobreestima as imaxes), custo proporcional á '
         'duración en todas as etapas (tamén o LLM: guion e escenas por bloques), carga dos modelos unha vez.', '',
         '| Etapa | Parede (min) | CPU (h de núcleo) |', '|---|---|---|']
    tp = tc = 0
    for k in ('1_guion', '2_corrixir', '3_voz', '4_escenas', '5_imaxes', '6_son', '7_montaxe', '8_qa'):
        p, c = g(k)['parede_s'] * fac / 60, g(k)['cpu_s'] * fac / 3600
        tp += p; tc += c
        L.append(f'| {k} | {p:.0f} | {c:.2f} |')
    L += [f'| **Total** | **{tp:.0f}** ({tp / 60:.1f} h) | **{tc:.2f}** |', '']
    return L


def _informe_de_novo(qa_json, tema_yaml, guion_txt, out_md):
    r = json.loads(Path(qa_json).read_text()); tema = yaml.safe_load(open(tema_yaml))
    Path(out_md).write_text(informe(r, tema, Path(guion_txt).read_text().strip()))


if __name__ == '__main__':
    if len(sys.argv) == 6 and sys.argv[1] == '--so-informe':
        _informe_de_novo(*sys.argv[2:])   # qa.json tema.yaml guion.txt qa.md
    else:
        main()
