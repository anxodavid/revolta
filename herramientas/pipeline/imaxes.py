"""Etapa IMAXES: SDXL-Turbo (stabilityai/sdxl-turbo) en CPU, bfloat16, 1024x576, 4 pasos, con porta de revisión.

Para cada plano: xera, revisa (revisor.py) e, se a revisión falla, rexenera con outra semente. Desde o
intento INTENTO_PRUDENTE engade ao prompt unha cola "prudente" (figuras de corpo enteiro, sen primeiros
planos de mans). Se MAX_INTENTOS fallan, fai ata RESERVAS intentos de reserva co prompt XENÉRICO (aldeáns
diante dunha casa torre: un plano que case sempre pasa). Se tamén fallan, escolle o intento con menos
problemas e márcao como non aprobado (a porta `imaxes_revisadas` do QA falla: NON PUBLICABLE).

Licenza do modelo: Stability AI Community License (uso non comercial e comercial ata 1 M USD de
ingresos anuais, con rexistro). Ver README. O estilo común vai aquí, non no LLM, para que todas as
imaxes do canal compartan acabado.
"""
import hashlib, json, os, re, time
from pathlib import Path

# Estilo curto e ao principio: CLIP só le 77 tokens e trunca o final. Sen "verde/brétema" fixos:
# a paleta e a luz de cada plano decídeas o prompt do LLM (ronda 1: todo saía cunha néboa verde uniforme).
# Ronda 3: UNHA paleta e un acabado para todo o episodio (o crítico visual viu planos pictóricos, saturados e sepia
# mesturados). O estilo vai ao principio e as cores que escriba o LLM quítanse (COR); despois `graduar` iguala a cor.
ESTILO = ("muted oil painting, soft overcast light, grey-green and slate palette, fifteenth-century Galicia, {p}, "
          "painterly realism, few figures")
COR = (r'\b(golden|gold|amber|blood[- ]orange|orange|crimson|red|sepia|neon|vivid|vibrant|saturated|fiery|'
       r'purple|pink|glowing|sunset|sunrise)\b')
PRUDENTE = ", full-body figures seen from a few metres away, hands not in focus"
XENERICO = ("two villagers in wool cloaks walking past a granite tower-house in a small hamlet, "
            "dark grey slate roofs, overcast morning light, wide shot")
SIM_MAX, CAP_MAX, VECIÑOS = 0.6, 0.5, 4   # porta de repetición: contra as VECIÑOS imaxes anteriores do episodio
MODELO = os.environ.get('IMG_MODEL', 'stabilityai/sdxl-turbo')
W, H, PASOS = 1024, 576, int(os.environ.get('IMG_STEPS', '4'))
MAX_INTENTOS, INTENTO_PRUDENTE, RESERVAS = int(os.environ.get('IMG_MAX_INTENTOS', '5')), 2, 3


def xerar(escenas, outdir, seed_base='sera', revisar=True):
    outdir = Path(outdir); outdir.mkdir(parents=True, exist_ok=True)
    rexf = outdir / 'revision.json'
    feito = json.loads(rexf.read_text()) if rexf.exists() else {}
    pipe = rev = None
    paths, rexistro = [], []
    aceptadas = []     # (vector, raíces da descrición) das imaxes escollidas, para a porta de repetición
    for i, e in enumerate(escenas):
        clave = f"{i:03d}-{hashlib.sha256(e['prompt'].encode()).hexdigest()[:8]}"
        previo = feito.get(clave)
        import revisor as _rv
        vella = previo and previo.get('version_revisor') != _rv.VERSION and revisar
        if previo and not vella and (outdir / previo['ficheiro']).exists() and (previo['ok'] or len(previo['intentos']) >= MAX_INTENTOS + RESERVAS):
            r = previo
        else:
            import torch
            torch.set_num_threads(int(os.environ.get('NTH', '4')))
            if rev is None and revisar:
                import revisor
                rev = revisor.Revisor()
            intentos = list(previo['intentos']) if previo else []     # continúa onde quedou (p. ex. falta a reserva)
            if intentos and rev is not None:     # se o revisor cambiou desde entón, volve revisar os intentos gardados
                for it in intentos:
                    rv = rev.revisar(outdir / it['ficheiro'])
                    if rv['problemas'] != it['problemas']:
                        it['problemas_revision_anterior'] = it['problemas']; it['problemas'] = rv['problemas']
                        it['descricion'] = rv.get('descricion', ''); it['obxectos'] = rv.get('obxectos', [])
                        print(f"imaxe {i:3d} intento {it['intento']} revisado de novo: {it['problemas'] or 'ok'}", flush=True)
            for k in range(len(intentos), MAX_INTENTOS + RESERVAS):
                if any(not x['problemas'] for x in intentos):
                    break
                base = XENERICO if k >= MAX_INTENTOS else re.sub(r'\s+', ' ', re.sub(COR, '', e['prompt'], flags=re.I))
                pr = ESTILO.format(p=base.strip().rstrip('.')) + (PRUDENTE if k >= INTENTO_PRUDENTE else '')
                seed = int(hashlib.sha256(f'{seed_base}-{i}-{pr}-{k}'.encode()).hexdigest()[:8], 16)
                if pipe is None:
                    from diffusers import AutoPipelineForText2Image
                    pipe = AutoPipelineForText2Image.from_pretrained(MODELO, torch_dtype=torch.bfloat16, variant='fp16')
                    pipe.set_progress_bar_config(disable=True)
                f = outdir / f'{clave}-{k}.png'
                t = time.time()
                im = pipe(prompt=pr, width=W, height=H, num_inference_steps=PASOS, guidance_scale=0.0,
                          generator=torch.Generator().manual_seed(seed)).images[0]
                im.save(f)
                it = {'intento': k, 'ficheiro': f.name, 'seed': seed, 's': round(time.time() - t, 1), 'prompt': pr,
                      'problemas': [], 'reserva': k >= MAX_INTENTOS}
                if rev is not None:
                    t = time.time(); rv = rev.revisar(f)
                    it.update({'problemas': rv['problemas'], 'descricion': rv.get('descricion', ''),
                               'obxectos': rv.get('obxectos', []), 'mans': rv['mans'], 'corpos': rv['corpos'],
                               's_revision': round(time.time() - t, 1)})
                rep = repetida(f, it.get('descricion', ''), aceptadas)
                if rep:
                    it['problemas'] = it['problemas'] + [rep]
                intentos.append(it)
                print(f"imaxe {i:3d} intento {k} {it['s']:5.1f}s + revisión {it.get('s_revision', 0):4.1f}s "
                      f"{it['problemas'] or 'ok'}", flush=True)
                if not it['problemas']:
                    break
            best = min(range(len(intentos)), key=lambda j: (len(intentos[j]['problemas']), j))
            r = {'ficheiro': intentos[best]['ficheiro'], 'escollida': best, 'ok': not intentos[best]['problemas'],
                 'intentos': intentos, 'version_revisor': _rv.VERSION}
            feito[clave] = r
            rexf.write_text(json.dumps(feito, ensure_ascii=False, indent=1))
        # as imaxes gardadas dunha versión anterior tamén pasan a porta de repetición
        rep = repetida(outdir / r['ficheiro'], r['intentos'][r['escollida']].get('descricion', ''), aceptadas)
        if rep and r['ok']:
            r = dict(r, ok=False); r['intentos'][r['escollida']]['problemas'] = [rep]
        aceptadas.append(firma(outdir / r['ficheiro'], r['intentos'][r['escollida']].get('descricion', '')))
        paths.append(str(outdir / r['ficheiro'])); rexistro.append(r)
    return paths, rexistro


def firma(f, descricion):
    import numpy as np
    from PIL import Image, ImageFilter
    a = np.asarray(Image.open(f).convert('L').filter(ImageFilter.GaussianBlur(8)).resize((48, 27)), np.float32).ravel()
    a -= a.mean()
    stop = {'image', 'shows', 'the', 'and', 'with', 'of', 'in', 'a', 'an', 'is', 'are', 'on', 'there', 'background',
            'foreground', 'front', 'to', 'at', 'from', 'which', 'that', 'this', 'it', 'its', 'they', 'their', 'some'}
    return a / (np.linalg.norm(a) + 1e-9), {w[:6] for w in re.findall(r'[a-z]+', descricion.lower()) if w not in stop and len(w) > 2}


def repetida(f, descricion, aceptadas):
    """Porta de repetición (ronda 3): a imaxe non pode parecerse de máis a ningunha das VECIÑOS anteriores
    (composición: correlación da imaxe en grises desenfocada a 48x27 > SIM_MAX; contido: Jaccard das palabras
    da descrición de Florence-2 > CAP_MAX). Calibración: nas 24 imaxes da ronda 2 o p95 da correlación era 0,50."""
    if not aceptadas:
        return None
    v, cap = firma(f, descricion)
    for k, (v2, cap2) in enumerate(aceptadas[-VECIÑOS:][::-1]):
        sim = float(v @ v2)
        jac = len(cap & cap2) / max(1, len(cap | cap2)) if cap and cap2 else 0
        if sim > SIM_MAX or jac > CAP_MAX:
            return f'repetida (parécese ao plano -{k + 1}: composición {sim:.2f}, descrición {jac:.2f})'
    return None


def graduar(paths, outdir, forza=0.75, sat=0.85):
    """Igualación de cor (ronda 3): cada imaxe lévase á media e desviación por canle do episodio (transferencia
    de Reinhard en YCbCr), cunha saturación común. Así non se mesturan planos saturados, sepia e grises."""
    import numpy as np
    from PIL import Image, ImageEnhance
    outdir = Path(outdir); outdir.mkdir(parents=True, exist_ok=True)
    ys = [np.asarray(Image.open(p).convert('YCbCr'), np.float32) for p in paths]
    mu = np.mean([x.reshape(-1, 3).mean(0) for x in ys], 0)
    sd = np.mean([x.reshape(-1, 3).std(0) for x in ys], 0)
    out = []
    for p, x in zip(paths, ys):
        m, s_ = x.reshape(-1, 3).mean(0), x.reshape(-1, 3).std(0) + 1e-6
        y = forza * ((x - m) / s_ * sd + mu) + (1 - forza) * x
        y[..., 0] = 0.5 * x[..., 0] + 0.5 * y[..., 0]       # a luminancia cambia menos que a cor
        im = Image.fromarray(np.clip(y, 0, 255).astype(np.uint8), 'YCbCr').convert('RGB')
        im = ImageEnhance.Color(im).enhance(sat)
        q = outdir / Path(p).name
        im.save(q); out.append(str(q))
    return out
