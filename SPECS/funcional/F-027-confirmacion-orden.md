# Spec funcional — F-027 Mostrar la confirmación de la orden

| Campo | Valor |
|---|---|
| ID | `F-027` |
| Estado | Aprobada para planificación; depende de F-026. |

Muestra al cliente el resultado confirmado de la creación del pedido: código, estado inicial, total, fecha y próximos pasos. Excluye correo, seguimiento detallado y actualización posterior.

- **RN-F027-01:** Sólo se confirma cuando F-026 posee `externalOrderId`; `PREPARED` no es pedido.
- **RN-F027-02:** Se presenta el snapshot devuelto por Ventas, no un pedido local reconstruido.
- **RN-F027-03:** Resultado incierto muestra verificación en curso y no éxito.

- [ ] **CA-F027-01:** Se muestra un único código de pedido verificable.
- [ ] **CA-F027-02:** Un fallo de correo no cambia la confirmación.
