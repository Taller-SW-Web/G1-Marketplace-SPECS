# Spec funcional — F-024 Validar y aplicar cupón o promoción

| Campo | Valor |
|---|---|
| ID | `F-024` |
| Estado | Aprobada para planificación; integración condicionada por `I-01`, `OPEN-11` y `OPEN-12`. |

Permite ingresar un cupón y presenta el mejor beneficio elegible para la cotización. Incluye promociones automáticas, validación sin consumo y recálculo temporal; excluye consumir cupón, que sólo ocurre al confirmar el pedido.

- **RN-F024-01:** Promociones decide elegibilidad/combinabilidad; Marketplace no calcula descuentos.
- **RN-F024-02:** Validar nunca consume cupón. El resultado puede vencer o ser rechazado al confirmar.
- **RN-F024-03:** Si hay empate, se respeta la prioridad del dueño: sin cupón, menor prioridad, identificador estable.
- **RN-F024-04:** Cupón se normaliza para consulta pero no se registra en logs en claro.
- **RN-F024-05:** Marketplace muestra el resultado y vigencia que devuelve Productos, sin recalcular ni asumir que existe un único `promotion_id` si se combinan beneficios. La evaluación/referencia y el desglose que viajarán al pedido dependen del snapshot canónico aún por acordar con Productos y Ventas (`X-P0-05/06`, `F-P1-05`).

- [ ] **CA-F024-01:** Un cupón inválido conserva el carrito y explica que no se aplicó.
- [ ] **CA-F024-02:** Un beneficio aplicado actualiza descuento/total estimado y su vencimiento.
- [ ] **CA-F024-03:** No se marca cupón como consumido antes de F-026.
- [ ] **CA-F024-04:** Una cotización vencida o una combinación de beneficios sin procedencia contractual no se confirma silenciosamente con el monto anterior.
