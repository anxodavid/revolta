"""Etapa VOZ: Nos_StyleTTS2-Brais-GL (Proxecto Nós, USC), en CPU, frase a frase.

Execútase como subproceso desde pipeline.py, co directorio do modelo (ST2_DIR) como cwd e co
PATH/PYTHONPATH que necesita Cotovía (ver README). Entrada: JSON [{"i":..,"texto":..}].
Saída: <dir>/NNN.wav (24 kHz, mono) por frase. As pausas pono pipeline.py.
Parámetros de inferencia: os do banco de probas (alpha 0,3, beta 0,7, 5 pasos de difusión),
escala de duracións por frase (campo "escala" do JSON; se falta, SCALE): o pipeline pon ~1,05 no gancho
e sobe ata ~1,25 (ritmo para durmir).
"""
import sys, os, json
frases_json, outdir = sys.argv[1], sys.argv[2]
st2 = os.environ['ST2_DIR']; os.chdir(st2); sys.path.insert(0, st2)
import torch, yaml, numpy as np, soundfile as sf
torch.set_num_threads(int(os.environ.get('NTH', '4')))
torch.manual_seed(int(os.environ.get('SEED', '1')))
from models import *
from utils import *
from text_utils_gal import TextCleanerGal
from Utils.ASR.AuxiliaryASR.phonemize import run_cotovia_with_phrase, clean_output
from Utils.PLBERT.util import load_plbert
from Utils.JDC.model import JDCNet
from Modules.diffusion.sampler import DiffusionSampler, ADPM2Sampler, KarrasSchedule
from collections import OrderedDict
import inference as INF

cfg = yaml.safe_load(open('Models/galician/brais/config.yml'))
text_aligner = load_ASR_models('Models/galician/ASR/epoch_00080.pth', 'Models/galician/ASR/config.yml')
pitch = JDCNet(num_class=1, seq_len=192); plbert = load_plbert('Models/galician/PLBERT/')
model = build_model(recursive_munch(cfg['model_params']), text_aligner, pitch, plbert)
params = torch.load('Models/galician/brais/epoch_2nd_00057.pth', map_location='cpu')['net']
for k in model:
    if k in params:
        try: model[k].load_state_dict(params[k])
        except Exception: model[k].load_state_dict(OrderedDict((n[7:], v) for n, v in params[k].items()), strict=False)
_ = [model[k].eval() for k in model]
sampler = DiffusionSampler(model.diffusion.diffusion, sampler=ADPM2Sampler(),
                           sigma_schedule=KarrasSchedule(sigma_min=0.0001, sigma_max=3.0, rho=9.0), clamp=False)
ref_s = INF.compute_style(os.environ['REF_WAV'], model, 'cpu')
tc = TextCleanerGal()
ALPHA, BETA, STEPS = 0.3, 0.7, 5
SCALE = float(os.environ.get('SCALE', '1.2'))


def infer(text, scale=SCALE):
    ps = clean_output(run_cotovia_with_phrase(text.strip()))
    tokens = tc(ps); tokens.insert(0, tc([" "], mode="phoneme")[0])
    tokens = torch.LongTensor(tokens).unsqueeze(0)
    with torch.no_grad():
        il = torch.LongTensor([tokens.shape[-1]]); tm = INF.length_to_mask(il)
        t_en = model.text_encoder(tokens, il, tm); bd = model.bert(tokens, attention_mask=(~tm).int())
        d_en = model.bert_encoder(bd).transpose(-1, -2)
        s_pred = sampler(noise=torch.randn((1, 256)).unsqueeze(1), embedding=bd, num_steps=STEPS,
                         embedding_scale=1, features=ref_s).squeeze(1)
        s = s_pred[:, 128:]; ref = s_pred[:, :128]
        ref = ALPHA * ref + (1 - ALPHA) * ref_s[:, :128]; s = BETA * s + (1 - BETA) * ref_s[:, 128:]
        d = model.predictor.text_encoder(d_en, s, il, tm); x, _ = model.predictor.lstm(d)
        dur = torch.sigmoid(model.predictor.duration_proj(x)).sum(axis=-1) * scale
        pd = torch.round(dur.squeeze()).clamp(min=1)
        aln = torch.zeros(il, int(pd.sum())); c = 0
        for i in range(aln.size(0)): aln[i, c:c + int(pd[i])] = 1; c += int(pd[i])
        en = d.transpose(-1, -2) @ aln.unsqueeze(0)
        F0, N = model.predictor.F0Ntrain(en, s); asr = t_en @ aln.unsqueeze(0)
        out = model.decoder(asr, F0, N, ref.squeeze().unsqueeze(0))
    return out.squeeze().numpy()[..., :-50], ps


os.makedirs(outdir, exist_ok=True)
log = []
for f in json.load(open(frases_json)):
    p = os.path.join(outdir, f['wav'])
    if os.path.exists(p): continue
    w, ps = infer(f['texto'], float(f.get('escala', SCALE)))
    sf.write(p, w, 24000)
    log.append({'i': f['i'], 'fonemas': ps, 's': round(len(w) / 24000, 2)})
    print(f"voz {f['i']:3d} {len(w)/24000:5.1f}s {f['texto'][:60]}", flush=True)
json.dump(log, open(os.path.join(outdir, 'fonemas.json'), 'a'), ensure_ascii=False)
