# Plan de implementación — F-035 Enviar actualización de despacho por correo

## 1. Metadatos y entradas

| Campo | Valor |
|---|---|
| ID / versión / estado | F-035 / 0.1.0 / En revisión |
| Objetivo académico | Sprint 5, semanas 14–15 |
| Entrada SDD | [Funcional](../../SPECS/funcional/F-035-enviar-actualizacion-despacho.md), [UI](../../SPECS/ui/F-035-enviar-actualizacion-despacho.md), [API](../../SPECS/contrato-api/F-035-enviar-actualizacion-despacho.md), [React](../../SPECS/componentes-react/F-035-enviar-actualizacion-despacho.md) |
| Ejecución y revisores | [Tareas de F-035](../seguimiento/F-035-enviar-actualizacion-despacho.md), propuesta según roles actuales |
| Plan general / seguridad | [Semanas 6–15](../PLAN-IMPLEMENTACION.md), [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md) |

## 2. Objetivo y límites

Entregar enviar actualización de despacho por correo conforme comportamiento/UI/API/React, no una pantalla aislada.
Contrato actual Despacho→Ventas no autoriza Marketplace a consumir. I-05 bloquea integración real; mocks versionados permiten probar composición sin fingir suscripción real.

## 3. Decisiones técnicas

| Área | Trabajo / decisión |
|---|---|
| Frontend / render | `ShipmentEmailTemplate`; hook `Sin hook navegador; handler evento y renderer servidor`; arquitectura transversal React. |
| Backend / adaptador | Consumir sólo evento homologado, validar/autenticar/deduplicar shipmentEventId y encolar sin alterar despacho. |
| Persistencia | NotificationDelivery. Siempre modelo lógico vigente, nunca el esquema histórico de dos tablas. |
| Remoto / caché | Evento versionado alimenta NotificationDelivery, no cache React ni persistencia de tracking. |
| Seguridad específica | Evento falso/replay/fuera de orden y firmas/scopes según contrato; no notificación inventada desde GET. |
| UI Kit | DS-001 v0.2.0; G-STACK pendiente, no fijar versiones no verificadas. |

## 4. Dependencias y Definition of Ready

- Dependencias de comportamiento/flujo: [F-032](F-032-seguimiento-despacho.md), [F-033](F-033-generar-plantilla-correo.md), [F-034](F-034-enviar-confirmacion-asincrona.md).
- Gates: I-05, G-MAIL; consultar [registro](../DECISIONES-Y-BLOQUEOS.md). G-STACK/G-SHELL para interfaz compartida aplicable.
- Pendientes específicos: I-05/H-05 y F-033/F-034.
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
Las tareas y el estado real viven únicamente en [seguimiento](../seguimiento/F-035-enviar-actualizacion-despacho.md); aquí no se duplica un tablero.

## 6. Criterios de terminado y pruebas

- evento repetido una entrega lógica.
- email render sin PII.
- enlace exige sesión/ownership.
- fallo correo no revierte estado.
- Cada estado documentado tiene caso verificable y foco/recuperación correctos.
- Seguridad: Evento falso/replay/fuera de orden y firmas/scopes según contrato; no notificación inventada desde GET.
- DB si aplica: identidad/constraints/versiones/transacción y rollback probados sin persistencia prohibida.
- Evidencias sanitizadas y revisión por persona distinta, según [DoD general](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-y-definition-of-done).
- Cuando se exige homologación, prueba real aprobada además de fixture. Si bloqueada, funcionalidad no se declara completa.

## 7. Riesgos y recuperación

EVENT_VALIDATED → RENDERED → QUEUED; evento duplicado reutiliza entrega; fallo envío no cambia despacho.

No reintentos ilimitados ni datos locales como fuente externa de verdad. Campos, endpoints y política que sigan abiertos permanecen explícitos; resolver/actualizar spec de origen antes de modificar código. Riesgo de capacidad/fecha se revisa cada sprint sin retirar esta funcionalidad ocultamente.

