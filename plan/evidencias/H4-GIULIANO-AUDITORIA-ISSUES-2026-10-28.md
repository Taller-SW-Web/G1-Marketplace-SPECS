# H4 — auditoría de las 30 issues de Giuliano

28/10/2026, Lima. Auditoría individual de títulos, trabajo, DoD, dependencias y cuatro niveles de evidencia de las 30 issues asignadas. Alcance F-006–F-010: 10 Frontend y 20 Backend. La issue histórica SPECS #5 ya cerrada no pertenece a este lote.

## Resultado de cierre

Actualización posterior: se incorpora la [conformidad de Jim con la demo local conjunta en escritorio y móvil](H4-GIULIANO-REVISION-CONJUNTA-JIM-2026-10-28.md), comunicada por Giuliano. Acredita el recorrido local revisado; no equivale a revisión técnica de Sebas/Leo ni a aceptación del SHA desplegado. El cierre completo y los bloqueos por operación conservan sus criterios.

**30 revisadas. Ninguna cumple todavía todos los requisitos de cierre escritos.** Las issues exigen revisión independiente/gates y prueba en despliegue; los tres PR siguen abiertos y los tres tienen una revisión de Leo con cambios solicitados al comenzar esta auditoría. Se corrige el código/contrato y se prepara nueva revisión, sin autoaprobar ni fusionar PR. No se cambia el DoD ni se cierra INT con fixtures.

## Correcciones y pruebas completadas

- Backend `cc9ecab9eee424b0c1b024d778b6f906f1fac2b5`: bloqueo de demo-no-auth en producción, home sin query, sort explícito/null y 503/CATALOG_TIMEOUT separado de CATALOG_UNAVAILABLE. OpenAPI 0.2.0 requerido y reproducible.
- Frontend `d4be0aa3cf35a2d1e0bda9c40cd9c9bf105dfd16`: error de timeout seguro y reintentable, cancelación del consumidor diferenciada y validación aditiva del metadato sort; tolera versión previa durante el despliegue.
- V-006/O-001/API/UI/funcional alineadas con un ID de categoría y uno de marca, AND; no CSV ni filtrado local de páginas. OPEN-03 define primera página explícita conservando criterios. La elección técnica no acredita aceptación final.
- Backend: 186 pruebas unitarias, 17 contratos HTTP locales y 31 HTTP de catálogo PASS; tipos/build y esquema OpenAPI PASS.
- Frontend: 242 componentes/proxy, 73 servidor y 25 recorridos de navegador MOCK PASS; tipos/lint/build PASS, con warning previo en OrdersHistory.
- Seguridad de ambos commits/artefactos: [Backend](H4-GIULIANO-AUDITORIA-ISSUES-2026-10-28/be-security.json) y [Frontend](H4-GIULIANO-AUDITORIA-ISSUES-2026-10-28/fe-security.json), todos los controles existentes PASS. Se conservan límites de SAST/inventario; no es aprobación jurídica ni DAST de staging.

## Estado externo y despliegue

[Sondeo saneado del 28/10 con timestamps y correlación](H4-GIULIANO-AUDITORIA-ISSUES-2026-10-28/provider-now.json): G6 categorías 200/8; marcas 503 de Caddy; precio 503 SERVICIO_NO_DISPONIBLE; home y productos de la web pública G1 503. No se atribuye un SHA a ese despliegue. Consultas de lectura pública sin JWT técnico; no certifican grants.

Los recorridos REAL locales anteriores y la validación manual comunicada por Giuliano (paginación, orden, categoría y móvil) son evidencia parcial válida; no se convierten en prueba autenticada o de despliegue. Persisten destacados/decisión de PO, maestro de marcas, precio REAL y garantía de desempate de G6.

## Matriz de las 30 issues

| TASK | Issue | Avance propio | Para cierre |
|---|---|---|---|
| TASK-F006-FE-001 | [Frontend #27](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/27) | En revisión; abierta | Revisión independiente y despliegue. Faltan curaduría/campos de destacados (G-FEATURED, Jim/PO y G6) y aceptación del recorrido de favoritos/autenticación aplicable. |
| TASK-F006-BE-001 | [Backend #44](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/44) | En revisión; abierta | Revisión independiente y despliegue. Faltan curaduría/campos de destacados (G-FEATURED, Jim/PO y G6) y aceptación del recorrido de favoritos/autenticación aplicable. |
| TASK-F006-INT-001 | [Backend #45](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/45) | Bloqueado; abierta | Revisión independiente y despliegue. Faltan curaduría/campos de destacados (G-FEATURED, Jim/PO y G6) y aceptación del recorrido de favoritos/autenticación aplicable. |
| TASK-F006-QA-001 | [Frontend #28](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/28) | En progreso; abierta | Revisión independiente y despliegue. Faltan curaduría/campos de destacados (G-FEATURED, Jim/PO y G6) y aceptación del recorrido de favoritos/autenticación aplicable. |
| TASK-F006-QA-002 | [Backend #46](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/46) | En progreso; abierta | Revisión independiente y despliegue. Faltan curaduría/campos de destacados (G-FEATURED, Jim/PO y G6) y aceptación del recorrido de favoritos/autenticación aplicable. DAST staging/revisión de riesgos. |
| TASK-F006-DOC-001 | [Backend #47](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/47) | En progreso; abierta | Revisión independiente y despliegue. Faltan curaduría/campos de destacados (G-FEATURED, Jim/PO y G6) y aceptación del recorrido de favoritos/autenticación aplicable. Dependencias INT/QA y revisión documental. |
| TASK-F007-FE-001 | [Frontend #29](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/29) | En revisión; abierta | Revisión independiente y despliegue. Falta acreditar identidad técnica/grants G1–G6/G7 y el recorrido desde el corte desplegado; demo pública sin JWT no los sustituye. |
| TASK-F007-BE-001 | [Backend #48](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/48) | En revisión; abierta | Revisión independiente y despliegue. Falta acreditar identidad técnica/grants G1–G6/G7 y el recorrido desde el corte desplegado; demo pública sin JWT no los sustituye. |
| TASK-F007-INT-001 | [Backend #49](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/49) | Bloqueado; abierta | Revisión independiente y despliegue. Falta acreditar identidad técnica/grants G1–G6/G7 y el recorrido desde el corte desplegado; demo pública sin JWT no los sustituye. |
| TASK-F007-QA-001 | [Frontend #30](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/30) | En progreso; abierta | Revisión independiente y despliegue. Falta acreditar identidad técnica/grants G1–G6/G7 y el recorrido desde el corte desplegado; demo pública sin JWT no los sustituye. |
| TASK-F007-QA-002 | [Backend #50](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/50) | En progreso; abierta | Revisión independiente y despliegue. Falta acreditar identidad técnica/grants G1–G6/G7 y el recorrido desde el corte desplegado; demo pública sin JWT no los sustituye. DAST staging/revisión de riesgos. |
| TASK-F007-DOC-001 | [Backend #51](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/51) | En progreso; abierta | Revisión independiente y despliegue. Falta acreditar identidad técnica/grants G1–G6/G7 y el recorrido desde el corte desplegado; demo pública sin JWT no los sustituye. Dependencias INT/QA y revisión documental. |
| TASK-F008-FE-001 | [Frontend #31](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/31) | En revisión; abierta | Revisión independiente y despliegue. G6 sigue 503 en marcas (Caddy) y precio (SERVICIO_NO_DISPONIBLE); falta soporte autorizado por operación además de homologar el contrato singular. |
| TASK-F008-BE-001 | [Backend #52](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/52) | En revisión; abierta | Revisión independiente y despliegue. G6 sigue 503 en marcas (Caddy) y precio (SERVICIO_NO_DISPONIBLE); falta soporte autorizado por operación además de homologar el contrato singular. |
| TASK-F008-INT-001 | [Backend #53](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/53) | Bloqueado; abierta | Revisión independiente y despliegue. G6 sigue 503 en marcas (Caddy) y precio (SERVICIO_NO_DISPONIBLE); falta soporte autorizado por operación además de homologar el contrato singular. |
| TASK-F008-QA-001 | [Frontend #32](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/32) | En progreso; abierta | Revisión independiente y despliegue. G6 sigue 503 en marcas (Caddy) y precio (SERVICIO_NO_DISPONIBLE); falta soporte autorizado por operación además de homologar el contrato singular. |
| TASK-F008-QA-002 | [Backend #54](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/54) | En progreso; abierta | Revisión independiente y despliegue. G6 sigue 503 en marcas (Caddy) y precio (SERVICIO_NO_DISPONIBLE); falta soporte autorizado por operación además de homologar el contrato singular. DAST staging/revisión de riesgos. |
| TASK-F008-DOC-001 | [Backend #55](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/55) | En progreso; abierta | Revisión independiente y despliegue. G6 sigue 503 en marcas (Caddy) y precio (SERVICIO_NO_DISPONIBLE); falta soporte autorizado por operación además de homologar el contrato singular. Dependencias INT/QA y revisión documental. |
| TASK-F009-FE-001 | [Frontend #33](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/33) | En revisión; abierta | Revisión independiente y despliegue. Falta confirmar con G6 el desempate global estable por identificador; el campo sort y MOCK no acreditan esa garantía externa. |
| TASK-F009-BE-001 | [Backend #56](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/56) | En revisión; abierta | Revisión independiente y despliegue. Falta confirmar con G6 el desempate global estable por identificador; el campo sort y MOCK no acreditan esa garantía externa. |
| TASK-F009-INT-001 | [Backend #57](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/57) | Bloqueado; abierta | Revisión independiente y despliegue. Falta confirmar con G6 el desempate global estable por identificador; el campo sort y MOCK no acreditan esa garantía externa. |
| TASK-F009-QA-001 | [Frontend #34](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/34) | En progreso; abierta | Revisión independiente y despliegue. Falta confirmar con G6 el desempate global estable por identificador; el campo sort y MOCK no acreditan esa garantía externa. |
| TASK-F009-QA-002 | [Backend #58](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/58) | En progreso; abierta | Revisión independiente y despliegue. Falta confirmar con G6 el desempate global estable por identificador; el campo sort y MOCK no acreditan esa garantía externa. DAST staging/revisión de riesgos. |
| TASK-F009-DOC-001 | [Backend #59](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/59) | En progreso; abierta | Revisión independiente y despliegue. Falta confirmar con G6 el desempate global estable por identificador; el campo sort y MOCK no acreditan esa garantía externa. Dependencias INT/QA y revisión documental. |
| TASK-F010-FE-001 | [Frontend #35](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/35) | En revisión; abierta | Revisión independiente y despliegue. OPEN-03 queda definido técnicamente: vacío controlado y regreso explícito a primera página; faltan aceptación independiente y validación desplegada. |
| TASK-F010-BE-001 | [Backend #60](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/60) | En revisión; abierta | Revisión independiente y despliegue. OPEN-03 queda definido técnicamente: vacío controlado y regreso explícito a primera página; faltan aceptación independiente y validación desplegada. |
| TASK-F010-INT-001 | [Backend #61](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/61) | Bloqueado; abierta | Revisión independiente y despliegue. OPEN-03 queda definido técnicamente: vacío controlado y regreso explícito a primera página; faltan aceptación independiente y validación desplegada. |
| TASK-F010-QA-001 | [Frontend #36](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/36) | En progreso; abierta | Revisión independiente y despliegue. OPEN-03 queda definido técnicamente: vacío controlado y regreso explícito a primera página; faltan aceptación independiente y validación desplegada. |
| TASK-F010-QA-002 | [Backend #62](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/62) | En progreso; abierta | Revisión independiente y despliegue. OPEN-03 queda definido técnicamente: vacío controlado y regreso explícito a primera página; faltan aceptación independiente y validación desplegada. DAST staging/revisión de riesgos. |
| TASK-F010-DOC-001 | [Backend #63](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/63) | En progreso; abierta | Revisión independiente y despliegue. OPEN-03 queda definido técnicamente: vacío controlado y regreso explícito a primera página; faltan aceptación independiente y validación desplegada. Dependencias INT/QA y revisión documental. |

## Dependencias y responsables de liberación

- Sebastian: revisor principal de las 30 tareas. Leo: nueva revisión de los contratos y correcciones de PR #237/#110/#13.
- Andres/Fernando: OPS #200/#201/#206, entorno y despliegue del corte; la evidencia de CI no sustituye CD ni el recorrido web desplegado.
- Jim/PO y G6: curaduría de destacados. Leo/Jim con G6/G7: identidad técnica y soporte/runtime de marcas/precio; G6 confirma el desempate global.
- DOC depende de INT/QA-001/QA-002; su trazabilidad local se actualiza ahora, pero su cierre completo conserva esas dependencias.

Los PR y cada issue se relacionan con esta auditoría y sus commits. Se registran avances verificables, sin usar palabras de cierre automático en los PR. Los informes personales permanecen ignorados y fuera de Git/GitHub.

## Verificación de publicación y CI

Se actualizaron las 30 issues con el bloque de auditoría, sus PR y el pendiente específico; se conservó su DoD y su estado abierto. Los tres PR también incluyen la matriz cruzada de 30 referencias. No se fusionaron PR ni se atribuyó aprobación a los revisores.

[Resultados saneados de CI](H4-GIULIANO-AUDITORIA-ISSUES-2026-10-28/ci-results.json): Backend cc9ecab pasó H4 verify y los checks de PR en Node 22/24; Frontend d4be0aa pasó H4 verify y el check web del PR. CI aprobado no sustituye los gates de despliegue, DAST o revisión independiente.

## Referencias de pruebas por función

| F | Pruebas y alcance propio |
|---|---|
| F-006 | FE tests/catalog.spec.ts cubre inicio/vacío/error; tests/components/wishlist.test.tsx cubre el diálogo compartido sin sesión. BE src/catalog/catalog.spec.ts prueba proyección, actividad y allowlist de medios. Curaduría y aceptación del recorrido completo siguen pendientes. |
| F-007 | FE tests/catalog.spec.ts: longitudes, vacío, cancelación, escape de texto y reintento. BE src/catalog/catalog.spec.ts y catálogo HTTP: validación y errores del adaptador. |
| F-008 | FE tests/catalog-h4.spec.ts y tests/components/catalog-controls-h4.test.tsx: borrador, rango, chips, recuperación parcial y foco. BE src/catalog/catalog-h4.spec.ts y catalog-review.spec.ts: AND, IDs únicos y validación antes del proveedor. |
| F-009 | FE tests/catalog-h4.spec.ts: orden entre páginas y metadato sort. BE catalog-review.spec.ts prueba ambos mapeos/metadata; catalog-h4.spec.ts verifica orden global de fixtures. El desempate externo no está certificado. |
| F-010 | FE tests/catalog.spec.ts y catalog-h4.spec.ts: límites y recuperación con contexto. BE src/catalog/catalog.spec.ts, catalog-h4.spec.ts y HTTP: límites/metadata/duplicados. Prueba desplegada pendiente. |
