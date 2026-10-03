# Spec de componentes React — F-011 Visualizar ficha y galería del producto

> Traducción técnica de las specs vigentes; no es código implementado ni aprobación de un contrato externo pendiente.

## 1. Metadatos y trazabilidad

| Campo | Valor |
|---|---|
| ID funcional | `F-011` |
| Versión / estado | `0.1.0` / En revisión |
| Fecha | 2026-10-02 |
| Funcional | [F-011](../funcional/F-011-detalle-producto.md) |
| UI funcional | [F-011](../ui/F-011-detalle-producto.md) |
| Contrato API | [F-011](../contrato-api/F-011-detalle-producto.md) |
| Entregables visuales | [V-007](../ui/vistas/V-007-ficha-producto.md), [O-002](../ui/overlays/O-002-visor-galeria.md) |
| Base transversal | [Arquitectura React](ARQUITECTURA-REACT.md), [DS-001 v0.2.0](../ui/DS-001-sistema-diseno-marketplace.md) |
| Stack | React + TypeScript; Next.js App Router propuesto por arquitectura existente; librería UI pendiente de DS-OPEN-03 |
| Responsables de implementación | Propuesta explícita en [plan F-011](../../plan/funcionalidades/F-011-detalle-producto.md); no reemplaza el reparto de mockups |
| Iteración objetivo | Sprint 2, sujeto a puertas de entrada y capacidad confirmada |

## 2. Rutas y pantallas

| Ruta / superficie | Acceso | Composición |
|---|---|---|
| `/productos/{slug}` | Pública | `ProductDetailContainer` + `ProductGallery` + `GalleryViewer` + `TechnicalSpecifications` |

Los enlaces de vistas/overlays definen todos los frames y variantes; no crear un nuevo ID V para un estado de la misma pantalla. Desktop se produce primero; mobile sigue dentro del alcance, no se elimina ni se simula reduciendo el desktop.

## 3. Árbol de componentes

```text
Layout de ruta → límite público/privado correspondiente
├── ProductDetailContainer
├── ProductGallery
├── GalleryViewer
└── TechnicalSpecifications
    └── Feedback accesible compartido según estado
```

El contenedor coordina transporte/estado; los componentes presentacionales no llaman servicios externos ni contienen reglas de descuento, stock o autorización.

## 4. Contratos de componentes

| ID / componente | Responsabilidad | Props tipadas (propuesta) | Eventos |
|---|---|---|---|
| `CMP-F011-001` · `ProductDetailContainer` | Sólo región descriptiva, no precio/stock. | `slug: string; detail: ProductDetailDTO; status: QueryStatus` | onRetryDetail() |
| `CMP-F011-002` · `ProductGallery` | Galería ordenada y controles finitos. | `media: ProductMedia[]; selectedIndex: number` | onSelect(index); onOpenViewer(index) |
| `CMP-F011-003` · `GalleryViewer` | O-002 con trampa/restauración de foco. | `opened: boolean; media: ProductMedia[]; index: number` | onClose(); onIndexChange(index) |
| `CMP-F011-004` · `TechnicalSpecifications` | Texto seguro, oculta bloques vacíos. | `groups: SpecificationGroup[]; description?: string` | — |

Los nombres de DTO y drafts son contratos TypeScript de implementación, no nuevos campos de la API. Su estructura se deriva exclusivamente del contrato enlazado; aplicar las convenciones de tipos de [ARQUITECTURA-REACT](ARQUITECTURA-REACT.md#3-tipos-y-contratos). Props con `busy` no habilitan dobles mutaciones. Eventos se invocan una vez y devuelven control al contenedor.

## 5. Estado y flujo de datos

- **Local:** Índice, visor y medios fallidos; reset al cambiar slug.
- **Compartido:** sólo sesión no sensible, identidad del contexto y contexto transitorio del flujo; no duplicar datos remotos en stores independientes.
- **Remoto / caché:** ['catalog','detail',slug]; respetar ETag/cache del BFF; query independiente de precio/variantes/stock.
- **Flujo específico:** Reintentar sólo detalle. Imagen principal fallida usa respaldo y no borra texto; secundaria fallida conserva principal anterior. F-013 puede proveer imagen de variante sin mutar DTO.
- Cancelar o ignorar respuestas de identidad/selección anterior. No guardar cuerpos sensibles en devtools, logs o analítica. Los cachés privados se eliminan al cerrar o cambiar de sesión.

## 6. Hooks, formularios y validaciones

| Elemento | Responsabilidad | Fuente |
|---|---|---|
| `useProductDetail` | Orquestar el flujo descrito; presentación consume estado discriminado y callbacks | Funcional F-011, UI F-011, API F-011 |
| Adaptador tipado | Validar DTO y mapear error público; sin aceptar shape externo no homologado | Contrato API enlazado |
| Validación local | Ayuda inmediata, nunca reemplaza validación ni autorización del servidor | Reglas siguientes |

Slug 1–120 con patrón canónico; respuesta activa sin medios es inválida; URLs permitidas, texto sanitizado, no dangerouslySetInnerHTML no seguro.

### Operaciones documentadas

- `GET /api/v1/catalog/products/{slug}`

Auth y rutas `/password` se traducen mediante el límite de integración aprobado; no se presupone que ya exista proxy BFF ni CORS habilitado. Rutas `/internal` jamás se consumen desde el navegador. Header, request y response exactos pertenecen al contrato API, no a las props.

## 7. Estados, errores y recuperación

LOADING → READY | NOT_AVAILABLE | ERROR; MEDIA_FALLBACK es estado de render de una imagen válida, no respuesta sin medios.

- **Carga:** skeleton de la región que consulta, o progreso local de mutación; nunca datos o importes de ejemplo.
- **Vacío / no aplicable:** sólo ante respuesta válida o condición explícita; errores nunca se convierten en colección vacía, precio cero o stock agotado.
- **Error:** mensaje público y recuperación específica del flujo; errores de campo se asocian a su control. Conservar valores no sensibles cuando sea seguro.
- **Éxito:** se deriva de la respuesta confirmada y actualiza sólo los recursos indicados; no usar navegación, color o cierre del modal como prueba de persistencia.
- **Reintentos:** lecturas acotadas/manuales; mutaciones no se repiten automáticamente si el contrato no garantiza idempotencia. `401` limpia datos privados y ofrece retorno interno seguro.

## 8. Accesibilidad, responsive y pruebas previstas

- Aplicar DS-001: etiquetas visibles, orden semántico, foco visible, controles de 44 px, contraste AA y movimiento reducido. No anidar botones de favoritos dentro de enlaces de tarjeta.
- Anunciar progreso/resultado sin duplicar anuncios; error de campo con `aria-describedby`, feedback con `status`/`alert` según severidad.
- Modal/drawer: nombre accesible, foco atrapado cuando modal, cierre permitido según spec y retorno a un elemento existente. Tras eliminar, foco a siguiente elemento/título.
- Probar desktop y, cuando estén listos los frames, mobile con teclado, zoom/reflow y sin depender de hover. Si es correo: HTML/texto legible sin imágenes/scripts, no aplicar roles de app interactiva.

| Caso técnico | Verificación mínima |
|---|---|
| `RC-F-011-01` | controles deshabilitados en extremos. |
| `RC-F-011-02` | imagen fallida conserva texto. |
| `RC-F-011-03` | 404 neutral. |
| `RC-F-011-04` | visor Escape restaura foco. |
| `RC-F-011-05` | descripción maliciosa no ejecuta script. |
| Estados UI | Render y transición de cada estado de la sección 7 y de la spec visual relacionada. |
| Transporte | Fixture de éxito, vacío/no aplicable, validación, autorización, conflicto, timeout y fallo externo que realmente correspondan al contrato. |
| Accesibilidad | Teclado/foco, nombre de controles, anuncios y contraste; pruebas automáticas más revisión manual. |

Pruebas de componentes con mocks del contrato Marketplace; pruebas reales del adaptador externo sólo al cerrar la homologación aplicable. Una demo con mocks no acredita integración real.

## 9. Criterios de aceptación técnica

- [ ] `RC-F-011-CONTRATO`: props, callbacks, DTO y operaciones respetan las specs enlazadas sin campos/endpoints inventados.
- [ ] `RC-F-011-ESTADOS`: todos los estados aplicables tienen render, transición, foco y prueba, incluidos vacíos y errores.
- [ ] `RC-F-011-DATOS`: autorización en servidor, caché aislada por sesión y ninguna persistencia de datos externos o secretos prohibidos.
- [ ] `RC-F-011-PRUEBAS`: casos de la sección 8 pasan y quedan evidencias vinculadas a las tareas.
- [ ] `RC-F-011-INTEGRACION`: condiciones de entrada resueltas y prueba de contrato externa aprobada antes de habilitar el flujo real.

## 10. Condiciones pendientes y límites de implementación

I-01; detalle no entrega SKU simple: resolver en contrato variantes F-013, cerrar shape hasVariants=false.

Estos pendientes no se resuelven inventando rutas ni comportamiento. El [registro de decisiones](../../plan/DECISIONES-Y-BLOQUEOS.md) separa las soluciones locales propuestas de las confirmaciones externas. Se puede diseñar, construir componentes puros y probar mocks sin activar una integración bloqueada.

