#!/usr/bin/env python
"""Pipeline automático de "Serán": ficha de tema (YAML) -> MP4 1920x1080 en galego, sen revisión humana.

    python pipeline.py temas/irmandinos-apertura.yaml --saida DIR [--queimar-subtitulos]

Etapas (cada unha garda o seu resultado en --traballo e non se repite se xa existe):
  1 guion      LLM (prompts/guion.md) co dossier de fontes do tema
  2 corrixir   LanguageTool gl-ES; se hai avisos, LLM (prompts/corrixir.md), unha volta
  3 escenas    LLM (prompts/escenas.md): agrupa as frases en escenas e escribe o prompt de cada imaxe
  4 voz        Nos_StyleTTS2-Brais-GL frase a frase (voz_st2.py) + pausas para durmir
  5 imaxes     SDXL-Turbo en CPU (imaxes.py)
  6 son        choiva procedural e mestura (son.py)
  7 montaxe    Ken Burns + brétema + fundidos, subtítulos SRT (montaxe.py)
  8 qa         ASR/WER, sincronía, lingua, duración, sonoridade, imaxes, peso (qa.py) -> qa.json, qa.md
"""
import argparse, json, os, re, shutil, subprocess, sys, time
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
OFFSET, GAP_FRASE, GAP_PAR, COLA = 4.0, 1.4, 1.0, 6.0   # segundos
UMBRAIS = {'dur_min_s': 180, 'dur_max_s': 300, 'wer_max': 0.25, 'desfase_av_max_s': 0.1,
           'pct_sincronia_min': 95.0, 'mb_max': 50, 'lt_max': 2, 'lufs': (-24, -18)}

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
        TEMPOS[self.nome] = {'parede_s': round(prev['parede_s'] + time.time() - self.t, 1),
                             'cpu_s': round(prev['cpu_s'] + cpu, 1)}


def partir(texto):
    frases, i = [], 0
    for pi, par in enumerate([p.strip() for p in texto.split('\n\n') if p.strip()]):
        for s in re.split(r'(?<=[.!?…])\s+', ' '.join(par.split())):
            if s.strip():
                i += 1; frases.append({'i': i, 'par': pi, 'texto': s.strip()})
    return frases


def srt(frases, tempos, out):
    def ts(x):
        h, r = divmod(x, 3600); m, s = divmod(r, 60)
        return f'{int(h):02d}:{int(m):02d}:{int(s):02d},{int(round((s % 1) * 1000)):03d}'.replace(',1000', ',999')
    lines, n = [], 0
    for f in frases:
        t0, t1 = tempos[f['i']]
        words = f['texto'].split(); parts, cur = [], []
        for w in words:
            if cur and len(' '.join(cur + [w])) > 84:
                parts.append(' '.join(cur)); cur = []
            cur.append(w)
        parts.append(' '.join(cur))
        tot = sum(len(p) for p in parts); acc = t0
        for p in parts:
            d = (t1 - t0) * len(p) / tot
            # dúas liñas de ata ~42 caracteres
            ws, l1 = p.split(), []
            while ws and len(' '.join(l1 + [ws[0]])) <= max(42, len(p) // 2 + 1):
                l1.append(ws.pop(0))
            txt = ' '.join(l1) + ('\n' + ' '.join(ws) if ws else '')
            n += 1; lines.append(f'{n}\n{ts(acc)} --> {ts(acc + d)}\n{txt}\n')
            acc += d
    Path(out).write_text('\n'.join(lines))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('tema'); ap.add_argument('--saida', required=True)
    ap.add_argument('--traballo', default=None); ap.add_argument('--queimar-subtitulos', action='store_true')
    ap.add_argument('--llm', default=os.environ.get('LLM_BACKEND', 'manual'), choices=['manual', 'openai'])
    a = ap.parse_args()
    tema = yaml.safe_load(open(a.tema))
    W = Path(a.traballo or f"{SCRATCH}/pipeline_work/{tema['id']}"); W.mkdir(parents=True, exist_ok=True)
    S = Path(a.saida); S.mkdir(parents=True, exist_ok=True)
    tp = W / 'tempos.json'
    if tp.exists():
        TEMPOS.update(json.loads(tp.read_text()))
    save_t = lambda: tp.write_text(json.dumps(TEMPOS, indent=1))
    info = {'tema': tema['id'], 'llm': {}}
    try:
        # 1-2 guion e corrección
        with Etapa('1_guion'):
            guion, meta = llm.complete('guion', a.llm, titulo=tema['titulo'], tema=tema['tema'],
                                       fragmento=tema['fragmento'], palabras=tema['palabras'],
                                       aviso=tema['aviso'], dossier=tema['dossier'].strip())
            info['llm']['guion'] = meta
        with Etapa('2_corrixir'):
            import qa
            lt1 = qa.lingua(guion, dossier=tema['dossier'])
            info['lt_antes'] = lt1
            if lt1:
                avisos = '\n'.join(f"- [{m['regra']}] {m['mensaxe']} | contexto: \"{m['contexto']}\" | "
                                   f"suxestións: {', '.join(m['suxestions']) or '-'}" for m in lt1)
                guion, meta = llm.complete('corrixir', a.llm, guion=guion, avisos=avisos)
                info['llm']['corrixir'] = meta
        (W / 'guion.txt').write_text(guion + '\n')
        frases = partir(guion)
        with Etapa('3_escenas'):
            numeradas = '\n'.join(f"{f['i']}. {f['texto']}" for f in frases)
            raw, meta = llm.complete('escenas', a.llm, titulo=tema['titulo'], frases=numeradas,
                                     n_escenas=tema.get('escenas', 16))
            info['llm']['escenas'] = meta
            escenas = json.loads(raw[raw.find('['): raw.rfind(']') + 1])
            vistas = [n for e in escenas for n in e['frases']]
            assert vistas == [f['i'] for f in frases], 'As escenas non cobren as frases en orde'
        save_t()
    except llm.PendingLLM as e:
        save_t(); print(e); sys.exit(3)

    # 4 voz
    escala = tema.get('escala', 1.25)
    with Etapa('4_voz'):
        import hashlib
        for f in frases:
            f['wav'] = f"{f['i']:03d}-{hashlib.sha256(f['texto'].encode()).hexdigest()[:8]}.wav"
        fj = W / 'frases.json'; fj.write_text(json.dumps(frases, ensure_ascii=False, indent=1))
        env = dict(os.environ, PATH=f"{CFG['st2_path']}:{os.environ['PATH']}", PYTHONPATH=CFG['st2_stubs'],
                   ST2_DIR=CFG['st2_dir'], REF_WAV=CFG['ref_wav'], SCALE=str(escala))
        vdir = W / f'voz_escala{escala}'
        subprocess.run([CFG['python_tts'], str(HERE / 'voz_st2.py'), str(fj), str(vdir)], env=env, check=True)
        sr = 24000; parts = []; tempos = {}; t = OFFSET
        for k, f in enumerate(frases):
            w, _ = sf.read(vdir / f['wav'])
            tempos[f['i']] = (round(t, 3), round(t + len(w) / sr, 3))
            parts.append(w); t += len(w) / sr
            if k + 1 < len(frases):
                g = GAP_FRASE + (GAP_PAR if frases[k + 1]['par'] != f['par'] else 0)
                parts.append(np.zeros(int(g * sr))); t += g
        voz = np.concatenate(parts).astype(np.float32)
        dur = OFFSET + len(voz) / sr + COLA
        srt(frases, tempos, W / 'subtitulos.srt')
        (W / 'tempos_frases.json').write_text(json.dumps(tempos, indent=1))
    save_t()

    # 5 imaxes
    with Etapa('5_imaxes'):
        import imaxes
        imgs, rex = imaxes.xerar(escenas, W / 'imaxes', seed_base=tema['id'])
        if rex:
            (W / 'imaxes' / 'rexistro.json').write_text(json.dumps(rex, ensure_ascii=False, indent=1))
        info['imaxes_xeracion_s'] = sum(x['s'] for x in rex)   # sen a carga do modelo
    save_t()

    # 6 son
    with Etapa('6_son'):
        import son
        info['son'] = son.mesturar(voz, dur, OFFSET, str(W / 'mestura.wav'), str(W / 'voz_linea.wav'))
    save_t()

    # 7 montaxe
    with Etapa('7_montaxe'):
        import montaxe
        esc_t = []
        for k, e in enumerate(escenas):
            b0 = 0.0 if k == 0 else tempos[e['frases'][0]][0] - 0.35
            esc_t.append({'b0': b0, 'movemento': e.get('movemento', 'zoom_in')})
        for k in range(len(esc_t)):
            esc_t[k]['b1'] = esc_t[k + 1]['b0'] if k + 1 < len(esc_t) else dur
        mp4 = S / 'ejemplo.mp4'
        montaxe.render(esc_t, imgs, dur, str(W / 'mestura.wav'), str(W / 'subtitulos.srt'), mp4, W / 'montaxe',
                       queimar=a.queimar_subtitulos)
        shutil.copy(W / 'subtitulos.srt', S / 'subtitulos.gl.srt')
    save_t()

    # 8 qa
    with Etapa('8_qa'):
        import qa
        res = {'umbrais': UMBRAIS, 'son': info['son'], 'llm': info['llm'],
               'imaxes_xeracion_s': info.get('imaxes_xeracion_s')}
        res['lingua_antes_correccion'] = info['lt_antes']
        res['lingua'] = qa.lingua(guion, dossier=tema['dossier'])
        res['estilo'] = qa.estilo(guion, frases, tema['aviso'], tema['palabras'])
        res['asr'] = qa.asr(str(W / 'mestura.wav'), str(W / 'voz_linea.wav'), frases, tempos, CFG['whisper_dir'])
        res['ficheiro'] = qa.ficheiro(mp4, dur)
        res['imaxes'] = qa.imaxes(imgs)
        res['escenas'] = [{'escena': k, 'frases': e['frases'], 'dur_s': round(t['b1'] - t['b0'], 1),
                           'movemento': t['movemento'], 'prompt': e['prompt']} for k, (e, t) in enumerate(zip(escenas, esc_t))]
        nw = res['estilo']['palabras']
        res['ritmo_palabras_min'] = round(nw / ((tempos[frases[-1]['i']][1] - OFFSET) / 60), 1)
        qa.folla_contactos(mp4, dur, S / 'contactsheet.jpg')
    TEMPOS['8_qa']['nota'] = 'inclúe a folla de contactos'
    save_t()
    res['tempos'] = TEMPOS
    f = res['ficheiro']
    res['portas'] = {
        'duracion': UMBRAIS['dur_min_s'] <= f['dur_video_s'] <= UMBRAIS['dur_max_s'],
        'wer_mestura': res['asr']['mestura']['wer'] <= UMBRAIS['wer_max'],
        'sincronia_av': f['desfase_av_s'] <= UMBRAIS['desfase_av_max_s'],
        'sincronia_subtitulos': res['asr']['mestura']['sincronia']['pct_dentro_da_sua_frase'] >= UMBRAIS['pct_sincronia_min'],
        'lingua_lt': len(res['lingua']) <= UMBRAIS['lt_max'],
        'estilo': not (res['estilo']['cifras'] or res['estilo']['signos_prohibidos'] or res['estilo']['palabras_vetadas'])
                  and res['estilo']['aviso_literal'] and res['estilo']['formula_literal'],
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
    L = [f"# QA automático: {tema['titulo']} ({tema['id']})", '',
         'Informe xerado por `herramientas/pipeline/pipeline.py` (etapa 8). Ningunha persoa revisou o vídeo.', '',
         f"**Veredicto automático: {'PUBLICABLE' if r['publicable'] else 'NON PUBLICABLE'}**", '',
         '| Porta | Resultado |', '|---|---|']
    L += [f'| {k} | {"pasa" if v else "FALLA"} |' for k, v in r['portas'].items()]
    L += ['', '## Ficheiro', '', '| Medida | Valor |', '|---|---|']
    L += [f'| {k} | {v} |' for k, v in f.items()]
    L += [f"| ritmo (palabras/min sobre a narración, pausas incluídas) | {r['ritmo_palabras_min']} |"]
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
          '## Lingua (LanguageTool 6.8 gl-ES, con hunspell galego)', '',
          f"Avisos antes da corrección automática: {len(r['lingua_antes_correccion'])}. Despois: {len(r['lingua'])}.", '']
    for m in r['lingua_antes_correccion']:
        L.append(f"- antes: `{m['regra']}` {m['mensaxe']} — \"{m['contexto']}\"")
    for m in r['lingua']:
        L.append(f"- despois: `{m['regra']}` {m['mensaxe']} — \"{m['contexto']}\"")
    L += ['', '## Estilo e densidade (regras do canal)', '', '| Control | Valor |', '|---|---|']
    L += [f'| {k} | {v} |' for k, v in e.items()]
    L += ['', '## Son', '', '| Medida | Valor |', '|---|---|'] + [f'| {k} | {v} |' for k, v in r['son'].items()]
    L += ['', '## Escenas e imaxes', '', '| # | Frases | Dur. (s) | Mov. | Lum. | Contr. | Simil. ant. | Prompt |', '|---|---|---|---|---|---|---|---|']
    for sc, im in zip(r['escenas'], r['imaxes']):
        L.append(f"| {sc['escena']} | {sc['frases'][0]}-{sc['frases'][-1]} | {sc['dur_s']} | {sc['movemento']} | "
                 f"{im['luminancia']} | {im['contraste']} | {im['similitude_coa_anterior']} | {sc['prompt']} |")
    L += ['', '## Tempos de render (CPU: 4 núcleos, sen GPU)', '', '| Etapa | Parede (s) | CPU (s) |', '|---|---|---|']
    L += [f"| {k} | {v['parede_s']} | {v['cpu_s']} |" for k, v in t.items()]
    L += [f'| **Total** | **{round(par, 1)}** | **{round(cpu, 1)}** |', '',
          f"Tempo total de CPU: {round(cpu / 3600, 2)} h de núcleo; parede: {round(par / 60, 1)} min. "
          'Non inclúe a descarga de modelos nin o tempo do LLM externo (ver LLM).', '']
    L += extrapolacion(r)
    L += [
          '## LLM', '', '| Etapa | Caché | Metadatos |', '|---|---|---|']
    for k, v in r['llm'].items():
        L.append(f"| {k} | `{v.get('cache')}` | {', '.join(f'{a}: {b}' for a, b in v.items() if a != 'cache')} |")
    L += ['', '## Guion final narrado', '', guion, '']
    return '\n'.join(L)


def extrapolacion(r, minutos=60, s_por_imaxe=15.0):
    """Extrapola linealmente os tempos medidos a un episodio longo [S: supón custo proporcional]."""
    t, f = r['tempos'], r['ficheiro']
    dur = f['dur_video_s']; n_img = len(r['escenas']); D = minutos * 60; n_d = D / s_por_imaxe
    g = lambda k: t.get(k, {'parede_s': 0, 'cpu_s': 0})
    fila = {  # etapa: (factor de escala, base)
        '4_voz': D / dur, '5_imaxes': n_d / n_img, '6_son': D / dur, '7_montaxe': D / dur, '8_qa': D / dur,
        '2_corrixir': D / dur}
    L = [f'## Extrapolación a un episodio de {minutos} min [S: escala lineal dos tempos medidos]', '',
         f'Supostos: mesma densidade de texto, unha imaxe cada {s_por_imaxe:.0f} s ({n_d:.0f} imaxes), '
         'custo de voz, montaxe e QA proporcional á duración (nas imaxes a carga do modelo cóntase unha vez), '
         'e LLM local non incluído.', '',
         '| Etapa | Parede (min) | CPU (h de núcleo) |', '|---|---|---|']
    tp = tc = 0
    for k, fac in fila.items():
        p, c = g(k)['parede_s'] * fac / 60, g(k)['cpu_s'] * fac / 3600
        xs = r.get('imaxes_xeracion_s')
        if k == '5_imaxes' and xs:   # a carga do modelo paga unha vez; só a xeración escala
            par = g(k)['parede_s']; p60 = (par - xs) + xs * fac
            p, c = p60 / 60, g(k)['cpu_s'] * p60 / par / 3600
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
