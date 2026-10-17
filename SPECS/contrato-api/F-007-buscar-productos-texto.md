# Spec de contrato API — F-007 Búsqueda

`GET /api/v1/catalog/products?q={texto}&page=0&pageSize=24` público. `q` 2–120; `400 INVALID_SEARCH_QUERY`; `200` tarjetas activas y página; `503 CATALOG_UNAVAILABLE`. BFF registra hash de query; externo `I-01`.

Ajuste 16/10/2026 solicitado por Giuliano, en revisión: `ProductCardDTO.image` admite `{url, alt}` o `null`. `images` omitido o `[]` en una tarjeta válida de G6 produce `image: null`; se conserva el producto y toda la metadata de paginación. Frontend muestra un placeholder local accesible. La validación de los demás campos, formato de imágenes, HTTPS y medios permitidos sigue aplicándose.

- [ ] **API-CA-F007-01:** Query inválida no llega a Catálogo.
