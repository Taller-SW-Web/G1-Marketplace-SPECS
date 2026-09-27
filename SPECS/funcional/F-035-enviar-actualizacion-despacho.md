# Spec funcional — F-035 Enviar actualización de despacho por correo

| Campo | Valor |
|---|---|
| ID | `F-035` |
| Estado | Aprobada para planificación; integración bloqueada por `I-05`. |

Envía correo cuando cambia un estado de despacho relevante. Incluye deduplicar por evento, plantilla F-033 y entrega asíncrona; excluye consultar tracking en cada correo o alterar despacho/pedido.

- **RN-F035-01:** Cada `shipmentEventId` y tipo produce como máximo una `NotificationDelivery`.
- **RN-F035-02:** Sólo se comunican estados aprobados para cliente y datos mínimos (pedido, estado, fecha estimada/enlace).
- **RN-F035-03:** Reintentos no cambian estado de pedido/despacho.
- **RN-F035-04:** Hasta cerrar `I-05`, Marketplace no presume recibir evento directo de Despacho.

- [ ] **CA-F035-01:** Evento repetido no duplica correo.
- [ ] **CA-F035-02:** Falla de correo no revierte transición de Despacho.
