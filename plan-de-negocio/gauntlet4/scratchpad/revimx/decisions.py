"""Decisións da revisión de imaxes r1 (planos 1-42), escritas por un axente Claude mirando as follas.
Xera plan-de-negocio/gauntlet4/video/revision-imaxes-r1.json e etiquetas.json (para rotular as follas)."""
import json
from pathlib import Path

SCR = Path('/tmp/claude-0/-home-user-revolta/c92eba35-e89d-5d11-bb3d-f517a84dab48/scratchpad')
REV = json.loads((SCR / 'revimx' / 'revision-copia.json').read_text())
IMX = SCR / 'v2' / 'w' / 'imaxes'
SAIDA = Path('/home/user/revolta/plan-de-negocio/gauntlet4/video/revision-imaxes-r1.json')
por_n = {int(k[:3]) + 1: (k, v) for k, v in REV.items()}

# n: (decisión, intento escollido ou None, motivo)
D = {
    1: ('vale', None, 'Dous mouchos sobre pedra con musgo, de noite no bosque: ilustra o que se oe. O sapo non saíu; non fai falta.'),
    2: ('rexenerar', None, 'Lume laranxa nunha pota ou tixola negra de ferro: lese como caldeiro (veto §8.5) e falta a clave (lapas azuis, cunca de barro). Só houbo un intento e a porta aprobouno.'),
    3: ('outro', 1, 'No [2] escollido sostén na outra man unha pluma ou un misto acendido (artefacto). O [1] é limpo: escribe nun caderno, con candeas e o porto de noite; o texto non se le (a porta rexeitouno por texto, de máis).'),
    4: ('vale', None, 'Barco vello amarrado a un peirao de granito de noite (semente da dorna): correcto. Non se ven os tres homes; non fai falta.'),
    5: ('vale', None, 'Home con barba e chapeu que escribe con pluma á luz das candeas, con xente detrás: lese como unha declaración ante o tribunal. Para MOVEMENTO: o home escribe e leva o chapeu posto, así que hai que cambiar a acción I2V.'),
    6: ('rexenerar', None, 'Non hai muller preñada nin home: unha vella sentada nunha cama e outra axeonllada diante, que se le como unha enferma. Os tres intentos fallan igual, e no [1] e [2] o prompt truncouse e perdeu o home.'),
    7: ('rexenerar', None, 'Os tres intentos levan zapatos modernos de cordóns (a porta acerta ao rexeitalos, aínda que dea outro motivo). Prompt máis curto, cunha chinela de coiro brando como a do plano 8.'),
    8: ('vale', None, 'Home dobrado sobre o banco, coma se lle petase a dor, con zapatos brandos: conta a historia. Defecto menor: ao fondo, noutro cuarto, unha fiestra de vidro pequena e desenfocada. O I2V do salto é fráxil; se deforma, paralaxe.'),
    9: ('rexenerar', None, 'Vela de bloque moderna nun prato negro, cunha bóla escura sen sentido ao lado e sen parede de granito: parece foto de produto actual, e é o plano do aviso.'),
    10: ('rexenerar', None, 'O hórreo sae con tellado de herba e, á dereita, unha caseta cun farol de parede aceso que parece eléctrico. Mesma semente (Muimenta) en img2img 0,5, que segundo o informe de imaxe §4 conserva o hórreo e os tornarratos.'),
    11: ('vale', None, 'Tres mozos arredor dunha cunca de barro con lume: unha queimada no século XX, encaixa. Defectos menores: lapa laranxa, contas azuis dentro da cunca e caras ben iluminadas (o prompt quería anonimato).'),
    12: ('vale', None, 'Escribán con pluma e candeas, papel sen texto lexible. A porta rexeitouno por texto na imaxe, que nun plano de escritura sobra. Lazo de encaixe ao pescozo algo tardío, aceptable.'),
    13: ('vale', None, 'Primeiro plano da parteira: boa calidade e sen artefactos. O pano é claro, non marrón escuro, e mira á cámara.'),
    14: ('vale', None, 'Pilas de papeis vellos: ilustra o que se oe. Ao fondo hai unha fiestra de vidro desenfocada, crible nun arquivo ou tribunal.'),
    15: ('vale', None, 'Letra cursiva antiga ilexible, con riscos: vale para un plano de escritura (a porta rexeita por texto). O [1] ten pseudopalabras góticas case lexibles e o [2] parece libro impreso.'),
    16: ('vale', None, 'A moza da trenza nunha pía de pedra de noite, con lume ao lado e xente que mira desde o fondo: encaixa coa lista e coa noite de san Xoán. Non hai cántaro; as mans están ben.'),
    17: ('rexenerar', None, 'Fiestras de vidro grandes, unha vasoira (veto §8.5), cofias brancas e mandís de tirantes de aspecto holandés, e marcas vermellas na parede. A porta aprobouno.'),
    18: ('rexenerar', None, 'Os tres intentos teñen luz eléctrica ou fiestra de vidro: o [0], unha bombilla acesa no teito; o [1] e o [2], fiestras de cristais. Ademais, o [0] non ten a enferma. Plano clave (a meiga que cura).'),
    19: ('vale', None, 'Muller que busca entre papeis cunha vela nun arquivo escuro: ilustra o «imos buscalas». Moitas candeas e libros encadernados, sen anacronismos; o texto non se le (a porta rexeitouno por texto).'),
    20: ('rexenerar', None, 'Salón palaciano con lampadario de cristal, ventás altas de vidro en arco e moita xente; María vai cun capuchón vermello de Carapuchiña. A porta aprobouno.'),
    21: ('rexenerar', None, 'Os tres intentos teñen casas inglesas con cheminea e unha muller con capa vermella de Carapuchiña (a porta acerta). Proposta con semente: a palloza (CC BY 3.0), recortada sen a cheminea metálica, en profundidade 0,6.'),
    22: ('rexenerar', None, 'Edificio de pedra con soportais, fiestras de vidro e baixante de canlón: non se le como igrexa de aldea. Dúas persoas separadas, sen murmurio. A porta aprobouno.'),
    23: ('vale', None, 'María (pano e bufanda vermellos) entre as vacas no monte, co vento: é xusto o que se oe. A porta rexeita por animais en grupo, pero o texto pide o gando arredor.'),
    24: ('vale', None, 'Dúas vacas de cornos longos nun regato do monte: ilustra o desexo das sete fontes. Sen a muller, que era opcional.'),
    25: ('outro', 1, 'O [2] escollido ten un segundo home de chaleco e gravata do século XIX e ninguén escribe. O [1] é a testemuña de perfil, con barba e roupa de la parda, á luz das candeas; a man sen corpo que viu a porta non se ve.'),
    26: ('outro', 1, 'O [0] ten dous instrumentos de escribir, un en cada man. O [1]: unha soa man con pluma e puño branco sobre a páxina, e o texto non se le.'),
    27: ('vale', None, 'Arquiveiro con luvas brancas entre feixes de papeis: encaixa. Viste chaleco e lazo de aspecto antigo; aceptable.'),
    28: ('vale', None, 'Escribán novo con pluma e candeas e, detrás, un home (non a muller): lese como «na voz doutros, e na man de quen escribía». Para MOVEMENTO: non hai muller detrás, así que hai que cambiar a acción I2V.'),
    29: ('rexenerar', None, 'Edificio monumental de columnas e ventás góticas (catedral, que estaba no negativo), tres mulleres e o cura de costas: non é a capela de aldea nin as dúas excomungadas soas. A porta aprobouno.'),
    30: ('outro', 0, 'O [1] escollido non ten a cunca (falta a clave) e ten unha fiestra de vidro. O [0] ten a cunca de barro entre as dúas mulleres no limiar, e as mans están ben (a porta viu mans de máis).'),
    31: ('rexenerar', None, 'Os tres intentos teñen unha lupa deformada (dous aros) e letra de imprenta ou pseudopalabras lexibles dentro da lente.'),
    32: ('outro', 2, 'O [0] ten lume laranxa sobre contas azuis. O [2] ten lapas azuis na cunca de barro e unha folla de versos ilexible (en 1967, mecanografada, é verosímil).'),
    33: ('vale', None, 'Tres amigos rindo no barco de noite, co porto ao fondo: é o que se oe. A porta viu un iate moderno que non hai. Defecto menor: o lume é laranxa.'),
    34: ('vale', None, 'Dous homes len unha folla de noite no porto, coas mans correctas. Falta o brillo azul; aceptable.'),
    35: ('outro', 1, 'O [3], que a porta aprobou, é a reserva xenérica: un labrego con boina nun prado, nada que ver co que se oe. O [1]: follas de versos espalladas, farol e vela, e texto ilexible.'),
    36: ('vale', None, 'Tenda con mostrador, papeis e cartóns: ilustra «unha empresa vendeu copias». Roupa de mediados do século XX; aceptable.'),
    37: ('outro', 2, 'O [0] ten dúas mans de persoas distintas con dúas plumas. O [2]: a man dun home maior asinando un formulario (2001), cunha soa pluma e texto ilexible.'),
    38: ('rexenerar', None, 'Gran fogueira laranxa cunha multitude cos brazos en alto: lembra unha queima (veto de autos de fe) e falta a cunca da queimada. A porta aprobouno.'),
    39: ('rexenerar', None, 'O barco arde: lume enorme na cuberta con cinco homes diante e sen pote (lapas sobre persoas). A porta aprobouno.'),
    40: ('rexenerar', None, 'Salón palaciano con lampadario de cristal, cadros e fiestra de vidro, todos de negro: non se ven as tres xustizas (falta o inquisidor de hábito branco). A porta aprobouno.'),
    41: ('rexenerar', None, 'Os tres intentos: ancián con lentes modernas e as bandas brancas dun xuíz inglés, vestido de negro e non co hábito branco do inquisidor.'),
    42: ('rexenerar', None, 'Dúas figuras de negro nun banco de parque ao aire libre: non hai xuíz, nin sala, nin as tres acusadas. A porta aprobouno.'),
}

BASE_XVII = 'electric light, light bulb, lamp, glass window, modern clothes, street lamp'
R = {
    2: {'prompt': "close-up of a man's face in the dark lit from below by pale blue flames, he lifts a wooden ladle of "
                  'burning liquid above a wide brown earthenware bowl of blue flames, blue fire dripping back into it, '
                  'black background',
        'negativo': 'cauldron, iron pot, frying pan, neon, plastic, television, smartphone, light bulb, lamp, glass, '
                    'modern kitchen'},
    6: {'prompt': 'medium shot of an old midwife in a dark brown wool headscarf kneeling beside a heavily pregnant '
                  'young woman lying on a straw mattress, stroking her brow, a burly bearded man watching from the dark '
                  'doorway, candlelight, rough granite walls, 17th century',
        'negativo': BASE_XVII + ', blood, nudity, hospital, metal bed, sofa'},
    7: {'prompt': 'close-up of an old midwife in a dark brown wool headscarf kneeling on a rough wooden floor, pushing '
                  "a small worn soft leather slipper onto a bearded man's large bare foot, candlelight, 17th century",
        'negativo': BASE_XVII + ', sneaker, high heel, shoelaces, boots'},
    9: {'prompt': 'close-up of a single thin beeswax taper candle just lit in a simple wrought-iron holder on a rough '
                  'dark oak table, a thin curl of smoke rising, rough granite wall behind in deep shadow, calm night',
        'negativo': BASE_XVII + ', glass jar, pillar candle, fruit'},
    10: {'prompt': 'wide shot of two old Galician granaries raised on granite pillars with mushroom-shaped staddle '
                   'stones, one of wood and one of granite, stone-tiled roofs, in a quiet village yard at dusk, soft '
                   'mist, calm',
         'negativo': BASE_XVII + ', modern house, brick chimney, cars, wall lantern, grass roof',
         'referencia': {'ficheiro': '01-horreo/16-horreos-de-muimenta-carballeda-de-avia-galiza.jpg',
                        'modo': 'img2img', 'forza': 0.5, 'recorte': [0.32, 0.2, 1.0, 1.0]}},
    17: {'prompt': 'medium shot of an old village woman sitting on a granite doorstep shelling beans into her lap, a '
                   'young woman in a dark wool headscarf standing in the dark open doorway beside her, long dark wool '
                   'skirts, soft evening light, 17th century',
         'negativo': BASE_XVII + ', modern door, flowerpots, broom, white cap'},
    18: {'prompt': 'medium shot of an old village healer in a dark blue wool shawl handing a steaming clay bowl of herb '
                   'infusion to a sick young woman lying under a wool blanket on a straw bed, dried herbs hanging from '
                   'dark beams, firelight, smoke-blackened granite walls',
         'negativo': BASE_XVII + ', witch hat, broom, warts, hooked nose, shelves of bottles'},
    20: {'prompt': 'medium shot of a woman of about thirty in a faded red wool headscarf standing before a plain wooden '
                   'table where a stern grey-bearded judge in a black gown points his quill at her, bare granite walls, '
                   'a narrow shaft of daylight',
         'negativo': BASE_XVII + ', framed pictures, chandelier, arched windows, red cloak'},
    21: {'prompt': 'wide shot of a woman in a faded red wool headscarf holding a horn lantern at the heavy wooden door '
                   'of a thatched granite house at dusk, letting in a man in a dark wool cloak, 17th century Galicia',
         'negativo': BASE_XVII + ', modern door, chimney, red cloak, hood',
         'referencia': {'ficheiro': '03-palloza-casa/10-palloza-cantexeira.jpg', 'modo': 'profundidade',
                        'forza': 0.6, 'recorte': [0.0, 0.3, 0.54, 0.7]}},
    22: {'prompt': 'medium shot of two village women in dark wool headscarves and an old man whispering together beside '
                   'the round-arched stone doorway of a small Romanesque granite church, one woman glancing sideways '
                   'with suspicion, overcast daylight, 17th century',
         'negativo': BASE_XVII + ', cars, cathedral, drainpipe, gutter'},
    29: {'prompt': 'wide shot of a stern priest in a black cassock reading a decree aloud at the door of a small rustic '
                   'granite chapel, below him two women stand alone, an old one in a dark brown wool headscarf and a '
                   'younger one in a faded red wool headscarf',
         'negativo': BASE_XVII + ', cathedral, cars, columns, crowd'},
    31: {'prompt': 'close-up of an old brass magnifying glass lying on a yellowed 17th-century manuscript of faded '
                   'brown ink, shallow depth of field, the handwriting soft and blurred, soft daylight in a quiet '
                   'archive',
         'negativo': 'hands, fingers, electric lamp, printed text, typewriter, plastic, computer'},
    38: {'prompt': 'wide shot of a village festival at night seen from behind the crowd, dark silhouettes raising small '
                   'clay cups toward a wide clay bowl of pale blue flames on a stone table, the blue glow on their '
                   'raised hands, 1980s',
         'negativo': 'neon, plastic, television, smartphone, plastic cups, stage lights, bonfire'},
    39: {'prompt': 'overhead shot of a wide clay bowl of pale blue flames on the wooden deck of an old boat at night, '
                   'the shoes and trouser legs of three men standing around it, coils of rope nearby, 1960s',
         'negativo': 'neon, plastic, television, smartphone, light bulb, bonfire, burning boat'},
    40: {'prompt': 'wide shot of three judges seated side by side at a long wooden table in a bare granite hall: a '
                   'grey-bearded judge in a black gown, a priest in a black cassock, an elderly friar in a white habit '
                   'and black cape, light from a high opening',
         'negativo': BASE_XVII + ', framed pictures, flags, chandelier, crowd'},
    41: {'prompt': 'medium shot of a lean elderly friar with a grey tonsure, in a white habit and black cape, closing a '
                   'thick bundle of trial papers tied with cord and laying it on a tall pile of bundles, single candle, '
                   'bare stone room, 17th century',
         'negativo': BASE_XVII + ', hood, pointed hat, fire, crowd, glasses, bookshelves'},
    42: {'prompt': 'over-the-shoulder shot from behind a stern grey-bearded judge in a black gown at a high wooden '
                   'table, looking down at three village women in dark wool headscarves seated on a rough bench below '
                   'him, cold light from a high opening, bare granite hall',
         'negativo': BASE_XVII + ', framed pictures, chains, park bench, trees'},
}


def main():
    esc, mot, rex, etiquetas = {}, {}, {}, {}
    for n, (dec, idx, motivo) in sorted(D.items()):
        k, r = por_n[n]
        mot[str(n)] = motivo
        if dec == 'rexenerar':
            assert n in R, n
            rex[str(n)] = dict(R[n], motivo=motivo)
            etiquetas[n] = 'REXENERAR'
            continue
        if dec == 'vale':
            f = r['ficheiro']
            etiquetas[n] = 'VALE' + ('' if r['ok'] else ' (contra a porta)')
        else:
            f = [x['ficheiro'] for x in r['intentos'] if x['intento'] == idx][0]
            assert f != r['ficheiro'], n
            ok = not [x for x in r['intentos'] if x['intento'] == idx][0]['problemas']
            etiquetas[n] = f'OUTRO INTENTO [{idx}]' + ('' if ok else ' (contra a porta)')
        assert (IMX / f).exists(), f
        esc[str(n)] = f
    assert set(R) == {n for n, d in D.items() if d[0] == 'rexenerar'}
    out = {
        'descricion': ('Revisión das imaxes escollidas da v2, rolda 1, planos 1-42 (Gauntlet 4). Feita por un axente '
                       'Claude (revisor de imaxes) mirando follas de contactos e recortes ampliados; ningunha persoa a '
                       'revisou. Aplícaa o orquestrador con video/scripts/produccion.py revision. escollas: os planos '
                       'que non se rexeneran (os que valen co seu ficheiro e os de outro intento co novo); rexenerar: '
                       'prompt revisado sen o prefixo de estilo da pipeline (<= 57 tokens CLIP), negativo completo do '
                       'plano e, nos de arquitectura allea, referencia semente. Planos 43-77: segunda pasada.'),
        'escollas': esc, 'motivos': mot, 'rexenerar': rex}
    SAIDA.write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n')
    (SCR / 'revimx' / 'etiquetas.json').write_text(json.dumps(etiquetas, ensure_ascii=False))
    c = {}
    for v in D.values():
        c[v[0]] = c.get(v[0], 0) + 1
    print(c, len(esc), len(rex))


if __name__ == '__main__':
    main()
