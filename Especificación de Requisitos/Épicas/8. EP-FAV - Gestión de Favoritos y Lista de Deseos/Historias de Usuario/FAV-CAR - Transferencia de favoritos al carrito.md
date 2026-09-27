- **Épica Relacionada:** `EP-FAV` - Gestión de Favoritos y Lista de Deseos
- **Prioridad:** Media
- **Puntos de Historia:** 5 pt
- **Responsable / Rol:** Integrante 2 - Leonidas (Arquitecto / Backend)
- **Precondiciones:**
    1. El cliente se encuentra autenticado con su sesión activa en el Marketplace.
    2. El cliente consulta un producto guardado en la vista "Mis Favoritos".
    3. La API del Módulo de Productos y el servicio de carrito están disponibles.

- **Descripción Ágil:** **Como** cliente registrado del Marketplace, **quiero** transferir un producto guardado en mis favoritos hacia el carrito de compras, **para** iniciar su proceso de compra.

- **Reglas de Negocio:**
    1. `WishlistItem` almacena el producto base. Antes de transferir al carrito, se valida la disponibilidad de stock en tiempo real con el Módulo de Productos.
    2. Para productos que requieren selección de variantes (talla o color), la acción redirige a la ficha técnica (P7) para completar la selección antes de añadir al carrito.
    3. Para productos simples sin variantes requeridas, se añade directamente a la bolsa de compras.
    4. El producto se elimina de la lista de favoritos únicamente tras una adición exitosa al carrito de compras.
    5. Si el producto se encuentra agotado, la adición se bloquea y el artículo permanece en la lista de favoritos.

- **Criterios de Aceptación (Sintaxis Gherkin):**

- **Escenario 1: Transferencia exitosa de producto simple con stock disponible**

```
Dado que un cliente autenticado consulta un producto simple sin variantes en favoritos con stock disponible,
Cuando presiona el botón "Mover al Carrito",
Entonces el sistema valida la existencia en el Módulo de Productos,
Y añade el artículo a la bolsa de compras y lo remueve de la lista de favoritos.
```

- **Escenario 2: Intento de transferencia de producto agotado**

```
Dado que un cliente consulta un producto en favoritos cuyo stock es igual a cero,
Cuando intenta presionar "Mover al Carrito",
Entonces el sistema notifica que el producto se encuentra agotado,
Y no lo añade al carrito de compras, manteniendo el producto en la lista de favoritos.
```

- **Escenario 3: Transferencia de producto que requiere selección de variantes**

```
Dado que un cliente consulta un producto con variantes de talla o color en favoritos,
Cuando presiona el botón "Mover al Carrito",
Entonces el sistema lo redirige a la ficha técnica (P7) para seleccionar las variantes deseadas,
Y mantiene el producto en la lista de favoritos hasta completar la adición al carrito.
```
