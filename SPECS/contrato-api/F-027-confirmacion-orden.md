# Spec de contrato API — F-027 Confirmación

`GET /api/v1/checkout/operations/{checkoutOperationId}` requiere JWT y sólo permite al dueño.

`200`: `{"data":{"state":"SUCCEEDED","order":{"orderId":"PED-1","state":"CREADO","total":{"amount":355,"currency":"PEN"},"createdAt":"2026-09-27T18:30:00Z"}}}`. Si `SUBMITTED`, responde `202`; si falló, `409` con código recuperable. No retorna contacto/dirección completa.

- [ ] **API-CA-F027-01:** Un cliente no puede consultar operación de otro cliente.
