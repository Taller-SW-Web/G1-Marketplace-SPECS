# Spec de contrato API — F-030 Detalle de pedido

`GET /api/v1/orders/{orderId}` requiere JWT. El BFF consulta `GET /api/v1/pedidos/{pedidoId}` de Ventas, que documenta `403` si el cliente no es titular y `404` si el pedido no existe. Proyecta `orderId`, estado, fechas, líneas históricas con SKU/descripción/cantidad/precio, totales, envío resumido e historial; elimina documento, email completo, tarjeta y secretos. Mapea `403/404` externo a `404 ORDER_NOT_AVAILABLE` para evitar enumeración. Contrato publicado; quedan implementación y prueba `I-03`.

- [ ] **API-CA-F030-01:** Una respuesta de pedido ajeno no filtra estado ni contacto.
