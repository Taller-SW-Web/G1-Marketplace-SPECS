# Plan de implementación — F-005 Restablecer contraseña

## 1. Metadatos y entradas

| Campo | Valor |
|---|---|
| ID / versión / estado | F-005 / 0.1.0 / En revisión |
| Objetivo académico | Sprint 1, semanas 6–7 |
| Entrada SDD | [Funcional](../../SPECS/funcional/F-005-restablecer-password.md), [UI](../../SPECS/ui/F-005-restablecer-password.md), [API](../../SPECS/contrato-api/F-005-restablecer-password.md), [React](../../SPECS/componentes-react/F-005-restablecer-password.md) |
| Ejecución y revisores | [Tareas de F-005](../seguimiento/F-005-restablecer-password.md), propuesta según roles actuales |
| Plan general / seguridad | [Semanas 6–15](../PLAN-IMPLEMENTACION.md), [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md) |

## 2. Objetivo y límites

Entregar restablecer contraseña conforme comportamiento/UI/API/React, no una pantalla aislada.
Token sólo enviado a Seguridad por la capa de transporte aprobada. No confundir con token de verificación F-001. 204 borra secretos y ofrece /login, sin sesión automática.

## 3. Decisiones técnicas

| Área | Trabajo / decisión |
|---|---|
| Frontend / render | `ResetPasswordForm`, `ResetLinkOutcome`; hook `usePasswordReset`; arquitectura transversal React. |
| Backend / adaptador | Delegar reset con token efímero, política y errores401/410/422; no sesión automática. |
| Persistencia | Sin persistencia de dominio local. Siempre modelo lógico vigente, nunca el esquema histórico de dos tablas. |
| Remoto / caché | Sin query inventada de validación de token. Sólo POST definido; estado inicial comprueba presencia/forma local. |
| Seguridad específica | Token reset usado/vencido, contraseña no filtrada, referrer/analítica y no sesión automática. |
| UI Kit | DS-001 v0.2.0; G-STACK pendiente, no fijar versiones no verificadas. |

## 4. Dependencias y Definition of Ready

- Dependencias de comportamiento/flujo: [F-004](F-004-solicitar-recuperacion-password.md).
- Gates: G-AUTH; consultar [registro](../DECISIONES-Y-BLOQUEOS.md). G-STACK/G-SHELL para interfaz compartida aplicable.
- Pendientes específicos: V-004-OPEN-02: validación previa no tiene endpoint; usar validación al enviar hasta homologarlo.
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
Las tareas y el estado real viven únicamente en [seguimiento](../seguimiento/F-005-restablecer-password.md); aquí no se duplica un tablero.

## 6. Criterios de terminado y pruebas

- sin token no llama API.
- 401 y 410 ofrecen nuevo enlace.
- 422 no muestra token.
- 204 no crea sesión.
- Cada estado documentado tiene caso verificable y foco/recuperación correctos.
- Seguridad: Token reset usado/vencido, contraseña no filtrada, referrer/analítica y no sesión automática.
- DB si aplica: identidad/constraints/versiones/transacción y rollback probados sin persistencia prohibida.
- Evidencias sanitizadas y revisión por persona distinta, según [DoD general](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-y-definition-of-done).
- Cuando se exige homologación, prueba real aprobada además de fixture. Si bloqueada, funcionalidad no se declara completa.

## 7. Riesgos y recuperación

CHECKING_INPUT → EDITING → SAVING → SUCCESS | INVALID | EXPIRED | POLICY_ERROR | ERROR; comprobación inicial no certifica vigencia externa.

No reintentos ilimitados ni datos locales como fuente externa de verdad. Campos, endpoints y política que sigan abiertos permanecen explícitos; resolver/actualizar spec de origen antes de modificar código. Riesgo de capacidad/fecha se revisa cada sprint sin retirar esta funcionalidad ocultamente.

