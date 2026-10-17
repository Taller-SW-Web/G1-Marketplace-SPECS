# Spec de contrato API — F-007 Búsqueda

`GET /api/v1/catalog/products?q={texto}&page=0&pageSize=24` público. `q` 2–120; `400 INVALID_SEARCH_QUERY`; `200` tarjetas activas y página; `503 CATALOG_UNAVAILABLE`. BFF registra hash de query; externo `I-01`.

Ajuste 16/10/2026 solicitado por Giuliano, en revisión: `ProductCardDTO.image` admite `{url, alt}` o `null`. `images` omitido o `[]` en una tarjeta válida de G6 produce `image: null`; se conserva el producto y toda la metadata de paginación. Frontend muestra un placeholder local accesible. La validación de los demás campos, formato de imágenes, HTTPS y medios permitidos sigue aplicándose.

**Prueba de entorno 17/10/2026:** el [ensayo conectado](../../plan/evidencias/H3-GIULIANO/H3-G6-DEMO-2026-10-17.md) verifica una búsqueda real que recibe 503 del proveedor y se presenta como `CATALOG_UNAVAILABLE`, con correlación y Reintentar. El modo temporal sin JWT se configura sólo en Backend; no cambia este contrato público ni sustituye el fallo por una página vacía o MOCK. La búsqueda real positiva y su paginación siguen pendientes de respuesta funcional del proveedor.

- [ ] **API-CA-F007-01:** Query inválida no llega a Catálogo.
