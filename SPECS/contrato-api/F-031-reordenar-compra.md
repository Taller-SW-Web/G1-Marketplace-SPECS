# Spec de contrato API — F-031 Reordenar

`POST /api/v1/orders/{orderId}/reorder` requiere JWT y `Idempotency-Key` UUID por acción; cuerpo vacío. `200`: `{"data":{"cartId":"CART-1","version":9,"added":[{"sku":"AERO-42-BLK","quantity":1}],"adjustments":[{"sku":"OLD-1","reason":"NOT_AVAILABLE"}]}}`. Si falta la cabecera o no es UUID v4, responde `400 IDEMPOTENCY_KEY_REQUIRED`.

El BFF autoriza orden en Ventas, revalida cada SKU con Catálogo/Pricing/Inventario y actualiza Cart atómicamente. `404 ORDER_NOT_AVAILABLE`, `409 CART_CONFLICT`, `503 COMMERCE_DATA_UNAVAILABLE`. Depende de `I-01` e `I-03`.

**Contrato local G1 para idempotencia:** `POST /api/v1/orders/{orderId}/reorder` conserva el cuerpo vacío y requiere `Idempotency-Key` UUID v4 por acción intencional. G1 guarda el recibo por titular + pedido fuente + clave dentro de la transacción del carrito. Una repetición con la misma clave reproduce el mismo resultado sin volver a sumar; una nueva intención usa otra clave y puede volver a agregar los productos disponibles. El BFF genera y conserva la clave durante un resultado incierto/reintento y la descarta tras una respuesta exitosa. El mock sigue restringido a pruebas y la funcionalidad continúa apagada por defecto.

- [ ] **API-CA-F031-01:** Reintento no duplica líneas por SKU.
