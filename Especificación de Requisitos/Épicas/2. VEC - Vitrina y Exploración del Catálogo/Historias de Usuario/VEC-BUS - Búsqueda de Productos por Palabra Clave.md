- **Épica Relacionada:** `EP-VEC` - Vitrina y Exploración del Catálogo
- **Prioridad:** Alta
- **Puntos de Historia (Estimación):** 3 pts
- **Responsable / Rol:** Integrante 2 - Leo (Vitrina y Exploración / Arquitecto de Aplicación)
- **Precondiciones:**
    1. El cliente se encuentra en la vista principal o cabecera del Marketplace.
    2. La API del Módulo de Productos y Ofertas se encuentra disponible o simulada (_mock_).

- **Descripción Ágil:** **Como** visitante o cliente del Marketplace, **quiero** ingresar un término o palabra clave en la barra de búsqueda, **para** localizar rápidamente artículos deportivos específicos dentro del catálogo.

- **Reglas de Negocio:**
    1. La búsqueda contempla coincidencias parciales o totales sobre nombres, categorías o descripciones registradas en la entidad producto.
    2. Los términos ingresados con menos de 2 caracteres no detonarán consultas automáticas para optimizar el rendimiento.

- **Criterios de Aceptación (Sintaxis Gherkin):**

- **Escenario 1: Búsqueda exitosa con coincidencias encontradas**

```
Dado que un cliente se encuentra en la barra de búsqueda del Marketplace,
Y escribe un término válido con al menos 2 caracteres,
Cuando ejecuta la búsqueda de productos,
Entonces el sistema consulta el catálogo y despliega la lista de artículos coincidentes,
Y muestra la cantidad total de resultados encontrados.
```

- **Escenario 2: Búsqueda sin productos coincidentes**

```
Dado que un cliente ingresa un término de búsqueda en el sistema,
Y el término no coincide con ningún producto del catálogo activo,
Cuando ejecuta la búsqueda,
Entonces la plataforma despliega una vista con el mensaje de "No se encontraron productos",
Y sugiere al usuario verificar la ortografía o intentar con otra palabra clave.
```

- **Escenario 3: Intento de búsqueda con longitud insuficiente**

```
Dado que un cliente se encuentra en la barra de búsqueda,
Y escribe un solo carácter en el campo de texto,
Cuando intenta ejecutar la consulta,
Entonces el sistema no procesa la solicitud,
Y resalta una indicación visual solicitando ingresar al menos 2 caracteres.
```