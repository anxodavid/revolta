"""Fragmento de proba da peza SON (Gauntlet 3): un episodio "comprimido" de ~2 min con voz, planos e son por plano.

Texto e lista de planos escritos por Claude (axente de son) só para medir o son: NON son guion nin lista de planos do
episodio. O texto é xenérico e o lendario vai como lenda ("contan"). Tres tramos, cada un nunha posición virtual do
episodio (palabra `pal0` dun guion de TOT palabras) para que voz, pausas, nivel do ambiente e escaseza dos eventos
sigan a curva do embude (curva.py) coma nun episodio de verdade:

  gancho  palabras 40-140    (curva: voz viva, ambiente -8 dB, eventos normais)
  medio   palabras 1000-1090 (transición/calma: ambiente -3 dB)
  durmir  palabras 3300-3380 (ton de durmir: ambiente +1 dB, eventos escasos e suaves)

Cada plano ten imaxe (prompt en inglés, coma os do pipeline), o son que lle poría quen escribe a lista de planos
segundo a guía (gauntlet3/son/guia-son.md) e as frases que se escoitan nel.
"""
TOT = 3600                       # palabras do episodio virtual (~30 min)
SECCIONS = {'gancho': 40, 'medio': 1000, 'durmir': 3300}   # pal0 da primeira frase de cada tramo
PAUSA_SECCION = 2.5              # s de silencio entre tramos (coma unha pausa de capítulo)

# (tramo, frase)
FRASES = [
    ('gancho', 'Nas noites de choiva, cando a auga batía na lousa, nas casas de pedra falábase das meigas.'),
    ('gancho', 'Arredor da lareira, as avoas contaban que había mulleres que sabían curar, e tamén facer mal.'),
    ('gancho', 'Pero as meigas de verdade non están só nos contos: están tamén nos papeis dos xuízos.'),
    ('gancho', 'Na feira, entre o gando e os cestos, os rumores corrían dunha boca a outra.'),
    ('gancho', 'Contan que na noite de San Xoán as mozas ían á fonte antes de que saíse o sol.'),
    ('gancho', 'Levaban herbas, auga e palabras moi antigas.'),
    ('gancho', 'E en Compostela, as campás da catedral marcaban as horas da cidade.'),
    ('medio', 'Nas aldeas, a vida seguía o seu curso: as vacas no prado, o leite na cociña e a horta ao pé da casa.'),
    ('medio', 'Os nenos corrían pola eira, e as galiñas buscaban o gran.'),
    ('medio', 'Moitas das mulleres que chamaban meigas eran, en realidade, curandeiras, e a xente ía a elas cando alguén enfermaba.'),
    ('medio', 'Na costa de Cangas, o mar batía nas pedras, coma o fixera sempre.'),
    ('medio', 'Os mariñeiros saían ao mar, e as mulleres agardaban na beira.'),
    ('medio', 'E polo monte, entre carballos e castiñeiros, o vento levaba as historias dunha parroquia a outra.'),
    ('durmir', 'Na noite de San Xoán, as fogueiras ardían lonxe, nos campos, e o ceo enchíase de estrelas.'),
    ('durmir', 'Cheiraba a fume e a herbas do monte.'),
    ('durmir', 'No mosteiro, os monxes gardaban silencio, e soaba unha campá moi lonxe.'),
    ('durmir', 'As pedras do claustro gardaban a calor do día.'),
    ('durmir', 'Pouco a pouco, a choiva volve caer amodo sobre a lousa.'),
    ('durmir', 'Chove na lousa, amodo, coma unha canción vella.'),
    ('durmir', 'Deixa que o corpo descanse, que a historia pode esperar ata mañá.'),
]

# Planos: frases (índices en FRASES), prompt da imaxe e son (None = voz limpa). O son é o que marca a guía.
PLANOS = [
    {'frases': [0], 'son': 'choiva',
     'prompt': 'A granite village lane at night in the rain, slate roofs shining wet, a warm light in one small window'},
    {'frases': [1], 'son': 'lume',
     'prompt': "An old woman's hands warming by a hearth fire in a dark stone kitchen, embers and firelight"},
    {'frases': [2], 'son': None,
     'prompt': 'A seventeenth-century handwritten court record on a wooden table, candlelight, close-up'},
    {'frases': [3], 'son': 'xente',
     'prompt': 'A crowded village fair in a granite square, people talking among cattle and wicker baskets'},
    {'frases': [4], 'son': 'fonte',
     'prompt': 'A granite village fountain at dawn, water running from a stone spout into a trough'},
    {'frases': [5], 'son': None,
     'prompt': 'Bundles of dried herbs hanging from a wooden beam in a farmhouse, soft window light'},
    {'frases': [6], 'son': 'campas',
     'prompt': 'The towers of Santiago de Compostela cathedral at dusk, bells in the belfry'},
    {'frases': [7, 8], 'son': 'aldea',
     'prompt': 'A green meadow with brown cows beside a granite village, morning light, birds in the oaks'},
    {'frases': [9], 'son': None,
     'prompt': 'Portrait of a village healer woman sorting herbs at a wooden table, soft window light'},
    {'frases': [10, 11], 'son': 'mar',
     'prompt': 'The rocky coast of Cangas at dusk, gentle waves breaking on granite rocks, small fishing boats'},
    {'frases': [12], 'son': 'vento',
     'prompt': 'Oak and chestnut woods moving in the wind on a Galician hillside, grey clouds'},
    {'frases': [13, 14], 'son': 'lume+noite',
     'prompt': 'Midsummer night, a small bonfire far away in a village field under a starry sky'},
    {'frases': [15, 16], 'son': 'campas',
     'prompt': 'A monastery cloister at night, moonlight on granite arches, a bell tower in the distance'},
    {'frases': [17, 18], 'son': 'choiva',
     'prompt': 'Rain falling softly on a slate roof at night, a candle behind a small window'},
    {'frases': [19], 'son': None,
     'prompt': 'An empty wooden bench by a window with moonlight, a sleeping village outside'},
]


def frases_con_pal0():
    """Lista de dicts {i, tramo, texto, pal0}: pal0 virtual (posición no episodio de TOT palabras)."""
    out, cont = [], {}
    for i, (tr, tx) in enumerate(FRASES):
        p = cont.get(tr, SECCIONS[tr])
        out.append({'i': i, 'tramo': tr, 'texto': tx, 'pal0': p})
        cont[tr] = p + len(tx.split())
    return out
