# Tareas y seguimiento — F-030 Visualizar detalle de pedido

Versión 0.1.0 · Planificación inicial · F-030 no está implementada por estos documentos.

## Fuente y control

- [Plan F-030](../funcionalidades/F-030-detalle-pedido.md); [sprint 5](../iteraciones/S05-semanas-14-15.md).
- [Funcional](../../SPECS/funcional/F-030-detalle-pedido.md), [UI](../../SPECS/ui/F-030-detalle-pedido.md), [API](../../SPECS/contrato-api/F-030-detalle-pedido.md), [React](../../SPECS/componentes-react/F-030-detalle-pedido.md).
- [Reglas del seguimiento](README.md), [pruebas/DevSecOps](../DEVSECOPS-Y-PRUEBAS.md), [gates](../DECISIONES-Y-BLOQUEOS.md).
- Responsables/revisores **propuestos**, no compromiso aceptado. Semana objetivo no es fecha de calendario; confirmar capacidad en planificación.
- Mock y real se reportan por separado. QA local puede avanzar con fixtures; QA real requiere INT. Evidencia inicial pendiente, no pruebas ejecutadas.

## Tablero

| ID | Área | Responsable | Revisor | Prioridad | Depende de | Semana objetivo | Estado |
|---|---|---|---|---|---|---|---|
| TASK-F030-FE-001 | Frontend | Sebastian | Fernando | P1 | TASK-TRANS-S01-OPS-001 | 14 | Pendiente |
| TASK-F030-BE-001 | Backend | Leonidas | Andres | P1 | TASK-TRANS-S01-OPS-001 | 14 | Pendiente |
| TASK-F030-INT-001 | Integración | Leonidas | Andres | P1 | TASK-F030-BE-001 + I-03 + TASK-F028-INT-001 | 15 | Bloqueado |
| TASK-F030-QA-001 | QA funcional | Fernando | Giuliano | P1 | TASK-F030-FE-001 + TASK-F030-BE-001 | 15 | Pendiente |
| TASK-F030-QA-002 | QA seguridad / DevSecOps | Andres | Fernando | P1 | TASK-F030-FE-001 + TASK-F030-BE-001 + TASK-TRANS-S05-OPS-002 | 15 | Pendiente |
| TASK-F030-DOC-001 | Documentación | Sebastian | Jim | P1 | TASK-F030-INT-001 + TASK-F030-QA-001 + TASK-F030-QA-002 | 15 | Pendiente |

Referentes de BD: Leonidas + Andres; ver [nombres y roles](../PLAN-IMPLEMENTACION.md#4-responsabilidad-sin-confundir-diseño-con-código). Dependencias transversales en [TRANSVERSALES](TRANSVERSALES.md). Los IDs DOC/OPS son extensiones de tareas documentales/operativas, no nuevos IDs funcionales.

## Trabajo, Definition of Done y evidencia

### TASK-F030-FE-001

- **Trabajo:** Implementar OrderDetailContainer, HistoricalOrderLines, OrderStateTimeline y todos los estados de React/UI.
- **Terminado cuando:** Props/eventos tipados, estado específico, sin requests internos navegador; desktop/mobile aplicables y casos de spec React cubiertos.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F030-BE-001

- **Trabajo:** Autorizar detalle en Ventas, devolver snapshots históricos mínimos y neutralizar 403/404 sin filtrar existencia.
- **Terminado cuando:** DTO, validación, errores y ownership probados con fixtures; transacciones/versiones donde aplica. Adaptador real no activado si gate externo sigue abierto.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F030-INT-001

- **Trabajo:** Homologar y probar integración real y condiciones: I-03; no sólo fixture.
- **Terminado cuando:** Contrato/configuración y gates enlazados, pruebas positivas/negativas y timeout autorizadas pasan; evidencia distingue sandbox de mock.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Falta cierre documentado de I-03. Contrato/configuración y prueba enlazados antes de cambiar a En progreso.

### TASK-F030-QA-001

- **Trabajo:** Probar precio histórico invariable si catálogo cambia; pedido ajeno neutral; sin tracking no CTA falso; timeline comprensible lector; incluir cada estado visual y transición documentada.
- **Terminado cuando:** Casos unitarios/componentes/API y E2E aplicables pasan con evidencias; pruebas mock y reales etiquetadas. Hallazgos corregidos/reprobados.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F030-QA-002

- **Trabajo:** 404 neutral para pedido ajeno, documento / tarjeta / email completo excluidos.
- **Terminado cuando:** Negativos de seguridad pasan en entorno propio/autorizado, scans SAST/SCA/secrets y DAST aplicable adjuntos sin secretos. Sin hallazgo crítico/alto explotable abierto.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F030-DOC-001

- **Trabajo:** Actualizar trazabilidad specs↔implementación↔pruebas, enlaces Figma y decisiones resueltas; documentar operación/errores relevantes.
- **Terminado cuando:** Fuentes vigentes coherentes, evidencias reales y revisión independiente; no marcar funcionalidad terminada con integración pendiente.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.


## Registro de revisión

| Fecha/semana | Cambios de estado | Evidencia / bloqueo / decisión | Revisó |
|---|---|---|---|
| Semana 6, preparación | Creación de tareas; sin ejecución | Specs y plan elaborados; integración pendiente donde se indica | Revisión humana pendiente |

Actualizar filas existentes; no crear un segundo conjunto de tareas por variante desktop/mobile ni por cada estado visual. Si hace falta dividir una tarea, conservar ID padre y crear sufijo incremental con alcance/existencia verificable.

