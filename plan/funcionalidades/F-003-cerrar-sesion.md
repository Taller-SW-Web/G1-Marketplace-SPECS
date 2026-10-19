# Plan de implementación — F-003 Cerrar sesión

## 1. Metadatos y entradas

| Campo | Valor |
|---|---|
| ID / versión / estado | F-003 / 0.1.0 / En revisión |
| Objetivo académico | S02/H4, semanas 9–11; cierre sólo con gates y prueba en despliegue |
| Entrada SDD | [Funcional](../../SPECS/funcional/F-003-cerrar-sesion.md), [UI](../../SPECS/ui/F-003-cerrar-sesion.md), [API](../../SPECS/contrato-api/F-003-cerrar-sesion.md), [React](../../SPECS/componentes-react/F-003-cerrar-sesion.md) |
| Ejecución y revisores | [Tareas de F-003](../seguimiento/F-003-cerrar-sesion.md); responsable asignado por el PO: **Jim Segovia**; revisor principal: **Andres Morales**. [Matriz de bloques](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md). Estimación base en la matriz; ejecución y evidencia pendientes. |
| Plan general / seguridad | [Semanas 7–16](../PLAN-IMPLEMENTACION.md), [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md) |

## Entrega de H4 y cierre objetivo

**Objetivo de cierre H4.** Implementar logout G7 y limpieza de sesión/caché de usuario; probar UI y API después de salir, expiración y repetición idempotente.

**Cierre base:** S02/H4, semanas 9–11; cierre sólo con gates y prueba en despliegue. El PO establece disponibilidad sin restricción horaria; todo el trabajo propio definido se implementa y prueba en H4. Los límites son contrato, entorno, datos, autorizaciones y calidad. [Inventario H4](../ALCANCE-H4-PRODUCTOS-SEGURIDAD.md) y [S02](../iteraciones/S02-semanas-09-11.md). Registrar diseñado, implementado con datos de prueba, integrado con otro módulo y probado en el despliegue por separado; no inventar contrato ni liberar gates por planificar.

## 2. Objetivo y límites

Entregar cerrar sesión conforme comportamiento/UI/API/React, no una pantalla aislada.
Solicitar revocación protegida, realizar limpieza local también si red falla y navegar /. Evitar que respuestas en vuelo repueblen la UI con datos del titular anterior.

## 3. Decisiones técnicas

| Área | Trabajo / decisión |
|---|---|
| Frontend / render | `LogoutAction`, `CheckoutLogoutDialog`; hook `useLogout`; arquitectura transversal React. |
| Backend / adaptador | Revocar refresh vía Seguridad y limpiar sesión protegida sin borrar carrito/favoritos. |
| Persistencia | Sin persistencia de dominio local. Siempre modelo lógico vigente, nunca el esquema histórico de dos tablas. |
| Remoto / caché | Al cerrar, cancelar queries privadas, limpiar caché por titular, estado de checkout y datos sensibles. |
| Seguridad específica | Revocación y cachés después logout/cambio cuenta, CSRF según transporte, no exposición refresh. |
| UI Kit | DS-001 v0.2.0; G-STACK pendiente, no fijar versiones no verificadas. |

## 4. Dependencias y Definition of Ready

- Dependencias de comportamiento/flujo: [F-002](F-002-iniciar-sesion.md).
- Gates: G-AUTH; consultar [registro](../DECISIONES-Y-BLOQUEOS.md). G-STACK/G-SHELL para interfaz compartida aplicable.
- Pendientes específicos: Contrato de transporte y revocación; diseño compartido de cuenta vigente.
- Responsable/revisor confirman alcance, contrato y criterios de prueba; contrato/fixtures definidos; estados de UI leídos. Mockups no asignan automáticamente código.
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
Las tareas y el estado real viven únicamente en [seguimiento](../seguimiento/F-003-cerrar-sesion.md); aquí no se duplica un tablero.

## 6. Criterios de terminado y pruebas

- cancelar mantiene sesión.
- fallo remoto cierra localmente.
- otro usuario no ve caché anterior.
- O-004 devuelve foco al cancelar.
- Cada estado documentado tiene caso verificable y foco/recuperación correctos.
- Seguridad: Revocación y cachés después logout/cambio cuenta, CSRF según transporte, no exposición refresh.
- DB si aplica: identidad/constraints/versiones/transacción y rollback probados sin persistencia prohibida.
- Evidencias sanitizadas y revisión por persona distinta, según [DoD general](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-done-y-evidencia).
- Cuando se exige homologación, prueba real aprobada además de fixture. Si bloqueada, funcionalidad no se declara completa.

## 7. Riesgos y recuperación

IDLE → CONFIRMING (si checkout) → REVOKING → LOGGED_OUT; revocación fallida termina igualmente LOGGED_OUT local.

No reintentos ilimitados ni datos locales como fuente externa de verdad. Campos, endpoints y política que sigan abiertos permanecen explícitos; resolver/actualizar spec de origen antes de modificar código. Los riesgos de contrato, entorno y calidad se revisan por operación, sin retirar esta funcionalidad por disponibilidad horaria.
