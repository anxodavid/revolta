# Cronómetro do dossier semiautomático: Samos (29-09-2026)

Medidas de reloxo [P] das partes de máquina; a parte humana medida en **volume** (o que a persoa ten que buscar e
ler) e convertida a minutos cun suposto de velocidade [S]. Detalle e conclusións no plan (§3.3).

| Paso | Quen | Medido | Minutos |
|---|---|---|---|
| 1 Buscar fontes (API de busca de Galipedia) e escoller 4 | persoa | 10 resultados; 4 escollidos (3 gl + 1 es) | [S] 10-20 |
| 2 Descargar e limpar o texto (`dossier.py fontes`) | máquina | 13,6 s e 16,0 s (dúas execucións); 2.852 palabras (865 + 243 + 653 + 1.091) | [P] 0,3 |
| 3 Extraer feitos con cita (LLM, `prompts/dossier.md`) | máquina | 45 feitos; ≈ 4.000 tokens de entrada e ≈ 3.500 de saída | [S] 1-3 por API |
| 4 Comprobar citas (`dossier.py comprobar`) | máquina | 0,02 s; 45/45 citas atopadas; 2 fóra por conflito (1835 fronte a 1836); proba negativa 0/3 aceptadas | [P] 0,0 |
| 5 Ler o informe (rexeitados, conflitos, lendas; non os 43 feitos) | persoa | ≈ 120 palabras de informe | [S] 2-5 |
| **Total por dossier de 4 fontes** | | | **≈ 15-30 min, dos que 12-25 son de persoa** |

Rendemento: 2.852 palabras de fonte → 43 feitos usables (611 palabras de dossier).
