- **Épica Relacionada:** `EP-FAV` - Gestión de Favoritos y Lista de Deseos
- **Prioridad:** Media
- **Puntos de Historia:** 3 pt
- **Responsable / Rol:** Integrante 8 - Alonso (Backend)
- **Precondiciones:**
    1. El usuario visualiza un producto en el catálogo o en su ficha técnica.
    2. La base de datos local del Marketplace para gestión de favoritos está operativa.

- **Descripción Ágil:** **Como** cliente registrado del Marketplace, **quiero** guardar productos desde el catálogo o la ficha de producto, **para** conservar los artículos que me interesan.

- **Reglas de Negocio:**
    1. Guardar favoritos requiere una sesión autenticada en la plataforma.
    2. Si el usuario no está autenticado, se solicita inicio de sesión; tras autenticarse con éxito, el sistema retorna a la pantalla de origen y completa el guardado.
    3. Cada favorito se asocia exclusivamente al ID del cliente.
    4. La combinación cliente y producto es única dentro de la entidad `WishlistItem`.

- **Criterios de Aceptación (Sintaxis Gherkin):**

- **Escenario 1: Guardado de un producto en favoritos**

```
Dado que un cliente autenticado visualiza un producto en el catálogo o ficha técnica,
Cuando presiona el botón "Agregar a Favoritos",
Entonces el sistema registra el producto en la base de datos local asociado a su ID de cliente,
Y marca el ícono visualmente para indicar que forma parte de sus favoritos.
```

- **Escenario 2: Intento de guardado sin sesión activa**

```
Dado que un visitante no autenticado intenta presionar el botón de "Agregar a Favoritos",
Cuando el sistema detecta la ausencia de sesión activa,
Entonces redirige a la vista o modal de inicio de sesión,
Y tras una autenticación exitosa, retorna a la pantalla de origen guardando automáticamente el producto en sus favoritos.
```

- **Escenario 3: Producto ya guardado previamente**

```
Dado que un cliente ya tiene un producto en su lista de favoritos,
Cuando intenta guardar nuevamente el mismo producto,
Entonces el sistema mantiene la asociación única entre el cliente y el producto sin duplicar registros.
```
