# Spec de contrato API — F-006 Inicio

`GET /api/v1/catalog/home` público: `categories[]` y `featuredProducts[]` con id/nombre/slug/imagen/tarjeta comercial. `featuredProducts[]` es una composición del BFF de Marketplace, no un campo atribuido al contrato actual de Productos. Su selección editorial por IDs es propuesta pendiente de homologar (`F-P1-04`); cada tarjeta se obtiene/valida contra la proyección comercial de Productos. Si no existe selección aprobada o el producto no está activo/elegible, se devuelve arreglo vacío u omite esa tarjeta. `200` admite arreglos vacíos; `503 CATALOG_UNAVAILABLE` cuando no puede obtenerse el catálogo necesario. Integración externa bajo `I-01`.

Ajuste 16/10/2026 solicitado por Giuliano, en revisión: `ProductCardDTO.image` admite `{url, alt}` o `null`. El adaptador transforma `images` omitido o `[]` de G6 en `image: null`; la interfaz muestra un placeholder local. Se conservan identidad, slug y elegibilidad, sin inventar una imagen del proveedor. Un campo de imágenes mal formado o una URL insegura mantiene el error técnico; no se reemplaza por placeholder para ocultarlo. G-FEATURED sigue pendiente.

- [ ] **API-CA-F006-01:** No devuelve datos administrativos.

**Prueba de entorno 17/10/2026:** el [ensayo conectado](../../plan/evidencias/H3-GIULIANO/H3-G6-DEMO-2026-10-17.md) verifica categorías 200 REAL en el proyecto usando el modo temporal sin JWT publicado por G6 (PR #130). El DTO público y la ausencia de destacados inventados se conservan. Esta excepción de demo se selecciona en Backend con `PRODUCTOS_AUTH_MODE=demo-no-auth`; no modifica el requisito de token del modo predeterminado ni acredita autenticación G7, homologación o aceptación del criterio.


Alineación del 28/10/2026: [errores, metadatos y límites comunes de catálogo H4](CATALOGO-H4-ERRORES-Y-METADATOS.md). La distinción pública de timeout usa 503/CATALOG_TIMEOUT; otras indisponibilidades conservan 503/CATALOG_UNAVAILABLE. Home/filtros rechazan query. No implica aceptación ni liberación de I-01.
