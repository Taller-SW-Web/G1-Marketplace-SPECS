# Plan de implementación — F-016 Agregar ítem al carrito

## 1. Metadatos y entradas

| Campo | Valor |
|---|---|
| ID / versión / estado | F-016 / 0.1.0 / En revisión |
| Objetivo académico | S02/H4, semanas 9–11; cierre sólo con gates y prueba en despliegue |
| Entrada SDD | [Funcional](../../SPECS/funcional/F-016-agregar-item-carrito.md), [UI](../../SPECS/ui/F-016-agregar-item-carrito.md), [API](../../SPECS/contrato-api/F-016-agregar-item-carrito.md), [React](../../SPECS/componentes-react/F-016-agregar-item-carrito.md) |
| Ejecución y revisores | [Tareas de F-016](../seguimiento/F-016-agregar-item-carrito.md); responsable asignado por el PO: **Andres Morales**; revisor principal: **Leonidas Garcia**. [Matriz de bloques](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md). Estimación base en la matriz; ejecución y evidencia pendientes. |
| Plan general / seguridad | [Semanas 7–16](../PLAN-IMPLEMENTACION.md), [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md) |

## Entrega de H4 y cierre objetivo

**Objetivo de cierre H4.** Implementar alta FE+BE por SKU elegible con precio/cantidad G6, BD propia, cookie invitado o titular G7; probar duplicado/rechazo/carrera y resolver G-ADD/G-DB/G-QUANTITY.

**Cierre base:** S02/H4, semanas 9–11; cierre sólo con gates y prueba en despliegue. El PO establece disponibilidad sin restricción horaria; todo el trabajo propio definido se implementa y prueba en H4. Los límites son contrato, entorno, datos, autorizaciones y calidad. [Inventario H4](../ALCANCE-H4-PRODUCTOS-SEGURIDAD.md) y [S02](../iteraciones/S02-semanas-09-11.md). Registrar diseñado, implementado con datos de prueba, integrado con otro módulo y probado en el despliegue por separado; no inventar contrato ni liberar gates por planificar.

## 2. Objetivo y límites

Entregar agregar ítem al carrito conforme comportamiento/UI/API/React, no una pantalla aislada.
No leer cookie HttpOnly ni enviar customerId. Timeout de POST no se reintenta ciegamente: GET cart y decisión explícita tras comprobar resultado; API no ofrece idempotencia de adición.

## 3. Decisiones técnicas

| Área | Trabajo / decisión |
|---|---|
| Frontend / render | `AddToCartAction`, `AddedToCartFeedback`; hook `useAddCartItem`; arquitectura transversal React. |
| Backend / adaptador | Crear/recuperar carrito seguro y sumar SKU en transacción con Cart.version; revalidar elegibilidad/precio/stock sin reserva. |
| Persistencia | Cart/CartItem. Siempre modelo lógico vigente, nunca el esquema histórico de dos tablas. |
| Remoto / caché | ['cart','current',sessionScope]; mutation reemplaza snapshot confirmado/invalida cart; cualquier cambio invalida quote/preparación. |
| Seguridad específica | Cookie HttpOnly/Secure/SameSite, CSRF, propietario carrito no manipulable y suma concurrente segura. |
| UI Kit | DS-001 v0.2.0; G-STACK pendiente, no fijar versiones no verificadas. |

## 4. Dependencias y Definition of Ready

- Dependencias de comportamiento/flujo: [F-012](F-012-precio-oferta-descuento.md), [F-013](F-013-seleccion-atributos-variante.md), [F-014](F-014-consultar-disponibilidad-stock.md).
- Gates: I-01, G-SKU, G-ADD; consultar [registro](../DECISIONES-Y-BLOQUEOS.md). G-STACK/G-SHELL para interfaz compartida aplicable.
- Pendientes específicos: I-01; semántica 409 STOCK_LIMIT_REACHED contradice no mutación: sólo snapshot devuelto es verdad.
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
Las tareas y el estado real viven únicamente en [seguimiento](../seguimiento/F-016-agregar-item-carrito.md); aquí no se duplica un tablero.

## 6. Criterios de terminado y pruebas

- doble click un POST.
- cookie anónima no JS.
- 409 renderiza carrito confirmado.
- timeout no suma automáticamente.
- Cada estado documentado tiene caso verificable y foco/recuperación correctos.
- Seguridad: Cookie HttpOnly/Secure/SameSite, CSRF, propietario carrito no manipulable y suma concurrente segura.
- DB si aplica: identidad/constraints/versiones/transacción y rollback probados sin persistencia prohibida.
- Evidencias sanitizadas y revisión por persona distinta, según [DoD general](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-done-y-evidencia).
- Cuando se exige homologación, prueba real aprobada además de fixture. Si bloqueada, funcionalidad no se declara completa.

## 7. Riesgos y recuperación

UNSELECTED | UNAVAILABLE | READY → ADDING → ADDED | ADJUSTED | ERROR; error de disponibilidad mantiene opción de reconsultar.

No reintentos ilimitados ni datos locales como fuente externa de verdad. Campos, endpoints y política que sigan abiertos permanecen explícitos; resolver/actualizar spec de origen antes de modificar código. Los riesgos de contrato, entorno y calidad se revisan por operación, sin retirar esta funcionalidad por disponibilidad horaria.
