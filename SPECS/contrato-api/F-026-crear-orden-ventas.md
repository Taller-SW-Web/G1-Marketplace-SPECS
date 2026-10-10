# Spec de contrato API — F-026 Crear orden

`POST /api/v1/checkout/orders` requiere JWT y `Idempotency-Key`.

```json
{"checkoutOperationId":"COP-1","contact":{"fullName":"Ana Pérez","documentType":"DNI","documentNumber":"12345678","phone":"+51999999999","email":"ana@example.com"}}
```

Respuesta BFF `202` para pedido creado pero transacción aún pendiente: `{"data":{"checkoutOperationId":"COP-1","orderId":"PED-1","state":"SUBMITTED","orderState":"CREADO"}}`. La respuesta BFF de éxito definitivo sólo se habilitará tras verificar `PAGADO` en Ventas para ese `orderId`; su código/payload final dependen del protocolo de simulación homologado y **no están publicados todavía**.

Errores conocidos de la capa BFF: `400 CONTACT_VALIDATION_ERROR`, `409 OPERATION_NOT_PREPARED`, `409 IDEMPOTENCY_KEY_REUSED`, `409 ORDER_CREATION_PENDING`, `503 SALES_UNAVAILABLE`. El BFF cambia `PREPARED→SUBMITTED`; sólo pasa a `SUCCEEDED` con `PAGADO` verificado o a fallo con resultado terminal inequívoco. Adapta a `POST /api/v1/pedidos`, envía dirección transitoria y no guarda contacto completo. La idempotencia externa, el evento/consulta de aptitud para pagar, el contrato de simulación y las compensaciones siguen abiertos bajo `I-02`; no usar el webhook reservado a la pasarela como si Marketplace fuese esa pasarela.

- [ ] **API-CA-F026-01:** Repetir clave/payload obtiene el mismo `orderId`.
- [ ] **API-CA-F026-02:** `CREADO` conserva el mismo `orderId` en `SUBMITTED` y no responde `SUCCEEDED`.
- [ ] **API-CA-F026-03:** Sólo una confirmación idempotente de `PAGADO` proveniente de Ventas cierra la operación; no se inventan tarjeta, autorización ni scope de webhook.
