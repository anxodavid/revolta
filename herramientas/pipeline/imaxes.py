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
        with safe_open(hf_hub_download(LIGHTNING, m['unet']), framework='pt') as g:   # tensor a tensor: pico de RAM ~5 GB
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


def xerar_unha(pipe, prompt, seed, m=None):
    import torch
    m = m or getattr(pipe, '_revolta', M)
    return pipe(prompt=prompt, width=m['W'], height=m['H'], num_inference_steps=m['pasos'], guidance_scale=0.0,
                generator=torch.Generator().manual_seed(seed)).images[0]


# ------------------------------------------------------------------ prompts (biblia visual)
# O importante vai ao principio: CLIP só le 77 tokens e trunca o resto. O estilo é curto.
ESTILOS = {
    'filme': 'cinematic film still, period drama, photorealistic',
    'pintura': 'realistic oil painting, dramatic chiaroscuro',
    'oleo_g2': 'muted oil painting, soft overcast light, grey-green and slate palette',   # o do Gauntlet 2
}
ESTILO_DEFECTO = 'filme'
ESTILO = ESTILOS[ESTILO_DEFECTO] + ', {p}'     # compatibilidade: ESTILO.format(p=...)
# Luz por defecto de cada fase (só se o prompt do plano non trae ningunha palabra de luz): vaise rotando.
LUZ_FASE = {
    'gancho': ['lit only by firelight, deep black shadows', 'single candle flame in darkness, chiaroscuro',
               'night, flickering torchlight, deep shadows', 'storm clouds, cold flash of lightning, rain'],
    'transicion': ['morning sunlight through mist', 'bright overcast daylight, soft shadows',
                   'low winter sun, long shadows', 'shafts of daylight through a doorway'],
    'calma': ['warm sunset light, golden hour', 'soft rain, grey-blue dusk', 'warm light of an oil lamp',
              'blue hour twilight, first stars'],
    'durmir': ['pale moonlight, deep blue night, soft and dim', 'faint glow of embers in darkness',
               'starry night sky, faint mist, very dim', 'a single dim candle, soft darkness'],
}
LUZ_RX = (r'\b(light|lit|lighting|glow\w*|sun\w*|moon\w*|candle\w*|fire\w*|lamp\w*|torch\w*|dusk|dawn|night\w*|'
          r'overcast|storm\w*|shadow\w*|twilight|ember\w*|backlit|silhouett\w*|golden hour|blue hour|dark\w*|'
          r'daylight|morning|evening|lightning|lantern\w*|hearth)\b')
TIPO_FRASE = {   # tipo de plano (gramática da biblia) -> fórmula de cámara se o prompt non a trae
    'detalle': 'extreme close-up detail shot of', 'primeiro_plano': 'close-up of', 'plano_medio': 'medium shot of',
    'xeral': 'wide establishing shot of', 'contraluz': 'backlit silhouette shot of', 'bodegon': 'still life of',
    'paisaxe': 'wide landscape of',
}
CAMARA_RX = r'\b(close-up|closeup|medium shot|wide shot|establishing|still life|detail|landscape|silhouette|overhead|portrait|long shot|full shot)\b'
# Correccións ao reintentar, segundo o motivo do rexeitamento (van ao principio: pesan máis)
CORRECCION = [
    (r'tellados|encalados|mediterr|iconograf', 'dark grey slate roofs, bare granite stone walls, green Atlantic landscape, '),
    (r'multitude|arquetipo', ''),
]
PRUDENTE = {   # colas que se engaden ao final desde o intento INTENTO_PRUDENTE, segundo o motivo
    'man': ', hands hidden in the sleeves or out of frame',
    'corpos': ', only one or two people',
    'multitude': ', only one or two people, no crowd',
    'xeral': ', full-body figures seen from a few metres away, hands not in focus',
}
# Planos de reserva por fase: sen persoas (sen mans nin caras), galegos e seguros. Rótanse para non repetir.
RESERVA_FASE = {
    'gancho': ['still life of a candle burning on a rough oak table in a dark granite room, deep shadows',
               'an iron pot hanging over the embers of an open stone hearth at night, firelight, smoke'],
    'transicion': ['a moss-covered granite wayside cross beside a stone wall, green fields, morning mist',
                   'dry-stone walls and small green fields on a hillside, oak trees, bright overcast daylight'],
    'calma': ['rain falling on dark grey slate roofs of granite houses at dusk, soft blue light',
              'a quiet river with an old stone bridge among oak trees, warm evening light'],
    'durmir': ['an ancient oak forest at night, mist between mossy trunks, pale moonlight, very dim',
               'glowing embers in a stone hearth in a dark kitchen, faint red glow'],
}
XENERICO = RESERVA_FASE['transicion'][1]          # compatibilidade (pipeline.py enche con el os planos sen prompt)
COR_LLM = r'\b(sepia|neon|vivid|vibrant|saturated|purple|pink|hdr)\b'   # só nos prompts sen fase (LLM do pipeline curto)
SIM_MAX, CAP_MAX, VECIÑOS = 0.6, 0.5, 4        # porta de repetición antiga (grises 48x27): contra as 4 anteriores


def compor_prompt(e, i=0, intento=0, problemas=(), m=None):
    """Prompt final dun plano: estilo común + (corrección polo motivo do rexeitamento) + fórmula de cámara do
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
    for rx, extra in CORRECCION:
        if extra and re.search(rx, txt_prob) and intento >= 1:
            pre += extra
    estilo = ESTILOS[os.environ.get('IMG_ESTILO', ESTILO_DEFECTO)]
    pr = f'{estilo}, {pre}{p}'
    if intento >= INTENTO_PRUDENTE:
        claves = [k for k in PRUDENTE if k in txt_prob] or ['xeral']
        pr += PRUDENTE[claves[0]]
    return pr


def tokens(pipe, texto):
    """Número de tokens de CLIP (con BOS e EOS) e a parte que se perde por pasar de 77."""
    ids = pipe.tokenizer(texto, truncation=False).input_ids
    if len(ids) <= 77:
        return len(ids), ''
    return len(ids), pipe.tokenizer.decode(ids[76:-1])


# ------------------------------------------------------------------ xeración con porta
def xerar(escenas, outdir, seed_base='sera', revisar=True):
    """escenas: [{'prompt', opcionais 'fase' (gancho|transicion|calma|durmir), 'u', 'luz', 'tipo', 'negativo'}].
    Devolve (rutas das imaxes escollidas, rexistro por plano). Garda todo en outdir/revision.json e retoma."""
    import revisor as _rv
    outdir = Path(outdir); outdir.mkdir(parents=True, exist_ok=True)
    rexf = outdir / 'revision.json'
    feito = json.loads(rexf.read_text()) if rexf.exists() else {}
    m = modelo()
    pipe = rev = clip = None
    paths, rexistro = [], []
    aceptadas = []     # (vector de grises, raíces da descrición) para a porta de repetición antiga
    emb_aceptadas, arquetipos = [], []   # CLIP: todas as imaxes aceptadas do episodio e o seu arquetipo
    n_total = len(escenas)
    reservas_usadas = {}

    def clip_de():
        nonlocal clip, rev
        if rev is not None and rev.clip is not None:
            return rev.clip
        if clip is None:
            clip = _rv.Clip()
        return clip

    for i, e in enumerate(escenas):
        clave = f"{i:03d}-{hashlib.sha256((e['prompt'] + m['nome'] + str(e.get('fase'))).encode()).hexdigest()[:8]}"
        previo = feito.get(clave)
        vella = previo and previo.get('version_revisor') != _rv.VERSION and revisar
        if previo and not vella and (outdir / previo['ficheiro']).exists() and \
                (previo['ok'] or len(previo['intentos']) >= MAX_INTENTOS + RESERVAS):
            r = previo
        else:
            import torch
            torch.set_num_threads(int(os.environ.get('NTH', '4')))
            if rev is None and revisar:
                rev = _rv.Revisor()
            intentos = list(previo['intentos']) if previo else []     # continúa onde quedou
            contexto = {'negativo': e.get('negativo'), 'n_total': n_total, 'fase': e.get('fase')}
            if intentos and rev is not None:     # se o revisor cambiou desde entón, volve revisar os intentos gardados
                for it in intentos:
                    rv = rev.revisar(outdir / it['ficheiro'], **contexto)
                    rep = rev.repeticion(rv['clip_emb'], emb_aceptadas, arquetipos, rv.get('arquetipo'), n_total)
                    novos = rv['problemas'] + rep
                    if novos != it['problemas']:
                        it['problemas_revision_anterior'] = it['problemas']; it['problemas'] = novos
                        it.update({k: v for k, v in rv.items() if k not in ('problemas', 'ok', 'clip_emb')})
                        print(f"imaxe {i:3d} intento {it['intento']} revisado de novo: {novos or 'ok'}", flush=True)
            for k in range(len(intentos), MAX_INTENTOS + RESERVAS):
                if any(not x['problemas'] for x in intentos):
                    break
                previos = [p for x in intentos for p in x['problemas']]
                if k >= MAX_INTENTOS:     # reserva segura da fase, sen persoas; rótase para non repetir
                    fase = e.get('fase') or 'transicion'
                    j = reservas_usadas.get(fase, 0); reservas_usadas[fase] = j + 1
                    base = dict(e, prompt=RESERVA_FASE[fase][j % len(RESERVA_FASE[fase])], tipo=None, luz=None)
                    pr = compor_prompt(base, i, 0, (), m)
                else:
                    pr = compor_prompt(e, i, k, previos, m)
                seed = int(hashlib.sha256(f'{seed_base}-{i}-{pr}-{k}'.encode()).hexdigest()[:8], 16)
                if pipe is None:
                    pipe = cargar_pipe()
                ntok, perdido = tokens(pipe, pr)
                f = outdir / f'{clave}-{k}.png'
                t = time.time()
                im = xerar_unha(pipe, pr, seed, m)
                tmp = f.with_suffix('.tmp.png'); im.save(tmp); os.replace(tmp, f)
                it = {'intento': k, 'ficheiro': f.name, 'seed': seed, 's': round(time.time() - t, 1), 'prompt': pr,
                      'modelo': m['nome'], 'tokens': ntok, 'truncado': perdido, 'problemas': [],
                      'reserva': k >= MAX_INTENTOS}
                if rev is not None:
                    t = time.time(); rv = rev.revisar(f, **contexto)
                    rep = rev.repeticion(rv['clip_emb'], emb_aceptadas, arquetipos, rv.get('arquetipo'), n_total)
                    it.update({k2: v for k2, v in rv.items() if k2 not in ('ok', 'clip_emb')})
                    it['problemas'] = rv['problemas'] + rep
                    it['s_revision'] = round(time.time() - t, 1)
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
                 'intentos': intentos, 'version_revisor': _rv.VERSION, 'modelo': m['nome'], 'fase': e.get('fase')}
            feito[clave] = r
            tmpj = rexf.with_suffix('.tmp'); tmpj.write_text(json.dumps(feito, ensure_ascii=False, indent=1))
            os.replace(tmpj, rexf)
        esc = r['intentos'][r['escollida']]
        # as imaxes gardadas dunha versión anterior tamén pasan as portas de repetición
        rep = repetida(outdir / r['ficheiro'], esc.get('descricion', ''), aceptadas)
        if revisar:
            cl = clip_de()
            emb = cl.imaxe(outdir / r['ficheiro'])
            arq = cl.arquetipo(emb)
            rep2 = [] if 'problemas' in esc and not esc['problemas'] and previo is None else \
                _rv.repeticion(emb, emb_aceptadas, arquetipos, arq, n_total)
            if (rep or rep2) and r['ok'] and previo is not None:
                r = dict(r, ok=False); esc['problemas'] = ([rep] if rep else []) + rep2
            emb_aceptadas.append(emb); arquetipos.append(arq)
        aceptadas.append(firma(outdir / r['ficheiro'], esc.get('descricion', '')))
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
LOOK = {
    'gancho':     {'lum': (0.13, 0.45), 'sat': 1.00, 'croma_max': 0.16},
    'transicion': {'lum': (0.25, 0.58), 'sat': 0.97, 'croma_max': 0.14},
    'calma':      {'lum': (0.18, 0.48), 'sat': 0.92, 'croma_max': 0.13},
    'durmir':     {'lum': (0.08, 0.30), 'sat': 0.80, 'croma_max': 0.10},
}
FILME = {'toe': 0.012, 'ombro': 0.86, 'sombra': (-0.010, 0.002, 0.012), 'luz': (0.012, 0.004, -0.010)}
SUAVIZADO = 3    # media móbil de ±3 planos nos parámetros: as fases cambian sen saltos


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
        crus.append([lk['lum'][0], lk['lum'][1], lk['sat'], lk['croma_max'], con, bri])
    out = []
    for k in range(n):
        viz = crus[max(0, k - SUAVIZADO): k + SUAVIZADO + 1]
        out.append([sum(v[j] for v in viz) / len(viz) for j in range(6)])
    return out


def graduar(paths, outdir, escenas=None, **_):
    """Gradación por fase (Gauntlet 3). Substitúe a igualación á media do episodio do Gauntlet 2, que aplanaba a
    luz. Por imaxe: (1) se a luminancia media sae do rango da fase, lévase cara ao bordo cunha gamma; (2) contraste
    arredor da súa propia media e brillo da curva do embude (curva.py); (3) saturación da fase e tope de croma
    (evita os verdes de videoxogo); (4) aspecto común de filme: negros non puros, ombreiro suave nas altas luces e
    un virado lixeiro (sombras frías, luces cálidas) que dá unidade sen igualar as cores.
    Os parámetros suavízanse entre planos veciños, así que o paso dunha fase a outra é gradual."""
    import numpy as np
    from PIL import Image
    outdir = Path(outdir); outdir.mkdir(parents=True, exist_ok=True)
    par = _parametros(escenas, len(paths))
    out, rex = [], []
    for p, (lo, hi, sat, croma_max, con, bri) in zip(paths, par):
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
        L2 = FILME['toe'] + (1 - FILME['toe']) * np.clip(L2, 0, 1)
        ratio = (L2 + 1e-4) / (L + 1e-4)
        y = x * ratio[..., None]
        # (3) saturación da fase e tope de croma
        Ly = (y @ np.array([0.2126, 0.7152, 0.0722], np.float32))[..., None]
        croma = float(np.abs(y - Ly).mean())
        s = sat * (min(1.0, croma_max / croma) if croma > croma_max else 1.0)
        y = Ly + (y - Ly) * s
        # (4) virado común: sombras frías, luces cálidas (pouco)
        w = np.clip(Ly, 0, 1)
        y = y + (1 - w) * np.array(FILME['sombra'], np.float32) + w * np.array(FILME['luz'], np.float32)
        y = np.clip(y, 0, 1)
        q = outdir / Path(p).name
        tmp = q.with_suffix('.tmp.png')
        Image.fromarray((y * 255 + 0.5).astype(np.uint8)).save(tmp); os.replace(tmp, q)
        out.append(str(q))
        rex.append({'imaxe': Path(p).name, 'lum_orixe': round(mu, 3), 'gamma': round(g, 3), 'contraste': round(con, 3),
                    'brillo': round(bri, 3), 'saturacion': round(s, 3), 'croma_orixe': round(croma, 3),
                    'lum_final': round(float((y @ np.array([0.2126, 0.7152, 0.0722], np.float32)).mean()), 3)})
    (outdir / 'graduacion.json').write_text(json.dumps(rex, ensure_ascii=False, indent=1))
    return out
