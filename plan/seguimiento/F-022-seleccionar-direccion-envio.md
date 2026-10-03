# Tareas y seguimiento — F-022 Capturar o seleccionar dirección de envío

Versión 0.1.0 · Planificación inicial · F-022 no está implementada por estos documentos.

## Fuente y control

- [Plan F-022](../funcionalidades/F-022-seleccionar-direccion-envio.md); [sprint 4](../iteraciones/S04-semanas-12-13.md).
- [Funcional](../../SPECS/funcional/F-022-seleccionar-direccion-envio.md), [UI](../../SPECS/ui/F-022-seleccionar-direccion-envio.md), [API](../../SPECS/contrato-api/F-022-seleccionar-direccion-envio.md), [React](../../SPECS/componentes-react/F-022-seleccionar-direccion-envio.md).
- [Reglas del seguimiento](README.md), [pruebas/DevSecOps](../DEVSECOPS-Y-PRUEBAS.md), [gates](../DECISIONES-Y-BLOQUEOS.md).
- Responsables/revisores **propuestos**, no compromiso aceptado. Semana objetivo no es fecha de calendario; confirmar capacidad en planificación.
- Mock y real se reportan por separado. QA local puede avanzar con fixtures; QA real requiere INT. Evidencia inicial pendiente, no pruebas ejecutadas.

## Tablero

| ID | Área | Responsable | Revisor | Prioridad | Depende de | Semana objetivo | Estado |
|---|---|---|---|---|---|---|---|
| TASK-F022-FE-001 | Frontend | Sebastian | Fernando | P0 | TASK-TRANS-S01-OPS-001 | 12 | Pendiente |
| TASK-F022-BE-001 | Backend | Leonidas | Andres | P0 | TASK-TRANS-S01-OPS-001 | 12 | Pendiente |
| TASK-F022-INT-001 | Integración | Leonidas | Andres | P0 | TASK-F022-BE-001 + G-ADDRESS + TASK-F002-INT-001 + TASK-F019-INT-001 | 13 | Bloqueado |
| TASK-F022-QA-001 | QA funcional | Fernando | Giuliano | P0 | TASK-F022-FE-001 + TASK-F022-BE-001 | 13 | Pendiente |
| TASK-F022-QA-002 | QA seguridad / DevSecOps | Andres | Fernando | P0 | TASK-F022-FE-001 + TASK-F022-BE-001 + TASK-TRANS-S04-OPS-002 | 13 | Pendiente |
| TASK-F022-DOC-001 | Documentación | Sebastian | Jim | P0 | TASK-F022-INT-001 + TASK-F022-QA-001 + TASK-F022-QA-002 | 13 | Pendiente |

Referentes de BD: Leonidas + Andres; ver [nombres y roles](../PLAN-IMPLEMENTACION.md#4-responsabilidad-sin-confundir-diseño-con-código). Dependencias transversales en [TRANSVERSALES](TRANSVERSALES.md). Los IDs DOC/OPS son extensiones de tareas documentales/operativas, no nuevos IDs funcionales.

## Trabajo, Definition of Done y evidencia

### TASK-F022-FE-001

- **Trabajo:** Implementar DeliveryAddressPicker, NewDeliveryAddressForm, AddressStepContainer y todos los estados de React/UI.
- **Terminado cuando:** Props/eventos tipados, estado específico, sin requests internos navegador; desktop/mobile aplicables y casos de spec React cubiertos.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F022-BE-001

- **Trabajo:** Adaptar GET/POST direcciones Seguridad con token del titular, sin userId manipulable ni persistencia local.
- **Terminado cuando:** DTO, validación, errores y ownership probados con fixtures; transacciones/versiones donde aplica. Adaptador real no activado si gate externo sigue abierto.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F022-INT-001

- **Trabajo:** Homologar y probar integración real y condiciones: G-ADDRESS; no sólo fixture.
- **Terminado cuando:** Contrato/configuración y gates enlazados, pruebas positivas/negativas y timeout autorizadas pasan; evidencia distingue sandbox de mock.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Falta cierre documentado de G-ADDRESS. Contrato/configuración y prueba enlazados antes de cambiar a En progreso.

### TASK-F022-QA-001

- **Trabajo:** Probar vacío formulario abierto; 400 conserva campos válidos; 401 retira direcciones; request no incluye identidad editable; dirección cambio invalida quote; incluir cada estado visual y transición documentada.
- **Terminado cuando:** Casos unitarios/componentes/API y E2E aplicables pasan con evidencias; pruebas mock y reales etiquetadas. Hallazgos corregidos/reprobados.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F022-QA-002

- **Trabajo:** Token titular no técnico, dirección ajena rechazada y cuerpos excluidos storage/logs.
- **Terminado cuando:** Negativos de seguridad pasan en entorno propio/autorizado, scans SAST/SCA/secrets y DAST aplicable adjuntos sin secretos. Sin hallazgo crítico/alto explotable abierto.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F022-DOC-001

- **Trabajo:** Actualizar trazabilidad specs↔implementación↔pruebas, enlaces Figma y decisiones resueltas; documentar operación/errores relevantes.
- **Terminado cuando:** Fuentes vigentes coherentes, evidencias reales y revisión independiente; no marcar funcionalidad terminada con integración pendiente.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.


## Registro de revisión

| Fecha/semana | Cambios de estado | Evidencia / bloqueo / decisión | Revisó |
|---|---|---|---|
| Semana 6, preparación | Creación de tareas; sin ejecución | Specs y plan elaborados; integración pendiente donde se indica | Revisión humana pendiente |

Actualizar filas existentes; no crear un segundo conjunto de tareas por variante desktop/mobile ni por cada estado visual. Si hace falta dividir una tarea, conservar ID padre y crear sufijo incremental con alcance/existencia verificable.

