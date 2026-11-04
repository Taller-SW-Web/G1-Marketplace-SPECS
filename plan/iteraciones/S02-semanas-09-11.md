# S2 — Integración de Productos y Seguridad, APIs y CI/CD

Versión 0.7.0 · Semanas 9–11, Hito 4 · 19/10/2026, Lima. El [inventario y dependencias](../ALCANCE-H4-PRODUCTOS-SEGURIDAD.md) clasifica las 40 F y las 25 dependientes de Productos. El [corte H3](../CORTE-H3-Y-TRASPASO-H4.md) conserva la evidencia histórica. Esta planificación asigna trabajo; no acredita su ejecución.

## Objetivo y alcance sin restricción horaria

**Principal: 25 F con objetivo de cierre H4:** **F-001–F-021 y F-036–F-039**. Son **20/20 del circuito de Productos** (20/25 de las dependientes G6) y **5/5 de cuenta/Seguridad**. Se retiran límites de horas y ampliaciones sujetas a tiempo. Registro, recuperación, relacionados, fusión y ambos movimientos se implementan e intentan integrar en H4 con los mismos criterios que el resto.

F-006/F-007 son arrastre H3. Se adelantan F-017/F-018 desde S03 y F-004/F-005/F-015/F-020/F-021/F-039 desde S05. Cada una exige contrato, provider autorizado, integración y prueba desplegada para cerrar; el número 25 es objetivo, no evidencia conseguida.

**Las otras 15 F también avanzan con implementación y pruebas propias G1 en H4.** Leonidas implementa F-022–F-027 y Fernando F-028–F-035; Diego implementa la parte G1 de F-040. Integran los tramos externos disponibles, con fixture rotulado y frontera aislada cuando falte contrato/entorno. No se inventan endpoints, reglas ni datos para completar una dependencia ajena. Checkout/pedidos/correos conservan cierre completo S03, seguimiento/evento S04 y filtro/recompra/CSAT S05.

CI/CD build/compile/test/deploy, diseño API completo y seguridad de pantallas/APIs son entregables obligatorios H4. La disponibilidad ilimitada del equipo permite ampliar trabajo propio; no concede acceso/grants ni acredita que G6/G7/G5/G2 estén listos. [Inventario de las 40 F y gates](../ALCANCE-H4-PRODUCTOS-SEGURIDAD.md).

**Extensión por contratos, sin condición de tiempo:** F-023/F-024/F-025/F-026 y F-031 pueden cerrar anticipadamente en H4 si también se liberan y prueban todas sus dependencias de Ventas/Despacho/Seguridad, además de G6. Son **5 F adicionales**, hasta **25/25 dependientes de Productos + 5 cuenta = 30 F distintas**. Su cierre base sigue S03 (cuatro) o S05 (recompra) hasta aceptación; después se descuenta de esa iteración y mantiene regresión. No se bloquea un cierre probado sólo para reservarlo a otro hito; H5/H6 conservan sus requisitos de ingeniería/calidad.

## Condiciones de factibilidad

1. Primero demostrar F-006/F-007 web→Next→BFF→G6 REAL, con positivo/vacío/error, URLs/SHAs y traza. Continuar F-008–F-011; acordar curaduría/campos/filtros sin omitir criterios para contar cierres.
2. Implementar/integrar F-012–F-015: precio, SKU, disponibilidad y relacionados; cerrar sólo con prueba REAL y contrato. productId ≠ variantId ≠ SKU; simple usa sku_base publicado. Orden sólo por nombre hasta homologación. G-G6-COMPAT debe resolver F-014 G1 (tres estados/agregación) frente a G6 (INDETERMINADO/fuente realizable).
3. Los cierres principales de carrito/favoritos F-016–F-021/F-036–F-039 exigen BD sana, titularidad, snapshot, cantidad y restauración. DISPONIBLE no prueba N unidades. DELETE es local, pero F-018/F-038 completas incluyen Deshacer acordado. Reservar/consumir pertenece a Ventas.
4. Separar sesión humana G7 de token técnico server-only G1→G6. No heredar grants de Chatbot ni exponer secretos en navegador.
5. **Revisión de gates al final de semana 9:** Diego registra por operación contrato/entorno/datos/credenciales/prueba faltante; Jim coordina con los owners externos y mantiene el principal de 25. Las partes G1 definidas se implementan/prueban mientras una frontera externa sigue bloqueada. No se recorta por horas ni se cierran gates con fixtures.

## Seguridad en pantallas y APIs

Jim implementa registro MARKETPLACE/verificación/retorno, login/desafío OTP efectivo, refresh/logout y recuperación/restablecimiento G7 durante H4. Registro no inicia sesión por inferencia. Confirmar registro/recuperación ejecutables con G7: no se encontró controlador HTTP en el corte revisado. Contrato v2 parcial MFA no autoriza un flujo incompatible. G1 no guarda contraseñas ni emite identidad.

**Actualización de alcance F-004/F-005 (decisión PO 26/10/2026):** la SPA G7 es la interfaz de recuperación y restablecimiento; G1 entrega la entrada desde Marketplace, mantiene su adaptador BFF e integra/prueba el retorno al login G1. La observación histórica sobre controladores faltantes corresponde al corte anterior: G7 confirmó v1 desplegada y G1 obtuvo `202` con correo y `204` de reset por API el 26/10. El retorno G7 → G1 y la UI completa aún no están probados. Ver [decisión y gates](../coordinacion/G7-F004-F005-ALCANCE-2026-10-27.md). No cerrar por esas respuestas aisladas.

Andres implementa/reutiliza el guard BFF común y Leonidas revisa: RS256/firma/JWKS, issuer, exp/nbf/sub/tipo=acceso según contrato, rotación/fallo de claves, roles/titularidad. El perfil humano G7 no exige audiencia adicional; el técnico usa validador separado aud/scope/cliente. Sandbox/HS256 se rechaza en modo REAL. Cada dueño aplica controles de propietario en su bloque.

UI protege cuenta/favoritos y operaciones autenticadas; catálogo y carrito invitado siguen públicos según spec. Probar también API directa: 401 sin sesión/vencida, 403 o error neutral contractual para dato ajeno, usuarios A/B aislados, refresh/logout y acceso público sin login. Definir/probar cookies/transporte, CSRF/CORS y retorno seguro con G7 antes de activarlos. Sin contraseñas, JWT, OTP ni PII en evidencias.

## APIs y CI/CD con responsables asignados

Los IDs siguientes llevan prefijo TASK-TRANS-S02-. El [tablero transversal](../seguimiento/TRANSVERSALES.md) conserva estados y semanas.

| Entrega / ID | Responsable | Revisor | Resultado verificable |
|---|---|---|---|
| OpenAPI BFF / API-001 | Leonidas | Jim | Semana 9: versión, rutas públicas/protegidas, DTO/errores/timeout/ownership/idempotencia; distinguir implementadas y propuestas; mapeos G6/G7 sin contratos inventados |
| Ejemplos y pruebas de contrato / API-002 | Sebastian | Leonidas | Semana 10: ejemplos positivos/negativos validados y consumer tests; cada owner aporta su operación; discrepancias enlazadas |
| Sesión G7 UI+BFF / AUTH-001 | Jim | Andres | Semanas 9–11: las 5 F de cuenta, verificación/MFA efectivo/refresh/logout y recuperación, dos usuarios y entorno real; contrato/dobles separados de integración |
| Guard/autorización compartida / SEC-001 | Andres | Leonidas | Semanas 10–11: JWT/JWKS, identidad humana/técnica separadas, owner en cada ruta y negativos |
| Identidad técnica G1→G6 / INT-001 | Leonidas | Jim | Semana 9: coordinar cliente/aud/scopes G7/G6 y probar grants por ruta; secretos sólo runtime |
| Pipeline / OPS-001/002 existentes | Andres | Leonidas | Validación PR/develop/main, instalación lockfile, compile/typecheck/lint, build FE/BE, tests/BD desechable/contratos/scans y deploy sólo tras checks aprobados |
| Preparación cloud y verificación CD / OPS-003 | Fernando | Andres | Semanas 10–11: variables/health/readiness, SHAs/artefactos/URLs, smoke, registro deploy y rollback; BD compartida con auditoría aparte |
| Verificación intermodular por F / QA-002 | Diego | Fernando | Semanas 10–11: matriz REAL/MOCK, positivo/vacío/error/timeout y usuarios A/B; provider directo distinto de web→BFF→G6 |
| E2E demo / QA-001 existente | Fernando | Jim | Semana 11: catálogo/ficha/carrito/favorito autenticado; negativos UI/API, logs saneados y revisión independiente |

OPS-001 conserva responsabilidad de Andres; Fernando colabora también en pasos build/deploy y runtime, Leonidas en contratos/API y Jim en sesión/consumo del guard. No se presupone que Andres ejecute solo cada paso. Si el revisor participó en el artefacto, Diego asigna segunda revisión independiente; nadie aprueba su trabajo.

Demostrar al menos un cambio del corte FE/BE desde verificación hasta despliegue. Asociar SHAs, versión OpenAPI, run CI, artefactos y ejecución CD; no reconstruir otro código sin trazabilidad. Un fallo build/test debe impedir deploy; ensayar rollback/smoke. No ocultar checks con continue-on-error. Migraciones desde cero en PostgreSQL desechable; historial/esquema Render se auditan por separado. YAML o deploy manual aislado no cierra CI/CD.

## Secuencia por semana

| Semana | Integración y trabajo propio | Decisión y evidencia |
|---|---|---|
| **9** | G-DB/CI/guard base Andres con Fernando; API/token G6 Leonidas; contratos/mapeos G6 Giuliano/Sebastian; G7 registro/sesión/recuperación Jim; Diego/Fernando dataset y casos. Jim crea V-011/V-013 mobile, Fernando revisa UI-001/002 | URLs/SHAs/grants y operaciones realmente ejecutables. Registrar y resolver G-G6-COMPAT/G-ADD/G-UNDO/G-QUANTITY; aislar sólo la frontera bloqueada |
| **10** | Implementar/integrar F-001–F-021 y F-036–F-039 por tramos G6/G7; todas las partes G1 de checkout/pedidos/correos/CSAT con pruebas. Jim corrige V-014 PAGADO con revisión Fernando. Ejemplos/consumer tests API-002 | Primera corrida compile/build/test/deploy y pruebas de contratos/BD/propietario/401/403/A-B; REAL y fixture diferenciados |
| **11** | Completar integración y retest por F principal; ejecutar CI/CD completo, smoke/rollback y demo web→BFF→G6/G7. Probar código propio de las otras 15 F y preparar I-02/I-03/I-05/I-06, gateway/evento H5 | Diego registra diseñado/datos de prueba/integrado/desplegado por F; Fernando verifica y Jim acepta con revisión independiente. Todo cierre requiere DoD; bloqueo externo conserva F parcial y pendiente trazable |

## Avance verificable de los siete integrantes

| Responsable / revisor funcional vigente | Corte propio H4 | Cantidad y límite |
|---|---|---|
| Jim / Andres | F-001–F-005 UI+BFF: registro/verificación, login/MFA, refresh/logout y recuperación/restablecimiento; tres correcciones visuales Checkout con Fernando | 5 cierres principales condicionados a G7/prueba; AUTH-001 adicional |
| Giuliano / Sebastian | F-006–F-010 REAL: inicio, búsqueda, filtros, orden y página; apoyo de tarjetas para relacionados | 5 cierres principales, incluidos 2 arrastre H3 |
| Sebastian / Giuliano | F-011–F-015 REAL: ficha/SKU/precio/estado comercial/relacionados; ejemplos y pruebas de contrato | 5 cierres principales; API-002 y DOC-001 adicionales |
| Andres / Leonidas | F-016–F-021: alta/cantidad/borrado/lectura/fusión/movimiento con BD, G6/G7 y fallos/concurrencia; pipeline/guard con colaboradores | 6 cierres principales; G-DB/CI-CD/SEC-001 adicionales |
| Diego / Fernando | F-036–F-039 completas con G6/G7 y handoff de carrito; implementar prompt/forma/adaptador F-040 según contrato y probarlo | 4 cierres principales + 1 implementación propia con cierre S05; QA/gates adicionales |
| Leonidas / Diego | F-022–F-027 FE+BE/adaptadores/pruebas propias y tramos G6 disponibles; aislar snapshot/envío/pedido/pago pendientes G5/G2 | 6 F implementadas/probadas en su alcance G1, cierre base S03; F-023–F-026 anticipables H4 con todos los gates; API-001/INT-001 adicionales |
| Fernando / Jim | F-028–F-035 FE+BFF/plantillas/worker/consumidor donde el contrato esté definido; pruebas locales y externas disponibles, con brechas aisladas | 8 F implementadas/probadas en su alcance G1; cierre integral S03/S04/S05 según F; cloud/CI-deploy/QA-001 adicionales |

Se conservan los diseñadores del [reparto UI](../../SPECS/ui/reparto/README.md). Dueño FE+BE y autor visual son campos distintos. Cada corte entrega commit, positivo/negativo, revisión y nivel de evidencia; los paquetes personales detallan trabajo y el tablero conserva su estado.

## Gates y continuación

Por F registrar **diseñado**, **implementado con datos de prueba**, **integrado con otro módulo** y **probado en el despliegue**, con evidencia/fecha de cada nivel. No inferir etapas ni cambiar a Terminado por planificar. Un 200 directo G6 no prueba la web; login visible no prueba autorización API. Falta de un criterio obligatorio conserva F Parcial.

H4 exige G6 REAL positivo y errores, G7 real UI+API, OpenAPI validado y build/compile/test/deploy del corte demostrado. Si falta una pieza, informar alcance parcial y gate abierto; ninguno se libera por esta actualización.

Partición objetivo sin duplicados: **H4 25 + S03 10 + S04 2 + S05 3 = 40 F**. S03 conserva F-022–F-028/F-030/F-033/F-034; S04 F-032/F-035; S05 F-029/F-031/F-040. Todas reciben trabajo propio H4. Un cierre principal H4 bloqueado externamente se registra como arrastre por su ID y causa, sin presentarlo como terminado ni duplicar el conteo. H5 conserva evento/gateway/performance y H6 seguridad/regresión/observabilidad. Ver [plan maestro](../PLAN-IMPLEMENTACION.md), [gates](../DECISIONES-Y-BLOQUEOS.md) y [seguimiento](../seguimiento/README.md).
