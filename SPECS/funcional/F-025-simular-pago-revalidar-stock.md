# Spec funcional — F-025 Simular pago y revalidar stock

| Campo | Valor |
|---|---|
| ID | `F-025` |
| Estado | Alineada con la respuesta de Ventas del 10/10/2026; integración pendiente de implementación y pruebas de `I-01`/`I-02`. |

Registra el consentimiento para una **futura operación de pago simulado** y revalida carrito, precio, beneficio, envío y estado comercial de stock antes de F-026. Crea `CheckoutOperation` en `PREPARED`; esto no equivale a pago aprobado, pedido creado ni reserva de stock. Ventas confirma reserva y cupón al responder `201 Created` a la creación posterior, y activa internamente su simulador. Marketplace observará el resultado en el estado del pedido. No hay captura bancaria en Marketplace.

- **RN-F025-01:** Simulación no solicita ni almacena tarjeta, CVV o token de pago.
- **RN-F025-02:** Revalidación usa el resumen vigente; toda variación exige volver a revisar antes de preparar. El estado comercial actual de un SKU no garantiza N unidades (`X-P0-03`); la reserva autoritativa ocurre bajo la orquestación de Ventas.
- **RN-F025-03:** Idempotency-Key + fingerprint protegen la preparación; misma clave/mismo contenido retorna resultado, clave reutilizada con otro contenido se rechaza.
- **RN-F025-04:** `PREPARED` no es pedido, reserva ni pago aprobado; F-026 enviará la orden y consultará su estado. Ventas coordina el simulador y su webhook de pago sin participación de Marketplace.

- [ ] **CA-F025-01:** Stock insuficiente o cupón vencido no deja operación `PREPARED`.
- [ ] **CA-F025-02:** Reintentar la misma preparación no duplica `CheckoutOperation`.
- [ ] **CA-F025-03:** Una preparación no descuenta stock ni consume cupón.
- [ ] **CA-F025-04:** Ninguna pantalla o respuesta API presenta `PREPARED` como transacción pagada.
