# Tareas y seguimiento — F-008 Filtrar catálogo

Versión 0.1.0 · Planificación inicial · F-008 no está implementada por estos documentos.

## Fuente y control

- [Plan F-008](../funcionalidades/F-008-filtrar-catalogo.md); [iteración S02/H4](../iteraciones/S02-semanas-09-11.md).
- [Funcional](../../SPECS/funcional/F-008-filtrar-catalogo.md), [UI](../../SPECS/ui/F-008-filtrar-catalogo.md), [API](../../SPECS/contrato-api/F-008-filtrar-catalogo.md), [React](../../SPECS/componentes-react/F-008-filtrar-catalogo.md).
- [Reglas del seguimiento](README.md), [pruebas/DevSecOps](../DEVSECOPS-Y-PRUEBAS.md), [gates](../DECISIONES-Y-BLOQUEOS.md).
- Responsable asignado por el PO: **Giuliano Macchiavello**; revisor principal: **Sebastian Malca** según la [matriz](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md). Estimación base fijada en la matriz; ejecución y evidencia pendientes. La semana objetivo es académica, no fecha de calendario.
- Mock y real se reportan por separado. QA local puede avanzar con fixtures; QA real requiere INT. Evidencia inicial pendiente, no pruebas ejecutadas.

## Corte planificado de H4

**Objetivo de cierre H4.** Integrar filtros soportados y homologados con G6; probar combinación/reset de página/vacío/error. No activar filtros sin semántica contractual.

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
| TASK-F008-FE-001 | Frontend | Giuliano Macchiavello | Sebastian Malca | P1 | TASK-TRANS-S01-OPS-001 | 9–10/H4 | En revisión |
| TASK-F008-BE-001 | Backend | Giuliano Macchiavello | Sebastian Malca | P1 | TASK-TRANS-S01-OPS-001 | 9–10/H4 | En revisión |
| TASK-F008-INT-001 | Integración | Giuliano Macchiavello | Sebastian Malca | P1 | TASK-F008-BE-001 + I-01 + TASK-F007-INT-001 | 11/H4 | Bloqueado |
| TASK-F008-QA-001 | QA funcional | Giuliano Macchiavello | Sebastian Malca | P1 | TASK-F008-FE-001 + TASK-F008-BE-001 | 11/H4 | En progreso |
| TASK-F008-QA-002 | QA seguridad / DevSecOps | Giuliano Macchiavello | Sebastian Malca | P1 | TASK-F008-FE-001 + TASK-F008-BE-001 + TASK-TRANS-S02-OPS-002 | 11/H4 | En progreso |
| TASK-F008-DOC-001 | Documentación | Giuliano Macchiavello | Sebastian Malca | P1 | H4 diseño/implementación: specs y pruebas locales; cierre completo: TASK-F008-INT-001 + TASK-F008-QA-001 + TASK-F008-QA-002 | 11/H4 | En progreso |

Referente de BD: Giuliano Macchiavello para este bloque, con revisión de Sebastian Malca; Andres mantiene soporte transversal de migraciones. Ver [matriz](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md).

## Trabajo, Definition of Done y evidencia

### TASK-F008-FE-001

- **Trabajo:** Implementar CatalogFilters, ActiveFilterChips y todos los estados de React/UI.
- **Terminado cuando:** Props/eventos tipados, estado específico, sin requests internos navegador; desktop/mobile aplicables y casos de spec React cubiertos.
- **Evidencia:** [Auditoría individual, commits, pruebas y relaciones del 28/10/2026](../evidencias/H4-GIULIANO-AUDITORIA-ISSUES-2026-10-28.md). Implementación local y REAL de demo separadas de revisión/despliegue.
- **Bloqueo / liberación:** Revisión independiente del revisor asignado (Sebastian), con resolución y nueva revisión de las observaciones de Leo. Evidencia del corte desplegado y cierre de las dependencias OPS aplicables; la web pública todavía devolvió 503 el 28/10. G6 sigue 503 en marcas (Caddy) y precio (SERVICIO_NO_DISPONIBLE); falta soporte autorizado por operación además de homologar el contrato singular.

### TASK-F008-BE-001

- **Trabajo:** Mapear IDs categoría/marca/rango PEN a proveedor, validar AND/min<=max y maestros autorizados.
- **Terminado cuando:** DTO, validación, errores y ownership probados con fixtures; transacciones/versiones donde aplica. Adaptador real no activado si gate externo sigue abierto.
- **Evidencia:** [Auditoría individual, commits, pruebas y relaciones del 28/10/2026](../evidencias/H4-GIULIANO-AUDITORIA-ISSUES-2026-10-28.md). Implementación local y REAL de demo separadas de revisión/despliegue.
- **Bloqueo / liberación:** Revisión independiente del revisor asignado (Sebastian), con resolución y nueva revisión de las observaciones de Leo. Evidencia del corte desplegado y cierre de las dependencias OPS aplicables; la web pública todavía devolvió 503 el 28/10. G6 sigue 503 en marcas (Caddy) y precio (SERVICIO_NO_DISPONIBLE); falta soporte autorizado por operación además de homologar el contrato singular.

### TASK-F008-INT-001

- **Trabajo:** Homologar y probar integración real y condiciones: I-01; no sólo fixture.
- **Terminado cuando:** Contrato/configuración y gates enlazados, pruebas positivas/negativas y timeout autorizadas pasan; evidencia distingue sandbox de mock.
- **Evidencia:** [Auditoría individual, commits, pruebas y relaciones del 28/10/2026](../evidencias/H4-GIULIANO-AUDITORIA-ISSUES-2026-10-28.md). Implementación local y REAL de demo separadas de revisión/despliegue.
- **Bloqueo / liberación vigente (27/11/2026):** La issue #53 sigue abierta; Backend #52 está cerrada, mientras I-01 y la dependencia formal Backend #49 siguen pendientes. La traza Render del 26/11 acredita respuestas 200 en los rangos de precio probados, pero el retest del 27/11 quedó bloqueado antes de HTTP por DNS del entorno y no agregó IDs ni metadata de página bajo filtro. Reanudar cuando el BFF sea resoluble desde el runner; completar los GET filtrados y sus trazas, sin inferir aceptación ni cambiar estado. La UI publicada/reset y la revisión independiente también siguen pendientes.

#### Retest propio de precios REAL — 27/11/2026

G6 confirmó `ord-001` (`93f7f500-077d-432e-be98-31cb9ee0d66d`, S/39.90) y `ord-002` (`8ad24563-c9da-4305-b650-1dd47a14fffb`, S/49.90), con igual nombre, categoría y marca. El [registro Render del 26/11](https://github.com/Taller-SW-Web/G1-Marketplace-SPECS/blob/8d9f5df5a537cdd8d1951e8cb4c2f8216c8e7e46/plan/evidencias/h5-giuliano-catalogo/retest-real-render.json) ya documenta S/0–100 y S/0–60 con dos slugs/total 2, y S/0–45 con `ord-001`/total 1. La [evidencia F-009](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/blob/e6b3eb9a3bc816510bc23c7126951799aab8eef9/docs/evidencias/H4/giuliano/2026-11-27/TASK-F009-INT-001-g6-tiebreak.json) vincula los slugs con sus IDs en el BFF REAL sin filtro.

El [runner y resultado Backend](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/blob/1d65b6d8ad14f32015eea17a939ccb501012b43f/docs/evidencias/H4/giuliano/2026-11-27/TASK-F008-INT-001-price-ranges.md) conserva el contrato de parámetros: G1 `minPrice`/`maxPrice` → G6 `precioMin`/`precioMax`; BFF `page=0&pageSize=24` → G6 `pagina=1&tamanio=24`. El caso 0–60 espera `ord-002` → `ord-001`: `NAME_ASC` aplica el desempate confirmado `product_id ASC`; el runner compara la secuencia completa, no sólo el conjunto. La spec local no define inclusividad de extremos; los rangos elegidos no coinciden con los precios conocidos. El único nuevo GET a 0–60 falló antes de HTTP en 72 ms (`NETWORK_OR_TIMEOUT`); `getent ahosts g1-marketplace-backend.onrender.com` no resolvió direcciones, por lo que 0–45 quedó sin ejecutar. No se llama G6 directamente ni se atribuye resultado al caso no ejecutado.

El intento de comentar Backend #53 con este avance devolvió HTTP 403 `Resource not accessible by integration`; se registra aquí y no se cambia el estado de la issue. La fila del tablero conserva **Bloqueado** hasta completar la prueba propia y sus dependencias.

### TASK-F008-QA-001

- **Trabajo:** Probar rango invertido no consulta; aplicar conserva búsqueda y orden; cancelar mobile no cambia filtros; Escape y restauración de foco; incluir cada estado visual y transición documentada.
- **Terminado cuando:** Casos unitarios/componentes/API y E2E aplicables pasan con evidencias; pruebas mock y reales etiquetadas. Hallazgos corregidos/reprobados.
- **Evidencia:** [Auditoría individual, commits, pruebas y relaciones del 28/10/2026](../evidencias/H4-GIULIANO-AUDITORIA-ISSUES-2026-10-28.md). Implementación local y REAL de demo separadas de revisión/despliegue.
- **Bloqueo / liberación:** Revisión independiente del revisor asignado (Sebastian), con resolución y nueva revisión de las observaciones de Leo. Evidencia del corte desplegado y cierre de las dependencias OPS aplicables; la web pública todavía devolvió 503 el 28/10. G6 sigue 503 en marcas (Caddy) y precio (SERVICIO_NO_DISPONIBLE); falta soporte autorizado por operación además de homologar el contrato singular.

### TASK-F008-QA-002

- **Trabajo:** IDs inválidos/rango negativo y manipulación URL, no filtros administrativos.
- **Terminado cuando:** Negativos de seguridad pasan en entorno propio/autorizado, scans SAST/SCA/secrets y DAST aplicable adjuntos sin secretos. Sin hallazgo crítico/alto explotable abierto.
- **Evidencia:** [Auditoría individual, commits, pruebas y relaciones del 28/10/2026](../evidencias/H4-GIULIANO-AUDITORIA-ISSUES-2026-10-28.md). Implementación local y REAL de demo separadas de revisión/despliegue.
- **Bloqueo / liberación:** Revisión independiente del revisor asignado (Sebastian), con resolución y nueva revisión de las observaciones de Leo. Evidencia del corte desplegado y cierre de las dependencias OPS aplicables; la web pública todavía devolvió 503 el 28/10. Completar DAST aplicable en staging autorizado y revisión independiente de riesgos; los scans locales/CI no certifican ese paso. G6 sigue 503 en marcas (Caddy) y precio (SERVICIO_NO_DISPONIBLE); falta soporte autorizado por operación además de homologar el contrato singular.

### TASK-F008-DOC-001

- **Trabajo:** Actualizar trazabilidad specs↔implementación↔pruebas, enlaces Figma y decisiones resueltas; documentar operación/errores relevantes.
- **Terminado cuando:** Fuentes vigentes coherentes, evidencias reales y revisión independiente; no marcar funcionalidad terminada con integración pendiente.
- **Evidencia:** [Auditoría individual, commits, pruebas y relaciones del 28/10/2026](../evidencias/H4-GIULIANO-AUDITORIA-ISSUES-2026-10-28.md). Implementación local y REAL de demo separadas de revisión/despliegue.
- **Bloqueo / liberación:** Revisión independiente del revisor asignado (Sebastian), con resolución y nueva revisión de las observaciones de Leo. Evidencia del corte desplegado y cierre de las dependencias OPS aplicables; la web pública todavía devolvió 503 el 28/10. Validación independiente de la documentación y cierre de INT/QA-001/QA-002 de esta misma función. G6 sigue 503 en marcas (Caddy) y precio (SERVICIO_NO_DISPONIBLE); falta soporte autorizado por operación además de homologar el contrato singular.


## Avance H4 de Giuliano — 26/10/2026

Implementación/pruebas propias actualizadas en las ramas `feat/giuliano-hito4` de FE y BE. [Evidencia del corte, comandos y resultados](../evidencias/H4-GIULIANO-2026-10-26.md). FE/BE de F-006/F-007 conservan revisión pendiente; el trabajo nuevo de F-008–F-010 y QA/DOC queda En progreso hasta revisión y DoD. Ninguna INT se cierra por los tests locales.

Se comprobaron categorías y búsqueda positiva/vacía por Next→BFF→G6 en el modo histórico demo sin JWT; no acredita grants técnicos ni despliegue. Marcas devolvió 503 y página/orden/filtros conservan fallos de integración por operación. Destacados, homologación de API/visual, revisión independiente y aceptación siguen pendientes. Los cuatro niveles de evidencia se detallan en la nota; no se infieren entre sí.

## Registro de revisión

| Fecha/semana | Cambios de estado | Evidencia / bloqueo / decisión | Revisó |
|---|---|---|---|
| Semana 6, preparación | Creación de tareas; sin ejecución | Specs y plan elaborados; integración pendiente donde se indica | Revisión humana pendiente |

Actualizar filas existentes; no crear un segundo conjunto de tareas por variante desktop/mobile ni por cada estado visual. Si hace falta dividir una tarea, conservar ID padre y crear sufijo incremental con alcance/existencia verificable.


## Auditoría por issue — 28/10/2026

[Resultado individual y pendientes verificables](../evidencias/H4-GIULIANO-AUDITORIA-ISSUES-2026-10-28.md). Se actualizan los estados del avance propio del tablero; ninguna tarea se declara Terminado ni issue cerrada. Las notas anteriores se conservan como cortes históricos, no como estado vigente de las pruebas.


## Revisión conjunta local con Jim — registro 28/10/2026

Jim comunicó conformidad con el recorrido local de F-006–F-010 en escritorio y móvil, según el mensaje aportado por Giuliano. [Constancia y límites](../evidencias/H4-GIULIANO-REVISION-CONJUNTA-JIM-2026-10-28.md). La revisión técnica de PR corresponde a Sebas en Frontend y Leo en Backend/contrato, según el circuito indicado. La nota registra evidencia funcional local; despliegue, JWT, marcas y precio conservan sus requisitos. El revisor de la matriz de tareas se conserva mientras no exista una actualización formal de esa asignación.
