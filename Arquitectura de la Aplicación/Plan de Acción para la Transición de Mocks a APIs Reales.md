Este plan establece los pasos ordenados para conmutar la simulación de `contratos-mocks-api-v3.md` hacia las integraciones reales con los 4 microservicios externos (Seguridad, Productos, Ventas y Despacho) durante el **Hito 4 (Semana 11)**, garantizando un impacto cero en el Frontend y en la base de datos local.

---

### **Fase 1: Auditoría y Mapeo de Diferencias (Pre-Conexión)**

1. **Recopilación de Especificaciones Oficiales:** Obtener los documentos Swagger/OpenAPI o colecciones de Postman definitivas publicadas por los equipos de Seguridad, Productos, Ventas y Despacho.

2. **Análisis de Discrepancias (_Diff Analysis_):**  Comparar endpoint por endpoint las APIs reales contra nuestro catálogo `contratos-mocks-api-v3.md`:
    - **Endpoints y Rutas:** Mapear variaciones en las URLs base o paths (ejemplo: `/api/v1/products` vs `/api/v2/catalogo`).
    - **Nombres de Atributos JSON:** Identificar diferencias de clave en el payload (ejemplo: `codProducto` \(\rightarrow\) `sku_id`, `precioOferta` \(\rightarrow\) `discount_price`).
    - **Encabezados HTTP:** Verificar la firma requerida para la autenticación delegada por token JWT (`Authorization: Bearer <token>`).

---

### **Fase 2: Actualización Encapsulada en el Backend (NestJS)**

3. **Ajuste de Mapeadores en la Capa D (Adaptadores NestJS):** Modificar **únicamente** las funciones de traducción/mapeo (`mapToInternalDTO()`) dentro de los 4 adaptadores del backend (`SecurityAdapter`, `ProductsAdapter`, `SalesAdapter`, `DispatchAdapter`).
    - _Garantía:_ Los controladores REST internos (`@Controller`) y los DTOs consumidos por Next.js no se modifican.
4. **Actualización del Archivo de Mocks de Respaldo (`v3` \(\rightarrow\) `v4`):** Actualizar `contratos-mocks-api-v3.md` con los esquemas reales para mantenerlo como un _fallback_ simulado en el entorno de desarrollo local y pruebas unitarias.
5. **Conmutación de Variables de Entorno (`.env`):**
    - Cambiar la bandera de control `USE_MOCKS=true` a `USE_MOCKS=false` en el panel de producción de Render.
    - Inyectar las URLs finales de los servidores Nube de los otros módulos (`SEC_SERVICE_URL`, `PROD_SERVICE_URL`, `SALES_SERVICE_URL`, `DISPATCH_SERVICE_URL`) a través de `@nestjs/config`.

---

### **Fase 3: Pruebas de Integración y Despliegue (Post-Conexión)**

6. **Ejecución de Pruebas E2E y Verificación del DoD:** Correr la suite de pruebas de integración para validar la respuesta asíncrona de los servicios externos y la cobertura de los códigos de estado HTTP (`200 OK`, `201 Created`, `400 Bad Request`, `404 Not Found`, `409 Conflict`, `503 Service Unavailable`).
7. **Verificación de Cero Impacto Interno:** Confirmar la estabilidad del sistema verificando que **no se haya cambiado una sola línea de código** en los componentes React de **Next.js**, los estados en **Zustand** ni en las 2 tablas relacionales de nuestra **Base de Datos Local PostgreSQL** (`CartItem` y `WishlistItem`).
8. **Despliegue Continuo (CI/CD):** Aprobar el Pull Request y realizar el merge a la rama principal (`main`) para que **GitHub Actions** ejecute la compilación y el despliegue automatizado hacia **Vercel** (Frontend) y **Render** (Backend) para la presentación del Hito 4.