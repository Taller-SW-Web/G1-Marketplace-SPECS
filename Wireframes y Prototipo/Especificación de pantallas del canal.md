# Antecedente — Especificación de 15 pantallas del canal

> [!CAUTION]
> **Documento histórico, no vigente para diseñar los mockups del próximo hito.** Conserva la descripción de los wireframes iniciales para trazabilidad. El inventario vigente está en [`SPECS/ui/vistas/README.md`](../SPECS/ui/vistas/README.md), los elementos superpuestos en [`SPECS/ui/overlays/README.md`](../SPECS/ui/overlays/README.md) y las comunicaciones en [`SPECS/ui/comunicaciones/README.md`](../SPECS/ui/comunicaciones/README.md).

## Correspondencia con el catálogo vigente

| Pantalla histórica | Entregable vigente | Cambio relevante |
|---|---|---|
| P1 Login | `V-001` Inicio de sesión | Es una ruta; `O-003` sólo intercepta y conserva el retorno. |
| P2 Registro | `V-002` Registro | Se mantiene como ruta dedicada. |
| P3 Recuperación | `V-003` Recuperación de contraseña | Se mantiene como ruta dedicada. |
| P4 Restablecimiento | `V-004` Restablecimiento de contraseña | Se mantiene como ruta dedicada. |
| P5 Home | `V-005` Inicio | Se integra con favoritos y navegación global. |
| P6 Catálogo | `V-006` Catálogo y resultados | Los filtros mobile se separan como `O-001`. |
| P7 Producto | `V-007` Ficha del producto | El visor se separa como `O-002` y el feedback de carrito como `O-005`. |
| P8 Carrito | `V-008` Carrito | Se mantiene como ruta `/carrito`; deshacer eliminación usa `O-006`. |
| P9 Favoritos | `V-009` Favoritos | Comparte `O-006` y autenticación requerida `O-003`. |
| P10 Checkout dirección | `V-010` Dirección de envío | Primer tramo del checkout vigente. |
| P11 Resumen y pago | `V-011` Resumen, envío y beneficio + `V-012` Pago simulado | Se divide en dos vistas. No existen campos de tarjeta ni CVV. |
| P12 Confirmación | `V-013` Creación de orden + `V-014` Pedido confirmado | Se separa el envío de la orden de su resultado final. |
| P13 Mis pedidos | `V-015` Historial de pedidos | Mantiene filtrado y estados vacíos. |
| P14 Detalle | `V-016` Detalle y reordenado | El resultado de reordenar se separa como `O-008`. |
| P15 Tracking | `V-017` Seguimiento | Se mantiene como ruta de seguimiento. |

## Inconsistencias conocidas del antecedente

- Las referencias a “modal o vista” para login, registro y recuperación fueron resueltas como rutas `V-001` a `V-004`.
- El formulario histórico de tarjeta quedó eliminado: `F-025` define una simulación explícita, sin número de tarjeta, titular, vencimiento ni código de seguridad.
- Agregar un producto no obliga a navegar inmediatamente al carrito; `O-005` proporciona feedback y permite continuar o abrir `V-008`.
- “Volver a comprar” ahora se presenta como “Agregar productos al carrito”; el resultado parcial se detalla en `O-008` y no implica una compra confirmada.
- La evaluación postentrega `O-009` y los correos `C-001`/`C-002` no formaban parte del inventario inicial.

---

## Contenido histórico preservado

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

- **Historias de Usuario que cumple:** `HU-VEC-HOM` (Visualización de la Página Principal y Secciones Destacadas), `HU-FAV-GUA` (Guardado de Productos en Favoritos).
- **Componentes Visuales:** Encabezado con buscador de texto, menú horizontal de categorías deportivas, insignias contadoras para Favoritos y Bolsa de Compras, carrusel principal de promociones y grilla de productos destacados.
- **Disposición de Componentes:** Disposición vertical por secciones: encabezado fijo superior, banner promocional deslizante en el bloque central, accesos directos a categorías y grilla de productos en la parte inferior.
- **Flujos de Usabilidad (Alto Nivel):**
    1. Al ingresar a la plataforma, la pantalla carga las categorías de productos disponibles y los artículos destacados del catálogo activo.
    2. El usuario puede hacer clic en cualquier categoría para filtrar la vitrina o seleccionar un producto destacado para ir directamente a su detalle.

#### **Pantalla 6: Catálogo de Productos y Resultados de Búsqueda**

- **Historias de Usuario que cumplen:** `HU-VEC-BUS` (Búsqueda por Palabra Clave), `HU-VEC-FIL` (Navegación y Filtrado Dinámico), `HU-VEC-ORD` (Ordenamiento del Catálogo), `HU-FAV-GUA` (Guardado de Productos en Favoritos).
- **Componentes Visuales:** Barra de búsqueda, panel lateral de filtros (categorías, marcas, rangos de precio), menú desplegable de ordenamiento ("Precio: Menor a Mayor", "Precio: Mayor a Menor", "Más Recientes"), tarjetas de producto y botón "Limpiar Filtros".
- **Disposición de Componentes:** Esquema de dos bloques: panel lateral izquierdo para filtros y área principal derecha para la grilla de productos. En dispositivos móviles, los filtros se pliegan en un panel deslizable.
- **Flujos de Usabilidad (Alto Nivel):**
    1. Si el usuario escribe menos de 2 caracteres en el buscador, el sistema bloquea la búsqueda automática e indica que se requieren más letras.
    2. Al ingresar un término de al menos 2 caracteres o seleccionar filtros laterales, la grilla se actualiza mostrando las coincidencias.
    3. Si no existen productos que coincidan con la búsqueda o combinación de filtros, se despliega el aviso "No se encontraron productos" y se ofrece el botón "Limpiar Filtros" para restablecer el catálogo.
    4. Seleccionar una opción de ordenamiento reorganiza los artículos exhibidos de forma inmediata.

---

### **3. Épica `EP-DDP` — Detalle y Disponibilidad de Producto**

#### **Pantalla 7: Ficha Técnica y Detalle del Producto**

- **Historias de Usuario que cumplen:** `HU-DDP-FIC` (Ficha Técnica y Ofertas), `HU-DDP-ATR` (Selección de Variantes), `HU-DDP-STK` (Consulta de Inventario), `HU-DDP-REL` (Productos Relacionados), `HU-FAV-GUA` (Guardado de Productos en Favoritos).
- **Componentes Visuales:** Galería de imágenes interactiva, nombre, marca, precio regular tachado, precio oferta con porcentaje de descuento, botones de selección de variantes (talla/color), etiqueta de estado de inventario ("Stock Disponible" / "Agotado"), botón "Agregar al Carrito", ícono de corazón para favoritos y carrusel inferior de productos recomendados.
- **Disposición de Componentes:** Estructura en dos columnas (galería visual a la izquierda e información comercial/controles de compra a la derecha), con la descripción técnica y artículos recomendados en la sección inferior.
- **Flujos de Usabilidad (Alto Nivel):**
    1. La pantalla presenta la información técnica, galería de fotos y precios vigentes del producto.
    2. Si el producto tiene oferta activa, se muestra el precio original tachado junto al precio promocional y el porcentaje descontado.
    3. El cliente debe seleccionar obligatoriamente las variantes de talla y color; de lo contrario, el botón de compra permanece bloqueado y se resaltan visualmente las opciones pendientes.
    4. El sistema verifica la disponibilidad de inventario en tiempo real: si hay existencias, muestra "Stock Disponible"; si la existencia es cero, despliega "Agotado" e inhabilita la opción de compra.
    5. En caso de intentar acceder a un producto inexistente o descontinuado, se muestra un aviso de alerta con un botón para retornar al catálogo.

---

### **4. Carrito y Favoritos — Épicas `EP-ITC` y `EP-FAV`**

#### **Pantalla 8: Vista Principal del Carrito de Compras (`/carrito`)**

- **Épica y responsable:** `EP-ITC`, Sebastián — Documentador / Desarrollo de Carrito.
- **Historias de Usuario que cumplen:** `HU-ITC-CAR` (Gestión del Carrito de Compras), `HU-ITC-RES` (Carrito Flotante y Subtotales).
- **Componentes Visuales:** Lista de productos agregados con miniatura, controles para modificar cantidades (`+` / `-`), botón para eliminar ítem, enlace "Mover a Favoritos", desglose de subtotales, costo estimado de envío, total acumulado y botón "Iniciar Checkout".
- **Disposición de Componentes:** Vista de página completa estructurada en dos columnas: lista desplazable de artículos a la izquierda y tarjeta fija con resumen de totales y botón de checkout a la derecha.
- **Flujos de Usabilidad (Alto Nivel):**
    1. Al presionar "Agregar al Carrito" en un producto con talla/color seleccionados, el ítem se añade al carrito y se incrementa el contador visual.
    2. Si el producto ya figuraba en el carrito, se suma la cantidad en lugar de duplicar la línea.
    3. Modificar cantidades o eliminar artículos recalcula automáticamente el subtotal por producto y el total general sin recargar la página.
    4. El incremento de unidades está restringido al límite de existencias disponibles en el inventario.
    5. Un usuario autenticado puede seleccionar "Mover a Favoritos" para trasladar el ítem a su lista de deseos personal.
    6. Si el carrito no contiene productos, se muestra el mensaje "Tu carrito está vacío" con el enlace "Explorar Tienda" para retornar a la vitrina comercial.

#### **Pantalla 9: Vista "Mis Favoritos" (Lista de Deseos)**

- **Historias de Usuario que cumple:** `HU-FAV-GES` (Consulta y Eliminación de Favoritos), `HU-FAV-CAR` (Transferencia de Favoritos al Carrito).
- **Componentes Visuales:** Grilla de productos guardados, ícono de corazón activo, botón para quitar de la lista y botón "Mover al Carrito".
- **Disposición de Componentes:** Disposición en catálogo personal en cuadrícula de varias columnas.
- **Flujos de Usabilidad (Alto Nivel):**
    1. Al presionar "Agregar a Favoritos", el sistema guarda el producto en la lista personal del usuario autenticado.
    2. Si un visitante no autenticado intenta guardar un favorito, se despliega el modal o vista de inicio de sesión; tras autenticarse con éxito, retorna a la pantalla de origen completando el guardado.
    3. En la sección de favoritos, el usuario puede eliminar productos guardados o presionar "Mover al Carrito". Si el producto requiere selección de variantes (talla o color), se redirige a la ficha técnica (P7); si es un producto simple sin variantes, valida existencias en tiempo real, lo añade al carrito y lo retira de favoritos.
    4. Si el producto no cuenta con stock disponible, el sistema informa al cliente y mantiene el artículo en la lista de favoritos.

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

> Este cierre pertenecía al alcance preliminar de 15 pantallas. Para el trabajo actual se deben diseñar los entregables `V-###`, `O-###` y `C-###` del catálogo vigente.
