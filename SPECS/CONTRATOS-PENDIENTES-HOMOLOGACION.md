# Paquete de homologación de integraciones — Marketplace

Este documento convierte las brechas `I-01` a `I-06` en solicitudes verificables para los módulos dueños. Es una **propuesta de Marketplace**, no una declaración de que los otros equipos ya aprobaron o implementaron estos contratos.

## Regla de aprobación

Cada acuerdo se considera homologado únicamente cuando el módulo dueño publica o actualiza su contrato versionado, Marketplace valida el mapeo contra su contrato BFF y ambos equipos registran la aceptación. Hasta entonces las specs pueden guiar diseño y mocks, pero no autorizan integración real.

## H-01 — Catálogo, pricing, promociones e inventario (`I-01`)

**Dueño que debe responder:** Productos y Ofertas.  
**Consumidor:** adaptador backend de Marketplace.  
**Afecta:** `F-006`–`F-016`, `F-024`, `F-031` y `F-039`.

Marketplace solicita un OpenAPI versionado que defina: rutas definitivas; autenticación entre servicios; audiencia o scopes; límites; `X-Request-Id`; errores; y paginación. El contrato debe cubrir estas operaciones semánticas, aunque la ruta final quede a decisión del módulo dueño:

| Operación requerida | Entrada mínima | Salida mínima requerida |
| --- | --- | --- |
| Explorar y buscar catálogo | canal, consulta, categoría, filtros, orden, cursor/página | productos activos, slug, imagen de tarjeta, atributos de filtro, SKU resoluble cuando aplique y paginación |
| Ficha descriptiva | slug, canal | producto activo, marca, descripción, atributos técnicos y medios ordenados con texto alternativo |
| Variantes | producto o slug, canal | combinaciones permitidas, `variantId`, `sku` y atributos seleccionables |
| Precio vigente | `sku`, canal, instante | precio regular, oferta opcional, moneda, vigencia y versión |
| Disponibilidad informativa | `sku`, canal | estado de disponibilidad; nunca un saldo interno obligatorio |
| Beneficios/cupón | líneas por SKU, cupón, canal | elegibilidad, descuentos aplicables, mensajes seguros y versión de evaluación |
| Recomendaciones | producto o SKU, canal, límite | candidatos ordenados y razón pública opcional |

**Decisiones ya cerradas por Marketplace:** su frontend nunca consume directamente este contrato externo; el BFF conserva sus contratos `F-006`–`F-016` y adapta el proveedor. La unidad comprable que cruza inventario, cotización y ventas es `sku`; `variantId` no la sustituye.

**Aceptación:** una prueba de contrato demuestra producto activo/no elegible, página vacía, precio con y sin oferta, SKU inválido/no disponible y cupón inválido, sin exponer información administrativa.

## H-02 — Creación idempotente de pedido (`I-02`)

**Dueño que debe responder:** Ventas y Postventas.  
**Afecta:** `F-025`–`F-027`.

Marketplace propone que `POST /api/v1/pedidos` acepte el header obligatorio `Idempotency-Key` (UUID o valor opaco de hasta 128 caracteres) y la identidad autenticada. Para la misma identidad y clave:

- igual payload: Ventas devuelve la representación previamente creada, sin crear otro pedido;
- payload distinto: responde `409 IDEMPOTENCY_KEY_REUSED`;
- petición concurrente: no produce más de una orden;
- error de validación previo a crear la orden no reserva una orden ficticia.

Marketplace conservará `CheckoutOperation` sólo como trazabilidad técnica del intento y reutilizará la clave durante sus reintentos; Ventas continúa siendo dueño de la orden, pago simulado y estado comercial.

**Aceptación:** dos solicitudes iguales, incluso concurrentes, devuelven el mismo `orderId`; una con la misma clave y distinto cuerpo devuelve `409`.

## H-03 — Historial asociado al titular (`I-03`)

**Dueño que debe responder:** Ventas y Postventas.  
**Afecta:** `F-028` y `F-029`.

Marketplace propone normalizar la consulta de historial como `GET /api/v1/pedidos/me`, donde Ventas deriva el cliente desde la credencial verificable del titular. Si Ventas mantiene `GET /api/v1/pedidos?clienteId=...`, debe ignorar o rechazar un `clienteId` distinto al titular y documentar el mecanismo de propagación de identidad desde Marketplace.

**Decisión Marketplace:** el navegador no envía ni confía en un `customerId` elegido por el usuario para consultar pedidos. La respuesta debe definir filtros permitidos, paginación, estados públicos y errores de autorización.

**Aceptación:** un cliente no puede consultar pedidos de otro alterando parámetros; el historial vacío es `200` con lista vacía, no `404`.

## H-04 — Evaluación postentrega (`I-04`)

**Dueño que debe responder:** Ventas y Postventas.  
**Afecta:** `F-040`.

La decisión UX de Marketplace queda fijada: **Bien → 5**, **Regular → 3**, **Mal → 1**. Los motivos condicionales se envían como datos estructurados si Ventas amplía el contrato; mientras tanto Marketplace los serializa de forma legible en el comentario con prefijo `Motivos:` sin almacenar una tabla local de CSAT.

Ventas debe verificar que el pedido pertenece al titular y que está en estado entregado antes de aceptar `POST /api/v2/csat`. Se solicita añadir opcionalmente `sentiment` (`POSITIVE`, `NEUTRAL`, `NEGATIVE`) y `reasons[]` con códigos publicados; el puntaje 1–5 y `comment` siguen siendo compatibles.

**Aceptación:** el mismo pedido no puede evaluarse por otro cliente ni antes de entregarse; la escala, motivos inválidos y una segunda respuesta se comportan según contrato publicado.

## H-05 — Estado de despacho para notificaciones (`I-05`)

**Dueños que deben responder:** Despacho y Entrega a Domicilio, y Ventas y Postventas.  
**Afecta:** `F-034` y `F-035`.

Marketplace propone que Ventas reexponga un evento versionado `ShipmentStatusUpdated` que ya recibe de Despacho, o publique un webhook equivalente para el servicio de notificaciones de Marketplace. Debe contener como mínimo `eventId`, versión, fecha UTC, `orderId`, estado público de envío, fecha estimada opcional y emisor. Se requieren reintentos, deduplicación por `eventId` y autenticación de emisor.

**Decisión Marketplace:** hasta homologar este evento, `F-035` no presume que puede consumir los eventos internos de Despacho ni enviará correos basados en estados no confirmados.

**Aceptación:** un mismo evento entregado dos veces no genera dos correos y un evento de orden ajena no puede revelar datos personales.

## H-06 — Cliente técnico para Despacho (`I-06`)

**Dueños que deben responder:** Seguridad y Despacho y Entrega a Domicilio.  
**Afecta:** `F-023` y `F-032`.

Registrar el cliente técnico `modulo-marketplace` con mínimo privilegio y sólo los scopes publicados por Despacho: `cotizaciones:calcular` y `seguimientos:leer`. El contrato debe indicar emisor de token, audiencia, expiración, rotación de secreto/certificado y respuestas `401`/`403`.

**Aceptación:** con cada scope se permite únicamente su operación; sin scope o con audiencia incorrecta se rechaza sin revelar información de envío.

## Registro de seguimiento

| ID | Estado actual | Próximo entregable verificable |
| --- | --- | --- |
| H-01 | Pendiente de respuesta externa | OpenAPI de Productos y Ofertas y prueba de mapeo del adaptador. |
| H-02 | Pendiente de respuesta externa | Contrato de Ventas con idempotencia y prueba concurrente. |
| H-03 | Pendiente de respuesta externa | Ruta/semántica de historial autenticado publicada por Ventas. |
| H-04 | Decisión UX interna cerrada; contrato externo pendiente | CSAT con validación de entrega y catálogo de motivos. |
| H-05 | Propuesta de arquitectura pendiente | Evento o webhook versionado y prueba de deduplicación. |
| H-06 | Solicitud de configuración pendiente | Cliente registrado y prueba de scopes. |
