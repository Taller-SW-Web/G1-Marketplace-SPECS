# Paquete de Fernando Saire — descubrimiento, producto y feedback global

## 1. Control del paquete

| Campo | Valor |
|---|---|
| Responsable | Fernando José Saire Tello |
| Revisor principal | Giuliano Macchiavello |
| Sistema de diseño | [`DS-001` v0.2.0](../DS-001-sistema-diseno-marketplace.md) |
| Alcance | 5 entregables visuales |
| Carga | **49 puntos** |
| Estado | Preparado para aceptación del integrante |

## 2. Entregables

| Orden | Spec | Resultado | Puntos |
|---:|---|---|---:|
| 1 | [`V-005` Inicio](../vistas/V-005-inicio.md) | Portada pública/autenticada y módulos de descubrimiento | 10 |
| 2 | [`V-006` Catálogo y resultados](../vistas/V-006-catalogo-resultados.md) | Búsqueda, filtros, orden y paginación | 12 |
| 3 | [`V-007` Ficha del producto](../vistas/V-007-ficha-producto.md) | Galería, variantes, precio, stock y compra | 11 |
| 4 | [`O-002` Visor de galería](../overlays/O-002-visor-galeria.md) | Exploración ampliada de imágenes | 7 |
| 5 | [`O-010` Alertas y feedback global](../overlays/O-010-alertas-feedback-global.md) | Toasts, banners, errores y estado offline | 9 |
| **Total** | — | — | **49** |

## 3. Frames exactos

### `V-005`

- `V-005 / Desktop / Público`
- `V-005 / Mobile / Público`
- `V-005 / Desktop / Autenticado`
- `V-005 / Mobile / Cargando`
- `V-005 / Desktop / Sin contenido`
- `V-005 / Mobile / Catálogo no disponible`
- `V-005 / Desktop / ProductCard favorita`
- `V-005 / Mobile / Producto no disponible`

### `V-006`

- `V-006 / Desktop / Catálogo`
- `V-006 / Mobile / Catálogo`
- `V-006 / Desktop / Búsqueda con filtros`
- `V-006 / Mobile / Resultados`
- `V-006 / Desktop / Cargando`
- `V-006 / Mobile / Sin resultados`
- `V-006 / Desktop / Query o rango inválido`
- `V-006 / Mobile / Catálogo no disponible`
- `V-006 / Desktop / Página intermedia`
- `V-006 / Mobile / ProductCard favorita`

### `V-007`

- `V-007 / Desktop / Producto simple`
- `V-007 / Mobile / Producto simple`
- `V-007 / Desktop / Variable sin selección`
- `V-007 / Mobile / Variante seleccionada`
- `V-007 / Desktop / Oferta vigente`
- `V-007 / Mobile / Agotado`
- `V-007 / Desktop / Precio o stock error`
- `V-007 / Mobile / Agregando`
- `V-007 / Desktop / Error de adición`
- `V-007 / Mobile / Imagen de respaldo`
- `V-007 / Desktop / Producto no disponible`
- `V-007 / Mobile / Error recuperable`

### `O-002`

- `O-002 / Desktop / Varias imágenes`
- `O-002 / Mobile / Varias imágenes`
- `O-002 / Desktop / Una imagen`
- `O-002 / Mobile / Imagen no disponible`

### `O-010`

- `O-010 / Desktop / Toast success`
- `O-010 / Mobile / Toast info`
- `O-010 / Desktop / Banner warning`
- `O-010 / Mobile / Error con reintento`
- `O-010 / Desktop / Cola priorizada`
- `O-010 / Mobile / Sin conexión`

## 4. Dependencias compartidas

- `ProductCard` es consumida también por Sebastián en carrito/favoritos; acordar variantes, favorito, disponibilidad e imagen de respaldo antes de duplicarla.
- `V-006` consume `O-001`, cuyo dueño es Sebastián. La apertura, aplicación y limpieza de filtros deben validarse juntos.
- `V-007` consume `O-002` y dispara `O-005`; coordinar con Sebastián los estados “agregando”, éxito y error.
- `O-010` es transversal a todos los paquetes: publicar reglas de prioridad, duración, acumulación, acción y comportamiento offline.
- Giuliano revisa que componentes y tokens permanezcan alineados con `DS-001`.

## 5. Decisiones abiertas que deben revisarse

| Entregable | IDs |
|---|---|
| `V-005` | `V-005-OPEN-01` a `V-005-OPEN-04` |
| `V-006` | `V-006-OPEN-01` a `V-006-OPEN-04` |
| `V-007` | `V-007-OPEN-01` a `V-007-OPEN-04` |
| `O-002` | `O-002-OPEN-01` a `O-002-OPEN-03` |
| `O-010` | `O-010-OPEN-01` a `O-010-OPEN-04` |

## 6. Orden de ejecución recomendado

1. Acordar con Giuliano las variantes base de cabecera, navegación, tarjeta y botones.
2. Diseñar `ProductCard` y `O-010` como componentes compartidos.
3. Diseñar `V-005` para validar portada, módulos y densidad responsive.
4. Diseñar `V-006` en coordinación con `O-001` de Sebastián.
5. Diseñar `V-007` y `O-002`; probar la continuidad hacia carrito/favoritos.
6. Completar enlaces de Figma y solicitar revisión de Giuliano.

## 7. Definition of Ready del paquete

- [ ] Fernando acepta alcance, carga y revisor.
- [ ] Las decisiones abiertas bloqueantes están resueltas o tienen supuesto aprobado.
- [ ] `ProductCard` y `O-010` están publicados como componentes reutilizables.
- [ ] Todos los frames de la sección 3 existen con esos nombres exactos.
- [ ] Cada spec enlaza su sección o frame de Figma.
- [ ] Filtros, imágenes, precios, disponibilidad, foco y responsive fueron comprobados.
- [ ] Giuliano revisó el paquete y Fernando cerró las observaciones.
