# Plan y seguimiento de implementación — Marketplace

Versión 0.1.0 · En revisión · 2026-10-02.

Este directorio desarrolla exclusivamente el punto 3 de la lista de preparación: plan de implementación y tareas para **semanas 6 a 15**, cinco sprints de dos semanas. No contiene specs ni afirma que ya exista código.

## Lectura sugerida

1. [Plan general, entregas y capacidad](PLAN-IMPLEMENTACION.md).
2. [Decisiones y bloqueos](DECISIONES-Y-BLOQUEOS.md).
3. [Pruebas y DevSecOps](DEVSECOPS-Y-PRUEBAS.md).
4. [Iteraciones](iteraciones/README.md).
5. [Seguimiento y tareas](seguimiento/README.md).
6. Plan individual F-### dentro de `funcionalidades/`, según el catálogo siguiente.

Plan ≠ specs: entrada = funcional + UI + API + React; salida = trabajo verificable. Las tareas están dentro de `plan/seguimiento` por petición del PO, no dentro de `SPECS`.

## Planes por funcionalidad

| ID | Plan | Sprint |
|---|---|---|
| F-001 | [Registrar cliente](funcionalidades/F-001-registrar-cliente.md) | S1 |
| F-002 | [Iniciar sesión](funcionalidades/F-002-iniciar-sesion.md) | S1 |
| F-003 | [Cerrar sesión](funcionalidades/F-003-cerrar-sesion.md) | S1 |
| F-004 | [Solicitar recuperación de contraseña](funcionalidades/F-004-solicitar-recuperacion-password.md) | S1 |
| F-005 | [Restablecer contraseña](funcionalidades/F-005-restablecer-password.md) | S1 |
| F-006 | [Visualizar inicio, categorías y destacados](funcionalidades/F-006-inicio-categorias-destacados.md) | S2 |
| F-007 | [Buscar productos por texto](funcionalidades/F-007-buscar-productos-texto.md) | S2 |
| F-008 | [Filtrar catálogo](funcionalidades/F-008-filtrar-catalogo.md) | S2 |
| F-009 | [Ordenar resultados](funcionalidades/F-009-ordenar-catalogo.md) | S2 |
| F-010 | [Paginar resultados](funcionalidades/F-010-paginar-catalogo.md) | S2 |
| F-011 | [Visualizar ficha y galería del producto](funcionalidades/F-011-detalle-producto.md) | S2 |
| F-012 | [Visualizar precio, oferta y descuento vigente](funcionalidades/F-012-precio-oferta-descuento.md) | S2 |
| F-013 | [Seleccionar atributos y variante del producto](funcionalidades/F-013-seleccion-atributos-variante.md) | S2 |
| F-014 | [Consultar disponibilidad de stock](funcionalidades/F-014-consultar-disponibilidad-stock.md) | S2 |
| F-015 | [Visualizar productos relacionados](funcionalidades/F-015-productos-relacionados.md) | S2 |
| F-016 | [Agregar ítem al carrito](funcionalidades/F-016-agregar-item-carrito.md) | S2 |
| F-017 | [Cambiar la cantidad de un ítem](funcionalidades/F-017-cambiar-cantidad-item-carrito.md) | S3 |
| F-018 | [Quitar un ítem del carrito](funcionalidades/F-018-quitar-item-carrito.md) | S3 |
| F-019 | [Visualizar el carrito, totales y estado vacío](funcionalidades/F-019-visualizar-carrito.md) | S3 |
| F-020 | [Fusionar carrito anónimo al iniciar sesión](funcionalidades/F-020-fusionar-carrito-anonimo.md) | S3 |
| F-021 | [Mover un ítem del carrito a favoritos](funcionalidades/F-021-mover-carrito-favoritos.md) | S3 |
| F-022 | [Capturar o seleccionar dirección de envío](funcionalidades/F-022-seleccionar-direccion-envio.md) | S4 |
| F-023 | [Calcular y mostrar resumen de compra y envío](funcionalidades/F-023-calcular-resumen-envio.md) | S4 |
| F-024 | [Validar y aplicar cupón o promoción](funcionalidades/F-024-validar-aplicar-cupon-promocion.md) | S4 |
| F-025 | [Simular pago y revalidar stock](funcionalidades/F-025-simular-pago-revalidar-stock.md) | S4 |
| F-026 | [Crear la orden en Ventas y Postventa](funcionalidades/F-026-crear-orden-ventas.md) | S4 |
| F-027 | [Mostrar la confirmación de la orden](funcionalidades/F-027-confirmacion-orden.md) | S4 |
| F-028 | [Consultar historial de pedidos](funcionalidades/F-028-historial-pedidos.md) | S5 |
| F-029 | [Filtrar el historial de pedidos](funcionalidades/F-029-filtrar-historial-pedidos.md) | S5 |
| F-030 | [Visualizar detalle de pedido](funcionalidades/F-030-detalle-pedido.md) | S5 |
| F-031 | [Reordenar una compra anterior](funcionalidades/F-031-reordenar-compra.md) | S5 |
| F-032 | [Consultar seguimiento de despacho](funcionalidades/F-032-seguimiento-despacho.md) | S5 |
| F-033 | [Generar plantilla de correo](funcionalidades/F-033-generar-plantilla-correo.md) | S5 |
| F-034 | [Enviar confirmación asíncrona](funcionalidades/F-034-enviar-confirmacion-asincrona.md) | S5 |
| F-035 | [Enviar actualización de despacho por correo](funcionalidades/F-035-enviar-actualizacion-despacho.md) | S5 |
| F-036 | [Agregar producto a favoritos](funcionalidades/F-036-agregar-favorito.md) | S3 |
| F-037 | [Visualizar favoritos](funcionalidades/F-037-visualizar-favoritos.md) | S3 |
| F-038 | [Quitar favorito](funcionalidades/F-038-quitar-favorito.md) | S3 |
| F-039 | [Mover favorito al carrito](funcionalidades/F-039-mover-favorito-carrito.md) | S3 |
| F-040 | [Registrar evaluación postentrega](funcionalidades/F-040-evaluacion-postentrega.md) | S5 |

Los responsables de ejecución que se proponen en las tareas usan los roles actuales; quedan por confirmar, no modifican paquetes de Figma. Los puntos 1,4,5 de la lista original no se marcan ni se ejecutan aquí. No se recuperan los dos planes que ya estaban eliminados en el árbol de trabajo.

