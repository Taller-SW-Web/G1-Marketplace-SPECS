# Modelo C4 — Canal Marketplace

**Inka Athletics · Grupo 1 · Hito 3**

**Snapshot de referencia:** 17/10/2026, frontend `develop@0b0ed1c` y backend `develop@62f077d`. Para la comparación con FE `main@ec1acfb`/BE `main@c7e8e8e`, categorías G6 locales y gates aún pendientes, ver el [corte del 18/10](../plan/CORTE-H3-Y-TRASPASO-H4.md). Las relaciones «previsto» de este diagrama se interpretan en el contexto de su snapshot.

El modelo conserva los tres niveles de aproximación del documento original: **contexto**, **contenedores** y **componentes**. La vista de componentes incluye frontend y backend. La explicación del stack, las capas, la persistencia, los entornos, el CI y las responsabilidades está en [Arquitectura de la Aplicación](Arquitectura.md).

## Convenciones de lectura

| Elemento | Significado |
| --- | --- |
| Persona | Cliente o visitante que utiliza el canal. |
| Sistema azul | Marketplace, sistema que desarrolla el Grupo 1. |
| Sistema gris | Módulo externo dueño de sus datos y reglas. |
| Contenedor / componente azul | Unidad de aplicación o componente existente en el corte de código. |
| Elemento ámbar / etiqueta MOCK | Demostración o implementación de prueba. |
| Relación con etiqueta «previsto» | Interacción del diseño funcional sin integración real acreditada en este corte. |

Los diagramas C4 utilizan relaciones rotuladas. La presencia de una flecha expresa responsabilidad o comunicación; cuando indica «previsto» no acredita una llamada real. La disponibilidad pública y el cierre de funcionalidades se sustentan en pruebas y evidencias adicionales.

## Nivel 1. Diagrama de contexto del sistema

**Pregunta que responde:** ¿quién utiliza Marketplace y con qué sistemas se relaciona?

El cliente emplea Marketplace como canal de compra. Seguridad conserva la identidad; Productos, el catálogo y el inventario; Ventas, el pedido; Despacho, el envío. El correo aparece como capacidad prevista cuyo proveedor todavía debe concretarse.

![Diagrama c4-01-contexto](diagramas/c4-01-contexto.svg)

<details>
<summary>Ver fuente Mermaid del diagrama</summary>

```mermaid
C4Context
    title Marketplace - C4 nivel 1: contexto del sistema

    Person(cliente, "Cliente / Visitante", "Explora productos y realiza el recorrido de compra.")
    System(marketplace, "Canal Marketplace", "Canal web de compra: catálogo, ficha, carrito, favoritos, checkout y pedidos.")

    System_Ext(seguridad, "Seguridad y Usuarios", "Identidad, credenciales y direcciones.")
    System_Ext(productos, "Productos y Ofertas", "Catálogo, precios, promociones y stock.")
    System_Ext(ventas, "Ventas y Postventa", "Pedidos, comprobantes y atención posterior.")
    System_Ext(despacho, "Despacho y Entrega", "Cotización y estado del envío.")
    System_Ext(correo, "Proveedor de correo [PREVISTO]", "Entrega de notificaciones; proveedor por definir.")

    Rel(cliente, marketplace, "Utiliza el canal web")
    Rel(marketplace, seguridad, "Previsto: delega acceso e identidad")
    Rel(marketplace, productos, "Previsto: consulta productos y stock")
    Rel(marketplace, ventas, "Previsto: crea y consulta pedidos")
    Rel(marketplace, despacho, "Previsto: consulta cotización y envío")
    Rel(marketplace, correo, "Previsto: envía notificaciones")

    UpdateElementStyle(correo, "#FFF2D6", "#6B450D", "#B7791F")
    UpdateLayoutConfig("3", "1")
```

</details>

### Límites y estado de las relaciones

| Relación | Rol dentro del sistema | Evidencia H3 del corte |
| --- | --- | --- |
| Cliente → Marketplace | Uso de la interfaz y del recorrido de compra. | Frontend publicado y avances locales parciales. |
| Marketplace → Productos | Lectura pública y revalidación comercial. | Ficha F-011 con fixture; integración real I-01 pendiente. |
| Marketplace → Seguridad | Acceso e identidad del titular. | Login de ejemplo y validación técnica de tokens; sesión real no acreditada. |
| Marketplace → Ventas | Creación y consulta de pedidos. | Gateway/proveedor MOCK; llamada real pendiente de evidencia. |
| Marketplace → Despacho | Cotización y seguimiento. | Dependencia funcional prevista. |
| Marketplace → correo | Confirmación de compra y actualización de envío. | Sin worker/proveedor de envío operativo acreditado. |

El contexto representa el alcance funcional completo del canal. No contiene frameworks ni tablas: esos detalles aparecen en los siguientes niveles.

## Nivel 2. Diagrama de contenedores

**Pregunta que responde:** ¿qué aplicaciones y almacenes forman Marketplace y cómo se comunican?

La aplicación Next.js se divide aquí por su ejecución: la interfaz React en el navegador y el servidor Next.js que resuelve páginas y rutas de API. Ambos pertenecen al mismo repositorio frontend y al despliegue web. El backend NestJS es una aplicación separada; PostgreSQL es el almacén propio del canal.

![Diagrama c4-02-contenedores](diagramas/c4-02-contenedores.svg)

<details>
<summary>Ver fuente Mermaid del diagrama</summary>

```mermaid
C4Container
    title Marketplace - C4 nivel 2: contenedores

    Person(cliente, "Cliente / Visitante", "Utiliza el canal desde su navegador.")

    System_Boundary(marketplace, "Canal Marketplace - Grupo 1") {
        Container(ui, "Interfaz web", "React 19 / TypeScript", "Páginas, formularios y estado de la experiencia de compra.")
        Container(next, "Servidor web y fachada", "Next.js 16 / App Router", "Entrega la web y expone proxies /api para el navegador.")
        Container(api, "API Marketplace", "NestJS 11 / Node.js", "Validación, servicios, persistencia y proveedores de demo.")
        ContainerDb(db, "Base de datos propia", "PostgreSQL 16 / Prisma 5", "Carrito, favoritos y control operativo de checkout y notificaciones.")
    }

    System_Ext(productos, "Productos y Ofertas", "Catálogo, precios y stock.")
    System_Ext(seguridad, "Seguridad y Usuarios", "Identidad y acceso.")
    System_Ext(ventas, "Ventas y Postventa", "Pedido e historial.")
    System_Ext(despacho, "Despacho y Entrega", "Cotización y seguimiento.")

    Rel(cliente, ui, "Interactúa")
    Rel(ui, next, "Solicita datos y acciones", "Fetch / mismo origen")
    Rel(next, api, "Reenvía solicitudes del canal", "HTTP JSON")
    Rel(api, db, "Lee y escribe datos propios", "Prisma")
    Rel(api, productos, "Previsto: contrato real")
    Rel(api, seguridad, "Previsto: sesión real")
    Rel(api, ventas, "Previsto: pedido real")
    Rel(api, despacho, "Previsto: entrega real")

    UpdateLayoutConfig("2", "1")
```

</details>

### Contenedores y despliegue

| Contenedor | Ubicación del código | Entorno / estado |
| --- | --- | --- |
| Interfaz React | Frontend: `src/app`, `src/features`, `src/shared/ui`. | Se ejecuta en el navegador; la versión pública debe contrastarse con el commit de la demo. |
| Servidor Next.js | Frontend: páginas servidor y `src/app/api`. | Vercel público accesible. `MARKETPLACE_API_URL` se resuelve en servidor. |
| API NestJS | Backend: `src/app.module.ts` y módulos por funcionalidad. | Probada localmente para F-011 MOCK. Render está definido en infraestructura; versión pública no registrada en este corte. |
| PostgreSQL | Backend: `prisma/schema.prisma` y migraciones. | Prisma define seis modelos; el despliegue y las migraciones aplicadas se comprueban por entorno. |

Los fixtures del backend son componentes internos de la aplicación; no se representan como un microservicio externo. C4 utiliza «contenedor» para una aplicación o almacén, incluso si no se empaqueta con Docker.

## Nivel 3A. Componentes del frontend

**Pregunta que responde:** ¿cómo se reparte la interfaz y dónde se encuentran sus llamadas al backend?

![Diagrama c4-03-componentes-frontend](diagramas/c4-03-componentes-frontend.svg)

<details>
<summary>Ver fuente Mermaid del diagrama</summary>

```mermaid
C4Component
    title Marketplace - C4 nivel 3A: componentes del frontend

    Person(cliente, "Cliente", "Navega y utiliza los controles.")

    Container_Boundary(frontend, "Aplicación web Next.js / React") {
        Component(paginas, "Páginas App Router", "src/app", "Define las rutas y compone cada funcionalidad.")
        Component(ui, "UI y funcionalidades", "src/features", "Catálogo, ficha, acceso, carrito, checkout, favoritos y pedidos.")
        Component(compartidos, "Componentes visuales", "src/shared/ui + CSS", "Cabecera, pie, campos, botones y estados reutilizables.")
        Component(estado, "Estado y servicios cliente", "Hooks / Context / Fetch", "Gestiona solicitudes, estado local y WishlistProvider.")
        Component(proxies, "Fachada HTTP", "Route Handlers /api", "Valida transporte y conecta con la API Marketplace.")
        Component(sandbox, "Sandbox local [MOCK]", "features/wishlist/server", "Sesión y tokens de prueba limitados a desarrollo.")
    }

    Container(api, "API Marketplace", "NestJS", "Servicios del canal.")

    Rel(cliente, paginas, "Abre una ruta")
    Rel(paginas, ui, "Compone")
    Rel(ui, compartidos, "Reutiliza")
    Rel(ui, estado, "Dispara acciones y refleja estado")
    Rel(estado, proxies, "Consulta o envía datos", "Fetch")
    Rel(proxies, api, "Reenvía al backend", "HTTP JSON")
    Rel(proxies, sandbox, "Usa solo en demo habilitada")

    UpdateElementStyle(sandbox, "#FFF2D6", "#6B450D", "#B7791F")
    UpdateLayoutConfig("2", "1")
```

</details>

| Área funcional | Ruta de pantalla | Entrada de datos / API |
| --- | --- | --- |
| Inicio y búsqueda | `/`, `/catalogo` | `/api/catalog/home`, `/api/catalog/products`. |
| Ficha | `/productos/[slug]` | `/api/catalog/products/[slug]`. |
| Acceso | `/login` | `/api/v1/auth/login`; registro y recuperación son páginas informativas del corte. |
| Carrito | `/carrito` | `/api/cart/*`. |
| Checkout | `/checkout`, `/checkout/confirmado/[orderId]` | `/api/checkout/*` y modo local/servidor según configuración. |
| Favoritos | `/favoritos` y rutas `/demo/h3/favoritos` | `WishlistProvider`, `/api/wishlist/*` y sesión sandbox cuando está habilitada. |
| Historial | `/mis-pedidos` | `/api/orders/me`. |

El listado de rutas describe su presencia en código, no la finalización de todas sus funciones. Los estados y límites se explican en [Arquitectura.md](Arquitectura.md#1-resumen-ejecutivo-y-visión-general-del-sistema).

## Nivel 3B. Componentes del backend

**Pregunta que responde:** ¿cómo organiza NestJS la entrada, los servicios, la persistencia y las respuestas MOCK?

![Diagrama c4-04-componentes-backend](diagramas/c4-04-componentes-backend.svg)

<details>
<summary>Ver fuente Mermaid del diagrama</summary>

```mermaid
C4Component
    title Marketplace - C4 nivel 3B: componentes del backend

    Container(next, "Fachada web", "Next.js /api", "Solicitudes del navegador.")

    Container_Boundary(backend, "API Marketplace - NestJS") {
        Component(controllers, "Controladores REST", "NestJS + DTO", "Entrada de catálogo, acceso, carrito, favoritos, checkout y pedidos.")
        Component(guards, "Identidad y autorización", "AuthGuard / IdentityGuard", "Valida tokens y principal en las rutas protegidas.")
        Component(producto, "Detalle y acceso", "ProductDetailService / AuthService", "Ficha F-011 y validación F-002 de demostración.")
        Component(carrito, "Carrito", "CartService", "Ítems y estado del carrito propio.")
        Component(favoritos, "Favoritos", "Wishlist services", "Guardar, leer y coordinar adición al carrito.")
        Component(checkout, "Checkout", "CheckoutService / QuotesService", "Preparación, resumen e idempotencia.")
        Component(pedidos, "Historial", "OrdersService", "Proyección de pedidos del titular de prueba.")
        Component(prisma, "Persistencia", "PrismaService / repositorios", "Acceso al esquema de datos propio.")
        Component(proveedores, "Proveedores de demo [MOCK]", "Gateway / puertos / fixtures", "Datos sintéticos, elegibilidad y respuestas de checkout.")
    }

    ContainerDb(db, "Base de datos propia", "PostgreSQL", "Seis modelos locales.")

    Rel(next, controllers, "Llama a la API", "HTTP JSON")
    Rel(controllers, guards, "Protege rutas aplicables")
    Rel(controllers, producto, "Detalle y login")
    Rel(controllers, carrito, "Operaciones de carrito")
    Rel(controllers, favoritos, "Operaciones de favoritos")
    Rel(controllers, checkout, "Flujo de checkout")
    Rel(controllers, pedidos, "Consulta historial")
    Rel(producto, proveedores, "Usa fixture")
    Rel(favoritos, proveedores, "Consulta puertos sandbox")
    Rel(favoritos, carrito, "Coordina alta en carrito")
    Rel(checkout, proveedores, "Usa MarketplaceGateway")
    Rel(pedidos, proveedores, "Usa ORDERS_PROVIDER")
    Rel(carrito, prisma, "Lee y escribe")
    Rel(favoritos, prisma, "Usa repositorio")
    Rel(checkout, prisma, "Registra operación")
    Rel(prisma, db, "Consulta y transacciona")

    UpdateElementStyle(proveedores, "#FFF2D6", "#6B450D", "#B7791F")
    UpdateLayoutConfig("3", "1")
```

</details>

### Correspondencia con el código

| Componente dibujado | Clases / módulos concretos | Aclaración |
| --- | --- | --- |
| Controladores REST | `ProductDetailController`, `AuthController`, `CartController`, `WishlistController`, `CheckoutController`, `OrdersController`. | No se incluye un controlador de tracking implementado ni un worker de correo. |
| Identidad | `AuthGuard`, `IdentityGuard`, `IdentityPort`. | La validación de JWT/JWKS no acredita el flujo real de inicio de sesión con Seguridad. |
| Detalle y acceso | `ProductDetailService`, `AuthService`. | Componentes separados, agrupados en el dibujo para mantenerlo legible; ambos contienen cortes MOCK. |
| Favoritos | `WishlistService`, `WishlistReadService`, `WishlistCartService`, `PrismaWishlistRepository`. | La transferencia a carrito reutiliza `CartService`. |
| Checkout | `CheckoutService`, `QuotesService`, `MarketplaceGateway`. | Maneja datos de preparación y control de operación; el gateway bloquea integraciones reales no configuradas. |
| Historial | `OrdersService`, `ORDERS_PROVIDER`, `MockOrdersProvider`. | Fuente MOCK optativa fuera de producción. |
| Proveedores de demo | Fixture F-011, `SandboxProductEligibility`, `SandboxWishlistCatalog`, `MockHttpAdapter` y proveedor de pedidos. | Son implementaciones de prueba; no son APIs reales de otros equipos. |
| Persistencia | `PrismaService`, repositorios y esquema Prisma. | El código define Cart, CartItem, WishlistItem, CheckoutOperation, PostDeliveryPrompt y NotificationDelivery. |
| Infraestructura adicional | `ConfigModule`, `PrismaModule`, `HealthModule`. | Configuración, conexión y estado de salud; se omiten del gráfico para centrar las dependencias funcionales. |

## Recorrido comprobado y relaciones que faltan

El recorrido local de referencia es:

**Cliente → ficha React → proxy Next.js → ProductDetailController → ProductDetailService → fixture MOCK.**

La ficha respondió con datos de prueba, galería y estados de error. En el mismo corte, inicio y listado de catálogo devolvieron 404; no se acreditó aún el recorrido completo catálogo → ficha. Tampoco se acredita una conexión real a Productos, Seguridad, Ventas o Despacho mediante estas pruebas.

El esquema contiene modelos para notificación e invitación postentrega. Eso prepara persistencia; el worker de correo, su proveedor y la entrega efectiva siguen por implementar/verificar.

## Cómo utilizar estos gráficos en la presentación

- **Contexto:** mostrar el nivel 1 para explicar cliente, Marketplace y módulos dueños.
- **Arquitectura:** mostrar el nivel 2 para explicar frontend, fachada Next.js, API NestJS y base propia.
- **Componentes:** utilizar nivel 3A o 3B si se necesita explicar una parte del código.
- **Flujo funcional y nube:** complementar con los diagramas de secuencia y despliegue de [Arquitectura.md](Arquitectura.md).

Cada gráfico incluye una vista SVG para mostrar figuras y relaciones con una distribución estable. Su fuente Mermaid está desplegable debajo. Las vistas vectoriales se mantienen con el [generador de diagramas](diagramas/generar-c4.py), que utiliza Python estándar.

## Fuentes

- [Arquitectura de la Aplicación](Arquitectura.md): stack, capas, despliegue, persistencia, responsables y modos de demo.
- [Modelo lógico de datos](Base%20de%20Datos/01-Modelo-logico-inicial.md).
- [Repositorios, prototipos y demo](../ENLACES-DEL-PROYECTO-Y-DEMO-H3.md).
- [Código frontend del corte](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/tree/0b0ed1c) y [backend del corte](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/tree/62f077d).
- [Modelo C4 oficial](https://c4model.com/diagrams) y [sintaxis C4 en Mermaid](https://mermaid.js.org/syntax/c4.html).
