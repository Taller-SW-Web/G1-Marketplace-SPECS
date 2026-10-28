# Plan de implementación — F-013 Seleccionar atributos y variante del producto

## 1. Metadatos y entradas

| Campo | Valor |
|---|---|
| ID / versión / estado | F-013 / 0.1.0 / En revisión |
| Objetivo académico | S02/H4, semanas 9–11; cierre sólo con gates y prueba en despliegue |
| Entrada SDD | [Funcional](../../SPECS/funcional/F-013-seleccion-atributos-variante.md), [UI](../../SPECS/ui/F-013-seleccion-atributos-variante.md), [API](../../SPECS/contrato-api/F-013-seleccion-atributos-variante.md), [React](../../SPECS/componentes-react/F-013-seleccion-atributos-variante.md) |
| Ejecución y revisores | [Tareas de F-013](../seguimiento/F-013-seleccion-atributos-variante.md); responsable asignado por el PO: **Sebastian Malca**; revisor principal: **Giuliano Macchiavello**. [Matriz de bloques](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md). Estimación base en la matriz; ejecución y evidencia pendientes. |
| Plan general / seguridad | [Semanas 7–16](../PLAN-IMPLEMENTACION.md), [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md) |

## Entrega de H4 y cierre objetivo

**Objetivo de cierre H4.** Integrar SKU simple sku_base y variantes elegibles variant_id/sku; validar selección inválida y handoff F-016, sin convertir productId en SKU.

**Cierre base:** S02/H4, semanas 9–11; cierre sólo con gates y prueba en despliegue. El PO establece disponibilidad sin restricción horaria; todo el trabajo propio definido se implementa y prueba en H4. Los límites son contrato, entorno, datos, autorizaciones y calidad. [Inventario H4](../ALCANCE-H4-PRODUCTOS-SEGURIDAD.md) y [S02](../iteraciones/S02-semanas-09-11.md). Registrar diseñado, implementado con datos de prueba, integrado con otro módulo y probado en el despliegue por separado; no inventar contrato ni liberar gates por planificar.

## 2. Objetivo y límites

Entregar seleccionar atributos y variante del producto conforme comportamiento/UI/API/React, no una pantalla aislada.
Propagar onResolved sólo con SKU real; imagen opcional falla con respaldo sin anular selección. hasVariants=false necesita SKU vendible en DTO homologado.

## 3. Decisiones técnicas

| Área | Trabajo / decisión |
|---|---|
| Frontend / render | `VariantSelector`, `SelectionSummary`; hook `useProductVariants`; arquitectura transversal React. |
| Backend / adaptador | Proyectar atributos/variantes activas, validar SKU único y definir representación del SKU simple ausente en ejemplo actual. |
| Persistencia | Sin persistencia de dominio local. Siempre modelo lógico vigente, nunca el esquema histórico de dos tablas. |
| Remoto / caché | ['catalog','variants',slug]; precio/stock cambian por SKU sólo cuando existe selección válida. |
| Seguridad específica | Variante inactiva/combinación duplicada / SKU ajeno, sin confiar selección del cliente. |
| UI Kit | DS-001 v0.2.0; G-STACK pendiente, no fijar versiones no verificadas. |

## 4. Dependencias y Definition of Ready

- Dependencias de comportamiento/flujo: [F-011](F-011-detalle-producto.md).
- Gates: I-01, G-SKU; consultar [registro](../DECISIONES-Y-BLOQUEOS.md). G-STACK/G-SHELL para interfaz compartida aplicable.
- Pendientes específicos: I-01; cerrar shape de SKU simple antes de implementarlo.
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
Las tareas y el estado real viven únicamente en [seguimiento](../seguimiento/F-013-seleccion-atributos-variante.md); aquí no se duplica un tablero.

## 6. Criterios de terminado y pruebas

- combinación inválida elimina SKU.
- agotado no equivale inexistente.
- simple oculta selector.
- cambio consulta precio/stock nuevos.
- Cada estado documentado tiene caso verificable y foco/recuperación correctos.
- Seguridad: Variante inactiva/combinación duplicada / SKU ajeno, sin confiar selección del cliente.
- DB si aplica: identidad/constraints/versiones/transacción y rollback probados sin persistencia prohibida.
- Evidencias sanitizadas y revisión por persona distinta, según [DoD general](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-done-y-evidencia).
- Cuando se exige homologación, prueba real aprobada además de fixture. Si bloqueada, funcionalidad no se declara completa.

## 7. Riesgos y recuperación

LOADING → SIMPLE | INCOMPLETE | VALID | INVALID_COMBINATION | UNAVAILABLE | ERROR; cambio incompatible elimina SKU anterior.

No reintentos ilimitados ni datos locales como fuente externa de verdad. Campos, endpoints y política que sigan abiertos permanecen explícitos; resolver/actualizar spec de origen antes de modificar código. Los riesgos de contrato, entorno y calidad se revisan por operación, sin retirar esta funcionalidad por disponibilidad horaria.
