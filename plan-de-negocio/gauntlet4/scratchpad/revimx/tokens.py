import os, sys, json
os.environ['HF_HOME'] = '/tmp/claude-0/-home-user-revolta/c92eba35-e89d-5d11-bb3d-f517a84dab48/scratchpad/hf'
os.environ['HF_HUB_OFFLINE'] = '1'
from transformers import CLIPTokenizer
t = CLIPTokenizer.from_pretrained('stabilityai/stable-diffusion-xl-base-1.0', subfolder='tokenizer')
PRE = 'cinematic film still, period drama, photorealistic, dramatic chiaroscuro, '
for l in open(sys.argv[1]):
    l = l.strip()
    if not l or l.startswith('#'):
        print(l); continue
    n, p = l.split('|', 1)
    a = len(t(p)['input_ids']) - 2
    b = len(t(PRE + p)['input_ids']) - 2
    print(f'{n}: {a} tokens (con prefixo {b})')
