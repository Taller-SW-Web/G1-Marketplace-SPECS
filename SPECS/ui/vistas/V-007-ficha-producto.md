# Vista — V-007 Ficha del producto

> Pantalla pública que integra información descriptiva, galería, precio, variantes, disponibilidad, carrito, favoritos y productos relacionados sin mezclar sus responsabilidades.

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID | `V-007` |
| Nombre | Ficha del producto |
| Ruta | `/productos/{slug}` |
| Versión | `0.1.0` |
| Estado | En revisión |
| Responsable | Fernando José Saire Tello |
| Revisor | Giuliano Macchiavello |
| Sistema de diseño | [`DS-001`](../DS-001-sistema-diseno-marketplace.md) |
| Enlace de Figma | Pendiente |

## 2. Propósito, actor y acceso

- **Objetivo del usuario:** evaluar un producto, elegir una variante cuando corresponda, consultar precio/disponibilidad y agregar un SKU vendible al carrito o guardar el producto en favoritos.
- **Actor principal:** visitante o cliente autenticado.
- **Permiso:** público; favoritos requieren sesión, carrito admite visitante mediante sesión anónima.
- **Condición de entrada:** slug válido desde inicio, catálogo, relacionados o enlace directo.
- **Resultado esperado:** producto comprendido y acción comercial consciente; consultar no reserva stock ni garantiza el precio del checkout.

## 3. Trazabilidad

| Funcionalidad | Spec funcional | Spec UI de origen | Aporte a esta vista |
|---|---|---|---|
| `F-011` | [`Ficha y galería`](../../funcional/F-011-detalle-producto.md) | [`UI F-011`](../F-011-detalle-producto.md) | Identidad, descripción, especificaciones y galería. |
| `F-012` | [`Precio y oferta`](../../funcional/F-012-precio-oferta-descuento.md) | [`UI F-012`](../F-012-precio-oferta-descuento.md) | Precio vigente por SKU y oferta válida. |
| `F-013` | [`Seleccionar variante`](../../funcional/F-013-seleccion-atributos-variante.md) | [`UI F-013`](../F-013-seleccion-atributos-variante.md) | Atributos, combinación y SKU. |
| `F-014` | [`Consultar stock`](../../funcional/F-014-consultar-disponibilidad-stock.md) | [`UI F-014`](../F-014-consultar-disponibilidad-stock.md) | Disponibilidad comercial sin cantidad ni reserva. |
| `F-015` | [`Productos relacionados`](../../funcional/F-015-productos-relacionados.md) | [`UI F-015`](../F-015-productos-relacionados.md) | Hasta ocho recomendaciones válidas. |
| `F-016` | [`Agregar al carrito`](../../funcional/F-016-agregar-item-carrito.md) | [`UI F-016`](../F-016-agregar-item-carrito.md) | Alta/incremento de SKU y feedback. |
| `F-036` | [`Agregar favorito`](../../funcional/F-036-agregar-favorito.md) | [`UI F-036`](../F-036-agregar-favorito.md) | Favorito por producto, no por SKU. |

Se consultaron los contratos API homónimos `F-011` a `F-016` y `F-036` de `SPECS/contrato-api/`.

## 4. Entradas, salidas y conservación de contexto

| Origen o acción | Destino | Condición | Contexto conservado |
|---|---|---|---|
| Tarjeta en `V-005` | `V-007` | Slug activo | Origen y posición cuando sea viable. |
| Resultado en `V-006` | `V-007` | Slug activo | URL completa, página, filtros, orden y scroll para volver. |
| Producto relacionado | Otra instancia de `V-007` | Slug relacionado | Nueva ficha; historial permite volver. |
| Migas → Catálogo | `V-006` | Acción explícita | Criterios previos cuando existan; si no, catálogo general. |
| “Ver carrito” en `O-005` | `V-008` | Adición exitosa/ajustada | Carrito actualizado. |
| Favorito sin sesión | `O-003` → `V-001` | Acción protegida | Ruta, producto e intención de favorito. |

Cambiar variante permanece en la misma ruta; la selección no debe presentarse como parámetro compartible hasta que el equipo defina una URL canónica para SKU.

## 5. Jerarquía y composición visual

```text
V-007 Ficha del producto
├── Cabecera global
├── Migas de navegación
├── Región principal
│   ├── Galería
│   │   ├── Imagen principal
│   │   ├── Miniaturas
│   │   ├── Anterior/siguiente
│   │   └── Ampliar → O-002
│   └── Resumen comercial
│       ├── Marca y nombre H1
│       ├── Favorito
│       ├── Precio/oferta F-012
│       ├── Selectores de variante F-013
│       ├── Disponibilidad F-014
│       └── Agregar al carrito F-016
├── Descripción
├── Especificaciones técnicas
├── Productos relacionados F-015
└── Pie global
```

| Región | Componente o contenido | Prioridad | Comportamiento |
|---|---|---|---|
| Galería | Imagen principal, miniaturas y controles | Primaria | Primera imagen válida inicial; carga diferida de secundarias; ampliación en `O-002`. |
| Identidad | Marca y nombre | Primaria | Nombre como único `h1`; contenido sanitizado. |
| Precio | Actual, referencia, descuento y vigencia | Primaria | Se actualiza por SKU sin recargar descripción. |
| Variantes | Grupos de atributos | Primaria | Combinaciones existentes; cambiar invalida SKU/precio/stock previos. |
| Disponibilidad | Disponible/stock bajo/agotado/error | Primaria | Nunca muestra cantidad, ubicación o reserva. |
| Compra | “Agregar al carrito” | Primaria | Sólo SKU válido con disponibilidad distinta de agotado. |
| Favorito | Control por producto | Secundaria | Independiente de talla/color; requiere sesión. |
| Descripción/especificaciones | Texto y pares técnicos | Secundaria | Sección ausente se omite; no se muestra vacía. |
| Relacionados | 1–8 `ProductCard` | Secundaria | Vacío o fallo se degrada omitiendo toda la sección. |

## 6. Contenido y acciones

| Elemento | Texto o dato | Acción | Condición de visibilidad |
|---|---|---|---|
| Migas | Inicio / Catálogo / producto | Navegar hacia atrás | Ficha válida. |
| Galería | Imágenes, alternativa y “Imagen X de Y” | Seleccionar/ampliar | Ficha válida. |
| Marca/nombre | Datos autoritativos | — | Ficha válida. |
| Precio regular | Importe y moneda | — | Precio vigente sin oferta. |
| Oferta | Precio actual, referencia, descuento y fecha | — | Oferta válida. |
| Selección requerida | “Selecciona una opción para ver precio y disponibilidad” | Orientar a atributos | Producto variable incompleto. |
| Atributos | Valores con etiqueta textual | Elegir combinación | Producto con variantes. |
| Disponibilidad | “Disponible”, “Quedan pocas unidades” o “Agotado” | Reintentar sólo ante error | SKU resuelto. |
| CTA carrito | “Agregar al carrito” | Agregar/incrementar SKU | SKU válido y comprable. |
| Favorito | “Guardar/Quitar de favoritos” | Cambiar estado o autenticar | Producto válido. |
| Descripción | Texto sanitizado | Expandir si se justifica | Contenido válido. |
| Relacionados | Tarjetas completas | Abrir nueva ficha | Lista no vacía. |

## 7. Estados de la vista

Las regiones de precio, variantes, stock y relacionados cargan de forma independiente; un fallo no crítico no debe reemplazar una ficha descriptiva válida por un error total.

| Estado | Disparador | Cambios visibles | Acción o recuperación | Frame requerido |
|---|---|---|---|---|
| Cargando ficha | Entrada a slug | Skeleton de galería, identidad y resumen; sin datos ficticios | Esperar | Sí |
| Producto simple listo | Ficha + SKU base válidos | Precio/stock y CTA sin selectores | Agregar/favorito | Sí |
| Variable sin selección | Existen variantes y falta combinación | Selectores; precio/stock en espera; CTA deshabilitado con explicación | Seleccionar | Sí |
| Variante válida | Combinación resuelve SKU | Imagen opcional, precio y stock se recargan | Comprar | Sí |
| Combinación inválida | Elección incompatible | Valor no disponible; SKU previo descartado | Elegir combinación válida | Sí |
| Actualizando variante | Cambio de selección | Skeleton sólo de precio/stock; descripción permanece | Esperar | Sí |
| Oferta vigente | Precio promocional válido | Actual, referencia, descuento y vigencia | — | Sí, variante comercial |
| Precio no disponible | Error/ausencia de Pricing | Región de precio neutral; ficha visible; compra no afirma importe | Reintentar precio | Sí |
| Disponible/stock bajo | Inventario responde | Texto + icono; CTA habilitable | Agregar | Anotado en principal |
| Agotado | `OUT_OF_STOCK` | Estado explícito y CTA deshabilitado | Cambiar variante/explorar | Sí |
| Stock desconocido | Error de Inventario | “No pudimos consultar disponibilidad”; no se muestra “Agotado” | Reintentar stock | Sí |
| Agregando | Pulsación válida | CTA ocupado y no repetible | Esperar | Sí, variante |
| Agregado/ajustado | `200/201` o límite | `O-005`; cantidad/ajuste comprensible | Ver carrito/seguir | Se diseña en `O-005` |
| Error de adición | No mutación o conflicto | Mensaje junto al CTA y acción segura | Reintentar/actualizar | Sí |
| Favorito sin sesión | Visitante pulsa corazón | `O-003` | Login/cancelar | Se diseña en `O-003` |
| Imagen no descargable | Fallo del navegador | Respaldo “Imagen no disponible”; texto sigue accesible | Elegir otra imagen | Sí |
| Relacionados vacíos/error | Sin tarjetas válidas | Sección completa omitida | — | No |
| Producto no disponible | Slug inválido/inactivo/inexistente | No se muestra contenido parcial; estado neutral | Volver a catálogo | Sí |
| Error total recuperable | Ficha inválida o proveedor falla | Mensaje general; slug conservado | Reintentar/volver | Sí |

## 8. Overlays y comunicaciones asociadas

| ID | Elemento | Cuándo aparece | Cómo se cierra o continúa |
|---|---|---|---|
| `O-002` | Visor de galería | Activar imagen principal o “Ampliar” | Cerrar devuelve foco; navegar conserva imagen elegida. |
| `O-003` | Autenticación requerida | Guardar favorito sin sesión | Login retorna a la ficha y completa intención si sigue siendo válida. |
| `O-005` | Producto agregado al carrito | Adición exitosa o cantidad ajustada | Ver `V-008` o seguir en la ficha. |
| `O-010` | Alertas y feedback global | Error no asociado a una región concreta | Reintentar/cerrar. |

## 9. Formularios y validación visual

| Campo/control | Tipo | Obligatorio | Regla | Mensaje o ayuda | Estado visual |
|---|---|---:|---|---|---|
| Grupo de atributo | Botones de opción | Para producto variable | Un valor activo por atributo; combinación existente | “Selecciona {atributo}” | Default/seleccionado/no disponible/error |
| Cantidad de adición | Fija en 1 en este alcance | Sí | F-016 envía `quantity=1`; posteriores adiciones incrementan la línea | No se presenta selector si no está especificado | No aplica |

Los colores se acompañan de nombre textual; agotado no convierte una variante existente en inexistente. El CTA no se habilita mientras falte SKU o el stock sea agotado/desconocido.

## 10. Responsive

### Desktop

- **Referencia:** 1440 px.
- Región principal en dos columnas: galería y resumen comercial; ninguna queda fija si oculta contenido.
- Miniaturas junto o debajo de la imagen según cantidad; descripción y especificaciones ocupan ancho legible inferior.
- Relacionados usan grilla o carril manual sin autoplay.

### Mobile

- **Referencia:** 390 px.
- Orden: migas compactas, galería, identidad, precio, variantes, stock y CTA; descripción y relacionados después.
- CTA puede ser persistente sólo si refleja selección/stock actual, no oculta controles y respeta áreas seguras.
- Miniaturas y relacionados usan desplazamiento manual con alternativa de teclado.
- Texto técnico puede agruparse en acordeones accesibles si el contenido es largo; los encabezados continúan visibles.

### Anchuras intermedias

- Cambiar a una columna cuando galería o resumen no conserven su ancho mínimo.
- Grupos de atributos envuelven valores completos; nunca truncan talla/color hasta volverlos ambiguos.

## 11. Accesibilidad

- Un único `h1`; migas, galería, resumen y relacionados tienen regiones comprensibles.
- Miniaturas y flechas anuncian producto, posición y selección; el visor `O-002` gestiona foco y teclado.
- Precio actual se anuncia antes de referencia/descuento; oferta no depende de tachado o color.
- Variantes usan `fieldset`/`legend`, nombre textual, estado seleccionado/no disponible y objetivos de al menos 44 px.
- Cambiar SKU anuncia selección y actualiza precio/stock con `aria-live="polite"` sin mover foco.
- Agotado, error de stock y carga son semántica y visualmente diferentes.
- Favorito es control separado del contenido; doble pulsación no duplica estado.
- CTA ocupado evita repetición y conserva un nombre accesible.
- Imágenes usan alternativa útil; contenido decorativo se omite del árbol accesible.

## 12. Frames requeridos en Figma

| Frame | Plataforma | Estado | Contenido diferencial |
|---|---|---|---|
| `V-007 / Desktop / Producto simple` | Desktop | Principal | Dos columnas, precio, stock y CTA. |
| `V-007 / Mobile / Producto simple` | Mobile | Principal | Orden apilado. |
| `V-007 / Desktop / Variable sin selección` | Desktop | Selección requerida | Selectores y regiones en espera. |
| `V-007 / Mobile / Variante seleccionada` | Mobile | Lista | Imagen/precio/stock actualizados. |
| `V-007 / Desktop / Oferta vigente` | Desktop | Comercial | Precio actual, referencia, descuento y vigencia. |
| `V-007 / Mobile / Agotado` | Mobile | No disponible | CTA explicado y alternativa. |
| `V-007 / Desktop / Precio o stock error` | Desktop | Error regional | Reintentos independientes. |
| `V-007 / Mobile / Agregando` | Mobile | Progreso | CTA ocupado/persistente si aplica. |
| `V-007 / Desktop / Error de adición` | Desktop | Error transaccional | Mensaje junto al CTA. |
| `V-007 / Mobile / Imagen de respaldo` | Mobile | Media fallback | Texto preservado. |
| `V-007 / Desktop / Producto no disponible` | Desktop | Estado final | Retorno al catálogo. |
| `V-007 / Mobile / Error recuperable` | Mobile | Error total | Reintentar/volver. |

Los overlays `O-002`, `O-003` y `O-005` tienen sus propios frames y no se duplican aquí.

## 13. Criterios de aceptación visual

- [ ] `UI-V007-001`: La ficha integra F-011–F-016 y F-036 sin mostrar precio, SKU, stock o promociones ficticios.
- [ ] `UI-V007-002`: Cambiar una variante descarta el SKU, precio y stock anteriores hasta obtener respuestas de la nueva selección.
- [ ] `UI-V007-003`: Agotado, stock desconocido y combinación inexistente son estados diferentes y comprensibles.
- [ ] `UI-V007-004`: Precio/oferta se comunica con texto y orden semántico, no sólo color o tachado.
- [ ] `UI-V007-005`: Agregar al carrito funciona para visitantes y clientes, evita doble envío y no implica reserva.
- [ ] `UI-V007-006`: Guardar favorito sin sesión usa `O-003` y conserva la ficha/acción de origen.
- [ ] `UI-V007-007`: Un fallo de precio, stock, imagen o relacionados no oculta una ficha descriptiva válida.
- [ ] `UI-V007-008`: Sin relacionados válidos se omite título y contenedor completos.
- [ ] `UI-V007-009`: Desktop y mobile enumeran los frames críticos y mantienen navegación completa por teclado.
- [ ] La vista aplica `DS-001` y reutiliza `ProductCard`, precio, galería, botones y feedback definidos allí.

## 14. Decisiones y pendientes

| ID | Pregunta o decisión | Responsable | Fecha límite | Estado |
|---|---|---|---|---|
| `V-007-OPEN-01` | Homologar rutas, autorización de canal y OpenAPI de Catálogo, Pricing e Inventario (`I-01`). | Backend + módulos dueños | Antes de implementación; informar diseño | Abierta |
| `V-007-OPEN-02` | Confirmar si la selección de SKU debe persistirse en URL para compartir una variante. | Producto + Arquitectura | Antes del diseño final | Abierta |
| `V-007-OPEN-03` | Aprobar tamaño/proporción de galería y comportamiento del CTA persistente mobile. | UX/UI | Antes del diseño final | Abierta |
| `V-007-OPEN-04` | Confirmar si Cross-sell/Upsell necesita etiqueta visible para el cliente o sólo orden editorial. | Producto + UX | Antes del diseño final | Abierta |
