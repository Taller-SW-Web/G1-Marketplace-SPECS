**1. Límites de Dominio y Propiedad de Entidades (Ownership)**

- **Entidad Usuario (Cliente/Vendedor):** El dueño legítimo de la entidad usuario es el **Módulo de Seguridad y Usuarios**. El Canal Marketplace no almacena credenciales ni contraseñas localmente; la autenticación y validación de usuarios se delega a este módulo mediante tokens (JWT).
- **Entidad Producto y Stock:** El dueño legítimo es el **Módulo de Productos y Ofertas**, incluyendo la propiedad del inventario. El Marketplace actúa como canal de consulta del catálogo, ofertas y revalidación de disponibilidad de stock.
- **Entidad Pedido:** El dueño legítimo de la entidad pedido es el **Módulo de Ventas y Postventa**. El Marketplace empaqueta y envía la orden aprobada tras el pago, y consume sus APIs como visor de lectura del historial de compras.
- **Entidad Despacho:** El dueño legítimo de la entidad despacho es el **Módulo de Despacho y Entrega a Domicilio**. El Marketplace consulta el estado actual del paquete para mostrar la barra de seguimiento.
- **Entidades Locales (Carrito Temporal y Favoritos):** La lista de favoritos y el estado temporal del carrito son gestionados de forma exclusiva por el **Canal Marketplace**10, utilizando su propia base de datos relacional local (MySQL o PostgreSQL).

---

**2. Matriz Cruzada de Integración entre Módulos**

Toda comunicación entre el Canal Marketplace y los demás módulos se realiza de forma asíncrona mediante **APIs**, respetando el principio de no realizar accesos directos a bases de datos entre módulos.

| Módulo Externo                     | Dirección de Integración                       | Propósito Funcional de la Integración                                                                                                          |
| ---------------------------------- | ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Módulo de Seguridad y Usuarios** | Marketplace $\rightarrow$ Seguridad y Usuarios | Envío de datos para el registro, inicio de sesión del cliente y procesamiento de solicitudes de recuperación de contraseña.                    |
| **Módulo de Productos y Ofertas**  | Marketplace $\rightarrow$ Productos y Ofertas  | Consulta del catálogo de productos, categorías, marcas, ficha técnica, ofertas y revalidación de disponibilidad de stock ($\text{Stock} > 0$). |
| **Módulo de Ventas y Postventa**   | Marketplace $\rightarrow$ Ventas y Postventa2  | Transmisión y registro del pedido empaquetado tras validar el pago en el Checkout, y consulta del historial de compras del cliente.            |
| **Módulo de Despacho y Entrega**   | Marketplace $\rightarrow$ Despacho y Entrega   | Consulta del estado del paquete y seguimiento del pedido en ruta para desplegar la barra de progreso al cliente.                               |