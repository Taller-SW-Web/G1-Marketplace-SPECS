# Spec de contrato API — F-032 Seguimiento

`GET /api/v1/orders/{orderId}/tracking` requiere JWT. BFF autoriza con Ventas y consulta `GET /api/v1/seguimientos/pedidos/{idPedido}` de Despacho usando token de servicio `seguimientos:leer`.

`200`: `{"data":{"state":"EN_CAMINO","estimatedDelivery":"2026-09-28","milestones":[{"state":"ASIGNADO","at":"2026-09-27T18:00:00Z"}]}}`; `202 TRACKING_NOT_READY`, `404 ORDER_NOT_AVAILABLE`, `503 TRACKING_UNAVAILABLE`. No PII/coordenadas.

- [ ] **API-CA-F032-01:** Sin scope técnico no se usa token del cliente en Despacho.
