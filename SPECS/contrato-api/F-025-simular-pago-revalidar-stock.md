# Spec de contrato API — F-025 Preparar checkout simulado

`POST /api/v1/checkout/preparations` requiere JWT y header `Idempotency-Key: <UUID>`.

```json
{"quoteId":"Q-2","cartVersion":8,"simulationConfirmed":true}
```

Respuesta `201`:
```json
{"data":{"checkoutOperationId":"COP-1","state":"PREPARED","paymentSimulation":"APPROVED","revalidatedAt":"2026-09-27T18:25:00Z"}}
```

Errores: `400 SIMULATION_NOT_CONFIRMED`, `409 IDEMPOTENCY_KEY_REUSED`, `409 QUOTE_EXPIRED`, `409 REVALIDATION_CHANGED`, `409 STOCK_NOT_AVAILABLE`, `503 REVALIDATION_UNAVAILABLE`. El BFF registra `CheckoutOperation(PREPARING→PREPARED)` con fingerprint, vuelve a consultar Pricing/Promociones/Inventario/Despacho según aplique y no crea pedido ni consume stock/cupón.

- [ ] **API-CA-F025-01:** Misma clave y payload retorna la misma operación preparada.
- [ ] **API-CA-F025-02:** La operación no contiene datos de tarjeta, dirección completa ni secreto de sesión.
