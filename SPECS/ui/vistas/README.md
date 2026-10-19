# Catálogo de vistas del Marketplace

Este directorio contiene las especificaciones visuales por pantalla o ruta principal. La [matriz de responsabilidad de implementación](../../RESPONSABILIDADES-PUNTA-A-PUNTA.md) asigna los bloques/F-### del código; cualquier responsable de diseño mencionado aquí conserva únicamente ese alcance visual. Una vista puede reunir varias funcionalidades `F-###`; las specs funcionales y UI atómicas continúan siendo las fuentes del comportamiento, mientras que cada documento `V-###` define cómo se compone el entregable que se diseñará en Figma.

Los mockups se ubican en la [carpeta de vistas de Figma](https://www.figma.com/files/team/1686774887312660587/folder/662579480?fuid=1686774885834417394), separada de la biblioteca enlazada en [`DS-001`](../DS-001-sistema-diseno-marketplace.md). El [archivo Mockups](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups) contiene la página [Checkout](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=1-5), verificada el 18/10 con enlace directo aportado por el PO.

## Reglas

- Cada archivo representa una pantalla completa, no una funcionalidad aislada.
- Los estados de carga, vacío, error, éxito y validación se documentan dentro de la vista.
- Los modales, drawers, toasts y demás elementos superpuestos se enlazan desde `../overlays/`.
- Los correos transaccionales se enlazan desde `../comunicaciones/`.
- Desktop y mobile son variantes obligatorias de la misma vista, salvo que la spec justifique una excepción.
- El nombre del frame de Figma debe comenzar con el ID `V-###`.

El diseño puede avanzar por etapas sin cambiar ese alcance. La afirmación anterior de que los frames mobile de Checkout se diseñarían después quedó superada: el 18/10 se encontraron frames desktop y mobile en las cinco vistas. Se verificó su existencia y se inspeccionaron visualmente muestras V-010 mobile y V-014 desktop; **no se aprobó** el conjunto. Faltan el frame `V-011 / Mobile / Promoción automática` y el frame `V-013 / Mobile / Operación no preparada` exigidos por sus specs. El frame `V-014 / Desktop / Confirmado` muestra `CREADO` y “Pago simulado aprobado”, en conflicto con la condición `PAGADO` de V-014/F-027. Jim y el responsable visual deben resolver esas brechas antes de cambiar `En revisión` a `Aprobada`.

| Vista | Frames desktop | Frames mobile | Verificación estructural |
|---|---:|---:|---|
| `V-010` | 7 | 10 | Diseñada en ambas plataformas; aceptación visual pendiente. |
| `V-011` | 8 | 8 | Falta el estado mobile de promoción automática requerido. |
| `V-012` | 7 | 7 | Diseñada en ambas plataformas; aceptación visual pendiente. |
| `V-013` | 6 | 6 | Falta el estado mobile de operación no preparada requerido. |
| `V-014` | 6 | 6 | Hay contradicción de estado de pedido en el frame desktop confirmado. |

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
