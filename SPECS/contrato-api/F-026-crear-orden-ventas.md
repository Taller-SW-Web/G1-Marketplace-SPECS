# Spec de contrato API — F-026 Crear orden

`POST /api/v1/checkout/orders` requiere JWT y `Idempotency-Key` UUID v4. El BFF conserva la clave asociada a `checkoutOperationId` y la usa al llamar a `POST /api/v1/pedidos` de Ventas; un reintento equivalente conserva exactamente el mismo payload externo.

```json
{"checkoutOperationId":"COP-1","contact":{"fullName":"Ana Pérez","documentType":"DNI","documentNumber":"12345678","phone":"+51999999999","email":"ana@example.com"}}
```

Respuesta BFF `202` para pedido creado pero pago simulado aún pendiente: `{"data":{"checkoutOperationId":"COP-1","orderId":"PED-2026-00981","state":"SUBMITTED","orderState":"CREADO","total":{"amount":355,"currency":"PEN"}}}`. Ventas responde `201 Created` con `pedidoId`, `estado=CREADO` y `total` autoritativo una vez confirmados reserva y cupón; inicia internamente su simulador. El BFF sólo responde éxito definitivo tras consultar `PAGADO` para ese mismo pedido.

Errores conocidos de la capa BFF: `400 CONTACT_VALIDATION_ERROR`, `409 OPERATION_NOT_PREPARED`, `409 IDEMPOTENCY_KEY_REUSED`, `409 ORDER_CREATION_PENDING`, `503 SALES_UNAVAILABLE`. El BFF cambia `PREPARED→SUBMITTED`; sólo pasa a `SUCCEEDED` con `PAGADO` verificado o a fallo con `ANULADO` inequívoco. Adapta a `POST /api/v1/pedidos`, envía dirección transitoria y no guarda contacto completo. Si pierde la respuesta de Ventas antes de conocer `pedidoId`, recupera el resultado repitiendo ese POST con la misma clave/payload de H-02; después consulta `GET /api/v1/pedidos/{pedidoId}`. Marketplace no invoca el simulador ni el webhook de pasarela. El mapeo del bloque obligatorio `pago.metodoPago` aún requiere un valor publicado compatible con el flujo sin captura de tarjeta.

- [ ] **API-CA-F026-01:** Repetir clave/payload obtiene el mismo `orderId`.
- [ ] **API-CA-F026-02:** `CREADO` conserva el mismo `orderId` en `SUBMITTED` y no responde `SUCCEEDED`.
- [ ] **API-CA-F026-03:** Sólo `PAGADO` verificado en la consulta de Ventas cierra la operación; no se inventan tarjeta, autorización ni scope de webhook.
- [ ] **API-CA-F026-04:** Pérdida de la respuesta `201` se recupera con la misma clave/payload y un solo `pedidoId`; `ANULADO` por `PAGO_NO_COMPLETADO` no se presenta como compra exitosa.

Fuente externa: [`RESPUESTAS_G1_MARKETPLACE.md`](https://github.com/Taller-SW-Web/G5-Ventas-Postventas/blob/8f32508/integraciones/RESPUESTAS_G1_MARKETPLACE.md) y `specs/api/api-ventas.md`, secciones 1.1 y 1.3.
