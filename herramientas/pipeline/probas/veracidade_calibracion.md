# Calibración da porta de veracidade (ronda 3, 30-09-2026)

Xerado con `python probas/veracidade_calibracion.py` (veracidade.py final). Columnas: modo (gan = gancho, rel = relato), resultado, NLI (implicación da mellor premisa), feitos de apoio, coincidencia léxica, contradición máxima (informativa), motivo | frase. Despois: o gancho e o relato da ronda 2 (con "fortaleiras" e "a irmandade venceu") e os feitos do dossier (todos teñen que pasar).

```
gan NON 0.923 [9, 15] 0.2 0.239 desenlace que non está no dossier (venceu); afirmación sen a | Os nobres tiñan poder, pero a irmandade venceu.
rel NON 0.923 [9, 15] 0.2 0.239 desenlace que non está no dossier (venceu); fala de persoas, | Os nobres tiñan poder, pero a irmandade venceu.
gan NON 0.938 [9, 2] 0.57 0.562 afirmación sen apoio no dossier | Os campesiños, mariñeiros e artesáns uníronse contra os señores das fortalezas.
rel OK  0.938 [9, 2] 0.57 0.562  | Os campesiños, mariñeiros e artesáns uníronse contra os señores das fortalezas.
gan NON 0.944 [14, 20] 0.29 0.907 afirmación sen apoio no dossier | A xente común botou abaixo torres con paus e pedras.
rel NON 0.944 [14, 20] 0.29 0.907 fala de persoas, nomes, tempo longo ou desenlace sen apoio n | A xente común botou abaixo torres con paus e pedras.
gan NON 0.988 [14, 17] 0.5 0.988 afirmación sen apoio no dossier | A Rocha Forte caeu baixo as súas mans.
rel OK  0.988 [14, 17] 0.5 0.988  | A Rocha Forte caeu baixo as súas mans.
gan NON 0.986 [9, 14] 0.4 0.212 afirmación sen apoio no dossier | As chaves da Rocha Forte caeron unha tras outra.
rel NON 0.986 [9, 14] 0.4 0.212 fala de persoas, nomes, tempo longo ou desenlace sen apoio n | As chaves da Rocha Forte caeron unha tras outra.
gan NON 0.019 [2, 18] 0.4 0.881 afirmación sen apoio no dossier | O lume ardeu en silencio durante séculos.
rel NON 0.019 [2, 18] 0.4 0.881 fala de persoas, nomes, tempo longo ou desenlace sen apoio n | O lume ardeu en silencio durante séculos.
gan OK  0.719 [15, 14] 0.83 0.821  | Labregos e mariñeiros botaron abaixo moitas fortalezas do reino.
rel OK  0.719 [15, 14] 0.83 0.821  | Labregos e mariñeiros botaron abaixo moitas fortalezas do reino.
gan NON 0.025 [17, 19] 0.75 0.981 desenlace que non está no dossier (venceron); quen fixo que  | Os señores volveron e venceron á irmandade.
rel NON 0.025 [17, 19] 0.75 0.981 desenlace que non está no dossier (venceron); quen fixo que  | Os señores volveron e venceron á irmandade.
gan NON 0.253 [18, 9] 1.0 0.868 desenlace que non está no dossier (derrotou) | A irmandade derrotou os señores.
rel NON 0.253 [18, 9] 1.0 0.868 desenlace que non está no dossier (derrotou) | A irmandade derrotou os señores.
gan OK  0.999 [17, 9] 1.0 0.973  | A irmandade foi derrotada cando os señores volveron.
rel OK  0.999 [17, 9] 1.0 0.973  | A irmandade foi derrotada cando os señores volveron.
gan OK  0.643 [18, 19] 0.67 0.038  | Despois os vasalos tiveron que levantar de novo as torres que derrubaran.
rel OK  0.996 [18, 2] 0.5 0.038  | Despois os vasalos tiveron que levantar de novo as torres que derrubaran.
gan NON 0.003 [17] 0.5 0.999 afirmación sen apoio no dossier | A irmandade gañou a guerra e os señores nunca volveron.
rel NON 0.003 [17] 0.5 0.999 fala de persoas, nomes, tempo longo ou desenlace sen apoio n | A irmandade gañou a guerra e os señores nunca volveron.
gan OK  0.995 [8, 14] 0.75 0.953  | Para a xente, as torres eran refuxios de malfeitores.
rel OK  0.995 [8, 14] 0.75 0.953  | Para a xente, as torres eran refuxios de malfeitores.
gan NON 0.944 [15, 14] 0.4 0.878 afirmación sen apoio no dossier | Un exército de xente diversa derrubou castelos.
rel NON 0.944 [15, 14] 0.4 0.878 fala de persoas, nomes, tempo longo ou desenlace sen apoio n | Un exército de xente diversa derrubou castelos.
gan NON 0.003 [1, 10] 0.33 0.872 afirmación sen apoio no dossier | A chuvia caía mansa sobre as pedras dos camiños.
rel OK  0.003 [1, 10] 0.33 0.872  | A chuvia caía mansa sobre as pedras dos camiños.
gan NON 0.923 [17, 18] 0.67 0.927 quen fixo que non coincide co dossier (señores + derru) | Os señores regresaron co seu exército e derrubaron as fortalezas dos irmandiños.
rel NON 0.923 [17, 18] 0.67 0.927 quen fixo que non coincide co dossier (señores + derru) | Os señores regresaron co seu exército e derrubaron as fortalezas dos irmandiños.
gan NON 0.995 [18, 16] 1.0 0.924 quen fixo que non coincide co dossier (señores + recon) | Os señores reconstruíron as fortalezas.
rel NON 0.995 [18, 16] 1.0 0.924 quen fixo que non coincide co dossier (señores + recon) | Os señores reconstruíron as fortalezas.
gan OK  0.998 [18] 1.0 0.015  | Os vasalos tiveron que traballar anos para reconstruír as fortalezas derrubadas.
rel OK  0.998 [18] 1.0 0.015  | Os vasalos tiveron que traballar anos para reconstruír as fortalezas derrubadas.
gan NON 0.972 [18, 1] 0.43 0.304 quen fixo que non coincide co dossier (señores + casti); afi | Os señores non foron castigados con morte, pero os campesiños tiveron que pagar moito diñeiro.
rel NON 0.972 [18, 1] 0.43 0.304 quen fixo que non coincide co dossier (señores + casti); fal | Os señores non foron castigados con morte, pero os campesiños tiveron que pagar moito diñeiro.
=== guion ronda 2
0 NON 0.868 0.57 0.472 afirmación sen apoio no dossier | Os campesiños, mariñeiros e artesáns uníronse contra os señores das fortaleiras.
0 NON 0.944 0.29 0.907 afirmación sen apoio no dossier | A xente común botou abaixo torres con paus e pedras.
0 NON 0.923 0.2 0.239 desenlace que non está no dossier (venceu); afirma | Os nobres tiñan poder, pero a irmandade venceu.
0 NON 0.988 0.5 0.988 afirmación sen apoio no dossier | A Rocha Forte caeu baixo as súas mans.
0 NON 0.944 0.4 0.878 afirmación sen apoio no dossier | Un exército de xente diversa derrubou castelos.
0 NON 0.974 0.2 0.986 desenlace que non está no dossier (perderon); afir | As fortaleiras perderon fronte á unión popular.
1 NON 0.669 0.25 0.893 afirmación sen apoio no dossier | Isto é Serán, historia de Galicia para durmir.
1 NON 0.044 0.25 0.027 afirmación sen apoio no dossier | Esta noite viaxamos no tempo para descubrir unha historia esquecida de Galicia: a revolta 
1 NON 0.01 0.73 0.769 quen fixo que non coincide co dossier (señores + d | Xuntáronse labregos, artesáns, mariñeiros, burgueses, clérigos e parte da pequena nobreza 
2 OK  0.968 0.17 0.987  | Estás a punto de embarcarche nunha viaxe tranquila pola historia de Galicia.
2 NON 0.818 0.1 0.942 fala de persoas, nomes, tempo longo ou desenlace s | Acomódate, apaga as luces e deixa que o aire che acompañe mentres escoitas esta historia d
3 NON 0.181 0.47 0.368 quen fixo que non coincide co dossier (señores + d | Na primavera de mil catrocentos sesenta e sete, un grupo diverso de xente, labregos, artes
3 OK  0.007 0.38 0.629  | Botaron abaixo moitas fortalezas, aproveitando a chuvia e o vento que mollan as pedras.
3 OK  0.002 0.29 0.792  | A luz do sol rompe entre as ruínas, mentres o lume arde nos camiños abandonados.
4 NON 0.136 0.12 0.909 fala de persoas, nomes, tempo longo ou desenlace s | As pedras, molladas polo chuvia e o vento, caeron baixo as ferramentas dos irmandiños.
4 OK  0.341 0.0 0.516  | A luz do sol filtraba entre os escombros, iluminando camiños esquecidos onde o lume ardeu 
5 NON 0.706 0.0 0.795 fala de persoas, nomes, tempo longo ou desenlace s | Cando o ceo se fundía coas chairas, os homes labraban a terra con ferramentas de ferro e m
5 NON 0.004 0.14 0.054 fala de persoas, nomes, tempo longo ou desenlace s | Algunhas casas tiñan tellados de lousa ou palla, e os teitos goteaban lentamente sobre as 
6 NON 0.001 0.12 0.819 fala de persoas, nomes, tempo longo ou desenlace s | O vento arrastraba o cheiro a terra mollada entre as pedras, mentres os homes camiñaban xu
6 NON 0.019 0.3 0.794 fala de persoas, nomes, tempo longo ou desenlace s | As chaves da Rocha Forte caeron unha tras outra, e cada golpe soaba como se o tempo mesmo 
6 OK  0.025 0.25 0.292  | A auga goteaba das teituras rachadas, mesturándose coa area dos camiños, mentres as sombra
7 NON 0.008 0.32 0.64 quen fixo que non coincide co dossier (señores + x | Os labregos, con aixadas e picos, os artesáns coas súas ferramentas de ferro, os mariñeiro
7 NON 0.002 0.04 0.897 fala de persoas, nomes, tempo longo ou desenlace s | O vento arrastraba a chuvia polos camiños empedrados, mentres o lume das antorchas ilumina
=== feitos
OK   Desde a peste negra as rendas dos señores minguaban en toda 
OK   Arredor da metade do século quince, Galicia era unha socieda
OK   Os vasalos pagaban tributos en diñeiro e en especie e debían
OK   Moitas familias labregas vivían no limiar da pobreza.
OK   O señor era tamén xuíz no seu señorío.
OK   Desde había un século mandaba unha nobreza nova, máis violen
OK   Había fortalezas das grandes casas nobres, como Lemos ou And
OK   Os vasalos dicían que desde as fortalezas se facían os males
OK   Unhas décadas antes, os vasalos dun gran señor das Mariñas f
OK   Desde a Rocha Forte asegurábanse os camiños que ían cara a P
OK   A Rocha Forte era do arcebispo de Compostela.
OK   O alzamento irmandiño foi entre as primaveras de mil catroce
OK   Na irmandade xuntáronse labregos, artesáns, mariñeiros, burg
OK   Despois dun asalto, a xente da cidade e os labregos da comar
OK   Os irmandiños derrubaron moitas das fortalezas do reino (non
OK   En mil catrocentos sesenta e nove houbo unha reacción armada
OK   En mil catrocentos sesenta e nove os señores volveron coas s
OK   Despois da derrota o castigo non foron tanto as execucións c
OK   Só unha parte das fortalezas derrubadas se volveu levantar.
OK   Moito despois, entre mil cincocentos vinte e seis e mil cinc
OK   Ao sur de Compostela hai un outeiro con restos da fortaleza 
```
