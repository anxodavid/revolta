#!/usr/bin/env python
"""Prueba mínima del entorno local del pipeline (una por etapa) con tiempos. La lanza `instalar.sh verificar`.

    source herramientas/pipeline/entorno.sh
    $PY herramientas/pipeline/probas/proba_entorno.py [--solo voz,imaxe,qa,montaxe]

1. voz      voz_st2.py narra 2 frases en galego con el mismo env que pone pipeline.py (PATH con pathbin, PYTHONPATH con
            stubs, ST2_DIR, REF_WAV); factor de tiempo real (RTF = segundos de cálculo / segundos de audio).
2. imaxe    SDXL-Turbo 1024x576, 4 pasos (como imaxes.py): dos imágenes (la 1.ª incluye el calentamiento) y
            `python revisor.py` sobre las dos (la 1.ª línea incluye cargar MediaPipe y Florence-2).
3. qa       faster-whisper + Whisper galego (CTranslate2 int8) sobre el audio de la prueba 1 (WER); LanguageTool gl-ES
            (qa.lingua) sobre una frase con un error de concordancia; NLI (veracidade.Verificador.nli) con dos pares.
4. montaxe  son.mesturar (voz + lluvia) y montaxe.render de 2 planos de 4 s; el MP4 se valida decodificándolo entero.

Cada prueba pesada toma el candado común de CPU ($CPU_LOCK, el mismo que `flock`); el tiempo de espera no cuenta.
Salida: $SCRATCH/proba_entorno/ (WAV, PNG, MP4) y resultado.json. Todo es automático; nada se revisa a mano.
"""
import argparse, contextlib, fcntl, json, os, re, subprocess, sys, time
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent          # herramientas/pipeline
sys.path.insert(0, str(HERE))
S = Path(os.environ['SCRATCH'])
OUT = S / 'proba_entorno'
OUT.mkdir(parents=True, exist_ok=True)
LOCK = os.environ.get('CPU_LOCK', str(S / 'cpu.lock'))
FRASES = ["Nas noites de inverno, a xente reuníase ao carón da lareira para escoitar vellas historias.",
          "Contan que polos camiños da aldea pasaba, en silencio, a Santa Compaña."]
RES = {}


@contextlib.contextmanager
def candado(nome):
    """Toma $CPU_LOCK (flock exclusivo, compatible con la orden flock) y mide tiempo de pared y de CPU sin la espera."""
    t = time.time()
    with open(LOCK, 'a') as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        espera = time.time() - t
        if espera > 1:
            print(f'   ({nome}: {espera:.0f} s esperando el candado de CPU)', flush=True)
        t0, c0 = time.time(), os.times()
        m = {}
        try:
            yield m
        finally:
            c1 = os.times()
            m['parede_s'] = round(time.time() - t0, 1)
            m['cpu_s'] = round(sum(getattr(c1, k) - getattr(c0, k) for k in
                                   ('user', 'system', 'children_user', 'children_system')), 1)
            fcntl.flock(f, fcntl.LOCK_UN)


def proba_voz():
    import numpy as np, soundfile as sf
    import pipeline as P
    vdir = OUT / 'voz'
    for w in vdir.glob('*.wav'):
        w.unlink()
    vdir.mkdir(exist_ok=True)
    fj = OUT / 'frases.json'
    fj.write_text(json.dumps([{'i': i + 1, 'texto': t, 'wav': f'{i + 1:03d}.wav', 'escala': 1.1}
                              for i, t in enumerate(FRASES)], ensure_ascii=False))
    env = dict(os.environ, PATH=f"{P.CFG['st2_path']}:{os.environ['PATH']}", PYTHONPATH=P.CFG['st2_stubs'],
               ST2_DIR=P.CFG['st2_dir'], REF_WAV=P.CFG['ref_wav'], SCALE='1.1')
    marcas = []
    with candado('voz') as m:
        t0 = time.time()
        p = subprocess.Popen([P.CFG['python_tts'], str(HERE / 'voz_st2.py'), str(fj), str(vdir)], env=env,
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        log = []
        for linea in p.stdout:
            log.append(linea.rstrip())
            if linea.startswith('voz '):
                marcas.append(time.time() - t0); print('  ', linea.rstrip(), flush=True)
        p.wait()
    if p.returncode:
        print('\n'.join(log[-30:])); raise SystemExit('voz_st2.py fallou')
    durs = [sf.info(str(vdir / f'{i + 1:03d}.wav')).duration for i in range(len(FRASES))]
    # la 1.ª marca incluye cargar el modelo; el RTF limpio es el de la 2.ª frase
    m.update({'audio_s': [round(d, 2) for d in durs], 'marcas_s': [round(x, 1) for x in marcas],
              'carga_mais_frase1_s': round(marcas[0], 1),
              'rtf_frase2': round((marcas[1] - marcas[0]) / durs[1], 3),
              'rtf_total_con_carga': round(m['parede_s'] / sum(durs), 3)})
    # audio de las dos frases seguido (para el ASR y el montaje), 24 kHz mono
    a = np.concatenate([np.concatenate([sf.read(str(vdir / f'{i + 1:03d}.wav'))[0], np.zeros(int(24000 * 0.6))])
                        for i in range(len(FRASES))])
    sf.write(str(OUT / 'voz.wav'), a.astype(np.float32), 24000)
    return m


def proba_imaxe():
    import torch
    import imaxes
    torch.set_num_threads(int(os.environ.get('NTH', '4')))
    prompt = imaxes.ESTILO.format(p='a granite hórreo beside a stone house with a slate roof, oak trees, Galicia')
    with candado('imaxe') as m:
        from diffusers import AutoPipelineForText2Image
        t = time.time()
        pipe = AutoPipelineForText2Image.from_pretrained(imaxes.MODELO, torch_dtype=torch.bfloat16, variant='fp16')
        pipe.set_progress_bar_config(disable=True)
        m['carga_s'] = round(time.time() - t, 1)
        m['xeracion_s'] = []
        for k, (nome, semente) in enumerate((('imaxe.png', 1), ('imaxe2.png', 2))):
            t = time.time()
            im = pipe(prompt=prompt, width=imaxes.W, height=imaxes.H, num_inference_steps=imaxes.PASOS,
                      guidance_scale=0.0, generator=torch.Generator().manual_seed(semente)).images[0]
            m['xeracion_s'].append(round(time.time() - t, 1))
            im.save(OUT / nome)
        m['tamaño'] = list(im.size)
        del pipe
    marcas, linas = [], []
    with candado('revisor') as r:
        t0 = time.time()
        p = subprocess.Popen([sys.executable, str(HERE / 'revisor.py'), str(OUT / 'imaxe.png'), str(OUT / 'imaxe2.png')],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        for linea in p.stdout:
            if linea.startswith('{'):
                marcas.append(round(time.time() - t0, 1)); linas.append(json.loads(linea))
        err = p.stderr.read(); p.wait()
    if p.returncode or len(linas) < 2:
        print(err[-3000:]); raise SystemExit('revisor.py fallou')
    m['revisor'] = {'parede_s': r['parede_s'], 'cpu_s': r['cpu_s'], 'carga_mais_imaxe1_s': marcas[0],
                    'imaxe2_s': round(marcas[1] - marcas[0], 1),
                    'resultados': [{'ok': rv['ok'], 'problemas': rv['problemas'], 'mans': len(rv.get('mans', [])),
                                    'corpos': rv.get('corpos'), 'descricion': rv.get('descricion', '')[:240]}
                                   for rv in linas]}
    return m


def proba_qa():
    import jiwer, qa
    from faster_whisper import WhisperModel
    res = {}
    with candado('asr') as m:
        t = time.time()
        w = WhisperModel(os.environ['WHISPER_DIR'], device='cpu', compute_type='int8', cpu_threads=4)
        m['carga_s'] = round(time.time() - t, 1)
        segs, _ = w.transcribe(str(OUT / 'voz.wav'), language='gl', beam_size=5, condition_on_previous_text=False)
        hip = ' '.join(s.text for s in segs).strip()
        ref = ' '.join(FRASES)
        m.update({'wer': round(jiwer.wer(qa.norm(ref), qa.norm(hip)), 3), 'hipotese': hip})
        del w
    res['asr'] = m
    with candado('languagetool') as m:
        avisos = qa.lingua('Os rapaces foi á praia.')
        m['avisos'] = [(a['regra'], a['palabra']) for a in avisos]
        m['detecta_concordancia'] = bool(avisos)
        qa.pechar_lt()
    res['languagetool'] = m
    with candado('nli') as m:
        import veracidade
        v = veracidade.Verificador([])
        pares = [('A irmandade foi derrotada no ano mil catrocentos sesenta e nove.', 'A irmandade perdeu a guerra.'),
                 ('Os irmandiños derrubaron moitas fortalezas.', 'Os irmandiños non derrubaron ningunha fortaleza.')]
        m['pares'] = [{'premisa': a, 'hipotese': b, **v.nli(a, b)} for a, b in pares]
    res['nli'] = m
    return res


def proba_montaxe():
    import numpy as np, soundfile as sf
    from PIL import Image, ImageOps
    import montaxe, son, qa
    img2 = OUT / 'imaxe_espello.png'
    ImageOps.mirror(Image.open(OUT / 'imaxe.png')).save(img2)
    dur = 8.0
    voz, sr = sf.read(str(OUT / 'voz.wav'))
    srt = OUT / 'proba.srt'
    srt.write_text('1\n00:00:00,500 --> 00:00:04,000\n' + FRASES[0] + '\n\n2\n00:00:04,000 --> 00:00:07,800\n'
                   + FRASES[1] + '\n', encoding='utf-8')
    mp4, tmp = OUT / 'proba.mp4', OUT / 'proba.tmp.mp4'
    with candado('montaxe') as m:
        m['son'] = son.mesturar(voz[:int(sr * (dur - 0.5))].astype(np.float32), dur, 0.5, str(OUT / 'mestura.wav'),
                                str(OUT / 'voz_linea.wav'))
        escenas = [{'b0': 0.0, 'b1': 4.0, 'movemento': 'zoom_in'}, {'b0': 4.0, 'b1': dur, 'movemento': 'pan_left'}]
        montaxe.render(escenas, [str(OUT / 'imaxe.png'), str(img2)], dur, str(OUT / 'mestura.wav'), str(srt),
                       str(tmp), OUT / 'montaxe_traballo', procs=4)
        os.replace(tmp, mp4)          # escritura atómica
    p = subprocess.run([qa.FFMPEG, '-v', 'error', '-i', str(mp4), '-f', 'null', '-'], capture_output=True, text=True)
    info = subprocess.run([qa.FFMPEG, '-i', str(mp4)], capture_output=True, text=True).stderr
    d = re.search(r'Duration: (\d+):(\d+):([\d.]+)', info)
    m.update({'decodifica_sen_erros': p.returncode == 0 and not p.stderr.strip(), 'erros_ffmpeg': p.stderr[-500:],
              'duracion_s': round(int(d[1]) * 3600 + int(d[2]) * 60 + float(d[3]), 2) if d else None,
              'mb': round(mp4.stat().st_size / 1e6, 2),
              'pistas': re.findall(r'Stream #0:\d+.*?: (Video: \w+[^,]*|Audio: \w+|Subtitle: \w+)', info),
              'resolucion': (re.search(r'(\d{3,4}x\d{3,4})', info) or [None])[0]})
    return m


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--solo', default='voz,imaxe,qa,montaxe')
    a = ap.parse_args()
    orde = [x for x in ('voz', 'imaxe', 'qa', 'montaxe') if x in a.solo.split(',')]
    previo = OUT / 'resultado.json'
    if previo.exists():
        RES.update(json.loads(previo.read_text()))
    for k in orde:
        print(f'== {k}', flush=True)
        t = time.time()
        RES[k] = globals()[f'proba_{k}']()
        print(f'   {k}: {time.time() - t:.0f} s', json.dumps(RES[k], ensure_ascii=False)[:1500], flush=True)
        previo.write_text(json.dumps(RES, ensure_ascii=False, indent=1))
    print('resultado en', previo)
