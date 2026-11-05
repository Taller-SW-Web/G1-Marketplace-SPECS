# Plan de implementación — F-024 Validar y aplicar cupón o promoción

## 1. Metadatos y entradas

| Campo | Valor |
|---|---|
| ID / versión / estado | F-024 / 0.1.0 / En revisión |
| Objetivo académico | S03, semanas 12–13; implementación y pruebas propias comienzan en H4 |
| Entrada SDD | [Funcional](../../SPECS/funcional/F-024-validar-aplicar-cupon-promocion.md), [UI](../../SPECS/ui/F-024-validar-aplicar-cupon-promocion.md), [API](../../SPECS/contrato-api/F-024-validar-aplicar-cupon-promocion.md), [React](../../SPECS/componentes-react/F-024-validar-aplicar-cupon-promocion.md) |
| Ejecución y revisores | [Tareas de F-024](../seguimiento/F-024-validar-aplicar-cupon-promocion.md); responsable asignado por el PO: **Leonidas Garcia**; revisor principal: **Diego Espinoza**. [Matriz de bloques](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md). Estimación base en la matriz; ejecución y evidencia pendientes. |
| Plan general / seguridad | [Semanas 7–16](../PLAN-IMPLEMENTACION.md), [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md) |

## Entrega de H4 y cierre objetivo

**Implementación propia y pruebas en H4; integración completa posterior.** Implementar cupón/promoción FE+BE, evaluación/validación G6 y errores/timeout; consumo/restauración sólo por G5/G6 y contrato G-BENEFIT/G-MONEY/G-COUPON-RELEASE. Cierre completo S03.

**Cierre base:** S03, semanas 12–13; implementación y pruebas propias comienzan en H4. El PO establece disponibilidad sin restricción horaria; todo el trabajo propio definido se implementa y prueba en H4. Los límites son contrato, entorno, datos, autorizaciones y calidad. [Inventario H4](../ALCANCE-H4-PRODUCTOS-SEGURIDAD.md) y [S02](../iteraciones/S02-semanas-09-11.md). Registrar diseñado, implementado con datos de prueba, integrado con otro módulo y probado en el despliegue por separado; no inventar contrato ni liberar gates por planificar.

**Cierre H4 anticipado por contratos:** esta F forma parte de la extensión de cinco funciones que puede llevar H4 de 25 a 30. Si todas las dependencias intermodulares y DoD se prueban antes del corte, aceptar H4 y descontar su cierre base posterior; el tiempo del equipo no limita esa decisión.

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
| UI Kit | Checkout: componentes propios existentes (`Button`, `TextField`) y tokens DS-001; no instalar Mantine. Decisión de G-STACK para este slice registrada el 2026-10-15. |

## 4. Dependencias y Definition of Ready

- Dependencias de comportamiento/flujo: [F-023](F-023-calcular-resumen-envio.md).
- Gates: I-01, G-BENEFIT; consultar [registro](../DECISIONES-Y-BLOQUEOS.md). G-STACK para Checkout está resuelto; el UI kit global de otras familias sigue abierto. Para la UI, usar V-010–V-014 del [canvas Checkout en Figma](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=1-5&p=f&t=PXeKrikbDjSdUQ5l-0) como referencia de G-SHELL. Revisar los frames desktop/mobile durante la aceptación visual.
- Pendientes específicos: I-01, OPEN-11/12 y V-011-OPEN-04.
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
Las tareas y el estado real viven únicamente en [seguimiento](../seguimiento/F-024-validar-aplicar-cupon-promocion.md); aquí no se duplica un tablero.

## 6. Criterios de terminado y pruebas

- aplicar no acumula descuento manual.
- 422 no pierde quote válida.
- quitar recalcula y no consume.
- respuesta vieja no reemplaza última quote.
- Cada estado documentado tiene caso verificable y foco/recuperación correctos.
- Seguridad: Quote ajena/vencida, cupón no logs, no consumo en validación ni fraude por total del cliente.
- DB si aplica: identidad/constraints/versiones/transacción y rollback probados sin persistencia prohibida.
- Evidencias sanitizadas y revisión por persona distinta, según [DoD general](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-done-y-evidencia).
- Cuando se exige homologación, prueba real aprobada además de fixture. Si bloqueada, funcionalidad no se declara completa.

## 7. Riesgos y recuperación

NO_COUPON → VALIDATING → APPLIED | NOT_APPLICABLE | INVALID | QUOTE_EXPIRED | ERROR; quitar requiere cotización sin cupón.

No reintentos ilimitados ni datos locales como fuente externa de verdad. Campos, endpoints y política que sigan abiertos permanecen explícitos; resolver/actualizar spec de origen antes de modificar código. Los riesgos de contrato, entorno y calidad se revisan por operación, sin retirar esta funcionalidad por disponibilidad horaria.
