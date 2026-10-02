# Spec de contrato API — F-028 Historial

`GET /api/v1/orders/me?page=0&pageSize=10` requiere JWT.

`200`: `{"data":[{"orderId":"PED-1","state":"PAGADO","total":{"amount":355,"currency":"PEN"},"createdAt":"2026-09-27T18:30:00Z"}],"page":{"number":0,"size":10,"totalElements":1,"totalPages":1}}`.

El BFF deriva el titular del JWT y adapta Ventas; no expone/acepta `clienteId`. Requiere homologar `I-03`.

- [ ] **API-CA-F028-01:** Un parámetro cliente no altera el ámbito.
