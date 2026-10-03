# Plan de implementación — F-038 Quitar favorito

## 1. Metadatos y entradas

| Campo | Valor |
|---|---|
| ID / versión / estado | F-038 / 0.1.0 / En revisión |
| Objetivo académico | Sprint 3, semanas 10–11 |
| Entrada SDD | [Funcional](../../SPECS/funcional/F-038-quitar-favorito.md), [UI](../../SPECS/ui/F-038-quitar-favorito.md), [API](../../SPECS/contrato-api/F-038-quitar-favorito.md), [React](../../SPECS/componentes-react/F-038-quitar-favorito.md) |
| Ejecución y revisores | [Tareas de F-038](../seguimiento/F-038-quitar-favorito.md), propuesta según roles actuales |
| Plan general / seguridad | [Semanas 6–15](../PLAN-IMPLEMENTACION.md), [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md) |

## 2. Objetivo y límites

Entregar quitar favorito conforme comportamiento/UI/API/React, no una pantalla aislada.
Esperar DELETE antes de POST deshacer para evitar carrera. Sin contrato de estrategia validado no ofrecer Deshacer como garantizado; rollback de rechazo no equivale a undo confirmado.

## 3. Decisiones técnicas

| Área | Trabajo / decisión |
|---|---|
| Frontend / render | `RemoveWishlistAction`, `WishlistUndoFeedback`; hook `useRemoveWishlistItem`; arquitectura transversal React. |
| Backend / adaptador | DELETE favorito idempotente del titular; restauración con F-036 sin recuperar timestamps ni aceptar otro customerId. |
| Persistencia | WishlistItem. Siempre modelo lógico vigente, nunca el esquema histórico de dos tablas. |
| Remoto / caché | Invalidar wishlist al DELETE204; rollback aislado conserva cambios concurrentes. |
| Seguridad específica | DELETE ajeno / ID inválido y CSRF; Undo no burla elegibilidad. |
| UI Kit | DS-001 v0.2.0; G-STACK pendiente, no fijar versiones no verificadas. |

## 4. Dependencias y Definition of Ready

- Dependencias de comportamiento/flujo: [F-037](F-037-visualizar-favoritos.md).
- Gates: I-01, G-UNDO; consultar [registro](../DECISIONES-Y-BLOQUEOS.md). G-STACK/G-SHELL para interfaz compartida aplicable.
- Pendientes específicos: O-006-OPEN-02/03 y F-036 (I-01 para restauración).
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
Las tareas y el estado real viven únicamente en [seguimiento](../seguimiento/F-038-quitar-favorito.md); aquí no se duplica un tablero.

## 6. Criterios de terminado y pruebas

- delete repetido sin error.
- fallo restaura foco.
- undo espera DELETE.
- producto inactivo no restaurado falsamente.
- Cada estado documentado tiene caso verificable y foco/recuperación correctos.
- Seguridad: DELETE ajeno / ID inválido y CSRF; Undo no burla elegibilidad.
- DB si aplica: identidad/constraints/versiones/transacción y rollback probados sin persistencia prohibida.
- Evidencias sanitizadas y revisión por persona distinta, según [DoD general](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-y-definition-of-done).
- Cuando se exige homologación, prueba real aprobada además de fixture. Si bloqueada, funcionalidad no se declara completa.

## 7. Riesgos y recuperación

READY → REMOVING → REMOVED | ROLLBACK;UNDO → SAVING → RESTORED | NOT_AVAILABLE | ERROR.

No reintentos ilimitados ni datos locales como fuente externa de verdad. Campos, endpoints y política que sigan abiertos permanecen explícitos; resolver/actualizar spec de origen antes de modificar código. Riesgo de capacidad/fecha se revisa cada sprint sin retirar esta funcionalidad ocultamente.

