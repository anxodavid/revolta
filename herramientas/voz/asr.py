import json, re, glob, jiwer
from faster_whisper import WhisperModel
m = WhisperModel('medium', device='cpu', compute_type='int8')
def norm(t):
    t = t.lower(); t = re.sub(r"[^\wáéíóúüñç ]", " ", t); return re.sub(r"\s+", " ", t).strip()
def tr(p):
    segs, _ = m.transcribe(p, language='gl', beam_size=5); return ' '.join(s.text for s in segs)
res = {}
idx = json.load(open('kit/t1/index.json'))
for it in idx:
    for kind in ('human', 'tts'):
        p = f"kit/t1/{it['voice']}_{it['i']}_{kind}.wav"; h = tr(p)
        res[p] = {'wer': round(jiwer.wer(norm(it['text']), norm(h)), 3), 'hyp': h}
ref = open('texto_provisional.txt').read()
for p in sorted(glob.glob('kit/t2/*.wav')):
    h = tr(p); res[p] = {'wer': round(jiwer.wer(norm(ref), norm(h)), 3), 'hyp': h}
json.dump(res, open('kit/asr.json', 'w'), ensure_ascii=False, indent=1)
for p, r in res.items(): print(f"{p:32s} WER={r['wer']}")
