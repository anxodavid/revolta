# Aprendizajes: pieza SON (Gauntlet 3)

Agente de sonido (Claude), 30-09-2026. Todo lo hizo Claude con código y medidas automáticas. **Nadie escuchó los
audios** (Claude no puede oír): lo único "visto" fueron espectrogramas, que Claude miró como imágenes.

## Qué funcionó

- **Catálogo procedural por escena** (`son.py`): 9 tipos (`choiva`, `lume`, `mar`, `vento`, `fonte`, `xente`,
  `noite`, `aldea`, `campas`) sin grabaciones de terceros. Cada uno genera 30 s de estéreo a 48 kHz en 0,3-4,7 s de un
  núcleo: un episodio de 30 min se sonoriza en pocos minutos de CPU.
- **Murmullo de gentío con nuestra propia voz**: 36 frases de conversa cotidiana (escritas por Claude) narradas con
  StyleTTS2 Brais con tono, tempo, entonación y referencia de estilo distintos (`son_xente.py`, ~2 min de CPU). El
  banco pesa 442 kB (OGG Vorbis, 16 kHz, 91,6 s) y va en el repo (`herramientas/pipeline/son_datos/`), así que no
  hay que regenerarlo en cada sesión. En tiempo de mezcla se toman 6-12 voces con timbres por remuestreo (0,84-1,33:
  graves y agudas), paso bajo a 0,9-1,5 kHz y reverberación.
- **Espectrogramas como "oído" de sustitución**: mirar el espectrograma de cada tipo detectó un defecto que las
  medidas no veían (ver abajo, bandas de peine en la lluvia).
- **Métrica de "sustos"** (arranques de +6 dB en 200 ms que quedan >10 dB sobre la mediana local de 400 ms, con
  ponderación K): separa bien lo que sobresalta (chasquidos de la lareira antigua, goteos del alero sin limitar) de lo
  que sube despacio (olas, fundidos).

## Qué falló y cómo se corrigió

1. **Un solo núcleo para todas las gotas finas** de `choiva2` → todas con el mismo espectro → bandas horizontales fijas
   por encima de 5 kHz (efecto de peine), visibles en el espectrograma. Solución: 6 núcleos distintos. Venía de la
   lluvia que el promotor ya había oído.
2. **Eventos normalizados por RMS**: si hay menos goteos, cada uno suena más fuerte (lo contrario de lo que se quiere
   al dormir). Solución: amplitud fija por evento, relativa al lecho, y la tasa se baja aparte.
3. **Limitador con RMS sin ponderar y ventana de 1 s**: dejaba pasar píos de pájaro y chasquidos 18-22 dB por encima
   del fondo (la ponderación K sube ~4 dB lo que está por encima de 2 kHz). Solución: potencia con ponderación K
   (BS.1770), lecho en 3 s y eventos en 50 ms; chasquidos de la lareira y píos también como eventos limitados (13 dB
   en el gancho, 6 al dormir).
4. **`uniform_filter1d` sobre potencias da valores negativos minúsculos** → `sqrt`/`log` con NaN → pista entera en
   NaN. Solución: `np.maximum(..., 0)`.
5. **Fundidos centrados en el corte se comen los planos limpios cortos**: con 4 de 15 planos limpios, solo un 11 %
   de voz limpia. Solución: hacia un plano limpio, el fundido se hace en 3/4 dentro del plano con sonido (17,8 %,
   casi la proporción de planos limpios); entre dos sonidos, fundido cruzado centrado.
6. **Artefacto de la métrica**: un fundido desde el silencio contaba como pico. Solución: solo cuentan arranques
   rápidos y ventanas con ambiente alrededor.

7. **El WER de un texto largo con pausas largas mide un defecto de Whisper**: en la zona de dormir se salta frases
   enteras tras los silencios (con voz sola, D, borró 31 de 77 palabras: WER 0,42; con lluvia continua, 2). Las
   palabras que sí reconoce son las mismas con cualquier ambiente. Hay que medir **frase a frase** (cada frase cortada
   con margen): así, 0,018 sin ambiente y 0,022-0,026 con él (el ambiente solo se lleva 1-2 palabras átonas de 271). Aviso para `qa.asr` del pipeline, que transcribe el episodio entero con `vad_filter=False`: puede
   suspender la puerta de WER en la zona de dormir sin que la voz tenga la culpa [S].
8. **La lista de planos decide el ritmo de cambios, no el código**: con una lista que alterna sonido y voz limpia en
   cada plano, el catálogo cambia cada ~9 s (62 cambios cada 10 min): un parpadeo. Soluciones: la guía pide bloques
   por escena y respiros limpios; `son.tramos_de_planos` no corta el ambiente en un inserto neutro de menos de 20 s
   entre dos planos con el mismo sonido (`"limpa"` sí corta); y la QA avisa con más de 20 cambios en 10 min en el
   gancho o 10 al dormir. **Mi primer intento de lista "según la guía" también se pasó** (78 % del tiempo con sonido,
   12,3 cambios cada 10 min al dormir): el aviso de la QA hace falta aunque la lista la escriba alguien que conoce la
   guía.
9. **Los generadores de antes sobresaltan al dormir**: en 15 min de zona de dormir simulada, la lluvia de 7541a9e da
   30 "sustos" (goteos del alero normalizados por RMS) y su lareira 72-169 (chasquidos sin limitar); el catálogo
   nuevo, 0.

## Qué dijeron las medidas (resumen; tabla completa en `son/informe.md`)

- DNSMOS SIG (la voz) no cambia con ningún ambiente (3,57-3,62); BAK/OVRL bajan con cualquier fondo por diseño.
- El murmullo de `xente` es ininteligible para Whisper (nada en 2 de 3 semillas; 8 palabras alucinadas con baja
  confianza en la tercera), que transcribe perfectas las mismas frases en seco.
- Monotonía en 30 min: lluvia continua 93 %, catálogo por escena 8-11 %.

## Entorno

- **Voces VITS de Nós (Celtia, Sabela, Icía) no instaladas**: el disco tenía 4,2 GB libres, cada checkpoint ronda
  1 GB (`herramientas/voz/README.md`) y `coqui-tts` en el venv común podía romper a los otros agentes. Las voces
  "de mujer" del murmullo son Brais con tono y formantes subidos por remuestreo; bajo el paso bajo y la reverberación
  no debería notarse [S], pero nadie lo ha escuchado.
- **DNSMOS**: la rueda `speechmos` 0.0.1.1 (Microsoft, MIT) trae los ONNX de DNSMOS P.835 y P.808. Se instala con
  `pip install --no-deps --target $SCRATCH/son/pylib`; **ojo**: `ST2_STUBS` trae un `speechmos` falso (stub para
  importar StyleTTS2), así que al medir no hay que poner `ST2_STUBS` en `PYTHONPATH`.
- **La cola del candado de CPU fue larga** (5-7 trabajos de voz, visual y dossier esperando; `flock` no respeta el
  orden de llegada): las pruebas ligeras de un hilo (generar ambientes, montar opciones, DNSMOS con un hilo: 3 min
  para 4 × 134 s) se hicieron fuera del candado con `nice` y `OMP_NUM_THREADS=1`; lo pesado (TTS, Whisper) con el
  candado. Partir las medidas en fases (`medir.py sinal | asr | frases`) permitió avanzar sin esperar por lo ligero.
- **Corte de la sesión (límite de uso) y reinicio del contenedor**: murieron los trabajos en cola, pero el scratchpad
  (venv, modelos, WAV) sobrevivió y las medidas ya escritas en el repo (JSON con escritura atómica) no se perdieron;
  el orquestador subió lo pendiente. Guardar cada fase en el repo en cuanto termina.
- La voz del fragmento se generó con **Cotovía 0.5**: el agente de voz cambió `entorno.sh` a la Cotovía "nova" pocos
  minutos después. Para comparar opciones de sonido da igual (la voz es la misma en las cuatro).
