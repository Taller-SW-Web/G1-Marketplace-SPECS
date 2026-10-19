# Tareas y seguimiento — F-007 Buscar productos por texto

Versión 0.2.0 · Revisión 2026-10-18. Hay código integrado; falta búsqueda positiva por la ruta pública completa y el gate F-007 pasa a H4.

## Fuente y control

- [Plan F-007](../funcionalidades/F-007-buscar-productos-texto.md); [iteración S02/H4](../iteraciones/S02-semanas-09-11.md).
- [Funcional](../../SPECS/funcional/F-007-buscar-productos-texto.md), [UI](../../SPECS/ui/F-007-buscar-productos-texto.md), [API](../../SPECS/contrato-api/F-007-buscar-productos-texto.md), [React](../../SPECS/componentes-react/F-007-buscar-productos-texto.md).
- [Reglas del seguimiento](README.md), [pruebas/DevSecOps](../DEVSECOPS-Y-PRUEBAS.md), [gates](../DECISIONES-Y-BLOQUEOS.md).
- Responsable asignado por el PO: **Giuliano Macchiavello**; revisor principal: **Sebastian Malca** según la [matriz](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md). Estimación base fijada en la matriz; ejecución y evidencia pendientes. La semana objetivo es académica, no fecha de calendario.
- Mock y real se reportan por separado. FE [#3](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/pull/3)/[#12](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/pull/12) y BE [#11](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/pull/11)/[#19](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/pull/19) están integradas. La búsqueda G6 devolvía 503 en la prueba local del 17/10; el 18/10 respondió 200 directo con lista vacía. La web G1 permite búsqueda de demostración y respondió 200/MOCK al repetir la consulta, sin acreditar G1→G6 REAL. Ver [corte H3](../CORTE-H3-Y-TRASPASO-H4.md). Revisar DoD FE/BE, casos positivos y negativos, INT y QA en H4.

## Corte planificado de H4

**Objetivo de cierre H4.** Integrar búsqueda REAL por texto/canal con producto vendible, vacío/error/timeout, parámetros y evidencia desde la web desplegada.

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
| TASK-F007-FE-001 | Frontend | Giuliano Macchiavello | Sebastian Malca | P0 | TASK-TRANS-S01-OPS-001 | 9/H4 (arrastre H3) | En revisión |
| TASK-F007-BE-001 | Backend | Giuliano Macchiavello | Sebastian Malca | P0 | TASK-TRANS-S01-OPS-001 | 9/H4 (arrastre H3) | En revisión |
| TASK-F007-INT-001 | Integración | Giuliano Macchiavello | Sebastian Malca | P0 | TASK-F007-BE-001 + I-01 + TASK-F006-INT-001 | 9/H4 (arrastre H3) | Bloqueado |
| TASK-F007-QA-001 | QA funcional | Giuliano Macchiavello | Sebastian Malca | P0 | TASK-F007-FE-001 + TASK-F007-BE-001 | 9/H4 (arrastre H3) | Pendiente |
| TASK-F007-QA-002 | QA seguridad / DevSecOps | Giuliano Macchiavello | Sebastian Malca | P0 | TASK-F007-FE-001 + TASK-F007-BE-001 + TASK-TRANS-S01-OPS-002 | 9/H4 (arrastre H3) | Pendiente |
| TASK-F007-DOC-001 | Documentación | Giuliano Macchiavello | Sebastian Malca | P0 | H4 diseño/implementación: specs y pruebas locales; cierre completo: TASK-F007-INT-001 + TASK-F007-QA-001 + TASK-F007-QA-002 | 9/H4 (arrastre H3) | Pendiente |

La auditoría BD/OPS S1 se propone para Andres; ver [transversales](TRANSVERSALES.md). Los IDs DOC/OPS son extensiones de tareas, no specs. El buscador compartido de Giuliano se coordina con Sebastian sin duplicar estos IDs.

## Trabajo, Definition of Done y evidencia

### TASK-F007-FE-001

- **Trabajo:** Implementar SearchBox, SearchResultsHeading y todos los estados de React/UI.
- **Terminado cuando:** Props/eventos tipados, estado específico, sin requests internos navegador; desktop/mobile aplicables y casos de spec React cubiertos.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F007-BE-001

- **Trabajo:** Validar q de 2–120 caracteres y adaptar búsqueda paginada pública, proteger query de logs identificables.
- **Terminado cuando:** DTO, validación, errores y ownership probados con fixtures; transacciones/versiones donde aplica. Adaptador real no activado si gate externo sigue abierto.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F007-INT-001

- **Trabajo:** Homologar y probar integración real y condiciones: I-01; no sólo fixture.
- **Terminado cuando:** Contrato/configuración y gates enlazados, pruebas positivas/negativas y timeout autorizadas pasan; evidencia distingue sandbox de mock.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Falta cierre documentado de I-01. Contrato/configuración y prueba enlazados antes de cambiar a En progreso.

### TASK-F007-QA-001

- **Trabajo:** Probar 1 y 121 caracteres no consultan; query vacía vuelve catálogo; respuesta lenta anterior no reemplaza nueva; cero resultados conserva q y limpiar; incluir cada estado visual y transición documentada.
- **Terminado cuando:** Casos unitarios/componentes/API y E2E aplicables pasan con evidencias; pruebas mock y reales etiquetadas. Hallazgos corregidos/reprobados.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F007-QA-002

- **Trabajo:** Entradas XSS/inyección y longitudes, consulta pública sin datos privados.
- **Terminado cuando:** Negativos de seguridad pasan en entorno propio/autorizado, scans SAST/SCA/secrets y DAST aplicable adjuntos sin secretos. Sin hallazgo crítico/alto explotable abierto.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F007-DOC-001

- **Trabajo:** Actualizar trazabilidad specs↔implementación↔pruebas, enlaces Figma y decisiones resueltas; documentar operación/errores relevantes.
- **Terminado cuando:** Fuentes vigentes coherentes, evidencias reales y revisión independiente; no marcar funcionalidad terminada con integración pendiente.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.


## Registro de revisión

| Fecha/semana | Cambios de estado | Evidencia / bloqueo / decisión | Revisó |
|---|---|---|---|
| Semana 6, preparación | Creación de tareas; sin ejecución | Specs y plan elaborados; integración pendiente donde se indica | Revisión humana pendiente |

Actualizar filas existentes; no crear un segundo conjunto de tareas por variante desktop/mobile ni por cada estado visual. Si hace falta dividir una tarea, conservar ID padre y crear sufijo incremental con alcance/existencia verificable.
