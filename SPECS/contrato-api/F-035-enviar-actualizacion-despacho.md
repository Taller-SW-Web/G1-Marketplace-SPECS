# Spec de contrato API — F-035 Entrega de actualización

Contrato interno BFF propuesto `POST /internal/v1/notifications/shipment-update` con `shipmentEventId`, `orderId`, `state`, `occurredAt`, `estimatedDelivery`. Crea `NotificationDelivery(type=SHIPMENT_UPDATE)` idempotente y usa worker F-034. Su origen externo homologado es el webhook de Ventas `pedidos.envio.estado_actualizado` v1.0.0: `eventId`, `eventType: "ShipmentStatusUpdated"`, `version`, `timestamp`, `emitter` y `data` con `orderId` textual (`PED-YYYY-NNNNN`), `publicStatus`, `trackingNumber`, `estimatedDeliveryDate`. El adaptador mapea `eventId→shipmentEventId` y deduplica por `eventId` antes de encolar.

Ventas es emisor del webhook hacia Marketplace y recibe antes los cambios de Despacho. El contrato `api-ventas.md` v1.8.0, sección 1.10, documenta que G5 persiste el evento en su outbox, envía cada 5 s y reintenta errores de red/timeout/5xx/401/403/404 hasta 10 intentos; 2xx confirma recepción y 400/409/422 no se reintentan. Siguen pendientes la URL y autenticación del endpoint receptor G1, la prueba conjunta de I-05 y la entrega de correo vía G-MAIL.

- [ ] **API-CA-F035-01:** Sin entrega autenticada y probada del webhook de Ventas no se emite correo basado en un estado inventado.
- [ ] **API-CA-F035-02:** Dos entregas del mismo `eventId` producen una sola notificación; `orderId` conserva el identificador textual de Ventas.
