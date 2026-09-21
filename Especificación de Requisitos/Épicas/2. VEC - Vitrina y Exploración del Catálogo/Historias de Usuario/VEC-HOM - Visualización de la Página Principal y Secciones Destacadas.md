- **Épica Relacionada:** `EP-VEC` - Vitrina y Exploración del Catálogo
- **Prioridad:** Alta
- **Puntos de Historia (Estimación):** 3 pts
- **Responsable / Rol:** Integrante 2 - Leo (Vitrina y Exploración / Arquitecto de Aplicación)
- **Precondiciones:**
    1. El cliente ingresa a la URL principal del Marketplace.
    2. La API de Productos y Ofertas está disponible para entregar las categorías e ítems destacados.

- **Descripción Ágil:** **Como** visitante o cliente del Marketplace, **quiero** acceder a la página principal con accesos a categorías y productos destacados, **para** orientar mi navegación e iniciar la exploración del catálogo.

- **Reglas de Negocio:**
    1. La página principal exhibirá accesos directos a las categorías superiores y un carrusel o grilla con artículos destacados.

- **Criterios de Aceptación (Sintaxis Gherkin):**

- **Escenario 1: Carga exitosa de la página principal**

```
Dado que un visitante ingresa a la plataforma del Marketplace,
Cuando se renderiza la página principal,
Entonces el sistema despliega el menú con las categorías de productos deportivas,
Y presenta la grilla de productos destacados obtenidos del catálogo activo.
```