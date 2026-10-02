# Spec UI — F-011 Visualizar ficha y galería del producto

> Documento de experiencia e interfaz de la zona descriptiva de la ficha de producto. Las regiones de precio, variantes, stock, carrito, favoritos y recomendaciones se integrarán mediante sus propias specs y no se definen aquí.

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID funcional | `F-011` |
| Nombre | Visualizar ficha y galería del producto |
| Versión | `0.1.0` |
| Estado | Aprobada para planificación; integración externa condicionada por `I-01`. |
| Spec funcional relacionada | `../funcional/F-011-detalle-producto.md` |
| Sistema de diseño aplicado | `DS-001-sistema-diseno-marketplace.md` versión `0.1.0` |
| Wireframe o prototipo | Pantalla 7 del documento histórico. El prototipo oficial deberá enlazarse desde Figma antes de aprobar esta spec. |
| Última actualización | `2026-09-27` |

## 2. Pantallas y rutas

| Pantalla | Ruta | Entrada | Salida o destino |
|---|---|---|---|
| Ficha de producto | `/productos/{slug}` | Tarjeta de Home, catálogo, productos relacionados o enlace directo. | Catálogo, ficha de otro producto o zonas de acciones definidas por otras funcionalidades. |
| Visor ampliado de galería | Misma ruta; diálogo modal no navegable por URL propia. | Activar imagen principal o control “Ampliar imagen”. | Cerrar y retornar el foco a la imagen/control de origen. |
| Producto no disponible | `/productos/{slug}` | Slug no encontrado, inactivo, privado o descontinuado. | `/catalogo` mediante “Volver al catálogo”. |
| Error recuperable | `/productos/{slug}` | Fallo de red, tiempo de espera o respuesta inválida. | Reintentar en la misma ruta o `/catalogo`. |

## 3. Estructura visual

Esta pantalla aplica el patrón **Ficha de producto** y los componentes `ProductGallery`, `Breadcrumb`, `Skeleton`, `Alert` y `Button` definidos en `DS-001`. No define colores, tipografías, espaciados ni anatomía base fuera de ese sistema.

```text
Ficha de producto
├── Cabecera global del canal
├── Migas de navegación
├── Región principal
│   ├── Galería
│   │   ├── Imagen principal / imagen de respaldo
│   │   ├── Control de ampliar
│   │   ├── Controles anterior y siguiente
│   │   └── Lista de miniaturas
│   └── Resumen descriptivo
│       ├── Marca
│       ├── Nombre del producto (H1)
│       ├── Descripción
│       └── Región reservada para F-012 a F-016 y F-036
├── Especificaciones técnicas
│   └── Grupos y pares nombre/valor
└── Pie global del canal

Visor ampliado
├── Diálogo modal con nombre accesible
├── Imagen ampliada y texto alternativo
├── Indicador de posición “Imagen X de Y”
├── Controles anterior/siguiente, si hay más de una imagen
└── Botón Cerrar
```

La región reservada no debe presentarse como un control deshabilitado ni como información ficticia. Las capacidades dependientes se integran sólo con sus specs aprobadas (`F-012` a `F-016` y `F-036`); si una capacidad no está disponible en una entrega, su región se omite sin dejar controles ni datos ficticios.

## 4. Componentes y contenido

| Componente | Contenido | Acción | Visibilidad |
|---|---|---|---|
| Migas de navegación | `Inicio / Catálogo / Nombre del producto`. | Inicio y Catálogo son enlaces; el producto actual no es enlace. | Ficha lista. |
| Galería principal | Imagen seleccionada, texto alternativo y posición. | Abrir visor ampliado. | Con ficha válida; usa respaldo sólo si una imagen válida no puede descargarse en el navegador. |
| Miniaturas | Una miniatura por imagen válida, con indicador de selección. | Cambiar imagen principal. | Dos o más imágenes. |
| Controles anterior/siguiente | Flechas con etiqueta accesible. | Cambiar imagen seleccionada. | Dos o más imágenes. |
| Marca | Nombre de la marca. | Sin acción dentro de `F-011`. | Cuando el proveedor entrega marca válida. |
| Título | Nombre del producto en `h1`. | Sin acción. | Ficha lista. |
| Descripción | Texto sanitizado y legible. | Expandir/contraer sólo si supera el límite visual acordado; conserva acceso al texto completo. | Cuando existe descripción. |
| Especificaciones | Grupo, nombre y valor técnico. | Expandir/contraer grupos en móvil cuando haya más de un grupo. | Cuando existe al menos una especificación válida. |
| Estado de respaldo de imagen | Ilustración neutra, texto “Imagen no disponible”. | Seleccionar otra miniatura válida, si existe. | La imagen seleccionada no puede descargarse en el navegador. |
| Estado no disponible | Título, explicación neutra y botón “Volver al catálogo”. | Navegar a `/catalogo`. | Producto no encontrado/no elegible. |
| Estado de error | Mensaje “No pudimos cargar este producto”, botón “Reintentar” y enlace al catálogo. | Reintentar o navegar. | Error recuperable. |

## 5. Estados de la interfaz

| Estado | Cuándo aparece | Elementos visibles | Acción disponible |
|---|---|---|---|
| Cargando inicial | Se abrió una ficha sin datos disponibles. | Skeleton de galería, marca, título, descripción y especificaciones; sin datos ficticios. | Volver al catálogo permanece disponible si la cabecera ya cargó. |
| Éxito con galería | Producto válido con una o más imágenes. | Contenido descriptivo, galería principal, miniaturas y controles según corresponda. | Seleccionar, navegar y ampliar imágenes. |
| Respaldo de imagen | Una imagen de una respuesta válida no puede mostrarse en el navegador. | Imagen de respaldo, contenido textual y miniaturas restantes si existen. | Seleccionar otra imagen disponible. |
| Éxito sin especificaciones | Producto válido sin pares técnicos publicables. | Galería, marca, título y descripción; sin bloque vacío de especificaciones. | Acciones de galería. |
| Imagen secundaria fallida | Una imagen no puede mostrarse. | Imagen principal actual, miniatura marcada como no disponible y demás medios. | Navegar por imágenes restantes. |
| Producto no disponible | API devuelve no encontrado/no elegible. | Ilustración neutra, título y botón de retorno. | Volver al catálogo. |
| Error recuperable | Error de red, `5xx` o respuesta no válida. | Mensaje claro, botón Reintentar y enlace al catálogo. | Reintentar o volver. |
| Visor ampliado | El visitante abre una imagen válida. | Modal, imagen, contador, controles y cerrar. | Navegar, cerrar con botón, Escape o fondo si el patrón visual lo permite. |

## 6. Interacciones y navegación

1. Seleccionar una tarjeta de producto o un enlace directo → abrir `/productos/{slug}` y mostrar el estado de carga.
2. Seleccionar una miniatura → actualizar imagen principal, texto alternativo, indicador de selección y posición; no reiniciar la página.
3. Presionar anterior/siguiente en galería → cambiar a la imagen previa/siguiente. En el primer o último elemento, el control correspondiente se deshabilita; no hay carrusel infinito.
4. Presionar imagen principal o “Ampliar imagen” → abrir el visor modal en la imagen seleccionada.
5. Presionar Escape, Cerrar o el fondo habilitado del modal → cerrar el visor y devolver foco al control que lo abrió.
6. Seleccionar Inicio o Catálogo en migas → navegar a la ruta correspondiente.
7. Seleccionar “Volver al catálogo” desde no disponible/error → navegar a `/catalogo` sin conservar un slug inválido.
8. Seleccionar “Reintentar” → repetir únicamente la consulta de `F-011`; no desencadenar precio, stock, variantes ni otras llamadas fuera de alcance.

## 7. Formularios y validaciones visuales

No hay formularios ni entradas editables en `F-011`.

| Elemento | Tipo | Obligatorio | Validación | Resultado visual |
|---|---|---:|---|---|
| `slug` de la ruta | Parámetro no editable | Sí | Si no cumple formato o la API lo rechaza, no se carga contenido. | Estado “Producto no disponible”. |
| Imagen seleccionada | Control de galería | No | Debe corresponder a un medio válido recibido. | Miniatura activa con indicador no basado sólo en color. |

## 8. Responsive y accesibilidad

- **Desktop (≥ 1024 px):** dos columnas en la región principal. Galería a la izquierda y resumen descriptivo a la derecha. Las miniaturas se muestran en columna o fila sin ocultar su estado seleccionado.
- **Tablet (768–1023 px):** dos columnas flexibles o galería sobre resumen cuando el ancho no permite conservar legibilidad; las especificaciones ocupan el ancho disponible debajo.
- **Mobile (< 768 px):** una columna. Galería primero, miniaturas en desplazamiento horizontal con controles alternativos; el visor utiliza todo el ancho útil sin cortar controles. Ningún gesto de deslizamiento es la única forma de navegar.
- **Teclado:** Tab recorre migas, galería, controles, miniaturas y enlaces en orden lógico. Flechas sólo cambian imagen cuando el foco está dentro del control de galería documentado. El modal atrapa el foco y Escape lo cierra.
- **Lectores de pantalla:** `h1` único; marca y descripción con estructura semántica; galería anunciada con posición; miniaturas son botones con estado `aria-pressed`; los errores se anuncian mediante región `role=status` o `role=alert` según severidad.
- **Contraste y tamaño:** texto y controles cumplen WCAG 2.2 AA; objetivo táctil mínimo de 44 × 44 px para controles principales; selección, error y estado deshabilitado nunca dependen sólo del color.
- **Movimiento:** el cambio de imagen no reproduce animación obligatoria; respeta la preferencia de movimiento reducido del dispositivo.
- **Imágenes:** reservan espacio para evitar saltos de diseño; cada medio tiene alternativa textual útil o la alternativa de respaldo definida en la spec funcional.

## 9. Criterios de aceptación UI

- [ ] **UI-F011-01:** Durante la carga inicial se muestran skeletons que reflejan la estructura final y no precios, stock ni datos inventados.
- [ ] **UI-F011-02:** En escritorio la galería y el resumen descriptivo se muestran sin superposición; en móvil se reorganizan en una sola columna sin perder controles.
- [ ] **UI-F011-03:** Con dos o más imágenes, la miniatura activa se distingue visualmente y de forma accesible; los controles previo/siguiente se deshabilitan en los extremos.
- [ ] **UI-F011-04:** Al abrir el visor ampliado, el foco queda dentro del diálogo; al cerrarlo, vuelve al elemento que lo abrió.
- [ ] **UI-F011-05:** Cuando una imagen no puede descargarse, se presenta la imagen de respaldo con el texto “Imagen no disponible”, pero no se ocultan título, marca, descripción ni especificaciones válidas.
- [ ] **UI-F011-06:** Cuando no hay especificaciones, no se renderiza un acordeón, tabla o título vacío.
- [ ] **UI-F011-07:** El estado de producto no disponible no diferencia si el producto no existe, fue retirado o no está habilitado; ofrece una única acción clara al catálogo.
- [ ] **UI-F011-08:** El estado de error permite reintentar y anuncia el resultado a tecnologías asistivas.
- [ ] **UI-F011-09:** La interfaz de `F-011` no contiene controles activos de precio, oferta, variante, stock, carrito, favoritos o recomendaciones antes de que se aprueben sus specs respectivas.
- [ ] **UI-F011-10:** Toda imagen y todo control de galería es operable por teclado y posee un nombre accesible.

## 10. Fuentes y decisiones pendientes

- Fuente: Pantalla 7 de `Wireframes y Prototipo/Especificación de pantallas del canal.md`.
- Fuente: `F-011` del catálogo de funcionalidades y la spec funcional relacionada.
- Fuente: `../specs-depreciadas/SPEC-03-EP-DDP-Detalle-y-Disponibilidad-Producto.md` como referencia histórica; sus regiones de precio, variantes, stock y recomendados se separaron en funcionalidades distintas.
- Pendiente: crear y enlazar el prototipo oficial de la Pantalla 7 en Figma.
- Pendiente `I-01` / `OPEN-03`: homologar la ruta, autenticación de canal y payload OpenAPI de Productos y Ofertas. Las reglas de producto activo, imágenes y atributos ya fueron confirmadas en sus specs y modelo conceptual.
