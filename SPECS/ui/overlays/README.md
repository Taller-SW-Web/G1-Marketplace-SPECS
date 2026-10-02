# Catálogo de overlays y feedback del Marketplace

Este directorio especifica elementos visuales que aparecen sobre una vista o modifican temporalmente su estado: modales, drawers, visores, toasts, confirmaciones y feedback global. No sustituyen una ruta principal.

## Inventario vigente

| ID | Elemento | Tipo previsto | Funcionalidades | Archivo | Estado |
|---|---|---|---|---|---|
| `O-001` | Filtros mobile | Drawer | F-008, F-029 | [`O-001-filtros-mobile.md`](./O-001-filtros-mobile.md) | En revisión |
| `O-002` | Visor de galería | Modal/visor | F-011 | [`O-002-visor-galeria.md`](./O-002-visor-galeria.md) | En revisión |
| `O-003` | Autenticación requerida con retorno | Modal de decisión | F-002, F-021, F-036 | [`O-003-autenticacion-requerida.md`](./O-003-autenticacion-requerida.md) | En revisión |
| `O-004` | Confirmación de cierre durante checkout | Modal de confirmación | F-003 | [`O-004-confirmacion-cierre-checkout.md`](./O-004-confirmacion-cierre-checkout.md) | En revisión |
| `O-005` | Producto agregado al carrito | Toast/feedback | F-016 | [`O-005-producto-agregado-carrito.md`](./O-005-producto-agregado-carrito.md) | En revisión |
| `O-006` | Deshacer eliminación | Toast con acción | F-018, F-038 | [`O-006-deshacer-eliminacion.md`](./O-006-deshacer-eliminacion.md) | En revisión |
| `O-007` | Resultado de fusión de carrito | Resumen/modal | F-020 | [`O-007-resultado-fusion-carrito.md`](./O-007-resultado-fusion-carrito.md) | En revisión |
| `O-008` | Resultado de reordenado | Resumen/modal | F-031 | [`O-008-resultado-reordenado.md`](./O-008-resultado-reordenado.md) | En revisión |
| `O-009` | Evaluación postentrega | Modal/formulario | F-040 | [`O-009-evaluacion-postentrega.md`](./O-009-evaluacion-postentrega.md) | En revisión |
| `O-010` | Alertas y feedback global | Toast/banner/alerta | Transversal | [`O-010-alertas-feedback-global.md`](./O-010-alertas-feedback-global.md) | En revisión |

Cada overlay usa [`PLANTILLA.md`](./PLANTILLA.md), aplica [`DS-001`](../DS-001-sistema-diseno-marketplace.md) y debe indicar desde qué vistas puede activarse.
