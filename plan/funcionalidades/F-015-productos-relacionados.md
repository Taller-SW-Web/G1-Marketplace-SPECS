# Plan de implementación — F-015 Visualizar productos relacionados

## 1. Metadatos y entradas

| Campo | Valor |
|---|---|
| ID / versión / estado | F-015 / 0.1.0 / En revisión |
| Objetivo académico | Sprint 2, semanas 8–9 |
| Entrada SDD | [Funcional](../../SPECS/funcional/F-015-productos-relacionados.md), [UI](../../SPECS/ui/F-015-productos-relacionados.md), [API](../../SPECS/contrato-api/F-015-productos-relacionados.md), [React](../../SPECS/componentes-react/F-015-productos-relacionados.md) |
| Ejecución y revisores | [Tareas de F-015](../seguimiento/F-015-productos-relacionados.md), propuesta según roles actuales |
| Plan general / seguridad | [Semanas 6–15](../PLAN-IMPLEMENTACION.md), [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md) |

## 2. Objetivo y límites

Entregar visualizar productos relacionados conforme comportamiento/UI/API/React, no una pantalla aislada.
BFF ya ordena/filtra/enriquece; frontend conserva orden y abre slug propio, ficha reconsulta comerciales.

## 3. Decisiones técnicas

| Área | Trabajo / decisión |
|---|---|
| Frontend / render | `RelatedProducts`; hook `useRelatedProducts`; arquitectura transversal React. |
| Backend / adaptador | Enriquecer hasta8 recomendaciones, deduplicar y degradar falla a sección omitida, sin bloquear ficha. |
| Persistencia | Sin persistencia de dominio local. Siempre modelo lógico vigente, nunca el esquema histórico de dos tablas. |
| Remoto / caché | ['catalog','recommendations',slug]; carga independiente y degradable. |
| Seguridad específica | URL/slug de recomendaciones seguros, no productos privados. |
| UI Kit | DS-001 v0.2.0; G-STACK pendiente, no fijar versiones no verificadas. |

## 4. Dependencias y Definition of Ready

- Dependencias de comportamiento/flujo: [F-011](F-011-detalle-producto.md).
- Gates: I-01; consultar [registro](../DECISIONES-Y-BLOQUEOS.md). G-STACK/G-SHELL para interfaz compartida aplicable.
- Pendientes específicos: I-01; etiqueta Cross-sell/Upsell pendiente no imponer jerga.
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
Las tareas y el estado real viven únicamente en [seguimiento](../seguimiento/F-015-productos-relacionados.md); aquí no se duplica un tablero.

## 6. Criterios de terminado y pruebas

- vacío omite título.
- error no afecta producto.
- precio null no cero.
- cada card navega SKU no requerido.
- Cada estado documentado tiene caso verificable y foco/recuperación correctos.
- Seguridad: URL/slug de recomendaciones seguros, no productos privados.
- DB si aplica: identidad/constraints/versiones/transacción y rollback probados sin persistencia prohibida.
- Evidencias sanitizadas y revisión por persona distinta, según [DoD general](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-y-definition-of-done).
- Cuando se exige homologación, prueba real aprobada además de fixture. Si bloqueada, funcionalidad no se declara completa.

## 7. Riesgos y recuperación

LOADING → READY | OMITTED; vacío o error técnico omite título y región completos.

No reintentos ilimitados ni datos locales como fuente externa de verdad. Campos, endpoints y política que sigan abiertos permanecen explícitos; resolver/actualizar spec de origen antes de modificar código. Riesgo de capacidad/fecha se revisa cada sprint sin retirar esta funcionalidad ocultamente.

