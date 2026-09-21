##### **1. Resumen Ejecutivo y Visión General del Sistema**

El **Canal Marketplace** es el módulo cliente dedicado a la exploración, selección y compra de productos deportivos dentro del ecosistema multicanal. El sistema está diseñado bajo una arquitectura de **Microservicios Desacoplados**, operando con total autonomía en su capa de presentación (frontend), backend de aplicación y persistencia relacional local aislada. La construcción del módulo sigue el enfoque de **Spec-Driven Development (SDD)** con desarrollo asistido por Inteligencia Artificial, asegurando trazabilidad total desde las Historias de Usuario escritas en sintaxis BDD (Gherkin) hasta la ejecución final.

```mermaid.js
graph TD

subgraph Marketplace["Canal Marketplace (Cliente)"]

    subgraph Frontend["Frontend Web (Vercel PaaS)"]
        NextJS["Next.js / React Framework"]
        Zustand["Zustand<br/>(Estado Global del Carrito)"]
        TQ["TanStack Query + Axios<br/>(HTTP)"]

        NextJS --- Zustand
        NextJS --- TQ
    end

    subgraph Backend["Backend de Aplicación (Render PaaS)"]
        NestJS["Node.js / NestJS Framework<br/>(@nestjs/config)"]
        HttpService["@nestjs/axios<br/>(HttpService)"]
        AuthGuard["Auth Guard<br/>(JWT Delegated)"]
        CartService["Cart & Wishlist Service"]
        CheckoutOrch["Checkout Orchestrator"]
        Adapters["Capa D: Adapter Services<br/>(Security, Products, Sales, Dispatch)"]
        MockAdapter["axios-mock-adapter<br/>(USE_MOCKS=true)"]
        EventEmitter["NestJS Event Emitter"]
        ResendSDK["Resend Node.js SDK"]

        NestJS --- AuthGuard
        NestJS --- CartService
        NestJS --- CheckoutOrch
        NestJS --- Adapters

        Adapters --- HttpService
        HttpService --- MockAdapter

        NestJS --- EventEmitter
        EventEmitter --> ResendSDK
    end

    subgraph Storage["Persistencia Relacional Local"]
        LocalDB["PostgreSQL<br/>Prod: Render PostgreSQL<br/>Dev: Docker Compose"]
    end

    TQ -->|"HTTPS / JSON<br/>(API Interna)"| NestJS
    NestJS -->|"Prisma ORM"| LocalDB

end

subgraph ExternalServices["APIs REST - Microservicios Externos"]

    SecModule["Módulo Seguridad y Usuarios<br/>(JWT / Auth)"]

    ProdModule["Módulo Productos y Ofertas<br/>(Catálogo / Stock)"]

    SalesModule["Módulo Ventas y Postventa<br/>(Órdenes)"]

    DispatchModule["Módulo Despacho y Entrega<br/>(Tracking)"]

    ResendSaaS["Resend API (SaaS)<br/>(Despacho de Emails)"]

end

Adapters -->|"REST / HTTPS<br/>o Axios Mock Adapter"| SecModule
Adapters -->|"REST / HTTPS<br/>o Axios Mock Adapter"| ProdModule
Adapters -->|"REST / HTTPS<br/>o Axios Mock Adapter"| SalesModule
Adapters -->|"REST / HTTPS<br/>o Axios Mock Adapter"| DispatchModule

ResendSDK -->|"API REST / HTTPS"| ResendSaaS
```

---

##### **2. Stack Tecnológico Seleccionado**

El stack tecnológico elegido combina alto rendimiento, agilidad y las herramientas seleccionadas para el proyecto:

| Capa / Componente                         | Tecnología Seleccionada                                    | Tipo de Servicio / Rol              | Justificación Técnica                                                                                                                                        |
| :---------------------------------------- | :--------------------------------------------------------- | :---------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Frontend Framework**                    | **Next.js (React)**                                        | **PaaS (Vercel)**                   | Renderizado híbrido (SSR/SSG), arquitectura basada en componentes y rendimiento optimizado para e-commerce.                                                  |
| **Componentes de UI**                     | **shadcn/ui (Radix UI)**                                   | Librería Cliente                    | Componentes accesibles, modulares y personalizables para drawers de carrito flotante (`EP-ITC`), modales de acceso y filtros.                                |
| **Sistema de Estilos**                    | **Tailwind CSS 4**                                         | Librería Cliente                    | Maquetación responsiva nativa (RNF-USA-01) mediante clases de utilidad y diseño visual consistente.                                                          |
| **Iconografía**                           | **Lucide React**                                           | Librería Cliente                    | Conjunto unificado de íconos vectoriales para la interfaz (lupa, favoritos, bolsa de compra, tracking).                                                      |
| **Formularios y Validación**              | **React Hook Form + Zod**                                  | Librería Cliente                    | Gestión eficiente de formularios sin re-renders innecesarios y validación de esquemas tipados en TypeScript (`HU-GAC-REG`, `HU-TRX-DIR`).                    |
| **Alertas e Interacción (Toasts)**        | **Sonner**                                                 | Librería Cliente                    | Notificaciones emergentes para confirmaciones de adición al carrito, lista de favoritos y alertas de validación.                                             |
| **Gestión de Estado Global**              | **Zustand**                                                | Librería Cliente                    | Manejo ligero y reactivo del carrito flotante, filtros de vitrina y token de sesión.                                                                         |
| **Cliente HTTP Frontend**                 | **Axios + TanStack Query**                                 | Librería Cliente / DX               | Peticiones asíncronas optimizadas hacia los controladores de la API Interna de NestJS.                                                                       |
| **Backend de Aplicación**                 | **Node.js con NestJS**                                     | **PaaS (Render)**                   | Framework modular con TypeScript, controladores estrictamente tipados e inyección de dependencias.                                                           |
| **Cliente HTTP Backend & Mocks (Capa D)** | **`@nestjs/axios` (`HttpService`) + `axios-mock-adapter`** | Módulo Backend / DX                 | Wrapper oficial de NestJS sobre Axios para la comunicación con microservicios externos, con soporte para intercepción y respuestas simuladas en Hitos 1 a 3. |
| **Gestión de Configuración**              | **`@nestjs/config` (`ConfigService`) + `.env`**            | Módulo Backend / Config             | Carga e inyección centralizada de credenciales, cadenas de conexión y bandera `USE_MOCKS` por entorno (`.env.development` y `.env.production`).              |
| **ORM & BD Local**                        | **Prisma ORM + PostgreSQL**                                | **PaaS (Render DB) / Docker (Dev)** | Mapeo objeto-relacional tipado con migraciones automáticas para las 2 únicas tablas locales: `CartItem` y `WishlistItem`.                                    |
| **Notificaciones Email**                  | **React Email + Resend**                                   | **SaaS (API REST)**                 | Plantillas HTML en `.tsx` para confirmaciones de orden y despacho de correos en segundo plano (RNF-PER-03).                                                  |
| **CI/CD y Automatización**                | **GitHub Actions + semantic-release**                      | Pipeline DevOps                     | Pruebas unitarias/integración, versión semántica automática y despliegue continuo.                                                                           |
| **Diseño y Prototipado**                  | **Stitch AI**                                              | **SaaS Design (IA)**                | Generación asistida de prototipos UI/UX, wireframes y maquetación visual para React.                                                                         |

---

##### **3. Arquitectura Interna en Capas del Módulo**

La estructura lógica de la aplicación se divide en 4 capas totalmente desacopladas:

###### **A. Capa de Presentación e Interfaces de Entrada**

- **A.1. Presentación UI (Frontend Client — Next.js Framework):** Capa visual e interactiva que se ejecuta en el navegador del cliente, encargada de la experiencia de usuario (UX/UI) y del renderizado de las pantallas para las 7 épicas del módulo (`EP-GAC`, `EP-VEC`, `EP-DDP`, `EP-ITC`, `EP-TRX`, `EP-SHP` y `EP-SNT`).
    - **Ecosistema UI:** Maquetación basada en componentes responsivos utilizando **shadcn/ui** y **Tailwind CSS 4**, iconografía vectorial con **Lucide React**, validación estricta de formularios mediante **React Hook Form + Zod**, y alertas emergentes (_toasts_) con **Sonner**.
    - **Gestión de Estado y Peticiones:** Control del estado reactivo del carrito flotante y token de sesión con **Zustand**, y peticiones asíncronas HTTP mediante **Axios + TanStack Query** dirigidas a la API Interna de NestJS.
- **A.2. Capa de API / Controladores REST (Backend Entrypoint — NestJS):** Capa de interfaz HTTP en el servidor backend que actúa como la puerta de entrada oficial a la aplicación de NestJS.
    - **Controladores HTTP (`@Controller`):** Endpoints REST que reciben las solicitudes HTTP enviadas por el Frontend, aplican middlewares de autenticación (`AuthGuard` para tokens JWT) y validan los datos de entrada mediante DTOs (_Data Transfer Objects_).
    - **Desacoplamiento e Interfaz:** No contienen lógica de negocio; interpretan la petición del cliente, delegan la ejecución a los servicios de dominio (`CartService`, `CheckoutOrchestrator`) y devuelven la respuesta formateada en JSON con su correspondiente código de estado HTTP.

###### **B. Capa de Lógica de Negocio y Dominio (NestJS Services)**

- **Cart & Wishlist Service:** Administración de ítems, cálculo de subtotales en tiempo real, unificación de carritos anónimos al iniciar sesión y persistencia de favoritos.
- **Checkout Orchestrator:** Coordinación del flujo multipaso: revalidación asíncrona de stock pre-pago, empaquetado de la orden y transmisión a Ventas.
- **Notification Worker:** Event listener que procesa asíncronamente en segundo plano los eventos de orden creada para enviar correos transaccionales.

###### **C. Capa de Persistencia Local (Prisma ORM / PostgreSQL)**

- **Modelos Relacionales:** Exclusivamente 2 tablas locales gestionadas mediante **Prisma ORM**: `CartItem` (estado temporal del carrito) y `WishlistItem` (favoritos asociados de forma única al ID del cliente).
- **Gestión de Esquemas e Identidad:** Prisma ORM administra los esquemas de datos, clientes tipados en TypeScript y migraciones automatizadas tanto en el contenedor Docker local como en Render PostgreSQL.
- **Aislamiento de Persistencia:** Cero tablas locales para usuarios, claves, productos, precios, pedidos o despachos.

###### **D. Capa de Adaptadores API Externa, Mocks y Configuración (HttpService, Axios & Env)**

- **Clientes API (`@nestjs/axios` + `@nestjs/config`):** Encapsulación de llamadas HTTP salientes hacia los 4 microservicios externos mediante servicios adaptadores (`SecurityAdapterService`, `ProductsAdapterService`, `SalesAdapterService`, `DispatchAdapterService`). Estos adaptadores inyectan `HttpService` (`@nestjs/axios`) para ejecutar las peticiones HTTP/REST y `ConfigService` (`@nestjs/config`) para obtener dinámicamente las URLs base de las variables de entorno (`.env`).
- **Capa de Mocks (`axios-mock-adapter`):** Cuando `ConfigService` detecta `USE_MOCKS=true`, se activa `axios-mock-adapter` vinculado a la instancia Axios nativa (`httpService.axiosRef`). Esto intercepta las llamadas salientes en el servidor y devuelve las respuestas JSON simuladas del catálogo de contratos (`contratos-mocks-api.md`), garantizando autonomía total de desarrollo en los Hitos 1 a 3.
- **Capa Anti-Corrupción (ACL):** En el Hito 4 (`USE_MOCKS=false`), la transición hacia los microservicios reales se absorbe únicamente en las funciones de mapeo de los adaptadores, manteniendo fijos e intactos el Frontend en Next.js, los controladores internos y el modelo de datos local.

---

##### **4. Límites de Dominio, Ownership y Matriz de Integración**

###### **Principio de Propiedad de Entidades (Ownership)**

El sistema respeta de forma estricta los límites de responsabilidad de cada microservicio del ecosistema:

|Entidad de Datos|Módulo Dueño (_Owner_)|Rol del Canal Marketplace|
|:--|:--|:--|
|**Usuario / Credenciales**|**Seguridad y Usuarios**|Delegación total de sesión vía JWT (sin guardar claves).|
|**Producto / Stock / Precio**|**Productos y Ofertas**|Consulta del catálogo, filtros, ficha técnica y revalidación de stock.|
|**Pedido / Comprobantes**|**Ventas y Postventa**|Empaquetado de la orden tras el pago y visor de historial de compras.|
|**Despacho / Ruta**|**Despacho y Entrega a Domicilio**|Consulta del estado del paquete para la barra de seguimiento.|
|**Carrito temporal / Favoritos**|**Canal Marketplace**|Persistencia exclusiva en la base de datos PostgreSQL local.|

###### **Matriz Cruzada de Integración por APIs REST (Sin Acceso Directo a BD)**

Queda **estrictamente prohibido el acceso directo entre bases de datos de distintos módulos**:

1. **Marketplace \(\rightarrow\) Seguridad y Usuarios:** Registro de clientes, login y recuperación de contraseña.
2. **Marketplace \(\rightarrow\) Productos y Ofertas:** Búsqueda, catálogo, filtros, ficha técnica, promociones y revalidación de stock.
3. **Marketplace \(\rightarrow\) Ventas y Postventa:** Transmisión de la orden empaquetada tras la aprobación del pago y consulta del historial "Mis Pedidos".
4. **Marketplace \(\rightarrow\) Despacho y Entrega:** Consulta del progreso del envío en ruta para la barra de seguimiento.

---

##### **5. Estrategia de Entornos y Gestión de Variables (`.env`)**

Para mantener la paridad entre desarrollo local y producción Cloud, se utiliza el módulo `@nestjs/config` para la inyección y validación estricta de variables de entorno mediante archivos `.env`:

###### **A. Archivos de Configuración por Entorno (`.env`)**

- **Desarrollo Local (`.env.development`):**

```
NODE_ENV=development
PORT=3000
DATABASE_URL="postgresql://postgres:postgres_password@localhost:5432/marketplace_local_db?schema=public"
USE_MOCKS=true
SEC_SERVICE_URL="http://localhost:3000/api/mock/security"
PROD_SERVICE_URL="http://localhost:3000/api/mock/products"
SALES_SERVICE_URL="http://localhost:3000/api/mock/sales"
DISPATCH_SERVICE_URL="http://localhost:3000/api/mock/dispatch"
RESEND_API_KEY="re_dev_mock_key"
```

- **Producción Cloud (`.env.production` / Render Environment Variables):**

```
NODE_ENV=production
PORT=10000
DATABASE_URL="postgresql://user:pass@ep-xyz.render.com/marketplace_db?ssl=true"
USE_MOCKS=false
SEC_SERVICE_URL="https://security-module.onrender.com/api/v1"
PROD_SERVICE_URL="https://products-module.onrender.com/api/v1"
SALES_SERVICE_URL="https://sales-module.onrender.com/api/v1"
DISPATCH_SERVICE_URL="https://dispatch-module.onrender.com/api/v1"
RESEND_API_KEY="re_live_production_key"
```

###### **B. Entorno de Desarrollo Local (Docker Compose)**

- **Motor:** PostgreSQL 16 ejecutándose dentro de un contenedor Docker (`postgres:16-alpine`) para garantizar que todos los integrantes usen la misma versión y configuración.
- **Mocks de Integración:** Cuando `USE_MOCKS=true`, la capa de adaptadores activa **`axios-mock-adapter`** sobre `HttpService` para simular las respuestas de los 4 microservicios externos sin requerir conexión a otros servidores.
- **Ventajas:** Aislamiento total, reseteo rápido de datos para pruebas unitarias/integración (Hito 5) y cero instalaciones nativas pesadas en las computadoras del equipo.

###### **C. Entorno de Producción y Nube (Vercel + Render Cloud)**

- **Frontend:** Desplegado en **Vercel** mediante integración directa con la rama main de GitHub.
- **Backend:** Servicio web en **Render** ejecutando el contenedor/runtime de **NestJS**.
- **Base de Datos:** Instancia gestionada de **Render PostgreSQL**, conectada por variable de entorno cifrada `DATABASE_URL` con SSL activo.

---

##### **6. Atributos de Calidad y Requisitos No Funcionales (RNF)**

- **Seguridad (RNF-SEC):**
    - **Autenticación Delegada (RNF-SEC-01):** Sesión administrada con tokens JWT emitidos por Seguridad (sin tabla local de contraseñas).
    - **Protección Financiera (RNF-SEC-02):** Prohibición absoluta de guardar datos sensibles de tarjetas (número completo, CVV) en la base de datos local.
    - **Cifrado en Tránsito (RNF-SEC-03):** Comunicaciones protegidas mediante protocolo seguro HTTPS/TLS.
- **Rendimiento y Performance (RNF-PER):**
    - **Consulta Eficiente (RNF-PER-01):** Peticiones asíncronas optimizadas hacia Productos y Ventas.
    - **Filtro de Búsqueda (RNF-PER-02):** Restricción en la barra de búsqueda para consultas con menos de 2 caracteres.
    - **Notificaciones Asíncronas (RNF-PER-03):** Procesamiento de correos en segundo plano mediante eventos.
- **Usabilidad y UX/UI (RNF-USA):**
    - **Diseño Responsivo (RNF-USA-01):** Adaptable a móviles, tablets y escritorio apoyado por **Tailwind CSS 4** y **shadcn/ui**.
    - **Reactividad Dinámica (RNF-USA-02):** Actualización inmediata de subtotales, inventario, carrito flotante y notificaciones emergentes (**Sonner**) sin recarga completa de página (_page reload_).
    - **Estándar de Prototipado (RNF-USA-03):** Maquetación de la interfaz web fiel a los esquemas y wireframes visuales diseñados en **Stitch AI**.
- **Disponibilidad e Infraestructura (RNF-DIS):**
    - **Aislamiento de Persistencia (RNF-DIS-01):** Base de datos PostgreSQL dedicada exclusivamente para carrito y favoritos.
    - **Despliegue Cloud (RNF-DIS-03):** Ejecución operativa en entorno Nube (Vercel + Render).

---

##### **7. Estrategia de CI/CD y Matriz de Responsabilidades del Equipo**

###### **Pipeline de CI/CD (GitHub Actions + semantic-release)**

1. **Pull Request / Commit:** Ejecución automatizada de linter y pruebas unitarias en Next.js y NestJS.
2. **Build & Test:** Validación de compilación de TypeScript y pases de pruebas de integración.
3. **Semantic Release:** Análisis de commits convencionales para el cálculo de la versión semántica y generación automática del _changelog_.
4. **Automated Deploy:** Despliegue automático a Vercel (Frontend) y Render (Backend) tras el _merge_ a la rama principal.

###### **Distribución de Trabajo y Matriz de Roles (22 HU / 83 PH Total)**

|Integrante|Rol Técnico|PH|Épica Asignada|Responsabilidad Clave|
|:--|:--|:--|:--|:--|
|**Andrés**|DevOps / Security|11 PH|**EP-GAC** — Gestión de Accesos|Formulario Login/Registro, token JWT y pipeline CI/CD.|
|**Leo**|Arquitecto de Aplicación|13 PH|**EP-VEC** — Vitrina y Catálogo|Búsqueda, navegación, filtros dinámicos y ordenamiento.|
|**Jim**|Product Owner|11 PH|**EP-DDP** — Detalle y Disponibilidad|Ficha técnica, selección de variantes y validación de stock.|
|**Sebastián**|Documentador|11 PH|**EP-ITC** — Carrito y Favoritos|Carrito flotante, subtotales y BD local de favoritos.|
|**Giuliano**|UX/UI Designer|13 PH|**EP-TRX** — Transacción y Checkout|Checkout multipaso, prototipado en Stitch AI, simulación de pago y envío a Ventas.|
|**Diego**|JP / QA|11 PH|**EP-SHP** — Historial y Seguimiento|Visor "Mis Pedidos", opción Reorder y barra de tracking.|
|**Saire**|QA / Cloud|13 PH|**EP-SNT** — Notificaciones + Cloud|React Email, Resend y despliegue unificado en Vercel/Render.|
|**TOTAL**|**7 Integrantes**|**83 PH**|**22 Historias de Usuario**|**Solución Completa Canal Marketplace**.|

---

##### **8. Persistencia Relacional Local (`schema.prisma`)**

En cumplimiento del **Principio de Aislamiento de Persistencia (RNF-DIS-01)** y las reglas de **Ownership**, la base de datos relacional local en **PostgreSQL 16** administrada con **Prisma ORM** solo contendrá **2 tablas independientes**:

- **`CartItem` (`cart_items`):** Almacena el estado del carrito temporal para usuarios anónimos (`sessionId`) y clientes autenticados (`customerId`).
- **`WishlistItem` (`wishlist_items`):** Gestiona la lista de favoritos de manera persistente, vinculada de forma única al identificador del cliente (`customerId`).

_Nota: La especificación técnica completa del esquema Prisma se encuentra formalizada en el archivo `schema.prisma`._

---

##### **10. Capa Anti-Corrupción y Catálogo de Mocks (`contratos-mocks-api.md`)**

La **Capa D (Adaptadores)** en NestJS encapsula las peticiones salientes hacia los 4 microservicios externos mediante **`@nestjs/axios` (`HttpService`)**, utilizando **`axios-mock-adapter`** durante los Hitos 1 al 3 para simular los contratos de API REST:

- **Módulo de Seguridad y Usuarios (`EP-GAC`):** Autenticación y emisión de tokens JWT.
- **Módulo de Productos y Ofertas (`EP-VEC` / `EP-DDP`):** Consulta del catálogo, ficha técnica y revalidación de stock pre-pago.
- **Módulo de Ventas y Postventa (`EP-TRX` / `EP-SHP`):** Transmisión de la orden empaquetada e historial de compras.
- **Módulo de Despacho y Entrega (`EP-SHP`):** Seguimiento del paquete en ruta.

_Nota: La especificación completa de payloads, headers y esquemas JSON simulados se encuentra formalizada en el archivo `contratos-mocks-api.md`._