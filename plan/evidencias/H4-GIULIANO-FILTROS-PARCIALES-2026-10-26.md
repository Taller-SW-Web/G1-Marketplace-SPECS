# H4 — filtros independientes y bloqueos concretos de G6

Giuliano, 26/10/2026 Lima. Rama `feat/giuliano-hito4`, commit Frontend `45d71dc`, publicado sin PR. Se conserva el contrato Backend F-008: el agregado de maestros devuelve 503 ante fallo externo. No se modificó código, infraestructura ni configuración de G6 ni se enviaron mensajes a terceros.

## Diagnóstico del proveedor

| Caso REAL | Resultado observado |
|---|---|
| `GET /api/v1/categorias` | 200 JSON, ocho categorías |
| `GET /api/v1/marcas` | 503, Server Caddy, texto correspondiente al handler estático de servicio pendiente |
| Nike + categoría existente | 200, un producto; búsqueda Nike sin categoría devuelve cinco |
| Nike + `precioMin=0`, con/sin categoría | 503 JSON `SERVICIO_NO_DISPONIBLE`, diagnóstico de adaptador `PROVIDER_HTTP_503`; no es timeout ni el handler estático de marcas |

El código publicado de G6 declara la ruta de marcas en [gateway](https://github.com/Taller-SW-Web/G6-Productos-Ofertas-backend/blob/master/apps/api-gateway/src/routing/contract-routes.ts) hacia Taxonomy, y [TaxonomyController](https://github.com/Taller-SW-Web/G6-Productos-Ofertas-backend/blob/master/apps/taxonomy-svc/src/taxonomy.controller.ts) implementa el sobre `brands`. La [auditoría de red de G6 del 19/10](https://github.com/Taller-SW-Web/G6-Productos-Ofertas-backend/blob/master/ops/oracle/auditorias/2026-10-19_22-32-52_UTC/REDES_CADDY_HTTPS.md) documenta publicación selectiva y handler general estático. Eso orienta la revisión de Caddy; no sustituye inspección de su configuración actual por el responsable.

Precio tiene otro bloqueo: [CommercialService.list](https://github.com/Taller-SW-Web/G6-Productos-Ofertas-backend/blob/master/apps/catalog-svc/src/commercial.service.ts) y el [repositorio](https://github.com/Taller-SW-Web/G6-Productos-Ofertas-backend/blob/master/apps/catalog-svc/src/postgres-catalog.repository.ts) rechazan explícitamente `precioMin`/`precioMax` con una excepción 503. El servicio deja pendiente la semántica de precio por producto y la frontera con Pricing. El rechazo se reprodujo a través del adaptador.

## Mejora de G1

- Si falla el agregado de maestros, la UI solicita categorías por la lectura existente `home`, validada. Esta lectura de recuperación no se hace cuando el agregado está disponible.
- Sólo el selector sin maestro queda deshabilitado. Precio conserva validación propia y puede enviarse al proveedor; su disponibilidad REAL no se afirma mientras G6 lo rechace.
- Se conservan URL, borrador al reintentar y IDs ya aplicados aunque no se conozca temporalmente su etiqueta. Las categorías recuperadas aportan sus nombres reales a los chips.
- El error de marcas permanece visible y reintentable. No se inventan opciones ni se construyen maestros con una página de productos.
- La API agregada de Backend conserva su 503 y su DTO. No hay filtrado local de páginas incompletas ni cambio de contratos.

## Verificación local

- Componentes/proxy/DTO: 236 PASS, con tres casos nuevos de fallo parcial, preservación de borrador/IDs y etiquetas.
- Tipos y lint: PASS; un warning previo de `OrdersHistory.tsx`, sin errores.
- Build Next: PASS.
- Playwright catálogo: 23 PASS, dos recorridos nuevos para fallo de marcas y fallo de ambos maestros en móvil. Al ajustar las pruebas nuevas se corrigieron el conteo de lecturas —la cabecera ya lee home— y la cardinalidad esperada de la intersección de fixtures.
- Tras ajustar sólo el aviso para no prometer precio REAL se recompiló y se repitieron los seis recorridos de filtros: PASS.
- Seguridad del commit/build final: todos los controles existentes PASS, SCA runtime/dev cero vulnerabilidades; [metadatos saneados](H4-GIULIANO-FILTROS-PARCIALES-2026-10-26/frontend-security.json).
- Navegador REAL: categorías y controles independientes, categoría con un producto y limpieza que conserva búsqueda/restaura cinco productos, PASS. Precio quedó registrado como `BLOCKED_G6`, 503; [metadatos de navegador](H4-GIULIANO-FILTROS-PARCIALES-2026-10-26/browser-real.json) y [sondeos por criterio](H4-GIULIANO-FILTROS-PARCIALES-2026-10-26/provider-filters.json).

Los informes personales y diagnóstico preparado para G6 se conservan en carpetas locales ignoradas.

El push inició el [CI #40445526383](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/actions/runs/40445526383) del HEAD `45d71dc`; seguía en ejecución al registrar esta evidencia. Los PASS locales no se atribuyen a esa corrida hasta comprobar su resultado. El workflow no despliega.

## Pendiente para completar F-008

G6 debe publicar la lectura de marcas a través de Caddy/Gateway/Taxonomy y confirmar con G7 cliente `modulo-marketplace`, permiso `catalogo:leer` y audiencia `api-productos`. Para precio, definir la regla por producto con Pricing e implementar el filtro global antes de total/paginación, incluidos límites y combinación de criterios. Repetir lectura autorizada de maestros, marca/precio, positivos/vacíos/negativos y varias páginas. Este avance no cierra INT ni aceptación independiente.
