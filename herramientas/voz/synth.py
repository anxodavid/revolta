"""Genera muestras de narración para dormir con voces del Proxecto Nós (Coqui VITS)."""
import re, sys, json, numpy as np, soundfile as sf
from TTS.utils.synthesizer import Synthesizer
import nos_front

VOICES = {
    'brais':  ('brais-vits-graphemes/brais.pth', 'brais-vits-graphemes/config.json', False),
    'icia':   ('icia-vits-phonemes/icia.pth', 'icia-vits-phonemes/icia_config.json', True),
    'iago':   ('iago-vits-phonemes/iago.pth', 'iago-vits-phonemes/config.json', True),
    'paulo':  ('paulo-vits-phonemes/paulo.pth', 'paulo-vits-phonemes/config.json', True),
    'celtia': ('celtia-vits-phonemes/celtia_ph.pth', 'celtia-vits-phonemes/config.json', True),
}

def sentences(par):
    return [s.strip() for s in re.split(r'(?<=[.!?…])\s+', par) if s.strip()]

def run(voice, text_file, out_wav, length_scale=1.0, sent_pause=0.7, par_pause=1.6):
    ckpt, cfg, phon = VOICES[voice]
    syn = Synthesizer(tts_checkpoint=ckpt, tts_config_path=cfg, use_cuda=False)
    syn.tts_model.length_scale = length_scale
    sr = syn.output_sample_rate
    pars = [p.strip() for p in open(text_file, encoding='utf-8').read().split('\n\n') if p.strip()]
    audio = [np.zeros(int(sr * 0.8))]
    for par in pars:
        for s in sentences(par):
            inp = nos_front.text_preprocess(s) if phon else s
            wav = np.array(syn.tts(inp), dtype=np.float32)
            audio += [wav, np.zeros(int(sr * sent_pause))]
        audio.append(np.zeros(int(sr * (par_pause - sent_pause))))
    a = np.concatenate(audio)
    a = a / (np.abs(a).max() + 1e-9) * 0.7
    sf.write(out_wav, a, sr)
    print(voice, 'ok', round(len(a) / sr, 1), 's')

if __name__ == '__main__':
    run(sys.argv[1], sys.argv[2], sys.argv[3], float(sys.argv[4]) if len(sys.argv) > 4 else 1.0)
