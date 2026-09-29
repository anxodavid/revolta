# Notas para Claude en este repo

## Gauntlet Loop: guardar resultados parciales en git

En los Gauntlet Loop (y en cualquier workflow multiagente largo) hay que **ir guardando en git los resultados parciales**, sin esperar al final:

- Commit y push de cada pieza cuando termina una ronda (borrador + veredicto del crítico), de la integración y de cada ronda del tribunal.
- Guardar también los veredictos de los críticos (ganó/perdió, mayor carencia), no solo los borradores.
- Motivo: el 29-09-2026 un reinicio del contenedor y el límite de uso de la sesión cortaron el Gauntlet del plan de negocio a medias. Lo que solo estaba en el scratchpad o en el journal del workflow estuvo a punto de perderse y el tribunal final quedó sin terminar.
- Los borradores de trabajo van en el repo (p. ej. `plan-de-negocio/gauntlet/`), no solo en el scratchpad.

## No subir ficheros a medio escribir

- Antes de hacer commit de un vídeo o audio, comprobar que se decodifica entero (`ffmpeg -v error -i fichero -f null -`) y que ningún proceso lo está escribiendo (`ps`).
- Los renders deben escribir en un fichero temporal y renombrarlo al final (escritura atómica), para que un commit intermedio nunca capture un MP4 incompleto.
- Motivo: el 29-09-2026 se subió `gauntlet2/video/ejemplo.mp4` a mitad de render y quedó corrupto en GitHub (commits fb72a95 y fba68aa).
