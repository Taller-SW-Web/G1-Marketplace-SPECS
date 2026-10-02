# Spec UI — F-027 Confirmación de la orden

Ruta `/checkout/confirmado/{orderId}`. Muestra código, fecha, total, estado `CREADO`, resumen corto y acciones “Ver mi pedido” / “Seguir comprando”. Informa que el correo se procesará por separado, sin prometer entrega inmediata.

Resultado incierto usa mensaje neutral y acción “Verificar pedido”, nunca icono de éxito. Código copiable y accesible. No muestra documento ni dirección completa.

- [ ] **UI-F027-01:** Éxito y verificación pendiente son distintos visual y semánticamente.
