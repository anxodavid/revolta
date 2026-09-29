# Tribunal final del Gauntlet: ronda 1 (29-09-2026)

Veredictos de los tres jueces (inversor, filóloga gallega y operador de canales para dormir) sobre `plan-de-negocio.md` y el guion muestra. El alisado posterior no llegó a completarse.

## Inversor: NO APRUEBA

**Mayor carencia:** §1.3 ("Ajustes de integración" y "Distribución integrada") y, arrastrado de ahí, §0.1 y el punto 1 de §0.2: falta un único árbol de probabilidades conjuntas que empiece en la voz y siga con la audiencia. Ramas: V-0 no (→ esperar, ~0-10 €) / V-0 sí → Puerta V pasa (Nós con doble permiso, o pago) / falla → vía (c) 700-1.250 € → pasa o falla → (b) 1.400-2.500 € o esperar. Después, P1-P4 con sus costes integrados. Hay que sacar de ese árbol:
- un EV a 36 meses de verdad (caja y horas);
- una tabla de resultados cuyas probabilidades sumen el 100 %;
- la probabilidad conjunta de acabar en caja positiva.

Y hay que corregir la fila optimista y los datos del resumen que dependen de ella: equilibrio mensual en M15, +3.355 € y "Solo el camino optimista (≈ 10 %)", que en realidad es un ≈ 10 % condicionado a que haya voz.

**Errores factuales:**
- §1.3, Distribución integrada, fila 'Optimista': '+1.700 a +2.400 €' no descuenta el revisor profesional de la Etapa 2 en el camino P4. P4 paga 30 meses de Etapa 2 (caja del modelo 3.510 € = 6×35 + 30×110), y el propio §1.3 usa esos meses en los '5,8 meses esperados' del ajuste de −160 €. Con los mismos ajustes que se aplican a P3: 3.355 − 70 − 32 − 30×28 (≈ 840) − 850/1.500 ≈ +1.560 a +910 €, no +1.700 a +2.400 €.
- §0.1, fila Etapa 2: 'equilibrio mensual en M15' y '+3.355 € acumulados en M36' son cifras del modelo con caja de 110 €/mes. Con la caja integrada de ≈ 138 €/mes (§5.4) el ingreso de M15 (~120 €, interpolado entre 66 € en M12 y 173 € en M18) no la cubre: el equilibrio mensual pasa a ~M16-M17 y el acumulado es el de la corrección anterior.
- §1.3: el 'Total integrado ≈ −1.250 a −1.900 €' y la tabla de distribución no son un valor esperado conjunto. Aplican la validación de 850-1.500 € a todos los caminos y ponderan con probabilidades condicionadas a que haya voz (61,8/11,1/17,0/10,2 %), mientras la fila 'Ninguna voz pasa' lleva un 60-80 % de otro árbol. Las probabilidades de la tabla no suman el 100 %.
- §1.2, §6.2, §8.1 y §8.6: el Día Mundial do Sono 2027 no es el 14-03. Se celebra el viernes anterior al equinoccio de marzo (13-03-2026; en 2027 el equinoccio cae el sábado 20-03, así que el día es el viernes 19-03-2027). El 14-03 solo vale como domingo cercano y debería decirse así.
- §1.2 y §8.1: con cadencia quincenal desde el 31-01-2027, los domingos que tocan son 14-02, 28-02, 14-03, 28-03, 11-04, 25-04, 09-05 y 23-05. El vídeo 12 el 16-05 rompe la cadencia declarada: una semana después del 09-05, o bien el vídeo 11 no cae en fecha de cadencia.
- Horas: el modelo usa 35 h/mes en la Etapa 2 (A15-17), pero §5.4 calcula 4 × 7,1-8,8 h + ~9 h de comunidad ≈ 37-44 h/mes (8,5-10 h/semana). Las '~400 h' del EV integrado infravaloran las horas de los caminos P2-P4.

**Razonamiento:** Como business angel escéptico: es de los planes de creador más honestos que he leído. Dice NO-GO como negocio y GO solo como hobby con opción. Pone delante una puerta barata (V-0, ~0-10 €), fija umbrales numéricos idénticos entre §1.1 y §8.2 y declara lo que no demuestra (A.4). Casi toda la aritmética de §1 cuadra al recalcularla:
- ramas 61,8/11,1/17,0/10,2 %;
- EV del modelo −147 € (−194 + 47);
- ingresos 711 € y caja 905 €;
- E3 −2.250 € y ~250 €/mes;
- oferta al locutor ≈ 170 €;
- filas P1, P2 y P3 de la distribución integrada;
- vídeos 12/36/60/78/132;
- mapeo M1 = dic 2026 → P1 mayo 2027, P2 nov 2027, P3 mayo 2028, M36 nov 2029.

Comprobé en la web: el cambio del YPP a 8.000 h desde el 1-02-2027 es real (blog.youtube), las Letras 2027 son para Neira Vilas (academia.gal) y el SPP llega a España el 20-10-2026 (Infobae). El guion muestra es de calidad, con fuentes trazadas a Barros y correcciones de anacronismos aplicadas.

Aun así no pondría dinero con este documento, por dos motivos:

1. **El titular de retornos no es un valor esperado.** El "valor esperado integrado a 36 meses ≈ −1.250 a −1.900 €" (§0.1, §1.3) carga la validación de voz (850-1.500 €) a todos los caminos. Luego pondera con probabilidades condicionadas a que la voz pase y ya está publicando. Pero el propio plan dice que hay un 60-80 % de probabilidad de que ninguna voz pase (§4.1, R1). La tabla de distribución integrada mezcla probabilidades de árboles distintos: "60-80 %" de voces de fábrica y "62 % de los caminos que publican". Esas filas no suman 100 % y no son conjuntas. No ponderan V-0 no / V-0 sí / Puerta V falla / vía (c) / vía (b) con su coste (700-1.250 € o 1.400-2.500 €) ni la rama "esperar". Un inversor no puede sacar de ahí la pérdida esperada real ni la probabilidad conjunta de acabar en caja positiva.
2. **El único escenario positivo está inflado.** La fila optimista (+1.700 a +2.400 €) no descuenta el revisor profesional de 30 meses de Etapa 2 (≈ −840 €). Ese coste sí se usa para calcular el −160 € del EV (5,8 meses esperados) y sí se aplica a la fila base P3. Además, el resumen ejecutivo sigue dando el equilibrio mensual en M15 y los +3.355 € del modelo sin integrar, con una caja de 110 € en vez de 138 €.

Para retornos que tienen que ser "creíbles y trazables" con "coherencia interna total", esto no alcanza el listón.

## Filóloga gallega: NO APRUEBA

**Mayor carencia:** §4.7 (Guion en galego: calidade e veracidade) e §5.4 (Caixa mensual e horas). Pasado o panel E2 da P0, a garantía lingüística e histórica depende de persoas sen cualificación acreditada, e a revisión histórica non está orzamentada.

1) O texto do guion revísano só o promotor e a súa muller, xunto con ferramentas automáticas e un LLM. O revisor profesional dos episodios 1-6 aparece na §4.6 como escoita do audio, e non queda claro se revisa o texto. Nos episodios 7-12 da Etapa 1 a revisión profesional é de 0 €.

2) A revisión histórica é "como mínimo 1 de cada 4 episodios", polo que 3 de cada 4 episodios saen sen historiador. Os 50-150 € por episodio que custa non aparecen na táboa de caixa da §5.4: o total da Etapa 1, de 18-24 €, non os inclúe. Con 2 episodios ao mes serían 25-300 €/mes, o que rompe o límite de 50 €/mes.

3) O aviso falado ("o texto revisárono persoas galegofalantes") apóiase nese sistema. Ser galegofalante non é unha cualificación.

Acción: definir un rol de revisor lingüístico cualificado (filólogo ou corrector acreditado) sobre o TEXTO de cada episodio, ou polo menos por mostraxe cun criterio de aceptación explícito. Definir tamén unha revisión histórica cualificada do 100 % das afirmacións de feito, ou unha regra clara de que temas a esixen. Meter as dúas nas §1.3 e §5.4 e recalcular a caixa e o valor esperado. Se non cabe no límite de 50 €/mes, dicilo e decidir: menos episodios ou un límite máis alto, en lugar de rebaixar a garantía.

**Errores factuales:**
- §3.7: "Serán [F, Dicionario da RAG: 'reunión nocturna… para contar']" é unha cita falsa. O DRAG di, na acepción 2, "Reunión de mulleres para fiar que se facía destas horas" e, na acepción 3, "Reunión nocturna de carácter festivo". En ningunha acepción aparece "para contar" (https://academia.gal/dicionario/-/termo/busca/serán).
- §1.2, §6.2 e §8.6: o Día Mundial do Sono 2027 non é o 14-03. Celébrase o venres anterior ao equinoccio de primavera, que en 2027 é o 19-03-2027. O especial pódese manter no domingo, pero sen presentar esa data como o Día Mundial.
- §3.5, regra 14: "Podes usar o temporizador de apagado de YouTube" é un castelanismo. No DRAG, "apagado" é participio ou adxectivo; como substantivo existe "apagada" (corte de luz), e o substantivo de acción é "apagamento". Debe dicir "temporizador de apagamento", ou empregar a etiqueta oficial da interface galega de YouTube.
- Guion mostra, último parágrafo narrado: "polo de agora" non figura no DRAG (a locución rexistrada é "por agora"). Mellor "polo momento" ou "por agora" (dubidoso, pero evitable).
- Convencións de evidencia: a etiqueta [COMP] úsase nas §3.7, §6.3 e §6.5, pero non está definida.
- §4.5 e guion: o aviso "o texto revisárono persoas galegofalantes" é vago e pode enganar. Ser galegofalante non é unha cualificación, e nos episodios 7 en diante da Etapa 1 a revisión recae só no promotor e na súa muller.

**Razonamiento:** Leín o contexto, o plan enteiro (con máis detalle nas §3-§9 e nos anexos) e o guion mostra. Comprobei os datos dubidosos no DRAG en liña e na web.

Guion mostra: é de moi boa calidade. O galego é sólido. Os pronomes átonos están ben colocados, tanto en énclise ("cercárona", "Uníronselles", "pedíuselles") como en próclise tras "non", tras relativo e con "con te deixares". O infinitivo conxugado e o pluscuamperfecto sintético están ben empregados, e o léxico é xenuíno e sen hiperenxebrismos. O rigor histórico tamén é serio: cada dato ten fonte en Barros, retiráronse os datos que só se apoiaban na Galipedia, corrixiuse o anacronismo de Pulgar e a asistencia a Melide cóntase como memoria dun testemuño. Comprobei a idade de Afonso (11 anos en xuño de 1465) e está ben. Só atopo un punto lingüístico: "polo de agora", que non figura no DRAG.

O plan tamén é serio en transparencia. Ten aviso falado nos primeiros 30 s, dobre permiso da voz, páxina de erratas, diálogo con ADA e AGPTI e unha norma que prohibe publicar coa voz "menos mala". Tamén comprobei que as Letras 2027 son para Neira Vilas e que "présa" leva acento diacrítico no DRAG: os dous datos están ben.

Aínda así, non me convence que o plan garanta a calidade lingüística e histórica episodio a episodio, que é o listón que se lle pide. Ademais, a propia xustificación do nome no DRAG está mal citada, o cal debilita a credibilidade do rigor que o plan di ter (detalle na lista de erros). E hai dous textos para o público con defectos: un castelanismo na liña fixa da descrición e unha data errada do Día Mundial do Sono.

## Operador de canales para dormir: NO APRUEBA

**Mayor carencia:** Hay que reescribir el guion muestra (guion-mostra-revolta-irmandina.md, "Texto narrado") para que cumpla las densidades del §3.2 (tabla "Minutado del episodio tipo") y del §3.5 del plan. Hoy las incumple con claridad:
- **Entrada suave (0:15-2:30):** 1 sola fecha y ≤2 nombres propios. Hoy hay 3 años y 6 o más nombres, y la apertura es un asalto.
- **Acto I:** ≤3 nombres nuevos por minuto, fechas redondeadas y sin cifras largas. Hoy hay ~3,5 nombres por minuto y 8 años escritos completos, más "cento vinte e oito" y "seis de xullo".

Cómo hacerlo:
- Redondear o eliminar los años y dejar como mucho 2-3 hitos temporales.
- Quitar la cadena Ávila, Fuensalida y Medina, o reducirla a una frase.
- Abrir con el lugar en calma y dejar el derribo como "final ya anticipado" y suave.
- Adjuntar al final la auditoría automática (nombres por minuto, fechas y cifras por bloque, activación 1-5 por párrafo) para demostrar que el auditor del pipeline lo aprobaría.

Alternativa: declarar explícitamente la muestra como excepción y añadir una muestra del Ep. 1 (Reino suevo, Acto II) que sí cumpla las reglas.

**Errores factuales:**
- El §1.2, §6.2, §8.1 y §8.6 sitúan el Día Mundial do Sono 2027 el 14-03-2027. Es el viernes anterior al equinoccio de marzo, es decir, el 19-03-2027 (el equinoccio es el 20-03-2027); el 14-03 es domingo. El propio plan cita days.to/world-sleep-day/2027 y Wikipedia. Si se quiere mantener la publicación en domingo, habría que decir 'el domingo anterior (14-03)' o moverlo al 21-03.
- El guion muestra incumple las propias reglas de densidad del plan (§3.2: 1 fecha y 2 nombres en la entrada; fechas redondeadas y sin números largos en el Acto I), aunque el §4.7 lo presenta como conforme. Es una inconsistencia interna, no un error externo.

**Razonamiento:** Evaluado como operador de canales de historia para dormir. El plan (/home/user/revolta/plan-de-negocio/plan-de-negocio.md) es de lo más sólido que he visto para un canal de nicho. Acierta en casi todo lo que decide si un canal de sueño funciona en YouTube. Tiene un veredicto económico honesto: NO-GO como negocio y GO como hobby con opción, porque la publicidad no paga en galego y lo que mueve la aguja es el patrocinio y las membresías. Tiene en cuenta que YouTube puede poner anuncios fuera del YPP (Términos de servicio), así que retira el "sen cortes" en la Etapa 1. Los mid-rolls solo van en los primeros 20 min, con una cola de ambiente de colchón para el post-roll. Incluye temporizador, −16 LUFS y control de picos, pantalla final muda y luminancia baja. Recoge los umbrales del YPP 2027 (8.000 h cualificadas desde el 1-02-2027) y la aclaración sobre contenido inauténtico del 16-07-2026 (verificados), con 12 controles anti-plantilla, cadencia nunca diaria y compilaciones fuera del canal principal. Para el descubrimiento plantea adyacencia a vídeos semilla en castellano, estrenos con ritual fijo, SEO bilingüe y dependencia del hábito (K4 y K5). Las puertas se basan en tasas base de canales clónicos, con regla de tamaño mínimo para las pruebas A/B. Declara lo que falta (la prueba de escucha larga R3-L y el volumen de búsqueda en galego).

Lo que no me convence es la pieza que demuestra el producto. El guion muestra (/home/user/revolta/plan-de-negocio/guion-mostra-revolta-irmandina.md) no cumple las reglas de sueño del propio plan. Un auditor QA con los umbrales del §3.2 lo rechazaría:
- **Entrada suave (0:15-2:30):** el límite es 1 fecha y 2 nombres propios. El guion mete 1467 y 1467-1469 (3 menciones de año) y nombra Conxo, Compostela, Rocha Forte, Santiago, irmandiños y Santa Irmandade, entre otros. Además abre con un asalto ("cercárona, asaltárona e derrubárona").
- **Acto I:** el límite es de ≤3 nombres propios nuevos por minuto, con fechas redondeadas y sin números largos. En ~1.180 palabras (~10 min a 115 palabras/min) hay unas 35 entidades nombradas (~3,5 por minuto). Hay 8 años escritos completos ("mil catrocentos cincuenta e catro e mil catrocentos cincuenta e oito", 1431, 1450, 1465, 1466…). También aparecen "cento vinte e oito deputados", "seis de xullo" y una cadena de juntas (Fuensalida, Medina del Campo, Ávila, Melide).

Se lee como una clase de historia rigurosa, no como una historia para dormir. Es justo el fallo típico que hunde la retención nocturna en este género: el oyente se engancha a seguir los datos y no se duerme. Como es la única prueba tangible del registro y además es el episodio de "tema caliente", debilita la credibilidad del formato.

Otros puntos menores:
- La duración de 75 min en la Etapa 1 queda por debajo de la norma del género (2-3 h o más). El plan lo compensa con la cola de ambiente y lo manda a la Etapa 2 (E11), una decisión defendible.
- La R3-L sigue sin diseñar, pero el plan lo reconoce.
- La "Continue watching?" de YouTube solo salta con reproducción automática entre vídeos. Refuerza la apuesta por vídeos largos únicos y no invalida nada.
