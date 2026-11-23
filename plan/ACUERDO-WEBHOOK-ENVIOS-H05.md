# Acuerdo H-05 · Webhook de envíos de Ventas

Acuerdo del 10/10 confirmado por G5 el 22/11/2026 para [BE #318](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/318). Fuentes: [api-ventas.md §1.10, revisión fijada](https://github.com/Taller-SW-Web/G5-Ventas-Postventas/blob/64608bb1ee89b29f0939660363ec5cbf87fbf239/specs/api/api-ventas.md) y comunicación «G5 → G1: webhook de envíos y cierre de la integración» (`G1-marketplace.md`). El contrato está acordado. Queda por verificar la entrega entre módulos.

## Envío de G5 a G1

Despacho comunica el cambio a Ventas. Ventas publica `pedidos.envio.estado_actualizado` para pedidos del canal MARKETPLACE, en orden de emisión. La ruta propuesta para Marketplace es `POST /api/v1/webhooks/ventas/envios` sobre HTTPS en Render. Se envía un evento por llamada, con `Content-Type: application/json` y la cabecera `X-Webhook-Token`. Configurar la credencial como variable protegida en el receptor y compartirla solo por el canal privado acordado.

| Campo | Formato H-05 |
|---|---|
| `eventId` | UUID único por evento. Se conserva en cada intento y es la clave de idempotencia. |
| `eventType` | Literal `ShipmentStatusUpdated`. |
| `version` | Literal `1.0.0`. |
| `timestamp` | Fecha y hora ISO 8601 con zona. |
| `emitter` | Literal `modulo-ventas`. |
| `data.orderId` | ID comercial de Ventas, `PED-AAAA-NNNNN`. |
| `data.publicStatus` | `DESPACHADO` al salir a reparto o reprogramar, `ENTREGADO` al completar la entrega. |
| `data.trackingNumber` | Identificador de despacho de G2, como cadena opaca. |
| `data.estimatedDeliveryDate` | Fecha `AAAA-MM-DD` o `null`. En reprogramación, `DESPACHADO` con una nueva fecha estimada. |

El evento excluye datos personales y dirección. Los estados comerciales como pagado y anulado se consultan en la API de pedidos de G5.

| Respuesta de Marketplace | Comportamiento de Ventas |
|---|---|
| `2xx`, incluido un `eventId` duplicado | Confirma la entrega. El receptor deduplica por ID antes de proyectar o generar un aviso. |
| `400`, `409` o `422` | Rechazo definitivo. |
| `5xx`, `401`, `403`, `404`, timeout o falta de conexión | Reintenta cada 5 s, hasta 10 intentos por evento. Conserva el `eventId` y espera antes de enviar los siguientes. |

Responder con rapidez, idealmente en menos de 10 segundos. Durante la prueba, devolver `2xx` a eventos válidos y autenticados aunque el pedido de prueba no exista en Marketplace. Registrar ese caso sin proyectar un estado ni crear un pedido.

## Prueba coordinada · lunes 23/11/2026

1. Fernando Saire termina y despliega el [receptor #319](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/319) con H-05. Marketplace configura el token en Render y confirma a Ventas por el canal privado que el receptor está listo. Ventas espera esa confirmación para activar el envío.
2. Ventas envía en orden **siete eventos reales de ejemplo** de pedidos de prueba con Despacho: despachados, entregados y una reprogramación. Son eventos del circuito G5/G2. Falta acreditar su recepción en G1.
3. Registrar hora, ruta, HTTP, ID de pedido de prueba, `eventId`, SHAs y entorno. Para [#320](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/320), coordinar un reenvío con el mismo ID y comprobar que la proyección no se duplica. Registrar reintento y fallo controlado si se acuerdan durante la prueba. Compartir solo el resumen sanitizado con Ventas.
4. Clasificar como **REAL** las entregas observadas entre despliegues. Las ejecuciones con simulador son **MOCK**. El acuerdo y los ejemplos disponibles no acreditan entrega en G1, cambios en el seguimiento ni envío de correo.

Pendientes al corte del 22/11: receptor desplegado, token configurado en Render y entregado por canal seguro, prueba del 23/11, evidencia de deduplicación y confirmación de Ventas.
