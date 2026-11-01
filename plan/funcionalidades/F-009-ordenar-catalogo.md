# Plan de implementación — F-009 Ordenar resultados

## 1. Metadatos y entradas

| Campo | Valor |
|---|---|
| ID / versión / estado | F-009 / 0.1.0 / En revisión |
| Objetivo académico | S02/H4, semanas 9–11; cierre sólo con gates y prueba en despliegue |
| Entrada SDD | [Funcional](../../SPECS/funcional/F-009-ordenar-catalogo.md), [UI](../../SPECS/ui/F-009-ordenar-catalogo.md), [API](../../SPECS/contrato-api/F-009-ordenar-catalogo.md), [React](../../SPECS/componentes-react/F-009-ordenar-catalogo.md) |
| Ejecución y revisores | [Tareas de F-009](../seguimiento/F-009-ordenar-catalogo.md); responsable asignado por el PO: **Giuliano Macchiavello**; revisor principal: **Sebastian Malca**. [Matriz de bloques](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md). Estimación base en la matriz; ejecución y evidencia pendientes. |
| Plan general / seguridad | [Semanas 7–16](../PLAN-IMPLEMENTACION.md), [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md) |

## Entrega de H4 y cierre objetivo

**Objetivo de cierre H4.** Integrar orden NAME_ASC/DESC→NOMBRE_ASC/DESC y estabilidad entre páginas; otros criterios permanecen en G-SORT hasta homologación.

**Cierre base:** S02/H4, semanas 9–11; cierre sólo con gates y prueba en despliegue. El PO establece disponibilidad sin restricción horaria; todo el trabajo propio definido se implementa y prueba en H4. Los límites son contrato, entorno, datos, autorizaciones y calidad. [Inventario H4](../ALCANCE-H4-PRODUCTOS-SEGURIDAD.md) y [S02](../iteraciones/S02-semanas-09-11.md). Registrar diseñado, implementado con datos de prueba, integrado con otro módulo y probado en el despliegue por separado; no inventar contrato ni liberar gates por planificar.

## 2. Objetivo y límites

Entregar ordenar resultados conforme comportamiento/UI/API/React, no una pantalla aislada.
Cambiar sort reinicia page=0 y conserva q/filtros; backend mantiene orden estable. Para el contrato actual sólo se habilita orden por nombre (`NAME_ASC/DESC` → `NOMBRE_ASC/DESC`); precio, novedad y relevancia requieren homologación posterior.

## 3. Decisiones técnicas

| Área | Trabajo / decisión |
|---|---|
| Frontend / render | `CatalogSortSelect`; hook `useCatalogSort`; arquitectura transversal React. |
| Backend / adaptador | Validar enum sort y delegar orden estable al dueño sin ordenar una página incompleta. |
| Persistencia | Sin persistencia de dominio local. Siempre modelo lógico vigente, nunca el esquema histórico de dos tablas. |
| Remoto / caché | Misma query de catálogo; sort en clave y request. |
| Seguridad específica | Enum desconocido/inyección no llega proveedor. |
| UI Kit | DS-001 v0.2.0; G-STACK pendiente, no fijar versiones no verificadas. |

## 4. Dependencias y Definition of Ready

- Dependencias de comportamiento/flujo: [F-007](F-007-buscar-productos-texto.md).
- Gates: I-01; consultar [registro](../DECISIONES-Y-BLOQUEOS.md). G-STACK/G-SHELL para interfaz compartida aplicable.
- Pendientes específicos: I-01; definición del orden sin q.
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
Las tareas y el estado real viven únicamente en [seguimiento](../seguimiento/F-009-ordenar-catalogo.md); aquí no se duplica un tablero.

## 6. Criterios de terminado y pruebas

- todos los enums permitidos enviados.
- sort inválido no llega externo.
- page se reinicia.
- no ordena sólo tarjetas de página actual.
- Cada estado documentado tiene caso verificable y foco/recuperación correctos.
- Seguridad: Enum desconocido/inyección no llega proveedor.
- DB si aplica: identidad/constraints/versiones/transacción y rollback probados sin persistencia prohibida.
- Evidencias sanitizadas y revisión por persona distinta, según [DoD general](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-done-y-evidencia).
- Cuando se exige homologación, prueba real aprobada además de fixture. Si bloqueada, funcionalidad no se declara completa.

## 7. Riesgos y recuperación

READY → UPDATING → READY | ERROR; enum desconocido de URL se normaliza a opción segura definida.

No reintentos ilimitados ni datos locales como fuente externa de verdad. Campos, endpoints y política que sigan abiertos permanecen explícitos; resolver/actualizar spec de origen antes de modificar código. Los riesgos de contrato, entorno y calidad se revisan por operación, sin retirar esta funcionalidad por disponibilidad horaria.
