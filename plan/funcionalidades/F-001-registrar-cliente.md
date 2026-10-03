# Plan de implementación — F-001 Registrar cliente

## 1. Metadatos y entradas

| Campo | Valor |
|---|---|
| ID / versión / estado | F-001 / 0.1.0 / En revisión |
| Objetivo académico | Sprint 1, semanas 6–7 |
| Entrada SDD | [Funcional](../../SPECS/funcional/F-001-registrar-cliente.md), [UI](../../SPECS/ui/F-001-registrar-cliente.md), [API](../../SPECS/contrato-api/F-001-registrar-cliente.md), [React](../../SPECS/componentes-react/F-001-registrar-cliente.md) |
| Ejecución y revisores | [Tareas de F-001](../seguimiento/F-001-registrar-cliente.md), propuesta según roles actuales |
| Plan general / seguridad | [Semanas 6–15](../PLAN-IMPLEMENTACION.md), [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md) |

## 2. Objetivo y límites

Entregar registrar cliente conforme comportamiento/UI/API/React, no una pantalla aislada.
Enviar canalOrigen=MARKETPLACE fijo, no returnUrl. 201 no autentica. El correo, su reenvío, expiración y enlace usado se resuelven exclusivamente en Seguridad; retorno configurado /login sin token.

## 3. Decisiones técnicas

| Área | Trabajo / decisión |
|---|---|
| Frontend / render | `RegistrationForm`, `RegistrationAccepted`; hook `useRegistration`; arquitectura transversal React. |
| Backend / adaptador | Adaptar registro Seguridad, fijar canalOrigen MARKETPLACE, mantener respuesta neutra y no almacenar contraseña. |
| Persistencia | Sin persistencia de dominio local. Siempre modelo lógico vigente, nunca el esquema histórico de dos tablas. |
| Remoto / caché | Sin query de perfil; mutation de registro sin caché de secretos. |
| Seguridad específica | Antienumeración409, canal/returnURL no manipulables, política servidor y secretos no log/storage. |
| UI Kit | DS-001 v0.2.0; G-STACK pendiente, no fijar versiones no verificadas. |

## 4. Dependencias y Definition of Ready

- Dependencias de comportamiento/flujo: base técnica y contratos aplicables; no otra funcionalidad obligatoria.
- Gates: G-AUTH; consultar [registro](../DECISIONES-Y-BLOQUEOS.md). G-STACK/G-SHELL para interfaz compartida aplicable.
- Pendientes específicos: Política de Seguridad, formato celular y URL base por ambiente aún por confirmar.
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
Las tareas y el estado real viven únicamente en [seguimiento](../seguimiento/F-001-registrar-cliente.md); aquí no se duplica un tablero.

## 6. Criterios de terminado y pruebas

- 201 conserva sesión no autenticada y muestra pendiente.
- 409 no revela cuenta existente.
- 422 vincula errores a política.
- payload excluye confirmación y URL de retorno.
- Cada estado documentado tiene caso verificable y foco/recuperación correctos.
- Seguridad: Antienumeración409, canal/returnURL no manipulables, política servidor y secretos no log/storage.
- DB si aplica: identidad/constraints/versiones/transacción y rollback probados sin persistencia prohibida.
- Evidencias sanitizadas y revisión por persona distinta, según [DoD general](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-y-definition-of-done).
- Cuando se exige homologación, prueba real aprobada además de fixture. Si bloqueada, funcionalidad no se declara completa.

## 7. Riesgos y recuperación

EDITING → SUBMITTING → ACCEPTED | FIELD_ERROR | NEUTRAL_CONFLICT | ERROR; 422 vuelve al formulario conservando campos no sensibles.

No reintentos ilimitados ni datos locales como fuente externa de verdad. Campos, endpoints y política que sigan abiertos permanecen explícitos; resolver/actualizar spec de origen antes de modificar código. Riesgo de capacidad/fecha se revisa cada sprint sin retirar esta funcionalidad ocultamente.

