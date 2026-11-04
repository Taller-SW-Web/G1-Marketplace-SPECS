# Tareas y seguimiento — F-029 Filtrar el historial de pedidos

Versión 0.1.0 · Planificación inicial · F-029 no está implementada por estos documentos.

## Fuente y control

- [Plan F-029](../funcionalidades/F-029-filtrar-historial-pedidos.md); [iteración S5](../iteraciones/S05-semanas-15-16.md).
- [Funcional](../../SPECS/funcional/F-029-filtrar-historial-pedidos.md), [UI](../../SPECS/ui/F-029-filtrar-historial-pedidos.md), [API](../../SPECS/contrato-api/F-029-filtrar-historial-pedidos.md), [React](../../SPECS/componentes-react/F-029-filtrar-historial-pedidos.md).
- [Reglas del seguimiento](README.md), [pruebas/DevSecOps](../DEVSECOPS-Y-PRUEBAS.md), [gates](../DECISIONES-Y-BLOQUEOS.md).
- Responsable asignado por el PO: **Fernando Saire**; revisor principal: **Jim Segovia** según la [matriz](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md). Estimación base fijada en la matriz; ejecución y evidencia pendientes. La semana objetivo es académica, no fecha de calendario.
- Mock y real se reportan por separado. QA local puede avanzar con fixtures; QA real requiere INT. Evidencia inicial pendiente, no pruebas ejecutadas.

## Corte planificado de H4

**Implementación y pruebas G1 en H4; cierre intermodular posterior.** Implementar filtros/estado UI y lógica G1 con dobles; aislar el adaptador de la brecha de fechas de /me G5. No inventar endpoint ni declarar filtro REAL sin contrato; cierre S05.

**Cierre base:** S05/H6, semanas 15–16; implementación propia y pruebas con dobles en H4. Disponibilidad sin restricción horaria por decisión del PO. Las entregas «local» o «con dobles» son etapas del mismo TASK, no cierres de INT. DOC prepara desde specs y QA ejecuta casos propios antes de INT; el cierre completo conserva dependencias/DoD. [Alcance H4](../ALCANCE-H4-PRODUCTOS-SEGURIDAD.md). Los estados no cambian al replanificar.

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
| TASK-F029-FE-001 | Frontend | Fernando Saire | Jim Segovia | P1 | TASK-TRANS-S01-OPS-001 | 9–11 implementación H4 | Pendiente |
| TASK-F029-BE-001 | Backend | Fernando Saire | Jim Segovia | P1 | TASK-TRANS-S01-OPS-001 | 9–11 implementación H4 | Pendiente |
| TASK-F029-INT-001 | Integración | Fernando Saire | Jim Segovia | P1 | TASK-F029-BE-001 + I-03 + TASK-F028-INT-001 | 11 local H4; 16/S05 REAL | Bloqueado |
| TASK-F029-QA-001 | QA funcional | Fernando Saire | Jim Segovia | P1 | TASK-F029-FE-001 + TASK-F029-BE-001 | 11 local H4; 16/S05 REAL | Pendiente |
| TASK-F029-QA-002 | QA seguridad / DevSecOps | Fernando Saire | Jim Segovia | P1 | TASK-F029-FE-001 + TASK-F029-BE-001 + TASK-TRANS-S02-OPS-002 (local H4); TASK-TRANS-S05-OPS-002 (cierre posterior) | 11 local H4; 16/S05 REAL | Pendiente |
| TASK-F029-DOC-001 | Documentación | Fernando Saire | Jim Segovia | P1 | H4 diseño/implementación: specs y pruebas locales; cierre completo: TASK-F029-INT-001 + TASK-F029-QA-001 + TASK-F029-QA-002 | 11 local H4; 16/S05 REAL | Pendiente |

Referente de BD: Fernando Saire para este bloque, con revisión de Jim Segovia; Andres mantiene soporte transversal de migraciones. Ver [matriz](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md).

## Trabajo, Definition of Done y evidencia

### TASK-F029-FE-001

- **Trabajo:** Implementar OrdersFilterForm, OrdersFilterSummary y todos los estados de React/UI.
- **Terminado cuando:** Props/eventos tipados, estado específico, sin requests internos navegador; desktop/mobile aplicables y casos de spec React cubiertos.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F029-BE-001

- **Trabajo:** Mapear estado/fechas ISO / rango <= 1 año a historial propio con reinicio página y validación antes de proveedor.
- **Terminado cuando:** DTO, validación, errores y ownership probados con fixtures; transacciones/versiones donde aplica. Adaptador real no activado si gate externo sigue abierto.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F029-INT-001

- **Trabajo:** Homologar y probar integración real y condiciones: I-03; no sólo fixture.
- **Terminado cuando:** Contrato/configuración y gates enlazados, pruebas positivas/negativas y timeout autorizadas pasan; evidencia distingue sandbox de mock.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Falta cierre documentado de I-03. Contrato/configuración y prueba enlazados antes de cambiar a En progreso.

### TASK-F029-QA-001

- **Trabajo:** Probar rango invertido no consulta; más un año no consulta; cero resultados permite limpiar; día local no cambia al serializar; incluir cada estado visual y transición documentada.
- **Terminado cuando:** Casos unitarios/componentes/API y E2E aplicables pasan con evidencias; pruebas mock y reales etiquetadas. Hallazgos corregidos/reprobados.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F029-QA-002

- **Trabajo:** Filtros no alteran titular, fechas abusivas no proveedor.
- **Terminado cuando:** Negativos de seguridad pasan en entorno propio/autorizado, scans SAST/SCA/secrets y DAST aplicable adjuntos sin secretos. Sin hallazgo crítico/alto explotable abierto.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F029-DOC-001

- **Trabajo:** Actualizar trazabilidad specs↔implementación↔pruebas, enlaces Figma y decisiones resueltas; documentar operación/errores relevantes.
- **Terminado cuando:** Fuentes vigentes coherentes, evidencias reales y revisión independiente; no marcar funcionalidad terminada con integración pendiente.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.


## Registro de revisión

### Avance local de H4 — 03/11/2026

Fernando preparó cambios sin commit en `feat/f028-f035-fernando-frontend` y `feat/f028-f035-fernando-backend`. Backend valida `state`, `from`, `to`, formato ISO, orden del rango y máximo de un año antes del provider; el fixture filtra por día de `America/Lima` antes de paginar. Frontend conserva el día `YYYY-MM-DD`, combina filtros, reinicia a página 0, permite quitar/limpiar criterios y reenvía al BFF sólo parámetros permitidos. La consulta real a G5 no está activada.

Evidencia disponible: Frontend `typecheck` aprobado; `tests/components/orders-history.test.tsx` 13/13; `tests/server/orders-me-route.test.ts` 1/1. Backend `typecheck` aprobado y 46/46 casos en cinco suites dirigidas (`orders-query.dto`, provider mock, provider G5 contractual, controller y environment). La prueba del provider G5 usa respuestas mock y no acredita llamada al servicio de Render. El adapter está inactivo por defecto y sólo se activa con `ORDERS_SOURCE=g5`, G7 real y `G5_API_URL` HTTPS. No hay SHA de commit, prueba REAL, despliegue ni aprobación de revisión todavía.

El acuerdo G5 para `desde`/`hasta` (formato `YYYY-MM-DD`, inclusivo por día `America/Lima`, error de rango/formato) está documentado en el plan de la rama Backend y en las PR G5 #53/#61. La integración F-029 sigue bloqueada por I-03/#146 y la prueba con JWT de cliente autorizado; estos cambios MOCK/LOCAL no cierran #146 ni el hito S05/H6.

### Preparación del timeout G5 — 04/11/2026

El servicio G5 avisó que un primer request tras inactividad puede tardar 1–2 minutos. El adapter usaba el `HTTP_TIMEOUT_MS` general de 3 s (máximo 30 s, y máximo 5 s al activar auth G7), mientras el BFF Frontend cancelaba a los 8 s; eso hacía fallar el flujo frío aunque el contrato estuviese disponible. Se separó `G5_HTTP_TIMEOUT_MS` (150 s por defecto, máximo 180 s) de los timeouts G7 y `G1_ORDERS_BFF_TIMEOUT_MS` (185 s por defecto, configurable entre 181–190 s) para historial/detalle/recompra; así la capa BFF no puede quedar configurada por debajo del máximo admitido por Backend. Ambos providers siguen desactivados por defecto. No se hizo request REAL; antes de integración/despliegue hay que verificar límites del hosting, realizar warm-up coordinado y probar la latencia observada.

Pruebas de la preparación: Backend `environment.spec` + `g5-orders.provider.spec` pasaron 29/29; verifican límites de ambos timeouts y que la llamada G5 recibe 150000 ms independiente del `HTTP_TIMEOUT_MS` de G7. Frontend `npm run test:server` pasó 9 archivos/94 pruebas y `typecheck`; pruebas nuevas cubren timeout BFF default y límites configurables. Build optimizado Frontend aprobado. Todo sigue siendo local, no es una llamada REAL a Render.

| 03/11/2026 | Implementación H4 local en curso; gates INT y cierre sin cambio | Ramas FE/BE locales indicadas arriba. Comandos y resultados parciales en este registro; SHA y revisión pendientes | Revisión de Jim pendiente |

| Fecha/semana | Cambios de estado | Evidencia / bloqueo / decisión | Revisó |
|---|---|---|---|
| Semana 6, preparación | Creación de tareas; sin ejecución | Specs y plan elaborados; integración pendiente donde se indica | Revisión humana pendiente |

Actualizar filas existentes; no crear un segundo conjunto de tareas por variante desktop/mobile ni por cada estado visual. Si hace falta dividir una tarea, conservar ID padre y crear sufijo incremental con alcance/existencia verificable.
