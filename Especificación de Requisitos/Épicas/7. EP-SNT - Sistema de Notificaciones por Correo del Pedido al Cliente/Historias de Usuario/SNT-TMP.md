- **Épica Relacionada:** `EP-SNT` - Sistema de Notificaciones por Correo del Pedido al Cliente
- **Prioridad:** Alta
- **Puntos de Historia (Estimación):** 3 pts
- **Responsable / Rol:** Integrante 7 - Saire (Notificaciones / QA)
- **Precondiciones:**
    1. Se dispone de la maquetación HTML responsiva y la identidad visual de la plataforma.

- **Descripción Ágil:** **Como** cliente del Marketplace, **quiero** recibir correos electrónicos maquetados con el resumen de mi pedido y sugerencias del catálogo, **para** disponer de un comprobante digital claro de mi compra y descubrir productos complementarios.

- **Reglas de Negocio:**
    1. Las plantillas de correo se maquetarán en HTML responsivo para garantizar su correcta visualización en dispositivos móviles y de escritorio.
    2. El correo de confirmación incluirá el detalle del pedido (código de orden, artículos, precios, dirección de envío) e incorporará un bloque con sugerencias de recomendación de productos del catálogo.

- **Criterios de Aceptación (Sintaxis Gherkin):**

- **Escenario 1: Generación exitosa de la plantilla de confirmación de pedido**

```
Dado que el sistema requiere notificar una compra confirmada,
Cuando se compila la plantilla HTML de confirmación,
Entonces el sistema renderiza el resumen detallado de la orden junto a los datos del cliente y la dirección de envío.
```

- **Escenario 2: Inclusión del catálogo de recomendaciones en la plantilla**

```
Dado que se renderiza el correo de confirmación de compra,
Cuando se construye la sección inferior del correo,
Entonces el sistema incorpora un bloque visual con recomendaciones de productos destacados del catálogo.
```