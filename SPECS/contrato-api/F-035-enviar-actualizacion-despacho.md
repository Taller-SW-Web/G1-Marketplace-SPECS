# Spec de contrato API — F-035 Entrega de actualización

Contrato interno BFF propuesto `POST /internal/v1/notifications/shipment-update` con `shipmentEventId`, `orderId`, `state`, `occurredAt`, `estimatedDelivery`. Crea `NotificationDelivery(type=SHIPMENT_UPDATE)` idempotente y usa worker F-034. Su origen externo homologado es el webhook de Ventas `pedidos.envio.estado_actualizado` v1.0.0: `eventId`, `eventType: "ShipmentStatusUpdated"`, `version`, `timestamp`, `emitter` y `data` con `orderId` textual (`PED-YYYY-NNNNN`), `publicStatus`, `trackingNumber`, `estimatedDeliveryDate`. El adaptador mapea `eventId→shipmentEventId` y deduplica por `eventId` antes de encolar.

Ventas es emisor del webhook hacia Marketplace y recibe antes los cambios de Despacho. H-05 tiene formato publicado, pero Ventas aún debe definir entrega, reintentos, backoff, autenticación del receptor y responsable de implementación (`I-05`). No se envían correos reales hasta probar ese mecanismo.

- [ ] **API-CA-F035-01:** Sin entrega autenticada y probada del webhook de Ventas no se emite correo basado en un estado inventado.
- [ ] **API-CA-F035-02:** Dos entregas del mismo `eventId` producen una sola notificación; `orderId` conserva el identificador textual de Ventas.
