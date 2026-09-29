# Reglas de integridad

## Responsabilidades por capa

| Regla | PostgreSQL | Aplicación o integración |
| --- | --- | --- |
| Tipos, nulabilidad y estados permitidos | Sí | — |
| Un carrito activo por propietario | Sí, índices parciales | Resolver conflictos y reintentar. |
| Propietario autenticado XOR anónimo | Sí, `CHECK` | Obtener identidad segura. |
| Fusión hacia carrito autenticado activo | Sí, trigger | Revalidar líneas y comunicar ajustes. |
| Un SKU por carrito | Sí, `UNIQUE` | Sumar cantidades transaccionalmente. |
| Carrito activo para mutar líneas | Sí, trigger | Autorizar al titular. |
| Incremento de `carts.version` | No automático | Debe ocurrir en la misma transacción que las líneas. |
| Precio y stock vigentes | No | Consultar Productos y Ofertas. |
| Pedido, entrega o cliente existentes | No | Consultar al módulo dueño. |
| Cifrado del correo | No | Cifrar antes del `INSERT`; gestionar claves fuera de la BD. |
| Retención y purga | No | Definir política y job operativo. |

## Carritos

### Propietario

Todo registro conserva exactamente uno de estos campos:

- `customer_id` para un carrito autenticado;
- `anonymous_session_hash` para un carrito anónimo.

Los índices parciales permiten como máximo un carrito `ACTIVE` por cliente y uno por hash de sesión. Los carritos históricos no ocupan esa unicidad.

### Estados

| Estado | Significado | Condiciones físicas |
| --- | --- | --- |
| `ACTIVE` | Acepta mutaciones. | No tiene destino de fusión ni fecha de checkout. |
| `MERGED` | Sus líneas fueron absorbidas. | Es anónimo, tiene `merged_into_cart_id` y `merged_at`. |
| `CHECKED_OUT` | Se completó la compra. | Tiene `checked_out_at`. |
| `ABANDONED` | Ya no se utilizará. | No tiene campos de fusión ni checkout. |

El trigger `carts_validate_merge_target` bloquea la fusión si el destino no es un carrito autenticado y `ACTIVE`. Usa un bloqueo de fila para serializar la validación con cambios concurrentes del destino.

Un carrito no puede fusionarse consigo mismo. Además, sólo un carrito anónimo puede adoptar el estado `MERGED`.

### Concurrencia optimista

La base inicializa `version` en cero y exige un valor no negativo, pero no lo incrementa automáticamente. Una mutación debe seguir este patrón dentro de una sola transacción:

1. Actualizar el carrito con `WHERE id = :cart_id AND version = :expected_version AND state = 'ACTIVE'`.
2. Incrementar `version = version + 1` y comprobar que se afectó exactamente una fila.
3. Insertar, actualizar o eliminar las líneas.
4. Confirmar la transacción.

Si el primer paso no afecta una fila, la aplicación debe releer el carrito y aplicar la regla funcional correspondiente.

## Líneas de carrito

- `cart_id + sku` es único.
- `quantity` acepta valores entre 1 y 99.
- El precio debe ser no negativo y no puede ser `NaN`.
- El snapshot de precio se guarda completo o se deja completo en `NULL`.
- `cart_id` no puede cambiar después de crear la línea.
- El trigger `cart_items_validate_active_cart` rechaza inserciones, actualizaciones y eliminaciones cuando el carrito no está `ACTIVE`.
- La FK usa `ON DELETE CASCADE`; cualquier estrategia de borrado también debe respetar el trigger de mutabilidad y la política de retención.

## Favoritos

- `customer_id + product_id` es único.
- Ambos identificadores son obligatorios.
- `customer_id` y `product_id` son referencias externas, no FK.
- Al mover un favorito al carrito, la aplicación elimina el favorito sólo después de confirmar la mutación del carrito.

## Checkout e idempotencia

La combinación `customer_id + idempotency_key` identifica una operación. `request_fingerprint` debe ser un SHA-256 hexadecimal de 64 caracteres.

| Estado | `external_order_id` | `failure_code` | `completed_at` |
| --- | --- | --- | --- |
| `PREPARING` | `NULL` | `NULL` | `NULL` |
| `PREPARED` | `NULL` | `NULL` | `NULL` |
| `SUBMITTED` | `NULL` | `NULL` | `NULL` |
| `SUCCEEDED` | Obligatorio | `NULL` | Obligatorio |
| `FAILED` | `NULL` | Obligatorio | Obligatorio |

La misma clave y fingerprint deben devolver el resultado persistido. La misma clave con otro fingerprint debe rechazarse. Hasta cerrar `I-02`, la protección local no garantiza por sí sola idempotencia en Ventas.

## Invitación postentrega

La unicidad `customer_id + external_order_id` impide más de una invitación lógica por pedido y cliente.

- `ELIGIBLE` no posee timestamps de interacción.
- `SHOWN` requiere `shown_at`.
- `DISMISSED` requiere `shown_at` y `dismissed_at`.
- `SUBMITTED` requiere `shown_at` y `submitted_at`; puede conservar un descarte anterior.
- `delivery_confirmed_at <= eligible_at <= shown_at` cuando esas fechas existen.

PostgreSQL no comprueba que el pedido esté entregado: la aplicación debe consultarlo antes de crear el registro. `SUBMITTED` se establece sólo después de éxito o conflicto de CSAT ya registrado.

## Notificaciones

- `type + event_key` es único.
- `recipient_email_encrypted` debe contener al menos un byte cifrado.
- `attempt_count = 0` implica `last_attempt_at IS NULL`.
- Un intento positivo requiere `last_attempt_at`.
- `FAILED` requiere al menos un intento.
- `SENT` requiere intento, `last_attempt_at` y `sent_at` coherentes.
- El worker debe reclamar y actualizar entregas de forma transaccional para evitar envíos concurrentes.

El esquema no define duración de retención. La política debe considerar borrado del correo cifrado, rotación de claves y necesidad de auditoría.

## Auditoría temporal

`set_updated_at()` asigna `statement_timestamp()` antes de cada actualización de `carts` y `cart_items`. Los constraints también impiden que fechas de fusión, checkout, finalización, intento o envío sean anteriores a la creación correspondiente.

Los timestamps registran hechos técnicos, no sustituyen el historial del pedido ni del despacho.

## Cadenas de texto

Los identificadores textuales, hashes, claves y códigos obligatorios no pueden quedar vacíos después de aplicar `btrim`. La misma regla se aplica a campos opcionales cuando contienen un valor. La aplicación debe normalizar entradas antes de persistirlas y no depender del constraint como validación de interfaz.
