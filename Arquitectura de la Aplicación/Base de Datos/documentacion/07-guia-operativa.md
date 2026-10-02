# Guía operativa

## Objetivo

Esta guía explica cómo aplicar y revisar el esquema inicial. No sustituye una herramienta de migraciones ni contiene credenciales.

## Requisitos

- PostgreSQL 16.
- Cliente `psql` compatible.
- Una base vacía destinada exclusivamente al Marketplace.
- Variable `PSQL_DATABASE_URL` compatible con libpq y configurada fuera del repositorio.
- Permisos para crear tipos, tablas, índices, funciones y triggers en el esquema objetivo.

Compruebe las versiones antes de continuar:

```bash
psql --version
psql "$PSQL_DATABASE_URL" -c "SELECT version();"
```

En PowerShell:

```powershell
psql --version
psql "$env:PSQL_DATABASE_URL" -c "SELECT version();"
```

`PSQL_DATABASE_URL` es distinta de una URL adaptada para Prisma. No use parámetros como `?schema=public` o `?ssl=true` con `psql`. Para TLS con libpq utilice el parámetro homologado por el ambiente, por ejemplo `sslmode=require`.

## Aplicación inicial

El script contiene `BEGIN` y `COMMIT`. Ante un error, PostgreSQL no debe dejar una instalación parcial.

Ejecute desde `Arquitectura de la Aplicación/Base de Datos`:

```bash
psql "$PSQL_DATABASE_URL" -v ON_ERROR_STOP=1 -c "SET search_path TO public;" -f "04-esquema-inicial-postgresql.sql"
```

En PowerShell:

```powershell
psql "$env:PSQL_DATABASE_URL" -v ON_ERROR_STOP=1 -c "SET search_path TO public;" -f "04-esquema-inicial-postgresql.sql"
```

El script no usa `IF NOT EXISTS`. Ejecutarlo de nuevo sobre el mismo esquema debe fallar, lo cual evita ocultar diferencias entre ambientes.

## Verificación

### Versión y tablas

```sql
SELECT current_database(), current_schema(), version();

SELECT table_name
FROM information_schema.tables
WHERE table_schema = current_schema()
  AND table_type = 'BASE TABLE'
ORDER BY table_name;
```

El resultado debe incluir:

- `carts`
- `cart_items`
- `wishlist_items`
- `checkout_operations`
- `post_delivery_prompts`
- `notification_deliveries`

### Enums

```sql
SELECT t.typname AS enum_type, e.enumlabel AS enum_value
FROM pg_type AS t
JOIN pg_enum AS e ON e.enumtypid = t.oid
JOIN pg_namespace AS n ON n.oid = t.typnamespace
WHERE n.nspname = current_schema()
ORDER BY t.typname, e.enumsortorder;
```

### Constraints

```sql
SELECT
  conrelid::regclass AS table_name,
  conname AS constraint_name,
  contype AS constraint_type
FROM pg_constraint
WHERE connamespace = current_schema()::regnamespace
ORDER BY conrelid::regclass::text, conname;
```

Tipos más relevantes: `p` para PK, `f` para FK, `u` para unicidad y `c` para `CHECK`.

### Índices

```sql
SELECT tablename, indexname, indexdef
FROM pg_indexes
WHERE schemaname = current_schema()
ORDER BY tablename, indexname;
```

Revise especialmente que los índices de carrito activo y los índices de worker conserven sus predicados parciales.

### Funciones y triggers

```sql
SELECT p.proname AS function_name
FROM pg_proc AS p
JOIN pg_namespace AS n ON n.oid = p.pronamespace
WHERE n.nspname = current_schema()
  AND p.proname IN (
    'set_updated_at',
    'validate_cart_merge_target',
    'validate_active_cart_item_mutation'
  )
ORDER BY p.proname;
```

```sql
SELECT
  event_object_table AS table_name,
  trigger_name,
  event_manipulation AS event
FROM information_schema.triggers
WHERE trigger_schema = current_schema()
ORDER BY event_object_table, trigger_name, event_manipulation;
```

## Comprobaciones funcionales mínimas

En un ambiente desechable o dentro de una transacción que termine en `ROLLBACK`, verifique:

1. No se pueden crear dos carritos `ACTIVE` para el mismo cliente.
2. No se pueden crear dos carritos `ACTIVE` para el mismo hash anónimo.
3. Un carrito no puede tener simultáneamente `customer_id` y `anonymous_session_hash`.
4. No se puede repetir `cart_id + sku`.
5. Una línea no puede mutarse después de fusionar o cerrar el carrito.
6. Una fusión sólo acepta como destino un carrito autenticado activo.
7. No se puede repetir `customer_id + idempotency_key`.
8. No se puede repetir `type + event_key` en notificaciones.
9. Los estados terminales exigen sus timestamps y resultados correspondientes.

No ejecute pruebas destructivas contra producción.

## Uso desde la aplicación

- Configure la conexión de la aplicación mediante `DATABASE_URL` y la operación manual mediante una URL libpq separada; no escriba credenciales en código, SQL o documentación.
- Use un pool con límites acordes al servicio y al plan de PostgreSQL administrado.
- Ejecute mutaciones de carrito dentro de transacciones cortas.
- Bloquee o actualice `carts.version` antes de modificar líneas.
- Trate una violación de unicidad parcial como conflicto concurrente recuperable.
- No registre `anonymous_session_hash`, `idempotency_key`, fingerprints ni correo cifrado innecesariamente.
- No descifre correos dentro de consultas SQL de negocio.

## Migraciones futuras

`04-esquema-inicial-postgresql.sql` es una instalación base. Después de desplegarlo:

1. No lo edite para cambiar ambientes existentes.
2. Cree una migración incremental nueva y versionada.
3. Documente compatibilidad hacia adelante y estrategia de rollback.
4. Pruebe la migración sobre una copia representativa.
5. Valide locks y duración para cambios de índices o tablas grandes.
6. Actualice el diccionario y el diagrama físico en el mismo cambio.

No existe un script automático de destrucción. Eliminar el esquema requiere una decisión explícita, respaldo previo y autorización del ambiente.

## Seguridad y retención

- `recipient_email_encrypted` debe ser un sobre cifrado versionado por la aplicación.
- Las claves de cifrado deben vivir en un gestor de secretos, nunca en PostgreSQL ni en Git.
- El secreto de sesión anónima nunca se persiste en claro.
- Defina antes de producción cuánto tiempo conservar operaciones fallidas, carritos abandonados y destinatarios cifrados.
- Las referencias externas no deben usarse para inferir acceso: toda consulta requiere validar identidad y ownership.

## Condiciones de activación

La creación de una tabla no habilita automáticamente su flujo:

- Checkout hacia Ventas requiere cerrar `I-02`.
- CSAT requiere cerrar `I-04`.
- Notificaciones de actualizaciones de despacho requieren cerrar `I-05`.

Consulte [Decisiones y brechas](../03-Decisiones-y-brechas-de-integracion.md) antes de desplegar consumidores de esas capacidades.
