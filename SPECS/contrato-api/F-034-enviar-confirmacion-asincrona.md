# Spec de contrato API — F-034 Entrega de confirmación

Contrato interno `POST /internal/v1/notifications/order-confirmation` recibe `orderId`, `customerId`, `eventKey` y correo cifrado; crea/upserta `NotificationDelivery`. Worker llama F-033 y proveedor. Estados `PENDING→SENT/FAILED`; misma `eventKey` retorna entrega existente. No hay endpoint público.

- [ ] **API-CA-F034-01:** Evento duplicado no genera dos envíos de proveedor.
