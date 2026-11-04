# Tareas y seguimiento — F-035 Enviar actualización de despacho por correo

Versión 0.1.0 · Planificación inicial · F-035 no está implementada por estos documentos.

## Fuente y control

- [Plan F-035](../funcionalidades/F-035-enviar-actualizacion-despacho.md); [iteración S4](../iteraciones/S04-semana-14.md).
- [Funcional](../../SPECS/funcional/F-035-enviar-actualizacion-despacho.md), [UI](../../SPECS/ui/F-035-enviar-actualizacion-despacho.md), [API](../../SPECS/contrato-api/F-035-enviar-actualizacion-despacho.md), [React](../../SPECS/componentes-react/F-035-enviar-actualizacion-despacho.md).
- [Reglas del seguimiento](README.md), [pruebas/DevSecOps](../DEVSECOPS-Y-PRUEBAS.md), [gates](../DECISIONES-Y-BLOQUEOS.md).
- Responsable asignado por el PO: **Fernando Saire**; revisor principal: **Jim Segovia** según la [matriz](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md). Estimación base fijada en la matriz; ejecución y evidencia pendientes. La semana objetivo es académica, no fecha de calendario.
- Mock y real se reportan por separado. QA local puede avanzar con fixtures; QA real requiere INT. Evidencia inicial pendiente, no pruebas ejecutadas.

## Corte planificado de H4

**Implementación y pruebas G1 en H4; cierre intermodular posterior.** Implementar consumidor/lógica/plantilla de actualización donde exista contrato de evento G5/G2; probar auth/dedupe/retry con fixtures explícitos. No inventar emisor/transporte/esquema; intercambio real cierra S04/H5.

**Cierre base:** S04/H5, semana 14; implementación y preparación de integración en H4. Disponibilidad sin restricción horaria por decisión del PO. Las entregas «local» o «con dobles» son etapas del mismo TASK, no cierres de INT. DOC prepara desde specs y QA ejecuta casos propios antes de INT; el cierre completo conserva dependencias/DoD. [Alcance H4](../ALCANCE-H4-PRODUCTOS-SEGURIDAD.md). Los estados no cambian al replanificar.

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
| TASK-F035-FE-001 | UI/render server-only | Fernando Saire | Jim Segovia | P0 | TASK-TRANS-S01-OPS-001 | 9–11 implementación H4 | Pendiente |
| TASK-F035-BE-001 | Backend | Fernando Saire | Jim Segovia | P0 | TASK-TRANS-S01-OPS-001 + TASK-TRANS-S01-DB-001 | 9–11 implementación H4 | Pendiente |
| TASK-F035-DB-001 | BD / Prisma | Fernando Saire | Jim Segovia | P0 | TASK-TRANS-S01-DB-001 | 9–11 implementación H4 | Pendiente |
| TASK-F035-INT-001 | Integración | Fernando Saire | Jim Segovia | P0 | TASK-F035-BE-001 + TASK-F035-DB-001 + I-05 + G-MAIL + TASK-F032-INT-001 + TASK-F033-INT-001 + TASK-F034-INT-001 | 11 local H4; 14/S04 REAL | Bloqueado |
| TASK-F035-QA-001 | QA funcional | Fernando Saire | Jim Segovia | P0 | TASK-F035-FE-001 + TASK-F035-BE-001 + TASK-F035-DB-001 | 11 local H4; 14/S04 REAL | Pendiente |
| TASK-F035-QA-002 | QA seguridad / DevSecOps | Fernando Saire | Jim Segovia | P0 | TASK-F035-FE-001 + TASK-F035-BE-001 + TASK-TRANS-S04-OPS-002 | 11 local H4; 14/S04 REAL | Pendiente |
| TASK-F035-DOC-001 | Documentación | Fernando Saire | Jim Segovia | P0 | H4 diseño/implementación: specs y pruebas locales; cierre completo: TASK-F035-INT-001 + TASK-F035-QA-001 + TASK-F035-QA-002 | 11 local H4; 14/S04 REAL | Pendiente |

Referente de BD: Fernando Saire para este bloque, con revisión de Jim Segovia; Andres mantiene soporte transversal de migraciones. Ver [matriz](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md).

## Trabajo, Definition of Done y evidencia

### TASK-F035-FE-001

- **Trabajo:** Implementar ShipmentEmailTemplate y todos los estados de React/UI.
- **Terminado cuando:** Props/eventos tipados, estado específico, sin requests internos navegador; desktop/mobile aplicables y casos de spec React cubiertos.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F035-BE-001

- **Trabajo:** Consumir sólo evento homologado, validar/autenticar/deduplicar shipmentEventId y encolar sin alterar despacho.
- **Terminado cuando:** DTO, validación, errores y ownership probados con fixtures; transacciones/versiones donde aplica. Adaptador real no activado si gate externo sigue abierto.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F035-DB-001

- **Trabajo:** Integrar/verificar persistencia NotificationDelivery; sin crear entidades externas. Reutilizar migración común, no recrear tablas por funcionalidad.
- **Terminado cuando:** Modelo Prisma/migraciones y documentación concuerdan con baseline; prueba constraints/ownership/concurrencia/rollback pertinente pasa en PostgreSQL 16 temporal.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F035-INT-001

- **Trabajo:** Homologar y probar integración real y condiciones: I-05, G-MAIL; no sólo fixture.
- **Terminado cuando:** Contrato/configuración y gates enlazados, pruebas positivas/negativas y timeout autorizadas pasan; evidencia distingue sandbox de mock.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Falta cierre documentado de I-05, G-MAIL. Contrato/configuración y prueba enlazados antes de cambiar a En progreso.

### TASK-F035-QA-001

- **Trabajo:** Probar evento repetido una entrega lógica; email render sin PII; enlace exige sesión/ownership; fallo correo no revierte estado; incluir cada estado visual y transición documentada.
- **Terminado cuando:** Casos unitarios/componentes/API y E2E aplicables pasan con evidencias; pruebas mock y reales etiquetadas. Hallazgos corregidos/reprobados.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F035-QA-002

- **Trabajo:** Evento falso/replay/fuera de orden y firmas/scopes según contrato; no notificación inventada desde GET.
- **Terminado cuando:** Negativos de seguridad pasan en entorno propio/autorizado, scans SAST/SCA/secrets y DAST aplicable adjuntos sin secretos. Sin hallazgo crítico/alto explotable abierto.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F035-DOC-001

- **Trabajo:** Actualizar trazabilidad specs↔implementación↔pruebas, enlaces Figma y decisiones resueltas; documentar operación/errores relevantes.
- **Terminado cuando:** Fuentes vigentes coherentes, evidencias reales y revisión independiente; no marcar funcionalidad terminada con integración pendiente.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.


## Registro de revisión

### Avance local de H4 — 03/11/2026

Frontend añade un renderer server-only C-002 determinista con texto/HTML, escape de datos y CTA al origen configurado de Marketplace. La función sólo compone contenido cuando la invoca el servidor; no acepta webhook, no encola notificaciones ni comunica entrega del correo. El evento H-05 tiene payload publicado, pero el mecanismo de entrega, autenticación y reintentos de I-05 siguen pendientes.

Las pruebas server-side del renderer C-002 pasan junto con las otras suites BFF/renderer Frontend (5/5 en total; dos verifican templates). No se han implementado ni validado el endpoint receptor/worker, autenticación de G5 ni persistencia idempotente de este avance. #172 continúa bloqueada; no registrar integración o correo enviado.

### Revisión del contrato G5 — 04/11/2026

La rama principal vigente de `G5-Ventas-Postventas`, contrato `api-ventas.md` v1.8.0, ahora documenta que G5 persiste H-05 en su tabla outbox y reintenta en intervalos de 5 s hasta 10 intentos; `2xx` confirma, y `400/409/422` no se reintentan. Esto actualiza el estado del emisor respecto del registro anterior. No prueba entrega desde G5 hacia G1: aún falta acordar URL y autenticación del receptor, y ejecutar prueba conjunta de I-05. Referencia fijada al corte revisado: [contrato G5 1.10](https://github.com/Taller-SW-Web/G5-Ventas-Postventas/blob/f3e523cb2f7063d919f05a68601a699db86ba874/specs/api/api-ventas.md#110-webhook-de-estado-de-env%C3%ADo-acuerdo-h-05-con-marketplace).

En `feat/f028-f035-fernando-backend` se añadió `normalizeShipmentStatusWebhook` para validar fixtures H-05 v1.0.0, mantener `PED-YYYY-NNNNN` textual, aceptar sólo `DESPACHADO`/`ENTREGADO`, validar fecha calendario y copiar campos públicos. El consumer interno busca sólo un pedido G1 `SUCCEEDED` con email cifrado; si la relación no existe o es ambigua, no encola. Luego hace upsert inmutable de `NotificationDelivery` por `shipmentEventId`; una repetición idéntica devuelve la entrega existente y una reutilización del id con distinto payload entra en conflicto. C-002/worker pueden procesar esa entrega. Esta función sólo puede invocarse después de autenticar el evento; aún no existe endpoint receptor/auth ni se consume el webhook en runtime porque URL y autenticación G1↔G5 no están acordadas. Pruebas unitarias H-05/consumer/renderer quedan incluidas en la suite Backend completa, aprobada con 33 suites/307 pruebas; no se envió email. #170 avanza en parsing/persistencia local; #172 sigue bloqueada por URL/auth y prueba conjunta. No cerrar #170/171/172/173.

El contrato H-05 también dice que se emite al procesar `DESPACHO_REPROGRAMADO`, con nueva `estimatedDeliveryDate`, pero su ejemplo conserva `publicStatus: DESPACHADO` y no define un tercer valor público específico para reprogramación. El parser acepta la fecha opcional y los estados públicos `DESPACHADO`/`ENTREGADO`; no inventar `REPROGRAMADO` como estado público. Antes de la homologación REAL, confirmar con G5 que la reprogramación se entrega como `DESPACHADO` con nueva fecha (u otro valor público acordado) y ampliar el contrato/parser sólo si G5 lo confirma. La búsqueda de código de G5 no devolvió evidencia indexada suficiente para resolverlo; este punto queda abierto junto con URL/auth de I-05.

Verificación adicional del carril #98 al 04/11: Backend autenticación API 18/18 sobre PostgreSQL 16 desechable; Frontend auth Playwright 15/15 con G7 fixture. Son pruebas locales/mock, no autenticación con G7 ni recepción del webhook en entorno REAL.

| Fecha/semana | Cambios de estado | Evidencia / bloqueo / decisión | Revisó |
|---|---|---|---|
| Semana 6, preparación | Creación de tareas; sin ejecución | Specs y plan elaborados; integración pendiente donde se indica | Revisión humana pendiente |

Actualizar filas existentes; no crear un segundo conjunto de tareas por variante desktop/mobile ni por cada estado visual. Si hace falta dividir una tarea, conservar ID padre y crear sufijo incremental con alcance/existencia verificable.
