- **Épica Relacionada:** `EP-SNT` - Sistema de Notificaciones por Correo del Pedido al Cliente
- **Prioridad:** Media
- **Puntos de Historia (Estimación):** 5 pts
- **Responsable / Rol:** Integrante 7 - Saire (Notificaciones / QA)
- **Precondiciones:**
    1. El Módulo de Despacho y Entrega actualiza el estado de seguimiento de un paquete en ruta.

- **Descripción Ágil:** **Como** cliente del Marketplace, **quiero** recibir notificaciones por correo cuando cambie el estado de entrega de mi paquete, **para** estar informado del avance del despacho y la recepción de mis productos.

- **Reglas de Negocio:**
    1. Se notificará al cliente vía correo electrónico ante hitos clave del envío ("En Ruta" o "Entregado") consumiendo los eventos del Módulo de Despacho.

- **Criterios de Aceptación (Sintaxis Gherkin):**

- **Escenario 1: Notificación automática por cambio de estado a "En Ruta"**

```
Dado que el Módulo de Despacho actualiza el estado de la entrega a "En Ruta",
Cuando el servicio de notificaciones detecta el evento de actualización,
Entonces genera y envía un correo electrónico notificando al cliente que su paquete está en camino.
```

- **Escenario 2: Notificación automática por confirmación de entrega**

```
Dado que el repartidor registra la recepción del pedido como "Entregado",
Cuando se procesa el evento en la plataforma,
Entonces el sistema envía el correo de confirmación de entrega solicitando opcionalmente la valoración del servicio.
```