# Plan de implementación — F-007 Buscar productos por texto

## 1. Metadatos y entradas

| Campo | Valor |
|---|---|
| ID / versión / estado | F-007 / 0.1.0 / En revisión |
| Objetivo académico | S02/H4, semanas 9–11; cierre sólo con gates y prueba en despliegue |
| Entrada SDD | [Funcional](../../SPECS/funcional/F-007-buscar-productos-texto.md), [UI](../../SPECS/ui/F-007-buscar-productos-texto.md), [API](../../SPECS/contrato-api/F-007-buscar-productos-texto.md), [React](../../SPECS/componentes-react/F-007-buscar-productos-texto.md) |
| Ejecución y revisores | [Tareas de F-007](../seguimiento/F-007-buscar-productos-texto.md); responsable asignado por el PO: **Giuliano Macchiavello**; revisor principal: **Sebastian Malca**. [Matriz de bloques](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md). Estimación base en la matriz; ejecución y evidencia pendientes. |
| Plan general / seguridad | [Semanas 7–16](../PLAN-IMPLEMENTACION.md), [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md) |

## Entrega de H4 y cierre objetivo

**Objetivo de cierre H4.** Integrar búsqueda REAL por texto/canal con producto vendible, vacío/error/timeout, parámetros y evidencia desde la web desplegada.

**Cierre base:** S02/H4, semanas 9–11; cierre sólo con gates y prueba en despliegue. El PO establece disponibilidad sin restricción horaria; todo el trabajo propio definido se implementa y prueba en H4. Los límites son contrato, entorno, datos, autorizaciones y calidad. [Inventario H4](../ALCANCE-H4-PRODUCTOS-SEGURIDAD.md) y [S02](../iteraciones/S02-semanas-09-11.md). Registrar diseñado, implementado con datos de prueba, integrado con otro módulo y probado en el despliegue por separado; no inventar contrato ni liberar gates por planificar.

## 2. Objetivo y límites

Entregar buscar productos por texto conforme comportamiento/UI/API/React, no una pantalla aislada.
Aplicar q reinicia page=0, conserva filtros/orden compatibles; cancelar respuesta anterior evita sobrescribir búsqueda nueva.

## 3. Decisiones técnicas

| Área | Trabajo / decisión |
|---|---|
| Frontend / render | `SearchBox`, `SearchResultsHeading`; hook `useCatalogSearch`; arquitectura transversal React. |
| Backend / adaptador | Validar q de 2–120 caracteres y adaptar búsqueda paginada pública, proteger query de logs identificables. |
| Persistencia | Sin persistencia de dominio local. Siempre modelo lógico vigente, nunca el esquema histórico de dos tablas. |
| Remoto / caché | ['catalog','products',{q,filters,sort,page,pageSize}]; URL es fuente de criterios aplicados. |
| Seguridad específica | Entradas XSS/inyección y longitudes, consulta pública sin datos privados. |
| UI Kit | DS-001 v0.2.0; G-STACK pendiente, no fijar versiones no verificadas. |

## 4. Dependencias y Definition of Ready

- Dependencias de comportamiento/flujo: [F-006](F-006-inicio-categorias-destacados.md).
- Gates: I-01; consultar [registro](../DECISIONES-Y-BLOQUEOS.md). G-STACK/G-SHELL para interfaz compartida aplicable.
- Pendientes específicos: I-01 y semántica de búsqueda Catálogo.
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
Las tareas y el estado real viven únicamente en [seguimiento](../seguimiento/F-007-buscar-productos-texto.md); aquí no se duplica un tablero.

## 6. Criterios de terminado y pruebas

- 1 y 121 caracteres no consultan.
- query vacía vuelve catálogo.
- respuesta lenta anterior no reemplaza nueva.
- cero resultados conserva q y limpiar.
- Cada estado documentado tiene caso verificable y foco/recuperación correctos.
- Seguridad: Entradas XSS/inyección y longitudes, consulta pública sin datos privados.
- DB si aplica: identidad/constraints/versiones/transacción y rollback probados sin persistencia prohibida.
- Evidencias sanitizadas y revisión por persona distinta, según [DoD general](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-done-y-evidencia).
- Cuando se exige homologación, prueba real aprobada además de fixture. Si bloqueada, funcionalidad no se declara completa.

## 7. Riesgos y recuperación

DRAFT → VALIDATING → LOADING → RESULTS | ZERO_RESULTS | ERROR; vacío elimina q; inválida no consulta.

No reintentos ilimitados ni datos locales como fuente externa de verdad. Campos, endpoints y política que sigan abiertos permanecen explícitos; resolver/actualizar spec de origen antes de modificar código. Los riesgos de contrato, entorno y calidad se revisan por operación, sin retirar esta funcionalidad por disponibilidad horaria.
