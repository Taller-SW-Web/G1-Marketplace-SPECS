# Plan de implementación — F-027 Mostrar la confirmación de la orden

## 1. Metadatos y entradas

| Campo | Valor |
|---|---|
| ID / versión / estado | F-027 / 0.1.0 / En revisión |
| Objetivo académico | Sprint 4, semanas 12–13 |
| Entrada SDD | [Funcional](../../SPECS/funcional/F-027-confirmacion-orden.md), [UI](../../SPECS/ui/F-027-confirmacion-orden.md), [API](../../SPECS/contrato-api/F-027-confirmacion-orden.md), [React](../../SPECS/componentes-react/F-027-confirmacion-orden.md) |
| Ejecución y revisores | [Tareas de F-027](../seguimiento/F-027-confirmacion-orden.md), propuesta según roles actuales |
| Plan general / seguridad | [Semanas 6–15](../PLAN-IMPLEMENTACION.md), [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md) |

## 2. Objetivo y límites

Entregar mostrar la confirmación de la orden conforme comportamiento/UI/API/React, no una pantalla aislada.
F-026 conserva asociación opaca para navegación; cerrar V-014-OPEN-01 antes de deep links/refresh. Polling pendiente: usar Verificar manual, acotado; no nuevo POST ni éxito desde query param.

## 3. Decisiones técnicas

| Área | Trabajo / decisión |
|---|---|
| Frontend / render | `OrderConfirmationContainer`, `OrderConfirmationSummary`; hook `useOrderConfirmation`; arquitectura transversal React. |
| Backend / adaptador | GET operación propietaria,200 SUCCEEDED / 202 SUBMITTED / 409 fallo; resolver orden pública versus operationId sin lookup inventado. |
| Persistencia | CheckoutOperation (sólo lectura). Siempre modelo lógico vigente, nunca el esquema histórico de dos tablas. |
| Remoto / caché | ['checkout','operation',sessionScope,operationId]; al montar validar pertenencia; respuestas privadas no caché pública. |
| Seguridad específica | Operación ajena / ID manipulado no filtra datos,202 no éxito y callback/query no autentica. |
| UI Kit | DS-001 v0.2.0; G-STACK pendiente, no fijar versiones no verificadas. |

## 4. Dependencias y Definition of Ready

- Dependencias de comportamiento/flujo: [F-026](F-026-crear-orden-ventas.md).
- Gates: I-02, G-CHECKOUT, G-CONFIRM; consultar [registro](../DECISIONES-Y-BLOQUEOS.md). G-STACK/G-SHELL para interfaz compartida aplicable.
- Pendientes específicos: I-02; resolver mapping y resumen de artículos (no presentes en GET operación actual).
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
Las tareas y el estado real viven únicamente en [seguimiento](../seguimiento/F-027-confirmacion-orden.md); aquí no se duplica un tablero.

## 6. Criterios de terminado y pruebas

- 202 sin icono éxito.
- otro titular no datos.
- fallo email no altera éxito.
- copiar falla ofrece copia manual.
- deep link sin mapeo no llamada con ID equivocado.
- Cada estado documentado tiene caso verificable y foco/recuperación correctos.
- Seguridad: Operación ajena / ID manipulado no filtra datos,202 no éxito y callback/query no autentica.
- DB si aplica: identidad/constraints/versiones/transacción y rollback probados sin persistencia prohibida.
- Evidencias sanitizadas y revisión por persona distinta, según [DoD general](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-y-definition-of-done).
- Cuando se exige homologación, prueba real aprobada además de fixture. Si bloqueada, funcionalidad no se declara completa.

## 7. Riesgos y recuperación

LOADING → CONFIRMED | VERIFYING | FAILED | NOT_ACCESSIBLE | ERROR;202 SUBMITTED conserva neutral; CONFIRMED requiere SUCCEEDED+orderId.

No reintentos ilimitados ni datos locales como fuente externa de verdad. Campos, endpoints y política que sigan abiertos permanecen explícitos; resolver/actualizar spec de origen antes de modificar código. Riesgo de capacidad/fecha se revisa cada sprint sin retirar esta funcionalidad ocultamente.

