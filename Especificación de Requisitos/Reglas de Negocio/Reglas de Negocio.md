**1. Propiedad de Entidades y Límites de Dominio (Ownership)**

- **RN-GEN-01.1 (Entidad Usuario):** El Canal Marketplace no almacena credenciales ni es dueño de la entidad _Usuario_; la creación de cuentas, inicio de sesión y gestión de tokens (JWT) es responsabilidad del Módulo de Seguridad y Usuarios.
- **RN-GEN-01.2 (Entidad Producto y Stock):** El Módulo de Productos y Ofertas es el único dueño de los datos del catálogo, precios, ofertas y niveles de inventario2more_horiz. El Marketplace actúa únicamente como canal de consulta.
- **RN-GEN-01.3 (Entidad Pedido):** La creación, gestión del ciclo de vida y estado final de las órdenes pertenece al Módulo de Ventas y Postventa2more_horiz. El Marketplace empaqueta y transmite la orden aprobada vía API.
- **RN-GEN-01.4 (Entidad Despacho):** La asignación de repartidores, seguimiento en ruta y registro de entrega es administrado por el Módulo de Despacho y Entrega a Domicilio.
- **RN-GEN-01.5 (Aislamiento de Persistencia y Comunicación por API):** Bajo ninguna circunstancia el backend del Marketplace accederá directamente a las bases de datos de otros módulos. Toda comunicación se realiza de forma asíncrona mediante APIs REST.

**2. Control e Integridad de Inventario y Promociones**

- **RN-GEN-02.1 (Validación de Stock Positivo):** Todo artículo o variante (talla/color) debe contar con un stock mayor a cero ($\text{Stock} > 0$) para permitir su adición al carrito o proceso de compra.
- **RN-GEN-02.2 (Revalidación Obligatoria Pre-Pago):** Inmediatamente antes de procesar la simulación de cobro en el Checkout, el backend reconfirmará la disponibilidad de inventario con el Módulo de Productos y Ofertas para evitar ventas de ítems agotados de último minuto.
- **RN-GEN-02.3 (Bloqueo por Agotamiento):** Si una variante o producto posee stock igual a cero, la interfaz mostrará la etiqueta "Agotado" e inhabilitará la opción de compra.
- **RN-GEN-02.4 (Validación de Cupones y Promociones):** Las ofertas, descuentos porcentuales y combos son calculados en tiempo real consultando al Módulo de Productos y Ofertas, quien determina su vigencia.
- **RN-GEN-02.5 (Disparo de Consumo de Stock):** Confirmada la creación del pedido en el Módulo de Ventas, se notificará vía API/evento al Módulo de Productos y Ofertas para ejecutar el descuento definitivo del inventario.

**3. Seguridad y Manejo de Datos Sensibles**

- **RN-GEN-03.1 (Protección de Datos Financieros):** No se almacenará ningún dato sensible de tarjetas de crédito o débito (número completo, fecha de vencimiento, CVV) en la base de datos local del Marketplace.
- **RN-GEN-03.2 (Seguridad en Recuperación de Accesos):** Las respuestas de la interfaz ante solicitudes de recuperación de clave serán neutras y no revelarán si un correo existe o no en el sistema.
- **RN-GEN-03.3 (Caducidad de Tokens):** Los enlaces/tokens de recuperación de clave cuentan con un tiempo límite de expiración.


