# Vista — V-005 Inicio

> Página pública de entrada al Marketplace para descubrir categorías y productos destacados, buscar productos y acceder a las áreas globales del canal.

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID | `V-005` |
| Nombre | Inicio |
| Ruta | `/` |
| Versión | `0.1.0` |
| Estado | En revisión |
| Responsable | Leonidas Garcia |
| Revisor | Giuliano Macchiavello |
| Sistema de diseño | [`DS-001`](../DS-001-sistema-diseno-marketplace.md) |
| Enlace de Figma | Pendiente |

## 2. Propósito, actor y acceso

- **Objetivo del usuario:** orientarse, descubrir categorías o productos destacados y comenzar una búsqueda o compra.
- **Actor principal:** visitante o cliente autenticado.
- **Permiso:** público.
- **Condiciones de entrada:** URL principal, logo de la cabecera, retorno desde un flujo o CTA “Seguir comprando”.
- **Resultado esperado:** navegación hacia `V-006` o `V-007`, o acceso a carrito, favoritos, pedidos y cuenta según el estado de sesión.

## 3. Trazabilidad

| Funcionalidad | Spec funcional | Spec UI de origen | Aporte a esta vista |
|---|---|---|---|
| `F-006` | [`F-006 Inicio, categorías y destacados`](../../funcional/F-006-inicio-categorias-destacados.md) | [`UI F-006`](../F-006-inicio-categorias-destacados.md) | Hero, categorías activas, productos destacados y degradación por sección. |
| `F-036` | [`F-036 Agregar favorito`](../../funcional/F-036-agregar-favorito.md) | [`UI F-036`](../F-036-agregar-favorito.md) | Control de favorito en `ProductCard`, autenticación y feedback. |

Contratos consultados: [`API F-006`](../../contrato-api/F-006-inicio-categorias-destacados.md) y [`API F-036`](../../contrato-api/F-036-agregar-favorito.md).

## 4. Entradas, salidas y conservación de contexto

| Origen o acción | Destino | Condición | Contexto que se conserva |
|---|---|---|---|
| Logo o URL principal | `V-005` | Cualquier usuario | Sesión y carrito. |
| Búsqueda enviada | `V-006` | Término válido según F-007 | Consulta ingresada. |
| Categoría seleccionada | `V-006` | Categoría activa | Filtro de categoría y origen. |
| Producto destacado | `V-007` | Producto activo con slug válido | Origen para volver y posición cuando sea viable. |
| Carrito en cabecera | `V-008` | Cualquier usuario | Carrito y sesión. |
| Favoritos en cabecera | `V-009` | Cliente autenticado | Sesión. Sin sesión se activa `O-003`. |
| Mis pedidos | `V-015` | Cliente autenticado | Sesión. Sin sesión se activa `O-003`. |
| Iniciar sesión / cuenta | `V-001` o menú de cuenta | Según sesión | Ruta de retorno interna. |

## 5. Jerarquía y composición visual

```text
V-005 Inicio
├── Cabecera global
│   ├── Logo
│   ├── Buscador
│   ├── Navegación de categorías
│   └── Cuenta, favoritos y carrito con contadores
├── Contenido principal
│   ├── Hero editorial/comercial
│   ├── Accesos a categorías activas
│   └── Productos destacados
│       └── ProductCard × N
└── Pie global
```

| Región | Componente o contenido | Prioridad | Comportamiento |
|---|---|---|---|
| Cabecera | Logo, búsqueda y accesos globales | Primaria | Permanece coherente con `V-006` y `V-007`; puede compactarse al desplazarse sin ocultar acciones esenciales. |
| Hero | Mensaje, imagen y CTA editorial | Primaria | Un CTA inequívoco; no depende de carrusel automático. |
| Categorías | Imagen/icono, nombre y enlace | Primaria | Sólo categorías activas; número y orden definidos por catálogo/editorial. |
| Destacados | `ProductCard` completa | Primaria | Sólo productos activos con imagen, slug y datos comerciales completos. |
| Pie | Ayuda, políticas y navegación secundaria | Secundaria | No duplica la acción primaria del hero. |

Una sección sin datos se omite completamente, incluyendo su título y espacio reservado. La ausencia de categorías o destacados no bloquea la cabecera, búsqueda ni navegación restante.

## 6. Contenido y acciones

| Elemento | Texto o dato | Acción | Condición de visibilidad |
|---|---|---|---|
| Logo | Variante oficial aprobada | Volver a `V-005` | Siempre. |
| Buscador | Etiqueta accesible “Buscar productos” | Abrir resultados en `V-006` | Siempre. |
| Acceso de cuenta | “Iniciar sesión” o menú del cliente | Abrir acceso/cuenta | Según sesión. |
| Favoritos | Icono + etiqueta + contador cuando exista | Abrir `V-009` o `O-003` | Siempre; estado según sesión. |
| Carrito | Icono + etiqueta + cantidad | Abrir `V-008` | Siempre. |
| Hero | Título, apoyo, recurso visual y CTA | Abrir destino editorial permitido | Cuando exista contenido aprobado; no inventar promoción. |
| Categoría | Nombre e imagen/icono | Abrir `V-006` filtrada | Categoría activa. |
| Producto | Imagen, marca, nombre, precio y oferta si aplica | Abrir `V-007` | Tarjeta comercial completa. |
| Favorito de producto | “Guardar en favoritos” / “Quitar de favoritos” | Ejecutar F-036 o activar `O-003` | En cada tarjeta válida. |

## 7. Estados de la vista

| Estado | Disparador | Cambios visibles | Acción o recuperación | Frame requerido |
|---|---|---|---|---|
| Principal público | Datos disponibles sin sesión | Inicio completo y acciones públicas | Explorar/iniciar sesión | Sí |
| Principal autenticado | Datos disponibles con sesión | Cuenta, favoritos y contadores personalizados | Explorar áreas privadas | Sí |
| Cargando | Solicitud inicial | Skeleton independiente para categorías y productos; cabecera operativa | Esperar/navegar | Sí |
| Categorías vacías | `categories: []` | Sección omitida; destacados permanecen | Explorar destacados/buscar | No; anotar en frame principal |
| Destacados vacíos | `featuredProducts: []` | Sección omitida; categorías permanecen | Explorar categorías/buscar | No; anotar en frame principal |
| Inicio sin contenido | Ambos arreglos vacíos | Orientación breve y CTA a `V-006`; navegación global operativa | Explorar catálogo | Sí |
| Catálogo no disponible | Respuesta `503` | Mensaje por región o estado general sin romper cabecera | Reintentar/usar navegación disponible | Sí |
| Favorito guardando | Cliente pulsa corazón | Control ocupado sin duplicar solicitud | Esperar | Sí, como variante de tarjeta |
| Favorito guardado | `201/200` | Estado activo con texto/icono y anuncio accesible | Continuar | Sí, como variante de tarjeta |
| Favorito sin sesión | Visitante pulsa corazón | Se activa `O-003`; no se crea favorito anónimo | Iniciar sesión o cancelar | Se diseña en `O-003` |
| Producto no disponible | F-036 devuelve `404` | Tarjeta se marca no disponible o se retira tras informar | Actualizar/explorar | Sí, como variante de tarjeta |

## 8. Overlays y comunicaciones asociadas

| ID | Elemento | Cuándo aparece | Cómo se cierra o continúa |
|---|---|---|---|
| `O-003` | Autenticación requerida con retorno | Favorito, pedidos u otra acción protegida sin sesión | Login conserva `V-005` y la intención; cancelar mantiene posición. |
| `O-010` | Alertas y feedback global | Error de favoritos o indisponibilidad recuperable | Cerrar o reintentar sin perder contexto. |

## 9. Formularios y validación visual

| Campo | Tipo | Obligatorio | Regla | Mensaje o ayuda | Estado visual |
|---|---|---:|---|---|---|
| Buscar productos | Search | No | Aplicar mínimo y normalización definidos por F-007 | Ayuda breve; no lanzar consulta inválida | Default/foco/error |

El hero no contiene formularios en el alcance actual. Sus CTA sólo apuntan a rutas internas aprobadas.

## 10. Responsive

### Desktop

- **Referencia:** 1440 px.
- Cabecera con logo, buscador visible y acciones globales; categorías pueden usar navegación horizontal con alternativa accesible.
- Hero amplio con texto e imagen equilibrados según `DS-001`.
- Categorías y productos usan grillas responsivas; las tarjetas mantienen relación de imagen y alineación de precios/acciones.
- No iniciar carruseles automáticamente; cualquier carril horizontal ofrece controles visibles, teclado y alternativa de exploración.

### Mobile

- **Referencia:** 390 px.
- Cabecera compacta con acceso claro a búsqueda, cuenta, favoritos y carrito; los contadores no reemplazan sus etiquetas accesibles.
- Hero prioriza título, CTA e imagen sin forzar texto sobre zonas ilegibles.
- Categorías pueden usar grilla de dos columnas o carril manual; destacados no dependen de carrusel automático.
- Las tarjetas conservan nombre, precio y favorito sin objetivos táctiles superpuestos.

### Anchuras intermedias

- Ajustar columnas por ancho mínimo de tarjeta y contenido, no por cantidad fija.
- El buscador puede cambiar de fila antes de comprimirse por debajo de su ancho usable.

## 11. Accesibilidad

- Existe un único encabezado principal y regiones con nombres comprensibles.
- Se ofrece salto al contenido principal.
- Todas las tarjetas tienen un enlace accesible; el control de favorito es una acción separada y no anida botones dentro del enlace.
- Imágenes comerciales tienen texto alternativo útil; decoración usa alternativa vacía.
- Precio anterior, actual y descuento se leen en orden comprensible sin depender del tachado o color.
- Controles de carril, si existen, funcionan con teclado y no mueven contenido automáticamente.
- El cambio de favorito se anuncia y mantiene el foco; doble pulsación no duplica el cambio.
- Skeletons no se anuncian como contenido repetitivo y respetan reducción de movimiento.

## 12. Frames requeridos en Figma

| Frame | Plataforma | Estado | Contenido diferencial |
|---|---|---|---|
| `V-005 / Desktop / Público` | Desktop | Principal | Hero, categorías, destacados y cabecera pública. |
| `V-005 / Mobile / Público` | Mobile | Principal | Cabecera compacta y secciones apiladas. |
| `V-005 / Desktop / Autenticado` | Desktop | Principal con sesión | Cuenta y estados de favorito. |
| `V-005 / Mobile / Cargando` | Mobile | Skeleton por sección | Cabecera operativa. |
| `V-005 / Desktop / Sin contenido` | Desktop | Vacío total | Orientación a catálogo. |
| `V-005 / Mobile / Catálogo no disponible` | Mobile | Error `503` | Reintento sin bloquear navegación. |
| `V-005 / Desktop / ProductCard favorita` | Desktop | Variante de componente | Estado guardando y guardado anotados. |
| `V-005 / Mobile / Producto no disponible` | Mobile | Variante de tarjeta | Feedback y retirada/actualización. |

Los estados de una sola sección vacía se documentan como anotaciones del frame principal, porque la sección se omite y no crea un layout nuevo.

## 13. Criterios de aceptación visual

- [ ] `UI-V005-001`: Sólo se muestran categorías y productos activos con los datos mínimos completos.
- [ ] `UI-V005-002`: Una sección vacía se omite sin bloquear búsqueda, cabecera ni otras secciones.
- [ ] `UI-V005-003`: Mobile no depende de carrusel automático para acceder al contenido.
- [ ] `UI-V005-004`: Cada `ProductCard` separa navegación y favorito con nombres y focos accesibles.
- [ ] `UI-V005-005`: Guardar favorito sin sesión activa `O-003`, no crea estado anónimo y conserva el retorno.
- [ ] `UI-V005-006`: Precios y ofertas mantienen jerarquía semántica y no dependen sólo de color o tachado.
- [ ] `UI-V005-007`: Los estados de carga/error se resuelven por sección cuando todavía existe contenido útil.
- [ ] La vista aplica `DS-001` y reutiliza los mismos patrones globales de `V-006` y `V-007`.

## 14. Decisiones y pendientes

| ID | Pregunta o decisión | Responsable | Fecha límite | Estado |
|---|---|---|---|---|
| `V-005-OPEN-01` | Definir contenido, CTA, fuente y caducidad del hero; no inventar promociones en Figma. | Producto + UX | Antes del diseño final | Abierta |
| `V-005-OPEN-02` | Confirmar orden, cantidad máxima e imagen/icono de categorías. | Catálogo + Producto | Antes del diseño final | Abierta |
| `V-005-OPEN-03` | Confirmar cantidad y regla editorial de productos destacados. | Catálogo + Producto | Antes del diseño final | Abierta |
| `V-005-OPEN-04` | Aprobar patrón de cabecera y navegación mobile compartido por las vistas comerciales. | UX/UI | Antes del diseño final | Abierta |
