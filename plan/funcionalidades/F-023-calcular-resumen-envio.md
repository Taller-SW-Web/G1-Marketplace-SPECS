# Plan de implementación — F-023 Calcular y mostrar resumen de compra y envío

## 1. Metadatos y entradas

| Campo | Valor |
|---|---|
| ID / versión / estado | F-023 / 0.1.0 / En revisión |
| Objetivo académico | Sprint 4, semanas 12–13 |
| Entrada SDD | [Funcional](../../SPECS/funcional/F-023-calcular-resumen-envio.md), [UI](../../SPECS/ui/F-023-calcular-resumen-envio.md), [API](../../SPECS/contrato-api/F-023-calcular-resumen-envio.md), [React](../../SPECS/componentes-react/F-023-calcular-resumen-envio.md) |
| Ejecución y revisores | [Tareas de F-023](../seguimiento/F-023-calcular-resumen-envio.md), propuesta según roles actuales |
| Plan general / seguridad | [Semanas 6–15](../PLAN-IMPLEMENTACION.md), [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md) |

## 2. Objetivo y límites

Entregar calcular y mostrar resumen de compra y envío conforme comportamiento/UI/API/React, no una pantalla aislada.
Desglose autoritativo BFF; respuesta a dirección antigua no actualiza contexto. Sin vigencia o línea válida no continuar; recuperar contexto faltante vuelve dirección/carrito.

## 3. Decisiones técnicas

| Área | Trabajo / decisión |
|---|---|
| Frontend / render | `CheckoutQuoteContainer`, `CheckoutOrderSummary`; hook `useCheckoutQuote`; arquitectura transversal React. |
| Backend / adaptador | Cotizar por addressId/cartVersion con dueños de comerciales y scope técnico de Despacho, quote temporal y expiración. |
| Persistencia | Sin persistencia de dominio local. Siempre modelo lógico vigente, nunca el esquema histórico de dos tablas. |
| Remoto / caché | Quote temporal por titular/addressId/cartVersion; mutation POST sin reintento automático no acotado. |
| Seguridad específica | Scope mínimo técnico, quote/cart/dirección propios y no manipulación montos/costo. |
| UI Kit | DS-001 v0.2.0; G-STACK pendiente, no fijar versiones no verificadas. |

## 4. Dependencias y Definition of Ready

- Dependencias de comportamiento/flujo: [F-022](F-022-seleccionar-direccion-envio.md), [F-019](F-019-visualizar-carrito.md).
- Gates: I-01, I-06; consultar [registro](../DECISIONES-Y-BLOQUEOS.md). G-STACK/G-SHELL para interfaz compartida aplicable.
- Pendientes específicos: I-01 e I-06; cotizaciones:calcular sólo servidor.
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
Las tareas y el estado real viven únicamente en [seguimiento](../seguimiento/F-023-calcular-resumen-envio.md); aquí no se duplica un tablero.

## 6. Criterios de terminado y pruebas

- cambio dirección no usa quote anterior.
- 503 no envío gratis.
- vencida bloquea CTA.
- cambio carrito explicado.
- Cada estado documentado tiene caso verificable y foco/recuperación correctos.
- Seguridad: Scope mínimo técnico, quote/cart/dirección propios y no manipulación montos/costo.
- DB si aplica: identidad/constraints/versiones/transacción y rollback probados sin persistencia prohibida.
- Evidencias sanitizadas y revisión por persona distinta, según [DoD general](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-y-definition-of-done).
- Cuando se exige homologación, prueba real aprobada además de fixture. Si bloqueada, funcionalidad no se declara completa.

## 7. Riesgos y recuperación

CALCULATING → QUOTED | NO_COVERAGE | CART_CHANGED | LINE_ATTENTION | ERROR; expiresAt → EXPIRED hasta recalcular.

No reintentos ilimitados ni datos locales como fuente externa de verdad. Campos, endpoints y política que sigan abiertos permanecen explícitos; resolver/actualizar spec de origen antes de modificar código. Riesgo de capacidad/fecha se revisa cada sprint sin retirar esta funcionalidad ocultamente.

