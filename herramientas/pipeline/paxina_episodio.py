"""Páxina privada para ver un episodio longo: reprodutor HLS 720p, capítulos, faixa do embude, portas de QA,
descrición para YouTube e folla de contactos.

    python paxina_episodio.py DIR_SAIDA TEMA.yaml DIR_HLS DIR_PAXINA [--etiqueta "episodio piloto · borrador"]

Le DIR_SAIDA/{qa.json,descricion.txt,contactsheet.jpg,video.mp4} (saída de longo.py), o tema e a copia HLS de
entregar.sh, e escribe en DIR_PAXINA: index.html (plantilla paxina_episodio.html cos datos dentro), poster.jpg,
contactsheet.jpg e hls/ (ligazón á copia HLS: init.mp4, fNNN.mp4 e lista.txt). As rutas son as que a páxina pide,
para publicalas tal cal; os subtítulos (subtitulos.gl.vtt da copia HLS) van dentro da páxina.
Toda a páxina vai en galego normativo (decisión do promotor do 01-10-2026).
"""
import argparse
import json
import os
import shutil
import subprocess
from datetime import date
from pathlib import Path

import imageio_ffmpeg
import yaml

AQUI = Path(__file__).resolve().parent
NOMES_PORTAS = {
    'autoria_declarada': 'autoría declarada', 'duracion': 'duración', 'wer_mestura': 'enténdese (ASR)',
    'sincronia_av': 'sincronía son-vídeo', 'sincronia_subtitulos': 'sincronía dos subtítulos',
    'lingua_lt': 'lingua (LanguageTool)', 'h1_ancoraxe': 'ancoraxe do gancho', 'veracidade': 'veracidade',
    'estilo': 'estilo', 'imaxes_revisadas': 'imaxes aprobadas', 'sonoridade': 'sonoridade', 'bitrate': 'taxa de bits',
    'resolucion': 'resolución 1080p'}
FASES = ('gancho', 'transicion', 'calma', 'durmir')


def coma(x, d=1):
    """Número coa coma decimal do galego."""
    return f'{x:.{d}f}'.replace('.', ',')


def romano(n):
    try:
        n = int(n)
    except (TypeError, ValueError):
        return str(n or '')
    out = ''
    for v, s in ((10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')):
        while n >= v:
            out += s; n -= v
    return out


def hms(s):
    s = int(round(s)); return f'{s // 3600}:{s % 3600 // 60:02d}:{s % 60:02d}' if s >= 3600 else f'{s // 60}:{s % 60:02d}'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('saida'); ap.add_argument('tema'); ap.add_argument('hls'); ap.add_argument('paxina')
    ap.add_argument('--etiqueta', default='episodio piloto · borrador sen publicar')
    ap.add_argument('--video', default=None, help='mestre (por defecto DIR_SAIDA/video.mp4; longo.py déixao en TRABALLO/video.mp4)')
    a = ap.parse_args()
    S, P = Path(a.saida), Path(a.paxina)
    P.mkdir(parents=True, exist_ok=True)
    qa = json.loads((S / 'qa.json').read_text())
    tema = yaml.safe_load(Path(a.tema).read_text())
    f = qa['ficheiro']; dur = float(f['dur_video_s'])

    caps = [{'t': 0.0, 'n': '', 'titulo': tema.get('capitulo_inicial', 'Comezo')}]
    caps += [{'t': round(float(c['t0']), 1), 'n': romano(c.get('num')), 'titulo': c['titulo']} for c in qa['capitulos']]

    fases = []
    for fase in FASES:
        pl = [e for e in qa['escenas'] if e['fase'] == fase]
        if pl:
            fases.append({'fase': fase, 't0': min(e['b0'] for e in pl), 't1': max(e['b0'] + e['dur_s'] for e in pl)})
    if fases:
        fases[0]['t0'] = 0.0; fases[-1]['t1'] = dur
        for x, y in zip(fases, fases[1:]):
            x['t1'] = y['t0']

    au = tema.get('autoria') or {}
    quen = [['Guion', au.get('guion', '(sen declarar)')],
            ['Dosier de fontes', au.get('dossier', '(sen declarar)')],
            ['Indicacións (prompts) das imaxes', au.get('escenas', '(sen declarar)')],
            ['Automático e local', au.get('automatico', '')],
            ['Revisión humana', 'ningunha polo momento: ninguén viu o vídeo enteiro antes desta páxina.']]

    rex = qa.get('revision_imaxes') or []
    intentos = [len(r.get('intentos', [])) for r in rex]
    a_ = qa['asr']['mestura']
    medidas = [
        ['Duración', f"{hms(dur)} ({len(qa['escenas'])} planos)"],
        ['Formato', f"{f['resolucion']} a {coma(f['fps'], 0)} fps, {coma(f['mb'])} MB, {f['kbps']} kb/s (aquí, copia de 720p)"],
        ['Sonoridade', f"{coma(f['lufs_integrado'])} LUFS integrados, pico real {coma(f['pico_real_dbtp'])} dBTP"],
        ['Intelixibilidade', f"WER {coma(a_['wer'], 3)} (Whisper frase a frase, sobre a mestura co ambiente)"],
        ['Ritmo por fase', ' → '.join(f"{v:.0f}" for v in qa['ritmo_palabras_min_por_fase'].values()) + ' palabras/min'],
        ['Duración media do plano', ' → '.join(f'{v:.0f} s' for v in qa['duracion_media_plano_por_fase_s'].values())],
    ]
    if rex:
        medidas.append(['Imaxes', f"{sum(r['ok'] for r in rex)}/{len(rex)} aprobadas pola porta automática, "
                                  f"{coma(sum(intentos) / len(intentos))} intentos de media"])
    cpu = sum(v.get('cpu_s', 0) for v in (qa.get('tempos') or {}).values())
    if cpu:
        medidas.append(['Cálculo', f'{coma(cpu / 3600)} h de CPU (4 núcleos, sen GPU)'])

    datos = {
        'id': tema['id'], 'serie': 'Cousas de Galiza para durmir', 'etiqueta': a.etiqueta, 'titulo': tema['titulo'],
        'meta': f"galego · voz sintética · xerado o {date.today().strftime('%d-%m-%Y')}",
        'duracion_s': dur, 'capitulos': caps, 'fases': fases, 'ritmo': qa['ritmo_palabras_min_por_fase'],
        'quen': quen, 'portas': qa['portas'], 'nomes_portas': NOMES_PORTAS, 'publicable': qa['publicable'],
        'medidas': medidas, 'descricion': (S / 'descricion.txt').read_text(),
        'vtt': (Path(a.hls) / 'subtitulos.gl.vtt').read_text() if (Path(a.hls) / 'subtitulos.gl.vtt').exists() else '',
        'pe': ['Páxina privada de traballo do Gauntlet 3. O vídeo non está publicado en ningunha canle.',
               f"Esta copia é de 720p para vela aquí; o orixinal é de {f['resolucion']} ({f['mb']:.0f} MB)."] + tema.get('creditos', []),
    }
    html = (AQUI / 'paxina_episodio.html').read_text()
    js = json.dumps(datos, ensure_ascii=False).replace('</', '<\\/')
    (P / 'index.html').write_text(html.replace('__TITULO__', tema['titulo']).replace('__DATOS__', js))

    shutil.copy(S / 'contactsheet.jpg', P / 'contactsheet.jpg')
    t_cartel = next((r['t0'] + 2.5 for r in qa.get('rotulos', []) if r.get('texto') == tema['titulo']), 50.0)
    subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), '-v', 'error', '-y', '-ss', str(t_cartel), '-i', str(a.video or S / 'video.mp4'),
                    '-frames:v', '1', '-vf', 'scale=1280:720', '-q:v', '4', str(P / 'poster.jpg')], check=True)
    h = P / 'hls'
    if h.is_symlink() or h.exists():
        h.unlink() if h.is_symlink() else shutil.rmtree(h)
    os.symlink(Path(a.hls).resolve(), h)
    print(P / 'index.html', f"{len(caps)} capítulos, {len(fases)} fases, publicable={qa['publicable']}")


if __name__ == '__main__':
    main()
