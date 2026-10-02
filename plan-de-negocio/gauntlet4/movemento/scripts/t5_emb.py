"""Embeddings de T5-XXL (codificador de texto de LTX-Video) nun proceso aparte.

Pesos en fp8 (e4m3, o ficheiro de comfyanonymous/flux_text_encoders, Apache-2.0) e cálculo en fp32 capa a capa:
~4,9 GB de memoria en vez dos ~19 GB do modelo en fp32. Garda un .pt por acción en EMB_DIR (clave = sha256 do texto).
Uso: python t5_emb.py accions.json [max_len]
"""
import hashlib, json, os, sys, time, threading
import torch
import torch.nn.functional as F
from safetensors import safe_open

SCR = os.environ['SCRATCH']
HF = f'{SCR}/video/hf/hub'
T5 = next(__import__('glob').iglob(f'{HF}/models--comfyanonymous--flux_text_encoders/snapshots/*/t5xxl_fp8_e4m3fn.safetensors'))
LTX = next(__import__('glob').iglob(f'{HF}/models--Lightricks--LTX-Video/snapshots/*'))
EMB_DIR = os.environ.get('EMB_DIR', f'{SCR}/video/emb')


class LinearF8(torch.nn.Module):
    """Linear sen nesgo con pesos en fp8: pasa a fp32 só no momento de multiplicar."""
    def __init__(self, w):
        super().__init__()
        self.w8 = torch.nn.Parameter(w, requires_grad=False)
        # transformers mira `wo.weight.dtype` e pasaría o estado oculto a fp8: un `weight` baleiro en fp32 evítao
        self.register_buffer('weight', torch.empty(0), persistent=False)

    def forward(self, x):
        return F.linear(x, self.w8.to(x.dtype))


def pico_mb():
    for l in open('/proc/self/status'):
        if l.startswith('VmHWM'):
            return int(l.split()[1]) / 1024


def cargar():
    from transformers import T5Config, T5EncoderModel, AutoTokenizer
    cfg = T5Config.from_json_file(f'{LTX}/text_encoder/config.json')
    with torch.device('meta'):
        m = T5EncoderModel(cfg)
    sd = {}
    with safe_open(T5, framework='pt') as g:
        for k in g.keys():
            sd[k] = g.get_tensor(k)
    # Linear -> LinearF8 (fp8); o resto (normas, nesgo relativo, embeddings) en fp32
    for nome, mod in list(m.named_modules()):
        for fn, fill in list(mod.named_children()):
            if isinstance(fill, torch.nn.Linear):
                k = f'{nome}.{fn}.weight' if nome else f'{fn}.weight'
                setattr(mod, fn, LinearF8(sd.pop(k)))
    resto = {k: v.float() for k, v in sd.items()}
    falta, sobra = m.load_state_dict(resto, strict=False, assign=True)
    falta = [k for k in falta if not k.endswith('.w8')]
    print('falta', falta[:5], 'sobra', sobra[:5], flush=True)
    m.eval()
    tok = AutoTokenizer.from_pretrained(f'{LTX}/tokenizer')
    return m, tok


@torch.no_grad()
def codificar(m, tok, texto, max_len=256):
    ti = tok([texto], padding='max_length', max_length=max_len, truncation=True, add_special_tokens=True,
             return_tensors='pt')
    mask = ti.attention_mask.bool()
    emb = m(ti.input_ids, attention_mask=mask)[0].float()
    return emb, mask, int(mask.sum())


def main():
    torch.set_num_threads(int(os.environ.get('NTH', '4')))
    accs = json.load(open(sys.argv[1]))
    max_len = int(sys.argv[2]) if len(sys.argv) > 2 else 256
    os.makedirs(EMB_DIR, exist_ok=True)
    t0 = time.time(); m, tok = cargar(); tc = time.time() - t0
    print(f'carga {tc:.1f} s, pico {pico_mb():.0f} MB', flush=True)
    res = {}
    for nome, texto in accs.items():
        h = hashlib.sha256(f'{texto}|{max_len}'.encode()).hexdigest()[:16]
        f = f'{EMB_DIR}/{h}.pt'
        if os.path.exists(f):
            res[nome] = {'ficheiro': f, 'cache': True}; continue
        t = time.time(); emb, mask, n = codificar(m, tok, texto, max_len)
        torch.save({'texto': texto, 'max_len': max_len, 'embeds': emb, 'mask': mask}, f + '.tmp')
        os.replace(f + '.tmp', f)
        res[nome] = {'ficheiro': f, 's': round(time.time() - t, 1), 'tokens': n}
        print(nome, res[nome], flush=True)
    res['_medidas'] = {'carga_s': round(tc, 1), 'pico_mb': round(pico_mb())}
    print(json.dumps(res['_medidas']), flush=True)
    json.dump(res, open(f'{EMB_DIR}/indice_{os.path.basename(sys.argv[1])}', 'w'), indent=1)


if __name__ == '__main__':
    main()
