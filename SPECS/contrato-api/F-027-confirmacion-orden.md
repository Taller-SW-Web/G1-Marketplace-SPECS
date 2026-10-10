# Spec de contrato API — F-027 Confirmación

`GET /api/v1/checkout/operations/{checkoutOperationId}` requiere JWT y sólo permite al dueño.

`200` para resultado final **propuesto**: `{"data":{"state":"SUCCEEDED","order":{"orderId":"PED-2026-00981","state":"PAGADO","total":{"amount":355,"currency":"PEN"},"createdAt":"2026-09-27T18:30:00Z"}}}`. El BFF contrasta el `pedidoId` asociado a la operación con `GET /api/v1/pedidos/{pedidoId}` y sólo devuelve éxito cuando Ventas informa `PAGADO`. Si sigue `CREADO`, responde `202` con `state=SUBMITTED` y sin semántica de éxito; si Ventas informa `ANULADO` por `PAGO_NO_COMPLETADO`, presenta un resultado terminal de fallo. El BFF no retorna contacto/dirección completa. Frecuencia de consulta, plazo de espera y recuperación de la operación local siguen como decisiones de implementación de G1; no requieren otro endpoint de pago externo.

- [ ] **API-CA-F027-01:** Un cliente no puede consultar operación de otro cliente.
- [ ] **API-CA-F027-02:** `CREADO` no produce `200 SUCCEEDED`; timeout no se convierte en `PAGADO` supuesto.
- [ ] **API-CA-F027-03:** `ANULADO` por rechazo simulado termina la verificación sin mostrar confirmación pagada.
