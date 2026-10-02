# Spec funcional — F-034 Enviar confirmación asíncrona

| Campo | Valor |
|---|---|
| ID | `F-034` |
| Estado | Aprobada para planificación; requiere proveedor de correo. |

Encola y entrega correo de confirmación tras pedido exitoso. Incluye `NotificationDelivery`, render, reintentos/deduplicación; excluye alterar pedido si falla correo.

- **RN-F034-01:** `ORDER_CONFIRMATION + eventKey` es único; reintentos no duplican.
- **RN-F034-02:** Se persiste salida `PENDING` antes del worker; la web no espera proveedor.
- **RN-F034-03:** Destinatario cifrado y plantilla F-033; sin email en logs.
- **RN-F034-04:** Máximo de reintentos termina `FAILED` sin cambiar orden.

- [ ] **CA-F034-01:** Pedido creado responde aunque email falle temporalmente.
- [ ] **CA-F034-02:** Evento repetido produce una entrega lógica.
