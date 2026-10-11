# Plan y seguimiento de implementación — Marketplace

Versión 0.2.0 · Replanificación 2026-10-10.

Este directorio planifica el software y sus evidencias para los hitos de **semanas 8, 11, 14 y 16**. Son cinco iteraciones de duración desigual desde semana 7. No contiene specs ni afirma que las tareas estén ejecutadas. La PPT y la explicación de IA pertenecen a la exposición, no al cronograma de desarrollo.

## Lectura sugerida

1. [Plan general, entregas y capacidad](PLAN-IMPLEMENTACION.md).
2. [Decisiones y bloqueos](DECISIONES-Y-BLOQUEOS.md).
3. [Pruebas y DevSecOps](DEVSECOPS-Y-PRUEBAS.md).
4. [Iteraciones](iteraciones/README.md).
5. [Seguimiento y tareas](seguimiento/README.md).
6. [Repartición por integrantes y guía de colaboración para H3/semana 8](repartición%20por%20integrantes/README.md).
7. Plan individual F-### dentro de `funcionalidades/`, según el catálogo siguiente.

Plan ≠ specs: entrada = funcional + UI + API + React; salida = trabajo verificable. Las tareas están dentro de `plan/seguimiento` por petición del PO, no dentro de `SPECS`.

## Planes por funcionalidad

| ID | Plan | Sprint |
|---|---|---|
| F-001 | [Registrar cliente](funcionalidades/F-001-registrar-cliente.md) | S2 |
| F-002 | [Iniciar sesión](funcionalidades/F-002-iniciar-sesion.md) | S2 |
| F-003 | [Cerrar sesión](funcionalidades/F-003-cerrar-sesion.md) | S2 |
| F-004 | [Solicitar recuperación de contraseña](funcionalidades/F-004-solicitar-recuperacion-password.md) | S5 |
| F-005 | [Restablecer contraseña](funcionalidades/F-005-restablecer-password.md) | S5 |
| F-006 | [Visualizar inicio, categorías y destacados](funcionalidades/F-006-inicio-categorias-destacados.md) | S1 |
| F-007 | [Buscar productos por texto](funcionalidades/F-007-buscar-productos-texto.md) | S1 |
| F-008 | [Filtrar catálogo](funcionalidades/F-008-filtrar-catalogo.md) | S2 |
| F-009 | [Ordenar resultados](funcionalidades/F-009-ordenar-catalogo.md) | S2 |
| F-010 | [Paginar resultados](funcionalidades/F-010-paginar-catalogo.md) | S2 |
| F-011 | [Visualizar ficha y galería del producto](funcionalidades/F-011-detalle-producto.md) | S2 |
| F-012 | [Visualizar precio, oferta y descuento vigente](funcionalidades/F-012-precio-oferta-descuento.md) | S2 |
| F-013 | [Seleccionar atributos y variante del producto](funcionalidades/F-013-seleccion-atributos-variante.md) | S2 |
| F-014 | [Consultar disponibilidad de stock](funcionalidades/F-014-consultar-disponibilidad-stock.md) | S2 |
| F-015 | [Visualizar productos relacionados](funcionalidades/F-015-productos-relacionados.md) | S5 |
| F-016 | [Agregar ítem al carrito](funcionalidades/F-016-agregar-item-carrito.md) | S2 |
| F-017 | [Cambiar la cantidad de un ítem](funcionalidades/F-017-cambiar-cantidad-item-carrito.md) | S3 |
| F-018 | [Quitar un ítem del carrito](funcionalidades/F-018-quitar-item-carrito.md) | S3 |
| F-019 | [Visualizar el carrito, totales y estado vacío](funcionalidades/F-019-visualizar-carrito.md) | S2 |
| F-020 | [Fusionar carrito anónimo al iniciar sesión](funcionalidades/F-020-fusionar-carrito-anonimo.md) | S5 |
| F-021 | [Mover un ítem del carrito a favoritos](funcionalidades/F-021-mover-carrito-favoritos.md) | S5 |
| F-022 | [Capturar o seleccionar dirección de envío](funcionalidades/F-022-seleccionar-direccion-envio.md) | S3 |
| F-023 | [Calcular y mostrar resumen de compra y envío](funcionalidades/F-023-calcular-resumen-envio.md) | S3 |
| F-024 | [Validar y aplicar cupón o promoción](funcionalidades/F-024-validar-aplicar-cupon-promocion.md) | S3 |
| F-025 | [Simular pago y revalidar stock](funcionalidades/F-025-simular-pago-revalidar-stock.md) | S3 |
| F-026 | [Crear la orden en Ventas y Postventa](funcionalidades/F-026-crear-orden-ventas.md) | S3 |
| F-027 | [Mostrar la confirmación de la orden](funcionalidades/F-027-confirmacion-orden.md) | S3 |
| F-028 | [Consultar historial de pedidos](funcionalidades/F-028-historial-pedidos.md) | S3 |
| F-029 | [Filtrar el historial de pedidos](funcionalidades/F-029-filtrar-historial-pedidos.md) | S5 |
| F-030 | [Visualizar detalle de pedido](funcionalidades/F-030-detalle-pedido.md) | S3 |
| F-031 | [Reordenar una compra anterior](funcionalidades/F-031-reordenar-compra.md) | S5 |
| F-032 | [Consultar seguimiento de despacho](funcionalidades/F-032-seguimiento-despacho.md) | S4 |
| F-033 | [Generar plantilla de correo](funcionalidades/F-033-generar-plantilla-correo.md) | S3 |
| F-034 | [Enviar confirmación asíncrona](funcionalidades/F-034-enviar-confirmacion-asincrona.md) | S3 |
| F-035 | [Enviar actualización de despacho por correo](funcionalidades/F-035-enviar-actualizacion-despacho.md) | S4 |
| F-036 | [Agregar producto a favoritos](funcionalidades/F-036-agregar-favorito.md) | S2 |
| F-037 | [Visualizar favoritos](funcionalidades/F-037-visualizar-favoritos.md) | S2 |
| F-038 | [Quitar favorito](funcionalidades/F-038-quitar-favorito.md) | S2 |
| F-039 | [Mover favorito al carrito](funcionalidades/F-039-mover-favorito-carrito.md) | S5 |
| F-040 | [Registrar evaluación postentrega](funcionalidades/F-040-evaluacion-postentrega.md) | S5 |

Este catálogo reparte por **fecha y entregable**; sólo S1/H3 tiene una [propuesta de reparto humano](repartición%20por%20integrantes/README.md), sujeta a estimación y aceptación. S2–S5 siguen sin asignar. Los paquetes Figma no determinan quién programa. [El plan maestro](PLAN-IMPLEMENTACION.md) gobierna los requisitos de cada hito.

