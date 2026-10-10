# Spec funcional — F-027 Mostrar la confirmación de la orden

| Campo | Valor |
|---|---|
| ID | `F-027` |
| Estado | Revisada por `G1-P0-01`; depende de la confirmación de pago simulado homologada con Ventas en F-026. |

Muestra al cliente el resultado final de la compra simulada sólo cuando Ventas confirma `PAGADO` para el pedido creado: código, estado, total, fecha y próximos pasos. Excluye correo, seguimiento detallado y actualización posterior.

- **RN-F027-01:** Sólo se muestra éxito cuando F-026 posee `externalOrderId` y ha verificado `PAGADO` en Ventas para ese mismo pedido. `PREPARED`, `CREADO` y `SUBMITTED` no son compra final confirmada.
- **RN-F027-02:** Se presenta el snapshot devuelto por Ventas, no un pedido local reconstruido.
- **RN-F027-03:** Resultado incierto muestra verificación en curso y no éxito.
- **RN-F027-04:** Un pedido `CREADO` puede mostrarse como pendiente de preparación/pago simulado, sin check de éxito ni promesa de despacho. La salida y recuperación dependen de los estados finales acordados con Ventas.

- [ ] **CA-F027-01:** Se muestra un único código de pedido verificable.
- [ ] **CA-F027-02:** Un fallo de correo no cambia la confirmación.
- [ ] **CA-F027-03:** Nunca se usa `CREADO` como evidencia de pago simulado aprobado.
