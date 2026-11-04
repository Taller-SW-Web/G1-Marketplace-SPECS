# Spec funcional — F-035 Enviar actualización de despacho por correo

| Campo | Valor |
|---|---|
| ID | `F-035` |
| Estado | H-05 y el envío outbox/reintentos de G5 están documentados; endpoint receptor/autenticación G1 y prueba conjunta de `I-05` siguen pendientes. |

Envía correo cuando cambia un estado de despacho relevante. Incluye deduplicar por evento, plantilla F-033 y entrega asíncrona; excluye consultar tracking en cada correo o alterar despacho/pedido.

- **RN-F035-01:** Cada `eventId` recibido de Ventas y tipo produce como máximo una `NotificationDelivery`.
- **RN-F035-02:** Sólo se comunican estados aprobados para cliente y datos mínimos (pedido, estado, fecha estimada/enlace).
- **RN-F035-03:** Reintentos no cambian estado de pedido/despacho.
- **RN-F035-04:** Marketplace recibe de Ventas el webhook `pedidos.envio.estado_actualizado` v1.0.0; no consume eventos internos de Despacho. G5 documenta su outbox y política de reintentos; URL/autenticación del endpoint receptor G1 y prueba conjunta siguen pendientes.

- [ ] **CA-F035-01:** Evento repetido no duplica correo.
- [ ] **CA-F035-02:** Falla de correo no revierte transición de Despacho.
