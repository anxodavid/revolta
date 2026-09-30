"""Etapa IMAXES: SDXL en CPU (bfloat16) con porta de revisión e gradación por fase.

Modelos (`IMG_MODEL`):
- `lightning` (por defecto desde o Gauntlet 3): SDXL base 1.0 coa UNet destilada de ByteDance/SDXL-Lightning a
  4 pasos, 1344x768 (unha das resolucións de adestramento de SDXL; antes 1024x576 reescalado, brando en pantalla
  grande). Licenza CreativeML OpenRAIL++-M (a de SDXL base), mellor que a Community License de Turbo.
  Os codificadores de texto son os do repo de SDXL-Turbo: o sha256 dos `model.fp16.safetensors` é idéntico ao de
  SDXL base (comprobado na API de HF o 30-09-2026), así que non se baixan dúas veces. O VAE é o de SDXL base.
- `lightning8`: a UNet de 8 pasos (máis lenta).
- `turbo`: SDXL-Turbo 1024x576, 4 pasos (o do Gauntlet 2). Tamén vale un id de repo de HF (compatibilidade).

Para cada plano: compón o prompt (estilo común + prompt do plano + luz por defecto da fase se o prompt non trae
luz), xera, revisa (revisor.py) e, se a revisión falla, rexenera con outra semente e unha corrección segundo o
motivo (lousa e granito ao principio se saen tellados laranxas; menos xente se hai multitude...). Se
MAX_INTENTOS fallan, fai ata RESERVAS intentos cun prompt de reserva seguro da fase (sen persoas). Se tamén fallan,
escolle o intento con menos problemas e márcao como non aprobado (a porta `imaxes_revisadas` do QA falla).

Gauntlet 3 (o crítico visual: luz plana e monótona, composicións repetidas, "óleo xenérico de IA"):
- estilo común de fotograma de cine de época e un guion de luz e cor por fase (biblia visual:
  plan-de-negocio/gauntlet3/visual/biblia.md); as palabras de luz e cor dos prompts do axente NON se quitan;
- porta de iconografía galega e de repetición con CLIP contra TODAS as imaxes aceptadas do episodio (revisor.py);
- `graduar` por fase (curva.py: contraste e brillo), sen igualar á media do episodio: conserva a luz de cada
  imaxe e só corrixe os extremos.
"""
import hashlib, json, math, os, re, time
from pathlib import Path

# ------------------------------------------------------------------ modelos
BASE = 'stabilityai/stable-diffusion-xl-base-1.0'
TEXTO_REPO = 'stabilityai/sdxl-turbo'       # mesmos codificadores de texto que SDXL base (sha256 idéntico)
LIGHTNING = 'ByteDance/SDXL-Lightning'
MODELOS = {
    'turbo': {'repo': 'stabilityai/sdxl-turbo', 'W': 1024, 'H': 576, 'pasos': 4},
    'lightning': {'unet': 'sdxl_lightning_4step_unet.safetensors', 'W': 1344, 'H': 768, 'pasos': 4},
    'lightning8': {'unet': 'sdxl_lightning_8step_unet.safetensors', 'W': 1344, 'H': 768, 'pasos': 8},
}
MODELO_DEFECTO = 'lightning'


def modelo(nome=None):
    """Configuración do modelo `nome` (ou de IMG_MODEL). Un id de repo de HF (con "/") cárgase como antes."""
    nome = nome or os.environ.get('IMG_MODEL', MODELO_DEFECTO)
    if '/' in nome:
        m = {'repo': nome, 'W': 1024, 'H': 576, 'pasos': 4}
    else:
        m = dict(MODELOS[nome])
    m['nome'] = nome
    m['W'] = int(os.environ.get('IMG_W', m['W'])); m['H'] = int(os.environ.get('IMG_H', m['H']))
    m['pasos'] = int(os.environ.get('IMG_STEPS', m['pasos']))
    return m


M = modelo()
MODELO, W, H, PASOS = M['nome'], M['W'], M['H'], M['pasos']       # compatibilidade co código anterior
MAX_INTENTOS, INTENTO_PRUDENTE, RESERVAS = int(os.environ.get('IMG_MAX_INTENTOS', '5')), 2, 2


def cargar_pipe(nome=None):
    """Pipeline de diffusers en CPU, bfloat16. VAE en channels_last: ~6 s en vez de ~11 s por imaxe con
    torch 2.10 (aprendizajes/entorno.md), mesma saída."""
    import torch
    m = modelo(nome)
    dt = torch.bfloat16
    if 'repo' in m:
        from diffusers import AutoPipelineForText2Image
        pipe = AutoPipelineForText2Image.from_pretrained(m['repo'], torch_dtype=dt, variant='fp16')
    else:
        from diffusers import (AutoencoderKL, EulerDiscreteScheduler, StableDiffusionXLPipeline,
                               UNet2DConditionModel)
        from transformers import CLIPTextModel, CLIPTextModelWithProjection, CLIPTokenizer
        from huggingface_hub import hf_hub_download
        from safetensors import safe_open
        from accelerate import init_empty_weights
        te1 = CLIPTextModel.from_pretrained(TEXTO_REPO, subfolder='text_encoder', variant='fp16', torch_dtype=dt)
        te2 = CLIPTextModelWithProjection.from_pretrained(TEXTO_REPO, subfolder='text_encoder_2', variant='fp16',
                                                          torch_dtype=dt)
        tok1 = CLIPTokenizer.from_pretrained(BASE, subfolder='tokenizer')
        tok2 = CLIPTokenizer.from_pretrained(BASE, subfolder='tokenizer_2')
        vae = AutoencoderKL.from_pretrained(BASE, subfolder='vae', variant='fp16', torch_dtype=dt)
        # Lightning: Euler con timesteps "trailing" e sen CFG (guidance 0), como indica a ficha do modelo
        sched = EulerDiscreteScheduler.from_pretrained(BASE, subfolder='scheduler', timestep_spacing='trailing')
        with init_empty_weights():
            unet = UNet2DConditionModel.from_config(UNet2DConditionModel.load_config(BASE, subfolder='unet'))
        sd = {}
        with safe_open(hf_hub_download(LIGHTNING, m["unet"]), framework="pt") as g:   # tensor a tensor (RSS ~9 GB ao cargar: páxinas do ficheiro + copias bf16)
            for k in g.keys():
                sd[k] = g.get_tensor(k).to(dt)
        unet.load_state_dict(sd, strict=True, assign=True)
        del sd
        pipe = StableDiffusionXLPipeline(vae=vae, text_encoder=te1, text_encoder_2=te2, tokenizer=tok1,
                                         tokenizer_2=tok2, unet=unet, scheduler=sched, add_watermarker=False)
    pipe.vae.to(memory_format=torch.channels_last)
    pipe.set_progress_bar_config(disable=True)
    pipe._revolta = m
    return pipe


def xerar_unha(pipe, prompt, seed, m=None, negativo=None, cfg=0.0):
    """Unha imaxe. Sen CFG (guidance 0) como pide Lightning; con `negativo` e cfg > 1 fai un intento guiado (dúas
    pasadas da UNet por paso: ~1,6 veces máis lento) para os planos con relato que fallan dúas veces."""
    import torch
    m = m or getattr(pipe, '_revolta', M)
    kw = {'negative_prompt': negativo, 'guidance_scale': cfg} if negativo and cfg > 1 else {'guidance_scale': 0.0}
    return pipe(prompt=prompt, width=m['W'], height=m['H'], num_inference_steps=m['pasos'],
                generator=torch.Generator().manual_seed(seed), **kw).images[0]


# ------------------------------------------------------------------ prompts (biblia visual)
# O importante vai ao principio: CLIP só le 77 tokens e trunca o resto. O estilo é curto.
ESTILOS = {
    'filme': 'cinematic film still, period drama, photorealistic',
    'pintura': 'realistic oil painting, dramatic chiaroscuro',
    'oleo_g2': 'muted oil painting, soft overcast light, grey-green and slate palette',   # o do Gauntlet 2
}
ESTILO_DEFECTO = 'filme'
ESTILO = ESTILOS[ESTILO_DEFECTO] + ', {p}'     # compatibilidade: ESTILO.format(p=...)
# Matiz de estilo por fase (curto: van diante e contan nos 77 tokens). O resto da fase vai na luz e na gradación.
ESTILO_FASE = {'gancho': ', dramatic chiaroscuro', 'transicion': '', 'calma': ', soft light', 'durmir': ', dim and quiet'}
# Luz por defecto de cada fase (só se o prompt do plano non trae ningunha palabra de luz): vaise rotando.
LUZ_FASE = {
    'gancho': ['lit only by firelight, deep black shadows', 'single candle flame in darkness, chiaroscuro',
               'night, flickering torchlight, deep shadows', 'storm clouds, cold flash of lightning, rain'],
    'transicion': ['morning sunlight through mist', 'bright overcast daylight, soft shadows',
                   'low winter sun, long shadows', 'shafts of daylight through a doorway'],
    'calma': ['warm sunset light, golden hour', 'soft rain, grey-blue dusk', 'warm light of an oil lamp',
              'blue hour twilight, first stars'],
    'durmir': ['pale moonlight, deep blue night, soft and dim', 'faint glow of dying embers in darkness',
               'starry night sky, faint mist, very dim', 'mist in the moonlight, soft darkness'],   # r2: sen chama viva
}
# palabras que indican a luz do plano ("dark" non: adoita ser a cor da roupa; "sun" só como luz, non "sunken")
LUZ_RX = (r'\b(light|lit|lighting|glow\w*|sun(light|lit|set|rise|beams?|shine|ny|s)?|moon\w*|candle\w*|fire\w*|'
          r'lamp\w*|torch\w*|dusk|dawn|night\w*|overcast|storm\w*|shadows?|twilight|embers?|backlit|silhouett\w*|'
          r'golden hour|blue hour|daylight|morning|evening|lightning|lantern\w*|hearth)\b')
TIPO_FRASE = {   # tipo de plano (gramática da biblia) -> fórmula de cámara se o prompt non a trae
    'detalle': 'extreme close-up detail shot of', 'primeiro_plano': 'close-up of', 'plano_medio': 'medium shot of',
    'xeral': 'wide establishing shot of', 'contraluz': 'backlit silhouette shot of', 'bodegon': 'still life of',
    'paisaxe': 'wide landscape of',
}
CAMARA_RX = r'\b(close-up|closeup|medium shot|wide shot|establishing|still life|detail|landscape|silhouette|backlit|overhead|portrait|long shot|full shot)\b'
# Correccións ao reintentar, segundo o motivo do rexeitamento. A de iconografía vai ao principio (pesa máis) desde
# o 2.º intento; as colas, ao final desde o intento INTENTO_PRUDENTE, e só para o seu motivo (Gauntlet 2: a cola de
# "figuras de corpo enteiro" engadíase sempre, tamén a paisaxes rexeitadas por tellados).
CORRECCION = [   # (motivo, corrección de exterior, corrección de interior). Versión 6: "green hills" diante dun interior
    # abría un ventanal ás colinas (plano 6 da r1); nun interior a corrección fecha o cuarto.
    (r'tellad|encalad|mediterr|ciprés|oliveir|palmeir|paisaxe seca|eucalipt|rodas|británic|patio|cidade|eléctric',
     'dark slate roofs, low granite houses, ', 'thick granite walls, small shuttered window, '),
    (r'interior moderno|salón', 'thick granite walls, ', 'smoke-blackened granite walls, open stone hearth at floor level, '),
]
INTERIOR_RX = r'\b(kitchen|room|interior|inside|indoors|hall|cell|chamber|byre|stable|table|bench|hearth|fireplace|bed|desk|doorway)\b'
# Prompt negativo dos intentos guiados, segundo o motivo do rexeitamento (e o campo `negativo` do plano)
NEG_MOTIVO = [
    (r'obxectos modernos|eléctric|cidade', 'street lamps, electric lights, lamp posts, city lights, glass'),
    (r'interior moderno|salón', 'sofa, cushions, armchair, mantelpiece, large window, potted plants'),
    (r'tellad|encalad|mediterr|patio|británic', 'orange roof tiles, white walls, arcades, chimneys, sash windows'),
    (r'texto', 'text, letters, writing, open book'),
    (r'multitude|corpos|animais', 'crowd, many people, herd'),
    (r'\bman\b|\bmans\b', 'extra hands, deformed hands, extra fingers'),
    (r'meiga|caldeiro', 'witch, cauldron, potion, pointed hat'),
    (r'lume vivo', 'flames, fire, bright light'),
]
NEG_BASE = 'modern, electric light, text, watermark, deformed'
CFG_REINTENTO = float(os.environ.get('IMG_CFG_REINTENTO', '1.5'))   # 0 = sen intentos guiados
INTENTOS_GUIADOS = (3, 4)      # os intentos 4.º e 5.º dun plano van guiados co prompt negativo
PRUDENTE = [   # (motivo, cola)
    (r'\bman\b|\bmans\b', ', hands hidden in the sleeves or out of frame'),
    (r'multitude|corpos', ', only one or two people'),
    (r'repetida|arquetipo', ', seen from a low angle'),
    (r'texto', ', plain surfaces'),
]
# Planos de reserva por fase: sen persoas (sen mans nin caras), galegos e seguros. Rótanse para non repetir.
RESERVA_FASE = {   # versión 6: fóra de durmir, a reserva ten persoas (un plano con relato non debe acabar nunha paisaxe baleira)
    'gancho': ['medium shot of an old woman in a dark wool headscarf holding a tallow candle in a dark granite room, her face lit by the small flame, deep black shadows',
               'close-up of an old man in a coarse wool cloak beside an open stone hearth at floor level at night, firelight on his face, smoke'],
    'transicion': ['medium shot of a farmer in a wool jacket resting against a mossy granite wall, green fields, bright overcast daylight',
                   'medium shot of a woman in a dark wool skirt and headscarf carrying a wicker basket of chestnuts past a granite wall, morning mist'],
    'calma': ['medium shot of an old woman in a brown wool shawl spinning wool by the warm light of a small iron oil lamp, dark granite wall',
              'rain falling on dark grey slate roofs of low granite houses at dusk, soft blue light'],
    'durmir': ['an ancient oak forest at night, mist between mossy trunks, pale moonlight, very dim',
               'extreme close-up detail of dying embers and grey ash on a granite hearth stone, faint red glow, soft darkness'],
}
XENERICO = RESERVA_FASE['transicion'][1]          # compatibilidade (pipeline.py enche con el os planos sen prompt)
COR_LLM = r'\b(sepia|neon|vivid|vibrant|saturated|purple|pink|hdr)\b'   # só nos prompts sen fase (LLM do pipeline curto)
SIM_MAX, CAP_MAX, VECIÑOS = 0.6, 0.5, 4        # porta de repetición antiga (grises 48x27): contra as 4 anteriores


def compor_prompt(e, i=0, intento=0, problemas=(), m=None):
    """Prompt final dun plano: estilo común e o seu matiz de fase + (corrección polo motivo do rexeitamento) + fórmula de cámara do
    `tipo` se o prompt non a trae + prompt do plano (sen tocar a luz nin a cor se vén co campo `fase`, é dicir,
    dun axente que segue a biblia) + luz do campo `luz` ou, se o prompt non ten luz, a luz por defecto da fase."""
    fase = e.get('fase')
    p = re.sub(r'\s+', ' ', str(e['prompt'])).strip().rstrip('.')
    if not fase:
        p = re.sub(r'\s+', ' ', re.sub(COR_LLM, '', p, flags=re.I)).strip()
    tipo = e.get('tipo')
    if tipo in TIPO_FRASE and not re.search(CAMARA_RX, p, re.I):
        p = f'{TIPO_FRASE[tipo]} {p}'
    luz = e.get('luz')
    if luz and luz.lower() not in p.lower():
        p = f'{p}, {luz}'
    elif not luz and not re.search(LUZ_RX, p, re.I):
        opcions = LUZ_FASE.get(fase or 'transicion')
        p = f'{p}, {opcions[i % len(opcions)]}'
    pre = ''
    txt_prob = ' '.join(problemas).lower()
    interior = bool(re.search(INTERIOR_RX, str(e['prompt']), re.I))
    for rx, ext, inte in CORRECCION:
        if intento >= 1 and re.search(rx, txt_prob):
            pre += inte if interior else ext
    estilo = ESTILOS[os.environ.get('IMG_ESTILO', ESTILO_DEFECTO)] + ESTILO_FASE.get(fase or '', '')
    pr = f'{estilo}, {pre}{p}'
    if intento >= INTENTO_PRUDENTE:
        for rx, cola in PRUDENTE:
            if re.search(rx, txt_prob):
                pr += cola; break
    return pr


def negativo_para(e, problemas):
    """Prompt negativo dun intento guiado: o campo `negativo` do plano + o dos motivos de rexeitamento + un común."""
    txt = ' '.join(problemas).lower()
    partes = [str(e.get('negativo') or '')] + [n for rx, n in NEG_MOTIVO if re.search(rx, txt)] + [NEG_BASE]
    return ', '.join(x for x in partes if x)


def tokens(pipe, texto):
    """Número de tokens de CLIP (con BOS e EOS) e a parte que se perde por pasar de 77."""
    ids = pipe.tokenizer(texto, truncation=False).input_ids
    if len(ids) <= 77:
        return len(ids), ''
    return len(ids), pipe.tokenizer.decode(ids[76:-1])


# ------------------------------------------------------------------ xeración con porta
def _teimudo(intentos):
    """O problema é do prompt e non da semente: os dous últimos intentos (sen reserva) repiten un arquetipo ou
    unha imaxe xa aceptada. Non paga a pena gastar máis intentos: pásase á reserva da fase."""
    ult = [x for x in intentos if not x.get('reserva')][-2:]
    return len(ult) == 2 and all(any(p.startswith(('arquetipo', 'repetida (CLIP')) for p in x['problemas']) for x in ult)


def xerar(escenas, outdir, seed_base='sera', revisar=True, n_total=None):
    """escenas: [{'prompt', opcionais 'fase' (gancho|transicion|calma|durmir), 'u', 'luz', 'tipo', 'negativo'}].
    n_total: planos do episodio para os topes de arquetipos (por defecto, len(escenas); nunha mostra, o do episodio).
    Devolve (rutas das imaxes escollidas, rexistro por plano). Garda todo en outdir/revision.json e retoma."""
    import numpy as np
    import revisor as _rv
    outdir = Path(outdir); outdir.mkdir(parents=True, exist_ok=True)
    rexf = outdir / 'revision.json'
    feito = json.loads(rexf.read_text()) if rexf.exists() else {}
    m = modelo()
    pipe = rev = clip = None
    paths, rexistro = [], []
    aceptadas = []                       # (vector de grises, raíces da descrición): porta de repetición antiga
    emb_aceptadas, arquetipos = [], []   # CLIP: imaxes escollidas de todos os planos anteriores e o seu arquetipo
    n_total = n_total or len(escenas)
    reservas_usadas = {}
    for i, e in enumerate(escenas):
        clave = f"{i:03d}-{hashlib.sha256((e['prompt'] + m['nome'] + str(e.get('fase'))).encode()).hexdigest()[:8]}"
        previo = feito.get(clave)
        vella = previo and previo.get('version_revisor') != _rv.VERSION and revisar
        embs = {}                        # ficheiro -> (embedding, arquetipo) dos intentos revisados agora
        novo = not (previo and not vella and (outdir / previo['ficheiro']).exists() and
                    (previo['ok'] or len(previo['intentos']) >= MAX_INTENTOS + RESERVAS))
        if not novo:
            r = previo
        else:
            import torch
            torch.set_num_threads(int(os.environ.get('NTH', '4')))
            if rev is None and revisar:
                rev = _rv.Revisor()
            intentos = list(previo['intentos']) if previo else []     # continúa onde quedou
            ctx = {'negativo': e.get('negativo'), 'clave': e.get('clave'), 'fase': e.get('fase')}
            if intentos and rev is not None:     # o revisor cambiou desde entón: volve revisar os intentos gardados
                for it in intentos:
                    rv = rev.revisar(outdir / it['ficheiro'], prompt=it.get('prompt'), **ctx)
                    embs[it['ficheiro']] = (rv['clip_emb'], rv.get('arquetipo'))
                    novos = rv['problemas'] + rev.repeticion(rv['clip_emb'], emb_aceptadas, arquetipos,
                                                             rv.get('arquetipo'), n_total)
                    if novos != it['problemas']:
                        it['problemas_revision_anterior'] = it['problemas']
                        it.update({k2: v for k2, v in rv.items() if k2 not in ('ok', 'clip_emb')})
                        it['problemas'] = novos
                        print(f"imaxe {i:3d} intento {it['intento']} revisado de novo: {novos or 'ok'}", flush=True)
            k = len(intentos)
            while k < MAX_INTENTOS + RESERVAS and not any(not x['problemas'] for x in intentos):
                if k < MAX_INTENTOS and _teimudo(intentos):
                    k = MAX_INTENTOS
                previos = [p for x in intentos for p in x['problemas']]
                if k >= MAX_INTENTOS:     # reserva segura da fase, sen persoas; rótase para non repetir
                    fase = e.get('fase') or 'transicion'
                    j = reservas_usadas.get(fase, 0); reservas_usadas[fase] = j + 1
                    base = {'prompt': RESERVA_FASE[fase][j % len(RESERVA_FASE[fase])], 'fase': e.get('fase')}
                    pr = compor_prompt(base, i, 0, (), m)
                else:
                    pr = compor_prompt(e, i, k, previos, m)
                guiado = k in INTENTOS_GUIADOS and CFG_REINTENTO > 1 and k < MAX_INTENTOS
                neg = negativo_para(e, previos) if guiado else None
                seed = int(hashlib.sha256(f'{seed_base}-{i}-{pr}-{k}'.encode()).hexdigest()[:8], 16)
                if pipe is None:
                    pipe = cargar_pipe()
                ntok, perdido = tokens(pipe, pr)
                f = outdir / f'{clave}-{k}.png'
                t = time.time()
                im = xerar_unha(pipe, pr, seed, m, negativo=neg, cfg=CFG_REINTENTO if guiado else 0.0)
                tmp = f.with_suffix('.tmp.png'); im.save(tmp); os.replace(tmp, f)
                it = {'intento': k, 'ficheiro': f.name, 'seed': seed, 's': round(time.time() - t, 1), 'prompt': pr,
                      'modelo': m['nome'], 'tokens': ntok, 'truncado': perdido, 'problemas': [],
                      'reserva': k >= MAX_INTENTOS, 'negativo_guiado': neg}
                if rev is not None:
                    # a reserva é outro motivo: non se lle pide a `clave` do plano (fallo visto na folla r2)
                    ctx_k = dict(ctx, clave=None) if k >= MAX_INTENTOS else ctx
                    t = time.time(); rv = rev.revisar(f, prompt=pr, **ctx_k)
                    embs[f.name] = (rv['clip_emb'], rv.get('arquetipo'))
                    it.update({k2: v for k2, v in rv.items() if k2 not in ('ok', 'clip_emb')})
                    it['problemas'] = rv['problemas'] + rev.repeticion(rv['clip_emb'], emb_aceptadas, arquetipos,
                                                                       rv.get('arquetipo'), n_total)
                    it['s_revision'] = round(time.time() - t, 1)
                rep = repetida(f, it.get('descricion', ''), aceptadas)
                if rep:
                    it['problemas'] = it['problemas'] + [rep]
                intentos.append(it)
                print(f"imaxe {i:3d} intento {k} {it['s']:5.1f}s + revisión {it.get('s_revision', 0):4.1f}s "
                      f"{it['problemas'] or 'ok'}", flush=True)
                k += 1
            best = min(range(len(intentos)), key=lambda j: (len(intentos[j]['problemas']), j))
            r = {'ficheiro': intentos[best]['ficheiro'], 'escollida': best, 'ok': not intentos[best]['problemas'],
                 'intentos': intentos, 'version_revisor': _rv.VERSION, 'modelo': m['nome'], 'fase': e.get('fase')}
            feito[clave] = r
            tmpj = rexf.with_suffix('.tmp'); tmpj.write_text(json.dumps(feito, ensure_ascii=False, indent=1))
            os.replace(tmpj, rexf)
        esc = r['intentos'][r['escollida']]
        fich = outdir / r['ficheiro']
        if not novo:     # imaxe gardada: volve pasar as portas de repetición contra o episodio de agora
            probs = [x for x in [repetida(fich, esc.get('descricion', ''), aceptadas)] if x]
        if revisar:
            if r['ficheiro'] in embs:
                emb, arq = embs[r['ficheiro']]
            else:
                if clip is None:
                    clip = rev.clip if rev is not None and rev.clip is not None else _rv.Clip()
                emb = clip.imaxe(fich); arq = clip.arquetipo(emb)
            if not novo:
                probs += _rv.repeticion(emb, emb_aceptadas, arquetipos, arq, n_total)
            emb_aceptadas.append(emb); arquetipos.append(arq)
        if not novo and probs and r['ok']:
            r = dict(r, ok=False, problemas_episodio=probs)
        aceptadas.append(firma(fich, esc.get('descricion', '')))
        paths.append(str(fich)); rexistro.append(r)
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
    """Porta de repetición do Gauntlet 2 (barata): a imaxe non pode parecerse de máis a ningunha das VECIÑOS
    anteriores (composición: correlación da imaxe en grises desenfocada a 48x27 > SIM_MAX; contido: Jaccard das
    palabras da descrición de Florence-2 > CAP_MAX). A porta de CLIP (revisor.repeticion) mira todo o episodio."""
    if not aceptadas:
        return None
    v, cap = firma(f, descricion)
    for k, (v2, cap2) in enumerate(aceptadas[-VECIÑOS:][::-1]):
        sim = float(v @ v2)
        jac = len(cap & cap2) / max(1, len(cap | cap2)) if cap and cap2 else 0
        if sim > SIM_MAX or jac > CAP_MAX:
            return f'repetida (parécese ao plano -{k + 1}: composición {sim:.2f}, descrición {jac:.2f})'
    return None


# ------------------------------------------------------------------ gradación por fase
# Obxectivo de cada fase (biblia visual): rango de luminancia media (0-1, sRGB) e saturación. A luz de cada imaxe
# consérvase: só se corrixen os extremos (unha imaxe fóra do rango lévase ata o bordo, non á media do episodio).
# croma = media de |RGB - luminancia|: nas 55 imaxes da comparativa, mediana 0,043 e máximo 0,099 (un prado verde ao sol);
# os "verdes de videoxogo" da ronda 2 dan 0,057 despois da brétema da montaxe. O tope só actúa nos extremos.
LOOK = {   # toe: nivel de negro (0 = negros profundos do claroscuro; máis alto = negros levantados, baixo contraste)
    'gancho':     {'lum': (0.13, 0.45), 'sat': 1.00, 'croma_max': 0.100, 'toe': 0.000},
    'transicion': {'lum': (0.25, 0.58), 'sat': 0.97, 'croma_max': 0.085, 'toe': 0.008},
    # versión 6 (veredicto visual-r1: a calma e o durmir saían tan luminosos coma o gancho): teitos máis baixos
    'calma':      {'lum': (0.15, 0.33), 'sat': 0.88, 'croma_max': 0.075, 'toe': 0.012},
    'durmir':     {'lum': (0.06, 0.18), 'sat': 0.60, 'croma_max': 0.050, 'toe': 0.020},
}
FILME = {'ombro': 0.86, 'sombra': (-0.008, 0.002, 0.010), 'luz': (0.012, 0.004, -0.010)}
SUAVIZADO = 60   # xanela triangular de ±60 palabras (~30 s de narración) nos parámetros: as fases cambian sen saltos


def _parametros(escenas, n):
    """Parámetros de gradación por plano: os da fase (LOOK) e os da curva (contraste, brillo), suavizados."""
    import curva
    crus = []
    tot = None
    if escenas:
        est = [e['pal0'] / e['u'] for e in escenas if e.get('u') and e.get('pal0')]
        tot = round(sum(est) / len(est)) if est else None
    for k in range(n):
        e = escenas[k] if escenas and k < len(escenas) else {}
        fase = e.get('fase') or 'transicion'
        lk = LOOK.get(fase, LOOK['transicion'])
        if tot and e.get('pal0') is not None:
            c = curva.en(e['pal0'], tot)
            con, bri = c['contraste'], c['brillo']
        else:
            con, bri = 1.0, 1.0
        crus.append([lk['lum'][0], lk['lum'][1], lk['sat'], lk['croma_max'], con, bri, lk['toe']])
    # suavizado: media ponderada cos planos veciños segundo a distancia en palabras (sen posición: ±1 plano)
    pos = [(escenas[k].get('pal0') if escenas and k < len(escenas) else None) for k in range(n)]
    out = []
    for k in range(n):
        if pos[k] is not None:
            ws = [(max(0.0, 1 - abs(pos[j] - pos[k]) / SUAVIZADO) if pos[j] is not None else 0.0) for j in range(n)]
        else:
            ws = [1.0 if abs(j - k) <= 1 else 0.0 for j in range(n)]
        tw = sum(ws)
        out.append([sum(w * v[j] for w, v in zip(ws, crus)) / tw for j in range(7)])
    return out


def graduar(paths, outdir, escenas=None, **_):
    """Gradación por fase (Gauntlet 3). Substitúe a igualación á media do episodio do Gauntlet 2, que aplanaba a
    luz. Por imaxe: (1) se a luminancia media sae do rango da fase, lévase cara ao bordo cunha gamma; (2) contraste
    arredor da súa propia media e brillo da curva do embude (curva.py), ombreiro suave nas altas luces e nivel de
    negro da fase (negros profundos no gancho, levantados ao durmir); (3) saturación da fase e tope de croma (evita
    os verdes de videoxogo); (4) un virado común lixeiro (sombras frías, luces cálidas) que dá unidade sen igualar
    as cores.
    Os parámetros suavízanse entre planos veciños, así que o paso dunha fase a outra é gradual."""
    import numpy as np
    from PIL import Image
    outdir = Path(outdir); outdir.mkdir(parents=True, exist_ok=True)
    par = _parametros(escenas, len(paths))
    out, rex = [], []
    for p, (lo, hi, sat, croma_max, con, bri, toe) in zip(paths, par):
        x = np.asarray(Image.open(p).convert('RGB'), np.float32) / 255
        L = x @ np.array([0.2126, 0.7152, 0.0722], np.float32)
        mu = float(L.mean())
        # (1) extremos de luminancia: gamma que leva a media ata o bordo do rango da fase
        g = 1.0
        if mu < lo:
            g = math.log(lo) / math.log(max(mu, 1e-3))
        elif mu > hi:
            g = math.log(hi) / math.log(mu)
        g = min(max(g, 0.55), 1.8)
        x = np.clip(x, 0, 1) ** g
        L = x @ np.array([0.2126, 0.7152, 0.0722], np.float32)
        mu2 = float(L.mean())
        # (2) contraste arredor da media propia e brillo (en luz lineal aproximada)
        L2 = mu2 + (L - mu2) * con
        L2 = L2 * bri ** (1 / 2.2)
        # ombreiro suave nas altas luces e negros non puros
        sh = FILME['ombro']
        L2 = np.where(L2 > sh, sh + (1 - sh) * np.tanh((L2 - sh) / (1 - sh)), L2)
        L2 = toe + (1 - toe) * np.clip(L2, 0, 1)
        ratio = (L2 + 1e-4) / (L + 1e-4)
        y = x * ratio[..., None]
        # (3) saturación da fase e tope de croma
        Ly = (y @ np.array([0.2126, 0.7152, 0.0722], np.float32))[..., None]
        croma = float(np.abs(y - Ly).mean())
        s = sat * (min(1.0, croma_max / croma) if croma > croma_max else 1.0)
        y = Ly + (y - Ly) * s
        # (4) virado común: sombras frías, luces cálidas (pouco)
        w = np.clip(Ly, 0, 1)
        y = y + (1 - w) * (1 - w) * np.array(FILME['sombra'], np.float32) + w * np.array(FILME['luz'], np.float32)
        y = np.clip(y, 0, 1)
        q = outdir / Path(p).name
        tmp = q.with_suffix('.tmp.png')
        Image.fromarray((y * 255 + 0.5).astype(np.uint8)).save(tmp); os.replace(tmp, q)
        out.append(str(q))
        rex.append({'imaxe': Path(p).name, 'lum_orixe': round(mu, 3), 'gamma': round(g, 3), 'contraste': round(con, 3),
                    'toe': round(toe, 4),
                    'brillo': round(bri, 3), 'saturacion': round(s, 3), 'croma_orixe': round(croma, 3),
                    'lum_final': round(float((y @ np.array([0.2126, 0.7152, 0.0722], np.float32)).mean()), 3)})
    (outdir / 'graduacion.json').write_text(json.dumps(rex, ensure_ascii=False, indent=1))
    return out
