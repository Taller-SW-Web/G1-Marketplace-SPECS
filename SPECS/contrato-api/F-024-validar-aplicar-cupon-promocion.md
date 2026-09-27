# Spec de contrato API — F-024 Beneficios de checkout

`POST /api/v1/checkout/benefits` requiere JWT.

```json
{"quoteId":"Q-1","couponCode":"DEPORTE20"}
```

Respuesta `200`: `{"data":{"quoteId":"Q-2","selectedBenefit":{"type":"COUPON","id":"COUPON-1","discount":{"amount":20,"currency":"PEN"}},"total":{"amount":335,"currency":"PEN"},"expiresAt":"2026-09-27T18:30:00Z"}}`.

Errores: `400 INVALID_COUPON_FORMAT`, `409 QUOTE_EXPIRED`, `422 COUPON_NOT_APPLICABLE`, `503 BENEFITS_UNAVAILABLE`. BFF envía líneas, canal, tiempo y `customer_ref` sólo si el contrato homologado lo exige; no persiste ni consume cupón. Integra `EXT-OUT-PROMO-01`/`COUPON-01`; request definitivo pendiente `OPEN-11`/`OPEN-12`.

- [ ] **API-CA-F024-01:** Validar dos veces no altera límite de uso.
