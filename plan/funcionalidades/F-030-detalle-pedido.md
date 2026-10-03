# Plan de implementación — F-030 Visualizar detalle de pedido

## 1. Metadatos y entradas

| Campo | Valor |
|---|---|
| ID / versión / estado | F-030 / 0.1.0 / En revisión |
| Objetivo académico | Sprint 5, semanas 14–15 |
| Entrada SDD | [Funcional](../../SPECS/funcional/F-030-detalle-pedido.md), [UI](../../SPECS/ui/F-030-detalle-pedido.md), [API](../../SPECS/contrato-api/F-030-detalle-pedido.md), [React](../../SPECS/componentes-react/F-030-detalle-pedido.md) |
| Ejecución y revisores | [Tareas de F-030](../seguimiento/F-030-detalle-pedido.md), propuesta según roles actuales |
| Plan general / seguridad | [Semanas 6–15](../PLAN-IMPLEMENTACION.md), [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md) |

## 2. Objetivo y límites

Entregar visualizar detalle de pedido conforme comportamiento/UI/API/React, no una pantalla aislada.
GET detalle; F-031 y F-032 acciones propias. O-009 sólo elegibilidad ENTREGADO comprobada, nunca sólo color badge.

## 3. Decisiones técnicas

| Área | Trabajo / decisión |
|---|---|
| Frontend / render | `OrderDetailContainer`, `HistoricalOrderLines`, `OrderStateTimeline`; hook `useOrderDetail`; arquitectura transversal React. |
| Backend / adaptador | Autorizar detalle en Ventas, devolver snapshots históricos mínimos y neutralizar 403/404 sin filtrar existencia. |
| Persistencia | Sin persistencia de dominio local. Siempre modelo lógico vigente, nunca el esquema histórico de dos tablas. |
| Remoto / caché | ['orders','detail',sessionScope,orderId]; snapshots externos privados. |
| Seguridad específica | 404 neutral para pedido ajeno, documento / tarjeta / email completo excluidos. |
| UI Kit | DS-001 v0.2.0; G-STACK pendiente, no fijar versiones no verificadas. |

## 4. Dependencias y Definition of Ready

- Dependencias de comportamiento/flujo: [F-028](F-028-historial-pedidos.md).
- Gates: I-03; consultar [registro](../DECISIONES-Y-BLOQUEOS.md). G-STACK/G-SHELL para interfaz compartida aplicable.
- Pendientes específicos: I-03; lista de estados/hitos y proyección mínima.
- Responsable/revisor confirman disponibilidad, estimación y criterio; contrato/fixtures definidos; estados de UI leídos. Mockups no asignan automáticamente código.
- Si gate afecta operación real, limitar trabajo a componentes puros, fixtures y tests locales. Nunca interpretar eso como integración terminada.

## 5. Fases, entregables y validación

| Fase | Entregable | Depende de | Verificación |
|---|---|---|---|
| 1 | Contratos tipados, fixtures y casos negativos | Ready y specs | Shape de API, estados y seguridad trazables |
| 2 | Componentes/contendedor o render server-only + BFF | Base, API/React; DB si aplica | Build/lint/typecheck y pruebas de contrato local |
| 3 | Persistencia/adaptador real o integración local | Gates aplicables y transacciones | Pruebas API/DB y sandbox autorizado |
| 4 | E2E/responsive/accesibilidad y seguridad | Partes conectadas | Casos de React y QA-002, scans y DAST aplicable |
| 5 | Revisión/evidencias/entrega | Pruebas y contratos aprobados | DoD, documentación y resultado demostrable |

Puede trabajarse FE/BE con mocks en paralelo, pero las condiciones bloquean activación real hasta cierre.
Las tareas y el estado real viven únicamente en [seguimiento](../seguimiento/F-030-detalle-pedido.md); aquí no se duplica un tablero.

## 6. Criterios de terminado y pruebas

- precio histórico invariable si catálogo cambia.
- pedido ajeno neutral.
- sin tracking no CTA falso.
- timeline comprensible lector.
- Cada estado documentado tiene caso verificable y foco/recuperación correctos.
- Seguridad: 404 neutral para pedido ajeno, documento / tarjeta / email completo excluidos.
- DB si aplica: identidad/constraints/versiones/transacción y rollback probados sin persistencia prohibida.
- Evidencias sanitizadas y revisión por persona distinta, según [DoD general](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-y-definition-of-done).
- Cuando se exige homologación, prueba real aprobada además de fixture. Si bloqueada, funcionalidad no se declara completa.

## 7. Riesgos y recuperación

LOADING → READY | NOT_AVAILABLE | ERROR; no tracking omite seguir envío, no inventa despacho.

No reintentos ilimitados ni datos locales como fuente externa de verdad. Campos, endpoints y política que sigan abiertos permanecen explícitos; resolver/actualizar spec de origen antes de modificar código. Riesgo de capacidad/fecha se revisa cada sprint sin retirar esta funcionalidad ocultamente.

