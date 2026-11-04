# Borradores de comentarios para issues — Fernando Saire — F-028 a F-035

Documento local de apoyo. **No se publicaron comentarios ni se modificó GitHub.** Las ramas de Backend y Frontend todavía contienen cambios locales sin commit/push; por eso estos textos no citan SHA ni PR. Antes de publicar, añadir los enlaces reales después de compartir las ramas o abrir PRs y ajustar lo que cambie tras la revisión.

Estos comentarios informan avance y evidencia MOCK/LOCAL. No piden cerrar issues que conservan dependencias reales. Evitar copiar el mismo bloque indiscriminadamente a todas las issues subordinadas: usarlo en el issue de implementación correspondiente y enlazar INT/QA/DOC cuando el tablero lo requiera.

## F-028 — Historial de pedidos

**Issues relacionadas:** Backend [#141](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/141)–[#144](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/144); Frontend [#71](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/71)–[#72](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/72).

> Avance local H4 en las ramas `feat/f028-f035-fernando-backend` y `feat/f028-f035-fernando-frontend`: `OrdersHistoryContainer`/`OrderList` presentan `/mis-pedidos`, paginación/estados; el enlace de cuenta aparece sólo con sesión habilitada; la fuente G5 sigue desactivada (`ORDERS_SOURCE=unconfigured`), aunque las rutas BFF están implementadas. Timeouts separados para G5 (150 s default) y BFF (185 s default); auth G7 conserva límite corto. Backend: typecheck y suite unitaria 33/307; Frontend: build/typecheck, componentes 37/294, servidor 9/94 y E2E principal 30/1 omitida (31 total). `tests/orders.e2e.spec.ts` recorre historial/filtros/detalle/seguimiento, 401 y respuesta neutral de pedido no disponible con fixtures, 3/3. Falta verificar límites del hosting, revisión independiente y prueba autorizada contra G5 con sesión G7; esto no equivale a integración ni despliegue y la issue conserva sus gates.

## F-029 — Filtros de historial

**Issues relacionadas:** Backend [#145](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/145)–[#148](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/148); Frontend [#73](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/73)–[#74](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/74).

> Avance local H4: se implementaron filtros de estado/fechas, validación de rango antes de llamar al proveedor, reinicio de paginación y adaptación al contrato G5 (`YYYY-MM-DD`, días inclusivos en `America/Lima`). Por el cold start G5 reportado se separó su timeout (150 s default) del límite de auth G7; el BFF tiene 185 s default y configuración acotada. Las pruebas locales Backend de environment/provider pasaron 29/29; Frontend server 9/94, typecheck y build aprobados. El flujo de navegador de pedidos cubrió filtros con fixtures; la fuente G5 sigue desactivada (`ORDERS_SOURCE=unconfigured`). La respuesta REAL de G5 y los casos con JWT autorizado requieren prueba coordinada; fixtures no acreditan integración.

## F-030 — Detalle de pedido

**Issues relacionadas:** Backend [#149](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/149)–[#152](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/152); Frontend [#75](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/75)–[#76](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/76).

> Avance local H4: se añadió detalle `/mis-pedidos/{orderId}`, consulta BFF y autorización de titularidad en Backend; los datos se proyectan al contrato G1 y el caso ajeno usa respuesta neutral. FE separa `HistoricalOrderLines`, `OrderDeliverySummary` (ubicación general y contacto enmascarado) y `OrderStateTimeline`. G5 entrega total y snapshots por línea, no desglose autoritativo de subtotal/descuentos/envío; no se inventa ni deriva dicho desglose y V-016 queda pendiente de confirmación. La prueba de presentación pasó 4/4 y E2E dirigida de pedidos 3/3 después de reconstruir `.next`. No se ha confirmado si el JWT de prueba sigue vigente: falta sesión autorizada para probar autorización A/B contra G5 REAL. Sin flujo desplegado; mantener pendientes las revisiones e integración definidas por la issue.

## F-031 — Reordenar compra

**Issues relacionadas:** Backend [#153](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/153)–[#156](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/156); Frontend [#77](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/77)–[#78](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/78).

> Avance local H4: `POST /api/v1/orders/{orderId}/reorder` consulta el pedido propio, revalida SKU/cantidad con provider de prueba y usa precio comercial actual. Cada acción requiere `Idempotency-Key` UUID v4: dos llamadas concurrentes con la misma clave produjeron una sola suma; una segunda clave intencional permitió otra recompra en PostgreSQL 16 temporal. El backend y la restricción de DB rechazan otras versiones. Suite Backend de integración: 5 suites/41 pruebas; unitarias 33 suites/307; typecheck y `prisma validate` aprobados. Frontend probó 3/3 casos del componente (incluye retry conservando clave y nueva acción con UUID distinto) y BFF 4/4; typecheck aprobado. DB temporal eliminada. La UI y provider mock permanecen apagados por defecto; no hay integración REAL G6.

## F-032 — Seguimiento de despacho

**Issues relacionadas:** Backend [#157](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/157)–[#160](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/160); Frontend [#79](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/79)–[#80](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/80).

> Avance local con fixtures: la consulta distingue disponible/sin seguimiento/no preparado y evita exponer PII/coordenadas; Frontend presenta estado, fecha estimada e hitos mediante `ShipmentTimeline` detrás del BFF. La prueba de presentación está incluida en las suites locales dirigidas (23/23). G2/Despacho no tiene contrato, sandbox ni acceso de prueba autorizado; provider runtime apagado. No registrar integración ni cierre INT.

## F-033 — Plantilla de correo

**Issues relacionadas:** Backend [#161](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/161)–[#164](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/164); Frontend [#81](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/81)–[#82](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/82).

> Avance local: componentes React server-only `TransactionalEmailTemplate`, `EmailOrderSummary` y `ShipmentEmailTemplate`, render HTML/texto C-001/C-002 escapado y CTA validado. C-001 exige estado `PAGADO`; C-002 usa datos públicos de despacho y no afirma envío. Prueba dirigida de templates 4/4; suite Frontend componentes 37/294, servidor 9/94, build/typecheck aprobados; Backend mantiene renderers propios probados. El frame de Figma que dice “Creado” discrepa con regla funcional `PAGADO`; envío y aprobación visual pendientes.

## F-034 — Confirmación asíncrona

**Issues relacionadas:** Backend [#165](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/165)–[#169](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/169); Frontend [#83](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/83)–[#84](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/84).

> Avance local: destinatario cifrado, outbox/worker con idempotencia, leases, reintentos acotados y reconciliación ante respuesta incierta. La persistencia se probó sólo sobre PostgreSQL 16 temporal; la confirmación Frontend aclara que el correo no fue enviado. Flags de outbox y worker apagados por defecto; no hay proveedor/scheduler ni envío G-MAIL. Faltan sandbox/credenciales y contrato autorizados, revisión y prueba REAL; no cerrar INT ni afirmar entrega de correo.

## F-035 — Aviso de despacho

**Issues relacionadas:** Backend [#170](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/170)–[#174](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/174); Frontend [#85](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/85)–[#86](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/86).

> Avance local: parser para fixtures H-05 v1.0.0 y consumidor interno que valida el pedido G1 pagado, persiste `NotificationDelivery` de forma idempotente y permite renderizar C-002. La suite Backend pasó (33 suites/307 pruebas); no se creó endpoint público y no se consumió evento en runtime. Faltan URL/auth de receptor, prueba conjunta I-05 y correo real. Además, el contrato dice que se notifica una reprogramación pero no determina si el `publicStatus` permanece `DESPACHADO`; confirmar ese valor con G5 antes de ampliar el enum o declarar homologación. Mantener abiertas las issues de integración/seguridad/documentación que dependan de ese gate.

## Transversales #98 Frontend y #215 Backend

> Corte local con fixtures 04/11: Frontend build/typecheck aprobados; E2E principal 30 aprobadas/1 omitida de 31 (incluye pedidos F-028–F-032 3/3), Favoritos MOCK HTTP 4/4 y UI 9/9, autenticación UI 10/10, componentes 37/294 y servidor 9/94. Backend auth API 18/18 con PostgreSQL temporal corresponde al corte previo, junto con suite unitaria revalidada 33/307 y typecheck; no se contactó G7. Todo usa fixtures/mock; no es G7 REAL ni E2E desplegado. Para #215 hay checklist local, pero no se verificaron runtime cloud, variables, SHA desplegado, smoke ni rollback. Falta revisión independiente y E2E desplegado de #98; ambos issues siguen en progreso.

## Antes de publicar

1. Revisar el diff y solicitar revisión independiente.
2. Commitear/publicar las ramas autorizadas y sustituir el nombre de rama por enlaces a commits/PRs reales.
3. Actualizar comandos o cifras si una repetición de pruebas produce otro resultado.
4. No incluir tokens, cookies, correos, PII ni respuestas sin sanitizar.
5. Publicar comentarios sólo en las issues apropiadas; no marcar cierre por evidencia local cuando falta el gate REAL o cloud.
