- **Épica Relacionada:** `EP-VEC` - Vitrina y Exploración del Catálogo
- **Prioridad:** Alta
- **Puntos de Historia (Estimación):** 5 pts
- **Responsable / Rol:** Integrante 2 - Leo (Vitrina y Exploración / Arquitecto de Aplicación)
- **Precondiciones:**
    1. El catálogo de productos se despliega en la interfaz del Marketplace.
    2. Las categorías y marcas activas son provistas por la API de Productos y Ofertas.

- **Descripción Ágil:** **Como** cliente del Marketplace, **quiero** seleccionar filtros dinámicos por categorías y marcas en el panel lateral, **para** acotar la vitrina comercial únicamente a los artículos que cumplen mis criterios.

- **Reglas de Negocio:**
    1. Se permite la selección múltiple e inclusiva de filtros dentro de los paneles laterales.
    2. Para mantener una alta usabilidad y rendimiento, los listados extensos se presentarán en bloques dosificados de productos.
    3. Debe existir la opción de restablecer todos los filtros aplicados en un solo clic.

- **Criterios de Aceptación (Sintaxis Gherkin):**

- **Escenario 1: Aplicación exitosa de filtros laterales**

```
Dado que un cliente visualiza el catálogo de productos en la página principal,
Y selecciona una o más categorías/marcas específicas en el panel lateral,
Cuando el sistema procesa la selección,
Entonces actualiza dinámicamente la lista de productos mostrados,
Y despliega únicamente los artículos que cumplen con los criterios seleccionados.
```

- **Escenario 2: Combinación de filtros sin resultados**

```
Dado que un cliente aplica una combinación restrictiva de categorías y marcas,
Y no existen artículos que coincidan simultáneamente con todos los filtros,
Cuando se actualiza la vista del catálogo,
Entonces el sistema despliega un mensaje notificando la ausencia de coincidencias,
Y habilita un botón directo para limpiar los filtros aplicados.
```

- **Escenario 3: Limpieza y restablecimiento de filtros**

```
Dado que un cliente tiene uno o más filtros activos en el panel lateral,
Cuando selecciona la opción "Limpiar Filtros",
Entonces el sistema desmarca todas las opciones seleccionadas,
Y vuelve a desplegar el catálogo general de productos en su estado inicial.
```