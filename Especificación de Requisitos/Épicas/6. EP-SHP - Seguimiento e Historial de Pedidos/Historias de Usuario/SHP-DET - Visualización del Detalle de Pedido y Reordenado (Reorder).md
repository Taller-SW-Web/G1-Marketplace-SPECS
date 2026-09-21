- **Épica Relacionada:** `EP-SHP` - Seguimiento e Historial de Pedidos
- **Prioridad:** Alta
- **Puntos de Historia (Estimación):** 3 pts
- **Responsable / Rol:** Integrante 6 - Diego (JP / QA / Seguimiento e Historial)
- **Precondiciones:**
    1. El cliente se encuentra en el panel "Mis Pedidos" y selecciona una orden específica.

- **Descripción Ágil:** **Como** cliente del Marketplace, **quiero** seleccionar un pedido de mi historial para ver su desglose completo y la opción de volver a comprarlo, **para** revisar el detalle de la transacción o agregar rápidamente los mismos productos a mi carrito activo.

- **Reglas de Negocio:**
    1. Presenta la ficha detallada con los productos (imágenes, nombres, variantes), precios unitarios, desglose de cobro y dirección de despacho.
    2. La opción "Volver a Comprar" revalida la disponibilidad de stock con la API de Productos y Ofertas antes de cargar los ítems en el carrito de compras.

- **Criterios de Aceptación (Sintaxis Gherkin):**

- **Escenario 1: Despliegue completo del detalle del pedido**

```
Dado que un cliente selecciona un pedido específico de su historial,
Cuando la vista carga el detalle provisto por el Módulo de Ventas y Postventa,
Entonces el sistema muestra la lista de artículos comprados con sus imágenes, el resumen de precios y la dirección de despacho asignada.
```

- **Escenario 2: Reordenar productos de una compra pasada (Reorder)**

```
Dado que un cliente consulta el detalle de un pedido registrado anteriormente,
Cuando presiona el botón "Volver a Comprar",
Entonces el sistema revalida la disponibilidad de stock con la API del Módulo de Productos y Ofertas,
Y añade los artículos con stock disponible al carrito de compras activo.
```