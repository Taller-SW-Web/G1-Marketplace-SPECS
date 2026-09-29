# Vista — V-016 Detalle y reordenado

> Pantalla privada para revisar el snapshot histórico de un pedido propio y agregar al carrito actual las líneas que todavía sean elegibles.

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID | `V-016` |
| Nombre | Detalle y reordenado |
| Ruta | `/mis-pedidos/{orderId}` |
| Versión | `0.1.0` |
| Estado | En revisión |
| Responsable | Diego Espinoza |
| Revisor | Sebastián Malca |
| Sistema de diseño | [`DS-001`](../DS-001-sistema-diseno-marketplace.md) |
| Enlace de Figma | Pendiente |

## 2. Propósito, actor y acceso

- **Objetivo del usuario:** comprender qué compró, cuánto pagó, dónde se entregó y cómo evolucionó el pedido; opcionalmente volver a agregar productos disponibles al carrito.
- **Actor principal:** cliente autenticado propietario del pedido.
- **Permiso:** privado; conocer `orderId` no concede acceso.
- **Condición de entrada:** pedido seleccionado desde `V-015`, `V-014` o comunicación autorizada.
- **Resultado esperado:** detalle histórico legible y, si se solicita, resultado explícito del reordenado sin crear una compra nueva.

## 3. Trazabilidad

| Funcionalidad | Spec funcional | Spec UI de origen | Aporte a esta vista |
|---|---|---|---|
| `F-030` | [`Visualizar detalle`](../../funcional/F-030-detalle-pedido.md) | [`UI F-030`](../F-030-detalle-pedido.md) | Snapshot, líneas, importes, entrega e historial de estados. |
| `F-031` | [`Reordenar compra`](../../funcional/F-031-reordenar-compra.md) | [`UI F-031`](../F-031-reordenar-compra.md) | Revalidación, adición parcial y resultado. |

Contratos consultados: [`API F-030`](../../contrato-api/F-030-detalle-pedido.md) y [`API F-031`](../../contrato-api/F-031-reordenar-compra.md).

## 4. Entradas, salidas y conservación de contexto

| Origen o acción | Destino | Condición | Contexto que se conserva |
|---|---|---|---|
| Pedido en `V-015` | `V-016` | Pedido propio | Filtros, página y scroll para volver. |
| `V-014` → “Ver mi pedido” | `V-016` | Pedido recién creado | Sesión y `orderId`. |
| Enlace de `C-001` | `V-016` | Autenticación y propiedad válidas | Sólo `orderId`; no tokens visibles permanentes. |
| “Volver a mis pedidos” | `V-015` | Acción explícita | Filtros/página anteriores si existen. |
| “Seguir envío” | `V-017` | Existe tracking | Pedido seleccionado. |
| `O-008` → “Ver carrito” | `V-008` | Reordenado total/parcial | Carrito actualizado. |
| Sesión vencida | `O-003` → `V-001` | `401` | Retorno autorizado a esta ruta. |

## 5. Jerarquía y composición visual

```text
V-016 Detalle del pedido
├── Cabecera global autenticada
├── Migas / volver a Mis pedidos
├── Encabezado
│   ├── Código y fecha
│   ├── Estado actual
│   └── “Seguir envío”, condicional
├── Líneas históricas
│   └── Producto/SKU, descripción, cantidad y precio histórico
├── Desglose histórico
│   └── Subtotal, descuentos, envío y total
├── Entrega resumida
├── Historial de estados
└── Acción “Agregar productos al carrito”
```

| Región | Componente o contenido | Prioridad | Comportamiento |
|---|---|---|---|
| Encabezado | Código, fecha y estado | Primaria | Snapshot de Ventas; estado con texto/icono/color. |
| Líneas | Datos históricos | Primaria | No reemplazar nombre/precio por catálogo vigente. |
| Desglose | Importes históricos | Primaria | Etiquetas y moneda; no se presenta como precio actual. |
| Entrega | Dirección/contacto minimizados | Secundaria | Sin documento, tarjeta ni datos completos innecesarios. |
| Timeline | Hitos y fechas | Primaria | Lista textual accesible además de representación visual. |
| Reordenado | Agregar productos al carrito | Secundaria | Revalida productos actuales y abre `O-008`; no crea orden. |

## 6. Contenido y acciones

| Elemento | Texto o dato | Acción | Condición de visibilidad |
|---|---|---|---|
| Código | `orderId` visible | Copiar | Siempre en detalle válido. |
| Estado | Estado publicado por Ventas | — | Siempre. |
| Línea | Descripción/SKU histórico, cantidad y unitario | — | Por línea. |
| Desglose | Subtotal, descuento, envío, total | — | Según snapshot. |
| Entrega | Dirección resumida | — | Si está autorizada. |
| Hito | Estado + fecha/hora | — | Historial no vacío. |
| Tracking | “Seguir envío” | Abrir `V-017` | Existe seguimiento consultable. |
| Reordenar | “Agregar productos al carrito” | Ejecutar F-031 una vez | Pedido elegible. |

No usar “Comprar de nuevo”: la acción sólo agrega al carrito, usa precio/stock actuales y no restaura dirección, cupón ni precio histórico.

## 7. Estados de la vista

| Estado | Disparador | Cambios visibles | Acción o recuperación | Frame requerido |
|---|---|---|---|---|
| Cargando | Consulta inicial | Skeleton de encabezado, líneas y desglose | Esperar | Sí |
| Detalle listo | Pedido propio disponible | Todas las regiones autorizadas | Revisar/seguir/reordenar | Sí |
| Sin tracking | Ventas no indica seguimiento | Acción “Seguir envío” omitida; resto intacto | — | Anotado en principal |
| Reordenando | POST F-031 | CTA ocupado y no repetible; detalle permanece | Esperar | Sí |
| Reordenado completo | Todas las líneas elegibles | `O-008` con agregadas | Ver carrito/cerrar | Se diseña en `O-008` |
| Reordenado parcial | Algunas líneas no elegibles/ajustadas | `O-008` separa agregadas, ajustadas y no disponibles | Ver carrito/cerrar | Se diseña en `O-008` |
| Ninguna línea agregada | Todas no elegibles | `O-008` explica sin afirmar cambio del carrito | Cerrar/explorar | Se diseña en `O-008` |
| Conflicto de carrito | `409 CART_CONFLICT` | Detalle permanece; mensaje y recuperación | Actualizar/reintentar seguro | Sí |
| Comercio no disponible | `503` | No se altera historial ni afirma adición | Reintentar | Sí |
| Pedido no disponible | Ajeno/inexistente (`404` neutral) | Sin datos del pedido; estado neutral | Volver a `V-015` | Sí |
| Error de detalle | Fallo temporal de Ventas | No se muestran snapshots parciales como definitivos | Reintentar/volver | Sí |

## 8. Overlays y comunicaciones asociadas

| ID | Elemento | Cuándo aparece | Cómo se cierra o continúa |
|---|---|---|---|
| `O-003` | Autenticación requerida | Sesión ausente/vencida | Login y retorno tras autorizar propiedad. |
| `O-008` | Resultado de reordenado | F-031 finaliza total, parcial o sin agregados | Ver `V-008` o cerrar. |
| `O-009` | Evaluación postentrega | Pedido entregado y elegible según política | Enviar/ahora no/cerrar. |
| `O-010` | Alertas y feedback global | Copia de código o error recuperable | Confirmar/reintentar. |
| `C-001` | Correo de confirmación | Enlace autorizado hacia esta vista | Abre tras autenticación. |

## 9. Formularios y validación visual

No hay formularios de pedido. Reordenar no solicita cantidades, dirección, cupón o datos de pago; toma las líneas históricas y comunica los ajustes actuales.

| Control | Regla | Feedback |
|---|---|---|
| Copiar código | Copia sólo el código visible | Confirmación accesible. |
| Agregar productos al carrito | Una solicitud activa; no doble envío | Progreso y `O-008`. |

## 10. Responsive

### Desktop

- **Referencia:** 1440 px.
- Líneas y contenido principal a la izquierda; estado/desglose/entrega pueden usar columna lateral.
- Timeline horizontal sólo si mantiene fechas y textos legibles; la representación textual siempre está disponible.

### Mobile

- **Referencia:** 390 px.
- Orden: código/estado, líneas, desglose, entrega, timeline y acciones.
- Cada línea es bloque legible; no usar tabla comprimida.
- Timeline vertical con estado y fecha explícitos.
- Reordenar no queda fijo si tapa contenido o avisos.

### Anchuras intermedias

- El desglose pasa debajo de las líneas cuando la columna lateral pierde ancho.
- Timeline cambia a vertical antes de truncar hitos.

## 11. Accesibilidad

- Código, estado y fecha tienen etiquetas comprensibles; copiar confirma resultado.
- Líneas se presentan como lista con encabezado por producto y precios históricos correctamente nombrados.
- Timeline es lista ordenada con estado y fecha; la línea/gráfico es decorativo.
- Badges no dependen sólo del color.
- Reordenar anuncia progreso y resultado total/parcial sin mover foco antes de abrir `O-008`.
- El detalle ajeno/inexistente usa el mismo estado neutral para no enumerar pedidos.
- Información sensible se omite o enmascara también para lectores de pantalla.

## 12. Frames requeridos en Figma

| Frame | Plataforma | Estado | Contenido diferencial |
|---|---|---|---|
| `V-016 / Desktop / Detalle listo` | Desktop | Principal | Dos columnas y timeline. |
| `V-016 / Mobile / Detalle listo` | Mobile | Principal | Bloques y timeline vertical. |
| `V-016 / Desktop / Sin tracking` | Desktop | Variante | Acción omitida. |
| `V-016 / Mobile / Reordenando` | Mobile | Progreso | CTA ocupado. |
| `V-016 / Desktop / Conflicto carrito` | Desktop | Error transaccional | Reintento seguro. |
| `V-016 / Mobile / Comercio no disponible` | Mobile | Error recuperable | Sin alteración de detalle. |
| `V-016 / Desktop / Pedido no disponible` | Desktop | No disponible | Estado neutral. |
| `V-016 / Mobile / Error detalle` | Mobile | Error | Reintentar/volver. |

Los resultados de reordenado se diseñan en `O-008`.

## 13. Criterios de aceptación visual

- [ ] `UI-V016-001`: El detalle sólo se muestra al propietario; ajeno/inexistente usa un estado neutral común.
- [ ] `UI-V016-002`: Líneas e importes son snapshots históricos y no se sustituyen silenciosamente por catálogo/precio actual.
- [ ] `UI-V016-003`: Documento, tarjeta y dirección/contacto completos no aparecen.
- [ ] `UI-V016-004`: Timeline comunica estado y fecha en texto, no sólo mediante una línea gráfica.
- [ ] `UI-V016-005`: “Seguir envío” sólo aparece cuando existe tracking.
- [ ] `UI-V016-006`: La acción se denomina “Agregar productos al carrito” y explica que usa disponibilidad/precios actuales.
- [ ] `UI-V016-007`: Reordenado parcial diferencia agregados, ajustados y no disponibles; no afirma compra ni reserva.
- [ ] Desktop y mobile aplican `DS-001` y mantienen lectura/foco accesibles.

## 14. Decisiones y pendientes

| ID | Pregunta o decisión | Responsable | Fecha límite | Estado |
|---|---|---|---|---|
| `V-016-OPEN-01` | Resolver `I-03` para autorización del detalle propio en Ventas. | Ventas + Arquitectura | Antes de implementación; informar diseño | Abierta |
| `V-016-OPEN-02` | Publicar estados/hitos y datos mínimos de entrega devueltos por Ventas. | Ventas + Producto | Antes del diseño final | Abierta |
| `V-016-OPEN-03` | Definir garantía técnica de reintento de reordenado sin duplicar cantidades por SKU. | Backend | Antes del diseño final | Abierta |
| `V-016-OPEN-04` | Confirmar elegibilidad y punto de activación de `O-009` para pedidos entregados. | Producto + UX | Antes del diseño final | Abierta |
