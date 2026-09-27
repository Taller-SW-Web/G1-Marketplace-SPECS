# Spec funcional — F-011 Visualizar ficha y galería del producto

> Documento de comportamiento. Define la consulta y presentación de la información descriptiva oficial de un producto, sin incluir precio, variantes, stock, carrito, favoritos ni recomendaciones.

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID | `F-011` |
| Nombre | Visualizar ficha y galería del producto |
| Versión | `0.1.0` |
| Estado | Aprobada para planificación; integración externa condicionada por `I-01`. |
| Última actualización | `2026-09-27` |
| Especificaciones relacionadas | UI y contrato API `F-011-detalle-producto.md` |

## 2. Objetivo y alcance

### Objetivo

Permitir que cualquier visitante consulte una ficha confiable de un producto comercialmente disponible, con su identidad, marca, descripción, especificaciones técnicas y galería de imágenes. La ficha debe ayudar a evaluar el producto antes de continuar con las capacidades de precio, variantes, disponibilidad y compra.

### Incluye

- Acceso desde una tarjeta del catálogo, un producto destacado, un producto relacionado o una URL directa con slug.
- Consulta de producto comercial activo al Módulo de Productos y Ofertas mediante la API de Marketplace.
- Visualización de nombre, marca, descripción, especificaciones técnicas estructuradas y galería de imágenes.
- Selección de miniatura, navegación de galería y ampliación de imagen.
- Estados de carga, producto no disponible, galería incompleta y fallo recuperable de consulta.

### No incluye

- Precio regular, oferta, descuento o cupón (`F-012`, `F-024`).
- Selección de talla, color u otros atributos comprables (`F-013`).
- Consulta o reserva de inventario (`F-014`).
- Productos relacionados (`F-015`).
- Agregar al carrito (`F-016`) o gestionar cantidades.
- Agregar a favoritos (`F-036`).
- Edición de información de producto o administración de catálogo.

## 3. Actores y permisos

| Actor | Permisos en esta funcionalidad |
|---|---|
| Visitante no autenticado | Consultar fichas de productos comercialmente activos y usar la galería. |
| Cliente autenticado | Mismos permisos que un visitante. La identidad no modifica la información de esta ficha. |
| Módulo Productos y Ofertas | Publicar la información autoritativa del producto y sus medios. |
| Personal administrativo de Productos y Ofertas | Gestionar el catálogo fuera del alcance de Marketplace. |

No se requiere sesión para consultar una ficha. Marketplace no concede acceso a productos inactivos, privados, inexistentes o descontinuados.

## 4. Conceptos y datos involucrados

| Concepto | Descripción | Datos relevantes | Dueño |
|---|---|---|---|
| Producto comercial | Artículo visible y elegible para un canal de venta. | `productId`, `slug`, nombre, estado comercial. | Productos y Ofertas |
| Marca | Identidad comercial asociada al producto. | `brandId`, nombre de marca. | Productos y Ofertas / Taxonomía |
| Descripción | Información textual para comprender el producto. | resumen y descripción detallada. | Productos y Ofertas |
| Especificación técnica | Atributo descriptivo no orientado a la selección de una variante. | grupo, nombre, valor y unidad opcional. | Productos y Ofertas |
| Medio de galería | Imagen asociada y ordenada para presentar el producto. | `mediaId`, URL, texto alternativo, orden, tipo. | Productos y Ofertas |
| `slug` | Identificador legible de la URL pública. | minúsculas, números y guiones. | Productos y Ofertas |

Marketplace no crea una tabla local de productos, marcas, especificaciones ni imágenes. Puede usar caché técnica temporal conforme al contrato, sin transformarla en una fuente de verdad.

## 5. Reglas de negocio

- **RN-F011-01 — Fuente autoritativa:** nombre, marca, descripción, especificaciones y medios deben provenir exclusivamente de Productos y Ofertas o de su capa de taxonomía autorizada. No se consultan bases de datos externas de forma directa.
- **RN-F011-02 — Elegibilidad comercial:** sólo se presenta una ficha cuando el producto está activo y habilitado para el canal Marketplace. Un recurso inexistente, inactivo, privado o descontinuado se trata como no disponible para el visitante.
- **RN-F011-03 — Separación de responsabilidades:** la ficha de `F-011` no muestra ni calcula precio, promociones, variantes, stock, recomendaciones, carrito o favoritos. Esas áreas se integrarán mediante sus propias specs en la misma pantalla.
- **RN-F011-04 — URL canónica:** cada producto se consulta por un slug canónico. Un slug inválido, no encontrado o que ya no corresponde a un producto disponible no revela información interna.
- **RN-F011-05 — Galería ordenada y obligatoria:** un producto comercial activo ya fue validado por Catálogo con al menos una imagen. Las imágenes se muestran según el orden entregado por el módulo dueño y la primera válida es la principal inicial. Una respuesta de producto activo sin imágenes es inválida, no un producto exitoso sin galería.
- **RN-F011-06 — Accesibilidad del medio:** cada imagen debe contar con texto alternativo útil. Si el proveedor no lo entrega, Marketplace genera un texto de respaldo con nombre del producto, marca y posición; nunca deja un control de galería sin nombre accesible.
- **RN-F011-07 — Contenido seguro:** descripción y especificaciones se muestran como contenido sanitizado. Marketplace no ejecuta HTML, scripts ni URLs no confiables recibidas como contenido de catálogo.
- **RN-F011-08 — Actualidad:** la información mostrada es informativa y puede cambiar en Productos y Ofertas. La ficha no promete precio ni disponibilidad porque se obtienen en funcionalidades posteriores.

## 6. Comportamiento funcional

### Precondiciones

- El visitante llega desde una entrada que contiene un slug de producto o escribe una URL directa válida.
- La API de Marketplace puede consultar el contrato de catálogo de Productos y Ofertas, o dispone de una respuesta temporal de caché permitida.
- No se requiere autenticación.

### Flujo principal

1. El visitante selecciona un producto desde una entrada habilitada o abre `/productos/{slug}`.
2. Marketplace valida la forma del slug y solicita la información descriptiva de la ficha.
3. Productos y Ofertas responde un producto comercialmente activo con identidad, marca, contenido técnico y medios ordenados.
4. Marketplace presenta el nombre, marca, descripción, especificaciones y la primera imagen válida como imagen principal.
5. El visitante puede seleccionar una miniatura, avanzar o retroceder por las imágenes y ampliar la imagen seleccionada.
6. Si existen zonas de pantalla pertenecientes a otras funcionalidades, se mantienen como espacio reservado o se cargan de forma independiente; la ficha descriptiva continúa disponible.

### Flujos alternativos y errores

| ID | Situación | Comportamiento esperado |
|---|---|---|
| ALT-F011-01 | Una imagen válida en la respuesta no puede descargarse en el navegador. | Se muestra un contenedor de galería con imagen de respaldo y texto “Imagen no disponible”. La ficha textual sigue disponible; este estado no implica que Catálogo haya publicado el producto sin imágenes. |
| ALT-F011-02 | El producto no posee especificaciones técnicas publicables. | Se muestra la descripción; la sección de especificaciones se oculta y no se presenta como error. |
| ALT-F011-03 | Una imagen secundaria no puede descargarse. | La miniatura indica que no está disponible; se mantiene la imagen principal anterior y el usuario puede navegar por las demás imágenes. |
| ALT-F011-04 | El visitante abre la ficha desde un enlace directo válido. | Se ejecuta el mismo flujo principal, sin exigir que provenga del catálogo. |
| ERR-F011-01 | El slug tiene formato inválido. | Marketplace no consulta al proveedor y presenta “No pudimos encontrar este producto”, con acceso para volver al catálogo. |
| ERR-F011-02 | El producto no existe, está inactivo o no está habilitado para Marketplace. | Se presenta el estado “Producto no disponible” sin distinguir el motivo interno; se ofrece volver al catálogo. |
| ERR-F011-03 | Productos y Ofertas no responde o responde fuera de tiempo. | Se presenta un error recuperable, se conserva el slug solicitado y se ofrece “Reintentar” y “Volver al catálogo”. |
| ERR-F011-04 | La respuesta del proveedor es incompleta, no pasa validación o declara un producto activo sin imágenes. | Marketplace no muestra contenido parcial engañoso; registra el incidente técnico y presenta el mismo error recuperable. |

### Estados

| Estado | Cuándo aplica | Transiciones permitidas |
|---|---|---|
| `LOADING` | Se solicitó la ficha y aún no hay respuesta válida. | `READY`, `NOT_AVAILABLE`, `ERROR`. |
| `READY` | Existe producto comercial activo con contenido mínimo válido. | `LOADING` al reintentar o cambiar de slug; `ERROR` si una actualización falla. |
| `MEDIA_FALLBACK` | La ficha es válida, pero el navegador no puede descargar la imagen seleccionada. | `READY` al seleccionar o cargar correctamente otro medio; mantiene el respaldo si todos fallan. |
| `NOT_AVAILABLE` | El proveedor informa ausencia o no elegibilidad. | `LOADING` al abrir otro slug; salida al catálogo. |
| `ERROR` | No fue posible obtener o validar la ficha. | `LOADING` al reintentar; salida al catálogo. |

## 7. Validaciones

| Campo o condición | Regla | Mensaje o resultado |
|---|---|---|
| `slug` de ruta | 1 a 120 caracteres; letras minúsculas sin tildes, números y guiones; sin espacios, `/`, `?`, `#` ni secuencias `..`. | Respuesta `400 INVALID_PRODUCT_SLUG` y estado “Producto no disponible”. |
| Producto recibido | Debe incluir `productId`, `slug`, nombre no vacío y estado comercial activo. | Si falta o no cumple, no se muestra la ficha; se responde error recuperable o no disponible según el origen. |
| Medio | Debe ser tipo imagen, URL HTTPS permitida y orden entero no negativo. La respuesta de producto activo requiere al menos un medio válido. | Se descarta el medio inválido; si no queda ninguno, se trata como respuesta inválida del proveedor. |
| Especificación | Nombre y valor no vacíos después de sanitizar; longitud máxima definida por el contrato. | Se omite la fila inválida; si no queda ninguna, se oculta la sección. |
| Contenido textual | No ejecutable y sanitizado antes de presentar. | Se muestra texto seguro; contenido inválido se trata como respuesta incompleta. |

## 8. Criterios de aceptación

- [ ] **CA-F011-01:** Dado un slug de producto activo válido, cuando un visitante abre la ficha, entonces visualiza nombre, marca, descripción y galería sin iniciar sesión.
- [ ] **CA-F011-02:** Dado un producto con especificaciones técnicas válidas, cuando carga la ficha, entonces se muestran como pares de nombre y valor, agrupados si el proveedor indica un grupo.
- [ ] **CA-F011-03:** Dado un producto con tres imágenes ordenadas, cuando carga la ficha, entonces la primera es la principal y el visitante puede seleccionar cualquiera de las otras sin recargar toda la página.
- [ ] **CA-F011-04:** Dado que el visitante usa los controles siguiente/anterior de la galería, cuando llega al extremo, entonces la navegación se mantiene dentro de las imágenes disponibles según el comportamiento definido en UI.
- [ ] **CA-F011-05:** Dado que una imagen válida de la respuesta no puede descargarse en el navegador, cuando se intenta presentarla, entonces se muestra una galería de respaldo y la información textual permanece accesible.
- [ ] **CA-F011-06:** Dado un slug inexistente, inactivo o descontinuado, cuando Marketplace solicita la ficha, entonces se muestra un único estado “Producto no disponible” y una acción para volver al catálogo, sin exponer la causa interna.
- [ ] **CA-F011-07:** Dado un fallo temporal del proveedor, cuando la consulta no puede completarse, entonces se muestra una acción de reintento y no se presenta información técnica parcial como si fuese completa.
- [ ] **CA-F011-08:** Dado que la ficha se muestra correctamente, entonces no presenta precios, descuentos, selectores de variante, stock, recomendaciones, carrito ni favoritos como parte del alcance de `F-011`.
- [ ] **CA-F011-09:** Dado cualquier imagen de la galería, cuando un lector de pantalla la anuncia, entonces recibe un texto alternativo útil o el respaldo definido por esta spec.
- [ ] **CA-F011-10:** Dado contenido recibido desde catálogo, cuando contiene marcado o URL no permitidos, entonces Marketplace no ejecuta contenido activo.

## 9. Restricciones y requisitos de calidad

- **Seguridad:** el endpoint es público sólo para productos comerciales activos; no expone estados internos, costos, identificadores de infraestructura ni contenido no sanitizado.
- **Rendimiento:** la respuesta de ficha debe estar disponible para renderizar contenido principal en un objetivo de p95 ≤ 2 s bajo condiciones normales de integración. La galería debe usar carga diferida para medios no seleccionados.
- **Disponibilidad:** si Productos y Ofertas falla, se ofrece recuperación explícita; una caché técnica sólo puede servir contenido dentro de la política de frescura acordada y nunca cambia ownership.
- **Accesibilidad:** navegación completa por teclado, foco visible, textos alternativos, controles con nombre accesible, diálogo de zoom modal accesible y contraste conforme a WCAG 2.2 AA.
- **Compatibilidad:** la ficha funciona en la versión vigente de navegadores móviles y de escritorio definida por el proyecto; no depende de hover para acceder a información o controles esenciales.
- **Observabilidad:** cada fallo de integración registra `requestId`, slug, código de error y latencia, sin registrar tokens ni datos personales.

## 10. Dependencias e integraciones

| Dependencia | Motivo | Tipo | Estado |
|---|---|---|---|
| Productos y Ofertas — catálogo | Proporciona producto, marca, descripción, especificaciones y medios. | REST síncrono vía adaptador de Marketplace. | Semántica documentada; ruta OpenAPI pendiente (`I-01`). |
| Productos y Ofertas — taxonomía | Puede resolver nombre de marca si catálogo entrega sólo `brandId`. | REST síncrono vía adaptador. | Pendiente de homologar junto a `I-01`. |
| API de Marketplace | Expone una respuesta estable y reducida al frontend. | REST síncrono. | Definida en la spec de contrato API de `F-011`. |

## 11. Fuentes y decisiones pendientes

- Fuente: `Almacen de Contexto/ANALISIS-FASE-2.md`, catálogo `F-011`.
- Fuente: `Wireframes y Prototipo/Especificación de pantallas del canal.md`, Pantalla 7.
- Fuente: `Productos-y-Ofertas-docs/Contrato_Api.md`, EXT-OUT-CAT-01 y EXT-OUT-CAT-02.
- Fuente: `Productos-y-Ofertas-docs/specs/SPEC-003-gestion-productos-crud.md`, reglas de activación y consulta de productos activos para canales.
- Fuente: `Productos-y-Ofertas-docs/Modelo_Conceptual.md`, relación Producto–Imagen y atributos vigentes.
- Fuente: `Arquitectura de la Aplicación/Base de Datos/01-Modelo-logico-inicial.md` y `03-Decisiones-y-brechas-de-integracion.md`.
- Pendiente `I-01` / `OPEN-03`: Productos y Ofertas debe homologar la ruta HTTP, autorización de canal y payload OpenAPI definitivo. La semántica del contenido ya está confirmada: producto activo, slug, atributos vigentes e imágenes obligatorias. Esta pendiente no impide revisar el comportamiento ni el contrato BFF de Marketplace, pero sí impide implementación integrada.
