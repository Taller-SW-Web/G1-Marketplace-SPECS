# Spec de contrato API — F-020 Fusionar carrito anónimo al iniciar sesión

`POST /api/v1/carts/current/merge-anonymous` requiere JWT y cookie anónima válida; no tiene cuerpo.

Respuesta `200`:

```json
{"data":{"cartId":"CART-AUTH","version":8,"merged":true,"adjustments":[{"sku":"AERO-42-BLK","requestedQuantity":4,"confirmedQuantity":2,"reason":"STOCK_LIMIT"}]}}
```

Sin carrito anónimo, responde `200` con `merged:false`. Errores: `401 UNAUTHENTICATED`, `409 MERGE_IN_PROGRESS`, `503 COMMERCE_DATA_UNAVAILABLE`. El BFF toma bloqueo breve/versión, revalida SKU/precio/stock, actualiza destino y marca origen `MERGED` con `mergedIntoCartId` en una transacción. La cookie se invalida después del commit.

- [ ] **API-CA-F020-01:** Una cookie ya fusionada no incrementa de nuevo el destino.
- [ ] **API-CA-F020-02:** Fallo antes del commit no cambia propietario ni cantidades.
