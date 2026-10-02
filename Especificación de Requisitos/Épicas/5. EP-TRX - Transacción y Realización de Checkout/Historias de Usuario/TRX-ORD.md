- **Épica Relacionada:** `EP-TRX` - Transacción y Realización de Checkout
- **Prioridad:** Alta
- **Puntos de Historia (Estimación):** 5 pts
- **Responsable / Rol:** Integrante 5 - Giuliano (UX/UI / Transacción y Checkout)
- **Precondiciones:**
    1. La simulación del pago con tarjeta ha sido aprobada satisfactoriamente.

- **Descripción Ágil:** **Como** cliente del Marketplace, **quiero** recibir el resumen de confirmación con el código único de mi pedido, **para** verificar que mi orden se ha registrado correctamente y disponer de un comprobante de compra.

- **Reglas de Negocio:**
    1. Al aprobarse el pago, el backend empaquetará la orden (cliente, ítems, precios, dirección de entrega) y la enviará vía API al Módulo de Ventas y Postventa, dueño legítimo de la entidad _Pedido_.
    2. Confirmada la creación de la orden, el sistema vaciará el carrito de compras activo del cliente.

- **Criterios de Aceptación (Sintaxis Gherkin):**

- **Escenario 1: Empaquetado y registro exitoso del pedido**

```
Dado que la simulación de pago del cliente ha sido aprobada,
Cuando el backend empaqueta la orden y la transmite vía API al Módulo de Ventas y Postventa,
Entonces el sistema confirma la creación del pedido,
Y despliega la pantalla de éxito mostrando el número de orden asignado y vaciando el carrito de compras.
```

- **Escenario 2: Falla de comunicación con el servicio de ventas al registrar la orden**

```
Dado que la simulación de pago fue aprobada pero ocurre una interrupción en la API hacia el Módulo de Ventas,
Cuando el sistema intenta registrar el pedido,
Entonces despliega una alerta al cliente indicando que la orden está en proceso de verificación,
Y conserva el registro temporal para reintentar la transmisión sin duplicar el cobro.
```