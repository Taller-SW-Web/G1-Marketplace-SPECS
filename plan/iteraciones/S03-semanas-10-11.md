# Sprint 3 — Carrito, fusión y favoritos

Versión 0.1.0 · En revisión · Semanas10–11, sin fechas calendario. Coordinación Diego; priorización Jim. No ejecutado por esta documentación.

## Objetivo e incremento

Completar cantidades/eliminación/merge/conversión y favoritos propios, con reconciliación por versión y continuar sin combinar.

**Demo al cierre:** Invitado agrega, inicia sesión, merge completo/parcial/error; continuar sólo muestra cuenta, retry seguro; mover entre listas, producto retirado, variante requerida y vacío.

## Alcance trazable

| ID | Plan | Tareas |
|---|---|---|
| F-017 · Cambiar la cantidad de un ítem | [Plan](../funcionalidades/F-017-cambiar-cantidad-item-carrito.md) | [Seguimiento](../seguimiento/F-017-cambiar-cantidad-item-carrito.md) |
| F-018 · Quitar un ítem del carrito | [Plan](../funcionalidades/F-018-quitar-item-carrito.md) | [Seguimiento](../seguimiento/F-018-quitar-item-carrito.md) |
| F-019 · Visualizar el carrito, totales y estado vacío | [Plan](../funcionalidades/F-019-visualizar-carrito.md) | [Seguimiento](../seguimiento/F-019-visualizar-carrito.md) |
| F-020 · Fusionar carrito anónimo al iniciar sesión | [Plan](../funcionalidades/F-020-fusionar-carrito-anonimo.md) | [Seguimiento](../seguimiento/F-020-fusionar-carrito-anonimo.md) |
| F-021 · Mover un ítem del carrito a favoritos | [Plan](../funcionalidades/F-021-mover-carrito-favoritos.md) | [Seguimiento](../seguimiento/F-021-mover-carrito-favoritos.md) |
| F-036 · Agregar producto a favoritos | [Plan](../funcionalidades/F-036-agregar-favorito.md) | [Seguimiento](../seguimiento/F-036-agregar-favorito.md) |
| F-037 · Visualizar favoritos | [Plan](../funcionalidades/F-037-visualizar-favoritos.md) | [Seguimiento](../seguimiento/F-037-visualizar-favoritos.md) |
| F-038 · Quitar favorito | [Plan](../funcionalidades/F-038-quitar-favorito.md) | [Seguimiento](../seguimiento/F-038-quitar-favorito.md) |
| F-039 · Mover favorito al carrito | [Plan](../funcionalidades/F-039-mover-favorito-carrito.md) | [Seguimiento](../seguimiento/F-039-mover-favorito-carrito.md) |

Son 9 funcionalidades y 63 tareas por área; además tareas comunes. Cada plan enlaza cuatro specs. No nuevas épicas ni historias de usuario.

## Entrada y bloqueos

I-01, G-UNDO, F-002/F-016 funcionales; preparar I-02–I-06/G-MAIL/G-PROMPT antes checkout/pedidos.

Leer [decisiones](../DECISIONES-Y-BLOQUEOS.md) y confirmar Ready/capacidad. Gates externos abiertos bloquean integración real, no componentes puros o preparación de fixtures. Fuente local vigente, no APIs asumidas por mensajes no registrados.

## Trabajo por semana

- **Semana10:** cerrar preparación/decisiones y priorizar corte vertical; FE estados con fixtures, BE DTO/adaptador y DB según ownership; escribir tests funcionales/seguridad antes o junto al código.
- **Semana11:** conectar partes y contrato real sólo aprobado; E2E/negativos/correcciones, responsive/a11y, escaneos y revisión independiente. No dejar toda seguridad para release.
- Validar transacciones/constraints Prisma/DB; preparar fixtures del worker/eventos/CSAT y casos negativos para no concentrar preparación en S5.

Frontend: Sebastian referentes propuestos; backend Leonidas; DB Leonidas+Andres; QA Fernando; DevSecOps Andres; documentación Sebastian; coordinación Diego; alcance/riesgo Jim. Propuesta por rol, no altera responsables de mockups.

## Pruebas y DevSecOps obligatorios

IDOR carrito/favoritos y cookie ajena, CSRF según transporte, carrera If-Match/merge, rollback y limpieza de caché entre dos cuentas. Scans y DAST autenticado sólo autorizado.

Además pruebas por tarea QA-001 y QA-002 de cada funcionalidad, y regresión acumulativa. Tool/version/entorno y resultados en evidencia. No scans de terceros sin autorización.

## Tareas comunes del sprint

- [TASK-TRANS-S03-OPS-001](../seguimiento/TRANSVERSALES.md#task-trans-s03-ops-001) — Andres; revisor Leonidas; semana10.
- [TASK-TRANS-S03-OPS-002](../seguimiento/TRANSVERSALES.md#task-trans-s03-ops-002) — Andres; revisor Fernando; semana11.
- [TASK-TRANS-S03-QA-001](../seguimiento/TRANSVERSALES.md#task-trans-s03-qa-001) — Fernando; revisor Diego; semana11.
- [TASK-TRANS-S03-DOC-001](../seguimiento/TRANSVERSALES.md#task-trans-s03-doc-001) — Sebastian; revisor Jim; semana11.
- [TASK-TRANS-S03-DOC-002](../seguimiento/TRANSVERSALES.md#task-trans-s03-doc-002) — Diego; revisor Jim; semana10.

## Cierre y Definition of Done

Carrito/favoritos y ambas salidas de merge probadas; Deshacer sólo completo si restauración segura contratada. No duplicar carrito ni guardar favoritado por SKU.

- Cumplir [DoD global](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-y-definition-of-done).
- Demo y evidencia real, no sólo mockups; distinguir contract fixture/sandbox/real.
- Tablero mantiene tareas no acabadas con motivo/gate/objetivo; no declarar sprint completo por un camino feliz.
- Revisar capacidad del siguiente corte y riesgo de semana 15, sin perder funcionalidades del alcance.

