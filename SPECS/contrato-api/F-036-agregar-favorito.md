# Spec de contrato API — F-036 Agregar favorito

`POST /api/v1/wishlist/items` JWT, cuerpo `{"productId":"PRD-1"}`. `201` creado o `200` existente; `401`, `404 PRODUCT_NOT_AVAILABLE`, `503 CATALOG_UNAVAILABLE`. BFF deriva cliente JWT y hace upsert local; no acepta customerId.

- [ ] **API-CA-F036-01:** Mismo producto/cliente produce una fila.
