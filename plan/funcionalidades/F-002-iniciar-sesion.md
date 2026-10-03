# Plan de implementación — F-002 Iniciar sesión

## 1. Metadatos y entradas

| Campo | Valor |
|---|---|
| ID / versión / estado | F-002 / 0.1.0 / En revisión |
| Objetivo académico | Sprint 1, semanas 6–7 |
| Entrada SDD | [Funcional](../../SPECS/funcional/F-002-iniciar-sesion.md), [UI](../../SPECS/ui/F-002-iniciar-sesion.md), [API](../../SPECS/contrato-api/F-002-iniciar-sesion.md), [React](../../SPECS/componentes-react/F-002-iniciar-sesion.md) |
| Ejecución y revisores | [Tareas de F-002](../seguimiento/F-002-iniciar-sesion.md), propuesta según roles actuales |
| Plan general / seguridad | [Semanas 6–15](../PLAN-IMPLEMENTACION.md), [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md) |

## 2. Objetivo y límites

Entregar iniciar sesión conforme comportamiento/UI/API/React, no una pantalla aislada.
No fusionar ni cargar información privada antes de completar MFA. Fusión fallida conserva sesión y ofrece Reintentar/Continuar sin combinar; retorno interno permitido, nunca URL externa. Volver desde Seguridad muestra login normal.

## 3. Decisiones técnicas

| Área | Trabajo / decisión |
|---|---|
| Frontend / render | `LoginForm`, `MfaChallengeForm`, `LoginFlowContainer`; hook `useLoginFlow`; arquitectura transversal React. |
| Backend / adaptador | Validar respuesta de login/desafío, completar MFA homologado y establecer sesión sólo al autenticarse; no fabricar sesión local. |
| Persistencia | Sin persistencia de dominio local. Siempre modelo lógico vigente, nunca el esquema histórico de dos tablas. |
| Remoto / caché | session en contexto sin secretos persistidos; al autenticarse invalidar cart y wishlist bajo nueva identidad. |
| Seguridad específica | MFA no bypass, JWT inválido/expirado, open redirects, rate limit y no tokens en almacenamiento web. |
| UI Kit | DS-001 v0.2.0; G-STACK pendiente, no fijar versiones no verificadas. |

## 4. Dependencias y Definition of Ready

- Dependencias de comportamiento/flujo: [F-001](F-001-registrar-cliente.md).
- Gates: G-AUTH; consultar [registro](../DECISIONES-Y-BLOQUEOS.md). G-STACK/G-SHELL para interfaz compartida aplicable.
- Pendientes específicos: Completar contrato MFA, transporte de sesión, PASSWORD_CADUCADA y cooldown 429.
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
Las tareas y el estado real viven únicamente en [seguimiento](../seguimiento/F-002-iniciar-sesion.md); aquí no se duplica un tablero.

## 6. Criterios de terminado y pruebas

- 401 es genérico.
- desafío no habilita rutas privadas.
- retorno externo rechazado.
- falla merge permite continuar sin sumar invitado.
- Cada estado documentado tiene caso verificable y foco/recuperación correctos.
- Seguridad: MFA no bypass, JWT inválido/expirado, open redirects, rate limit y no tokens en almacenamiento web.
- DB si aplica: identidad/constraints/versiones/transacción y rollback probados sin persistencia prohibida.
- Evidencias sanitizadas y revisión por persona distinta, según [DoD general](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-y-definition-of-done).
- Cuando se exige homologación, prueba real aprobada además de fixture. Si bloqueada, funcionalidad no se declara completa.

## 7. Riesgos y recuperación

CREDENTIALS → AUTHENTICATING → MFA_REQUIRED → VERIFYING → AUTHENTICATED → MERGING → NAVIGATING | MERGE_ERROR; errores de login vuelven al paso activo.

No reintentos ilimitados ni datos locales como fuente externa de verdad. Campos, endpoints y política que sigan abiertos permanecen explícitos; resolver/actualizar spec de origen antes de modificar código. Riesgo de capacidad/fecha se revisa cada sprint sin retirar esta funcionalidad ocultamente.

