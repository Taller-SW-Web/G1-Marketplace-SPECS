# Tareas y seguimiento — F-022 Capturar o seleccionar dirección de envío

Versión 0.1.0 · Planificación inicial · F-022 no está implementada por estos documentos.

## Fuente y control

- [Plan F-022](../funcionalidades/F-022-seleccionar-direccion-envio.md); [iteración S3](../iteraciones/S03-semanas-12-13.md).
- [Funcional](../../SPECS/funcional/F-022-seleccionar-direccion-envio.md), [UI](../../SPECS/ui/F-022-seleccionar-direccion-envio.md), [API](../../SPECS/contrato-api/F-022-seleccionar-direccion-envio.md), [React](../../SPECS/componentes-react/F-022-seleccionar-direccion-envio.md).
- [Reglas del seguimiento](README.md), [pruebas/DevSecOps](../DEVSECOPS-Y-PRUEBAS.md), [gates](../DECISIONES-Y-BLOQUEOS.md).
- Responsable asignado por el PO: **Leonidas Garcia**; revisor principal: **Diego Espinoza** según la [matriz](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md). Estimación base fijada en la matriz; ejecución y evidencia pendientes. La semana objetivo es académica, no fecha de calendario.
- Mock y real se reportan por separado. QA local puede avanzar con fixtures; QA real requiere INT. Evidencia inicial pendiente, no pruebas ejecutadas.

## Tablero

| ID | Área | Responsable | Revisor | Prioridad | Depende de | Semana objetivo | Estado |
|---|---|---|---|---|---|---|---|
| TASK-F022-FE-001 | Frontend | Leonidas Garcia | Diego Espinoza | P0 | TASK-TRANS-S01-OPS-001 | 12 | Pendiente |
| TASK-F022-BE-001 | Backend | Leonidas Garcia | Diego Espinoza | P0 | TASK-TRANS-S01-OPS-001 | 12 | Pendiente |
| TASK-F022-INT-001 | Integración | Leonidas Garcia | Diego Espinoza | P0 | TASK-F022-BE-001 + G-ADDRESS + TASK-F002-INT-001 + TASK-F019-INT-001 | 13 | Bloqueado |
| TASK-F022-QA-001 | QA funcional | Leonidas Garcia | Diego Espinoza | P0 | TASK-F022-FE-001 + TASK-F022-BE-001 | 13 | Pendiente |
| TASK-F022-QA-002 | QA seguridad / DevSecOps | Leonidas Garcia | Diego Espinoza | P0 | TASK-F022-FE-001 + TASK-F022-BE-001 + TASK-TRANS-S03-OPS-002 | 13 | Pendiente |
| TASK-F022-DOC-001 | Documentación | Leonidas Garcia | Diego Espinoza | P0 | TASK-F022-INT-001 + TASK-F022-QA-001 + TASK-F022-QA-002 | 13 | Pendiente |

Referente de BD: Leonidas Garcia para este bloque, con revisión de Diego Espinoza; Andres mantiene soporte transversal de migraciones. Ver [matriz](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md).

## Trabajo, Definition of Done y evidencia

### TASK-F022-FE-001

- **Trabajo:** Implementar DeliveryAddressPicker, NewDeliveryAddressForm, AddressStepContainer y todos los estados de React/UI.
- **Terminado cuando:** Props/eventos tipados, estado específico y sin requests internos navegador; usar los frames V-010 del [canvas Checkout en Figma](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=1-5&p=f&t=PXeKrikbDjSdUQ5l-0) como referencia visual. Cubrir estados desktop/mobile y casos de spec React.
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
