# Spec de contrato API — F-016 Agregar ítem al carrito

`POST /api/v1/carts/current/items`

```json
{"sku":"AERO-42-BLK","quantity":1}
```

Respuesta `200` (línea existente) o `201` (línea creada):

```json
{"data":{"cartId":"CART-1","version":4,"items":[{"sku":"AERO-42-BLK","quantity":2,"unitPrice":{"amount":170.0,"currency":"PEN","version":8}}]}}
```

Autenticación opcional: JWT identifica el carrito autenticado; sin JWT se usa cookie `HttpOnly`, `Secure`, `SameSite=Lax` de sesión anónima. Errores: `400 INVALID_QUANTITY`, `404 SKU_NOT_AVAILABLE`, `409 STOCK_LIMIT_REACHED` (devuelve carrito ajustado), `409 CART_CONFLICT`, `503 COMMERCE_DATA_UNAVAILABLE`.

`quantity` es entero 1–99. El BFF valida SKU/precio/stock y muta `Cart`/`CartItem` con `version`; no expone inventario ni reserva. La respuesta incluye sólo snapshot de precio. Integraciones externas: Catálogo, Pricing e Inventario (`I-01`).

- [ ] **API-CA-F016-01:** Mismo SKU mantiene unicidad por carrito.
- [ ] **API-CA-F016-02:** Una solicitud fallida no deja una línea nueva ni una cantidad incrementada.
