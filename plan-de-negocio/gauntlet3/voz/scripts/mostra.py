#!/usr/bin/env python
"""Mostra de escoita para o promotor (peza VOZ, Gauntlet 3): mostra-embude.m4a (AAC, mono).

    source herramientas/pipeline/entorno.sh
    PATH=$COTOVIA_NOVA_PATHBIN:$PATH PYTHONPATH=$ST2_STUBS:$SCRATCH/voz/pylib flock "$CPU_LOCK" \
        $PY plan-de-negocio/gauntlet3/voz/scripts/mostra.py SAIDA.m4a [--curva CANDIDATA.json]

1. As mesmas 3 frases en ton de gancho (palabra 0 da curva) e despois en ton de durmir (palabra 3600).
2. O embude enteiro en ~80 s: 11 frases, cada unha no seu punto da curva (de 0 a 3600 palabras), coas pausas e a
   ganancia de curva.py (ou da candidata --curva, co formato de puntos.py), como as montaría longo.py.
Voz seca, sen choiva (para escoitar a voz). Escritura atómica e validación con ffmpeg. Ninguén a escoitou antes de
subila: as medidas son automáticas.
"""
import json, os, subprocess, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI); sys.path.insert(0, '/home/user/revolta/herramientas/pipeline')
import numpy as np, soundfile as sf
import imageio_ffmpeg
import curva, textos, puntos

SR = 24000
VOZ_KW = ('escala', 'estilo', 'f0_media', 'f0_rango', 'enerxia', 'alpha', 'beta', 'embedding_scale', 'pasos')
PARTE1 = [textos.PASAXE_MEIGAS[0], textos.PASAXE_MEIGAS[2], textos.PASAXE_MEIGAS[4]]
# (palabra da curva, frase, novo parágrafo antes). Tema elixido: "As meigas de verdade" (tema/investigacion.md).
EMBUDE = [
    (0, 'Seguramente oíches o conxuro da queimada e pensas que é moi antigo.', False),
    (40, 'Non o é: escribiuno en Vigo, en mil novecentos sesenta e sete, Mariano Marcos Abalo.', False),
    (90, 'E en Vilalba, en mil seiscentos dezasete, unha testemuña declarou que unha parteira dicía poder pasarlle a un '
         'home as dores do parto.', False),
    (150, 'Isto é Cousas de Galiza para durmir.', True),
    (280, 'Esta noite imos buscar as meigas de verdade, as que deixaron o seu nome nos papeis.', True),
    (500, 'A meiga dos papeis non era a bruxa dos contos, senón a curandeira, a parteira, a muller que sabía de herbas.', False),
    (950, 'Nas casas de pedra, arredor da lareira, as avoas falaban das herbas, do leite e do mal de ollo.', True),
    (1400, 'Contan que na noite de San Xoán as mozas ían á fonte antes de que saíse o sol.', False),
    (1800, 'Levaban herbas, auga e palabras moi antigas.', True),
    (2700, 'Fóra, a choiva caía amodo sobre os tellados de lousa.', False),
    (3600, 'Chove na lousa, amodo, e a historia pode esperar ata mañá.', False),
]


def voz(V, texto, pal, cv):
    c = puntos.en(pal, cv)
    w, _ = V.infer(texto, **{k: c[k] for k in VOZ_KW if k in c})
    return w * 10 ** (c['ganancia_db'] / 20), c


def main():
    import argparse
    ap = argparse.ArgumentParser(); ap.add_argument('saida'); ap.add_argument('--curva', default=None)
    a = ap.parse_args()
    saida = os.path.abspath(a.saida)
    cv = puntos.curva_candidata(a.curva)
    os.environ.update(puntos.refs_de(cv))
    import voz_st2 as V
    V.cargar()
    sil = lambda s: np.zeros(int(s * SR))
    partes, marcas, t = [sil(0.5)], [], 0.5
    for nome, pal in (('gancho', 0), ('durmir', 3600)):
        marcas.append((nome, round(t, 1)))
        for k, tx in enumerate(PARTE1):
            w, c = voz(V, tx, pal, cv)
            partes += [w, sil(c['pausa_frase'] + 0.3)]; t += len(w) / SR + c['pausa_frase'] + 0.3
        partes.append(sil(1.5)); t += 1.5
    marcas.append(('embude', round(t, 1)))
    for k, (pal, tx, par) in enumerate(EMBUDE):
        w, c = voz(V, tx, pal, cv)
        partes.append(w); t += len(w) / SR
        if k + 1 < len(EMBUDE):
            seg = EMBUDE[k + 1]
            g = c['pausa_frase'] + min(0.3, max(-0.15, 0.02 * (len(seg[1].split()) - 14)))
            g += c['pausa_parrafo'] if seg[2] else 0
            g += 0.6 if tx.startswith('Isto é Cousas') else 0
            partes.append(sil(g)); t += g
    partes.append(sil(1.0)); t += 1.0
    x = np.concatenate(partes).astype(np.float32)
    # normalización simple de pico a -3 dBFS (a mestura real normaliza a -17 LUFS en longo.py/son.py)
    x *= 10 ** (-3 / 20) / max(1e-6, float(np.abs(x).max()))
    wav = saida + '.tmp.wav'; tmp = saida + '.tmp.m4a'
    sf.write(wav, x, SR)
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    subprocess.run([ff, '-y', '-v', 'error', '-i', wav, '-ac', '1', '-ar', '24000', '-c:a', 'aac', '-b:a', '96k',
                    '-movflags', '+faststart', tmp], check=True)
    p = subprocess.run([ff, '-v', 'error', '-i', tmp, '-f', 'null', '-'], capture_output=True, text=True)
    if p.returncode or p.stderr.strip():
        raise SystemExit(f'm4a con erros: {p.stderr[:300]}')
    os.replace(tmp, saida); os.remove(wav)
    json.dump({'duracion_s': round(len(x) / SR, 1), 'marcas_s': marcas, 'curva': a.curva or 'curva.py',
               'ref_wav': os.environ.get('REF_WAV'), 'ref_wav_calmo': os.environ.get('REF_WAV_CALMO'),
               'embude': [{'pal': pal, 'texto': tx} for pal, tx, _ in EMBUDE], 'parte1': PARTE1},
              open(saida.replace('.m4a', '.json'), 'w'), ensure_ascii=False, indent=1)
    print('mostra', saida, round(len(x) / SR, 1), 's', marcas, round(os.path.getsize(saida) / 1e6, 2), 'MB')


if __name__ == '__main__':
    main()
