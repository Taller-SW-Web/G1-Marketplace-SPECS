# Spec de contrato API — F-026 Crear orden

`POST /api/v1/checkout/orders` requiere JWT y `Idempotency-Key`.

```json
{"checkoutOperationId":"COP-1","contact":{"fullName":"Ana Pérez","documentType":"DNI","documentNumber":"12345678","phone":"+51999999999","email":"ana@example.com"}}
```

Respuesta `201`: `{"data":{"checkoutOperationId":"COP-1","orderId":"PED-1","state":"SUCCEEDED","orderState":"CREADO"}}`.

Errores: `400 CONTACT_VALIDATION_ERROR`, `409 OPERATION_NOT_PREPARED`, `409 IDEMPOTENCY_KEY_REUSED`, `409 ORDER_CREATION_PENDING`, `503 SALES_UNAVAILABLE`. El BFF cambia `PREPARED→SUBMITTED→SUCCEEDED/FAILED`, adapta a `POST /api/v1/pedidos` y envía copia de dirección; no guarda contacto completo. Contrato externo carece de idempotencia explícita: `I-02` bloquea implementación real.

- [ ] **API-CA-F026-01:** Repetir clave/payload obtiene el mismo `orderId`.
