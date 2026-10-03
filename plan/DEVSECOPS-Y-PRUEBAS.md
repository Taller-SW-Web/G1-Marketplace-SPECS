# DevSecOps y estrategia de pruebas por iteración

Versión 0.1.0 · En revisión · Semana 6–15. Esto especifica trabajo futuro, no escaneos ni pruebas ya ejecutadas.

## 1. Responsabilidad y límites

Andres es referente propuesto de pipeline/seguridad; Fernando de QA/verificación; Leonidas de correcciones y arquitectura; FE corrige componentes; Diego controla bloqueos; Jim valida riesgo/alcance. Revisor distinto al autor. Nombres completos en plan general.

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
| S1 semanas 6–7 | Registro/login/MFA/recuperación/reset/logout, fixtures y estado sesión | Antienumeración, rate limit, token expirado/used, MFA bypass, redirección, cookies/CORS/CSRF según transporte; scans iniciales | Resultados CI, política sesión, matriz amenazas y pruebas negativas sin secretos |
| S2 semanas 8–9 | Catálogo/paginación/variantes/precio/stock/adición | XSS, slug traversal, URL/medios SSRF, enum/query abusiva, no stock/costos internos; scans y DAST público propio | Reportes por F y prueba no datos privados |
| S3 semanas 10–11 | Cantidad/delete/merge/continuar/mover/favoritos, undo aprobado | IDOR en carrito/favoritos, CSRF, concurrencia versiones/fusión, aislamiento cachés entre usuarios y no doble suma | DB/contract/E2E con 2 cuentas de prueba y cookie invitado |
| S4 semanas 12–13 | Dirección/quote/cupón/preparación/orden/confirmación, timeout SUBMITTED | Token titular vs técnico, IDOR de dirección/quote/operación, alteración precio/cupón, idempotencia/replay, PII en logs/storage; DAST autenticado autorizado | Evidencia un pedido ante doble envío, mapeo de recuperación y no tarjeta |
| S5 semanas 14–15 | Pedidos/recompra/tracking/email/CSAT, regresión y responsive/a11y | IDOR en historial/tracking/CSAT, autenticación de webhook / replay de eventos, inyección de correo/URL, cifrado outbox, SAST/SCA/secrets/DAST finales y restauración de backup | Checklist release con riesgo residual, no envíos duplicados ni PII |

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

