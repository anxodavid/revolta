"""¿Ve Florence-2-base os obxectos pequenos que CLIP non ve? (bombilla e radiador do plano 84, maleta de rodas do 56,
billa do 31 e cociña de ferro do 91, todos da v1 antes dos arranxos) con <OPEN_VOCABULARY_DETECTION> e con
<DENSE_REGION_CAPTION>, fronte a 24 imaxes limpas da v1. Proba de calibración da porta v6 (Gauntlet 4, peza IMAXE).

    flock "$CPU_LOCK" $PY florence_ovd.py      # ≈ 5-8 min
"""
import json, os, sys, time
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
sys.path.insert(0, str(AQUI))
import calibrar_clip as c

CONSULTAS = ['light bulb', 'radiator', 'rolling suitcase', 'faucet', 'cast iron stove', 'street lamp', 'wall lamp',
             'framed picture']
MALAS = {(84, 'vella'), (56, 'vella'), (31, 'vella'), (91, 'vella'), (82, 'actual'), (148, 'actual'), (94, 'actual'),
         (17, 'actual'), (123, 'actual')}


def main():
    import torch
    from PIL import Image
    from transformers import AutoProcessor, Florence2ForConditionalGeneration
    torch.set_num_threads(int(os.environ.get('NTH', '4')))
    nome = os.environ.get('REVISOR_VLM', 'florence-community/Florence-2-base')
    m = Florence2ForConditionalGeneration.from_pretrained(nome, torch_dtype=torch.float32).eval()
    proc = AutoProcessor.from_pretrained(nome)
    ims = c.imaxes()
    limpas = [(d, p) for d, p in ims if c.limpa(d)][::4][:24]
    malas = [(d, p) for d, p in ims if (d['n'], d['version']) in MALAS]
    out = []

    def florence(im, task, texto=None, max_new=120):
        inp = proc(text=task + (texto or ''), images=im, return_tensors='pt')
        with torch.no_grad():
            ids = m.generate(**inp, max_new_tokens=max_new, num_beams=1, do_sample=False)
        txt = proc.batch_decode(ids, skip_special_tokens=False)[0]
        return proc.post_process_generation(txt, task=task, image_size=im.size)[task]

    for d, p in malas + limpas:
        im = Image.open(p).convert('RGB')
        t = time.time()
        r = {'n': d['n'], 'version': d['version'], 'mala': (d['n'], d['version']) in MALAS, 'ovd': {}}
        for q in CONSULTAS:
            o = florence(im, '<OPEN_VOCABULARY_DETECTION>', q, 60)
            caixas = o.get('bboxes', [])
            r['ovd'][q] = [[round(v) for v in b] for b in caixas]
        r['densa'] = florence(im, '<DENSE_REGION_CAPTION>', None, 200).get('labels', [])
        r['s'] = round(time.time() - t, 1)
        out.append(r)
        print(json.dumps(r, ensure_ascii=False), flush=True)
    dest = Path(os.environ.get('SCRATCH', '/tmp')) / 'imaxe4' / 'calib' / 'florence_ovd.json'
    dest.write_text(json.dumps(out, ensure_ascii=False, indent=1))
    print('feito', dest)


if __name__ == '__main__':
    main()
