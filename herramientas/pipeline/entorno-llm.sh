# Entorno do LLM local da mostra (29-09-2026). SCRATCH: directorio con llm/venv e o GGUF.
export LLM_URL=http://127.0.0.1:8080 LLM_MODEL=eurollm-9b-instruct-2512-q4km LLM_FORMATO=chat
export LLM_MODEL_FILE=mradermacher/EuroLLM-9B-Instruct-2512-GGUF/EuroLLM-9B-Instruct-2512.Q4_K_M.gguf
export LLM_MODEL_SHA256=fe9b50d4ba67eb0131f1ceeaab2e56ea8fb6b2bbc37391d3219c791c3b140a28
export LLM_SERVER_CMD="$SCRATCH/llm/venv/bin/python -m llama_cpp.server --model $SCRATCH/llm/eurollm-9b-instruct-2512.Q4_K_M.gguf --model_alias eurollm-9b-instruct-2512-q4km --n_ctx 8192 --n_threads 4 --use_mmap false --host 127.0.0.1 --port 8080"
export LLM_SERVER_LOG=$SCRATCH/llm/server.log LLM_TEMP=0.3 LLM_MAX_TOKENS=1600
