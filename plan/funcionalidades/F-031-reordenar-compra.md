# Plan de implementación — F-031 Reordenar una compra anterior

## 1. Metadatos y entradas

| Campo | Valor |
|---|---|
| ID / versión / estado | F-031 / 0.1.0 / En revisión |
| Objetivo académico | S05/H6, semanas 15–16; implementación propia y pruebas con dobles en H4 |
| Entrada SDD | [Funcional](../../SPECS/funcional/F-031-reordenar-compra.md), [UI](../../SPECS/ui/F-031-reordenar-compra.md), [API](../../SPECS/contrato-api/F-031-reordenar-compra.md), [React](../../SPECS/componentes-react/F-031-reordenar-compra.md) |
| Ejecución y revisores | [Tareas de F-031](../seguimiento/F-031-reordenar-compra.md); responsable asignado por el PO: **Fernando Saire**; revisor principal: **Jim Segovia**. [Matriz de bloques](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md). Estimación base en la matriz; ejecución y evidencia pendientes. |
| Plan general / seguridad | [Semanas 7–16](../PLAN-IMPLEMENTACION.md), [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md) |

## Entrega de H4 y cierre objetivo

**Implementación propia y pruebas en H4; integración completa posterior.** Implementar recompra G1, dedupe/ajustes/transacción carrito, autorización del pedido y revalidación SKU/precio/cantidad G6; fixtures donde falte G5. Resolver I-03/G-REORDER antes del cierre S05.

**Cierre base:** S05/H6, semanas 15–16; implementación propia y pruebas con dobles en H4. El PO establece disponibilidad sin restricción horaria; todo el trabajo propio definido se implementa y prueba en H4. Los límites son contrato, entorno, datos, autorizaciones y calidad. [Inventario H4](../ALCANCE-H4-PRODUCTOS-SEGURIDAD.md) y [S02](../iteraciones/S02-semanas-09-11.md). Registrar diseñado, implementado con datos de prueba, integrado con otro módulo y probado en el despliegue por separado; no inventar contrato ni liberar gates por planificar.

**Cierre H4 anticipado por contratos:** esta F forma parte de la extensión de cinco funciones que puede llevar H4 de 25 a 30. Si todas las dependencias intermodulares y DoD se prueban antes del corte, aceptar H4 y descontar su cierre base posterior; el tiempo del equipo no limita esa decisión.

## 2. Objetivo y límites

Entregar reordenar una compra anterior conforme comportamiento/UI/API/React, no una pantalla aislada.
Mostrar respuesta y dejar checkout explícito. Tras timeout releer cart y no repetir hasta garantía de ejecución; no sugerencias sustitutas automáticas fuera alcance.

## 3. Decisiones técnicas

| Área | Trabajo / decisión |
|---|---|
| Frontend / render | `ReorderAction`, `ReorderResultDialog`; hook `useReorder`; arquitectura transversal React. |
| Backend / adaptador | Autorizar pedido y revalidar cada SKU antes de sumar al carrito; resultados parciales y garantía de reintento no duplicador. |
| Persistencia | Sin persistencia de dominio local. Siempre modelo lógico vigente, nunca el esquema histórico de dos tablas. |
| Remoto / caché | Después de éxito invalidar cart y quote; detalle histórico no cambia. |
| Seguridad específica | Reordenado de pedido ajeno y replay no incrementa duplicadamente, no precios históricos. |
| UI Kit | DS-001 v0.2.0; G-STACK pendiente, no fijar versiones no verificadas. |

## 4. Dependencias y Definition of Ready

- Dependencias de comportamiento/flujo: [F-030](F-030-detalle-pedido.md), [F-016](F-016-agregar-item-carrito.md).
- Gates: I-01, I-03, G-REORDER; consultar [registro](../DECISIONES-Y-BLOQUEOS.md). G-STACK/G-SHELL para interfaz compartida aplicable.
- Pendientes específicos: I-01/I-03 y garantía reintento reordenado.
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
Las tareas y el estado real viven únicamente en [seguimiento](../seguimiento/F-031-reordenar-compra.md); aquí no se duplica un tablero.

## 6. Criterios de terminado y pruebas

- agotado excluido con razón.
- resultado parcial conserva elegibles.
- sin añadidos no éxito falso.
- doble click no repetir y timeout no auto retry.
- Cada estado documentado tiene caso verificable y foco/recuperación correctos.
- Seguridad: Reordenado de pedido ajeno y replay no incrementa duplicadamente, no precios históricos.
- DB si aplica: identidad/constraints/versiones/transacción y rollback probados sin persistencia prohibida.
- Evidencias sanitizadas y revisión por persona distinta, según [DoD general](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-done-y-evidencia).
- Cuando se exige homologación, prueba real aprobada además de fixture. Si bloqueada, funcionalidad no se declara completa.

## 7. Riesgos y recuperación

READY → REORDERING → COMPLETE | PARTIAL | NONE_ADDED | CONFLICT | ERROR; solicitud incierta no POST automático.

No reintentos ilimitados ni datos locales como fuente externa de verdad. Campos, endpoints y política que sigan abiertos permanecen explícitos; resolver/actualizar spec de origen antes de modificar código. Los riesgos de contrato, entorno y calidad se revisan por operación, sin retirar esta funcionalidad por disponibilidad horaria.
