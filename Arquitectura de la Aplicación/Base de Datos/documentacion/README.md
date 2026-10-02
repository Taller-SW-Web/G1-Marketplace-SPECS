# Documentación técnica de la base de datos

Esta carpeta explica la persistencia local del Marketplace para quienes desarrollan, revisan u operan el servicio. La implementación vigente está en PostgreSQL 16 y contiene seis tablas locales.

> **Estado:** el SQL es una línea base física ejecutable para desarrollo y revisión. Su existencia no autoriza activar en producción checkout, evaluación postentrega ni notificaciones mientras sus contratos continúen bloqueados.

## Lectura recomendada

1. [Visión general](01-vision-general.md): alcance, ownership y decisiones principales.
2. [Diccionario de datos](02-diccionario-de-datos.md): enums, tablas, columnas e índices.
3. [Reglas de integridad](03-reglas-de-integridad.md): constraints, estados, concurrencia y triggers.
4. [Diagrama entidad-relación](04-diagrama-entidad-relacion.md): conceptos y cardinalidades del dominio.
5. [Diagrama lógico](05-diagrama-logico.md): límites entre persistencia local y módulos externos.
6. [Diagrama físico](06-diagrama-fisico.md): implementación exacta de tablas y relaciones locales.
7. [Guía operativa](07-guia-operativa.md): aplicación y verificación del esquema con `psql`.

## Fuentes de verdad

| Prioridad | Fuente | Responsabilidad |
| --- | --- | --- |
| 1 | [Modelo lógico inicial](../01-Modelo-logico-inicial.md) | Alcance funcional, entidades y propiedad de datos. |
| 2 | [Matriz de integración](../02-Matriz-de-integracion-y-contratos.md) | Identificadores, contratos y límites entre módulos. |
| 3 | [Decisiones y brechas](../03-Decisiones-y-brechas-de-integracion.md) | Acuerdos vigentes y dependencias pendientes. |
| 4 | [Esquema PostgreSQL](../04-esquema-inicial-postgresql.sql) | Tipos, tablas, constraints, índices, funciones y triggers implementados. |
| 5 | Esta carpeta | Explicación derivada para desarrollo y operación. |

Si esta documentación discrepa del SQL en un detalle físico, prevalece el SQL. Si el SQL contradice los límites de ownership, debe corregirse mediante una decisión arquitectónica y una migración revisada, no sólo editando esta documentación.

## Estado de integraciones

El esquema permite preparar las seis capacidades locales, pero no significa que todas sus integraciones estén habilitadas:

| Brecha | Área | Condición pendiente |
| --- | --- | --- |
| `I-02` | Checkout | Ventas debe homologar `Idempotency-Key`. |
| `I-04` | Evaluación postentrega | Ventas debe completar la validación y el contrato CSAT. |
| `I-05` | Notificaciones de despacho | Debe publicarse un evento o webhook consumible por Marketplace. |

Las tablas `checkout_operations`, `post_delivery_prompts` y `notification_deliveries` no sustituyen esos contratos externos.

## Convenciones

- Tablas y columnas físicas usan `snake_case`.
- Entidades y atributos lógicos se mencionan en `PascalCase` y `camelCase` cuando se citan los documentos originales.
- Los IDs internos y `customer_id` usan `uuid`.
- Los identificadores externos no homologados usan texto acotado.
- Una referencia externa no es una clave foránea.
- Todos los timestamps físicos usan `timestamptz`.
