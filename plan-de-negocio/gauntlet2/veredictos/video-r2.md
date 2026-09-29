# video · ronda 2

### Crítico visual ciego: PIERDE/NO APRUEBA

En la imagen 1, los fotogramas 2:24 y 2:41 son una toma repetida y casi idéntica, con una paleta inconsistente (pictórica, saturada o sepia) y multitudes clónicas y recargadas. En la imagen 2, la baja resolución del storyboard impide verificar bien los artefactos finos.

Elijo la imagen 2 por su calidad cinematográfica, aunque sus fotogramas son capturas de 160x90 de un storyboard de YouTube, reescaladas y borrosas. Por eso los artefactos finos de manos y caras no se pueden comprobar igual de bien que en la imagen 1.

Imagen 2: la estética es muy coherente de principio a fin (palacio barroco, luz dorada de velas y lámparas de araña, paleta cálida uniforme). La composición es de cine: profundidad, simetría en la galería y en el jardín, planos a contraluz ante la ventana. Tiene variedad de planos: de detalle, medio y general del parterre. El conjunto transmite un relato de corte con atmósfera sostenida. No se ven texto basura ni deformaciones evidentes a esa resolución.

Imagen 1: tiene más resolución y personajes plausibles, pero varios problemas:
- Los fotogramas 2:24 y 2:41 son prácticamente idénticos: hay una toma repetida o congelada durante unos 17 s.
- La paleta es inconsistente. Mezcla un look pictórico (el castillo en 0:08) con verdes saturados de videojuego (2:24) y fotogramas sepia desvaídos (el barco en 1:16).
- Las multitudes son densas y genéricas, con caras de relleno clónicas en 0:08 y 3:15.
- La escena de niños con cuervos y perros sobre escombros (1:33) queda rara y recargada.
- Los planos de 2:07 y 3:15 están saturados de figuras pequeñas.

La imagen 1 evoca bien lo medieval, pero se siente menos pulida y menos unificada como pieza.

### Operador de canales faceless con IA: PIERDE/NO APRUEBA

El guion (sobre todo el gancho de los primeros 30 s) es falso y no es galego normativo, y aun así el pipeline publica el MP4 cuando su propia QA dice NON PUBLICABLE. Afirma 'a irmandade venceu', cuando los irmandiños fueron derrotados en 1469, e inventa 'fortaleiras' (x2). Además repite frases y mete relleno sin sentido. Acción: (a) convertir las puertas lingua_lt y h1_ancoraxe en bloqueantes, que regeneren el bloque o recurran a frases literales del dossier en vez de emitir el vídeo; (b) añadir una puerta de veracidad por frase del gancho: cada afirmación debe tener implicación NLI o coincidencia con un hecho de feitos.yaml, y se rechazan los resultados o desenlaces no presentes en el dossier; (c) incluir en el dossier el desenlace (derrota de 1469, reconstrucción de las fortalezas) para que el LLM no lo invente; (d) hacer que un fallo de hunspell/LT sobre palabras inexistentes bloquee siempre. Regenerar ejemplo.mp4 solo cuando pase 12/12.

Errores factuales: Guion/gancho: 'Os nobres tiñan poder, pero a irmandade venceu' — falso: los irmandiños fueron derrotados en 1469 (batalla de Almáciga) y obligados a reconstruir las fortalezas (es.wikipedia.org/wiki/Gran_Guerra_Irmandiña) | Guion: 'fortaleiras' (x2) no es una palabra gallega; es 'fortalezas' | Guion: 'o lume ardeu en silencio durante séculos' y 'As chaves da Rocha Forte caeron unha tras outra': inventados, no están en el dossier | Entrega: se presenta como vídeo de ejemplo un MP4 que qa.md marca como NON PUBLICABLE (10/12 puertas)

Inspeccioné el MP4 real: decodifica entero sin errores (ffmpeg -v error, rc=0), dura 203,85 s, 1080p a 24 fps, AAC 48 kHz y pista mov_text en glg. El desfase audio-vídeo es de 0,03 s. El sonido está bien: -17,1 LUFS y -1,0 dBTP de pico real. El ASR de Nós da un WER de 0,026 sobre la mezcla y los subtítulos están alineados. Las imágenes (contactsheet) tienen aspecto medieval creíble y coherente, pasan una puerta automática de anacronismos y hay 9 planos en el primer minuto. El pipeline parece de verdad desatendido, con LLM local EuroLLM-9B y caché de llamadas, pero se relanzó 4 veces con cambios de código a mitad de la ejecución. Hay tres fallos graves.

1) El propio qa.md del pipeline dice 'Veredicto automático: NON PUBLICABLE' porque fallan las puertas lingua_lt y h1_ancoraxe. Se entrega como ejemplo un vídeo que el propio sistema rechaza.

2) El gancho, que es justo lo que pidió el promotor, contiene falsedades y palabras inventadas: 'Os nobres tiñan poder, pero a irmandade venceu' es falso, porque en 1469 los ejércitos de Pedro Madruga, Fonseca y Lemos derrotaron a los irmandiños y los obligaron a reconstruir las fortalezas (https://es.wikipedia.org/wiki/Gran_Guerra_Irmandi%C3%B1a, https://www.despertaferro-ediciones.com/2020/revuelta-gran-guerra-irmandina-galicia-1467-1469/). Además, 'fortaleiras' no existe y aparece dos veces, 'unión popular' es un calco, y hay palabras no normativas como 'teituras', 'esgadanaban', 'antorchas' y 'rostros'. Hay relleno sin sentido: 'burgueses coa súa contabilidade de loitas', 'o lume ardeu en silencio durante séculos'. Los párrafos se repiten, como avisa el propio revisor ('Non repitas frases'), y el resumen del gancho se repite casi literal tres veces en 90 s.

3) La duración es de 3,4 min frente a un formato de dormir de 1 h o más. La extrapolación a 60 min da unas 27 h de reloj de pared en CPU.

Un espectador gallegohablante notaría la palabra inventada en la segunda frase y la historia falsa, así que no da el pego. Las imágenes y el audio sí están a la altura. Donde falla es en la corrección factual y lingüística del guion.
