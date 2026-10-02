# Spec de contrato API — F-018 Quitar un ítem del carrito

`DELETE /api/v1/carts/current/items/{sku}`

Respuesta `204 No Content` si se elimina o ya está ausente; devuelve `X-Cart-Version` actualizado cuando hubo mutación. `400 INVALID_SKU` para formato inválido y `409 CART_CONFLICT` para versión desactualizada no reconciliable.

Autorización/cookie igual a F-016. La operación es idempotente y transaccional sobre `Cart`/`CartItem`; no toca servicios externos ni reserva.

- [ ] **API-CA-F018-01:** Dos `DELETE` del mismo SKU dejan la misma representación final.
