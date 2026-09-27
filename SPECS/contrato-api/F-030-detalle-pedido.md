# Spec de contrato API — F-030 Detalle de pedido

`GET /api/v1/orders/{orderId}` requiere JWT. Devuelve `orderId`, estado, fechas, líneas históricas con SKU/descripción/cantidad/precio, totales, envío resumido e historial; no documento, email completo, tarjeta, secretos ni datos de otro cliente. Mapea `403/404` externo a `404 ORDER_NOT_AVAILABLE` para evitar enumeración. Dependencia Ventas e `I-03`.

- [ ] **API-CA-F030-01:** Una respuesta de pedido ajeno no filtra estado ni contacto.
