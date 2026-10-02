# Spec funcional — F-026 Crear la orden en Ventas y Postventa

| Campo | Valor |
|---|---|
| ID | `F-026` |
| Estado | Aprobada para planificación; integración bloqueada por `I-02`. |

Envía una operación `PREPARED` a Ventas para crear un pedido. Incluye completar el contacto requerido por Ventas, copiar transitoriamente dirección/resumen y registrar resultado en `CheckoutOperation`; excluye cobro real, consumo directo de stock y notificación al cliente.

- **RN-F026-01:** Sólo una operación `PREPARED` del cliente puede enviarse; misma clave y fingerprint devuelve el resultado original.
- **RN-F026-02:** Si perfil no aporta nombre, documento, teléfono o email requeridos por Ventas, Marketplace solicita sólo los campos faltantes y los valida; no los persiste como perfil local.
- **RN-F026-03:** Se envían SKU, cantidades, snapshots revalidados, beneficio seleccionado, dirección/cotización y pago simulado. Ventas es dueño del pedido final.
- **RN-F026-04:** Marketplace no considera éxito incierto como fallo: conserva `SUBMITTED` y permite consultar el resultado idempotente.

- [ ] **CA-F026-01:** Misma operación no crea dos pedidos.
- [ ] **CA-F026-02:** Datos de documento inválidos no se transmiten.

Fuente: `POST /api/v1/pedidos` de Ventas. Falta que Ventas acepte y documente `Idempotency-Key`, misma clave/mismo payload y respuesta repetida (`I-02`).
