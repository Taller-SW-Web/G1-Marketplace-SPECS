# Spec de contrato API — F-039 Agregar conservando favorito

Decisión solicitada el 28/10/2026; revisión independiente pendiente. Se conservan los IDs de tarea.

`POST /api/v1/wishlist/items/{productId}/add-to-cart` JWT, sin body, query ni Idempotency-Key. `200` devuelve `{productId, cart:{cartId,version,items}}` y conserva el favorito y su fecha. Cada solicitud explícita agrega una unidad. `409 STOCK_LIMIT_REACHED`, `409 CART_CONFLICT` si no hay favorito propio o hay contención, `422 VARIANT_SELECTION_REQUIRED` con `redirectUrl` interna validada, `404 PRODUCT_NOT_AVAILABLE`, `503 CATALOG_UNAVAILABLE/COMMERCE_DATA_UNAVAILABLE`. Reutiliza F-016 dentro de una transacción local; no elimina WishlistItem, no reserva stock y no expone move-to-cart.

- [ ] **API-CA-F039-01:** SKU no disponible conserva favorito.
- [ ] **API-CA-F039-02:** Éxito conserva favorito/createdAt y confirma el incremento transaccional del carrito.
