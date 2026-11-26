# Catálogo H4 — contrato de errores y metadatos

28/10/2026. Corrección de contrato implementada en respuesta a la revisión de Leo; homologación final pendiente. OpenAPI Backend 0.2.0 generado desde código.

| Situación | HTTP | code público | Conducta |
|---|---|---|---|
| G1 agota su presupuesto al esperar G6, o Next al esperar al BFF | 503 | CATALOG_TIMEOUT | Mensaje seguro de espera agotada, reintento explícito; no devuelve vacío ni revela detalles privados |
| G6 devuelve 503, falla red/DTO u otra indisponibilidad | 503 | CATALOG_UNAVAILABLE | Mantiene error y criterios; no se confunde con vacío válido |
| Query en home o filtros | 400 | INVALID_PARAMETERS | Se rechaza cualquier query, incluso claves reconocidas/vacías, antes del proveedor |

Se conserva HTTP 503 y se distingue la causa pública mediante `code`, sin inventar un nuevo status. Un 503 recibido de G6 no se etiqueta automáticamente como timeout. La cancelación del consumidor en Next no se presenta como un timeout confirmado del proveedor. Se mantienen no-store y correlación.

`GET /api/v1/catalog/home` y `filters` no admiten parámetros. Productos acepta sólo los criterios publicados, con una categoría y una marca combinadas con AND. Todas las páginas nuevas incluyen `sort: NAME_ASC | NAME_DESC | null`; null conserva el orden por defecto externo. No certifica desempate global de G6.

`PRODUCTOS_AUTH_MODE=demo-no-auth` es exclusivamente de demo/desarrollo; se rechaza con NODE_ENV=production aunque el flag de integración esté activo. Producción usa service-token y requiere el acuerdo/grant técnico server-only. El modo público de demo no homologa identidad ni despliegue.
