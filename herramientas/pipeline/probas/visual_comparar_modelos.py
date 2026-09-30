"""Comparativa de modelos de imaxe (Gauntlet 3, peza VISUAL): mesmos prompts e sementes en varios modelos e estilos.

    flock "$CPU_LOCK" $PY probas/visual_comparar_modelos.py MODELO SAIDA [--estilos filme,pintura] [--n 8]

MODELO: turbo | lightning | lightning8 (imaxes.MODELOS). Garda PNG e un JSON cos segundos por imaxe.
Os prompts son escenas galegas xenéricas das catro fases (biblia visual), sen a palabra "Galicia": a iconografía
descríbese (granito, lousa, hórreo como "granary on pillars"). Con --malos engade escenas alleas (calibración de
revisor.py) e unha proba co nome "Galicia, Spain" (resultado: aldea de pedra verosímil). Con --prompts, outra lista.
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
# Escenas deliberadamente alleas (calibración da porta de iconografía de revisor.py): o que o crítico viu.
MALOS = [
    ('malo', 'toscana', 'a Tuscan hill village with tall cypress trees and red-orange terracotta tile roofs, sunny'),
    ('malo', 'andalucia', 'a white-washed Andalusian village with white houses and orange tile roofs on a dry hill'),
    ('malo', 'oliveiras', 'an olive grove on dry red soil with a stone farmhouse, hot summer light'),
    ('malo', 'palmeiras', 'a village square with palm trees and whitewashed houses, bright sun'),
    ('malo', 'rodas', 'a wooden farm wagon with large spoked wheels pulled by horses on a dusty road'),
    ('malo', 'eucaliptos', 'a dense eucalyptus plantation with tall straight pale trunks and peeling bark'),
    # ¿sabe SDXL que é Galicia? (a biblia di que non se escriba: compróbase)
    ('proba', 'galicia', 'a traditional village in Galicia, Spain, stone houses, rural landscape'),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modelo'); ap.add_argument('saida')
    ap.add_argument('--estilos', default='filme,pintura'); ap.add_argument('--n', type=int, default=len(PROMPTS))
    ap.add_argument('--malos', action='store_true', help='engade as escenas alleas (só no primeiro estilo)')
    ap.add_argument('--prompts', default=None, help='JSON [[fase, nome, prompt], ...] en vez dos PROMPTS de aquí')
    a = ap.parse_args()
    import torch
    torch.set_num_threads(int(os.environ.get('NTH', '4')))
    out = Path(a.saida); out.mkdir(parents=True, exist_ok=True)
    t = time.time(); pipe = imaxes.cargar_pipe(a.modelo); carga = round(time.time() - t, 1)
    m = pipe._revolta
    res = {'modelo': m, 'carga_s': carga, 'imaxes': []}
    print(f'{a.modelo}: carga {carga} s', flush=True)
    prompts = [tuple(x) for x in json.loads(Path(a.prompts).read_text())] if a.prompts else PROMPTS
    tarefas = [(estilo, k, x) for estilo in a.estilos.split(',') for k, x in enumerate(prompts[:a.n])]
    if a.malos:
        tarefas += [(a.estilos.split(',')[0], 100 + k, x) for k, x in enumerate(MALOS)]
    for estilo, k, (fase, nome, p) in tarefas:
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
