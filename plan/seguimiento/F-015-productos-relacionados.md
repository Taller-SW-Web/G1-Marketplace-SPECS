# Tareas y seguimiento — F-015 Visualizar productos relacionados

Versión 0.1.0 · Planificación inicial · F-015 no está implementada por estos documentos.

## Fuente y control

- [Plan F-015](../funcionalidades/F-015-productos-relacionados.md); [sprint 2](../iteraciones/S02-semanas-08-09.md).
- [Funcional](../../SPECS/funcional/F-015-productos-relacionados.md), [UI](../../SPECS/ui/F-015-productos-relacionados.md), [API](../../SPECS/contrato-api/F-015-productos-relacionados.md), [React](../../SPECS/componentes-react/F-015-productos-relacionados.md).
- [Reglas del seguimiento](README.md), [pruebas/DevSecOps](../DEVSECOPS-Y-PRUEBAS.md), [gates](../DECISIONES-Y-BLOQUEOS.md).
- Responsables/revisores **propuestos**, no compromiso aceptado. Semana objetivo no es fecha de calendario; confirmar capacidad en planificación.
- Mock y real se reportan por separado. QA local puede avanzar con fixtures; QA real requiere INT. Evidencia inicial pendiente, no pruebas ejecutadas.

## Tablero

| ID | Área | Responsable | Revisor | Prioridad | Depende de | Semana objetivo | Estado |
|---|---|---|---|---|---|---|---|
| TASK-F015-FE-001 | Frontend | Giuliano | Fernando | P2 | TASK-TRANS-S01-OPS-001 | 8 | Pendiente |
| TASK-F015-BE-001 | Backend | Leonidas | Andres | P2 | TASK-TRANS-S01-OPS-001 | 8 | Pendiente |
| TASK-F015-INT-001 | Integración | Leonidas | Andres | P2 | TASK-F015-BE-001 + I-01 + TASK-F011-INT-001 | 9 | Bloqueado |
| TASK-F015-QA-001 | QA funcional | Fernando | Sebastian | P2 | TASK-F015-FE-001 + TASK-F015-BE-001 | 9 | Pendiente |
| TASK-F015-QA-002 | QA seguridad / DevSecOps | Andres | Fernando | P2 | TASK-F015-FE-001 + TASK-F015-BE-001 + TASK-TRANS-S02-OPS-002 | 9 | Pendiente |
| TASK-F015-DOC-001 | Documentación | Sebastian | Jim | P2 | TASK-F015-INT-001 + TASK-F015-QA-001 + TASK-F015-QA-002 | 9 | Pendiente |

Referentes de BD: Leonidas + Andres; ver [nombres y roles](../PLAN-IMPLEMENTACION.md#4-responsabilidad-sin-confundir-diseño-con-código). Dependencias transversales en [TRANSVERSALES](TRANSVERSALES.md). Los IDs DOC/OPS son extensiones de tareas documentales/operativas, no nuevos IDs funcionales.

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

