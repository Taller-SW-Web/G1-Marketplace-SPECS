# Plan de implementación — F-019 Visualizar el carrito, totales y estado vacío

## 1. Metadatos y entradas

| Campo | Valor |
|---|---|
| ID / versión / estado | F-019 / 0.1.0 / En revisión |
| Objetivo académico | Sprint 3, semanas 10–11 |
| Entrada SDD | [Funcional](../../SPECS/funcional/F-019-visualizar-carrito.md), [UI](../../SPECS/ui/F-019-visualizar-carrito.md), [API](../../SPECS/contrato-api/F-019-visualizar-carrito.md), [React](../../SPECS/componentes-react/F-019-visualizar-carrito.md) |
| Ejecución y revisores | [Tareas de F-019](../seguimiento/F-019-visualizar-carrito.md), propuesta según roles actuales |
| Plan general / seguridad | [Semanas 6–15](../PLAN-IMPLEMENTACION.md), [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md) |

## 2. Objetivo y límites

Entregar visualizar el carrito, totales y estado vacío conforme comportamiento/UI/API/React, no una pantalla aislada.
Anónimo inicia auth mediante O-003 con /checkout/direccion seguro y revalida al retornar. Continuar sin merge muestra sólo carrito autenticado y Reintentar mientras cookie disponible.

## 3. Decisiones técnicas

| Área | Trabajo / decisión |
|---|---|
| Frontend / render | `CartPageContainer`, `CartLine`, `CartSubtotal`; hook `useCurrentCart`; arquitectura transversal React. |
| Backend / adaptador | Leer Cart/CartItem y enriquecer sin modificar cantidad en GET; subtotal nulo para precio pendiente y attention por línea. |
| Persistencia | Cart/CartItem. Siempre modelo lógico vigente, nunca el esquema histórico de dos tablas. |
| Remoto / caché | ['cart','current',sessionScope]; scope evita mezclar anónimo/autenticado y cuentas distintas. |
| Seguridad específica | Aislamiento anónimo/cuentas, snapshot mínimo sin PII y fallo no fuga de datos. |
| UI Kit | DS-001 v0.2.0; G-STACK pendiente, no fijar versiones no verificadas. |

## 4. Dependencias y Definition of Ready

- Dependencias de comportamiento/flujo: [F-016](F-016-agregar-item-carrito.md).
- Gates: I-01; consultar [registro](../DECISIONES-Y-BLOQUEOS.md). G-STACK/G-SHELL para interfaz compartida aplicable.
- Pendientes específicos: I-01, mapeo attention pendiente y F-020.
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
Las tareas y el estado real viven únicamente en [seguimiento](../seguimiento/F-019-visualizar-carrito.md); aquí no se duplica un tablero.

## 6. Criterios de terminado y pruebas

- vacío sin resumen CTA.
- subtotal null no gratuito.
- error no borra líneas por inferencia.
- cuenta no muestra invitado tras continuar.
- Cada estado documentado tiene caso verificable y foco/recuperación correctos.
- Seguridad: Aislamiento anónimo/cuentas, snapshot mínimo sin PII y fallo no fuga de datos.
- DB si aplica: identidad/constraints/versiones/transacción y rollback probados sin persistencia prohibida.
- Evidencias sanitizadas y revisión por persona distinta, según [DoD general](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-y-definition-of-done).
- Cuando se exige homologación, prueba real aprobada además de fixture. Si bloqueada, funcionalidad no se declara completa.

## 7. Riesgos y recuperación

LOADING → VALID_ANONYMOUS | VALID_AUTHENTICATED | ATTENTION | EMPTY | ERROR; merge pendiente es aviso transversal, no segundo carrito.

No reintentos ilimitados ni datos locales como fuente externa de verdad. Campos, endpoints y política que sigan abiertos permanecen explícitos; resolver/actualizar spec de origen antes de modificar código. Riesgo de capacidad/fecha se revisa cada sprint sin retirar esta funcionalidad ocultamente.

