# Tareas y seguimiento — F-016 Agregar ítem al carrito

Versión 0.1.0 · Planificación inicial · F-016 no está implementada por estos documentos.

## Fuente y control

- [Plan F-016](../funcionalidades/F-016-agregar-item-carrito.md); [sprint 2](../iteraciones/S02-semanas-08-09.md).
- [Funcional](../../SPECS/funcional/F-016-agregar-item-carrito.md), [UI](../../SPECS/ui/F-016-agregar-item-carrito.md), [API](../../SPECS/contrato-api/F-016-agregar-item-carrito.md), [React](../../SPECS/componentes-react/F-016-agregar-item-carrito.md).
- [Reglas del seguimiento](README.md), [pruebas/DevSecOps](../DEVSECOPS-Y-PRUEBAS.md), [gates](../DECISIONES-Y-BLOQUEOS.md).
- Responsables/revisores **propuestos**, no compromiso aceptado. Semana objetivo no es fecha de calendario; confirmar capacidad en planificación.
- Mock y real se reportan por separado. QA local puede avanzar con fixtures; QA real requiere INT. Evidencia inicial pendiente, no pruebas ejecutadas.

## Tablero

| ID | Área | Responsable | Revisor | Prioridad | Depende de | Semana objetivo | Estado |
|---|---|---|---|---|---|---|---|
| TASK-F016-FE-001 | Frontend | Sebastian | Fernando | P0 | TASK-TRANS-S01-OPS-001 | 8 | Pendiente |
| TASK-F016-BE-001 | Backend | Leonidas | Andres | P0 | TASK-TRANS-S01-OPS-001 + TASK-TRANS-S01-DB-001 | 8 | Pendiente |
| TASK-F016-DB-001 | BD / Prisma | Leonidas | Andres | P0 | TASK-TRANS-S01-DB-001 | 8 | Pendiente |
| TASK-F016-INT-001 | Integración | Leonidas | Andres | P0 | TASK-F016-BE-001 + TASK-F016-DB-001 + I-01 + G-SKU + G-ADD + TASK-F012-INT-001 + TASK-F013-INT-001 + TASK-F014-INT-001 | 9 | Bloqueado |
| TASK-F016-QA-001 | QA funcional | Fernando | Giuliano | P0 | TASK-F016-FE-001 + TASK-F016-BE-001 + TASK-F016-DB-001 | 9 | Pendiente |
| TASK-F016-QA-002 | QA seguridad / DevSecOps | Andres | Fernando | P0 | TASK-F016-FE-001 + TASK-F016-BE-001 + TASK-TRANS-S02-OPS-002 | 9 | Pendiente |
| TASK-F016-DOC-001 | Documentación | Sebastian | Jim | P0 | TASK-F016-INT-001 + TASK-F016-QA-001 + TASK-F016-QA-002 | 9 | Pendiente |

Referentes de BD: Leonidas + Andres; ver [nombres y roles](../PLAN-IMPLEMENTACION.md#4-responsabilidad-sin-confundir-diseño-con-código). Dependencias transversales en [TRANSVERSALES](TRANSVERSALES.md). Los IDs DOC/OPS son extensiones de tareas documentales/operativas, no nuevos IDs funcionales.

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

