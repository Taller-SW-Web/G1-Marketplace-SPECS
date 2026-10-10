# Spec UI — F-025 Simular pago y revalidar stock

Ruta `/checkout/pago`. Explica que el entorno usará pago simulado más adelante; muestra resumen final, checkbox de consentimiento y botón “Preparar compra simulada”. Esta acción no aprueba un pago.

| Estado | Interfaz |
|---|---|
| Listo | Resumen vigente y acción habilitada. |
| Procesando | CTA bloqueado, progreso y no navegación destructiva. |
| Preparado | “Preparación lista; aún no se ha confirmado ningún pago”; CTA de F-026 separado. |
| Revisión requerida | Cambios de precio/stock/cupón/envío con retorno a resumen. |
| Error | Reintentar seguro sin duplicar preparación. |

No hay campos de tarjeta ni iconografía que implique pago real. El foco llega a confirmación/error, con `aria-live` y texto explícito.

- [ ] **UI-F025-01:** El usuario no interpreta la simulación como cargo real.
- [ ] **UI-F025-02:** `PREPARED` tampoco se presenta como pago aprobado o pedido definitivo.
