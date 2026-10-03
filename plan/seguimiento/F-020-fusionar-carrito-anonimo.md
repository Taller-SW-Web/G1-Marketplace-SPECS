# Tareas y seguimiento — F-020 Fusionar carrito anónimo al iniciar sesión

Versión 0.1.0 · Planificación inicial · F-020 no está implementada por estos documentos.

## Fuente y control

- [Plan F-020](../funcionalidades/F-020-fusionar-carrito-anonimo.md); [sprint 3](../iteraciones/S03-semanas-10-11.md).
- [Funcional](../../SPECS/funcional/F-020-fusionar-carrito-anonimo.md), [UI](../../SPECS/ui/F-020-fusionar-carrito-anonimo.md), [API](../../SPECS/contrato-api/F-020-fusionar-carrito-anonimo.md), [React](../../SPECS/componentes-react/F-020-fusionar-carrito-anonimo.md).
- [Reglas del seguimiento](README.md), [pruebas/DevSecOps](../DEVSECOPS-Y-PRUEBAS.md), [gates](../DECISIONES-Y-BLOQUEOS.md).
- Responsables/revisores **propuestos**, no compromiso aceptado. Semana objetivo no es fecha de calendario; confirmar capacidad en planificación.
- Mock y real se reportan por separado. QA local puede avanzar con fixtures; QA real requiere INT. Evidencia inicial pendiente, no pruebas ejecutadas.

## Tablero

| ID | Área | Responsable | Revisor | Prioridad | Depende de | Semana objetivo | Estado |
|---|---|---|---|---|---|---|---|
| TASK-F020-FE-001 | Frontend | Sebastian | Fernando | P0 | TASK-TRANS-S01-OPS-001 | 10 | Pendiente |
| TASK-F020-BE-001 | Backend | Leonidas | Andres | P0 | TASK-TRANS-S01-OPS-001 + TASK-TRANS-S01-DB-001 | 10 | Pendiente |
| TASK-F020-DB-001 | BD / Prisma | Leonidas | Andres | P0 | TASK-TRANS-S01-DB-001 | 10 | Pendiente |
| TASK-F020-INT-001 | Integración | Leonidas | Andres | P0 | TASK-F020-BE-001 + TASK-F020-DB-001 + I-01 + TASK-F002-INT-001 + TASK-F019-INT-001 | 11 | Bloqueado |
| TASK-F020-QA-001 | QA funcional | Fernando | Giuliano | P0 | TASK-F020-FE-001 + TASK-F020-BE-001 + TASK-F020-DB-001 | 11 | Pendiente |
| TASK-F020-QA-002 | QA seguridad / DevSecOps | Andres | Fernando | P0 | TASK-F020-FE-001 + TASK-F020-BE-001 + TASK-TRANS-S03-OPS-002 | 11 | Pendiente |
| TASK-F020-DOC-001 | Documentación | Sebastian | Jim | P0 | TASK-F020-INT-001 + TASK-F020-QA-001 + TASK-F020-QA-002 | 11 | Pendiente |

Referentes de BD: Leonidas + Andres; ver [nombres y roles](../PLAN-IMPLEMENTACION.md#4-responsabilidad-sin-confundir-diseño-con-código). Dependencias transversales en [TRANSVERSALES](TRANSVERSALES.md). Los IDs DOC/OPS son extensiones de tareas documentales/operativas, no nuevos IDs funcionales.

## Trabajo, Definition of Done y evidencia

### TASK-F020-FE-001

- **Trabajo:** Implementar CartMergeCoordinator, MergeFailureNotice, MergeAdjustmentsDialog y todos los estados de React/UI.
- **Terminado cuando:** Props/eventos tipados, estado específico, sin requests internos navegador; desktop/mobile aplicables y casos de spec React cubiertos.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F020-BE-001

- **Trabajo:** Fusionar con bloqueo/transacción, suma limitada, origen MERGED y cookie invalidada sólo tras commit; fallo conserva ambos.
- **Terminado cuando:** DTO, validación, errores y ownership probados con fixtures; transacciones/versiones donde aplica. Adaptador real no activado si gate externo sigue abierto.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F020-DB-001

- **Trabajo:** Integrar/verificar persistencia Cart/CartItem (MERGED/destino); sin crear entidades externas. Reutilizar migración común, no recrear tablas por funcionalidad.
- **Terminado cuando:** Modelo Prisma/migraciones y documentación concuerdan con baseline; prueba constraints/ownership/concurrencia/rollback pertinente pasa en PostgreSQL 16 temporal.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F020-INT-001

- **Trabajo:** Homologar y probar integración real y condiciones: I-01; no sólo fixture.
- **Terminado cuando:** Contrato/configuración y gates enlazados, pruebas positivas/negativas y timeout autorizadas pasan; evidencia distingue sandbox de mock.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Falta cierre documentado de I-01. Contrato/configuración y prueba enlazados antes de cambiar a En progreso.

### TASK-F020-QA-001

- **Trabajo:** Probar fusión repetida no suma; MFA incompleto no dispara; continuar conserva sesión y no fusiona; banner de pendientes no revela segundo carrito; incluir cada estado visual y transición documentada.
- **Terminado cuando:** Casos unitarios/componentes/API y E2E aplicables pasan con evidencias; pruebas mock y reales etiquetadas. Hallazgos corregidos/reprobados.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F020-QA-002

- **Trabajo:** Fusionar cookie de otra sesión / sin origen / MERGED concurrente sin duplicar, token inválido no cambia dueño.
- **Terminado cuando:** Negativos de seguridad pasan en entorno propio/autorizado, scans SAST/SCA/secrets y DAST aplicable adjuntos sin secretos. Sin hallazgo crítico/alto explotable abierto.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F020-DOC-001

- **Trabajo:** Actualizar trazabilidad specs↔implementación↔pruebas, enlaces Figma y decisiones resueltas; documentar operación/errores relevantes.
- **Terminado cuando:** Fuentes vigentes coherentes, evidencias reales y revisión independiente; no marcar funcionalidad terminada con integración pendiente.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.


## Registro de revisión

| Fecha/semana | Cambios de estado | Evidencia / bloqueo / decisión | Revisó |
|---|---|---|---|
| Semana 6, preparación | Creación de tareas; sin ejecución | Specs y plan elaborados; integración pendiente donde se indica | Revisión humana pendiente |

Actualizar filas existentes; no crear un segundo conjunto de tareas por variante desktop/mobile ni por cada estado visual. Si hace falta dividir una tarea, conservar ID padre y crear sufijo incremental con alcance/existencia verificable.

