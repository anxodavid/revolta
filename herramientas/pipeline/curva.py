"""Curva do embude para vídeos longos (Gauntlet 3): gancho vivo ao principio e baixada gradual ao ton de durmir.

Todo o que cambia co avance do episodio (ritmo e ton da voz, pausas, duración dos planos, fundidos, luz) sae
dunha soa curva, para que voz, imaxe e montaxe baixen xuntas. A posición mídese en palabras do guion (a voz vai
máis lenta co tempo, así que as palabras son unha medida estable antes de ter o audio).

Nós da curva (palabras):
  0          comezo do gancho (arranque en frío)
  GANCHO     fin do gancho (~2 min de narración viva)
  TRANSICION fin da transición (~8 min)
  CALMA      metade do episodio: desde aquí, ton de durmir
  total      fin do episodio

Os valores de voz (escala, estilo, f0_*, enerxia, beta, embedding_scale) calibrounos a peza VOZ con medidas
automáticas (gauntlet3/voz/informe.md): nos 5 nós, o arousal (0,64 -> 0,43), a desviación da F0 (4,8 -> 2,6 st) e a
velocidade (7,6 -> 5,2 síl/s; 182 -> 113 palabras/min con pausas) baixan en cada paso e o WER frase a frase queda
<= 0,054. Os de imaxe, a peza VISUAL; as pausas e os planos veñen da ronda 3 do Gauntlet 2 estendidos.
"""
GANCHO, TRANSICION = 280, 950

# Valores en cada nó: [comezo, fin do gancho, fin da transición, metade, final]
CURVA = {
    # ritmo da voz e da montaxe
    'escala':        [0.97, 1.03, 1.14, 1.24, 1.30],   # escala das duracións de StyleTTS2 (máis alta = máis lenta)
    'pausa_frase':   [0.45, 0.55, 0.85, 1.15, 1.40],   # silencio entre frases (s)
    'pausa_parrafo': [0.35, 0.45, 0.75, 1.00, 1.30],   # silencio extra entre parágrafos (s)
    'pausa_capitulo': [1.2, 1.6, 2.4, 3.0, 3.5],      # silencio extra antes dun capítulo novo (s), co rótulo en pantalla
    'plano_s':       [5.0, 6.5, 10.0, 14.0, 17.0],     # duración obxectivo dun plano (s)
    'fundido_s':     [0.7, 1.0, 1.5, 2.2, 2.8],        # fundido encadeado cara a ese plano (s)
    # ton da voz (peza VOZ, voz_st2.py): estilo 0 = referencia viva (REF_WAV), 1 = calma (REF_WAV_CALMO); F0 e
    # enerxía como multiplicadores (f0_rango escala o log F0 arredor da media da frase); beta = canto manda o estilo
    # predito do texto fronte á referencia (máis baixo = máis a referencia calma); embedding_scale = guía do texto
    'estilo':        [0.0, 0.2, 0.6, 0.9, 1.0],
    'f0_rango':      [1.2, 1.1, 0.95, 0.82, 0.76],     # amplitude da entoación arredor da media
    'f0_media':      [1.02, 1.005, 0.985, 0.965, 0.955],  # altura media
    'enerxia':       [1.00, 1.00, 0.98, 0.96, 0.95],   # sobre todo volume: o nivel lévao ganancia_db
    'beta':          [0.8, 0.75, 0.6, 0.45, 0.4],
    'embedding_scale': [1.4, 1.2, 1.0, 1.0, 1.0],
    'ganancia_db':   [0.8, 0.5, 0.0, -0.8, -1.5],       # nivel relativo da voz na mestura
    # son (orquestador): nivel do ambiente (choiva2) respecto do de base (17 dB baixo a voz): case nada no gancho,
    # máis presente ao durmir (o promotor oíu a choiva da mostra como "ruído branco": ver son.py)
    'ambiente_db':   [-8.0, -6.0, -3.0, 0.0, 1.5],
    # imaxe (peza VISUAL): intensidade da luz e do contraste da gradación
    'contraste':     [1.08, 1.05, 1.00, 0.94, 0.90],
    'brillo':        [1.00, 1.00, 0.96, 0.88, 0.80],   # Gauntlet 3 r2 visual: calma e durmir máis escuros
}
VOZ = ('estilo', 'f0_rango', 'f0_media', 'enerxia', 'beta', 'embedding_scale')   # campos por frase de voz_st2.py
FASES = ('gancho', 'transicion', 'calma', 'durmir')


def nos(total):
    """Posicións (palabras) dos nós para un guion de `total` palabras."""
    total = max(total, TRANSICION + 200)
    metade = max(TRANSICION + 100, total // 2)
    return [0, GANCHO, TRANSICION, metade, total]


def en(pal, total):
    """Valores da curva na palabra `pal` dun guion de `total` palabras (interpolación lineal entre nós)."""
    xs = nos(total)
    pal = min(max(pal, 0), xs[-1])
    k = max(i for i in range(len(xs) - 1) if xs[i] <= pal) if pal < xs[-1] else len(xs) - 2
    u = (pal - xs[k]) / max(1, xs[k + 1] - xs[k])
    out = {n: v[k] + (v[k + 1] - v[k]) * u for n, v in CURVA.items()}
    out['fase'] = FASES[min(k, len(FASES) - 1)]
    out['u'] = round(pal / max(1, xs[-1]), 4)       # posición relativa no episodio (0-1)
    return out
