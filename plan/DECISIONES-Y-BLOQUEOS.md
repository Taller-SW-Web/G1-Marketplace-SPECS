# Decisiones y bloqueos de implementación

Versión 0.1.0 · En revisión · Corte local 2026-10-02. No se han consultado ni actualizado remotos en esta preparación.

## Integraciones externas: evidencia pendiente, no solicitudes nuevas

Fuente: [brechas BD/integración](../Arquitectura%20de%20la%20Aplicación/Base%20de%20Datos/03-Decisiones-y-brechas-de-integracion.md) y contratos F individuales. Se respeta el acuerdo de verificación de Seguridad registrado en F-001; los estados siguientes no significan que nadie haya respondido, sino que **falta registrar contrato/configuración/prueba suficiente en repo para activar integración**.

| Gate | Funcionalidades | Evidencia que libera | Referente / objetivo |
|---|---|---|---|
| I-01 / H-01 | Catálogo F-006–017,019–021,023–026,031,036–037,039 | OpenAPI de Catálogo/Pricing/Inventario/Promociones con rutas/auth/error, payload y prueba de mapeo | Leonidas + Jim, antes S2; fixture local no libera |
| I-02 / H-02 | F-025–027,034 | Ventas idempotente con misma clave/payload; misma clave con payload distinto se rechaza; pruebas de timeout/concurrencia | Leonidas + Jim, antes S4 |
| I-03 / H-03 | F-028–032,040 | Autorización del titular en lista/detalle de Ventas y prueba IDOR; query cliente externo validada contra JWT o /me | Leonidas + Jim, antes S5 |
| I-04 / H-04 | F-040 | Elegibilidad entregado/ownership, mapeo5/3/1 y motivos/comentario, prueba duplicado | Jim + Leonidas, antes S5 |
| I-05 / H-05 | F-035 y origen externo de notificaciones si aplica | Emisor/destinatario, evento versionado, autenticación, dedupe/orden/replay y prueba | Leonidas + Andres, preparar S3 cerrar antes S5 |
| I-06 / H-06 | F-023,025,032 | Cliente técnico por ambiente y scopes cotizaciones:calcular/seguimientos:leer probados; acuerdo Seguridad no basta sin Despacho | Andres + Leonidas, antes S4 |

Cuando se libere un gate: enlazar evidencia/versiones, fecha, aprobador y prueba; revisar tareas dependientes manualmente. No marcar todos los INT como terminados por recibir una respuesta de chat.

## Brechas técnicas locales detectadas y tratamiento

| Gate | Evidencia / problema | Tratamiento para código (sin endpoint inventado) | Referente / fecha |
|---|---|---|---|
| G-STACK | DS-001 Mantine/Tabler preliminar vs README Tailwind/shadcn; frontend sólo README | Aprobar una biblioteca, versiones compatibles y lockfile; ajustar docs al decidir, no mantener dos sistemas | Giuliano + Leonidas, semana 6 |
| G-SHELL | Header/footer final aún no aprobado en UI; checkout sólo logo+4 etapas fue preferencia del PO | Diseñar wrappers desacoplados. Validar logo/no salida accidental/progreso y footer antes pixel final; sin rutas legales/ayuda supuestas | Giuliano + Jim, antes integrar layouts |
| G-AUTH | F-002 abrevia token/desafío, no MFA/refresh/transporte completo; políticas y URLs base pendientes | Tipos de desafío, endpoint MFA, transporte seguro/CORS/CSRF, expiración y PASSWORD_CADUCADA según Seguridad. Registro usa canal fijo y regreso /login sin token | Andres + Leonidas, semana 6–7 |
| G-SKU | F-011 no devuelve SKU; ejemplo variantes sólo hasVariants=true | Extender/documentar proyección autorizada de SKU simple de F-013; frontend nunca usa productId como SKU | Leonidas, antes F-016 S2 |
| G-ADD | F-016 409 stock retorna ajustado vs CA dice ninguna mutación en fallo | Aclarar estados que confirman ajuste frente rechazo sin mutación; UI sólo acepta snapshot confirmado, nunca incremento supuesto | Leonidas + Jim, S2 |
| G-UNDO | UI exige Deshacer y O-006 reconoce contrato de restauración no aprobado | Carrito: definir operación/restauración concurrencia/stock; F-016 suma y no garantiza restaurar cantidad original. Favoritos: reutilizar F-036 tras DELETE, producto puede no estar activo. Sin resolver no prometer restauración ni marcar F-018/038 completas | Leonidas + Sebastian + Fernando, S3 |
| G-ADDRESS | label/phone/mapa maestros no completamente definidos | Usar campos contractuales, token titular y memoria; acordar límites y fuente geo. No añadir mapas/SUNAT/RENIEC por mockup | Andres + Jim, antes S4 |
| G-BENEFIT | Quitar cupón y degradación error no endpoints/política completos | Recotizar F-023 sin cupón; confirmar combinabilidad/formato y validez quote base. Sin monto autoritativo no continuar | Leonidas + Jim, S4 |
| G-CHECKOUT | POST preparación/orden usan distinto payload y misma tabla key/fingerprint; reload/TTL no definido | Definir ámbito/fingerprint por fase y clave estable de operación. GEToperation necesita operación conocida. Recuperación segura y mapeo orderId↔operationId; no inventar lookup ni reenvío nuevo en SUBMITTED | Leonidas + Andres, antes S4 |
| G-CONFIRM | V-014 pública por orderId, API GET por operationId; resumen artículos/email faltan | Durante flujo conservar asociación opaca; deep link/reload requiere contrato acordado, detalle F-030 sólo confirma pedido autorizado, no sustituye resultado operación. No cart reconstruido | Leonidas + Jim, S4 |
| G-REORDER | POST reorder sin clave; unicidad SKU no impide doble aumento | Homologar garantía de dedupe/idempotencia con backend. Timeout relee carrito y nunca retry automático de POST; cerrar V-016-OPEN-03 | Leonidas, antes S5 |
| G-PROMPT | CSAT POST existe, leer/elegible/SHOWN/DISMISSED no endpoints en contrato | Diseñar ciclo prompt y políticas ahora no/Escape/superficies V-016/017; ampliar contrato antes persistir transiciones reales. No deducir durable status desde localStorage | Jim + Leonidas + Fernando, antes S5 |
| G-MAIL | Proveedor/motor/retención/retry y fuente de payload no cerrados | Email server-only, outbox y cifrado/reconciliación provider timeout, URLs seguras. React renderer opcional, no librería instalada por suposición | Andres + Leonidas, preparar S3 cerrar S5 |
| G-DB | README y guía refieren04-esquema-inicial-postgresql.sql, pero archivo no existe en checkout; frontend/backend sólo README | Localizar artefacto del equipo sin sobrescribirlo o formalizar baseline/migraciones en repo backend; comparar 6 entidades/documentación. No afirmar esquema físico ejecutable ya disponible | Leonidas + Andres, S1 |
| G-CAPACITY | Hasta semana 15,2 referentes FE / 1 BE y 9 funciones más regresión en S5 | Estimar horas y reservar corrección; preparar fixtures temprano y revisar carga semanal; escalamiento si no cabe, sin eliminar alcance ocultamente | Diego + Jim, semana 6 y cada sprint |

No se alteran nombres/asignaciones de paquetes UI en esta entrega. La corrección pendiente del paquete Leonidas/Fernando pertenece al cambio separado que el equipo hará; no basar asignación de código en ese nombre histórico.

## Registro de cierre (a completar con evidencia real)

| Gate | Decisión/evidencia versionada | Prueba | Fecha/semana | Validado por | Estado |
|---|---|---|---|---|---|
| Ninguno liberado por esta entrega | Elaborar documentación no cierra contratos | — | — | — | Pendiente |

Registrar cada cierre en una fila; no borrar la explicación original del riesgo. Pruebas con fixtures = prueba local, no aceptación del proveedor.

