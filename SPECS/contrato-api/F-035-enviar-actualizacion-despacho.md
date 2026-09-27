# Spec de contrato API — F-035 Entrega de actualización

Contrato propuesto `POST /internal/v1/notifications/shipment-update` con `shipmentEventId`, `orderId`, `state`, `occurredAt`, `estimatedDelivery`. Crea `NotificationDelivery(type=SHIPMENT_UPDATE)` idempotente y usa worker F-034.

Fuente actual: Despacho publica a Ventas, no Marketplace. Debe acordarse si Ventas reexpone eventos, Marketplace sondea API o Despacho habilita webhook (`I-05`) antes de implementar.

- [ ] **API-CA-F035-01:** Sin contrato de origen homologado no se emite correo basado en un estado inventado.
