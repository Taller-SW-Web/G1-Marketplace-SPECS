# Plan de implementación — F-025 Simular pago y revalidar stock

## 1. Metadatos y entradas

| Campo | Valor |
|---|---|
| ID / versión / estado | F-025 / 0.1.0 / En revisión |
| Objetivo académico | S3, semanas 12–13 |
| Entrada SDD | [Funcional](../../SPECS/funcional/F-025-simular-pago-revalidar-stock.md), [UI](../../SPECS/ui/F-025-simular-pago-revalidar-stock.md), [API](../../SPECS/contrato-api/F-025-simular-pago-revalidar-stock.md), [React](../../SPECS/componentes-react/F-025-simular-pago-revalidar-stock.md) |
| Ejecución y revisores | [Tareas de F-025](../seguimiento/F-025-simular-pago-revalidar-stock.md); responsable asignado por el PO: **Leonidas Garcia**; revisor principal: **Diego Espinoza**. [Matriz de bloques](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md). Estimación base en la matriz; ejecución y evidencia pendientes. |
| Plan general / seguridad | [Semanas 7–16](../PLAN-IMPLEMENTACION.md), [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md) |

## 2. Objetivo y límites

Entregar simular pago y revalidar stock conforme comportamiento/UI/API/React, no una pantalla aislada.
201 deja `PREPARED` y continúa a creación separada V-013; no confirma pago. 409 QUOTE_EXPIRED/REVALIDATION_CHANGED vuelve a resumen; STOCK_NOT_AVAILABLE requiere evidencia cuantitativa homologada. No tarjeta/CVV ni reserva stock.

## 3. Decisiones técnicas

| Área | Trabajo / decisión |
|---|---|
| Frontend / render | `PaymentSimulationForm`, `PreparationOutcome`; hook `useCheckoutPreparation`; arquitectura transversal React. |
| Backend / adaptador | Preparar CheckoutOperation con clave/fingerprint; PREPARED sólo conserva consentimiento y revalidación permitida, sin pedido/pago aprobado/reserva. Cantidad y snapshot final requieren contrato externo. |
| Persistencia | CheckoutOperation. Siempre modelo lógico vigente, nunca el esquema histórico de dos tablas. |
| Remoto / caché | CheckoutOperation del BFF es autoridad; almacenar referencia opaca según estrategia de recuperación aún abierta. |
| Seguridad específica | Fingerprint/clave reutilizada, replay de POST y concurrencia; no tarjeta/CVV ni reserva. |
| UI Kit | Checkout: componentes propios existentes (`Button`, `TextField`) y tokens DS-001; no instalar Mantine. Decisión de G-STACK para este slice registrada el 2026-10-15. |

## 4. Dependencias y Definition of Ready

- Dependencias de comportamiento/flujo: [F-023](F-023-calcular-resumen-envio.md), [F-024](F-024-validar-aplicar-cupon-promocion.md).
- Gates: I-01, I-02, I-06, G-CHECKOUT; consultar [registro](../DECISIONES-Y-BLOQUEOS.md). G-STACK para Checkout está resuelto; el UI kit global de otras familias sigue abierto. Para la UI, usar V-010–V-014 del [canvas Checkout en Figma](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=1-5&p=f&t=PXeKrikbDjSdUQ5l-0) como referencia de G-SHELL. Revisar los frames desktop/mobile durante la aceptación visual.
- Pendientes específicos: I-01; I-02 para activar creación posterior; recuperación PREPARED al recargar pendiente.
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
Las tareas y el estado real viven únicamente en [seguimiento](../seguimiento/F-025-simular-pago-revalidar-stock.md); aquí no se duplica un tablero.

## 6. Criterios de terminado y pruebas

- sin checkbox no preparación.
- doble click único intento.
- reintento misma clave.
- PREPARED no pantalla pedido exitoso.
- Cada estado documentado tiene caso verificable y foco/recuperación correctos.
- Seguridad: Fingerprint/clave reutilizada, replay de POST y concurrencia; no tarjeta/CVV ni reserva.
- DB si aplica: identidad/constraints/versiones/transacción y rollback probados sin persistencia prohibida.
- Evidencias sanitizadas y revisión por persona distinta, según [DoD general](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-done-y-evidencia).
- Cuando se exige homologación, prueba real aprobada además de fixture. Si bloqueada, funcionalidad no se declara completa.

## 7. Riesgos y recuperación

READY → PREPARING → PREPARED | NEEDS_REVIEW | NO_STOCK | ERROR; respuesta incierta consulta operación cuando hay ID, nunca marca pago aprobado por timeout o por `PREPARED`.

No reintentos ilimitados ni datos locales como fuente externa de verdad. Campos, endpoints y política que sigan abiertos permanecen explícitos; resolver/actualizar spec de origen antes de modificar código. Riesgo de capacidad/fecha se revisa cada sprint sin retirar esta funcionalidad ocultamente.
