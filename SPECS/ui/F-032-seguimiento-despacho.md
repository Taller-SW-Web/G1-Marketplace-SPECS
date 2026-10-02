# Spec UI — F-032 Seguimiento de despacho

Ruta `/mis-pedidos/{orderId}/seguimiento`. Línea de tiempo con estado actual, fecha estimada e hitos fechados. Estados: sin despacho, cargando, disponible y error recuperable. No mapa/geolocalización.

Cada hito comunica texto/fecha; no sólo color. Retorno al detalle y diseño móvil.

- [ ] **UI-F032-01:** “Aún estamos preparando tu pedido” no se confunde con fallo.
