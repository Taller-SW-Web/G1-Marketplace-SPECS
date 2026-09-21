- **Épica Relacionada:** `EP-ITC` - Intención de Transacción y Carrito de Compras
- **Prioridad:** Alta
- **Puntos de Historia (Estimación):** 5 pts
- **Responsable / Rol:** Integrante 4 - Sebastián (Documentador / Intención de Compra)
- **Precondiciones:**
    1. El cliente se encuentra explorando la vitrina comercial, el detalle de un producto o su carrito actual.
    2. La disponibilidad de stock es provista por la API del Módulo de Productos y Ofertas.

- **Descripción Ágil:** **Como** cliente o visitante del Marketplace, **quiero** agregar, modificar cantidades, eliminar y trasladar productos en el carrito de compras, **para** controlar los artículos que pretendo adquirir antes de pasar al pago.

- **Reglas de Negocio:**
    1. Si un producto ya existe en el carrito y se vuelve a agregar, el sistema incrementará la cantidad seleccionada en lugar de duplicar la línea.
    2. La cantidad solicitada de un producto no podrá superar el límite de stock disponible devuelto por la API de productos.
    3. Al iniciar sesión, los productos acumulados en el carrito anónimo temporal se unificarán automáticamente con la sesión del cliente.
    4. Se permite mover ítems directamente a la lista de favoritos si el cliente se encuentra autenticado.

- **Criterios de Aceptación (Sintaxis Gherkin):**

- **Escenario 1: Agregar un producto al carrito de compras**

```
Dado que un cliente selecciona un producto con talla/color y stock disponible,
Cuando presiona el botón "Agregar al Carrito",
Entonces el sistema añade el artículo al estado temporal del carrito,
Y muestra una confirmación visual incrementando el contador de artículos.
```

- **Escenario 2: Modificación de cantidad de un producto en el carrito**

```
Dado que un cliente tiene un producto en su carrito de compras,
Cuando incrementa o disminuye el contador de unidades de dicho producto,
Entonces el sistema actualiza la cantidad seleccionada,
Y recalcula de inmediato los valores sin recargar la página.
```

- **Escenario 3: Eliminación de un producto del carrito**

```
Dado que un cliente revisa la lista de productos en su carrito,
Cuando selecciona la opción "Eliminar" en un artículo específico,
Entonces el sistema remueve el ítem del carrito de compras,
Y actualiza la vista del listado y los totales.
```

- **Escenario 4: Trasladar un producto del carrito a la lista de favoritos**

```
Dado que un cliente autenticado tiene un producto en su carrito de compras,
Cuando selecciona la opción "Guardar para después" o "Mover a Favoritos",
Entonces el sistema remueve el artículo del carrito temporal,
Y lo registra en la base de datos local dentro de su lista de favoritos.
```

- **Escenario 5: Sincronización de carrito anónimo al iniciar sesión**

```
Dado que un visitante no autenticado ha agregado productos a su carrito temporal,
Cuando completa exitosamente el inicio de sesión en la plataforma,
Entonces el sistema conserva los productos previamente agregados,
Y asocia el estado del carrito activo a la sesión del cliente autenticado.
```