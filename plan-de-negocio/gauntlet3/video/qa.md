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

- Duración: 31:22 (1882.04 s), 1920x1080 a 24.0 fps, 330.6 MB, 1405 kb/s.
- Palabras do guion: 3952. Ritmo por fase (palabras/min, pausas incluídas): {'gancho': 157.0, 'transicion': 154.5, 'calma': 136.3, 'durmir': 114.5}.
- Planos por fase: {'gancho': 21, 'transicion': 37, 'calma': 39, 'durmir': 65}; duración media por fase (s): {'gancho': 5.2, 'transicion': 7.2, 'calma': 11.6, 'durmir': 16.2}.
- ASR (Whisper galego de Nós) sobre a mestura, frase a frase no seu treito: WER 0.03; frases que soan no seu treito 100.0 %.
- Sonoridade: -17.1 LUFS, LRA 10.1 LU, pico real -1.7 dBTP; desfase A/V 0.02 s.
- Ambiente sonoro (D13): modo escena; lume 302.0 s, fonte 108.4 s, noite 526.4 s, aldea 130.0 s, mar 61.9 s, xente 21.6 s, choiva 300.8 s, campas 12.6 s; voz limpa 38.7 % do tempo de voz.
- Lingua (LanguageTool gl-ES + hunspell): 0 avisos. H1: 0 sen ancorar.
- Veracidade: 240 frases, 0 marcadas polo verificador automático, 0 sen xustificación (as xustificacións escribiunas o crítico de veracidade, un axente Claude).
- Imaxes: 162 planos; 124 aprobados pola porta; 377 imaxes xeradas.
- Tempo: 177.3 min de reloxo e 9.89 h de CPU de núcleo (etapas: 1_texto 4.8 min, 3_voz 13.5 min, 4_escenas 0.0 min, 5_imaxes 37.8 min, 6_son 7.0 min, 7_montaxe 77.5 min, 8_qa 36.7 min).

## Capítulos

- 1:55 I. Sete fontes e un gato
- 4:38 II. O conxuro do barco
- 6:39 III. O tribunal e os xuíces
- 9:14 IV. Quen eran de verdade
- 12:09 V. Á beira da lareira
- 16:21 VI. A noite de san Xoán
- 22:49 VII. O frade que dubidaba
- 26:51 VIII. Chove na lousa

## Nota da execución

Rolda de arranxos do tribunal final (01-10-2026): Claude (Anthropic) reescribiu a man os prompts dos planos 5, 31, 56, 61, 67, 84, 91, 133, 145, 153 e 161 e engadiu á porta os anacronismos que se escaparan. Mirou cada intento ao saír e volveu reescribir os dos planos 5, 31, 61, 67 e 91 (aldeas inglesas, un corredor moderno, farolas, estrada asfaltada e un salón con estufa; dous deles pasaran a porta automática). Nos planos 91 e 145 Claude escolleu a man o intento 0 en vez do que escollera a porta (lámpada acesa ao fondo; carballeira que repetía o plano 11); queda anotado en revision.json. Só eses planos se xeraron de novo; o resto saíu da caché da produción anterior. O limitador mide agora o pico real. Ningunha persoa viu nin escoitou o resultado.
