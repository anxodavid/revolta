import csv, json, urllib.request, numpy as np, soundfile as sf
from TTS.utils.synthesizer import Synthesizer
import nos_front
SENTS = [
 "O carballo da Retorta ten unha folla revirada que lla revirou o aire unha noite de xeada.",
 "As medidas afectan en Galicia a máis dun cento de barcos e dous milleiros de mariñeiros.",
 "Hai xiros da linguaxe con sentido figurado que non deben interpretarse en sentido literal.",
 "Os enxeñeiros cualificaron a obra de moi complexa debido á orografía das zonas polas que discorre a vía.",
]
CFG = {'brais': ('human/brais_test.csv', 'Nos_Brais-GL', 'brais-vits-graphemes/brais.pth', 'brais-vits-graphemes/config.json', False),
       'celtia': ('human/celtia_test.csv', 'Nos_Celtia-GL', 'celtia-vits-phonemes/celtia_ph.pth', 'celtia-vits-phonemes/config.json', True)}
out = []
for voice, (csvp, ds, ckpt, cfg, phon) in CFG.items():
    rows = {r['transcripts']: r['file_name'] for r in csv.DictReader(open(csvp), delimiter='\t')}
    syn = Synthesizer(tts_checkpoint=ckpt, tts_config_path=cfg, use_cuda=False)
    for i, s in enumerate(SENTS):
        hf = f'kit/t1/{voice}_{i}_human.wav'
        urllib.request.urlretrieve(f'https://huggingface.co/datasets/proxectonos/{ds}/resolve/main/audio/test/{rows[s]}', hf)
        wav = np.array(syn.tts(nos_front.text_preprocess(s) if phon else s), dtype=np.float32)
        sf.write(f'kit/t1/{voice}_{i}_tts.wav', wav / (np.abs(wav).max() + 1e-9) * 0.7, syn.output_sample_rate)
        out.append({'voice': voice, 'i': i, 'text': s})
json.dump(out, open('kit/t1/index.json', 'w'), ensure_ascii=False, indent=1)
print('done', len(out))
