# Plan de implementación — F-026 Crear la orden en Ventas y Postventa

## 1. Metadatos y entradas

| Campo | Valor |
|---|---|
| ID / versión / estado | F-026 / 0.1.0 / En revisión |
| Objetivo académico | S03, semanas 12–13; implementación y pruebas propias comienzan en H4 |
| Entrada SDD | [Funcional](../../SPECS/funcional/F-026-crear-orden-ventas.md), [UI](../../SPECS/ui/F-026-crear-orden-ventas.md), [API](../../SPECS/contrato-api/F-026-crear-orden-ventas.md), [React](../../SPECS/componentes-react/F-026-crear-orden-ventas.md) |
| Ejecución y revisores | [Tareas de F-026](../seguimiento/F-026-crear-orden-ventas.md); responsable asignado por el PO: **Leonidas Garcia**; revisor principal: **Diego Espinoza**. [Matriz de bloques](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md). Estimación base en la matriz; ejecución y evidencia pendientes. |
| Plan general / seguridad | [Semanas 7–16](../PLAN-IMPLEMENTACION.md), [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md) |

## Entrega de H4 y cierre objetivo

**Implementación propia y pruebas en H4; integración completa posterior.** Implementar orquestación G1, payload/clave/fingerprint, persistencia permitida y recuperación idempotente; probar con dobles y con G5 al habilitarse. G5 crea/reserva/inicia simulador; cierre S03.

**Cierre base:** S03, semanas 12–13; implementación y pruebas propias comienzan en H4. El PO establece disponibilidad sin restricción horaria; todo el trabajo propio definido se implementa y prueba en H4. Los límites son contrato, entorno, datos, autorizaciones y calidad. [Inventario H4](../ALCANCE-H4-PRODUCTOS-SEGURIDAD.md) y [S02](../iteraciones/S02-semanas-09-11.md). Registrar diseñado, implementado con datos de prueba, integrado con otro módulo y probado en el despliegue por separado; no inventar contrato ni liberar gates por planificar.

**Cierre H4 anticipado por contratos:** esta F forma parte de la extensión de cinco funciones que puede llevar H4 de 25 a 30. Si todas las dependencias intermodulares y DoD se prueban antes del corte, aceptar H4 y descontar su cierre base posterior; el tiempo del equipo no limita esa decisión.

## 2. Objetivo y límites

Entregar crear la orden en ventas y postventa conforme comportamiento/UI/API/React, no una pantalla aislada.
POST BFF envía snapshot/dirección homologados a Ventas. `CREADO` permanece pendiente hasta la aptitud para pagar y la confirmación simulada autorizada por Ventas. 503 podría ser incierto: consultar operación original; no enviar una compra nueva.

## 3. Decisiones técnicas

| Área | Trabajo / decisión |
|---|---|
| Frontend / render | `OrderCreationForm`, `OrderSubmissionStatus`; hook `useCreateOrder`; arquitectura transversal React. |
| Backend / adaptador | Orquestar PREPARED→SUBMITTED (`CREADO`)→SUCCEEDED sólo con `PAGADO` verificable; Ventas idempotente, señal de aptitud, contrato simulado y recuperación incierta siguen bajo I-02. |
| Persistencia | CheckoutOperation. Siempre modelo lógico vigente, nunca el esquema histórico de dos tablas. |
| Remoto / caché | Invalidate operaciones/pedidos/cart después de SUCCEEDED; no reconstruir pedido a partir de carrito. |
| Seguridad específica | Idempotencia real con Ventas, operación/contacto manipulados y ownership; timeout no segundo pedido. |
| UI Kit | Checkout: componentes propios existentes (`Button`, `TextField`) y tokens DS-001; no instalar Mantine. Decisión de G-STACK para este slice registrada el 2026-10-15. |

## 4. Dependencias y Definition of Ready

- Dependencias de comportamiento/flujo: [F-025](F-025-simular-pago-revalidar-stock.md).
- Gates: I-01, I-02, G-CHECKOUT; consultar [registro](../DECISIONES-Y-BLOQUEOS.md). G-STACK para Checkout está resuelto; el UI kit global de otras familias sigue abierto. Para la UI, usar V-010–V-014 del [canvas Checkout en Figma](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=1-5&p=f&t=PXeKrikbDjSdUQ5l-0) como referencia de G-SHELL. Revisar los frames desktop/mobile durante la aceptación visual.
- Pendientes específicos: I-02 bloquea integración real; reglas contacto, idempotencia preparación/orden y recuperación abiertas.
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
Las tareas y el estado real viven únicamente en [seguimiento](../seguimiento/F-026-crear-orden-ventas.md); aquí no se duplica un tablero.

## 6. Criterios de terminado y pruebas

- doble click no dos pedidos.
- timeout no compra nueva.
- campos faltantes únicamente.
- 400 conserva datos válidos.
- contacto no persiste localmente.
- Cada estado documentado tiene caso verificable y foco/recuperación correctos.
- Seguridad: Idempotencia real con Ventas, operación/contacto manipulados y ownership; timeout no segundo pedido.
- DB si aplica: identidad/constraints/versiones/transacción y rollback probados sin persistencia prohibida.
- Evidencias sanitizadas y revisión por persona distinta, según [DoD general](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-done-y-evidencia).
- Cuando se exige homologación, prueba real aprobada además de fixture. Si bloqueada, funcionalidad no se declara completa.

## 7. Riesgos y recuperación

PREPARED → SUBMITTING → SUBMITTED (`CREADO`) | FIELD_ERROR | FAILED; SUBMITTED → VERIFYING → SUCCEEDED sólo con `PAGADO` | SUBMITTED | FAILED.

No reintentos ilimitados ni datos locales como fuente externa de verdad. Campos, endpoints y política que sigan abiertos permanecen explícitos; resolver/actualizar spec de origen antes de modificar código. Los riesgos de contrato, entorno y calidad se revisan por operación, sin retirar esta funcionalidad por disponibilidad horaria.
