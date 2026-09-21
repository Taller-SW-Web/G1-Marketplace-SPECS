### **1. Épica `EP-GAC` — Gestión de Accesos del Cliente**

#### **Pantalla 1: Modal / Vista de Inicio de Sesión (Login)**

- **Historias de Usuario que cumple:** `HU-GAC-SES` (Inicio y Cierre de Sesión del Cliente).
- **Componentes Visuales:** Cuadro de diálogo o tarjeta de acceso, campos de texto para correo electrónico y contraseña (con botón de visibilidad de clave), botón principal ("Iniciar Sesión") y enlace de recuperación ("¿Olvidaste tu contraseña?").
- **Disposición de Componentes:** Estructura vertical centrada con el logotipo e ícono de seguridad en la cabecera, campos de entrada con etiquetas superiores en el cuerpo y botones/enlaces de acción en el pie.
- **Flujos de Usabilidad (Alto Nivel):**
    1. El usuario ingresa sus credenciales de acceso.
    2. Al presionar "Iniciar Sesión", el sistema valida la información.
    3. Si los datos son correctos, se concede el acceso, se activan las funciones personalizadas de la cuenta (favoritos, historial, checkout) y se despliega una confirmación visual en pantalla.
    4. Si existe una bolsa de compras anónima activa en el navegador, el sistema unifica automáticamente los productos con la cuenta del usuario.
    5. En caso de credenciales erróneas, el sistema muestra un mensaje de error genérico en pantalla sin indicar cuál campo fue el incorrecto, protegiendo la cuenta.

#### **Pantalla 2: Vista / Modal de Registro de Cliente**

- **Historias de Usuario que cumple:** `HU-GAC-REG` (Registro de Cliente).
- **Componentes Visuales:** Formulario con campos para Nombre, Apellidos, Correo Electrónico, Teléfono de Contacto y Contraseña, casilla de aceptación de términos y botón de confirmación ("Crear Cuenta").
- **Disposición de Componentes:** Organización en cuadrícula a dos columnas en pantallas anchas y una columna en dispositivos móviles, finalizando con el botón de registro centrado en el bloque inferior.
- **Flujos de Usabilidad (Alto Nivel):**
    1. El visitante ingresa sus datos personales en el formulario público.
    2. Si omite rellenar un campo obligatorio, el sistema bloquea el envío y resalta visualmente los campos pendientes con indicaciones explícitas.
    3. Si el correo electrónico ya se encuentra registrado por otro usuario, se deniega la solicitud y se muestra una alerta avisando que la cuenta ya existe.
    4. Al completar todos los datos de forma válida, el sistema registra la cuenta y despliega un aviso de éxito invitando al usuario a iniciar sesión.

#### **Pantalla 3: Modal de Solicitud de Recuperación de Contraseña**

- **Historias de Usuario que cumple:** `HU-GAC-REC` (Recuperación de Contraseña).
- **Componentes Visuales:** Ventana modal con un campo para correo electrónico, mensaje explicativo y botón de acción ("Enviar Instrucciones").
- **Disposición de Componentes:** Diseño compacto y centrado con un campo único de entrada a ancho completo.
- **Flujos de Usabilidad (Alto Nivel):**
    1. El usuario que ha olvidado su clave ingresa su dirección de correo electrónico.
    2. Al presionar el botón de envío, el sistema procesa la solicitud.
    3. Por políticas de seguridad, el sistema muestra siempre una respuesta neutra confirmando el envío de instrucciones, independientemente de si el correo existe o no en la plataforma, evitando la divulgación de cuentas registradas.

#### **Pantalla 4: Vista de Restablecimiento de Contraseña (Reset Password)**

- **Historias de Usuario que cumple:** `HU-GAC-REC` (Recuperación de Contraseña).
- **Componentes Visuales:** Formulario con campos para nueva contraseña y confirmación de contraseña, indicador visual de requisitos de clave y botón de actualización ("Guardar Contraseña").
- **Disposición de Componentes:** Tarjeta central en pantalla completa enfocada exclusivamente en la captura de la nueva clave.
- **Flujos de Usabilidad (Alto Nivel):**
    1. El usuario accede mediante el enlace de recuperación recibido en su correo.
    2. Si el enlace ha expirado o ha sido alterado, el sistema bloquea el acceso al formulario y muestra un aviso sugiriendo solicitar un nuevo enlace.
    3. Si el enlace es válido y la clave cumple los requisitos de seguridad, el sistema confirma la actualización exitosa y habilita al usuario a iniciar sesión con su nueva credencial.

---

### **2. Épica `EP-VEC` — Vitrina y Exploración del Catálogo**

#### **Pantalla 5: Página Principal (Home Comercial)**

- **Historias de Usuario que cumple:** `HU-VEC-HOM` (Visualización de la Página Principal y Secciones Destacadas).
- **Componentes Visuales:** Encabezado con buscador de texto, menú horizontal de categorías deportivas, insignias contadoras para Favoritos y Bolsa de Compras, carrusel principal de promociones y grilla de productos destacados.
- **Disposición de Componentes:** Disposición vertical por secciones: encabezado fijo superior, banner promocional deslizante en el bloque central, accesos directos a categorías y grilla de productos en la parte inferior.
- **Flujos de Usabilidad (Alto Nivel):**
    1. Al ingresar a la plataforma, la pantalla carga las categorías de productos disponibles y los artículos destacados del catálogo activo.
    2. El usuario puede hacer clic en cualquier categoría para filtrar la vitrina o seleccionar un producto destacado para ir directamente a su detalle.

#### **Pantalla 6: Catálogo de Productos y Resultados de Búsqueda**

- **Historias de Usuario que cumplen:** `HU-VEC-BUS` (Búsqueda por Palabra Clave), `HU-VEC-FIL` (Navegación y Filtrado Dinámico), `HU-VEC-ORD` (Ordenamiento del Catálogo).
- **Componentes Visuales:** Barra de búsqueda, panel lateral de filtros (categorías, marcas, rangos de precio), menú desplegable de ordenamiento ("Precio: Menor a Mayor", "Precio: Mayor a Menor", "Más Recientes"), tarjetas de producto y botón "Limpiar Filtros".
- **Disposición de Componentes:** Esquema de dos bloques: panel lateral izquierdo para filtros y área principal derecha para la grilla de productos. En dispositivos móviles, los filtros se pliegan en un panel deslizable.
- **Flujos de Usabilidad (Alto Nivel):**
    1. Si el usuario escribe menos de 2 caracteres en el buscador, el sistema bloquea la búsqueda automática e indica que se requieren más letras.
    2. Al ingresar un término de al menos 2 caracteres o seleccionar filtros laterales, la grilla se actualiza mostrando las coincidencias.
    3. Si no existen productos que coincidan con la búsqueda o combinación de filtros, se despliega el aviso "No se encontraron productos" y se ofrece el botón "Limpiar Filtros" para restablecer el catálogo.
    4. Seleccionar una opción de ordenamiento reorganiza los artículos exhibidos de forma inmediata.

---

### **3. Épica `EP-DPP` / `EP-DDP` — Detalle y Disponibilidad de Producto**

#### **Pantalla 7: Ficha Técnica y Detalle del Producto**

- **Historias de Usuario que cumplen:** `HU-DDP-FIC` (Ficha Técnica y Ofertas), `HU-DDP-ATR` (Selección de Variantes), `HU-DDP-STK` (Consulta de Inventario), `HU-DDP-REL` (Productos Relacionados).
- **Componentes Visuales:** Galería de imágenes interactiva, nombre, marca, precio regular tachado, precio oferta con porcentaje de descuento, botones de selección de variantes (talla/color), etiqueta de estado de inventario ("Stock Disponible" / "Agotado"), botón "Agregar al Carrito", ícono de corazón para favoritos y carrusel inferior de productos recomendados.
- **Disposición de Componentes:** Estructura en dos columnas (galería visual a la izquierda e información comercial/controles de compra a la derecha), con la descripción técnica y artículos recomendados en la sección inferior.
- **Flujos de Usabilidad (Alto Nivel):**
    1. La pantalla presenta la información técnica, galería de fotos y precios vigentes del producto.
    2. Si el producto tiene oferta activa, se muestra el precio original tachado junto al precio promocional y el porcentaje descontado.
    3. El cliente debe seleccionar obligatoriamente las variantes de talla y color; de lo contrario, el botón de compra permanece bloqueado y se resaltan visualmente las opciones pendientes.
    4. El sistema verifica la disponibilidad de inventario en tiempo real: si hay existencias, muestra "Stock Disponible"; si la existencia es cero, despliega "Agotado" e inhabilita la opción de compra.
    5. En caso de intentar acceder a un producto inexistente o descontinuado, se muestra un aviso de alerta con un botón para retornar al catálogo.

---

### **4. Épica `EP-ITC` — Intención de Transacción y Carrito**

#### **Pantalla 8: Carrito Flotante (Panel Lateral / Drawer)**

- **Historias de Usuario que cumplen:** `HU-ITC-CAR` (Gestión del Carrito de Compras), `HU-ITC-RES` (Carrito Flotante y Subtotales).
- **Componentes Visuales:** Panel lateral emergente, lista de productos agregados con miniatura, controles para modificar cantidades (`+` / `-`), botón para eliminar ítem, enlace "Mover a Favoritos", desglose de subtotales, costo estimado de envío, total acumulado y botón "Iniciar Checkout".
- **Disposición de Componentes:** Panel desplegable sobre el margen derecho de la pantalla con lista desplazable de artículos y el resumen de totales fijo en la franja inferior.
- **Flujos de Usabilidad (Alto Nivel):**
    1. Al presionar "Agregar al Carrito" en un producto con talla/color seleccionados, el ítem se añade al carrito y se incrementa el contador visual.
    2. Si el producto ya figuraba en el carrito, se suma la cantidad en lugar de duplicar la línea.
    3. Modificar cantidades o eliminar artículos recalcula automáticamente el subtotal por producto y el total general sin recargar la página.
    4. El incremento de unidades está restringido al límite de existencias disponibles en el inventario.
    5. Un usuario autenticado puede seleccionar "Mover a Favoritos" para trasladar el ítem a su lista de deseos personal.
    6. Si el carrito no contiene productos, se muestra el mensaje "Tu carrito está vacío" con un enlace para explorar la tienda.

#### **Pantalla 9: Vista "Mis Favoritos" (Lista de Deseos)**

- **Historias de Usuario que cumple:** `HU-ITC-FAV` (Gestión de Lista de Deseos / Favoritos).
- **Componentes Visuales:** Grilla de productos guardados, ícono de corazón activo, botón para quitar de la lista y botón "Mover al Carrito".
- **Disposición de Componentes:** Disposición en catálogo personal en cuadrícula de varias columnas.
- **Flujos de Usabilidad (Alto Nivel):**
    1. Al presionar "Agregar a Favoritos", el sistema guarda el producto en la lista personal del usuario autenticado.
    2. Si un visitante no autenticado intenta guardar un favorito, se despliega el modal de inicio de sesión exigiendo identificarse.
    3. En la sección de favoritos, el usuario puede eliminar productos guardados o presionar "Mover al Carrito", lo cual valida las existencias en tiempo real antes de añadir el artículo a la bolsa de compras.

---

### **5. Épica `EP-TRX` — Transacción y Realización de Checkout**

#### **Pantalla 10: Checkout — Paso 1: Datos de Envío y Dirección**

- **Historias de Usuario que cumple:** `HU-TRX-DIR` (Captura de Datos de Envío).
- **Componentes Visuales:** Indicador de pasos del proceso (paso 1 de 3), selector de direcciones previamente guardadas, formulario de dirección (calle, departamento, provincia, distrito, teléfono) y botón "Continuar al Pago".
- **Disposición de Componentes:** Estructura en dos columnas: formulario de captura a la izquierda y tarjeta fija con el resumen de la compra a la derecha.
- **Flujos de Usabilidad (Alto Nivel):**
    1. El usuario autenticado revisa o ingresa los datos del lugar donde desea recibir su pedido.
    2. Todos los campos de dirección son obligatorios; si alguno falta, el sistema detiene el avance y resalta los campos que requieren atención.
    3. Al validar la información de entrega, se habilita el avance al siguiente paso.

#### **Pantalla 11: Checkout — Paso 2: Resumen, Cupones y Pago**

- **Historias de Usuario que cumple:** `HU-TRX-PAG` (Simulación de Pago y Revalidación de Inventario).
- **Componentes Visuales:** Desglose final de costos (Subtotal + Envío - Descuentos = Total a Pagar), campo para aplicar cupones promocionales, formulario de tarjeta simulada (Número de tarjeta, Titular, Vencimiento, Código de seguridad) y botón "Pagar y Finalizar Orden".
- **Disposición de Componentes:** Formulario de pago y validación de cupones en el bloque principal, apoyado por la caja del desglose financiero.
- **Flujos de Usabilidad (Alto Nivel):**
    1. El cliente visualiza el desglose detallado del monto final.
    2. Al ingresar un código de cupón, el sistema comprueba su vigencia y descuenta el porcentaje o monto correspondiente del total.
    3. Al hacer clic en "Pagar", el sistema ejecuta una revalidación final de inventario para confirmar que los productos siguen disponibles.
    4. Si el inventario de algún producto se agotó mientras se completaba el formulario, el proceso se detiene sin realizar cobro alguno y se notifica qué producto no está disponible.
    5. Si los datos de la tarjeta son erróneos, se deniega la transacción y se muestra la alerta correspondiente.
    6. Por seguridad, no se almacenan números completos ni códigos de tarjetas.

#### **Pantalla 12: Checkout — Paso 3: Confirmación de Pedido Exitoso**

- **Historias de Usuario que cumple:** `HU-TRX-ORD` (Generación del Pedido).
- **Componentes Visuales:** Mensaje visual de compra exitosa, código único de pedido asignado, resumen final de entrega, resumen de artículos y botones "Seguir Comprando" y "Ver Mi Pedido".
- **Disposición de Componentes:** Tarjeta central de confirmación con datos del comprobante.
- **Flujos de Usabilidad (Alto Nivel):**
    1. Aprobado el pago, el sistema registra el pedido con su identificador único, vacía automáticamente el carrito activo del usuario y emite la orden de descuento definitivo del inventario.
    2. Se desencadena el proceso automático de notificación para enviar el comprobante por correo electrónico.
    3. Si ocurre un fallo temporal en el registro central de pedidos, el sistema alerta al cliente que la orden está en proceso de verificación sin duplicar ningún cobro.

---

### **6. Épica `EP-SHP` — Seguimiento e Historial de Pedidos**

#### **Pantalla 13: Panel "Mis Pedidos" (Historial de Compras)**

- **Historias de Usuario que cumple:** `HU-SHP-HIS` (Consulta y Filtrado del Historial).
- **Componentes Visuales:** Pestañas de filtrado por estado ("Todos", "En proceso", "Entregado", "Cancelado"), tarjetas de pedido con fecha, número de orden, cantidad de artículos, monto total y estado actual.
- **Disposición de Componentes:** Listado vertical ordenado de manera cronológica (las compras más recientes aparecen primero).
- **Flujos de Usabilidad (Alto Nivel):**
    1. El usuario autenticado accede a su historial para revisar sus compras.
    2. Seleccionar una pestaña de estado filtra las órdenes para mostrar únicamente las coincidencias.
    3. Si el usuario no registra compras previas, se muestra el mensaje "Aún no has realizado ninguna compra" con un botón para explorar la tienda.

#### **Pantalla 14: Detalle de Pedido Específico y Reordenado**

- **Historias de Usuario que cumple:** `HU-SHP-DET` (Visualización del Detalle y Reordenado / Reorder).
- **Componentes Visuales:** Ficha detallada del pedido con productos, imágenes, precios unitarios, dirección de entrega, desglose de costos y botón destacado "Volver a Comprar".
- **Disposición de Componentes:** Estructura en dos columnas (artículos de la compra a la izquierda e información de cobro/entrega a la derecha).
- **Flujos de Usabilidad (Alto Nivel):**
    1. Muestra el desglose completo del pedido seleccionado.
    2. Al presionar "Volver a Comprar", el sistema consulta la disponibilidad actual de los productos en el inventario y carga los artículos disponibles directamente en el carrito activo.

#### **Pantalla 15: Seguimiento de Envío (Tracking)**

- **Historias de Usuario que cumple:** `HU-SHP-TRK` (Seguimiento del Estado del Envío).
- **Componentes Visuales:** Número de orden, empresa de transporte, fecha estimada de entrega, línea de tiempo ilustrada con las 4 etapas del despacho ("Pedido Registrado", "En Preparación", "En Ruta", "Entregado") y caja de avisos ante incidencias.
- **Disposición de Componentes:** Barra de progreso horizontal o vertical que ilumina la etapa actual del envío.
- **Flujos de Usabilidad (Alto Nivel):**
    1. Muestra el estado del paquete en tiempo real iluminando el tramo alcanzado en la barra de progreso.
    2. Si ocurre una reprogramación o inconveniente en la entrega, se despliega una etiqueta explicativa avisando de la nueva fecha de llegada.

---

🎯 ¿Deseas que preparemos las secuencias de comandos y guías de maquetación para generar estas 15 pantallas en **Stitch AI**?