"""Etapa IMAXES: SDXL-Turbo (stabilityai/sdxl-turbo) en CPU, bfloat16, 1024x576, 4 pasos.

Licenza do modelo: Stability AI Community License (uso non comercial e comercial ata 1 M USD de
ingresos anuais, con rexistro). Ver README. O estilo común vai aquí, non no LLM, para que todas as
imaxes do canal compartan paleta e acabado.
"""
import hashlib, os, time
from pathlib import Path

# Estilo curto e ao principio: CLIP só le 77 tokens e trunca o final.
ESTILO = ("cinematic film still, medieval Galicia, rainy green Atlantic land, grey granite, "
          "{p}, soft light, muted colors, painterly realism")
MODELO = os.environ.get('IMG_MODEL', 'stabilityai/sdxl-turbo')
W, H, PASOS = 1024, 576, int(os.environ.get('IMG_STEPS', '4'))


def xerar(escenas, outdir, seed_base='sera'):
    import torch
    from diffusers import AutoPipelineForText2Image
    torch.set_num_threads(int(os.environ.get('NTH', '4')))
    outdir = Path(outdir); outdir.mkdir(parents=True, exist_ok=True)
    nome = lambda i, e: outdir / f"{i:03d}-{hashlib.sha256(e['prompt'].encode()).hexdigest()[:8]}.png"
    paths = [str(nome(i, e)) for i, e in enumerate(escenas)]
    falta = [(i, e) for i, e in enumerate(escenas) if not nome(i, e).exists()]
    rex = []
    if not falta:
        return paths, rex
    pipe = AutoPipelineForText2Image.from_pretrained(MODELO, torch_dtype=torch.bfloat16, variant='fp16')
    pipe.set_progress_bar_config(disable=True)
    for i, e in falta:
        pr = ESTILO.format(p=e['prompt'].strip().rstrip('.'))
        seed = int(hashlib.sha256(f'{seed_base}-{i}-{pr}'.encode()).hexdigest()[:8], 16)
        t = time.time()
        im = pipe(prompt=pr, width=W, height=H, num_inference_steps=PASOS, guidance_scale=0.0,
                  generator=torch.Generator().manual_seed(seed)).images[0]
        im.save(nome(i, e))
        rex.append({'escena': i, 'seed': seed, 's': round(time.time() - t, 1), 'prompt': pr})
        print(f'imaxe {i:3d} {time.time()-t:5.1f}s', flush=True)
    return paths, rex
