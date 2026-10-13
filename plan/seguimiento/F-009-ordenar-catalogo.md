# Tareas y seguimiento — F-009 Ordenar resultados

Versión 0.1.0 · Planificación inicial · F-009 no está implementada por estos documentos.

## Fuente y control

- [Plan F-009](../funcionalidades/F-009-ordenar-catalogo.md); [iteración S2](../iteraciones/S02-semanas-09-11.md).
- [Funcional](../../SPECS/funcional/F-009-ordenar-catalogo.md), [UI](../../SPECS/ui/F-009-ordenar-catalogo.md), [API](../../SPECS/contrato-api/F-009-ordenar-catalogo.md), [React](../../SPECS/componentes-react/F-009-ordenar-catalogo.md).
- [Reglas del seguimiento](README.md), [pruebas/DevSecOps](../DEVSECOPS-Y-PRUEBAS.md), [gates](../DECISIONES-Y-BLOQUEOS.md).
- Responsable propuesto: **Giuliano Macchiavello**; revisor principal: **Sebastian Malca** según la [matriz](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md). Aceptación y estimación personales pendientes. La semana objetivo es académica, no fecha de calendario.
- Mock y real se reportan por separado. QA local puede avanzar con fixtures; QA real requiere INT. Evidencia inicial pendiente, no pruebas ejecutadas.

## Tablero

| ID | Área | Responsable | Revisor | Prioridad | Depende de | Semana objetivo | Estado |
|---|---|---|---|---|---|---|---|
| TASK-F009-FE-001 | Frontend | Giuliano Macchiavello | Sebastian Malca | P1 | TASK-TRANS-S01-OPS-001 | 9 | Pendiente |
| TASK-F009-BE-001 | Backend | Giuliano Macchiavello | Sebastian Malca | P1 | TASK-TRANS-S01-OPS-001 | 9 | Pendiente |
| TASK-F009-INT-001 | Integración | Giuliano Macchiavello | Sebastian Malca | P1 | TASK-F009-BE-001 + I-01 + TASK-F007-INT-001 | 11 | Bloqueado |
| TASK-F009-QA-001 | QA funcional | Giuliano Macchiavello | Sebastian Malca | P1 | TASK-F009-FE-001 + TASK-F009-BE-001 | 11 | Pendiente |
| TASK-F009-QA-002 | QA seguridad / DevSecOps | Giuliano Macchiavello | Sebastian Malca | P1 | TASK-F009-FE-001 + TASK-F009-BE-001 + TASK-TRANS-S02-OPS-002 | 11 | Pendiente |
| TASK-F009-DOC-001 | Documentación | Giuliano Macchiavello | Sebastian Malca | P1 | TASK-F009-INT-001 + TASK-F009-QA-001 + TASK-F009-QA-002 | 11 | Pendiente |

Referente de BD: Giuliano Macchiavello para este bloque, con revisión de Sebastian Malca; Andres mantiene soporte transversal de migraciones. Ver [matriz](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md).

## Trabajo, Definition of Done y evidencia

### TASK-F009-FE-001

- **Trabajo:** Implementar CatalogSortSelect y todos los estados de React/UI.
- **Terminado cuando:** Props/eventos tipados, estado específico, sin requests internos navegador; desktop/mobile aplicables y casos de spec React cubiertos.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F009-BE-001

- **Trabajo:** Validar enum sort y delegar orden estable al dueño sin ordenar una página incompleta.
- **Terminado cuando:** DTO, validación, errores y ownership probados con fixtures; transacciones/versiones donde aplica. Adaptador real no activado si gate externo sigue abierto.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F009-INT-001

- **Trabajo:** Homologar y probar integración real y condiciones: I-01; no sólo fixture.
- **Terminado cuando:** Contrato/configuración y gates enlazados, pruebas positivas/negativas y timeout autorizadas pasan; evidencia distingue sandbox de mock.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Falta cierre documentado de I-01. Contrato/configuración y prueba enlazados antes de cambiar a En progreso.

### TASK-F009-QA-001

- **Trabajo:** Probar todos los enums permitidos enviados; sort inválido no llega externo; page se reinicia; no ordena sólo tarjetas de página actual; incluir cada estado visual y transición documentada.
- **Terminado cuando:** Casos unitarios/componentes/API y E2E aplicables pasan con evidencias; pruebas mock y reales etiquetadas. Hallazgos corregidos/reprobados.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F009-QA-002

- **Trabajo:** Enum desconocido/inyección no llega proveedor.
- **Terminado cuando:** Negativos de seguridad pasan en entorno propio/autorizado, scans SAST/SCA/secrets y DAST aplicable adjuntos sin secretos. Sin hallazgo crítico/alto explotable abierto.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F009-DOC-001

- **Trabajo:** Actualizar trazabilidad specs↔implementación↔pruebas, enlaces Figma y decisiones resueltas; documentar operación/errores relevantes.
- **Terminado cuando:** Fuentes vigentes coherentes, evidencias reales y revisión independiente; no marcar funcionalidad terminada con integración pendiente.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.


## Registro de revisión

| Fecha/semana | Cambios de estado | Evidencia / bloqueo / decisión | Revisó |
|---|---|---|---|
| Semana 6, preparación | Creación de tareas; sin ejecución | Specs y plan elaborados; integración pendiente donde se indica | Revisión humana pendiente |

Actualizar filas existentes; no crear un segundo conjunto de tareas por variante desktop/mobile ni por cada estado visual. Si hace falta dividir una tarea, conservar ID padre y crear sufijo incremental con alcance/existencia verificable.
