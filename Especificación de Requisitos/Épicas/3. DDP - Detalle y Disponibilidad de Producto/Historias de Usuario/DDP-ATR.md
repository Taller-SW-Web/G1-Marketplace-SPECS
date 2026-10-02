- **Épica Relacionada:** `EP-DDP` - Detalle y Disponibilidad de Producto
- **Prioridad:** Alta
- **Puntos de Historia (Estimación):** 3 pts
- **Responsable / Rol:** Integrante 3 - Jim (Product Owner)
- **Precondiciones:**
    1. El producto seleccionado cuenta con atributos configurables (ej. talla, color).

- **Descripción Ágil:** **Como** cliente del Marketplace, **quiero** seleccionar los atributos específicos del producto (como talla y color), **para** personalizar el artículo deportivo según mis preferencias antes de añadirlo al carrito.

- **Reglas de Negocio:**
    1. Se debe exigir la selección de todos los atributos obligatorios antes de habilitar la opción de agregar al carrito.
    2. La selección de una variante debe actualizar dinámicamente la galería visual y el precio asociado a dicha combinación.

- **Criterios de Aceptación (Sintaxis Gherkin):**

- **Escenario 1: Selección exitosa de variantes de producto**

```
Dado que un cliente se encuentra en la vista de detalle de un producto con atributos configurables,
Y selecciona una combinación válida de talla y color,
Cuando confirma la selección de la variante,
Entonces el sistema actualiza la galería de imágenes y el precio correspondiente a la combinación elegida.
```

- **Escenario 2: Intento de agregar al carrito sin seleccionar atributos obligatorios**

```
Dado que un cliente visualiza un producto que requiere selección de talla o color,
Y no ha seleccionado alguno de los atributos obligatorios,
Cuando intenta presionar el botón de agregar al carrito,
Entonces el sistema bloquea la acción,
Y resalta visualmente los atributos pendientes de selección.
```