# Spec de contrato API — F-030 Detalle de pedido

`GET /api/v1/orders/{orderId}` requiere sesión autenticada. El BFF consulta `GET /api/v1/pedidos/{pedidoId}` de Ventas, que documenta `403` si el cliente no es titular y `404` si el pedido no existe. Proyecta `orderId`, estado, fechas, líneas históricas con SKU/descripción/cantidad/precio, total, ubicación resumida (distrito/provincia/departamento), email parcialmente enmascarado, teléfono enmascarado e historial; elimina calle, referencia, documento, identificadores de contacto, email completo, tarjeta y secretos. Mapea `403/404` externo a `404 ORDER_NOT_AVAILABLE` para evitar enumeración.

**Límite del contrato G5:** publica `pago.total` y snapshots de líneas (`cantidad`, `precioUnitario`), pero no importes autoritativos de subtotal, descuentos ni envío. G1 no deriva esos conceptos por suma ni los presenta como desglose hasta que G5/Producto apruebe explícitamente la regla y moneda/redondeo. La UI conserva la solicitud de desglose en V-016 como discrepancia pendiente.

La proyección tiene pruebas locales con fixtures de contrato; la homologación REAL de `I-03`, incluida autorización A/B con JWT autorizado, sigue pendiente.

- [ ] **API-CA-F030-01:** Una respuesta de pedido ajeno no filtra estado ni contacto.
