# Diccionario de datos

Este diccionario describe el esquema implementado en [`04-esquema-inicial-postgresql.sql`](../04-esquema-inicial-postgresql.sql). `PK`, `FK` y `UK` indican clave primaria, clave foránea local y unicidad, respectivamente.

## Enums

| Tipo | Valores |
| --- | --- |
| `cart_state` | `ACTIVE`, `MERGED`, `CHECKED_OUT`, `ABANDONED` |
| `checkout_operation_state` | `PREPARING`, `PREPARED`, `SUBMITTED`, `SUCCEEDED`, `FAILED` |
| `post_delivery_prompt_state` | `ELIGIBLE`, `SHOWN`, `DISMISSED`, `SUBMITTED` |
| `notification_delivery_type` | `ORDER_CONFIRMATION`, `SHIPMENT_UPDATE` |
| `notification_delivery_state` | `PENDING`, `SENT`, `FAILED`, `SUPPRESSED` |

## `carts`

Representa un carrito durante todo su ciclo de vida.

| Columna | Tipo | Nulo | Default | Clave | Descripción |
| --- | --- | --- | --- | --- | --- |
| `id` | `uuid` | No | `gen_random_uuid()` | PK | Identificador local. |
| `customer_id` | `uuid` | Sí | — | Externa | Cliente de Seguridad y Usuarios. |
| `anonymous_session_hash` | `varchar(128)` | Sí | — | — | Hash del secreto de cookie; nunca el secreto en claro. |
| `state` | `cart_state` | No | `ACTIVE` | — | Estado del carrito. |
| `merged_into_cart_id` | `uuid` | Sí | — | FK → `carts.id` | Carrito autenticado que recibió una fusión. |
| `currency` | `char(3)` | No | `PEN` | — | Moneda; inicialmente sólo acepta PEN. |
| `version` | `integer` | No | `0` | — | Control de concurrencia optimista. |
| `created_at` | `timestamptz` | No | `CURRENT_TIMESTAMP` | — | Creación. |
| `updated_at` | `timestamptz` | No | `CURRENT_TIMESTAMP` | — | Última actualización mediante trigger. |
| `merged_at` | `timestamptz` | Sí | — | — | Momento de fusión. |
| `checked_out_at` | `timestamptz` | Sí | — | — | Momento de checkout exitoso. |

Índices:

| Índice | Tipo | Propósito |
| --- | --- | --- |
| `carts_one_active_per_customer_uidx` | Único parcial | Un carrito `ACTIVE` por cliente. |
| `carts_one_active_per_anonymous_session_uidx` | Único parcial | Un carrito `ACTIVE` por sesión anónima. |
| `carts_merged_into_cart_idx` | Parcial | Encontrar carritos fusionados hacia un destino. |

## `cart_items`

Representa una línea comprable. El SKU, no `variant_id`, identifica comercialmente la línea.

| Columna | Tipo | Nulo | Default | Clave | Descripción |
| --- | --- | --- | --- | --- | --- |
| `id` | `uuid` | No | `gen_random_uuid()` | PK | Identificador local. |
| `cart_id` | `uuid` | No | — | FK → `carts.id` | Carrito propietario; borrado en cascada. |
| `sku` | `varchar(100)` | No | — | UK con `cart_id` | Unidad comprable externa. |
| `product_id` | `varchar(100)` | Sí | — | Externa | Producto para navegación o presentación. |
| `variant_id` | `varchar(100)` | Sí | — | Externa | Variante para presentación. |
| `quantity` | `integer` | No | `1` | — | Cantidad entre 1 y 99. |
| `unit_price_snapshot` | `numeric(12,2)` | Sí | — | — | Precio informativo no autoritativo. |
| `price_version` | `varchar(100)` | Sí | — | Externa | Versión del precio consultado. |
| `quoted_at` | `timestamptz` | Sí | — | — | Momento del snapshot. |
| `created_at` | `timestamptz` | No | `CURRENT_TIMESTAMP` | — | Creación. |
| `updated_at` | `timestamptz` | No | `CURRENT_TIMESTAMP` | — | Última actualización mediante trigger. |

La terna `unit_price_snapshot`, `price_version` y `quoted_at` debe estar completa o completamente ausente.

Índices:

- Constraint único `cart_items_cart_sku_uk` sobre `cart_id + sku`.
- `cart_items_product_id_idx` para referencias por producto.
- `cart_items_variant_id_idx` para referencias por variante.

## `wishlist_items`

Representa un favorito a nivel de producto para un cliente autenticado.

| Columna | Tipo | Nulo | Default | Clave | Descripción |
| --- | --- | --- | --- | --- | --- |
| `id` | `uuid` | No | `gen_random_uuid()` | PK | Identificador local. |
| `customer_id` | `uuid` | No | — | Externa | Cliente de Seguridad y Usuarios. |
| `product_id` | `varchar(100)` | No | — | Externa | Producto de Productos y Ofertas. |
| `created_at` | `timestamptz` | No | `CURRENT_TIMESTAMP` | — | Momento de guardado. |

La combinación `customer_id + product_id` es única. El índice `wishlist_items_customer_created_idx` permite listar los favoritos más recientes de un cliente.

## `checkout_operations`

Representa una operación técnica de checkout, no un pedido ni un pago.

| Columna | Tipo | Nulo | Default | Clave | Descripción |
| --- | --- | --- | --- | --- | --- |
| `id` | `uuid` | No | `gen_random_uuid()` | PK | Identificador local. |
| `customer_id` | `uuid` | No | — | Externa | Cliente que confirma el checkout. |
| `cart_id` | `uuid` | No | — | FK → `carts.id` | Carrito de origen; borrado restringido. |
| `idempotency_key` | `varchar(255)` | No | — | UK con `customer_id` | Clave recibida para reintentar la operación. |
| `request_fingerprint` | `char(64)` | No | — | — | SHA-256 hexadecimal del contenido relevante. |
| `state` | `checkout_operation_state` | No | `PREPARING` | — | Estado técnico. |
| `external_order_id` | `varchar(100)` | Sí | — | Externa | Pedido devuelto por Ventas. |
| `failure_code` | `varchar(100)` | Sí | — | — | Código de diagnóstico no sensible. |
| `created_at` | `timestamptz` | No | `CURRENT_TIMESTAMP` | — | Inicio. |
| `completed_at` | `timestamptz` | Sí | — | — | Finalización exitosa o fallida. |

Índices adicionales:

- `checkout_operations_cart_created_idx` para historial por carrito.
- `checkout_operations_state_created_idx` para operaciones por estado.
- `checkout_operations_external_order_idx` para búsquedas por pedido externo.

## `post_delivery_prompts`

Conserva el estado UX de la invitación postentrega. No almacena puntuación, motivos ni comentario.

| Columna | Tipo | Nulo | Default | Clave | Descripción |
| --- | --- | --- | --- | --- | --- |
| `id` | `uuid` | No | `gen_random_uuid()` | PK | Identificador local. |
| `customer_id` | `uuid` | No | — | Externa | Cliente elegible. |
| `external_order_id` | `varchar(100)` | No | — | Externa | Pedido entregado. |
| `delivery_confirmed_at` | `timestamptz` | No | — | — | Instante externo usado para comprobar entrega. |
| `state` | `post_delivery_prompt_state` | No | `ELIGIBLE` | — | Estado de presentación. |
| `eligible_at` | `timestamptz` | No | `CURRENT_TIMESTAMP` | — | Momento en que Marketplace declaró elegibilidad. |
| `shown_at` | `timestamptz` | Sí | — | — | Primera presentación. |
| `dismissed_at` | `timestamptz` | Sí | — | — | Descarte de la invitación. |
| `submitted_at` | `timestamptz` | Sí | — | — | Confirmación de CSAT aceptado o ya existente. |

La combinación `customer_id + external_order_id` es única. El índice `post_delivery_prompts_customer_state_idx` soporta consulta por cliente y estado.

## `notification_deliveries`

Representa una salida idempotente de correo, no una copia del pedido.

| Columna | Tipo | Nulo | Default | Clave | Descripción |
| --- | --- | --- | --- | --- | --- |
| `id` | `uuid` | No | `gen_random_uuid()` | PK | Identificador local. |
| `external_order_id` | `varchar(100)` | No | — | Externa | Pedido relacionado. |
| `customer_id` | `uuid` | No | — | Externa | Titular del pedido. |
| `type` | `notification_delivery_type` | No | — | UK con `event_key` | Tipo de correo. |
| `event_key` | `varchar(255)` | No | — | UK con `type` | Identidad idempotente del evento. |
| `recipient_email_encrypted` | `bytea` | No | — | — | Sobre cifrado generado por la aplicación. |
| `payload_version` | `varchar(50)` | No | — | — | Versión de plantilla o payload. |
| `state` | `notification_delivery_state` | No | `PENDING` | — | Estado de entrega. |
| `provider_message_id` | `varchar(255)` | Sí | — | — | Identificador devuelto por el proveedor. |
| `attempt_count` | `integer` | No | `0` | — | Número de intentos. |
| `last_attempt_at` | `timestamptz` | Sí | — | — | Último intento. |
| `sent_at` | `timestamptz` | Sí | — | — | Envío exitoso. |
| `created_at` | `timestamptz` | No | `CURRENT_TIMESTAMP` | — | Creación de la salida. |

Índices adicionales:

- `notification_deliveries_state_created_idx`, parcial para `PENDING` y `FAILED`, soporta al worker.
- `notification_deliveries_order_idx` permite rastrear salidas por pedido.
