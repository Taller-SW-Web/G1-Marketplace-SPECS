# Plan de implementación — F-032 Consultar seguimiento de despacho

## 1. Metadatos y entradas

| Campo | Valor |
|---|---|
| ID / versión / estado | F-032 / 0.1.0 / En revisión |
| Objetivo académico | Sprint 5, semanas 14–15 |
| Entrada SDD | [Funcional](../../SPECS/funcional/F-032-seguimiento-despacho.md), [UI](../../SPECS/ui/F-032-seguimiento-despacho.md), [API](../../SPECS/contrato-api/F-032-seguimiento-despacho.md), [React](../../SPECS/componentes-react/F-032-seguimiento-despacho.md) |
| Ejecución y revisores | [Tareas de F-032](../seguimiento/F-032-seguimiento-despacho.md), propuesta según roles actuales |
| Plan general / seguridad | [Semanas 6–15](../PLAN-IMPLEMENTACION.md), [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md) |

## 2. Objetivo y límites

Entregar consultar seguimiento de despacho conforme comportamiento/UI/API/React, no una pantalla aislada.
BFF valida propiedad con Ventas antes Despacho.No hay un estado HTTP 203 definido; usar 202. Entregado puede habilitar F-040 sólo con eligibility comprobada, sin persistir tracking completo.

## 3. Decisiones técnicas

| Área | Trabajo / decisión |
|---|---|
| Frontend / render | `ShipmentTrackingContainer`, `ShipmentTimeline`; hook `useShipmentTracking`; arquitectura transversal React. |
| Backend / adaptador | Autorizar pedido en Ventas y leer Despacho con seguimientos:leer;202 sin tracking distinto de 503, sin PII/coordenadas. |
| Persistencia | Sin persistencia de dominio local. Siempre modelo lógico vigente, nunca el esquema histórico de dos tablas. |
| Remoto / caché | ['orders','tracking',sessionScope,orderId]; no polling continuo hasta confirmar intervalo. |
| Seguridad específica | Propiedad antes Despacho, token técnico fuera bundle, respuesta sin repartidor/coordenadas. |
| UI Kit | DS-001 v0.2.0; G-STACK pendiente, no fijar versiones no verificadas. |

## 4. Dependencias y Definition of Ready

- Dependencias de comportamiento/flujo: [F-030](F-030-detalle-pedido.md).
- Gates: I-03, I-06; consultar [registro](../DECISIONES-Y-BLOQUEOS.md). G-STACK/G-SHELL para interfaz compartida aplicable.
- Pendientes específicos: I-03/I-06 y mapeo estados/hitos/intervalo.
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
Las tareas y el estado real viven únicamente en [seguimiento](../seguimiento/F-032-seguimiento-despacho.md); aquí no se duplica un tablero.

## 6. Criterios de terminado y pruebas

- 202 distinto de503.
- ajeno no tracking.
- sin scope técnico no fallback token usuario.
- no mapa/PII.
- refresh único en vuelo.
- Cada estado documentado tiene caso verificable y foco/recuperación correctos.
- Seguridad: Propiedad antes Despacho, token técnico fuera bundle, respuesta sin repartidor/coordenadas.
- DB si aplica: identidad/constraints/versiones/transacción y rollback probados sin persistencia prohibida.
- Evidencias sanitizadas y revisión por persona distinta, según [DoD general](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-y-definition-of-done).
- Cuando se exige homologación, prueba real aprobada además de fixture. Si bloqueada, funcionalidad no se declara completa.

## 7. Riesgos y recuperación

LOADING → AVAILABLE | INCIDENT | DELIVERED | NOT_READY | NOT_AVAILABLE | ERROR;202 NOT_READY es informativo.

No reintentos ilimitados ni datos locales como fuente externa de verdad. Campos, endpoints y política que sigan abiertos permanecen explícitos; resolver/actualizar spec de origen antes de modificar código. Riesgo de capacidad/fecha se revisa cada sprint sin retirar esta funcionalidad ocultamente.

