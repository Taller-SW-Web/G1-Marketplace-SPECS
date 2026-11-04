# Tareas y seguimiento — F-031 Reordenar una compra anterior

Versión 0.1.0 · Planificación inicial · F-031 no está implementada por estos documentos.

## Fuente y control

- [Plan F-031](../funcionalidades/F-031-reordenar-compra.md); [iteración S5](../iteraciones/S05-semanas-15-16.md).
- [Funcional](../../SPECS/funcional/F-031-reordenar-compra.md), [UI](../../SPECS/ui/F-031-reordenar-compra.md), [API](../../SPECS/contrato-api/F-031-reordenar-compra.md), [React](../../SPECS/componentes-react/F-031-reordenar-compra.md).
- [Reglas del seguimiento](README.md), [pruebas/DevSecOps](../DEVSECOPS-Y-PRUEBAS.md), [gates](../DECISIONES-Y-BLOQUEOS.md).
- Responsable asignado por el PO: **Fernando Saire**; revisor principal: **Jim Segovia** según la [matriz](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md). Estimación base fijada en la matriz; ejecución y evidencia pendientes. La semana objetivo es académica, no fecha de calendario.
- Mock y real se reportan por separado. QA local puede avanzar con fixtures; QA real requiere INT. Evidencia inicial pendiente, no pruebas ejecutadas.

## Corte planificado de H4

**Implementación y pruebas G1 en H4; cierre intermodular posterior.** Implementar recompra G1, dedupe/ajustes/transacción carrito, autorización del pedido y revalidación SKU/precio/cantidad G6; fixtures donde falte G5. Resolver I-03/G-REORDER antes del cierre S05.

**Cierre base:** S05/H6, semanas 15–16; implementación propia y pruebas con dobles en H4. Disponibilidad sin restricción horaria por decisión del PO. Las entregas «local» o «con dobles» son etapas del mismo TASK, no cierres de INT. DOC prepara desde specs y QA ejecuta casos propios antes de INT; el cierre completo conserva dependencias/DoD. [Alcance H4](../ALCANCE-H4-PRODUCTOS-SEGURIDAD.md). Los estados no cambian al replanificar.

Extensión por contratos: puede cerrar H4 si todas sus dependencias y pruebas reales pasan; mantener cierre base posterior hasta esa aceptación, sin duplicar conteo.

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
| TASK-F031-FE-001 | Frontend | Fernando Saire | Jim Segovia | P1 | TASK-TRANS-S01-OPS-001 | 9–11 implementación H4 | Pendiente |
| TASK-F031-BE-001 | Backend | Fernando Saire | Jim Segovia | P1 | TASK-TRANS-S01-OPS-001 | 9–11 implementación H4 | Pendiente |
| TASK-F031-INT-001 | Integración | Fernando Saire | Jim Segovia | P1 | TASK-F031-BE-001 + I-01 + I-03 + G-REORDER + TASK-F030-INT-001 + TASK-F016-INT-001 | 11 H4 REAL si gates; 16/S05 REAL | Bloqueado |
| TASK-F031-QA-001 | QA funcional | Fernando Saire | Jim Segovia | P1 | TASK-F031-FE-001 + TASK-F031-BE-001 | 11 H4 REAL si gates; 16/S05 REAL | Pendiente |
| TASK-F031-QA-002 | QA seguridad / DevSecOps | Fernando Saire | Jim Segovia | P1 | TASK-F031-FE-001 + TASK-F031-BE-001 + TASK-TRANS-S02-OPS-002 (local H4); TASK-TRANS-S05-OPS-002 (cierre posterior) | 11 H4 REAL si gates; 16/S05 REAL | Pendiente |
| TASK-F031-DOC-001 | Documentación | Fernando Saire | Jim Segovia | P1 | H4 diseño/implementación: specs y pruebas locales; cierre completo: TASK-F031-INT-001 + TASK-F031-QA-001 + TASK-F031-QA-002 | 11 H4 REAL si gates; 16/S05 REAL | Pendiente |

Referente de BD: Fernando Saire para este bloque, con revisión de Jim Segovia; Andres mantiene soporte transversal de migraciones. Ver [matriz](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md).

## Trabajo, Definition of Done y evidencia

### TASK-F031-FE-001

- **Trabajo:** Implementar ReorderAction, ReorderResultDialog y todos los estados de React/UI.
- **Terminado cuando:** Props/eventos tipados, estado específico, sin requests internos navegador; desktop/mobile aplicables y casos de spec React cubiertos.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F031-BE-001

- **Trabajo:** Autorizar pedido y revalidar cada SKU antes de sumar al carrito; resultados parciales y garantía de reintento no duplicador.
- **Terminado cuando:** DTO, validación, errores y ownership probados con fixtures; transacciones/versiones donde aplica. Adaptador real no activado si gate externo sigue abierto.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F031-INT-001

- **Trabajo:** Homologar y probar integración real y condiciones: I-01, I-03, G-REORDER; no sólo fixture.
- **Terminado cuando:** Contrato/configuración y gates enlazados, pruebas positivas/negativas y timeout autorizadas pasan; evidencia distingue sandbox de mock.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Falta cierre documentado de I-01, I-03, G-REORDER. Contrato/configuración y prueba enlazados antes de cambiar a En progreso.

### TASK-F031-QA-001

- **Trabajo:** Probar agotado excluido con razón; resultado parcial conserva elegibles; sin añadidos no éxito falso; doble click no repetir y timeout no auto retry; incluir cada estado visual y transición documentada.
- **Terminado cuando:** Casos unitarios/componentes/API y E2E aplicables pasan con evidencias; pruebas mock y reales etiquetadas. Hallazgos corregidos/reprobados.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F031-QA-002

- **Trabajo:** Reordenado de pedido ajeno y replay no incrementa duplicadamente, no precios históricos.
- **Terminado cuando:** Negativos de seguridad pasan en entorno propio/autorizado, scans SAST/SCA/secrets y DAST aplicable adjuntos sin secretos. Sin hallazgo crítico/alto explotable abierto.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F031-DOC-001

- **Trabajo:** Actualizar trazabilidad specs↔implementación↔pruebas, enlaces Figma y decisiones resueltas; documentar operación/errores relevantes.
- **Terminado cuando:** Fuentes vigentes coherentes, evidencias reales y revisión independiente; no marcar funcionalidad terminada con integración pendiente.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.


## Registro de revisión

### Alcance pendiente — 03/11/2026

No se modificó el carrito ni se presentó un resultado positivo simulado. La funcionalidad depende de validar SKUs/precio/stock en G6 y aplicar una operación idempotente al carrito; sin esas condiciones, una pantalla que informe éxito podría duplicar o aceptar productos no disponibles. I-01/#154 permanece bloqueada. Fernando confirmó que aún no cuenta con contratos, sandbox y credenciales aprobadas de G6; continuar sólo cuando se habilite el acceso o el equipo apruebe fixtures locales para esta operación.

### Evidencia local Frontend — 03/11/2026

En `feat/f028-f035-fernando-frontend` se añadieron los componentes presentacionales `ReorderAction` y `ReorderResultDialog`: el CTA evita doble acción durante `busy`, el resultado distingue completo/parcial/sin líneas agregadas, separa agregados de ajustes, ofrece “Ver carrito” sólo si la respuesta confirmada trae líneas agregadas y cierra con Escape con manejo de foco. Este corte inicial no los conectaba a una mutación; la conexión se documenta en la actualización del 04/11.

### Evidencia local Backend — 04/11/2026

En `feat/f028-f035-fernando-backend` F-031 tiene `POST /api/v1/orders/{orderId}/reorder`, autenticado, cuerpo vacío y `200`; requiere `Idempotency-Key` UUID v4 por intención. El servicio consulta el pedido propio mediante F-030, valida SKUs con un provider mock local, agrupa cantidades y agrega elegibles con precio actual validado en una transacción Cart. Guarda recibo por titular + pedido fuente + clave. PostgreSQL 16 temporal con las siete migraciones versionadas aplicadas: suite completa de integración 5/5 suites y 41/41 pruebas; el caso F-031 confirmó que dos solicitudes concurrentes con la misma clave hacen una sola suma y que una segunda clave intencional agrega una segunda vez (cantidad acumulada 6). La base fue descartada al terminar. La selección de fixtures/mock requiere `REORDER_ENABLED=true`, `REORDER_SOURCE=mock`, `ORDERS_SOURCE=mock` y `NODE_ENV=test`; el validator impide activarla en development o production y los valores por defecto siguen apagados. Backend unitario 33/33 suites y 307/307 pruebas, `typecheck` y `prisma validate` aprobados. Persisten I-01/I-03/G-REORDER, revisión independiente y G6 REAL apagado.

### Evidencia local Frontend — 04/11/2026

`OrderDetailContainer` conecta el CTA al BFF `POST /api/orders/{orderId}/reorder`. La ruta verifica mismo origen, rechaza Bearer directo/cuerpo/query, reenvía sólo cookie G1 permitida y conserva `no-store`. Emite UUID por acción y retiene la clave tras un error incierto; una acción nueva posterior al éxito usa otra clave. El diálogo usa únicamente la respuesta confirmada y navega a `/carrito` cuando hubo añadidos. `REORDER_UI_ENABLED=false` por defecto. Verificación dirigida actual: componentes del flujo 3/3 y BFF 4/4; typecheck aprobado. No es E2E contra backend desplegado ni integración con G6. El BFF local sólo funcionará al habilitar su flag de vista y el backend mock local; los valores por defecto siguen desactivados.

| Fecha/semana | Cambios de estado | Evidencia / bloqueo / decisión | Revisó |
|---|---|---|---|
| Semana 6, preparación | Creación de tareas; sin ejecución | Specs y plan elaborados; integración pendiente donde se indica | Revisión humana pendiente |

Actualizar filas existentes; no crear un segundo conjunto de tareas por variante desktop/mobile ni por cada estado visual. Si hace falta dividir una tarea, conservar ID padre y crear sufijo incremental con alcance/existencia verificable.
