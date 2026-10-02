"""Etiquetas das imaxes da v1 para calibrar a porta v6 e a medida de correlación (Gauntlet 4, peza IMAXE).

Fontes: (1) tribunal final do Gauntlet 3 (`gauntlet3/veredictos/tribunal-final.md` §2: "Bloquea", "Molesta", "Menor",
"Lo que funciona" e os rexeitamentos que considerou falsos); viu as imaxes ANTES da rolda de arranxos, así que os 11
planos cambiados (5, 31, 56, 61, 67, 84, 91, 133, 145, 153, 161) etiquétanse na súa versión vella (git 4f43fb5, `v`);
as versións novas entran como imaxes sen etiqueta do tribunal. (2) Claude (este axente), mirando as follas de contactos
o 02-10-2026: defectos que o tribunal non listou (`fonte: claude`), se a `clave` do plano se ve (`clave_ve`) e se a
imaxe ilustra o que se di (`ilustra`: 2 = ilustra o que se oe, 1 = relacionada ou de ambiente, 0 = desconectada).
Son xuízos dun axente, non dunha persoa.
Saída: calibracion/etiquetas-v1.json. Uso: python etiquetas_v1.py
"""
import json, os
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
V1 = REPO / 'plan-de-negocio/gauntlet3/video'
VELLAS = {5: '004-983abd46-0', 31: '030-ef658184-0', 56: '055-93ec6c81-0', 61: '060-879e4f8a-1', 67: '066-1eb7df19-4',
          84: '083-5779b492-3', 91: '090-c464f180-1', 133: '132-a8a95fcc-0', 145: '144-f4f740ab-4',
          153: '152-179e853a-0', 161: '160-32b10266-0'}
# --- tribunal (sobre as imaxes vistas por el) ---------------------------------------------------------------------
BLOQUEA = {84: ['luz_electrica', 'radiador'], 133: ['luz_electrica'], 161: ['casa_allea', 'luz_electrica'],
           56: ['maleta_rodas']}
MOLESTA = {5: ['casa_allea'], 23: ['casa_allea'], 29: ['casa_allea'], 33: ['casa_allea'], 61: ['catedral_inventada'],
           68: ['casa_allea'], 75: ['casa_allea'], 134: ['casa_allea'], 24: ['roupa_actual'], 26: ['roupa_actual'],
           34: ['roupa_actual'], 35: ['roupa_actual'], 46: ['roupa_actual'], 78: ['roupa_actual'], 85: ['roupa_actual'],
           31: ['billa_fregadoiro'], 91: ['cocina_economica', 'luz_electrica'], 94: ['interior_moderno', 'luz_electrica'],
           67: ['interior_moderno', 'xesto_contrario'], 82: ['luz_electrica'], 105: ['luz_electrica'], 148: ['luz_electrica'],
           123: ['luz_electrica'], 20: ['lume_mesa'], 116: ['roupa_actual'], 145: ['lume_durmir'], 153: ['lume_durmir'],
           7: ['clixe_meiga'], 77: ['casa_allea']}   # 77: "rechazos que acertaban y molestan en pantalla"
MENOR = {9: ['estilo'], 10: ['texto'], 13: ['obxecto_mal'], 55: ['obxecto_mal'], 129: ['obxecto_mal'], 141: ['obxecto_mal'],
         147: ['obxecto_mal'], 150: ['mobles_actuais'], 156: ['roupa_actual'], 130: ['xanela_moderna']}
FUNCIONA = {1, 2, 14, 32, 53, 64, 69, 72, 98, 128, 137, 138, 139, 143} | set(range(98, 133)) | set(range(155, 161))
ACEPTABLE = {59, 100, 104, 108, 110, 113, 127, 146, 154, 160, 162}   # rexeitamentos da v5 que o tribunal deu por falsos
# --- Claude (02-10-2026), defectos que o tribunal non listou ------------------------------------------------------
CLAUDE = {40: ['casa_allea', 'roupa_actual'], 90: ['casa_allea'], 111: ['casa_allea'], 159: ['casa_allea'],
          80: ['luz_electrica'], 112: ['luz_electrica'], 122: ['xanela_moderna'], 131: ['xanela_moderna'],
          135: ['xanela_moderna'], 37: ['roupa_actual']}
# 20th century na narración (47-60: o conxuro de 1967, a queimada dos anos 50): roupa e obxectos do XX son de época
SECULO_XX = set(range(47, 61))
# --- Claude: ¿vese a clave? (False = non se ve) e ¿ilustra o que se di? (0/1/2) ------------------------------------
NON_CLAVE = {8, 16, 17, 19, 20, 22, 26, 34, 37, 39, 48, 55, 67, 70, 73, 97, 126, 135}
ILUSTRA = {1: 1, 2: 2, 3: 1, 4: 1, 5: 1, 6: 2, 7: 1, 8: 0, 9: 2, 10: 1, 11: 1, 12: 0, 13: 2, 14: 2, 15: 2, 16: 0, 17: 2,
           18: 1, 19: 0, 20: 0, 21: 0, 22: 1, 23: 1, 24: 1, 25: 2, 26: 0, 27: 2, 28: 2, 29: 1, 30: 1, 31: 2, 32: 2, 33: 1,
           34: 0, 35: 1, 36: 2, 37: 0, 38: 2, 39: 1, 40: 1, 41: 2, 42: 2, 43: 2, 44: 1, 45: 2, 46: 0, 47: 2, 48: 0, 49: 0,
           50: 1, 51: 1, 52: 1, 53: 2, 54: 2, 55: 0, 56: 2, 57: 2, 58: 2, 59: 2, 60: 2, 61: 1, 62: 2, 63: 1, 64: 1, 65: 1,
           66: 2, 67: 0, 68: 1, 69: 2, 70: 1, 71: 1, 72: 2, 73: 1, 74: 2, 75: 1, 76: 1, 77: 1, 78: 2, 79: 2, 80: 2, 81: 2,
           82: 1, 83: 2, 84: 2, 85: 2, 86: 2, 87: 1, 88: 1, 89: 1, 90: 1, 91: 2, 92: 2, 93: 2, 94: 1, 95: 2, 96: 2, 97: 2,
           98: 2, 99: 2, 100: 2, 101: 2, 102: 2, 103: 2, 104: 1, 105: 2, 106: 2, 107: 2, 108: 1, 109: 2, 110: 2, 111: 2,
           112: 2, 113: 2, 114: 2, 115: 2, 116: 1, 117: 2, 118: 2, 119: 2, 120: 1, 121: 2, 122: 2, 123: 1, 124: 2, 125: 2,
           126: 1, 127: 2, 128: 2, 129: 2, 130: 2, 131: 2, 132: 0, 133: 0, 134: 1, 135: 1, 136: 2, 137: 2, 138: 2, 139: 2,
           140: 0, 141: 1, 142: 2, 143: 2, 144: 2, 145: 1, 146: 0, 147: 2, 148: 2, 149: 2, 150: 1, 151: 2, 152: 2, 153: 2,
           154: 1, 155: 2, 156: 0, 157: 2, 158: 2, 159: 1, 160: 1, 161: 2, 162: 2}
# versións vellas dos 11 planos cambiados (ilustra, clave_ve), segundo o tribunal e Claude
VELLA_ILUSTRA = {5: (1, True), 31: (2, True), 56: (2, True), 61: (1, True), 67: (0, False), 84: (1, False), 91: (1, False),
                 133: (1, False), 145: (0, False), 153: (1, True), 161: (2, True)}


def main():
    esc = json.load(open(V1 / 'escenas-montadas.json'))
    fich = sorted(f for f in os.listdir(V1 / 'imaxes') if f.endswith('.jpg'))
    out = []
    for i, f in enumerate(fich):
        n = i + 1
        d = {'n': n, 'ficheiro': f'imaxes/{f}', 'version': 'actual', 'clave': esc[i].get('clave'),
             'clave_ve': n not in NON_CLAVE, 'ilustra': ILUSTRA[n], 'seculo_xx': n in SECULO_XX,
             'fase': esc[i].get('fase')}
        if n in VELLAS:
            d['tribunal'] = 'despois_dos_arranxos'      # o tribunal non viu esta versión
        elif n in BLOQUEA or n in MOLESTA or n in MENOR:
            d['tribunal'] = 'bloquea' if n in BLOQUEA else 'molesta' if n in MOLESTA else 'menor'
            d['defectos'] = (BLOQUEA.get(n) or MOLESTA.get(n) or MENOR.get(n))
        elif n in ACEPTABLE:
            d['tribunal'] = 'aceptable'
        elif n in FUNCIONA:
            d['tribunal'] = 'funciona'
        else:
            d['tribunal'] = 'sen_mencion'
        if n in CLAUDE and n not in VELLAS:
            d['defectos_claude'] = CLAUDE[n]
        out.append(d)
    for n, base in VELLAS.items():
        il, cv = VELLA_ILUSTRA[n]
        d = {'n': n, 'ficheiro': f'vellas/{base}.jpg', 'version': 'vella', 'clave': None, 'clave_ve': cv, 'ilustra': il,
             'seculo_xx': n in SECULO_XX, 'fase': esc[n - 1].get('fase'),
             'tribunal': 'bloquea' if n in BLOQUEA else 'molesta' if n in MOLESTA else 'sen_mencion'}
        if n in BLOQUEA or n in MOLESTA:
            d['defectos'] = BLOQUEA.get(n) or MOLESTA.get(n)
        out.append(d)
    p = Path(__file__).resolve().parents[1] / 'calibracion' / 'etiquetas-v1.json'
    p.write_text(json.dumps({'descricion': __doc__.strip(), 'imaxes': out}, ensure_ascii=False, indent=1))
    from collections import Counter
    print(p, len(out), Counter(d['tribunal'] for d in out))


if __name__ == '__main__':
    main()
