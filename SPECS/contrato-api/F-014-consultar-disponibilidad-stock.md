# Spec de contrato API — F-014 Consultar disponibilidad de stock

`GET /api/v1/catalog/products/{slug}/availability?sku={sku}` — lectura pública de disponibilidad comercial por SKU.

```json
{"data":{"productId":"PRD-1","sku":"AERO-42-BLK","availability":"STOCK_LOW","checkedAt":"2026-09-27T18:15:00Z"}}
```

```json
{"data":{"productId":"PRD-1","sku":"AERO-42-BLK","availability":"UNDETERMINED","checkedAt":"2026-09-27T18:15:00Z"}}
```

`availability` admite `AVAILABLE`, `STOCK_LOW`, `OUT_OF_STOCK` o `UNDETERMINED`. El BFF adapta `DISPONIBLE`, `STOCK_BAJO`, `AGOTADO` e `INDETERMINADO` de Inventario y no expone cantidades, `locationId`, `onHand` ni `reserved`.

`UNDETERMINED` es un **resultado comercial válido con HTTP 200**, no un error: significa que Productos no pudo determinar una ruta de abastecimiento única y verificable (`INDETERMINADO` en su contrato). Nunca equivale a `OUT_OF_STOCK` ni garantiza disponibilidad; admite reintento y no se confunde con `503`, timeout ni respuesta inválida. El contrato de origen publica sólo `sku` y `status`, por lo que el BFF **no** expone un motivo ni infiere una causa.

> Este cuarto estado forma parte de `G-G6-COMPAT`: la propuesta no se considera homologada hasta que G6 documente conformidad y las specs de G1 se aprueben.

Errores: `400 INVALID_PRODUCT_SLUG`, `409 PRODUCT_VARIANT_SELECTION_REQUIRED`/`SKU_NOT_BELONG_TO_PRODUCT`, `502 INVENTORY_INVALID_RESPONSE`, `503 INVENTORY_UNAVAILABLE`, `504 INVENTORY_TIMEOUT`.

Consulta segura e idempotente; caché corta máxima 30 s. BFF → `GET /api/v1/inventario/disponibilidad/comercial` de Productos: homologar parámetro SKU, mapeo de estado comercial (`DISPONIBLE`/`STOCK_BAJO`/`AGOTADO`/`INDETERMINADO`), auth y esquema dentro de `I-01` / `OPEN-03`. Este contrato sólo informa estado comercial; no valida cantidad. La futura consulta `sku` + `quantity` de `X-P0-03` requiere contrato del owner y no se sustituye por balances internos.

- [ ] **API-CA-F014-01:** Error externo nunca se mapea a `OUT_OF_STOCK`.
- [ ] **API-CA-F014-02:** La respuesta no contiene saldo ni ubicación.
- [ ] **API-CA-F014-03:** `INDETERMINADO` del proveedor se publica como `UNDETERMINED` con `200`; no se convierte en `OUT_OF_STOCK` ni en error, y no se añade un campo de motivo.
