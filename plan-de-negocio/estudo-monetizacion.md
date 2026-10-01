# Estudo de monetización: "Cousas de Galiza para durmir"

Versión do 01-10-2026, en galego (D17). Escribiuno Claude a petición do promotor co que xa había no repo:
- o plan v2;
- a investigación do Gauntlet 1;
- o Gauntlet 3, co episodio longo "As meigas de verdade";
- a busca de referencias gráficas da rama `ccr-17437293-x0i276`.

Despois **contrastáronse na web as referencias que sosteñen o plan** (§9). As cifras con fonte levan a URL ou o
documento do repo onde está; as estimacións van marcadas **[S]**. Ningunha persoa revisou este documento.

---

## 0. Resumo

1. **Os anuncios de YouTube non son o modelo do primeiro ano.** Desde o 1-02-2027, para entrar no YPP unha canle
   nova precisa **8.000 h de visualización en 365 días** (comprobado, §9). O requisito de 1.000 subscritores non o
   menciona esa fonte; segue como supuesto [S]. No escenario base do plan v2, a canle faría 45-400 subscritores en
   12 meses. Ingresos por anuncios o primeiro ano: **≈ 0 €**.
2. **Os cartos posibles están noutras cinco vías.** Por orde de calendario:
   - premios en galego: Youtubeiras+, con inscrición **ata o 15-11-2026**;
   - audio longo: o Spotify Partner Program, que chega a España o **20-10-2026**, e iVoox;
   - encargos públicos: convocatoria dixital da CRTVG, ata 25.000-26.000 € por proxecto;
   - o Camiño no **Xacobeo 2027**, que comeza o 31-12-2026;
   - encargos B2B de "historia local para durmir".

   Ningunha é segura, e case todas chocan cunha decisión vixente (punto 4).
3. **O que hai que vender é a capacidade, non as visualizacións.** Producir 31 minutos en galego con fontes custa
   hoxe **≈ 16,5 h de CPU e uns poucos euros de caixa** (§2). Iso fai viable o que ningunha produtora faría por ese
   prezo: series temáticas, a historia dun concello concreto, versións de 2-3 h para durmir. A canle de YouTube é o
   **escaparate** que demostra esa capacidade.
4. **O anonimato (D6) pecha case todas as vías con cartos.**
   - As axudas e a CRTVG esixen un solicitante identificado.
   - O B2B precisa alguén que venda e asine.

   En anónimo, o teito realista é **premios + audio + fan funding: 0-1.500 € o primeiro ano [S]**. **É a decisión
   principal do promotor** (§6).
5. **Antes de cobrar nada hai tres bloqueos:**
   - **A voz.** O dataset de Brais é CC BY 4.0, pero os seus termos prohiben expoñer as gravacións en público e
     limitan o uso á investigación (comprobado, §9). Fai falta o si de Nós/USC ou unha voz con licenza clara.
   - **A imaxe.** O tribunal di que o episodio non se pode publicar tal cal, por 4 planos con obxectos modernos.
   - **A política de contido inauténtico de YouTube**, que se avalía a nivel de canle (comprobado).

   As referencias gráficas (D15) arranxan parte da imaxe e, ben usadas, tamén axudan coa política (§3.2).

---

## 1. Que sabemos agora que non sabía o plan v2

| Feito | Dato | Onde |
|---|---|---|
| Un episodio longo é factible | 31:22, 1080p, 162 planos, WER 0,031, −17,1 LUFS, embude de voz medido (157 → 114 palabras/min) | `gauntlet3/video/qa.md` |
| Custo de máquina medido | 285,9 min de reloxo e **16,55 h de CPU de núcleo** (imaxes 142 min, montaxe 67, QA 31, voz 16) | `gauntlet3/video/qa.md` |
| O guion e o gancho gañan á referencia | Gancho 4/5; zona de durmir máis tranquila e veracidade moi superior | `gauntlet3/veredictos/tribunal-final.md` §7 |
| **A imaxe perde**, por pouco | 35/162 planos non pasaron a porta; 4 bloquean (bombilla, farolas, casa colonial, maleta de rodas); casas inglesas en 9 planos | idem §2 e §7 |
| Ninguén o viu nin o oíu | O son gaña "por medidas", sen escoita | idem §5 |
| Tema con datos | "Brujas" sobe × 2,0 en outubro; o Camiño ten o mellor dato "para durmir" dun tema galego (**182.373 visualizacións**, en castelán); 0 vídeos para durmir en galego en ningún tema | `gauntlet3/tema/investigacion.md` |
| Referencias gráficas | **226 candidatas** con licenza libre en 14 conceptos. **A maioría son CC BY-SA**; ningunha se mirou a ollo | rama `ccr-17437293-x0i276`, `docs/referencias-graficas/referencias.md` |
| Xerar imaxes fóra é barato | SDXL-Lightning en Replicate: **≈ 0,0057 $ por execución** (comprobado o 01-10-2026; antes anotárase 0,0018 $) | https://replicate.com/bytedance/sdxl-lightning-4step |

---

## 2. Custo unitario: o que fai posible o negocio

| Partida por episodio de ~30 min | Hoxe | Co guion por API e as imaxes fóra [S] |
|---|---|---|
| Guion | Claude con axentes (Gauntlet, horas de sesión; non é desatendido, D8) | ≈ 0,5-1 USD (a metade do episodio de 60 min do plan v2 §3.3) |
| Imaxes (≈ 400 intentos) | 142 min de CPU | ≈ 2,3 USD en Replicate; en local, de balde pero lento |
| Voz, son, montaxe e QA | ≈ 2,3 h de reloxo en local | igual |
| **Caixa por episodio** | ≈ 0 € máis a electricidade | **≈ 3-4 €** |
| Horas do promotor | Revisar, subir, etiquetar e sementar: 40-100 min (plan v2 §3.4) | igual, **máis unha escoita enteira se se vende** (§3.1) |

Comparación: a garantía humana do plan v1 custaba ≈ 305 € por episodio (`decisiones.md`, D5). A CRTVG financia ata
**25.000 € por proxecto dixital** (§9). **A marxe está entre esas dúas cifras**: non nas visualizacións, senón en
producir barato o que outros pagan caro.

---

## 3. Condicións previas para cobrar calquera cousa

### 3.1 Bloqueos

| Bloqueo | Por que importa para os cartos | Saída |
|---|---|---|
| **Voz de Brais** | Os termos do dataset prohiben a "public exposure" das gravacións e limitan o uso á investigación e a ferramentas de IA con fins lingüísticos (§9). Con *Right to Monetize*, YouTube pode pór anuncios aínda que a canle non estea no YPP: **en YouTube non existe o uso "non comercial"** (plan v2 §7.1) | Enviar xa o correo a Nós/USC (borrador en `gauntlet2/piezas/ecosistema.md`). En paralelo, probar o embude cunha voz CC BY 4.0 do corpus CRPIH_UVigo (Sabela, Icía, Iago, Paulo). Para o B2B e a CRTVG só vale unha voz con licenza comercial clara |
| **Imaxe** | O tribunal non deixa publicar así. Para premios e encargos, a imaxe é o primeiro que se xulga | Rolda de arranxos (≈ 3,5 h de máquina, `docs/HANDOFF.md` §0) e referencias semente (§3.2) |
| **Contido inauténtico** (YouTube, desde o 15-07-2025; aclarado o 16-07-2026 en tres categorías) | "AI-generated content made with generic or unoriginal templates giving the impression of mass production" non se monetiza. A política "applies to your channel as a whole" (§9). Probabilidade de que deneguen o YPP: 40-60 % [S] (plan v2 §7.2) | Un **elemento orixinal** en cada episodio: tese, fontes citadas en voz e un documento ou foto real en pantalla. Cadencia lenta. Variedade real entre episodios. YouTube di que segue sendo monetizable o contido con "real research, distinct storytelling" (TechCrunch, §9) |
| **Escoita humana** | Un encargo pagado, un premio ou unha emisión non aceptan "ninguén o escoitou". D5 vale para a canle, non para un cliente | Para o que se venda: unha escoita enteira (≈ 1 h por episodio de 30 min) **declarada**. Para a canle, D5 segue igual |
| **Etiqueta de IA** | YouTube esíxea; Spotify esixe declarar a narración sintética e prohibe suplantar voces (`gauntlet/investigacion/ingresos_alt.md` §3.1) | Ao subir: Studio → "AI use: Yes". O aviso falado xa o cumpre |

### 3.2 As referencias gráficas: calidade, licenza e "elemento orixinal"

- **Calidade.** As referencias cobren xusto o que SDXL non sabe debuxar: hórreo, carro de roda maciza, palloza,
  pazo, lousa e granito. Con elas como semente (img2img, ControlNet ou IP-Adapter, D15) deberían baixar as "casas
  inglesas" que custan o veredicto. **Falta probalo:** ninguén mirou esas imaxes.
- **Licenza: o detalle que importa para monetizar.** A maioría son **CC BY-SA**; por exemplo, o carro da Arnoia de
  Lmbuga é CC BY-SA 3.0 (§9). Unha imaxe xerada a partir dunha delas é, seguramente, "Adapted Material": algo
  "translated, altered, arranged, transformed, or otherwise modified". Iso obriga a acreditala e, polo *ShareAlike*,
  a compartila cunha licenza BY-SA ou compatible (texto legal comprobado en §9; aplicalo a img2img é interpretación
  non xurídica [S]). **Non impide monetizar**, porque a licenza non restrinxe o uso comercial. Pero un encargo con
  cesión de dereitos (CRTVG) podería non aceptalo [S]. Regra proposta:
  1. Para as sementes, preferir CC0, dominio público ou CC BY: o hórreo de Christof46 é **CC0 (comprobado)**, as
     armas do Met son CC0 e o traxe de Doré é de 1862.
  2. As BY-SA, mellor **amosalas tal cal** en pantalla, como documento real e co crédito, que transformalas.
  3. **Fotos propias do promotor** (hórreos, cruceiros, lareiras do seu contorno): licenza limpa e, ademais,
     **elemento orixinal** fronte á política de contido inauténtico.
- **O que non cobren** (ocos do informe): queimada limpa, carro de lado sen xente, traxe sobre fondo neutro, roupa
  dos séculos XV-XVII. Fontes a pedir: Museo do Pobo Galego, Galiciana e a Hispanic Society (fotos de Ruth Anderson,
  1924-26). Pedilas obriga a identificarse: outra vez D6.

---

## 4. Vías de ingreso, unha por unha

Probabilidades e importes **[S]** salvo que se indique fonte. "Ano 1" vai de outubro de 2026 a setembro de 2027.

| # | Vía | Requisito ou limiar (fonte) | Encaixe | Ano 1 [S] | Ano 2 [S] | ¿Compatible co anonimato? |
|---|---|---|---|---|---|---|
| A | **Anuncios de YouTube (YPP)** | 8.000 h en 365 días desde o 1-02-2027 (§9); 1.000 subscritores [S]. RPM 1,5-4 € (`retornos.md` §2.4) | Baixo: o sono acumula horas, pero non subscritores | 0 € | 0-300 € (só no optimista, 8-12 %) | Si |
| B | **Fan funding de YouTube** (membresías, Super Thanks) | 500 subscritores + 3.000 h, limiares que non cambian en 2027 (§9); 70 % para quen crea | Medio: público identitario e diáspora | 0 € | 0-200 €/mes no optimista | Si |
| C | **Spotify Partner Program** | Desde o 20-10-2026 en España: enderezo legal no mercado, 3 episodios, **2.000 h e 1.000 persoas de audiencia en 30 días** (§9). Está pensado para **pódcast en vídeo** | **O mellor encaixe estrutural**: o formato de durmir é audio de escoita nocturna repetida, e o mestre xa existe en vídeo | 0 € (limiar) | 0-60 €/mes | Si, declarando a IA |
| D | **iVoox** (fans, pago único por paquetes) | Sen limiar; comisión ¿5 %? sen verificar | Medio: paquetes do tipo "6 h de meigas para durmir" a 3-5 € | 0-50 € | 0-300 € | Si |
| E | **Premio Youtubeiras+ 2026** | Inscrición do 17-09 ao **15-11-2026 ás 23:59**; ≥ 3 publicacións desde o 16-11-2025; maioría en galego. 7 premios con dotación de 1.000-1.250 € (7.500 € en total) e un honorífico. As bases non mencionan a IA (§9) | Medio en cartos, **alto como validación externa**. O xurado valora "dotes interpretativos", o que penaliza a voz sintética | 0-1.000 € (P(premio) 5-15 %) | idem | Si |
| F | **Encargo da CRTVG/CSAG** | Convocatoria 2025: ata 357.000 € para 15 proxectos en cinco categorías (ficción, entretemento, **divulgación**, infantil, **videopódcast**), inéditos e integramente en galego. Seleccionáronse 12, con ata 25.000 € cada un (§9). Non atopei convocatoria de 2026; patrón ≈ xuño | **A única vía que cambia a escala.** Hai que presentar unha tempada inédita de 6-8 episodios, non o catálogo xa publicado | 0 € (preséntase no ano 1) | 0 ou 10.000-25.000 € (P 5-15 %) | **Non**: solicitante con nome e factura |
| G | **Xacobeo 2027** ("O teu Xacobeo", TU300A) | Prazo para actividades de 2027: **1-31-10-2026**. Ata 25.000 €: ao 60 % para autónomos e pemes, ao 80 % para entidades sen ánimo de lucro (§9). O ano santo comeza o 31-12-2026 | Alto no tema (o Camiño ten o mellor dato "para durmir"), pero esixe RETA ou unha asociación **este mes** | 0 € (non chegamos) | Seguinte convocatoria, se a hai | **Non** |
| H | **B2B: "a historia do teu concello para durmir"**, audioguías, museos | Contrato menor < 15.000 €; tícket de 1.000-6.000 € [S] (`ingresos_alt.md` §6) | Medio-alto se se vende: o custo unitario (§2) permite prezos que unha produtora non pode dar | 0-3.000 € | 3.000-15.000 € | **Non** |
| I | **Patrocinio de marcas galegas** (balnearios, editoriais, descanso) | Audiencia de miles por episodio; só unha mención ao comezo | Baixo ata ter datos | 0 € ou troco | 0-500 €/mes | En parte |
| J | **Máis linguas** (pistas pt/en no mesmo vídeo; castelán aparte) | Pistas: funcións avanzadas (verificación con DNI ante Google, non pública). En castelán, o tema fai 5-108 K visualizacións | **O mercado máis grande**, pero o castelán choca coa tese pro lingua e está descartado o primeiro ano (plan v2 §4.4) | 0 € | × 1,3-2 sobre A-C se as pistas funcionan | Si |

**Lectura:**

- **En anónimo** (A-E, I en parte, J): 0-1.500 € o primeiro ano e 0-3.000 € o segundo, case todo dun premio e, se
  hai tracción, das membresías.
- **Sen anonimato** (engadindo F, G e H): o valor esperado sobe a **≈ 1.500-5.000 € o segundo ano [S]**, cunha cola
  posible de 10.000-25.000 € se a CRTVG escolle o proxecto.

O valor esperado é pequeno nos dous casos. **A pregunta real é se o promotor quere un hobby que se pague só ou un
pequeno negocio de produción cunha canle de escaparate.**

---

## 5. Plan proposto por fases (desde o 01-10-2026)

Cada fase ten unha porta que decide se se segue. Os limiares do nicho son os do plan v2 §2.4, sen tocalos.

### Fase 0 · De outubro a mediados de novembro de 2026: saír ben e a tempo

Obxectivo: chegar ao **15-11 con 3 publicacións** (requisito de Youtubeiras+) e aproveitar o pico de "brujas" de
outubro.

1. **Esta semana:** rolda de arranxos de "As meigas de verdade" (11 planos, pico real ≤ −1 dBTP e descrición) e
   **escoita enteira do promotor** (31 min).
2. **Correo a Nós/USC xa.** Se o 31-10 non contestaron, publícase cunha voz CC BY de reserva (plan v2 §7.1), probada
   antes no embude.
3. **Publicación 1:** meigas, na segunda quincena de outubro. O mesmo día, en YouTube, en Spotify for Creators (o
   SPP abre o 20-10) e en iVoox, co mesmo mestre.
4. **Publicación 2:** Santa Compaña ou Samaín para o 1-2 de novembro, cando a busca da Santa Compaña se multiplica
   por 2,3-3,2. Ollo: o seu público é de terror (`tema/investigacion.md`), así que o embude ten que baixar antes.
5. **Publicación 3:** primeiro episodio do Camiño, a aposta para o Xacobeo 2027.
6. **Probar as referencias semente (D15)** nos planos máis difíciles (hórreo, carro, lousa), só con sementes CC0 ou
   CC BY, ou con fotos propias (§3.2).
7. **Inscribir a canle en Youtubeiras+** antes do 15-11 (Revelación e Calidade lingüística), dicindo con claridade
   como está feita.

**Porta 0 (15-11):** ¿tres publicacións sen planos bloqueantes e cunha voz con permiso ou con licenza CC BY? Se non,
non hai inscrición e a fase 1 empeza co que haxa.

### Fase 1 · De novembro de 2026 a febreiro de 2027: a proba do nicho do plan v2

- 8 episodios en total (os 3 da fase 0 contan), sementados en 3-5 comunidades galegas. Primeiro un por semana e
  despois un cada dúas semanas.
- **Novidade fronte ao plan v2: unha versión longa para o audio.** O mesmo episodio con 30-60 min de cola de choiva
  (a mellora 5 do tribunal). En Spotify e iVoox as horas son o limiar; en YouTube, a cola sobe o tempo medio de
  visualización.
- Medir o CTR, a retención aos 2 min, a porcentaxe de Galicia, as horas por plataforma, os subscritores por cada
  1.000 visualizacións e os comentarios.
- **Porta 1 (≈ M0 + 10 semanas):** a do plan v2 §2.4 (PARADA, MÍNIMO ou PLAN), cun dato novo: **¿que plataforma dá
  máis horas por episodio?** Iso decide onde se pon o esforzo.

### Fase 2 · De febreiro a xuño de 2027, só se a porta 1 dá MÍNIMO ou PLAN

- **Serie do Camiño para o Xacobeo 2027:** 4-6 episodios, con fotos propias ou con licenza en pantalla.
- **Pistas pt/en** en 4 episodios, con outros 4 de control (plan v2 §4.4, fase 2).
- Se o promotor levanta o anonimato (§6):
  - preparar a convocatoria da CRTVG (≈ xuño de 2027) cunha tempada **inédita** de 6-8 episodios;
  - unha **oferta B2B dun folio** para 3-5 concellos con patrimonio e turismo (Combarro, O Cebreiro, Samos,
    Allariz...): un episodio da súa historia para durmir e unha audioguía, a prezo pechado.
- Fan funding en canto haxa 500 subscritores e 3.000 h.

**Porta 2 (xuño de 2027):** ¿algún ingreso que non sexa un premio, ou un si da CRTVG? Se non, a canle volve ao
réxime MÍNIMO (un episodio ao mes) como hobby, e publícanse a canalización e o informe de erros para Nós.

### Fase 3 · Segundo semestre de 2027: escalar o que funcionou

Só con datos da fase 2:
- patrocinio de tempada;
- paquetes de pago en iVoox;
- como decisión explícita do promotor, revisar o castelán aos 12 meses (regra do plan v2: só se o galego conserva
  ≥ 40 % do tempo de visualización).

---

## 6. Decisións que precisa o promotor

| # | Decisión | Opcións | O que cambia |
|---|---|---|---|
| M1 | **Anonimato (revisa D6)** | (a) Seguir en anónimo; (b) pseudónimo público cunha persoa identificable para as axudas e os clientes; (c) con nome | (a) Teito de 0-1.500 € ao ano [S]. (b) e (c) abren F, G e H e a petición de fotos aos arquivos |
| M2 | Alta no RETA ou asociación | Non / asociación sen ánimo de lucro / autónomo cando haxa un encargo | O Xacobeo pide RETA, empresa ou entidade sen ánimo de lucro (§9); a CRTVG e o B2B, facturar |
| M3 | **Escoita humana do que se venda** | Si, declarada / non | Sen ela, E, F e H son moi improbables. Non toca o aviso da canle: só cambia nos episodios que de verdade se escoiten |
| M4 | Voz | Agardar por Nós / pasar xa a unha voz CC BY | Fixa a data da primeira publicación |
| M5 | Fotos propias como referencia e como documento | Si / non | Licenza limpa para as sementes e "elemento orixinal" fronte a YouTube |
| M6 | Onde arquivar os mestres (333 MB por episodio) | Disco propio / nube / ningún | Fan falta para Spotify, iVoox e calquera cliente |

---

## 7. Riscos que afectan aos cartos

| Risco | Prob. [S] | Mitigación |
|---|---|---|
| YouTube denega o YPP ou desmonetiza por "contido inauténtico" | 40-60 % se se pide | Elemento orixinal en cada episodio, fotos reais, cadencia lenta. **O plan non depende do YPP** |
| Nós/USC di que non á voz | 20-40 % | Voz CC BY de reserva, probada na fase 0 |
| A comunidade galega reacciona mal a "unha canle de IA" | 15-30 % | Transparencia total (aviso falado e descrición "Como se fai") e fontes en pantalla. Nunca afirmar unha revisión que non existe |
| Non aparece o nicho (a porta 1 dá PARADA) | 20-30 % (plan v2 §2.4) | Custo afundido acoutado; queda o portafolio para F e H se M1 o permite |
| Licenzas das sementes BY-SA mal resoltas | Baixo se se aplica §3.2 | Para sementes, CC0, CC BY ou fotos propias; as BY-SA, só tal cal e co crédito |
| Horas do promotor por riba de D3 (~1 h/semana) | Alto nas fases 0 e 2 | A fase 0 son 6 semanas intensas; vender ao B2B é traballo de persoa, non de máquina |

---

## 8. Que mirar aos 30, 60 e 90 días

- **30 días (≈ 31-10):**
  - meigas publicado e arranxado;
  - resposta de Nós;
  - ¿as sementes quitan as casas inglesas nos planos de proba? Si ou non, cunha folla de contactos.
- **60 días (≈ 30-11):** 3 publicacións e inscrición en Youtubeiras+; primeiras cifras de CTR, retención aos 2 min e
  horas por plataforma.
- **90 días (≈ 31-12):** decisión M1 tomada e proba do nicho a medio camiño. Se M1 é (b) ou (c), borrador da oferta
  B2B e da tempada para a CRTVG.

---

## 9. Contraste das referencias na web (01-10-2026)

Fíxoo Claude con buscas web e lendo as páxinas o 01-10-2026. A columna "Cambio" di o que se corrixiu neste documento.

| Referencia | Resultado | Cambio | Fonte |
|---|---|---|---|
| Youtubeiras+ 2026: prazo, requisitos, premios | **Confirmado.** Do 17-09 ao 15-11-2026 ás 23:59; ≥ 3 publicacións desde o 16-11-2025; maioría en galego; 7 premios con dotación (7.500 €) e un honorífico; as bases non mencionan a IA | Engádese o premio honorífico | https://youtubeiras.gal/bases-youtubeiras-2026/ |
| Limiares do YPP en 2027 | **Confirmado en parte.** Desde o 1-02-2027: 8.000 h en 365 días ou 20 M de visualizacións de Shorts en 90 días; os limiares de fan funding non cambian; non afecta a quen xa está dentro. **O resumo da páxina non menciona os 1.000 subscritores** | Os 1.000 subscritores pasan a [S] | https://blog.youtube/news-and-events/youtube-partner-program-updates-2027-new-opportunities-earn/ |
| Spotify Partner Program en España | **Confirmado.** Desde o 20-10-2026; 3 episodios, 2.000 h e 1.000 persoas de audiencia en 30 días; enderezo legal no mercado. Está orientado a **pódcast en vídeo** | Engádese o enderezo legal e o foco no vídeo | https://dircomfidencial.com/marketing-digital/spotify-expande-a-espana-y-otros-34-mercados-el-programa-para-atraer-a-creadores-de-podcast-en-video-20260918-1216/ ; https://support.spotify.com/us/creators/article/spotify-partner-program/ |
| "O teu Xacobeo" (TU300A) | **Confirmado.** Para actividades de 2027, do 1 ao 31-10-2026; ata 25.000 €; 60 % para persoas autónomas e pemes, 80 % para entidades sen ánimo de lucro; 3 M€ en total | — | https://www.xunta.gal/dog/Publicados/2026/20260325/AnuncioG0256-090326-0002_gl.html |
| Xacobeo 2027 é ano santo | **Confirmado.** O 25-07-2027 cae en domingo; a Porta Santa ábrese o 31-12-2026 | Engádese a data de inicio | https://www.g24.gal/-/conta-atras-para-o-xacobeo-2027-cen-dias-para-converter-galicia-nunha-gran-festa- ; https://vivecamino.com/en/holy-year-2027:-everything-you-need-to-know-about-the-next-xacobeo-no-953/ |
| Convocatoria dixital da CRTVG | **Confirmado (2025):** ata 357.000 € para 15 proxectos en cinco categorías, entre elas divulgación e videopódcast; inéditos e integramente en galego. Resolución: 12 proxectos, ata 25.000 € cada un (300.000 €). **Non atopei convocatoria de 2026** | Importe máximo: "ata 25.000-26.000 €"; a tempada ten que ser inédita | https://www.observatoriodalingua.gal/gl/actualidade/nova/crtvg-lanza-unha-convocatoria-de-contidos-dixitais-en-galego-para-15-novos ; https://www.crtvg.es/w/a-crtvg-producir%C3%A1-12-novos-proxectos-nativos-dixitais-en-galego |
| Política de contido inauténtico | **Confirmado.** "AI-generated content made with generic or unoriginal templates giving the impression of mass production" non se monetiza; "applies to your channel as a whole". A aclaración foi o **16-07-2026**, en tres categorías; segue sendo monetizable o contido con "real research, distinct storytelling" | O plan v2 dicía 13-07-2026: queda corrixido aquí | https://support.google.com/youtube/answer/1311392?hl=en ; https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/ |
| Termos da voz de Brais | **Confirmado.** O dataset é CC BY 4.0, pero "Dissemination of the voice recordings in an open-access manner or their public exposure is strictly prohibited" e o uso limítase "solely for research purposes and for developing artificial intelligence tools focused on linguistic objectives" | Reforza o bloqueo 1 | https://huggingface.co/datasets/proxectonos/Nos_Brais-GL |
| CC BY-SA 4.0: obra derivada e ShareAlike | **Confirmado.** Definición de "Adapted Material" e obriga de compartir coa mesma licenza ou unha compatible; a licenza non restrinxe o uso comercial | — | https://creativecommons.org/licenses/by-sa/4.0/legalcode.en |
| Licenzas de dúas referencias | **Confirmado.** Hórreos de Christof46: CC0 1.0. Carro da Arnoia de Lmbuga: CC BY-SA 3.0 | — | https://commons.wikimedia.org/wiki/File:Horreos-Galicien-IMG_0274a.jpg ; https://commons.wikimedia.org/wiki/File:A_Arnoia_-_Carro_%C3%A1_beira_do_Mi%C3%B1o_-_Galiza-3.jpg |
| Prezo de SDXL-Lightning en Replicate | **Cambiou.** ≈ 0,0057 $ por execución (≈ 175 por dólar) e < 5 s, fronte aos 0,0018 $ anotados en `docs/APRENDIZAJES.md` | Custo das imaxes fóra: ≈ 2,3 USD por episodio | https://replicate.com/bytedance/sdxl-lightning-4step |

**Sen contrastar nesta sesión:** os RPM de España, as comisións de iVoox, a ventá permanente de programas sonoros da
CSAG e as cifras de comparables de YouTube (son as do 29-09/30-09-2026 que están no repo).

---

**Quen fixo que.** Claude escribiu este estudo e fixo o contraste na web o 01-10-2026. Non hai medidas novas do
pipeline. Ningunha persoa o revisou. Os prazos e as bases hai que volvelos mirar o día de actuar.
