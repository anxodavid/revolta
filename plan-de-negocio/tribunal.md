# Tribunal final del Gauntlet (29-09-2026)

Tres jueces con contexto limpio (inversor, filóloga gallega y operador de canales para dormir) sobre `plan-de-negocio.md` y el guion muestra. Entre rondas, un agente de alisado corrigió el plan con sus objeciones. Máximo: 3 rondas.

## Ronda 1: 0/3 aprueban

### Inversor: NO APRUEBA

§1.3 ("Ajustes de integración" y "Distribución integrada") y, arrastrado de ahí, §0.1 y el punto 1 de §0.2: falta un único árbol de probabilidades conjuntas que empiece en la voz y siga con la audiencia. Ramas: V-0 no (→ esperar, ~0-10 €) / V-0 sí → Puerta V pasa (Nós con doble permiso, o pago) / falla → vía (c) 700-1.250 € → pasa o falla → (b) 1.400-2.500 € o esperar. Después, P1-P4 con sus costes integrados. Hay que sacar de ese árbol:
- un EV a 36 meses de verdad (caja y horas);
- una tabla de resultados cuyas probabilidades sumen el 100 %;
- la probabilidad conjunta de acabar en caja positiva.

Y hay que corregir la fila optimista y los datos del resumen que dependen de ella: equilibrio mensual en M15, +3.355 € y "Solo el camino optimista (≈ 10 %)", que en realidad es un ≈ 10 % condicionado a que haya voz.

**Errores factuales señalados:**
- §1.3, Distribución integrada, fila 'Optimista': '+1.700 a +2.400 €' no descuenta el revisor profesional de la Etapa 2 en el camino P4. P4 paga 30 meses de Etapa 2 (caja del modelo 3.510 € = 6×35 + 30×110), y el propio §1.3 usa esos meses en los '5,8 meses esperados' del ajuste de −160 €. Con los mismos ajustes que se aplican a P3: 3.355 − 70 − 32 − 30×28 (≈ 840) − 850/1.500 ≈ +1.560 a +910 €, no +1.700 a +2.400 €.
- §0.1, fila Etapa 2: 'equilibrio mensual en M15' y '+3.355 € acumulados en M36' son cifras del modelo con caja de 110 €/mes. Con la caja integrada de ≈ 138 €/mes (§5.4) el ingreso de M15 (~120 €, interpolado entre 66 € en M12 y 173 € en M18) no la cubre: el equilibrio mensual pasa a ~M16-M17 y el acumulado es el de la corrección anterior.
- §1.3: el 'Total integrado ≈ −1.250 a −1.900 €' y la tabla de distribución no son un valor esperado conjunto. Aplican la validación de 850-1.500 € a todos los caminos y ponderan con probabilidades condicionadas a que haya voz (61,8/11,1/17,0/10,2 %), mientras la fila 'Ninguna voz pasa' lleva un 60-80 % de otro árbol. Las probabilidades de la tabla no suman el 100 %.
- §1.2, §6.2, §8.1 y §8.6: el Día Mundial do Sono 2027 no es el 14-03. Se celebra el viernes anterior al equinoccio de marzo (13-03-2026; en 2027 el equinoccio cae el sábado 20-03, así que el día es el viernes 19-03-2027). El 14-03 solo vale como domingo cercano y debería decirse así.
- §1.2 y §8.1: con cadencia quincenal desde el 31-01-2027, los domingos que tocan son 14-02, 28-02, 14-03, 28-03, 11-04, 25-04, 09-05 y 23-05. El vídeo 12 el 16-05 rompe la cadencia declarada: una semana después del 09-05, o bien el vídeo 11 no cae en fecha de cadencia.
- Horas: el modelo usa 35 h/mes en la Etapa 2 (A15-17), pero §5.4 calcula 4 × 7,1-8,8 h + ~9 h de comunidad ≈ 37-44 h/mes (8,5-10 h/semana). Las '~400 h' del EV integrado infravaloran las horas de los caminos P2-P4.

### Filóloga gallega: NO APRUEBA

§4.7 (Guion en galego: calidade e veracidade) e §5.4 (Caixa mensual e horas). Pasado o panel E2 da P0, a garantía lingüística e histórica depende de persoas sen cualificación acreditada, e a revisión histórica non está orzamentada.

1) O texto do guion revísano só o promotor e a súa muller, xunto con ferramentas automáticas e un LLM. O revisor profesional dos episodios 1-6 aparece na §4.6 como escoita do audio, e non queda claro se revisa o texto. Nos episodios 7-12 da Etapa 1 a revisión profesional é de 0 €.

2) A revisión histórica é "como mínimo 1 de cada 4 episodios", polo que 3 de cada 4 episodios saen sen historiador. Os 50-150 € por episodio que custa non aparecen na táboa de caixa da §5.4: o total da Etapa 1, de 18-24 €, non os inclúe. Con 2 episodios ao mes serían 25-300 €/mes, o que rompe o límite de 50 €/mes.

3) O aviso falado ("o texto revisárono persoas galegofalantes") apóiase nese sistema. Ser galegofalante non é unha cualificación.

Acción: definir un rol de revisor lingüístico cualificado (filólogo ou corrector acreditado) sobre o TEXTO de cada episodio, ou polo menos por mostraxe cun criterio de aceptación explícito. Definir tamén unha revisión histórica cualificada do 100 % das afirmacións de feito, ou unha regra clara de que temas a esixen. Meter as dúas nas §1.3 e §5.4 e recalcular a caixa e o valor esperado. Se non cabe no límite de 50 €/mes, dicilo e decidir: menos episodios ou un límite máis alto, en lugar de rebaixar a garantía.

**Errores factuales señalados:**
- §3.7: "Serán [F, Dicionario da RAG: 'reunión nocturna… para contar']" é unha cita falsa. O DRAG di, na acepción 2, "Reunión de mulleres para fiar que se facía destas horas" e, na acepción 3, "Reunión nocturna de carácter festivo". En ningunha acepción aparece "para contar" (https://academia.gal/dicionario/-/termo/busca/serán).
- §1.2, §6.2 e §8.6: o Día Mundial do Sono 2027 non é o 14-03. Celébrase o venres anterior ao equinoccio de primavera, que en 2027 é o 19-03-2027. O especial pódese manter no domingo, pero sen presentar esa data como o Día Mundial.
- §3.5, regra 14: "Podes usar o temporizador de apagado de YouTube" é un castelanismo. No DRAG, "apagado" é participio ou adxectivo; como substantivo existe "apagada" (corte de luz), e o substantivo de acción é "apagamento". Debe dicir "temporizador de apagamento", ou empregar a etiqueta oficial da interface galega de YouTube.
- Guion mostra, último parágrafo narrado: "polo de agora" non figura no DRAG (a locución rexistrada é "por agora"). Mellor "polo momento" ou "por agora" (dubidoso, pero evitable).
- Convencións de evidencia: a etiqueta [COMP] úsase nas §3.7, §6.3 e §6.5, pero non está definida.
- §4.5 e guion: o aviso "o texto revisárono persoas galegofalantes" é vago e pode enganar. Ser galegofalante non é unha cualificación, e nos episodios 7 en diante da Etapa 1 a revisión recae só no promotor e na súa muller.

### Operador de canales para dormir: NO APRUEBA

Hay que reescribir el guion muestra (guion-mostra-revolta-irmandina.md, "Texto narrado") para que cumpla las densidades del §3.2 (tabla "Minutado del episodio tipo") y del §3.5 del plan. Hoy las incumple con claridad:
- **Entrada suave (0:15-2:30):** 1 sola fecha y ≤2 nombres propios. Hoy hay 3 años y 6 o más nombres, y la apertura es un asalto.
- **Acto I:** ≤3 nombres nuevos por minuto, fechas redondeadas y sin cifras largas. Hoy hay ~3,5 nombres por minuto y 8 años escritos completos, más "cento vinte e oito" y "seis de xullo".

Cómo hacerlo:
- Redondear o eliminar los años y dejar como mucho 2-3 hitos temporales.
- Quitar la cadena Ávila, Fuensalida y Medina, o reducirla a una frase.
- Abrir con el lugar en calma y dejar el derribo como "final ya anticipado" y suave.
- Adjuntar al final la auditoría automática (nombres por minuto, fechas y cifras por bloque, activación 1-5 por párrafo) para demostrar que el auditor del pipeline lo aprobaría.

Alternativa: declarar explícitamente la muestra como excepción y añadir una muestra del Ep. 1 (Reino suevo, Acto II) que sí cumpla las reglas.

**Errores factuales señalados:**
- El §1.2, §6.2, §8.1 y §8.6 sitúan el Día Mundial do Sono 2027 el 14-03-2027. Es el viernes anterior al equinoccio de marzo, es decir, el 19-03-2027 (el equinoccio es el 20-03-2027); el 14-03 es domingo. El propio plan cita days.to/world-sleep-day/2027 y Wikipedia. Si se quiere mantener la publicación en domingo, habría que decir 'el domingo anterior (14-03)' o moverlo al 21-03.
- El guion muestra incumple las propias reglas de densidad del plan (§3.2: 1 fecha y 2 nombres en la entrada; fechas redondeadas y sin números largos en el Acto I), aunque el §4.7 lo presenta como conforme. Es una inconsistencia interna, no un error externo.

## Ronda 2: 1/3 aprueban

### Inversor: NO APRUEBA

§0.2 (y §1.3/§9): la recomendación no tiene una puerta que dé valor a lo que se compra. El plan demuestra que ningún camino recupera caja con la garantía de calidad. Aun así, tras una V-0 positiva, manda gastar ≈ 2.700-3.400 € (validación de voz + RLC/RHC de 12 episodios) bajo una política ('parar siempre en P1') que hace que la P1 no decida nada, y la llama 'la que minimiza la pérdida', cuando en su propio árbol no gastar tras la V-0 da ≈ −40 €.

Arreglo accionable: añadir entre la V-0 y la D1 una 'Puerta F (financiación de la calidad)'. Antes de pagar la validación formal y el paquete de calidad, se exige un compromiso de terceros que cubra al menos el diferencial de calidad (≈ 1.550 € en la E1 y ≈ 440 €/mes en la E2). Fuentes posibles:
- servicios de normalización de concellos, cuya línea PL400A de la SXL financia a entidades locales acciones de dinamización en galego en formato digital y audiolibros;
- mecenas y membresías fundadoras o preventa (Patreon/Ko-fi, sin umbral);
- patrocinio identitario prevendido;
- un convenio con Nós/USC o con la AGPTI que cofinancie la revisión.

Hay que recalcular el árbol del §1.3 con esa puerta, dar el umbral que hace positiva alguna hoja y fijar un 'presupuesto de hobby' explícito si la Puerta F falla. Así la P1 vuelve a decidir algo y el plan deja de pedir dinero para comprar datos que no usará.

**Errores factuales señalados:**
- §0.1 y §1.3: 'Política que minimiza la pérdida: publicar los 12 vídeos y parar en la P1' (≈ −1.715 €) es falso dentro del propio árbol. No gastar tras la V-0 (hoja A, ≈ −40 €) o no seguir tras ella pierde mucho menos; como mucho es la política menos mala entre las que publican.
- §1.1 frente a §1.6: la rama base en la P1 figura con 24 suscriptores en el §1.1 y con 25 en el §1.6 (M6); en la P2, con 107 en el §1.1 y con 108 en el §1.6 (M12).
- §0.1 y §5.4 frente a §1.1: el coste mensual de la E1 (≈ 160-400 €/mes, central 290) reparte los 1.550 € en 6 meses (dic-may), pero el §1.1 define la Etapa 1 como ene-may (M2-M6). Con 5 meses, el central sería ≈ 345 €/mes.
- §5.4: la escucha completa con texto de los episodios 1-6 (≈ 9-15 h de RLC a 20-35 €/h) se da por incluida 'dentro de la excepción de voz'. Pero el revisor de 250-500 € del §4.4 está presupuestado para el protocolo de la Puerta V, así que el coste de la E1 queda probablemente infravalorado en ≈ 200-500 €.
- §4.6: 'Etapa 2: muestreo de aceptación (40 bloques de 2 min)' frente a 'cada muestreo de la Etapa 2 (20 bloques)' en el mismo apartado y en el §4.7, sin aclarar que son dos muestreos distintos (audio del promotor frente a texto del RLC).

### Filóloga gallega: NO APRUEBA

§5.4 (fila "RLC" da táboa de caixa), §4.6 (viñeta "RLC pagado") e §4.7 (RLC, "Episodios 1-6"). A "revisión íntegra" que o aviso falado promete nos episodios 1-6 non é unha corrección de mesa nin está orzamentada:
- Faise ao ritmo da escoita, co texto na man.
- Cárgase á excepción de voz, cuxo revisor de 250-500 € é para o panel da Puerta V e que non existe nos camiños V-0 non ou vía (b).
- Engade só ~0,4 h (8-14 €) de traballo de texto para ~8.400 palabras.

Acción:
- Definir unha corrección de mesa do 100 % do texto de cada episodio 1-6 antes do render TTS, a 0,015-0,025 €/palabra (≈ 126-210 € por episodio, ≈ +750-1.260 € na Etapa 1), e manter despois a escoita co texto.
- Recalcular D5, §0.1, §1.3 e §5.4.
- Xustificar ou endurecer a tolerancia da mostraxe dos episodios 7 e seguintes (≤ 1/1.000 sobre 1/3 do texto). Por exemplo: lectura de mesa íntegra por defecto, e inspección reducida só tras 8-10 episodios limpos.

**Errores factuales señalados:**
- §5.4, táboa Caixa mensual, fila RLC, e §4.6: "Ep. 1-6: la escucha completa va dentro de la excepción de voz". A excepción (§4.4) orzamenta un revisor de 250-500 € para o panel da Puerta V, non para escoitar seis episodios de 75 min (≈ 10-16 h). Ademais, a excepción só existe se V-0 dá sinal. A revisión íntegra dos episodios 1-6 queda sen orzamento, e ~0,4 h de texto para ~8.400 palabras non é unha revisión íntegra real, polo que o aviso falado promete máis do que hai.
- §3.3 (regra de decisión de G0) e §4.4 (criterio de V-0): "durmiríame con isto" usa "durmir" como pronominal. O DRAG só recolle usos intransitivo e transitivo (https://academia.gal/dicionario/-/termo/busca/durmir). Correcto: "durmiría con isto" ou "quedaría durmido con isto".
- Guion mostra, Acto I, "Outros non, e co tempo marcharon cara a Castela": incompleto. Parte dos señores refuxiouse en Portugal (p. ex. Pedro Álvarez de Soutomaior), e de alí veu parte da reacción de 1469. Mellor "cara a Castela e Portugal".
- Guion mostra, último parágrafo: "a súa obra ía durar pouco máis de dous anos", dito desde "aquel verán" de 1467, non cadra coa propia fonte ([B-2024], "entre as primaveras de 1467 e 1469"). Desde o verán de 1467 son menos de dous anos. Mellor "uns dous anos" ou "ata dúas primaveras despois".
- Guion mostra, Acto I: "en todas partes" é dubidoso, porque en galego "todo" leva artigo. Recomendo "en todas as partes" ou "por todas as partes" (non o verifiquei na RAG).

### Operador de canales para dormir: APRUEBA (lo que falta es menor)

La mayor carencia está en el §3.2 (duración de la Etapa 1), el §8.3 y el §8.5 (E11 pasa a la Etapa 2) y el §8.2 (la P1 para "sin prórroga").

La Etapa 2 no se abre por defecto (D5). Por tanto, la única prueba real del canal son 12 episodios de 75 min, más 20-30 min de cola, publicados cada dos semanas. Los líderes del género publican 2-3 h. Si la P1 falla, no se sabrá si ha fallado el galego o la duración, y el experimento de duración (E11) no llegará a hacerse nunca.

Propuesta, con cambios en §3.2, §5.4 y §8.5:
- **Duración:** ampliar la cola de ambiente, que es barata (hasta alcanzar un total de ≥ 2 h en pantalla), o hacer 3-4 de los 12 vídeos de 2 h narradas. La mayoría de los costes de revisión son por episodio o se hacen por muestreo.
- **Métrica:** registrar el CTR y el AVD por duración como diagnóstico, para que un NO-GO en la P1 no se confunda con un fallo de formato.
- **Otros ajustes:**
  - pasar la plantilla de miniatura (drafts/formato.md §7.3) al §3.6;
  - explicitar en el §2.1 o el §3.6 que en el móvil, sin Premium, la reproducción se corta con la pantalla bloqueada;
  - anotar en R7 (§7.1) la diferencia de sonoridad entre los anuncios y el contenido a −16 LUFS.

## Ronda 3: 1/3 aprueban

### Inversor: NO APRUEBA (lo que falta es menor)

§1.3, tabla "Qué suma cada hoja que publica" (y, en cascada, §0.1 fila Etapa 2 y lista de resultados, §1.3 "Lectura", §8.2 filas P2 y P3). La Puerta F2 exige terceros con ≥ 440 €/mes solo durante "al menos 6 meses" (§0.2, §1.3 y §8.2). Sin embargo, la fila "Resultado con las Puertas F y F2" da por hecho que esos terceros pagan el diferencial de la E2 durante 12 meses en P3 (5.305 €) y durante 30 meses en P4 (13.260 €). Ni la P2 ni la P3 del §8.2 exigen renovar la F2.

Con la cobertura que la puerta realmente exige (6 meses), el P4 con voz de pago queda en ≈ 2.105 − 24 × 442 ≈ −8.500 € y el P3 en ≈ −5.430 €. Así, la probabilidad de caja positiva pasa del 0,3 % a ≈ 0 %.

Además, las fuentes que el plan asigna a la F2 (patrocinio y membresías, §8.6 M5) son las mismas líneas A12-A14 que el modelo ya cuenta como ingreso: suman el 83 % de los 509 €/mes del P4 en M36. Hay, por tanto, un riesgo de doble conteo.

Cómo arreglarlo:
- añadir a la P2 y a la P3 (§8.2 y §1.1) la condición "F2 renovada hasta M36", o recalcular P3 y P4 con 6 meses de cobertura;
- restar de A12-A14 lo que venga de patrocinio o membresías y se destine a la F2;
- propagar el resultado al §0.1 y al §0.2.

**Errores factuales señalados:**
- §0.1 vs §1.3: el resumen da '≈ +1.190 €' para el optimista con F y F2, mientras el §1.3 da +1.185 € (discrepancia menor de redondeo).
- §0.1, fila Etapa 2: 'P4: 10,2 % de los caminos que publican' es la probabilidad del modelo sin F2. Con la política recomendada, P4 es 0,41/10,0 ≈ 4,1 % de los caminos que publican.
- §0.1, fila Etapa 2: los '≈ −15.750 €' si el promotor paga la garantía son una media ponderada por vías de voz que no aparece en el §1.3 (allí la hoja con voz de pago es −14.835 €) y no se etiqueta como tal.
- §1.3, filas P3/P4 'con las Puertas F y F2': suponen 12 y 30 meses de pago de terceros, mientras la F2 definida en §0.2, §1.3 y §8.2 solo exige 6 meses (incoherencia interna, no error de fuente).
- Verificado sin errores: regla del YPP de 8.000 h desde el 1-02-2027 (blog.youtube, support.google.com/youtube/answer/12843009), Spotify Partner Program en España desde el 20-10-2026 (Infobae, 25-09-2026) y PL400A del DOG n.º 63 del 7-04-2026 (350.000 €, ≥ 3.000 hab., ejecución del 1-01 al 15-10-2026).

### Filóloga gallega: NO APRUEBA

§4.5 (aviso falado, punto 5), §6.6 (Transparencia sobre a IA) e §3.6 ("Nota sobre o proceso"), e con eles a entrada do guion mostra: ningún texto para o público di que o GUION está redactado por un modelo de linguaxe.

O aviso falado só declara a voz sintética e engade "O texto revisouno enteiro un corrector profesional". Isto suxire autoría humana. Ademais, "a IA non aparece en títulos nin miniaturas", e a "Nota sobre o proceso" e a páxina "Como facemos Serán" non teñen redacción.

Accións:
1. Cambiar as dúas variantes do aviso para que digan explicitamente que o texto se redactou con IA. Exemplo: "A voz que vas escoitar é sintética, e o texto redactouse con axuda de intelixencia artificial. Revisouno enteiro un corrector profesional de lingua galega e comprobou os datos un historiador." Aplicalo tamén ao guion mostra e á auditoría dos 30 s.
2. Redactar en galego, dentro do plan, a "Nota sobre o proceso" fixa da descrición e o texto de "Como facemos Serán". Deben dicir que fai cada modelo (guion, voz, imaxes) e que fai cada persoa, co nome do RLC e do RHC. Que os revise o RLC.
3. Aliñar o §7.3 (exención do art. 50.4): aínda que a exención se aplique, o plan declara igual que o texto é xerado con IA.

**Errores factuales señalados:**
- §3.2, promesa da canle en galego: "Cada noite, un serán" promete un episodio diario, pero a cadencia do plan é de domingo ás 21:30, quincenal ou semanal (§6.5, §8.1), e o propio plan prohibe a cadencia diaria (§5.5). Ademais, a mesma promesa no §0.3 xa non leva esa frase, e iso é unha incoherencia interna. Hai que quitala ou cambiala por algo como "Cada domingo, un serán".
- §4.5, §6.6 e §7.3: o aviso falado e os compromisos públicos presentan como IA só a voz e omiten que o guion o redacta un LLM (§5.1). O texto "O texto revisouno enteiro un corrector profesional" pode inducir a crer que é de autoría humana.
- Guion mostra, Pendentes: o cinturón automático (Hunspell-gl, LanguageTool-gl) non se pasou sobre a propia mostra, a pesar de que o §4.7 o presenta como control sistemático. Non é un erro de lingua, pero a mostra non demostra o proceso que declara.
- Guion mostra, Acto I (dúbida, non confirmada): "seguía o seu curso, coma sempre". No uso modal de "como sempre" a forma habitual é "como"; "coma" resérvase para a comparación de igualdade. Que o confirme o RLC.

### Operador de canales para dormir: APRUEBA (lo que falta es menor)

§8.3 (K5) and §6.4/§8.5 (E13, Test & Compare). K5 counts "navegación" (Browse features) as habit traffic. For a small channel, Browse is mostly Home recommendations, which is algorithmic acquisition, not habit. That can inflate the habit reading that decides the type of GO at P1 (§8.4). Fix: define K5 as Subscriptions feed + own playlists + channel page + returning viewers, and leave Home as an acquisition metric. Also correct §6.4: Test & Compare does work on premiered videos once the premiere ends and the video turns into a normal long-form video (it is only blocked while the premiere is active). So choosing to premiere does not block thumbnail and title testing, and E13 should not be justified by that.

**Errores factuales señalados:**
- §6.4: 'Test & Compare... no sirve para vídeos publicados como estrea'. That is inaccurate. YouTube only excludes 'active Premieres'. Once the premiere ends and the video becomes a long-form video, it can be tested (YouTube Help, Test & compare thumbnails: https://support.google.com/youtube/answer/13861714).
