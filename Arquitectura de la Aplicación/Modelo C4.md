A continuación se presenta el **Modelo C4 Completo** para el **Canal Marketplace**, formalizado en sus tres primeros niveles de abstracción (Contexto, Contenedores y Componentes) en sintaxis **Mermaid C4** [70, 71, 73–76].

---

### **Nivel 1: Diagrama de Contexto del Sistema (System Context)**

El Nivel 1 muestra la visión global del **Canal Marketplace** dentro del ecosistema de microservicios deportivos, detallando sus interacciones con el cliente y con los sistemas externos.

```mermaid.js
C4Context
    title C4 - Nivel 1: Diagrama de Contexto para el Canal Marketplace

    Person(cliente, "Cliente / Visitante", "Usuario final que explora la vitrina, busca productos, gestiona su carrito/favoritos, realiza compras y consulta el estado de sus pedidos.")

    System(marketplace, "Canal Marketplace", "Plataforma e-commerce e interfaz cliente para la exploración del catálogo, carrito de compras, checkout multipaso, favoritos y seguimiento de envíos.")

    System_Ext(seguridad, "Módulo de Seguridad y Usuarios", "Microservicio dueño de las credenciales y cuentas de usuario. Emite y gestiona tokens JWT.")
    System_Ext(productos, "Módulo de Productos y Ofertas", "Microservicio dueño del catálogo, precios, categorías, marcas, promociones e inventario (stock).")
    System_Ext(ventas, "Módulo de Ventas y Postventa", "Microservicio dueño de la entidad Pedido. Registra las órdenes aprobadas y mantiene el historial de compras.")
    System_Ext(despacho, "Módulo de Despacho y Entrega", "Microservicio dueño de la entidad Despacho. Gestiona las rutas y el estado en tiempo real de los envíos.")
    System_Ext(resend, "Resend API (SaaS)", "Plataforma externa para el envío masivo y asíncrono de correos electrónicos transaccionales.")

    Rel(cliente, marketplace, "Navega, agrega productos al carrito, realiza pagos y consulta pedidos", "HTTPS")
    Rel(marketplace, seguridad, "Delega el registro, autenticación de usuarios y recuperación de clave", "REST / HTTPS")
    Rel(marketplace, productos, "Consulta catálogo, obtiene precios/ofertas y revalida stock pre-pago", "REST / HTTPS")
    Rel(marketplace, ventas, "Transmite órdenes de compra aprobadas y lee el historial 'Mis Pedidos'", "REST / HTTPS")
    Rel(marketplace, despacho, "Consulta el progreso del paquete en ruta para la barra de tracking", "REST / HTTPS")
    Rel(marketplace, resend, "Dispara notificaciones de confirmación de compra y avisos de despacho", "REST / HTTPS")
```

---

### **Nivel 2: Diagrama de Contenedores (Containers)**

El Nivel 2 desglosa la arquitectura tecnológica del **Canal Marketplace** en sus unidades de ejecución y despliegue independientes (Frontend, Backend y Persistencia Local).

```mermaid.js
C4Container
    title C4 - Nivel 2: Diagrama de Contenedores para el Canal Marketplace

    Person(cliente, "Cliente / Visitante", "Usuario del e-commerce desde navegador web o dispositivo móvil.")

    Container_Boundary(c1, "Canal Marketplace (Límite del Módulo)") {
        Container(web_app, "Web App (Frontend)", "Next.js 14 / React (Vercel PaaS)", "Proporciona las 15 pantallas web independientes, gestión de estado del carrito con Zustand y peticiones asíncronas con TanStack Query/Axios.")
        Container(api_app, "API Application (Backend)", "Node.js / NestJS (Render PaaS)", "Procesa los controladores REST, orquestación de checkout, gestión de accesos, adaptadores API y workers de eventos de correo.")
        ContainerDb(db_local, "Base de Datos Local", "PostgreSQL 16 / Prisma ORM (Render DB)", "Almacena de forma aislada e independiente el carrito temporal (CartItem) y los favoritos (WishlistItem).")
    }

    System_Ext(seguridad, "Módulo de Seguridad", "API REST Externa")
    System_Ext(productos, "Módulo de Productos", "API REST Externa")
    System_Ext(ventas, "Módulo de Ventas", "API REST Externa")
    System_Ext(despacho, "Módulo de Despacho", "API REST Externa")
    System_Ext(resend, "Resend SaaS", "API REST Externa")

    Rel(cliente, web_app, "Renderiza interfaz e-commerce responsiva", "HTTPS / TLS")
    Rel(web_app, api_app, "Consume la API Interna del Marketplace", "HTTPS / JSON")
    Rel(api_app, db_local, "Persiste y lee carrito y favoritos", "Prisma TCP")

    Rel(api_app, seguridad, "Valida credenciales y emite tokens JWT", "HTTPS / REST")
    Rel(api_app, productos, "Consulta productos y revalida stock pre-pago", "HTTPS / REST")
    Rel(api_app, ventas, "Envía órdenes empaquetadas", "HTTPS / REST")
    Rel(api_app, despacho, "Obtiene la etapa del paquete", "HTTPS / REST")
    Rel(api_app, resend, "Despacha emails transaccionales en segundo plano", "HTTPS / REST")
```

---

### **Nivel 3: Diagrama de Componentes (Components)**

El Nivel 3 hace un _zoom-in_ dentro de la **API Application (Backend de NestJS)**, detallando la interacción entre los **Controladores HTTP (Capa A)**, los **Servicios de Dominio (Capa B)**, la **Persistencia Local (Capa C)** y los **Adaptadores Externe API / Capa Anti-Corrupción (Capa D)** [73–76].

```mermaid.js
C4Component
    title C4 - Nivel 3: Diagrama de Componentes Internos (Backend NestJS)

    Container(web_app, "Web App (Next.js)", "Frontend Client", "Envía peticiones HTTP/REST.")
    ContainerDb(db_local, "PostgreSQL Local", "Prisma ORM", "Almacena CartItem y WishlistItem.")

    Container_Boundary(b1, "API Application (Backend NestJS)") {

        %% CAPA A: CONTROLADORES REST
        Component(auth_ctrl, "Auth Controller", "@Controller('/auth')", "Maneja peticiones de login, registro y recuperación.")
        Component(catalog_ctrl, "Catalog Controller", "@Controller('/products')", "Recibe peticiones de búsqueda, catálogo, filtros y ficha técnica.")
        Component(cart_ctrl, "Cart & Wishlist Controller", "@Controller('/cart')", "Maneja la adición, edición, eliminación y favoritos.")
        Component(checkout_ctrl, "Checkout Controller", "@Controller('/checkout')", "Recibe direcciones, cupones y simulación de pago.")
        Component(orders_ctrl, "Orders & Tracking Controller", "@Controller('/orders')", "Recibe solicitudes de historial 'Mis Pedidos' y tracking.")

        %% CAPA B: SERVICIOS DE DOMINIO Y ORQUESTADORES
        Component(cart_srv, "Cart & Wishlist Service", "@Injectable()", "Calcula subtotales en tiempo real, unifica carritos anónimos tras el login y gestiona favoritos.")
        Component(checkout_orch, "Checkout Orchestrator", "@Injectable()", "Coordina el flujo multipaso: ejecuta la revalidación de stock pre-pago y empaqueta la orden.")
        Component(notif_worker, "Notification Worker", "@Injectable()", "Event Listener que escucha 'order.created' y despacha emails con React Email/Resend SDK.")
        Component(event_emitter, "NestJS Event Emitter", "EventEmitter2", "Bus de eventos interno para desacoplar el envío de correos.")

        %% CAPA C: PERSISTENCIA LOCAL
        Component(prisma_srv, "Prisma Service", "@Injectable()", "Cliente ORM tipado para acceso a PostgreSQL local.")

        %% CAPA D: ADAPTADORES DE INTEGRACIÓN (CAPA ANTI-CORRUPCIÓN)
        Component(sec_adapter, "Security Adapter", "Adapter Service", "Aísla llamadas al Módulo de Seguridad.")
        Component(prod_adapter, "Products Adapter", "Adapter Service", "Aísla consultas de catálogo y revalidación de stock.")
        Component(sales_adapter, "Sales Adapter", "Adapter Service", "Aísla el empaquetado de órdenes hacia Ventas.")
        Component(disp_adapter, "Dispatch Adapter", "Adapter Service", "Aísla consultas de tracking hacia Despacho.")
        Component(http_srv, "HttpService / Mocks", "@nestjs/axios", "Wrapper Axios con interceptor axios-mock-adapter según USE_MOCKS.")
    }

    System_Ext(ext_sec, "Módulo Seguridad", "API REST")
    System_Ext(ext_prod, "Módulo Productos", "API REST")
    System_Ext(ext_sales, "Módulo Ventas", "API REST")
    System_Ext(ext_disp, "Módulo Despacho", "API REST")
    System_Ext(ext_resend, "Resend API", "SaaS REST")

    %% RELACIONES INTERNAS
    Rel(web_app, auth_ctrl, "POST /auth/*", "JSON")
    Rel(web_app, catalog_ctrl, "GET /products/*", "JSON")
    Rel(web_app, cart_ctrl, "GET, POST, DELETE /cart/*", "JSON")
    Rel(web_app, checkout_ctrl, "POST /checkout/*", "JSON")
    Rel(web_app, orders_ctrl, "GET /orders/*", "JSON")

    Rel(auth_ctrl, sec_adapter, "Delega autenticación")
    Rel(catalog_ctrl, prod_adapter, "Delega consultas de catálogo")
    Rel(cart_ctrl, cart_srv, "Delega cálculo e ítems")
    Rel(checkout_ctrl, checkout_orch, "Delega orquestación de pago")
    Rel(orders_ctrl, sales_adapter, "Consulta historial")
    Rel(orders_ctrl, disp_adapter, "Consulta tracking")

    Rel(cart_srv, prisma_srv, "CRUD CartItem / WishlistItem")
    Rel(cart_srv, prod_adapter, "Valida stock de ítems")
    Rel(checkout_orch, prod_adapter, "Ejecuta revalidación pre-pago")
    Rel(checkout_orch, sales_adapter, "Transmite orden empaquetada")
    Rel(checkout_orch, event_emitter, "Emite evento 'order.created'")
    Rel(event_emitter, notif_worker, "Dispara notificación asíncrona")

    Rel(prisma_srv, db_local, "Consulta / Modifica", "Prisma TCP")

    Rel(sec_adapter, http_srv, "Llamada HTTP saliente")
    Rel(prod_adapter, http_srv, "Llamada HTTP saliente")
    Rel(sales_adapter, http_srv, "Llamada HTTP saliente")
    Rel(disp_adapter, http_srv, "Llamada HTTP saliente")

    Rel(http_srv, ext_sec, "Petición REST / Mocks", "HTTPS")
    Rel(http_srv, ext_prod, "Petición REST / Mocks", "HTTPS")
    Rel(http_srv, ext_sales, "Petición REST / Mocks", "HTTPS")
    Rel(http_srv, ext_disp, "Petición REST / Mocks", "HTTPS")
    Rel(notif_worker, ext_resend, "Despacha email en segundo plano", "HTTPS")
```

