- **Épica Relacionada:** `EP-DDP` - Detalle y Disponibilidad de Producto
- **Prioridad:** Alta
- **Puntos de Historia (Estimación):** 3 pts
- **Responsable / Rol:** Integrante 3 - Jim (Product Owner)
- **Precondiciones:**
    1. El cliente se encuentra en la vista de detalle con una variante o producto seleccionado.

- **Descripción Ágil:** **Como** cliente del Marketplace, **quiero** consultar la disponibilidad de stock en tiempo real, **para** asegurarme de que el artículo está disponible antes de proceder con la compra.

- **Reglas de Negocio:**
    1. La verificación de disponibilidad se realiza mediante peticiones asíncronas al Módulo de Productos y Ofertas para asegurar que el stock sea estrictamente mayor a cero.
    2. Si el producto o la variante seleccionada no cuenta con inventario (stock = 0), la opción de compra debe quedar inhabilitada.

- **Criterios de Aceptación (Sintaxis Gherkin):**

- **Escenario 1: Producto con stock disponible**

```
Dado que un cliente selecciona un producto o variante que cuenta con inventario positivo,
Cuando la vista consulta la disponibilidad con la API de productos,
Entonces el sistema muestra el indicador de "Stock Disponible",
Y mantiene habilitado el botón para agregar al carrito.
```

- **Escenario 2: Producto sin stock disponible (Agotado)**

```
Dado que un cliente selecciona un producto o variante cuyo stock es cero en el inventario,
Cuando la vista valida la disponibilidad con la API,
Entonces el sistema despliega la etiqueta de "Agotado",
Y deshabilita la opción de agregar al carrito impidiendo la transacción.
```