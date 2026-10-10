# Plan de implementación — F-026 Crear la orden en Ventas y Postventa

## 1. Metadatos y entradas

| Campo | Valor |
|---|---|
| ID / versión / estado | F-026 / 0.1.0 / En revisión |
| Objetivo académico | Sprint 4, semanas 12–13 |
| Entrada SDD | [Funcional](../../SPECS/funcional/F-026-crear-orden-ventas.md), [UI](../../SPECS/ui/F-026-crear-orden-ventas.md), [API](../../SPECS/contrato-api/F-026-crear-orden-ventas.md), [React](../../SPECS/componentes-react/F-026-crear-orden-ventas.md) |
| Ejecución y revisores | [Tareas de F-026](../seguimiento/F-026-crear-orden-ventas.md), propuesta según roles actuales |
| Plan general / seguridad | [Semanas 6–15](../PLAN-IMPLEMENTACION.md), [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md) |

## 2. Objetivo y límites

Entregar crear la orden en ventas y postventa conforme comportamiento/UI/API/React, no una pantalla aislada.
POST BFF envía snapshot/dirección homologados a Ventas. `CREADO` permanece pendiente hasta la aptitud para pagar y la confirmación simulada autorizada por Ventas. 503 podría ser incierto: consultar operación original; no enviar una compra nueva.

## 3. Decisiones técnicas

| Área | Trabajo / decisión |
|---|---|
| Frontend / render | `OrderCreationForm`, `OrderSubmissionStatus`; hook `useCreateOrder`; arquitectura transversal React. |
| Backend / adaptador | Orquestar PREPARED→SUBMITTED (`CREADO`)→SUCCEEDED sólo con `PAGADO` verificable; Ventas idempotente, señal de aptitud, contrato simulado y recuperación incierta siguen bajo I-02. |
| Persistencia | CheckoutOperation. Siempre modelo lógico vigente, nunca el esquema histórico de dos tablas. |
| Remoto / caché | Invalidate operaciones/pedidos/cart después de SUCCEEDED; no reconstruir pedido a partir de carrito. |
| Seguridad específica | Idempotencia real con Ventas, operación/contacto manipulados y ownership; timeout no segundo pedido. |
| UI Kit | DS-001 v0.2.0; G-STACK pendiente, no fijar versiones no verificadas. |

## 4. Dependencias y Definition of Ready

- Dependencias de comportamiento/flujo: [F-025](F-025-simular-pago-revalidar-stock.md).
- Gates: I-01, I-02, G-CHECKOUT; consultar [registro](../DECISIONES-Y-BLOQUEOS.md). G-STACK/G-SHELL para interfaz compartida aplicable.
- Pendientes específicos: I-02 bloquea integración real; reglas contacto, idempotencia preparación/orden y recuperación abiertas.
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
Las tareas y el estado real viven únicamente en [seguimiento](../seguimiento/F-026-crear-orden-ventas.md); aquí no se duplica un tablero.

## 6. Criterios de terminado y pruebas

- doble click no dos pedidos.
- timeout no compra nueva.
- campos faltantes únicamente.
- 400 conserva datos válidos.
- contacto no persiste localmente.
- Cada estado documentado tiene caso verificable y foco/recuperación correctos.
- Seguridad: Idempotencia real con Ventas, operación/contacto manipulados y ownership; timeout no segundo pedido.
- DB si aplica: identidad/constraints/versiones/transacción y rollback probados sin persistencia prohibida.
- Evidencias sanitizadas y revisión por persona distinta, según [DoD general](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-y-definition-of-done).
- Cuando se exige homologación, prueba real aprobada además de fixture. Si bloqueada, funcionalidad no se declara completa.

## 7. Riesgos y recuperación

PREPARED → SUBMITTING → SUBMITTED (`CREADO`) | FIELD_ERROR | FAILED; SUBMITTED → VERIFYING → SUCCEEDED sólo con `PAGADO` | SUBMITTED | FAILED.

No reintentos ilimitados ni datos locales como fuente externa de verdad. Campos, endpoints y política que sigan abiertos permanecen explícitos; resolver/actualizar spec de origen antes de modificar código. Riesgo de capacidad/fecha se revisa cada sprint sin retirar esta funcionalidad ocultamente.

