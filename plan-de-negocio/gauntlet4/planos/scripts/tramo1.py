# Tramo 1 da lista de planos v2: gancho (planos 1-19, frases 1-20) e transición (20-38, frases 21-44).
# pl(frases, texto_en, tipo, prompt, clave, son, (modo, camara, efectos, accion), prioridade_i2v, persoas, ...)
# persoas: fan = persoas facendo algo; mans = só mans que fan algo; estan = presentes pero quietas; non = sen persoas.

# ---------------------------------------------------------------- GANCHO (3-6 s)
pl([1], 'Owls, barn owls, toads and witches.', 'primeiro_plano',
   'close-up of a little owl perched on a mossy granite wall at night, its round yellow eyes catching a faint blue '
   'glow from below, a small toad on the stone beside it, deep darkness behind',
   'owl', 'noite', ('i2v', 'avanza', [], 'the owl slowly turns its head and blinks'), 2, 'non',
   neg='witch, hat, cartoon, moon face')
pl([2], 'With the lights out, someone recites the spell while lifting the burning liquid with a ladle.', 'primeiro_plano',
   "close-up of a man's face in the dark, lit from below by blue flames, his lips moving as he lifts a clay ladle of "
   'burning spirits above a wide clay bowl, a thin stream of blue fire falling back into it, black background',
   'blue flames', 'lume', ('i2v', 'avanza', ['lume'], 'he slowly raises the ladle and pours a thin stream of blue fire '
                                                       'back into the bowl'), 1, 'fan',
   epoca='xx', neg='light bulb, lamp, glass, modern kitchen', arq='retrato')
pl([3, 4], 'It seems centuries old. But it has a known author and dates from nineteen sixty-seven:', 'plano_medio',
   'medium shot of {mariano} writing verses with a fountain pen in a small notebook, sitting on the deck of an old '
   'wooden boat at night, lit by an oil lantern beside him, 1967',
   'notebook', 'mar', ('i2v', 'avanza', ['candea'], 'the man writes slowly, pauses and looks up from the notebook'), 2,
   'fan', epoca='xx', neg='ballpoint pen, laptop, light bulb')
pl([4], 'Mariano Marcos Abalo wrote it on an old boat moored in the port of Vigo.', 'xeral',
   'wide shot of an old wooden sailing boat moored beside a granite quay in a harbour at night, a warm oil lantern '
   'glowing on its deck, the small silhouettes of three men sitting there, dark still water reflecting the light, 1960s',
   'boat', 'mar', ('paralaxe', 'pan_der', ['auga'], None), 3, 'estan', desde='escribiuno Mariano Marcos Abalo',
   ref={'ficheiro': '11-barcos-costa/16-dorna-a-vela-rianxo-de-noite.jpg', 'modo': 'img2img', 'forza': 0.5},
   epoca='xx', neg='street lamps, cars, modern yacht')
pl([5, 6], 'Vilalba, sixteen seventeen. A witness declares', 'plano_medio',
   'medium shot of {testemuna}, cap in his hands, testifying before a table where {escriban} writes with a goose '
   'quill, bare granite room, candlelight, 17th century',
   'bearded man', 'limpa', ('i2v', 'avanza', ['candea'], 'the man turns his cap in his hands as he speaks while the '
                                                         'scribe writes'), 1, 'fan',
   neg='glasses, framed pictures, bookshelves')
pl([6], "that the midwife Dorotea do Barro had said she could take away a woman's labour pains and pass them on to a "
        'man.', 'plano_medio',
   'medium shot of {dorotea}, laying her hand on the brow of a heavily pregnant young woman on a straw bed under a wool '
   'blanket, a worried bearded man beside the bed, warm side light',
   'pregnant woman', 'limpa', ('i2v', 'avanza', [], "the old midwife gently strokes the young woman's brow while the "
                                                    'man shifts his weight'), 2, 'fan',
   desde='que a parteira Dorotea do Barro', neg='blood, nudity, hospital, metal bed')
pl([7], "It would be enough to put the woman's shoes on the man, saying some words that she knew.", 'detalle',
   "close-up of an old midwife's weathered hands slipping a small worn woman's leather shoe onto a man's large bare "
   'foot, her lined face murmuring above under a dark brown wool headscarf, warm candlelight, rough wooden floor, '
   '17th century',
   'shoe', 'limpa', ('i2v', 'baixa', ['candea'], "her hands slowly push the small shoe onto the man's foot"), 2, 'mans',
   neg='sneaker, high heel, shoelaces', arq='mans')
pl([8], 'And the man would leap like a wild colt.', 'plano_medio',
   'full shot of a startled burly bearded peasant man in a coarse wool shirt leaping up from a low wooden bench, arms '
   "flung wide, small women's shoes on his feet, bare granite room lit from an open doorway, 17th century",
   'man', 'limpa', ('i2v', 'recua', [], 'the man jumps up from the bench with his arms flung wide'), 1, 'fan',
   neg='horse')
pl([9, 10], 'Good night. The voice you are about to hear is synthetic, and this text was prepared by an automatic '
            'process.', 'detalle',
   'close-up of a single beeswax candle just lit in a simple iron holder on a dark wooden table, a thin curl of smoke '
   'rising, rough granite wall behind in deep shadow, calm night',
   'candle', 'limpa', ('paralaxe', 'avanza', ['candea'], None), 3, 'non', neg='glass jar')
pl([11], 'This is Cousas de Galiza para durmir (Things of Galicia for falling asleep).', 'xeral',
   'wide shot of two old Galician granaries raised on stone pillars with mushroom-shaped staddle stones, one of granite '
   'and one of wood, in a misty village yard at night, moonlight on wet stone and moss, deep blue darkness, calm',
   'granary', 'noite', ('paralaxe', 'pan_der', ['bretema', 'ceo'], None), 3, 'non',
   ref={'ficheiro': '01-horreo/16-horreos-de-muimenta-carballeda-de-avia-galiza.jpg', 'modo': 'profundidade',
        'forza': 0.6, 'recorte': [0.32, 0.2, 1.0, 1.0]},
   neg='modern house, brick chimney, cars')
pl([12], 'The words of the spell seem old but are new, and there is a reason why they seem to belong to no one.',
   'plano_medio',
   'medium shot of blue flames rising from a wide clay bowl on a dark wooden table, three people around it with their '
   'faces lost in shadow, only their hands lit as they raise small clay cups toward the flames, darkness all around, '
   '20th century',
   'clay bowl', 'lume', ('i2v', 'recua', ['lume'], 'the people slowly raise their small cups toward the flames'), 2,
   'fan', epoca='xx', neg='light bulb, lamp, glass, modern kitchen')
pl([13], 'What was told about Dorotea is truly old, and we only know it because someone wrote it down in a witchcraft '
         'trial.', 'plano_medio',
   'medium shot of {escriban}, bent over a thick bundle of trial papers, writing with a goose quill by the light of a '
   'single candle, inkpot at hand, bare granite wall, 17th century',
   'papers', 'limpa', ('i2v', 'xira_esq', ['candea'], 'the scribe dips the quill in the inkpot and writes'), 2, 'fan',
   neg='glasses, printed book, bookshelves')
pl([14], 'The words she knew, those we do not know.', 'primeiro_plano',
   'close-up portrait of {dorotea}, eyes lowered, lips murmuring words we cannot hear, half her face in shadow, warm '
   'light from the side',
   'old woman', 'limpa', ('i2v', 'avanza', [], 'her lips move slightly as she murmurs, her eyes stay lowered'), 1, 'fan',
   neg='witch hat, warts, hooked nose, smile', arq='retrato')
pl([15], 'In the papers of those trials there are many more words.', 'bodegon',
   'still life of tall stacks of yellowed 17th-century trial papers tied with faded cords on a long dark wooden table, '
   'dust floating in a shaft of light from a small shuttered opening, deep shadows',
   'papers', 'limpa', ('paralaxe', 'xira_der', ['po'], None), 3, 'non', neg='printed books, modern office')
pl([16], 'There is a mistaken word that no one has erased in more than four hundred years.', 'detalle',
   'extreme close-up of faded brown handwriting on a yellowed 17th-century page, one word struck through with a single '
   'line of ink, soft raking light showing the texture of the old paper',
   'handwritten page', 'limpa', ('paralaxe', 'pan_der', [], None), 3, 'non', neg='printed text, typewriter')
pl([17], "And there is even news of a list of the women some neighbours saw at a fountain on Saint John's night.",
   'plano_medio',
   "medium shot of {moza} filling a clay jug at a granite fountain spout on Saint John's night, a distant bonfire "
   'glowing behind her, she looks up into the darkness as if someone were watching',
   'fountain', 'fonte+noite', ('i2v', 'avanza', ['auga'], 'she lifts her eyes from the jug and looks into the darkness '
                                                         'as the water keeps pouring'), 1, 'fan', neg='plastic')
pl([18], 'There were village women behind all those words.', 'plano_medio',
   'medium shot of two village women at the dark doorway of a granite farmhouse, an old one sitting and shelling beans '
   'into her apron and a young one leaning on the stone doorframe, long dark wool skirts and headscarves, faces lit '
   'from the side by soft evening light',
   'women', 'aldea', ('i2v', 'pan_esq', [], 'the old woman shells beans while the young woman turns her head toward '
                                           'her'), 2, 'fan', neg='modern door, flowerpots')
pl([19], 'The meiga, many times, was not the witch of tales, but the one who healed, who helped in childbirth, who '
         'knew about herbs.', 'plano_medio',
   'over-the-shoulder shot of {curandeira} handing a steaming clay bowl of herbal infusion to a sick young woman lying '
   'under a wool blanket, bunches of dried herbs hanging behind, warm light from the side, dignified and ordinary',
   'clay bowl', 'limpa', ('i2v', 'avanza', [], 'the healer slowly hands over the steaming bowl and the young woman '
                                              'takes it'), 1, 'fan', neg='witch hat, broom, warts, hooked nose')
pl([20], 'Tonight we will look for them in the little that was written about them, and ask ourselves whose those '
         'words really are.', 'plano_medio',
   'medium shot of a woman in a dark wool shawl raising a candle to tall wooden shelves stacked with old bundles of '
   'papers tied with cords, searching among them in a dark archive at night, seen from the side, candlelight on her '
   'face and on the paper edges',
   'papers', 'limpa', ('i2v', 'pan_der', ['candea'], 'she slowly moves the candle along the shelf, looking at the '
                                                    'bundles'), 2, 'fan', neg='modern books, computer')

# ---------------------------------------------------------------- TRANSICIÓN (5-9 s)
# I. Auga, digo, leite
pl([21], "In Vilalba, the Royal Court also tried María do Barro, Dorotea's daughter.", 'plano_medio',
   'medium shot of {maria}, standing before a court table in a bare granite hall while {xuiz} points his quill at her, '
   'light from a high opening',
   'judge', 'limpa', ('i2v', 'recua', [], 'the judge points his quill at her and she lowers her eyes'), 2, 'fan',
   neg='framed pictures')
pl([22], 'Of the daughter they said something else: that she was a go-between, and that she took married men and '
         'unmarried women into her house.', 'plano_medio',
   'medium shot of {maria}, holding a horn lantern at the heavy oak door of a granite house at dusk, letting in a man '
   'in a dark wool cloak, seen from behind a mossy wall across the path',
   'door', 'aldea', ('i2v', 'avanza', ['candea'], 'she opens the heavy door wider and the cloaked man steps inside'), 2,
   'fan', neg='modern door')
pl([23], 'A witness heard some neighbours murmuring that María was a meiga, and that she was not a good Christian.',
   'plano_medio',
   'medium shot of two village women and an old man whispering together under the stone porch of a small granite '
   'country church after mass, one woman glancing sideways with suspicion, dark wool clothes and headscarves, overcast '
   'daylight',
   'church', 'campas', ('i2v', 'pan_esq', [], 'they lean closer and whisper, and one woman glances sideways'), 1, 'fan',
   neg='cars, cathedral', arq='grupo de pé')
pl([24, 25], 'And he said that María, when she had the cattle up on the hill, said some words: some under her breath, '
             'and others that could be heard. Let us picture her there, with the cattle around her and the wind half '
             'carrying away what she said.', 'plano_medio',
   'medium shot of {maria}, standing among brown cows on a windswept hillside of heather and gorse, murmuring words to '
   'them, her scarf and the long grass blown by the wind, low grey clouds',
   'cows', 'vento', ('i2v', 'avanza', ['ceo'], "the wind blows her scarf and the grass as she speaks softly and touches "
                                               "a cow's neck"), 1, 'fan', neg='fence, wind turbines, power lines, road')
pl([26], 'And, among them, a wish for the cattle: that they drink water from seven springs and bring milk from seven '
         'byres and seven hills.', 'plano_medio',
   'medium shot of two brown cows lowering their heads to drink from a clear spring running over mossy stones on a '
   'green hillside, {maria}, watching them from behind, soft morning light',
   'cows', 'fonte', ('i2v', 'pan_der', ['auga'], 'the cows drink from the stream and the water ripples around their '
                                                'muzzles'), 2, 'estan', neg='fence, road, power lines')
pl([27, 28], "They were words for the cattle, not for a court. But from the hill they passed into the witness's mouth, "
             'and from the mouth onto paper.', 'primeiro_plano',
   'close-up of {testemuna} speaking in profile, and behind him, in soft focus, {escriban} writing his words with a '
   'goose quill, candlelight, bare granite wall',
   'scribe', 'limpa', ('i2v', 'xira_der', ['candea'], 'the man speaks while the scribe writes behind him'), 2, 'fan',
   neg='glasses, printed book', arq='retrato')
pl([29], 'On the paper even the correction of the one writing remained: that she bring water, I mean, milk.', 'detalle',
   "close-up of a scribe's hand with a goose quill striking through a word on a page of trial notes and writing the "
   'next one, black wool sleeve with a white cuff, fresh ink glistening, candlelight',
   'quill', 'limpa', ('i2v', 'avanza', ['candea'], 'the hand strikes through a word with the quill and writes on'), 2,
   'mans', neg='ballpoint pen, printed text', arq='mans')
pl([30, 31], 'The paper is kept by the Archive of the Kingdom of Galicia, with other witchcraft trials of the Royal '
             'Court. More than four hundred years later, the mistaken word is still there, just before the right one.',
   'plano_medio',
   'medium shot of an archivist in white cotton gloves carefully opening an old bundle of 17th-century trial papers on '
   'a grey table between tall shelves of bound bundles, one page with a struck-through word catching the soft '
   'daylight, quiet archive',
   'papers', 'limpa', ('i2v', 'recua', ['po'], 'the archivist gently unfolds the bundle and smooths the page'), 2, 'fan',
   epoca='xx', neg='computer, plastic folders')
pl([32], 'This is how the words of those women reach us: in the voice of others, and in the hand of the one who wrote.',
   'plano_medio',
   'medium shot of {escriban} writing with a goose quill at a table in the foreground, and behind him, in shadow, '
   '{maria}, standing silent with her lips closed, candlelight',
   'scribe', 'limpa', ('i2v', 'avanza', ['candea'], 'the scribe writes while the woman behind him stands still and '
                                                   'lowers her eyes'), 2, 'fan', neg='glasses, printed book')
pl([33, 34], 'And words could also close doors. The vicar general of the bishopric of Mondoñedo excommunicated the '
             'mother and the daughter, and ordered that no one give them bread, salt, water or fire.', 'xeral',
   'wide shot of {vicario} reading a decree aloud on the steps of a small granite church, while {dorotea}, and {maria}, '
   'stand alone below him',
   'priest', 'campas', ('i2v', 'pan_esq', [], 'the priest reads from the paper while the two women lower their heads'), 2, 'fan',
   neg='cathedral, cars')
pl([35, 36], 'Water from seven springs for the cattle. And for them, not even water.', 'plano_medio',
   'medium shot of {dorotea}, and {maria}, sitting on a stone doorstep at dusk, an empty clay jug on its side between '
   'them',
   'clay jug', 'vento', ('i2v', 'avanza', [], 'the younger woman picks up the empty jug and looks into it'), 1, 'fan',
   neg='glass bottle, plastic, modern door')
# II. O conxuro do barco
pl([37], 'That paper kept even the smallest thing, a mistaken word.', 'bodegon',
   'still life of a single old bundle of trial papers tied with a faded red cord, resting on a dark wooden shelf, a '
   'narrow beam of light falling across it, dust in the air, deep shadows',
   'papers', 'limpa', ('paralaxe', 'sobe', ['po'], None), 3, 'non', neg='printed books, plastic')
pl([38], 'With the queimada spell the opposite happened: along the way it was left without the most important thing, '
         'the name of the one who wrote it.', 'detalle',
   'close-up of a handwritten sheet of verses lying beside a wide clay bowl of blue flames on a wooden table, the bottom '
   'corner of the sheet torn away where a signature would be, blue light flickering on the paper, 1960s',
   'sheet of paper', 'lume', ('paralaxe', 'baixa', ['lume'], None), 3, 'non', epoca='xx',
   neg='printed text, typewriter, light bulb')
pl([39], 'Mariano Marcos Abalo used to meet his friends aboard the old boat, moored in the port, and there they made '
         'queimadas.', 'plano_medio',
   'medium shot of {mariano}, and {amigos}, laughing on coils of rope around a clay bowl of blue flames on the deck of '
   'an old wooden boat in a harbour at night',
   'boat', 'lume+mar', ('i2v', 'xira_esq', ['lume'], 'the three men laugh and lean toward the flames as one stirs with '
                                                    'the ladle'), 1, 'fan', epoca='xx',
   neg='modern yacht, street lamps')
pl([40], 'He used to say he had written the spell to give those queimadas a bit of ritual.', 'plano_medio',
   'medium close-up of {mariano}, reading verses aloud from a sheet of paper with a solemn face, lit from below by a '
   'soft blue glow, a friend smiling beside him, night on the deck of a boat, 1960s',
   'sheet of paper', 'lume', ('i2v', 'avanza', [], 'he reads aloud with a solemn face and slowly raises one hand'), 1,
   'fan', epoca='xx', neg='light bulb, glasses')
pl([41], 'And that there were five or six other spells from that time, but none was as successful as his.', 'bodegon',
   'still life of five or six handwritten sheets of verses scattered on a worn wooden table beside an oil lantern on '
   'the deck of a boat at night, one sheet lit in the warm light, the others in shadow, 1960s',
   'papers', 'mar', ('paralaxe', 'xira_der', ['candea'], None), 3, 'non', epoca='xx',
   neg='printed text, typewriter, light bulb')
pl([42], "A company sold copies of the spell without the author's name, and so many people thought it was a popular, "
         'anonymous text.', 'plano_medio',
   'medium shot of two tourists in late-20th-century clothes reading a printed card with a poem and a small drawing of a clay '
   'bowl, at the wooden counter of a souvenir shop where stacks of the same printed cards lie for sale, warm shop light',
   'printed card', 'xente', ('i2v', 'avanza', [], 'they read the card together and one points at the poem'), 2, 'fan',
   epoca='xx', neg='computer')
pl([43], 'In two thousand and one, the author registered it as intellectual property.', 'detalle',
   "close-up of an older man's hand signing an official registration form with a fountain pen on an office desk, a "
   'rubber stamp and a printed copy of a poem beside it, daylight, 2001',
   'document', 'limpa', ('i2v', 'baixa', [], 'the hand slowly signs the form'), 2, 'mans', epoca='xx',
   neg='laptop', arq='mans')
pl([44], 'So some nameless words on paper ended up seeming to belong to everyone, and to have always existed.', 'xeral',
   'wide shot of a village festival at night, a crowd raising small clay cups toward a large clay bowl of blue flames '
   'on a stone table, faces softly blurred in the darkness, warm and blue light',
   'clay bowl', 'xente', ('i2v', 'recua', ['lume'], 'people raise their cups and the blue flames flicker'), 2, 'fan',
   epoca='xx', neg='plastic cups, stage lights')
