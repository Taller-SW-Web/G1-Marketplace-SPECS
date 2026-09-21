- **Épica Relacionada:** `EP-SNT` - Sistema de Notificaciones por Correo del Pedido al Cliente
- **Prioridad:** Alta
- **Puntos de Historia (Estimación):** 5 pts
- **Responsable / Rol:** Integrante 7 - Saire (Notificaciones / QA)
- **Precondiciones:**
    1. El flujo de Checkout (`EP-TRX`) procesa exitosamente la simulación de pago y emite el evento de creación de orden.

- **Descripción Ágil:** **Como** cliente del Marketplace, **quiero** recibir un correo de confirmación inmediatamente después de realizar mi compra, **para** asegurar que mi pedido fue registrado correctamente por la plataforma.

- **Reglas de Negocio:**
    1. El backend de notificaciones "escuchará" de forma asíncrona los eventos de creación de pedido generados por el Integrante 5 para disparar los correos.
    2. El procesamiento de notificaciones debe ser totalmente asíncrono para no demorar la respuesta de la interfaz del cliente al finalizar su pago.

- **Criterios de Aceptación (Sintaxis Gherkin):**

- **Escenario 1: Disparo automático de notificación tras confirmación de compra**

```
Dado que un cliente completa exitosamente su proceso de compra en el Checkout,
Cuando el microservicio de notificaciones detecta el evento de orden creada,
Entonces dispara asíncronamente el correo electrónico de confirmación al buzón del cliente.
```

- **Escenario 2: Manejo de reintentos ante falla del servidor de correo**

```
Dado que se genera un evento de pedido exitoso pero el servicio de correo presenta una indisponibilidad temporal,
Cuando el microservicio intenta realizar el despacho del mensaje,
Entonces encola la solicitud y reintenta el envío automáticamente sin duplicar correos ni afectar la sesión del cliente.
```