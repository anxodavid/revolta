# QA automático: As meigas de verdade (meigas-de-verdade)

Informe xerado por `herramientas/pipeline/longo.py`. Ningunha persoa revisou o vídeo, o guion nin as imaxes.

**Veredicto das portas automáticas: NON PUBLICABLE** (12/13).

## Quen fixo que

- Guion: Claude (Anthropic), con axentes no Gauntlet 3: un axente constructor escribe e críticos independentes revisan. Non é unha execución desatendida nin un LLM por API. Ningunha persoa o revisou.
- Lista de planos (prompts das imaxes): Claude (Anthropic), un axente escribe un prompt por plano.
- Automático e local: voz (Nós StyleTTS2), imaxes e a súa porta de revisión, son, montaxe e controis automáticos

## Portas

| Porta | Resultado |
|---|---|
| autoria_declarada | ✅ |
| duracion | ✅ |
| wer_mestura | ✅ |
| sincronia_av | ✅ |
| sincronia_subtitulos | ✅ |
| lingua_lt | ✅ |
| h1_ancoraxe | ✅ |
| veracidade | ✅ |
| estilo | ✅ |
| imaxes_revisadas | ❌ |
| sonoridade | ✅ |
| bitrate | ✅ |
| resolucion | ✅ |

## Medidas

- Duración: 31:22 (1882.04 s), 1920x1080 a 24.0 fps, 333.4 MB, 1417 kb/s.
- Palabras do guion: 3952. Ritmo por fase (palabras/min, pausas incluídas): {'gancho': 157.0, 'transicion': 154.5, 'calma': 136.3, 'durmir': 114.5}.
- Planos por fase: {'gancho': 21, 'transicion': 37, 'calma': 39, 'durmir': 65}; duración media por fase (s): {'gancho': 5.2, 'transicion': 7.2, 'calma': 11.6, 'durmir': 16.2}.
- ASR (Whisper galego de Nós) sobre a mestura, frase a frase no seu treito: WER 0.031; frases que soan no seu treito 100.0 %.
- Sonoridade: -17.1 LUFS, LRA 10.2 LU, pico real -0.1 dBTP; desfase A/V 0.02 s.
- Ambiente sonoro (D13): modo escena; lume 302.0 s, fonte 108.4 s, noite 526.4 s, aldea 130.0 s, mar 61.9 s, xente 21.6 s, choiva 300.8 s, campas 12.6 s; voz limpa 38.7 % do tempo de voz.
- Lingua (LanguageTool gl-ES + hunspell): 0 avisos. H1: 0 sen ancorar.
- Veracidade: 240 frases, 0 marcadas polo verificador automático, 0 sen xustificación (as xustificacións escribiunas o crítico de veracidade, un axente Claude).
- Imaxes: 162 planos; 127 aprobados pola porta; 396 imaxes xeradas.
- Tempo: 285.9 min de reloxo e 16.55 h de CPU de núcleo (etapas: 1_texto 27.2 min, 3_voz 16.0 min, 4_escenas 0.0 min, 5_imaxes 141.9 min, 6_son 2.7 min, 7_montaxe 66.8 min, 8_qa 31.3 min).

## Capítulos

- 1:55 I. Sete fontes e un gato
- 4:38 II. O conxuro do barco
- 6:39 III. O tribunal e os xuíces
- 9:14 IV. Quen eran de verdade
- 12:09 V. Á beira da lareira
- 16:21 VI. A noite de san Xoán
- 22:49 VII. O frade que dubidaba
- 26:51 VIII. Chove na lousa
