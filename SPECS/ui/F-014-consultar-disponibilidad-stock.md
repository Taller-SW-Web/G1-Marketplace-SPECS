# Spec UI — F-014 Consultar disponibilidad de stock

| Campo | Valor |
|---|---|
| ID | `F-014` |
| Estado | Aprobada para planificación; actualización a cuatro estados alineada con M01 de G6; aprobación G1 e integración pendientes; integración condicionada por `I-01`. |
| Sistema de diseño vigente | `DS-001` v`0.2.0`; aplicación visual pendiente de revisión |

La región se sitúa bajo F-012 y F-013 en `/productos/{slug}`.

| Estado | Contenido |
|---|---|
| Sin SKU | “Selecciona una opción para consultar disponibilidad”. |
| Cargando | Skeleton de una línea; no texto “Disponible”. |
| Disponible | Icono y texto “Disponible”. |
| Stock bajo | Icono y texto “Quedan pocas unidades”. No se muestra cantidad. |
| Agotado | Icono y texto “Agotado”; F-016 deberá deshabilitar compra. |
| Disponibilidad por confirmar | Icono y texto “Disponibilidad por confirmar”; botón “Volver a consultar”. Es un resultado comercial válido, no un error: no se muestra “Agotado” ni se prometen unidades. |
| Error | “No pudimos consultar disponibilidad” y botón Reintentar. |

No se comunica ubicación, saldo interno ni promesa de reserva. Estado usa texto, icono y color de DS-001; se anuncia mediante `aria-live="polite"`. En móvil permanece junto al selector, no en un modal.

- [ ] **UI-F014-01:** Agotado, error y carga son distinguibles sin depender sólo del color.
- [ ] **UI-F014-02:** Cambiar SKU elimina el estado anterior hasta tener respuesta nueva.
- [ ] **UI-F014-03:** “Disponibilidad por confirmar” se distingue de “Agotado” y del error técnico por texto e icono, no sólo por color.

## Contraste con G6 — 03/11/2026

Fuente: [M01–M03 del acuerdo G1/G6](https://github.com/Taller-SW-Web/G6-Productos-Ofertas-docs/blob/40b566976fb94d924116dcd01d41b3276c2bc9e3/integraciones/ACUERDO_G1_G6_H4_2026-10-20.md). Se adopta la semántica del owner para avanzar diseño y pruebas propias. El código local/MOCK no acredita homologación REAL ni cierra la issue. Se conserva fuente única de cumplimiento; no se suman ubicaciones ni se garantiza cantidad por consultar un estado.
