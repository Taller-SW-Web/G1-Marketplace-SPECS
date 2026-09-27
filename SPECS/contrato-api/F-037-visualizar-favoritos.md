# Spec de contrato API — F-037 Favoritos

`GET /api/v1/wishlist` JWT devuelve favoritos del titular ordenados por `createdAt DESC`, enriquecidos con slug/nombre/imagen/estado. `200` arreglo vacío, `401`, `503 CATALOG_UNAVAILABLE`. No devuelve customerId.

- [ ] **API-CA-F037-01:** Ítems ajenos nunca aparecen.
