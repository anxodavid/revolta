"""Comparativa de modelos de imaxe (Gauntlet 3, peza VISUAL): mesmos prompts e sementes en varios modelos e estilos.

    flock "$CPU_LOCK" $PY probas/visual_comparar_modelos.py MODELO SAIDA [--estilos filme,pintura] [--n 8]

MODELO: turbo | lightning | lightning8 (imaxes.MODELOS). Garda PNG e un JSON cos segundos por imaxe.
Os prompts son escenas galegas xenéricas das catro fases (biblia visual), sen a palabra "Galicia" (SDXL confúndea
coa Galitzia de Polonia e Ucraína [S]): a iconografía descríbese (granito, lousa, hórreo como "granary on pillars").
"""
import argparse, json, os, sys, time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import imaxes

PROMPTS = [
    ('gancho', 'lareira', 'medium shot of an old woman in a dark wool shawl stirring an iron pot hanging over an open '
     'hearth fire, rough granite walls, smoke, lit only by the firelight, deep black shadows'),
    ('gancho', 'cruceiro', 'a weathered granite stone wayside cross on a stepped pedestal at a crossroads at night, '
     'dark oak trees, mist, pale moonlight breaking through storm clouds'),
    ('transicion', 'horreo', 'wide shot of a hamlet of granite stone houses with dark grey slate roofs and a long narrow '
     'granite granary raised on stone pillars, green fields, bright morning sunlight after rain'),
    ('transicion', 'carro', 'two brown oxen pulling a wooden cart with solid wooden disc wheels along a muddy lane '
     'between mossy stone walls, chestnut trees, soft daylight'),
    ('calma', 'costa', 'rugged Atlantic coast at sunset, dark granite cliffs, waves breaking on the rocks, a small stone '
     'chapel on the headland, warm low sun'),
    ('calma', 'mans', "close-up of an old woman's hands spinning wool with a wooden distaff beside a small oil lamp, "
     'warm dim lamplight, dark background'),
    ('durmir', 'carballeira', 'an ancient oak forest at night, moss-covered trunks, mist drifting between the trees, '
     'cold blue moonlight, calm and still'),
    ('durmir', 'brasas', 'glowing embers in a stone hearth, an iron pot and a wooden stool, a dark sleeping kitchen, '
     'faint red glow'),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modelo'); ap.add_argument('saida')
    ap.add_argument('--estilos', default='filme,pintura'); ap.add_argument('--n', type=int, default=len(PROMPTS))
    a = ap.parse_args()
    import torch
    torch.set_num_threads(int(os.environ.get('NTH', '4')))
    out = Path(a.saida); out.mkdir(parents=True, exist_ok=True)
    t = time.time(); pipe = imaxes.cargar_pipe(a.modelo); carga = round(time.time() - t, 1)
    m = pipe._revolta
    res = {'modelo': m, 'carga_s': carga, 'imaxes': []}
    print(f'{a.modelo}: carga {carga} s', flush=True)
    for estilo in a.estilos.split(','):
        for k, (fase, nome, p) in enumerate(PROMPTS[:a.n]):
            pr = f'{imaxes.ESTILOS[estilo]}, {p}'
            seed = 1000 + k
            t = time.time(); im = imaxes.xerar_unha(pipe, pr, seed, m); s = round(time.time() - t, 1)
            f = out / f'{a.modelo}-{estilo}-{k}-{nome}.png'
            im.save(f)
            ntok, perdido = imaxes.tokens(pipe, pr)
            res['imaxes'].append({'ficheiro': f.name, 'estilo': estilo, 'fase': fase, 'nome': nome, 'seed': seed,
                                  's': s, 'tokens': ntok, 'truncado': perdido, 'prompt': pr})
            print(f'{f.name}: {s} s ({ntok} tokens)', flush=True)
            (out / f'{a.modelo}.json').write_text(json.dumps(res, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
