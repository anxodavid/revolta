"""Capa LLM do pipeline.

Cada chamada renderiza un prompt de prompts/ coas súas variables, calcula o hash do texto
renderizado e busca a resposta na caché (<caché>/<etapa>-<hash>.txt). Se non está:

- backend "openai" (o do canal): chama a un servidor local compatible coa API de OpenAI
  (llama-cpp-python, llama.cpp server, vLLM, Ollama) en $LLM_URL co modelo $LLM_MODEL e garda a
  resposta e os seus metadatos (modelo, tokens, segundos) na caché. Se $LLM_SERVER_CMD está
  definido e o servidor non responde, o propio pipeline arráncao e párao ao rematar as etapas LLM:
  un só comando, sen ningunha persoa nin axente externo polo medio.
  $LLM_FORMATO: "chat" (/v1/chat/completions, modelos con plantilla de chat) ou "user-assistant"
  (/v1/completions co formato "User:\\n ...\\nAssistant:\\n" das instrucións de adestramento de
  Llama-3.1-Carballo-Instr3, que non trae plantilla de chat).
- backend "manual" (só para depurar prompts): escribe o prompt en <pendentes>/<etapa>-<hash>.prompt.md
  e sae co código 3. Unha resposta escrita a man ou por un LLM externo NON é unha execución desatendida;
  a ronda 1 da mostra (29-09-2026) fíxose así con Claude Opus 5.5 e por iso non contaba.

A caché vai por defecto no directorio de traballo de cada execución (pipeline.py fixa CACHE), así
unha execución en --traballo baleiro chama de verdade ao LLM.
"""
import hashlib, json, os, shlex, subprocess, sys, time, urllib.request, urllib.error
from pathlib import Path

HERE = Path(__file__).resolve().parent
CACHE = Path(os.environ.get('LLM_CACHE', HERE / 'llm_cache'))
PENDING = Path(os.environ.get('LLM_PENDING', HERE / 'llm_pending'))
_SERVER = {}


class PendingLLM(Exception):
    pass


def render(prompt_name, **vars):
    tpl = (HERE / 'prompts' / f'{prompt_name}.md').read_text()
    body = tpl.split('-->', 1)[1].lstrip() if tpl.startswith('<!--') else tpl
    for k, v in vars.items():
        body = body.replace('{' + k + '}', str(v))
    return body


def _url():
    return os.environ.get('LLM_URL', 'http://127.0.0.1:8080')


def _vivo():
    try:
        urllib.request.urlopen(_url() + '/v1/models', timeout=5).read(); return True
    except Exception:
        return False


def arrancar():
    """Arranca o servidor local se $LLM_SERVER_CMD está definido e non hai ningún escoitando."""
    if _vivo() or 'proc' in _SERVER:
        return
    cmd = os.environ.get('LLM_SERVER_CMD')
    if not cmd:
        raise RuntimeError(f'Non hai servidor LLM en {_url()} e LLM_SERVER_CMD non está definido')
    log = open(os.environ.get('LLM_SERVER_LOG', '/dev/null'), 'a')
    t = time.time()
    _SERVER['proc'] = subprocess.Popen(shlex.split(cmd), stdout=log, stderr=log)
    while not _vivo():
        if _SERVER['proc'].poll() is not None or time.time() - t > 600:
            raise RuntimeError('O servidor LLM non arrancou (ver LLM_SERVER_LOG)')
        time.sleep(2)
    _SERVER['arranque_s'] = round(time.time() - t, 1)
    _SERVER['arranque_cpu_s'] = round(_cpu_servidor() or 0, 1)
    _SERVER['comando'] = cmd
    print(f'servidor LLM listo en {_SERVER["arranque_s"]} s', flush=True)


def _cpu_servidor():
    p = _SERVER.get('proc')
    if not p:
        return None
    try:
        x = open(f'/proc/{p.pid}/stat').read().rsplit(')', 1)[1].split()
        return (int(x[11]) + int(x[12])) / os.sysconf('SC_CLK_TCK')
    except Exception:
        return None


def parar():
    p = _SERVER.pop('proc', None)
    if p:
        p.terminate()
        try: p.wait(30)
        except subprocess.TimeoutExpired: p.kill()


def _chamar(prompt):
    fmt = os.environ.get('LLM_FORMATO', 'chat')
    model = os.environ.get('LLM_MODEL', 'local')
    common = {'model': model, 'temperature': float(os.environ.get('LLM_TEMP', '0.6')),
              'top_p': float(os.environ.get('LLM_TOP_P', '0.9')),
              'repeat_penalty': float(os.environ.get('LLM_REPEAT_PENALTY', '1.1')),
              'max_tokens': int(os.environ.get('LLM_MAX_TOKENS', '2200')),
              'seed': int(os.environ.get('LLM_SEED', '1'))}
    if fmt == 'user-assistant':
        url = _url() + '/v1/completions'
        body = {**common, 'prompt': 'User:\n ' + prompt.strip() + '\nAssistant:\n', 'stop': ['\nUser:']}
    else:
        url = _url() + '/v1/chat/completions'
        body = {**common, 'messages': [{'role': 'user', 'content': prompt}]}
    req = urllib.request.Request(url, data=json.dumps(body).encode(), headers={
        'Content-Type': 'application/json', 'Authorization': 'Bearer ' + os.environ.get('LLM_KEY', 'none')})
    t = time.time()
    r = json.load(urllib.request.urlopen(req, timeout=7200))
    ch = r['choices'][0]
    txt = (ch.get('text') if fmt == 'user-assistant' else ch['message']['content']).strip()
    s = time.time() - t
    u = r.get('usage') or {}
    meta = {'backend': 'openai', 'modelo': model, 'formato': fmt, 'url': url, 'segundos': round(s, 1),
            'usage': u, 'fin': ch.get('finish_reason'),
            'tokens_saida_por_s': round(u.get('completion_tokens', 0) / s, 2) if s else None,
            'parametros': {k: v for k, v in common.items() if k != 'model'}}
    if os.environ.get('LLM_MODEL_FILE'):
        meta['ficheiro_modelo'] = os.environ['LLM_MODEL_FILE']
    if os.environ.get('LLM_MODEL_SHA256'):
        meta['sha256_modelo'] = os.environ['LLM_MODEL_SHA256']
    return txt, meta


def complete(prompt_name, backend=None, **vars):
    backend = backend or os.environ.get('LLM_BACKEND', 'openai')
    prompt = render(prompt_name, **vars)
    h = hashlib.sha256(prompt.encode()).hexdigest()[:12]
    CACHE.mkdir(parents=True, exist_ok=True)
    out = CACHE / f'{prompt_name}-{h}.txt'
    if out.exists():
        return out.read_text().strip(), {'cache': out.name, 'da_cache': True, **_meta(out)}
    if backend == 'openai':
        arrancar()
        (CACHE / f'{prompt_name}-{h}.prompt.md').write_text(prompt)
        c0 = _cpu_servidor()
        txt, meta = _chamar(prompt)
        if c0 is not None:
            meta['cpu_s_servidor'] = round(_cpu_servidor() - c0, 1)
        out.write_text(txt + '\n')
        out.with_suffix('.meta.json').write_text(json.dumps(meta, ensure_ascii=False, indent=1))
        print(f"LLM {prompt_name}: {meta['segundos']} s, {meta['usage']}", flush=True)
        return txt, {'cache': out.name, 'da_cache': False, **meta}
    PENDING.mkdir(parents=True, exist_ok=True)
    p = PENDING / f'{prompt_name}-{h}.prompt.md'
    p.write_text(prompt)
    raise PendingLLM(f'Falta a resposta do LLM para "{prompt_name}". Prompt: {p}\n'
                     f'Modo manual (só depuración): escribe a resposta en {out} e volve lanzar o comando.')


def _meta(out):
    m = out.with_suffix('.meta.json')
    return json.loads(m.read_text()) if m.exists() else {}
