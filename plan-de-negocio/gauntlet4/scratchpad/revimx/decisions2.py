"""Segunda pasada da revisión de imaxes r1 (planos 43-77), dun axente Claude. Engade as decisións ao JSON da
primeira pasada (sen tocar as dos planos 1-42) e escribe etiquetas2.json para rotular as follas."""
import json
from pathlib import Path

SCR = Path('/tmp/claude-0/-home-user-revolta/c92eba35-e89d-5d11-bb3d-f517a84dab48/scratchpad')
REV = json.loads((SCR / 'revimx' / 'revision-copia2.json').read_text())
IMX = SCR / 'v2' / 'w' / 'imaxes'
SAIDA = Path('/home/user/revolta/plan-de-negocio/gauntlet4/video/revision-imaxes-r1.json')
por_n = {int(k[:3]) + 1: (k, v) for k, v in REV.items()}
BASE = 'electric light, light bulb, lamp, glass window, modern clothes, street lamp'
BASE_XX = 'neon, plastic, television, smartphone'

D = {
    43: ('vale', None, 'María Cibreira co pano gris, sentada, e as outras veciñas agardando detrás: é o que se oe. As luces da parede son candeas; sen anacronismos.'),
    44: ('rexenerar', None, 'Paredes encaladas e talladas grandes de aspecto mediterráneo, e a visitante leva unha cunca que parece un vaso de papel con tapa. Non hai pote de unguento nin neno, e a curandeira non leva o pano negro. Os outros dous intentos tamén son mediterráneos.'),
    45: ('rexenerar', None, 'Os tres intentos: unha dama vitoriana con vestido negro e pendentes diante dun xuíz do XIX entre candelabros. Non é María Cibreira (no 43, campesiña de pano gris) e falta o escribán.'),
    46: ('rexenerar', None, 'Retrato de tres caras con marco branco esvaído (viñeta) e roupa do XIX; sen papel nin pregunta, e a muller non é a Cibreira do 43. A porta aprobouno.'),
    47: ('rexenerar', None, 'Os tres intentos: fonte ornamental nun parque urbano, con farolas eléctricas e un edificio coas fiestras acesas (a porta acerta).'),
    48: ('rexenerar', None, 'Tres homes do XIX discutindo diante de casas de tellado de herba de aspecto irlandés, cun animal que parece unha ovella; falta a muller acusada. A porta aprobouno.'),
    49: ('rexenerar', None, 'Dous vellos de pé diante dun muro cun lume nun oco: ninguén espreita, e non hai fonte nin mulleres (a porta só avisou de que faltaba a fonte).'),
    50: ('vale', None, 'Dous veciños agachados ao pé dun muro de noite, cun papel e candeas no chan: apuntan a lista. Mans correctas; chalecos de la, coherentes cos outros veciños.'),
    51: ('rexenerar', None, 'Fonte de xardín con pía de pé e un cano metálico coma unha billa: non é unha fonte de aldea. Os ollos na escuridade non saíron e quítoos do prompt (risco de monstro); a escuridade das follas abonda.'),
    52: ('rexenerar', None, 'Tres figuras con túnicas e capuchas vermellas arredor dun lume dentro dunha pía, cunha arcada e unha luz eléctrica ao fondo: parece un rito sectario, non tres veciñas rindo. A porta aprobouno.'),
    53: ('vale', None, 'Dúas mozas camiñan cara á cámara cos caldeiros da auga ao serán: é o que se oe. Os caldeiros metálicos no canto de cántaros de barro son verosímiles; a casa do fondo é pequena e está desenfocada.'),
    54: ('rexenerar', None, 'Os tres intentos son dúas mulleres nunha mesa dentro da casa, sen fonte nin noite, e a vella sorrí en vez de mirar con receo: perdeuse a idea das dúas maneiras de mirar a mesma fonte.'),
    55: ('vale', None, 'Nai e filla axeonlladas á lareira de granito (semente da lareira), co lume pequeno e as olas: ilustra o oficio que pasa de nai a filla. Non se ve o morteiro; aceptable.'),
    56: ('vale', None, 'Un vello coas ovellas xunto a un muro de pedra no outono: a porta rexeita por animais en grupo, pero as ovellas son o asunto. Non se ve a viña nin a liorta entre dous; aceptable.'),
    57: ('vale', None, 'A curandeira do chal azul (a mesma do 18) e un labrego axeonllados xunto a un becerro deitado: a saúde e o gando, xusto o que se oe. Defecto menor: ao fondo, casas con tellado de herba.'),
    58: ('rexenerar', None, 'Monxe vello e fraco lendo un libro nun xardín: non aparecen a herba nin a curandeira que defendía Sarmiento. Ademais, Sarmiento é robusto e de cara redonda, e este confúndese co Feijoo do 59.'),
    59: ('vale', None, 'Dous monxes beneditinos escribindo á luz dunha vela (Feijoo co capucho): encaixa. A fiestra de vidro é verosímil nun mosteiro do XVIII e o libro non ten texto lexible; a porta rexeitouno por texto, de máis.'),
    60: ('vale', None, 'Un mozo murmura á orella dunha muller pensativa contra un muro con musgo: le como o rumor que corre. Os papeis están invertidos con respecto ao prompt; aceptable.'),
    61: ('rexenerar', None, 'Muller tendida de costas, ríxida e cos brazos estirados sobre unha esteira: semella un corpo amortallado, e non hai a sombra do paxaro do soño.'),
    62: ('vale', None, 'Feixes e rolos de papeis con cordón vermello e dúas velas: pecha os papeis. A folla aberta ten letra miúda ilexible; a porta rexeitouno por repetición co 26, un eco aceptable.'),
    63: ('rexenerar', None, 'Fonte ornamental redonda con remate de estatua e luz de día gris: nin noite, nin lúa, nin fonte de aldea. Rexenérase coa mesma fonte rústica do 47 e do 51.'),
    64: ('rexenerar', None, 'Non hai talla nin auga: unha planta nun recanto de muros que parecen de formigón. A porta aprobouno sen a clave.'),
    65: ('rexenerar', None, 'Os tres intentos: unha fila de siluetas diante dun incendio enorme que ocupa o horizonte. Non son as brasas da cacharela (a porta acerta: lume vivo ao durmir).'),
    66: ('vale', None, 'A moza da trenza e a blusa branca (a mesma do 16) nunha pía de pedra coa primeira luz e unha cunca verde: ilustra a flor da auga. Defecto menor: unha fonte ornamental á esquerda.'),
    67: ('rexenerar', None, 'Os tres intentos levan fiestras de vidro modernas, contraventás con macetas ou portas de cristal (a porta acerta, aínda que diga casas británicas).'),
    68: ('rexenerar', None, 'A cunca coas cuncas no bordo e os grans de café está ben (semente 07-01), pero os tres intentos teñen luz de día forte e o texto di «apáganse as luces». A porta rexeitou por lume vivo (é o barro laranxa). Proposta: a mesma semente en profundidade 0,6, que mantén a forma e deixa escurecer. Se volve fallar, o [0] (a xerra vertendo) vale.'),
    69: ('rexenerar', None, 'Lume laranxa grande nunha cunca no chan e un só vello: o crítico pedira lapas azul pálido para o durmir, e faltan os comensais.'),
    70: ('rexenerar', None, 'Dous veleiros grandes de tres mastros e unha cidade ao fondo: perdeuse o eco buscado co plano 4 (o barco vello e pequeno no peirao). Proposta: a mesma semente do 4. Se a porta rexeita por repetición co 4, escollelo a man, como dixo o crítico de planos.'),
    71: ('outro', 0, 'O [1] ten dúas vellas sorrindo, sen o xesto. O [0]: a vella do pano escuro e o chaleco negro ergue o dedo ao dicir o dito, e a outra ri. Os cadros da parede son verosímiles no XX; a porta viu obxectos modernos e unha catedral que non hai.'),
    72: ('rexenerar', None, 'Os tres intentos teñen lapas laranxas grandes; o escollido, ademais, unha pota negra de ferro (veto do caldeiro) e unha lareira acesa. O texto pide as últimas lapas azuis, que se apagan.'),
    73: ('outro', 2, 'O [1] ten dúas vellas lendo. O [2] ten a avoa e unha nena co libro: é o conto que pasa do libro á aldea. A lareira do fondo dá lume vivo (4,6 %), pero é ambiente; aceptable.'),
    74: ('rexenerar', None, 'Vacas frisoas brancas e negras (raza leiteira moderna) e faroles de parede; os outros intentos teñen lámpadas eléctricas. Rexenérase con dúas vacas pardas.'),
    75: ('vale', None, 'Regato con musgo entre a brétema do bosque: é o que se oe, calmo para durmir.'),
    76: ('outro', 0, 'O [3], que pasou a porta, é a reserva xenérica: un bosque con brétema, que repite o 75 e non ten candea. O [0]: velas no peitoril de pedra dun muro groso. A porta rexeitouno por repetición co 9, pero é o eco buscado (a candea do principio e a do final).'),
    77: ('rexenerar', None, 'Tellado de lousa con musgo, pero cunha bufarda de fiestras de vidro acesas e cheminea de aspecto inglés; é a última imaxe do vídeo. Encadre pechado nas lousas, sen casa.'),
}

R = {
    44: {'prompt': 'medium shot of an old healer with white hair under a black wool headscarf at the door of her rough '
                   'granite house, handing a small clay pot of ointment to a peasant woman holding a child, villagers '
                   'waiting behind, soft morning light, 17th century',
         'negativo': BASE + ', witch hat, broom, modern door, plastered walls, amphora, olive trees, paper cup'},
    45: {'prompt': 'over-the-shoulder shot from behind a peasant woman in a grey wool headscarf on a stool: a stern '
                   'grey-bearded judge in a black gown questions her while a gaunt clean-shaven scribe beside him writes '
                   'with a quill, bare stone room, candlelight',
         'negativo': BASE + ', devil, horns, demon, fire, chandelier, ball gown, earrings'},
    46: {'prompt': 'close-up two-shot in profile: a stern grey-bearded judge in a black gown reads a question from a '
                   'paper to a pale exhausted peasant woman in a grey wool headscarf, who nods in silence with her lips '
                   'closed, candlelight',
         'negativo': BASE + ', glasses, printed book, vignette, white frame, bonnet'},
    47: {'prompt': 'wide shot of a simple rustic spring at night: water pouring from a stone spout set in a mossy '
                   'granite wall into a stone trough, among chestnut trees, the faint orange glow of a distant bonfire '
                   'between the trunks, moonlight',
         'negativo': BASE + ', houses, statue, ornamental fountain, park, buildings'},
    48: {'prompt': 'medium shot of two village men in sheepskin vests pointing and shouting at a village woman in a '
                   'dark wool shawl at the door of a stone byre, a sick calf and two piglets lying still on the straw '
                   'inside, overcast daylight, 17th century',
         'negativo': BASE + ', blood, tractor, turf roof, thatched cottage, sheep'},
    49: {'prompt': 'over-the-shoulder shot of two village men in sheepskin vests crouching behind a mossy granite wall '
                   'at night, peering over it at distant women gathered around a small bonfire by a rustic stone '
                   'spring, deep shadows',
         'negativo': BASE + ', ornamental fountain, houses'},
    51: {'prompt': 'close-up of cold water pouring from a rough stone spout in a mossy granite wall into a stone trough '
                   'on a short June night, moonlight on the water, dark leaves and ferns all around',
         'negativo': BASE + ', monster, animal eyes, plastic pipe, metal tap, ornamental fountain'},
    52: {'prompt': 'wide shot of three village women in dark wool shawls and headscarves talking and laughing softly '
                   'around a rustic stone spring at night, lit by a small bonfire, seen from far away through dark '
                   'branches',
         'negativo': BASE + ', hooded robes, cloaks, ritual, arcade, columns'},
    54: {'prompt': 'close-up two-shot at a rustic stone spring at night: a young woman with a long dark braid smiles as '
                   'she fills a clay jug at the spout, beside her an old woman in a black wool headscarf crosses '
                   'herself, looking warily into the dark',
         'negativo': BASE + ', witch hat, broom, table, teapot'},
    58: {'prompt': 'medium shot of a stout round-faced Benedictine friar of about fifty in a black habit holding a '
                   'sprig of a medicinal herb that an old village woman in a dark blue wool shawl offers him from her '
                   'basket, monastery herb garden, 18th century',
         'negativo': BASE + ', glasses, cathedral, skullcap'},
    61: {'prompt': 'medium shot of a village woman asleep curled on her side under a wool blanket on a straw mattress '
                   'in a dark granite room, her face calm, moonlight from a small opening, on the wall above her the '
                   'soft shadow of a bird in flight',
         'negativo': BASE + ', broom, witch, demon, corpse, coffin'},
    63: {'prompt': 'high-angle close-up of the full moon reflected in the still dark water of a stone trough under a '
                   'rustic spring spout, ferns and moss around its edge, a thin stream falling, soft mist, night, no '
                   'one around',
         'negativo': BASE + ', houses, plastic pipe, statue, ornamental fountain, daylight'},
    64: {'prompt': 'a wide brown earthenware basin full of water with floating sprigs of fennel, ferns and wild '
                   'flowers, resting on top of a mossy granite wall outside at night, dew drops on the leaves, '
                   'moonlight, calm',
         'negativo': BASE + ', plastic, glass vase, concrete'},
    65: {'prompt': 'wide shot of a dark misty meadow at night, far away a low ring of dull red embers almost burnt out '
                   'on the ground, small dark silhouettes of villagers around it, one leaping over the embers, deep '
                   'blue darkness, calm',
         'negativo': BASE + ', fireworks, city lights, wildfire, big flames'},
    67: {'prompt': 'close-up of bunches of dried herbs and wild flowers hanging from a dark smoke-blackened wooden beam '
                   'against a rough granite wall, dust floating in a thin beam of light, dim and quiet',
         'negativo': BASE + ', plastic, vase, flowerpots, shutters'},
    68: {'prompt': "close-up of an old woman's hand pouring clear spirits from an earthenware jug into a wide clay bowl "
                   'holding sugar, lemon peel and coffee beans, small clay cups hanging on its rim, dim room at night, '
                   'faint warm light',
         'negativo': BASE_XX + ', glass bottle, modern kitchen, light bulb, daylight',
         'referencia': {'ficheiro': '07-queimada/02-camino-de-santiago-may-2008.jpg', 'modo': 'profundidade',
                        'forza': 0.6}},
    69: {'prompt': 'medium shot of an old man with white stubble in a dark wool waistcoat lifting a clay ladle of pale '
                   'blue flames over a wide clay bowl of blue flames, an old woman in a dark headscarf beside him, '
                   'faces lit blue in a dark kitchen',
         'negativo': BASE_XX + ', light bulb, modern kitchen, glass, fireplace, candles, cauldron, orange fire'},
    70: {'prompt': 'wide calm view of a misty harbour at night, a small old wooden sailing boat moored at a granite '
                   'quay, a faint blue glow and three small seated figures on its deck, still dark water, 1960s',
         'negativo': BASE_XX + ', street lamps, modern yacht, city lights, tall ship',
         'referencia': {'ficheiro': '11-barcos-costa/16-dorna-a-vela-rianxo-de-noite.jpg', 'modo': 'img2img',
                        'forza': 0.5}},
    72: {'prompt': 'close-up of a wide brown earthenware bowl on a wooden table with a few faint low blue flames dying '
                   'on its surface, the dark kitchen lit only by a dim red glow of embers, an old bundle of papers tied '
                   'with a faded red cord beside it',
         'negativo': BASE_XX + ', light bulb, glass, cauldron, iron pot, fireplace, orange flames'},
    74: {'prompt': 'medium shot of two brown cows asleep on straw in a dark stone byre at night, bunches of dried herbs '
                   'hanging from the wooden beam above them, fine rain falling outside the open half-door, the faint '
                   'glow of a small horn lantern, calm',
         'negativo': BASE + ', metal stalls, black and white cows, wall lamp'},
    77: {'prompt': 'close-up of fine rain falling on dark wet stone slates of an old roof at night, drops gathering '
                   'and dripping from the edge, moss between the slates, deep blue darkness, calm',
         'negativo': BASE + ', tiles, gutter, window, dormer, chimney'},
}


def main():
    J = json.loads(SAIDA.read_text())
    etiquetas = {}
    for n, (dec, idx, motivo) in sorted(D.items()):
        k, r = por_n[n]
        assert not r.get('revision_manual'), n
        J['motivos'][str(n)] = motivo
        if dec == 'rexenerar':
            J['rexenerar'][str(n)] = dict(R[n], motivo=motivo)
            etiquetas[n] = 'REXENERAR'
            continue
        if dec == 'vale':
            f = r['ficheiro']
            etiquetas[n] = 'VALE' + ('' if r['ok'] else ' (contra a porta)')
        else:
            x = [x for x in r['intentos'] if x['intento'] == idx][0]
            f = x['ficheiro']
            assert f != r['ficheiro'], n
            etiquetas[n] = f'OUTRO INTENTO [{idx}]' + ('' if not x['problemas'] else ' (contra a porta)')
        assert (IMX / f).exists(), f
        J['escollas'][str(n)] = f
    assert set(R) == {n for n, d in D.items() if d[0] == 'rexenerar'}
    assert set(D) == set(range(43, 78))
    for k in ('escollas', 'motivos', 'rexenerar'):
        J[k] = dict(sorted(J[k].items(), key=lambda kv: int(kv[0])))
    J['descricion'] = J['descricion'].replace('planos 1-42 (Gauntlet 4)', 'planos 1-77 en dúas pasadas (Gauntlet 4)'
                                              ).replace(' Planos 43-77: segunda pasada.', '')
    SAIDA.write_text(json.dumps(J, ensure_ascii=False, indent=1) + '\n')
    (SCR / 'revimx' / 'etiquetas2.json').write_text(json.dumps(etiquetas, ensure_ascii=False))
    c = {}
    for v in D.values():
        c[v[0]] = c.get(v[0], 0) + 1
    print(c, 'total escollas', len(J['escollas']), 'rexenerar', len(J['rexenerar']), 'motivos', len(J['motivos']))


if __name__ == '__main__':
    main()
