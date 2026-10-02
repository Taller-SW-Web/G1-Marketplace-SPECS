# Visión general

## Propósito

La base de datos conserva únicamente el estado que pertenece al canal Marketplace. PostgreSQL no replica clientes, catálogo, inventario, precios autoritativos, pedidos, despachos ni respuestas CSAT completas.

La separación permite que cada módulo mantenga su propia fuente de verdad y evita relaciones SQL entre bases de datos de microservicios distintos.

## Tecnología y alcance

| Elemento | Decisión |
| --- | --- |
| Motor | PostgreSQL 16 |
| Esquema | El primero disponible en el `search_path`; la guía operativa usa `public` explícitamente |
| Script inicial | [`04-esquema-inicial-postgresql.sql`](../04-esquema-inicial-postgresql.sql) |
| Identificadores locales | UUID generados con `gen_random_uuid()` |
| Moneda inicial | `PEN` |
| Fechas | `timestamptz` |
| Integración entre módulos | API REST o contrato de eventos; nunca FK entre bases de datos |

## Entidades locales

| Entidad lógica | Tabla física | Responsabilidad |
| --- | --- | --- |
| `Cart` | `carts` | Ciclo de vida y propietario de un carrito anónimo o autenticado. |
| `CartItem` | `cart_items` | Línea comprable identificada por SKU y asociada a un carrito. |
| `WishlistItem` | `wishlist_items` | Producto guardado por un cliente autenticado. |
| `CheckoutOperation` | `checkout_operations` | Idempotencia y resultado técnico de una confirmación de checkout. |
| `PostDeliveryPrompt` | `post_delivery_prompts` | Estado local de presentación de la encuesta postentrega. |
| `NotificationDelivery` | `notification_deliveries` | Salida idempotente para un correo transaccional. |

## Datos externos referenciados

| Dato | Dueño | Uso local |
| --- | --- | --- |
| `customer_id` | Seguridad y Usuarios | Identifica al titular; no existe una tabla local de clientes. |
| `product_id`, `variant_id`, `sku` | Productos y Ofertas | Permiten navegar y validar una línea; SKU es la identidad comercial. |
| `external_order_id` | Ventas y Postventa | Vincula el resultado del checkout, la invitación CSAT y las notificaciones. |
| Entrega confirmada | Despacho o Ventas | Determina elegibilidad; sólo se conserva el instante comprobado. |

Estas columnas no tienen FK porque sus entidades viven y se validan en otros servicios.

## Datos excluidos

No deben crearse tablas locales para:

- usuarios, credenciales, roles, sesiones de acceso o tokens;
- direcciones guardadas;
- productos, variantes, stock, precios autoritativos o cupones;
- pedidos, pagos, líneas históricas o despachos;
- puntuaciones, motivos o comentarios CSAT;
- respuestas completas de proveedores externos.

Tampoco se almacenan números de tarjeta, CVV, tokens de pago ni el secreto en claro de una sesión anónima.

## Relaciones locales reales

- Un `cart` contiene cero o más `cart_items`.
- Un `cart` registra cero o más `checkout_operations`.
- Un carrito `MERGED` referencia al carrito autenticado que recibió sus líneas.
- `wishlist_items`, `post_delivery_prompts` y `notification_deliveries` no tienen FK locales hacia clientes, productos o pedidos.

## Principios para desarrollar

1. Validar identidad y ownership en la aplicación antes de consultar o mutar datos.
2. Usar transacciones para toda operación que cambie líneas y `carts.version`.
3. Revalidar precio y disponibilidad mediante Productos y Ofertas; el snapshot local no es autoritativo.
4. Usar la clave de idempotencia y el fingerprint para reintentos de checkout.
5. Cifrar el correo antes de escribir `recipient_email_encrypted` y nunca registrarlo en logs.
6. No activar integraciones bloqueadas hasta cerrar `I-02`, `I-04` e `I-05`.
