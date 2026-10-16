# Tareas y seguimiento — F-007 Buscar productos por texto

Versión 0.2.1 · Corte MOCK y automatización actualizados al 16/10/2026; integración, revisión y cierre pendientes.

## Fuente y control

- [Plan F-007](../funcionalidades/F-007-buscar-productos-texto.md); [iteración S1](../iteraciones/S01-semanas-07-08.md).
- [Funcional](../../SPECS/funcional/F-007-buscar-productos-texto.md), [UI](../../SPECS/ui/F-007-buscar-productos-texto.md), [API](../../SPECS/contrato-api/F-007-buscar-productos-texto.md), [React](../../SPECS/componentes-react/F-007-buscar-productos-texto.md).
- [Reglas del seguimiento](README.md), [pruebas/DevSecOps](../DEVSECOPS-Y-PRUEBAS.md), [gates](../DECISIONES-Y-BLOQUEOS.md).
- Responsable asignado por el PO: **Giuliano Macchiavello**; revisor principal: **Sebastian Malca** según la [matriz](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md). Estimación base fijada en la matriz; ejecución y evidencia pendientes. La semana objetivo es académica, no fecha de calendario.
- Mock y real se reportan por separado. QA local puede avanzar con fixtures; QA real requiere INT. La evidencia local del 14/10 está enlazada en el registro; no acredita QA REAL.

## Tablero

| ID | Área | Responsable | Revisor | Prioridad | Depende de | Semana objetivo | Estado |
|---|---|---|---|---|---|---|---|
| TASK-F007-FE-001 | Frontend | Giuliano Macchiavello | Sebastian Malca | P0 | TASK-TRANS-S01-OPS-001 | 7 | En progreso |
| TASK-F007-BE-001 | Backend | Giuliano Macchiavello | Sebastian Malca | P0 | TASK-TRANS-S01-OPS-001 | 7 | En progreso |
| TASK-F007-INT-001 | Integración | Giuliano Macchiavello | Sebastian Malca | P0 | TASK-F007-BE-001 + I-01 + TASK-F006-INT-001 | 8 | Bloqueado |
| TASK-F007-QA-001 | QA funcional | Giuliano Macchiavello | Sebastian Malca | P0 | TASK-F007-FE-001 + TASK-F007-BE-001 | 8 | En progreso |
| TASK-F007-QA-002 | QA seguridad / DevSecOps | Giuliano Macchiavello | Sebastian Malca | P0 | TASK-F007-FE-001 + TASK-F007-BE-001 + TASK-TRANS-S01-OPS-002 | 8 | En progreso |
| TASK-F007-DOC-001 | Documentación | Giuliano Macchiavello | Sebastian Malca | P0 | TASK-F007-INT-001 + TASK-F007-QA-001 + TASK-F007-QA-002 | 8 | En progreso |

La auditoría BD/OPS S1 se propone para Andres; ver [transversales](TRANSVERSALES.md). Los IDs DOC/OPS son extensiones de tareas, no specs. El buscador compartido de Giuliano se coordina con Sebastian sin duplicar estos IDs.

## Trabajo, Definition of Done y evidencia

### TASK-F007-FE-001

- **Trabajo:** Implementar SearchBox, SearchResultsHeading y todos los estados de React/UI.
- **Terminado cuando:** Props/eventos tipados, estado específico, sin requests internos navegador; desktop/mobile aplicables y casos de spec React cubiertos.
- **Evidencia:** [Corte local y verificaciones del 14/10](../evidencias/H3-GIULIANO-CATALOGO-2026-10-14.md): buscador, resultados, validación, cancelación, URL, vacío/error y paginación básica MOCK.
- **Bloqueo / liberación:** Revisión de Sebastian, integración de ficha y conformidad de tarjeta completa pendientes; respetar dependencias para cierre.

### TASK-F007-BE-001

- **Trabajo:** Validar q de 2–120 caracteres y adaptar búsqueda paginada pública, proteger query de logs identificables.
- **Terminado cuando:** DTO, validación, errores y ownership probados con fixtures; transacciones/versiones donde aplica. Adaptador real no activado si gate externo sigue abierto.
- **Evidencia:** [BFF y pruebas locales](../evidencias/H3-GIULIANO-CATALOGO-2026-10-14.md): ruta de búsqueda, validación antes del proveedor, proyección pública, errores, timeout y mapeo de paginación con respuestas sintéticas.
- **Bloqueo / liberación:** I-01 sin configuración/prueba real; adaptador candidato requiere revisión de Leonidas y homologación antes de activarse.

### TASK-F007-INT-001

- **Trabajo:** Homologar y probar integración real y condiciones: I-01; no sólo fixture.
- **Terminado cuando:** Contrato/configuración y gates enlazados, pruebas positivas/negativas y timeout autorizadas pasan; evidencia distingue sandbox de mock.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Falta cierre documentado de I-01. Contrato/configuración y prueba enlazados antes de cambiar a En progreso.

### TASK-F007-QA-001

- **Trabajo:** Probar 1 y 121 caracteres no consultan; query vacía vuelve catálogo; respuesta lenta anterior no reemplaza nueva; cero resultados conserva q y limpiar; incluir cada estado visual y transición documentada.
- **Terminado cuando:** Casos unitarios/componentes/API y E2E aplicables pasan con evidencias; pruebas mock y reales etiquetadas. Hallazgos corregidos/reprobados.
- **Evidencia:** [Resultados y retest MOCK](../evidencias/H3-GIULIANO-CATALOGO-2026-10-14.md): consulta válida/inválida, cero, error/reintento, respuesta anterior ignorada, foco, mobile y URL.
- **Bloqueo / liberación:** QA local parcial; faltan revisión independiente y ejecución contra proveedor autorizado antes del cierre.

### TASK-F007-QA-002

- **Trabajo:** Entradas XSS/inyección y longitudes, consulta pública sin datos privados.
- **Terminado cuando:** Negativos de seguridad pasan en entorno propio/autorizado, scans SAST/SCA/secrets y DAST aplicable adjuntos sin secretos. Sin hallazgo crítico/alto explotable abierto.
- **Evidencia:** [Controles locales/CI y hallazgos](../evidencias/H3-AUTONOMIA-2026-10-16.md), [entrega, trazabilidad y demo](../entrega/H3-GIULIANO.md). Revisión humana, QA REAL y aceptación pendientes.
- **Bloqueo / liberación:** Avance independiente documentado; requiere entorno REAL autorizado, DAST staging, revisión y aceptación de riesgos para el cierre. Ninguna tarea se declara terminada.

### TASK-F007-DOC-001

- **Trabajo:** Actualizar trazabilidad specs↔implementación↔pruebas, enlaces Figma y decisiones resueltas; documentar operación/errores relevantes.
- **Terminado cuando:** Fuentes vigentes coherentes, evidencias reales y revisión independiente; no marcar funcionalidad terminada con integración pendiente.
- **Evidencia:** [Controles locales/CI y hallazgos](../evidencias/H3-AUTONOMIA-2026-10-16.md), [entrega, trazabilidad y demo](../entrega/H3-GIULIANO.md). Revisión humana, QA REAL y aceptación pendientes.
- **Bloqueo / liberación:** Avance independiente documentado; requiere entorno REAL autorizado, DAST staging, revisión y aceptación de riesgos para el cierre. Ninguna tarea se declara terminada.


## Registro de revisión

Avance local del 14/10/2026: [evidencia individual y límites](../evidencias/H3-GIULIANO-CATALOGO-2026-10-14.md). Búsqueda UI→Next→BFF con consulta válida/inválida, estados, URL, cancelación y pruebas MOCK; adaptador candidato sin llamada real a G6. Revisión independiente, tarjeta comercial completa y ficha de Sebastian pendientes. INT permanece bloqueada por I-01. QA-001 refleja ejecución local parcial, no cierre de QA REAL. Los resultados iniciales pendientes de las fichas de tarea se complementan con esta evidencia, sin declarar Done.

| Fecha/semana | Cambios de estado | Evidencia / bloqueo / decisión | Revisó |
|---|---|---|---|
| Semana 6, preparación | Creación de tareas; sin ejecución | Specs y plan elaborados; integración pendiente donde se indica | Revisión humana pendiente |
| 14/10/2026, avance local | FE/BE/QA-001 en progreso; INT bloqueada | Corte MOCK, pruebas/build y evidencia enlazada; ninguna tarea terminada | Revisión de Sebastian/Leonidas pendiente |
| 16/10/2026, automatización H3 | QA-002 y DOC-001 en progreso; INT sigue bloqueada | [Pruebas, seguridad, CI y límites](../evidencias/H3-AUTONOMIA-2026-10-16.md); [paquete de entrega](../entrega/H3-GIULIANO.md). FE/BE/QA-001 mantienen estado hasta revisión | Revisión humana pendiente |

Actualizar filas existentes; no crear un segundo conjunto de tareas por variante desktop/mobile ni por cada estado visual. Si hace falta dividir una tarea, conservar ID padre y crear sufijo incremental con alcance/existencia verificable.
