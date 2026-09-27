# Spec de contrato API — F-021 Mover un ítem del carrito a favoritos

`POST /api/v1/carts/current/items/{sku}/move-to-wishlist` requiere JWT; cuerpo vacío.

Respuesta `200`: `{"data":{"cartId":"CART-1","version":6,"productId":"PRD-1","wishlistCreated":false}}`.

Errores: `401 UNAUTHENTICATED`, `404 CART_ITEM_NOT_FOUND`, `404 PRODUCT_NOT_AVAILABLE`, `409 CART_CONFLICT`, `503 CATALOG_UNAVAILABLE`. El BFF resuelve `productId` desde la línea, verifica elegibilidad y ejecuta upsert de `WishlistItem` + delete de `CartItem` + incremento de versión como transacción local. No crea favorito por SKU ni toca stock.

- [ ] **API-CA-F021-01:** Reintentar tras éxito no crea favorito duplicado.
