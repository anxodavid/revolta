"""Proba de imaxe a vídeo (I2V) con LTX-Video 2B 0.9.8 destilado en CPU (sen bf16 nativo).

Pesos do transformer e do VAE gardados en bf16 e cálculo en fp32 capa a capa (o truco de imaxes.bf16_rapido);
o codificador de texto non se carga: os embeddings de T5 calcúlaos t5_emb.py noutro proceso.
Carga só as claves que precisa de cada parte do ficheiro único (safe_open), sen ler o ficheiro enteiro en RAM.

Uso: python ltx_proba.py traballos.json saida_dir
traballos.json: [{"id", "imaxe", "accion" (texto, ou clave de accions.json), "W", "H", "F", "pasos", "semente",
                  "ruido_cond" (opcional, image_cond_noise_scale)}]
"""
import glob, hashlib, json, math, os, sys, threading, time
import numpy as np
import torch

SCR = os.environ['SCRATCH']
HF = f'{SCR}/video/hf/hub'
CKPT = glob.glob(f'{HF}/models--Lightricks--LTX-Video/snapshots/*/ltxv-2b-0.9.8-distilled.safetensors')[0]
EMB_DIR = os.environ.get('EMB_DIR', f'{SCR}/video/emb')
AQUI = os.path.dirname(os.path.abspath(__file__))

# Configuracións de diffusers de Lightricks/LTX-Video-0.9.5 (a mesma arquitectura que o 2B 0.9.6-0.9.8)
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
         7: [1000, 993.7, 987.5, 981.2, 975.0, 909.4, 725.0],
         6: [1000, 987.5, 975.0, 909.4, 725.0, 421.9],
         5: [1000, 981.2, 909.4, 725.0, 421.9],
         4: [1000, 975.0, 725.0, 421.9]}


class Memoria(threading.Thread):
    """Mostraxe da memoria: RSS do proceso e RSS de todo o cgroup (todos os procesos das ferramentas)."""
    CG = None

    def __init__(self):
        super().__init__(daemon=True)
        self.pico_cg = 0; self.parar = False
        for c in glob.glob('/sys/fs/cgroup/memory/process_api/*/claude-code-bash/memory.stat'):
            Memoria.CG = c

    def run(self):
        while not self.parar:
            try:
                if Memoria.CG:
                    for l in open(Memoria.CG):
                        if l.startswith('total_rss '):
                            self.pico_cg = max(self.pico_cg, int(l.split()[1]))
            except OSError:
                pass
            time.sleep(0.5)


def pico_proceso_mb():
    for l in open('/proc/self/status'):
        if l.startswith('VmHWM'):
            return int(l.split()[1]) / 1024


def fp32_capa_a_capa(mod):
    """Pesos en bf16 e cálculo en fp32 (CPU sen bf16 nativo). Normas e parámetros soltos pasan a fp32 e as
    entradas en coma flotante do módulo pásanse a fp32 antes de cada chamada."""
    mod.enable_layerwise_casting(storage_dtype=torch.bfloat16, compute_dtype=torch.float32,
                                 skip_modules_pattern=(), skip_modules_classes=())
    for m in mod.modules():
        if not isinstance(m, (torch.nn.Linear, torch.nn.Conv1d, torch.nn.Conv2d, torch.nn.Conv3d,
                              torch.nn.ConvTranspose2d)):
            for _, p in list(m.named_parameters(recurse=False)):
                if p.dtype == torch.bfloat16:
                    p.data = p.data.float()

    def _entradas(m_, args, kwargs):
        def c(x):
            if torch.is_tensor(x) and x.is_floating_point():
                return x.float()
            return x
        return tuple(c(a) for a in args), {k: c(v) for k, v in kwargs.items()}
    mod.register_forward_pre_hook(_entradas, with_kwargs=True)


def cargar():
    from safetensors import safe_open
    from accelerate import init_empty_weights
    from diffusers import (AutoencoderKLLTXVideo, FlowMatchEulerDiscreteScheduler, LTXConditionPipeline,
                           LTXVideoTransformer3DModel)
    from diffusers.loaders.single_file_utils import (convert_ltx_transformer_checkpoint_to_diffusers,
                                                     convert_ltx_vae_checkpoint_to_diffusers)
    t = time.time()
    with safe_open(CKPT, framework='pt') as g:
        sd_tr = {k: g.get_tensor(k) for k in g.keys() if not k.startswith('vae.')}
    sd_tr = convert_ltx_transformer_checkpoint_to_diffusers(sd_tr)
    with init_empty_weights():
        tr = LTXVideoTransformer3DModel.from_config(CFG_TR)
    tr.load_state_dict({k: v.to(torch.bfloat16) for k, v in sd_tr.items()}, strict=True, assign=True)
    del sd_tr
    with safe_open(CKPT, framework='pt') as g:
        sd_v = {k: g.get_tensor(k) for k in g.keys() if k.startswith('vae.')}
    sd_v = convert_ltx_vae_checkpoint_to_diffusers(sd_v)
    with init_empty_weights():
        vae = AutoencoderKLLTXVideo.from_config(CFG_VAE)
    falta, sobra = vae.load_state_dict({k: v.to(torch.bfloat16) for k, v in sd_v.items()}, strict=False, assign=True)
    print('vae falta', falta, 'sobra', sobra[:8], flush=True)
    del sd_v
    tr.eval(); vae.eval()
    fp32_capa_a_capa(tr); fp32_capa_a_capa(vae)
    # latents_mean/std son buffers: a fp32
    for n, b in list(vae.named_buffers()):
        if b.dtype == torch.bfloat16:
            b.data = b.data.float()
    vae.enable_tiling()
    sch = FlowMatchEulerDiscreteScheduler(num_train_timesteps=1000, shift=1.0, use_dynamic_shifting=False,
                                          shift_terminal=None, base_shift=0.5, max_shift=1.15,
                                          base_image_seq_len=256, max_image_seq_len=4096)
    pipe = LTXConditionPipeline(scheduler=sch, vae=vae, text_encoder=None, tokenizer=None, transformer=tr)
    pipe.set_progress_bar_config(disable=True)
    print(f'carga {time.time() - t:.1f} s, pico proceso {pico_proceso_mb():.0f} MB', flush=True)
    return pipe, round(time.time() - t, 1)


def embeddings(texto, max_len=256):
    h = hashlib.sha256(f'{texto}|{max_len}'.encode()).hexdigest()[:16]
    d = torch.load(f'{EMB_DIR}/{h}.pt')
    return d['embeds'].float(), d['mask']


def gardar_mp4(frames, f, fps=24, crf=12):
    import imageio_ffmpeg
    import subprocess
    h, w = frames.shape[1:3]
    cmd = [imageio_ffmpeg.get_ffmpeg_exe(), '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24',
           '-s', f'{w}x{h}', '-r', str(fps), '-i', '-', '-c:v', 'libx264', '-preset', 'medium', '-crf', str(crf),
           '-pix_fmt', 'yuv444p', f + '.tmp.mp4']
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    p.stdin.write(frames.tobytes()); p.stdin.close(); p.wait()
    os.replace(f + '.tmp.mp4', f)


def tira(frames, f, n=8, ancho=480):
    """Tira de n fotogramas repartidos (4x2) en JPEG, co número de fotograma."""
    from PIL import Image, ImageDraw
    idx = np.linspace(0, len(frames) - 1, n).round().astype(int)
    h, w = frames.shape[1:3]
    alto = round(ancho * h / w)
    folla = Image.new('RGB', (ancho * 4, alto * 2), 'black')
    for k, i in enumerate(idx):
        im = Image.fromarray(frames[i]).resize((ancho, alto), Image.LANCZOS)
        d = ImageDraw.Draw(im); d.rectangle((0, 0, 70, 18), fill='black'); d.text((4, 3), f'f{i}', fill='white')
        folla.paste(im, ((k % 4) * ancho, (k // 4) * alto))
    folla.save(f, quality=88)


def main():
    from PIL import Image
    from diffusers.pipelines.ltx.pipeline_ltx_condition import LTXVideoCondition
    torch.set_num_threads(int(os.environ.get('NTH', '4')))
    traballos = json.load(open(sys.argv[1])); saida = sys.argv[2]
    os.makedirs(saida, exist_ok=True)
    accs = json.load(open(f'{AQUI}/accions.json'))
    mem = Memoria(); mem.start()
    pipe, t_carga = cargar()
    resf = f'{saida}/medidas.json'
    res = json.load(open(resf)) if os.path.exists(resf) else {}
    for tb in traballos:
        if tb['id'] in res:
            continue
        texto = accs.get(tb['accion'], tb['accion'])
        emb, mask = embeddings(texto)
        im = Image.open(tb['imaxe']).convert('RGB')
        W, H, F = tb['W'], tb['H'], tb['F']
        tempos = []
        t0 = time.time()

        def cb(p, i, t, kw):
            tempos.append(time.time())
            return kw
        cond = LTXVideoCondition(image=im, frame_index=0)
        out = pipe(conditions=[cond], prompt_embeds=emb, prompt_attention_mask=mask, width=W, height=H,
                   num_frames=F, frame_rate=24, timesteps=PASOS[tb.get('pasos', 8)], guidance_scale=1.0,
                   decode_timestep=0.05, decode_noise_scale=0.025,
                   image_cond_noise_scale=tb.get('ruido_cond', 0.15),
                   generator=torch.Generator().manual_seed(tb.get('semente', 42)), output_type='np',
                   callback_on_step_end=cb)
        t_total = time.time() - t0
        fr = (np.clip(out.frames[0], 0, 1) * 255 + 0.5).astype(np.uint8)
        pasos_s = [round(b - a, 1) for a, b in zip([t0] + tempos[:-1], tempos)]
        t_decod = round(t_total - (tempos[-1] - t0), 1) if tempos else None
        gardar_mp4(fr, f"{saida}/{tb['id']}.mp4")
        tira(fr, f"{saida}/{tb['id']}_tira.jpg")
        lat_tokens = ((F - 1) // 8 + 1) * (H // 32) * (W // 32)
        res[tb['id']] = {**tb, 'modelo': 'ltxv-2b-0.9.8-distilled', 's_total': round(t_total, 1),
                         's_pasos': pasos_s, 's_decodificar_aprox': t_decod, 'tokens': lat_tokens,
                         'fotogramas': int(fr.shape[0]), 'res': f'{fr.shape[2]}x{fr.shape[1]}',
                         'pico_proceso_mb': round(pico_proceso_mb()), 'pico_cgroup_rss_mb': round(mem.pico_cg / 2**20),
                         's_carga_modelo': t_carga, 'cpu': open('/proc/cpuinfo').read().count('processor\t')}
        print(json.dumps(res[tb['id']], ensure_ascii=False), flush=True)
        json.dump(res, open(resf + '.tmp', 'w'), indent=1, ensure_ascii=False); os.replace(resf + '.tmp', resf)
    mem.parar = True


if __name__ == '__main__':
    main()
