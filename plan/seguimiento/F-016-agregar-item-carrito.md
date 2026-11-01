# Tareas y seguimiento — F-016 Agregar ítem al carrito

Versión 0.1.0 · Planificación inicial · F-016 no está implementada por estos documentos.

## Fuente y control

- [Plan F-016](../funcionalidades/F-016-agregar-item-carrito.md); [iteración S02/H4](../iteraciones/S02-semanas-09-11.md).
- [Funcional](../../SPECS/funcional/F-016-agregar-item-carrito.md), [UI](../../SPECS/ui/F-016-agregar-item-carrito.md), [API](../../SPECS/contrato-api/F-016-agregar-item-carrito.md), [React](../../SPECS/componentes-react/F-016-agregar-item-carrito.md).
- [Reglas del seguimiento](README.md), [pruebas/DevSecOps](../DEVSECOPS-Y-PRUEBAS.md), [gates](../DECISIONES-Y-BLOQUEOS.md).
- Responsable asignado por el PO: **Andres Morales**; revisor principal: **Leonidas Garcia** según la [matriz](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md). Estimación base fijada en la matriz; ejecución y evidencia pendientes. La semana objetivo es académica, no fecha de calendario.
- Mock y real se reportan por separado. QA local puede avanzar con fixtures; QA real requiere INT. Evidencia inicial pendiente, no pruebas ejecutadas.

## Corte planificado de H4

**Objetivo de cierre H4.** Implementar alta FE+BE por SKU elegible con precio/cantidad G6, BD propia, cookie invitado o titular G7; probar duplicado/rechazo/carrera y resolver G-ADD/G-DB/G-QUANTITY.

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
| TASK-F016-FE-001 | Frontend | Andres Morales | Leonidas Garcia | P0 | TASK-TRANS-S01-OPS-001 | 9–10/H4 | Pendiente |
| TASK-F016-BE-001 | Backend | Andres Morales | Leonidas Garcia | P0 | TASK-TRANS-S01-OPS-001 + TASK-TRANS-S01-DB-001 | 9–10/H4 | Pendiente |
| TASK-F016-DB-001 | BD / Prisma | Andres Morales | Leonidas Garcia | P0 | TASK-TRANS-S01-DB-001 | 9–10/H4 | Pendiente |
| TASK-F016-INT-001 | Integración | Andres Morales | Leonidas Garcia | P0 | TASK-F016-BE-001 + TASK-F016-DB-001 + I-01 + G-SKU + G-ADD + TASK-F012-INT-001 + TASK-F013-INT-001 + TASK-F014-INT-001 + G-QUANTITY | 11/H4 | Bloqueado |
| TASK-F016-QA-001 | QA funcional | Andres Morales | Leonidas Garcia | P0 | TASK-F016-FE-001 + TASK-F016-BE-001 + TASK-F016-DB-001 | 11/H4 | Pendiente |
| TASK-F016-QA-002 | QA seguridad / DevSecOps | Andres Morales | Leonidas Garcia | P0 | TASK-F016-FE-001 + TASK-F016-BE-001 + TASK-TRANS-S02-OPS-002 | 11/H4 | Pendiente |
| TASK-F016-DOC-001 | Documentación | Andres Morales | Leonidas Garcia | P0 | H4 diseño/implementación: specs y pruebas locales; cierre completo: TASK-F016-INT-001 + TASK-F016-QA-001 + TASK-F016-QA-002 | 11/H4 | Pendiente |

Referente de BD: Andres Morales para este bloque, con revisión de Leonidas Garcia; Andres mantiene soporte transversal de migraciones. Ver [matriz](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md).

## Trabajo, Definition of Done y evidencia

### TASK-F016-FE-001

- **Trabajo:** Implementar AddToCartAction, AddedToCartFeedback y todos los estados de React/UI.
- **Terminado cuando:** Props/eventos tipados, estado específico, sin requests internos navegador; desktop/mobile aplicables y casos de spec React cubiertos.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F016-BE-001

- **Trabajo:** Crear/recuperar carrito seguro y sumar SKU en transacción con Cart.version; revalidar elegibilidad/precio/stock sin reserva.
- **Terminado cuando:** DTO, validación, errores y ownership probados con fixtures; transacciones/versiones donde aplica. Adaptador real no activado si gate externo sigue abierto.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F016-DB-001

- **Trabajo:** Integrar/verificar persistencia Cart/CartItem; sin crear entidades externas. Reutilizar migración común, no recrear tablas por funcionalidad.
- **Terminado cuando:** Modelo Prisma/migraciones y documentación concuerdan con baseline; prueba constraints/ownership/concurrencia/rollback pertinente pasa en PostgreSQL 16 temporal.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F016-INT-001

- **Trabajo:** Homologar y probar integración real y condiciones: I-01, G-SKU, G-ADD; no sólo fixture.
- **Terminado cuando:** Contrato/configuración y gates enlazados, pruebas positivas/negativas y timeout autorizadas pasan; evidencia distingue sandbox de mock.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Falta cierre documentado de I-01, G-SKU, G-ADD. Contrato/configuración y prueba enlazados antes de cambiar a En progreso.

### TASK-F016-QA-001

- **Trabajo:** Probar doble click un POST; cookie anónima no JS; 409 renderiza carrito confirmado; timeout no suma automáticamente; incluir cada estado visual y transición documentada.
- **Terminado cuando:** Casos unitarios/componentes/API y E2E aplicables pasan con evidencias; pruebas mock y reales etiquetadas. Hallazgos corregidos/reprobados.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F016-QA-002

- **Trabajo:** Cookie HttpOnly/Secure/SameSite, CSRF, propietario carrito no manipulable y suma concurrente segura.
- **Terminado cuando:** Negativos de seguridad pasan en entorno propio/autorizado, scans SAST/SCA/secrets y DAST aplicable adjuntos sin secretos. Sin hallazgo crítico/alto explotable abierto.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F016-DOC-001

- **Trabajo:** Actualizar trazabilidad specs↔implementación↔pruebas, enlaces Figma y decisiones resueltas; documentar operación/errores relevantes.
- **Terminado cuando:** Fuentes vigentes coherentes, evidencias reales y revisión independiente; no marcar funcionalidad terminada con integración pendiente.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.


## Registro de revisión

| Fecha/semana | Cambios de estado | Evidencia / bloqueo / decisión | Revisó |
|---|---|---|---|
| Semana 6, preparación | Creación de tareas; sin ejecución | Specs y plan elaborados; integración pendiente donde se indica | Revisión humana pendiente |

Actualizar filas existentes; no crear un segundo conjunto de tareas por variante desktop/mobile ni por cada estado visual. Si hace falta dividir una tarea, conservar ID padre y crear sufijo incremental con alcance/existencia verificable.
