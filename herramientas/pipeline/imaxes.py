"""Etapa IMAXES: SDXL-Turbo (stabilityai/sdxl-turbo) en CPU, bfloat16, 1024x576, 4 pasos, con porta de revisión.

Para cada plano: xera, revisa (revisor.py) e, se a revisión falla, rexenera con outra semente. Desde o
intento INTENTO_PRUDENTE engade ao prompt unha cola "prudente" (figuras de corpo enteiro, sen primeiros
planos de mans). Tras MAX_INTENTOS escolle o intento con menos problemas e márcao como non aprobado
(a porta `imaxes_revisadas` do QA falla e o vídeo sae NON PUBLICABLE).

Licenza do modelo: Stability AI Community License (uso non comercial e comercial ata 1 M USD de
ingresos anuais, con rexistro). Ver README. O estilo común vai aquí, non no LLM, para que todas as
imaxes do canal compartan acabado.
"""
import hashlib, json, os, time
from pathlib import Path

# Estilo curto e ao principio: CLIP só le 77 tokens e trunca o final. Sen "verde/brétema" fixos:
# a paleta e a luz de cada plano decídeas o prompt do LLM (ronda 1: todo saía cunha néboa verde uniforme).
ESTILO = "cinematic film still, fifteenth-century Galicia, {p}, natural light, detailed, painterly realism"
PRUDENTE = ", full-body figures seen from a few metres away, hands not in focus"
XENERICO = ("villagers in wool cloaks walking past a granite tower-house in a small hamlet, "
            "slate roofs, overcast morning light, wide shot")
MODELO = os.environ.get('IMG_MODEL', 'stabilityai/sdxl-turbo')
W, H, PASOS = 1024, 576, int(os.environ.get('IMG_STEPS', '4'))
MAX_INTENTOS, INTENTO_PRUDENTE = int(os.environ.get('IMG_MAX_INTENTOS', '5')), 2


def xerar(escenas, outdir, seed_base='sera', revisar=True):
    outdir = Path(outdir); outdir.mkdir(parents=True, exist_ok=True)
    rexf = outdir / 'revision.json'
    feito = json.loads(rexf.read_text()) if rexf.exists() else {}
    pipe = rev = None
    paths, rexistro = [], []
    for i, e in enumerate(escenas):
        clave = f"{i:03d}-{hashlib.sha256(e['prompt'].encode()).hexdigest()[:8]}"
        if clave in feito and (outdir / feito[clave]['ficheiro']).exists():
            r = feito[clave]
        else:
            if pipe is None:
                import torch
                from diffusers import AutoPipelineForText2Image
                torch.set_num_threads(int(os.environ.get('NTH', '4')))
                pipe = AutoPipelineForText2Image.from_pretrained(MODELO, torch_dtype=torch.bfloat16, variant='fp16')
                pipe.set_progress_bar_config(disable=True)
                if revisar:
                    import revisor
                    rev = revisor.Revisor()
            import torch
            intentos = []
            for k in range(MAX_INTENTOS):
                pr = ESTILO.format(p=e['prompt'].strip().rstrip('.')) + (PRUDENTE if k >= INTENTO_PRUDENTE else '')
                seed = int(hashlib.sha256(f'{seed_base}-{i}-{pr}-{k}'.encode()).hexdigest()[:8], 16)
                f = outdir / f'{clave}-{k}.png'
                t = time.time()
                im = pipe(prompt=pr, width=W, height=H, num_inference_steps=PASOS, guidance_scale=0.0,
                          generator=torch.Generator().manual_seed(seed)).images[0]
                im.save(f)
                it = {'intento': k, 'ficheiro': f.name, 'seed': seed, 's': round(time.time() - t, 1), 'prompt': pr,
                      'problemas': []}
                if rev is not None:
                    t = time.time(); rv = rev.revisar(f)
                    it.update({'problemas': rv['problemas'], 'descricion': rv.get('descricion', ''),
                               'obxectos': rv.get('obxectos', []), 'mans': rv['mans'], 'corpos': rv['corpos'],
                               's_revision': round(time.time() - t, 1)})
                intentos.append(it)
                print(f"imaxe {i:3d} intento {k} {it['s']:5.1f}s + revisión {it.get('s_revision', 0):4.1f}s "
                      f"{it['problemas'] or 'ok'}", flush=True)
                if not it['problemas']:
                    break
            best = min(range(len(intentos)), key=lambda j: (len(intentos[j]['problemas']), j))
            r = {'ficheiro': intentos[best]['ficheiro'], 'escollida': best, 'ok': not intentos[best]['problemas'],
                 'intentos': intentos}
            feito[clave] = r
            rexf.write_text(json.dumps(feito, ensure_ascii=False, indent=1))
        paths.append(str(outdir / r['ficheiro'])); rexistro.append(r)
    return paths, rexistro
