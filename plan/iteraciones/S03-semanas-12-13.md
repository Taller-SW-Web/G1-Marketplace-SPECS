# S3 — Checkout y base asíncrona (semanas 12–13)

Versión 0.7.0 · Disponibilidad sin restricción horaria, revisión 19/10/2026 · Preparación obligatoria del Hito 5, sin afirmar contratos externos cerrados.

## Objetivo y alcance

Cerrar F-022–027 (dirección, cotización, cupón, preparación simulada, pedido y confirmación), F-028/F-030 (historial y detalle) y F-033–034 (plantilla/confirmación asíncrona). Son diez funcionalidades; F-028/F-030 se adelantan porque F-032 depende de detalle de pedido y debe estar listo en H5. QA/contratos de Ventas y Despacho son parte del cierre. Los datos de dirección usan token del titular y no se copian a BD de Marketplace. La compra no termina en `PREPARED` ni `CREADO`: F-027 exige `PAGADO` verificado en Ventas.

## Secuencia por semana

- **Semana 12:** resolver I-02/I-06, contrato de importes/reserva/cupón y recuperación idempotente. Ejecutar regresión del carrito completo con objetivo H4 y completar integración dirección/resumen con errores desde el código probado en H4. Conectar y completar `CheckoutOperation` y worker/outbox preparados en H4 en su parte definida, y acordar la frontera del evento F-034/F-035; elegir producto de API Management y broker/cola o mecanismo equivalente **entre servicios** con el módulo emisor.
- **Semana 13:** completar creación/confirmación de orden sin pago ficticio; probar doble clic, timeout, expiración, resultado incierto y reconciliación. Entregar historial/detalle autorizado F-028/F-030 como entrada real a F-032. Enviar confirmación por vía asíncrona aprobada, no desde el navegador. Instalar/configurar API Management en entorno autorizado y producir primeras trazas del intercambio asíncrono con productor/consumidor real. Preparar plan de carga, umbrales y dataset para la prueba formal de semana 14.

## Gate de salida

Flujo carrito→dirección→pedido/resultado demostrado con servicios reales; contrato de simulación de Ventas documentado; outbox/cola/evento identificable con reintento/deduplicación y consumidor. Si no hay evento externo aprobado, la funcionalidad que dependa de él continúa bloqueada; no llamar «entre microservicios» a una cola interna. [Gates](../DECISIONES-Y-BLOQUEOS.md) y [tablero](../seguimiento/README.md) conservan el estado real.

## Responsables asignados y coordinación

Andres mantiene y prueba la regresión de F-016–F-021 y apoya operación; Leonidas F-022–027; Fernando F-028/F-030/F-033/F-034. La [matriz](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md) fija revisores independientes y handoffs: Leonidas entrega estado de pedido autorizado a Fernando; Fernando no interpreta `CREADO` como `PAGADO`. Checkout y correo/evento dependen de contratos y entornos de Ventas, Productos, Despacho y proveedor de correo. Fernando tiene dos bloques relacionados por decisión del PO; Diego sigue evidencia y gates por operación; Jim coordina desbloqueos y revisión.

## Implementación recibida de H4 y tratamiento de bloqueos

H4 tiene 25 objetivos de cierre F-001–F-021/F-036–F-039. F-017/F-018 ya no son cierres nuevos S03. Leonidas entrega código/pruebas propias F-022–F-027; Fernando F-028/F-030/F-033/F-034, con adaptadores, plantillas y worker donde el contrato esté definido. S03 completa conexión autoritativa G5/G2/G6/correo y evidencia desplegada, sin rehacer como diseño inicial lo que puede implementarse H4.

Los bloqueos externos H4 que persistan se registran por F, causa, owner y prueba que falta; conservan su ID y no se duplican en el conteo. No hay restricción de horas del equipo ni promociones por tiempo. Mantener I-02/I-03/I-06/G-MONEY/G-COUPON-RELEASE/G-MAIL y PAGADO verificado; un fixture no los libera. [S02](S02-semanas-09-11.md) define las cuatro etapas de evidencia.

Extensión H4 por contratos: F-023/F-024/F-025/F-026 pueden aceptarse antes si pasan todos los gates G5/G2/G6/G7 y la prueba desplegada. Sólo entonces se descuentan de los diez cierres base S03 (hasta seis restantes) y conservan regresión; no se retienen por una cuota temporal.
