"""Medidas con modelos (peza VOZ do Gauntlet 3): WER con Whisper galego de Nós e arousal con audeering.

- ASR: faster-whisper co modelo proxectonos/whisper-large-v3-turbo-gl-v1.0 en CTranslate2 int8 (WHISPER_DIR), coas
  mesmas opcións que qa.asr do pipeline (gl, beam 5, sen VAD, sen condicionar ao texto anterior). WER con jiwer
  sobre o texto normalizado con qa.norm.
- Emoción dimensional: audeering/wav2vec2-large-robust-12-ft-emotion-msp-dim (arousal, dominancia, valencia, ~0-1).
  LICENZA CC-BY-NC-SA-4.0: SÓ PARA AVALIACIÓN INTERNA, nunca no produto. Adestrado en inglés (MSP-Podcast): en galego
  mide sobre todo o acústico (ritmo, ton, esforzo); serve para comparar versións da mesma voz, non como valor
  absoluto. O procesador normaliza o sinal (media 0, varianza 1): o volume non lle afecta.

Todo o pesado vai co candado de CPU: quen chama estes módulos lánzase con  flock "$CPU_LOCK" ...
"""
import os, sys
import numpy as np
import soundfile as sf

sys.path.insert(0, '/home/user/revolta/herramientas/pipeline')
AROUSAL = 'audeering/wav2vec2-large-robust-12-ft-emotion-msp-dim'


def norm(t):
    import qa
    return qa.norm(t)


class ASR:
    def __init__(self, nth=4):
        from faster_whisper import WhisperModel
        self.m = WhisperModel(os.environ['WHISPER_DIR'], device='cpu', compute_type='int8', cpu_threads=nth)

    def transcribir(self, path):
        segs, _ = self.m.transcribe(path, language='gl', beam_size=5, vad_filter=False,
                                    condition_on_previous_text=False)
        return ' '.join(s.text for s in segs).strip()

    def wer(self, path, ref):
        import jiwer
        hip = self.transcribir(path)
        r = jiwer.process_words(norm(ref), norm(hip))
        return {'wer': round(r.wer, 4), 'erros': r.substitutions + r.deletions + r.insertions,
                'palabras_ref': len(norm(ref).split()), 'hipotese': hip}


class Emocion:
    def __init__(self, nth=4):
        import torch, torch.nn as nn
        from transformers import Wav2Vec2FeatureExtractor
        from transformers.models.wav2vec2.modeling_wav2vec2 import Wav2Vec2Model, Wav2Vec2PreTrainedModel
        torch.set_num_threads(nth)

        class RegressionHead(nn.Module):
            def __init__(self, config):
                super().__init__()
                self.dense = nn.Linear(config.hidden_size, config.hidden_size)
                self.dropout = nn.Dropout(config.final_dropout)
                self.out_proj = nn.Linear(config.hidden_size, config.num_labels)

            def forward(self, x):
                return self.out_proj(torch.tanh(self.dense(self.dropout(x))))

        class EmotionModel(Wav2Vec2PreTrainedModel):
            def __init__(self, config):
                super().__init__(config)
                self.config = config
                self.wav2vec2 = Wav2Vec2Model(config)
                self.classifier = RegressionHead(config)
                self.post_init()

            def forward(self, input_values):
                h = self.wav2vec2(input_values)[0]
                return self.classifier(torch.mean(h, dim=1))

        self.torch = torch
        self.fe = Wav2Vec2FeatureExtractor.from_pretrained(AROUSAL)
        self.m = EmotionModel.from_pretrained(AROUSAL).eval()

    def medir(self, path_ou_wav, sr=None):
        import librosa
        if isinstance(path_ou_wav, str):
            w, sr = sf.read(path_ou_wav, dtype='float32')
        else:
            w = path_ou_wav
        if w.ndim > 1:
            w = w.mean(1)
        if sr != 16000:
            w = librosa.resample(w, orig_sr=sr, target_sr=16000)
        x = self.fe(w, sampling_rate=16000)['input_values'][0].reshape(1, -1)
        with self.torch.no_grad():
            a, d, v = self.m(self.torch.from_numpy(np.asarray(x, dtype=np.float32)))[0].tolist()
        return {'arousal': round(a, 4), 'dominancia': round(d, 4), 'valencia': round(v, 4)}
