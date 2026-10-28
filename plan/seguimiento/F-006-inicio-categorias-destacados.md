# Tareas y seguimiento — F-006 Visualizar inicio, categorías y destacados

Versión 0.2.0 · Revisión 2026-10-18. Hay código integrado y demo local parcial; el gate F-006 en nube permanece abierto y pasa a H4.

## Fuente y control

- [Plan F-006](../funcionalidades/F-006-inicio-categorias-destacados.md); [iteración S02/H4](../iteraciones/S02-semanas-09-11.md).
- [Funcional](../../SPECS/funcional/F-006-inicio-categorias-destacados.md), [UI](../../SPECS/ui/F-006-inicio-categorias-destacados.md), [API](../../SPECS/contrato-api/F-006-inicio-categorias-destacados.md), [React](../../SPECS/componentes-react/F-006-inicio-categorias-destacados.md).
- [Reglas del seguimiento](README.md), [pruebas/DevSecOps](../DEVSECOPS-Y-PRUEBAS.md), [gates](../DECISIONES-Y-BLOQUEOS.md).
- Responsable asignado por el PO: **Giuliano Macchiavello**; revisor principal: **Sebastian Malca** según la [matriz](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md). Estimación base fijada en la matriz; ejecución y evidencia pendientes. La semana objetivo es académica, no fecha de calendario.
- Mock y real se reportan por separado. FE [#3](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/pull/3)/[#12](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/pull/12) y BE [#11](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/pull/11)/[#19](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/pull/19) están integradas. La [prueba local de categorías G6](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/blob/f821e9e/docs/INTEGRACION-G6-H3.md) no acredita la ruta pública completa; el [corte H3](../CORTE-H3-Y-TRASPASO-H4.md) distingue la web demo 200/MOCK de Productos REAL. Revisar DoD de FE/BE y ejecutar INT/QA en H4 antes de cambiar a Terminado.

## Corte planificado de H4

**Objetivo de cierre H4.** Integrar inicio/categorías/productos elegibles con G6 REAL y traza web→BFF→G6. Resolver campos de tarjetas y curaduría; destacados omitidos no acreditan su criterio de cierre.

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
| TASK-F006-FE-001 | Frontend | Giuliano Macchiavello | Sebastian Malca | P0 | TASK-TRANS-S01-OPS-001 | 9/H4 (arrastre H3) | En revisión |
| TASK-F006-BE-001 | Backend | Giuliano Macchiavello | Sebastian Malca | P0 | TASK-TRANS-S01-OPS-001 | 9/H4 (arrastre H3) | En revisión |
| TASK-F006-INT-001 | Integración | Giuliano Macchiavello | Sebastian Malca | P0 | TASK-F006-BE-001 + I-01 | 9/H4 (arrastre H3) | Bloqueado |
| TASK-F006-QA-001 | QA funcional | Giuliano Macchiavello | Sebastian Malca | P0 | TASK-F006-FE-001 + TASK-F006-BE-001 | 9/H4 (arrastre H3) | En progreso |
| TASK-F006-QA-002 | QA seguridad / DevSecOps | Giuliano Macchiavello | Sebastian Malca | P0 | TASK-F006-FE-001 + TASK-F006-BE-001 + TASK-TRANS-S01-OPS-002 | 9/H4 (arrastre H3) | En progreso |
| TASK-F006-DOC-001 | Documentación | Giuliano Macchiavello | Sebastian Malca | P0 | H4 diseño/implementación: specs y pruebas locales; cierre completo: TASK-F006-INT-001 + TASK-F006-QA-001 + TASK-F006-QA-002 | 9/H4 (arrastre H3) | En progreso |

La auditoría BD/OPS S1 se propone para Andres; ver [transversales](TRANSVERSALES.md). Los IDs DOC/OPS son extensiones de tareas, no specs. Los aportes de shell/buscador de Giuliano se coordinan con Fernando y Sebastian sin duplicar estos IDs.

## Trabajo, Definition of Done y evidencia

### TASK-F006-FE-001

- **Trabajo:** Implementar HomePageContainer, CategoryGrid, FeaturedProducts y todos los estados de React/UI.
- **Terminado cuando:** Props/eventos tipados, estado específico, sin requests internos navegador; desktop/mobile aplicables y casos de spec React cubiertos.
- **Evidencia:** [Auditoría individual, commits, pruebas y relaciones del 28/10/2026](../evidencias/H4-GIULIANO-AUDITORIA-ISSUES-2026-10-28.md). Implementación local y REAL de demo separadas de revisión/despliegue.
- **Bloqueo / liberación:** Revisión independiente del revisor asignado (Sebastian), con resolución y nueva revisión de las observaciones de Leo. Evidencia del corte desplegado y cierre de las dependencias OPS aplicables; la web pública todavía devolvió 503 el 28/10. Faltan curaduría/campos de destacados (G-FEATURED, Jim/PO y G6) y aceptación del recorrido de favoritos/autenticación aplicable.

### TASK-F006-BE-001

- **Trabajo:** Adaptar home Catálogo, filtrar tarjetas/categorías activas completas y permitir listas vacías.
- **Terminado cuando:** DTO, validación, errores y ownership probados con fixtures; transacciones/versiones donde aplica. Adaptador real no activado si gate externo sigue abierto.
- **Evidencia:** [Auditoría individual, commits, pruebas y relaciones del 28/10/2026](../evidencias/H4-GIULIANO-AUDITORIA-ISSUES-2026-10-28.md). Implementación local y REAL de demo separadas de revisión/despliegue.
- **Bloqueo / liberación:** Revisión independiente del revisor asignado (Sebastian), con resolución y nueva revisión de las observaciones de Leo. Evidencia del corte desplegado y cierre de las dependencias OPS aplicables; la web pública todavía devolvió 503 el 28/10. Faltan curaduría/campos de destacados (G-FEATURED, Jim/PO y G6) y aceptación del recorrido de favoritos/autenticación aplicable.

### TASK-F006-INT-001

- **Trabajo:** Homologar y probar integración real y condiciones: I-01; no sólo fixture.
- **Terminado cuando:** Contrato/configuración y gates enlazados, pruebas positivas/negativas y timeout autorizadas pasan; evidencia distingue sandbox de mock.
- **Evidencia:** [Auditoría individual, commits, pruebas y relaciones del 28/10/2026](../evidencias/H4-GIULIANO-AUDITORIA-ISSUES-2026-10-28.md). Implementación local y REAL de demo separadas de revisión/despliegue.
- **Bloqueo / liberación:** Revisión independiente del revisor asignado (Sebastian), con resolución y nueva revisión de las observaciones de Leo. Evidencia del corte desplegado y cierre de las dependencias OPS aplicables; la web pública todavía devolvió 503 el 28/10. Liberar I-01 con contrato/configuración autorizada, grant técnico y positivos/negativos/timeout desde web→BFF→G6. Faltan curaduría/campos de destacados (G-FEATURED, Jim/PO y G6) y aceptación del recorrido de favoritos/autenticación aplicable.

### TASK-F006-QA-001

- **Trabajo:** Probar ambos arreglos vacíos ofrecen catálogo; error no rompe cabecera; categoría genera URL válida; favorito sin sesión abre O-003; incluir cada estado visual y transición documentada.
- **Terminado cuando:** Casos unitarios/componentes/API y E2E aplicables pasan con evidencias; pruebas mock y reales etiquetadas. Hallazgos corregidos/reprobados.
- **Evidencia:** [Auditoría individual, commits, pruebas y relaciones del 28/10/2026](../evidencias/H4-GIULIANO-AUDITORIA-ISSUES-2026-10-28.md). Implementación local y REAL de demo separadas de revisión/despliegue.
- **Bloqueo / liberación:** Revisión independiente del revisor asignado (Sebastian), con resolución y nueva revisión de las observaciones de Leo. Evidencia del corte desplegado y cierre de las dependencias OPS aplicables; la web pública todavía devolvió 503 el 28/10. Faltan curaduría/campos de destacados (G-FEATURED, Jim/PO y G6) y aceptación del recorrido de favoritos/autenticación aplicable.

### TASK-F006-QA-002

- **Trabajo:** Producto inactivo no publicable, enlaces hero seguros y medios allowlist.
- **Terminado cuando:** Negativos de seguridad pasan en entorno propio/autorizado, scans SAST/SCA/secrets y DAST aplicable adjuntos sin secretos. Sin hallazgo crítico/alto explotable abierto.
- **Evidencia:** [Auditoría individual, commits, pruebas y relaciones del 28/10/2026](../evidencias/H4-GIULIANO-AUDITORIA-ISSUES-2026-10-28.md). Implementación local y REAL de demo separadas de revisión/despliegue.
- **Bloqueo / liberación:** Revisión independiente del revisor asignado (Sebastian), con resolución y nueva revisión de las observaciones de Leo. Evidencia del corte desplegado y cierre de las dependencias OPS aplicables; la web pública todavía devolvió 503 el 28/10. Completar DAST aplicable en staging autorizado y revisión independiente de riesgos; los scans locales/CI no certifican ese paso. Faltan curaduría/campos de destacados (G-FEATURED, Jim/PO y G6) y aceptación del recorrido de favoritos/autenticación aplicable.

### TASK-F006-DOC-001

- **Trabajo:** Actualizar trazabilidad specs↔implementación↔pruebas, enlaces Figma y decisiones resueltas; documentar operación/errores relevantes.
- **Terminado cuando:** Fuentes vigentes coherentes, evidencias reales y revisión independiente; no marcar funcionalidad terminada con integración pendiente.
- **Evidencia:** [Auditoría individual, commits, pruebas y relaciones del 28/10/2026](../evidencias/H4-GIULIANO-AUDITORIA-ISSUES-2026-10-28.md). Implementación local y REAL de demo separadas de revisión/despliegue.
- **Bloqueo / liberación:** Revisión independiente del revisor asignado (Sebastian), con resolución y nueva revisión de las observaciones de Leo. Evidencia del corte desplegado y cierre de las dependencias OPS aplicables; la web pública todavía devolvió 503 el 28/10. Validación independiente de la documentación y cierre de INT/QA-001/QA-002 de esta misma función. Faltan curaduría/campos de destacados (G-FEATURED, Jim/PO y G6) y aceptación del recorrido de favoritos/autenticación aplicable.


## Avance H4 de Giuliano — 26/10/2026

Implementación/pruebas propias actualizadas en las ramas `feat/giuliano-hito4` de FE y BE. [Evidencia del corte, comandos y resultados](../evidencias/H4-GIULIANO-2026-10-26.md). FE/BE de F-006/F-007 conservan revisión pendiente; el trabajo nuevo de F-008–F-010 y QA/DOC queda En progreso hasta revisión y DoD. Ninguna INT se cierra por los tests locales.

Se comprobaron categorías y búsqueda positiva/vacía por Next→BFF→G6 en el modo histórico demo sin JWT; no acredita grants técnicos ni despliegue. Marcas devolvió 503 y página/orden/filtros conservan fallos de integración por operación. Destacados, homologación de API/visual, revisión independiente y aceptación siguen pendientes. Los cuatro niveles de evidencia se detallan en la nota; no se infieren entre sí.

## Registro de revisión

Avance local del 14/10/2026: [evidencia individual y límites](../evidencias/H3-GIULIANO/H3-GIULIANO-CATALOGO-2026-10-14.md). Inicio/categorías y ruta BFF preparados con fixtures MOCK, pruebas locales y build; revisión independiente y cierre de dependencias pendientes. INT sigue bloqueada por I-01; destacados permanecen vacíos por G-FEATURED. QA-001 refleja ejecución local parcial, no QA REAL ni aceptación. Los resultados iniciales pendientes de las fichas de tarea se complementan con esta evidencia, sin declarar Done.

| Fecha/semana | Cambios de estado | Evidencia / bloqueo / decisión | Revisó |
|---|---|---|---|
| Semana 6, preparación | Creación de tareas; sin ejecución | Specs y plan elaborados; integración pendiente donde se indica | Revisión humana pendiente |
| 14/10/2026, avance local | FE/BE/QA-001 en progreso; INT bloqueada | Corte MOCK, pruebas/build y evidencia enlazada; ninguna tarea terminada | Revisión de Sebastian/Leonidas pendiente |
| 16/10/2026, automatización H3 | QA-002 y DOC-001 en progreso; INT sigue bloqueada | [Pruebas, seguridad, CI y límites](../evidencias/H3-GIULIANO/H3-AUTONOMIA-2026-10-16.md); [paquete de entrega](../entrega/H3-GIULIANO.md). FE/BE/QA-001 mantienen estado hasta revisión | Revisión humana pendiente |

Actualizar filas existentes; no crear un segundo conjunto de tareas por variante desktop/mobile ni por cada estado visual. Si hace falta dividir una tarea, conservar ID padre y crear sufijo incremental con alcance/existencia verificable.


## Auditoría por issue — 28/10/2026

[Resultado individual y pendientes verificables](../evidencias/H4-GIULIANO-AUDITORIA-ISSUES-2026-10-28.md). Se actualizan los estados del avance propio del tablero; ninguna tarea se declara Terminado ni issue cerrada. Las notas anteriores se conservan como cortes históricos, no como estado vigente de las pruebas.
