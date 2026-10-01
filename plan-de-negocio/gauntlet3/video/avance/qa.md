# QA automático: As meigas de verdade (meigas-de-verdade)

Informe xerado por `herramientas/pipeline/longo.py`. Ningunha persoa revisou o vídeo, o guion nin as imaxes.

**Veredicto das portas automáticas: NON PUBLICABLE** (10/13).

## Quen fixo que

- Guion: Claude (Anthropic), con axentes no Gauntlet 3: un axente constructor escribe e críticos independentes revisan. Non é unha execución desatendida nin un LLM por API. Ningunha persoa o revisou.
- Lista de planos (prompts das imaxes): Claude (Anthropic), un axente escribe un prompt por plano.
- Automático e local: voz (Nós StyleTTS2), imaxes e a súa porta de revisión, son, montaxe e controis automáticos

## Portas

| Porta | Resultado |
|---|---|
| autoria_declarada | ✅ |
| duracion | ❌ |
| wer_mestura | ✅ |
| sincronia_av | ✅ |
| sincronia_subtitulos | ✅ |
| lingua_lt | ✅ |
| h1_ancoraxe | ✅ |
| veracidade | ✅ |
| estilo | ✅ |
| imaxes_revisadas | ❌ |
| sonoridade | ❌ |
| bitrate | ✅ |
| resolucion | ✅ |

## Medidas

- Duración: 4:50 (289.75 s), 1920x1080 a 24.0 fps, 53.2 MB, 1468 kb/s.
- Palabras do guion: 3952. Ritmo por fase (palabras/min, pausas incluídas): {'gancho': 157.0, 'transicion': 159.8}.
- Planos por fase: {'gancho': 21, 'transicion': 26, 'calma': 0, 'durmir': 0}; duración media por fase (s): {'gancho': 5.2, 'transicion': 7.0}.
- ASR (Whisper galego de Nós) sobre a mestura, frase a frase no seu treito: WER 0.031; frases que soan no seu treito 100.0 %.
- Sonoridade: -18.5 LUFS, LRA 5.5 LU, pico real -1.1 dBTP; desfase A/V 0.02 s.
- Ambiente sonoro (D13): modo escena; lume 20.0 s, fonte 11.9 s, noite 11.9 s, aldea 130.0 s, mar 12.0 s; voz limpa 39.6 % do tempo de voz.
- Lingua (LanguageTool gl-ES + hunspell): 0 avisos. H1: 0 sen ancorar.
- Veracidade: 240 frases, 0 marcadas polo verificador automático, 0 sen xustificación (as xustificacións escribiunas o crítico de veracidade, un axente Claude).
- Imaxes: 47 planos; 43 aprobados pola porta; 104 imaxes xeradas.
- Tempo: 21.1 min de reloxo e 1.09 h de CPU de núcleo (etapas: 1_texto 0.0 min, 3_voz 0.3 min, 4_escenas 0.0 min, 5_imaxes 1.8 min, 6_son 0.3 min, 7_montaxe 10.9 min, 8_qa 7.7 min).

## Capítulos

- 1:55 I. Sete fontes e un gato
- 4:38 II. O conxuro do barco

## Nota da execución

Avance: planos 0-46 do episodio (arranque en frío, cabeceira, capítulo I e entrada do II), montado mentres se xeran as demais imaxes.
