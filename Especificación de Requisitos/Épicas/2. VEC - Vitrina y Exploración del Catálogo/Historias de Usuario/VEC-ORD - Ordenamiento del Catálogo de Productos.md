- **Épica Relacionada:** `EP-VEC` - Vitrina y Exploración del Catálogo
- **Prioridad:** Media
- **Puntos de Historia (Estimación):** 2 pts
- **Responsable / Rol:** Integrante 2 - Leo (Vitrina y Exploración / Arquitecto de Aplicación)
- **Precondiciones:**
    1. El cliente se encuentra visualizando un listado de productos en la vitrina del Marketplace.

- **Descripción Ágil:** **Como** cliente del Marketplace, **quiero** ordenar el listado de productos por precio y novedad, **para** priorizar la visualización según mis necesidades de presupuesto o interés comercial.

- **Reglas de Negocio:**
    1. Las opciones de ordenamiento estándar soportadas serán: "Precio: Menor a Mayor", "Precio: Mayor a Menor" y "Más Recientes".

- **Criterios de Aceptación (Sintaxis Gherkin):**

- **Escenario 1: Ordenamiento por precio de menor a mayor**

```
Dado que un cliente está visualizando un listado de productos en el catálogo,
Cuando selecciona el criterio de ordenamiento "Precio: Menor a Mayor",
Entonces la interfaz reorganiza de forma inmediata los artículos exhibidos,
Y presenta los productos con el precio de venta más bajo en las primeras posiciones.
```

- **Escenario 2: Ordenamiento por precio de mayor a menor**

```
Dado que un cliente está visualizando un listado de productos en el catálogo,
Cuando selecciona el criterio de ordenamiento "Precio: Mayor a Menor",
Entonces la interfaz reorganiza los artículos exhibidos,
Y presenta los productos con el precio de venta más alto en las primeras posiciones.
```

- **Escenario 3: Ordenamiento por novedad (más recientes)**

```
Dado que un cliente está visualizando un listado de productos en el catálogo,
Cuando selecciona el criterio de ordenamiento "Más Recientes",
Entonces la interfaz reorganiza los artículos exhibidos,
Y presenta los productos registrados o ingresados más recientemente en las primeras posiciones.
```