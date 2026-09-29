"""Capa LLM do pipeline.

Cada chamada renderiza un prompt de prompts/ coas súas variables, calcula o hash do texto
renderizado e busca a resposta na caché (llm_cache/<etapa>-<hash>.txt). Se non está:

- backend "openai": chama a un servidor compatible coa API de OpenAI (llama.cpp server,
  vLLM, Ollama...) en $LLM_URL co modelo $LLM_MODEL e garda a resposta na caché.
- backend "manual": escribe o prompt en llm_pending/<etapa>-<hash>.prompt.md e sae co código 3.
  Un LLM externo (na mostra, Claude Opus 5.5 actuando como LLM) escribe a resposta en
  llm_cache/<etapa>-<hash>.txt e vólvese lanzar o mesmo comando. Non hai edición humana.

A caché fai o proceso reproducible: co mesmo tema e os mesmos prompts sae o mesmo guion.
"""
import hashlib, json, os, sys, time, urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
CACHE = Path(os.environ.get('LLM_CACHE', HERE / 'llm_cache'))
PENDING = Path(os.environ.get('LLM_PENDING', HERE / 'llm_pending'))


class PendingLLM(Exception):
    pass


def render(prompt_name, **vars):
    tpl = (HERE / 'prompts' / f'{prompt_name}.md').read_text()
    body = tpl.split('-->', 1)[1].lstrip() if tpl.startswith('<!--') else tpl
    for k, v in vars.items():
        body = body.replace('{' + k + '}', str(v))
    return body


def complete(prompt_name, backend=None, **vars):
    backend = backend or os.environ.get('LLM_BACKEND', 'manual')
    prompt = render(prompt_name, **vars)
    h = hashlib.sha256(prompt.encode()).hexdigest()[:12]
    CACHE.mkdir(parents=True, exist_ok=True)
    out = CACHE / f'{prompt_name}-{h}.txt'
    if out.exists():
        return out.read_text().strip(), {'cache': out.name, **_meta(out)}
    if backend == 'openai':
        url = os.environ.get('LLM_URL', 'http://127.0.0.1:8080') + '/v1/chat/completions'
        model = os.environ.get('LLM_MODEL', 'local')
        req = urllib.request.Request(url, data=json.dumps({
            'model': model, 'temperature': float(os.environ.get('LLM_TEMP', '0.7')),
            'messages': [{'role': 'user', 'content': prompt}]}).encode(),
            headers={'Content-Type': 'application/json',
                     'Authorization': 'Bearer ' + os.environ.get('LLM_KEY', 'none')})
        t = time.time()
        r = json.load(urllib.request.urlopen(req, timeout=3600))
        txt = r['choices'][0]['message']['content'].strip()
        out.write_text(txt + '\n')
        meta = {'backend': 'openai', 'model': model, 'url': url, 'segundos': round(time.time() - t, 1),
                'usage': r.get('usage')}
        out.with_suffix('.meta.json').write_text(json.dumps(meta, ensure_ascii=False, indent=1))
        return txt, {'cache': out.name, **meta}
    PENDING.mkdir(parents=True, exist_ok=True)
    p = PENDING / f'{prompt_name}-{h}.prompt.md'
    p.write_text(prompt)
    raise PendingLLM(f'Falta a resposta do LLM para "{prompt_name}". Prompt: {p}\n'
                     f'Escribe a resposta en {out} e volve lanzar o comando.')


def _meta(out):
    m = out.with_suffix('.meta.json')
    return json.loads(m.read_text()) if m.exists() else {}
