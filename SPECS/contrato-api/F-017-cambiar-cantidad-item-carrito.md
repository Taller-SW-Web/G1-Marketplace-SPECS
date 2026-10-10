# Spec de contrato API — F-017 Cambiar la cantidad de un ítem

`PATCH /api/v1/carts/current/items/{sku}`

Headers: `If-Match: <cart-version>` opcional recomendado; cuerpo `{"quantity":3}`.

Respuesta `200`: carrito actualizado con `version`, línea confirmada y snapshot de precio. Errores: `400 INVALID_QUANTITY`, `404 CART_ITEM_NOT_FOUND`, `409 CART_CONFLICT`, `409 STOCK_LIMIT_REACHED` sólo si el contrato cuantitativo homologado entrega un límite (entonces incluye máximo confirmado y carrito actual), `503 COMMERCE_DATA_UNAVAILABLE`.

La cantidad es reemplazo absoluto, no delta. El BFF valida SKU, precio y estado comercial publicado; no afirma disponibilidad para N unidades hasta contar con `X-P0-03`. Actualiza la línea y `Cart.version` atómicamente, y no reserva stock. Autorización/cookie igual a F-016; dependencias Productos y Ofertas bajo `I-01`.

- [ ] **API-CA-F017-01:** `quantity:0` es `400`, nunca eliminación implícita.
- [ ] **API-CA-F017-02:** Conflicto de versión no pierde el cambio ya confirmado por otra operación.
