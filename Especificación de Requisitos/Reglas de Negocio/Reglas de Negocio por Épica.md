**1. Épica: EP-GAC - Gestión de Accesos del Cliente**

- **HU-GAC-REG: Registro de Cliente**
    1. El correo electrónico proporcionado debe ser único dentro de la plataforma.
    2. Todos los campos obligatorios del formulario deben completarse adecuadamente.
- **HU-GAC-SES: Inicio y Cierre de Sesión del Cliente**
    1. El inicio de sesión correcto habilita las funciones personalizadas del cliente (favoritos, historial de compras, checkout).
    2. El cierre de sesión invalida e inhabilita inmediatamente la sesión activa en el navegador.
- **HU-GAC-REC: Recuperación de Contraseña**
    1. Por motivos de seguridad, la respuesta de la interfaz ante solicitudes de recuperación no revelará explícitamente si un correo existe o no en el sistema.
    2. El enlace o token de recuperación debe contar con un tiempo de caducidad definido antes de ser utilizado.

---

**2. Épica: EP-VEC - Vitrina y Exploración del Catálogo**

- **HU-VEC-BUS: Búsqueda de Productos por Palabra Clave**
    1. La búsqueda contempla coincidencias parciales o totales sobre nombres, categorías o descripciones registradas en la entidad producto.
    2. Los términos ingresados con menos de 2 caracteres no detonarán consultas automáticas para optimizar el rendimiento.
- **HU-VEC-FIL: Navegación y Filtrado Dinámico por Categorías y Marcas**
    1. Se permite la selección múltiple e inclusiva de filtros dentro de los paneles laterales.
    2. Para mantener una alta usabilidad y rendimiento, los listados extensos se presentarán en bloques dosificados de productos.
    3. Debe existir la opción de restablecer todos los filtros aplicados en un solo clic.
- **HU-VEC-HOM: Visualización de la Página Principal y Secciones Destacadas**
    1. La página principal exhibirá accesos directos a las categorías superiores y un carrusel o grilla con artículos destacados.
- **HU-VEC-ORD: Ordenamiento del Catálogo de Productos**
    1. Las opciones de ordenamiento estándar soportadas serán: "Precio: Menor a Mayor", "Precio: Mayor a Menor" y "Más Recientes".

---

**3. Épica: EP-DDP - Detalle y Disponibilidad de Producto**

- **HU-DDP-FIC: Visualización de la Ficha Técnica, Galería y Ofertas del Producto**
    1. La información mostrada debe ser la versión oficial provista por el Módulo de Productos y Ofertas, dueño legítimo de la entidad producto.
    2. Si el producto cuenta con una promoción o descuento vigente, se debe exhibir el precio original tachado junto al precio final en oferta y el porcentaje de descuento.
- **HU-DDP-ATR: Selección de Atributos y Variantes de Producto**
    1. Se debe exigir la selección de todos los atributos obligatorios antes de habilitar la opción de agregar al carrito.
    2. La selección de una variante debe actualizar dinámicamente la galería visual y el precio asociado a dicha combinación.
- **HU-DDP-STK: Consulta y Validación de Disponibilidad de Inventario**
    1. La verificación de disponibilidad se realiza mediante peticiones asíncronas al Módulo de Productos y Ofertas para asegurar que el stock sea estrictamente mayor a cero.
    2. Si el producto o la variante seleccionada no cuenta con inventario (stock = 0), la opción de compra debe quedar inhabilitada.
- **HU-DDP-REL: Visualización de Productos Relacionados y Sugeridos**
    1. Las recomendaciones se obtienen dinámicamente según la categoría o marca del producto principal en consulta.

---

**4. Épica: EP-ITC - Intención de Transacción y Carrito de Compras**

- **HU-ITC-CAR: Gestión de Productos en el Carrito de Compras**
    1. Si un producto ya existe en el carrito y se vuelve a agregar, el sistema incrementará la cantidad seleccionada en lugar de duplicar la línea.
    2. La cantidad solicitada de un producto no podrá superar el límite de stock disponible devuelto por la API de productos.
    3. Al iniciar sesión, los productos acumulados en el carrito anónimo temporal se unificarán automáticamente con la sesión del cliente.
    4. Se permite mover ítems directamente a la lista de favoritos si el cliente se encuentra autenticado.
- **HU-ITC-RES: Visualización del Carrito Flotante y Cálculo de Subtotales en Tiempo Real**
    1. El cálculo de subtotales por producto y el total general acumulado deben actualizarse dinámicamente ante cualquier cambio en el carrito.
    2. La interfaz ofrecerá acceso rápido mediante un panel lateral/flotante o una vista dedicada del carrito.
- **HU-ITC-FAV: Gestión de Lista de Deseos / Favoritos**
    1. Las listas de favoritos se almacenan de forma persistente en la base de datos local del Marketplace asociadas de forma exclusiva al ID del cliente.
    2. Al transferir un producto desde la lista de favoritos al carrito de compras, el sistema debe validar la disponibilidad de stock en tiempo real con la API de productos.

---

**5. Épica: EP-TRX - Transacción y Realización de Checkout**

- **HU-TRX-DIR: Captura de Datos de Envío y Dirección de Entrega**
    1. Todos los campos de dirección (calle/avenida, departamento, provincia, distrito y teléfono de contacto) son obligatorios.
    2. La interfaz permite seleccionar direcciones previamente guardadas o ingresar una nueva dirección de envío.
- **HU-TRX-PAG: Simulación de Pago con Tarjeta y Revalidación de Inventario**
    1. La interfaz exhibirá el desglose transparente del monto final (Subtotal + Costo de envío = Total a pagar).
    2. Antes de procesar el pago, el backend verificará asíncronamente con el Módulo de Productos y Ofertas que el stock siga disponible.
    3. No se almacenarán datos sensibles de tarjetas de crédito en bases de datos locales por motivos de seguridad.
- **HU-TRX-ORD: Generación del Pedido y Envío al Módulo de Ventas**
    1. Al aprobarse el pago, el backend empaquetará la orden (cliente, ítems, precios, dirección de entrega) y la enviará vía API al Módulo de Ventas y Postventa, dueño legítimo de la entidad _Pedido_.
    2. Confirmada la creación de la orden, el sistema vaciará el carrito de compras activo del cliente.

---

**6. Épica: EP-SHP - Seguimiento e Historial de Pedidos**

- **HU-SHP-HIS: Consulta y Filtrado del Historial de Pedidos**
    1. Funciona como un visor de lectura que consulta las órdenes vinculadas al ID del cliente desde el Módulo de Ventas y Postventa, dueño legítimo de la entidad _Pedido_.
    2. Los pedidos se ordenan cronológicamente (más recientes primero) desplegando fecha, código de orden, cantidad de artículos, estado actual y monto total.
    3. Se permite el filtrado dinámico por estado del pedido ("En proceso", "Entregado" o "Cancelado").
- **HU-SHP-DET: Visualización del Detalle de Pedido y Reordenado (Reorder)**
    1. Presenta la ficha detallada con los productos (imágenes, nombres, variantes), precios unitarios, desglose de cobro y dirección de despacho.
    2. La opción "Volver a Comprar" revalida la disponibilidad de stock con la API de Productos y Ofertas antes de cargar los ítems en el carrito de compras.
- **HU-SHP-TRK: Seguimiento del Estado del Envío y Progreso en Ruta**
    1. La interfaz consulta asíncronamente la API del Módulo de Despacho y Entrega a Domicilio, dueño legítimo de la entidad _Despacho_.
    2. La barra de progreso refleja las etapas del envío: "Pedido Registrado" ➔ "En Preparación" ➔ "En Ruta" ➔ "Entregado".

---

**7. Épica: EP-SNT - Sistema de Notificaciones por Correo del Pedido al Cliente**

- **HU-SNT-TMP: Diseño de Plantillas de Correo Transaccionales y Recomendaciones de Productos**
    1. Las plantillas de correo se maquetarán en HTML responsivo para garantizar su correcta visualización en dispositivos móviles y de escritorio.
    2. El correo de confirmación incluirá el detalle del pedido (código de orden, artículos, precios, dirección de envío) e incorporará un bloque con sugerencias de recomendación de productos del catálogo.
- **HU-SNT-EML: Envío Automático y Asíncrono de Confirmación de Pedido**
    1. El backend de notificaciones "escuchará" de forma asíncrona los eventos de creación de pedido generados por el Integrante 5 para disparar los correos.
    2. El procesamiento de notificaciones debe ser totalmente asíncrono para no demorar la respuesta de la interfaz del cliente al finalizar su pago.
- **HU-SNT-DES: Notificación por Correo de Actualización del Estado de Despacho**
    1. Se notificará al cliente vía correo electrónico ante hitos clave del envío ("En Ruta" o "Entregado") consumiendo los eventos del Módulo de Despacho.