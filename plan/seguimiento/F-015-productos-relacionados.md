# Tareas y seguimiento — F-015 Visualizar productos relacionados

Versión 0.1.0 · Planificación inicial · F-015 no está implementada por estos documentos.

## Fuente y control

- [Plan F-015](../funcionalidades/F-015-productos-relacionados.md); [iteración S02/H4](../iteraciones/S02-semanas-09-11.md).
- [Funcional](../../SPECS/funcional/F-015-productos-relacionados.md), [UI](../../SPECS/ui/F-015-productos-relacionados.md), [API](../../SPECS/contrato-api/F-015-productos-relacionados.md), [React](../../SPECS/componentes-react/F-015-productos-relacionados.md).
- [Reglas del seguimiento](README.md), [pruebas/DevSecOps](../DEVSECOPS-Y-PRUEBAS.md), [gates](../DECISIONES-Y-BLOQUEOS.md).
- Responsable asignado por el PO: **Sebastian Malca**; revisor principal: **Giuliano Macchiavello** según la [matriz](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md). Estimación base fijada en la matriz; ejecución y evidencia pendientes. La semana objetivo es académica, no fecha de calendario.
- Mock y real se reportan por separado. QA local puede avanzar con fixtures; QA real requiere INT. Evidencia inicial pendiente, no pruebas ejecutadas.

## Corte planificado de H4

**Objetivo de cierre H4.** Implementar e integrar recomendaciones G6, enriquecimiento, máximo 8 tarjetas, dedupe/sin origen y degradación; cerrar sólo con request, grant y runtime autorizados y probados.

**Cierre base:** S02/H4, semanas 9–11; cierre sólo con gates y prueba en despliegue. Disponibilidad sin restricción horaria por decisión del PO. Las entregas «local» o «con dobles» son etapas del mismo TASK, no cierres de INT. DOC prepara desde specs y QA ejecuta casos propios antes de INT; el cierre completo conserva dependencias/DoD. [Alcance H4](../ALCANCE-H4-PRODUCTOS-SEGURIDAD.md). Los estados no cambian al replanificar.

| Nivel de evidencia | Registro del corte de esta F |
|---|---|
| Diseñado | Specs enlazadas arriba; añadir revisión del flujo/contrato/frame concreto de H4. Su existencia no acredita aprobación de todas las discrepancias |
| Implementado con datos de prueba | Enlazar commit FE/BE, fixture explícito, comando y resultado positivo/negativo. Recuperar evidencia del código existente antes de certificar cobertura completa |
| Integrado con otro módulo | Pendiente de evidencia por operación: proveedor/versión, entorno, auth, request/response REAL, negativos y traza; respetar gates de esta F |
| Probado en el despliegue | Pendiente: URLs/SHAs/run CI-CD y caso desde web/API desplegada con revisión independiente. No inferir de prueba local ni de provider directo |

La actualización del 19/10/2026 cambia planificación, no estados de ejecución ni aprobación de gates. Registrar aquí evidencia concreta a medida que exista, sin calificar todo el bloque por una sola prueba.

## Tablero

| ID | Área | Responsable | Revisor | Prioridad | Depende de | Semana objetivo | Estado |
|---|---|---|---|---|---|---|---|
| TASK-F015-FE-001 | Frontend | Sebastian Malca | Giuliano Macchiavello | P2 | TASK-TRANS-S01-OPS-001 | 9–10/H4 | Pendiente |
| TASK-F015-BE-001 | Backend | Sebastian Malca | Giuliano Macchiavello | P2 | TASK-TRANS-S01-OPS-001 | 9–10/H4 | Pendiente |
| TASK-F015-INT-001 | Integración | Sebastian Malca | Giuliano Macchiavello | P2 | TASK-F015-BE-001 + I-01 + TASK-F011-INT-001 | 11/H4 | Bloqueado |
| TASK-F015-QA-001 | QA funcional | Sebastian Malca | Giuliano Macchiavello | P2 | TASK-F015-FE-001 + TASK-F015-BE-001 | 11/H4 | Pendiente |
| TASK-F015-QA-002 | QA seguridad / DevSecOps | Sebastian Malca | Giuliano Macchiavello | P2 | TASK-F015-FE-001 + TASK-F015-BE-001 + TASK-TRANS-S02-OPS-002 | 11/H4 | Pendiente |
| TASK-F015-DOC-001 | Documentación | Sebastian Malca | Giuliano Macchiavello | P2 | H4 diseño/implementación: specs y pruebas locales; cierre completo: TASK-F015-INT-001 + TASK-F015-QA-001 + TASK-F015-QA-002 | 11/H4 | Pendiente |

Referente de BD: Sebastian Malca para este bloque, con revisión de Giuliano Macchiavello; Andres mantiene soporte transversal de migraciones. Ver [matriz](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md).

## Trabajo, Definition of Done y evidencia

### TASK-F015-FE-001

- **Trabajo:** Implementar RelatedProducts y todos los estados de React/UI.
- **Terminado cuando:** Props/eventos tipados, estado específico, sin requests internos navegador; desktop/mobile aplicables y casos de spec React cubiertos.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F015-BE-001

- **Trabajo:** Enriquecer hasta8 recomendaciones, deduplicar y degradar falla a sección omitida, sin bloquear ficha.
- **Terminado cuando:** DTO, validación, errores y ownership probados con fixtures; transacciones/versiones donde aplica. Adaptador real no activado si gate externo sigue abierto.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F015-INT-001

- **Trabajo:** Homologar y probar integración real y condiciones: I-01; no sólo fixture.
- **Terminado cuando:** Contrato/configuración y gates enlazados, pruebas positivas/negativas y timeout autorizadas pasan; evidencia distingue sandbox de mock.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Falta cierre documentado de I-01. Contrato/configuración y prueba enlazados antes de cambiar a En progreso.

### TASK-F015-QA-001

- **Trabajo:** Probar vacío omite título; error no afecta producto; precio null no cero; cada card navega SKU no requerido; incluir cada estado visual y transición documentada.
- **Terminado cuando:** Casos unitarios/componentes/API y E2E aplicables pasan con evidencias; pruebas mock y reales etiquetadas. Hallazgos corregidos/reprobados.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F015-QA-002

- **Trabajo:** URL/slug de recomendaciones seguros, no productos privados.
- **Terminado cuando:** Negativos de seguridad pasan en entorno propio/autorizado, scans SAST/SCA/secrets y DAST aplicable adjuntos sin secretos. Sin hallazgo crítico/alto explotable abierto.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F015-DOC-001

- **Trabajo:** Actualizar trazabilidad specs↔implementación↔pruebas, enlaces Figma y decisiones resueltas; documentar operación/errores relevantes.
- **Terminado cuando:** Fuentes vigentes coherentes, evidencias reales y revisión independiente; no marcar funcionalidad terminada con integración pendiente.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.


## Registro de revisión

| Fecha/semana | Cambios de estado | Evidencia / bloqueo / decisión | Revisó |
|---|---|---|---|
| Semana 6, preparación | Creación de tareas; sin ejecución | Specs y plan elaborados; integración pendiente donde se indica | Revisión humana pendiente |

Actualizar filas existentes; no crear un segundo conjunto de tareas por variante desktop/mobile ni por cada estado visual. Si hace falta dividir una tarea, conservar ID padre y crear sufijo incremental con alcance/existencia verificable.
