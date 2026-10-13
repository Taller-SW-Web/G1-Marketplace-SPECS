# S3 — Checkout y base asíncrona (semanas 12–13)

Versión 0.3.0 · Preparación obligatoria del Hito 5, sin afirmar contratos externos cerrados.

## Objetivo y alcance

Cerrar F-017–018 (cambiar/quitar ítem), F-022–027 (dirección, cotización, cupón, preparación simulada, pedido y confirmación), F-028/F-030 (historial y detalle) y F-033–034 (plantilla/confirmación asíncrona). Son doce funcionalidades; F-028/F-030 se adelantan porque F-032 depende de detalle de pedido y debe estar listo en H5. QA/contratos de Ventas y Despacho son parte del cierre. Los datos de dirección usan token del titular y no se copian a BD de Marketplace. La compra no termina en `PREPARED` ni `CREADO`: F-027 exige `PAGADO` verificado en Ventas.

## Secuencia por semana

- **Semana 12:** resolver I-02/I-06, contrato de importes/reserva/cupón y recuperación idempotente. Implementar carrito completo y dirección/resumen con errores. Preparar `CheckoutOperation`, worker/outbox y contrato de evento para F-034/F-035; elegir producto de API Management y broker/cola o mecanismo equivalente **entre servicios** con el módulo emisor.
- **Semana 13:** completar creación/confirmación de orden sin pago ficticio; probar doble clic, timeout, expiración, resultado incierto y reconciliación. Entregar historial/detalle autorizado F-028/F-030 como entrada real a F-032. Enviar confirmación por vía asíncrona aprobada, no desde el navegador. Instalar/configurar API Management en entorno autorizado y producir primeras trazas del intercambio asíncrono con productor/consumidor real. Preparar plan de carga, umbrales y dataset para la prueba formal de semana 14.

## Gate de salida

Flujo carrito→dirección→pedido/resultado demostrado con servicios reales; contrato de simulación de Ventas documentado; outbox/cola/evento identificable con reintento/deduplicación y consumidor. Si no hay evento externo aprobado, la funcionalidad que dependa de él continúa bloqueada; no llamar «entre microservicios» a una cola interna. [Gates](../DECISIONES-Y-BLOQUEOS.md) y [tablero](../seguimiento/README.md) conservan el estado real.

## Responsables propuestos y carga

Andres lleva F-017/F-018; Leonidas F-022–027; Fernando F-028/F-030/F-033/F-034. La [matriz](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md) fija revisores independientes y handoffs: Leonidas entrega estado de pedido autorizado a Fernando; Fernando no interpreta `CREADO` como `PAGADO`. Checkout y correo/evento dependen de contratos y entornos de Ventas, Productos, Despacho y proveedor de correo. Fernando tiene dos bloques relacionados; su capacidad y apoyos se confirman antes de aceptar S3.
