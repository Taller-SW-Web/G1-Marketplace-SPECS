# Spec de contrato API — F-014 Consultar disponibilidad de stock

`GET /api/v1/catalog/products/{slug}/availability?sku={sku}` — lectura pública de disponibilidad comercial por SKU.

```json
{"data":{"productId":"PRD-1","sku":"AERO-42-BLK","availability":"STOCK_LOW","checkedAt":"2026-09-27T18:15:00Z"}}
```

`availability` sólo admite `AVAILABLE`, `STOCK_LOW` o `OUT_OF_STOCK`. El BFF adapta `DISPONIBLE`, `STOCK_BAJO`, `AGOTADO` de Inventario y no expone cantidades, `locationId`, `onHand` ni `reserved`.

Errores: `400 INVALID_PRODUCT_SLUG`, `409 PRODUCT_VARIANT_SELECTION_REQUIRED`/`SKU_NOT_BELONG_TO_PRODUCT`, `502 INVENTORY_INVALID_RESPONSE`, `503 INVENTORY_UNAVAILABLE`, `504 INVENTORY_TIMEOUT`.

Consulta segura e idempotente; caché corta máxima 30 s. BFF → `EXT-OUT-INV-01`: debe homologar proyección agregada, ruta, auth y esquema dentro de `I-01` / `OPEN-03`.

- [ ] **API-CA-F014-01:** Error externo nunca se mapea a `OUT_OF_STOCK`.
- [ ] **API-CA-F014-02:** La respuesta no contiene saldo ni ubicación.
