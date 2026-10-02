"""Baixa á caché principal ($SCRATCH/hf) os modelos que pide a peza IMAXE (orde pensada para non baixar de 1,5 GB libres):
Florence-2-base (MIT) -> borrar Florence-2-large -> ControlNet depth small fp16 (OpenRAIL++) -> Depth-Anything-V2-Small (Apache-2.0)."""
import os, shutil, sys, time
from huggingface_hub import snapshot_download
H = os.environ['HF_HOME'] + '/hub'
def libre():
    s = shutil.disk_usage('/'); return s.free / 1e9
t = time.time()
print('libre', round(libre(), 2), 'GB', flush=True)
snapshot_download('florence-community/Florence-2-base')
print('florence-base ok', round(time.time() - t), 's; libre', round(libre(), 2), flush=True)
grande = f'{H}/models--florence-community--Florence-2-large'
if os.path.isdir(grande) and len(sys.argv) > 1 and sys.argv[1] == 'borrar_large':
    shutil.rmtree(grande); print('borrado Florence-2-large; libre', round(libre(), 2), flush=True)
snapshot_download('diffusers/controlnet-depth-sdxl-1.0-small', allow_patterns=['config.json', 'diffusion_pytorch_model.fp16.safetensors'])
print('controlnet depth small ok; libre', round(libre(), 2), flush=True)
snapshot_download('depth-anything/Depth-Anything-V2-Small-hf')
print('depth-anything small ok; libre', round(libre(), 2), flush=True)
print('rematou', round(time.time() - t), 's', flush=True)
