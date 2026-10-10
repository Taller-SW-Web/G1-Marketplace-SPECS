# Spec funcional — F-025 Simular pago y revalidar stock

| Campo | Valor |
|---|---|
| ID | `F-025` |
| Estado | Revisada por `G1-P0-01` y `X-P0-02/03`; integración final bloqueada por `I-01` e `I-02`. |

Registra el consentimiento para una **futura operación de pago simulado** y revalida carrito, precio, beneficio, envío y estado comercial de stock antes de F-026. Crea `CheckoutOperation` en `PREPARED`; esto no equivale a pago aprobado, pedido creado ni reserva de stock. El resultado simulado definitivo sólo puede confirmarse después de crear el pedido y recibir de Ventas una señal contractual de aptitud para pagar, cuya forma sigue pendiente (`X-P0-02`). No hay procesador bancario real.

- **RN-F025-01:** Simulación no solicita ni almacena tarjeta, CVV o token de pago.
- **RN-F025-02:** Revalidación usa el resumen vigente; toda variación exige volver a revisar antes de preparar. El estado comercial actual de un SKU no garantiza N unidades (`X-P0-03`); la reserva autoritativa ocurre bajo la orquestación de Ventas.
- **RN-F025-03:** Idempotency-Key + fingerprint protegen la preparación; misma clave/mismo contenido retorna resultado, clave reutilizada con otro contenido se rechaza.
- **RN-F025-04:** `PREPARED` no es pedido, reserva ni pago aprobado; F-026 enviará la orden y coordinará la conclusión simulada mediante el protocolo homologado con Ventas, sin asumir el rol de una pasarela.

- [ ] **CA-F025-01:** Stock insuficiente o cupón vencido no deja operación `PREPARED`.
- [ ] **CA-F025-02:** Reintentar la misma preparación no duplica `CheckoutOperation`.
- [ ] **CA-F025-03:** Una preparación no descuenta stock ni consume cupón.
- [ ] **CA-F025-04:** Ninguna pantalla o respuesta API presenta `PREPARED` como transacción pagada.
