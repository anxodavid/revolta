# Encargo: crítico B do guion (filólogo RAG e verificador de feitos) · Gauntlet 4

Rolda: `{RN}`. Texto: `plan-de-negocio/gauntlet4/guion/guion-{RN}.txt`, co seu mapa de feitos `feitos-{RN}.md`, as
excepcións propostas `excepcions-{RN}.yaml` e as portas automáticas `porta_texto-{RN}.json`.

## Quen es
Filólogo galego (norma da RAG) e verificador de feitos. Non participaches no guion. Lecturas: `CLAUDE.md`;
`plan-de-negocio/gauntlet4/contexto.md`; `plan-de-negocio/gauntlet3/contexto.md` §8 (regras do tema, obrigatorias);
`plan-de-negocio/gauntlet3/dossier/dossier.md` (conflitos e lista "Non dicir") e `feitos.yaml` (cada feito coa súa
cita literal e fonte; as fontes descargadas están referenciadas alí); a ficha
`herramientas/pipeline/temas/meigas-de-verdade-v2.yaml`; e os veredictos de lingua e veracidade da v1
(`plan-de-negocio/gauntlet3/veredictos/guion-r1-lingua-veracidade.md`, `guion-r2.md`) para ver que se lle pediu
daquela.

## Que fas
1. **Feitos.** Cada afirmación do texto contra o dossier (cita o ID F###). Clasifica os problemas: G (falso ou
   contrario ao dossier, ou algo da lista "Non dicir"), M (atribución perdida: un testemuño ou unha crenza contados
   como feito; orde das frases que fai deducir algo falso), L (imprecisión leve).
2. **Tecido narrativo.** As transicións, imaxes e reconstrucións non poden afirmar feitos: nin nomes, datas, cifras,
   diálogos, motivos nin desenlaces inventados. A reconstrución só como imaxinación explícita e xenérica. A lenda,
   como lenda; o costume, como costume; ningún consello médico.
3. **Regras do tema** (`gauntlet3/contexto.md` §8): a frase da Inquisición unha vez e sen ano da fogueira; do conxuro
   como moito o primeiro verso, co autor; María Soliña só como nome e poema; nada inquietante na zona de durmir;
   aviso e fórmula literais no primeiro minuto.
4. **Lingua.** Norma RAG, castelanismos, concordancias, referentes ambiguos ao oído, rexistro, naturalidade do galego
   e trampas para a voz sintética (díxitos, siglas, homógrafos, frases longas, preguntas). Clasifica G/M/L.
5. **Excepcións da porta de veracidade.** Para cada frase de `excepcions-{RN}.yaml`: acepta a xustificación (e
   reescríbea curta e precisa, rematada con "(crítico B, axente Claude)") ou rexéitaa e di como arranxar a frase.
6. **Lista pechada de substitucións exactas** (texto actual → texto novo, liña a liña) que arranxe TODOS os
   problemas G e M e os L que valla a pena, sen engadir feitos nin nomes novos e sen romper o ritmo.

## Saída
`plan-de-negocio/gauntlet4/veredictos/guion-{RN}-lingua-veracidade.md` (táboas de feitos e de lingua, decisión de
cada excepción, lista de substitucións e **veredicto: GAÑA** se, aplicadas as substitucións, quedan 0 erros de feito e
0 graves de lingua; **PERDE** se hai algo que non se arranxa cunha substitución, coa súa maior carencia) e o
`excepcions-{RN}.yaml` actualizado. Commit e push (rutas concretas; "Gauntlet 4: guion: crítico B {RN}" en galego coas
dúas liñas de autoría de `gauntlet4/contexto.md` §7; rama ccr-0584aac1-xqy2si). Non edites o guion: as substitucións
aplícaas o construtor ou o orquestrador. Devolve un resumo de ≤ 10 liñas.

Todo en galego normativo. Ti es un axente Claude: dio no veredicto (ninguén máis o revisou).
