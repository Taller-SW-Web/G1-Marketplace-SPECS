- **Épica Relacionada:** `EP-SHP` - Seguimiento e Historial de Pedidos
- **Prioridad:** Alta
- **Puntos de Historia (Estimación):** 5 pts
- **Responsable / Rol:** Integrante 6 - Diego (JP / QA / Seguimiento e Historial)
- **Precondiciones:**
    1. El pedido seleccionado cuenta con una orden de entrega generada en el Módulo de Despacho y Entrega a Domicilio.

- **Descripción Ágil:** **Como** cliente del Marketplace, **quiero** visualizar la barra de progreso y el estado actual de despacho de mi pedido, **para** conocer en tiempo real la trayectoria y fecha estimada de entrega de mi paquete.

- **Reglas de Negocio:**
    1. La interfaz consulta asíncronamente la API del Módulo de Despacho y Entrega a Domicilio, dueño legítimo de la entidad _Despacho_.
    2. La barra de progreso refleja las etapas del envío: "Pedido Registrado" ➔ "En Preparación" ➔ "En Ruta" ➔ "Entregado".

- **Criterios de Aceptación (Sintaxis Gherkin):**

- **Escenario 1: Visualización de la barra de progreso en tiempo real**

```
Dado que un cliente consulta el seguimiento de un pedido en proceso de despacho,
Cuando el backend obtiene el estado actual desde la API del Módulo de Despacho y Entrega,
Entonces el sistema ilumina la etapa correspondiente en la barra de progreso visual,
Y muestra la ventana estimada de entrega al cliente.
```

- **Escenario 2: Notificación de evento o reprogramación de entrega**

```
Dado que el estado enviado por el Módulo de Despacho indica una incidencia o reprogramación de la entrega,
Cuando el cliente consulta el panel de seguimiento,
Entonces la interfaz muestra una etiqueta de alerta explicativa,
Y ofrece la información actualizada del estado del paquete.
```