# Comunicación — C-002 Correo de actualización de despacho

> Correo transaccional asíncrono que comunica un cambio de despacho aprobado para clientes y dirige al seguimiento autenticado.

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID | `C-002` |
| Nombre | Correo de actualización de despacho |
| Canal | Correo electrónico |
| Versión | `0.1.0` |
| Estado | En revisión |
| Responsable | Diego Espinoza |
| Revisor | Sebastián Malca |
| Sistema de diseño | [`DS-001`](../DS-001-sistema-diseno-marketplace.md) |
| Enlace de Figma | Pendiente |

## 2. Propósito y trazabilidad

- **Evento de envío:** cambio de estado de despacho relevante y homologado, identificado por `shipmentEventId`.
- **Destinatario:** cliente propietario del pedido, resuelto de forma autorizada.
- **Funcionalidades:** `F-033` Generar plantilla y `F-035` Enviar actualización de despacho.
- **Specs de origen:** [`UI F-033`](../F-033-generar-plantilla-correo.md), [`UI F-035`](../F-035-enviar-actualizacion-despacho.md) y [`V-017`](../vistas/V-017-seguimiento.md).

> [!WARNING]
> No se debe emitir este correo hasta resolver `I-05` y disponer de un origen autorizado de eventos. Marketplace no inventa ni infiere cambios de despacho.

## 3. Jerarquía del contenido

| Orden | Bloque | Contenido | Datos dinámicos | Obligatorio |
|---:|---|---|---|---:|
| 1 | Preheader | Cambio de estado resumido | `stateLabel` | Sí |
| 2 | Encabezado | Logo oficial + identidad Marketplace | Variante aprobada | Sí |
| 3 | Estado principal | “Tu pedido tiene una actualización” | `orderId`, `stateLabel` | Sí |
| 4 | Resumen del evento | Estado y momento ocurrido | `stateLabel`, `occurredAt` | Sí |
| 5 | Entrega estimada | Fecha vigente o reprogramada | `estimatedDelivery` | No; omitir si no existe |
| 6 | Incidencia | Explicación genérica publicable | `publicMessage` aprobado | No |
| 7 | Acción | “Ver seguimiento” | `trackingUrl` segura | Sí |
| 8 | Ayuda | Orientación/canales oficiales | `supportUrl` | Sí |
| 9 | Pie | Motivo transaccional y datos legales | Versión de plantilla | Sí |

No incluye ubicación precisa, coordenadas, ruta, nombre/teléfono del repartidor, almacén, contacto completo, documento ni datos de otros pedidos.

## 4. Copy y variables

| Elemento | Texto base propuesto | Variable | Fallback o restricción |
|---|---|---|---|
| Asunto | `Actualización de tu pedido {{orderId}}: {{stateLabel}}` | Pedido/estado | Estado público y breve. |
| Preheader | `Consulta el estado y la fecha estimada de tu entrega.` | — | Si no hay fecha, usar copy sin prometerla. |
| Título | `Tu pedido tiene una actualización` | — | No usar “ubicación en vivo”. |
| Pedido | `Pedido {{orderId}}` | `orderId` | Identificador opaco. |
| Estado | `Estado: {{stateLabel}}` | Estado público | Nunca enum técnico sin traducir. |
| Evento | `Actualizado el {{occurredAtLocalized}}` | `occurredAt` | Zona local aprobada. |
| Estimación | `Entrega estimada: {{estimatedDeliveryLocalized}}` | Fecha estimada | Omitir si no está disponible. |
| Reprogramación | `La fecha estimada de entrega cambió.` | Mensaje/fecha | Sólo evento autorizado. |
| CTA | `Ver seguimiento` | `trackingUrl` | Ruta interna HTTPS, sin token/PII; exige sesión. |
| Ayuda | `Consulta el seguimiento para ver la información más reciente.` | — | No invitar a responder con datos sensibles. |

Variables permitidas preliminares:

| Variable | Tipo | Fuente | Regla |
|---|---|---|---|
| `shipmentEventId` | string | Evento homologado | Sólo deduplicación; no necesita mostrarse. |
| `orderId` | string | Pedido autorizado | Obligatorio y opaco. |
| `stateLabel` | string | Mapeo aprobado de Despacho | Texto para cliente. |
| `occurredAtLocalized` | string | `occurredAt` | Fecha/hora localizada. |
| `estimatedDeliveryLocalized` | string opcional | Despacho | No inventar ni conservar fecha vencida. |
| `publicMessage` | string opcional | Catálogo aprobado de incidencias | Sanitizado y sin datos operativos. |
| `trackingUrl` | URL interna | Generador | Lleva a `V-017` y requiere autenticación. |

## 5. Estados y variantes

| Variante | Condición | Diferencia visible | Frame requerido |
|---|---|---|---|
| Cambio normal | Estado publicable | Estado, momento y CTA | Sí |
| Reprogramación/incidencia | Fecha cambió o existe mensaje público | Alerta contextual y nueva estimación | Sí |
| Entregado | Estado final | Confirmación de entrega y CTA de seguimiento/detalle | Sí |
| Sin fecha estimada | Estado válido sin `estimatedDelivery` | Bloque de fecha omitido; no muestra “por definir” salvo copy aprobado | Sí, anotado |
| Sin imágenes remotas | Cliente bloquea recursos | Identidad textual, estado y CTA siguen comprensibles | Sí |
| Texto plano | Cliente sin HTML | Mismo estado, fecha/mensaje y URL segura | Sí como contenido |

Estados internos `PENDING/SENT/FAILED` y reintentos del proveedor no aparecen dentro del correo.

## 6. Responsive, compatibilidad y accesibilidad

- Contenedor principal aproximado de 600 px y una sola columna adaptable a mobile.
- Fuentes del sistema como fallback; logo con texto alternativo y marca textual.
- Estado, fecha e incidencia se expresan como texto; color/icono son complementarios.
- CTA “Ver seguimiento” conserva contraste AA, área táctil y alternativa de URL visible segura.
- Sin imágenes, la comunicación mantiene asunto, estado, estimación y enlace.
- No usar mapa, scripts, seguimiento embebido, vídeo, animaciones esenciales o formularios.
- Orden de lectura: estado → momento/estimación → incidencia → CTA → ayuda/pie.
- Existe parte `text/plain` semánticamente equivalente.
- Compatibilidad y dark mode deben probarse con la matriz aprobada; nunca invertir colores de marca de modo que pierdan contraste.

## 7. Frames requeridos

| Frame | Plataforma | Estado |
|---|---|---|
| `C-002 / Desktop / Cambio normal` | Desktop 600 px | Estado publicable |
| `C-002 / Mobile / Cambio normal` | Mobile 320–390 px | Estado publicable |
| `C-002 / Desktop / Reprogramación` | Desktop | Incidencia y nueva fecha |
| `C-002 / Mobile / Entregado` | Mobile | Estado final |
| `C-002 / Mobile / Sin imágenes` | Mobile | Fallback de recursos |

Figma debe anotar la variante sin fecha y el contenido de texto plano aunque no requieran un frame decorado adicional.

## 8. Criterios de aceptación visual

- [ ] `UI-C002-001`: Sólo se genera a partir de un evento homologado, relevante y deduplicado.
- [ ] `UI-C002-002`: Estado de entrega se comunica en texto y no depende del color.
- [ ] `UI-C002-003`: El CTA enlaza a `V-017` mediante URL interna sin token/PII y requiere autenticación.
- [ ] `UI-C002-004`: Sin fecha estimada, el bloque se omite y no se inventa una promesa.
- [ ] `UI-C002-005`: Reprogramación distingue fecha nueva e incidencia publicable sin exponer operación interna.
- [ ] `UI-C002-006`: No contiene mapa, coordenadas, ubicación precisa ni datos del repartidor.
- [ ] `UI-C002-007`: Sin imágenes y en texto plano conserva estado, fecha disponible y CTA.
- [ ] La pieza aplica `DS-001` adaptado a compatibilidad de correo.

## 9. Decisiones pendientes

| ID | Pregunta o decisión | Responsable | Estado |
|---|---|---|---|
| `C-002-OPEN-01` | Resolver `I-05`: Ventas reexpone eventos, webhook de Despacho o sondeo autorizado. | Despacho + Ventas + Arquitectura | Abierta |
| `C-002-OPEN-02` | Publicar estados que generan correo y sus etiquetas/copy para cliente. | Despacho + Producto | Abierta |
| `C-002-OPEN-03` | Definir catálogo de incidencias publicables y tratamiento de reprogramaciones. | Despacho + UX | Abierta |
| `C-002-OPEN-04` | Aprobar ayuda, pie legal, logo y matriz de clientes de correo. | Producto + UX/UI + QA | Abierta |
