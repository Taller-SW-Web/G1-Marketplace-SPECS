# Spec de contrato API — F-006 Inicio

`GET /api/v1/catalog/home` público: `categories[]` y `featuredProducts[]` con id/nombre/slug/imagen/tarjeta comercial. `featuredProducts[]` es una composición del BFF de Marketplace, no un campo atribuido al contrato actual de Productos. Su composición sigue la prioridad confirmada el 03/11/2026: destacados definidos, históricos más vendidos y aleatorios sólo cuando se confirma que todavía no hay historial. Cada tarjeta se obtiene/valida contra la proyección comercial de Productos; la fuente real del ranking aún debe homologarse (`F-P1-04`). Con la selección automática desactivada se conserva el vacío seguro; con ella habilitada, una selección definida vacía pasa al ranking y una ausencia comprobada de historial permite aleatorios. Un fallo de la fuente no equivale a historial vacío. Se omiten tarjetas no elegibles. `200` admite arreglos vacíos; `503 CATALOG_UNAVAILABLE` cuando no puede obtenerse el catálogo necesario. Integración externa bajo `I-01`.

Ajuste 16/10/2026 solicitado por Giuliano, en revisión: `ProductCardDTO.image` admite `{url, alt}` o `null`. El adaptador transforma `images` omitido o `[]` de G6 en `image: null`; la interfaz muestra un placeholder local. Se conservan identidad, slug y elegibilidad, sin inventar una imagen del proveedor. Un campo de imágenes mal formado o una URL insegura mantiene el error técnico; no se reemplaza por placeholder para ocultarlo. G-FEATURED sigue pendiente.

- [ ] **API-CA-F006-01:** No devuelve datos administrativos.

**Prueba de entorno 17/10/2026:** el [ensayo conectado](../../plan/evidencias/H3-GIULIANO/H3-G6-DEMO-2026-10-17.md) verifica categorías 200 REAL en el proyecto usando el modo temporal sin JWT publicado por G6 (PR #130). El DTO público y la ausencia de destacados inventados se conservan. Esta excepción de demo se selecciona en Backend con `PRODUCTOS_AUTH_MODE=demo-no-auth`; no modifica el requisito de token del modo predeterminado ni acredita autenticación G7, homologación o aceptación del criterio.


Alineación del 28/10/2026: [errores, metadatos y límites comunes de catálogo H4](CATALOGO-H4-ERRORES-Y-METADATOS.md). La distinción pública de timeout usa 503/CATALOG_TIMEOUT; otras indisponibilidades conservan 503/CATALOG_UNAVAILABLE. Home/filtros rechazan query. No implica aceptación ni liberación de I-01.

## Preparación editorial — 03/11/2026

Se preparó la propuesta de selección ordenada por IDs en configuración de G1. El adaptador usa la operación comercial publicada `GET /api/v1/productos/{productoId}?canal=MARKETPLACE`; valida identidad y proyecta el mismo ProductCardDTO. No se añade un campo público de configuración ni se inventa una ruta del owner.

La propuesta tiene máximo técnico de ocho IDs, sin duplicados, tres lecturas simultáneas y un deadline compartido de Home. Se omiten ausencia comercial confirmada, inactividad conocida o slug no publicable; fallos técnicos e imágenes inseguras mantienen error. REAL exige habilitación y aprobación editorial explícitas además de I-01. Los defaults mantienen la selección desactivada.

La demo usa dos IDs sintéticos y no requiere fingir aprobación del grupo. La elección real de IDs, su mantenimiento editorial y la aceptación de la política vacía siguen pendientes. Esta preparación no libera G-FEATURED ni cambia el DTO o el nivel de evidencia.


## Regla confirmada por Giuliano a partir del mensaje de Jim — 03/11/2026

**Prioridad:** destacados definidos → históricos más vendidos → aleatorios sólo cuando todavía no hay historial. Esto sustituye la selección exclusivamente editorial propuesta en el corte anterior. La confirmación de la prioridad y de la métrica no certifica revisión de código, contrato aceptado por el proveedor ni despliegue.

Giuliano eligió documentar como criterio de históricos las **unidades vendidas del canal MARKETPLACE, en todo el historial, con pago confirmado, descontando devoluciones confirmadas**. Se agrupan por producto, no por variante/SKU. La fuente autorizada y su contrato siguen pendientes de homologación; no se calculó un ranking con datos de compradores o importes administrativos.

La alternativa se evalúa al quedar vacía la selección anterior. Una selección definida parcialmente elegible se conserva sin rellenarla con otras fuentes. Si hay historial pero ninguno de sus productos es publicable, la sección puede quedar vacía: no se afirma que no haya historial. Un fallo o ausencia de la fuente de ventas es indisponibilidad técnica y no habilita aleatorios.

Preparación técnica: muestreo sin reemplazo sobre posiciones de páginas ordenadas, hasta ocho tarjetas, deadline compartido y errores seguros. REAL requiere un adaptador autorizado de ranking; aún no está conectado. Ver [decisión, fuente pendiente y límites](../../plan/coordinacion/DESTACADOS-HISTORICOS-2026-11-03.md). No cambia el DTO público ni acredita integración/despliegue.
