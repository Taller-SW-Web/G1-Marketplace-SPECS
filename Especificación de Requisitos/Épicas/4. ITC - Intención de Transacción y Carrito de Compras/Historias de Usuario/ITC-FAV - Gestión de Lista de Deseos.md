- **Épica Relacionada:** `EP-ITC` - Intención de Transacción y Carrito de Compras
- **Prioridad:** Media
- **Puntos de Historia (Estimación):** 3 pts
- **Responsable / Rol:** Integrante 4 - Sebastián (Documentador / Intención de Compra)
- **Precondiciones:**
    1. El cliente se encuentra autenticado con su sesión activa en el Marketplace.
    2. La base de datos local del Marketplace para gestión de favoritos está operativa.

- **Descripción Ágil:** **Como** cliente registrado del Marketplace, **quiero** guardar y gestionar mis productos favoritos en una lista de deseos y transferirlos al carrito, **para** consultar o comprar posteriormente los artículos que me interesan.

- **Reglas de Negocio:**
    1. Las listas de favoritos se almacenan de forma persistente en la base de datos local del Marketplace asociadas de forma exclusiva al ID del cliente.
    2. Al transferir un producto desde la lista de favoritos al carrito de compras, el sistema debe validar la disponibilidad de stock en tiempo real con la API de productos.

- **Criterios de Aceptación (Sintaxis Gherkin):**

- **Escenario 1: Agregar un producto a la lista de favoritos**

```
Dado que un cliente autenticado visualiza un producto en el catálogo o ficha técnica,
Cuando presiona el botón "Agregar a Favoritos",
Entonces el sistema registra el producto en la base de datos local asociado al ID del cliente,
Y marca el ícono visualmente para indicar que forma parte de sus favoritos.
```

- **Escenario 2: Consulta y eliminación desde la vista de favoritos**

```
Dado que un cliente autenticado ingresa a la sección "Mis Favoritos",
Cuando visualiza su lista de productos guardados y selecciona "Quitar de Favoritos" en un ítem,
Entonces el sistema elimina el registro de la base de datos local,
Y actualiza la vista removiendo el producto de la lista.
```

- **Escenario 3: Transferir un producto desde favoritos hacia el carrito de compras**

```
Dado que un cliente autenticado revisa su lista de favoritos,
Cuando presiona el botón "Mover al Carrito" en un ítem guardado,
Entonces el sistema verifica la disponibilidad de stock con la API de productos,
Y añade el artículo al carrito de compras manteniendo el ítem en favoritos o removiéndolo según la preferencia del usuario.
```

- **Escenario 4: Intento de agregar a favoritos sin sesión activa**

```
Dado que un visitante no autenticado intenta presionar el botón de "Agregar a Favoritos",
Cuando el sistema detecta la ausencia de sesión activa,
Entonces despliega el modal o vista de inicio de sesión,
Y requiere autenticar la cuenta para guardar el ítem en su lista.
```