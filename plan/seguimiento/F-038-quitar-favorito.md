# Tareas y seguimiento — F-038 Quitar favorito

Versión 0.1.0 · Planificación inicial · F-038 no está implementada por estos documentos.

## Fuente y control

- [Plan F-038](../funcionalidades/F-038-quitar-favorito.md); [iteración S2](../iteraciones/S02-semanas-09-11.md).
- [Funcional](../../SPECS/funcional/F-038-quitar-favorito.md), [UI](../../SPECS/ui/F-038-quitar-favorito.md), [API](../../SPECS/contrato-api/F-038-quitar-favorito.md), [React](../../SPECS/componentes-react/F-038-quitar-favorito.md).
- [Reglas del seguimiento](README.md), [pruebas/DevSecOps](../DEVSECOPS-Y-PRUEBAS.md), [gates](../DECISIONES-Y-BLOQUEOS.md).
- Responsable asignado por el PO: **Diego Espinoza**; revisor principal: **Fernando Saire** según la [matriz](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md). Estimación base fijada en la matriz; ejecución y evidencia pendientes. La semana objetivo es académica, no fecha de calendario.
- Mock y real se reportan por separado. QA local puede avanzar con fixtures; QA real requiere INT. Evidencia inicial pendiente, no pruebas ejecutadas.

## Tablero

| ID | Área | Responsable | Revisor | Prioridad | Depende de | Semana objetivo | Estado |
|---|---|---|---|---|---|---|---|
| TASK-F038-FE-001 | Frontend | Diego Espinoza | Fernando Saire | P1 | TASK-TRANS-S01-OPS-001 | 9 | Pendiente |
| TASK-F038-BE-001 | Backend | Diego Espinoza | Fernando Saire | P1 | TASK-TRANS-S01-OPS-001 + TASK-TRANS-S01-DB-001 | 9 | Pendiente |
| TASK-F038-DB-001 | BD / Prisma | Diego Espinoza | Fernando Saire | P1 | TASK-TRANS-S01-DB-001 | 11 | Pendiente |
| TASK-F038-INT-001 | Integración | Diego Espinoza | Fernando Saire | P1 | TASK-F038-BE-001 + TASK-F038-DB-001 + I-01 + G-UNDO + TASK-F037-INT-001 | 11 | Bloqueado |
| TASK-F038-QA-001 | QA funcional | Diego Espinoza | Fernando Saire | P1 | TASK-F038-FE-001 + TASK-F038-BE-001 + TASK-F038-DB-001 | 11 | Pendiente |
| TASK-F038-QA-002 | QA seguridad / DevSecOps | Diego Espinoza | Fernando Saire | P1 | TASK-F038-FE-001 + TASK-F038-BE-001 + TASK-TRANS-S02-OPS-002 | 11 | Pendiente |
| TASK-F038-DOC-001 | Documentación | Diego Espinoza | Fernando Saire | P1 | TASK-F038-INT-001 + TASK-F038-QA-001 + TASK-F038-QA-002 | 11 | Pendiente |

Referente de BD: Diego Espinoza para este bloque, con revisión de Fernando Saire; Andres mantiene soporte transversal de migraciones. Ver [matriz](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md).

## Trabajo, Definition of Done y evidencia

### TASK-F038-FE-001

- **Trabajo:** Implementar RemoveWishlistAction, WishlistUndoFeedback y todos los estados de React/UI.
- **Terminado cuando:** Props/eventos tipados, estado específico, sin requests internos navegador; desktop/mobile aplicables y casos de spec React cubiertos.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F038-BE-001

- **Trabajo:** DELETE favorito idempotente del titular; restauración con F-036 sin recuperar timestamps ni aceptar otro customerId.
- **Terminado cuando:** DTO, validación, errores y ownership probados con fixtures; transacciones/versiones donde aplica. Adaptador real no activado si gate externo sigue abierto.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F038-DB-001

- **Trabajo:** Integrar/verificar persistencia WishlistItem; sin crear entidades externas. Reutilizar migración común, no recrear tablas por funcionalidad.
- **Terminado cuando:** Modelo Prisma/migraciones y documentación concuerdan con baseline; prueba constraints/ownership/concurrencia/rollback pertinente pasa en PostgreSQL 16 temporal.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F038-INT-001

- **Trabajo:** Homologar y probar integración real y condiciones: I-01, G-UNDO; no sólo fixture.
- **Terminado cuando:** Contrato/configuración y gates enlazados, pruebas positivas/negativas y timeout autorizadas pasan; evidencia distingue sandbox de mock.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Falta cierre documentado de I-01, G-UNDO. Contrato/configuración y prueba enlazados antes de cambiar a En progreso.

### TASK-F038-QA-001

- **Trabajo:** Probar delete repetido sin error; fallo restaura foco; undo espera DELETE; producto inactivo no restaurado falsamente; incluir cada estado visual y transición documentada.
- **Terminado cuando:** Casos unitarios/componentes/API y E2E aplicables pasan con evidencias; pruebas mock y reales etiquetadas. Hallazgos corregidos/reprobados.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F038-QA-002

- **Trabajo:** DELETE ajeno / ID inválido y CSRF; Undo no burla elegibilidad.
- **Terminado cuando:** Negativos de seguridad pasan en entorno propio/autorizado, scans SAST/SCA/secrets y DAST aplicable adjuntos sin secretos. Sin hallazgo crítico/alto explotable abierto.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F038-DOC-001

- **Trabajo:** Actualizar trazabilidad specs↔implementación↔pruebas, enlaces Figma y decisiones resueltas; documentar operación/errores relevantes.
- **Terminado cuando:** Fuentes vigentes coherentes, evidencias reales y revisión independiente; no marcar funcionalidad terminada con integración pendiente.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.


## Registro de revisión

| Fecha/semana | Cambios de estado | Evidencia / bloqueo / decisión | Revisó |
|---|---|---|---|
| Semana 6, preparación | Creación de tareas; sin ejecución | Specs y plan elaborados; integración pendiente donde se indica | Revisión humana pendiente |

Actualizar filas existentes; no crear un segundo conjunto de tareas por variante desktop/mobile ni por cada estado visual. Si hace falta dividir una tarea, conservar ID padre y crear sufijo incremental con alcance/existencia verificable.
