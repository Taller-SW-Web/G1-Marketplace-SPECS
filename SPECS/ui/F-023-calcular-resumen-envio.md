# Spec UI — F-023 Resumen y envío

Ruta `/checkout/resumen`. Presenta líneas, subtotal, descuentos automáticos, envío, total estimado, plazo y dirección resumida; muestra enlace para editar dirección/carrito.

| Estado | Interfaz |
|---|---|
| Calculando | Skeleton y texto “Calculando tu envío”. |
| Cotizado | Desglose con moneda, plazo y vigencia. |
| Sin cobertura | Mensaje, editar dirección y volver al carrito. |
| Atención | Línea/precio cambió; lista acción correctiva. |
| Error | Reintentar cotización; no inventa montos. |

Cada importe tiene etiqueta; total usa texto “estimado”. No se ocultan cambios tras recargar, y `aria-live` anuncia resultado sin desplazar foco.

- [ ] **UI-F023-01:** Envío gratis sólo se muestra si Despacho devuelve costo cero válido.
