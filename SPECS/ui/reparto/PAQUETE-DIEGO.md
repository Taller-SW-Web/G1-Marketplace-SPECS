# Paquete de Diego — pedidos, postentrega y despacho

## 1. Control del paquete

| Campo | Valor |
|---|---|
| Responsable | Diego Espinoza |
| Revisor principal | Sebastián Malca |
| Sistema de diseño | [`DS-001` v0.2.0](../DS-001-sistema-diseno-marketplace.md) |
| Alcance | 6 entregables visuales |
| Carga | **47 puntos** |
| Estado | Preparado para aceptación del integrante |

## 2. Entregables

| Orden | Spec | Resultado | Puntos |
|---:|---|---|---:|
| 1 | [`V-015` Historial de pedidos](../vistas/V-015-historial-pedidos.md) | Consulta y filtros de pedidos | 10 |
| 2 | [`V-016` Detalle y reordenado](../vistas/V-016-detalle-reordenado.md) | Detalle de orden y recompra | 9 |
| 3 | [`V-017` Seguimiento](../vistas/V-017-seguimiento.md) | Estado y cronología de despacho | 7 |
| 4 | [`O-008` Resultado de reordenado](../overlays/O-008-resultado-reordenado.md) | Resultado total/parcial de recompra | 5 |
| 5 | [`O-009` Evaluación postentrega](../overlays/O-009-evaluacion-postentrega.md) | Calificación y comentario | 9 |
| 6 | [`C-002` Actualización de despacho](../comunicaciones/C-002-correo-actualizacion-despacho.md) | Correo transaccional de estado | 7 |
| **Total** | — | — | **47** |

## 3. Frames exactos

### `V-015`

- `V-015 / Desktop / Con pedidos`
- `V-015 / Mobile / Con pedidos`
- `V-015 / Desktop / Con filtros`
- `V-015 / Mobile / Historial vacío`
- `V-015 / Desktop / Sin coincidencias`
- `V-015 / Mobile / Rango inválido`
- `V-015 / Desktop / Cargando`
- `V-015 / Mobile / Error recuperable`

### `V-016`

- `V-016 / Desktop / Detalle listo`
- `V-016 / Mobile / Detalle listo`
- `V-016 / Desktop / Sin tracking`
- `V-016 / Mobile / Reordenando`
- `V-016 / Desktop / Conflicto carrito`
- `V-016 / Mobile / Comercio no disponible`
- `V-016 / Desktop / Pedido no disponible`
- `V-016 / Mobile / Error detalle`

### `V-017`

- `V-017 / Desktop / Disponible`
- `V-017 / Mobile / Disponible`
- `V-017 / Desktop / Incidencia`
- `V-017 / Mobile / Entregado`
- `V-017 / Desktop / Aún sin despacho`
- `V-017 / Mobile / Pedido no disponible`
- `V-017 / Desktop / Error recuperable`
- `V-017 / Mobile / Cargando`

### `O-008`

- `O-008 / Desktop / Completo`
- `O-008 / Mobile / Parcial`
- `O-008 / Desktop / Con ajustes`
- `O-008 / Mobile / Ninguno agregado`

### `O-009`

- `O-009 / Desktop / Invitación`
- `O-009 / Mobile / Sin selección`
- `O-009 / Desktop / Bien`
- `O-009 / Mobile / Mal`
- `O-009 / Desktop / Enviada`
- `O-009 / Mobile / Error recuperable`

### `C-002`

- `C-002 / Desktop / Cambio normal`
- `C-002 / Mobile / Cambio normal`
- `C-002 / Desktop / Reprogramación`
- `C-002 / Mobile / Entregado`
- `C-002 / Mobile / Sin imágenes`

## 4. Dependencias compartidas

- Reutilizar de Jim el bloque de orden, resumen de importes y transición desde `V-014`.
- `V-015` consume `O-001` de Sebastián; validar fechas, aplicación, limpieza y errores del rango.
- `V-016` reordena hacia el carrito de Sebastián y consume `O-008`; acordar ajustes, conflictos y CTA final.
- `C-002` debe compartir cabecera, pie, ancho y reglas de fallback con `C-001` de Giuliano.
- La timeline de `V-017` debe servir como componente de referencia para estados de despacho en `V-016` y `C-002`.

## 5. Decisiones abiertas que deben revisarse

| Entregable | IDs |
|---|---|
| `V-015` | `V-015-OPEN-01` a `V-015-OPEN-04` |
| `V-016` | `V-016-OPEN-01` a `V-016-OPEN-04` |
| `V-017` | `V-017-OPEN-01` a `V-017-OPEN-04` |
| `O-008` | `O-008-OPEN-01` a `O-008-OPEN-03` |
| `O-009` | `O-009-OPEN-01` a `O-009-OPEN-04` |
| `C-002` | `C-002-OPEN-01` a `C-002-OPEN-04` |

## 6. Orden de ejecución recomendado

1. Acordar con Jim el bloque de pedido y con Sebastián los filtros mobile.
2. Diseñar `V-015` y fijar lista/tarjeta de pedido.
3. Diseñar `V-016` y `O-008` como un flujo continuo de recompra.
4. Diseñar la timeline en `V-017` y reutilizarla en detalle.
5. Diseñar `O-009` para el estado entregado.
6. Diseñar `C-002` coordinando la familia de correos con Giuliano.
7. Completar enlaces de Figma y solicitar revisión de Sebastián.

## 7. Definition of Ready del paquete

- [ ] Diego acepta alcance, carga y revisor.
- [ ] Las decisiones abiertas bloqueantes están resueltas o tienen supuesto aprobado.
- [ ] Tarjeta de pedido, timeline, filtros y bloque de email son componentes reutilizables.
- [ ] Todos los frames de la sección 3 existen con esos nombres exactos.
- [ ] Cada spec enlaza su sección o frame de Figma.
- [ ] Vacíos, filtros, tracking, recompra, postentrega, foco y responsive fueron comprobados.
- [ ] Sebastián revisó el paquete y Diego cerró las observaciones.
