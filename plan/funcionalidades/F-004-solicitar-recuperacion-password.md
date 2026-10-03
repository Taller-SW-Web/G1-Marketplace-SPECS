# Plan de implementación — F-004 Solicitar recuperación de contraseña

## 1. Metadatos y entradas

| Campo | Valor |
|---|---|
| ID / versión / estado | F-004 / 0.1.0 / En revisión |
| Objetivo académico | Sprint 1, semanas 6–7 |
| Entrada SDD | [Funcional](../../SPECS/funcional/F-004-solicitar-recuperacion-password.md), [UI](../../SPECS/ui/F-004-solicitar-recuperacion-password.md), [API](../../SPECS/contrato-api/F-004-solicitar-recuperacion-password.md), [React](../../SPECS/componentes-react/F-004-solicitar-recuperacion-password.md) |
| Ejecución y revisores | [Tareas de F-004](../seguimiento/F-004-solicitar-recuperacion-password.md), propuesta según roles actuales |
| Plan general / seguridad | [Semanas 6–15](../PLAN-IMPLEMENTACION.md), [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md) |

## 2. Objetivo y límites

Entregar solicitar recuperación de contraseña conforme comportamiento/UI/API/React, no una pantalla aislada.
202 muestra el mismo copy y composición exista o no cuenta. No invocar email/provider ni crear token desde frontend.

## 3. Decisiones técnicas

| Área | Trabajo / decisión |
|---|---|
| Frontend / render | `RecoveryForm`, `RecoveryAcknowledgement`; hook `usePasswordRecovery`; arquitectura transversal React. |
| Backend / adaptador | Delegar recuperación con202 uniforme y rate limiting publicado, sin existencia de cuenta ni tokens locales. |
| Persistencia | Sin persistencia de dominio local. Siempre modelo lógico vigente, nunca el esquema histórico de dos tablas. |
| Remoto / caché | Mutation sin cachear correo ni resultado por usuario. |
| Seguridad específica | Respuesta/latencia antienumeración y rate limit; no email/token en logs. |
| UI Kit | DS-001 v0.2.0; G-STACK pendiente, no fijar versiones no verificadas. |

## 4. Dependencias y Definition of Ready

- Dependencias de comportamiento/flujo: base técnica y contratos aplicables; no otra funcionalidad obligatoria.
- Gates: G-AUTH; consultar [registro](../DECISIONES-Y-BLOQUEOS.md). G-STACK/G-SHELL para interfaz compartida aplicable.
- Pendientes específicos: Tiempo/copy de límite con Seguridad.
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
Las tareas y el estado real viven únicamente en [seguimiento](../seguimiento/F-004-solicitar-recuperacion-password.md); aquí no se duplica un tablero.

## 6. Criterios de terminado y pruebas

- 202 idéntico con ambos fixtures de existencia.
- formato inválido no llama API.
- 429 no enumera.
- Enter no duplica envío.
- Cada estado documentado tiene caso verificable y foco/recuperación correctos.
- Seguridad: Respuesta/latencia antienumeración y rate limit; no email/token en logs.
- DB si aplica: identidad/constraints/versiones/transacción y rollback probados sin persistencia prohibida.
- Evidencias sanitizadas y revisión por persona distinta, según [DoD general](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-y-definition-of-done).
- Cuando se exige homologación, prueba real aprobada además de fixture. Si bloqueada, funcionalidad no se declara completa.

## 7. Riesgos y recuperación

EDITING → REQUESTING → ACCEPTED | RATE_LIMITED | ERROR; 429 conserva correo y permite reintento después de espera aprobada.

No reintentos ilimitados ni datos locales como fuente externa de verdad. Campos, endpoints y política que sigan abiertos permanecen explícitos; resolver/actualizar spec de origen antes de modificar código. Riesgo de capacidad/fecha se revisa cada sprint sin retirar esta funcionalidad ocultamente.

