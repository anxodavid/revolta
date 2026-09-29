# Barrido de escala de duraciones en Nós StyleTTS2 Brais (CPU). Salida: sweep/<cfg>_<scale>.wav y .json
import sys, time, json, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),'st2')); sys.path.insert(0,'.')
import torch, yaml, numpy as np, soundfile as sf
torch.set_num_threads(int(os.environ.get('NTH','4')))
from models import *
from utils import *
from text_utils_gal import TextCleanerGal
from Utils.ASR.AuxiliaryASR.phonemize import run_cotovia_with_phrase, clean_output
from Utils.PLBERT.util import load_plbert
from Utils.JDC.model import JDCNet
from Modules.diffusion.sampler import DiffusionSampler, ADPM2Sampler, KarrasSchedule
from collections import OrderedDict
cfg=yaml.safe_load(open('Models/galician/brais/config.yml'))
text_aligner=load_ASR_models('Models/galician/ASR/epoch_00080.pth','Models/galician/ASR/config.yml')
pitch=JDCNet(num_class=1, seq_len=192); plbert=load_plbert('Models/galician/PLBERT/')
model=build_model(recursive_munch(cfg['model_params']), text_aligner, pitch, plbert)
params=torch.load('Models/galician/brais/epoch_2nd_00057.pth', map_location='cpu')['net']
for k in model:
    if k in params:
        try: model[k].load_state_dict(params[k])
        except Exception: model[k].load_state_dict(OrderedDict((n[7:],v) for n,v in params[k].items()), strict=False)
_=[model[k].eval() for k in model]
sampler=DiffusionSampler(model.diffusion.diffusion, sampler=ADPM2Sampler(), sigma_schedule=KarrasSchedule(sigma_min=0.0001, sigma_max=3.0, rho=9.0), clamp=False)
import inference as INF
ref_s=INF.compute_style(os.environ.get('REF_WAV','brais_ref_humana.wav'), model, 'cpu')
tc=TextCleanerGal()
def infer(text, s_prev, alpha, beta, t, steps, scale):
    ps=clean_output(run_cotovia_with_phrase(text.strip()))
    tokens=tc(ps); tokens.insert(0, tc([" "],mode="phoneme")[0])
    tokens=torch.LongTensor(tokens).unsqueeze(0)
    with torch.no_grad():
        il=torch.LongTensor([tokens.shape[-1]]); tm=INF.length_to_mask(il)
        t_en=model.text_encoder(tokens, il, tm); bd=model.bert(tokens, attention_mask=(~tm).int()); d_en=model.bert_encoder(bd).transpose(-1,-2)
        s_pred=sampler(noise=torch.randn((1,256)).unsqueeze(1), embedding=bd, num_steps=steps, embedding_scale=1, features=ref_s).squeeze(1)
        if s_prev is not None: s_pred=t*s_prev+(1-t)*s_pred
        s=s_pred[:,128:]; ref=s_pred[:,:128]
        ref=alpha*ref+(1-alpha)*ref_s[:,:128]; s=beta*s+(1-beta)*ref_s[:,128:]
        s_pred=torch.cat([ref,s],dim=-1)
        d=model.predictor.text_encoder(d_en, s, il, tm); x,_=model.predictor.lstm(d)
        dur=torch.sigmoid(model.predictor.duration_proj(x)).sum(axis=-1)*scale
        pd=torch.round(dur.squeeze()).clamp(min=1)
        aln=torch.zeros(il, int(pd.sum()))
        c=0
        for i in range(aln.size(0)): aln[i,c:c+int(pd[i])]=1; c+=int(pd[i])
        en=d.transpose(-1,-2)@aln.unsqueeze(0)
        F0,N=model.predictor.F0Ntrain(en,s); asr=t_en@aln.unsqueeze(0)
        out=model.decoder(asr,F0,N,ref.squeeze().unsqueeze(0))
    return out.squeeze().numpy()[...,:-50], s_pred, ps, pd.tolist()
CFGS={'bench':dict(alpha=0.3,beta=0.7,t=0.0,steps=5),'ficha':dict(alpha=0.6,beta=1.0,t=0.6,steps=10)}
# Render para dormir: por frases, escala de duraciones y pausas largas
scale=float(os.environ.get('SCALE','1.2'))
pars=[p.strip() for p in open(os.environ['TXT']).read().split('\n\n') if p.strip()]
sr=24000; out=[np.zeros(int(sr*0.8))]; sp=None
for par in pars:
    for s in INF.split_text_into_sentences(par):
        w,sp,_,_=infer(s, sp, scale=scale, **CFGS['bench'])
        out+=[w, np.zeros(int(sr*0.7))]
    out.append(np.zeros(int(sr*0.9)))
a=np.concatenate(out); a=a/(np.abs(a).max()+1e-9)*0.7
sf.write(os.environ['OUT'], a, sr); print('st2 ok', round(len(a)/sr,1))
