# Spec de contrato API — F-040 Evaluación

`POST /api/v1/orders/{orderId}/csat` JWT: `{"sentiment":"GOOD","reasons":["ENTREGA_RAPIDA"],"comment":"Excelente"}`. `GOOD/REGULAR/BAD` son valores internos de G1; el BFF adapta a `POST /api/v2/csat` de Ventas con `pedidoId`, cliente derivado del JWT, `canal:"MARKETPLACE"`, `puntuacion:5/3/1` y `comentario` como texto libre (`Motivos: [ENTREGA_RAPIDA] - Excelente`). No envía `sentiment` ni `reasons[]` al proveedor. Ventas valida titularidad del pedido contra `sub` del JWT.

Respuestas externas homologadas: `201` creado; `403` pedido ajeno; `422 ORDER_NOT_DELIVERED`; `409 CSAT_ALREADY_SUBMITTED`. El BFF mantiene códigos públicos equivalentes y no persiste una segunda tabla de calificaciones. H-04 está documentada; faltan implementación y prueba de titularidad, elegibilidad y duplicado (`I-04`).

- [ ] **API-CA-F040-01:** Bien/Regular/Mal se mapean determinísticamente 5/3/1.
- [ ] **API-CA-F040-02:** Pedido no entregado devuelve `422 ORDER_NOT_DELIVERED`; un `409 CSAT_ALREADY_SUBMITTED` no crea otra encuesta.
