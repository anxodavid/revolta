"""Etapa VOZ: Nos_StyleTTS2-Brais-GL (Proxecto Nós, USC), en CPU, frase a frase.

    python voz_st2.py FRASES.json DIR_SAIDA

Execútase como subproceso desde pipeline.py e longo.py, co PATH/PYTHONPATH que necesita Cotovía e o código do
modelo (ver README). Entrada: JSON [{"i": .., "texto": .., "wav": ..}, ...]. Saída: DIR_SAIDA/<wav> (24 kHz, mono)
por frase e fonemas.json. As pausas entre frases pono quen chama.

Campos opcionais por frase (a curva do embude, curva.py; se faltan, a voz é a de sempre):
  escala           escala das duracións (máis alta = máis lenta); se falta, a variable SCALE (1,2)
  estilo           0 = referencia viva (REF_WAV) ... 1 = referencia calma (REF_WAV_CALMO): interpola o vector de
                   estilo das dúas (se REF_WAV_CALMO non está definida, non fai nada)
  f0_media         multiplica a F0 (altura media da voz)
  f0_rango         escala a desviación do log F0 arredor da súa media na frase (amplitude da entoación)
  enerxia          multiplica a enerxía N (log da norma do espectro mel) que recibe o descodificador. Efecto
                   medido: sobre todo volume (0,8 -> -1,8 dB) e algo menos de HNR; non suaviza o timbre
  alpha, beta      mestura do estilo predito co da referencia (0,3 e 0,7): canto máis baixos, máis manda a referencia
  embedding_scale  guía do texto na difusión do estilo (1; máis alto = máis expresivo)
  pasos            pasos da difusión do estilo (5)
REF_WAV e REF_WAV_CALMO admiten varias grabacións separadas por ':' (vector de estilo medio).

Cada frase ten a súa semente (SEED + texto): a mesma frase dá o mesmo audio aínda que se retome a execución ou se
cambie a súa posición, e dúas frases iguais con parámetros distintos só se diferencian polos parámetros.
Tamén se pode importar (cargar() + infer()) para as probas da peza de voz (gauntlet3/voz/scripts).
"""
import sys, os, json, math, zlib

ALPHA, BETA, PASOS, EMB = 0.3, 0.7, 5, 1.0
SCALE = float(os.environ.get('SCALE', '1.2'))
SEED = int(os.environ.get('SEED', '1'))
# Límites de seguridade: fóra deles a voz rompe ou as medidas non os cubriron (gauntlet3/voz/informe.md)
LIMITES = {'escala': (0.7, 1.6), 'estilo': (0.0, 1.0), 'f0_media': (0.85, 1.15), 'f0_rango': (0.5, 1.5),
           'enerxia': (0.7, 1.3), 'alpha': (0.0, 1.0), 'beta': (0.0, 1.0), 'embedding_scale': (0.5, 3.0),
           'pasos': (3, 20)}
F0_PISO = 40.0            # Hz: por debaixo, tramo xordo ou transición (non se toca)
M = {}                    # modelo cargado (cargar)


def cargar():
    """Carga o modelo unha vez (cwd = ST2_DIR, como espera o código de Nós)."""
    if M:
        return M
    st2 = os.environ['ST2_DIR']; os.chdir(st2); sys.path.insert(0, st2)
    import torch, yaml
    torch.set_num_threads(int(os.environ.get('NTH', '4')))
    import models, utils
    from text_utils_gal import TextCleanerGal
    from Utils.ASR.AuxiliaryASR.phonemize import run_cotovia_with_phrase, clean_output
    from Utils.PLBERT.util import load_plbert
    from Utils.JDC.model import JDCNet
    from Modules.diffusion.sampler import DiffusionSampler, ADPM2Sampler, KarrasSchedule
    from collections import OrderedDict
    import inference as INF
    cfg = yaml.safe_load(open('Models/galician/brais/config.yml'))
    text_aligner = models.load_ASR_models('Models/galician/ASR/epoch_00080.pth', 'Models/galician/ASR/config.yml')
    pitch = JDCNet(num_class=1, seq_len=192); plbert = load_plbert('Models/galician/PLBERT/')
    model = models.build_model(utils.recursive_munch(cfg['model_params']), text_aligner, pitch, plbert)
    params = torch.load('Models/galician/brais/epoch_2nd_00057.pth', map_location='cpu')['net']
    for k in model:
        if k in params:
            try:
                model[k].load_state_dict(params[k])
            except Exception:
                model[k].load_state_dict(OrderedDict((n[7:], v) for n, v in params[k].items()), strict=False)
    _ = [model[k].eval() for k in model]
    sampler = DiffusionSampler(model.diffusion.diffusion, sampler=ADPM2Sampler(),
                               sigma_schedule=KarrasSchedule(sigma_min=0.0001, sigma_max=3.0, rho=9.0), clamp=False)
    M.update(torch=torch, model=model, sampler=sampler, tc=TextCleanerGal(), INF=INF,
             fonemas=lambda t: clean_output(run_cotovia_with_phrase(t)), estilos={})
    return M


def estilo_de(refs):
    """Vector de estilo (1 x 256: 128 acústico + 128 prosódico) dunha ou varias grabacións separadas por ':'."""
    if refs not in M['estilos']:
        vs = [M['INF'].compute_style(p, M['model'], 'cpu') for p in refs.split(os.pathsep) if p]
        M['estilos'][refs] = M['torch'].stack(vs).mean(0)
    return M['estilos'][refs]


def _limitar(k, v):
    lo, hi = LIMITES[k]
    if not lo <= v <= hi:
        print(f'aviso: {k}={v} fóra de [{lo}, {hi}]; úsase o límite', file=sys.stderr, flush=True)
    return min(max(v, lo), hi)


def axustar_f0(F0, media=1.0, rango=1.0):
    """F0 (Hz) dos tramos sonoros: log F0 -> media + rango * (log F0 - media) + log(media). Os xordos quedan igual."""
    if media == 1.0 and rango == 1.0:
        return F0
    torch = M['torch']
    v = F0 > F0_PISO
    if int(v.sum()) < 3:
        return F0
    lf = torch.log(F0[v]); mu = lf.mean()
    F0 = F0.clone()
    F0[v] = torch.exp(mu + rango * (lf - mu) + math.log(media)).clamp(50.0, 400.0)
    return F0


def infer(texto, escala=None, estilo=0.0, f0_media=1.0, f0_rango=1.0, enerxia=1.0, alpha=ALPHA, beta=BETA,
          embedding_scale=EMB, pasos=PASOS, ref=None, ref_calma=None, semente=None):
    """Audio (numpy, 24 kHz) e fonemas dunha frase. Os parámetros son os campos opcionais do JSON (ver arriba)."""
    cargar()
    torch, model, tc = M['torch'], M['model'], M['tc']
    INF = M['INF']
    p = {k: _limitar(k, float(v)) for k, v in dict(escala=SCALE if escala is None else escala, estilo=estilo,
                                                      f0_media=f0_media, f0_rango=f0_rango, enerxia=enerxia,
                                                      alpha=alpha, beta=beta, embedding_scale=embedding_scale,
                                                      pasos=pasos).items()}
    ref = ref or os.environ['REF_WAV']
    ref_calma = ref_calma if ref_calma is not None else os.environ.get('REF_WAV_CALMO')
    rs = estilo_de(ref)
    if ref_calma and p['estilo'] > 0:
        rs = (1 - p['estilo']) * rs + p['estilo'] * estilo_de(ref_calma)
    texto = texto.strip()
    torch.manual_seed(semente if semente is not None else (SEED * 1000003 + zlib.crc32(texto.encode())) % 2 ** 31)
    ps = M['fonemas'](texto)
    tokens = tc(ps); tokens.insert(0, tc([" "], mode="phoneme")[0])
    tokens = torch.LongTensor(tokens).unsqueeze(0)
    with torch.no_grad():
        il = torch.LongTensor([tokens.shape[-1]]); tm = INF.length_to_mask(il)
        t_en = model.text_encoder(tokens, il, tm); bd = model.bert(tokens, attention_mask=(~tm).int())
        d_en = model.bert_encoder(bd).transpose(-1, -2)
        s_pred = M['sampler'](noise=torch.randn((1, 256)).unsqueeze(1), embedding=bd, num_steps=int(p['pasos']),
                              embedding_scale=p['embedding_scale'], features=rs).squeeze(1)
        s = s_pred[:, 128:]; r = s_pred[:, :128]
        r = p['alpha'] * r + (1 - p['alpha']) * rs[:, :128]; s = p['beta'] * s + (1 - p['beta']) * rs[:, 128:]
        d = model.predictor.text_encoder(d_en, s, il, tm); x, _ = model.predictor.lstm(d)
        dur = torch.sigmoid(model.predictor.duration_proj(x)).sum(axis=-1) * p['escala']
        pd = torch.round(dur.squeeze()).clamp(min=1)
        aln = torch.zeros(il, int(pd.sum())); c = 0
        for i in range(aln.size(0)):
            aln[i, c:c + int(pd[i])] = 1; c += int(pd[i])
        en = d.transpose(-1, -2) @ aln.unsqueeze(0)
        F0, N = model.predictor.F0Ntrain(en, s); asr = t_en @ aln.unsqueeze(0)
        F0 = axustar_f0(F0, p['f0_media'], p['f0_rango'])
        if p['enerxia'] != 1.0:
            N = N * p['enerxia']
        out = model.decoder(asr, F0, N, r.squeeze().unsqueeze(0))
    return out.squeeze().numpy()[..., :-50], ps


CAMPOS = ('escala', 'estilo', 'f0_media', 'f0_rango', 'enerxia', 'alpha', 'beta', 'embedding_scale', 'pasos')


def main(frases_json, outdir):
    import soundfile as sf
    frases = json.load(open(frases_json))
    os.makedirs(outdir, exist_ok=True)
    outdir = os.path.abspath(outdir)
    cargar()
    log = []
    for f in frases:
        p = os.path.join(outdir, f['wav'])
        if os.path.exists(p):
            continue
        w, ps = infer(f['texto'], **{k: f[k] for k in CAMPOS if f.get(k) is not None})
        pico = float(abs(w).max())
        if pico >= 0.99:
            print(f"aviso: frase {f['i']} con pico {pico:.3f} (saturación?)", file=sys.stderr, flush=True)
        sf.write(p + '.tmp.wav', w, 24000); os.replace(p + '.tmp.wav', p)
        log.append({'i': f['i'], 'fonemas': ps, 's': round(len(w) / 24000, 2), 'pico': round(pico, 3)})
        print(f"voz {f['i']:3d} {len(w)/24000:5.1f}s {f['texto'][:60]}", flush=True)
    fp = os.path.join(outdir, 'fonemas.json')
    try:
        vello = json.load(open(fp)) if os.path.exists(fp) else []
    except ValueError:
        vello = []
    json.dump(vello + log, open(fp, 'w'), ensure_ascii=False)


if __name__ == '__main__':
    main(os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2]))
