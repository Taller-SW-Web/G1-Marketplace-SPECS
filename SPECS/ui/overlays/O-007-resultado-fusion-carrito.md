# Overlay — O-007 Resultado de fusión del carrito

> Resumen posterior al login que informa los ajustes aplicados al combinar el carrito anónimo con el carrito autenticado.

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID | `O-007` |
| Nombre | Resultado de fusión del carrito |
| Tipo | Modal/resumen cuando hay ajustes; feedback breve cuando no los hay |
| Versión | `0.1.0` |
| Estado | En revisión |
| Responsable | Sebastián Malca |
| Revisor | Diego Espinoza |
| Sistema de diseño | [`DS-001`](../DS-001-sistema-diseno-marketplace.md) |
| Enlace de Figma | Pendiente |

## 2. Propósito y trazabilidad

- **Propósito:** explicar el resultado determinista de F-020 sin pedir al usuario resolver duplicados.
- **Funcionalidad:** `F-020` Fusionar carrito anónimo al iniciar sesión.
- **Vistas relacionadas:** [`V-001`](../vistas/V-001-inicio-sesion.md) y [`V-008`](../vistas/V-008-carrito.md); puede aparecer al retornar a otra vista de origen.
- **Spec UI de origen:** [`UI F-020`](../F-020-fusionar-carrito-anonimo.md).

## 3. Activación y cierre

| Evento | Condición | Resultado |
|---|---|---|
| Fusión sin ajustes | `merged:true` y lista vacía | Feedback breve “Actualizamos tu carrito”; no bloquea retorno. |
| Fusión con ajustes | Cantidades/SKU ajustados | Abre resumen con cada cambio comprensible. |
| Ver carrito | Acción explícita | Navega a [`V-008`](../vistas/V-008-carrito.md) y resalta cambios una vez. |
| Continuar | Cerrar | Regresa a la ruta/acción de origen. |
| Cerrar/Escape | Modal de ajustes | Cierra; la fusión no se revierte. |

Un error previo al commit no abre un resumen exitoso: se comunica mediante la vista de acceso/carrito y `O-010`, con sesión iniciada y acción Reintentar.

## 4. Estructura, contenido y acciones

```text
O-007 Resultado de fusión
├── Título “Actualizamos tu carrito”
├── Explicación breve
├── Lista de ajustes
│   └── producto/SKU comprensible + solicitado + confirmado + motivo
├── “Ver carrito”
└── “Continuar” / Cerrar
```

| Región | Contenido | Acción | Prioridad |
|---|---|---|---|
| Encabezado | Resultado de combinación | Informar | Primaria |
| Ajustes | Productos y cantidades | Revisar | Primaria condicional |
| Ver carrito | CTA | Abrir `V-008` | Primaria |
| Continuar | Acción secundaria | Cerrar y volver | Secundaria |

No muestra dos carritos, reglas internas de bloqueo, saldo exacto de inventario, IDs técnicos o decisiones sobre duplicados.

## 5. Estados y variantes

| Estado o variante | Cuándo aparece | Cambio visual | Frame requerido |
|---|---|---|---|
| Fusionado sin ajustes | Carritos combinados exactamente | Toast/banner breve | Sí |
| Cantidad limitada | Suma supera máximo confirmado | Solicitado vs confirmado + motivo amigable | Sí |
| Producto no elegible | SKU dejó de estar disponible según resultado permitido | Elemento y explicación, sin borrado ambiguo | Sí |
| Varios ajustes | Más de un elemento | Lista desplazable con resumen; acciones siempre alcanzables | Sí |
| Sin carrito anónimo | `merged:false` | No se muestra overlay; login continúa normalmente | No |

## 6. Responsive y accesibilidad

- Desktop: modal de tamaño medio sólo con ajustes; feedback breve para resultado simple.
- Mobile: diálogo/bottom sheet alta con lista desplazable; acciones no quedan fuera de alcance.
- Foco inicial en título del resumen; trampa de foco sólo en variante modal.
- Escape/cerrar devuelve foco/contexto de la vista de origen; no revierte la fusión.
- Cada ajuste se expresa con nombre, cantidad solicitada/confirmada y motivo textual, no sólo color.
- La lista usa estructura semántica y el total de ajustes se anuncia.
- `aria-live` informa el resultado simple sin robar foco.

## 7. Frames requeridos

| Frame | Plataforma | Estado |
|---|---|---|
| `O-007 / Desktop / Sin ajustes` | Desktop | Feedback breve |
| `O-007 / Mobile / Cantidad limitada` | Mobile | Modal con ajuste |
| `O-007 / Desktop / Varios ajustes` | Desktop | Lista |
| `O-007 / Mobile / Producto no elegible` | Mobile | Ajuste crítico |

## 8. Criterios de aceptación visual

- [ ] `UI-O007-001`: La interfaz muestra un único carrito final y nunca pide elegir cómo resolver duplicados.
- [ ] `UI-O007-002`: Cada ajuste diferencia cantidad solicitada y confirmada sin exponer inventario interno.
- [ ] `UI-O007-003`: `merged:false` no genera un modal innecesario.
- [ ] `UI-O007-004`: “Ver carrito” lleva a `V-008`; cerrar no revierte la fusión.
- [ ] `UI-O007-005`: Un fallo previo al commit no se presenta como fusión exitosa ni afirma pérdida de productos.
- [ ] El overlay cumple `DS-001`, foco y lectura accesible.

## 9. Decisiones pendientes

| ID | Pregunta o decisión | Responsable | Estado |
|---|---|---|---|
| `O-007-OPEN-01` | Publicar todos los códigos de ajuste y su copy comprensible. | Backend + UX | Abierta |
| `O-007-OPEN-02` | Confirmar umbral entre feedback breve y modal de resumen. | Producto + UX | Abierta |
| `O-007-OPEN-03` | Definir cómo identificar visualmente un producto si la respuesta sólo entrega SKU. | Backend + Catálogo | Abierta |
