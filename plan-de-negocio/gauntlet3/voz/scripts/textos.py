"""Textos fixos das probas da peza VOZ (Gauntlet 3). Escritos por Claude (axente de voz) para medir; non son guion.

PASAXE: 7 frases sobre a lenda da Santa Compaña, escritas antes de que a peza TEMA elixise tema: úsanse no barrido
das 40 referencias e nas medidas do efecto de cada control. O legendario vai como lenda ("contan", "din").
PASAXE_MEIGAS: 7 frases do tema elixido ("As meigas de verdade", tema/investigacion.md: o conxuro de 1967, a parteira
de Vilalba segundo unha testemuña, a meiga como curandeira) para as medidas da curva nos 5 puntos e a mostra. Cada
pasaxe rendérase igual en cada punto da curva: as diferenzas entre puntos son só da voz.

COTOVIA_PROPIAS: frases con vogais abertas e pechadas (porta, terra, home, pedra, óso), monosílabos (que, de, o, si,
non, á) e nomes propios galegos, para o A/B de Cotovía. Complétanse con frases de test do corpus Nos_Brais-GL (que
teñen transcrición fonética da Cotovía coa que se adestrou o modelo).
"""
PASAXE = [
    'Contan os vellos que, nas noites de néboa, unha procesión de ánimas percorre en silencio os camiños das aldeas.',
    'Chámanlle a Santa Compaña, e din que quen a atopa debe apartarse do camiño e non mirar atrás.',
    'Diante vai sempre un vivo cunha cruz na man, e non pode soltala ata que atopa outra persoa que a leve.',
    'Non había casa sen lareira, nin lareira sen historias: o lume quentaba as mans e tamén as palabras.',
    'Mentres fóra chovía sobre os tellados de lousa, en Ourense ou na Costa da Morte, as avoas falaban das meigas e dos mortos.',
    'Os nenos escoitaban co corpo quedo e os ollos pechados, ata que o sono os levaba amodo.',
    'E así, noite tras noite, a memoria da terra pasaba dunha voz a outra, coma unha auga mansa.',
]

PASAXE_MEIGAS = [
    'Seguramente oíches o conxuro da queimada e pensas que é moi antigo.',
    'Non o é: escribiuno en Vigo, en mil novecentos sesenta e sete, Mariano Marcos Abalo.',
    'En Vilalba, en mil seiscentos dezasete, unha testemuña declarou que unha parteira dicía poder pasarlle a un home as dores do parto.',
    'Abondaba con calzarlle ao home os zapatos dela e dicir unhas palabras.',
    'A meiga dos papeis non era a bruxa dos contos, senón a curandeira, a parteira, a muller que sabía de herbas.',
    'Contan que na noite de San Xoán as mozas ían á fonte antes de que saíse o sol.',
    'Chove na lousa, amodo, e a historia pode esperar ata mañá.',
]
PARRAFO = {'PASAXE': 3, 'PASAXE_MEIGAS': 4}      # índice da frase que abre o segundo parágrafo (pausa_parrafo)

COTOVIA_PROPIAS = [
    'A porta da torre estaba aberta, e o home entrou sen facer ruído.',
    'O óso quedou no chan, preto da pedra do forno vello.',
    'Rosalía de Castro naceu en Santiago de Compostela e morreu en Padrón.',
    'Pardo de Cela foi degolado en Mondoñedo, diante da catedral.',
    'Xelmírez mandou erguer torres e murallas arredor da cidade.',
    'O mar de Fisterra é bravo no inverno, e as ondas baten nas rochas.',
    'Nesta terra de néboa, cada pedra garda unha historia vella.',
    'Dixo que si, que o faría, pero non o fixo nunca.',
    'Ela veu á feira de Ourense co seu irmán e coa súa nai.',
    'Onte á noite choveu moito sobre os tellados de lousa de Lugo.',
    'Din que a Santa Compaña pasa de noite polos camiños de Lalín e do Carballiño.',
    'O corvo pousou na pena, e a moza botou a correr cara á ponte.',
]
