# Plan de implementación — F-020 Fusionar carrito anónimo al iniciar sesión

## 1. Metadatos y entradas

| Campo | Valor |
|---|---|
| ID / versión / estado | F-020 / 0.1.0 / En revisión |
| Objetivo académico | Sprint 3, semanas 10–11 |
| Entrada SDD | [Funcional](../../SPECS/funcional/F-020-fusionar-carrito-anonimo.md), [UI](../../SPECS/ui/F-020-fusionar-carrito-anonimo.md), [API](../../SPECS/contrato-api/F-020-fusionar-carrito-anonimo.md), [React](../../SPECS/componentes-react/F-020-fusionar-carrito-anonimo.md) |
| Ejecución y revisores | [Tareas de F-020](../seguimiento/F-020-fusionar-carrito-anonimo.md), propuesta según roles actuales |
| Plan general / seguridad | [Semanas 6–15](../PLAN-IMPLEMENTACION.md), [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md) |

## 2. Objetivo y límites

Entregar fusionar carrito anónimo al iniciar sesión conforme comportamiento/UI/API/React, no una pantalla aislada.
Servidor conserva ambos ante fallo e invalida cookie sólo commit. Frontend no puede comprobar HttpOnly: no fuente se conoce por respuesta; retirar opción de retry sólo por evidencia de origen ausente/expirado, no prometer disponibilidad indefinida.

## 3. Decisiones técnicas

| Área | Trabajo / decisión |
|---|---|
| Frontend / render | `CartMergeCoordinator`, `MergeFailureNotice`, `MergeAdjustmentsDialog`; hook `useAnonymousCartMerge`; arquitectura transversal React. |
| Backend / adaptador | Fusionar con bloqueo/transacción, suma limitada, origen MERGED y cookie invalidada sólo tras commit; fallo conserva ambos. |
| Persistencia | Cart/CartItem (MERGED/destino). Siempre modelo lógico vigente, nunca el esquema histórico de dos tablas. |
| Remoto / caché | Después de éxito refrescar cart autenticado y descartar caché anónima. 200 merged:false no suma. Cookie sólo BFF. |
| Seguridad específica | Fusionar cookie de otra sesión / sin origen / MERGED concurrente sin duplicar, token inválido no cambia dueño. |
| UI Kit | DS-001 v0.2.0; G-STACK pendiente, no fijar versiones no verificadas. |

## 4. Dependencias y Definition of Ready

- Dependencias de comportamiento/flujo: [F-002](F-002-iniciar-sesion.md), [F-019](F-019-visualizar-carrito.md).
- Gates: I-01; consultar [registro](../DECISIONES-Y-BLOQUEOS.md). G-STACK/G-SHELL para interfaz compartida aplicable.
- Pendientes específicos: I-01; semántica cookie TTL/detección de fuente a documentar con BFF.
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
Las tareas y el estado real viven únicamente en [seguimiento](../seguimiento/F-020-fusionar-carrito-anonimo.md); aquí no se duplica un tablero.

## 6. Criterios de terminado y pruebas

- fusión repetida no suma.
- MFA incompleto no dispara.
- continuar conserva sesión y no fusiona.
- banner de pendientes no revela segundo carrito.
- Cada estado documentado tiene caso verificable y foco/recuperación correctos.
- Seguridad: Fusionar cookie de otra sesión / sin origen / MERGED concurrente sin duplicar, token inválido no cambia dueño.
- DB si aplica: identidad/constraints/versiones/transacción y rollback probados sin persistencia prohibida.
- Evidencias sanitizadas y revisión por persona distinta, según [DoD general](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-y-definition-of-done).
- Cuando se exige homologación, prueba real aprobada además de fixture. Si bloqueada, funcionalidad no se declara completa.

## 7. Riesgos y recuperación

IDLE → MERGING → MERGED | NO_SOURCE | FAILED; FAILED → MERGING o DEFERRED; DEFERRED sólo carrito de cuenta.

No reintentos ilimitados ni datos locales como fuente externa de verdad. Campos, endpoints y política que sigan abiertos permanecen explícitos; resolver/actualizar spec de origen antes de modificar código. Riesgo de capacidad/fecha se revisa cada sprint sin retirar esta funcionalidad ocultamente.

