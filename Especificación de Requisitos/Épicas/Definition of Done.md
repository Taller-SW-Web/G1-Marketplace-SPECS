### 📋 **Definition of Done (DoD) — Versión Mejorada para el Canal Marketplace**

#### **1. Nivel Funcional, BDD y SDD** *(Validado por Product Owner: Jim / QA: Diego)*

- [ ] **Cumplimiento BDD (Gherkin):** Ejecución y paso satisfactorio del 100% de los escenarios *Dado-Cuando-Entonces* definidos en las Historias de Usuario.
- [ ] **Validación de Reglas de Negocio:** Verificación estricta del cumplimiento de las reglas de negocio asociadas a cada funcionalidad.
- [ ] **Trazabilidad SDD (Spec-Driven Development):** Documentación y trazabilidad entre la especificación en lenguaje natural, los prompts utilizados y el código generado mediante asistencia con IA.
- [ ] **Manejo de Excepciones:** Cobertura de rutas alternas, validación de campos obligatorios e indisponibilidades temporales de servicios.

#### **2. Nivel de Arquitectura, Seguridad y Microservicios** *(Validado por Arquitecto de Aplicación: Leo / DevOps: Andrés)*

- [ ] **Límites de Dominio (Ownership):** Cero acceso o consultas directas a las bases de datos de otros módulos (Seguridad, Productos, Ventas, Despacho).
- [ ] **Autenticación Delegada:** Sesión gestionada exclusivamente vía tokens JWT conectados al Módulo de Seguridad (sin almacenamiento local de credenciales/contraseñas).
- [ ] **Protección de Datos Financieros:** Prohibición absoluta de guardar datos sensibles de tarjetas (números completos, CVV) en la base de datos local.
- [ ] **Contratos de API REST / Mocks:** Integración asíncrona mediante endpoints REST o Mocks con contratos de interfaz definidos.
- [ ] **Aislamiento de Persistencia Local:** Uso exclusivo de la base de datos relacional local (PostgreSQL 16) para gestionar el estado temporal del carrito y la lista de favoritos.

#### **3. Nivel de UX/UI y Frontend React** *(Validado por UX/UI: Giuliano / Documentador: Sebastián)*

- [ ] **Fidelidad Stitch AI:** Maquetación en React conforme a los prototipos e interfaces diseñadas en Stitch AI.
- [ ] **Diseño Responsivo:** Interfaz adaptable y funcional en dispositivos móviles, tablets y monitores de escritorio.
- [ ] **Reactividad Dinámica (Sin Page Reload):** Actualización en tiempo real de subtotales, inventario, carrito flotante y filtros sin recarga completa de la página.

#### **4. Nivel de Código, CI/CD y Cloud** *(Validado por DevOps: Andrés / Cloud &amp; QA: Saire)*

- [ ] **Calidad de Código y Pruebas:** Pases de pruebas unitarias, de integración y rendimiento según la fase correspondiente del hito.
- [ ] **Repositorio y CI/CD:** Código versionado en el repositorio central del proyecto pasando los pipelines de integración continua.
- [ ] **Despliegue Cloud:** Funcionalidad desplegada y ejecutándose de forma operativa en el entorno de servidor en la Nube.

---

### 📊 **Matriz de Verificación Rápida por Épicas y Roles**


| Épica / Módulo                | Integrante Responsable | Rol Técnico                        | Verificación Clave Nivel 1 (Funcional / BDD)     | Verificación Clave Nivel 2 (Arquitectura / Seguridad)                         | Verificación Clave Nivel 3 (UX/UI React)         | Verificación Clave Nivel 4 (CI/CD / Cloud)                                 |
| :----------------------------- | :---------------------- | :---------------------------------- | :------------------------------------------------ | :----------------------------------------------------------------------------- | :------------------------------------------------ | :-------------------------------------------------------------------------- |
| **`EP-GAC`** Gest. Accesos    | **Andrés**             | DevOps                             | Gherkin `HU-GAC-REG`, `SES`, `REC`               | Token JWT capturado; cero almacenamiento local de claves                      | Formulario responsivo de Login/Registro          | Pipeline CI/CD base en GitHub                                              |
| **`EP-VEC`** Vitrina/Catálogo | **Leo**                | Arquitecto de Aplicación           | Gherkin `HU-VEC-BUS`, `FIL`, `ORD`               | Peticiones asíncronas a API Productos y Ofertas                               | Filtros laterales dinámicos y grilla de catálogo | Despliegue de servicio frontend en nube                                    |
| **`EP-DDP`** Detalle/Stock    | **Jim**                | Product Owner                      | Gherkin `HU-DDP-FIC`, `ATR`, `STK`               | Validar stock (&gt;0) con API Productos antes de añadir                       | Galería interactiva y selector de variantes      | Pruebas de carga en consulta de ficha                                      |
| **`EP-ITC`** Carrito          | **Sebastián**          | Documentador / Carrito             | Gherkin `HU-ITC-CAR`, `HU-ITC-RES`               | Persistencia en `CartItem` e integración con EP-FAV                           | Carrito y subtotales en tiempo real              | Versionado de migraciones de carrito                                       |
| **`EP-TRX`** Checkout/Pago    | **Giuliano**           | UX/UI                              | Gherkin `HU-TRX-DIR`, `PAG`, `ORD`               | Revalidación pre-pago y empaquetado de orden a Ventas                         | Formulario multipaso de envío y pago             | Validación de protocolo HTTPS/TLS                                          |
| **`EP-SHP`** Seguimiento      | **Diego**              | JP / QA                            | Gherkin `HU-SHP-HIS`, `DET`, `TRK`               | Visor de lectura consumiendo APIs de Ventas y Despacho                        | Barra de progreso de envío en tiempo real        | Pruebas de integración de lectura                                          |
| **`EP-SNT`** Notificaciones   | **Saire**              | QA / Cloud                         | Gherkin `HU-SNT-TMP`, `EML`, `DES`               | Microservicio asíncrono que escucha eventos de orden                          | Plantillas HTML responsivas con recomendaciones  | Entorno unificado Cloud y CI/CD completo                                   |
| **`EP-FAV`** Favoritos        | **Alonso**             | Backend                            | Gherkin `HU-FAV-GUA`, `HU-FAV-GES`, `HU-FAV-CAR` | `WishlistItem`, identidad del cliente y persistencia local                     | P9 y acciones de guardado en catálogo/ficha      | Pruebas de integración de favoritos en pipeline                            |

