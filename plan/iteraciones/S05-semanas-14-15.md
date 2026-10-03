# Sprint 5 — Postcompra y entrega validada

Versión 0.1.0 · En revisión · Semanas14–15, sin fechas calendario. Coordinación Diego; priorización Jim. No ejecutado por esta documentación.

## Objetivo e incremento

Historial propio/filtros/detalle/recompra/tracking, renderer/worker correos, CSAT después entrega y estabilización final.

**Demo al cierre:** Pedido propio/histórico → tracking/202; recomprar sin precio histórico; confirmación email y evento homologado sin duplicados; GOOD/REGULAR/BAD en ENTREGADO, duplicado controlado.

## Alcance trazable

| ID | Plan | Tareas |
|---|---|---|
| F-028 · Consultar historial de pedidos | [Plan](../funcionalidades/F-028-historial-pedidos.md) | [Seguimiento](../seguimiento/F-028-historial-pedidos.md) |
| F-029 · Filtrar el historial de pedidos | [Plan](../funcionalidades/F-029-filtrar-historial-pedidos.md) | [Seguimiento](../seguimiento/F-029-filtrar-historial-pedidos.md) |
| F-030 · Visualizar detalle de pedido | [Plan](../funcionalidades/F-030-detalle-pedido.md) | [Seguimiento](../seguimiento/F-030-detalle-pedido.md) |
| F-031 · Reordenar una compra anterior | [Plan](../funcionalidades/F-031-reordenar-compra.md) | [Seguimiento](../seguimiento/F-031-reordenar-compra.md) |
| F-032 · Consultar seguimiento de despacho | [Plan](../funcionalidades/F-032-seguimiento-despacho.md) | [Seguimiento](../seguimiento/F-032-seguimiento-despacho.md) |
| F-033 · Generar plantilla de correo | [Plan](../funcionalidades/F-033-generar-plantilla-correo.md) | [Seguimiento](../seguimiento/F-033-generar-plantilla-correo.md) |
| F-034 · Enviar confirmación asíncrona | [Plan](../funcionalidades/F-034-enviar-confirmacion-asincrona.md) | [Seguimiento](../seguimiento/F-034-enviar-confirmacion-asincrona.md) |
| F-035 · Enviar actualización de despacho por correo | [Plan](../funcionalidades/F-035-enviar-actualizacion-despacho.md) | [Seguimiento](../seguimiento/F-035-enviar-actualizacion-despacho.md) |
| F-040 · Registrar evaluación postentrega | [Plan](../funcionalidades/F-040-evaluacion-postentrega.md) | [Seguimiento](../seguimiento/F-040-evaluacion-postentrega.md) |

Son 9 funcionalidades y 57 tareas por área; además tareas comunes. Cada plan enlaza cuatro specs. No nuevas épicas ni historias de usuario.

## Entrada y bloqueos

I-01/I-02/I-03/I-04/I-05/I-06 aplicables, G-REORDER/G-PROMPT/G-MAIL, todos gates de release pertinentes cerrados.

Leer [decisiones](../DECISIONES-Y-BLOQUEOS.md) y confirmar Ready/capacidad. Gates externos abiertos bloquean integración real, no componentes puros o preparación de fixtures. Fuente local vigente, no APIs asumidas por mensajes no registrados.

## Trabajo por semana

- **Semana14:** cerrar preparación/decisiones y priorizar corte vertical; FE estados con fixtures, BE DTO/adaptador y DB según ownership; escribir tests funcionales/seguridad antes o junto al código.
- **Semana15:** conectar partes y contrato real sólo aprobado; E2E/negativos/correcciones, responsive/a11y, escaneos y revisión independiente. No dejar toda seguridad para release.
- Semana14 completar/enganchar funciones sobre fixtures preparados; semana 15 cerrar regresión, responsive/a11y, contrato real, reproducibilidad/migraciones/backup/runbook y evidencias.

Frontend: Sebastian / Giuliano referentes propuestos; backend Leonidas; DB Leonidas+Andres; QA Fernando; DevSecOps Andres; documentación Sebastian; coordinación Diego; alcance/riesgo Jim. Propuesta por rol, no altera responsables de mockups.

## Pruebas y DevSecOps obligatorios

IDOR pedidos/tracking/CSAT, replay webhook, remitente autenticado, plantilla XSS/header injection/URLs, email cifrado, no secretos/PII. Scans y DAST finales, regresión MFA/checkout y restauración backup propia.

Además pruebas por tarea QA-001 y QA-002 de cada funcionalidad, y regresión acumulativa. Tool/version/entorno y resultados en evidencia. No scans de terceros sin autorización.

## Tareas comunes del sprint

- [TASK-TRANS-S05-OPS-001](../seguimiento/TRANSVERSALES.md#task-trans-s05-ops-001) — Andres; revisor Leonidas; semana 14.
- [TASK-TRANS-S05-OPS-002](../seguimiento/TRANSVERSALES.md#task-trans-s05-ops-002) — Andres; revisor Fernando; semana 15.
- [TASK-TRANS-S05-QA-001](../seguimiento/TRANSVERSALES.md#task-trans-s05-qa-001) — Fernando; revisor Diego; semana 15.
- [TASK-TRANS-S05-DOC-001](../seguimiento/TRANSVERSALES.md#task-trans-s05-doc-001) — Sebastian; revisor Jim; semana 15.
- [TASK-TRANS-S05-DOC-002](../seguimiento/TRANSVERSALES.md#task-trans-s05-doc-002) — Diego; revisor Jim; semana 14.
- [TASK-TRANS-S05-OPS-003](../seguimiento/TRANSVERSALES.md#task-trans-s05-ops-003) — Andres; revisor Leonidas; semana 15.

## Cierre y Definition of Done

Cobertura F-001–F-040 demostrada con evidencia, no hallazgos críticos/altos explotables abiertos; lista honesta de bloqueos/desvíos si algo no cabe. Mock no se reporta como integración real.

- Cumplir [DoD global](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-y-definition-of-done).
- Demo y evidencia real, no sólo mockups; distinguir contract fixture/sandbox/real.
- Tablero mantiene tareas no acabadas con motivo/gate/objetivo; no declarar sprint completo por un camino feliz.
- Revisar capacidad del siguiente corte y riesgo de semana 15, sin perder funcionalidades del alcance.

