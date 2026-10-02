# Overlay — O-005 Producto agregado al carrito

> Feedback no modal que confirma una adición al carrito o explica un ajuste de cantidad sin obligar a abandonar la ficha.

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID | `O-005` |
| Nombre | Producto agregado al carrito |
| Tipo | Toast o banner de confirmación con acciones |
| Versión | `0.1.0` |
| Estado | En revisión |
| Responsable | Sebastián Malca |
| Revisor | Diego Espinoza |
| Sistema de diseño | [`DS-001`](../DS-001-sistema-diseno-marketplace.md) |
| Enlace de Figma | Pendiente |

## 2. Propósito y trazabilidad

- **Propósito:** confirmar que F-016 creó/incrementó la línea o ajustó la cantidad al máximo disponible.
- **Funcionalidad:** `F-016` Agregar ítem al carrito.
- **Vista que lo invoca:** [`V-007`](../vistas/V-007-ficha-producto.md).
- **Spec UI de origen:** [`UI F-016`](../F-016-agregar-item-carrito.md).

Errores que no mutan el carrito permanecen junto al CTA de `V-007` o usan `O-010`; este overlay sólo aparece tras un resultado confirmado.

## 3. Activación y cierre

| Evento | Condición | Resultado |
|---|---|---|
| Abrir éxito | API confirma creación/incremento | Anuncia producto/cantidad de forma breve. |
| Abrir ajustado | API confirma carrito con límite | Explica que se ajustó la cantidad, sin exponer saldo interno. |
| Ver carrito | Acción explícita | Navega a [`V-008`](../vistas/V-008-carrito.md). |
| Seguir comprando/cerrar | Acción explícita | Cierra y conserva foco/contexto de `V-007`. |
| Expiración | Tiempo suficiente y sin foco dentro | Cierra sin alterar carrito. |

## 4. Estructura, contenido y acciones

```text
O-005 Producto agregado
├── Icono + título de resultado
├── Nombre/variante resumidos
├── Cantidad confirmada o ajuste
├── “Ver carrito”
├── “Seguir comprando”
└── Cerrar
```

| Región | Contenido | Acción | Prioridad |
|---|---|---|---|
| Resultado | “Producto agregado al carrito” | Informar | Primaria |
| Resumen | Producto, variante y cantidad confirmada | Informar | Primaria |
| Ajuste | “Ajustamos la cantidad disponible en tu carrito” | Informar | Primaria condicional |
| Ver carrito | CTA | Abrir `V-008` | Primaria |
| Continuar | Acción secundaria | Cerrar | Secundaria |

No muestra subtotal o total de checkout; el precio de ficha es informativo y el carrito se revalida.

## 5. Estados y variantes

| Estado o variante | Cuándo aparece | Cambio visual | Frame requerido |
|---|---|---|---|
| Línea creada | `201` | Mensaje de nueva línea y cantidad 1 | Sí |
| Línea incrementada | `200` | Cantidad total confirmada | Sí, anotado |
| Cantidad ajustada | `409 STOCK_LIMIT_REACHED` con carrito confirmado/ajustado | Mensaje de ajuste, no error total | Sí |
| Cierre temporizado pausado | Foco/hover dentro | Permanece hasta interacción o nuevo tiempo suficiente | No; documentar |

## 6. Responsive y accesibilidad

- Desktop: toast/banner en región consistente, sin cubrir navegación ni CTA de compra.
- Mobile: banner inferior o superior que respeta áreas seguras y no tapa CTA persistente, variantes o teclado.
- No roba foco al abrir; usa `aria-live="polite"` para éxito y mensaje apropiado para ajuste.
- Acciones son alcanzables por teclado antes de expirar; el temporizador se pausa con foco/hover.
- Cerrar tiene nombre accesible; al cerrar manualmente, foco permanece o vuelve al CTA de agregar según interacción.
- Éxito y ajuste usan texto/icono además de color.

## 7. Frames requeridos

| Frame | Plataforma | Estado |
|---|---|---|
| `O-005 / Desktop / Línea creada` | Desktop | Éxito |
| `O-005 / Mobile / Línea creada` | Mobile | Éxito |
| `O-005 / Desktop / Cantidad ajustada` | Desktop | Ajuste |
| `O-005 / Mobile / Cantidad ajustada` | Mobile | Ajuste |

## 8. Criterios de aceptación visual

- [ ] `UI-O005-001`: Sólo aparece después de una mutación confirmada del carrito.
- [ ] `UI-O005-002`: Diferencia línea creada, incrementada y cantidad ajustada mediante texto comprensible.
- [ ] `UI-O005-003`: “Ver carrito” abre `V-008`; cerrar conserva `V-007` y no revierte la adición.
- [ ] `UI-O005-004`: No muestra total final ni afirma reserva de stock.
- [ ] `UI-O005-005`: No roba foco y su expiración se pausa durante interacción.
- [ ] El overlay cumple `DS-001` y no depende sólo del color.

## 9. Decisiones pendientes

| ID | Pregunta o decisión | Responsable | Estado |
|---|---|---|---|
| `O-005-OPEN-01` | Definir duración, posición y convivencia con CTA persistente mobile. | UX/UI | Abierta |
| `O-005-OPEN-02` | Confirmar datos mínimos permitidos en el resumen del producto/variante. | Producto + UX | Abierta |
