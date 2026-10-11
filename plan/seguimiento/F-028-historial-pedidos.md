# Tareas y seguimiento — F-028 Consultar historial de pedidos

Versión 0.1.0 · Planificación inicial · F-028 no está implementada por estos documentos.

## Fuente y control

- [Plan F-028](../funcionalidades/F-028-historial-pedidos.md); [iteración S3](../iteraciones/S03-semanas-12-13.md).
- [Funcional](../../SPECS/funcional/F-028-historial-pedidos.md), [UI](../../SPECS/ui/F-028-historial-pedidos.md), [API](../../SPECS/contrato-api/F-028-historial-pedidos.md), [React](../../SPECS/componentes-react/F-028-historial-pedidos.md).
- [Reglas del seguimiento](README.md), [pruebas/DevSecOps](../DEVSECOPS-Y-PRUEBAS.md), [gates](../DECISIONES-Y-BLOQUEOS.md).
- Responsables y revisores **por asignar** tras estimar capacidad. La semana objetivo es académica, no fecha de calendario.
- Mock y real se reportan por separado. QA local puede avanzar con fixtures; QA real requiere INT. Evidencia inicial pendiente, no pruebas ejecutadas.

## Tablero

| ID | Área | Responsable | Revisor | Prioridad | Depende de | Semana objetivo | Estado |
|---|---|---|---|---|---|---|---|
| TASK-F028-FE-001 | Frontend | Por asignar | Por asignar | P0 | TASK-TRANS-S01-OPS-001 | 12 | Pendiente |
| TASK-F028-BE-001 | Backend | Por asignar | Por asignar | P0 | TASK-TRANS-S01-OPS-001 | 12 | Pendiente |
| TASK-F028-INT-001 | Integración | Por asignar | Por asignar | P0 | TASK-F028-BE-001 + I-03 + TASK-F002-INT-001 | 13 | Bloqueado |
| TASK-F028-QA-001 | QA funcional | Por asignar | Por asignar | P0 | TASK-F028-FE-001 + TASK-F028-BE-001 | 13 | Pendiente |
| TASK-F028-QA-002 | QA seguridad / DevSecOps | Por asignar | Por asignar | P0 | TASK-F028-FE-001 + TASK-F028-BE-001 + TASK-TRANS-S03-OPS-002 | 13 | Pendiente |
| TASK-F028-DOC-001 | Documentación | Por asignar | Por asignar | P0 | TASK-F028-INT-001 + TASK-F028-QA-001 + TASK-F028-QA-002 | 13 | Pendiente |

Referentes de BD: por asignar junto con el resto de tareas; ver [plan general](../PLAN-IMPLEMENTACION.md). Dependencias transversales en [TRANSVERSALES](TRANSVERSALES.md). Los IDs DOC/OPS son extensiones de tareas, no specs.

## Trabajo, Definition of Done y evidencia

### TASK-F028-FE-001

- **Trabajo:** Implementar OrdersHistoryContainer, OrderList y todos los estados de React/UI.
- **Terminado cuando:** Props/eventos tipados, estado específico, sin requests internos navegador; desktop/mobile aplicables y casos de spec React cubiertos.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F028-BE-001

- **Trabajo:** Adaptar historial/me con titular del JWT validado en Ventas y paginación, sin clienteId del navegador ni réplica.
- **Terminado cuando:** DTO, validación, errores y ownership probados con fixtures; transacciones/versiones donde aplica. Adaptador real no activado si gate externo sigue abierto.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F028-INT-001

- **Trabajo:** Homologar y probar integración real y condiciones: I-03; no sólo fixture.
- **Terminado cuando:** Contrato/configuración y gates enlazados, pruebas positivas/negativas y timeout autorizadas pasan; evidencia distingue sandbox de mock.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Falta cierre documentado de I-03. Contrato/configuración y prueba enlazados antes de cambiar a En progreso.

### TASK-F028-QA-001

- **Trabajo:** Probar request no clienteId; vacío catálogo; 401 retira lista previa; meta pagina y conserva filtros; incluir cada estado visual y transición documentada.
- **Terminado cuando:** Casos unitarios/componentes/API y E2E aplicables pasan con evidencias; pruebas mock y reales etiquetadas. Hallazgos corregidos/reprobados.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F028-QA-002

- **Trabajo:** IDOR con JWT con clienteId forjado y cachés entre usuarios, sólo pedidos propios.
- **Terminado cuando:** Negativos de seguridad pasan en entorno propio/autorizado, scans SAST/SCA/secrets y DAST aplicable adjuntos sin secretos. Sin hallazgo crítico/alto explotable abierto.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F028-DOC-001

- **Trabajo:** Actualizar trazabilidad specs↔implementación↔pruebas, enlaces Figma y decisiones resueltas; documentar operación/errores relevantes.
- **Terminado cuando:** Fuentes vigentes coherentes, evidencias reales y revisión independiente; no marcar funcionalidad terminada con integración pendiente.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.


## Registro de revisión

| Fecha/semana | Cambios de estado | Evidencia / bloqueo / decisión | Revisó |
|---|---|---|---|
| Semana 6, preparación | Creación de tareas; sin ejecución | Specs y plan elaborados; integración pendiente donde se indica | Revisión humana pendiente |

Actualizar filas existentes; no crear un segundo conjunto de tareas por variante desktop/mobile ni por cada estado visual. Si hace falta dividir una tarea, conservar ID padre y crear sufijo incremental con alcance/existencia verificable.

