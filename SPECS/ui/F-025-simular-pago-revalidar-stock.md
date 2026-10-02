# Spec UI — F-025 Simular pago y revalidar stock

Ruta `/checkout/pago`. Explica que el entorno usa pago simulado; muestra resumen final, checkbox de confirmación y botón “Confirmar pago simulado”.

| Estado | Interfaz |
|---|---|
| Listo | Resumen vigente y acción habilitada. |
| Procesando | CTA bloqueado, progreso y no navegación destructiva. |
| Preparado | Confirmación “Pago simulado aprobado”; CTA de F-026 separado. |
| Revisión requerida | Cambios de precio/stock/cupón/envío con retorno a resumen. |
| Error | Reintentar seguro sin duplicar preparación. |

No hay campos de tarjeta ni iconografía que implique pago real. El foco llega a confirmación/error, con `aria-live` y texto explícito.

- [ ] **UI-F025-01:** El usuario no interpreta la simulación como cargo real.
