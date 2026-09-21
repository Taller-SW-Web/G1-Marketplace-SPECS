**1. Seguridad (RNF-SEC)**

- **RNF-SEC-01 (Autenticación Delegada):** El manejo y validación de usuarios no almacenará credenciales ni contraseñas localmente; se delegará la autenticación al Módulo de Seguridad y Usuarios gestionando la sesión mediante tokens (JWT).
- **RNF-SEC-02 (Protección de Datos Financieros):** En la simulación de pago del Checkout (`EP-TRX`), no se guardarán datos sensibles de tarjetas de crédito/débito (número completo, CVV) en la base de datos local del Marketplace bajo ninguna circunstancia.
- **RNF-SEC-03 (Comunicación Cifrada):** Todo intercambio de información entre la interfaz en React, el backend del Marketplace y las APIs de microservicios externos debe realizarse bajo el protocolo seguro HTTPS/TLS.

**2. Rendimiento y Performance (RNF-PER)**

- **RNF-PER-01 (Eficiencia en la Consulta de Catálogo):** La exploración de la vitrina (`EP-VEC`) y la ficha técnica (`EP-DDP`) ejecutarán consultas asíncronas optimizadas hacia el Módulo de Productos y Ofertas.
- **RNF-PER-02 (Optimización de Búsquedas):** La barra de búsqueda por palabras clave restringirá el envío de peticiones automáticas para entradas menores a 2 caracteres, evitando la saturación innecesaria de solicitudes al servidor.
- **RNF-PER-03 (Procesamiento Asíncrono de Notificaciones):** El microservicio de notificaciones (`EP-SNT`) despachará los correos transaccionales en segundo plano mediante eventos, evitando ralentizar o bloquear la confirmación de la compra en la interfaz.

**3. Usabilidad y Experiencia de Usuario - UX/UI (RNF-USA)**

- **RNF-USA-01 (Diseño Responsivo):** La interfaz web desarrollada en React debe garantizar una navegación intuitiva y adaptable para pantallas de escritorio, tablets y dispositivos móviles.
- **RNF-USA-02 (Actualización Dinámica de Estado):** Las acciones dentro del carrito de compras (`EP-ITC`) —modificación de cantidades, eliminación y cálculo de subtotales— se actualizarán de inmediato en la vista sin requerir la recarga completa de la página (`page reload`).
- **RNF-USA-03 (Estándar de Prototipado):** La maquetación del diseño debe ser fiel a los esquemas y wireframes construidos en Figma.

**4. Disponibilidad, Arquitectura e Infraestructura (RNF-DIS)**

- **RNF-DIS-01 (Aislamiento de Persistencia):** El Canal Marketplace dispondrá únicamente de una base de datos relacional local (MySQL o PostgreSQL) para almacenar el carrito temporal y las listas de favoritos, respetando el principio de no acceder directamente a las bases de datos de otros módulos.
- **RNF-DIS-02 (Integración mediante APIs Desacopladas):** La comunicación con los microservicios externos (Productos, Ventas, Despacho y Seguridad) se realizará estrictamente mediante APIs de forma asíncrona.
- **RNF-DIS-03 (Despliegue Cloud):** El sistema estará alojado y operativo en una infraestructura de servidor en la Nube.