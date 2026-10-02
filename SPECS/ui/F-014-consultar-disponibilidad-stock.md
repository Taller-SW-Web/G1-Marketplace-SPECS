# Spec UI — F-014 Consultar disponibilidad de stock

| Campo | Valor |
|---|---|
| ID | `F-014` |
| Estado | Aprobada para planificación; integración condicionada por `I-01`. |
| Sistema de diseño | `DS-001` v`0.1.0` |

La región se sitúa bajo F-012 y F-013 en `/productos/{slug}`.

| Estado | Contenido |
|---|---|
| Sin SKU | “Selecciona una opción para consultar disponibilidad”. |
| Cargando | Skeleton de una línea; no texto “Disponible”. |
| Disponible | Icono y texto “Disponible”. |
| Stock bajo | Icono y texto “Quedan pocas unidades”. No se muestra cantidad. |
| Agotado | Icono y texto “Agotado”; F-016 deberá deshabilitar compra. |
| Error | “No pudimos consultar disponibilidad” y botón Reintentar. |

No se comunica ubicación, saldo interno ni promesa de reserva. Estado usa texto, icono y color de DS-001; se anuncia mediante `aria-live="polite"`. En móvil permanece junto al selector, no en un modal.

- [ ] **UI-F014-01:** Agotado, error y carga son distinguibles sin depender sólo del color.
- [ ] **UI-F014-02:** Cambiar SKU elimina el estado anterior hasta tener respuesta nueva.
