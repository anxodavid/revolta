#!/usr/bin/env python3
"""Extrapola a un episodio de 60 min narrados + 30 min de cola os tempos MEDIDOS nas dúas execucións
reais do pipeline (29-09-2026) e na proba de ASR longo. Saída: extrapolacion.md (táboa de §4.1 do plan).

    python3 extrapolacion.py            (desde este directorio)

Cada cifra sae dunha medida [P] multiplicada por unha unidade de escala declarada; os parámetros de
deseño do episodio (duración, imaxes por minuto, cola) son supostos [S] e van arriba.
"""
import json
from pathlib import Path

H = Path(__file__).resolve().parent
M = H.parent
# ---- supostos de deseño do episodio [S]
NARR = 60 * 60          # s de liña de tempo narrada (voz + pausas)
COLA = 30 * 60          # s de cola sen voz
SEG_ESCENA = (14.0, 16.0)   # s por imaxe na parte narrada (medido: 13,6 e 16,1 s de media)
SEG_ESCENA_COLA = 60.0      # s por imaxe na cola [S]

# ---- medidas [P]
r1 = json.loads((M / 'r2-irmandinos-apertura-1/qa.json').read_text())
r2 = json.loads((M / 'r2-irmandinos-limpo-2/qa.json').read_text())
rex1 = json.loads((M / 'r2-irmandinos-apertura-1/imaxes_rexistro.json').read_text())
el2 = (M / 'r2-irmandinos-limpo-2/tempos_por_elemento.txt').read_text().splitlines()
img2 = [float(l.split()[2].rstrip('s')) for l in el2 if l.startswith('imaxe ')]
voz2 = [float(l.split()[2].rstrip('s')) for l in el2 if l.startswith('voz ')]
asr = {}
for n in ('x4', 'x15'):
    p = H / f'asr_longo_{n}.json'
    if p.exists():
        asr[n] = json.loads(p.read_text())

out, fil = [], []
def row(et, med, esc, lo, hi, nota=''):
    fil.append((lo, hi)); out.append(f'| {et} | {med} | {esc} | {lo/60:.0f}-{hi/60:.0f} | {nota} |')

dur = [r['ficheiro']['dur_video_s'] for r in (r1, r2)]
narr = [d - 10 for d in dur]      # 4 s de choiva antes da voz e 6 s de cola
tv = [r['tempos']['4_voz']['parede_s'] for r in (r1, r2)]
carga_voz = tv[1] - sum(voz2)
k_voz = sum(voz2) / narr[1]
lo = carga_voz + k_voz * NARR; hi = max(tv[0] / narr[0], tv[1] / narr[1]) * NARR
row('4 voz (StyleTTS2 Brais, frase a frase)', f'{tv[0]:.0f} s e {tv[1]:.0f} s para {narr[0]:.0f} e {narr[1]:.0f} s narrados; '
    f'na 2.ª, {sum(voz2):.0f} s de síntese + {carga_voz:.0f} s de carga', 's de liña narrada', lo, hi,
    f'{k_voz:.2f}-{hi/NARR:.2f} s de reloxo por s narrado')

i1 = [x['s'] for x in rex1]; m1, m2 = sum(i1) / len(i1), sum(img2) / len(img2)
carga_img = (r2['tempos']['5_imaxes']['parede_s'] - sum(img2), r1['tempos']['5_imaxes']['parede_s'] - sum(i1))
n_lo = NARR / SEG_ESCENA[1] + COLA / SEG_ESCENA_COLA; n_hi = NARR / SEG_ESCENA[0] + COLA / SEG_ESCENA_COLA
row('5 imaxes (SDXL-Turbo, 4 pasos, 1024x576, CPU)', f'{min(i1+img2):.1f}-{max(i1+img2):.1f} s por imaxe '
    f'(media {m1:.1f} e {m2:.1f} s; 30 imaxes); carga do modelo {min(carga_img):.0f}-{max(carga_img):.0f} s',
    f'imaxes ({n_lo:.0f}-{n_hi:.0f})', n_lo * min(m1, m2) + min(carga_img), n_hi * max(m1, m2) + max(carga_img),
    'a carga de 5,4 min foi en frío (disco)')

ts = [r['tempos']['6_son']['parede_s'] / d for r, d in zip((r1, r2), dur)]
row('6 son (choiva e mestura)', f"{r1['tempos']['6_son']['parede_s']} e {r2['tempos']['6_son']['parede_s']} s",
    's de vídeo', min(ts) * (NARR + COLA), max(ts) * (NARR + COLA))

tm = [r['tempos']['7_montaxe']['parede_s'] / d for r, d in zip((r1, r2), dur)]
row('7 montaxe (Ken Burns, brétema, x264)', f"{r1['tempos']['7_montaxe']['parede_s']:.0f} e "
    f"{r2['tempos']['7_montaxe']['parede_s']:.0f} s ({min(tm):.2f}-{max(tm):.2f} s por s de vídeo)", 's de vídeo',
    min(tm) * (NARR + COLA), max(tm) * (NARR + COLA), 'só se se cambia a carga de imaxes por treitos (RAM, §5.1)')

tq = [r['tempos']['8_qa']['parede_s'] for r in (r1, r2)]
if 'x15' in asr:
    a = asr['x15']; rtf = a['rtf']; base = f"ASR sobre {a['dur_audio_s']/60:.0f} min: RTF {rtf}, WER {a['wer_mestura']}"
else:
    a = asr['x4']; rtf = a['rtf']; base = f"ASR sobre {a['dur_audio_s']/60:.0f} min: RTF {rtf}, WER {a['wer_mestura']}"
resto = [q - 2 * 0.2 * d for q, d in zip(tq, dur)]   # QA menos dúas pasadas de ASR
lo = rtf * NARR + min(resto) / dur[0] * (NARR + COLA)
hi = 2 * rtf * NARR + max(resto) / dur[1] * (NARR + COLA)
row('8 QA (ASR mestura e voz, LanguageTool, ebur128, follas)', f'{tq[0]:.0f} e {tq[1]:.0f} s; {base}',
    'ASR: s narrados; resto: s de vídeo', lo, hi, '1 ou 2 pasadas de ASR (mestura / mestura + voz soa)')

tc = [r['tempos']['2_corrixir']['parede_s'] for r in (r1, r2)]
row('2 corrección (LanguageTool)', f'{min(tc):.0f}-{max(tc):.0f} s para 475 palabras', 'palabras (x15,6)',
    min(tc) * NARR / narr[1], max(tc) * NARR / narr[0])

tot_lo = sum(x[0] for x in fil); tot_hi = sum(x[1] for x in fil)
L = ['| Etapa | Medido [P] | Escala | 60 + 30 min (min de reloxo) | Nota |', '|---|---|---|---|---|'] + out
L.append(f'| **Subtotal sen LLM** | | | **{tot_lo/60:.0f}-{tot_hi/60:.0f}** (**{tot_lo/3600:.1f}-{tot_hi/3600:.1f} h**) | |')
(H / 'extrapolacion.md').write_text('# Extrapolación a 60 min narrados + 30 min de cola\n\n'
                                    'Xerado por `extrapolacion.py` a partir das medidas do 29-09-2026.\n\n'
                                    + '\n'.join(L) + '\n')
print('\n'.join(L))
