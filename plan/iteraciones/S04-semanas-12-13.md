# Sprint 4 — Checkout idempotente

Versión 0.1.0 · En revisión · Semanas12–13, sin fechas calendario. Coordinación Diego; priorización Jim. No ejecutado por esta documentación.

## Objetivo e incremento

Dirección del titular, quote y beneficio vigentes, pago simulado sin cobro, preparación/creación única y confirmación neutral ante incertidumbre.

**Demo al cierre:** Seleccionar/crear dirección V-010; cotizar/cupón/no cobertura/expiración; preparar; crear pedido o mostrar SUBMITTED y consultar operación original.

## Alcance trazable

| ID | Plan | Tareas |
|---|---|---|
| F-022 · Capturar o seleccionar dirección de envío | [Plan](../funcionalidades/F-022-seleccionar-direccion-envio.md) | [Seguimiento](../seguimiento/F-022-seleccionar-direccion-envio.md) |
| F-023 · Calcular y mostrar resumen de compra y envío | [Plan](../funcionalidades/F-023-calcular-resumen-envio.md) | [Seguimiento](../seguimiento/F-023-calcular-resumen-envio.md) |
| F-024 · Validar y aplicar cupón o promoción | [Plan](../funcionalidades/F-024-validar-aplicar-cupon-promocion.md) | [Seguimiento](../seguimiento/F-024-validar-aplicar-cupon-promocion.md) |
| F-025 · Simular pago y revalidar stock | [Plan](../funcionalidades/F-025-simular-pago-revalidar-stock.md) | [Seguimiento](../seguimiento/F-025-simular-pago-revalidar-stock.md) |
| F-026 · Crear la orden en Ventas y Postventa | [Plan](../funcionalidades/F-026-crear-orden-ventas.md) | [Seguimiento](../seguimiento/F-026-crear-orden-ventas.md) |
| F-027 · Mostrar la confirmación de la orden | [Plan](../funcionalidades/F-027-confirmacion-orden.md) | [Seguimiento](../seguimiento/F-027-confirmacion-orden.md) |

Son 6 funcionalidades y 39 tareas por área; además tareas comunes. Cada plan enlaza cuatro specs. No nuevas épicas ni historias de usuario.

## Entrada y bloqueos

I-01/I-02/I-06, G-ADDRESS/G-BENEFIT/G-CHECKOUT/G-CONFIRM; no real checkout hacia Ventas sin evidencia.

Leer [decisiones](../DECISIONES-Y-BLOQUEOS.md) y confirmar Ready/capacidad. Gates externos abiertos bloquean integración real, no componentes puros o preparación de fixtures. Fuente local vigente, no APIs asumidas por mensajes no registrados.

## Trabajo por semana

- **Semana12:** cerrar preparación/decisiones y priorizar corte vertical; FE estados con fixtures, BE DTO/adaptador y DB según ownership; escribir tests funcionales/seguridad antes o junto al código.
- **Semana13:** conectar partes y contrato real sólo aprobado; E2E/negativos/correcciones, responsive/a11y, escaneos y revisión independiente. No dejar toda seguridad para release.
- CheckoutOperation y recuperación, probar timeout con respuesta tardía; preparar NotificationDelivery/outbox con contrato aunque correo final se completa S5.

Frontend: Sebastian referentes propuestos; backend Leonidas; DB Leonidas+Andres; QA Fernando; DevSecOps Andres; documentación Sebastian; coordinación Diego; alcance/riesgo Jim. Propuesta por rol, no altera responsables de mockups.

## Pruebas y DevSecOps obligatorios

Token titular vs técnico, IDOR de dirección/quote/operación, alteración montos, cupón sin consumo, fingerprints/idempotencia/replay y no PII/tarjetas. Scans/DAST autorizado y concurrencia controlada.

Además pruebas por tarea QA-001 y QA-002 de cada funcionalidad, y regresión acumulativa. Tool/version/entorno y resultados en evidencia. No scans de terceros sin autorización.

## Tareas comunes del sprint

- [TASK-TRANS-S04-OPS-001](../seguimiento/TRANSVERSALES.md#task-trans-s04-ops-001) — Andres; revisor Leonidas; semana12.
- [TASK-TRANS-S04-OPS-002](../seguimiento/TRANSVERSALES.md#task-trans-s04-ops-002) — Andres; revisor Fernando; semana13.
- [TASK-TRANS-S04-QA-001](../seguimiento/TRANSVERSALES.md#task-trans-s04-qa-001) — Fernando; revisor Diego; semana13.
- [TASK-TRANS-S04-DOC-001](../seguimiento/TRANSVERSALES.md#task-trans-s04-doc-001) — Sebastian; revisor Jim; semana13.
- [TASK-TRANS-S04-DOC-002](../seguimiento/TRANSVERSALES.md#task-trans-s04-doc-002) — Diego; revisor Jim; semana12.

## Cierre y Definition of Done

Un pedido bajo doble click/retry y estado incierto recuperable; deep link/mapping definidos, ningún PREPARED se presenta como pedido. Email envío todavía asíncrono, no afirmación SENT.

- Cumplir [DoD global](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-y-definition-of-done).
- Demo y evidencia real, no sólo mockups; distinguir contract fixture/sandbox/real.
- Tablero mantiene tareas no acabadas con motivo/gate/objetivo; no declarar sprint completo por un camino feliz.
- Revisar capacidad del siguiente corte y riesgo de semana 15, sin perder funcionalidades del alcance.

