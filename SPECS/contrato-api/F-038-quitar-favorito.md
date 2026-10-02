# Spec de contrato API — F-038 Quitar favorito

`DELETE /api/v1/wishlist/items/{productId}` JWT; `204` si se elimina o ya ausente; `401`, `400 INVALID_PRODUCT_ID`. Delete local por cliente derivado del JWT.

- [ ] **API-CA-F038-01:** No puede borrar favorito ajeno.
