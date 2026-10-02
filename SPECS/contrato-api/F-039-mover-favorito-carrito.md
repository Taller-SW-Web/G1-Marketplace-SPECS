# Spec de contrato API — F-039 Mover favorito

`POST /api/v1/wishlist/items/{productId}/move-to-cart` JWT. `200` carrito actualizado y favorito eliminado; `409 STOCK_LIMIT_REACHED`, `422 VARIANT_SELECTION_REQUIRED` con `redirectUrl`, `404 PRODUCT_NOT_AVAILABLE`. Transacción local elimina sólo después de F-016 exitoso.

- [ ] **API-CA-F039-01:** SKU no disponible conserva favorito.
