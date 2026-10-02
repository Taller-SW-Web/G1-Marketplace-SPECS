# Comunicación — C-001 Correo de confirmación de pedido

> Correo transaccional asíncrono que confirma un pedido ya creado. Su entrega no condiciona ni modifica el estado del pedido.

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID | `C-001` |
| Nombre | Correo de confirmación de pedido |
| Canal | Correo electrónico |
| Versión | `0.1.0` |
| Estado | En revisión |
| Responsable | Giuliano Macchiavello |
| Revisor | Jim Segovia |
| Sistema de diseño | [`DS-001`](../DS-001-sistema-diseno-marketplace.md) |
| Enlace de Figma | Pendiente |

## 2. Propósito y trazabilidad

- **Evento de envío:** pedido creado con `orderId` confirmado y entrega lógica `ORDER_CONFIRMATION` encolada.
- **Destinatario:** cliente propietario, obtenido por el flujo autorizado y almacenado cifrado para la entrega.
- **Funcionalidades:** `F-033` Generar plantilla y `F-034` Enviar confirmación asíncrona.
- **Specs de origen:** [`UI F-033`](../F-033-generar-plantilla-correo.md), [`UI F-034`](../F-034-enviar-confirmacion-asincrona.md) y [`V-014`](../vistas/V-014-pedido-confirmado.md).

La web no espera este correo. Un fallo temporal o definitivo de entrega no revierte ni degrada visualmente el pedido confirmado.

## 3. Jerarquía del contenido

| Orden | Bloque | Contenido | Datos dinámicos | Obligatorio |
|---:|---|---|---|---:|
| 1 | Preheader | Confirmación breve no repetida literalmente en el cuerpo | `orderId` opcional | Sí |
| 2 | Encabezado | Logo oficial + nombre Inka Athletics/Marketplace | Variante de logo aprobada | Sí |
| 3 | Estado principal | “Tu pedido fue creado” | `orderId`, estado público | Sí |
| 4 | Introducción | Agradecimiento y explicación de próximos pasos | Nombre sólo si está autorizado | Sí |
| 5 | Resumen | Código, fecha y total; líneas resumidas sólo si el payload las incluye | `orderId`, `createdAt`, `total`, `currency`, `items[]` opcional | Sí |
| 6 | Acción | “Ver mi pedido” | `orderDetailUrl` segura | Sí |
| 7 | Recomendados | Productos relacionados opcionales | `recommendations[]` | No |
| 8 | Ayuda | Qué hacer si no reconoce el pedido | URL/canal oficial de ayuda | Sí |
| 9 | Pie | Identidad, motivo del correo y datos legales aprobados | Versión de plantilla | Sí |

El correo no consulta ni incluye dirección completa, documento, tarjeta, contraseña, tokens, contacto interno, inventario o información de otros pedidos.

## 4. Copy y variables

| Elemento | Texto base propuesto | Variable | Fallback o restricción |
|---|---|---|---|
| Asunto | `Tu pedido {{orderId}} fue creado` | `orderId` | Obligatorio; no incluir total o PII. |
| Preheader | `Ya registramos tu pedido. Consulta aquí sus detalles.` | — | Debe complementar el asunto. |
| Título | `Tu pedido fue creado` | — | No usar “pago cobrado”. |
| Código | `Pedido {{orderId}}` | `orderId` | Visible y copiable como texto. |
| Estado | `Estado: {{orderStateLabel}}` | Estado público | Inicial esperado “Creado”; no mostrar enum técnico. |
| Fecha | `Fecha: {{createdAtLocalized}}` | `createdAt` | Zona `America/Lima` o política aprobada. |
| Total | `Total: {{formattedTotal}}` | Importe/moneda | Snapshot de Ventas, no cálculo del email. |
| Introducción | `Gracias por comprar con nosotros. Puedes revisar el estado y los detalles de tu pedido cuando quieras.` | — | No prometer entrega ni correo adicional. |
| CTA | `Ver mi pedido` | `orderDetailUrl` | Ruta interna con identificador opaco; exige autenticación. |
| Ayuda | `Si no reconoces este pedido, comunícate con nuestros canales oficiales de ayuda.` | `supportUrl` | No responder con datos sensibles. |

Variables permitidas preliminares:

| Variable | Tipo | Fuente | Regla |
|---|---|---|---|
| `orderId` | string | Evento/pedido confirmado | Obligatoria y opaca. |
| `orderStateLabel` | string | Mapeo aprobado de Ventas | Texto para cliente. |
| `createdAtLocalized` | string | `createdAt` | Formato localizado. |
| `formattedTotal` | string | Snapshot de Ventas | Incluye moneda; no se recalcula. |
| `items[]` | lista opcional | Snapshot autorizado | Nombre/variante/cantidad; sin datos internos. |
| `orderDetailUrl` | URL interna | Generador | HTTPS, sin token/PII; requiere sesión. |
| `recommendations[]` | lista opcional | Recomendaciones + Catálogo | Máximo a aprobar; sólo tarjetas completas. |

## 5. Estados y variantes

| Variante | Condición | Diferencia visible | Frame requerido |
|---|---|---|---|
| Principal | Pedido confirmado y datos mínimos | Estado, resumen y CTA | Sí |
| Sin imágenes remotas | Cliente bloquea recursos | Logo con texto alternativo/fallback, resumen y CTA siguen comprensibles | Sí |
| Sin recomendados | Fallo/lista vacía | Bloque completo omitido, sin título ni hueco | Sí |
| Con recomendados | 1–N tarjetas válidas | Bloque secundario después del CTA principal | Sí |
| Resumen extenso | Varias líneas autorizadas | Lista acotada y acción “Ver mi pedido”; no correo interminable | Sí, anotado |
| Texto plano | Cliente sin HTML | Mismo orden semántico, URL visible segura y sin decoración | Sí como contenido, no mockup visual separado |

No existe variante visible `PENDING/SENT/FAILED`; esos son estados internos de entrega.

## 6. Responsive, compatibilidad y accesibilidad

- Contenedor principal aproximado de 600 px en desktop y ancho fluido en mobile.
- Estructura de una columna; tablas de presentación sólo cuando sean necesarias para compatibilidad y con lectura semántica preservada.
- Fuentes web tienen fallback seguro; el mensaje no depende de Oswald/Inter cargadas remotamente.
- Logo tiene texto alternativo; imágenes de producto usan nombre útil; decoración usa alternativa vacía.
- Título, código, fecha, total y CTA permanecen como texto aunque no carguen imágenes.
- CTA usa texto descriptivo, contraste AA y tamaño táctil; debajo puede incluirse enlace seguro visible como fallback.
- Estado no depende sólo del color o icono.
- Orden de lectura: estado → resumen → CTA → recomendados → ayuda/pie.
- No usar scripts, vídeo, formularios, animaciones esenciales o CSS no compatible como única implementación.
- Existe parte `text/plain` semánticamente equivalente.

## 7. Frames requeridos

| Frame | Plataforma | Estado |
|---|---|---|
| `C-001 / Desktop / Principal` | Desktop 600 px | Pedido confirmado |
| `C-001 / Mobile / Principal` | Mobile 320–390 px | Pedido confirmado |
| `C-001 / Desktop / Con recomendados` | Desktop | Bloque opcional |
| `C-001 / Mobile / Sin imágenes` | Mobile | Fallback de recursos |

Figma debe anotar el contenido de texto plano y el comportamiento al omitir recomendados, aunque no requiera un frame decorado adicional.

## 8. Criterios de aceptación visual

- [ ] `UI-C001-001`: El correo sólo se genera para un pedido confirmado y muestra un único código verificable.
- [ ] `UI-C001-002`: El CTA usa una URL interna segura, sin token ni PII, y exige autenticación.
- [ ] `UI-C001-003`: Sin imágenes ni fuentes remotas, título, código, total y CTA siguen siendo comprensibles.
- [ ] `UI-C001-004`: El bloque de recomendados es opcional y se omite completo si falla.
- [ ] `UI-C001-005`: No incluye documento, dirección completa, tarjeta ni estado interno de notificación.
- [ ] `UI-C001-006`: El mensaje no afirma cobro real ni promete fecha de entrega no recibida.
- [ ] `UI-C001-007`: HTML y texto plano conservan el mismo significado y orden esencial.
- [ ] La pieza aplica `DS-001` adaptado a compatibilidad de correo.

## 9. Decisiones pendientes

| ID | Pregunta o decisión | Responsable | Estado |
|---|---|---|---|
| `C-001-OPEN-01` | Confirmar payload autorizado de líneas y límite de productos en el resumen. | Ventas + Producto | Abierta |
| `C-001-OPEN-02` | Aprobar URL/copy de ayuda y contenido legal del pie. | Producto | Abierta |
| `C-001-OPEN-03` | Definir máximo, fuente y etiquetado de recomendados opcionales. | Producto + Catálogo + UX | Abierta |
| `C-001-OPEN-04` | Seleccionar variante de logo optimizada para fondo claro y clientes de correo. | UX/UI | Abierta |
| `C-001-OPEN-05` | Confirmar proveedor, matriz de clientes soportados y pruebas de render. | Backend + QA | Abierta |
