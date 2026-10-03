# Specs de componentes React — Marketplace

Versión 0.1.0 · En revisión · 2026-10-02.

Esta carpeta completa el punto 2 de la lista de preparación: **40 specs React F-001–F-040**, con props/eventos, estado, consultas, validaciones, recuperación, accesibilidad y pruebas. No contiene implementación.

1. Leer [arquitectura transversal](ARQUITECTURA-REACT.md).
2. Leer funcional + UI + contrato API de la funcionalidad y las V/O/C relacionadas.
3. Leer su spec React y comprobar gates en [decisiones](../../plan/DECISIONES-Y-BLOQUEOS.md).
4. Implementar según [plan semanas 6–15](../../plan/PLAN-IMPLEMENTACION.md) y [seguimiento](../../plan/seguimiento/README.md).

Se respeta nomenclatura: mismo ID y nombre de archivo en las cuatro capas. DS-001 v0.2.0 es fuente visual vigente; aprobación de UI kit pendiente. Desktop primero, luego mobile; responsive no se elimina. F-033–F-035 describen también el límite no interactivo/servidor de correos, no nuevos endpoints navegador.

## Catálogo y trazabilidad

| Funcionalidad | React | Sprint objetivo |
|---|---|---|
| F-001 · Registrar cliente | [Spec](F-001-registrar-cliente.md) | S1 |
| F-002 · Iniciar sesión | [Spec](F-002-iniciar-sesion.md) | S1 |
| F-003 · Cerrar sesión | [Spec](F-003-cerrar-sesion.md) | S1 |
| F-004 · Solicitar recuperación de contraseña | [Spec](F-004-solicitar-recuperacion-password.md) | S1 |
| F-005 · Restablecer contraseña | [Spec](F-005-restablecer-password.md) | S1 |
| F-006 · Visualizar inicio, categorías y destacados | [Spec](F-006-inicio-categorias-destacados.md) | S2 |
| F-007 · Buscar productos por texto | [Spec](F-007-buscar-productos-texto.md) | S2 |
| F-008 · Filtrar catálogo | [Spec](F-008-filtrar-catalogo.md) | S2 |
| F-009 · Ordenar resultados | [Spec](F-009-ordenar-catalogo.md) | S2 |
| F-010 · Paginar resultados | [Spec](F-010-paginar-catalogo.md) | S2 |
| F-011 · Visualizar ficha y galería del producto | [Spec](F-011-detalle-producto.md) | S2 |
| F-012 · Visualizar precio, oferta y descuento vigente | [Spec](F-012-precio-oferta-descuento.md) | S2 |
| F-013 · Seleccionar atributos y variante del producto | [Spec](F-013-seleccion-atributos-variante.md) | S2 |
| F-014 · Consultar disponibilidad de stock | [Spec](F-014-consultar-disponibilidad-stock.md) | S2 |
| F-015 · Visualizar productos relacionados | [Spec](F-015-productos-relacionados.md) | S2 |
| F-016 · Agregar ítem al carrito | [Spec](F-016-agregar-item-carrito.md) | S2 |
| F-017 · Cambiar la cantidad de un ítem | [Spec](F-017-cambiar-cantidad-item-carrito.md) | S3 |
| F-018 · Quitar un ítem del carrito | [Spec](F-018-quitar-item-carrito.md) | S3 |
| F-019 · Visualizar el carrito, totales y estado vacío | [Spec](F-019-visualizar-carrito.md) | S3 |
| F-020 · Fusionar carrito anónimo al iniciar sesión | [Spec](F-020-fusionar-carrito-anonimo.md) | S3 |
| F-021 · Mover un ítem del carrito a favoritos | [Spec](F-021-mover-carrito-favoritos.md) | S3 |
| F-022 · Capturar o seleccionar dirección de envío | [Spec](F-022-seleccionar-direccion-envio.md) | S4 |
| F-023 · Calcular y mostrar resumen de compra y envío | [Spec](F-023-calcular-resumen-envio.md) | S4 |
| F-024 · Validar y aplicar cupón o promoción | [Spec](F-024-validar-aplicar-cupon-promocion.md) | S4 |
| F-025 · Simular pago y revalidar stock | [Spec](F-025-simular-pago-revalidar-stock.md) | S4 |
| F-026 · Crear la orden en Ventas y Postventa | [Spec](F-026-crear-orden-ventas.md) | S4 |
| F-027 · Mostrar la confirmación de la orden | [Spec](F-027-confirmacion-orden.md) | S4 |
| F-028 · Consultar historial de pedidos | [Spec](F-028-historial-pedidos.md) | S5 |
| F-029 · Filtrar el historial de pedidos | [Spec](F-029-filtrar-historial-pedidos.md) | S5 |
| F-030 · Visualizar detalle de pedido | [Spec](F-030-detalle-pedido.md) | S5 |
| F-031 · Reordenar una compra anterior | [Spec](F-031-reordenar-compra.md) | S5 |
| F-032 · Consultar seguimiento de despacho | [Spec](F-032-seguimiento-despacho.md) | S5 |
| F-033 · Generar plantilla de correo | [Spec](F-033-generar-plantilla-correo.md) | S5 |
| F-034 · Enviar confirmación asíncrona | [Spec](F-034-enviar-confirmacion-asincrona.md) | S5 |
| F-035 · Enviar actualización de despacho por correo | [Spec](F-035-enviar-actualizacion-despacho.md) | S5 |
| F-036 · Agregar producto a favoritos | [Spec](F-036-agregar-favorito.md) | S3 |
| F-037 · Visualizar favoritos | [Spec](F-037-visualizar-favoritos.md) | S3 |
| F-038 · Quitar favorito | [Spec](F-038-quitar-favorito.md) | S3 |
| F-039 · Mover favorito al carrito | [Spec](F-039-mover-favorito-carrito.md) | S3 |
| F-040 · Registrar evaluación postentrega | [Spec](F-040-evaluacion-postentrega.md) | S5 |

## Límites de esta entrega

Todos los documentos nuevos están en revisión; integración real continúa condicionada por I-01–I-06 y pendientes técnicos. Envío de solicitudes no equivale a acuerdo publicado ni prueba aprobada. Se preserva el reparto UI existente sin renombrarlo. El plan separa capacidad de diseño, implementación y homologación.

