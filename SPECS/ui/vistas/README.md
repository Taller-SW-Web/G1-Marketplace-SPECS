# Catálogo de vistas del Marketplace

Este directorio contiene las especificaciones visuales por pantalla o ruta principal. Una vista puede reunir varias funcionalidades `F-###`; las specs funcionales y UI atómicas continúan siendo las fuentes del comportamiento, mientras que cada documento `V-###` define cómo se compone el entregable que se diseñará en Figma.

Los mockups de estas vistas se ubicarán en la [carpeta de vistas de Figma](https://www.figma.com/files/team/1686774887312660587/folder/662579480?fuid=1686774885834417394), separada del archivo de la biblioteca del sistema de diseño enlazado en [`DS-001`](../DS-001-sistema-diseno-marketplace.md). El enlace recibido es de carpeta; falta registrar la URL directa del archivo de pantallas y los enlaces específicos de páginas y frames.

## Reglas

- Cada archivo representa una pantalla completa, no una funcionalidad aislada.
- Los estados de carga, vacío, error, éxito y validación se documentan dentro de la vista.
- Los modales, drawers, toasts y demás elementos superpuestos se enlazan desde `../overlays/`.
- Los correos transaccionales se enlazan desde `../comunicaciones/`.
- Desktop y mobile son variantes obligatorias de la misma vista, salvo que la spec justifique una excepción.
- El nombre del frame de Figma debe comenzar con el ID `V-###`.

El diseño puede avanzar por etapas sin cambiar ese alcance. En el paquete de checkout (`V-010` a `V-014`), Jim está trabajando primero los frames desktop; los frames mobile se diseñarán después. Los estados de la sección 7 siguen vigentes en ambas etapas. Al incorporar un frame desktop adicional, se registra con su nombre exacto en la sección 12 de la spec correspondiente y se enlaza el frame final de Figma.

## Estados documentales

- `Pendiente`: archivo todavía no creado.
- `Borrador`: estructura y decisiones iniciales documentadas.
- `En revisión`: contenido completo pendiente de validación del equipo.
- `Aprobada`: lista para asignación y diseño de alta fidelidad.

## Inventario vigente

| ID | Vista | Ruta | Funcionalidades | Archivo | Estado |
|---|---|---|---|---|---|
| `V-001` | Inicio de sesión | `/login` | F-002, F-020 | [`V-001-inicio-sesion.md`](./V-001-inicio-sesion.md) | En revisión |
| `V-002` | Registro | `/registro` | F-001 | [`V-002-registro.md`](./V-002-registro.md) | En revisión |
| `V-003` | Recuperación de contraseña | `/recuperar-contrasena` | F-004 | [`V-003-recuperacion-contrasena.md`](./V-003-recuperacion-contrasena.md) | En revisión |
| `V-004` | Restablecimiento de contraseña | `/restablecer-contrasena` | F-005 | [`V-004-restablecimiento-contrasena.md`](./V-004-restablecimiento-contrasena.md) | En revisión |
| `V-005` | Inicio | `/` | F-006, F-036 | [`V-005-inicio.md`](./V-005-inicio.md) | En revisión |
| `V-006` | Catálogo y resultados | `/catalogo` | F-007–F-010, F-036 | [`V-006-catalogo-resultados.md`](./V-006-catalogo-resultados.md) | En revisión |
| `V-007` | Ficha del producto | `/productos/{slug}` | F-011–F-016, F-036 | [`V-007-ficha-producto.md`](./V-007-ficha-producto.md) | En revisión |
| `V-008` | Carrito | `/carrito` | F-017–F-021 | [`V-008-carrito.md`](./V-008-carrito.md) | En revisión |
| `V-009` | Favoritos | `/favoritos` | F-037–F-039 | [`V-009-favoritos.md`](./V-009-favoritos.md) | En revisión |
| `V-010` | Dirección de envío | `/checkout/direccion` | F-022 | [`V-010-direccion-envio.md`](./V-010-direccion-envio.md) | En revisión |
| `V-011` | Resumen, envío y beneficio | `/checkout/resumen` | F-023, F-024 | [`V-011-resumen-envio-beneficio.md`](./V-011-resumen-envio-beneficio.md) | En revisión |
| `V-012` | Pago simulado | `/checkout/pago` | F-025 | [`V-012-pago-simulado.md`](./V-012-pago-simulado.md) | En revisión |
| `V-013` | Creación de la orden | `/checkout/confirmacion` | F-026 | [`V-013-creacion-orden.md`](./V-013-creacion-orden.md) | En revisión |
| `V-014` | Pedido confirmado | `/checkout/confirmado/{orderId}` | F-027, F-034 | [`V-014-pedido-confirmado.md`](./V-014-pedido-confirmado.md) | En revisión |
| `V-015` | Historial de pedidos | `/mis-pedidos` | F-028, F-029 | [`V-015-historial-pedidos.md`](./V-015-historial-pedidos.md) | En revisión |
| `V-016` | Detalle y reordenado | `/mis-pedidos/{orderId}` | F-030, F-031 | [`V-016-detalle-reordenado.md`](./V-016-detalle-reordenado.md) | En revisión |
| `V-017` | Seguimiento | `/mis-pedidos/{orderId}/seguimiento` | F-032 | [`V-017-seguimiento.md`](./V-017-seguimiento.md) | En revisión |

## Fuente transversal

Todas las vistas deben aplicar [`DS-001`](../DS-001-sistema-diseno-marketplace.md) y utilizar [`PLANTILLA.md`](./PLANTILLA.md) como estructura mínima.
