#!/usr/bin/env python3
"""Instantánea do scratchpad no repo: copia os ficheiros de texto pequenos que deixan os axentes (scripts, notas,
medidas, configuracións e rexistros) a unha carpeta do repo e fai commit e push SÓ desa carpeta.

Para que serve: o scratchpad sobrevive aos reinicios do contedor pero non a unha sesión nova. Se a sesión se corta,
co que hai no repo (encargos, estado de cada peza e esta instantánea) pódese relanzar o Gauntlet noutra sesión.

    python3 herramientas/gauntlet/instantanea.py              # unha vez
    python3 herramientas/gauntlet/instantanea.py --bucle 1200  # cada 20 min, ata que se mate o proceso
    # desacoplado (non o corta o límite de 30 min das tarefas da ferramenta Bash):
    setsid nohup python3 herramientas/gauntlet/instantanea.py --bucle 1200 > "$SCRATCH/logs/instantanea.log" 2>&1 &

Que NON copia: modelos, venvs e cachés (hf, venv, tts, bench...), binarios (imaxes, audio, vídeo, pesos), material de
terceiros e os materiais a cegas dos críticos (`cego/`: a clave non pode chegar ao repo mentres o crítico xulga).
Os rexistros de máis de 1 MB gárdanse recortados (as últimas 3.000 liñas). Commit só da carpeta de destino
(`git commit -- RUTA`): non arrastra o que outro axente teña preparado no índice.
"""
import argparse, hashlib, os, subprocess, sys, time
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
RAMA = 'ccr-0584aac1-xqy2si'
DEST = REPO / 'plan-de-negocio' / 'gauntlet4' / 'scratchpad'
EXT = {'.py', '.sh', '.md', '.json', '.jsonl', '.yaml', '.yml', '.txt', '.csv', '.tsv', '.log', '.srt', '.vtt',
       '.toml', '.cfg', '.ini'}
# directorios que non se copian (relativos ao scratchpad); calquera directorio con estes nomes tamén se salta
EXCLUIR_RUTAS = {'hf', 'video/hf', 'video/venv', 'video/emb', 'tts', 'bench', 'languagetool', 'cotovia', 'cotovia_nova',
                 'deb', 'revisor', 'tmp', 'cego', 'referencia', '.instalado'}
EXCLUIR_NOMES = {'venv', '.venv', '__pycache__', 'site-packages', 'node_modules', '.git', 'hf', 'huggingface',
                 'cego', 'wt-pr4', 'wt-pr5'}
MAX_BYTES = 1_000_000
COLA_LINAS = 3000
TOPE_TOTAL = 40_000_000


def scratch():
    s = os.environ.get('SCRATCH')
    if s:
        return Path(s)
    c = sorted(Path('/tmp').glob('claude-*/*/*/scratchpad'), key=lambda p: p.stat().st_mtime, reverse=True)
    return c[0] if c else None


def candidatos(S):
    for raiz, dirs, fichs in os.walk(S):
        rel = Path(raiz).relative_to(S)
        dirs[:] = [d for d in dirs if d not in EXCLUIR_NOMES and (rel / d).as_posix() not in EXCLUIR_RUTAS]
        for f in fichs:
            p = Path(raiz) / f
            if p.suffix.lower() in EXT and not p.is_symlink():
                yield p


def contido(p):
    """Bytes que se gardan: o ficheiro enteiro, ou a cola se é un texto grande; None se é grande e non é texto."""
    n = p.stat().st_size
    if n <= MAX_BYTES:
        return p.read_bytes()
    if p.suffix.lower() in {'.log', '.txt', '.jsonl'}:
        with open(p, 'rb') as f:
            linas = f.read().splitlines()[-COLA_LINAS:]
        cab = f'[instantanea: recortado; o orixinal ten {n} bytes, gárdanse as últimas {len(linas)} liñas]\n'.encode()
        return cab + b'\n'.join(linas) + b'\n'
    return None


def copiar(S):
    gardados, saltados, total = [], [], 0
    vistos = set()
    for p in sorted(candidatos(S)):
        rel = p.relative_to(S)
        try:
            b = contido(p)
        except OSError:
            continue
        if b is None or total + len(b) > TOPE_TOTAL:
            saltados.append((rel.as_posix(), p.stat().st_size)); continue
        d = DEST / rel
        vistos.add(d)
        total += len(b)
        if not d.exists() or hashlib.sha256(d.read_bytes()).digest() != hashlib.sha256(b).digest():
            d.parent.mkdir(parents=True, exist_ok=True)
            tmp = d.with_name('.' + d.name + '.tmp')
            tmp.write_bytes(b); os.replace(tmp, d)
        gardados.append((rel.as_posix(), len(b)))
    # o que desapareceu do scratchpad tamén desaparece da instantánea (o historial de git consérvao)
    for d in DEST.rglob('*'):
        if d.is_file() and d not in vistos and d.name != 'INDICE.md':
            d.unlink()
    L = ['# Instantánea do scratchpad (Gauntlet 4)', '',
         f'Xerada por `herramientas/gauntlet/instantanea.py` o {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC desde `{S}`.',
         'Só ficheiros de texto pequenos (scripts, notas, medidas, rexistros recortados); nada de modelos, binarios nin',
         'materiais a cegas. Para relanzar unha peza, ler antes `plan-de-negocio/gauntlet4/estado.md`.', '',
         f'{len(gardados)} ficheiros, {total / 1e6:.1f} MB.', '']
    if saltados:
        L += ['## Saltados (grandes de máis e non son texto)', ''] + [f'- `{r}` ({n} bytes)' for r, n in saltados] + ['']
    DEST.mkdir(parents=True, exist_ok=True)
    (DEST / 'INDICE.md').write_text('\n'.join(L) + '\n')
    return len(gardados), total


def git(*a, check=True):
    return subprocess.run(['git', '-C', str(REPO), *a], capture_output=True, text=True, check=check)


def commit_push():
    ruta = DEST.relative_to(REPO).as_posix()
    for intento in range(6):
        try:
            git('add', '-A', '--', ruta)
            if git('diff', '--cached', '--quiet', '--', ruta, check=False).returncode == 0:
                return 'sen cambios'
            git('commit', '-q', '-m', 'Gauntlet 4: instantánea do scratchpad (scripts, notas e medidas dos axentes)\n\n'
                'Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\n'
                'Claude-Session: https://claude.ai/code/session_011Mvqh6XmuGVpmihPtorogQ', '--', ruta)
            break
        except subprocess.CalledProcessError as e:          # index.lock doutro axente: agardar e reintentar
            if intento == 5:
                return f'commit fallou: {e.stderr.strip()[:200]}'
            time.sleep(7)
    for intento in range(4):
        r = git('push', '-q', 'origin', RAMA, check=False)
        if r.returncode == 0:
            return 'commit e push'
        time.sleep(2 ** (intento + 1))
    return f'push fallou: {r.stderr.strip()[:200]}'


# Autogardado do traballo en curso dos axentes no repo (petición do promotor, 02-10-2026): ficheiros novos ou
# cambiados destas carpetas que leven QUEDOS polo menos AUTO_QUEDO s (para non coller un ficheiro a medio escribir).
# Só texto e imaxes pequenas: vídeo e audio non, porque hai que validalos con ffmpeg antes de subilos (CLAUDE.md).
AUTO_RUTAS = ('plan-de-negocio/gauntlet4', 'herramientas')
AUTO_EXT = EXT | {'.jpg', '.jpeg', '.png'}
AUTO_MAX = {'.jpg': 3_000_000, '.jpeg': 3_000_000, '.png': 3_000_000}
AUTO_QUEDO = 120


def autogardar():
    r = git('status', '--porcelain', '-uall', '--', *AUTO_RUTAS, check=False)
    ruta_inst = DEST.relative_to(REPO).as_posix()
    xa = []
    for liña in r.stdout.splitlines():
        estado, f = liña[:2], liña[3:].strip().strip('"')
        if ' -> ' in f or f.startswith(ruta_inst):
            continue
        p = REPO / f
        if 'D' in estado or not p.is_file():
            continue
        ext = p.suffix.lower()
        if ext not in AUTO_EXT or p.stat().st_size > AUTO_MAX.get(ext, 5_000_000):
            continue
        if time.time() - p.stat().st_mtime < AUTO_QUEDO:
            continue
        xa.append(f)
    if not xa:
        return 'autogardado: nada'
    for intento in range(6):
        try:
            git('add', '--', *xa)
            git('commit', '-q', '-m', f'Gauntlet 4: autogardado do traballo en curso dos axentes ({len(xa)} ficheiros)\n\n'
                'Commit automático de herramientas/gauntlet/instantanea.py: ficheiros de texto e imaxes pequenas quedos\n'
                f'≥ {AUTO_QUEDO} s; os axentes seguen traballando e poden cambialos despois.\n\n'
                'Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\n'
                'Claude-Session: https://claude.ai/code/session_011Mvqh6XmuGVpmihPtorogQ', '--', *xa)
            break
        except subprocess.CalledProcessError as e:
            if intento == 5:
                return f'autogardado: commit fallou: {e.stderr.strip()[:200]}'
            time.sleep(7)
    r = git('push', '-q', 'origin', RAMA, check=False)
    return f'autogardado: {len(xa)} ficheiros' + ('' if r.returncode == 0 else f' (push fallou: {r.stderr.strip()[:120]})')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--bucle', type=int, default=0, help='segundos entre instantáneas (0 = unha soa vez)')
    ap.add_argument('--autogardar', action='store_true', help='gardar tamén o traballo en curso de gauntlet4/ e herramientas/')
    a = ap.parse_args()
    while True:
        S = scratch()
        if S and S.exists():
            n, total = copiar(S)
            print(f'{datetime.now(timezone.utc):%H:%M:%S} {n} ficheiros, {total / 1e6:.1f} MB: {commit_push()}', flush=True)
        if a.autogardar:
            print(f'{datetime.now(timezone.utc):%H:%M:%S} {autogardar()}', flush=True)
        if not a.bucle:
            break
        time.sleep(a.bucle)


if __name__ == '__main__':
    sys.exit(main())
