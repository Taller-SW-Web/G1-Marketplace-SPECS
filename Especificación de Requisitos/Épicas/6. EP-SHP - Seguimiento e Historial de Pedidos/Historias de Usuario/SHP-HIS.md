- **Épica Relacionada:** `EP-SHP` - Seguimiento e Historial de Pedidos
- **Prioridad:** Alta
- **Puntos de Historia (Estimación):** 3 pts
- **Responsable / Rol:** Integrante 6 - Diego (JP / QA / Seguimiento e Historial)
- **Precondiciones:**
    1. El cliente se encuentra autenticado con su sesión activa en la plataforma.
    2. La API del Módulo de Ventas y Postventa se encuentra disponible para consultar los pedidos registrados.

- **Descripción Ágil:** **Como** cliente registrado del Marketplace, **quiero** acceder al panel "Mis Pedidos" y filtrar mi historial por estado, **para** consultar mis compras pasadas y ubicar rápidamente órdenes específicas.

- **Reglas de Negocio:**
    1. Funciona como un visor de lectura que consulta las órdenes vinculadas al ID del cliente desde el Módulo de Ventas y Postventa, dueño legítimo de la entidad _Pedido_.
    2. Los pedidos se ordenan cronológicamente (más recientes primero) desplegando fecha, código de orden, cantidad de artículos, estado actual y monto total.
    3. Se permite el filtrado dinámico por estado del pedido ("En proceso", "Entregado" o "Cancelado").

- **Criterios de Aceptación (Sintaxis Gherkin):**

- **Escenario 1: Carga exitosa del historial de compras**

```
Dado que un cliente autenticado ingresa al panel "Mis Pedidos",
Cuando el sistema consulta la API del Módulo de Ventas y Postventa,
Entonces se despliega la lista cronológica de sus pedidos registrados,
Y muestra el resumen básico de cada orden (código, fecha, cantidad de productos, estado y total).
```

- **Escenario 2: Filtrado de historial por estado de pedido**

```
Dado que un cliente autenticado se encuentra en la vista "Mis Pedidos",
Cuando aplica un filtro por el estado "En proceso",
Entonces el sistema actualiza el listado desplegando únicamente las órdenes que se encuentran pendientes de entrega.
```

- **Escenario 3: Cliente sin compras registradas**

```
Dado que un cliente recién registrado o sin historial accede al panel "Mis Pedidos",
Cuando el sistema consulta sus órdenes en la API de Ventas,
Entonces la interfaz muestra el mensaje "Aún no has realizado ninguna compra",
Y ofrece un botón directo para explorar el catálogo de productos.
```