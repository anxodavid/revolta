"""Onde vai o tempo dunha imaxe SDXL-Lightning nesta CPU (sen bf16 nativo)? Codificar o texto, os 4 pasos da UNet e
o VAE (por teselas, en fp32), a 1024x576 e a 1344x768. Gauntlet 4, peza IMAXE (para a configuración de D18).

    herramientas/gauntlet/candado.sh $PY perfil_tempos.py
"""
import json, os, sys, time
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parents[3] / 'herramientas/pipeline'))


def main():
    import torch
    import imaxes
    torch.set_num_threads(int(os.environ.get('NTH', '4')))
    out = {}
    t = time.time(); pipe = imaxes.cargar_pipe('lightning'); out['carga_s'] = round(time.time() - t, 1)
    pr = imaxes.compor_prompt({'prompt': 'medium shot of an old woman in a dark wool headscarf spinning wool beside an '
                                         'open stone hearth, lit by the fire', 'fase': 'calma'}, 0, 0, (), None)
    for nome in ('lightning1024', 'lightning'):
        m = imaxes.modelo(nome)
        r = {}
        t = time.time()
        with torch.no_grad():
            emb = pipe.encode_prompt(pr, do_classifier_free_guidance=False)
        r['texto_s'] = round(time.time() - t, 1)
        t = time.time()
        lat = pipe(prompt_embeds=emb[0], pooled_prompt_embeds=emb[2], width=m['W'], height=m['H'],
                   num_inference_steps=4, guidance_scale=0.0, output_type='latent',
                   generator=torch.Generator().manual_seed(1)).images
        r['unet_4_pasos_s'] = round(time.time() - t, 1)
        t = time.time()
        with torch.no_grad():
            x = pipe.vae.decode(lat.to(pipe.vae.dtype) / pipe.vae.config.scaling_factor).sample
        r['vae_decode_s'] = round(time.time() - t, 1)
        out[nome] = r
        print(nome, r, flush=True)
        imaxes._liberar()
    dest = Path(os.environ.get('SCRATCH', '/tmp')) / 'imaxe4' / 'perfil_tempos.json'
    dest.write_text(json.dumps(out, indent=1))
    print(json.dumps(out))


if __name__ == '__main__':
    main()
