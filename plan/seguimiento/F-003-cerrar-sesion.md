# Tareas y seguimiento — F-003 Cerrar sesión

Versión 0.1.0 · Planificación inicial · F-003 no está implementada por estos documentos.

## Fuente y control

- [Plan F-003](../funcionalidades/F-003-cerrar-sesion.md); [sprint 1](../iteraciones/S01-semanas-06-07.md).
- [Funcional](../../SPECS/funcional/F-003-cerrar-sesion.md), [UI](../../SPECS/ui/F-003-cerrar-sesion.md), [API](../../SPECS/contrato-api/F-003-cerrar-sesion.md), [React](../../SPECS/componentes-react/F-003-cerrar-sesion.md).
- [Reglas del seguimiento](README.md), [pruebas/DevSecOps](../DEVSECOPS-Y-PRUEBAS.md), [gates](../DECISIONES-Y-BLOQUEOS.md).
- Responsables/revisores **propuestos**, no compromiso aceptado. Semana objetivo no es fecha de calendario; confirmar capacidad en planificación.
- Mock y real se reportan por separado. QA local puede avanzar con fixtures; QA real requiere INT. Evidencia inicial pendiente, no pruebas ejecutadas.

## Tablero

| ID | Área | Responsable | Revisor | Prioridad | Depende de | Semana objetivo | Estado |
|---|---|---|---|---|---|---|---|
| TASK-F003-FE-001 | Frontend | Giuliano | Fernando | P0 | TASK-TRANS-S01-OPS-001 | 6 | Pendiente |
| TASK-F003-BE-001 | Backend | Leonidas | Andres | P0 | TASK-TRANS-S01-OPS-001 | 6 | Pendiente |
| TASK-F003-INT-001 | Integración | Leonidas | Andres | P0 | TASK-F003-BE-001 + G-AUTH + TASK-F002-INT-001 | 7 | Bloqueado |
| TASK-F003-QA-001 | QA funcional | Fernando | Sebastian | P0 | TASK-F003-FE-001 + TASK-F003-BE-001 | 7 | Pendiente |
| TASK-F003-QA-002 | QA seguridad / DevSecOps | Andres | Fernando | P0 | TASK-F003-FE-001 + TASK-F003-BE-001 + TASK-TRANS-S01-OPS-002 | 7 | Pendiente |
| TASK-F003-DOC-001 | Documentación | Sebastian | Jim | P0 | TASK-F003-INT-001 + TASK-F003-QA-001 + TASK-F003-QA-002 | 7 | Pendiente |

Referentes de BD: Leonidas + Andres; ver [nombres y roles](../PLAN-IMPLEMENTACION.md#4-responsabilidad-sin-confundir-diseño-con-código). Dependencias transversales en [TRANSVERSALES](TRANSVERSALES.md). Los IDs DOC/OPS son extensiones de tareas documentales/operativas, no nuevos IDs funcionales.

## Trabajo, Definition of Done y evidencia

### TASK-F003-FE-001

- **Trabajo:** Implementar LogoutAction, CheckoutLogoutDialog y todos los estados de React/UI.
- **Terminado cuando:** Props/eventos tipados, estado específico, sin requests internos navegador; desktop/mobile aplicables y casos de spec React cubiertos.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F003-BE-001

- **Trabajo:** Revocar refresh vía Seguridad y limpiar sesión protegida sin borrar carrito/favoritos.
- **Terminado cuando:** DTO, validación, errores y ownership probados con fixtures; transacciones/versiones donde aplica. Adaptador real no activado si gate externo sigue abierto.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F003-INT-001

- **Trabajo:** Homologar y probar integración real y condiciones: G-AUTH; no sólo fixture.
- **Terminado cuando:** Contrato/configuración y gates enlazados, pruebas positivas/negativas y timeout autorizadas pasan; evidencia distingue sandbox de mock.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Falta cierre documentado de G-AUTH. Contrato/configuración y prueba enlazados antes de cambiar a En progreso.

### TASK-F003-QA-001

- **Trabajo:** Probar cancelar mantiene sesión; fallo remoto cierra localmente; otro usuario no ve caché anterior; O-004 devuelve foco al cancelar; incluir cada estado visual y transición documentada.
- **Terminado cuando:** Casos unitarios/componentes/API y E2E aplicables pasan con evidencias; pruebas mock y reales etiquetadas. Hallazgos corregidos/reprobados.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F003-QA-002

- **Trabajo:** Revocación y cachés después logout/cambio cuenta, CSRF según transporte, no exposición refresh.
- **Terminado cuando:** Negativos de seguridad pasan en entorno propio/autorizado, scans SAST/SCA/secrets y DAST aplicable adjuntos sin secretos. Sin hallazgo crítico/alto explotable abierto.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F003-DOC-001

- **Trabajo:** Actualizar trazabilidad specs↔implementación↔pruebas, enlaces Figma y decisiones resueltas; documentar operación/errores relevantes.
- **Terminado cuando:** Fuentes vigentes coherentes, evidencias reales y revisión independiente; no marcar funcionalidad terminada con integración pendiente.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.


## Registro de revisión

| Fecha/semana | Cambios de estado | Evidencia / bloqueo / decisión | Revisó |
|---|---|---|---|
| Semana 6, preparación | Creación de tareas; sin ejecución | Specs y plan elaborados; integración pendiente donde se indica | Revisión humana pendiente |

Actualizar filas existentes; no crear un segundo conjunto de tareas por variante desktop/mobile ni por cada estado visual. Si hace falta dividir una tarea, conservar ID padre y crear sufijo incremental con alcance/existencia verificable.

