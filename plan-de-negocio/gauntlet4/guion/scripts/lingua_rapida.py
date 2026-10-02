#!/usr/bin/env python
"""Porta de lingua rápida (LanguageTool gl-ES + hunspell) sobre un guion de longo.py, sen NLI. Guionista do Gauntlet 4
(axente Claude), 02-10-2026. É a mesma función que usa a porta de texto (`qa.lingua`), co mesmo texto normalizado
(`longo.ler_guion`) e as mesmas palabras do dossier da ficha (que non contan como erro de hunspell).

    flock "$CPU_LOCK" "$PY" lingua_rapida.py GUION.txt TEMA.yaml

Tarda ≈ 1 min (arranca o servidor Java de LanguageTool). Imprime cada aviso co seu contexto e sae con código 1 se
hai algún.
"""
import sys
from pathlib import Path
import yaml

PIPE = Path(__file__).resolve().parents[4] / 'herramientas' / 'pipeline'
sys.path.insert(0, str(PIPE))
import longo, pipeline as P, qa  # noqa: E402


def main():
    guion, tema_path = sys.argv[1], sys.argv[2]
    tema = yaml.safe_load(open(tema_path))
    texto, caps = longo.ler_guion(guion)
    avisos = qa.lingua(texto, dossier=P.ancora(tema))
    for a in avisos:
        print(f"- [{a['regra']}] «{a['palabra']}»: {a['mensaxe']}\n    …{a['contexto']}… suxestións: {a['suxestions']}")
    print(f'avisos: {len(avisos)} | palabras: {len(texto.split())} | capítulos: {len(caps)}')
    qa.pechar_lt()
    sys.exit(1 if avisos else 0)


if __name__ == '__main__':
    main()
