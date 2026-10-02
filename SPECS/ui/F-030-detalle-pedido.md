# Spec UI — F-030 Detalle de pedido

Ruta `/mis-pedidos/{orderId}`: cabecera con código/estado, lista de ítems, desglose histórico, envío resumido e historial. Acción “Seguir envío” se muestra sólo si existe tracking (F-032). Datos sensibles se omiten o enmascaran. Timeline accesible en texto, no sólo visual.

- [ ] **UI-F030-01:** El detalle comunica estado y fecha de cada hito a lectores de pantalla.
