# Plan y seguimiento de implementación — Marketplace

Versión 0.7.0 · Replanificación H4 2026-10-19; responsables asignados y estimación base fijada por el PO. Disponibilidad sin restricción horaria; verificar contrato, entorno y evidencia.

Este directorio planifica el software y sus evidencias para los hitos de **semanas 8, 11, 14 y 16**. Son cinco iteraciones de duración desigual desde semana 7. No contiene specs ni afirma que las tareas estén ejecutadas. La PPT y la explicación de IA pertenecen a la exposición, no al cronograma de desarrollo.

## Lectura sugerida

1. [Plan general, entregas y dependencias](PLAN-IMPLEMENTACION.md).
2. [Decisiones y bloqueos](DECISIONES-Y-BLOQUEOS.md).
3. [Pruebas y DevSecOps](DEVSECOPS-Y-PRUEBAS.md).
4. [Iteraciones](iteraciones/README.md).
5. [Seguimiento y tareas](seguimiento/README.md).
6. [Matriz de bloques, F-### y responsables](../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md), [paquetes individuales H3–H6](repartición%20por%20integrantes/README.md) y guía de colaboración.
7. Plan individual F-### dentro de `funcionalidades/`, según el catálogo siguiente.

Plan ≠ specs: entrada = funcional + UI + API + React; salida = trabajo verificable. Las tareas están dentro de `plan/seguimiento` por petición del PO, no dentro de `SPECS`.

[Inventario de Productos/Seguridad H4](ALCANCE-H4-PRODUCTOS-SEGURIDAD.md): 25 F dependientes de Productos; principal H4 20 circuito G6 + 5 cuenta = 25 cierres objetivo. Todas las otras F reciben implementación/pruebas G1 H4; los gates externos y cuatro niveles de evidencia permanecen.

## Planes por funcionalidad

| ID | Plan | Sprint |
|---|---|---|
| F-001 | [Registrar cliente](funcionalidades/F-001-registrar-cliente.md) | S02/H4 |
| F-002 | [Iniciar sesión](funcionalidades/F-002-iniciar-sesion.md) | S02/H4 |
| F-003 | [Cerrar sesión](funcionalidades/F-003-cerrar-sesion.md) | S02/H4 |
| F-004 | [Solicitar recuperación de contraseña](funcionalidades/F-004-solicitar-recuperacion-password.md) | S02/H4 |
| F-005 | [Restablecer contraseña](funcionalidades/F-005-restablecer-password.md) | S02/H4 |
| F-006 | [Visualizar inicio, categorías y destacados](funcionalidades/F-006-inicio-categorias-destacados.md) | S02/H4 (arrastre H3) |
| F-007 | [Buscar productos por texto](funcionalidades/F-007-buscar-productos-texto.md) | S02/H4 (arrastre H3) |
| F-008 | [Filtrar catálogo](funcionalidades/F-008-filtrar-catalogo.md) | S02/H4 |
| F-009 | [Ordenar resultados](funcionalidades/F-009-ordenar-catalogo.md) | S02/H4 |
| F-010 | [Paginar resultados](funcionalidades/F-010-paginar-catalogo.md) | S02/H4 |
| F-011 | [Visualizar ficha y galería del producto](funcionalidades/F-011-detalle-producto.md) | S02/H4 |
| F-012 | [Visualizar precio, oferta y descuento vigente](funcionalidades/F-012-precio-oferta-descuento.md) | S02/H4 |
| F-013 | [Seleccionar atributos y variante del producto](funcionalidades/F-013-seleccion-atributos-variante.md) | S02/H4 |
| F-014 | [Consultar disponibilidad de stock](funcionalidades/F-014-consultar-disponibilidad-stock.md) | S02/H4 |
| F-015 | [Visualizar productos relacionados](funcionalidades/F-015-productos-relacionados.md) | S02/H4 |
| F-016 | [Agregar ítem al carrito](funcionalidades/F-016-agregar-item-carrito.md) | S02/H4 |
| F-017 | [Cambiar la cantidad de un ítem](funcionalidades/F-017-cambiar-cantidad-item-carrito.md) | S02/H4 |
| F-018 | [Quitar un ítem del carrito](funcionalidades/F-018-quitar-item-carrito.md) | S02/H4 |
| F-019 | [Visualizar el carrito, totales y estado vacío](funcionalidades/F-019-visualizar-carrito.md) | S02/H4 |
| F-020 | [Fusionar carrito anónimo al iniciar sesión](funcionalidades/F-020-fusionar-carrito-anonimo.md) | S02/H4 |
| F-021 | [Mover un ítem del carrito a favoritos](funcionalidades/F-021-mover-carrito-favoritos.md) | S02/H4 |
| F-022 | [Capturar o seleccionar dirección de envío](funcionalidades/F-022-seleccionar-direccion-envio.md) | S03 integral; implementación H4 |
| F-023 | [Calcular y mostrar resumen de compra y envío](funcionalidades/F-023-calcular-resumen-envio.md) | S03 integral; implementación H4 |
| F-024 | [Validar y aplicar cupón o promoción](funcionalidades/F-024-validar-aplicar-cupon-promocion.md) | S03 integral; implementación H4 |
| F-025 | [Simular pago y revalidar stock](funcionalidades/F-025-simular-pago-revalidar-stock.md) | S03 integral; implementación H4 |
| F-026 | [Crear la orden en Ventas y Postventa](funcionalidades/F-026-crear-orden-ventas.md) | S03 integral; implementación H4 |
| F-027 | [Mostrar la confirmación de la orden](funcionalidades/F-027-confirmacion-orden.md) | S03 integral; implementación H4 |
| F-028 | [Consultar historial de pedidos](funcionalidades/F-028-historial-pedidos.md) | S03 integral; implementación H4 |
| F-029 | [Filtrar el historial de pedidos](funcionalidades/F-029-filtrar-historial-pedidos.md) | S05 integral; implementación H4 |
| F-030 | [Visualizar detalle de pedido](funcionalidades/F-030-detalle-pedido.md) | S03 integral; implementación H4 |
| F-031 | [Reordenar una compra anterior](funcionalidades/F-031-reordenar-compra.md) | S05 integral; implementación H4 |
| F-032 | [Consultar seguimiento de despacho](funcionalidades/F-032-seguimiento-despacho.md) | S04 integral; implementación H4 |
| F-033 | [Generar plantilla de correo](funcionalidades/F-033-generar-plantilla-correo.md) | S03 integral; implementación H4 |
| F-034 | [Enviar confirmación asíncrona](funcionalidades/F-034-enviar-confirmacion-asincrona.md) | S03 integral; implementación H4 |
| F-035 | [Enviar actualización de despacho por correo](funcionalidades/F-035-enviar-actualizacion-despacho.md) | S04 integral; implementación H4 |
| F-036 | [Agregar producto a favoritos](funcionalidades/F-036-agregar-favorito.md) | S02/H4 |
| F-037 | [Visualizar favoritos](funcionalidades/F-037-visualizar-favoritos.md) | S02/H4 |
| F-038 | [Quitar favorito](funcionalidades/F-038-quitar-favorito.md) | S02/H4 |
| F-039 | [Mover favorito al carrito](funcionalidades/F-039-mover-favorito-carrito.md) | S02/H4 |
| F-040 | [Registrar evaluación postentrega](funcionalidades/F-040-evaluacion-postentrega.md) | S05 integral; implementación H4 |

Este catálogo reparte por **fecha y entregable**. La [matriz humana S1–S5](../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md) y los [paquetes individuales](repartición%20por%20integrantes/README.md) conservan responsables asignados por el PO; contratos/entornos y evidencia se verifican durante ejecución. Los paquetes Figma no determinan quién programa. [El plan maestro](PLAN-IMPLEMENTACION.md) gobierna los requisitos de cada hito.
