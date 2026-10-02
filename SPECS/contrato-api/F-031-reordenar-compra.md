# Spec de contrato API — F-031 Reordenar

`POST /api/v1/orders/{orderId}/reorder` requiere JWT; cuerpo vacío. `200`: `{"data":{"cartId":"CART-1","version":9,"added":[{"sku":"AERO-42-BLK","quantity":1}],"adjustments":[{"sku":"OLD-1","reason":"NOT_AVAILABLE"}]}}`.

El BFF autoriza orden en Ventas, revalida cada SKU con Catálogo/Pricing/Inventario y actualiza Cart atómicamente. `404 ORDER_NOT_AVAILABLE`, `409 CART_CONFLICT`, `503 COMMERCE_DATA_UNAVAILABLE`. Depende de `I-01` e `I-03`.

- [ ] **API-CA-F031-01:** Reintento no duplica líneas por SKU.
