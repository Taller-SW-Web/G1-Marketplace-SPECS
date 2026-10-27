# Plan de implementación — F-029 Filtrar el historial de pedidos

## 1. Metadatos y entradas

| Campo | Valor |
|---|---|
| ID / versión / estado | F-029 / 0.1.0 / En revisión |
| Objetivo académico | S05/H6, semanas 15–16; implementación propia y pruebas con dobles en H4 |
| Entrada SDD | [Funcional](../../SPECS/funcional/F-029-filtrar-historial-pedidos.md), [UI](../../SPECS/ui/F-029-filtrar-historial-pedidos.md), [API](../../SPECS/contrato-api/F-029-filtrar-historial-pedidos.md), [React](../../SPECS/componentes-react/F-029-filtrar-historial-pedidos.md) |
| Ejecución y revisores | [Tareas de F-029](../seguimiento/F-029-filtrar-historial-pedidos.md); responsable asignado por el PO: **Fernando Saire**; revisor principal: **Jim Segovia**. [Matriz de bloques](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md). Estimación base en la matriz; ejecución y evidencia pendientes. |
| Plan general / seguridad | [Semanas 7–16](../PLAN-IMPLEMENTACION.md), [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md) |

## Entrega de H4 y cierre objetivo

**Implementación propia y pruebas en H4; integración completa posterior.** Implementar filtros/estado UI y lógica G1 con dobles; aislar el adaptador de la brecha de fechas de /me G5. No inventar endpoint ni declarar filtro REAL sin contrato; cierre S05.

**Cierre base:** S05/H6, semanas 15–16; implementación propia y pruebas con dobles en H4. El PO establece disponibilidad sin restricción horaria; todo el trabajo propio definido se implementa y prueba en H4. Los límites son contrato, entorno, datos, autorizaciones y calidad. [Inventario H4](../ALCANCE-H4-PRODUCTOS-SEGURIDAD.md) y [S02](../iteraciones/S02-semanas-09-11.md). Registrar diseñado, implementado con datos de prueba, integrado con otro módulo y probado en el despliegue por separado; no inventar contrato ni liberar gates por planificar.

## 2. Objetivo y límites

Entregar filtrar el historial de pedidos conforme comportamiento/UI/API/React, no una pantalla aislada.
Aplicar page0, mantiene sesión; Cancelar panel no aplica; 400 vincula ambos campos de rango.

## 3. Decisiones técnicas

| Área | Trabajo / decisión |
|---|---|
| Frontend / render | `OrdersFilterForm`, `OrdersFilterSummary`; hook `useOrderFilters`; arquitectura transversal React. |
| Backend / adaptador | Mapear estado/fechas ISO / rango <= 1 año a historial propio con reinicio página y validación antes de proveedor. |
| Persistencia | Sin persistencia de dominio local. Siempre modelo lógico vigente, nunca el esquema histórico de dos tablas. |
| Remoto / caché | Misma query historial, criterios completos en clave. |
| Seguridad específica | Filtros no alteran titular, fechas abusivas no proveedor. |
| UI Kit | DS-001 v0.2.0; G-STACK pendiente, no fijar versiones no verificadas. |

## 4. Dependencias y Definition of Ready

- Dependencias de comportamiento/flujo: [F-028](F-028-historial-pedidos.md).
- Gates: I-03; consultar [registro](../DECISIONES-Y-BLOQUEOS.md). G-STACK/G-SHELL para interfaz compartida aplicable.
- Pendientes específicos: I-03; semántica inclusiva de from/to a confirmar.
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
Las tareas y el estado real viven únicamente en [seguimiento](../seguimiento/F-029-filtrar-historial-pedidos.md); aquí no se duplica un tablero.

## 6. Criterios de terminado y pruebas

- rango invertido no consulta.
- más un año no consulta.
- cero resultados permite limpiar.
- día local no cambia al serializar.
- Cada estado documentado tiene caso verificable y foco/recuperación correctos.
- Seguridad: Filtros no alteran titular, fechas abusivas no proveedor.
- DB si aplica: identidad/constraints/versiones/transacción y rollback probados sin persistencia prohibida.
- Evidencias sanitizadas y revisión por persona distinta, según [DoD general](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-done-y-evidencia).
- Cuando se exige homologación, prueba real aprobada además de fixture. Si bloqueada, funcionalidad no se declara completa.

## 7. Riesgos y recuperación

EDITING → INVALID | APPLYING → FILTERED | NO_MATCHES | ERROR; limpiar reinicia página y ámbito sigue privado.

No reintentos ilimitados ni datos locales como fuente externa de verdad. Campos, endpoints y política que sigan abiertos permanecen explícitos; resolver/actualizar spec de origen antes de modificar código. Los riesgos de contrato, entorno y calidad se revisan por operación, sin retirar esta funcionalidad por disponibilidad horaria.
