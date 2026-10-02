# Vista — V-006 Catálogo y resultados

> Pantalla pública para explorar productos activos mediante búsqueda, filtros, ordenamiento y paginación conservados en la URL.

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID | `V-006` |
| Nombre | Catálogo y resultados |
| Ruta | `/catalogo` |
| Versión | `0.1.0` |
| Estado | En revisión |
| Responsable | Leonidas Garcia |
| Revisor | Giuliano Macchiavello |
| Sistema de diseño | [`DS-001`](../DS-001-sistema-diseno-marketplace.md) |
| Enlace de Figma | Pendiente |

## 2. Propósito, actor y acceso

- **Objetivo del usuario:** encontrar productos activos combinando texto, categoría, marca, precio y orden, y abrir una ficha de producto.
- **Actor principal:** visitante o cliente autenticado.
- **Permiso:** público.
- **Condiciones de entrada:** búsqueda o categoría desde `V-005`, acceso directo, enlace compartido o retorno desde `V-007`.
- **Resultado esperado:** criterios comprensibles y reproducibles en URL, resultados paginados o una recuperación clara cuando no existen coincidencias.

## 3. Trazabilidad

| Funcionalidad | Spec funcional | Spec UI de origen | Aporte a esta vista |
|---|---|---|---|
| `F-007` | [`Buscar productos`](../../funcional/F-007-buscar-productos-texto.md) | [`UI F-007`](../F-007-buscar-productos-texto.md) | Consulta de 2–120 caracteres, estados y limpieza. |
| `F-008` | [`Filtrar catálogo`](../../funcional/F-008-filtrar-catalogo.md) | [`UI F-008`](../F-008-filtrar-catalogo.md) | Categoría, marca, rango, chips, aplicar y limpiar. |
| `F-009` | [`Ordenar resultados`](../../funcional/F-009-ordenar-catalogo.md) | [`UI F-009`](../F-009-ordenar-catalogo.md) | Relevancia, novedades y precio con orden estable. |
| `F-010` | [`Paginar resultados`](../../funcional/F-010-paginar-catalogo.md) | [`UI F-010`](../F-010-paginar-catalogo.md) | Página, tamaño, límites y foco tras actualizar. |
| `F-036` | [`Agregar favorito`](../../funcional/F-036-agregar-favorito.md) | [`UI F-036`](../F-036-agregar-favorito.md) | Estado de favorito en tarjetas y autenticación requerida. |

Contratos consultados: [`API F-007`](../../contrato-api/F-007-buscar-productos-texto.md), [`API F-008`](../../contrato-api/F-008-filtrar-catalogo.md), [`API F-009`](../../contrato-api/F-009-ordenar-catalogo.md), [`API F-010`](../../contrato-api/F-010-paginar-catalogo.md) y [`API F-036`](../../contrato-api/F-036-agregar-favorito.md).

## 4. Entradas, salidas y conservación de contexto

| Origen o acción | Destino | Condición | Contexto conservado |
|---|---|---|---|
| Búsqueda en `V-005` | `V-006?q=...` | Consulta válida | Texto normalizado. |
| Categoría en `V-005` | `V-006?categoryIds=...` | ID activo | Categoría aplicada. |
| Enlace compartido | `V-006` | Parámetros válidos | Query, filtros, orden y página. |
| Tarjeta de producto | `V-007` | Producto activo | URL completa del catálogo y posición para volver. |
| Volver desde `V-007` | `V-006` | Historial disponible | Criterios, página y posición cuando sea viable. |
| Limpiar búsqueda | `V-006` | Query eliminada | Filtros y orden compatibles; página vuelve a cero. |
| Aplicar/limpiar filtros | `V-006` | Criterios válidos | Query y orden; página vuelve a cero. |
| Cambiar orden | `V-006` | Enum permitido | Query y filtros; página vuelve a cero. |
| Cambiar página | `V-006` | Página existente | Query, filtros y orden. |

La URL es la representación compartible del estado aplicado, no de valores aún sin confirmar dentro de `O-001`.

## 5. Jerarquía y composición visual

```text
V-006 Catálogo y resultados
├── Cabecera global
│   └── Buscador con query actual
├── Migas o contexto de exploración
├── Encabezado de resultados
│   ├── Título/query
│   ├── Cantidad de resultados
│   ├── Botón filtros mobile + contador
│   └── Selector “Ordenar por”
├── Chips de criterios aplicados
├── Área principal
│   ├── Panel de filtros desktop
│   └── Región de resultados
│       ├── Grilla ProductCard
│       └── Estado vacío/error
├── Paginación
└── Pie global
```

| Región | Componente o contenido | Prioridad | Comportamiento |
|---|---|---|---|
| Búsqueda | Query actual editable | Primaria | Confirmar actualiza URL y reinicia página. |
| Encabezado | Contexto y cantidad | Primaria | La cantidad se anuncia sin mover el foco. |
| Filtros desktop | Categoría, marca y precio | Primaria | Panel lateral; aplicar/limpiar explícitos. |
| Filtros mobile | Botón y resumen | Primaria | Abre `O-001`; criterios sin aplicar no alteran resultados. |
| Chips | Criterios aplicados | Secundaria | Cada chip removible actualiza URL y página cero. |
| Orden | Selector permitido | Primaria | Relevancia sólo si existe query y el proveedor la define. |
| Resultados | Grilla de `ProductCard` | Primaria | Máximo inicial de 24 por página. |
| Paginación | Anterior, estado y siguiente | Primaria | Sólo páginas existentes operables. |

## 6. Contenido y acciones

| Elemento | Texto o dato | Acción | Condición de visibilidad |
|---|---|---|---|
| Título sin query | “Catálogo” | — | Exploración general. |
| Título con query | `Resultados para “{query}”` | — | Búsqueda válida. |
| Cantidad | “{n} productos” | Anunciar actualización | Total conocido. |
| Filtro categoría | Maestros activos por ID | Seleccionar | Opciones disponibles. |
| Filtro marca | Maestros activos por ID | Seleccionar | Opciones disponibles. |
| Precio mínimo/máximo | Importes PEN | Editar y validar | Siempre en filtros. |
| Aplicar | “Aplicar filtros” | Confirmar filtros y cerrar mobile | Criterios válidos. |
| Limpiar | “Limpiar filtros” | Retirar filtros, conservar query/orden | Existe filtro aplicado o borrador. |
| Orden | Relevancia, novedades, menor/mayor precio | Cambiar orden | Según query y capacidades. |
| Tarjeta | Imagen, marca, nombre, precio/oferta, favorito | Abrir producto o guardar favorito | Producto activo. |
| Vacío | “No encontramos productos con estos criterios” | Limpiar filtros o editar búsqueda | Cero resultados. |
| Paginación | “Anterior”, “Página X de Y”, “Siguiente” | Navegar | Más de una página. |

## 7. Estados de la vista

| Estado | Disparador | Cambios visibles | Acción o recuperación | Frame requerido |
|---|---|---|---|---|
| Catálogo general | Sin query ni filtros | Productos, orden por defecto y filtros | Explorar | Sí |
| Resultados de búsqueda | Query válida | Título con query; relevancia disponible si aplica | Refinar/abrir producto | Sí |
| Filtros aplicados | Uno o más criterios | Chips, contador y resultados combinados con AND | Quitar/limpiar | Sí |
| Cargando inicial | Entrada o enlace compartido | Skeleton de filtros/resultados; cabecera operativa | Esperar | Sí |
| Actualizando criterios | Aplicar filtro, orden o página | Región de resultados ocupada sin resultados ficticios; controles coherentes | Esperar | Sí |
| Sin resultados | Respuesta vacía válida | Estado vacío dentro de la región, criterios visibles | Limpiar/editar | Sí |
| Query inválida | Menos de 2 o más de 120 caracteres confirmados | Ayuda/error; no se consulta catálogo | Corregir o limpiar | Sí |
| Rango inválido | Min negativo o mayor que max | Errores junto a precio; no se consulta | Corregir | Se diseña en `O-001` y panel desktop |
| Catálogo no disponible | `503` | Error en resultados, criterios conservados | Reintentar | Sí |
| Página fuera de rango | URL o datos cambiaron | Resultado controlado y retorno a página válida | Ir a primera/última permitida | Sí |
| Favorito guardando/guardado | Acción autenticada | Variante de tarjeta y anuncio | Continuar | Sí, variante de tarjeta |
| Favorito sin sesión | Acción protegida | `O-003` con retorno a esta URL y producto | Login/cancelar | Se diseña en `O-003` |

## 8. Overlays y comunicaciones asociadas

| ID | Elemento | Cuándo aparece | Cómo se cierra o continúa |
|---|---|---|---|
| `O-001` | Filtros mobile | Activar “Filtros” en pantalla estrecha | Aplicar actualiza URL; cancelar conserva criterios aplicados. |
| `O-003` | Autenticación requerida | Guardar favorito sin sesión | Login conserva catálogo, página, scroll e intención. |
| `O-010` | Alertas y feedback global | Error de favorito o catálogo recuperable | Reintentar/cerrar sin perder criterios. |

## 9. Formularios y validación visual

| Campo | Tipo | Obligatorio | Regla | Mensaje o ayuda | Estado visual |
|---|---|---:|---|---|---|
| Buscar | Search | No | Vacía abre catálogo; si contiene texto, 2–120 caracteres tras normalizar espacios | “Escribe al menos 2 caracteres” | Default/foco/error |
| Categorías | Selección múltiple | No | Sólo IDs activos | Opción inactiva no se ofrece | Default/seleccionado |
| Marcas | Selección múltiple | No | Sólo IDs activos | Opción inactiva no se ofrece | Default/seleccionado |
| Precio mínimo | Numérico/moneda | No | PEN, valor ≥ 0 y ≤ máximo | “Revisa el precio mínimo” | Default/foco/error |
| Precio máximo | Numérico/moneda | No | PEN, valor ≥ mínimo | “El máximo debe ser mayor o igual al mínimo” | Default/foco/error |
| Orden | Select | Sí | Enum permitido | Valor inválido vuelve a orden seguro | Default/foco |

## 10. Responsive

### Desktop

- **Referencia:** 1440 px.
- Panel de filtros lateral y resultados en región principal.
- Encabezado alinea título/cantidad con orden; chips ocupan una fila flexible.
- Grilla adapta columnas manteniendo ancho mínimo y alineación de tarjetas.
- Paginación aparece después de resultados y no obliga a recorrer el panel lateral.

### Mobile

- **Referencia:** 390 px.
- Filtros se abren en `O-001`; selector de orden permanece independiente.
- Botones Filtros/Ordenar no se confunden y muestran estado actual.
- Grilla de una o dos columnas según el ancho mínimo aprobado de `ProductCard`; información esencial nunca se oculta.
- Al aplicar criterios, vuelve el foco al encabezado de resultados y se anuncia la cantidad.

### Anchuras intermedias

- El panel lateral se reemplaza por `O-001` cuando comprime la grilla por debajo del ancho útil.
- Chips envuelven líneas; no provocan desplazamiento horizontal de toda la página.

## 11. Accesibilidad

- Buscador dentro de una región `search` con etiqueta explícita.
- Panel de filtros usa grupos y leyendas; cada chip informa criterio y acción de retiro.
- Cantidad de resultados se anuncia de manera no intrusiva sin mover el foco al cambiar criterios.
- Tras paginar, el foco llega al encabezado de resultados; no salta al inicio total de la página.
- Controles anterior/siguiente deshabilitados no son enlaces operables.
- Tarjeta y favorito son objetivos separados con foco visible.
- Carga no anuncia cada skeleton y respeta reducción de movimiento.
- Precio/oferta y estados no dependen sólo de color.

## 12. Frames requeridos en Figma

| Frame | Plataforma | Estado | Contenido diferencial |
|---|---|---|---|
| `V-006 / Desktop / Catálogo` | Desktop | General | Panel lateral y grilla. |
| `V-006 / Mobile / Catálogo` | Mobile | General | Acceso a `O-001` y grilla compacta. |
| `V-006 / Desktop / Búsqueda con filtros` | Desktop | Resultados | Query, chips, orden y paginación. |
| `V-006 / Mobile / Resultados` | Mobile | Resultados | Resumen de criterios y cantidad. |
| `V-006 / Desktop / Cargando` | Desktop | Skeleton | Filtros y resultados. |
| `V-006 / Mobile / Sin resultados` | Mobile | Vacío | Recuperación y criterios visibles. |
| `V-006 / Desktop / Query o rango inválido` | Desktop | Validación | Sin consulta al catálogo. |
| `V-006 / Mobile / Catálogo no disponible` | Mobile | Error `503` | Reintento y criterios conservados. |
| `V-006 / Desktop / Página intermedia` | Desktop | Paginación | Anterior/siguiente y foco documentado. |
| `V-006 / Mobile / ProductCard favorita` | Mobile | Variante | Guardando y guardado anotados. |

## 13. Criterios de aceptación visual

- [ ] `UI-V006-001`: Query, filtros, orden y página aplicados pueden comprenderse y reproducirse desde la URL.
- [ ] `UI-V006-002`: Cambiar búsqueda, filtro u orden reinicia la página y conserva los demás criterios compatibles.
- [ ] `UI-V006-003`: En mobile los filtros usan `O-001`; cancelar no altera resultados y aplicar devuelve foco al encabezado.
- [ ] `UI-V006-004`: Query y rango inválidos no generan una solicitud ni presentan resultados ficticios.
- [ ] `UI-V006-005`: El estado vacío conserva los criterios y ofrece limpiar o corregir.
- [ ] `UI-V006-006`: Relevancia no aparece como opción válida sin búsqueda si Catálogo no la define.
- [ ] `UI-V006-007`: No existe control operable hacia una página inexistente.
- [ ] `UI-V006-008`: Favoritos, precios y resultados se comunican sin depender sólo del color.
- [ ] La vista aplica `DS-001` y comparte cabecera y `ProductCard` con `V-005`/`V-007`.

## 14. Decisiones y pendientes

| ID | Pregunta o decisión | Responsable | Fecha límite | Estado |
|---|---|---|---|---|
| `V-006-OPEN-01` | Confirmar maestros, orden y conteos disponibles para categorías y marcas. | Catálogo | Antes del diseño final | Abierta |
| `V-006-OPEN-02` | Confirmar si Relevancia existe sin query y el criterio exacto de Novedades. | Catálogo + Producto | Antes del diseño final | Abierta |
| `V-006-OPEN-03` | Definir comportamiento del BFF ante página fuera de rango: vacía controlada o redirección a última página. | Backend + Catálogo | Antes del diseño final | Abierta |
| `V-006-OPEN-04` | Aprobar ancho mínimo y número máximo de columnas de `ProductCard` por breakpoint. | UX/UI | Antes del diseño final | Abierta |
