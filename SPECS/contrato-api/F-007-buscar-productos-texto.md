# Spec de contrato API — F-007 Búsqueda

`GET /api/v1/catalog/products?q={texto}&page=0&pageSize=24` público. `q` 2–120; `400 INVALID_SEARCH_QUERY`; `200` tarjetas activas y página; `503 CATALOG_UNAVAILABLE`. BFF registra hash de query; externo `I-01`.

- [ ] **API-CA-F007-01:** Query inválida no llega a Catálogo.
