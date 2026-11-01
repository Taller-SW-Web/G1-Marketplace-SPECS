# Plan de implementación — F-040 Registrar evaluación postentrega

## 1. Metadatos y entradas

| Campo | Valor |
|---|---|
| ID / versión / estado | F-040 / 0.1.0 / En revisión |
| Objetivo académico | S05/H6, semanas 15–16; implementación propia y pruebas con dobles en H4 |
| Entrada SDD | [Funcional](../../SPECS/funcional/F-040-evaluacion-postentrega.md), [UI](../../SPECS/ui/F-040-evaluacion-postentrega.md), [API](../../SPECS/contrato-api/F-040-evaluacion-postentrega.md), [React](../../SPECS/componentes-react/F-040-evaluacion-postentrega.md) |
| Ejecución y revisores | [Tareas de F-040](../seguimiento/F-040-evaluacion-postentrega.md); responsable asignado por el PO: **Diego Espinoza**; revisor principal: **Fernando Saire**. [Matriz de bloques](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md). Estimación base en la matriz; ejecución y evidencia pendientes. |
| Plan general / seguridad | [Semanas 7–16](../PLAN-IMPLEMENTACION.md), [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md) |

## Entrega de H4 y cierre objetivo

**Implementación propia y pruebas en H4; integración completa posterior.** Implementar prompt/formulario CSAT y adaptador conforme G5, reglas/payload/casos con fixture de pedido entregado; aislar transiciones durables aún sin contrato SHOWN/DISMISSED. Cierre S05 exige I-04/G-PROMPT resueltos.

**Cierre base:** S05/H6, semanas 15–16; implementación propia y pruebas con dobles en H4. El PO establece disponibilidad sin restricción horaria; todo el trabajo propio definido se implementa y prueba en H4. Los límites son contrato, entorno, datos, autorizaciones y calidad. [Inventario H4](../ALCANCE-H4-PRODUCTOS-SEGURIDAD.md) y [S02](../iteraciones/S02-semanas-09-11.md). Registrar diseñado, implementado con datos de prueba, integrado con otro módulo y probado en el despliegue por separado; no inventar contrato ni liberar gates por planificar.

## 2. Objetivo y límites

Entregar registrar evaluación postentrega conforme comportamiento/UI/API/React, no una pantalla aislada.
No mostrar desde pago ni sólo por dato local. Backend comprueba entrega y persiste únicamente PostDeliveryPrompt; CSAT en Ventas. Hasta definir lectura/actualización prompt sólo diseñar/test mocks, sin dismiss duradero inventado.

## 3. Decisiones técnicas

| Área | Trabajo / decisión |
|---|---|
| Frontend / render | `PostDeliveryInvitation`, `PostDeliveryFeedbackForm`; hook `usePostDeliveryFeedback`; arquitectura transversal React. |
| Backend / adaptador | Autorizar pedido entregado y prompt, mapear GOOD/REGULAR/BAD a 5/3/1 en Ventas; sólo estado UX local, ciclo prompt documentado. |
| Persistencia | PostDeliveryPrompt. Siempre modelo lógico vigente, nunca el esquema histórico de dos tablas. |
| Remoto / caché | POST csat está definido; endpoint eligibility/show/dismiss NO existe en contrato: no inventarlo. Caché por orderId/titular y prompt autoridad backend pendiente. |
| Seguridad específica | CSAT de pedido ajeno/no entregado/replay; XSS en comentario y PII en logs y no almacenar rating local. |
| UI Kit | DS-001 v0.2.0; G-STACK pendiente, no fijar versiones no verificadas. |

## 4. Dependencias y Definition of Ready

- Dependencias de comportamiento/flujo: [F-030](F-030-detalle-pedido.md), [F-032](F-032-seguimiento-despacho.md).
- Gates: I-03, I-04, G-PROMPT; consultar [registro](../DECISIONES-Y-BLOQUEOS.md). G-STACK/G-SHELL para interfaz compartida aplicable.
- Pendientes específicos: I-04; O-009-OPEN-02/03/04 y contrato del ciclo prompt.
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
Las tareas y el estado real viven únicamente en [seguimiento](../seguimiento/F-040-evaluacion-postentrega.md); aquí no se duplica un tablero.

## 6. Criterios de terminado y pruebas

- no entregado no banner.
- sentimiento cambia motivos coherentes.
- duplicado cierra como enviado.
- fallo conserva formulario.
- logout borra comentario.
- Escape respeta política sin registro supuesto.
- Cada estado documentado tiene caso verificable y foco/recuperación correctos.
- Seguridad: CSAT de pedido ajeno/no entregado/replay; XSS en comentario y PII en logs y no almacenar rating local.
- DB si aplica: identidad/constraints/versiones/transacción y rollback probados sin persistencia prohibida.
- Evidencias sanitizadas y revisión por persona distinta, según [DoD general](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-done-y-evidencia).
- Cuando se exige homologación, prueba real aprobada además de fixture. Si bloqueada, funcionalidad no se declara completa.

## 7. Riesgos y recuperación

INELIGIBLE | ELIGIBLE → SHOWN → EDITING → SENDING → SUBMITTED | NO_LONGER_ELIGIBLE | ERROR; dismiss protocolo pendiente, no mentir que guardó DISMISSED.

No reintentos ilimitados ni datos locales como fuente externa de verdad. Campos, endpoints y política que sigan abiertos permanecen explícitos; resolver/actualizar spec de origen antes de modificar código. Los riesgos de contrato, entorno y calidad se revisan por operación, sin retirar esta funcionalidad por disponibilidad horaria.
