# H4 — catálogo completo conectado en demo local

Giuliano, 26/10/2026, Lima. Continuación de la [revisión propia](H4-GIULIANO-REVISION-PROPIA-2026-10-26.md). Frontend `71fd8de`, rama `feat/giuliano-hito4`. No modifica contratos, despliegues ni estados de issues.

## Defecto reproducido y corrección

Al abrir `/catalogo` sin búsqueda, Next devolvía 503 REAL a los 7 s. G6 devolvía directamente sus 15 productos con el mismo criterio/tamaño de página en unos 11,5 s. El adaptador confirmó `PROVIDER_TIMEOUT`; la consulta no era un catálogo vacío. Búsqueda Nike devolvía cinco productos dentro del presupuesto anterior.

El proxy ahora admite la variable server-only `CATALOG_BFF_TIMEOUT_MS`, entera entre 1000 y 30000 ms. Conserva 8000 ms si falta o es inválida y sigue respetando la cancelación del consumidor. No acepta cambios de presupuesto desde query/header del navegador.

En la demo local conectada se configuraron únicamente los procesos: Backend→G6 20000 ms y Next→Backend 25000 ms. No se modificaron `.env` ni valores por defecto de producción. El incremento permite ensayar con la latencia observada; no corrige la lentitud del proveedor ni certifica cumplimiento de un SLO.

## Verificación ejecutada

| Caso | Resultado |
|---|---|
| Componentes/proxy/DTO | 233 PASS, incluidos ocho casos nuevos de configuración/límites |
| Servidor | 73 PASS |
| Tipos, build Next, lint | PASS; lint sin errores y un warning previo en `OrdersHistory.tsx` |
| Regresiones Playwright de catálogo | 21 PASS contra Next/BFF MOCK |
| Seguridad del commit y artefacto | Todos los controles existentes PASS; SCA runtime/dev cero vulnerabilidades; [metadatos](H4-GIULIANO-CATALOGO-COMPLETO-2026-10-26/frontend-security.json) |
| Navegador conectado, entrada directa `/catalogo` | 15 tarjetas, 200 REAL, unos 12,8 s |
| Navegador conectado, búsqueda Nike | 5 tarjetas, 200 REAL |
| Navegador conectado, click «Todo el catálogo» desde búsqueda | 15 tarjetas, URL sin búsqueda, 200 REAL, unos 11,6 s |
| API Next→BFF→G6: home | 200 REAL, 8 categorías |
| API Next→BFF→G6: orden NAME_ASC, primera página de tamaño 4 | 200 REAL, 4 productos, unos 11,1 s; no acredita orden global entre múltiples páginas |
| API Next→BFF→G6: maestros de filtros | Sigue 503 por marcas; no se reemplazó por fixtures |

Se publican [metadatos saneados de los tres recorridos REAL](H4-GIULIANO-CATALOGO-COMPLETO-2026-10-26/browser-real.json); las capturas permanecen en carpetas locales ignoradas. La demo REAL sigue en localhost:3400 y MOCK en localhost:3500, con procesos separados.

## Límites pendientes

Se usó la API pública de demo G6 en modo `demo-no-auth`, sin token técnico, con el pin contractual existente. No acredita grants G1/G6/G7, homologación bilateral ni despliegue. La ruta de marcas, curaduría de destacados, latencia aceptable, recorrido de dos páginas REAL y aceptación independiente mantienen su verificación aparte. La conexión REAL de esta evidencia corresponde al catálogo; no atribuye integración REAL a otras funcionalidades.
