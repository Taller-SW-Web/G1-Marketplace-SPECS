# Spec UI — F-027 Confirmación de la orden

Ruta `/checkout/confirmado/{orderId}`. La confirmación de compra requiere `PAGADO` verificado en Ventas. Muestra código, fecha, total, resumen corto y acciones “Ver mi pedido” / “Seguir comprando”. Si el pedido permanece `CREADO`, se muestra un estado neutral de preparación/verificación, no esta confirmación. El correo se procesa por separado, sin prometer entrega inmediata.

Resultado incierto usa mensaje neutral y acción “Verificar pedido”, nunca icono de éxito. Si Ventas informa `ANULADO` por `PAGO_NO_COMPLETADO`, se comunica el rechazo de la simulación y se ofrece una salida segura. Código copiable y accesible sólo en la variante confirmada. No muestra documento ni dirección completa.

- [ ] **UI-F027-01:** Éxito y verificación pendiente son distintos visual y semánticamente.
- [ ] **UI-F027-02:** No se muestra título, icono ni CTA de compra confirmada cuando Ventas sólo devolvió `CREADO`.
- [ ] **UI-F027-03:** Un pedido `ANULADO` por pago simulado rechazado no se presenta como compra confirmada ni invita a repetir el mismo POST.
