# Calibración da porta de veracidade (ronda 3). Uso: python probas/veracidade_calibracion.py > probas/veracidade_calibracion.txt
import sys, yaml, json
sys.path.insert(0,'/home/user/revolta/herramientas/pipeline')
import pipeline, veracidade
tema=yaml.safe_load(open('/home/user/revolta/herramientas/pipeline/temas/irmandinos-apertura.yaml'))
fs=pipeline.feitos(tema)
v=veracidade.Verificador(fs)
H=["Os nobres tiñan poder, pero a irmandade venceu.",
"Os campesiños, mariñeiros e artesáns uníronse contra os señores das fortalezas.",
"A xente común botou abaixo torres con paus e pedras.",
"A Rocha Forte caeu baixo as súas mans.",
"As chaves da Rocha Forte caeron unha tras outra.",
"O lume ardeu en silencio durante séculos.",
"Labregos e mariñeiros botaron abaixo moitas fortalezas do reino.",
"Os señores volveron e venceron á irmandade.",
"A irmandade derrotou os señores.",
"A irmandade foi derrotada cando os señores volveron.",
"Despois os vasalos tiveron que levantar de novo as torres que derrubaran.",
"A irmandade gañou a guerra e os señores nunca volveron.",
"Para a xente, as torres eran refuxios de malfeitores.",
"Un exército de xente diversa derrubou castelos.",
"A chuvia caía mansa sobre as pedras dos camiños."]
for h in H[:0]+H:
    for modo in ('gancho','relato'):
        r=v.frase(h,modo)
        print(modo[:3], 'OK ' if r['ok'] else 'NON', r['E'], r['apoio'], r['cobertura'], r['C_max'], r['motivo'][:60],'|',h)
print('=== guion ronda 2')
g=open('/home/user/revolta/plan-de-negocio/gauntlet2/video/execucion/guion.txt').read()
pars=[p for p in g.split('\n\n') if p.strip()]
for k,p in enumerate(pars[1:]):
    pr,rs=v.texto(p,'gancho' if k<2 else 'relato')
    for r in rs: print(k,'OK ' if r['ok'] else 'NON', r['E'], r['cobertura'], r['C_max'], r['motivo'][:50],'|',r['frase'][:90])
print('=== feitos')
for f in fs:
    r=v.frase(pipeline.normalizar(f),'gancho'); print('OK ' if r['ok'] else 'NON', r['motivo'][:50], f[:60])
