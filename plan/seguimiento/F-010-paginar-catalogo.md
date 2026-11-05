# Tareas y seguimiento — F-010 Paginar resultados

**Estado actualizado al 05/11:** implementación principal integrada; [matriz por issue, evidencia y requisito exacto de cierre](../evidencias/H4-GIULIANO-F010-CIERRE-2026-11-05.md). Esta reconciliación prevalece sobre pendientes de registros anteriores. No falta escribir de nuevo la paginación ni conseguir una primera prueba REAL local: ya existe. Falta acreditar el corte publicado y su aceptación.

Versión 0.3.0 · Reconciliación 2026-11-05. Código principal integrado; aceptación y cierre individual según la matriz vigente.

## Fuente y control

- [Plan F-010](../funcionalidades/F-010-paginar-catalogo.md); [iteración S02/H4](../iteraciones/S02-semanas-09-11.md).
- [Funcional](../../SPECS/funcional/F-010-paginar-catalogo.md), [UI](../../SPECS/ui/F-010-paginar-catalogo.md), [API](../../SPECS/contrato-api/F-010-paginar-catalogo.md), [React](../../SPECS/componentes-react/F-010-paginar-catalogo.md).
- [Reglas del seguimiento](README.md), [pruebas/DevSecOps](../DEVSECOPS-Y-PRUEBAS.md), [gates](../DECISIONES-Y-BLOQUEOS.md).
- Responsable asignado por el PO: **Giuliano Macchiavello**; revisor principal: **Sebastian Malca** según la [matriz](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md). Estimación base fijada en la matriz; ejecución/evidencias actualizadas en la reconciliación del 05/11. La semana objetivo es académica, no fecha de calendario.
- Mock y real se reportan por separado. QA local puede avanzar con fixtures; QA real requiere INT. Evidencia inicial pendiente, no pruebas ejecutadas.

## Corte planificado de H4

**Objetivo de cierre H4.** Integrar paginación page 0→pagina 1, tamaño/total/límites/última página y cambios de consulta con G6.

**Cierre base:** S02/H4, semanas 9–11; cierre sólo con gates y prueba en despliegue. Disponibilidad sin restricción horaria por decisión del PO. Las entregas «local» o «con dobles» son etapas del mismo TASK, no cierres de INT. DOC prepara desde specs y QA ejecuta casos propios antes de INT; el cierre completo conserva dependencias/DoD. [Alcance H4](../ALCANCE-H4-PRODUCTOS-SEGURIDAD.md). Los estados no cambian al replanificar.

| Nivel de evidencia | Registro del corte de esta F |
|---|---|
| Diseñado | Specs enlazadas arriba; añadir revisión del flujo/contrato/frame concreto de H4. Su existencia no acredita aprobación de todas las discrepancias |
| Implementado con datos de prueba | Entregas FE #124 y BE #265 fusionadas tras revisión de Jim; commits individuales y pruebas en [matriz del 05/11](../evidencias/H4-GIULIANO-F010-CIERRE-2026-11-05.md). No es falta de implementación inicial |
| Integrado con otro módulo | Reensayo local del 04/11: siete casos PASS de paginación, incluidas primera/siguiente/última/fuera de rango y límites inválidos. No acredita el G1 publicado. Repetir con universo G6 conocido: total, páginas/extremos y ausencia de duplicados observados; verificar desde UI publicada reset y criterios de URL, OPEN-03 y revisión. No presumir snapshot global entre solicitudes. |
| Probado en el despliegue | Sigue pendiente de aceptación: web G1 devuelve CATALOG_TIMEOUT en el sondeo del 05/11 a las 13:45 Lima; BFF directo no responde en 20 s. OPS debe acreditar runtime/SHA/configuración y Giuliano retestar |

La actualización del 19/10/2026 cambia planificación, no estados de ejecución ni aprobación de gates. Registrar aquí evidencia concreta a medida que exista, sin calificar todo el bloque por una sola prueba.

## Tablero

| ID | Área | Responsable | Revisor | Prioridad | Depende de | Semana objetivo | Estado |
|---|---|---|---|---|---|---|---|
| TASK-F010-FE-001 | Frontend | Giuliano Macchiavello | Sebastian Malca | P1 | TASK-TRANS-S01-OPS-001 | 9–10/H4 | En revisión |
| TASK-F010-BE-001 | Backend | Giuliano Macchiavello | Sebastian Malca | P1 | TASK-TRANS-S01-OPS-001 | 9–10/H4 | En revisión |
| TASK-F010-INT-001 | Integración | Giuliano Macchiavello | Sebastian Malca | P1 | TASK-F010-BE-001 + I-01 + TASK-F007-INT-001 | 11/H4 | Bloqueado |
| TASK-F010-QA-001 | QA funcional | Giuliano Macchiavello | Sebastian Malca | P1 | TASK-F010-FE-001 + TASK-F010-BE-001 | 11/H4 | En progreso |
| TASK-F010-QA-002 | QA seguridad / DevSecOps | Giuliano Macchiavello | Sebastian Malca | P1 | TASK-F010-FE-001 + TASK-F010-BE-001 + TASK-TRANS-S02-OPS-002 | 11/H4 | En progreso |
| TASK-F010-DOC-001 | Documentación | Giuliano Macchiavello | Sebastian Malca | P1 | H4 diseño/implementación: specs y pruebas locales; cierre completo: TASK-F010-INT-001 + TASK-F010-QA-001 + TASK-F010-QA-002 | 11/H4 | En progreso |

Referente de BD: Giuliano Macchiavello para este bloque, con revisión de Sebastian Malca; Andres mantiene soporte transversal de migraciones. Ver [matriz](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md).

## Trabajo, Definition of Done y evidencia

### TASK-F010-FE-001

- **Trabajo:** Implementar CatalogPagination y todos los estados de React/UI.
- **Terminado cuando:** Props/eventos tipados, estado específico, sin requests internos navegador; desktop/mobile aplicables y casos de spec React cubiertos.
- **Evidencia:** [Reconciliación individual del 05/11](../evidencias/H4-GIULIANO-F010-CIERRE-2026-11-05.md): commit original, incorporación a develop, PR/reviews/CI y evidencia REAL etiquetada. El historial fechado se conserva debajo.
- **Bloqueo / liberación:** Registrar la aceptación de los criterios FE de esta tarea con Sebastián (estados, props/eventos, desktop/mobile y navegación/URL aplicables) y de su dependencia OPS. El merge revisado por Jim ya está acreditado. Los pendientes de integración de la función no se convierten en falta de implementación del componente. Giuliano aporta la trazabilidad y atiende observaciones; Sebastián valida el DoD asignado, con revisión Backend de Leónidas y dependencia OPS aplicable.

### TASK-F010-BE-001

- **Trabajo:** Validar page/pageSize y mapear meta cero basada, cerrar página fuera de rango.
- **Terminado cuando:** DTO, validación, errores y ownership probados con fixtures; transacciones/versiones donde aplica. Adaptador real no activado si gate externo sigue abierto.
- **Evidencia:** [Reconciliación individual del 05/11](../evidencias/H4-GIULIANO-F010-CIERRE-2026-11-05.md): commit original, incorporación a develop, PR/reviews/CI y evidencia REAL etiquetada. El historial fechado se conserva debajo.
- **Bloqueo / liberación:** Registrar la aceptación del DoD Backend y dependencia OPS con el revisor asignado: DTO, validación, errores y proyección/ownership probados. Jim ya aprobó el merge; Leónidas revisó el alcance MOCK. Los casos REAL pendientes pertenecen al cierre de INT; no exigir reescribir el adaptador ya entregado. Giuliano aporta la trazabilidad y atiende observaciones; Sebastián valida el DoD asignado, con revisión Backend de Leónidas y dependencia OPS aplicable.

### TASK-F010-INT-001

- **Trabajo:** Homologar y probar integración real y condiciones: I-01; no sólo fixture.
- **Terminado cuando:** Contrato/configuración y gates enlazados, pruebas positivas/negativas y timeout autorizadas pasan; evidencia distingue sandbox de mock.
- **Evidencia:** [Reconciliación individual del 05/11](../evidencias/H4-GIULIANO-F010-CIERRE-2026-11-05.md): commit original, incorporación a develop, PR/reviews/CI y evidencia REAL etiquetada. El historial fechado se conserva debajo.
- **Bloqueo / liberación:** Repetir con universo G6 conocido: total, páginas/extremos y ausencia de duplicados observados; verificar desde UI publicada reset y criterios de URL, OPEN-03 y revisión. No presumir snapshot global entre solicitudes. Confirmar configuración/acceso del entorno: public-read-only explícito tras integrar #273, o JWT con grant/emisión verificados. JWT no es un prerrequisito técnico del modo público acordado. Conservar las dependencias formales originales de esta INT. Giuliano: casos/UI/evidencia; G6: dataset/versión/universo; Andrés/Fernando: publicación; Sebastián/Leónidas: revisión aplicable.

### TASK-F010-QA-001

- **Trabajo:** Probar primera no anterior; última no siguiente; cambio criterios vuelve 0; URL inválida ofrece salida controlada; incluir cada estado visual y transición documentada.
- **Terminado cuando:** Casos unitarios/componentes/API y E2E aplicables pasan con evidencias; pruebas mock y reales etiquetadas. Hallazgos corregidos/reprobados.
- **Evidencia:** [Reconciliación individual del 05/11](../evidencias/H4-GIULIANO-F010-CIERRE-2026-11-05.md): commit original, incorporación a develop, PR/reviews/CI y evidencia REAL etiquetada. El historial fechado se conserva debajo.
- **Bloqueo / liberación:** Completar y revisar la matriz por criterio de esta QA con Sebastián/QA, incluyendo el recorrido REAL y los casos pendientes de la función en el entorno acordado. Repetir con universo G6 conocido: total, páginas/extremos y ausencia de duplicados observados; verificar desde UI publicada reset y criterios de URL, OPEN-03 y revisión. No presumir snapshot global entre solicitudes. Las pruebas locales/fixtures ya ejecutadas permanecen como evidencia y no se repiten por rutina. Giuliano: casos/UI/evidencia; G6: dataset/versión/universo; Andrés/Fernando: publicación; Sebastián/Leónidas: revisión aplicable.

### TASK-F010-QA-002

- **Trabajo:** pageSize excesivo/negativo no amplifica consulta, límites contra consumo abusivo.
- **Terminado cuando:** Negativos de seguridad pasan en entorno propio/autorizado, scans SAST/SCA/secrets y DAST aplicable adjuntos sin secretos. Sin hallazgo crítico/alto explotable abierto.
- **Evidencia:** [Reconciliación individual del 05/11](../evidencias/H4-GIULIANO-F010-CIERRE-2026-11-05.md): commit original, incorporación a develop, PR/reviews/CI y evidencia REAL etiquetada. El historial fechado se conserva debajo.
- **Bloqueo / liberación:** Adjuntar/revisar negativos del corte y SAST/SCA/secret scan ya existentes; completar DAST aplicable y revisión de riesgos con Andrés/seguridad en entorno propio/autorizado, corregir/reprobar hallazgos y acreditar la dependencia OPS de la tarea. No confundir controles locales/CI con aceptación de staging. Giuliano ejecuta/adjunta y retesta; Andrés/seguridad y el revisor acuerdan entorno, alcance, riesgos y aceptación.

### TASK-F010-DOC-001

- **Trabajo:** Actualizar trazabilidad specs↔implementación↔pruebas, enlaces Figma y decisiones resueltas; documentar operación/errores relevantes.
- **Terminado cuando:** Fuentes vigentes coherentes, evidencias reales y revisión independiente; no marcar funcionalidad terminada con integración pendiente.
- **Evidencia:** [Reconciliación individual del 05/11](../evidencias/H4-GIULIANO-F010-CIERRE-2026-11-05.md): commit original, incorporación a develop, PR/reviews/CI y evidencia REAL etiquetada. El historial fechado se conserva debajo.
- **Bloqueo / liberación:** Revisión independiente y merge de esta actualización en SPECS #16; coherencia de fuentes/specs/evidencias y dependencias INT/QA funcional/QA seguridad originales satisfechas. El texto y el commit documental ya están entregados; no falta redactar la tarea desde cero. Giuliano actualiza; Sebastián/revisor independiente valida documentación; los owners de INT y QA entregan su cierre.


## Historial anterior al corte vigente del 05/11

Los pendientes/estados de las notas siguientes corresponden a su fecha; no sustituyen la matriz actual enlazada arriba.

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


## Reconciliación por issue — 03/11/2026

[Evidencia actualizada y bloqueos](../evidencias/H4-GIULIANO-F010-2026-11-03.md). Los registros del 26–28/10 son históricos. Nuevos cambios propios preparados y probados; las seis issues permanecen abiertas conforme a su DoD.
