"""Imaxe a vídeo (I2V) en CPU para a etapa MOVEMENTO: LTX-Video 2B 0.9.8 destilado.

Corre no venv de vídeo (`$SCRATCH/video/venv`: torch 2.14.1+cpu, diffusers 0.40.0, transformers 5.18.0), non no
principal. Dúas fases en procesos distintos para non ter os dous modelos grandes en memoria á vez:

    python movemento_i2v.py texto PLANOS.json     # embeddings de T5-XXL (fp8, cálculo fp32) das accións que falten
    python movemento_i2v.py xerar PLANOS.json     # clips que falten na caché (movemento.i2v_ficheiro)

PLANOS.json: lista de planos (formato da lista de planos v2) ou [{"imaxe", "accion", "i2v": {parámetros}}]; só se
usan os que teñen `animacion.modo == "i2v"` (ou os que traen `imaxe` e `accion` directamente). A imaxe vai en
`imaxe` (ruta) ou se pasa `--imaxes DIR` co patrón NNN-*.{png,jpg} da caché de imaxes (n - 1).

Cada clip colle o candado de CPU ($CPU_LOCK) só mentres se xera: outras pezas poden pasar entre clip e clip.
**Non lanzalo dentro de `flock $CPU_LOCK`**: o candado xa o colle el e quedaría bloqueado esperando por si mesmo.
Medidas medidas o 02-10-2026 (4 núcleos sen bf16): ver plan-de-negocio/gauntlet4/movemento/informe-r1.md.
Licenza do modelo: LTXV Open Weights License 0.X (uso comercial permitido a entidades con < 10 M$ de ingresos
anuais; restricións de uso do anexo A, entre elas avisar de que o contido é xerado por máquina).
"""
import fcntl, glob, hashlib, json, os, sys, threading, time
from contextlib import contextmanager
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import movemento as M                                                    # noqa: E402

SCR = os.environ.get('SCRATCH', '/tmp/revolta-scratch')
HF = os.environ.get('VIDEO_HF_HOME', f'{SCR}/video/hf') + '/hub'
LTX_REPO, LTX_FICH = 'Lightricks/LTX-Video', 'ltxv-2b-0.9.8-distilled.safetensors'
T5_REPO, T5_FICH = 'comfyanonymous/flux_text_encoders', 't5xxl_fp8_e4m3fn.safetensors'
MAX_LEN = 256
EMB_DIR = Path(os.environ.get('EMB_DIR', f'{SCR}/video/emb'))

# Configuracións de diffusers de Lightricks/LTX-Video-0.9.5 (mesma arquitectura que o 2B 0.9.6-0.9.8)
CFG_TR = {"activation_fn": "gelu-approximate", "attention_bias": True, "attention_head_dim": 64,
          "attention_out_bias": True, "caption_channels": 4096, "cross_attention_dim": 2048, "in_channels": 128,
          "norm_elementwise_affine": False, "norm_eps": 1e-06, "num_attention_heads": 32, "num_layers": 28,
          "out_channels": 128, "patch_size": 1, "patch_size_t": 1, "qk_norm": "rms_norm_across_heads"}
CFG_VAE = {"block_out_channels": [128, 256, 512, 1024, 2048], "decoder_block_out_channels": [256, 512, 1024],
           "decoder_causal": False, "decoder_inject_noise": [False, False, False, False],
           "decoder_layers_per_block": [5, 5, 5, 5], "decoder_spatio_temporal_scaling": [True, True, True],
           "down_block_types": ["LTXVideo095DownBlock3D"] * 4,
           "downsample_type": ["spatial", "temporal", "spatiotemporal", "spatiotemporal"], "encoder_causal": True,
           "in_channels": 3, "latent_channels": 128, "layers_per_block": [4, 6, 6, 2, 2], "out_channels": 3,
           "patch_size": 4, "patch_size_t": 1, "resnet_norm_eps": 1e-06, "scaling_factor": 1.0,
           "spatial_compression_ratio": 32, "spatio_temporal_scaling": [True, True, True, True],
           "temporal_compression_ratio": 8, "timestep_conditioning": True, "upsample_factor": [2, 2, 2],
           "upsample_residual": [True, True, True]}
# Pasos do modelo destilado (allowed_inference_steps do propio checkpoint), en milésimas
PASOS = {8: [1000, 993.7, 987.5, 981.2, 975.0, 909.4, 725.0, 421.9],
         6: [1000, 987.5, 975.0, 909.4, 725.0, 421.9],
         5: [1000, 981.2, 909.4, 725.0, 421.9],
         4: [1000, 975.0, 725.0, 421.9]}


def _snap(repo):
    s = glob.glob(f"{HF}/models--{repo.replace('/', '--')}/snapshots/*")
    return s[0] if s else None


def baixar():
    """Baixa só os ficheiros que se cargan (≈ 11,2 GB; o T5 pódese borrar cando estean os embeddings)."""
    from huggingface_hub import hf_hub_download
    os.environ.setdefault('HF_HUB_DISABLE_XET', '1')
    cd = HF
    for f in ['model_index.json', 'scheduler/scheduler_config.json', 'text_encoder/config.json',
              'tokenizer/added_tokens.json', 'tokenizer/special_tokens_map.json', 'tokenizer/spiece.model',
              'tokenizer/tokenizer_config.json', LTX_FICH]:
        hf_hub_download(LTX_REPO, f, cache_dir=cd)
    hf_hub_download(T5_REPO, T5_FICH, cache_dir=cd)


CEDER_SAINDO = 75     # código de saída cando cede a CPU a un traballo prioritario co LTX en memoria (movemento.sh)


def prio_agarda():
    """¿Hai un traballo prioritario agardando ou traballando (alguén ten "$CPU_LOCK.prio")?"""
    f = os.environ.get('CPU_LOCK')
    if not f:
        return False
    with open(f + '.prio', 'a') as fp:
        try:
            fcntl.flock(fp, fcntl.LOCK_EX | fcntl.LOCK_NB)
            fcntl.flock(fp, fcntl.LOCK_UN)
            return False
        except BlockingIOError:
            return True


@contextmanager
def candado(sair_se_prio=False):
    """O candado común de CPU, só mentres dura un clip ou un lote de textos, co mesmo protocolo cooperativo ca
    `herramientas/gauntlet/candado.sh`: despois de coller "$CPU_LOCK" mira sen agardar "$CPU_LOCK.prio"; se un
    traballo do camiño crítico (guion, voz) o ten, solta o candado e volve tentalo aos 15 s. Con `sair_se_prio`
    (o LTX xa está en memoria, ≈ 8 GB) sae do proceso en vez de agardar: se o prioritario (p. ex. unha rexeneración
    de imaxes, ≈ 9 GB) collese a CPU co LTX cargado, os dous pasarían do límite de memoria (13,4 GiB)."""
    f = os.environ.get('CPU_LOCK')
    if not f:
        yield; return
    fh = open(f, 'a')
    while True:
        fcntl.flock(fh, fcntl.LOCK_EX)
        try:
            with open(f + '.prio', 'a') as fp:
                fcntl.flock(fp, fcntl.LOCK_EX | fcntl.LOCK_NB)
                fcntl.flock(fp, fcntl.LOCK_UN)
            break
        except BlockingIOError:
            fcntl.flock(fh, fcntl.LOCK_UN)
            if sair_se_prio:
                print('cedo a CPU a un traballo prioritario: saio para liberar a memoria', flush=True)
                sys.exit(CEDER_SAINDO)
            time.sleep(15)
    try:
        yield
    finally:
        fcntl.flock(fh, fcntl.LOCK_UN); fh.close()


class Memoria(threading.Thread):
    """Mostraxe da memoria anónima de todo o cgroup (todos os procesos das ferramentas) cada 0,5 s."""

    def __init__(self):
        super().__init__(daemon=True)
        self.pico = 0; self.cg = (glob.glob('/sys/fs/cgroup/memory/process_api/*/claude-code-bash/memory.stat')
                                  or [None])[0]

    def run(self):
        while self.cg:
            try:
                for l in open(self.cg):
                    if l.startswith('total_rss '):
                        self.pico = max(self.pico, int(l.split()[1]))
            except OSError:
                pass
            time.sleep(0.5)


def pico_proceso_mb():
    for l in open('/proc/self/status'):
        if l.startswith('VmHWM'):
            return round(int(l.split()[1]) / 1024)


# ------------------------------------------------------------------ texto (T5-XXL en fp8)
def emb_ficheiro(texto):
    return EMB_DIR / (hashlib.sha256(f'{texto}|{MAX_LEN}'.encode()).hexdigest()[:16] + '.pt')


def textos(accions, lote=8):
    """Embeddings de T5 das accións que non estean xa en EMB_DIR. Pesos en fp8 e cálculo en fp32: a conversión
    dos pesos págase unha vez por lote (≈ 20 s), non por texto."""
    import torch
    import torch.nn.functional as F
    from safetensors import safe_open
    from transformers import AutoTokenizer, T5Config, T5EncoderModel
    falta = sorted({a for a in accions if a and not emb_ficheiro(a).exists()})
    if not falta:
        return {}
    EMB_DIR.mkdir(parents=True, exist_ok=True)

    class LinearF8(torch.nn.Module):
        def __init__(self, w):
            super().__init__()
            self.w8 = torch.nn.Parameter(w, requires_grad=False)
            # transformers mira `wo.weight.dtype` e pasaría o estado oculto a fp8: un `weight` baleiro en fp32
            self.register_buffer('weight', torch.empty(0), persistent=False)

        def forward(self, x):
            return F.linear(x, self.w8.to(x.dtype))

    ltx, t5 = _snap(LTX_REPO), _snap(T5_REPO)
    cfg = T5Config.from_json_file(f'{ltx}/text_encoder/config.json')
    with torch.device('meta'):
        m = T5EncoderModel(cfg)
    with safe_open(f'{t5}/{T5_FICH}', framework='pt') as g:
        sd = {k: g.get_tensor(k) for k in g.keys()}
    for nome, mod in list(m.named_modules()):
        for fn, fill in list(mod.named_children()):
            if isinstance(fill, torch.nn.Linear):
                setattr(mod, fn, LinearF8(sd.pop(f'{nome}.{fn}.weight' if nome else f'{fn}.weight')))
    m.load_state_dict({k: v.float() for k, v in sd.items()}, strict=False, assign=True)
    m.eval()
    tok = AutoTokenizer.from_pretrained(f'{ltx}/tokenizer')
    res = {}
    with torch.no_grad():
        for i in range(0, len(falta), lote):
            tx = falta[i:i + lote]
            t = time.time()
            ti = tok(tx, padding='max_length', max_length=MAX_LEN, truncation=True, add_special_tokens=True,
                     return_tensors='pt')
            mask = ti.attention_mask.bool()
            emb = m(ti.input_ids, attention_mask=mask)[0].float()
            for k, a in enumerate(tx):
                f = emb_ficheiro(a)
                torch.save({'texto': a, 'max_len': MAX_LEN, 'embeds': emb[k:k + 1].clone(), 'mask': mask[k:k + 1]},
                           f.with_suffix('.tmp'))
                os.replace(f.with_suffix('.tmp'), f)
                res[a] = round((time.time() - t) / len(tx), 1)
            print(f'textos {i + len(tx)}/{len(falta)}: {(time.time() - t) / len(tx):.1f} s por texto', flush=True)
    return res


# ------------------------------------------------------------------ vídeo (LTX-Video 2B destilado)
def fp32_capa_a_capa(mod):
    """Pesos en bf16 e cálculo en fp32 (CPU sen bf16 nativo), como imaxes.bf16_rapido."""
    import torch
    mod.enable_layerwise_casting(storage_dtype=torch.bfloat16, compute_dtype=torch.float32,
                                 skip_modules_pattern=(), skip_modules_classes=())
    for m in mod.modules():
        if not isinstance(m, (torch.nn.Linear, torch.nn.Conv1d, torch.nn.Conv2d, torch.nn.Conv3d,
                              torch.nn.ConvTranspose2d)):
            for _, p in list(m.named_parameters(recurse=False)):
                if p.dtype == torch.bfloat16:
                    p.data = p.data.float()
    for _, b in list(mod.named_buffers()):
        if b.dtype == torch.bfloat16:
            b.data = b.data.float()

    def _entradas(m_, args, kwargs):
        def c(x):
            return x.float() if torch.is_tensor(x) and x.is_floating_point() else x
        return tuple(c(a) for a in args), {k: c(v) for k, v in kwargs.items()}
    mod.register_forward_pre_hook(_entradas, with_kwargs=True)


def cargar_ltx():
    """Transformer e VAE desde o ficheiro único, lendo só as claves de cada parte (3 s; pesos mapeados do disco)."""
    import torch
    from accelerate import init_empty_weights
    from diffusers import (AutoencoderKLLTXVideo, FlowMatchEulerDiscreteScheduler, LTXConditionPipeline,
                           LTXVideoTransformer3DModel)
    from diffusers.loaders.single_file_utils import (convert_ltx_transformer_checkpoint_to_diffusers,
                                                     convert_ltx_vae_checkpoint_to_diffusers)
    from safetensors import safe_open
    ck = f'{_snap(LTX_REPO)}/{LTX_FICH}'
    with safe_open(ck, framework='pt') as g:
        sd_tr = {k: g.get_tensor(k) for k in g.keys() if not k.startswith('vae.')}
    with init_empty_weights():
        tr = LTXVideoTransformer3DModel.from_config(CFG_TR)
    tr.load_state_dict({k: v.to(torch.bfloat16) for k, v in convert_ltx_transformer_checkpoint_to_diffusers(sd_tr).items()},
                       strict=True, assign=True)
    with safe_open(ck, framework='pt') as g:
        sd_v = {k: g.get_tensor(k) for k in g.keys() if k.startswith('vae.')}
    with init_empty_weights():
        vae = AutoencoderKLLTXVideo.from_config(CFG_VAE)
    vae.load_state_dict({k: v.to(torch.bfloat16) for k, v in convert_ltx_vae_checkpoint_to_diffusers(sd_v).items()},
                        strict=False, assign=True)
    del sd_tr, sd_v
    tr.eval(); vae.eval()
    fp32_capa_a_capa(tr); fp32_capa_a_capa(vae)
    vae.enable_tiling()
    sch = FlowMatchEulerDiscreteScheduler(num_train_timesteps=1000, shift=1.0, use_dynamic_shifting=False,
                                          shift_terminal=None, base_shift=0.5, max_shift=1.15,
                                          base_image_seq_len=256, max_image_seq_len=4096)
    pipe = LTXConditionPipeline(scheduler=sch, vae=vae, text_encoder=None, tokenizer=None, transformer=tr)
    pipe.set_progress_bar_config(disable=True)
    return pipe


def gardar_mp4(frames, f, fps=24, crf=12):
    import subprocess
    import imageio_ffmpeg
    h, w = frames.shape[1:3]
    tmp = str(f) + '.tmp.mp4'
    p = subprocess.Popen([imageio_ffmpeg.get_ffmpeg_exe(), '-y', '-loglevel', 'error', '-f', 'rawvideo',
                          '-pix_fmt', 'rgb24', '-s', f'{w}x{h}', '-r', str(fps), '-i', '-', '-c:v', 'libx264',
                          '-preset', 'medium', '-crf', str(crf), '-pix_fmt', 'yuv444p', tmp], stdin=subprocess.PIPE)
    p.stdin.write(np.ascontiguousarray(frames).tobytes()); p.stdin.close(); p.wait()
    os.replace(tmp, f)


def un_clip(pipe, imaxe, accion, params, saida):
    import torch
    from PIL import Image
    from diffusers.pipelines.ltx.pipeline_ltx_condition import LTXVideoCondition
    pr = dict(M.I2V_PARAMS, **(params or {}))
    d = torch.load(emb_ficheiro(accion))
    im = M.a_16_9(Image.open(imaxe).convert('RGB'))
    tempos = []
    t0 = time.time()

    def cb(p, i, t, kw):
        tempos.append(time.time()); return kw
    out = pipe(conditions=[LTXVideoCondition(image=im, frame_index=0)], prompt_embeds=d['embeds'].float(),
               prompt_attention_mask=d['mask'], width=pr['W'], height=pr['H'], num_frames=pr['F'], frame_rate=24,
               timesteps=PASOS[pr['pasos']], guidance_scale=1.0, decode_timestep=0.05, decode_noise_scale=0.025,
               image_cond_noise_scale=pr['ruido_cond'], generator=torch.Generator().manual_seed(pr['semente']),
               output_type='np', callback_on_step_end=cb)
    tt = time.time() - t0
    fr = (np.clip(out.frames[0], 0, 1) * 255 + 0.5).astype(np.uint8)
    gardar_mp4(fr, saida)
    info = {'imaxe': str(imaxe), 'accion': accion, **pr, 's_total': round(tt, 1),
            's_pasos': [round(b - a, 1) for a, b in zip([t0] + tempos[:-1], tempos)],
            's_descodificar': round(tt - (tempos[-1] - t0), 1) if tempos else None, 'fotogramas': int(len(fr)),
            'pico_proceso_mb': pico_proceso_mb()}
    Path(str(saida).replace('.mp4', '.json')).write_text(json.dumps(info, ensure_ascii=False, indent=1))
    return info


def traballos(planos, imaxes_dir=None):
    out = []
    for p in planos:
        an = p.get('animacion') or {}
        if p.get('imaxe') and p.get('accion'):
            out.append((p['imaxe'], p['accion'], p.get('i2v')))
        elif an.get('modo') == 'i2v' and an.get('accion'):
            im = p.get('imaxe')
            if not im and imaxes_dir:
                c = sorted(glob.glob(f"{imaxes_dir}/{int(p['n']) - 1:03d}-*.png") +
                           glob.glob(f"{imaxes_dir}/{int(p['n']) - 1:03d}-*.jpg"))
                im = c[0] if c else None
            if im:
                out.append((im, an['accion'], an.get('i2v')))
    return out


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('fase', choices=['baixar', 'texto', 'xerar'])
    ap.add_argument('planos', nargs='?')
    ap.add_argument('--imaxes')
    a = ap.parse_args()
    if a.fase == 'baixar':
        baixar(); return
    import torch
    torch.set_num_threads(int(os.environ.get('NTH', '4')))
    tb = traballos(json.loads(Path(a.planos).read_text()), a.imaxes)
    if a.fase == 'texto':
        with candado():
            print(json.dumps(textos([x[1] for x in tb]), ensure_ascii=False))
        return
    falta = [(im, ac, pr) for im, ac, pr in tb if not M.i2v_ficheiro(im, ac, pr).exists()]
    print(f'{len(tb)} clips, faltan {len(falta)}', flush=True)
    if not falta:
        return
    mem = Memoria(); mem.start()
    pipe = None
    for k, (im, ac, pr) in enumerate(falta):
        if not emb_ficheiro(ac).exists():
            print(f'falta o embedding da acción (fase texto): {ac[:60]}', flush=True); continue
        if pipe is not None and prio_agarda():
            print('cedo a CPU a un traballo prioritario: saio para liberar a memoria', flush=True)
            sys.exit(CEDER_SAINDO)
        with candado(sair_se_prio=pipe is not None):
            if pipe is None:
                pipe = cargar_ltx()
            info = un_clip(pipe, im, ac, pr, M.i2v_ficheiro(im, ac, pr))
        info['pico_cgroup_mb'] = round(mem.pico / 2**20)
        print(f'clip {k + 1}/{len(falta)}: ' + json.dumps(info, ensure_ascii=False), flush=True)


if __name__ == '__main__':
    main()
