# Overlay — O-001 Filtros mobile

> Panel accesible para editar y aplicar filtros en pantallas estrechas. Tiene variantes de catálogo y de historial de pedidos.

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID | `O-001` |
| Nombre | Filtros mobile |
| Tipo | Drawer modal / diálogo de pantalla parcial o completa |
| Versión | `0.1.0` |
| Estado | En revisión |
| Responsable | Sebastián Malca |
| Revisor | Diego Espinoza |
| Sistema de diseño | [`DS-001`](../DS-001-sistema-diseno-marketplace.md) |
| Enlace de Figma | Pendiente |

## 2. Propósito y trazabilidad

- **Propósito:** permitir editar criterios complejos sin comprimir la grilla/lista mobile y aplicarlos de forma explícita.
- **Funcionalidades:** `F-008` Filtrar catálogo y `F-029` Filtrar historial.
- **Vistas que lo invocan:** [`V-006`](../vistas/V-006-catalogo-resultados.md) y [`V-015`](../vistas/V-015-historial-pedidos.md).
- **Specs UI de origen:** [`UI F-008`](../F-008-filtrar-catalogo.md) y [`UI F-029`](../F-029-filtrar-historial-pedidos.md).

La variante se determina por la vista invocadora. Nunca muestra simultáneamente filtros comerciales y de pedidos.

## 3. Activación y cierre

| Evento | Condición | Resultado |
|---|---|---|
| Abrir | Pulsar “Filtros” en `V-006` o `V-015` | Copia los criterios aplicados a un borrador y enfoca el título. |
| Modificar | Cambiar controles | Sólo cambia el borrador; resultados y URL permanecen iguales. |
| Aplicar | Borrador válido | Actualiza URL, reinicia página, cierra y enfoca encabezado de resultados. |
| Limpiar | Existen valores en borrador/aplicados | Vacía el borrador; requiere Aplicar para actualizar resultados. |
| Cancelar/cerrar | Botón Cerrar, Escape o gesto aprobado | Descarta el borrador y conserva criterios aplicados. |
| Fondo | Panel modal abierto | No cierra si provocaría pérdida accidental sin señal clara; comportamiento consistente con DS-001. |

## 4. Estructura, contenido y acciones

```text
O-001 Filtros mobile
├── Encabezado
│   ├── Título “Filtros”
│   ├── cantidad de filtros aplicados
│   └── Cerrar
├── Cuerpo desplazable
│   ├── Variante catálogo
│   │   ├── Categorías
│   │   ├── Marcas
│   │   └── Precio mínimo/máximo
│   └── Variante pedidos
│       ├── Estado
│       └── Fecha desde/hasta
└── Pie de acciones
    ├── Limpiar
    └── Aplicar filtros
```

| Región | Contenido | Acción | Prioridad |
|---|---|---|---|
| Encabezado | Título y cierre | Cerrar sin aplicar | Primaria |
| Grupos | Controles etiquetados | Editar borrador | Primaria |
| Resumen | Cantidad/criterios | Comprender cambios | Secundaria |
| Limpiar | Acción secundaria | Vaciar borrador | Secundaria |
| Aplicar | CTA “Aplicar filtros” | Validar y actualizar vista | Primaria |

## 5. Estados y variantes

| Estado o variante | Cuándo aparece | Cambio visual | Frame requerido |
|---|---|---|---|
| Catálogo — sin filtros | `V-006` sin criterios | Grupos vacíos; Limpiar inactivo | Sí |
| Catálogo — aplicados | `V-006` con criterios | Valores seleccionados y contador | Sí |
| Catálogo — rango inválido | Mínimo negativo o mayor al máximo | Errores asociados; Aplicar inactivo | Sí |
| Pedidos — sin filtros | `V-015` sin criterios | Estado “Todos” y fechas vacías | Sí |
| Pedidos — aplicados | Estado/rango existente | Valores y contador | Sí |
| Pedidos — rango inválido | Desde > Hasta o intervalo > un año | Error vinculado a ambas fechas | Sí |
| Aplicando | Solicitud iniciada tras validar | CTA ocupado; cierre evita doble envío | Sí, variante anotada |

Los resultados vacíos o errores de servidor se muestran en la vista que invocó el overlay, no dentro de este panel ya cerrado.

## 6. Responsive y accesibilidad

- Se usa únicamente cuando el panel lateral deja de ser apropiado; desktop conserva filtros visibles en la página.
- En mobile puede ser drawer lateral, bottom sheet alta o diálogo de pantalla completa según el patrón aprobado, pero debe permitir contenido largo y teclado sin ocultar acciones.
- Al abrir, el foco llega al título o primer control; existe trampa de foco por ser modal.
- Escape y botón Cerrar descartan el borrador; al cerrar, foco vuelve al botón “Filtros”.
- Fondo bloqueado para scroll y marcado como no interactivo.
- Grupos usan `fieldset`/`legend`; errores de rango se asocian a ambos campos.
- Contador y selección no dependen sólo de color.
- Pie de acciones permanece alcanzable sin tapar campos ni mensajes con teclado abierto.

## 7. Frames requeridos

| Frame | Plataforma | Estado |
|---|---|---|
| `O-001 / Mobile / Catálogo aplicado` | Mobile | Criterios de categoría, marca y precio |
| `O-001 / Mobile / Catálogo error rango` | Mobile | Validación |
| `O-001 / Mobile / Pedidos aplicado` | Mobile | Estado y fechas |
| `O-001 / Mobile / Pedidos error rango` | Mobile | Validación |

No requiere frame desktop: allí los filtros están integrados en `V-006` y `V-015`.

## 8. Criterios de aceptación visual

- [ ] `UI-O001-001`: Cancelar o cerrar no cambia filtros aplicados, resultados ni URL.
- [ ] `UI-O001-002`: Aplicar criterios válidos actualiza la vista, reinicia página y devuelve foco al encabezado de resultados.
- [ ] `UI-O001-003`: Rangos inválidos bloquean Aplicar y no generan solicitudes.
- [ ] `UI-O001-004`: Catálogo y pedidos usan variantes separadas y comprensibles.
- [ ] `UI-O001-005`: El panel gestiona foco, Escape, scroll del fondo y retorno al invocador.
- [ ] `UI-O001-006`: Limpiar afecta primero el borrador y sólo actualiza resultados al aplicar.
- [ ] El overlay cumple `DS-001` y no introduce nuevos criterios funcionales.

## 9. Decisiones pendientes

| ID | Pregunta o decisión | Responsable | Estado |
|---|---|---|---|
| `O-001-OPEN-01` | Aprobar drawer, bottom sheet alta o pantalla completa como patrón mobile definitivo. | UX/UI | Abierta |
| `O-001-OPEN-02` | Confirmar componente y localización del selector de rango de fechas. | UX/UI | Abierta |
| `O-001-OPEN-03` | Definir si el CTA muestra una cantidad de resultados prevista; no incorporarla sin contrato. | Producto + Backend | Abierta |
