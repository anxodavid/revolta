#!/usr/bin/env python
"""Compara dous guions e as súas execucións: mesmos controis automáticos (LanguageTool, estilo, H1) e o ASR
que xa mediu a etapa QA de cada execución.

    python comparar.py tema.yaml A.txt A_qa.json "etiqueta A" B.txt B_qa.json "etiqueta B" > comparacion.md
"""
import json, sys
from pathlib import Path
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import qa, ancoraxe
from pipeline import partir


def medir(tema, txt, qaj):
    g = Path(txt).read_text().strip()
    r = json.loads(Path(qaj).read_text())
    lt = qa.lingua(g, dossier=tema['dossier'])
    e = qa.estilo(g, partir(g), tema['aviso'], tema['palabras'])
    h1 = ancoraxe.ancoraxe(g, tema['dossier'], [tema['aviso']])
    return {'guion': g, 'lt': lt, 'estilo': e, 'h1': h1, 'asr': r['asr'], 'ficheiro': r['ficheiro'],
            'llm': r.get('llm', {}), 'ritmo': r.get('ritmo_palabras_min')}


def main():
    tema = yaml.safe_load(open(sys.argv[1]))
    A = medir(tema, sys.argv[2], sys.argv[3]); la = sys.argv[4]
    B = medir(tema, sys.argv[5], sys.argv[6]); lb = sys.argv[7]
    fil = [
        ('Palabras', lambda x: x['estilo']['palabras']),
        ('Avisos LanguageTool gl-ES (medidos agora sobre o guion final)', lambda x: len(x['lt'])),
        ('Nomes/cantidades sen ancorar no dossier (H1)', lambda x: len(x['h1']['non_ancorados'])),
        ('Cifras / signos prohibidos / preguntas', lambda x: f"{len(x['estilo']['cifras'])} / {len(x['estilo']['signos_prohibidos'])} / {x['estilo']['preguntas']}"),
        ('Aviso e fórmula literais', lambda x: f"{x['estilo']['aviso_literal']} / {x['estilo']['formula_literal']}"),
        ('Frases fóra de 8-25 palabras', lambda x: len(x['estilo']['frases_fora_8_25'])),
        ('Máx. nomes propios novos por 110 palabras', lambda x: x['estilo']['max_nomes_novos_por_110_palabras']),
        ('WER ASR mestura (voz + choiva)', lambda x: x['asr']['mestura']['wer']),
        ('WER ASR voz soa', lambda x: x['asr']['voz']['wer']),
        ('Frases con WER > 0,5', lambda x: len(x['asr']['mestura']['frases_wer_mais_0_5'])),
        ('Sincronía subtítulos (%)', lambda x: x['asr']['mestura']['sincronia']['pct_dentro_da_sua_frase']),
        ('Duración do vídeo (s)', lambda x: x['ficheiro']['dur_video_s']),
        ('Ritmo global (palabras/min)', lambda x: x['ritmo']),
    ]
    L = [f'| Control | {la} | {lb} |', '|---|---|---|']
    L += [f'| {n} | {f(A)} | {f(B)} |' for n, f in fil]
    L += ['']
    for lab, X in ((la, A), (lb, B)):
        L += [f'**Avisos LanguageTool, {lab}:**', '']
        L += [f"- `{m['regra']}` {m['mensaxe']} — \"{m['contexto']}\"" for m in X['lt']] or ['- ningún']
        L += ['', f'**Sen ancorar (H1), {lab}:** ' + (', '.join(f"\"{x['texto']}\"" for x in X['h1']['non_ancorados']) or 'ningún'), '']
    print('\n'.join(L))


if __name__ == '__main__':
    main()
