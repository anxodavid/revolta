"""Escolla das referencias gráficas por concepto (Gauntlet 4, peza IMAXE): xera `referencias.json`.

A escolla e o campo `ensina` son de Claude (este axente), que mirou as 226 referencias en follas de contactos o
02-10-2026; a licenza, o autor e o crédito saen da API de Wikimedia Commons (extmetadata da páxina de cada ficheiro)
e da API do Met (isPublicDomain), comprobados ese día (scripts/licenzas_commons.py).
Uso permitido (contexto do Gauntlet 4 §2): `semente` só CC0, dominio público ou CC BY; `tal_cal` as CC BY-SA (amosala
enteira, co crédito, sen transformala); `semente` dunha BY-SA só se o promotor o decide.
Uso: python escoller_refs.py CATALOGO.json LICENZAS.json > ../referencias.json
"""
import json, sys

# (ficheiro, ensina, notas). As BY-SA levan uso tal_cal e as demais semente (o script compróbao coa licenza).
ESCOLLA = {
    '01-horreo': [
        ('01-horreo/02-horreos-galicien-img-0274a.jpg', 'hórreo de granito enteiro, de tres cuartos: pés con tornarratos en forma de cogomelo, corpo de cantaría con lamas, tellado a dúas augas con remates', 'vertical (4000x6000): para 16:9 hai que encaixalo (modo profundidade con marxes) ou recortar o corpo'),
        ('01-horreo/16-horreos-de-muimenta-carballeda-de-avia-galiza.jpg', 'varios hórreos de pedra e madeira sobre pés, nun eido de aldea', 'horizontal, vale para img2img en 16:9; tellados de tella'),
        ('01-horreo/11-2-horreos.jpg', 'dous hórreos de madeira sobre esteos de pedra (tipo do interior)', 'hai unha estrada e cables: o prompt e a porta teñen que quitalos'),
        ('01-horreo/12-horreo-en-paradela-boboras.jpg', 'hórreo pequeno de granito coa porta aberta e o millo dentro', 'vertical; detalle'),
        ('01-horreo/07-horreo-de-lira-carnota-galiza.jpg', 'hórreo longo de Lira (Carnota), perspectiva', 'BY-SA'),
        ('01-horreo/04-2013-horreo-en-cambados-galicia-spain.jpg', 'hórreo de granito de perfil, coa ría detrás', 'BY-SA; tella laranxa'),
        ('01-horreo/14-eira-e-rua-de-as-ventelas.jpg', 'aldea de lousa con hórreos baixo a neve', 'BY-SA; postes de luz'),
    ],
    '02-carro-bois': [
        ('02-carro-bois/15-carro-monte-pio-santiago-de-compostela.jpg', 'carro do país enteiro, de tres cuartos, con rodas macizas de táboas e treitoiro', 'a única semente permitida que ensina ben a roda maciza'),
        ('02-carro-bois/11-carro-santiago-de-compostela.jpg', 'carro na neve ao solpor, perfil baixo', 'a roda ten ocos: non serve para ensinar a roda maciza'),
        ('02-carro-bois/01-a-arnoia-carro-a-beira-do-mino-galiza-3.jpg', 'carro de perfil con rodas macizas, a carón do Miño', 'BY-SA; o mellor carro do lote'),
        ('02-carro-bois/03-carros-na-praia-de-peralto-galicia-galiza-galicia.jpg', 'dous carros de perfil con rodas macizas e pipas', 'BY-SA'),
        ('02-carro-bois/10-carro-barrana-boiro.jpg', 'roda maciza en primeiro plano', 'BY-SA'),
    ],
    '03-palloza-casa': [
        ('03-palloza-casa/10-palloza-cantexeira.jpg', 'palloza de muros de pedra e cuberta de colmo', 'leva un tubo de cheminea metálico: quitalo no prompt'),
        ('03-palloza-casa/16-canedo-01-palloza-by-dpc.jpg', 'casa redonda de pedra con teito de colmo', 'restaurada, con fiestras de carpintería actual'),
        ('03-palloza-casa/02-el-cebreiro-lugo-palloza-ni.jpg', 'palloza do Cebreiro de fronte: porta de madeira, colmo, lousas', 'BY-SA'),
        ('03-palloza-casa/11-palloza-galega.jpg', 'palloza enteira de perfil, colmo ata o chan', 'BY-SA'),
        ('03-palloza-casa/04-ancares-1976-63.jpg', 'pallozas dos Ancares en 1976 (foto antiga)', 'BY-SA; documento de época'),
    ],
    '04-pazo': [
        ('04-pazo/15-vigo-casa-torre-de-pazos-figueroa-3.jpg', 'casa torre urbana de cantaría', 'CC0 pero con tenda e rótulos: semente pobre'),
        ('04-pazo/07-torre-do-pazo-de-oca-a-estrada.jpg', 'torre ameada de pazo', 'BY-SA'),
        ('04-pazo/12-fachada-principal-do-pazo-de-mos.jpg', 'fachada de pazo con balcóns e escudo', 'BY-SA'),
    ],
    '05-cruceiro-peto': [
        ('05-cruceiro-peto/03-peto-de-animas-vilanova-dos-infantes-celanova-galiza-vi-01.jpg', 'peto de ánimas de cantaría con reixa', 'BY-SA (non hai ningunha permitida neste concepto)'),
        ('05-cruceiro-peto/10-peto-de-animas-e-muino-en-escuadra-a-la.jpg', 'peto de ánimas nun camiño, con muíño', 'BY-SA'),
        ('05-cruceiro-peto/09-2018-cruceiro-en-vigo-galiza.jpg', 'cruceiro labrado (Cristo e Virxe)', 'BY-SA; SDXL xa debuxa ben o cruceiro'),
    ],
    '06-cocina': [
        ('06-cocina/03-reitoral-de-beiro-carballeda-de-avia-3.jpg', 'lareira grande de granito con cambota (campá) sobre o lar, baleira', 'o mellor esqueleto de lareira permitido'),
        ('06-cocina/14-rfk-005-feuerstelle-im-17-jh.jpg', 'lar alto do século XVII cun pote colgado dunha cadea e un brazo de ferro (como a gramalleira)', 'museo alemán (paredes de entramado): usar só a estrutura'),
        ('06-cocina/11-cocina-de-lena-forno.jpg', 'cociña económica de ferro co lume', 'NON como semente: é o anacronismo que o tribunal viu no plano 91; serve de exemplo negativo'),
        ('06-cocina/02-lareira-rural.jpg', 'cociña de aldea: pote colgado sobre a lareira, andeis con louza', 'BY-SA; a mellor lareira do lote'),
        ('06-cocina/05-lalin-casa-do-patron-01-15b.jpg', 'lareira con potes e cambota (museo)', 'BY-SA'),
        ('06-cocina/04-coles-ucelle-pazo-de-fontefiz-lareira.jpg', 'lareira de pedra co brazo da gramalleira', 'BY-SA'),
    ],
    '07-queimada': [
        ('07-queimada/02-camino-de-santiago-may-2008.jpg', 'tarteira de barro con patas, cuncas colgadas no bordo e cazo de madeira', 'sen lume; vale de bodegón'),
        ('07-queimada/09-pequena-queimada.jpg', 'lapas azuis nunha cunca de barro', 'mesa de restaurante con botellas e vasos: recortar a cunca'),
        ('07-queimada/06-queimada.jpg', 'un home agachado ante a queimada ardendo, de noite, con xente arredor', 'persoas recoñecibles e roupa actual: só a cunca co lume (recorte) ou a profundidade'),
        ('07-queimada/01-queimada-fuego.jpg', 'lapa azul enchendo a tarteira, primeiro plano', 'BY-SA; a mellor queimada do lote'),
        ('07-queimada/10-sao-miguel-5470-portugal-panoramio.jpg', 'o cazo vertendo a queimada en chamas azuis', 'BY-SA'),
    ],
    '08-traje': [
        ('08-traje/02-gallega-galicienne-en-costume-de-fete-19316007923.jpg', 'traxe de festa galego dunha muller (gravado de Doré, 1862)', 'século XIX, non XVII; mellor amosalo tal cal como documento'),
        ('08-traje/03-traxe-tradicional-galego-santiago-de-compostela.jpg', 'cofia de encaixe, xoias e dengue (traxe de festa)', 'persoa real recoñecible: NON usar como semente de caras'),
        ('08-traje/12-museo-liste-vigo-zocas.jpg', 'zocas de madeira (museo)', 'BY-SA'),
    ],
    '09-herramientas': [
        ('09-herramientas/12-apeiros-de-labregos-4560316123.jpg', 'apeiros de labranza de madeira e ferro', ''),
        ('09-herramientas/13-gadana-2767974677.jpg', 'gadaña', 'vertical'),
        ('09-herramientas/06-arado-no-pazo-de-hermida-dodro.jpg', 'arado de madeira', ''),
    ],
    '10-muino-fonte': [
        ('10-muino-fonte/01-molino-batans-do-mosquetin.jpg', 'interior de muíño: moa de pedra e moega de madeira', 'vertical'),
        ('10-muino-fonte/03-muino-da-veiga.jpg', 'moa, moega e millo en primeiro plano', ''),
        ('10-muino-fonte/08-batanes-interior.jpg', 'interior dun batán de madeira', 'pequena (1189x789)'),
    ],
    '11-barcos-costa': [
        ('11-barcos-costa/16-dorna-a-vela-rianxo-de-noite.jpg', 'dorna a vela de noite xunto a un peirao de pedra', ''),
        ('11-barcos-costa/15-dorna-afundida-taramancos-boa-noia.jpg', 'dorna de madeira na auga', 'pintura e matrícula actuais'),
    ],
    '12-iconografia': [
        ('12-iconografia/04-dende-a-fiestra-8578368554.jpg', 'tellados de pedra e tella e campanario vistos desde unha fiestra de pedra', 'semente de aldea galega desde dentro'),
        ('12-iconografia/02-castelo-de-pambre-palas-de-rei.jpg', 'torre e muralla de granito con musgo (castelo de Pambre)', ''),
        ('12-iconografia/10-iglesia-de-san-salvador-de-asma-2.jpg', 'canecillos románicos e cornixa de granito', ''),
        ('12-iconografia/21-cantigas-de-santa-maria-codice-de-el-escorial-cantiga-123-miniaturas.jpg', 'miniaturas das Cantigas (s. XIII)', 'dominio público: documento para amosar tal cal (elemento orixinal) en temas medievais'),
    ],
    '13-armas-ropa': [
        ('13-armas-ropa/16-cabasset-second-half-16th-century.jpg', 'capacete (cabasset) do XVI, como o dos gardas', 'CC0 do Met; fondo neutro'),
    ],
    '14-samos-antiguo': [
        ('14-samos-antiguo/02-2017-mosteiro-de-samos-samos-galiza-3.jpg', 'mosteiro de Samos', 'BY-SA (ningunha permitida neste concepto)'),
    ],
}


def main():
    cat = {x['ficheiro']: x for x in json.load(open(sys.argv[1]))}
    lic = json.load(open(sys.argv[2]))
    out = []
    for c, xs in ESCOLLA.items():
        for k, (f, ensina, notas) in enumerate(xs):
            if f not in cat:     # os nomes de descargar.sh van cortados: búscase polo número do concepto ("01-horreo/02-")
                cand = [x for x in cat if x.startswith(f[:len(c) + 4])]
                if len(cand) != 1:
                    raise SystemExit(f'non está no catálogo: {f} (candidatos {cand[:3]})')
                f = cand[0]
            x, l = cat[f], lic[f]
            licenza = l['licenza']
            permitida = 'SA' not in licenza and 'NON' not in licenza
            uso = 'semente' if permitida else 'tal_cal'
            if 'NON como semente' in notas:
                uso = 'non'
            autor = l.get('autor') or x['autor']
            lic_url = l.get('licenza_url') or ''
            credito = f'«{x["titulo"]}», de {autor}' + (f', {licenza} ({lic_url})' if lic_url else f', {licenza}') + \
                      (', vía Wikimedia Commons' if 'commons' in x['url_pagina'] else ', The Metropolitan Museum of Art (Open Access)')
            out.append({'id': f'{c[:2]}-{k + 1:02d}', 'ficheiro': f, 'concepto': c, 'licenza': licenza,
                        'licenza_comprobada': 'API de Commons (extmetadata), 02-10-2026' if 'commons' in x['url_pagina'] else 'API do Met (isPublicDomain), 02-10-2026',
                        'autor': autor, 'url': x['url_pagina'], 'credito': credito, 'uso': uso, 'ensina': ensina,
                        'notas': notas, 'tamaño': f"{l.get('ancho') or ''}x{l.get('alto') or ''}"})
    json.dump({'descricion': __doc__.strip(), 'referencias': out}, sys.stdout, ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
