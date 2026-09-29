# Overlay — O-008 Resultado de reordenado

> Resumen de los productos de un pedido anterior que fueron agregados, ajustados o rechazados al intentar copiarlos al carrito actual.

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID | `O-008` |
| Nombre | Resultado de reordenado |
| Tipo | Modal de resultado |
| Versión | `0.1.0` |
| Estado | En revisión |
| Responsable | Diego Espinoza |
| Revisor | Sebastián Malca |
| Sistema de diseño | [`DS-001`](../DS-001-sistema-diseno-marketplace.md) |
| Enlace de Figma | Pendiente |

## 2. Propósito y trazabilidad

- **Propósito:** explicar el resultado total o parcial de copiar líneas históricas al carrito con datos actuales.
- **Funcionalidad:** `F-031` Reordenar una compra anterior.
- **Vista que lo invoca:** [`V-016`](../vistas/V-016-detalle-reordenado.md).
- **Spec UI de origen:** [`UI F-031`](../F-031-reordenar-compra.md).

El overlay no representa una compra, orden, reserva o restauración del precio/cupón/dirección históricos.

## 3. Activación y cierre

| Evento | Condición | Resultado |
|---|---|---|
| Abrir | F-031 responde resultado confirmado | Presenta líneas agrupadas por resultado. |
| Ver carrito | Existe al menos una línea agregada/ajustada | Navega a [`V-008`](../vistas/V-008-carrito.md). |
| Cerrar | Acción, Escape o fondo según patrón | Vuelve a `V-016`; no revierte adiciones. |
| Explorar alternativas | Ninguna línea agregada, si se aprueba | Abre `V-006` o cierra para revisar el pedido. |

Errores sin mutación confirmada permanecen en `V-016`/`O-010`; este overlay sólo muestra un resultado conocido.

## 4. Estructura, contenido y acciones

```text
O-008 Resultado de reordenado
├── Título según resultado
├── Explicación: productos agregados al carrito, no compra
├── Agregados
│   └── producto/SKU + cantidad confirmada
├── Ajustados
│   └── solicitada vs confirmada + motivo
├── No disponibles
│   └── producto/SKU + motivo público
├── “Ver carrito”, condicional
└── “Cerrar” / “Explorar productos”
```

| Región | Contenido | Acción | Prioridad |
|---|---|---|---|
| Encabezado | Resultado general | Informar | Primaria |
| Agregados | Producto y cantidad | Revisar | Primaria |
| Ajustados | Diferencia y motivo | Revisar | Primaria |
| No disponibles | Elemento y explicación | Revisar | Primaria |
| Ver carrito | CTA | Abrir `V-008` | Primaria si hay agregados |
| Cerrar/explorar | Acción secundaria | Volver o explorar | Secundaria |

## 5. Estados y variantes

| Estado o variante | Cuándo aparece | Cambio visual | Frame requerido |
|---|---|---|---|
| Completo | Todas las líneas agregadas sin ajustes | Resumen positivo y lista agregada | Sí |
| Parcial | Hay agregadas y no disponibles/ajustadas | Tres grupos claramente separados | Sí |
| Con ajustes | Todas o algunas cantidades cambiaron | Solicitado vs confirmado | Sí |
| Ninguna agregada | `added: []` con ajustes/no disponibles | Título neutral, sin CTA “Ver carrito” si no cambió | Sí |
| Lista extensa | Muchos productos | Cuerpo desplazable; encabezado/acciones permanecen accesibles | Anotado |

## 6. Responsive y accesibilidad

- Desktop: modal medio/amplio con listas; mobile: diálogo/bottom sheet alta o pantalla casi completa.
- Foco inicial en título; trampa de foco y retorno al CTA de `V-016` al cerrar.
- Escape cierra sin revertir el carrito.
- Grupos usan encabezados y listas semánticas; iconos/colores son complementarios.
- Cada ajuste anuncia cantidad solicitada y confirmada en orden comprensible.
- El título no usa “Compra realizada” ni “Pedido creado”.
- Acciones permanecen visibles/alcanzables con listas largas.

## 7. Frames requeridos

| Frame | Plataforma | Estado |
|---|---|---|
| `O-008 / Desktop / Completo` | Desktop | Todo agregado |
| `O-008 / Mobile / Parcial` | Mobile | Agregado + no disponible |
| `O-008 / Desktop / Con ajustes` | Desktop | Cantidades cambiadas |
| `O-008 / Mobile / Ninguno agregado` | Mobile | Sin mutación útil |

## 8. Criterios de aceptación visual

- [ ] `UI-O008-001`: El título y el copy indican “agregado al carrito”, nunca compra o pedido confirmado.
- [ ] `UI-O008-002`: Resultado parcial separa agregados, ajustados y no disponibles.
- [ ] `UI-O008-003`: Cantidades históricas no se presentan como disponibles; se muestra la confirmada actual.
- [ ] `UI-O008-004`: “Ver carrito” sólo aparece como CTA principal cuando existe al menos una línea agregada.
- [ ] `UI-O008-005`: Cerrar no revierte las líneas confirmadas.
- [ ] `UI-O008-006`: Errores técnicos sin resultado conocido no se presentan como “ninguno agregado”.
- [ ] El overlay cumple `DS-001`, foco y lectura accesible.

## 9. Decisiones pendientes

| ID | Pregunta o decisión | Responsable | Estado |
|---|---|---|---|
| `O-008-OPEN-01` | Publicar motivos de ajuste/no disponibilidad y su copy de cliente. | Backend + Catálogo + UX | Abierta |
| `O-008-OPEN-02` | Confirmar si “Ninguno agregado” ofrece explorar catálogo o sólo cerrar. | Producto + UX | Abierta |
| `O-008-OPEN-03` | Definir garantía de reintento sin duplicar cantidades por SKU. | Backend | Abierta |
