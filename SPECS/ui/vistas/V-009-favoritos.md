# Vista — V-009 Favoritos

> Pantalla privada para consultar productos guardados, quitar favoritos y trasladar productos comprables al carrito sin elegir variantes arbitrarias.

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID | `V-009` |
| Nombre | Favoritos |
| Ruta | `/favoritos` |
| Versión | `0.1.0` |
| Estado | En revisión |
| Responsable | Sebastián Malca |
| Revisor | Diego Espinoza |
| Sistema de diseño | [`DS-001`](../DS-001-sistema-diseno-marketplace.md) |
| Enlace de Figma | Pendiente |

## 2. Propósito, actor y acceso

- **Objetivo del usuario:** revisar sus productos guardados, retirar los que ya no desea y mover al carrito los que pueden comprarse.
- **Actor principal:** cliente autenticado.
- **Permiso:** privado; la identidad se deriva de la sesión, nunca de parámetros visibles.
- **Condición de entrada:** acceso “Favoritos” desde la cabecera o retorno de una acción.
- **Resultado esperado:** lista actualizada; mover sólo retira el favorito después de confirmar el carrito.

## 3. Trazabilidad

| Funcionalidad | Spec funcional | Spec UI de origen | Aporte a esta vista |
|---|---|---|---|
| `F-037` | [`Visualizar favoritos`](../../funcional/F-037-visualizar-favoritos.md) | [`UI F-037`](../F-037-visualizar-favoritos.md) | Lista propia, orden, enriquecimiento y vacío. |
| `F-038` | [`Quitar favorito`](../../funcional/F-038-quitar-favorito.md) | [`UI F-038`](../F-038-quitar-favorito.md) | Eliminación idempotente, deshacer y foco. |
| `F-039` | [`Mover al carrito`](../../funcional/F-039-mover-favorito-carrito.md) | [`UI F-039`](../F-039-mover-favorito-carrito.md) | Producto simple, variante requerida, agotado y atomicidad. |

Se consultaron los contratos API `F-037` a `F-039` de `SPECS/contrato-api/`.

## 4. Entradas, salidas y conservación de contexto

| Origen o acción | Destino | Condición | Contexto conservado |
|---|---|---|---|
| Cabecera autenticada | `V-009` | Sesión válida | Sesión. |
| Acceso sin sesión | `O-003` → `V-001` | Ruta protegida | Retorno a `V-009`. |
| Tarjeta favorita | `V-007` | Producto disponible | Retorno a lista y posición cuando sea viable. |
| Mover producto simple | `V-009` | Carrito confirmado | Lista sin ese favorito; carrito actualizado. |
| Mover producto con variantes | `V-007` | `422 VARIANT_SELECTION_REQUIRED` | Explicación, producto y retorno; favorito permanece hasta agregar. |
| “Ver carrito” tras mover | `V-008` | Movimiento exitoso | Carrito actualizado. |
| Estado vacío → explorar | `V-006` | Sin favoritos | Sesión. |

## 5. Jerarquía y composición visual

```text
V-009 Favoritos
├── Cabecera global autenticada
├── Encabezado “Mis favoritos” + cantidad
├── Región de avisos
├── Grilla/lista de FavoriteCard
│   ├── Imagen, marca y nombre
│   ├── Precio informativo si está disponible
│   ├── Estado comercial
│   ├── “Mover al carrito”
│   └── “Quitar de favoritos”
└── Estado vacío, error o pie global
```

| Región | Componente o contenido | Prioridad | Comportamiento |
|---|---|---|---|
| Encabezado | Título y cantidad | Primaria | Cantidad se actualiza tras confirmación de mutaciones. |
| Colección | Tarjetas en orden más reciente | Primaria | Sólo favoritos del titular; producto no disponible conserva intención hasta decisión explícita. |
| Mover | Acción comercial | Primaria | No afirma éxito hasta confirmar carrito y eliminación. |
| Quitar | Acción destructiva reversible | Secundaria | `O-006` y restauración ante error. |
| Vacío | Mensaje y CTA | Primaria | Sustituye toda la grilla; no deja contenedor vacío. |

## 6. Contenido y acciones

| Elemento | Texto o dato | Acción | Condición de visibilidad |
|---|---|---|---|
| Título | “Mis favoritos” | — | Siempre. |
| Cantidad | “{n} productos guardados” | Anunciar cambios | Lista no vacía. |
| Tarjeta | Imagen, marca, nombre y precio informativo | Abrir `V-007` | Producto disponible. |
| No disponible | “Este producto ya no está disponible” | Quitar favorito | Catálogo no puede ofrecer compra. |
| Mover | “Mover al carrito” | F-039 | Producto disponible. |
| Quitar | “Quitar de favoritos” | F-038 | Todo favorito visible. |
| Vacío | “Aún no tienes favoritos” | Abrir catálogo | Sin elementos. |
| Ver carrito | “Ver carrito” | Abrir `V-008` | Al menos un movimiento confirmado. |

El favorito identifica un `productId`; talla/color pertenecen al SKU del carrito. Por ello la tarjeta nunca conserva o inventa una variante.

## 7. Estados de la vista

| Estado | Disparador | Cambios visibles | Acción o recuperación | Frame requerido |
|---|---|---|---|---|
| Cargando | Consulta inicial | Skeleton de tarjetas sin datos ficticios | Esperar | Sí |
| Con favoritos | Lista enriquecida | Tarjetas ordenadas por guardado reciente | Abrir/mover/quitar | Sí |
| Vacío | Arreglo vacío o última tarjeta retirada | Mensaje y CTA al catálogo; sin grilla | Explorar | Sí |
| Producto no disponible | Producto retirado/inactivo | Tarjeta neutral sin compra; quitar disponible | Quitar/conservar intención | Sí |
| Error de catálogo | No se puede enriquecer coherentemente | Mensaje sin borrar favoritos por suposición | Reintentar | Sí |
| No autenticado/sesión vencida | `401` | `O-003` o redirección segura; no muestra datos previos | Iniciar sesión | Se diseña en `O-003` |
| Quitando | Acción F-038 | Tarjeta retirada visualmente y `O-006` | Deshacer | Sí, con overlay |
| Error al quitar | Eliminación rechazada | Tarjeta restaurada y foco válido | Reintentar | Sí |
| Moviendo producto simple | Solicitud F-039 | Tarjeta ocupada; aún visible | Esperar | Sí |
| Movimiento exitoso | Carrito actualizado y favorito eliminado | Tarjeta retirada; confirmación y acceso al carrito | Ver carrito/continuar | Sí |
| Variante requerida | Respuesta `422` | Explicación; favorito permanece | Abrir `V-007` para seleccionar | Sí |
| Agotado/no disponible | `409`/`404` aplicable | Favorito permanece y compra no disponible | Conservar/quitar/ver ficha | Sí |
| Error al mover | Conflicto o dependencia externa | Tarjeta permanece; no se indica traslado | Reintentar | Sí |

## 8. Overlays y comunicaciones asociadas

| ID | Elemento | Cuándo aparece | Cómo se cierra o continúa |
|---|---|---|---|
| `O-003` | Autenticación requerida con retorno | Acceso sin sesión o sesión vencida | Login regresa a `V-009`. |
| `O-006` | Deshacer eliminación | F-038 retira una tarjeta | Deshacer dentro de la ventana o expirar. |
| `O-010` | Alertas y feedback global | Movimiento confirmado, error o indisponibilidad | Ver carrito, reintentar o cerrar. |

## 9. Formularios y validación visual

No hay formularios editables. Todas las acciones usan identificadores internos derivados de la tarjeta y la sesión; nunca solicitan `customerId`, SKU arbitrario o cantidad.

| Control | Regla | Mensaje o ayuda |
|---|---|---|
| Mover al carrito | Una solicitud por tarjeta; sólo producto simple resuelve SKU automáticamente | Variante requerida dirige a ficha. |
| Quitar favorito | Idempotente; reversible visualmente según `O-006` | Resultado anunciado. |

## 10. Responsive

### Desktop

- **Referencia:** 1440 px.
- Grilla con tarjetas de altura coherente; acciones permanecen visibles sin hover.
- Producto no disponible conserva estructura suficiente para reconocerlo y quitarlo.
- Los cambios de colección no provocan saltos que desorienten el foco.

### Mobile

- **Referencia:** 390 px.
- Una o dos columnas sólo si nombre, estado y acciones mantienen ancho y objetivos táctiles suficientes.
- Acciones pueden apilarse; “Mover” y “Quitar” no se representan sólo con iconos.
- Tras retirar una tarjeta, el foco se mueve a una tarjeta vecina o al título/estado vacío.

### Anchuras intermedias

- Las columnas dependen del ancho mínimo de `FavoriteCard`; no se truncan nombre, precio ni estado para mantener una columna adicional.

## 11. Accesibilidad

- La colección es una lista semántica y cada tarjeta tiene un encabezado con el producto.
- Enlace de producto, mover y quitar son controles separados, con nombres que incluyen el producto cuando sea necesario.
- Estado no disponible usa texto e icono además del color.
- Durante una mutación, sólo la tarjeta afectada queda ocupada y se evita doble activación.
- Tras quitar/mover, el foco nunca queda en un nodo eliminado; el cambio de cantidad se anuncia.
- “Deshacer” es alcanzable por teclado y no depende de percibir una animación.
- El vacío recibe foco en su encabezado cuando desaparece la última tarjeta.

## 12. Frames requeridos en Figma

| Frame | Plataforma | Estado | Contenido diferencial |
|---|---|---|---|
| `V-009 / Desktop / Con favoritos` | Desktop | Principal | Grilla y acciones. |
| `V-009 / Mobile / Con favoritos` | Mobile | Principal | Tarjetas y acciones apiladas. |
| `V-009 / Desktop / Cargando` | Desktop | Skeleton | Colección. |
| `V-009 / Mobile / Vacío` | Mobile | Vacío | CTA catálogo. |
| `V-009 / Desktop / Producto no disponible` | Desktop | Atención | Tarjeta sin compra. |
| `V-009 / Mobile / Error catálogo` | Mobile | Error | Reintento sin falso vacío. |
| `V-009 / Desktop / Moviendo` | Desktop | Progreso local | Tarjeta conservada. |
| `V-009 / Mobile / Variante requerida` | Mobile | Redirección explicada | Favorito permanece. |
| `V-009 / Desktop / Movimiento exitoso` | Desktop | Éxito | Tarjeta retirada y acceso a carrito. |
| `V-009 / Mobile / Error al mover` | Mobile | Error local | Tarjeta y favorito conservados. |

`O-003` y `O-006` se diseñan en sus specs propias.

## 13. Criterios de aceptación visual

- [ ] `UI-V009-001`: Sólo se muestran favoritos del cliente autenticado y se ordenan del más reciente al más antiguo.
- [ ] `UI-V009-002`: El estado vacío reemplaza la grilla y ofrece una salida clara al catálogo.
- [ ] `UI-V009-003`: Un producto retirado no ofrece compra ni se elimina automáticamente de favoritos.
- [ ] `UI-V009-004`: Quitar es reversible visualmente, restaura la tarjeta ante fallo y mantiene un foco válido.
- [ ] `UI-V009-005`: Mover sólo retira el favorito después de confirmar el carrito.
- [ ] `UI-V009-006`: Producto con variantes abre `V-007` y no elige un SKU arbitrario; agotado conserva el favorito.
- [ ] `UI-V009-007`: Error de catálogo no se presenta como lista vacía ni borra intención del usuario.
- [ ] `UI-V009-008`: Desktop y mobile mantienen enlace de producto, mover y quitar como controles separados.
- [ ] La vista aplica `DS-001` y reutiliza las reglas de `ProductCard` sin ocultar acciones críticas.

## 14. Decisiones y pendientes

| ID | Pregunta o decisión | Responsable | Fecha límite | Estado |
|---|---|---|---|---|
| `V-009-OPEN-01` | Definir política única para favoritos cuyo producto fue retirado: mostrar tarjeta no disponible u omitirla manteniendo la intención interna. | Producto + UX | Antes del diseño final | Abierta |
| `V-009-OPEN-02` | Definir la operación técnica de “Deshacer” tras `DELETE` de favorito. | Backend + UX | Antes del diseño final | Abierta |
| `V-009-OPEN-03` | Confirmar si un movimiento exitoso ofrece sólo feedback o navegación opcional inmediata a `V-008`. | Producto + UX | Antes del diseño final | Abierta |
| `V-009-OPEN-04` | Homologar Catálogo/stock usados para enriquecimiento y traslado (`I-01`). | Backend + módulos dueños | Antes de implementación; informar diseño | Abierta |
