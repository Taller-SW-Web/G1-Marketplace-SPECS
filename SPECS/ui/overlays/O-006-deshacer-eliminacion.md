# Overlay — O-006 Deshacer eliminación

> Feedback con acción temporal para recuperar una línea retirada del carrito o una tarjeta quitada de favoritos.

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID | `O-006` |
| Nombre | Deshacer eliminación |
| Tipo | Toast persistente temporal con acción |
| Versión | `0.1.0` |
| Estado | En revisión |
| Responsable | Sebastián Malca |
| Revisor | Diego Espinoza |
| Sistema de diseño | [`DS-001`](../DS-001-sistema-diseno-marketplace.md) |
| Enlace de Figma | Pendiente |

## 2. Propósito y trazabilidad

- **Propósito:** comunicar una eliminación confirmada y ofrecer una ventana breve para intentar restaurarla.
- **Funcionalidades:** `F-018` Quitar ítem del carrito y `F-038` Quitar favorito.
- **Vistas que lo invocan:** [`V-008`](../vistas/V-008-carrito.md) y [`V-009`](../vistas/V-009-favoritos.md).
- **Specs UI de origen:** [`UI F-018`](../F-018-quitar-item-carrito.md) y [`UI F-038`](../F-038-quitar-favorito.md).

> [!WARNING]
> El patrón visual no prueba que la restauración sea técnicamente reversible. Debe conectarse a una operación definida: en favoritos puede reutilizar F-036; en carrito debe revalidar SKU, cantidad, precio y stock. Si esa operación no se aprueba, se reemplaza “Deshacer” por confirmación informativa sin prometer recuperación.

## 3. Activación y cierre

| Evento | Condición | Resultado |
|---|---|---|
| Abrir | DELETE confirmado o eliminación optimista respaldada por estrategia segura | Elemento sale de la colección y aparece mensaje por 5 segundos. |
| Deshacer | Acción dentro de ventana | Inicia restauración; pausa expiración y evita doble solicitud. |
| Restauración confirmada | Operación exitosa | Elemento vuelve en posición comprensible y se anuncia. |
| Restauración ajustada | Carrito revalida una cantidad menor | Línea vuelve con cantidad confirmada y explicación. |
| Restauración fallida | Producto/SKU no disponible o error | Elemento no reaparece como éxito; mensaje y salida apropiada. |
| Expirar/cerrar | Sin acción | Toast cierra; eliminación permanece. |

## 4. Estructura, contenido y acciones

```text
O-006 Deshacer eliminación
├── Mensaje contextual
├── Acción “Deshacer”
├── Indicador temporal no exclusivo
└── Cerrar
```

| Región | Contenido | Acción | Prioridad |
|---|---|---|---|
| Mensaje carrito | “Quitaste {producto} del carrito” | Informar | Primaria |
| Mensaje favoritos | “Quitaste {producto} de favoritos” | Informar | Primaria |
| Deshacer | Texto completo | Restaurar | Primaria |
| Cerrar | Icono + nombre accesible | Confirmar eliminación visual | Secundaria |

## 5. Estados y variantes

| Estado o variante | Cuándo aparece | Cambio visual | Frame requerido |
|---|---|---|---|
| Carrito — disponible | Línea retirada | Producto y “Deshacer” | Sí |
| Favoritos — disponible | Tarjeta retirada | Producto y “Deshacer” | Sí |
| Deshaciendo | Acción activada | Progreso y controles bloqueados | Sí, anotado |
| Restaurado | Operación confirmada | Mensaje breve de restauración; foco válido | Sí |
| Restaurado con ajuste | Cantidad original ya no es posible | Cantidad confirmada y explicación | Sí |
| No se pudo restaurar | Producto/SKU/error | Mensaje neutral y acción Ver producto/Reintentar según caso | Sí |
| Último elemento retirado | La vista pasa a vacío | Toast permanece sobre estado vacío sin ocultar CTA | Sí, anotado |

## 6. Responsive y accesibilidad

- Desktop: toast en región consistente sin cubrir resumen, paginación o acciones.
- Mobile: ancho disponible y área segura; no tapa CTA ni navegación inferior.
- Usa `aria-live="polite"`; errores de restauración pueden usar anuncio más urgente sin repetir.
- No roba foco al aparecer. “Deshacer” entra en el orden de foco y el temporizador se pausa con foco/hover.
- La disponibilidad temporal se comunica con texto suficiente; una barra animada no es la única señal.
- Tras restaurar, foco vuelve a la línea/tarjeta o a un encabezado cercano según origen.
- Al expirar, no mueve el foco ni elimina un control actualmente enfocado sin aviso.

## 7. Frames requeridos

| Frame | Plataforma | Estado |
|---|---|---|
| `O-006 / Desktop / Carrito` | Desktop | Deshacer disponible |
| `O-006 / Mobile / Favoritos` | Mobile | Deshacer disponible |
| `O-006 / Desktop / Restaurado con ajuste` | Desktop | Ajuste |
| `O-006 / Mobile / No restaurado` | Mobile | Error |

## 8. Criterios de aceptación visual

- [ ] `UI-O006-001`: El mensaje identifica el elemento y la colección afectada.
- [ ] `UI-O006-002`: “Deshacer” sólo se muestra cuando existe una operación de restauración implementable y segura.
- [ ] `UI-O006-003`: El temporizador se pausa durante interacción y no constituye la única indicación de tiempo.
- [ ] `UI-O006-004`: Restauración de carrito puede ajustar/fallar por stock y nunca promete recuperar precio histórico.
- [ ] `UI-O006-005`: Fallo no muestra el elemento como restaurado y mantiene un foco válido.
- [ ] `UI-O006-006`: Al quitar el último elemento, el toast no oculta el estado vacío ni su CTA.
- [ ] El overlay cumple `DS-001` y no depende sólo del color.

## 9. Decisiones pendientes

| ID | Pregunta o decisión | Responsable | Estado |
|---|---|---|---|
| `O-006-OPEN-01` | Definir contrato de restauración del carrito y tratamiento de cantidad/precio/stock cambiados. | Backend + Producto | Abierta |
| `O-006-OPEN-02` | Confirmar que favoritos reutiliza F-036 y cómo se resuelve si el producto dejó de estar activo. | Backend | Abierta |
| `O-006-OPEN-03` | Validar duración de 5 segundos con accesibilidad y preferencia de tiempo extendido. | UX/UI + QA | Abierta |
