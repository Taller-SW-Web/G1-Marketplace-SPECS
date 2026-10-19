# Plan de implementación — F-028 Consultar historial de pedidos

## 1. Metadatos y entradas

| Campo | Valor |
|---|---|
| ID / versión / estado | F-028 / 0.1.0 / En revisión |
| Objetivo académico | S03, semanas 12–13; implementación y pruebas propias comienzan en H4 |
| Entrada SDD | [Funcional](../../SPECS/funcional/F-028-historial-pedidos.md), [UI](../../SPECS/ui/F-028-historial-pedidos.md), [API](../../SPECS/contrato-api/F-028-historial-pedidos.md), [React](../../SPECS/componentes-react/F-028-historial-pedidos.md) |
| Ejecución y revisores | [Tareas de F-028](../seguimiento/F-028-historial-pedidos.md); responsable asignado por el PO: **Fernando Saire**; revisor principal: **Jim Segovia**. [Matriz de bloques](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md). Estimación base en la matriz; ejecución y evidencia pendientes. |
| Plan general / seguridad | [Semanas 7–16](../PLAN-IMPLEMENTACION.md), [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md) |

## Entrega de H4 y cierre objetivo

**Implementación propia y pruebas en H4; integración completa posterior.** Implementar historial FE+BFF con fixture o Ventas autorizado, paginación/vacío/error y usuarios A/B; integrar G5 donde esté habilitado. Cierre integral S03 con titularidad y despliegue.

**Cierre base:** S03, semanas 12–13; implementación y pruebas propias comienzan en H4. El PO establece disponibilidad sin restricción horaria; todo el trabajo propio definido se implementa y prueba en H4. Los límites son contrato, entorno, datos, autorizaciones y calidad. [Inventario H4](../ALCANCE-H4-PRODUCTOS-SEGURIDAD.md) y [S02](../iteraciones/S02-semanas-09-11.md). Registrar diseñado, implementado con datos de prueba, integrado con otro módulo y probado en el despliegue por separado; no inventar contrato ni liberar gates por planificar.

## 2. Objetivo y límites

Entregar consultar historial de pedidos conforme comportamiento/UI/API/React, no una pantalla aislada.
GET BFF /orders/me deriva usuario JWT, backend autoriza contra Ventas. Lista enlaza detalle por orderId opaco.

## 3. Decisiones técnicas

| Área | Trabajo / decisión |
|---|---|
| Frontend / render | `OrdersHistoryContainer`, `OrderList`; hook `useMyOrders`; arquitectura transversal React. |
| Backend / adaptador | Adaptar historial/me con titular del JWT validado en Ventas y paginación, sin clienteId del navegador ni réplica. |
| Persistencia | Sin persistencia de dominio local. Siempre modelo lógico vigente, nunca el esquema histórico de dos tablas. |
| Remoto / caché | ['orders','me',sessionScope,{page,pageSize,state,from,to}]; sin clienteId en URL/request; limpiar en cambio identidad. |
| Seguridad específica | IDOR con JWT con clienteId forjado y cachés entre usuarios, sólo pedidos propios. |
| UI Kit | DS-001 v0.2.0; G-STACK pendiente, no fijar versiones no verificadas. |

## 4. Dependencias y Definition of Ready

- Dependencias de comportamiento/flujo: [F-002](F-002-iniciar-sesion.md).
- Gates: I-03; consultar [registro](../DECISIONES-Y-BLOQUEOS.md). G-STACK/G-SHELL para interfaz compartida aplicable.
- Pendientes específicos: I-03, estados publicados Ventas y política fuera de rango.
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
Las tareas y el estado real viven únicamente en [seguimiento](../seguimiento/F-028-historial-pedidos.md); aquí no se duplica un tablero.

## 6. Criterios de terminado y pruebas

- request no clienteId.
- vacío catálogo.
- 401 retira lista previa.
- meta pagina y conserva filtros.
- Cada estado documentado tiene caso verificable y foco/recuperación correctos.
- Seguridad: IDOR con JWT con clienteId forjado y cachés entre usuarios, sólo pedidos propios.
- DB si aplica: identidad/constraints/versiones/transacción y rollback probados sin persistencia prohibida.
- Evidencias sanitizadas y revisión por persona distinta, según [DoD general](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-done-y-evidencia).
- Cuando se exige homologación, prueba real aprobada además de fixture. Si bloqueada, funcionalidad no se declara completa.

## 7. Riesgos y recuperación

LOADING → LIST | EMPTY | FILTER_EMPTY | ERROR;401 oculta datos y ofrece login seguro.

No reintentos ilimitados ni datos locales como fuente externa de verdad. Campos, endpoints y política que sigan abiertos permanecen explícitos; resolver/actualizar spec de origen antes de modificar código. Los riesgos de contrato, entorno y calidad se revisan por operación, sin retirar esta funcionalidad por disponibilidad horaria.
