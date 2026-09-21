- **Épica Relacionada:** `EP-ITC` - Intención de Transacción y Carrito de Compras
- **Prioridad:** Alta
- **Puntos de Historia (Estimación):** 3 pts
- **Responsable / Rol:** Integrante 4 - Sebastián (Documentador / Intención de Compra)
- **Precondiciones:**
    1. El cliente interactúa con la interfaz del Marketplace desde cualquier vista pública o privada.

- **Descripción Ágil:** **Como** cliente del Marketplace, **quiero** visualizar el carrito flotante o la vista dedicada con los subtotales calculados en tiempo real, **para** conocer el monto acumulado de mi compra antes de iniciar el checkout.

- **Reglas de Negocio:**
    1. El cálculo de subtotales por producto y el total general acumulado deben actualizarse dinámicamente ante cualquier cambio en el carrito.
    2. La interfaz ofrecerá acceso rápido mediante un panel lateral/flotante o una vista dedicada del carrito.

- **Criterios de Aceptación (Sintaxis Gherkin):**

- **Escenario 1: Cálculo automático de subtotales y total en tiempo real**

```
Dado que un cliente tiene uno o más productos agregados en el carrito,
Cuando abre el panel del carrito flotante o la vista dedicada,
Entonces el sistema calcula y despliega el subtotal por cada ítem y el total general acumulado.
```

- **Escenario 2: Visualización de carrito vacío**

```
Dado que un cliente no ha agregado ningún producto al carrito,
Cuando abre el panel del carrito de compras,
Entonces el sistema despliega el mensaje "Tu carrito está vacío",
Y muestra un botón de acceso directo a la vitrina de productos.
```