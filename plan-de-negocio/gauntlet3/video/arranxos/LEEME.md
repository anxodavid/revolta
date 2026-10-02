# Ronda de arreglos del tribunal final (01-02/10/2026)

Qué hay aquí (todo lo demás del episodio está en `video/`):

| Fichero | Qué es |
|---|---|
| `antes-despois.jpg` | Los 11 planos que pidió cambiar el tribunal, antes (izquierda) y después (derecha); aclarados ×1,5 para verlos |
| `escollas-manuais.txt` | Los dos planos (91 y 145) en que Claude eligió a mano un intento distinto del que eligió la puerta |
| `produccion1.log`, `produccion2.log` | Registros de las dos ejecuciones de `lanzar-longo.sh`, sin los avisos de las librerías |

**Quién hizo qué:** Claude (Anthropic) reescribió a mano los prompts de los 11 planos, miró cada intento al salir,
reescribió otra vez los de 5, 31, 61, 67 y 91 tras ver los primeros intentos y eligió a mano los planos 91 y 145. La
generación, la puerta, el sonido, el montaje y la QA son automáticos. **Ninguna persona ha visto ni oído el
resultado.**

**Cronología:**
- `produccion1` (21:12-21:59 UTC): voz e imágenes; se paró en el plano 126 (FileNotFoundError de la caché restaurada).
- `produccion2` (21:59 UTC): imágenes con los prompts reescritos; el contenedor se reinició a las 22:32 al empezar el
  montaje. Relanzada a las 23:04; parada a las 23:16 porque iba a añadir un intento al plano 145 y perder la elección
  manual (arreglado en `imaxes.py`); relanzada a las 23:16 y terminada a las 01:23 del 02-10 (rc 0).

**Resultado (QA, `video/qa.md`):** 12/13 puertas, como antes; pico real −1,7 dBTP (antes −0,1); 124/162 imágenes
aprobadas por la puerta. De las 38 que no pasan: el 91 y el 145 son las elecciones manuales, y 6 imágenes que no se
tocaron (46, 121, 130, 149, 157 y 159) caen ahora por repetición o por "caminantes de espaldas" al compararse con los
planos nuevos. Los planos 133, 153 y 161 pasan ahora la puerta.
