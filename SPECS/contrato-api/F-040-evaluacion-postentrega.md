# Spec de contrato API — F-040 Evaluación

`POST /api/v1/orders/{orderId}/csat` JWT: `{"sentiment":"GOOD","reasons":["ENTREGA_RAPIDA"],"comment":"Excelente"}`. BFF confirma elegibilidad y adapta a `POST /api/v2/csat`: `pedidoId`, cliente derivado, `canal:"MARKETPLACE"`, `puntuacion:5`, comentario con motivos. `201`, `409 CSAT_ALREADY_SUBMITTED`, `409 ORDER_NOT_DELIVERED`; no tabla de calificaciones.

Contrato Ventas hoy no acepta motivos ni declara validación entregado en endpoint; cerrar `I-04` antes de implementación.

- [ ] **API-CA-F040-01:** Bien/Regular/Mal se mapean determinísticamente 5/3/1.
