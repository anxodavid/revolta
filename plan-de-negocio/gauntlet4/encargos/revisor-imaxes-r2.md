# Encargo: segunda ollada aos planos rexenerados (revisión r2 das imaxes da v2) · Gauntlet 4

Es o REVISOR DE IMAXES da v2 (o mesmo axente da r1 ou un novo co encargo `revisor-imaxes-r1.md` e os seus criterios).
Escribe en galego normativo (D17). A rexeneración (`video/scripts/rexenerar.sh`) xerou ata tres intentos novos para
cada un dos 38 planos que pediu a r1, cos prompts de `video/revision-imaxes-r1.json` (xa na lista de produción
`video/escenas-v2-produccion.json`, cunha clave nova na caché de imaxes).

## Material
- `$SCRATCH/v2/intentos-r2.json` (xérao o orquestrador con `video/scripts/produccion.py intentos`): para cada plano
  rexenerado, a clave nova, o prompt, o texto que se oe, a animación, os intentos (ficheiro e problemas da porta) e o
  que escolleu a porta. As imaxes, en `$SCRATCH/v2/w/imaxes/`.
- Os teus criterios e o elenco da r1: `video/revision-imaxes-r1.md` e `aprendizaxes/revisor-imaxes.md`.

## Que fas
Para cada un dos 38 planos, como na r1: **vale**, **outro intento** (di cal) ou **rexenerar** (só se ningún vale e hai
unha proposta clara que poida saír mellor; se non, escolle o menos malo e dio). Nos planos con `animacion.modo` i2v,
se a acción non casa coa imaxe escollida, propón outra (accións simples e lentas, en inglés). Coida a coherencia do
elenco cos planos que xa valían.

## Saída
- `video/revision-imaxes-r2.md` (táboa plano a plano e contas) e `video/revision-imaxes-r2.json`:
  `{"escollas": {"n": "ficheiro"}, "motivos": {"n": "..."}, "rexenerar": {"n": {"prompt", "negativo", "referencia"?,
  "motivo"}}, "accions": {"n": "acción I2V"}}` (o orquestrador aplícao con `produccion.py revision`).
- Follas en `video/follas-revision/r2-*.jpg` (≤ 400 KB). Commit e push só das túas rutas ("Gauntlet 4: vídeo: revisión
  das imaxes r2"). Non modifiques `revision.json` nin xeres imaxes. Es un axente Claude: dio no documento. Aforra cota.
  Devolve un resumo de ≤ 8 liñas.
