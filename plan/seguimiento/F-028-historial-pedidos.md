# Tareas y seguimiento — F-028 Consultar historial de pedidos

Versión 0.1.0 · Planificación inicial · F-028 no está implementada por estos documentos.

## Fuente y control

- [Plan F-028](../funcionalidades/F-028-historial-pedidos.md); [iteración S3](../iteraciones/S03-semanas-12-13.md).
- [Funcional](../../SPECS/funcional/F-028-historial-pedidos.md), [UI](../../SPECS/ui/F-028-historial-pedidos.md), [API](../../SPECS/contrato-api/F-028-historial-pedidos.md), [React](../../SPECS/componentes-react/F-028-historial-pedidos.md).
- [Reglas del seguimiento](README.md), [pruebas/DevSecOps](../DEVSECOPS-Y-PRUEBAS.md), [gates](../DECISIONES-Y-BLOQUEOS.md).
- Responsable asignado por el PO: **Fernando Saire**; revisor principal: **Jim Segovia** según la [matriz](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md). Estimación base fijada en la matriz; ejecución y evidencia pendientes. La semana objetivo es académica, no fecha de calendario.
- Mock y real se reportan por separado. QA local puede avanzar con fixtures; QA real requiere INT. Evidencia inicial pendiente, no pruebas ejecutadas.

## Corte planificado de H4

**Implementación y pruebas G1 en H4; cierre intermodular posterior.** Implementar historial FE+BFF con fixture o Ventas autorizado, paginación/vacío/error y usuarios A/B; integrar G5 donde esté habilitado. Cierre integral S03 con titularidad y despliegue.

**Cierre base:** S03, semanas 12–13; implementación y pruebas propias comienzan en H4. Disponibilidad sin restricción horaria por decisión del PO. Las entregas «local» o «con dobles» son etapas del mismo TASK, no cierres de INT. DOC prepara desde specs y QA ejecuta casos propios antes de INT; el cierre completo conserva dependencias/DoD. [Alcance H4](../ALCANCE-H4-PRODUCTOS-SEGURIDAD.md). Los estados no cambian al replanificar.

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
| TASK-F028-FE-001 | Frontend | Fernando Saire | Jim Segovia | P0 | TASK-TRANS-S01-OPS-001 | 9–11 implementación H4 | Pendiente |
| TASK-F028-BE-001 | Backend | Fernando Saire | Jim Segovia | P0 | TASK-TRANS-S01-OPS-001 | 9–11 implementación H4 | Pendiente |
| TASK-F028-INT-001 | Integración | Fernando Saire | Jim Segovia | P0 | TASK-F028-BE-001 + I-03 + TASK-F002-INT-001 | 11 local H4; 13/S03 REAL | Bloqueado |
| TASK-F028-QA-001 | QA funcional | Fernando Saire | Jim Segovia | P0 | TASK-F028-FE-001 + TASK-F028-BE-001 | 11 local H4; 13/S03 REAL | Pendiente |
| TASK-F028-QA-002 | QA seguridad / DevSecOps | Fernando Saire | Jim Segovia | P0 | TASK-F028-FE-001 + TASK-F028-BE-001 + TASK-TRANS-S02-OPS-002 (local H4); TASK-TRANS-S03-OPS-002 (cierre posterior) | 11 local H4; 13/S03 REAL | Pendiente |
| TASK-F028-DOC-001 | Documentación | Fernando Saire | Jim Segovia | P0 | H4 diseño/implementación: specs y pruebas locales; cierre completo: TASK-F028-INT-001 + TASK-F028-QA-001 + TASK-F028-QA-002 | 11 local H4; 13/S03 REAL | Pendiente |

Referente de BD: Fernando Saire para este bloque, con revisión de Jim Segovia; Andres mantiene soporte transversal de migraciones. Ver [matriz](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md).

## Trabajo, Definition of Done y evidencia

### TASK-F028-FE-001

- **Trabajo:** Implementar OrdersHistoryContainer, OrderList y todos los estados de React/UI.
- **Terminado cuando:** Props/eventos tipados, estado específico, sin requests internos navegador; desktop/mobile aplicables y casos de spec React cubiertos.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F028-BE-001

- **Trabajo:** Adaptar historial/me con titular del JWT validado en Ventas y paginación, sin clienteId del navegador ni réplica.
- **Terminado cuando:** DTO, validación, errores y ownership probados con fixtures; transacciones/versiones donde aplica. Adaptador real no activado si gate externo sigue abierto.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F028-INT-001

- **Trabajo:** Homologar y probar integración real y condiciones: I-03; no sólo fixture.
- **Terminado cuando:** Contrato/configuración y gates enlazados, pruebas positivas/negativas y timeout autorizadas pasan; evidencia distingue sandbox de mock.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Falta cierre documentado de I-03. Contrato/configuración y prueba enlazados antes de cambiar a En progreso.

### TASK-F028-QA-001

- **Trabajo:** Probar request no clienteId; vacío catálogo; 401 retira lista previa; meta pagina y conserva filtros; incluir cada estado visual y transición documentada.
- **Terminado cuando:** Casos unitarios/componentes/API y E2E aplicables pasan con evidencias; pruebas mock y reales etiquetadas. Hallazgos corregidos/reprobados.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F028-QA-002

- **Trabajo:** IDOR con JWT con clienteId forjado y cachés entre usuarios, sólo pedidos propios.
- **Terminado cuando:** Negativos de seguridad pasan en entorno propio/autorizado, scans SAST/SCA/secrets y DAST aplicable adjuntos sin secretos. Sin hallazgo crítico/alto explotable abierto.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F028-DOC-001

- **Trabajo:** Actualizar trazabilidad specs↔implementación↔pruebas, enlaces Figma y decisiones resueltas; documentar operación/errores relevantes.
- **Terminado cuando:** Fuentes vigentes coherentes, evidencias reales y revisión independiente; no marcar funcionalidad terminada con integración pendiente.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.


## Registro de revisión

### Implementación local Frontend — 04/11/2026

En `feat/f028-f035-fernando-frontend`, la ruta `/mis-pedidos` presenta historial responsive, filtros, paginación y estados de carga/vacío/error. El código separa `OrdersHistoryContainer` y el presentacional `OrderList`; el menú de cuenta añade el enlace sólo cuando la sesión G1 está habilitada y autenticada. La vista consulta el BFF, que deriva titularidad desde la sesión y no recibe `customerId` del navegador. La prueba del menú cubre sesión autenticada/no autenticada. Revalidación local 04/11/2026: `typecheck` y build aprobados; componentes 37 archivos/294 pruebas, server 9 archivos/94 pruebas y E2E principal 30 aprobadas/1 omitida de 31. `tests/orders.e2e.spec.ts` recorre con fixtures la lista, filtros, detalle, seguimiento, 401 y pedido no disponible con respuesta neutral (3/3); no acredita autorización A/B real. Falta la integración G5 y la prueba autorizada de titularidad; UI/fixtures no acreditan despliegue ni cierre de TASK-F028-FE/BE/INT/QA.

### Timeout del adapter G5 — 04/11/2026

G5 informó que una primera petición tras inactividad puede tardar 1–2 minutos. Para historial/detalle se separó el límite de G5 del límite corto de auth G7: Backend `G5_HTTP_TIMEOUT_MS` 150 s por defecto (máximo 180 s) y BFF Frontend `G1_ORDERS_BFF_TIMEOUT_MS` 185 s por defecto (configurable entre 181–190 s). `ORDERS_SOURCE` continúa `unconfigured`; no se hizo request REAL. Antes de activar, verificar que el hosting soporte esa duración y coordinar warm-up/prueba con JWT autorizado.

### Avance local de H4 — 03/11/2026

El Backend ya incluye un adapter de Ventas `G5OrdersProvider` para historial y detalle. Usa el JWT del usuario autenticado, traduce la página G1 desde 0 a la página G5 desde 1 y sólo proyecta los campos de compra aprobados. El adapter real está preparado, pero permanece apagado (`ORDERS_SOURCE=unconfigured`); no se usó token ni se envió ninguna solicitud a Render durante este avance. La fuente mock sigue separada y sólo usa datos sintéticos. Las cinco suites Backend dirigidas (incluida la suite del adapter bajo contrato mock) aprobaron 46/46 casos; no es una prueba REAL.

Las pruebas actuales del historial son locales/mock; la integración #142 sigue bloqueada hasta coordinar la prueba de I-03 con credenciales de cliente autorizadas y evidencia sanitizada. No cambiar su estado ni registrar cierre S03 a partir de este adapter.

| Fecha/semana | Cambios de estado | Evidencia / bloqueo / decisión | Revisó |
|---|---|---|---|
| Semana 6, preparación | Creación de tareas; sin ejecución | Specs y plan elaborados; integración pendiente donde se indica | Revisión humana pendiente |

Actualizar filas existentes; no crear un segundo conjunto de tareas por variante desktop/mobile ni por cada estado visual. Si hace falta dividir una tarea, conservar ID padre y crear sufijo incremental con alcance/existencia verificable.
