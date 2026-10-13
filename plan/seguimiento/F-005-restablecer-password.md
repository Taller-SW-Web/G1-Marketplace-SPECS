# Tareas y seguimiento — F-005 Restablecer contraseña

Versión 0.1.0 · Planificación inicial · F-005 no está implementada por estos documentos.

## Fuente y control

- [Plan F-005](../funcionalidades/F-005-restablecer-password.md); [iteración S5](../iteraciones/S05-semanas-15-16.md).
- [Funcional](../../SPECS/funcional/F-005-restablecer-password.md), [UI](../../SPECS/ui/F-005-restablecer-password.md), [API](../../SPECS/contrato-api/F-005-restablecer-password.md), [React](../../SPECS/componentes-react/F-005-restablecer-password.md).
- [Reglas del seguimiento](README.md), [pruebas/DevSecOps](../DEVSECOPS-Y-PRUEBAS.md), [gates](../DECISIONES-Y-BLOQUEOS.md).
- Responsable asignado por el PO: **Jim Segovia**; revisor principal: **Andres Morales** según la [matriz](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md). Estimación base fijada en la matriz; ejecución y evidencia pendientes. La semana objetivo es académica, no fecha de calendario.
- Mock y real se reportan por separado. QA local puede avanzar con fixtures; QA real requiere INT. Evidencia inicial pendiente, no pruebas ejecutadas.

## Tablero

| ID | Área | Responsable | Revisor | Prioridad | Depende de | Semana objetivo | Estado |
|---|---|---|---|---|---|---|---|
| TASK-F005-FE-001 | Frontend | Jim Segovia | Andres Morales | P0 | TASK-TRANS-S01-OPS-001 | 15 | Pendiente |
| TASK-F005-BE-001 | Backend | Jim Segovia | Andres Morales | P0 | TASK-TRANS-S01-OPS-001 | 15 | Pendiente |
| TASK-F005-INT-001 | Integración | Jim Segovia | Andres Morales | P0 | TASK-F005-BE-001 + G-AUTH + TASK-F004-INT-001 | 16 | Bloqueado |
| TASK-F005-QA-001 | QA funcional | Jim Segovia | Andres Morales | P0 | TASK-F005-FE-001 + TASK-F005-BE-001 | 16 | Pendiente |
| TASK-F005-QA-002 | QA seguridad / DevSecOps | Jim Segovia | Andres Morales | P0 | TASK-F005-FE-001 + TASK-F005-BE-001 + TASK-TRANS-S05-OPS-002 | 16 | Pendiente |
| TASK-F005-DOC-001 | Documentación | Jim Segovia | Andres Morales | P0 | TASK-F005-INT-001 + TASK-F005-QA-001 + TASK-F005-QA-002 | 16 | Pendiente |

Referente de BD: Jim Segovia para este bloque, con revisión de Andres Morales; Andres mantiene soporte transversal de migraciones. Ver [matriz](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md).

## Trabajo, Definition of Done y evidencia

### TASK-F005-FE-001

- **Trabajo:** Implementar ResetPasswordForm, ResetLinkOutcome y todos los estados de React/UI.
- **Terminado cuando:** Props/eventos tipados, estado específico, sin requests internos navegador; desktop/mobile aplicables y casos de spec React cubiertos.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F005-BE-001

- **Trabajo:** Delegar reset con token efímero, política y errores401/410/422; no sesión automática.
- **Terminado cuando:** DTO, validación, errores y ownership probados con fixtures; transacciones/versiones donde aplica. Adaptador real no activado si gate externo sigue abierto.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F005-INT-001

- **Trabajo:** Homologar y probar integración real y condiciones: G-AUTH; no sólo fixture.
- **Terminado cuando:** Contrato/configuración y gates enlazados, pruebas positivas/negativas y timeout autorizadas pasan; evidencia distingue sandbox de mock.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Falta cierre documentado de G-AUTH. Contrato/configuración y prueba enlazados antes de cambiar a En progreso.

### TASK-F005-QA-001

- **Trabajo:** Probar sin token no llama API; 401 y 410 ofrecen nuevo enlace; 422 no muestra token; 204 no crea sesión; incluir cada estado visual y transición documentada.
- **Terminado cuando:** Casos unitarios/componentes/API y E2E aplicables pasan con evidencias; pruebas mock y reales etiquetadas. Hallazgos corregidos/reprobados.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F005-QA-002

- **Trabajo:** Token reset usado/vencido, contraseña no filtrada, referrer/analítica y no sesión automática.
- **Terminado cuando:** Negativos de seguridad pasan en entorno propio/autorizado, scans SAST/SCA/secrets y DAST aplicable adjuntos sin secretos. Sin hallazgo crítico/alto explotable abierto.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F005-DOC-001

- **Trabajo:** Actualizar trazabilidad specs↔implementación↔pruebas, enlaces Figma y decisiones resueltas; documentar operación/errores relevantes.
- **Terminado cuando:** Fuentes vigentes coherentes, evidencias reales y revisión independiente; no marcar funcionalidad terminada con integración pendiente.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.


## Registro de revisión

| Fecha/semana | Cambios de estado | Evidencia / bloqueo / decisión | Revisó |
|---|---|---|---|
| Semana 6, preparación | Creación de tareas; sin ejecución | Specs y plan elaborados; integración pendiente donde se indica | Revisión humana pendiente |

Actualizar filas existentes; no crear un segundo conjunto de tareas por variante desktop/mobile ni por cada estado visual. Si hace falta dividir una tarea, conservar ID padre y crear sufijo incremental con alcance/existencia verificable.
