# Spec funcional — F-026 Crear la orden en Ventas y Postventa

| Campo | Valor |
|---|---|
| ID | `F-026` |
| Estado | Flujo homologado con Ventas el 10/10/2026; implementación y pruebas de integración pendientes. |

Envía una operación `PREPARED` a Ventas para crear un pedido y observa su estado hasta `PAGADO` o un resultado terminal. Incluye completar el contacto requerido por Ventas, transmitir dirección/snapshot autorizados, conservar `pedidoId` y el total autoritativo de Ventas, y registrar el resultado en `CheckoutOperation`. El `201 Created` de Ventas confirma reserva de stock y cupón, pero deja el pedido en `CREADO`; Ventas inicia internamente el simulador. Marketplace no coordina ese cobro ni habilita F-027 como éxito hasta verificar `PAGADO`.

- **RN-F026-01:** Sólo una operación `PREPARED` del cliente puede enviarse; al llamar a Ventas se usa `Idempotency-Key` UUID v4. Misma clave y payload devuelven el mismo `pedidoId`; una clave reutilizada con otro payload recibe `409 IDEMPOTENCY_KEY_REUSED`.
- **RN-F026-02:** Si perfil no aporta nombre, documento, teléfono o email requeridos por Ventas, Marketplace solicita sólo los campos faltantes y los valida; no los persiste como perfil local.
- **RN-F026-03:** Se envían SKU, cantidades, referencias/snapshot comercial homologados y dirección/cotización. Ventas valida precio, cantidad y cupón al crear, y devuelve el `total` autoritativo; Marketplace no fabrica un importe final ni consume cupón o inventario. El mapeo del bloque `pago.metodoPago` requerido por Ventas debe concretarse sin inventar valores ni datos de tarjeta.
- **RN-F026-04:** Si se pierde la respuesta de creación antes de conocer el `pedidoId`, Marketplace repite `POST /api/v1/pedidos` con la misma clave y el mismo payload; no crea una operación nueva. Con el `pedidoId` recuperado consulta `GET /api/v1/pedidos/{pedidoId}`. Si el resultado sigue incierto, conserva `SUBMITTED`.
- **RN-F026-05:** Tras el `201` en `CREADO`, Ventas invoca internamente al simulador. Marketplace consulta el estado por `pedidoId`; no invoca al simulador ni a `POST /api/v1/pedidos/{pedidoId}/pagos/notificacion`. El identificador externo es texto con formato `PED-YYYY-NNNNN`.
- **RN-F026-06:** `SUCCEEDED` local requiere `PAGADO` confirmado por Ventas para el mismo `pedidoId`. `CREADO` permanece pendiente; `ANULADO` por `PAGO_NO_COMPLETADO` es fallo terminal. Ventas repone stock ante rechazo; la liberación del cupón ante Productos sigue como dependencia externa abierta.

- [ ] **CA-F026-01:** Misma operación no crea dos pedidos.
- [ ] **CA-F026-02:** Datos de documento inválidos no se transmiten.
- [ ] **CA-F026-03:** El happy path con y sin cupón termina en `PAGADO` observable en Ventas; reintentos con la misma clave no duplican pedido, reserva ni simulación.
- [ ] **CA-F026-04:** `CREADO` o un resultado incierto nunca navega a confirmación pagada.
- [ ] **CA-F026-05:** Una respuesta perdida antes de conocer `pedidoId` se recupera con replay idempotente; un rechazo posterior lleva a `ANULADO` sin presentar éxito.

Fuente: [`RESPUESTAS_G1_MARKETPLACE.md`](https://github.com/Taller-SW-Web/G5-Ventas-Postventas/blob/8f32508/integraciones/RESPUESTAS_G1_MARKETPLACE.md) y secciones 1.1/1.3 de `specs/api/api-ventas.md` de Ventas. La homologación documental está cerrada; quedan la implementación/prueba de G5, el mapeo completo del payload de creación y la liberación del cupón ante una anulación.
