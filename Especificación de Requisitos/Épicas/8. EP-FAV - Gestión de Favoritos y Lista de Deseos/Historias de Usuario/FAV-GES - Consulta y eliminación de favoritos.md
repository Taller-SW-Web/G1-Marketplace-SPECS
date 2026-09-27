- **Épica Relacionada:** `EP-FAV` - Gestión de Favoritos y Lista de Deseos
- **Prioridad:** Media
- **Puntos de Historia:** 3 pt
- **Responsable / Rol:** Integrante 2 - Leonidas (Arquitecto / Backend)
- **Precondiciones:**
    1. El cliente se encuentra autenticado con su sesión activa en el Marketplace.
    2. La base de datos local para gestión de favoritos se encuentra operativa.

- **Descripción Ágil:** **Como** cliente registrado del Marketplace, **quiero** consultar y eliminar productos de mi lista de deseos, **para** mantener organizados mis artículos de interés.

- **Reglas de Negocio:**
    1. La lista de favoritos desplegada corresponde exclusivamente al cliente autenticado.
    2. Eliminar un favorito remueve la asociación en la base de datos local sin afectar el catálogo de productos.

- **Criterios de Aceptación (Sintaxis Gherkin):**

- **Escenario 1: Consulta de la lista de favoritos**

```
Dado que un cliente autenticado tiene productos guardados en su lista de deseos,
Cuando ingresa a la sección "Mis Favoritos",
Entonces el sistema muestra la grilla de productos asociados a su ID de cliente.
```

- **Escenario 2: Eliminación de un producto de favoritos**

```
Dado que un cliente visualiza su lista de favoritos,
Cuando selecciona "Quitar de Favoritos" en un producto,
Entonces el sistema elimina el registro en la base de datos local,
Y actualiza la vista removiendo el producto de la lista en tiempo real.
```
