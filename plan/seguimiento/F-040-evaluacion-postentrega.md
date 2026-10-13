# Tareas y seguimiento — F-040 Registrar evaluación postentrega

Versión 0.1.0 · Planificación inicial · F-040 no está implementada por estos documentos.

## Fuente y control

- [Plan F-040](../funcionalidades/F-040-evaluacion-postentrega.md); [iteración S5](../iteraciones/S05-semanas-15-16.md).
- [Funcional](../../SPECS/funcional/F-040-evaluacion-postentrega.md), [UI](../../SPECS/ui/F-040-evaluacion-postentrega.md), [API](../../SPECS/contrato-api/F-040-evaluacion-postentrega.md), [React](../../SPECS/componentes-react/F-040-evaluacion-postentrega.md).
- [Reglas del seguimiento](README.md), [pruebas/DevSecOps](../DEVSECOPS-Y-PRUEBAS.md), [gates](../DECISIONES-Y-BLOQUEOS.md).
- Responsable propuesto: **Diego Espinoza**; revisor principal: **Fernando Saire** según la [matriz](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md). Aceptación y estimación personales pendientes. La semana objetivo es académica, no fecha de calendario.
- Mock y real se reportan por separado. QA local puede avanzar con fixtures; QA real requiere INT. Evidencia inicial pendiente, no pruebas ejecutadas.

## Tablero

| ID | Área | Responsable | Revisor | Prioridad | Depende de | Semana objetivo | Estado |
|---|---|---|---|---|---|---|---|
| TASK-F040-FE-001 | Frontend | Diego Espinoza | Fernando Saire | P2 | TASK-TRANS-S01-OPS-001 | 15 | Pendiente |
| TASK-F040-BE-001 | Backend | Diego Espinoza | Fernando Saire | P2 | TASK-TRANS-S01-OPS-001 + TASK-TRANS-S01-DB-001 | 15 | Pendiente |
| TASK-F040-DB-001 | BD / Prisma | Diego Espinoza | Fernando Saire | P2 | TASK-TRANS-S01-DB-001 | 16 | Pendiente |
| TASK-F040-INT-001 | Integración | Diego Espinoza | Fernando Saire | P2 | TASK-F040-BE-001 + TASK-F040-DB-001 + I-03 + I-04 + G-PROMPT + TASK-F030-INT-001 + TASK-F032-INT-001 | 16 | Bloqueado |
| TASK-F040-QA-001 | QA funcional | Diego Espinoza | Fernando Saire | P2 | TASK-F040-FE-001 + TASK-F040-BE-001 + TASK-F040-DB-001 | 16 | Pendiente |
| TASK-F040-QA-002 | QA seguridad / DevSecOps | Diego Espinoza | Fernando Saire | P2 | TASK-F040-FE-001 + TASK-F040-BE-001 + TASK-TRANS-S05-OPS-002 | 16 | Pendiente |
| TASK-F040-DOC-001 | Documentación | Diego Espinoza | Fernando Saire | P2 | TASK-F040-INT-001 + TASK-F040-QA-001 + TASK-F040-QA-002 | 16 | Pendiente |

Referente de BD: Diego Espinoza para este bloque, con revisión de Fernando Saire; Andres mantiene soporte transversal de migraciones. Ver [matriz](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md).

## Trabajo, Definition of Done y evidencia

### TASK-F040-FE-001

- **Trabajo:** Implementar PostDeliveryInvitation, PostDeliveryFeedbackForm y todos los estados de React/UI.
- **Terminado cuando:** Props/eventos tipados, estado específico, sin requests internos navegador; desktop/mobile aplicables y casos de spec React cubiertos.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F040-BE-001

- **Trabajo:** Autorizar pedido entregado y prompt, mapear GOOD/REGULAR/BAD a 5/3/1 en Ventas; sólo estado UX local, ciclo prompt documentado.
- **Terminado cuando:** DTO, validación, errores y ownership probados con fixtures; transacciones/versiones donde aplica. Adaptador real no activado si gate externo sigue abierto.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F040-DB-001

- **Trabajo:** Integrar/verificar persistencia PostDeliveryPrompt; sin crear entidades externas. Reutilizar migración común, no recrear tablas por funcionalidad.
- **Terminado cuando:** Modelo Prisma/migraciones y documentación concuerdan con baseline; prueba constraints/ownership/concurrencia/rollback pertinente pasa en PostgreSQL 16 temporal.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F040-INT-001

- **Trabajo:** Homologar y probar integración real y condiciones: I-03, I-04, G-PROMPT; no sólo fixture.
- **Terminado cuando:** Contrato/configuración y gates enlazados, pruebas positivas/negativas y timeout autorizadas pasan; evidencia distingue sandbox de mock.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Falta cierre documentado de I-03, I-04, G-PROMPT. Contrato/configuración y prueba enlazados antes de cambiar a En progreso.

### TASK-F040-QA-001

- **Trabajo:** Probar no entregado no banner; sentimiento cambia motivos coherentes; duplicado cierra como enviado; fallo conserva formulario; logout borra comentario; Escape respeta política sin registro supuesto; incluir cada estado visual y transición documentada.
- **Terminado cuando:** Casos unitarios/componentes/API y E2E aplicables pasan con evidencias; pruebas mock y reales etiquetadas. Hallazgos corregidos/reprobados.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F040-QA-002

- **Trabajo:** CSAT de pedido ajeno/no entregado/replay; XSS en comentario y PII en logs y no almacenar rating local.
- **Terminado cuando:** Negativos de seguridad pasan en entorno propio/autorizado, scans SAST/SCA/secrets y DAST aplicable adjuntos sin secretos. Sin hallazgo crítico/alto explotable abierto.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F040-DOC-001

- **Trabajo:** Actualizar trazabilidad specs↔implementación↔pruebas, enlaces Figma y decisiones resueltas; documentar operación/errores relevantes.
- **Terminado cuando:** Fuentes vigentes coherentes, evidencias reales y revisión independiente; no marcar funcionalidad terminada con integración pendiente.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.


## Registro de revisión

| Fecha/semana | Cambios de estado | Evidencia / bloqueo / decisión | Revisó |
|---|---|---|---|
| Semana 6, preparación | Creación de tareas; sin ejecución | Specs y plan elaborados; integración pendiente donde se indica | Revisión humana pendiente |

Actualizar filas existentes; no crear un segundo conjunto de tareas por variante desktop/mobile ni por cada estado visual. Si hace falta dividir una tarea, conservar ID padre y crear sufijo incremental con alcance/existencia verificable.
