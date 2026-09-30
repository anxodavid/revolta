#!/usr/bin/env python
"""Mostra de escoita para o promotor (peza VOZ, Gauntlet 3): mostra-embude.m4a (AAC, mono).

    source herramientas/pipeline/entorno.sh
    PATH=$COTOVIA_NOVA_PATHBIN:$PATH PYTHONPATH=$ST2_STUBS:$SCRATCH/voz/pylib flock "$CPU_LOCK" \
        $PY plan-de-negocio/gauntlet3/voz/scripts/mostra.py SAIDA.m4a

1. As mesmas 3 frases en ton de gancho (palabra 0 da curva) e despois en ton de durmir (palabra 3600).
2. O embude enteiro en ~80 s: 11 frases, cada unha no seu punto da curva (de 0 a 3600 palabras), coas pausas e a
   ganancia de curva.py, como as montaría longo.py.
Voz seca, sen choiva (para escoitar a voz). Escritura atómica e validación con ffmpeg. Ninguén a escoitou antes de
subila: as medidas son automáticas.
"""
import json, os, subprocess, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI); sys.path.insert(0, '/home/user/revolta/herramientas/pipeline')
import numpy as np, soundfile as sf
import imageio_ffmpeg
import curva, textos

SR = 24000
VOZ_KW = ('escala', 'estilo', 'f0_media', 'f0_rango', 'enerxia', 'alpha', 'beta', 'embedding_scale', 'pasos')
PARTE1 = [textos.PASAXE[0], textos.PASAXE[1], textos.PASAXE[5]]
# (palabra da curva, frase, novo parágrafo antes)
EMBUDE = [
    (0, 'Hai unha procesión que ninguén quere atopar, e aínda así, moita xente di que a viu.', False),
    (60, 'Pasa de noite, en silencio, e din que quen a atopa pode acabar camiñando con ela.', False),
    (130, 'Isto é Cousas de Galiza para durmir.', False),
    (280, 'Esta noite imos camiñar amodo por unha das lendas máis vellas do país: a Santa Compaña.', True),
    (500, 'Contan os vellos que, nas noites de néboa, unha procesión de ánimas percorre os camiños das aldeas.', False),
    (750, 'Diante vai sempre un vivo cunha cruz na man, e non pode soltala ata que atopa outra persoa que a leve.', False),
    (950, 'Non había casa sen lareira, nin lareira sen historias.', True),
    (1400, 'Mentres fóra chovía sobre os tellados de lousa, as avoas falaban das meigas e dos mortos.', False),
    (1800, 'Os nenos escoitaban co corpo quedo e os ollos pechados, ata que o sono os levaba amodo.', True),
    (2700, 'E así, noite tras noite, a memoria da terra pasaba dunha voz a outra, coma unha auga mansa.', False),
    (3600, 'A chuvia segue a caer, lenta, sobre os tellados.', False),
]


def voz(V, texto, pal):
    c = curva.en(pal, 3600)
    w, _ = V.infer(texto, **{k: c[k] for k in VOZ_KW if k in c})
    return w * 10 ** (c['ganancia_db'] / 20), c


def main():
    saida = os.path.abspath(sys.argv[1])
    import voz_st2 as V
    V.cargar()
    sil = lambda s: np.zeros(int(s * SR))
    partes, marcas, t = [sil(0.5)], [], 0.5
    for nome, pal in (('gancho', 0), ('durmir', 3600)):
        marcas.append((nome, round(t, 1)))
        for k, tx in enumerate(PARTE1):
            w, c = voz(V, tx, pal)
            partes += [w, sil(c['pausa_frase'] + 0.3)]; t += len(w) / SR + c['pausa_frase'] + 0.3
        partes.append(sil(1.5)); t += 1.5
    marcas.append(('embude', round(t, 1)))
    for k, (pal, tx, par) in enumerate(EMBUDE):
        w, c = voz(V, tx, pal)
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
    json.dump({'duracion_s': round(len(x) / SR, 1), 'marcas_s': marcas,
               'embude': [{'pal': pal, 'texto': tx} for pal, tx, _ in EMBUDE], 'parte1': PARTE1},
              open(saida.replace('.m4a', '.json'), 'w'), ensure_ascii=False, indent=1)
    print('mostra', saida, round(len(x) / SR, 1), 's', marcas, round(os.path.getsize(saida) / 1e6, 2), 'MB')


if __name__ == '__main__':
    main()
