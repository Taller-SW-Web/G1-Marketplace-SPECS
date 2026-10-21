# Tareas transversales — hitos de semanas 8, 11, 14 y 16

Versión 0.7.0 · Replanificación 19/10/2026. Se conservan los 30 IDs/estados previos (incluidos arrastres y tres correcciones visuales) y se añaden 7 tareas H4: **37 tareas transversales**. Responsables/revisores quedan asignados para ejecutar el pedido del PO; no requieren aceptación individual previa. Asignación no acredita inicio ni cierre. La [matriz](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md) conserva owners funcionales; [S02](../iteraciones/S02-semanas-09-11.md) y [alcance y dependencias](../ALCANCE-H4-PRODUCTOS-SEGURIDAD.md) gobiernan prioridades.

## Tablero único

| ID | Semana objetivo | Estado | Trabajo y evidencia de cierre |
|---|---:|---|---|
| TASK-TRANS-S01-OPS-001 | 7 | Pendiente | Base FE/BFF ejecutable; auditar Prisma/Render remotos; build/test mínimo, configuración de entornos, origen/CORS, secretos fuera de Git. Evidencia: commit, build y configuración saneada. |
| TASK-TRANS-S01-OPS-002 | 9 (original 8) | Pendiente · arrastre H3→H4 | Demostrar FE y BE desplegados del mismo corte; `/ready` y flujo web→BFF→Productos REAL. Evidencia: commits, URLs, petición/respuesta y logs sanitizados. La web demo MOCK no cierra esta tarea. |
| TASK-TRANS-S01-QA-001 | 9 (original 8) | Pendiente · arrastre H3→H4 | Probar F-006/F-007 en nube con dato REAL positivo, vacío, error, timeout, responsive y regresión mínima. Evidencia de integración distinta de fixture. |
| TASK-TRANS-S01-DOC-001 | 8 | Pendiente | Diagrama de contexto/arquitectura conforme despliegue, enlaces de repo/commit/contrato y registro de lo funcional/bloqueado. |
| TASK-TRANS-S01-DOC-002 | 7 | Pendiente | Registrar decisiones y dependencias del corte histórico S1/H3; aplicar disponibilidad sin restricción horaria a S02; escalar I-01/entorno si no hay prueba intermodular posible. |
| TASK-TRANS-S01-DB-001 | 9 (original 7) | Bloqueado · arrastre H3→H4 | Reparar la migración que recrea `cart_items_product_id_idx`; probar instalación limpia/rollback en PostgreSQL desechable y auditar por separado historial y esquema real de Render, sin borrar datos compartidos. Ver G-DB. |
| TASK-TRANS-S02-OPS-001 | 9 | Pendiente | Integrar OpenAPI de API-001/002 al pipeline: instalación lockfile, compile/typecheck/lint/build FE+BE, tests con PostgreSQL desechable y contratos; disparadores PR/develop/main, deploy tras checks, versionado/rollback/secretos. Evidencia de un cambio desde run hasta CD, más prueba de fallo que bloquee deploy. |
| TASK-TRANS-S02-OPS-002 | 11 | Pendiente | Ejecutar pipeline con revisión de seguridad, controles SAST/SCA/secret scan y smoke de auth/API; corregir y retestar hallazgos. |
| TASK-TRANS-S02-QA-001 | 11 | Pendiente | E2E de segundo demo: catálogo/ficha/carrito/favoritos y autenticación UI+API; negativos JWT vencido, ownership y MFA según contrato. |
| TASK-TRANS-S02-DOC-001 | 11 | Pendiente | Enlazar diseño de APIs, specs, código, contratos externos, pruebas, URL de demo y evidencias CI/CD. |
| TASK-TRANS-S02-DOC-002 | 9 | Pendiente | Seguir los 25 objetivos H4 y las partes G1 de las otras 15 F; registrar contrato/entorno/datos/grants y escalamiento I-02/I-03/I-05/I-06 por operación. La disponibilidad no limita alcance. |
| TASK-TRANS-S02-UI-001 | 9 · H4 | Pendiente · traspaso visual | Crear en la [página Checkout](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=1-5) el frame exacto `V-011 / Mobile / Promoción automática`, conforme a [V-011](../../SPECS/ui/vistas/V-011-resumen-envio-beneficio.md) y F-024. Cierre: enlace directo en la spec, estado/promoción comprensibles en mobile y revisión de Fernando registrada. |
| TASK-TRANS-S02-UI-002 | 9 · H4 | Pendiente · traspaso visual | Crear en la [página Checkout](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=1-5) el frame exacto `V-013 / Mobile / Operación no preparada`, conforme a [V-013](../../SPECS/ui/vistas/V-013-creacion-orden.md). Cierre: enlace directo en la spec, mensaje/acción de recuperación sin confirmar compra y revisión de Fernando registrada. |
| TASK-TRANS-S02-UI-003 | 10 · H4 | Pendiente · traspaso visual | Corregir el [frame V-014 / Desktop / Confirmado](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=420-6225) para que confirme sólo `PAGADO` verificado por Ventas; quitar la combinación de `CREADO` con «pago simulado aprobado», revisar coherencia del equivalente mobile y [V-014](../../SPECS/ui/vistas/V-014-pedido-confirmado.md). Cierre: enlaces a frames corregidos, copy coherente con F-027 y revisión de Fernando registrada. |
| TASK-TRANS-S02-API-001 | 9 | Pendiente | Leonidas diseña/versiona OpenAPI BFF: rutas públicas/protegidas, DTO/errores/timeout/ownership/idempotencia y mapa G6/G7; distinguir implementadas/propuestas, registrar G-G6-COMPAT. Cierre: schema válido, revisión Jim y trazabilidad por operación, sin declarar runtime. |
| TASK-TRANS-S02-API-002 | 10 | Pendiente | Sebastian valida ejemplos/schema y pruebas consumidor con casos positivos/negativos aportados por cada owner. Cierre: versión/commit, comandos/resultados y revisión Leonidas; dobles separados de provider REAL. |
| TASK-TRANS-S02-AUTH-001 | 9–11 | En progreso | Jim implementa las cinco F de cuenta: registro/verificación/retorno, login/MFA efectivo, refresh/logout y recuperación/restablecimiento UI+BFF con G7. Bloqueo: confirmar implementación/URL/issuer/transporte y usuarios de prueba. Cierre: evidencia G7 por F-001–F-005, positivos/negativos y UI/API revisados por Andres. Si una operación G7 falta, conservar su TASK/INT bloqueado; tiempo disponible no equivale a provider listo. |
| TASK-TRANS-S02-SEC-001 | 10–11 | Pendiente | Andres reutiliza/completa guard RS256/JWKS, claims/roles/titularidad y separación usuario/servicio; owners aplican a sus rutas. Cierre: expiración/firma/tipo/usuario ajeno, API directa/UI, rechazo sandbox en REAL y revisión Leonidas. |
| TASK-TRANS-S02-INT-001 | 9 | Bloqueado | Leonidas coordina/provisiona por canales autorizados token técnico G1→G6. Bloqueo: grant G7/G6 por cliente/aud/scope/ruta y entorno. Cierre: 200/401/403 reales, fuente/versión/fecha y revisión Jim; secreto fuera de browser/Git. |
| TASK-TRANS-S02-QA-002 | 10–11 | Pendiente | Diego verifica integración individual de F: positivo/vacío/error/timeout, usuarios A/B, source REAL/MOCK y contrato/provider. Cierre: matriz de casos/resultados/trazas revisada por Fernando; no confundir prueba directa G6 con web desplegada. |
| TASK-TRANS-S02-OPS-003 | 10–11 | Pendiente | Fernando prepara/verifica runtime cloud, variables/readiness, SHAs/artefactos/URLs, smoke y rollback del corte CI/CD. Cierre: registro de deploy/prueba de recuperación y revisión Andres; auditar Render antes de tocar esquema compartido. |
| TASK-TRANS-S03-OPS-001 | 12 | Pendiente | Preparar gateway/API Management, contrato de evento real con otro módulo, outbox/consumer, correlación, retry/deduplicación; entorno de prueba. |
| TASK-TRANS-S03-OPS-002 | 13 | Pendiente | Probar checkout/idempotencia, seguridad token titular/técnico, CORS/CSRF según transporte; preparar carga/umbrales y traza asíncrona. |
| TASK-TRANS-S03-QA-001 | 13 | Pendiente | E2E de dirección→cotización→pedido: cupón, timeout, doble clic, resultado incierto; `PREPARED`/`CREADO` nunca pagado. Prueba de F-034 asíncrona. |
| TASK-TRANS-S03-DOC-001 | 13 | Pendiente | Registrar contrato checkout/worker/evento, arquitectura actualizada, pruebas y gates; preparar evidencia H5. |
| TASK-TRANS-S03-DOC-002 | 12 | Pendiente | Reestimar S3–S5 y riesgo de H5/H6; confirmar proveedor de evento y autorización de carga antes de semana 14. |
| TASK-TRANS-S04-OPS-001 | 14 | Pendiente | Mostrar API Management aplicado y mensaje asíncrono entre módulos: productor/consumidor, esquema, correlación, reintento/dedupe y fallo recuperado. |
| TASK-TRANS-S04-OPS-002 | 14 | Pendiente | Ejecutar CI/CD con revisión de seguridad y prueba de performance autorizada (dataset, concurrencia, p50/p95, tasa de error, umbral); corregir/retest. |
| TASK-TRANS-S04-QA-001 | 14 | Pendiente | Prueba de integración positiva/negativa y de evento real para F-032/F-035; verificar traza y comportamiento ante timeout/duplicado. |
| TASK-TRANS-S04-DOC-001 | 14 | Pendiente | Publicar paquete de evidencia H5: versiones, commits, run CI/CD, contrato/proveedor, gateway, pruebas de integración/performance y limitaciones. |
| TASK-TRANS-S04-DOC-002 | 14 | Pendiente | Revisar gate H5 contra evidencia, registrar bloqueos técnicos/contractuales y evidencia pendiente H6; no declarar completado un mock. |
| TASK-TRANS-S05-OPS-001 | 15 | Pendiente | Instalar observabilidad (logs, métricas, trazas) y alerta con owner/umbral; revisar arquitectura as built, backups/migraciones y rollback. |
| TASK-TRANS-S05-OPS-002 | 16 | Pendiente | Ejecutar dos controles/pruebas OWASP distintos y retest, escaneos de release, E2E/regresión y alerta disparada; archivar evidencia sanitizada. |
| TASK-TRANS-S05-QA-001 | 16 | Pendiente | Validar F-001–F-040 integradas, multi-módulo, responsive/a11y, seguridad y demo final reproducible; registrar hallazgos pendientes honestamente. |
| TASK-TRANS-S05-DOC-001 | 16 | Pendiente | Arquitectura final actualizada, trazabilidad specs↔código↔tests, evidencia UX y observabilidad/alertas, runbook y enlaces a repos/commits. |
| TASK-TRANS-S05-DOC-002 | 15 | Pendiente | Revisar gates de cierre, contribuciones Git verificables y riesgo de release; congelar alcance demostrado sin ocultar pendientes. |
| TASK-TRANS-S05-OPS-003 | 16 | Pendiente | Release final versionado en nube, smoke multi-módulo, rollback ensayado, enlaces/URL y evidencias de contribución y despliegue. |

## Regla de registro

### Responsables transversales asignados para S1–S5

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
| TASK-TRANS-S02-UI-001 | Jim Segovia | Fernando José Saire Tello |
| TASK-TRANS-S02-UI-002 | Jim Segovia | Fernando José Saire Tello |
| TASK-TRANS-S02-UI-003 | Jim Segovia | Fernando José Saire Tello |
| TASK-TRANS-S02-API-001 | Leonidas Garcia | Jim Segovia |
| TASK-TRANS-S02-API-002 | Sebastian Malca | Leonidas Garcia |
| TASK-TRANS-S02-AUTH-001 | Jim Segovia | Andres Morales |
| TASK-TRANS-S02-SEC-001 | Andres Morales | Leonidas Garcia |
| TASK-TRANS-S02-INT-001 | Leonidas Garcia | Jim Segovia |
| TASK-TRANS-S02-QA-002 | Diego Espinoza | Fernando Saire |
| TASK-TRANS-S02-OPS-003 | Fernando Saire | Andres Morales |
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

El responsable de cada F conserva implementación FE+BE, pruebas y evidencia de su bloque; estas tareas transversales coordinan CI, QA, arquitectura, documentación y release. En un gate que incluye trabajo propio del revisor, asignar una segunda revisión independiente antes de aprobar. Fernando hace smoke cloud de H3, Leonidas revisa adaptadores, Jim acepta producto y Diego coordina QA/gates sin reemplazar la autoría individual. Ninguna asignación libera I-01–I-06 ni un G-*.

Para pasar a `En progreso`, confirmar inicio efectivo, responsable/revisor distintos, contrato y dependencias; la asignación no exige aceptación individual previa. Para `Terminado`, añadir URL/commit/entorno/fecha/comando o caso/resultado y revisión, sin secretos ni PII. Un pipeline configurado sin corrida, un `render.yaml` sin URL verificada o un outbox sin otro módulo no cumplen los hitos. Las integraciones pendientes de contrato permanecen bloqueadas aunque el código local avance con fixtures.

[Plan maestro](../PLAN-IMPLEMENTACION.md) · [Iteraciones](../iteraciones/README.md) · [Decisiones y bloqueos](../DECISIONES-Y-BLOQUEOS.md).

## Evidencia H4 y secuencia de dependencias

G-DB y versión del corte → contrato/API-001 e identidad técnica INT-001 → implementación funcional/guard/ejemplos API-002 → tests/OPS-001/002 → deploy/OPS-003 → QA-002 por operación y QA-001 del demo. AUTH-001 coordina las tareas F-001–F-005 y SEC-001 el guard; estas tareas son coordinación/implementación compartida, no sustituyen los TASK funcionales ni crean cierres circulares entre sí. Se puede diseñar/probar con dobles mientras el INT externo está bloqueado; la aceptación REAL espera contrato/configuración/provider.

Cada entrega registra cuatro niveles separados: diseñado, implementado con datos de prueba, integrado con otro módulo y probado en el despliegue. Mantener el estado original hasta prueba de su DoD. CI/CD requiere build/compile/test/deploy del mismo corte, bloqueo de deploy ante fallo y recuperación/smoke; API necesita schema/ejemplos/errores y prueba; auth exige UI y API directa con propietario real. Si un revisor aportó al artefacto, Diego asigna otra revisión independiente.

## Disponibilidad y coordinación de H4

El PO establece disponibilidad sin restricción horaria. Se retiran presupuestos diarios/semanales y promociones por tiempo. Principal de 25 F (20 Productos + 5 cuenta); todas las otras 15 reciben implementación/pruebas G1 conforme fuentes. Fernando colabora build/deploy/runtime de OPS-001/003, Leonidas contratos/API y Jim sesión; Andres conserva responsabilidad CI/guard. Diego sigue progreso, gates y calidad. No se modifica ningún estado al ampliar planificación; [S02](../iteraciones/S02-semanas-09-11.md) conserva DoD por función.

### Avance AUTH H4 — 21/10/2026

Ampliación: BE `224486b` prepara introspección G7 detrás de flag apagado; firma antes de consulta, credencial técnica sólo servidor, sin caché de actividad ni fallback ante fallo. Recarga invalida fila/cookie revocadas; fallo transitorio no declara logout. [Evidencia](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/blob/feat/s2-f002-f003-g7/docs/evidencias/H4/jim-segovia/INTROSPECCION-H4.md): 148 unitarias/189 e2e locales y CI PostgreSQL50 casos PASS; scans del corte PASS con los mismos moderados de desarrollo pendientes. No hay cliente/scope/despliegue confirmados; mantiene INT Bloqueado y revisión Andrés pendiente.

Actualización QA: [evidencia FE](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/blob/feat/s2-f002-f003-g7/docs/evidencias/H4/jim-segovia/SEGURIDAD-H4.md) y [BE](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/blob/feat/s2-f002-f003-g7/docs/evidencias/H4/jim-segovia/SEGURIDAD-H4.md) incorporan SAST/SCA/secrets e inventario ejecutados en CI, con límites y revisión pendientes. BE mantiene19 moderados de desarrollo; runtime0. DAST y aceptación de riesgo no se infieren del PASS automático. La [propuesta de sesión temporal](../../Arquitectura%20de%20la%20Aplicación/Base%20de%20Datos/05-Propuesta-sesion-temporal-H4.md) explicita la excepción arquitectónica y requiere aprobación.

Jim avanza implementación/pruebas propias de F-001–F-005 en [FE #105](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/pull/105) y [BE #229](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/pull/229), con contrato propuesto [SPECS #9](https://github.com/Taller-SW-Web/G1-Marketplace-SPECS/pull/9). FE `49e6281`: 201 componentes/73 servidor y 5 recorridos navegador con fixture PASS; BE `06f950f`: 26 casos dirigidos locales y CI PostgreSQL 30 PASS incluyendo auth previo. Revisión Andrés pendiente. Las INT por operación permanecen bloqueadas: Jim confirma pendientes las cuentas A/B y URL/revisiones BFF desplegadas; registro y recuperación/restablecimiento aún pendientes de publicación G7 y apagados por defecto. Las evidencias completas están enlazadas en el seguimiento de cada F. Los tests locales no liberan G-AUTH ni G-DB. No se completa esta transversal por el avance local; F-020, política por etapa de O-004, documentos legales y prueba REAL conservan sus gates.
