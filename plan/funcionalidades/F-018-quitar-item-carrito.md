# Plan de implementación — F-018 Quitar un ítem del carrito

## 1. Metadatos y entradas

| Campo | Valor |
|---|---|
| ID / versión / estado | F-018 / 0.1.0 / En revisión |
| Objetivo académico | Sprint 3, semanas 10–11 |
| Entrada SDD | [Funcional](../../SPECS/funcional/F-018-quitar-item-carrito.md), [UI](../../SPECS/ui/F-018-quitar-item-carrito.md), [API](../../SPECS/contrato-api/F-018-quitar-item-carrito.md), [React](../../SPECS/componentes-react/F-018-quitar-item-carrito.md) |
| Ejecución y revisores | [Tareas de F-018](../seguimiento/F-018-quitar-item-carrito.md), propuesta según roles actuales |
| Plan general / seguridad | [Semanas 6–15](../PLAN-IMPLEMENTACION.md), [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md) |

## 2. Objetivo y límites

Entregar quitar un ítem del carrito conforme comportamiento/UI/API/React, no una pantalla aislada.
Rollback si rechazo; si timeout, releer cart antes de declarar. 5s O-006 con pausa accesible; el contrato F-016 suma y no restaura cantidad absoluta concurrente: implementación de Deshacer bloqueada hasta resolver O-006-OPEN-01.

## 3. Decisiones técnicas

| Área | Trabajo / decisión |
|---|---|
| Frontend / render | `RemoveCartItemAction`, `UndoRemovalFeedback`; hook `useRemoveCartItem`; arquitectura transversal React. |
| Backend / adaptador | DELETE local idempotente por SKU/titular con versión, sin consultar stock; especificar restauración segura aparte. |
| Persistencia | CartItem/Cart.version. Siempre modelo lógico vigente, nunca el esquema histórico de dos tablas. |
| Remoto / caché | DELETE invalida cart/quote; X-Cart-Version o GET reconcilia versión. Sin GET externo stock para eliminar. |
| Seguridad específica | DELETEde carrito ajeno/no activo, CSRF y rollback y concurrencia. |
| UI Kit | DS-001 v0.2.0; G-STACK pendiente, no fijar versiones no verificadas. |

## 4. Dependencias y Definition of Ready

- Dependencias de comportamiento/flujo: [F-019](F-019-visualizar-carrito.md).
- Gates: I-01, G-UNDO; consultar [registro](../DECISIONES-Y-BLOQUEOS.md). G-STACK/G-SHELL para interfaz compartida aplicable.
- Pendientes específicos: O-006-OPEN-01; disponibilidad para deshacer no está autorizada por DELETE.
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
Las tareas y el estado real viven únicamente en [seguimiento](../seguimiento/F-018-quitar-item-carrito.md); aquí no se duplica un tablero.

## 6. Criterios de terminado y pruebas

- última línea estado vacío.
- DELETE repetido estable.
- rollback mantiene foco.
- sin restauración aprobada feedback no ofrece éxito falso.
- Cada estado documentado tiene caso verificable y foco/recuperación correctos.
- Seguridad: DELETEde carrito ajeno/no activo, CSRF y rollback y concurrencia.
- DB si aplica: identidad/constraints/versiones/transacción y rollback probados sin persistencia prohibida.
- Evidencias sanitizadas y revisión por persona distinta, según [DoD general](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-y-definition-of-done).
- Cuando se exige homologación, prueba real aprobada además de fixture. Si bloqueada, funcionalidad no se declara completa.

## 7. Riesgos y recuperación

READY → REMOVING → REMOVED | ROLLED_BACK; UNDO_PENDING → RESTORED | RESTORE_ADJUSTED | RESTORE_ERROR sólo si restauración aprobada.

No reintentos ilimitados ni datos locales como fuente externa de verdad. Campos, endpoints y política que sigan abiertos permanecen explícitos; resolver/actualizar spec de origen antes de modificar código. Riesgo de capacidad/fecha se revisa cada sprint sin retirar esta funcionalidad ocultamente.

