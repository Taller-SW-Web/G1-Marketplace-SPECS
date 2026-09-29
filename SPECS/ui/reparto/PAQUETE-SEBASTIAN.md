# Paquete de Sebastián — carrito, favoritos y filtros mobile

## 1. Control del paquete

| Campo | Valor |
|---|---|
| Responsable | Sebastián Malca |
| Revisor principal | Diego Espinoza |
| Sistema de diseño | [`DS-001` v0.2.0](../DS-001-sistema-diseno-marketplace.md) |
| Alcance | 6 entregables visuales |
| Carga | **43 puntos** |
| Estado | Preparado para aceptación del integrante |

## 2. Entregables

| Orden | Spec | Resultado | Puntos |
|---:|---|---|---:|
| 1 | [`V-008` Carrito](../vistas/V-008-carrito.md) | Edición, validación y fusión del carrito | 11 |
| 2 | [`V-009` Favoritos](../vistas/V-009-favoritos.md) | Lista guardada y movimiento al carrito | 8 |
| 3 | [`O-001` Filtros mobile](../overlays/O-001-filtros-mobile.md) | Filtros de catálogo y pedidos | 10 |
| 4 | [`O-005` Producto agregado](../overlays/O-005-producto-agregado-carrito.md) | Confirmación inmediata de adición | 3 |
| 5 | [`O-006` Deshacer eliminación](../overlays/O-006-deshacer-eliminacion.md) | Recuperación temporal de carrito/favoritos | 6 |
| 6 | [`O-007` Resultado de fusión](../overlays/O-007-resultado-fusion-carrito.md) | Resumen de ajustes tras iniciar sesión | 5 |
| **Total** | — | — | **43** |

## 3. Frames exactos

### `V-008`

- `V-008 / Desktop / Válido autenticado`
- `V-008 / Mobile / Válido anónimo`
- `V-008 / Desktop / Cargando`
- `V-008 / Mobile / Vacío`
- `V-008 / Desktop / Atención`
- `V-008 / Mobile / Cantidad actualizando`
- `V-008 / Desktop / Cantidad ajustada`
- `V-008 / Mobile / Error de cantidad`
- `V-008 / Desktop / Moviendo a favoritos`
- `V-008 / Mobile / Fusión fallida`
- `V-008 / Desktop / Error de carga`

### `V-009`

- `V-009 / Desktop / Con favoritos`
- `V-009 / Mobile / Con favoritos`
- `V-009 / Desktop / Cargando`
- `V-009 / Mobile / Vacío`
- `V-009 / Desktop / Producto no disponible`
- `V-009 / Mobile / Error catálogo`
- `V-009 / Desktop / Moviendo`
- `V-009 / Mobile / Variante requerida`
- `V-009 / Desktop / Movimiento exitoso`
- `V-009 / Mobile / Error al mover`

### `O-001`

- `O-001 / Mobile / Catálogo aplicado`
- `O-001 / Mobile / Catálogo error rango`
- `O-001 / Mobile / Pedidos aplicado`
- `O-001 / Mobile / Pedidos error rango`

### `O-005`

- `O-005 / Desktop / Línea creada`
- `O-005 / Mobile / Línea creada`
- `O-005 / Desktop / Cantidad ajustada`
- `O-005 / Mobile / Cantidad ajustada`

### `O-006`

- `O-006 / Desktop / Carrito`
- `O-006 / Mobile / Favoritos`
- `O-006 / Desktop / Restaurado con ajuste`
- `O-006 / Mobile / No restaurado`

### `O-007`

- `O-007 / Desktop / Sin ajustes`
- `O-007 / Mobile / Cantidad limitada`
- `O-007 / Desktop / Varios ajustes`
- `O-007 / Mobile / Producto no elegible`

## 4. Dependencias compartidas

- Reutilizar `ProductCard` de Leonidas y acordar la variante compacta de línea de carrito/favorito.
- `O-001` es consumido por `V-006` de Leonidas y `V-015` de Diego; acordar un patrón único con configuración por contexto.
- La autenticación para favoritos usa `O-003` de Giuliano y debe preservar retorno/intención.
- `V-008` entrega contexto a `V-010`–`V-014` de Jim; alinear resumen, importes, alertas de stock y CTA de checkout.
- `O-007` debe corresponder con los estados de fusión documentados en `V-001` de Giuliano.

## 5. Decisiones abiertas que deben revisarse

| Entregable | IDs |
|---|---|
| `V-008` | `V-008-OPEN-01` a `V-008-OPEN-04` |
| `V-009` | `V-009-OPEN-01` a `V-009-OPEN-04` |
| `O-001` | `O-001-OPEN-01` a `O-001-OPEN-03` |
| `O-005` | `O-005-OPEN-01` a `O-005-OPEN-02` |
| `O-006` | `O-006-OPEN-01` a `O-006-OPEN-03` |
| `O-007` | `O-007-OPEN-01` a `O-007-OPEN-03` |

## 6. Orden de ejecución recomendado

1. Acordar línea de producto, controles de cantidad y variante compacta de `ProductCard`.
2. Diseñar `V-008`, porque define la mayor parte de los componentes del paquete.
3. Diseñar `O-005`, `O-006` y `O-007` sobre los estados ya fijados del carrito.
4. Diseñar `V-009` reutilizando los componentes compartidos.
5. Diseñar `O-001` con Leonidas y Diego para los dos contextos de uso.
6. Completar enlaces de Figma y solicitar revisión de Diego.

## 7. Definition of Ready del paquete

- [ ] Sebastián acepta alcance, carga y revisor.
- [ ] Las decisiones abiertas bloqueantes están resueltas o tienen supuesto aprobado.
- [ ] Línea de producto, selector de cantidad y filtros mobile son componentes compartidos.
- [ ] Todos los frames de la sección 3 existen con esos nombres exactos.
- [ ] Cada spec enlaza su sección o frame de Figma.
- [ ] Vacíos, conflictos, reintentos, deshacer, foco y responsive fueron comprobados.
- [ ] Diego revisó el paquete y Sebastián cerró las observaciones.
