#!/usr/bin/env python3
"""Rolda 2 do guion v2 (Gauntlet 4): aplica a lista pechada do crítico B (B1-B14 no guion, B15 na ficha) e despois as
melloras do crítico A escollidas (A1-A10). Cada texto "actual" ten que aparecer unha soa vez. Guionista (axente Claude).

    python3 aplicar_r2.py guion-r1.txt guion-r2.txt [--so-b SAIDA_B.txt]
"""
import sys
from pathlib import Path

B = [  # veredictos/guion-r1-lingua-veracidade.md §7, literal
 ('B1', 'Abondaba con calzarlle ao home os zapatos da muller,', 'Abondaría con calzarlle ao home os zapatos da muller,'),
 ('B2', 'As de Dorotea son vellas de verdade, e só as coñecemos porque alguén as escribiu nun proceso por bruxería.',
        'O que se contou de Dorotea é vello de verdade, e só o coñecemos porque alguén o escribiu nun proceso por bruxería.'),
 ('B3', 'E hai mesmo unha lista coas mulleres', 'E hai mesmo noticia dunha lista coas mulleres'),
 ('B4', 'Algúns veciños murmuraban que María era meiga, e que non era boa cristiá.',
        'Unha testemuña oíu murmurar entre algúns veciños que María era meiga, e que non era boa cristiá.'),
 ('B5', 'Unha testemuña contou que, cando tiña o gando no monte,', 'E contou que María, cando tiña o gando no monte,'),
 ('B6', 'Podemos pensala alí,', 'Pensemos nela alí,'),
 ('B7', 'As palabras dos procesos naceron noutro sitio: nos tribunais.', 'As palabras dos procesos acabaron noutro sitio: nos tribunais.'),
 ('B8', 'coas meigas a temida Inquisición foi branda', 'coas meigas galegas a temida Inquisición foi branda'),
 ('B9', 'Cómpre pensala diante de quen pregunta e de quen escribe.', 'Pensemos nela diante de quen pregunta e de quen escribe.'),
 ('B10', 'Que á casa da nai acudía moita xente,', 'Que á nai acudía moita xente,'),
 ('B11', 'Alí viron e recoñeceron as mulleres,', 'Alí, dixo, viron e recoñeceron as mulleres,'),
 ('B12', 'Do que elas falaban aquela noite, nestes papeis non queda nin unha palabra. Queda a lista, escrita por outros.',
         'Do que elas dixesen aquela noite, non nos chegou nin unha palabra. Só nos chegou a noticia da lista, na voz doutros.'),
 ('B13', 'a miúdo das súas nais. Nai e filla eran as de Vilalba. Nos papeis,', 'a miúdo das súas nais. Nos papeis,'),
 ('B14', 'Para el, eran necesarias,', 'Para el, aquelas mulleres eran necesarias,'),
]

A = [  # veredictos/guion-r1-cego.md, "As 10 melloras", adaptadas sen desfacer B
 ('A2', 'e só o coñecemos porque alguén o escribiu nun proceso por bruxería.',
        'e só o coñecemos porque alguén o escribiu nun proceso por bruxería. As palabras que ela sabía, esas non as coñecemos.'),
 ('A5', 'Esta noite imos buscalas no pouco que delas quedou escrito.',
        'Esta noite imos buscalas no pouco que delas quedou escrito, e preguntarnos de quen son, de verdade, esas palabras.'),
 ('A4a', 'O papel consérvao o Arquivo do Reino de Galicia, entre uns trinta procesos por bruxería da xustiza real.',
         'O papel gárdao o Arquivo do Reino de Galicia, con outros procesos por bruxería da Real Audiencia.'),
 ('A7', 'Ese papel gardou ata unha palabra trabucada. Ás veces pasa o contrario, e o que se perde é o nome de quen escribiu. Foi o que lle pasou ao conxuro da queimada.',
        'Aquel papel gardou ata o máis pequeno, unha palabra trabucada. Ao conxuro da queimada pasoulle ao revés: polo camiño quedou sen o máis importante, o nome de quen o escribiu.'),
 ('A10a', 'Contaba que escribira o conxuro para darlles un pouco de ritual.',
          'Contaba que escribira o conxuro para darlles un pouco de ritual a aquelas queimadas.'),
 ('A10b', 'Unha empresa vendeu copias sen o nome do autor,', 'Unha empresa vendeu copias do conxuro sen o nome do autor,'),
 ('A4b', 'Os xuíces da xustiza ordinaria foron moito máis duros. Nos procesos da Real Audiencia, a xustiza do rei, todas as acusadas eran mulleres.',
         'Os xuíces civís foron moito máis duros. E nos procesos civís da Real Audiencia, todas as acusadas eran mulleres.'),
 ('A3a', 'Pensemos nela diante de quen pregunta e de quen escribe.', 'Diante dela, alguén preguntaba, e alguén escribía.'),
 ('A3b', 'Podemos pensar nunha noite curta de xuño, na auga fría da fonte e nuns ollos que miran desde a escuridade.',
         'Pensemos nunha noite curta de xuño: a auga fría da fonte, e uns ollos que miran desde a escuridade.'),
 ('A1', 'Nos papeis, Pousa atopou esta expresión: maldita a nai que non ensina a súa filla a meigar.\n\n'
        'Para el, aquelas mulleres eran necesarias, porque resolvían os problemas de cada día: a saúde, as colleitas e o gando. '
        'Moitas denuncias nacían de liortas entre veciños, coma en Campo Lameiro. Ás veces había quen falaba de bruxería cando, '
        'en realidade, as ovellas dun veciño lle comeran a viña ao outro.\n\n'
        'Moito despois, o frade Benito Xerónimo Feijoo escribiu contra as falsas crenzas e as supersticións.',
        'Nos papeis, Pousa atopou esta expresión: maldita a nai que non ensina a súa filla a meigar.\n\n'
        'Moitas denuncias nacían de liortas entre veciños, coma en Campo Lameiro. Ás veces había quen falaba de bruxería cando, '
        'en realidade, as ovellas dun veciño lle comeran a viña ao outro. E, con todo, para Pousa aquelas mulleres eran '
        'necesarias, porque resolvían os problemas de cada día: a saúde, as colleitas e o gando. Xa no século dezaoito, '
        'frei Martín Sarmiento defendeu o saber das curandeiras, as meigas, como o de auténticos médicos e botánicos.\n\n'
        'No mesmo século, o frade Benito Xerónimo Feijoo escribiu contra as falsas crenzas e as supersticións.'),
 ('A1b', 'No mesmo século, frei Martín Sarmiento defendeu o saber das curandeiras, as meigas, como o de auténticos médicos e botánicos. E aquí deixamos os papeis.',
         'E aquí deixamos os papeis.'),
 ('A6', 'Nunha cociña de aldea, tras a cea, apáganse as luces.', 'Outra noite, nunha cociña de aldea, tras a cea, apáganse as luces.'),
 ('A0', 'Os comensais xúntanse arredor do pote, para animar os corazóns e estreitar os lazos de amizade.',
        'Os comensais xúntanse arredor do pote, para animar os corazóns.'),
 ('A9', 'A outra meiga, a dos contos, saíu das fábulas que van da aldea aos libros.',
        'A outra meiga, a dos contos, saíu das fábulas que van da aldea aos libros, e dos libros outra vez á aldea.'),
]


def aplicar(t, lista):
    for k, a, b in lista:
        n = t.count(a)
        if n != 1:
            raise SystemExit(f'{k}: o texto actual aparece {n} veces: {a[:70]}')
        t = t.replace(a, b)
    return t


def main():
    src, dst = sys.argv[1], sys.argv[2]
    t = Path(src).read_text()
    tb = aplicar(t, B)
    if '--so-b' in sys.argv:
        Path(sys.argv[sys.argv.index('--so-b') + 1]).write_text(tb)
    Path(dst).write_text(aplicar(tb, A))
    print('feito:', len(B), 'de B e', len(A), 'de A')


if __name__ == '__main__':
    main()
