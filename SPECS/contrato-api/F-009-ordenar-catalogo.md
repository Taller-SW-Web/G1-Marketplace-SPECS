# Spec de contrato API — F-009 Ordenamiento

`GET /api/v1/catalog/products?sort=PRICE_ASC` valida enum y delega orden estable a Catálogo/Pricing; `400 INVALID_SORT`. Respuesta incluye sort aplicado y página; `I-01` pendiente.

- [ ] **API-CA-F009-01:** Empates tienen orden estable por identificador.
