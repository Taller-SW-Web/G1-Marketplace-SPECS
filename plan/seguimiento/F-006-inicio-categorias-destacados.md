# Tareas y seguimiento — F-006 Visualizar inicio, categorías y destacados

Versión 0.2.0 · Avance local parcial MOCK registrado el 14/10/2026; integración, revisión y cierre pendientes.

## Fuente y control

- [Plan F-006](../funcionalidades/F-006-inicio-categorias-destacados.md); [iteración S1](../iteraciones/S01-semanas-07-08.md).
- [Funcional](../../SPECS/funcional/F-006-inicio-categorias-destacados.md), [UI](../../SPECS/ui/F-006-inicio-categorias-destacados.md), [API](../../SPECS/contrato-api/F-006-inicio-categorias-destacados.md), [React](../../SPECS/componentes-react/F-006-inicio-categorias-destacados.md).
- [Reglas del seguimiento](README.md), [pruebas/DevSecOps](../DEVSECOPS-Y-PRUEBAS.md), [gates](../DECISIONES-Y-BLOQUEOS.md).
- Responsable asignado por el PO: **Giuliano Macchiavello**; revisor principal: **Sebastian Malca** según la [matriz](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md). Estimación base fijada en la matriz; ejecución y evidencia pendientes. La semana objetivo es académica, no fecha de calendario.
- Mock y real se reportan por separado. QA local puede avanzar con fixtures; QA real requiere INT. La evidencia local del 14/10 está enlazada en el registro; no acredita QA REAL.

## Tablero

| ID | Área | Responsable | Revisor | Prioridad | Depende de | Semana objetivo | Estado |
|---|---|---|---|---|---|---|---|
| TASK-F006-FE-001 | Frontend | Giuliano Macchiavello | Sebastian Malca | P0 | TASK-TRANS-S01-OPS-001 | 7 | En progreso |
| TASK-F006-BE-001 | Backend | Giuliano Macchiavello | Sebastian Malca | P0 | TASK-TRANS-S01-OPS-001 | 7 | En progreso |
| TASK-F006-INT-001 | Integración | Giuliano Macchiavello | Sebastian Malca | P0 | TASK-F006-BE-001 + I-01 | 8 | Bloqueado |
| TASK-F006-QA-001 | QA funcional | Giuliano Macchiavello | Sebastian Malca | P0 | TASK-F006-FE-001 + TASK-F006-BE-001 | 8 | En progreso |
| TASK-F006-QA-002 | QA seguridad / DevSecOps | Giuliano Macchiavello | Sebastian Malca | P0 | TASK-F006-FE-001 + TASK-F006-BE-001 + TASK-TRANS-S01-OPS-002 | 8 | Pendiente |
| TASK-F006-DOC-001 | Documentación | Giuliano Macchiavello | Sebastian Malca | P0 | TASK-F006-INT-001 + TASK-F006-QA-001 + TASK-F006-QA-002 | 8 | Pendiente |

La auditoría BD/OPS S1 se propone para Andres; ver [transversales](TRANSVERSALES.md). Los IDs DOC/OPS son extensiones de tareas, no specs. Los aportes de shell/buscador de Giuliano se coordinan con Fernando y Sebastian sin duplicar estos IDs.

## Trabajo, Definition of Done y evidencia

### TASK-F006-FE-001

- **Trabajo:** Implementar HomePageContainer, CategoryGrid, FeaturedProducts y todos los estados de React/UI.
- **Terminado cuando:** Props/eventos tipados, estado específico, sin requests internos navegador; desktop/mobile aplicables y casos de spec React cubiertos.
- **Evidencia:** [Corte local y verificaciones del 14/10](../evidencias/H3-GIULIANO-CATALOGO-2026-10-14.md): home/categorías, vacío/error, responsive y pruebas de navegador MOCK. Revisión independiente pendiente.
- **Bloqueo / liberación:** G-SHELL/G-STACK y conformidad de tarjeta/frames pendientes; respetar dependencias y Ready para cierre.

### TASK-F006-BE-001

- **Trabajo:** Adaptar home Catálogo, filtrar tarjetas/categorías activas completas y permitir listas vacías.
- **Terminado cuando:** DTO, validación, errores y ownership probados con fixtures; transacciones/versiones donde aplica. Adaptador real no activado si gate externo sigue abierto.
- **Evidencia:** [BFF y pruebas locales](../evidencias/H3-GIULIANO-CATALOGO-2026-10-14.md): ruta home, categorías activas y adaptador candidato con respuestas sintéticas. Revisión de Leonidas/Sebastian pendiente.
- **Bloqueo / liberación:** I-01 sin configuración/prueba real; G-FEATURED mantiene destacados vacíos. La implementación local no libera INT.

### TASK-F006-INT-001

- **Trabajo:** Homologar y probar integración real y condiciones: I-01; no sólo fixture.
- **Terminado cuando:** Contrato/configuración y gates enlazados, pruebas positivas/negativas y timeout autorizadas pasan; evidencia distingue sandbox de mock.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Falta cierre documentado de I-01. Contrato/configuración y prueba enlazados antes de cambiar a En progreso.

### TASK-F006-QA-001

- **Trabajo:** Probar ambos arreglos vacíos ofrecen catálogo; error no rompe cabecera; categoría genera URL válida; favorito sin sesión abre O-003; incluir cada estado visual y transición documentada.
- **Terminado cuando:** Casos unitarios/componentes/API y E2E aplicables pasan con evidencias; pruebas mock y reales etiquetadas. Hallazgos corregidos/reprobados.
- **Evidencia:** [Resultados y retest MOCK](../evidencias/H3-GIULIANO-CATALOGO-2026-10-14.md): ejecución de pruebas BFF y navegador; inicio vacío, categorías y errores incluidos.
- **Bloqueo / liberación:** QA parcial local; favorito/auth, revisión y cobertura real requieren sus dependencias. No es aceptación completa de F-006.

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

Avance local del 14/10/2026: [evidencia individual y límites](../evidencias/H3-GIULIANO-CATALOGO-2026-10-14.md). Inicio/categorías y ruta BFF preparados con fixtures MOCK, pruebas locales y build; revisión independiente y cierre de dependencias pendientes. INT sigue bloqueada por I-01; destacados permanecen vacíos por G-FEATURED. QA-001 refleja ejecución local parcial, no QA REAL ni aceptación. Los resultados iniciales pendientes de las fichas de tarea se complementan con esta evidencia, sin declarar Done.

| Fecha/semana | Cambios de estado | Evidencia / bloqueo / decisión | Revisó |
|---|---|---|---|
| Semana 6, preparación | Creación de tareas; sin ejecución | Specs y plan elaborados; integración pendiente donde se indica | Revisión humana pendiente |
| 14/10/2026, avance local | FE/BE/QA-001 en progreso; INT bloqueada | Corte MOCK, pruebas/build y evidencia enlazada; ninguna tarea terminada | Revisión de Sebastian/Leonidas pendiente |

Actualizar filas existentes; no crear un segundo conjunto de tareas por variante desktop/mobile ni por cada estado visual. Si hace falta dividir una tarea, conservar ID padre y crear sufijo incremental con alcance/existencia verificable.
