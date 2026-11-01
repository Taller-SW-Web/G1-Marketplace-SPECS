# Spec de contrato API — F-034 Entrega de confirmación

Contrato interno `POST /internal/v1/notifications/order-confirmation` recibe `orderId`, `customerId`, `eventKey` y correo cifrado; crea/upserta `NotificationDelivery` sólo tras la verificación interna de `PAGADO` para ese mismo pedido. `CREADO` no habilita esta entrega. Worker llama F-033 y proveedor. Estados `PENDING→SENT/FAILED`; misma `eventKey` retorna entrega existente. No hay endpoint público ni se presume evento de correo publicado por Ventas.

- [ ] **API-CA-F034-01:** Evento duplicado no genera dos envíos de proveedor.
