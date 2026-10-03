# Plan de implementación — F-008 Filtrar catálogo

## 1. Metadatos y entradas

| Campo | Valor |
|---|---|
| ID / versión / estado | F-008 / 0.1.0 / En revisión |
| Objetivo académico | Sprint 2, semanas 8–9 |
| Entrada SDD | [Funcional](../../SPECS/funcional/F-008-filtrar-catalogo.md), [UI](../../SPECS/ui/F-008-filtrar-catalogo.md), [API](../../SPECS/contrato-api/F-008-filtrar-catalogo.md), [React](../../SPECS/componentes-react/F-008-filtrar-catalogo.md) |
| Ejecución y revisores | [Tareas de F-008](../seguimiento/F-008-filtrar-catalogo.md), propuesta según roles actuales |
| Plan general / seguridad | [Semanas 6–15](../PLAN-IMPLEMENTACION.md), [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md) |

## 2. Objetivo y límites

Entregar filtrar catálogo conforme comportamiento/UI/API/React, no una pantalla aislada.
Aplicar reinicia page=0 y conserva q/sort; chips reflejan criterio aplicado, no borrador; error conserva draft.

## 3. Decisiones técnicas

| Área | Trabajo / decisión |
|---|---|
| Frontend / render | `CatalogFilters`, `ActiveFilterChips`; hook `useCatalogFilters`; arquitectura transversal React. |
| Backend / adaptador | Mapear IDs categoría/marca/rango PEN a proveedor, validar AND/min<=max y maestros autorizados. |
| Persistencia | Sin persistencia de dominio local. Siempre modelo lógico vigente, nunca el esquema histórico de dos tablas. |
| Remoto / caché | Maestros sólo publicados; contrato BFF de maestros pendiente, no crear endpoint. Criterios aplicados en URL y cache key completa. |
| Seguridad específica | IDs inválidos/rango negativo y manipulación URL, no filtros administrativos. |
| UI Kit | DS-001 v0.2.0; G-STACK pendiente, no fijar versiones no verificadas. |

## 4. Dependencias y Definition of Ready

- Dependencias de comportamiento/flujo: [F-007](F-007-buscar-productos-texto.md).
- Gates: I-01; consultar [registro](../DECISIONES-Y-BLOQUEOS.md). G-STACK/G-SHELL para interfaz compartida aplicable.
- Pendientes específicos: I-01; contrato de maestros/conteos de categoría y marca.
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
Las tareas y el estado real viven únicamente en [seguimiento](../seguimiento/F-008-filtrar-catalogo.md); aquí no se duplica un tablero.

## 6. Criterios de terminado y pruebas

- rango invertido no consulta.
- aplicar conserva búsqueda y orden.
- cancelar mobile no cambia filtros.
- Escape y restauración de foco.
- Cada estado documentado tiene caso verificable y foco/recuperación correctos.
- Seguridad: IDs inválidos/rango negativo y manipulación URL, no filtros administrativos.
- DB si aplica: identidad/constraints/versiones/transacción y rollback probados sin persistencia prohibida.
- Evidencias sanitizadas y revisión por persona distinta, según [DoD general](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-y-definition-of-done).
- Cuando se exige homologación, prueba real aprobada además de fixture. Si bloqueada, funcionalidad no se declara completa.

## 7. Riesgos y recuperación

EDITING → INVALID | APPLYING → APPLIED | EMPTY | ERROR; retirar chip actualiza criterios; limpiar sólo filtros.

No reintentos ilimitados ni datos locales como fuente externa de verdad. Campos, endpoints y política que sigan abiertos permanecen explícitos; resolver/actualizar spec de origen antes de modificar código. Riesgo de capacidad/fecha se revisa cada sprint sin retirar esta funcionalidad ocultamente.

