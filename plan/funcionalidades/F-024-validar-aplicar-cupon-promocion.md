# Plan de implementación — F-024 Validar y aplicar cupón o promoción

## 1. Metadatos y entradas

| Campo | Valor |
|---|---|
| ID / versión / estado | F-024 / 0.1.0 / En revisión |
| Objetivo académico | Sprint 4, semanas 12–13 |
| Entrada SDD | [Funcional](../../SPECS/funcional/F-024-validar-aplicar-cupon-promocion.md), [UI](../../SPECS/ui/F-024-validar-aplicar-cupon-promocion.md), [API](../../SPECS/contrato-api/F-024-validar-aplicar-cupon-promocion.md), [React](../../SPECS/componentes-react/F-024-validar-aplicar-cupon-promocion.md) |
| Ejecución y revisores | [Tareas de F-024](../seguimiento/F-024-validar-aplicar-cupon-promocion.md), propuesta según roles actuales |
| Plan general / seguridad | [Semanas 6–15](../PLAN-IMPLEMENTACION.md), [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md) |

## 2. Objetivo y límites

Entregar validar y aplicar cupón o promoción conforme comportamiento/UI/API/React, no una pantalla aislada.
POST benefits no consume. Quitar solicita nueva quote base con F-023 según V-011; no crear DELETE cupón. Falla promociones sólo permite continuar si BFF devuelve quote base válida y política aprobada.

## 3. Decisiones técnicas

| Área | Trabajo / decisión |
|---|---|
| Frontend / render | `CouponForm`, `SelectedBenefit`; hook `useCheckoutBenefits`; arquitectura transversal React. |
| Backend / adaptador | Validar/mejor beneficio con proveedor, sin consumo de cupón; sustituir quote, definir quitar y falla segura. |
| Persistencia | Sin persistencia de dominio local. Siempre modelo lógico vigente, nunca el esquema histórico de dos tablas. |
| Remoto / caché | Quote nuevo sustituye atómicamente anterior y su total/vencimiento; invalida preparación. |
| Seguridad específica | Quote ajena/vencida, cupón no logs, no consumo en validación ni fraude por total del cliente. |
| UI Kit | DS-001 v0.2.0; G-STACK pendiente, no fijar versiones no verificadas. |

## 4. Dependencias y Definition of Ready

- Dependencias de comportamiento/flujo: [F-023](F-023-calcular-resumen-envio.md).
- Gates: I-01, G-BENEFIT; consultar [registro](../DECISIONES-Y-BLOQUEOS.md). G-STACK/G-SHELL para interfaz compartida aplicable.
- Pendientes específicos: I-01, OPEN-11/12 y V-011-OPEN-04.
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
Las tareas y el estado real viven únicamente en [seguimiento](../seguimiento/F-024-validar-aplicar-cupon-promocion.md); aquí no se duplica un tablero.

## 6. Criterios de terminado y pruebas

- aplicar no acumula descuento manual.
- 422 no pierde quote válida.
- quitar recalcula y no consume.
- respuesta vieja no reemplaza última quote.
- Cada estado documentado tiene caso verificable y foco/recuperación correctos.
- Seguridad: Quote ajena/vencida, cupón no logs, no consumo en validación ni fraude por total del cliente.
- DB si aplica: identidad/constraints/versiones/transacción y rollback probados sin persistencia prohibida.
- Evidencias sanitizadas y revisión por persona distinta, según [DoD general](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-y-definition-of-done).
- Cuando se exige homologación, prueba real aprobada además de fixture. Si bloqueada, funcionalidad no se declara completa.

## 7. Riesgos y recuperación

NO_COUPON → VALIDATING → APPLIED | NOT_APPLICABLE | INVALID | QUOTE_EXPIRED | ERROR; quitar requiere cotización sin cupón.

No reintentos ilimitados ni datos locales como fuente externa de verdad. Campos, endpoints y política que sigan abiertos permanecen explícitos; resolver/actualizar spec de origen antes de modificar código. Riesgo de capacidad/fecha se revisa cada sprint sin retirar esta funcionalidad ocultamente.

