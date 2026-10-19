# Tareas transversales — hitos de semanas 8, 11, 14 y 16

Versión 0.4.0 · Propuesta punta a punta 2026-10-13, replanificada el 2026-10-18 con el [corte H3](../CORTE-H3-Y-TRASPASO-H4.md). Se conservan los 27 IDs y estados; las filas S01 arrastradas indican la semana original y la nueva semana objetivo de S2/H4. Responsables/revisores de S1–S5 son propuestas sujetas a estimación, aceptación y revisión cruzada; ninguna tarea se declara ejecutada por figurar aquí. Las tareas funcionales tienen owner en la [matriz](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md).

## Tablero único

| ID | Semana objetivo | Estado | Trabajo y evidencia de cierre |
|---|---:|---|---|
| TASK-TRANS-S01-OPS-001 | 7 | Pendiente | Base FE/BFF ejecutable; auditar Prisma/Render remotos; build/test mínimo, configuración de entornos, origen/CORS, secretos fuera de Git. Evidencia: commit, build y configuración saneada. |
| TASK-TRANS-S01-OPS-002 | 9 (original 8) | Pendiente · arrastre H3→H4 | Demostrar FE y BE desplegados del mismo corte; `/ready` y flujo web→BFF→Productos REAL. Evidencia: commits, URLs, petición/respuesta y logs sanitizados. La web demo MOCK no cierra esta tarea. |
| TASK-TRANS-S01-QA-001 | 9 (original 8) | Pendiente · arrastre H3→H4 | Probar F-006/F-007 en nube con dato REAL positivo, vacío, error, timeout, responsive y regresión mínima. Evidencia de integración distinta de fixture. |
| TASK-TRANS-S01-DOC-001 | 8 | Pendiente | Diagrama de contexto/arquitectura conforme despliegue, enlaces de repo/commit/contrato y registro de lo funcional/bloqueado. |
| TASK-TRANS-S01-DOC-002 | 7 | Pendiente | Estimar S1–S2, registrar capacidad real y decisión de prioridad H3; escalar I-01/entorno si no hay prueba intermodular posible. |
| TASK-TRANS-S01-DB-001 | 9 (original 7) | Bloqueado · arrastre H3→H4 | Reparar la migración que recrea `cart_items_product_id_idx`; probar instalación limpia/rollback en PostgreSQL desechable y auditar por separado historial y esquema real de Render, sin borrar datos compartidos. Ver G-DB. |
| TASK-TRANS-S02-OPS-001 | 9 | Pendiente | Publicar OpenAPI del BFF; CI/CD build, typecheck, tests y deploy por entorno, versionado/rollback y secretos. Primera corrida reproducible. |
| TASK-TRANS-S02-OPS-002 | 11 | Pendiente | Ejecutar pipeline con revisión de seguridad, controles SAST/SCA/secret scan y smoke de auth/API; corregir y retestar hallazgos. |
| TASK-TRANS-S02-QA-001 | 11 | Pendiente | E2E de segundo demo: catálogo/ficha/carrito/favoritos y autenticación UI+API; negativos JWT vencido, ownership y MFA según contrato. |
| TASK-TRANS-S02-DOC-001 | 11 | Pendiente | Enlazar diseño de APIs, specs, código, contratos externos, pruebas, URL de demo y evidencias CI/CD. |
| TASK-TRANS-S02-DOC-002 | 9 | Pendiente | Estimar carga S2–S3, revisar capacidad/cuello de botella y escalamiento de I-02/I-05/I-06 antes del hito siguiente. |
| TASK-TRANS-S03-OPS-001 | 12 | Pendiente | Preparar gateway/API Management, contrato de evento real con otro módulo, outbox/consumer, correlación, retry/deduplicación; entorno de prueba. |
| TASK-TRANS-S03-OPS-002 | 13 | Pendiente | Probar checkout/idempotencia, seguridad token titular/técnico, CORS/CSRF según transporte; preparar carga/umbrales y traza asíncrona. |
| TASK-TRANS-S03-QA-001 | 13 | Pendiente | E2E de dirección→cotización→pedido: cupón, timeout, doble clic, resultado incierto; `PREPARED`/`CREADO` nunca pagado. Prueba de F-034 asíncrona. |
| TASK-TRANS-S03-DOC-001 | 13 | Pendiente | Registrar contrato checkout/worker/evento, arquitectura actualizada, pruebas y gates; preparar evidencia H5. |
| TASK-TRANS-S03-DOC-002 | 12 | Pendiente | Reestimar S3–S5 y riesgo de H5/H6; confirmar proveedor de evento y autorización de carga antes de semana 14. |
| TASK-TRANS-S04-OPS-001 | 14 | Pendiente | Mostrar API Management aplicado y mensaje asíncrono entre módulos: productor/consumidor, esquema, correlación, reintento/dedupe y fallo recuperado. |
| TASK-TRANS-S04-OPS-002 | 14 | Pendiente | Ejecutar CI/CD con revisión de seguridad y prueba de performance autorizada (dataset, concurrencia, p50/p95, tasa de error, umbral); corregir/retest. |
| TASK-TRANS-S04-QA-001 | 14 | Pendiente | Prueba de integración positiva/negativa y de evento real para F-032/F-035; verificar traza y comportamiento ante timeout/duplicado. |
| TASK-TRANS-S04-DOC-001 | 14 | Pendiente | Publicar paquete de evidencia H5: versiones, commits, run CI/CD, contrato/proveedor, gateway, pruebas de integración/performance y limitaciones. |
| TASK-TRANS-S04-DOC-002 | 14 | Pendiente | Revisar gate H5 contra evidencia, registrar desvíos y capacidad restante para H6; no declarar completado un mock. |
| TASK-TRANS-S05-OPS-001 | 15 | Pendiente | Instalar observabilidad (logs, métricas, trazas) y alerta con owner/umbral; revisar arquitectura as built, backups/migraciones y rollback. |
| TASK-TRANS-S05-OPS-002 | 16 | Pendiente | Ejecutar dos controles/pruebas OWASP distintos y retest, escaneos de release, E2E/regresión y alerta disparada; archivar evidencia sanitizada. |
| TASK-TRANS-S05-QA-001 | 16 | Pendiente | Validar F-001–F-040 integradas, multi-módulo, responsive/a11y, seguridad y demo final reproducible; registrar hallazgos pendientes honestamente. |
| TASK-TRANS-S05-DOC-001 | 16 | Pendiente | Arquitectura final actualizada, trazabilidad specs↔código↔tests, evidencia UX y observabilidad/alertas, runbook y enlaces a repos/commits. |
| TASK-TRANS-S05-DOC-002 | 15 | Pendiente | Revisar capacidad de cierre, contribuciones Git verificables y riesgo de release; congelar alcance demostrado sin ocultar pendientes. |
| TASK-TRANS-S05-OPS-003 | 16 | Pendiente | Release final versionado en nube, smoke multi-módulo, rollback ensayado, enlaces/URL y evidencias de contribución y despliegue. |

## Regla de registro

### Responsables transversales propuestos para S1–S5

| ID | Responsable | Revisor |
|---|---|---|
| TASK-TRANS-S01-OPS-001 | Andres Morales | Leonidas Garcia |
| TASK-TRANS-S01-OPS-002 | Andres Morales | Leonidas Garcia |
| TASK-TRANS-S01-QA-001 | Diego Espinoza | Jim Segovia |
| TASK-TRANS-S01-DOC-001 | Jim Segovia | Diego Espinoza |
| TASK-TRANS-S01-DOC-002 | Jim Segovia | Diego Espinoza |
| TASK-TRANS-S01-DB-001 | Andres Morales | Leonidas Garcia |
| TASK-TRANS-S02-OPS-001 | Andres Morales | Leonidas Garcia |
| TASK-TRANS-S02-OPS-002 | Andres Morales | Leonidas Garcia |
| TASK-TRANS-S02-QA-001 | Fernando Saire | Jim Segovia |
| TASK-TRANS-S02-DOC-001 | Sebastian Malca | Jim Segovia |
| TASK-TRANS-S02-DOC-002 | Diego Espinoza | Jim Segovia |
| TASK-TRANS-S03-OPS-001 | Andres Morales | Leonidas Garcia |
| TASK-TRANS-S03-OPS-002 | Andres Morales | Leonidas Garcia |
| TASK-TRANS-S03-QA-001 | Diego Espinoza | Jim Segovia |
| TASK-TRANS-S03-DOC-001 | Sebastian Malca | Jim Segovia |
| TASK-TRANS-S03-DOC-002 | Diego Espinoza | Jim Segovia |
| TASK-TRANS-S04-OPS-001 | Andres Morales | Leonidas Garcia |
| TASK-TRANS-S04-OPS-002 | Andres Morales | Leonidas Garcia |
| TASK-TRANS-S04-QA-001 | Diego Espinoza | Jim Segovia |
| TASK-TRANS-S04-DOC-001 | Sebastian Malca | Jim Segovia |
| TASK-TRANS-S04-DOC-002 | Jim Segovia | Diego Espinoza |
| TASK-TRANS-S05-OPS-001 | Andres Morales | Leonidas Garcia |
| TASK-TRANS-S05-OPS-002 | Andres Morales | Leonidas Garcia |
| TASK-TRANS-S05-QA-001 | Fernando Saire | Jim Segovia |
| TASK-TRANS-S05-DOC-001 | Sebastian Malca | Jim Segovia |
| TASK-TRANS-S05-DOC-002 | Jim Segovia | Diego Espinoza |
| TASK-TRANS-S05-OPS-003 | Andres Morales | Leonidas Garcia |

El responsable de cada F conserva implementación FE+BE, pruebas y evidencia de su bloque; estas tareas transversales coordinan CI, QA, arquitectura, documentación y release. En un gate que incluye trabajo propio del revisor, asignar una segunda revisión independiente antes de aprobar. Fernando hace smoke cloud de H3, Leonidas revisa adaptadores, Jim acepta producto y Diego coordina QA/capacidad sin reemplazar la autoría individual. Ninguna asignación libera I-01–I-06 ni un G-*.

Para pasar a `En progreso`, asignar persona responsable y revisor distinto, aceptar estimación/alcance y comprobar dependencias. Para `Terminado`, añadir URL/commit/entorno/fecha/comando o caso/resultado y revisión, sin secretos ni PII. Un pipeline configurado sin corrida, un `render.yaml` sin URL verificada o un outbox sin otro módulo no cumplen los hitos. Las integraciones pendientes de contrato permanecen bloqueadas aunque el código local avance con fixtures.

[Plan maestro](../PLAN-IMPLEMENTACION.md) · [Iteraciones](../iteraciones/README.md) · [Decisiones y bloqueos](../DECISIONES-Y-BLOQUEOS.md).
