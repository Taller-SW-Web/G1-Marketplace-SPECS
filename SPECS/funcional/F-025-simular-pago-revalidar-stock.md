# Spec funcional — F-025 Simular pago y revalidar stock

| Campo | Valor |
|---|---|
| ID | `F-025` |
| Estado | Aprobada para planificación; integración condicionada por `I-01` e `I-02` para creación posterior. |

Simula aprobación de pago y realiza la última revalidación de carrito, precio, beneficio, envío y stock antes de F-026. Incluye crear `CheckoutOperation` en estado `PREPARED`; excluye procesador de pagos real, consumo definitivo de inventario y creación de pedido.

- **RN-F025-01:** Simulación no solicita ni almacena tarjeta, CVV o token de pago.
- **RN-F025-02:** Revalidación usa el resumen vigente; toda variación exige volver a revisar antes de aprobar.
- **RN-F025-03:** Idempotency-Key + fingerprint protegen la preparación; misma clave/mismo contenido retorna resultado, clave reutilizada con otro contenido se rechaza.
- **RN-F025-04:** `PREPARED` no es pedido ni cobro; F-026 será responsable de enviar la orden.

- [ ] **CA-F025-01:** Stock insuficiente o cupón vencido no deja operación `PREPARED`.
- [ ] **CA-F025-02:** Reintentar la misma preparación no duplica `CheckoutOperation`.
- [ ] **CA-F025-03:** Una preparación no descuenta stock ni consume cupón.
