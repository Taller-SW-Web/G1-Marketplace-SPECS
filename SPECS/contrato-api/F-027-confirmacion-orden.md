# Spec de contrato API — F-027 Confirmación

`GET /api/v1/checkout/operations/{checkoutOperationId}` requiere JWT y sólo permite al dueño.

`200` para resultado final **propuesto**: `{"data":{"state":"SUCCEEDED","order":{"orderId":"PED-1","state":"PAGADO","total":{"amount":355,"currency":"PEN"},"createdAt":"2026-09-27T18:30:00Z"}}}`. Sólo se devuelve cuando Ventas confirma `PAGADO` para el mismo pedido. Si existe `CREADO`, espera de aptitud para pagar o confirmación simulada incierta, responde `202` con `state=SUBMITTED`, `orderId` si es seguro exponerlo y sin semántica de éxito. Si hay fallo terminal inequívoco, `409` con código recuperable. Forma final, frecuencia de consulta y plazo de espera requieren homologación `I-02`; no retorna contacto/dirección completa.

- [ ] **API-CA-F027-01:** Un cliente no puede consultar operación de otro cliente.
- [ ] **API-CA-F027-02:** `CREADO` no produce `200 SUCCEEDED`; timeout no se convierte en `PAGADO` supuesto.
