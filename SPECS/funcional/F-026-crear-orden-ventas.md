# Spec funcional — F-026 Crear la orden en Ventas y Postventa

| Campo | Valor |
|---|---|
| ID | `F-026` |
| Estado | Revisada por `G1-P0-01`; integración bloqueada por `I-02` y protocolo Productos–Ventas aún no homologado. |

Envía una operación `PREPARED` a Ventas para crear un pedido y observa su preparación transaccional. Incluye completar el contacto requerido por Ventas, transmitir dirección/snapshot autorizados, conservar `orderId` y registrar el resultado en `CheckoutOperation`; excluye cobro real, consumo directo de stock y notificación al cliente. `CREADO` es un estado intermedio: no finaliza la compra ni habilita F-027 como éxito pagado.

- **RN-F026-01:** Sólo una operación `PREPARED` del cliente puede enviarse; misma clave y fingerprint devuelve el resultado original.
- **RN-F026-02:** Si perfil no aporta nombre, documento, teléfono o email requeridos por Ventas, Marketplace solicita sólo los campos faltantes y los valida; no los persiste como perfil local.
- **RN-F026-03:** Se envían SKU, cantidades, referencias/snapshot comercial homologados, dirección/cotización y la indicación de modalidad simulada cuando Ventas la acepte. Ventas es dueño del pedido, la reserva y el estado de pago; Marketplace no fabrica un snapshot monetario ni consume cupón o inventario.
- **RN-F026-04:** Marketplace no considera éxito incierto como fallo: conserva `SUBMITTED` y permite consultar el resultado idempotente.
- **RN-F026-05:** Tras `CREADO`, Marketplace espera una señal verificable de pedido apto para pagar (reserva y cupón resueltos). Sólo entonces se confirma el pago simulado mediante un contrato/adaptador autorizado por Ventas, con referencia e idempotencia. El webhook actual de pasarela `POST /api/v1/pedidos/{pedidoId}/pagos/notificacion` no se invoca con credenciales de Marketplace ni datos de tarjeta inventados. Contrato, actor, scopes, errores y compensaciones siguen abiertos en `I-02`/`X-P0-02`.
- **RN-F026-06:** `SUCCEEDED` local requiere `PAGADO` confirmado por Ventas para el mismo `orderId`; `CREADO`, aptitud incierta, timeout o respuesta de pago incierta permanecen pendientes de reconciliación. Una expiración/cancelación no se convierte en éxito por un replay tardío.

- [ ] **CA-F026-01:** Misma operación no crea dos pedidos.
- [ ] **CA-F026-02:** Datos de documento inválidos no se transmiten.
- [ ] **CA-F026-03:** El happy path con y sin cupón termina en `PAGADO` observable en Ventas; reintentos no duplican pedido ni confirmación simulada.
- [ ] **CA-F026-04:** `CREADO` o un resultado incierto nunca navega a confirmación pagada.

Fuente: `POST /api/v1/pedidos` de Ventas. Faltan idempotencia contractual para creación, señal de aptitud para pagar y vía autorizada para confirmar pago simulado (`I-02`). No se asigna una URL o scope inexistente al proveedor.
