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

## Entorno

- **Voces VITS de Nós (Celtia, Sabela, Icía) no instaladas**: el disco tenía 4,2 GB libres, cada checkpoint ronda
  1 GB (`herramientas/voz/README.md`) y `coqui-tts` en el venv común podía romper a los otros agentes. Las voces
  "de mujer" del murmullo son Brais con tono y formantes subidos por remuestreo; bajo el paso bajo y la reverberación
  no debería notarse [S], pero nadie lo ha escuchado.
- **DNSMOS**: la rueda `speechmos` 0.0.1.1 (Microsoft, MIT) trae los ONNX de DNSMOS P.835 y P.808. Se instala con
  `pip install --no-deps --target $SCRATCH/son/pylib`; **ojo**: `ST2_STUBS` trae un `speechmos` falso (stub para
  importar StyleTTS2), así que al medir no hay que poner `ST2_STUBS` en `PYTHONPATH`.
- **La cola del candado de CPU fue larga** (5-6 trabajos de voz, visual y dossier esperando): las pruebas ligeras de un
  hilo (generar ambientes, montar opciones) se hicieron fuera del candado con `nice` y `OMP_NUM_THREADS=1`; lo pesado
  (TTS, DNSMOS, Whisper) con el candado.
- La voz del fragmento se generó con **Cotovía 0.5**: el agente de voz cambió `entorno.sh` a la Cotovía "nova" pocos
  minutos después. Para comparar opciones de sonido da igual (la voz es la misma en las cuatro).
