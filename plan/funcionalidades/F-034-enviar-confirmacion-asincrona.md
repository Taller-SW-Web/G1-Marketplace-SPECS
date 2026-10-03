# Plan de implementación — F-034 Enviar confirmación asíncrona

## 1. Metadatos y entradas

| Campo | Valor |
|---|---|
| ID / versión / estado | F-034 / 0.1.0 / En revisión |
| Objetivo académico | Sprint 5, semanas 14–15 |
| Entrada SDD | [Funcional](../../SPECS/funcional/F-034-enviar-confirmacion-asincrona.md), [UI](../../SPECS/ui/F-034-enviar-confirmacion-asincrona.md), [API](../../SPECS/contrato-api/F-034-enviar-confirmacion-asincrona.md), [React](../../SPECS/componentes-react/F-034-enviar-confirmacion-asincrona.md) |
| Ejecución y revisores | [Tareas de F-034](../seguimiento/F-034-enviar-confirmacion-asincrona.md), propuesta según roles actuales |
| Plan general / seguridad | [Semanas 6–15](../PLAN-IMPLEMENTACION.md), [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md) |

## 2. Objetivo y límites

Entregar enviar confirmación asíncrona conforme comportamiento/UI/API/React, no una pantalla aislada.
Backend persiste NotificationDelivery PENDING antes worker, deduplica ORDER_CONFIRMATION+eventKey; UI no espera SENT. Proveedor no se llama al montar V-014.

## 3. Decisiones técnicas

| Área | Trabajo / decisión |
|---|---|
| Frontend / render | `OrderEmailNotice`; hook `Sin hook de envío; usa resultado confirmado F-027`; arquitectura transversal React. |
| Backend / adaptador | Outbox NotificationDelivery atómica con transición local SUCCEEDED de CheckoutOperation, no con la BD de Ventas ni el proveedor; deduplicación, cifrado destinatario, worker y reconciliación de respuesta perdida. |
| Persistencia | NotificationDelivery. Siempre modelo lógico vigente, nunca el esquema histórico de dos tablas. |
| Remoto / caché | No endpoint público de notificaciones, no polling entrega. |
| Seguridad específica | Carrera en outbox, replay de eventos, destinatario cifrado y claves fuera repo; reconciliar timeout para no duplicar envío. |
| UI Kit | DS-001 v0.2.0; G-STACK pendiente, no fijar versiones no verificadas. |

## 4. Dependencias y Definition of Ready

- Dependencias de comportamiento/flujo: [F-026](F-026-crear-orden-ventas.md), [F-033](F-033-generar-plantilla-correo.md).
- Gates: I-02, G-MAIL; consultar [registro](../DECISIONES-Y-BLOQUEOS.md). G-STACK/G-SHELL para interfaz compartida aplicable.
- Pendientes específicos: F-026 éxito,I-02; proveedor/cifrado/retries backend; I-05 si origen evento lo necesita.
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
Las tareas y el estado real viven únicamente en [seguimiento](../seguimiento/F-034-enviar-confirmacion-asincrona.md); aquí no se duplica un tablero.

## 6. Criterios de terminado y pruebas

- remontar vista no reenvía email.
- provider503 mantiene éxito pedido.
- sin email no placeholder PII.
- aviso no afirma entrega confirmada.
- Cada estado documentado tiene caso verificable y foco/recuperación correctos.
- Seguridad: Carrera en outbox, replay de eventos, destinatario cifrado y claves fuera repo; reconciliar timeout para no duplicar envío.
- DB si aplica: identidad/constraints/versiones/transacción y rollback probados sin persistencia prohibida.
- Evidencias sanitizadas y revisión por persona distinta, según [DoD general](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-y-definition-of-done).
- Cuando se exige homologación, prueba real aprobada además de fixture. Si bloqueada, funcionalidad no se declara completa.

## 7. Riesgos y recuperación

ORDER_PENDING → OMITTED; ORDER_CONFIRMED → ASYNC_NOTICE; fallo provider no modifica CONFIRMED.

No reintentos ilimitados ni datos locales como fuente externa de verdad. Campos, endpoints y política que sigan abiertos permanecen explícitos; resolver/actualizar spec de origen antes de modificar código. Riesgo de capacidad/fecha se revisa cada sprint sin retirar esta funcionalidad ocultamente.

