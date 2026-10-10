# Spec de contrato API — F-025 Preparar checkout simulado

`POST /api/v1/checkout/preparations` requiere JWT y header `Idempotency-Key: <UUID>`.

```json
{"quoteId":"Q-2","cartVersion":8,"simulationConfirmed":true}
```

Respuesta `201`:
```json
{"data":{"checkoutOperationId":"COP-1","state":"PREPARED","simulationConsent":"RECORDED","revalidatedAt":"2026-09-27T18:25:00Z"}}
```

Errores: `400 SIMULATION_NOT_CONFIRMED`, `409 IDEMPOTENCY_KEY_REUSED`, `409 QUOTE_EXPIRED`, `409 REVALIDATION_CHANGED`, `409 STOCK_NOT_AVAILABLE` sólo si el proveedor puede determinarlo con la cantidad solicitada, `503 REVALIDATION_UNAVAILABLE`. El BFF registra `CheckoutOperation(PREPARING→PREPARED)` con fingerprint y revalida el resumen mediante contratos publicados. La consulta comercial actual de Inventario sólo informa estado por SKU; no garantiza N unidades. La revalidación cuantitativa `X-P0-03` y el snapshot `X-P0-05/06` quedan bloqueados hasta homologación. No crea pedido, reserva, consume cupón ni confirma pago.

- [ ] **API-CA-F025-01:** Misma clave y payload retorna la misma operación preparada.
- [ ] **API-CA-F025-02:** La operación no contiene datos de tarjeta, dirección completa ni secreto de sesión.
- [ ] **API-CA-F025-03:** `simulationConsent=RECORDED` nunca se interpreta como autorización de pasarela, `PAGADO` ni disponibilidad de N unidades.
