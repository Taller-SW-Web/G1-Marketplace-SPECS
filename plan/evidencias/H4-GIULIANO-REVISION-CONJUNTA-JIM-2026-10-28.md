# H4 — conformidad de Jim con la demo local y respuesta a revisores

Registro: 28/10/2026, Lima. Funciones F-006–F-010. Fuente: mensaje de Jim compartido por Giuliano en la conversación de trabajo. La conformidad corresponde al recorrido local probado; el mensaje deja el SHA ejecutado y los modos de datos por caso sin especificar. La aceptación del corte desplegado permanece pendiente, tal como indicó Jim.

## Resultado comunicado de la revisión conjunta

Jim informó que revisó con Giuliano la demo local en escritorio y móvil y que el recorrido probado funcionó. Expresó conformidad con esa demo local y dejó pendiente la aceptación del corte desplegado. Esta constancia se vincula a las 30 issues como evidencia funcional del recorrido revisado, sin ampliar la afirmación a casos o modos de datos que el mensaje no enumera.

| Alcance | Resultado registrable |
|---|---|
| Escritorio y móvil, F-006–F-010 | Revisión conjunta local y recorrido probado satisfactorio, según el mensaje aportado |
| G6 REAL frente a fixtures | Se conserva la separación de la evidencia técnica previa; el mensaje no especifica el modo por cada caso |
| Marcas, precio y acceso con JWT | Pendientes explícitos de G6/G7 en el mismo mensaje |
| Revisión técnica de PR | Sebas: Frontend #110. Leo: Backend #237 y contrato G6; la revisión de SPECS #13 conserva sus observaciones |
| Integración y despliegue | Después de revisión/correcciones: coordinar con Andres integración a develop, despliegue y prueba del SHA publicado |
| Cierre de issues | Pendiente del DoD completo; la conformidad local no constituye aceptación del despliegue |

Los datos REAL locales previamente capturados, las pruebas automatizadas con fixtures y los pendientes actuales están en la [auditoría individual de las 30 issues](H4-GIULIANO-AUDITORIA-ISSUES-2026-10-28.md). La conformidad de la demo no libera por sí sola destacados, desempate global de G6, identidad técnica, DAST ni otros criterios que no figuran resueltos.

## Respuesta verificable a las observaciones de Leo

Se releyeron las revisiones de los tres PR y sus conversaciones: no había comentarios inline ni una segunda revisión distinta de las solicitudes del 27/10. Los HEAD actuales conservan las correcciones publicadas el 28/10 y sus checks aprobados; no fue necesario cambiar nuevamente el código ni repetir las mismas suites.

| Observación | Corrección publicada / evidencia | Pendiente |
|---|---|---|
| Backend: demo-no-auth en producción | [provider.ts en cc9ecab](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/blob/cc9ecab/src/catalog/provider.ts) rechaza esa combinación antes de consultar; [regresiones](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/blob/cc9ecab/src/catalog/catalog-review.spec.ts) | Nueva revisión de Leo |
| Backend: orden aplicado | DTO/REAL/MOCK/OpenAPI incluyen sort NAME_ASC/NAME_DESC/null; null conserva el predeterminado del proveedor | Garantía externa de desempate estable sigue explícitamente pendiente de G6 |
| Backend/proxy: timeout | 503/CATALOG_TIMEOUT distingue presupuesto agotado de 503/CATALOG_UNAVAILABLE; mensajes seguros y cancelación del consumidor diferenciada | Homologación final del contrato, sin inventar un nuevo HTTP status |
| Backend: query de home | Cualquier parámetro se rechaza con 400/INVALID_PARAMETERS antes del proveedor; pruebas HTTP incluidas | Nueva revisión de Leo |
| Frontend: selección múltiple frente a singular | [V-006 alineada](../../SPECS/ui/vistas/V-006-catalogo-resultados.md), un ID por categoría/marca con AND; pruebas de select único, CSV y repetidos | Revisión técnica de Sebas/Leo; multiselección requiere otro contrato |
| SPECS: OPEN-03 | Vacío controlado, acción explícita a primera página conservando criterios, sin redirección/retry automático | Aceptación final de la F y del corte desplegado |
| SPECS: alcance amplio | Se mantiene intencionalmente la integración previa de main; [comparación posterior a la base ffe3993](https://github.com/Taller-SW-Web/G1-Marketplace-SPECS/compare/ffe3993...feat/giuliano-hito4) permite aislar el aporte del bloque | Revisión del diff completo; no se atribuye el trabajo de base a Giuliano |

Backend [PR #237](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/pull/237), HEAD cc9ecab: unitarias/contratos/HTTP, build/tipos, seguridad y checks Node 22/24/H4 aprobados. Frontend [PR #110](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/pull/110), HEAD d4be0aa: componentes/proxy, servidor, navegador, build/tipos, seguridad y checks web/H4 aprobados. [Resultados saneados de CI](H4-GIULIANO-AUDITORIA-ISSUES-2026-10-28/ci-results.json).

Esta nota se incorpora al [PR SPECS #13](https://github.com/Taller-SW-Web/G1-Marketplace-SPECS/pull/13) y a las relaciones de las issues. No fusiona los PR, no elimina las solicitudes de cambios de los revisores y no marca sus aprobaciones en su nombre.
