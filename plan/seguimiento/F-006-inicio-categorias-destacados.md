# Tareas y seguimiento — F-006 Visualizar inicio, categorías y destacados

Versión 0.2.0 · Revisión 2026-10-18. Hay código integrado y demo local parcial; el gate F-006 en nube permanece abierto y pasa a H4.

## Fuente y control

- [Plan F-006](../funcionalidades/F-006-inicio-categorias-destacados.md); [iteración S1](../iteraciones/S01-semanas-07-08.md).
- [Funcional](../../SPECS/funcional/F-006-inicio-categorias-destacados.md), [UI](../../SPECS/ui/F-006-inicio-categorias-destacados.md), [API](../../SPECS/contrato-api/F-006-inicio-categorias-destacados.md), [React](../../SPECS/componentes-react/F-006-inicio-categorias-destacados.md).
- [Reglas del seguimiento](README.md), [pruebas/DevSecOps](../DEVSECOPS-Y-PRUEBAS.md), [gates](../DECISIONES-Y-BLOQUEOS.md).
- Responsable asignado por el PO: **Giuliano Macchiavello**; revisor principal: **Sebastian Malca** según la [matriz](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md). Estimación base fijada en la matriz; ejecución y evidencia pendientes. La semana objetivo es académica, no fecha de calendario.
- Mock y real se reportan por separado. FE [#3](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/pull/3)/[#12](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/pull/12) y BE [#11](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/pull/11)/[#19](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/pull/19) están integradas. La [prueba local de categorías G6](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/blob/f821e9e/docs/INTEGRACION-G6-H3.md) no acredita la ruta pública completa; el [corte H3](../CORTE-H3-Y-TRASPASO-H4.md) distingue la web demo 200/MOCK de Productos REAL. Revisar DoD de FE/BE y ejecutar INT/QA en H4 antes de cambiar a Terminado.

## Tablero

| ID | Área | Responsable | Revisor | Prioridad | Depende de | Semana objetivo | Estado |
|---|---|---|---|---|---|---|---|
| TASK-F006-FE-001 | Frontend | Giuliano Macchiavello | Sebastian Malca | P0 | TASK-TRANS-S01-OPS-001 | 7 → 9/H4 | En revisión |
| TASK-F006-BE-001 | Backend | Giuliano Macchiavello | Sebastian Malca | P0 | TASK-TRANS-S01-OPS-001 | 7 → 9/H4 | En revisión |
| TASK-F006-INT-001 | Integración | Giuliano Macchiavello | Sebastian Malca | P0 | TASK-F006-BE-001 + I-01 | 8 → 9/H4 | Bloqueado |
| TASK-F006-QA-001 | QA funcional | Giuliano Macchiavello | Sebastian Malca | P0 | TASK-F006-FE-001 + TASK-F006-BE-001 | 8 → 9/H4 | Pendiente |
| TASK-F006-QA-002 | QA seguridad / DevSecOps | Giuliano Macchiavello | Sebastian Malca | P0 | TASK-F006-FE-001 + TASK-F006-BE-001 + TASK-TRANS-S01-OPS-002 | 8 → 9/H4 | Pendiente |
| TASK-F006-DOC-001 | Documentación | Giuliano Macchiavello | Sebastian Malca | P0 | TASK-F006-INT-001 + TASK-F006-QA-001 + TASK-F006-QA-002 | 8 → 9/H4 | Pendiente |

La auditoría BD/OPS S1 se propone para Andres; ver [transversales](TRANSVERSALES.md). Los IDs DOC/OPS son extensiones de tareas, no specs. Los aportes de shell/buscador de Giuliano se coordinan con Fernando y Sebastian sin duplicar estos IDs.

## Trabajo, Definition of Done y evidencia

### TASK-F006-FE-001

- **Trabajo:** Implementar HomePageContainer, CategoryGrid, FeaturedProducts y todos los estados de React/UI.
- **Terminado cuando:** Props/eventos tipados, estado específico, sin requests internos navegador; desktop/mobile aplicables y casos de spec React cubiertos.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F006-BE-001

- **Trabajo:** Adaptar home Catálogo, filtrar tarjetas/categorías activas completas y permitir listas vacías.
- **Terminado cuando:** DTO, validación, errores y ownership probados con fixtures; transacciones/versiones donde aplica. Adaptador real no activado si gate externo sigue abierto.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F006-INT-001

- **Trabajo:** Homologar y probar integración real y condiciones: I-01; no sólo fixture.
- **Terminado cuando:** Contrato/configuración y gates enlazados, pruebas positivas/negativas y timeout autorizadas pasan; evidencia distingue sandbox de mock.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Falta cierre documentado de I-01. Contrato/configuración y prueba enlazados antes de cambiar a En progreso.

### TASK-F006-QA-001

- **Trabajo:** Probar ambos arreglos vacíos ofrecen catálogo; error no rompe cabecera; categoría genera URL válida; favorito sin sesión abre O-003; incluir cada estado visual y transición documentada.
- **Terminado cuando:** Casos unitarios/componentes/API y E2E aplicables pasan con evidencias; pruebas mock y reales etiquetadas. Hallazgos corregidos/reprobados.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F006-QA-002

- **Trabajo:** Producto inactivo no publicable, enlaces hero seguros y medios allowlist.
- **Terminado cuando:** Negativos de seguridad pasan en entorno propio/autorizado, scans SAST/SCA/secrets y DAST aplicable adjuntos sin secretos. Sin hallazgo crítico/alto explotable abierto.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F006-DOC-001

- **Trabajo:** Actualizar trazabilidad specs↔implementación↔pruebas, enlaces Figma y decisiones resueltas; documentar operación/errores relevantes.
- **Terminado cuando:** Fuentes vigentes coherentes, evidencias reales y revisión independiente; no marcar funcionalidad terminada con integración pendiente.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.


## Registro de revisión

| Fecha/semana | Cambios de estado | Evidencia / bloqueo / decisión | Revisó |
|---|---|---|---|
| Semana 6, preparación | Creación de tareas; sin ejecución | Specs y plan elaborados; integración pendiente donde se indica | Revisión humana pendiente |

Actualizar filas existentes; no crear un segundo conjunto de tareas por variante desktop/mobile ni por cada estado visual. Si hace falta dividir una tarea, conservar ID padre y crear sufijo incremental con alcance/existencia verificable.
