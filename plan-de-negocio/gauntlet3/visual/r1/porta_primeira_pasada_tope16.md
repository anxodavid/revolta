# Puerta de revisión de la hoja de prueba (automático)

Modelo `lightning` (1344x768, 4 pasos), estilo `filme`, revisor versión 5. Generación + revisión: 24.4 min de reloj; gradación 10 s.

| Plano | Fase | Tipo | Intentos | Problemas de los intentos rechazados | Escogida | s generación | s revisión |
|---|---|---|---|---|---|---|---|
| 1 | gancho | detalle | 2 | 0: man sen corpo (1) | 1 (ok) | 34.4, 32.9 | 16.7, 16.6 |
| 2 | gancho | xeral | 4 | 0: obxectos modernos; 1: obxectos modernos; 2: obxectos modernos | 3 (ok) | 32.7, 33.2, 30.0, 33.6 | 17.7, 17.4, 15.9, 19.6 |
| 3 | gancho | primeiro_plano | 1 | - | 0 (ok) | 30.1 | 16.6 |
| 4 | gancho | plano_medio | 1 | - | 0 (ok) | 28.7 | 19.8 |
| 5 | transicion | xeral | 1 | - | 0 (ok) | 30.8 | 19.4 |
| 6 | transicion | contraluz | 2 | 0: interior moderno, paisaxe seca (CLIP) | 1 (ok) | 31.0, 31.5 | 19.5, 20.3 |
| 7 | transicion | primeiro_plano | 1 | - | 0 (ok) | 33.3 | 17.9 |
| 8 | transicion | plano_medio | 3 | 0: arquetipo repetido: camiñantes de costas (1 xa, tope 1); 1: man sen corpo (1) | 2 (ok) | 35.3, 31.2, 33.8 | 17.3, 17.8, 18.1 |
| 9 | calma | paisaxe | 1 | - | 0 (ok) | 33.0 | 17.1 |
| 10 | calma | bodegon | 1 | - | 0 (ok) | 33.2 | 16.9 |
| 11 | calma | plano_medio | 1 | - | 0 (ok) | 36.5 | 19.2 |
| 12 | calma | contraluz | 4 | 0: arquetipo repetido: persoa á lareira (1 xa, tope 1); 1: interior moderno, arquetipo repetido: persoa á lareira (1 xa, tope 1); 5: tellados laranxas | 3 (ok, reserva) | 31.5, 34.9, 30.5, 32.6 | 17.8, 18.7, 18.2, 19.8 |
| 13 | durmir | paisaxe | 1 | - | 0 (ok) | 34.5 | 26.1 |
| 14 | durmir | bodegon | 1 | - | 0 (ok) | 35.9 | 16.3 |
| 15 | durmir | plano_medio | 3 | 0: arquetipo repetido: persoa á lareira (1 xa, tope 1); 1: arquetipo repetido: persoa á lareira (1 xa, tope 1) | 2 (ok, reserva) | 31.7, 37.2, 33.9 | 17.7, 17.7, 17.2 |
| 16 | durmir | detalle | 1 | - | 0 (ok) | 36.9 | 18.7 |

Imágenes generadas: 28 para 16 planos; aprobadas a la primera: 10; tras regenerar: 6; sin aprobar: 0.
Segundos por imagen (generación): mediana 33.2, media 33.0; revisión: mediana 17.8, media 18.3.
Rechazos por motivo: {"man sen corpo": 2, "obxectos modernos": 3, "interior moderno": 2, "paisaxe seca": 1, "arquetipo repetido": 5, "tellados laranxas": 1}.
