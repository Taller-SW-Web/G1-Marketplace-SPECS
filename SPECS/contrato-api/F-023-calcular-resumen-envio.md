# Spec de contrato API — F-023 Cotización de checkout

`POST /api/v1/checkout/quotes` requiere JWT.

```json
{"addressId":"ADR-1","cartVersion":8}
```

Respuesta `200`:
```json
{"data":{"quoteId":"Q-1","expiresAt":"2026-09-27T18:30:00Z","subtotal":{"amount":340,"currency":"PEN"},"discount":{"amount":0,"currency":"PEN"},"shipping":{"amount":15,"currency":"PEN","estimatedDays":2},"total":{"amount":355,"currency":"PEN"},"lines":[{"sku":"AERO-42-BLK","quantity":2}]}}
```

Errores: `400 CART_VERSION_REQUIRED`, `409 CART_CHANGED`, `409 NO_SHIPPING_COVERAGE`, `409 LINE_NOT_AVAILABLE`, `503 QUOTE_UNAVAILABLE`. El BFF lee dirección del titular, revalida catálogo/precio/promoción/stock y llama `POST /api/v1/cotizaciones` de Despacho. `quoteId` es opaco/transitorio y vence; no se persiste como entidad Marketplace.

- [ ] **API-CA-F023-01:** Una cotización vencida no se acepta para preparación posterior.
