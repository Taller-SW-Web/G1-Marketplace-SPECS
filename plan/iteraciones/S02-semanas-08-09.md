# Sprint 2 — Descubrimiento, detalle y adición

Versión 0.1.0 · En revisión · Semanas8–9, sin fechas calendario. Coordinación Diego; priorización Jim. No ejecutado por esta documentación.

## Objetivo e incremento

Corte público desde home a catálogo/ficha/SKU/precio/stock y primer agregado al carrito; consultas independientes y errores recuperables.

**Demo al cierre:** Buscar, filtrar, ordenar, paginar, abrir galería/variante, precio/oferta y disponibilidad, agregar una unidad con resultado ajustado/error.

## Alcance trazable

| ID | Plan | Tareas |
|---|---|---|
| F-006 · Visualizar inicio, categorías y destacados | [Plan](../funcionalidades/F-006-inicio-categorias-destacados.md) | [Seguimiento](../seguimiento/F-006-inicio-categorias-destacados.md) |
| F-007 · Buscar productos por texto | [Plan](../funcionalidades/F-007-buscar-productos-texto.md) | [Seguimiento](../seguimiento/F-007-buscar-productos-texto.md) |
| F-008 · Filtrar catálogo | [Plan](../funcionalidades/F-008-filtrar-catalogo.md) | [Seguimiento](../seguimiento/F-008-filtrar-catalogo.md) |
| F-009 · Ordenar resultados | [Plan](../funcionalidades/F-009-ordenar-catalogo.md) | [Seguimiento](../seguimiento/F-009-ordenar-catalogo.md) |
| F-010 · Paginar resultados | [Plan](../funcionalidades/F-010-paginar-catalogo.md) | [Seguimiento](../seguimiento/F-010-paginar-catalogo.md) |
| F-011 · Visualizar ficha y galería del producto | [Plan](../funcionalidades/F-011-detalle-producto.md) | [Seguimiento](../seguimiento/F-011-detalle-producto.md) |
| F-012 · Visualizar precio, oferta y descuento vigente | [Plan](../funcionalidades/F-012-precio-oferta-descuento.md) | [Seguimiento](../seguimiento/F-012-precio-oferta-descuento.md) |
| F-013 · Seleccionar atributos y variante del producto | [Plan](../funcionalidades/F-013-seleccion-atributos-variante.md) | [Seguimiento](../seguimiento/F-013-seleccion-atributos-variante.md) |
| F-014 · Consultar disponibilidad de stock | [Plan](../funcionalidades/F-014-consultar-disponibilidad-stock.md) | [Seguimiento](../seguimiento/F-014-consultar-disponibilidad-stock.md) |
| F-015 · Visualizar productos relacionados | [Plan](../funcionalidades/F-015-productos-relacionados.md) | [Seguimiento](../seguimiento/F-015-productos-relacionados.md) |
| F-016 · Agregar ítem al carrito | [Plan](../funcionalidades/F-016-agregar-item-carrito.md) | [Seguimiento](../seguimiento/F-016-agregar-item-carrito.md) |

Son 11 funcionalidades y 67 tareas por área; además tareas comunes. Cada plan enlaza cuatro specs. No nuevas épicas ni historias de usuario.

## Entrada y bloqueos

I-01/H-01, G-SKU, G-ADD y decisiones de maestros/página fuera de rango; no datos ficticios como integración.

Leer [decisiones](../DECISIONES-Y-BLOQUEOS.md) y confirmar Ready/capacidad. Gates externos abiertos bloquean integración real, no componentes puros o preparación de fixtures. Fuente local vigente, no APIs asumidas por mensajes no registrados.

## Trabajo por semana

- **Semana8:** cerrar preparación/decisiones y priorizar corte vertical; FE estados con fixtures, BE DTO/adaptador y DB según ownership; escribir tests funcionales/seguridad antes o junto al código.
- **Semana9:** conectar partes y contrato real sólo aprobado; E2E/negativos/correcciones, responsive/a11y, escaneos y revisión independiente. No dejar toda seguridad para release.
- Contrato local con fixture autorizado por cada región; cache policy/ETag/timeouts y observabilidad, preparar recursos DB del carrito sin reserva inventada.

Frontend: Giuliano / Sebastian referentes propuestos; backend Leonidas; DB Leonidas+Andres; QA Fernando; DevSecOps Andres; documentación Sebastian; coordinación Diego; alcance/riesgo Jim. Propuesta por rol, no altera responsables de mockups.

## Pruebas y DevSecOps obligatorios

XSS/traversal, medios/URL/SSRF, enums/rangos/pageSize abusivos, producto privado y cantidades/precios no autoritativos. Scans y DAST sobre entorno propio.

Además pruebas por tarea QA-001 y QA-002 de cada funcionalidad, y regresión acumulativa. Tool/version/entorno y resultados en evidencia. No scans de terceros sin autorización.

## Tareas comunes del sprint

- [TASK-TRANS-S02-OPS-001](../seguimiento/TRANSVERSALES.md#task-trans-s02-ops-001) — Andres; revisor Leonidas; semana8.
- [TASK-TRANS-S02-OPS-002](../seguimiento/TRANSVERSALES.md#task-trans-s02-ops-002) — Andres; revisor Fernando; semana9.
- [TASK-TRANS-S02-QA-001](../seguimiento/TRANSVERSALES.md#task-trans-s02-qa-001) — Fernando; revisor Diego; semana9.
- [TASK-TRANS-S02-DOC-001](../seguimiento/TRANSVERSALES.md#task-trans-s02-doc-001) — Sebastian; revisor Jim; semana9.
- [TASK-TRANS-S02-DOC-002](../seguimiento/TRANSVERSALES.md#task-trans-s02-doc-002) — Diego; revisor Jim; semana8.

## Cierre y Definition of Done

Catálogo y ficha completa con todos los estados relevantes; ningún error se convierte en agotado/gratis; una pulsación de adición no duplica solicitud.

- Cumplir [DoD global](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-y-definition-of-done).
- Demo y evidencia real, no sólo mockups; distinguir contract fixture/sandbox/real.
- Tablero mantiene tareas no acabadas con motivo/gate/objetivo; no declarar sprint completo por un camino feliz.
- Revisar capacidad del siguiente corte y riesgo de semana 15, sin perder funcionalidades del alcance.

