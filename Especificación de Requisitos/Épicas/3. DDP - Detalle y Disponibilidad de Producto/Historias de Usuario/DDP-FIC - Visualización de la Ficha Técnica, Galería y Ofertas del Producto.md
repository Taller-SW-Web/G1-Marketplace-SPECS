- **Épica Relacionada:** `EP-DDP` - Detalle y Disponibilidad de Producto
- **Prioridad:** Alta
- **Puntos de Historia (Estimación):** 3 pts
- **Responsable / Rol:** Integrante 3 - Jim (Product Owner)
- **Precondiciones:**
    1. El cliente selecciona un producto desde la vitrina comercial o mediante enlace directo.
    2. La API del Módulo de Productos y Ofertas está disponible para proveer la información detallada.

- **Descripción Ágil:** **Como** cliente del Marketplace, **quiero** visualizar la ficha técnica con imágenes, descripción, marca, precio regular y ofertas vigentes del producto, **para** evaluar sus características y tomar una decisión de compra informada.

- **Reglas de Negocio:**
    1. La información mostrada debe ser la versión oficial provista por el Módulo de Productos y Ofertas, dueño legítimo de la entidad producto.
    2. Si el producto cuenta con una promoción o descuento vigente, se debe exhibir el precio original tachado junto al precio final en oferta y el porcentaje de descuento.

- **Criterios de Aceptación (Sintaxis Gherkin):**

- **Escenario 1: Carga exitosa de la ficha técnica del producto**

```
Dado que un cliente selecciona un producto del catálogo,
Cuando la interfaz carga la vista de detalle,
Entonces el sistema despliega la galería de imágenes, el nombre, la marca, la descripción técnica y el precio de venta actualizado.
```

- **Escenario 2: Visualización de producto con promoción o descuento activo**

```
Dado que un cliente ingresa a la ficha de un producto que posee un descuento vigente,
Cuando la vista renderiza la información comercial recibida de la API,
Entonces el sistema despliega el precio original tachado, el precio final promocional y la etiqueta con el porcentaje de descuento.
```

- **Escenario 3: Intento de acceso a un producto no disponible o inexistente**

```
Dado que un cliente intenta acceder a la ficha de un producto descontinuado o inexistente,
Cuando el sistema consulta el catálogo,
Entonces despliega una vista de alerta indicando que el producto no se encuentra disponible,
Y ofrece un botón directo para retornar a la vitrina principal.
```