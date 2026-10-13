# DevSecOps y estrategia de pruebas por iteración

Versión 0.2.0 · En revisión · Semanas 7–16. Esto especifica trabajo futuro, no escaneos ni pruebas ya ejecutadas.

## 1. Responsabilidad y límites

Las funciones de pipeline/seguridad, QA/verificación, corrección técnica y aceptación de riesgo deben tener responsables y revisores distintos; **la matriz de bloques fija responsables por decisión del PO; la capacidad real se vigila durante la ejecución**. Las tareas transversales proponen responsable/revisor en [TRANSVERSALES](seguimiento/TRANSVERSALES.md). El reparto de mockups no asigna código.

Sólo pruebas sobre entornos propios o expresamente autorizados. No hacer DAST, fuzzing, carga, intentos de autenticación o escaneos al GitHub/Figma/servicios de otros grupos sin permiso. Proveedor simulado prueba contratos, no seguridad de tercero.

## 2. Pipeline propuesto desde S1 y repetido en cada sprint

1. Instalación reproducible de dependencias con lockfile; ningún secreto en scripts/bundle.
2. Typecheck, lint y build FE/BE; test unitario/componentes y API contra fixtures.
3. Secret scanning de cambios y artefactos; SAST de TS/JS, SCA de runtime/dev y licencias. Seleccionar herramienta disponible y fijar versión en código, sin afirmar una ya instalada aquí.
4. PostgreSQL 16 temporal de prueba, migraciones Prisma, constraints/triggers y transacciones; ninguna conexión a BD ajena.
5. Contract tests BFF/adaptadores, mocks de errores/timeout/concurrencia.
6. E2E en entorno efímero propio, pruebas de accesibilidad y negativos de seguridad.
7. DAST baseline en staging propio y validación manual dirigida; no ejecutar escaneo autenticado con cuentas reales/PII.
8. Artefactos/evidencias sin tokens/direcciones/documentos/email claro; retención definida, acceso equipo, no dumps sensibles en CI.

Cada sprint incluye tareas OPS de escaneos y QA-002 por funcionalidad. La configuración no sustituye la ejecución. Dependencias vulnerables no se declaran seguras porque build pasa.

## 3. Cobertura por sprint

| Sprint | Pruebas funcionales | Seguridad / DevSecOps | Evidencia y salida |
|---|---|---|---|
| S1 semanas 7–8 | Home/búsqueda real con Productos, backend/frontend desplegados | Query abusiva, errores/timeout, CORS, secretos, XSS y escaneo inicial sobre entorno propio | H3: URL, prueba web→BFF→Productos, build/test y logs sanitizados |
| S2 semanas 9–11 | Registro/login/logout, catálogo/ficha/carrito/favoritos básicos | JWT expirado, MFA, ownership, rate limit, IDOR, XSS/SSRF y escaneos CI/CD | H4: autenticación UI+API, OpenAPI, ejecución build/test/deploy y segundo demo |
| S3 semanas 12–13 | Cantidad/quitar, dirección/quote/cupón/pedido y correo asíncrono | CSRF/concurrencia, token titular vs técnico, alteración de montos, idempotencia/replay, PII y DAST propio | Checkout sin pago ficticio; worker/evento y carga de prueba preparados |
| S4 semana 14 | Seguimiento/evento de despacho y pruebas de integración/performance | Autenticación del mensaje, duplicados/reintento, gateway, scans y revisión de seguridad CI/CD | H5: traza intermodular, prueba de integración y carga con p50/p95/errores/umbral |
| S5 semanas 15–16 | Recuperación, fusión, postventa/CSAT y regresión integral | IDOR histórico/CSAT, seguridad de recuperación, OWASP al menos dos evidencias, SAST/SCA/DAST finales, alertas y rollback | H6: release integrado, arquitectura as built, alertas disparadas y riesgo residual registrado |

## 4. Matriz de pruebas mínimas por capa

- **Unitarias:** normalización de query/slug/enums, selección única de SKU, clave/fingerprint, mapeo de errores, transformaciones DTO/CSAT, sin políticas inventadas.
- **React/componentes:** props/eventos, cada estado UI, foco/modal/undo, formularios y filtros, caché/cuenta nueva, error vs vacío, timeout vs confirmado.
- **API/BFF:** validación 400/401/403/404 neutral/409/422/429/5xx según contrato, JWT/canal/scopes, campos prohibidos, requestId sin secreto.
- **DB:** ownership XOR, Cart.version atómica, unicidad SKU/favorito, destino MERGED válido, seis entidades permitidas, rollback parcial, cifrado de recipient y carrera de outbox.
- **Contract:** fixture validado/inválido y mapeo todos los campos, paginación, errores/timeout, compatibilidad de versiones; sandbox externo sólo homologado.
- **E2E:** invitado → carrito → login/MFA → merge exitoso/fallido y continuar; favoritos; checkout y duplicado/incierto; pedido propio/history/tracking; email asíncrono; encuesta entregado.
- **Accesibilidad/responsive:** navegación teclado, nombres, aria-live no duplicado, contraste, zoom/reflow y controles móviles; correo sin imágenes y texto plano.
- **Resiliencia:** latencia de catálogo/precio independiente, expiración de quote, proveedor Ventas con timeout y respuesta tardía, carreras de worker / reintentos, eventos duplicados.

No porcentaje de cobertura ficticio: se exige cubrir cada criterio funcional/UI/API/React con al menos un caso/evidencia y todos los riesgos críticos/altos. El porcentaje se acordará tras establecer baseline, no reemplaza casos de seguridad.

## 5. Criterios de bloqueo de entrega

Bloquear release por vulnerabilidad crítica/alta explotable, secreto expuesto, JWT/MFA bypass, acceso a datos ajenos, duplicación de pedido/envío por carrera, persistencia prohibida, pérdida silenciosa de carrito, o flujo real habilitado sin contrato.

Fallo scan→ticket/corrección/retest y evidencia; falso positivo necesita justificación revisada, no excluir regla globalmente. Riesgo medio/bajo requiere dueño/fecha y aceptación registrada del equipo. Ningún hallazgo pendiente se oculta para declarar Done.

Si se detecta secreto: detener difusión, retirar de logs/artefactos y **coordinar rotación/revocación** con dueño; borrar texto no invalida credencial. No ejecutar cambios de infraestructura externos como parte de esta entrega documental.

## 6. Evidencias y trazabilidad

Formato por tarea: ID, commit/revisión futuro, comando/herramienta/versión, entorno, fixtures y cuentas no sensibles, casos/resultado/fecha, hallazgos, corrección/retest y revisor. Sanitizar screenshots y reportes.

Guardar evidencia en rutas del repo de código o almacenamiento autorizado y enlazarla desde plan/seguimiento; no crear resultados inventados. Inicialmente todas las evidencias están pendientes. Distinguir simulación, sandbox homologado y producción.
