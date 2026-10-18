# Spec de contrato API — F-016 Agregar ítem al carrito

`POST /api/v1/carts/current/items`

Entrada normal, con la identidad comercial ya resuelta:

```json
{"sku":"AERO-42-BLK","quantity":1}
```

Durante el gate I-01, el BFF acepta además una entrada **sólo para productos MOCK** cuando el fixture tiene un mapeo de servidor conocido:

```json
{"productId":"PRD-MOCK-001","quantity":1}
```

El BFF resuelve `productId` a un SKU MOCK; el cliente nunca trata ambos identificadores como equivalentes. Un ID sin mapeo devuelve `400 PRODUCT_NOT_PURCHASABLE`. Esta ruta sólo está habilitada en `BFF_MODE=mock`; en modo REAL se requiere el `sku` autorizado por el contrato de variantes/precio. F-011 no se amplía ni expone SKU.

Respuesta `200` (línea existente) o `201` (línea creada):

```json
{"data":{"cartId":"CART-1","version":4,"items":[{"sku":"AERO-42-BLK","quantity":2,"unitPrice":{"amount":170.0,"currency":"PEN","version":8}}]}}
```

Autenticación opcional: JWT identifica el carrito autenticado; sin JWT se usa cookie `HttpOnly`, `Secure`, `SameSite=Lax` de sesión anónima. Errores: `400 INVALID_QUANTITY`, `404 SKU_NOT_AVAILABLE`, `409 STOCK_LIMIT_REACHED` sólo si una operación cuantitativa homologada informa el límite, `409 CART_CONFLICT`, `503 COMMERCE_DATA_UNAVAILABLE`. No devolver carrito ajustado por un máximo de stock que el provider no publicó.

`quantity` es entero 1–99. El BFF valida SKU/precio/estado comercial publicado y muta `Cart`/`CartItem` con `version`; la respuesta incluye sólo snapshot de precio. La cantidad no se garantiza hasta validar N unidades (`X-P0-03`) y, finalmente, reservar bajo Ventas. No expone saldos ni reserva. Integraciones externas: Catálogo, Pricing e Inventario (`I-01`).

- [ ] **API-CA-F016-01:** Mismo SKU mantiene unicidad por carrito.
- [ ] **API-CA-F016-02:** Una solicitud fallida no deja una línea nueva ni una cantidad incrementada.
