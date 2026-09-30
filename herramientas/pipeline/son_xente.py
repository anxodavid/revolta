#!/usr/bin/env python
"""Banco de voces para o murmullo de xente (son.py, tipo `xente`): frases de conversa cotiá en galego narradas coa
nosa propia voz sintética (Nos_StyleTTS2-Brais-GL, voz_st2.py), con ton, tempo e entoación distintos en cada frase.

    source herramientas/pipeline/entorno.sh
    PATH=$ST2_PATHBIN:$PATH PYTHONPATH=$ST2_STUBS flock "$CPU_LOCK" $PY herramientas/pipeline/son_xente.py [DIR_WAV]

Escribe son_datos/xente-banco.ogg (mono, 16 kHz, Vorbis) e son_datos/xente-banco.json (onde empeza e acaba cada
frase). son.xente() colle deste banco 6-12 "voces" (cada unha coa súa altura e timbre, por remostraxe), superpóñeas
con pausas ao chou, pásaas por un paso baixo e unha reverberación e así ningunha palabra se entende.

Os textos escribiunos Claude (axente de son): conversa de feira ou de xuntanza, sen datos nin nomes de persoas reais.
Todas as voces saen de Brais (voz masculina): as máis agudas (voces "de muller" ou de rapaz) fanse en son.py subindo
ton e formantes por remostraxe. Non se instalaron as voces VITS de Nós (Celtia, Sabela, Icía): ver
gauntlet3/aprendizajes/son.md. Semente fixa: o banco sae igual cada vez. ~2 min de CPU (4 núcleos).
"""
import json, os, sys
from pathlib import Path
import numpy as np, soundfile as sf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
DATOS = HERE / 'son_datos'
SR_BANCO = 16000

FRASES_XENTE = [
    'Este ano as castañas viñeron cedo e son ben grandes.',
    'Mira que caro está o millo, non hai quen o compre.',
    'Onte estiven na casa da túa tía e deume uns ovos.',
    'Á tarde imos baixar ao muíño, se non chove.',
    'A vaca marela xa pariu, e o becerro está san.',
    'Non sei se chegaremos a tempo á misa das doce.',
    'Tráeme o cesto das mazás, que pesa moito.',
    'Canto pides por ese porco? É moito, home, é moito.',
    'Ai, muller, que ben estás, parece que non pasan os anos por ti.',
    'O señor cura vai falar despois da procesión.',
    'Aquí hai viño e pan para todos, collede sen medo.',
    'Mañá cedo hai que ir segar o prado de abaixo.',
    'Xa che dixen que o gando non entra na horta.',
    'Onde deixaches a chave do hórreo, rapaz?',
    'A min contáronmo na fonte, e eu non digo nada.',
    'Este inverno foi moi longo e choveu moito.',
    'Os rapaces andan xogando na eira desde a mañá.',
    'Veña, sentade aquí, que hai sitio para todos.',
    'Que bo está este caldo, parece o da miña avoa.',
    'Hai que levar o trigo ao muíño antes do sábado.',
    'O tratante quería pagar pouco polo xato, pero non llo dei.',
    'Se vés á festa, trae a gaita, que hai baile.',
    'A miña nai sempre dicía que a lúa nova trae choiva.',
    'Levaba tres días sen saír da casa co catarro.',
    'Pois eu vin a túa curmá na feira o outro día.',
    'Isto non se fai así, hai que ter paciencia.',
    'Deume o recado para ti, pero esquecinme del.',
    'Vai frío, pero o sol xa quenta un pouco.',
    'Compramos unha manta de la para o inverno.',
    'Moi boas, como vai iso? Ben, grazas, e vós?',
    'O viño deste ano saíu mellor ca o do ano pasado.',
    'Díxenlle que non, e el marchou todo enfadado.',
    'Temos que arranxar o tellado antes de que veñan as choivas.',
    'Pasade, pasade, que aínda queda polbo na pota.',
    'E logo, que tal a colleita das patacas?',
    'Ata a semana que vén, se Deus quere.',
]


def parametros(i, refs):
    """Ton, tempo, entoación e referencia de estilo de cada frase (semente fixa)."""
    r = np.random.default_rng(1000 + i)
    return {'escala': round(float(r.uniform(0.85, 1.15)), 3), 'f0_media': round(float(r.uniform(0.88, 1.12)), 3),
            'f0_rango': round(float(r.uniform(0.9, 1.4)), 3), 'semente': 5000 + i,
            'ref': refs[int(r.integers(0, len(refs)))] if refs else None}


def recortar(w, sr, umbral_db=-45.0):
    """Quita o silencio do principio e do final (deixa 40 ms)."""
    fr = int(0.02 * sr)
    e = np.array([np.sqrt(np.mean(w[k:k + fr] ** 2) + 1e-12) for k in range(0, max(1, len(w) - fr), fr)])
    on = np.where(20 * np.log10(e / (e.max() + 1e-12)) > umbral_db)[0]
    if not len(on):
        return w
    a, b = max(0, on[0] * fr - int(0.04 * sr)), min(len(w), (on[-1] + 1) * fr + int(0.04 * sr))
    return w[a:b]


def main(dir_wav):
    import voz_st2 as V
    from scipy import signal
    dir_wav = Path(dir_wav).resolve(); dir_wav.mkdir(parents=True, exist_ok=True)
    rd = os.environ.get('REFS_DIR')
    # referencias de estilo: exclamacións e preguntas do corpus (prosodia de conversa); se non hai, REF_WAV
    refs = []
    if rd and Path(rd, 'refs.tsv').exists():
        for li in Path(rd, 'refs.tsv').read_text().splitlines()[1:]:
            c = li.split('\t')
            if len(c) > 2 and c[2] in ('exclamacion', 'pregunta', 'suspensivos'):
                refs.append(str(Path(rd, c[0])))
    pars, wavs = [], []
    for i, tx in enumerate(FRASES_XENTE):
        p = parametros(i, refs)
        f = dir_wav / f'xente_{i:02d}.wav'
        if not f.exists():
            V.cargar()
            w, _ = V.infer(tx, escala=p['escala'], f0_media=p['f0_media'], f0_rango=p['f0_rango'],
                           semente=p['semente'], ref=p['ref'])
            sf.write(str(f) + '.tmp.wav', w, 24000); os.replace(str(f) + '.tmp.wav', f)
            print(f'xente {i:02d} {len(w) / 24000:4.1f}s {tx}', flush=True)
        w, sr = sf.read(f)
        w = recortar(signal.resample_poly(w, 2, 3), SR_BANCO)          # 24 -> 16 kHz
        w = w / (np.sqrt(np.mean(w ** 2)) + 1e-9) * 0.08                # mesmo RMS en todas
        wavs.append(w.astype(np.float32))
        pars.append(dict(p, ref=Path(p['ref']).name if p['ref'] else None, texto=tx))
    gap = np.zeros(int(0.25 * SR_BANCO), np.float32)
    pos, partes, t = [], [], 0
    for w in wavs:
        pos.append([t, t + len(w)]); partes += [w, gap]; t += len(w) + len(gap)
    banco = np.clip(np.concatenate(partes), -1, 1)
    DATOS.mkdir(exist_ok=True)
    tmp = DATOS / '.xente-banco.tmp.ogg'
    sf.write(tmp, banco, SR_BANCO, format='OGG', subtype='VORBIS'); os.replace(tmp, DATOS / 'xente-banco.ogg')
    meta = {'sr': SR_BANCO, 'voz': 'Nos_StyleTTS2-Brais-GL (voz_st2.py)', 'autoria_textos': 'Claude (axente de son)',
            'frases': [dict(p, ini=a, fin=b) for p, (a, b) in zip(pars, pos)]}
    (DATOS / 'xente-banco.json').write_text(json.dumps(meta, ensure_ascii=False, indent=1))
    print('banco:', DATOS / 'xente-banco.ogg', f'{len(banco) / SR_BANCO:.1f} s,',
          f"{(DATOS / 'xente-banco.ogg').stat().st_size / 1e3:.0f} kB", flush=True)


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.environ.get('SCRATCH', '/tmp'), 'son', 'banco'))
