# Encargo: tribunal final do Gauntlet 4 (v1 fronte a v2 de "As meigas de verdade")

Encargo para un único axente (Claude) que xulga a v2 rematada fronte á v1. Escribiuno Claude (orquestador) o
03-10-2026. Ningunha persoa revisa: o veredicto é dun axente e así hai que dicilo. Escribe en galego normativo (D17).

## Papel

Un só tribunal con catro miradas: (1) a persoa que viu a v1 e se queixou (as tres queixas literais de
`gauntlet4/contexto.md` §1); (2) director de fotografía e montador de documentais de época; (3) guionista de canles de
historia para durmir; (4) responsable de cumprimento para publicar en YouTube. Esixente e concreto: cada defecto co
minuto:segundo, o plano e o ficheiro.

## Material (rutas desde a raíz do repo; `$SCRATCH` = `source herramientas/pipeline/entorno.sh`)

Preparado polo orquestrador en `plan-de-negocio/gauntlet4/tribunal/` (ver `LEEME.md` alí):

- **A cegas (antes de destapar):** `cego/A-texto.txt` e `cego/B-texto.txt` (os dous guions; a lonxitude delata cal é
  cal: xulga polos criterios, non pola duración); `cego/A-imaxes-*.jpg` e `cego/B-imaxes-*.jpg` (a imaxe de cada
  plano mostrado, coas palabras que se oen nese plano debaixo, mostrados ás mesmas fraccións do episodio). **Non
  leas `$SCRATCH/tribunal4/clave.txt` ata ter escrita a sección 1.**
- **Despois de destapar:** `tiras-movemento-*.jpg` (catro fotogramas ao longo de cada plano da v2: o que se move de
  verdade), `detalle-*.jpg` (todos os planos da v2 co minuto:segundo), `medidas.json` (correlación automática
  CLIP-L fronte ao texto en inglés da v1 e da v2, planos con I2V que pasaron a porta, paralaxe, duracións por fase).
- **QA automático da v2:** `gauntlet4/video/qa.md` (e `qa.json`); descrición `descricion.txt`; créditos na ficha
  `herramientas/pipeline/temas/meigas-de-verdade-v2.yaml`.
- **Proceso:** veredictos das pezas (`gauntlet4/veredictos/`), revisión das imaxes por un axente
  (`video/revision-imaxes-r1.md`, `revision-imaxes-r2.md` se existe), porta de vídeo (`video/porta-i2v.json`),
  informe de movemento (`movemento/informe-r1.md`). O tribunal anterior: `gauntlet3/veredictos/tribunal-final.md`.

## Veredicto: `plan-de-negocio/gauntlet4/veredictos/tribunal-final.md`

1. **A cegas, por queixa** (antes de destapar), A fronte a B, cunha nota de 1 a 5 e a elección con porcentaxe:
   - Queixa 1, texto: ¿fío condutor e sentido de conxunto ou frases inconexas? ¿Calidade literaria (ritmo, imaxes,
     voz propia, remates)? Cita frases concretas.
   - Queixa 2, imaxe e texto: plano a plano, ¿a imaxe ilustra o que se oe (quen, que, onde, con que)? ¿Chama a
     mirada (rostros, mans, xesto, luz, primeiro termo)? Conta os planos con correlación ≥ 4.
   Despois, destapa.
2. **Queixa 3, movemento** (destapado): coas tiras, ¿hai xente que camiña e fai cousas, planos que evolucionan, ou só
   cámara sobre fotos? ¿O movemento é crible ou deforma (caras, mans, corpos)? Conta os planos con movemento propio.
3. **Defectos da v2** nas follas de detalle, en tres grupos: bloquea publicar / molesta / menor (anacronismos,
   artefactos, clixés de bruxa vetados en `gauntlet3/contexto.md` §8.5, personaxes incoherentes, repeticións).
4. **Gancho e embude:** ¿engancha o primeiro minuto? ¿Baixa amodo cara ao durmir sen tramos que esperten?
5. **Cumprimento:** aviso falado literal, autoría (que é automático e que fixo Claude, sen afirmar revisión humana),
   aviso de contido xerado por máquina (cláusula (e) da licenza LTXV), créditos das sementes CC BY, conxuro (só o
   primeiro verso, co autor), descrición e capítulos.
6. **Veredicto:** por queixa, GAÑA ou PERDE a v2; global, **a v2 gaña** se gaña nas tres queixas, sen defectos que
   bloqueen publicar e coas portas automáticas da QA en verde. Ata 5 arranxos antes de publicar (minuto, plano e
   ficheiro) e ata 5 melloras para o seguinte episodio.

## Regras

- Cada cifra con fonte ou marcada [S]. Distinguir o automático, o que fixo Claude e o que faría unha persoa. Non
  afirmar nada que non se poida ver ou ler no material. Non podes oír o son nin ver o vídeo enteiro: dio, e xulga co
  material.
- Gardar en git cada sección rematada (commit e push só de rutas explícitas, coas dúas liñas de autoría de
  `gauntlet4/contexto.md` §7).
- Escribir só en `gauntlet4/tribunal/` e en `veredictos/tribunal-final.md`. Nada de modelos nin traballos pesados de
  CPU; un ffmpeg puntual, con `herramientas/gauntlet/candado.sh`.
- Ao rematar, devolve un resumo de ≤ 10 liñas: veredicto por queixa e global, e os arranxos antes de publicar.
