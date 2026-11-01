# Plan de implementación — F-012 Visualizar precio, oferta y descuento vigente

## 1. Metadatos y entradas

| Campo | Valor |
|---|---|
| ID / versión / estado | F-012 / 0.1.0 / En revisión |
| Objetivo académico | S02/H4, semanas 9–11; cierre sólo con gates y prueba en despliegue |
| Entrada SDD | [Funcional](../../SPECS/funcional/F-012-precio-oferta-descuento.md), [UI](../../SPECS/ui/F-012-precio-oferta-descuento.md), [API](../../SPECS/contrato-api/F-012-precio-oferta-descuento.md), [React](../../SPECS/componentes-react/F-012-precio-oferta-descuento.md) |
| Ejecución y revisores | [Tareas de F-012](../seguimiento/F-012-precio-oferta-descuento.md); responsable asignado por el PO: **Sebastian Malca**; revisor principal: **Giuliano Macchiavello**. [Matriz de bloques](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md). Estimación base en la matriz; ejecución y evidencia pendientes. |
| Plan general / seguridad | [Semanas 7–16](../PLAN-IMPLEMENTACION.md), [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md) |

## Entrega de H4 y cierre objetivo

**Objetivo de cierre H4.** Integrar precio/oferta por SKU/canal con importe, moneda, vigencia y errores autoritativos G6; no calcular descuentos ni presentar oferta no publicada.

**Cierre base:** S02/H4, semanas 9–11; cierre sólo con gates y prueba en despliegue. El PO establece disponibilidad sin restricción horaria; todo el trabajo propio definido se implementa y prueba en H4. Los límites son contrato, entorno, datos, autorizaciones y calidad. [Inventario H4](../ALCANCE-H4-PRODUCTOS-SEGURIDAD.md) y [S02](../iteraciones/S02-semanas-09-11.md). Registrar diseñado, implementado con datos de prueba, integrado con otro módulo y probado en el despliegue por separado; no inventar contrato ni liberar gates por planificar.

## 2. Objetivo y límites

Entregar visualizar precio, oferta y descuento vigente conforme comportamiento/UI/API/React, no una pantalla aislada.
F-013 resuelve SKU; respuesta vieja no pisa selección nueva. Expiración invalida región y refresca según vigencia, no promete precio final.

## 3. Decisiones técnicas

| Área | Trabajo / decisión |
|---|---|
| Frontend / render | `ProductPriceRegion`, `PriceDisplay`; hook `useProductPrice`; arquitectura transversal React. |
| Backend / adaptador | Adaptar Pricing por SKU/canal/momento, validar vigencia y precio, limitar caché y derivar descuento de importes autoritativos. |
| Persistencia | Sin persistencia de dominio local. Siempre modelo lógico vigente, nunca el esquema histórico de dos tablas. |
| Remoto / caché | ['catalog','price',slug,sku]; deshabilitar query hasta SKU aplicable; freshness no supera validUntil. |
| Seguridad específica | SKU de otro producto, versión/vigencia inválida y caché sin costos internos. |
| UI Kit | DS-001 v0.2.0; G-STACK pendiente, no fijar versiones no verificadas. |

## 4. Dependencias y Definition of Ready

- Dependencias de comportamiento/flujo: [F-011](F-011-detalle-producto.md), [F-013](F-013-seleccion-atributos-variante.md).
- Gates: I-01; consultar [registro](../DECISIONES-Y-BLOQUEOS.md). G-STACK/G-SHELL para interfaz compartida aplicable.
- Pendientes específicos: I-01/Pricing; cache comercial no autoritativa.
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
Las tareas y el estado real viven únicamente en [seguimiento](../seguimiento/F-012-precio-oferta-descuento.md); aquí no se duplica un tablero.

## 6. Criterios de terminado y pruebas

- sin SKU no precio ajeno.
- sin oferta no 0%.
- caducidad retira badge y referencia juntos.
- error no oculta descripción.
- Cada estado documentado tiene caso verificable y foco/recuperación correctos.
- Seguridad: SKU de otro producto, versión/vigencia inválida y caché sin costos internos.
- DB si aplica: identidad/constraints/versiones/transacción y rollback probados sin persistencia prohibida.
- Evidencias sanitizadas y revisión por persona distinta, según [DoD general](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-done-y-evidencia).
- Cuando se exige homologación, prueba real aprobada además de fixture. Si bloqueada, funcionalidad no se declara completa.

## 7. Riesgos y recuperación

WAITING_FOR_VARIANT → LOADING → REGULAR | SALE | UNAVAILABLE; al cambiar SKU retirar importe previo.

No reintentos ilimitados ni datos locales como fuente externa de verdad. Campos, endpoints y política que sigan abiertos permanecen explícitos; resolver/actualizar spec de origen antes de modificar código. Los riesgos de contrato, entorno y calidad se revisan por operación, sin retirar esta funcionalidad por disponibilidad horaria.
